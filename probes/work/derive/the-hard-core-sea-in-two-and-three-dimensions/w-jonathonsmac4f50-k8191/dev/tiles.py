import numpy as np, itertools, time, sys
from lib import *
def patch(shape, base=None):
    d=len(shape); sites=list(itertools.product(*[range(L) for L in shape][::-1]))
    sites=[s[::-1] for s in sites]
    if base is None: base=(0,)*d
    idx={s:i for i,s in enumerate(sites)}
    bonds=[]
    for s in sites:
        for j in range(d):
            s2=list(s); s2[j]+=1; s2=tuple(s2)
            if s2 in idx:
                g=tuple(s[k]+base[k] for k in range(d))
                sign=1 if j==0 else (-1)**sum(g[:j])
                bonds.append((idx[s],idx[s2],j,0.5*sign,s))
    return len(sites),bonds
def spec_min(n,bonds,ferm,omega=None,allN=True):
    best=None
    out={}
    for N in range(1,n):
        for Nup in range(N//2,N//2+1):  # lowest Sz sector holds all spins
            H,_=build_sector(n,bonds,N,Nup,ferm)
            if omega is not None: H=H*omega
            dim=H.shape[0]
            if dim<=3000: w=np.linalg.eigvalsh(H.toarray())[0]
            else: w=sla.eigsh(H,k=1,which='SA',tol=1e-11)[0][0]
            out[N]=w
    return out
if __name__=="__main__":
    shape=tuple(int(a) for a in sys.argv[1].split('x'))
    n,b=patch(shape)
    for ferm in (True,False):
        o=spec_min(n,b,ferm)
        print(shape,"F" if ferm else "B",{k:round(v,9) for k,v in o.items()},"min",min(o.values()))
