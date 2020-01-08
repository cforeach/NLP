

import  random

def get_Data(w, num):
    x = [random.uniform(0,5) for i in range(0, num)]
    y = [w*x]
    return zip(x,y)

dic = get_Data(5,5)

a = ["a" , "b" , "c"]
b = ["d", "c" , "e"]
zipped = zip(a, b)

print(list(zipped))