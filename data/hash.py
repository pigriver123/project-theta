from __future__ import print_function, division

import hashlib
import os
import os.path
import os
import json

import data

d = {}

rootDir = 'ds005'

for dirName, subdirList, fileList in os.walk(rootDir):
    # print('Found directory: %s' % dirName)
    for fname in fileList:
        a = os.path.join(dirName, fname)
        d[a] = data.generate_file_md5(a, blocksize=2**20)


json.dump(d, open("hashList.txt",'w'))