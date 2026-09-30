"""Kill-check T53: is the column order (ascending eigenvalue -> nu1,nu2,nu3) a further hidden label? Enumerate all 36 (row perm, col perm)
at the repo pin and test the 9 |U| entries against the repo-quoted NuFIT-6.1-ish angle windows via (s12,s13,s23) 3sigma boxes."""
import numpy as np, itertools, math
from chart import H
pin=(0.657061342210,0.933806343759,0.715042329587)
w,V=np.linalg.eigh(H(*pin)); o=np.argsort(w.real); V=V[:,o]
def angles(P):
    a=abs(P)**2; s13=a[0,2]; c13=1-s13; return a[0,1]/c13, s13, a[1,2]/c13
box=dict(s12=(0.2893,0.3295),s13=(0.02070,0.02420),s23=(0.432,0.587))
for rp in itertools.permutations(range(3)):
    for cp in itertools.permutations(range(3)):
        P=V[list(rp),:][:,list(cp)]
        s12,s13,s23=angles(P)
        ok = box['s12'][0]<=s12<=box['s12'][1] and box['s13'][0]<=s13<=box['s13'][1] and box['s23'][0]<=s23<=box['s23'][1]
        if ok: print('rows',rp,'cols',cp,'(s12,s13,s23)=(%.4f,%.4f,%.4f)'%(s12,s13,s23))
print('done')
