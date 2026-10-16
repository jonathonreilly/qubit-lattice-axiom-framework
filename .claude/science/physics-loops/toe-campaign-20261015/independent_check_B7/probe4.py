import numpy as np
from walks import *
from part2_cone import Q, quat
rng=np.random.default_rng(3)
def deg_profile(qA,qB,nk=200):
    A = two_layer(qA.astype(complex), qB.astype(complex))
    gaps=[]; sym=[]
    for k in rng.uniform(-np.pi,np.pi,(nk,3)):
        p=np.sort(np.mod(-np.angle(np.linalg.eigvals(symbol(A,k))),2*np.pi))
        gaps.append(np.diff(np.concatenate([p,[p[0]+2*np.pi]])).min())
        q=np.sort(np.mod(-p,2*np.pi)); sym.append(np.abs(np.sort(p)-q).max())
    return np.min(gaps), np.max(sym)
a=b=np.pi/4
print("special a=b=pi/4 (K, S1):", deg_profile(np.cos(a)*np.eye(8)+np.sin(a)*Q[0], np.cos(b)*np.eye(8)+np.sin(b)*Q[1]))
for t in range(3):
    qA=quat(rng.normal(size=4)); qB=quat(rng.normal(size=4))
    print("random:", deg_profile(qA,qB))
for t in range(3):
    x=rng.normal(size=3); y=rng.normal(size=3)
    qA=quat([x[0],x[1],0,0]); qB=quat([y[0],0,y[1],y[2]])
    print("qA in span(I,K), qB generic:", deg_profile(qA,qB))
