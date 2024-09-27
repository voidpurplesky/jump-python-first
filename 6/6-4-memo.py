'''
& C:/Python312/python.exe d:/cmj/workspaces/python/6/6-4-memo.py -w "Life is too short"
& C:/Python312/python.exe d:/cmj/workspaces/python/6/6-4-memo.py -r
& C:/Python312/python.exe d:/cmj/workspaces/python/6/6-4-memo.py -a "dddddddddddddddddd"
'''
import sys
option = sys.argv[1]


print(option)



if option == "-w":
    with open('6/6-4-memo.txt', 'w', encoding='utf-8') as f:
        memo = sys.argv[2]
        print(memo)
        f.write(memo)
        f.write('\n')
elif option == "-r":
    with open('6/6-4-memo.txt', 'r', encoding='utf-8') as f:
        memo = f.read()
        print(memo)
elif option == "-a":
    with open('6/6-4-memo.txt', 'a', encoding='utf-8') as f:
        memo = sys.argv[2]
        print(memo)
        f.write(memo)

else:
    print("wrong")
