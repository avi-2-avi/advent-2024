import os
import re
doc = open(os.getcwd()+'/input.txt').read().strip()
c = 0

muls = doc.split('mul')
for mul in muls:
    # (int,int)
    print(mul)
    ok = re.search(r"^\((\d{1,3}),(\d{1,3})\)", mul)
    if ok:
        ls = list(map(int, re.findall(r"\d{1,3}", mul)))
        c += ls[0]*ls[1]
print(c)
