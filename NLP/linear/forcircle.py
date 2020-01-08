import random

def get_data(w, num):
    x = [random.uniform(0,5) for i in range (0, num)]
    y = [w*s for s in x]
    return (x,y)

dic =  get_data(5,2)

print(dic)

print('==============================')
def getXY(data):
    x  = [x for (x,y) in data]
    print('line=',x)
    return x
dic2 = getXY(dic)

print('============================')

def getXYSuare(data,w):
    x = sum([(w*x) for [x,y] in data])
    print(x)

dic3 = getXYSuare(dic,5)