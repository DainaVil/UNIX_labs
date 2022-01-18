import multiprocessing as mp
import random
import time

FILE = "matrix.txt"


def print_matrix(matrix):
    r = "\n" + "\n".join(["\t".join([str(cell) for cell in row]) for row in matrix])
    print(r)

def write_matrix(matrix, info):
    with open(FILE, mode="a", encoding="utf-8") as f:
        r = "\n" + "\n".join(["\t".join([str(cell) for cell in row]) for row in matrix])
        f.write("\n\n" + info + "\n" + r )


def rand_matrix(n, m):
    """Генерация матрицы заданного размера случайными чслами от 1 до 10"""

    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(random.randint(1, 10))
    return matrix

def multiply(i, j, A, B, q):
    """Простое перемножение элементов матрицы"""

    buffer = []
    
    for k in range(len(A[0]) or len(B)):
        buffer.append(A[i][k] * B[k][j])

    res = sum(buffer)
    pos = i,j
    q.put((res, pos))
   
def parallel_multiply(m1, m2, pos):
    """Перемножение элементов матрицы для непрерывных вычислений"""
    
    n = len(m1[0])
    i, j = pos
    res = sum([m1[i][k] * m2[k][j] for k in range(n)])

    return res, pos


def parallel_calc(m1, m2):
    
    n = len(m2[0])
    args = [(m1, m2, (i, j)) for i in range(n) for j in range(n)]
    
    with mp.Pool() as pool:
        res = pool.starmap(parallel_multiply, args)
    pool.join()
    
    write_matrix(m1, "matrix 1: ")
    write_matrix(m2, "matrix 2: ")

    res_matrix = []
    for i in range(n):
        res_matrix.append([])
        for j in range(n):
            res_matrix[i].append(res[i+j][0])
    write_matrix(res_matrix, "result: ")
    return res


def new_matrix():
    """Создание новых матриц"""
    
    n = int(input("lines = "))
    m = int(input("columns = "))

    m1 = rand_matrix(n, m)
    m2 = rand_matrix(m, n)
    return m1, m2

def main():

    manager = mp.Manager()
    m1, m2 = new_matrix()

    #вычисление размера итоговой матрицы
    res = [[0 for _ in range(len(m2[0]))] for _ in range(len(m2[0]))]

    print("\nmatrix 1: ")
    print_matrix(m1)
    print("\nmatrix 2: ")
    print_matrix(m2)

    proc = []
    q = manager.Queue()

    for i in range(len(res)):
        for j in range(len(res[i])):
            p = mp.Process(target=multiply, args=(i, j, m1, m2, q)) 
            proc.append(p)

    for p in proc:
        p.start()
    for p in proc:
        p.join()

    for i in range(len(res)):
        for j in range(len(res[i])):
            r = q.get()
            res[r[1][0]][r[1][1]] = r[0]
    
    print("\nresult: ")
    print_matrix(res)

if __name__ == "__main__":
    main()