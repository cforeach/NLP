import numpy as np


def read_data(path):
    with open(path) as data:
        lines = data.readlines()
        lines_eval = [eval(line.strip()) for line in lines]
        lines_without_eval = [line.strip() for line in lines]
        print('lines_without_eval=',lines_without_eval)
        print('lines_eval=',lines_eval)

        # x = data[0]
        # print('x=',x)
        # x, y, z= zip(*lines)
        # x = np.array(x)
        # y = np.array(y)
        # z = np.array(z)
        # print('x=', x)
        # print('y=', y)
        # print('z=', z)

read_data('rubish_data');
