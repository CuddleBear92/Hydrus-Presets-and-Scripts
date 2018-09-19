#!/usr/bin/python

import re
import os
import sys

input_file = './yiff.party favourites.txt'
template = '[3, "0 yiff.party", 8, ["REPLACEME2", "yiff.party creator id"], [[54, 2, ["REPLACE1", true, 0, 0, false, 0, [67, 1, [26, 1, []]], [8, 8, [26, 1, []]]]]]]'
out_path = './'
combined_out_file = 'yiff.party subscriptions.txt'
filename_template = 'zzz_-_REPLACEME1booru.org_tag_search.txt'

def gethex():
    if (sys.version_info < (3, 0)):
        return os.urandom(32).encode('hex')
    else:
        return os.urandom(32).hex()

combined_outf_str = '[3, "0 yiff.party", 8, ['
for id in open(input_file):
    id = id.strip()
    match = re.search('\d{2,12}',id)
    if len(id) > 0 and match:
        id = match.group(1)
        print(id)
        result = template.replace("REPLACEME1",id).replace("REPLACEME2",gethex())
        filename_result = filename_template.replace("REPLACEME1",id)
        outf = open(out_path+'/'+filename_result,'w')
        outf.write(result+'\n')
        outf.flush()
        outf.close()
        combined_outf_str += result+', '
combined_outf = open(out_path+'/'+combined_out_file,'w')
combined_outf.write(combined_outf_str[:-2]+']]')
combined_outf.flush()
combined_outf.close()