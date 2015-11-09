from __future__ import print_function, division
import os
<<<<<<< HEAD
=======
import hashlib
import json
>>>>>>> 20a3b16e852d9587c544d6b078c663717e0a8e6f


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
            # print("The file {0} has the correct hash.".format(k))
        else:
            print("ERROR: The file {0} has the WRONG hash!".format(k))
            all_good = False
    print("There are " + str(counter) + " correct files.")
    return all_good


if __name__ == "__main__":
<<<<<<< HEAD
    d = json.load(open("hashList.txt"))
=======
    with open('hashList.txt', 'r') as hl:
        d = json.load(hl)
>>>>>>> 20a3b16e852d9587c544d6b078c663717e0a8e6f
    check_hashes(d)
