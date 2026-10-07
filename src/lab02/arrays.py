def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums) == 0:
        return "ValueError"
    minn = nums[0]
    maxx = nums[0]
    for num in nums:
        if num < minn:
            minn = num
        if num > maxx:
            maxx = num
    return minn, maxx

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    l = []
    for num in nums:
        if num not in l:
            l.append(num)
    for i in range(len(l)):
        for j in range(0, len(l) - i - 1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l

def flatten(mat: list[list | tuple]) -> list:
    res = []
    for i in mat:
        if not isinstance(i, (list, tuple)):
            return 'TypeError'

        for j in i:
            res.append(j)
    return res
print('min_max')
print('[3, -1, 5, 5, 0] ->', min_max([3, -1, 5, 5, 0]))
print('[42] ->', min_max([42]))
print('[-5, -2, -9] ->', min_max([-5, -2, -9]))
print('[] ->', min_max([]))
print('[1.5, 2, 2.0, -3.1] ->', min_max([1.5, 2, 2.0, -3.1]))
print('')
print('unique_sorted')
print('[3, 1, 2, 1, 3] ->', unique_sorted([3, 1, 2, 1, 3]))
print('[] ->', unique_sorted([]))
print('[-1, -1, 0, 2, 2] ->', unique_sorted([-1, -1, 0, 2, 2]))
print('[1.0, 1, 2.5, 2.5, 0] ->', unique_sorted([1.0, 1, 2.5, 2.5, 0]))
print('')
print('flatten')
print('[[1, 2], [3, 4]] ->', flatten([[1, 2], [3, 4]]))
print('[[1, 2], (3, 4, 5)] ->', flatten([[1, 2], (3, 4, 5)]))
print('[[1], [], [2, 3]] ->', flatten([[1], [], [2, 3]]))
print('[[1, 2], "ab"] ->', flatten([[1, 2], "ab"]))
