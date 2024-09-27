from time import sleep
from threading import Thread

def long_task(): # 5초 걸리는 함수
    for i in range(5):
        sleep(1) # 1초 대기
        print("working:%s\n" % i)

print("start")

threads = []

for i in range(5):
    #long_task()
    t = Thread(target=long_task) # 스레드 생성
    threads.append(t)

for t in threads:
    t.start()   #스레드 실행


for t in threads:
    t.join() # 스레드가 종료될때까지 대기
print("end")
'''
start
end
working:0
working:0

working:0

working:0

working:0

--- join 추가후
start
working:0
working:0

working:0

working:0


working:0

end
'''