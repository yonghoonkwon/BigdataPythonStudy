import numpy as np

a = np.array([[1, 2, 3, 4], 
              [5, 6, 7, 8], 
              [9, 10, 11, 12]])

b = a[:2, 1:3]

print (a[0, 1]) # 2
b[0, 0] = 77
print (a[0, 1]) # 77

row_r1 = a[1, :]
row_r2 = a[1:2, :]

print('row_r1: {}, row_r1.shape: {}'.format(row_r1, row_r1.shape))
print('row_r2: {}, row_r2.shape: {}'.format(row_r2, row_r2.shape))

col_r1 = a[:, 1]
col_r2 = a[:, 1:2]

print('col_r1: {}, col_r1.shape: {}'.format(col_r1, col_r1.shape))
print('col_r2: {}, col_r2.shape: {}'.format(col_r2, col_r2.shape))

print (a[[0, 1, 2], [0, 1, 0]]) # [1 6 9]
print (np.array([a[0,0],a[1,1],a[2,0]])) # [1 6 9]


bool_idx = (a > 2)
print (bool_idx)
'''
[[False  True  True  True]
 [ True  True  True  True]
 [ True  True  True  True]]
'''
print (a[bool_idx]) # [77  3  4  5  6  7  8  9 10 11 12]
print (a[a>2]) # [77  3  4  5  6  7  8  9 10 11 12]
