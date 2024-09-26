#relative 패키지
from game.sound.echo import echo_test
#from ..sound.echo import echo_test
'''
ImportError: attempted relative import with no known parent package
'''
def render_test():
    print('render')
    echo_test()


