# def 함수
def add(a, b):
    return a + b

a = 3
b = 4
c = add(a, b)
print(c)

#입력값이 없는 함수
def hi():
    return 'hi'
print(hi())

#리턴값이 없는 함수
def add(a,b):
    print("%d, %d의 합은 %d입니다." % (a, b, a + b))
add(3, 4)

#입력값도 리턴값도 없는 함수
def hi():
    print('hi')
hi()

# 매개변수를 지정하여 호출
def sub(a, b):
    return a - b
result = sub(a=7, b=3)
print(result)
#순서에 상관없이 사용 가능
print(sub(b=3, a=5))

# *args : 모든 입력 인수를 튜플로 변환
# 입력값이 몇개가 될지 모를때
## 여러개의 입력값을 받는 함수
def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result

print("*args")
print(add_many(1,2,3))
print(add_many(1,2,3,4,5,6,7,8,9,10))
print(add_many()) #0

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result *= i
    return result

print(add_mul("add", 1,2,3,4,5))
print(add_mul("mul", 1,2,3,4,5))

# **kwargs : 모든 키=값 형태의 입력 인수를 딕셔너리로 변환
# 키워드 매개변수, kwargs
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)
print_kwargs(name='foo', age=3)

print("\n*args, **kwargs")
def func(*args, **kwargs):
    print(args)
    print(kwargs)

func()
func(1,2,3,name='foo',age='3')
func(name='foo',age=3)
func(1,2,3)
#func(name='foo', 1,2 3) 형태는 안됨
'''
*args, **kwargs
()
{}
(1, 2, 3)
{'name': 'foo', 'age': '3'}
()
{'name': 'foo', 'age': 3}
(1, 2, 3)
{}
'''
# 함수의 리턴값은 언제나 하나
def add_and_mul(a, b):
    return a + b, a * b
print(add_and_mul(3, 4))
#(7, 12)

r1, r2 = add_and_mul(3, 4)
print(r1)
print(r2)

# 매개변수에 초기값 미리 설정
def say_myself(name, age, man=True):
    print("my name is %s." % name)
    print("my age is %d." % age)
    if man:
        print("i am man")
    else:
        print("I'm a woman.")

say_myself("MJ", 30)
say_myself("MJ", 30, False)
