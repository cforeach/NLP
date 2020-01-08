import numpy as np

"""np.arange() 
Return a even array within a given interval
====== ======
Starts   5
Types    2
====== ======
    Parameters
    ----------
    array:return an even array within a given interval
    
    array:return an even array within a given start int to the end int and self increase by the given steps
    
    Examples
    --------
    >>>np.arange(3)
    array([1,2,3])
    
    >>>np.arange(3.0)
    array([1.0,2.0,3.0])
    
    >>>np.arange(1,5,2)
    array([1,3,5])
"""
result = np.arange(10)

print(result)

step_result = np.arange(1, 5, 2)
print(step_result)
