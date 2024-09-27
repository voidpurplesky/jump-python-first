# glob(pathname)
# 디렉터리에 있는 파일을 리스트로

from glob import glob

print(glob("c:/*"))

'''
['c:/$Recycle.Bin', 'c:/$WinREAgent', 'c:/AMTAG.BIN', 

'c:/Update.ini', 'c:/Users', 'c:/webserver', 'c:/Windows', 'c:/XecureSSL', 'c:/컴활수업']

'''

print(glob("c:/*.ini")) #['c:/Update.ini']

