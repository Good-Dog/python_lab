name = input()
ini = ''
a = name.split()
for i in a:
    if i[0].isupper():
        ini = ini + i[0] 
ini = ini + '.'
print(ini)
print(len('+'.join(a)))