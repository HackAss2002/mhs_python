import copy
import struct
from task_1.matrix import Matrix

class HashMixin:
    def __hash__(self) -> int:
        res = 0
        for val in self._data:
            res ^= struct.unpack('!Q', struct.pack('!d', val))[0]
        return res
    
    
class HashedMatrix(Matrix, HashMixin):
    storage = {}

    def __matmul__(self, m: 'HashedMatrix') -> 'HashedMatrix':
        hash1 = hash(self)
        hash2 = hash(m)
        key = (hash1, hash2)
        if key not in HashedMatrix.storage:
            val = super().__matmul__(m)
            HashedMatrix.storage[key] = val
        return copy.deepcopy(HashedMatrix.storage[key])
