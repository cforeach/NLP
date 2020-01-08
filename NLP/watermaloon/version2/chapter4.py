import get_ent as ent
import get_gain_ent as gain

root_ent = 0.998

color_gain = 0.108
kick_gain = 0.141
texture_gain = 0.381
touch_gain = 0.006
root_gain = 0.143
ubilical_gain = 0.289

root_max_ent = texture_gain
def show_split(str1, str2):
    print('=========================================')
    print('     ',str1,str2)
    # print('===================  ===================')
'''
Obvirsily the Texture figure is the max info welfare,so choise it as the division property or demision
'''
texture_clear_id = [1, 2, 3, 4, 5, 6, 8, 10, 15]
texture_clear_size = 9
base_size = texture_clear_size
'''
t-color-green
'''
t_color_green_prob = 3/4
t_color_green_size = 4
t_color_green_ent = ent.get_ent(t_color_green_prob)
'''
t_color-dark
'''
t_color_dark_size = 4
t_color_dark_prob = 3/4
t_color_dark_ent = ent.get_ent(t_color_dark_prob)
'''
white
'''
t_color_white_size = 1
t_color_white_prob = 1
t_color_white_ent = ent.get_ent(t_color_white_prob)
'''
color_ent array
'''
ent_array_color = [(t_color_green_ent,t_color_green_size),(t_color_dark_ent,t_color_dark_size),(t_color_white_ent,t_color_white_size)]
'''
t_color_gain
'''
color_cluster_size = t_color_dark_size + t_color_white_size + t_color_green_size

'''
color-base-ent
'''
base_ent_color = ent.get_ent(7/9)
base_ent = base_ent_color
t_color_gain = gain.get_gain_withp(ent_array_color,color_cluster_size,base_ent_color)


show_split('t_color_gain=',t_color_gain);

'''
t_root
'''
'''
t_root_curled
'''

t_root_curled_size = 5
t_root_curled_prob = 1
t_root_curled_ent = ent.get_ent(t_root_curled_prob)
'''
little_curled
'''
t_root_lcurled_size = 3
t_root_lcurled_prob = 2/3
t_root_lcurled_ent = ent.get_ent(t_root_lcurled_prob)
'''
hard
'''
t_root_hard_size = 1
t_root_hard_prob = 0
t_root_hard_ent = ent.get_ent(t_root_hard_prob)
'''
ent_array_curled
'''
ent_array_curled = [(t_root_curled_ent,t_root_curled_size),(t_root_lcurled_ent,t_root_lcurled_size),(t_root_hard_ent,t_root_hard_size)]
'''
curled_gain
'''
root_gain = gain.get_gain_withp(ent_array_curled,base_size,base_ent)
show_split('root_gain=',root_gain)

'''
kick
'''
'''
kick_mud
'''
t_kick_mud_size = 6
t_kick_mud_prob = 5/6
t_kick_mud_ent = ent.get_ent(t_kick_mud_prob)
'''
heavy
'''
t_kick_heavy_size = 2
t_kick_heavy_prob = 1
t_kick_heavy_ent = ent.get_ent(t_kick_heavy_prob)
'''
clear
'''
t_kick_clear_size = 1
t_kick_clear_prob = 0
t_kick_clear_ent = ent.get_ent(t_kick_clear_prob)
'''
ent arry
'''
ent_array_kick = [(t_kick_mud_ent,t_kick_mud_size),(t_kick_heavy_ent,t_kick_heavy_size),(t_kick_clear_ent,t_kick_clear_size)]
'''
kick_gain
'''
kick_gain = gain.get_gain_withp(ent_array_kick,base_size,base_ent)

show_split('kick_gain=',kick_gain)























texture_littlefuzzy_id = [7, 9, 13, 14, 17]
texture_littlefuzzy_size = 5

texture_fuzzy_id = [11, 12, 16]
texture_fuzzy_size = 3

