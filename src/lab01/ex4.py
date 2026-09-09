minutes = int(input())
howmuch = minutes // 60
seconds = minutes - (howmuch * 60)
print(f"{howmuch}:{seconds}")