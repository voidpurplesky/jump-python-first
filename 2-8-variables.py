a = 1
b = a
print(id(a)) #140723356043704
print(id(b)) #140723356043704
print(a is b)#True
a = 2
print(a)
print('b=')
print(b)
print(id(a)) #140723356043736
print(id(b)) #140723356043704

# 리스트 복사
a = [1,2,3]
b = a
a[1] = 4
print(a)
print(b)
'''[1, 4, 3]
[1, 4, 3]'''

a = [1,2,3]
b = a[:]
a[1] = 4
print(a)
print(b)
'''
[1, 4, 3]
[1, 2, 3]'''

from copy import copy
a = [1,2,3]
b = copy(a)
print(a is b)#f

#변수를 만드는 여러가지 방법
a,b = ('c', 'd')
print(a)
print(b)

(a,b) = 'c', 'd'
print(a)
print(b)

[v1,v2] = ['c','d']
print(v1)

a = 3
b = 5
a,b = b,a
print(a)
print(b)