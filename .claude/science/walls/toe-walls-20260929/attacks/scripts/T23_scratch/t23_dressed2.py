import itertools, numpy as np
from collections import Counter
src=open('t23_dressed.py').read().split("rec=[]")[0]
exec(src)
rec=[]
for (p,s,M) in G:
    if det(M)!=1: continue
    U=site_unitary(M); res=find_dressing(U)
    eps,S_=res; R8=V.T@(S_@U)@V
    rec.append((M,order(M),R8))
def eigs(R): 
    w=np.linalg.eigvals(R); return sorted(Counter(np.round(np.angle(w)/(2*np.pi)*12).astype(int)%12).items())
for name,o in [("C2 axis",2),("C3",3),("C4",4)]:
    M,_,R8=[r for r in rec if r[1]==o][0]
    print(name,"dressed eigenphases (units of 2pi/12) on the 8-dim kernel:",eigs(R8),"| trace",np.round(np.trace(R8),6))
# classes: traces of all 24 dressed proper rotations by element order and axis type
tr=Counter()
for M,o,R8 in rec:
    kind={1:"E",3:"C3"}.get(o)
    if o==2: kind="C2axis" if np.count_nonzero(M-np.diag(np.diag(M)))==0 else "C2face-diag"
    if o==4: kind="C4"
    tr[(kind,round(np.trace(R8).real,6))]+=1
print("trace by class:",dict(tr))
