import numpy as np

x = np.array([1, 2])
print (x.dtype) # int32

y = np.array([1, 2], dtype=np.int64)
print (y.dtype) # int64

z = np.array([1.0, 2.0])
print (z.dtype) # float64