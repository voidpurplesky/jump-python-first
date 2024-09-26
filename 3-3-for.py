#for
l = [1,2,3]
for i in l:
    print(i)

a = [(1,2),(3,4),(5,6)]
for (f,s) in a:
    print(f + s)

a = range(10)
print(a)
#range(0, 10) : 0 <= x < 10

sum = 0
for i in range(1,11):
    sum = sum + i
print(sum)
sum = 0
for i in range(1,11):
    sum += i
print(sum)

# list comprehension
# 리스트안에 for문을 포함시키는

a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)
print("result=")
print(result)

result = [num*3 for num in a]
print(result)

# 짝수만
result = [num*3 for num in a if num%2 == 0]
print(result)

result = [num*2 for num in a if num%2 != 0]
print(result)

# for 문 2개 이상 사용
result = [x*y for x in range(2,10)
          for y in range(1,10)]
print(result)

for i in range(2, 10):
    for j in range(1, 10):
        print('%d * %d = %d' % (i, j, i * j), end=' ')
    print()

for i in range(1, 101):
    if i < 100: print(i, end=',')
    else: print(i)