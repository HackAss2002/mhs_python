import multiprocessing
import time
import codecs
from datetime import datetime


def process_a(input_queue, output_queue):
    first_time = time.perf_counter()
    while True:
        message = input_queue.get()
        print(f"[{datetime.now()}] Process A received: {message}")
        if first_time is not None:
            time.sleep(max(0, 5 - (time.perf_counter() - time.perf_counter())))
        first_time = datetime.now()
        output_queue.put(message.lower())


def process_b(input_queue, output_queue):
    while True:
        message = input_queue.get()
        print(f"[{datetime.now()}] Process B received: {message}")
        rot_message = codecs.encode(message, "rot_13")
        print(rot_message)
        output_queue.put(rot_message)


if __name__ == "__main__":
    queue_to_a = multiprocessing.Queue()
    queue_to_b = multiprocessing.Queue()
    queue_to_main = multiprocessing.Queue()

    process_a_worker = multiprocessing.Process(target=process_a, args=(queue_to_a, queue_to_b))
    process_b_worker = multiprocessing.Process(target=process_b, args=(queue_to_b, queue_to_main))

    process_a_worker.start()
    process_b_worker.start()

    try:
        while True:
            user_input = input()
            queue_to_a.put(user_input)

    finally:
        process_a_worker.join()
        process_b_worker.join()