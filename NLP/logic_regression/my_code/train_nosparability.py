import numpy as np
import random
from sklearn.linear_model import LogisticRegression

center_label = [[[0, 0], 1], [[1, 1], 1], [[0, 1], 0], [[1, 0], 0]]

sigma = 0.01


def get_data(label, size):
    x_train = []
    y_train = []
    for point, score in label:
        x1, x2 = point
        for i in range(0, size):
            c1 = x1 + random.uniform(-sigma, sigma)
            c2 = x2 + random.uniform(-sigma, sigma)
            x_train.append([c1, c2])
            y_train.append([score])
            # y_train.append(score)
    return x_train, y_train


x_train, y_train = get_data(center_label, 100)
# print('x_train=', x_train[0])
# print(x_train.__len__())
# print('y_train=', y_train)
# print(y_train.__len__())

dimension3_x_train = [data + [data[0] * data[1]] for data in x_train]
'''
np.array() with x_train
1.list类型中的元素可以为任意类型，ndarray必须元素类型一致，否则会强转
2.ndarray有mean,std等内置函数
3.ndarray可以更方便的对多维数组进行运算
'''
# print('before np.array=', dimension3_x_train[0])
# print(type(dimension3_x_train))
dimension3_x_train = np.array(dimension3_x_train)
# print('after np.array=', dimension3_x_train[0])
# print(type(dimension3_x_train))

print('new_x_train=', dimension3_x_train)

'''
train model
'''
model = LogisticRegression(penalty='l2')

model.fit(dimension3_x_train, y_train)

coef = model.coef_
print('coef=', coef)

intercept = model.intercept_
print('intercept=', intercept)
















