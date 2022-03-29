#!/bin/python3

import os

basepath="/home/Adrixan/Music"

def clean(path):
    print("Checking %0", path)
    files = os.listdir(path)
    if len(files) == 1 and files[0].endswith("jpg"):
        print("Deleting stale album art")
        os.remove(os.path.join(path, files[0]))
    files = os.listdir(path)
    for f in files:
        if f.startswith('.'):
            continue
        fullpath = os.path.join(path, f)
        if os.path.isdir(fullpath):
            clean(fullpath)
    files = os.listdir(path)
    if len(files) == 0:
        print("Deleting folder")
        os.rmdir(path)
        return


def main():
    files = os.listdir(basepath)
 
    print(files)
    return
    for f in files:
        if f.startswith('.'):
            continue
        fullpath = os.path.join(basepath, f)
        if os.path.isdir(fullpath):
            clean(fullpath)

if __name__ == "__main__":
    main()
