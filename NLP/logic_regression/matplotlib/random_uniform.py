import random
from matplotlib import pyplot as plt

sigma = 0.01
x = [random.uniform(-sigma, sigma) for num in range(0, 30)]
# print('x')
# print(x)
# print('===================')

'''
split utils
'''


def get_axis_xy(data):
    x = [line[0] for line in data]
    y = [line[1] for line in data]
    return x, y


'''
step2 return the point added the random num
'''

label = [[0, 0], [0, 1], [1, 0], [1, 1]]


def get_data(label):
    x = [data[0] for data in label]
    y = [data[1] for data in label]
    return x, y


x, y = get_data(label)
# print(x)
# print(y)

'''
get final data
'''


def get_random_point(label, point_num):
    result = []
    for i in range(0, point_num):
        for line in label:
            c1 = line[0] + random.uniform(-sigma, sigma)
            c2 = line[1] + random.uniform(-sigma, sigma)
            result.append([c1, c2])
    return result


data = get_random_point(label, 20)
print('data of get_random_point = ', data)
print(data.__len__())
print('===================')
x1, y1 = get_axis_xy(data)

plt.scatter(x1, y1)
plt.show()



'''
try to first circle the label
'''


def get_random_point2(label, point_num):
    result = []
    for line in label:
        cl_1 = line[0]
        cl_2 = line[1]
        for i in range(0, point_num):
            print('cl1=', cl_1)
            print('cl2=', cl_2)
            x = cl_1 + random.uniform(-sigma, sigma)
            y = cl_2 + random.uniform(-sigma, sigma)
            print('x=', x)
            print('y=', y)
            result.append([x, y])
            print('result in the circle=', result)
    return result


result = get_random_point2(label, 4)
print('outside result = ', result)

'''
get the axis x , and the axis y of the data
'''

axis_x, axis_y = get_axis_xy(result)
print('axis_x=', axis_x)
print('axis_y=', axis_y)
'''
show by plt
'''

plt.scatter(axis_x, axis_y)
plt.show()
