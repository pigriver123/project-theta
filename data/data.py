from __future__ import print_function, division
import os
import hashlib
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


#def make_hash_list(directory, title):
    """
    Returns a list of hashes for each path in directory

    Parameters
    ----------
    directory: the path of the directory you want to make a hash list for
    title: give a title for the hash list, include .txt or .json extension
    
    Returns
    ----------
    Writes a hash list in this directory
    
    ex: make_hash_list("ds005", "temp") makes hashlist for all of ds005
    including subdirectories
    """
    """
    file_paths = []
    for path, subdirs, files in os.walk(directory):
        for name in files:
            file_paths.append(os.path.join(path, name))
    dictionary = {path: generate_file_md5(path) for path in file_paths}
    with open(title, 'w') as outfile:
        json.dump(dictionary, outfile)
    return dictionary
    """

if __name__ == "__main__":
    with open('total_hash.txt', 'r') as hl:
        d = json.load(hl)
    check_hashes(d)
    #with open('new_hashList.txt', 'r') as hl2:
    #    data = json.load(hl2)
    #check_hashes(data)
    #with open('mni_hash.txt', 'r') as hl3:
    #    data = json.load(hl3)
    #check_hashes(data)
