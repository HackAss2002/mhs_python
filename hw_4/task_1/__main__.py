import time
import threading
import multiprocessing

def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    prev = 0
    cur = 1
    for i in range(1, n):
        last_cur = cur
        cur = cur + prev
        prev = last_cur
    return cur

def measure(file: str, multi) -> None:
    multis = []
    for i in range(10):
        multis.append(multi(
            target=fibonacci,
            args=(200000,)
        ))
    start = time.perf_counter_ns()
    for m in multis:
        m.start()
    for m in multis:
        m.join()
    end = time.perf_counter_ns()
    with open(file, "w") as f:
        print((end - start) / 10 ** 9, file=f)

if __name__ == "__main__":
    measure("artifacts/1_thread.txt", threading.Thread)
    measure("artifacts/1_process.txt", multiprocessing.Process)
