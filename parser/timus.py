import argparse
import re
import time
from pathlib import Path
from typing import Any

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://acm.timus.ru/"

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Referer": "https://acm.timus.ru/problemset.aspx",
    "Upgrade-Insecure-Requests": "1",
})


def format_element_text(element: BeautifulSoup | None) -> str:
    """Форматирует блочный текст элемента в чистый Markdown."""
    if not element:
        return ""

    # Заменяем <br> на переносы
    for br in element.find_all("br"):
        br.replace_with("\n")

    text = element.get_text(separator=" ")
    # Нормализуем пробелы и пустые строки
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n\s*\n", "\n\n", text)
    return text.strip()


def parse_problem(task_id: int) -> dict[str, Any] | None:
    """Загружает и аккуратно структурирует страницу одной задачи."""
    url = f"https://acm.timus.ru/problem.aspx?space=1&num={task_id}&locale=ru"
    try:
        time.sleep(1)
        res = session.get(url, timeout=10)
        res.raise_for_status()
    except requests.RequestException as e:
        print(f"  [!] Ошибка сети при запросе задачи {task_id}: {e}")
        return None

    soup = BeautifulSoup(res.text, "html.parser")

    title_el = soup.find("h2", class_="problem_title")
    text_el = soup.find("div", id="problem_text")

    if not title_el or not text_el:
        print(f"  [-] Задача {task_id} не найдена.")
        return None

    # 1. Извлекаем ограничения
    limits_el = soup.find("div", class_="problem_limits")
    limits_text = format_element_text(limits_el)

    # 2. Извлекаем и сразу удаляем подтаблицу примеров и источник/замечания из основного HTML
    samples = []
    sample_table = text_el.find("table", class_="sample")
    if sample_table:
        rows = sample_table.find_all("tr")[1:]  # пропуск заголовка таблицы
        for row in rows:
            cols = row.find_all("td")
            if len(cols) >= 2:
                samples.append({
                    "input": cols[0].get_text().strip(),
                    "output": cols[1].get_text().strip(),
                })
        sample_table.decompose()

    # Извлекаем и форматируем подзаголовки h3 -> ## Subtitle
    for h3 in text_el.find_all("h3", class_="problem_subtitle"):
        sub_title = h3.get_text(strip=True)
        h3.replace_with(f"\n\n## {sub_title}\n\n")

    # Форматируем основной текст задачи
    body_text = format_element_text(text_el)

    return {
        "id": task_id,
        "title": title_el.get_text(strip=True),
        "limits": limits_text,
        "body": body_text,
        "samples": samples,
    }


def generate_files(task_dir: Path, problem_data: dict[str, Any]) -> None:
    """Создает структуру файлов для задачи Timus."""
    # 1. Форматирование красивого README.md
    readme_lines = [
        f"# {problem_data['title']}\n",
        f"**Ограничения:**\n{problem_data['limits']}\n" if problem_data["limits"] else "",
        problem_data["body"],
    ]

    if problem_data["samples"]:
        readme_lines.append("\n## Пример\n")
        for idx, sample in enumerate(problem_data["samples"], 1):
            readme_lines.append(f"**Пример {idx}**\n")
            readme_lines.append(f"```in\n{sample['input']}\n```")
            readme_lines.append(f"```out\n{sample['output']}\n```\n")

    (task_dir / "README.md").write_text("\n".join(readme_lines), encoding="utf-8")

    solution_template = (
        "import sys\n\n\n"
        "def solve() -> None:\n"
        "    input_data = sys.stdin.read().split()\n"
        "    if not input_data:\n"
        "        return\n"
        "    # TODO: Реализовать решение\n"
        "    pass\n\n\n"
        'if __name__ == "__main__":\n'
        "    solve()\n"
    )
    (task_dir / "solution.py").write_text(solution_template, encoding="utf-8")

    # 3. Файлы примеров для тестов
    for idx, sample in enumerate(problem_data["samples"], 1):
        (task_dir / f"sample_{idx}.in").write_text(sample["input"], encoding="utf-8")
        (task_dir / f"sample_{idx}.out").write_text(sample["output"], encoding="utf-8")


def main() -> None:
    parser_cli = argparse.ArgumentParser(description="Парсер задач с Timus Online Judge")
    parser_cli.add_argument("-s", "--start", type=int, default=1000, help="Начальный ID задачи (напр. 1000)")
    parser_cli.add_argument("-c", "--count", type=int, default=5, help="Количество задач для скачивания")
    args = parser_cli.parse_args()

    base_dir = Path(__file__).resolve().parent.parent / "tasks" / "timus"
    base_dir.mkdir(parents=True, exist_ok=True)

    added_count = 0
    current_id = args.start

    print(f"[*] Старт парсинга Timus начиная с ID {current_id}. Цель: {args.count} задач.")
    print(f"[*] Папка сохранения: {base_dir}")

    while added_count < args.count:
        task_dir = base_dir / str(current_id)

        if task_dir.exists():
            print(f"[-] Задача {current_id} уже существует, пропускаем...")
            current_id += 1
            continue

        print(f"[*] Загрузка задачи {current_id}...")
        problem_data = parse_problem(current_id)

        if problem_data:
            task_dir.mkdir(exist_ok=True)
            try:
                generate_files(task_dir, problem_data)
                print(f"[+] Задача {current_id} ({problem_data['title']}) успешно сохранена!")
                added_count += 1
            except OSError as e:
                print(f"[!] Ошибка записи файлов для задачи {current_id}: {e}")

        current_id += 1

    print(f"\n[*] Завершено. Успешно добавлено задач: {added_count}")


if __name__ == "__main__":
    main()