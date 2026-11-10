import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.lib.text import normalize, tokenize, count_freq, top_n

def main():
    parser = argparse.ArgumentParser(description="CLI-утилиты для текста")
    subparsers = parser.add_subparsers(dest="command", required=True, help="Доступные команды")
    parser_cat = subparsers.add_parser("cat", help="Вывести содержимое файла")
    parser_cat.add_argument("--input", required=True, help="Путь к файлу")
    parser_cat.add_argument("-n", action="store_true", help="Нумеровать строки")
    parser_stats = subparsers.add_parser("stats", help="Анализ частот слов в тексте")
    parser_stats.add_argument("--input", required=True, help="Путь к файлу")
    parser_stats.add_argument("--top", type=int, default=5, help="Сколько топ-слов вывести (по умолчанию 5)")

    args = parser.parse_args()

    if args.command == "cat":
        try:
            with open(args.input, "r", encoding="utf-8") as f:
                if args.n:
                    for i, line in enumerate(f, start=1):
                        print(f"{i:4d} | {line}", end="")
                else:
                    print(f.read(), end="")
        except FileNotFoundError:
            parser.error(f"Файл не найден: {args.input}")

    elif args.command == "stats":
        try:
            with open(args.input, "r", encoding="utf-8") as f:
                text = f.read()
            norm = normalize(text)
            token = tokenize(norm)
            cnt_freq = count_freq(token)
            top = top_n(cnt_freq, n=args.top)
            print(f"Всего слов: {len(token)}")
            print(f"Уникальных слов: {len(cnt_freq)}")
            print(f"Топ-{args.top}:")
            for word, cnt in top:
                print(f"  {word}: {cnt}")

        except FileNotFoundError:
            parser.error(f"Файл не найден: {args.input}")

if __name__ == "__main__":
    main()