import os
def get_path(filename):
    base = os.path.dirname(__file__)
    return os.path.join(base, filename)

with open(get_path("names.txt"), 'r') as f:
    '''f.write("Ashu ")
    f.write("chala ")
    f.write("dibaba ")
    f.write("shewa ")
    f.write("alem ")'''
    print(f.readlines())
