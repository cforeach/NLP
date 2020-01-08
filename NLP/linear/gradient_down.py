import random

def get_data (w, num):
    x = [random.uniform(0,5) for i in range(0,num)]
    y = [w*s for s in x ]
    return zip(x,y)


def gradient_down (data,w,rate):
    gradient = sum([(x*w - y)*2*x for [x,y] in data])/data_size
    print('gradient',gradient)
    w = w - rate*gradient
    print('w',w)
    return w

data_size = 3
true_w = 10
fake_w = 5

data = get_data(true_w, data_size)
print(list(data))
for i in range(0,5):
    fake_w = gradient_down(data, fake_w,0.03)





