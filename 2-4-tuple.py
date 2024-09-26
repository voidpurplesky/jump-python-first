#typle
#튜플은 요소값을 바꿀수없다 - 삭제변경 불가

a = ()
print(a)
#()

a = (1)
print(type(a)) # <class 'int'>
print(a)

a = (1,)
print(type(a)) # <class 'tuple'>
print(a)
#(1,)
a = (1,2,3)
a = 1,2,3
print(a)
#(1, 2, 3)
a = (1,2,(3,4))

a = (1,2,3)
print(a[0])
# 1
# 튜플 요소값 삭제 - 에러
#del a[0]


#a[0] = 'a'

#인덱싱
a = ('a', 'b', 'c')
print(a[0]) # a

#슬라이싱
print(a[1:2]) #('b',)
print(a[0:1])
print(a[0:2]) # ('a', 'b')

# 튜플 요소 추가
t = (1,2,3)
t+=(4,)
print(t)

print(t)


