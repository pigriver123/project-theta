from __future__ import print_function, division

import hashlib
import os
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


def check_hashes(d):
    counter = 0
    all_good = True
    for k, v in d.items():
        digest = generate_file_md5(k)
        if v == digest:
            counter += 1
            # print("The file {0} has the correct hash.".format(k))
        else:
            print("ERROR: The file {0} has the WRONG hash!".format(k))
            all_good = False
    print("There are " + str(counter) + " correct files.")
    return all_good

d = json.load(open("data/hashList.txt"))

if __name__ == "__main__":
    d = json.load(open("data/hashList.txt"))
    check_hashes(d)
