# 파이썬 내장 클래스인 Exception 클래스를 상속하여 만들수있다
class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)

#say_nick('천사')
#say_nick('바보')

try:
    say_nick('천사') # 천사
    say_nick('바보') # 허용되지않는
except MyError:
    print("허용되지않는 별명입니다.")

try:
    say_nick('천사') # 천사
    say_nick('바보') # 허용되지않는
except MyError as e:
    print(e)