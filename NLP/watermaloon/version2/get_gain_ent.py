from math import log
"""
Parameters:
-----------
    array:
        Example:
        array:[(x1_ent_,y1_size),(x2,y2),(x3,y3)]
"""
def get_gain(array):
    result = sum([ent*size/17  for [ent,size] in array])
    return 0.998 - result

def get_gain_withp(array,data_size,base_ent):
    result = sum([ent * size / data_size for [ent, size] in array])
    return base_ent - result