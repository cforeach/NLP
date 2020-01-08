import get_ent as ent
import get_gain_ent as gain

'''
curled quansuo
'''
curled_prob = 5/8
curled_size = 8
curled_ent = ent.get_ent(curled_prob)
'''
littlecurled 
'''
littlecurled_prob = 3/7
littlecurled_size = 7
littlecurled_ent = ent.get_ent(littlecurled_prob)
'''
hard yingting
'''
hard_prob = 0
hard_size = 2
hard_ent = ent.get_ent(hard_prob)

ent_array = [(curled_ent,curled_size),(littlecurled_ent,littlecurled_size),(hard_ent,hard_size)]

root_gain = gain.get_gain(ent_array)
print('root gain = ',root_gain)


