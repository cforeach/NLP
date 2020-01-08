import  numpy as np

"""
np.reshape
Return the array with new shape, x rows, y columns

Parameters
----------
    [x, y]:x the rows, y the columns

Examples
--------
    >>>np.arange(8).reshape([4,2])
    np.array([[x,y][x,y][x,y][x,y]])

"""
array = np.arange(8)
metrix = array.reshape([4, 2])

print(metrix)