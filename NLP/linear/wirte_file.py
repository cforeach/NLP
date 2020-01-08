
import  random

data = [random.uniform(0,5)*100 for i in range(0,20)]

print(data)

def write_in(path):
    with open(path,'w') as file:
        file.writelines('xxx')


write_in('xxxx.csv')


