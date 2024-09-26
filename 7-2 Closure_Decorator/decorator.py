from time import time

def elapsed(original_func):
    def wrapper(*args, **kwargs):
        start = time()
        result = original_func(*args, **kwargs)
        end = time()
        print("함수수행시간: %f초" % (end-start))
        return result 
    return wrapper

@elapsed
def myfunc(msg):
    print("힘수가 실행됩니다.")
    print("'%s'을 출력합니다." % msg)

#decorated_myfunc = elapsed(myfunc)
#decorated_myfunc()
#myfunc()
myfunc("You need python")
