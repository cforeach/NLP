from math import log

'''
p:possibilty
'''


def get_ent(p):
    if (p == 0):
        left = 0
        right = 1
    else:
        left = p * log(p, 2)
        right = (1 - p) * log((1 - p), 2)
    result = -1 * (left + right)
    return result


'''
ent_arr: [(x,y)],x=entropy,y=sample_size
base_ent: 
data_size: data's length
'''


def get_gain_ent(ent_arr, base_ent, data_size):
    dif = sum([x*y for [x, y] in ent_arr])/data_size
    # print('dif=', dif)
    # print('base_ent=', base_ent)
    return base_ent - dif
