from sklearn import metrics

'''
__name__是python中的一个内置属性，是一个字符串
1.如果是引入的模块，就是模块名字
2.如果是当前执行程序的名字， __name__就是__main__
'''
print('metrics __class__ = ', metrics.__name__)
print(__name__)


class test_class:
    print('THIS IS MY TEST CLASS')


print('__class__', test_class.__class__)

array = []

print(' array __class__', array.__class__)

import numpy as np

np_array = np.arange(10)

print(' np_array __class__', np_array.__class__)

'''
sth about the conception of python class
'''


class my_init():
    static_array = [6, 6, 6, 6, 6, 6]

    def __init__(self):
        print()


my_init_a = my_init()
print(my_init_a.static_array)
