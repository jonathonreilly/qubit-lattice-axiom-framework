import sys
from covariant2d import find, NAMES
R=[NAMES.index(x) for x in sys.argv[1].split(",")]
for sh in [tuple(int(x) for x in s.split("x")) for s in sys.argv[2].split(",")]:
    g,lv,unk,cp=find(sh[0],sh[1],R,cap=2000000,budget=100000)
    print(sys.argv[1],sh,"good",len(g),"leaves",lv,"unknown",unk,"capped",cp,flush=True)
    if len(g)>=2: break
