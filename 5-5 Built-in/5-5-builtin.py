# 모두 참이면 true, 빈값 true
print(all([1,2,3])) # T
print(all([1,2,3,0])) # F
print(all([1,2,3,5])) # T
print(all([1,3,4,5])) # t
print(all([0])) # F
print(all([])) # T 인수가 빈값

# 하나라도 참이 있으면 true, 빈값 false
print(any([1,2,3,4])) # true
print(any([1,2,3,0])) # true
print(any([0])) # F
print(any([])) # F 빈값

#chr
print(chr(97)) # a
print(chr(44032)) # 가

#ord : 문자의 유니코드 숫자값 리턴
print(ord('a'))
print(ord('가'))


print(dir([]))
'''
'__subclasshook__', 
'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
'''


for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)

# eval 문자열을 표현식으로 받아들여 실행
print(eval('1 + 2'))




# 변환 list, int, tuple, str
# int
print(int(3.5)) # 3
print(int('11', 2)) # 2진수 3
print(int('1A', 16)) # 16진수 26

# list 반복가능한 데이터를 입력받아 리스트로 만들어 리턴
print(list("abcd"))
print(list((1,2,3)))
'''
['a', 'b', 'c', 'd']
[1, 2, 3]
'''

# 리스트함수에 리스트를 입력하면 똑같은 리스트를 복사(값만)
a = [1,2,3]
b = list(a)
print(b)
a[0] = 4
print(a)
print(b) # [1,2,3]
