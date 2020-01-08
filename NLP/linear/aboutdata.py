import random

def getData(w, num):
    x = [random.uniform(0,5) for i in range(0,num)]
    y = [w*x]
    return (x,y)

def get_data2(w,num):
	x=[ random.uniform(0,5) for  i in range(0,num)]
	y=[ w*s for s in x]
	return zip(x,y)

dic1 = getData(5,5)
dic2 = get_data2(5,5)
print(dic1)


print(dic2)



#for i in range(0,10):
#x = random.uniform(0,5)
#print(x)