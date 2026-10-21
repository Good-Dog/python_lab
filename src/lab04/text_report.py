import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.lib.text import normalize, tokenize, count_freq, top_n
from src.lab04.io_txt_csv import read_text, write_csv
text_input = "data/lab04/input.txt"

def text_report():
    try:
        text = read_text(text_input, encoding="utf-8")
    except FileNotFoundError:
        print("файл не найден")
        sys.exit(1)
    except UnicodeDecodeError:
        print("неверная кодировка")
        sys.exit(1)

    norm = normalize(text)
    token = tokenize(norm)
    cnt_freq = count_freq(token)
    top = top_n(cnt_freq)

    print(f'Всего слов: {len(token)}')
    print(f'Уникальных слов: {len(cnt_freq)}')
    print('Топ-5:')
    for i in top:
        print(f'{i[0]}: {i[1]}')
    
    top = sorted(cnt_freq.items(), key=lambda x: (-x[1], x[0]))
    write_csv(top, "data/lab04/report.csv", header=("word","count"))

if __name__ == "__main__":
    text_report()