import sys, numpy as np
sys.path.insert(0,'.')
from driver import Sim, binned_se
L=int(sys.argv[1]); T=float(sys.argv[2]); pr=np.array([float(x) for x in sys.argv[3].split(',')]); N=int(sys.argv[4])
sim=Sim(L,0.0,T,seed=9,cap=128); sim.pr=pr
for i in range(int(sys.argv[5]) if len(sys.argv)>5 else 2000): sim.do_sweep()
nk=[];nf=[]
for i in range(N):
    sim.do_sweep()
    nk.append(sim.nkinks())
    st=sim.states(np.array([0.0,T]))
    nf.append(0.5*(sim.lat.flippable(st[0]).sum()+sim.lat.flippable(st[1]).sum()))
a=binned_se(nk); b=binned_se(np.array(nf)*T)
print(f"L={L} T={T} pr={pr}: <n>={a[0]:.3f}+-{a[1]:.3f}  T<Nf_end>={b[0]:.3f}+-{b[1]:.3f}  valid={sim.valid()}")
