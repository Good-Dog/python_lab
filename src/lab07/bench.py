import random
import timeit
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from src.lab04.io_txt_csv import write_csv
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast

def bench_sorts() -> list[tuple[str, int, str, str]]:
    random.seed(42)
    rows = []
    sizes = [1_000, 10_000, 100_000]
    for n in sizes:
        data = [random.randint(-1_000_000, 1_000_000) for _ in range(n)]
        time1 = timeit.timeit(lambda: sorted(data), number = 1)

        rows.append(("sorting", n, "sorted", f"{time1:.6f}"))
        func = [("bubble_sort", bubble_sort), ("insertion_sort", insertion_sort), ("selection_sort", selection_sort)]

        for name, j in func:
            if n <= 10_000:
                time2 = timeit.timeit(lambda: j(data), number = 1)
                rows.append(("sorting", n, name, f"{time2:.6f}"))
            else:
                rows.append(("sorting", n, name, ">60"))
    return rows

def bench_search() -> list[tuple[str, int, str, str]]:
    random.seed(42)
    rows = []
    data = [random.randint(-1_000_000, 1_000_000) for _ in range(100_000)]
    targets = [random.choice(data) for _ in range(10000)]

    time = timeit.timeit(lambda: [linear_search(data, t) for t in targets], number = 1)
    rows.append(("search", 100_000, "linear_search", f"{time:.6f}"))

    sorted_data = sorted(data)
    time = timeit.timeit(lambda: [binary_search(sorted_data, t) for t in targets], number = 1)
    rows.append(("search", 100_000, "binary_search", f"{time:.6f}"))

    for n in [1_000, 10_000]:
        data = [random.randint(-1_000_000, 1_000_000) for _ in range(n)]
        i, j = random.sample(data, 2)
        summ = i + j

        k = timeit.timeit(lambda: two_sum_brute(data, summ), number = 1)
        rows.append(("two_sum", n, "two_sum_brute", f"{k:.6f}"))
        k = timeit.timeit(lambda: two_sum_fast(data, summ), number = 1)
        rows.append(("two_sum", n, "two_sum_fast", f"{k:.6f}"))
    
    return rows

def main():
    header = ("Task", "Length", "Method", "Time")
    rows = []
    rows.extend(bench_sorts())
    rows.extend(bench_search())
    write_csv(rows, "data/lab_07/bench.csv", header)
    print(f"{'Task':<7}  {'Length':<6}  {'Method':<18}  {'Time'}")
    for task, leng, meth, time in rows:
        print(f"{task:<7}  {leng:<6}  {meth:<18}  {time}")

        
if __name__ == "__main__":
    main()

