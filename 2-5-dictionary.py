#2-5 dictionary 93

a = {0:11, 'k':'v'}
print(a[0]) # 11
print(a['k']) # v


# 딕셔너리 쌍 추가
a[1] = 'b'
print(a) # {0: 11, 'k': 'v', 1: 'b'}

# 딕셔너리 값 변경
a[1] = 'c'
print(a) # {0: 11, 'k': 'v', 1: 'c'}

# 딕셔너리 요소 삭제
del a[1]
print(a) # {0: 11, 'k': 'v'}

a = {'가': '나'}
print(a) # {'가': '나'}

#key : 리스트 x, tuple O

#딕셔너리 관련 함수
#key 리스트 만들기 - keys
a = {'name':'pey', 'phone':'010-1234-5678', 'birth':'2024'}
print(a.keys())
#dict_keys(['name', 'phone', 'birth'])

print(a.values())
#dict_values(['pey', '010-1234-5678', '2024'])

print(a.items())
#dict_items([('name', 'pey'), ('phone', '010-1234-5678'), ('birth', '2024')])

print(a.get('name'))
print(a.get('nokey', 'foo'))

print('name' in a) #True

d = {'국어':80,'영어':75,'수학':55}
for k in d:
    print(k)

for k, v in d.items():
    print(k, v)
'''
국어 80
영어 75
수학 55
'''
print(sum(list(d.values())))
print(len(d))
print(sum(list(d.values()))/len(d))


# pop(key)
print(d.pop('영어')) #75
print(d) #{'국어': 80, '수학': 55}


# pop() : 없다
d = {'A':'key A value', 'B': 'key B value', 'C': 'c', 'D': 'd', 'E': 'e'}
#print(d.pop())
#TypeError: pop expected at least 1 argument, got 0

d = dict()
d[(1,)] = 'tuple key value'
print(d)
#{(1,): 'tuple key value'}

