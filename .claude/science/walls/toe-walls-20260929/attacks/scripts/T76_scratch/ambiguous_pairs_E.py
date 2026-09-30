import sys, collections
import reachE_fast as F, reachE as R
L=int(sys.argv[1])
fs=F.frozen_all(L); nbs=R.make(L); memo={}
rs=[rows for rows in fs if R.reachable(rows,L,nbs,memo)]
g=collections.defaultdict(list)
for rows in rs:
    key=tuple((rows[r]>>q)&1 for r in range(L) for q in range(L) if min(r,q,L-1-r,L-1-q)<1)
    g[key].append(rows)
amb=[v for v in g.values() if len(v)>1]
print("L",L,"reachable",len(rs),"depth-1 shells",len(g),"ambiguous shells",len(amb))
def show(a,b):
    for r in range(L):
        print("".join(("#" if (a[r]>>q)&1 else ".") for q in range(L)),"  ","".join(("#" if (b[r]>>q)&1 else ".") for q in range(L)),"  ","".join(("X" if ((a[r]^b[r])>>q)&1 else ".") for q in range(L)))
    print()
for v in amb[:6]:
    a,b=v[0],v[1]
    diff=[(r,q) for r in range(L) for q in range(L) if ((a[r]^b[r])>>q)&1]
    print("diff size",len(diff),"rows",sorted({r for r,q in diff}),"cols",sorted({q for r,q in diff}))
    show(a,b)
