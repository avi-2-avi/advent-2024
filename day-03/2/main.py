import os
import re
doc = open(os.getcwd()+'/input.txt').read().strip()
c = 0

dos = doc.split('do')

def getMulResult(do):
    ce = 0
    muls = do.split('mul')
    for mul in muls:
        # (int,int)
        ok = re.search(r"^\((\d{1,3}),(\d{1,3})\)", mul)
        if ok:
            ls = list(map(int, re.findall(r"\d{1,3}", mul)))
            ce += ls[0]*ls[1]
    return ce

for do in dos:
    print("TO DO PRINT: ", do)
    doer = re.search(r"^\(\)", do)
    if doer or dos[0] == do:
        print("IS DO")
        c += getMulResult(do)

print(c)
