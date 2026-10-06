def format_record(rec: tuple[str, str, float]):

    fio, group, gpa = rec
    if len(group) == 0:
        raise TypeError('Неправильная группа')
    
    fio = fio.strip()
    words = fio.split()
    if len(words) < 2:
        raise TypeError("Неправильное ФИО")
    if not (0.0 <= gpa <= 5.0):
        raise ValueError("Неверное значение GPA")
        
    name = f"{words[0].capitalize()} " + "".join(f"{w[0].upper()}." for w in words[1:])
    return f"{name}, гр. {group}, GPA {gpa:.2f}"
print('("Иванов Иван Иванович", "BIVT-25", 4.6) ->', format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print('("Петров Пётр", "IKBO-12", 5.0) ->', format_record(("Петров Пётр", "IKBO-12", 5.0)))
print('("Петров Пётр Петрович", "IKBO-12", 5.0) ->', format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print('("  сидорова  анна   сергеевна ", "ABB-01", 3.999) ->', format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))