import multiprocessing as mp
import threading
import matrix

queue = mp.Queue()
is_working = mp.Event()


def generate(size):
    while is_working.is_set():
        queue.put(matrix.rand_matrix(size, size))


def parallel_calc():
    while is_working.is_set():
        if queue.qsize() > 1:
            m1 = queue.get()
            m2 = queue.get()
            matrix.parallel_calc(m1, m2)


def parallel():
    with mp.Pool() as pool:
        while is_working.is_set():
            m1 = queue.get()
            m2 = queue.get()
            n = matrix.SIZE
            args = [(m1, m2, (i, j)) for i in range(n) for j in range(n)]
            pool.starmap(matrix.parallel_multiply, args)
    pool.join()


def console():
    while is_working.is_set():
        cmd = input(">>> ")
        if cmd.lower() == "exit":
            is_working.clear()
            exit(-1)


if __name__ == '__main__':
    is_working.set()
    size = int(input("matrix size = "))
    threading.Thread(target=generate, args=(size,)).start()
    threading.Thread(target=parallel_calc).start()
    console()
