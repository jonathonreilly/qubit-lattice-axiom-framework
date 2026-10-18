import sys, numpy as np, math
sys.path.insert(0,'.')
from driver import Sim
from scipy.sparse import csr_matrix
from lattice import Lattice
lat=Lattice(2)
s=lat.canonical(); seen={tuple(s):0}; lst=[s]; edges=[]; i=0
while i<len(lst):
    c=lst[i]
    for p in np.flatnonzero(lat.flippable(c)):
        t=c.copy(); t[lat.plinks[p]]*=-1; k=tuple(t)
        if k not in seen: seen[k]=len(lst); lst.append(t)
        edges.append((i,seen[k]))
    i+=1
e=np.array(edges); A=csr_matrix((np.ones(len(e)),(e[:,0],e[:,1])),shape=(len(lst),len(lst))).toarray()
T=float(sys.argv[1]); N=int(sys.argv[2]); local=float(sys.argv[3])
one=np.ones(len(lst)); v=one.copy(); w=[]
for n in range(14): w.append(T**n/math.factorial(n)*one@v); v=A@v
P=np.array(w)/sum(w); print('exact P(n)',np.round(P[:8],4))
sim=Sim(2,0.0,T,seed=11,cap=64); sim.hist=1.0
for i in range(500): sim.do_sweep()
sim.nm_fixed=int(local*24)
h=np.zeros(14)
for it in range(N):
    sim.do_sweep(); n=sim.nkinks()
    if n<14: h[n]+=1
print('qmc   P(n)',np.round(h[:8]/h.sum(),4),'valid',sim.valid())
