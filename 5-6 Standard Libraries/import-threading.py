from time import sleep

def long_task(): # 5초 걸리는 함수
    for i in range(5):
        sleep(1) # 1초 대기
        print("working:%s\n" % i)

print("start")

for i in range(5):
    long_task()

print("end")