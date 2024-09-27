# 4-4 프로그램의 입출력 183

# sys1.py
import sys
args = sys.argv[1:]
for i in args:
    print(i)
'''
D:\cmj\workspaces\python> python 4-4-inout-program.py aaa bbb ccc
aaa
bbb
ccc
'''