import sys, numpy as np, math
sys.path.insert(0,'.')
from lattice import Lattice
from driver import Sim
from scipy.sparse import csr_matrix
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
T=float(sys.argv[1]); pr=np.array([float(x) for x in sys.argv[2].split(',')]); N=int(sys.argv[3])
one=np.ones(len(lst)); v=one.copy(); w=[]
for n in range(12):
    w.append(T**n/math.factorial(n)*one@v); v=A@v
w=np.array(w); P=w/w.sum()
print('exact P(n)',np.round(P[:7],4))
sim=Sim(2,0.0,T,seed=7,cap=64); sim.pr=pr
h=np.zeros(12)
for it in range(N):
    sim.do_sweep(1.0)
    n=sim.nkinks()
    if n<12: h[n]+=1
print('qmc   P(n)',np.round(h[:7]/h.sum(),4), 'valid', sim.valid(), flush=True)
