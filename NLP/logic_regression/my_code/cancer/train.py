import numpy as np


def get_data(path):
    with open(path) as f:
        lines = f.readlines()
        lines = [eval(line.strip()) for line in lines]
        x, y = zip(*lines)
        x = np.array(x)
        y = np.array(y)
        return x, y


train_data_x, train_data_y = get_data("data/train_data");
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

test_data_x, test_data_y = get_data("data/test_data");

model = LogisticRegression()

model.fit(train_data_x, train_data_y)

predict_y = model.predict_proba(test_data_x)


def transform_proba2discrete(data):
    result = []
    for line in data:
        x = line[0]
        y = line[1]
        if (x >= 0.5):
            result.append([0])
        else:
            result.append([1])
    return result

tranformed_predict_y = transform_proba2discrete(predict_y)
print('w=', model.coef_)

print('d=', model.intercept_)

print(roc_auc_score(test_data_y, tranformed_predict_y))
