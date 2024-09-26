# 문자열 관련 함수들 72
# 문자 개수 세기 - count 대소문자구분
a = "hobby"
a.count('b') # 2
s = "ABCDabcd"
print(s.count("A")) # 1

# 위치 알려주기 1 - find 처음 나온 위치 -1 없으면
#a = 
print(s.find("A")) # 0
print(s.find("AB")) # 0
# 위치 알려주기 2 - index 없으면 에러
print(s.index("A"))

# 문자열 삽입 - join
print(",".join('abcd')) #a,b,c,d
#리스트,튜플도
print(",".join(['a', 'b', 'c', 'd']))

print(s.upper()) # ABCDABCD
print(s.lower())

s = "          hi            "
s2 = s.lstrip()
print(f'[{s2}]') # [hi            ]
s2 = s.rstrip()
print(f'[{s2}]') # [          hi]
s2 = s.strip()
print(f'[{s2}]') # [hi]

s = "abcd"
print(s.replace("ab", "cd")) # cdcd
s = "a@a@"
print(s.replace("@", "#"))

s = "a b c d"
print(s.split()) # ['a', 'b', 'c', 'd'] list
s = "a:b:c:d"
print(s.split(':')) # ['a', 'b', 'c', 'd'] list