#set
a = set([1,2,3])
print(a) # {1, 2, 3}

a = set("Hello")
print(a)
# {'e', 'o', 'l', 'H'}

s = set([1,2,3])
l = list(s)
print(l)
print(l[0])

t = tuple(s)
print(t)
print(t[0])

#교집합
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
print(s1 & s2)
print(s1.intersection(s2))

#합집합
print(s1 | s2)
print(s1.union(s2))

#차집합
print(s1 - s2)
print(s2 - s1)
print(s1.difference(s2))

# 1개 추가 - add
s = set([1,2,3])
s.add(4)
print(s)
# {1, 2, 3, 4}

# 여러개 추가 - update
s = set([1,2,3])
s.update([4,5,6])
print(s)
#{1, 2, 3, 4, 5, 6}

# 특정값 제거 - remove
s = set([1,2,3])
s.remove(2)
print(s)
#{1, 3}


# 리스트 중복제거
l = [1,1,1,1,2,2,2,1,3,3,3,1,2]
print(set(l)) #{1, 2, 3}

# set을 list로
print(list(set(l))) #[1, 2, 3]
