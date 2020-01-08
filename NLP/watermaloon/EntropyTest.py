import EntropyGain

root_curl_pt = 5 / 8
root_curl_size = 8
root_curl_ent = EntropyGain.get_ent(root_curl_pt)
# print('root_curl_ent=', root_curl_ent)

root_litle_pt = 3 / 7
root_litle_size = 7
root_litle_ent = EntropyGain.get_ent(root_litle_pt)
# print('root_litle_ent=', root_litle_ent)

root_hard_pt = 0
root_hard_size = 2
root_hard_ent = EntropyGain.get_ent(root_hard_pt)
# print('root_hard_ent=', root_hard_ent)

data_size = 17
base_ent = 0.998
ent_arr = [(root_curl_size, root_curl_ent), (root_litle_ent, root_litle_size), (root_hard_ent, root_curl_size)]

root_gain = EntropyGain.get_gain_ent(ent_arr, base_ent, data_size)
# print('root_gain=', root_gain)

ubilical_trapped_pt = 5 / 7
ubilical_trapped_size = 7


ubilical_trappedc_ent = EntropyGain.get_ent(ubilical_trapped_pt)
print('ubilical_trappedc_ent=',ubilical_trappedc_ent)

ubilical_little_pt = 1 / 2
ubilical_little_size = 6
ubilical_little_ent = EntropyGain.get_ent(ubilical_little_pt)
print('ubilical_little_ent=',ubilical_little_ent)

ublilical_flat_pt = 0
ubilical_flat_size = 4
ublical_flat_ent = EntropyGain.get_ent(ublilical_flat_pt)
print('ublical_flat_ent=',ublical_flat_ent)

ubilcal_arr = [(ubilical_trappedc_ent, ubilical_trapped_size), (ubilical_little_ent, ubilical_little_size),
               (ublical_flat_ent, ubilical_flat_size)]

ubilical_gain = EntropyGain.get_gain_ent(ubilcal_arr, base_ent, data_size)
print('ubilical_gain=', ubilical_gain)
