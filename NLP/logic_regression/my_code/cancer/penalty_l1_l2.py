import numpy as np
from sklearn.linear_model import LogisticRegression


def get_data(path):
    with open(path) as f:
        lines = f.readlines()
        line = [eval(line.strip()) for line in lines]
        x, y = zip(*line)
        # transform yuanzu to ndarray
        print(type(x))
        x = np.array(x)
        y = np.array(y)
        return x, y


train_x, train_y = get_data("data/train_data")
test_x, test_y = get_data("data/test_data")
from sklearn.metrics import mean_squared_error as mse


def train_data(reg):
    model = LogisticRegression(penalty=reg)
    model.fit(train_x, train_y)
    return model


model_l1 = train_data("l1")
model_l2 = train_data("l2")

predict_y_l1 = model_l1.predict(test_x)
predict_y_l2 = model_l2.predict(test_x)

mse_l1 = mse(test_y, predict_y_l1)
mse_l2 = mse(test_y, predict_y_l2)

print('l1-mse=', mse_l1)
print('l1 coef={}'.format(model_l1.coef_))
print('l2-mse=', mse_l2)
print('l2-coef={}'.format(model_l2.coef_))
