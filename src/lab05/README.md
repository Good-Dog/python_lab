# ЛР5
## Задание 1: реализация функций json_to_csv и csv_to_json

### Функция `json_to_csv`

```python
def json_to_csv(json_path: str, csv_path: str) -> None:
    file = Path(json_path)

    if not file.exists():
        raise FileNotFoundError('Файл не существует')
    if file.suffix != '.json':
        raise ValueError('Файл должен быть .json')

    with open(file, encoding='utf-8') as f:
        data = json.load(f)

    if not data or type(data) is not list or not all(type(item) is dict for item in data):
        raise ValueError("Пустой или неверный JSON")

    colums = []
    for item in data:
        for key in item:
            if key not in colums:
                colums.append(key)

    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(colums)
        for item in data:
            values = []
            for i in colums:
                values.append(item.get(i, ''))
            writer.writerow(values)
```

Функция:

1. проверяет существование входного файла;
2. проверяет расширение `.json`;
3. читает JSON в кодировке UTF-8;
4. проверяет, что корневой объект является непустым списком словарей;
5. собирает названия всех ключей в порядке их первого появления;
6. записывает заголовок и строки в CSV в кодировке UTF-8.

Если в одном из словарей отсутствует ключ, `csv.DictWriter` записывает в
соответствующую ячейку пустое значение.


### Функция `csv_to_json`

```python
def csv_to_json(csv_path: str, json_path: str) -> None:
    file = Path(csv_path)

    if not file.exists():
        raise FileNotFoundError('Файл не существует')
    if file.suffix != '.csv':
         raise ValueError('Файл должен быть .csv')

    with open(file, encoding='utf-8', newline='') as f:
        i = csv.DictReader(f)
        data = list(i)
        if not i.fieldnames:
                raise ValueError('Пустой CSV или нет заголовка')

    if not data:
        raise ValueError('В CSV нет данных')

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
```

Функция:

1. проверяет существование входного файла;
2. проверяет расширение `.csv`;
3. читает CSV в кодировке UTF-8;
4. проверяет наличие заголовка и хотя бы одной строки данных;
5. преобразует каждую строку в словарь;
6. сохраняет список словарей в JSON с отступом в два пробела.


## Задание 2: реализация функции csv_to_xlsx


```python
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
```

Функция:

1. проверяет существование CSV-файла;
2. проверяет расширение `.csv`;
3. читает строки в кодировке UTF-8;
4. создаёт книгу Excel с помощью `openpyxl`;
5. добавляет строки CSV на лист `Sheet1`;
6. рассчитывает ширину столбцов;
7. сохраняет результат по указанному пути.


##ПРИМЕРЫ

json_to_csv

<img width="730" height="346" alt="people_from_json" src="https://github.com/user-attachments/assets/ddd73f6a-8c96-40df-8229-660306c2bdc5" />

csv_to_json

<img width="956" height="872" alt="people_from_csv" src="https://github.com/user-attachments/assets/948ba1de-3c35-4547-ba37-38e7e512e992" />

csv_to_xlsx

<img width="938" height="1218" alt="people_in_xlsx" src="https://github.com/user-attachments/assets/04013d2e-96eb-497c-8c31-d32db617a18d" />
