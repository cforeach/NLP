from math import log

def get_gain_ratio(V):
    if(V == 0):
        part1=0
        part2=0
    else:
        part1 = V/17
        part2 = log(part1,2)
    return part2

data_size = 17
s = (-1)*(get_gain_ratio(12)+get_gain_ratio(5))
# print(s)

hard_size = 12
hard_rate = 12/17
ratio_hard = (hard_rate)*(log(hard_rate,2))
print(ratio_hard)

other_size = 5
other_rate = 5/17
other_ratio = (other_rate)*(log(other_size,2))
print(other_rate)