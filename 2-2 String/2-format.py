n = 3
s = "입니다."

print(str(n) + s)

# format() 함수
print("{0}입니다.".format(3))

print("{0}입니다. {1}".format(3, 2))
print("{number}입니다. {day}".format(number=3, day=2))

n = 1
print("\n %s % n = 1")
print("%s" % n)


# 포맷 코드와 숫자 함께 사용하기 66
# 1. 정렬과 공백
print("%10s" % "hi") # 오른쪽 정렬
#        hi
print("%-10sjane" % "hi") # 왼쪽 정렬 
#hi        jane

# 2. 소수점 표현하기
print("%0.4f" % 0.1234567)
print("%10.4f" % 0.1234567)
#    0.1235

# 왼쪽 정렬
print("{0:<10}jane".format("hi"))
print("{0:>10}".format("hi")) #오른쪽
#        hi
print("{0:^10}jane".format("hi")) #가운데
#    hi    jane
#공백채우기 70
print("{0:=^10}jane".format("hi"))
#====hi====jane
print("{0:!<10}jane".format("hi"))
#hi!!!!!!!!jane
print("{0:0.4f} {1:0.5f}".format(0.123456, 0.123456)) # 0.1235 0.12346
print("{0:10.4f}".format(0.123456))

# f 문자열 포매팅 71 3.6 버전이후 가능
name = "홍길동"

sf = f'{name}입니다.'
print(sf)
print(f"{name}입니다.")
d = {'name':'홍길동', 'age':30} # dictionary
print(f'이름은 {d["name"]}입니다. 나이는 {d["age"]}')

print(f'{"ERROR":=^30}')
#============ERROR=============