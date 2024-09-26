from game.sound.echo import echo_test

echo_test()

from game import VERSION, print_version_info, render_test
print(VERSION)
print_version_info()


# 패키지 내 모듈을 미리 import < game/__init__.py 

render_test()


'''
Initializing game...
echo
3.5
The version of this game is 3.5.
render
'''

