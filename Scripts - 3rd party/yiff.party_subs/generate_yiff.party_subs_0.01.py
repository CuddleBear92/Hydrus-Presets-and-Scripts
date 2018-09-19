#!/usr/bin/python

import re
import os
import sys

input_file = './yiff.party_favourites.txt'
template = '[3, "0 yiff.party", 8, [["7b7eafd51fe58946a87f49d502dacc760204d6c0c9a63475e7e143ebb4e21b4a", "yiff.party creator id"], [SUBS_HERE], [52, 1, [1, 86400, 1209600, [1, 2592000]]], 10000, 10000, false, [7, 3, [[true, true, null, null, null, null, null], false, [true, true, true]]], [6, 7, [false, false, [44, 1, []], [], true]], 0, "", true, true, true]]'
sub_template = '[54, 2, ["ID_HERE", true, 0, 0, false, 0, [67, 1, [26, 1, []]], [8, 8, [26, 1, []]]]], '
out_path = './'
combined_out_file = 'yiff.party subscriptions.txt'

def gethex():
    if (sys.version_info < (3, 0)):
        return os.urandom(32).encode('hex')
    else:
        return os.urandom(32).hex()

line = open(input_file,'r').readline().strip()
if line.startswith('['): line = line[1:]
if line.endswith(']'): line = line[:-1]
ids = [i.strip() for i in line.split(',')]
subs_str = ''
for i in ids:
    subs_str = subs_str + sub_template.replace("ID_HERE", i)

combined_outf = open(out_path+'/'+combined_out_file,'w')
combined_outf.write(template.replace("SUBS_HERE",subs_str[:-2]))
combined_outf.flush()
combined_outf.close()
