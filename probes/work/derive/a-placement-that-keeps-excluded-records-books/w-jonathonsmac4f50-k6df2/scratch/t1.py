from engine import *
import itertools, time
t=time.time()
dim=2
for excl in ([], [(0,1)]):
    W=Walk(dim,2,excl)
    bad=[]; cnt=0
    maxr=0
    for rx in range(-6,7):
        for ry in range(-6,7):
            for c1 in range(2):
                for c2 in range(2):
                    st=(((rx,ry),c1),((0,0),c2))
                    if excl and not W.allowed(st): continue
                    o=W.O16(1 and {st:(1,0)},0)
                    if o:
                        cnt+=1; maxr=max(maxr,abs(rx),abs(ry))
    print("excl",excl,"nonzero basis cols",cnt,"max |r|inf",maxr, time.time()-t)
