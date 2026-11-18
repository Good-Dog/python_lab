def bubble_sort(nums: list[int]) -> list[int]:   
    nums = list(nums)
    for i in range(len(nums)):
        flag = True
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                flag = False
        if flag:
            return nums
    return nums

def insertion_sort(nums: list[int]) -> list[int]:
    nums = list(nums)
    for index in range(1, len(nums)):
        el  = nums[index]
        border = index - 1
        while border >= 0 and nums[border] > el:
            nums[border + 1] = nums[border]
            border -= 1
        nums[border + 1] = el
    return nums
    
def selection_sort(nums: list[int]) -> list[int]:
    nums = list(nums)
    for index in range(len(nums)):
        min_el = index
        for el in range(index + 1, len(nums)):
            if nums[el] < nums[min_el]:
                min_el = el
        nums[index], nums[min_el] = nums[min_el], nums[index]
    return nums