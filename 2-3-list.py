# list
# list는 여러 타입을 한번에 담을수있고 리스트 안에 리스트도 가능
a = [1, 2, "String", 'String2',[3, 4, "String2"]]
print(a)

a = [1,2,3,4,5]
print(a[0]) # 1
print(a[1]+a[3]) # 2+4=6
print(a[-1]) # 5

a = [1,2,3,['a','b','c']]
print(a[3][0]) # a

# 리스트의 슬라이싱 80
a = [1,2,3,4,5]
print(a[0:2]) # [1, 2]
print(a[:2]) # [1, 2]
print(a[2:]) # [3, 4, 5]
print(a[1:3]) # [2, 3]

# 중첩된 리스트에서 슬라이싱 81
a = [1,2,3,['a','b','c'], 4, 5]
print(a[3][:2]) # ['a', 'b']

# 리스트 연산 82
# 리스트 더하기 +
a = [1,2,3]
b = [4,5,6]
print(a+b)
a += b
print(a)
a + [7,8]
print(a) # 안바뀜 그대로

print(a + [7,8])
# 리스트 확장 extend +=
a.extend([7,8])
print(a)


# 리스트 반복 *
a = [1,2,3]
print(a * 3) # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# 리스트 길이
print(len(a)) # 3

# 리스트 수정
a = [1,2,3]
a[2] = 4
print(a)
# [1, 2, 4]

# 리스트 요소 삭제 del
del a[1]
print(a)
# [1, 4]

# 슬라이싱 여러개 삭제
a = [1,2,3,4,5]
del a[2:]
print(a)
# [1, 2]

# 리스트 관련 함수
a = [1,2,3]
a.append(4)
print(a)

a.append([5,6])
print(a)
# [1, 2, 3, 4, [5, 6]]

# 리스트 정렬 sort
l = [4,2,3,1]
l.sort()
print(l)
# 역순정렬 : reverse는 역순정렬이 아니라 순서만 바꾸므로 정렬 후 reverse해야 역순정렬됨
l.reverse()
print(l)
## sorted(iterable) 차이 : 
# sort는 원래의 리스트를 정렬하고 sorted는 정렬된 리스트를 반환하지만 원래의 리스트는 변함없음
# sorted는 리스트말고 튜플도됨
l = [4,2,3,1]
print("sorted(l)=")
print(sorted(l))
print(l)


l = [1,3,5,4,2]
l.reverse()
print("l.reverse()")
print(l)
#[2, 4, 5, 3, 1] 순서만 반대로! 역순정렬은 안됨

# 인덱스 반환 index
a = [1,2,3]
print(a.index(3))
# 2

# 리스트에 요소 삽입 insert
a.insert(0, 4)
print(a)
#[4, 1, 2, 3]

# 리스트 요소 제거 remove
a =  [1,2,3,1,2,3]
a.remove(3)
print(a)
#[1, 2, 1, 2, 3] 
# 첫번째 3만 제거

# l.pop() : 리스트 요소 끄집어 내기 pop 맨 마지막 요소를 리턴하고 그 요소 삭제
a = [1,2,3]
print(a.pop())
print(a)
#3
#[1, 2]

a = [1,2,3]
print(a.pop(1))
print(a)
#2
#[1, 3]
# pop(x) : x번째 요소를 리턴하고 그 요소 삭제

# 리스트에 포함된 요소 x의 개수 세기 count
a = [1,[1]]
print(a.count(1))
#1

a = ['1','123']
print('count("1")=')
print(a.count('1'))
# 1

# 리스트 확장 - extend
a = [1,2,3]
a.extend([4,5])
print(a)
#[1, 2, 3, 4, 5]
