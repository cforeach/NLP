'''
主要用途：
    1.字符串填充内容
    2.数字格式化
'''

'''
    =========   
    字符串处理
'''

'''
{}{}.formate(arg1,arg2)
'''
print("aaaa{0},aaaa{1}".format("bbb", "ccc"))

'''
通过设定指定位置，输出元素
{i},{j},{}
'''
print('{2}{1}{0}'.format('before', 'middle', 'after'))

'''
通过字典设置参数
({key},{key}).formate(**dic)
'''
dic = {"name": "PeterSong", "hobey": "Python"}
print('姓名：{name},爱好:{hobey}'.format(**dic))


'''
通过列表索引
'''
list = ['元素1', '元素2']
print('元素1={0[0]},元素1={0[1]}'.format(list))




'''
    =========
    数字格式化
'''

from math import pi

print('Before str.format, the pi={}'.format(pi))

print('After the str.formate, the pi={}'.format(pi))