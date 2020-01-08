from sklearn.linear_model import LinearRegression
import numpy as np
def read_data(path):
    with open(path) as file:
        #文件对象？ list
        lines  = file.readlines()
        lines = [eval(line.strip()) for line in lines]
        # 解压为x,y
        x,y = zip(*lines)
        x = np.array(x)
        y = np.array(y)
        return x,y


x_train,y_train = read_data('data/train_data')

model = LinearRegression()

model.fit(x_train,y_train)
# coefficient 系数
print('w = ',model.coef_)
#intercept 截距
print('b = ',model.intercept_)

x_test,y_test = read_data('data/test_data')

y_train_pridict= model.predict(x_train)

from sklearn import  metrics

mse_train =metrics.mean_squared_error(y_train,y_train_pridict)

print('mse_train = ',mse_train)

y_test_pridict = model.predict(x_test)

mse_test = metrics.mean_squared_error(y_test,y_test_pridict)

print('mese_test=',mse_test)

# curve

# train

def curve_data(x, y, y_predict):
    # print('before to list typeof x = ',type(x))
    x = x.tolist()
    # print('after to list typeof x = ',type(x))
    y = y .tolist()
    y_predict = y_predict.tolist()
    results = zip(x, y, y_predict)
    '''
    print('==========================')
    print(list(results))
    print('==========================')
    '''
    results = ['{},{},{}'.format(item[0][0], item[1][0], item[2][0]) for item in results]
    return  results
results = curve_data(x_train, y_train, y_train_pridict)

print('result=', results)


# 把结果写入文件

with open('curve_data.csv','w') as f:
        f.writelines('\n'.join(results))