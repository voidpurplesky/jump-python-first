#피보나치 함수
'''
0 1 1 2 3 5 8 13
'''


for i in range(10):
    pass

def fibo(n):
    x = 0
    #1에 피보에 들어오게
    # 2. 1에 0리턴하고끗
    if n == 1:
        return x
    if n == 2:
        return 1
    if n > 3:
        pass
    return x

def fibo1(n):

    if n == 1:
        x = 0
    if n == 2:
        return 1
    if n > 3:
        n1 = 0
        n2 = 1

        
    return n
#x = 0
n = 2 # 항의 값. 입력받기

for i in range(n):
    print(fibo1(i), end=', ')

'''
n
1: 0
2: 1
3: 0+1=1 n1 + n2
4: 1+1=2 n2 + n3


'''

fibo1(n)

n1 = 0
n2 = 1

print("\n fibo2 - 0, 1, 1, 2, ...")
def fibo2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return fibo2(n-2) + fibo2(n-1)

print(fibo2(4))

for i in range(9):
    print(fibo2(i), end=', ')
#0, 1, 1, 2, 3, 5, 8, 13, 21,


print("\n fib(n)")
def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-2) + fib(n-1)

for i in range(9):
    print(fib(i), end=', ')


print("\n fib2(n)")
memo = {}

def fib2(n):
    if n == 0 or n == 1:
        return n
        
    if n not in memo:
        memo[n] = fib2(n-2) + fib2(n-1)
    
    return memo[n]


print(memo)
for i in range(9):
    print(fib2(i), end=', ')