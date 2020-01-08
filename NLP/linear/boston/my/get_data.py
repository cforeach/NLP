from sklearn.datasets import load_boston
import numpy as np
boston = load_boston()

'''
boston.data
@return ndarray n dimension array

'''
data = boston.data
target = boston.target


# data_list =data.tolist()
# print(type(data_list))