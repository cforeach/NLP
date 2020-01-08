from sklearn.model_selection import  train_test_split
import  numpy as np

"""train_test_split
Split arrays or matrics into random subsets
Parameters
----------
*arrays:sequence or indexble with the same length/shape[0]



 
Example
-------
 
"""

x = np.arange(10).reshape([5,2])
y = np.arange(5).reshape([1,5])
print(x.shape)
print(x.shape[0])

print(len(x)/x.shape[0])

print(len(y)/y.shape[0])

x_train, x_test, y_train, y_test = train_test_split(x,list(range(5)),train_size=0.8)

# print('x_train',x_train)
# print('x_test',x_test)
# print('y_train',y_train)
# print('y_test',y_test)