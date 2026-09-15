number = int(input('in_1: '))
r = 0
o = 0
k = 0
for i in range(number):
    k = k + 1
    name = input(f'in_{k}: ').split()
    if name[-1] == 'True':
        r = r + 1
    if name[-1] == 'False':
        o = o + 1
print(f'out: {r} {o}')