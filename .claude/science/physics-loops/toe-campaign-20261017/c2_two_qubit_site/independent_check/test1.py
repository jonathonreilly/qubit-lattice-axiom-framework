from polytools import *
CH=(0,1,1,3,3,2,2)
D_ex=(0,)+tuple(l|(1<<2) for l in CH[1:])  # spin chamon x flavour X on neighbours
print(name(D_ex))
for nm,rule in [('chamon',[CH]),('Dex',[D_ex])]:
    r=analyse(rule,nm); print(nm,r['ext3zero'],r['local_logicals'])
