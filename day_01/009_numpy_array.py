import numpy as np

a = np.array([1, 2, 3])
print(type(a)) # <class 'numpy.ndarray'>

print (np.shape(a)) # (3,)
print (a[0]) # 1

a[0] = 5
print (a) # [5 2 3]

b = np.array([[1, 2, 3], [4, 5, 6]])
print (np.shape(b)) # (2, 3)

c = np.arange(32).reshape(8, 4)
print (c) 
'''
 [[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]
 [16 17 18 19]
 [20 21 22 23]
 [24 25 26 27]
 [28 29 30 31]]
'''

a = np.zeros((2, 2))
print (a)
'''
[[0. 0.]
 [0. 0.]]
'''

b = np.ones((1, 2))
print (b) # [[1. 1.]]

c = np.full((2, 2), 7)
print (c) # [[7 7], [7 7]]

d = np.eye(2)
print (d)
'''
[[1. 0.]
 [0. 1.]]
'''

e = np.random.random((2, 2))
print (e)
'''
[[0.81099309 0.7558072 ]
 [0.51913879 0.30149723]]
'''