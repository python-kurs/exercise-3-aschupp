# utility functions

# Use this file for all functions you create and might want to reuse later.
# Import them in the `main.py` script

def countelem(l:list):
    elem = {}
    for x in l:
        if x in elem.keys():
            elem[x] += 1
        else:
            elem[x] = 1
    return(elem)