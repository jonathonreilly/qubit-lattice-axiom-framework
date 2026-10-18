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
T=float(sys.argv[1]); N=int(sys.argv[2])
v=np.ones(len(lst)); w=[]
for n in range(12): w.append(T**n/math.factorial(n)*v[0]); v=A@v
P=np.array(w)/sum(w); print('exact',np.round(P[:6],4))
sim=Sim(2,0.0,T,seed=9,cap=64); sim.pr=np.array([0.,0.,0.,1.0])
h=np.zeros(12)
for i in range(N):
    sim.do_sweep(); n=sim.nkinks()
    if n<12: h[n]+=1
print('numba',np.round(h[:6]/h.sum(),4))
