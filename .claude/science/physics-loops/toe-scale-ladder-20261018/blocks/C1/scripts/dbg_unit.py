import sys, numpy as np
sys.path.insert(0,'.')
from driver import Sim
import qmc
sim=Sim(2,0.0,0.05,seed=3,cap=64); sim.pr=np.array([0.,0.,0.,1.0])
# from X (empty), count start-insertion acceptances over many single moves, reverting each time
nf=sim.lat.flippable(sim.s0).sum()
acc=0; N=200000
for i in range(N):
    s0=sim.s0.copy(); kt=sim.kt.copy(); kc=sim.kc.copy(); st=np.zeros(10,dtype=np.int64)
    qmc.sweep(s0,kt,kc,*sim.args,1.0,0.0,0.05,0,1,sim.buf,st,sim.pr)
    if kc.sum()==1: acc+=1
print('X->Y prob per move', acc/N, 'expected 0.1*0.5*Nf/Np*T =', 0.1*0.5*nf/24*0.05, 'nf',nf)
# build Y
while sim.kc.sum()!=1:
    qmc.sweep(sim.s0,sim.kt,sim.kc,*sim.args,1.0,0.0,0.05,0,1,sim.buf,sim.stats,sim.pr)
rem=0; ins=0
for i in range(N):
    s0=sim.s0.copy(); kt=sim.kt.copy(); kc=sim.kc.copy(); st=np.zeros(10,dtype=np.int64)
    qmc.sweep(s0,kt,kc,*sim.args,1.0,0.0,0.05,0,1,sim.buf,st,sim.pr)
    if kc.sum()==0: rem+=1
    if kc.sum()==2: ins+=1
print('Y->X prob', rem/N, 'expected', 0.5/24, ' Y->2 prob', ins/N)
