#!/usr/bin/python

import shutil
import subprocess
import os
import re
import sys
import xml.etree.ElementTree as ET

p7zip_executable="7z"
#Folder Paths, Temp folder needs to have a folder named `comics_tmp` inside it.
templatename="PublisherName"
outfile=templatename+".cbl"
temp_path="/volume1/Comics/tmp"
comics_path="/volume1/Comics/Comics/"+templatename

xml_template = """<?xml version="1.0"?>
<ReadingList xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <Name>WebP Processing %PLACEHOLDER%</Name>
  <Books>
%BOOKS%
  </Books>
  <Matchers />
</ReadingList>
"""

book_entry_template = """
    <Book>
      <FileName>%FILENAME%</FileName>
    </Book>
"""

def is_archive(fname):
    return len(fname) >= 4 and fname[-4:].lower() in [".zip",".cbz",".cbr",".rar",".7z"]

def find_non_webp():
    for root, dr, files in os.walk(temp_path+'/comics_tmp'):
        for f in files:
            if re.match(r'.*\.(jpg|png|jpeg|bmp|gif|flif|heif|djvu|tiff|tif)', f.lower()):
                return True
    return False

def extract_data(fname):
    try:
        shutil.rmtree(temp_path+'/comics_tmp')
    except IOError:
        pass
    os.makedirs(temp_path+'/comics_tmp')
    try:
        FNULL = open(os.devnull, 'w')
        subprocess.call([p7zip_executable, "x", fname, "-o"+temp_path+"/comics_tmp"], stdout=FNULL, stderr=subprocess.STDOUT)
        return True
    except:
        return False

books=""
for root, dr, files in os.walk(comics_path):
    for f in files:
        basename = os.path.basename(f)
        if is_archive(f):
            relpath = os.path.relpath(root+'/'+f,comics_path)
            if extract_data(root+"/"+f):
                 #print("Extracted: "+f)
                 if find_non_webp():
                     books += book_entry_template.replace("%FILENAME%",basename[:basename.rindex(".")])
            else:
                 print("Can't extract: "+root+"/"+f)

open(outfile,"w").write(xml_template.replace("%BOOKS%",books).replace("%PLACEHOLDER%",templatename))
