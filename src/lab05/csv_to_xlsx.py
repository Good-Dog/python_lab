from pathlib import Path
from openpyxl import Workbook
import csv


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    file = Path(csv_path)

    if not file.exists():
        raise FileNotFoundError('Файл не существует')
    if file.suffix != '.csv':
        raise ValueError('Файл не .csv')

    with open(file, encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    if not data:
        raise ValueError('Файл пустой')

    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    for item in data:
        ws.append(item)

    for i in ws.columns:
        mx_len = 0
        for j in i:
            if j.value is not None:
                new_len = len(str(j.value))
                if new_len > mx_len:
                    mx_len = new_len
        bukva = i[0].column_letter
        ws.column_dimensions[bukva].width = max(mx_len + 2, 8)

    wb.save(xlsx_path)

if __name__ == '__main__':
    csv_to_xlsx('data/lab05/samples/people.csv', 'data/lab05/out/people.xlsx')
    csv_to_xlsx('data/lab05/samples/cities.csv', 'data/lab05/out/cities.xlsx')