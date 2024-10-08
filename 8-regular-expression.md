# 8장 정규 표현식
## 8-2 정규 표현식 시작하기

#### 컴파일 옵션 <sup>367</sup>

- DOTALL S : .이 줄바꿈 문자 \n를 포함해 모든 문자와 매치
- IGNORECASE I : 대소문자에 관계없이
- MUTILINE M : 여러줄과 매치 ^ $ 메타문자 사용과 관계
- VERBOSE X : verbose 모드. 정규식을 보기 편하게 만들고 주석 사용 가능

##### DOTALL S

##### IGNORECASE I

##### MULTILINE M <sup>369</sup>
메타 문자인 ^, $과 연관된 옵션

^는 문자열의 처음, $는 문자열의 마지막

예를 들어, ^python인 경우, 문자열의 처음은 항상 python으로 시작해야 매치됨

python$이라면 문자열의 마지막은 항상 python으로 끝나야 매치됨

코드
```
data = """python one
life is too short
python two
you need python
python three"""

p = compile("^python\s\w+")
print(p.findall(data))
```
결과
```
['python one']
```
문자열 전체의 처음이 아니라 각 줄의 처음으로 인식시키고 싶을때 MULTILINE(M) 사용

코드
```
p = compile("^python\s\w+", M)
print(p.findall(data))
```
결과
```
['python one', 'python two', 'python three']
```
##### VERBOSE X
정규식을 주석 또는 줄단위로 구분할 수 있는 옵션
```
p = compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')
```

```
p = compile(r"""
            &[#]            # Start of a numeric entity reference
            (
            0[0-7]+         # Octal form
            |[0-9]+         # Decimal form
            |x[0-9a-fA-F]+  # Hexadecimal form
            )
            ;               # trailing semicolon
            """, X)
```

#### 역슬래시 문제
예를 들어 \section 문자열을 찾기 위한 정규식을 만들때
`\section` 는 \s 문자가 whitespace로 해석되어 `[\t\n\r\f\v]ection` 으로 읽어져서 `\\section` 이라고 해야함

파이썬 정규식 엔진의 문제로 \\이 \로 변경되어 \\ 를 전달하려면 \\\\라고 해야함

이 문제를 해결하려면 raw string 표현법을 사용해야한다.
```
p = compile(r'\\section')
```
### 08-3 강력한 정규표현식의 세계로
#### 문자열 소비가 없는 메타 문자
zerowidth assertions 메타문자
