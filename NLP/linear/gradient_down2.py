import  random

def get_data(w, num):
    x = [random.uniform(0, 5) for x in range(0, num)]
    y = [(var*w) for var in x]
    return zip(x, y)

real_w =10
fake_w = 7
rate = 0.02
data_size = 10
dic = get_data(real_w, data_size)

def gradient_step(data, fake_w, rate):
    gradient = sum([(fake_w*x - y)*2*x for [x, y] in data])/data_size
    print gradient
    fake_w = fake_w - gradient*rate
    print 'fake_w=', fake_w
    return fake_w


for i in range(0,100):
    fake_w=gradient_step(dic, fake_w, rate)

print 'After traning fake_w:', fake_w



