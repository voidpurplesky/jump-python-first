f = open('4-3-새파일.txt', 'w')
f.close()
'''파일열기모드
r 읽기모드: 파일을 읽기만
w 쓰기모드: 파일에 내용을 쓸때 - 해당파일이 이미 존재할 경우 원래 있던 내용이 사라지고 새파일이 생성됨
a 추가모드: 파일의 마지막에 새로운 내용 추가'''

#D:\cmj\workspaces\python
f = open('D:/cmj/workspaces/python/4-3-write2.txt', 'w', encoding='UTF-8')
for i in range(1, 11):
    data = "%d번쨰 줄입니다.\n" % i
    f.write(data)
f.close()

# readline
#UnicodeDecodeError: 'cp949' codec can't decode byte 0x80 in position 5: illegal multibyte sequence
'''encoding 안써주면 에러'''
f = open('4-3-read.txt', 'r', encoding='UTF-8')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

# readlines
f = open('4-3-read.txt', 'r', encoding='UTF-8')
lines = f.readlines()
for line in lines:
    print(line.strip()) # strip 줄바꿈문자(\n) 제거
f.close()

# 3. read
'''파일의 전체를 문자열로 리턴'''
f = open('4-3-read.txt', 'r', encoding='UTF-8')
data = f.read()
print(data)
f.close()

# 4. 파일 객체를 for문과 함께
f = open('4-3-read.txt', 'r', encoding='UTF-8')
for line in f:
    print(line)
f.close()

# a 추가모드 : 파일에 새로운 내용 추가하기 
f = open('4-3-write2.txt', 'a', encoding='UTF-8')
for i in range(11, 21):
    data = 'line %d번째 줄입니다.\n' % i
    f.write(data)
f.close()

# with
with open('4-3-with.txt', 'w', encoding='UTF-8') as f:
    f.write('ABC가나다')