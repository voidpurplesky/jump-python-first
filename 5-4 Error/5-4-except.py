# 5-4 예외처리
# try-except
# 1. try-except만: 오류의 종류에 상관없이
try:
    4/0
except:
    print('error')
'''error'''

# 2. 발생오류 포함
try:
    4/0
except ZeroDivisionError:
    print('error')
'''error'''

# 3. 오류 변수까지 포함
try:
    4/0
except ZeroDivisionError as e:
    print(e)
'''division by zero'''

# try-finally - 예외발생여부에 상관없이 항상 수행
try:
    f = open('5-4-finally.txt', 'w')
#    4/0 # 이후예제실행이 안되므로주석처리
finally:
    print('finally')
    f.close() # 중간에 오류가 발생해도 무조건 실행
'''
finally
Traceback (most recent call last):
  File "d:\cmj\workspaces\python\5-4-except.py", line 27, in <module>
    4/0
    ~^~
ZeroDivisionError: division by zero
'''
# 여러개의 오류 처리하기
print("여러개의 오류 처리하기")
try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print("0으로 나눌수없음")
except IndexError:
    print("인덱싱할수없음")

try:
    a = [1,2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError):
    print("error")

#try-else 오류가 없을경우에만 수행
#오류있을때 else 안실행 - error
try:
    4/0
except:
    print("try-else error")
else:
    print("try-else no error")

#오류없을때 else 실행됨 - no error
try:
    pass
except:
    print("try-else error")
else:
    print("try-else no error")


#오류회피하기 pass
#오류발생시키기 raise
