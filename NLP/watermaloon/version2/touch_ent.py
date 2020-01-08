import get_ent as ent
import get_gain_ent as gain

'''
touch hard
'''
touch_hard_size = 12
touch_hard_prob = 1/2
touch_hard_ent = ent.get_ent(touch_hard_prob)
'''
touch soft
'''
touch_soft_size = 5
touch_soft_prob = 2/5
touch_soft_ent = ent.get_ent(touch_soft_prob)
'''
touch_ent_array
'''

touch_ent_arrary = [(touch_hard_ent, touch_hard_size),(touch_soft_ent,touch_soft_size)]
touch_gain = gain.get_gain(touch_ent_arrary)
print('touch_gain=',touch_gain)
