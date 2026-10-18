import sys, numpy as np, math
sys.path.insert(0,'.')
from lattice import Lattice
from driver import Sim, binned_se
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
lam,U=np.linalg.eigh(A)
f=lambda T: (U@(np.exp(T*lam)*(U.T@np.ones(len(lst)))))[0]
dlnZ=(np.log(f(T*1.0001))-np.log(f(T*0.9999)))/(2e-4)  # dlnZ/dlnT
print('exact <n> fixed end=canonical:', dlnZ)
sim=Sim(2,0.0,T,seed=9,cap=64); sim.pr=np.array([0.,0.,0.,1.0])
for i in range(5000): sim.do_sweep()
nk=[]
for i in range(N):
    sim.do_sweep(); nk.append(sim.nkinks())
print('qmc start-only', binned_se(nk)[:2], 'end state canonical?', np.all(sim.states(np.array([T]))[0]==lat.canonical()))
