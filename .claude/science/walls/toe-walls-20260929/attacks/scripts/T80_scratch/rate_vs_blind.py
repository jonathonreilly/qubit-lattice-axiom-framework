# Block 39 T4: formation rate lambda = z Z_x, Z_x = c^k sum_a prod_{recorded nbrs y} omega(a,s_y).  At c0 = 6/(p+q+4r).
# How much does the c0 rate depend on the neighbours' CONTENTS (T01's blind clause = no dependence at all)?
import itertools
from fractions import Fraction as F
p,q,r=F(3),F(1),F(2); T=p+q+4*r; c0=F(6)/T
ax=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
def om(a,b):
    d=sum(u*v for u,v in zip(ax[a],ax[b])); return p if d==1 else (q if d==-1 else r)
print("triple (3,1,2), c0 =",c0)
for k in range(1,7):
    vals=[]
    avg=F(0); cnt=0
    for cont in itertools.product(range(6),repeat=k):
        Z=c0**k*sum(F(1) if False else __import__('math').prod([om(a,s) for s in cont]) for a in range(6))
        vals.append(Z/6); avg+=Z/6; cnt+=1
    print(f"k={k}: Z/6 min={float(min(vals)):.4f} max={float(max(vals)):.4f} mean over uniform contents={float(avg/cnt):.4f}")
