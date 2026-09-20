import argparse
import re
from pathlib import Path
from typing import Any
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


def clean_html(html_text: str) -> str:
    """Очищает HTML-разметку, сохраняя структуру текста."""
    soup = BeautifulSoup(html_text, "html.parser")
    for br in soup.find_all("br"):
        br.replace_with("\n")
    text = soup.get_text(separator=" ")
    text = re.sub(r"\n\s*\n", "\n\n", text)
    return text.strip()


def generate_files(
        task_dir: Path,
        task_id: int,
        task_number: int,
        text: str,
        answer: str,
        files: list[dict[str, Any]],
) -> None:
    """Создает файлы README.md, .answer, solution.py и скачивает файлы внутри папки задачи."""
    (task_dir / "README.md").write_text(
        f"# Задача {task_id} (ЕГЭ №{task_number})\n\n{clean_html(text)}\n",
        encoding="utf-8",
    )
    (task_dir / ".answer").write_text(str(answer).strip(), encoding="utf-8")

    base_url = "https://kompege.ru"
    for file_info in files:
        file_url = file_info.get("url")
        if not file_url:
            continue
        file_name = file_url.split("/")[-1]
        try:
            res = requests.get(urljoin(base_url, file_url), timeout=10)
            res.raise_for_status()
            (task_dir / file_name).write_bytes(res.content)
        except (requests.RequestException, OSError) as e:
            print(f"  [!] Ошибка скачивания файла {file_name}: {e}")

    solution_template = (
        "def solve(*args, **kwargs):\n"
        '    """\n'
        "    Основная логика решения.\n"
        '    """\n'
        "    \n\n"
        'if __name__ == "__main__":\n'
        "    print(solve())\n"
    )
    (task_dir / "solution.py").write_text(solution_template, encoding="utf-8")


def main() -> None:
    parser_cli = argparse.ArgumentParser(description="Автоматический парсер задач с Kompege.ru")
    parser_cli.add_argument("-n", "--number", type=int, required=True, help="Номер задания ЕГЭ (например, 23)")
    parser_cli.add_argument("-c", "--count", type=int, default=5, help="Количество задач для добавления")
    args = parser_cli.parse_args()

    task_number = args.number
    target_count = args.count

    base_dir = Path.cwd() / "tasks" / "kege" / str(task_number)
    base_dir.mkdir(parents=True, exist_ok=True)

    url = f"https://kompege.ru/api/v1/task/number/{task_number}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        tasks_data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"[!] Ошибка подключения к API: {e}")
        return

    added_count = 0

    for task in tasks_data:
        if added_count >= target_count:
            break

        task_id = task.get("taskId")
        task_dir = base_dir / str(task_id)

        if task_dir.exists():
            continue

        task_dir.mkdir(exist_ok=True)
        try:
            generate_files(
                task_dir=task_dir,
                task_id=task_id,
                task_number=task_number,
                text=task.get("text", ""),
                answer=str(task.get("key", "")),
                files=task.get("files", []),
            )
            print(f"[+] Задача {task_id} успешно добавлена!")
            added_count += 1
        except OSError as e:
            print(f"[!] Ошибка при создании файлов для задачи {task_id}: {e}")

    print(f"\n[*] Импорт завершен. Добавлено новых задач: {added_count}")


if __name__ == "__main__":
    main()
