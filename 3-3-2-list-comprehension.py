# list comprehension 리스트 컴프리헨션
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
'''
[2, 4, 6, 8, 10, 12, 14, 16, 18, 3, 6, 9, 12, 15, 18, 21, 24, 27, 4, 8, 12, 16, 20, 24, 28, 32, 36, 5, 10, 15, 20, 25, 30, 35, 40, 45, 6, 12, 18, 24, 30, 36, 42, 48, 54, 7, 14, 21, 28, 35, 42, 49, 56, 63, 8, 16, 
24, 32, 40, 48, 56, 64, 72, 9, 18, 27, 36, 45, 54, 63, 72, 81]
'''
l = [10,2,3,11,5]
result = [num for num in l if num > 5]
print(result) #[10,11]
print(sum(result)) #21