import get_ent as ent
import get_gain_ent as gain

'''
clear
'''
clear_prob = 7/9
clear_size = 9
clear_ent = ent.get_ent(clear_prob)
'''
littlefuzzy
'''
littlefuzzy_prob = 1/5
littlefuzzy_size = 5
littlefuzzy_ent = ent.get_ent(littlefuzzy_prob)
'''
fuzzy
'''
fuzzy_prob = 0
fuzzy_size = 3
fuzzy_ent = ent.get_ent(fuzzy_prob)

'''
ent arrary
'''
ent_array = [(clear_ent,clear_size),(littlefuzzy_ent,littlefuzzy_size),(fuzzy_ent,fuzzy_size)]
'''
ent_gain
'''
ent_gain = gain.get_gain(ent_array)

print('texture gain=',ent_gain)


