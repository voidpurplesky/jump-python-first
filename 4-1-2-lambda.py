    
# lambda 예약어
add = lambda a, b: a + b
print(add(3, 4))

mul3 = lambda x: x * 3
print(mul3(3)) # 3*3=9

# 리스트 요소 중에 양수만
print(list(filter(lambda x: x > 0, [1,-3,2,0,-5,6])))

# 리스트 요소에 2씩 곱하기
print(list(map(lambda a: a * 2, [1,2,3,4])))