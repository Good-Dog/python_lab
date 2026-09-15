number = int(input())
r = 0
o = 0
for i in range(number):
    name = input().split()
    if name[-1] == 'True':
        r = r + 1
    if name[-1] == 'False':
        o = o + 1
print(r, o)