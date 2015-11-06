from __future__ import print_function, division

import hashlib
import os
import json


<<<<<<< HEAD
d = {'ds005_raw.tgz': "ab475fb09b300744548493394764f50e"}
=======
d = json.load(open("data/hashList.txt"))
>>>>>>> a96098ccbb47c304f972e54f9161165806dc04f1


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
    all_good = True
    counter = 0
    for k, v in d.items():
        digest = generate_file_md5(k)
        if v == digest:
            counter += 1
            #print("The file {0} has the correct hash.".format(k))
        else:
            print("ERROR: The file {0} has the WRONG hash!".format(k))
            all_good = False
    print("There are " + str(counter) + " correct files.")
    return all_good


if __name__ == "__main__":
    check_hashes(d)
