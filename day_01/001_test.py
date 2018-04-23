print('hello world')

x=1
y=1.
str='abc123'

print(x)
print(y)
print(str)

x=['a', 'b', 'c', 'd']

print(x[0])
print(x[-1])
print(x[1:3])
print(x[-2:])

print('welcome %s'%('python'))
print('%d * %d = %d'%(3, 3, 3*3))
print('test {} * {}'.format(10, 20))

x = {'A':'apple', 'B':'banana'}
print(x) # {'A':'apple', 'B':'banana'}
print(x['A']) # apple
print(x.get('C', 'not found')) # not found

print(pow(2, 3)) # 8
print(int(12.3)) # 12
print(int(-4.3)) # -4


from math import floor, sqrt
print(floor(12.3)) # 12
print(sqrt(40)) # 6.2324555320336759

import cmath
print(cmath.sqrt(-1)) # 1j
print((1+2j)+(3+4j))
