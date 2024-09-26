from re import compile, match

data = """
park 800905-1049118
kim  700905-1059119
"""
pat = compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))


p = compile("[abc]")
print(p.match("a")) #<re.Match object; span=(0, 1), match='a'>
print(p.match("dude")) #None

# . - \n을 제외한 모든 문자
p = compile("a.b") # a + 모든문자 + b
print(p.match("aab")) #<re.Match object; span=(0, 3), match='aab'>
print(p.match("abc")) #None
print(p.match("abb")) #<re.Match object; span=(0, 3), match='abb'>

# [.] 대괄호사이는 반드시들어가야하는문자
p = compile("a[.]b") # a + . + b
print(p.match("a.b")) #<re.Match object; span=(0, 3), match='a.b'>
print(p.match("abc")) #None
print(p.match("a0c")) #None

# * - 0~n개 사용
p = compile("ca*t") #문자 a가 0~n개
# 0개
print(p.match("ct")) #<re.Match object; span=(0, 2), match='ct'>
print(p.match("caaaaaaat")) #<re.Match object; span=(0, 9), match='caaaaaaat'>

# + : 최소한번이상반복
p = compile("ca+t") #문자 a가 1~n개
# 0개
print(p.match("ct")) #None
print(p.match("caaaaaaat")) #<re.Match object; span=(0, 9), match='caaaaaaat'>

# 반복횟수 {m, n}

# {3,} 3이상 
# {,3} 3이하
'''
{m} : m번 반복
{m, } : m번 이상 반복
생략된 m은 0과 동일, 생략된 n은 무한대(약2억개 미만)
{1,} = +
{0,} = *
'''
# 2번 반복
p = compile("ca{2}t") 

print(p.match("cat")) #None
print(p.match("caat")) #<re.Match object; span=(0, 4), match='caat'>
print(p.match("caaaaaaat")) #None

# 2~5번 반복
print("\nca{2, 5}t")
p = compile("ca{2, 5}t") 

print(p.match("cat")) #None
print(p.match("caaat")) #None
print(p.match("caaaaat")) #None

# ? {0,1}
print("\nab?c")
p = compile("ab?c") 

print(p.match("abc")) #<re.Match object; span=(0, 3), match='abc'>
print(p.match("ac")) #<re.Match object; span=(0, 2), match='ac'>
print(p.match("ad")) #None

# + 1~n개
print("\n [a-z]+")
p = compile("[a-z]+") 

print(p.match("a")) #<re.Match object; span=(0, 1), match='a'>
print(p.match("")) #None
print(p.match("3a")) #None


m = p.match("a")
print(m.group()) #a

# match : 문자열의 처음부터
# search : 문자열 전체에서 검색
print("\n search(str)")
print(p.search("3a")) #<re.Match object; span=(1, 2), match='a'>

# findall(str) list : 매치되는 값을 찾아 리스트로 리턴
print("\n findall(str)")
print(p.findall("life is too short")) #['life', 'is', 'too', 'short']

print("\n match 객체 - match()")
m = p.match("python")
print(m.group()) 
print(m.start())
print(m.end())
print(m.span())
'''
python
0
6
(0, 6)
'''
# None 이면 에러
# #AttributeError: 'NoneType' object has no attribute 'group'

print("\n match 객체 - search()")
m = p.search("3 python")
print(m.group()) 
print(m.start())
print(m.end())
print(m.span())

'''
python
2
8
(2, 8)
'''

#m = match('[a-z]+', "3 python")