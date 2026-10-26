import numpy as np, itertools
from lib import *
exec(open('t1.py').read().split("hh=V")[0])
def orig_many(h,n,N,fermion):
    states=[]
    for sites in itertools.combinations(range(n),N):
        for cs in itertools.product((0,1),repeat=N):
            states.append((sites,cs))
    idx={s:i for i,s in enumerate(states)}
    M=np.zeros((len(states),len(states)),complex)
    for (sites,cs),i in idx.items():
        for p,(s,c) in enumerate(zip(sites,cs)):
            for e in range(n):
                if e in sites: continue
                for c2 in (0,1):
                    amp=h[2*e+c2,2*s+c]
                    if amp==0: continue
                    new=dict(zip(sites,cs)); del new[s]; new[e]=c2
                    ns=tuple(sorted(new)); ncs=tuple(new[k] for k in ns)
                    sg=1
                    if fermion:
                        lo,hi=min(s,e),max(s,e)
                        k=sum(1 for t in sites if lo<t<hi); sg=(-1)**k
                    M[idx[(ns,ncs)],i]+=amp*sg
    return M
for N in (2,3):
  for ferm in (True,False):
    M=orig_many(h,n,N,ferm)
    assert np.abs(M-M.conj().T).max()<1e-12
    ev=np.sort(np.linalg.eigvalsh(M))
    allev=[]
    for Nup in range(N+1):
        H,_=build_sector(n,bonds,N,Nup,ferm)
        allev+=list(np.linalg.eigvalsh(H.toarray()))
    allev=np.sort(allev)
    print(N,ferm,len(ev),len(allev),np.abs(ev-allev).max(), ev[0])
