# ——*- coding: utf-8 -*-
from datetime import datetime

#不带参装饰器
def log(func):
    def wrapper(*args, **kw):
        print('call {0}(): @ {1}'.format(func.__name__, datetime.now()))
        return func(*args, **kw)
    return wrapper

#带参装饰器
def metric(str1):
    def wrapper1(fn):
        def wrapper2(*args, **kw):
            print('The keyword is {0}'.format(str1))
            print('execute at {0}'.format(datetime.now()))
            return fn(*args, **kw)
        return wrapper2
    return wrapper1

@log
def now():
    pass

@metric('KEYWORD')
def test():
    pass

if __name__ == '__main__':
    # now()
    test()