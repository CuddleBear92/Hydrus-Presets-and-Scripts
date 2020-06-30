#!/usr/bin/python

import re
import os
import sys

input_file = './boorus1'
template = '[69, "zzz - REPLACEME1@booru.org tag search", 1, ["REPLACEME3", "https://REPLACEME2.booru.org/index.php?page=post&s=list&tags=%tags%", "%tags%", "+", "search tags", "pepe feels"]]'
out_path = './'
combined_out_file = 'all_boorus.org_subdomains.txt'
filename_template = 'zzz_-_REPLACEME1booru.org_tag_search.txt'

def gethex():
    if (sys.version_info < (3, 0)):
        return os.urandom(32).encode('hex')
    else:
        return os.urandom(32).hex()

combined_outf_str = '[26, 1, ['
for booru in open(input_file):
    booru = booru.strip()
    match = re.search('https?://(.*)\\.booru\\.org',booru)
    if len(booru) > 0 and match:
        booru = match.group(1)
        print(booru)
        result = template.replace("REPLACEME1",booru).replace("REPLACEME2",booru).replace("REPLACEME3",gethex())
        filename_result = filename_template.replace("REPLACEME1",booru)
        outf = open(out_path+'/'+filename_result,'w')
        outf.write(result+'\n')
        outf.flush()
        outf.close()
        combined_outf_str += result+', '
combined_outf = open(out_path+'/'+combined_out_file,'w')
combined_outf.write(combined_outf_str[:-2]+']]')
combined_outf.flush()
combined_outf.close()