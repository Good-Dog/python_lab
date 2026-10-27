# ЛР4
## Задание A — модуль src/lab04/io_txt_csv.py
### read_text
Функция читает весь текст файла и возвращает одной строкой.

### ensure_parent_dir
Cоздает родительские директории, если их нет

### write_csv
Функция принимает список из строк таблицы, путь, где создаст csv, и заголовок таблицы; проверяет прямоугольность таблицы; перезаписывает строки в csv
  
## Задание B — скрипт src/lab04/text_report.py
### text_report
Функция читает текст из файла `src/data/lab04/input.txt`; с помощью функций `normalize, tokenize, count_freq, top_n` из ЛР3 обрабатывает текст и выводит в консоль количество всех слов, уникальных слов и топ-5; создает таблицу в csv с колонками `word,count` со всеми словами текста 

# ПРИМЕРЫ ЗАПУСКОВ
В обоих примерах input.txt содержит в себе строку "Привет, мир! Привет!!!"

### Задача A

<img width="390" height="146" alt="TEST_A_io_txt_csv_csv" src="https://github.com/user-attachments/assets/ecb1830e-2dd3-42a6-b7fb-738311034ef9" />
<img width="1894" height="144" alt="TEST_A_io_txt_csv" src="https://github.com/user-attachments/assets/9177cce5-15d7-4a9d-9780-2b953fa413f9" />

### Задача B

<img width="418" height="260" alt="TEST_A_text_report_csv" src="https://github.com/user-attachments/assets/2c9ff5ad-88a3-4144-ad26-585757f8ac09" />
<img width="1908" height="336" alt="TEST_A_text_report" src="https://github.com/user-attachments/assets/ac2d2d65-2582-42f3-8150-3a3187ee1c4e" />
