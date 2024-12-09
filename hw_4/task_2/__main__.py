import os
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import math

def worker(f, a, step, start, end, num):
    print(f"Start worker {num}")
    acc = 0
    for i in range(start, end):
        acc += f(a + i * step) * step
    print(f"End worker {num}")
    return acc

def integrate(f, a, b, *, n_jobs=1, n_iter=10000000, exec):
    step = (b - a) / n_iter
    with exec(max_workers=n_jobs) as executor:
        futures = [executor.submit(worker, f, a, step, math.ceil(n_iter / n_jobs) * i, min(math.ceil(n_iter / n_jobs) * (i + 1), n_iter), i) for i in range(n_jobs)]
        return sum([future.result() for future in futures])

if __name__ == "__main__":
    with open("artifacts/2_results.txt", "w") as f:
        for cpu in range(1, os.cpu_count() * 2):
            print(f"Launch ThreadPoolExecutor {cpu}")
            start = time.perf_counter_ns()
            integrate(math.cos, 0, math.pi / 2, n_jobs=cpu, exec=ThreadPoolExecutor)
            end = time.perf_counter_ns()
            print(f"ThreadPoolExecutor {cpu}: {(end - start) / 10 ** 9}", file=f)

        for cpu in range(1, os.cpu_count() * 2):
            print(f"Launch ProcessPoolExecutor {cpu}")
            start = time.perf_counter_ns()
            integrate(math.cos, 0, math.pi / 2, n_jobs=cpu, exec=ProcessPoolExecutor)
            end = time.perf_counter_ns()
            print(f"ProcessPoolExecutor {cpu}: {(end - start) / 10 ** 9}", file=f)
    