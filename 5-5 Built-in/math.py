#abs(x) 절대값
print(abs(-1)) #1

#round(number [, ndigits]) : 반올림
# ndigits : 반올림하는 소수점 자리

print(round(3.4)) # 3
print(round(3.5)) # 4

print(round(3.4, 1)) # 3.4
print(round(3.5, 1)) # 3.5

print(round(3.01, 1)) # 3.0
print(round(3.09, 1)) # 3.1

# divmod(a, b) : a를 b로 나눈 몫과 나머지를 튜플로 리턴
print(divmod(5, 2)) # (2, 1)

#pow(x, y) : x를 y제곱
print(pow(2,10)) #1024

#oct(x) 8진수
print(oct(34)) #0o42
# hex(x) 정수를 16진수로 변환
print(hex(234)) # 0xea

# iterable
#sum(iterable) 
print(sum([1,2,3]))
print(sum((1,2,3)))

#max(iterable)
print("max")
print(max([1,2,3]))
print(max((1,2,3)))