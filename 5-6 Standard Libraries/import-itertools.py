from itertools import zip_longest, permutations, combinations
student = ['한민서', '황지민', '이영철', '이광수', '김승민']
snacks = ['사탕', '초콜릿', '젤리']

print(list(zip(student, snacks)))
#[('한민서', '사탕'), ('황지민', '초콜릿'), ('이영철', '젤리')]

result = zip_longest(student, snacks, fillvalue='새우깡')
print(list(result))
'''
[('한민서', '사탕'), ('황지민', '초콜릿'), ('이영철', '젤리'), ('이광수', '새우깡'), ('김승민', '새우깡')]
'''

#순열 permutations - 순서
print(list(permutations(['a','b','c'], 2)))
#[('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b')]

for a, b in permutations(['a', 'b', 'c'], 2):
    print(a, b)
'''
a b
a c
b a
b c
c a
c b
'''

# 조합 순서x combinations
# combinations(iterable, r) : 반복가능한 객체중에서 r개를 선택한 조합
print(list(combinations(['a', 'b', 'c'], 2)))
#[('a', 'b'), ('a', 'c'), ('b', 'c')]

#로또 1~45 중 6개
print(len(list(combinations(range(1, 46), 6))))


