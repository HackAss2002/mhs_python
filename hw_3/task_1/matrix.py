import numpy as np

class Matrix:
    def __init__(self, *, data: np.ndarray | None = None, height: int | None = None, width: int | None = None) -> None:
        self._data = []
        if data is not None:
            self._height = data.shape[0]
            self._width = data.shape[1]

            for y in range(data.shape[0]):
                for x in range(data.shape[1]):
                    self._data.append(data[y][x])
        elif height is not None and width is not None: 
            self._height = height
            self._width = width
            for _ in range(width * height):
                self._data.append(0)
        else:
            self._height = 0
            self._width = 0

    def __add__(self, m: 'Matrix') -> 'Matrix':
        if self._height != m._height or self._width != m._width:
            raise ValueError("Different matrices sizes")
        result = Matrix(height=self._height, width=self._width)
        for i in range(self._width * self._height):
            result._data[i] = self._data[i] + m._data[i]
        return result

    def __mul__(self, m: 'Matrix') -> 'Matrix':
        if self._height != m._height or self._width != m._width:
            raise ValueError("Different matrices sizes")
        result = Matrix(height=self._height, width=self._width)
        for i in range(self._width * self._height):
            result._data[i] = self._data[i] * m._data[i]
        return result

    def __matmul__(self, m: 'Matrix') -> 'Matrix':
        if self._width != m._height:
            raise ValueError("Incompatible matrices sizes")
        result = Matrix(height=self._height, width=m._width)
        for i in range(self._height):
            for k in range(self._width):
                for j in range(m._width):
                    result._data[i * result._width + j] += self._data[i * self._width + k] * m._data[k * m._width + j]
        return result
