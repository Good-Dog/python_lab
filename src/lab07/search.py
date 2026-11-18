def linear_search(nums, x) -> int:
    for numb, el in enumerate(nums):
        if el == x:
            return numb
    return -1

def binary_search(sorted_nums, x) -> int:
    low, high = 0, len(sorted_nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_nums[mid] == x:
            return mid
        elif x > sorted_nums[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def two_sum_brute(nums, target) -> tuple[int, int] | None:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None

def two_sum_fast(nums, target) -> tuple[int, int] | None:
    see = {}
    for i, num in enumerate(nums):
        comp = target - num
        if comp in see:
            return (see[comp], i)
        see[num] = i
    return None