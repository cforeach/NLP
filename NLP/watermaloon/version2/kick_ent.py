import get_ent as ent
import get_gain_ent as gain

right_gain = 0.141

'''
dark
'''
dark_size = 10
dark_prob = 6/10
dark_ent = ent.get_ent(dark_prob)
print(dark_ent)
'''
heavy
'''
heavy_size = 5
heavy_prob = 2/5
heavy_ent = ent.get_ent(heavy_prob)
'''
clear
'''
clear_size = 2
clear_prob = 0
clear_ent = ent.get_ent(clear_prob)
'''
ent_array
'''
ent_array = [(dark_ent,dark_size),(heavy_ent,heavy_size),(clear_ent,clear_size)]
'''
kick_gain
'''
kick_gain = gain.get_gain(ent_array)
print('kick_gain=',kick_gain)

print((dark_ent*15+clear_ent*clear_size)/17)