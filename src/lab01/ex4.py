minutes = int(input())
hours = minutes // 60
new_minutes = minutes - (hours * 60)
print(f"{hours}:{new_minutes:02d}")