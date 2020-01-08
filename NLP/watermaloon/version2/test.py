import get_ent as ent_tool
from math import log
import get_gain_ent as gain_ent_tool
p1 = 3/6
p2 = 2/3
p3 = 1/5

ent_p1 = ent_tool.get_ent(p1)
ent_p2 = ent_tool.get_ent(p2)
ent_p3 = ent_tool.get_ent(p3)

test_array = [(ent_p1,6),(ent_p2,6),(ent_p3,5)]
data_size = 17
test_gain = gain_ent_tool.get_gain(test_array)
print('test_gain',test_gain)