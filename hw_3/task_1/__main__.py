from task_1.matrix import Matrix
import numpy as np
    
if __name__ == "__main__":
    def print_to_file(m: Matrix, filename: str) -> None:
        with open(filename, "w") as file:
            for y in range(m._height):
                print(" ".join([str(m._data[y * m._width + x]) for x in range(m._width)]), file=file)

    np.random.seed(0)
    anp = np.random.randint(0, 10, (10, 10))
    bnp = np.random.randint(0, 10, (10, 10))
    a = Matrix(data=anp)
    b = Matrix(data=bnp)
    print_to_file(a + b, "artifacts/3.1/matrix+.txt")
    print_to_file(a * b, "artifacts/3.1/matrix*.txt")
    print_to_file(a @ b, "artifacts/3.1/matrix@.txt")
