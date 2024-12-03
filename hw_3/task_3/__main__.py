import numpy as np
from task_3.hashed_matrix import HashedMatrix
from task_1.matrix import Matrix

if __name__ == "__main__":
    def print_to_file(m: Matrix, filename: str) -> None:
        with open(filename, "w") as file:
            for y in range(m._height):
                print(" ".join([str(m._data[y * m._width + x]) for x in range(m._width)]), file=file)
    anp = np.array([[10, 20], [30, 40]])
    bnp = np.array([[50, 60], [70, 80]])
    cnp = np.array([[20, 10], [40, 30]])
    dnp = bnp

    a = HashedMatrix(data=anp)
    b = HashedMatrix(data=bnp)
    c = HashedMatrix(data=cnp)
    d = HashedMatrix(data=dnp)

    print_to_file(a, "artifacts/3.3/A.txt")
    print_to_file(b, "artifacts/3.3/B.txt")
    print_to_file(c, "artifacts/3.3/C.txt")
    print_to_file(d, "artifacts/3.3/D.txt")

    print_to_file(Matrix(data=anp) @ Matrix(data=bnp), "artifacts/3.3/AB.txt")
    print_to_file(Matrix(data=cnp) @ Matrix(data=dnp), "artifacts/3.3/CD.txt")

    assert hash(a) == hash(c)
    with open("artifacts/3.3/hash.txt", "w") as file:
        print(hash(a), file=file)
