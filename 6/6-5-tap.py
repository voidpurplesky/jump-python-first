# 6.5 탭문자를 공백문자 4개로 바꾸기
'''

python d:/cmj/workspaces/python/6/6-5-tap.py 6-5-tab.txt 6-5-space.txt
'''

import sys

src = sys.argv[1]
dst = sys.argv[2]

print(src)
print(dst)
print('6/'+src)
with open('6/'+src, 'r', encoding='utf-8') as f:
    tab_content = f.read()
    print(tab_content)
    space_content = tab_content.replace("\t", " " * 4)
    print(space_content)