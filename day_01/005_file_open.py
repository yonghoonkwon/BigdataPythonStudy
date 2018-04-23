# file write from text
f = open('test_file.txt', 'w')
f.write('hello~')
f.close()

f = open('test_file.txt', 'r')
print(f.read())
f.close()