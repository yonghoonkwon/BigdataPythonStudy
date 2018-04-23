import numpy as np

x = np.array([[1, 2],[3, 4]], dtype=np.float64)
y = np.array([[5, 6],[7, 8]], dtype=np.float64)


'''
[[ 6.  8.]
 [10. 12.]]
'''
print (x+y)
print (np.add(x, y))


'''
[[-4. -4.]
 [-4. -4.]]
'''
print (x-y)
print (np.subtract(x, y))


'''
[[ 5. 12.]
 [21. 32.]]
'''
print (x*y)
print (np.multiply(x, y))


'''
[[0.2        0.33333333]
 [0.42857143 0.5       ]]
'''
print (x/y)
print (np.divide(x, y))


'''
[[19. 22.]
 [43. 50.]]
'''
print (x.dot(y))
print (np.dot(x, y))


print(np.sum(x)) # 10.0
print(np.sum(x, axis=0)) # [4. 6.] 
print(np.sum(x, axis=1)) # [3. 7.]


'''
[[1. 2.]
 [3. 4.]]
'''
print(x)
'''
[[1. 3.]
 [2. 4.]]
'''
print(x.T) # transpose
