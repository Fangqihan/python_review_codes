# 参考：https://www.cnblogs.com/huchong/p/8244279.html#undefined

# 1、实现一个单例模式

# 1.1
class Singleton(object):
    def __init__(self):
        pass

    @classmethod
    def instance(cls):
        if not hasattr(Singleton, "_instance"):
            Singleton._instance = Singleton()
        return Singleton._instance


if __name__ == '__main__':
    obj1 = Singleton.instance()
    obj2 = Singleton.instance()
    print(id(obj1))
    print(id(obj2))



# 1.2  多线程下存在的问题
class Foo(object):
    def __init__(self):
        import time
        time.sleep(1)  # 注意此处阻塞
        pass

    @classmethod
    def instance(cls):
        if not hasattr(Foo, "_instance"):
            Foo._instance = Foo()
        return Foo._instance


from threading import Thread
def task():
    obj = Foo.instance()
    print(id(obj))


if __name__ == '__main__':
    for i in range(10):
        t = Thread(target=task, args=())
        t.start()

'''
1、init处存在IO阻塞，此单例模式会失效，即无法很好的支持多线程
线程1 开启，调用task(),最终在init处阻塞，时间1s中，后面的9个线程都会在init阻塞，随后逐个调用Foo()实例化
'''



# 1.3、线程安全改进
import threading
class Foo(object):
    instance_lock = threading.Lock()
    def __init__(self):
        import time
        time.sleep(1)
        pass

    @classmethod
    def instance(cls):
        with Foo.instance_lock:
            if not hasattr(Foo, "_instance"):
                Foo._instance = Foo()
        return Foo._instance


def task():
    obj = Foo.instance()
    print(id(obj))


if __name__ == '__main__':
    for i in range(10):
        t = threading.Thread(target=task, args=())
        t.start()
'''
加线程锁，保证Foo._instance完成赋之后才其他线程才开始进入实例化
'''



# 1.4 基于__new__()方法实现单例模式
import threading

class Foo(object):
    instance_lock = threading.Lock()
    def __new__(cls, *args, **kwargs):
        # print(cls)
        with Foo.instance_lock:
            if not hasattr(Foo,'_instance'):
                Foo._instance = object.__new__(cls)  # 默认调用object.__new__()

            return Foo._instance

    def __init__(self):
        import time
        time.sleep(1)
        pass


def task():
    obj = Foo()
    print(id(obj), end='\n')


if __name__ == '__main__':
    for i in range(10):
        t  = threading.Thread(target=task,args=())
        t.start()

