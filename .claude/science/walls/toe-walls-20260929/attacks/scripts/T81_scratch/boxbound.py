"""R2 probe: eta' in an LxL box with ALL-ONES outside (worst-case monotone boundary).  A finite-window rigorous
bound would have to certify a density here.  Reports late-time mean density in the box and in its central quarter."""
import numpy as np
from sim import d123
def run(p,L,T,seed,q=1.0,r=2.0):
    rng=np.random.default_rng(seed); d1,d2,d3=d123(p,q,r); e1=d1; e2=max(d2,d3)
    s=np.zeros((L,L),dtype=np.int8); acc=[]; 
    for n in range(1,T+1):
        a=np.ones((L,L),dtype=np.int8); a[1:,:]=s[:-1,:]      # (i-1,j), outside=1
        b=np.ones((L,L),dtype=np.int8); b[:,1:]=s[:,:-1]      # (i,j-1), outside=1
        cnt=a+b+s
        u=rng.random((L,L))
        s=np.where(cnt>=2,1,np.where(cnt==1,(u<e2),(u<e1))).astype(np.int8)
        if n>T//2: acc.append((s.mean(), s[L//4:3*L//4,L//4:3*L//4].mean()))
    acc=np.array(acc); return acc.mean(0)
for p in (25,30,40,60,84,150):
    row=[]
    for L in (8,16,32,64):
        m=run(p,L,3000,1)
        row.append("L=%d all=%.3f core=%.3f"%(L,m[0],m[1]))
    print("p=%g"%p," | ".join(row))
