import math, sys
import numpy as np
from scipy.sparse.linalg import expm_multiply
sys.path.insert(0,"/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/main_wt/scripts")
import repeated_formation_check as rf
delta,kappa=1.3,0.7
model=rf.tree_model(None)
g=model['g'];dim=len(g)
W=model['W'].astype(float);T=model['T'].astype(float);N=model['N'].astype(float)
w=np.diag(W)
for eps in (0.2,0.1,0.05):
    Hp=delta*W/eps**2+delta*T/eps
    L=rf.superop(Hp,[math.sqrt(kappa)*j/eps for j in model['coherent']])
    rho0=np.outer(g,g).astype(complex)
    for tmax in (14,60,200):
        v=expm_multiply(L,rho0.reshape(-1,order='F'),start=0,stop=tmax,num=2,traceA=L.diagonal().sum())[-1]
        r=v.reshape((dim,dim),order='F')
        pw={int(k):float(np.trace(r[np.ix_(w==k,w==k)]).real) for k in sorted(set(w))}
        b=(np.trace(N@r).real-1*0-np.trace(N@rho0).real)/2
        Ep=np.trace(Hp@r).real
        print(f"eps={eps} tmax={tmax}: births={b:.4f}  E'/delta={Ep/delta:.4f}  P(W)= {pw}")
