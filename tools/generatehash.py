from __future__ import print_function, division

import hashlib
import os
import os.path
import json

def generate_file_md5(filename, blocksize=2**20):
    m = hashlib.md5()
    with open(filename, "rb") as f:
        while True:
            buf = f.read(blocksize)
            if not buf:
                break
            m.update(buf)
    return m.hexdigest()

d = {}

rootDir = 'ds005'

for dirName, subdirList, fileList in os.walk(rootDir):
    # print('Found directory: %s' % dirName)
    for fname in fileList:
        a = os.path.join(dirName, fname)
        d[a] = generate_file_md5(a, blocksize=2**20)


json.dump(d, open("hashList.txt",'w'))

