import numpy as np

class FileMixin:
    def save_to_file(self, filename: str) -> None:
        with open(filename, 'w') as file:
            file.write(str(self))

class StrMixin:
    def __str__(self) -> str:
        return str(self._data)
    
class GetterSetterMixin:
    @property
    def value(self):
        return self._data

    @value.setter
    def value(self, val):
        self._data = val

class Value(np.lib.mixins.NDArrayOperatorsMixin, FileMixin, StrMixin, GetterSetterMixin):
    def __init__(self, value):
        self._data = value 

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        inputs = [input._data if isinstance(input, Value) else input for input in inputs]
        result = ufunc(*inputs, **kwargs)
        return Value(result)


if __name__ == "__main__":
    a = Value(10)
    b = Value(6)
    (a+b).save_to_file("artifacts/3.2/val+.txt")
    (a*b).save_to_file("artifacts/3.2/val*.txt")
    (a**b).save_to_file("artifacts/3.2/val**.txt")
    a.value = a.value * a.value
    (a).save_to_file("artifacts/3.2/val_get_set.txt")
