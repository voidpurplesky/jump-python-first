from math import gcd, lcm

#gcd 최대공약수
print(gcd(60, 100, 80))
# 3.5 버전부터 사용가능
# 3.9부터 여러개의 인수

# lcm 최소공배수
print(lcm(15, 25))

from random import random, randint, sample
# random : 0.0~1.0 사이의 실수 중에서 난수
print(random()) # 0.5109109281574612

l = ['a','b','c','d']
print("sample(iterable, length)")
print(sample(l, len(l)))
print(sample(l, 1))

# randint : rand+int 
print(randint(1, 10)) # 7 1~10사이 정수 중에서 난수