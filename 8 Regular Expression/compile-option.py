'''
DOTALL S .이 줄바꿈문자를 포함해 모든 문자와 매치
IGNORECASE I 대소문자에 관계없이
MULTILINE M 여러줄과 매치 ^ $ 메타 문자 사용과 관계
VERBOSE X   verbose 모드를 사용할수있게한다. 정규식을 보기 편하게 만들고 주석등을 사용할수있음

'''

from re import compile, DOTALL, S, I, M

# DOTALL S
p = compile('a.b')
m = p.match('a\nb')
print(m) #None

p = compile('a.b', DOTALL)
m = p.match('a\nb')
print(m) #<re.Match object; span=(0, 3), match='a\nb'>

p = compile('a.b', S)
m = p.match('a\nb')
print(m) 

# IGNORECASE I
p = compile('[a-z]+', I)
m = p.match('python')
print(m) #<re.Match object; span=(0, 6), match='python'>
print(p.match('Python')) #<re.Match object; span=(0, 6), match='Python'>
# [a-z]+ 정규식은 소문자만을 의미하지만 I옵션으로 대소문자 구별없이 매치됨

##### MULTILINE, M
''' ^는 문자열의 처음, $는 문자열의 마지막 '''

p = compile("^python\s\w+")

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data)) #['python one']

p = compile("^python\s\w+", M)
print(p.findall(data)) #['python one']

##### VERBOSE, X
'''정규식을 주석 또는 줄단위로 구분할 수 있는 옵션'''
p = compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')

p = compile(r"""
            &[#]            # Start of a numeric entity reference
            (
            0[0-7]+         # Octal form
            |[0-9]+         # Decimal form
            |x[0-9a-fA-F]+  # Hexadecimal form
            )
            ;               # trailing semicolon
            """, X)

#### 역슬래시 문제
p = compile(r'\\section')
