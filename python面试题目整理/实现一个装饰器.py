# 普通模式
def outer(f1):
    def inner(*args, **kwargs):
        print('in inner')
        obj = f1(*args, **kwargs)
        return obj
    return inner


@outer
def f1(a,b):
    print('result>>> %s' % (a*b))

'''
f1 = outer(f1) = inner
f1(*args)= inner(*args)
'''

# if __name__ == '__main__':
#     f1(1212,2323)



# 计时器
def timer(fun):
    def inner(*args, **kwargs):
        import time
        start = time.time()
        obj = fun(*args, **kwargs)
        end = time.time()
        print('耗时<%s>' % (end-start))
    return inner


@timer
def f(m):
    sum(range(m))

f(1201212)