#!/usr/bin/python

import shutil
import subprocess
import os
import re
import sys
import xml.etree.ElementTree as ET

#ScannerInfo to look for. True or False (example: ExtractCovers)
look_for_keyword = True
extract_keyword="ExtractCovers"
#Blacklist, can be left empty to not write. These should be the same to keep an unified blacklist.
blacklist="/volume1/Comics/Covers/blacklist.txt"
blacklist_out="/volume1/Comics/Covers/blacklist.txt"
p7zip_executable="7z"
#Folder Paths, Temp folder needs to have a folder named `comics_tmp` inside it.
temp_path="/volume1/Comics/Covers"
comics_path="/volume1/Comics/Comics"
out_path="/volume1/Comics/Covers/Extracts"

#Useable PageTypes it can extract
# ["FrontCover","InnerCover","Roundup","Story","Advertisement","Editorial","Letters","Preview","BackCover","Other","Deleted"]
cover_filter = ["FrontCover","InnerCover","BackCover"]
#Usable Keys for filenaming:
#%Year% %Volume% %Series% %Title% %Number% %Count% %PageNum% %PageCount% %CoverType% %FileExt% %Writer% %Publisher% %Genre% %BlackAndWhite% %Manga% %Characters%
fname_template = "%Publisher%/%Series% V%Volume% - %Number%, p%PageNum% %CoverType%%FileExt%"


metadata_tag_list = ['Title', 'Series', 'Number', 'Volume', 'Year', 'Count', 'PageCount', 'Writer', 'Publisher', 'Genre', 'BlackAndWhite', 'Manga', 'Characters', 'ScanInformation']

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

def find_metadata():
    comicinfo = None
    flist = []
    for root, dr, files in os.walk(temp_path+'/comics_tmp'):
        for f in files:
            if f.lower() == "comicinfo.xml":
                comicinfo = ET.parse(root + "/" + f)
            elif re.match(r'.*\.(jpg|png|jpeg|bmp|gif|flif|webp|webm|heif|djvu|tiff|tif)', f.lower()):
                flist.append(root+'/'+f)
    if comicinfo:
        return (comicinfo, sorted(flist))
    return None

def is_archive(fname):
    return len(fname) >= 4 and fname[-4:].lower() in [".zip",".cbz",".cbr",".rar",".7z"]

data = dict()
def extract_metadata(tree):
    global data
    for child in tree:
      if child.tag in metadata_tag_list:
          data[child.tag] = child.text
      if child.tag == 'Page':
          if 'Type' in child.attrib and 'Image' in child.attrib:
              page_entry = [child.attrib['Image'],child.attrib['Type']]
              if '_pages' in data:
                  data['_pages'].append(page_entry)
              else:
                  data['_pages'] = [page_entry]

      extract_metadata(child)

b = []
def write_blacklist():
    if len(blacklist_out) > 0:
        open(blacklist_out,'w').write("\n".join(b))

def copy_file(pagenum, imglist, covertype):
    if pagenum < len(imglist):
        target_fname = fname_template[:]
        for tag in metadata_tag_list:
            target_fname = target_fname.replace("%"+tag+"%", re.sub(r'(\\|/)', ' ', data.get(tag, "")))
        target_fname = target_fname.replace("%PageNum%",str(pagenum))
        target_fname = target_fname.replace("%CoverType%",covertype)
        target_fname = target_fname.replace("%FileExt%",os.path.splitext(imglist[pagenum])[1])
        target_fname = target_fname.split("/")
        if len(target_fname) > 1:
            if not os.path.exists(out_path+"/"+"/".join(target_fname[:-1])):
                os.makedirs(out_path+"/"+"/".join(target_fname[:-1]))
        shutil.copyfile(imglist[pagenum],out_path+"/"+"/".join(target_fname))
        print("Copied file: "+target_fname[-1])
    else:
        print("Image not found for page #"+str(pagenum))
        write_blacklist()
        sys.exit(0)

if os.path.isfile(blacklist):
    f = open(blacklist, 'r')
    for line in f.readlines():
        if len(line.strip()) > 0:
            b.append(line.strip())
    f.close()

for root, dr, files in os.walk(comics_path):
    for f in files:
        if is_archive(f):
            relpath = os.path.relpath(root+'/'+f,comics_path)
            skip = False
            for p in b:
                if p == relpath:
                    skip = True
            if not skip:
                b.append(relpath)
                if extract_data(root+"/"+f):
                    print("Extracted: "+f)
                    metadata = find_metadata()
                    if metadata:
                        print("Metadata found")
                        data = dict()
                        extract_metadata(metadata[0].getroot())
                        if look_for_keyword:
                            if not "ScanInformation" in data:
                                b=b[:-1]
                                continue
                            elif not extract_keyword in data["ScanInformation"]:
                                b=b[:-1]
                                continue
                        if '_pages' in data:
                            for page in data['_pages']:
                                if page[1] in cover_filter:
                                    copy_file(int(page[0]), metadata[1], page[1])
                        else:
                            print("No cover pages found")
                else:
                    print("Can't extract: "+root+"/"+f)
                    write_blacklist()
                    sys.exit(0)
write_blacklist()
