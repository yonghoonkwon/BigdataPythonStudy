
people = {   
    'Kim': {
        'phone':'1234',
        'addr':'seoul'}
    ,
    'Lee':{
        'phone':'5678',
        'addr':'pusan'}
    ,
    'Park':{
        'phone':'9090',
        'addr':'guro'}
    }

name = input('Name: ')
request = input('phone (p) or addr (a): ')
key = ''

if request == 'p':
    key = 'phone'
elif request == 'a':
    key= 'addr'
else:
    assert('key error' and False)
    
name_ = people.get(name, {})
value = name_.get(key, key)
    
print('name: %s, %s: %s'%(name, key, value))