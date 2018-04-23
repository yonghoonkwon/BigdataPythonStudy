
import numpy as np

def makeNumpyMatrix(n):
    n = int(n)
   
    if n > 0 and n%3 == 0:
        return np.arange(int(n)).reshape(int(n/3), 3).T   
    else:
        print("%d is not divided 3"%(n))      
        return 0
    
num = input('one number: ')
print(makeNumpyMatrix(num))


