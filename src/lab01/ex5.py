name = input()
ini = ''
a = name.split()
for i in a:
    if i[0].isupper():
        ini = ini + i[0] 
ini = ini + '.'
print(f'Инициалы: {ini}')
print(f'Длина: {len('+'.join(a))}')