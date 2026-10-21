from pathlib import Path
import csv

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)
    # FileNotFoundError и UnicodeDecodeError пусть «всплывают» — это нормально
    return p.read_text(encoding=encoding)

def ensure_parent_dir(path: str | Path) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)

def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    if rows:
        normal = len(rows[0])
        for r in rows:
            if len(r) != normal:
                raise ValueError('Строки разной длины')
            
    ensure_parent_dir(path)

    with Path(path).open('w', newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header:
            w.writerow(header)
        for row in rows:
            w.writerow(row)

if __name__ == "__main__":
    txt = read_text("data/lab04/input.txt") # должен вернуть строку
    print(txt)
    write_csv([("word","count"),("test",3)], "data/lab04/check.csv")  # создаст CSV