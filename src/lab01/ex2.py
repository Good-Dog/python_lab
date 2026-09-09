a = input().replace(',', '.')
b = input().replace(',', '.')
print(a, b)
a, b = float(a), float(b)
summ = a + b
avg = (a + b) / 2
print(f'sum={summ:.2f}; avg={avg:.2f}')