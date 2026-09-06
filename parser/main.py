import os
import argparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def clean_html(html_text: str) -> str:
    """Очищает HTML-разметку, сохраняя структуру текста."""
    soup = BeautifulSoup(html_text, "html.parser")
    for br in soup.find_all("br"):
        br.replace_with("\n")
    text = soup.get_text(separator=" ")
    import re
    # Убираем множественные пустые строки и пробелы
    text = re.sub(r'\n\s*\n', '\n\n', text)
    return text.strip()


def generate_files(task_dir: str, task_id: int, task_number: int, text: str, answer: str, files: list):
    """Создает файлы README.md, solution.py и test_solution.py внутри папки задачи."""
    
    # 1. README.md
    with open(os.path.join(task_dir, "README.md"), "w", encoding="utf-8") as f:
        f.write(f"# Задача {task_id} (ЕГЭ №{task_number})\n\n")
        f.write(clean_html(text) + "\n")

    with open(os.path.join(task_dir, ".answer"), "w", encoding="utf-8") as f:
        f.write(str(answer).strip())
        
    # 2. Скачивание приложенных файлов (если есть)
    base_url = "https://kompege.ru"
    for file_info in files:
        file_url = file_info.get("url")
        if file_url:
            file_name = file_url.split("/")[-1]
            try:
                full_url = urljoin(base_url, file_url)
                res = requests.get(full_url)
                with open(os.path.join(task_dir, file_name), "wb") as f:
                    f.write(res.content)
            except Exception as e:
                print(f"  [!] Ошибка скачивания файла {file_name}: {e}")

    # 3. solution.py
    solution_template = (
        "def solve(*args, **kwargs):\n"
        "    \"\"\"\n"
        "    Основная логика решения.\n"
        "    \"\"\"\n"
        "    pass\n\n\n"
        "if __name__ == \"__main__\":\n"
        "    print(solve())\n"
    )
    with open(os.path.join(task_dir, "solution.py"), "w", encoding="utf-8") as f:
        f.write(solution_template)


#     # 4. test_solution.py
#     test_template = f"""import pytest
# from solution import solve
#
# def test_main_answer():
#     \"\"\"
#     Проверка эталонного ответа с сайта Компегэ.
#     \"\"\"
#     expected = "{answer.strip()}"
#     # TODO: Передай в solve() необходимые аргументы (путь к файлу или стартовые значения)
#     result = str(solve())
#     assert result == expected, f"Ожидалось {{expected}}, но получено {{result}}"
#
# # TODO (для ИИ-Агента):
# # Проанализируй README.md и найди демонстрационный пример траектории/вычислений.
# # Напиши функцию test_example(), которая проверяет solve() на данных из примера.
# """
#     with open(os.path.join(task_dir, "test_solution.py"), "w", encoding="utf-8") as f:
#         f.write(test_template)


def main():
    # Настройка аргументов командной строки
    parser_cli = argparse.ArgumentParser(description="Автоматический парсер задач с Kompege.ru")
    parser_cli.add_argument("-n", "--number", type=int, required=True, help="Номер задания ЕГЭ (например, 23)")
    parser_cli.add_argument("-c", "--count", type=int, default=5, help="Количество задач для добавления")
    args = parser_cli.parse_args()

    task_number = args.number
    target_count = args.count

    base_dir = os.path.join(os.getcwd(), "tasks", "kege", str(task_number))
    os.makedirs(base_dir, exist_ok=True)

    print(f"[*] Поиск задач №{task_number} на Kompege. Цель: добавить {target_count} новых задач.")
    
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
        task_dir = os.path.join(base_dir, str(task_id))

        # Проверка на дубликат (существует ли папка)
        if os.path.exists(task_dir):
            print(f"[-] Задача {task_id} уже существует в базе, пропускаем...")
            continue

        # Создаем папку и генерируем файлы
        os.makedirs(task_dir)
        try:
            generate_files(
                task_dir=task_dir,
                task_id=task_id,
                task_number=task_number,
                text=task.get("text", ""),
                answer=str(task.get("key", "")),
                files=task.get("files", [])
            )
            print(f"[+] Задача {task_id} успешно добавлена!")
            added_count += 1
        except Exception as e:
            print(f"[!] Ошибка при создании файлов для задачи {task_id}: {e}")

    print(f"\n[*] Импорт завершен. Добавлено новых задач: {added_count}")


if __name__ == "__main__":
    main()