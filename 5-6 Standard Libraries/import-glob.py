# glob(pathname)
# 디렉터리에 있는 파일을 리스트로

from glob import glob

print(glob("c:/*"))

'''
['c:/$Recycle.Bin', 'c:/$WinREAgent', 'c:/AMTAG.BIN', 
'''

print(glob("c:/*.ini"))