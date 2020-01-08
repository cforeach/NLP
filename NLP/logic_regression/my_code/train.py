import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import log_loss


def read_data(path):
    with open(path) as file:
        lines = [eval(line.strip()) for line in file.readlines()]
        x, y = zip(*lines)
        print('x====', x)
        print('y====', y)
        x = np.array(x)
        y = np.array(y)
        return x, y


'''
get_data
'''
x_train, y_train = read_data('train_data')

'''
get logic_regression model
'''

model = LogisticRegression()
model.fit(x_train, y_train)

'''
get the intercept and coeficient of the model trained
'''
w0 = model.intercept_
w = model.coef_
print('w=', w)
print('w0=', w0)

'''
Teacher_lu's result
w [[ 1.87177154 -1.9022195 ]]
w0 [0.0340858]

'''

'''
predict the model
'''
x_test, y_test = read_data('test_Data')

y_predict = model.predict_proba(x_test)
# print('y_predict=', y_predict)
# print('y_test=', y_test)
# print('y_predict.shape=', y_predict.shape)
# print('y_test.shape=', y_test.shape)
kl_loss = log_loss(y_test, y_predict)

from sklearn.metrics import roc_auc_score as auc

'''
离散  discrete 
连续  succession
Map the succession probility into discrete value  
'''


def transform_succession2descrete(data):
    result = []
    t = [1]
    t = np.array(t)
    f = [0]
    f = np.array(f)
    for p1, p2 in data:
        if p1 > 0.5:
            result.append(t)
        else:
            result.append(f)
    return result


print('train before trainsform=', y_predict)
train = transform_succession2descrete(y_predict)

print('result ======================================== ', train)
print('type of test', type(y_test))
print('type of train', type(train))

print('test=', y_test)
train = np.array(train)
print('train=', train)
model_auc = auc(y_test, train)
print('auc=', model_auc)
test_data_train = [1, 0, 1, 0]
test_data_test = [1, 0, 0, 0]
auc2 = auc(test_data_test, test_data_train)
print('auc2=', auc2)
print('kl_loss=', kl_loss)
