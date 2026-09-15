name = input()
ini = ''
a = name.split()
for i in ''.join(a):
    if i.isupper():
        ini = ini + i
ini = ini + '.'
print(f'Инициалы: {ini}')
print(f'Длина: {len('+'.join(a))}')