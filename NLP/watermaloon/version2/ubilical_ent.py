import get_ent as ent
import get_gain_ent as gain

'''
sunk  aoxian
'''
sunk_prob = 5/7
sunk_size = 7
sunk_ent = ent.get_ent(sunk_prob)
'''
littlesunk
'''
littlesunk_prob = 3/6
littlesunk_size = 6
littlesunk_ent = ent.get_ent(littlesunk_prob)
'''
flat ping
'''
flat_prob = 0
flat_size = 4
flat_ent = ent.get_ent(flat_prob)


'''
ent_array
'''
ent_array = [(sunk_ent,sunk_size),(littlesunk_ent,littlesunk_size),(flat_ent,flat_size)]
'''
gain_ent
'''
gain_ent = gain.get_gain(ent_array)

print('ubilical gain ent = ',gain_ent)
