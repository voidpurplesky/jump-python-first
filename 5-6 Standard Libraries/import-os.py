#os
# 환경변수
from os import environ, getcwd, system, chdir, popen

print(environ)
'''
딕셔너리형태 environ 객체
environ({'ADSK_3DSMAX_X64_2018': 'C:\\Program Files\\Autodesk\\3ds Max 2018\\', 


'''
print("\nPATH=")
print(environ['PATH'])
'''
C:\Python312\Scripts\;C:\Python312\;C:\oraclexe\app\oracle\product\11.2.0\server\bin;
'''


print(getcwd())
#D:\cmj\workspaces\python

print(system("dir"))
'''
 D 드라이브의 볼륨: 새 볼륨
 볼륨 일련 번호: 3004-19A0

 D:\cmj\workspaces\python 디렉터리

2024-09-25  오후 02:57    <DIR>          .
2024-09-25  오후 02:57    <DIR>          ..
2024-09-23  오전 10:30               230 2-1-1.py
'''

chdir("c:\\")
print(getcwd()) #c:\
print(system("dir"))
'''
 C 드라이브의 볼륨에는 이름이 없습니다.
 볼륨 일련 번호: C27F-7655

 c:\ 디렉터리

2024-08-02  오후 09:25    <DIR>          apache-tomcat-9.0.93
2024-08-06  오전 09:20    <DIR>          app
'''

#os.popen(str command) 시스템 명령어 결과값을 파일 객체로 리턴

f = popen("dir")
print(f.read())