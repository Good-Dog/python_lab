import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast


def check_sorting(fn, trials=100) -> None:
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        orig = list(nums)
        res = fn(nums)
        assert res == sorted(nums), f"{fn.__name__} ошиблась на {nums}: {res}"
        assert nums == orig, f"{fn.__name__} изменила исходный список"
    return trials

def check_search() -> int:
    trials = 100
    for _ in range(trials):
        nums = [random.randint(-50, 50) for _ in range(random.randint(0, 42))]
        target = random.randint(-60, 60)
        func_result = linear_search(nums, target)
        try:
            index_result = nums.index(target)
        except ValueError:
            index_result = -1
        assert func_result == index_result, f"linear_search ошибся при поиске {target} в {nums}"
        
        srt_nums = sorted(nums)
        bin_result = binary_search(srt_nums, target)
        try:
            index_result = srt_nums.index(target)
        except ValueError:
            index_result = -1
        assert bin_result == index_result, f"binary_search ошибся при поиске {target} в {srt_nums}"
    return trials

def check_two_sum(trials=100) -> None:
    for _ in range(trials):
        n = random.randint(2,30)
        nums = [random.randint(-50,50) for _ in range(n)]

        target = random.randint(-200, 200)
        expected = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    expected.append((i, j))

        res_brute = two_sum_brute(nums, target)
        res_fast = two_sum_fast(nums, target)
        if expected:
            assert res_brute in expected, f"Поиск индексов двумя циклами элементов, образующих сумму не выполнен верно: {nums}, {target}"
            assert res_fast in expected, f"Поиск индексов словарем элементов, образующих сумму не выполнен верно: {nums}, {target}"
        else:
            assert res_brute  is None
            assert res_fast is None
    return trials
        
if __name__ == "__main__":
    random.seed(42)
    total = 0
    for i in (bubble_sort, insertion_sort, selection_sort):
        total += check_sorting(i)
    total += check_search()
    total += check_two_sum()
    print(f"OK: {total} проверок")        