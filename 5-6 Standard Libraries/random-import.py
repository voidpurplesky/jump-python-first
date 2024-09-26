from random import random, randint, sample
# random : 0.0~1.0 사이의 실수 중에서 난수
print(random()) # 0.5109109281574612

l = ['a','b','c','d']
print("sample(iterable, length)")
print(sample(l, len(l)))#['a', 'd', 'b', 'c']
print(sample(l, 1)) #['a']
#print(sample(l, 10))
#ValueError: Sample larger than population or is negative

# randint : rand+int 
print(randint(1, 10)) # 7 1~10사이 정수 중에서 난수

# xx.xx
print("\n xx.xx")
print(round(random() * 10, 2))