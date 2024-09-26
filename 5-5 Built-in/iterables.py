#sorted
#sorted(iteable)

print(sorted([3,1,2]))
print(sorted(['c','a','b']))
print(sorted("zero"))
'''
[1, 2, 3]
['a', 'b', 'c']
['e', 'o', 'r', 'z']
'''




## sorted(iterable) 차이 : 
# sort는 원래의 리스트를 정렬하고 sorted는 정렬된 리스트를 반환하지만 원래의 리스트는 변함없음
# sorted는 리스트말고 튜플, 문자열도됨

l = [4,2,3,1]
print("sorted(l)=")
print(sorted(l))
print(l)

# 리스트 정렬 sort
l.sort()
print(l)

#zip
#zip(*iterable)
print(list(zip([1,2,3],[4,5,6])))
print(list(zip([1,2,3],[4,5,6],[7,8,9])))
'''
[(1, 4), (2, 5), (3, 6)]
[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
'''
print(list(zip("abc", "def")))
#[('a', 'd'), ('b', 'e'), ('c', 'f')]