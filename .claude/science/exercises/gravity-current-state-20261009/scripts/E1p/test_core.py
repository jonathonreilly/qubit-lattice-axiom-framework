import numpy as np, time
from e1p_core import *
rng=np.random.default_rng(1)
P=sprinkle4d_diamond(6.0,rng); N=len(P); print("N",N)
ip,ix=past_links(P)
# brute force
def prec(i,j):
    d=P[j]-P[i]; return d[0]>0 and d[0]**2>d[1]**2+d[2]**2+d[3]**2
C=np.array([[prec(i,j) for j in range(N)] for i in range(N)])  # C[i,j]: i<j
C2=(C.astype(int)@C.astype(int))>0
Lb=C & ~C2
ok=True
for x in range(N):
    s1=set(ix[ip[x]:ip[x+1]]); s2=set(np.where(Lb[:,x])[0])
    if s1!=s2: ok=False; print("mismatch",x); break
print("links match brute force:",ok, "total links",ip[-1])
for T in [12,16,20]:
    P=sprinkle4d_diamond(float(T),rng); t0=time.time(); ip,ix=past_links(P); print(T,len(P),"links",ip[-1],"time %.1fs"%(time.time()-t0))
