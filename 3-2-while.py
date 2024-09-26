#while
a = 0
while a < 10:
    print(a)
    a = a + 1
    if a == 10: print('a is 10 end')

'''
0
1
2
3
4
5
6
7
8
9
a is 10 end'''

i = 0
while True:
    i += 1
    if (i > 5): break
    print('*' * i)
