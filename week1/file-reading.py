import os
def get_path(filename):
    base = os.path.dirname(__file__)
    return os.path.join(base, filename)

with open(get_path("namess.txt")) as f:
    #print(f.read())
    #print(f.readline()[2])
    #print(f.readline())
    for lines in f.readlines():
        print(lines)

f.close()