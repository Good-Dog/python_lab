import argparse
from pathlib import Path
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))) 

from src.lib.text import normalize, tokenize, count_freq, top_n
def main():
    parser = argparse.ArgumentParser(description="Вывод файлов и анализ частот слов")
    subparsers = parser.add_subparsers(dest="command", required=True)
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла", description="Выводит файл построчно.")
    cat_parser.add_argument("--input", required=True, help="Путь к входному файлу")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")
    stats_parser = subparsers.add_parser("stats", help="Показать частоты слов", description="Выводит количество слов и наиболее частые слова.")
    stats_parser.add_argument("--input", required=True, help="Путь к текстовому файлу")
    stats_parser.add_argument("--top", type=int, default=5, help="Количество слов в топе (по умолчанию 5)")

    args = parser.parse_args()

    if args.command == "stats" and args.top <= 0:
        parser.error("--top должен быть положительным числом")

    path = Path(args.input)

    if not path.is_file():
        raise FileNotFoundError(f"Файл не найден: {path}")

    if args.command == "cat":
        with path.open(encoding="utf-8") as file:
            for number, line in enumerate(file, start=1):
                if args.n:
                    print(f"{number}: ", end="")
                print(line, end="")
    elif args.command == "stats":
        with path.open(encoding="utf-8") as f:
            text = f.read()

        norm = normalize(text)
        token = tokenize(norm)
        cnt_freq = count_freq(token)
        top = top_n(cnt_freq, n=args.top)
        print(f"Всего слов: {len(token)}")
        print(f"Уникальных слов: {len(cnt_freq)}")
        print(f"Топ-{args.top}:")
        for word, count in top:
            print(f"{word}: {count}")

if __name__ == "__main__":
    main()