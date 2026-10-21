import sys, numpy as np, time
sys.path.insert(0,'.')
from driver import Sim, config_obs
L=int(sys.argv[1]); T=float(sys.argv[2]); N=int(sys.argv[3]); seed=int(sys.argv[4])
sim=Sim(L,0.0,T,seed=seed,cap=200)
for i in range(5000): sim.do_sweep()
sim.nm_fixed=sim.lat.np+sim.nkinks()
PEs=[];Pns=[];Nfs=[]
for i in range(N):
    sim.do_sweep()
    if i%4==0:
        st=sim.states(np.array([T/2])); PE,Pn,Nf,Ek=config_obs(sim.lat,st)
        PEs.append(PE[0].astype(np.float32)); Pns.append(Pn[0].astype(np.float32)); Nfs.append(Nf[0])
PEs=np.array(PEs); Pns=np.array(Pns); Nfs=np.array(Nfs)
B=250; nb=len(Nfs)//B
bN=Nfs[:nb*B].reshape(nb,B).mean(1); lo=bN<np.median(bN)
bPE=PEs[:nb*B].reshape(nb,B,L,L,L,3).mean(1); bPn=Pns[:nb*B].reshape(nb,B,L,L,L,3).mean(1)
dE=bPE[lo].mean(0)-bPE[~lo].mean(0); dn=bPn[lo].mean(0)-bPn[~lo].mean(0)
print('blocks',nb,'Nf/Np low %.4f high %.4f'%(bN[lo].mean()/sim.lat.np,bN[~lo].mean()/sim.lat.np))
idx=np.argsort(-np.abs(dE).ravel())[:8]
for k in idx:
    q=np.unravel_index(k,dE.shape); print('  E comp',q[3],'q',q[:3],'low-high %.3f  (low %.3f high %.3f)'%(dE[q],bPE[lo].mean(0)[q],bPE[~lo].mean(0)[q]))
idx=np.argsort(-np.abs(dn).ravel())[:8]
for k in idx:
    q=np.unravel_index(k,dn.shape); print('  n ori',q[3],'q',q[:3],'low-high %.3f  (low %.3f high %.3f)'%(dn[q],bPn[lo].mean(0)[q],bPn[~lo].mean(0)[q]))
