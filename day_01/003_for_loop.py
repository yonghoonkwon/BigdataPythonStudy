words = ['this', 'is', 'wonder']

for x in words:
    print(x, end=' ') # this is wonder

print(' ')

for x in range(10):
    print(x, end=' ') # 0 1 2 3 4 5 6 7 8 9
    
print(' ')

dic = {'kim':111, 'park':222}

for k,v in dic.items():
    print('key: %s, value: %s'%(k, v)) 