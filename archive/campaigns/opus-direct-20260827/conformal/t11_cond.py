"""T11 - conditioning of the two-parameter fit: how collinear are dVol and dS_Regge?"""
import numpy as np, sys; sys.path.insert(0,".")
from bridge_fit import *
pol={'TT (0,1,-1,0)':[0,1,-1,0],'conf(1,1,1,1)':[1,1,1,1],'tran(0,1,0,0)':[0,1,0,0],
     'mix (0,2,-1,-1)':[0,2,-1,-1],'mix2(3,1,1,1)':[3,1,1,1]}
L=16
print(f"L={L} nk=1 amp=0.03:   corr(dVol,dS)   |x2|/|x1|   cond(X)")
for name,AL in pol.items():
    S0=edge_s(L,0.0,1,AL); g0=geometry(S0,L); S=edge_s(L,0.03,1,AL); g=geometry(S,L)
    x1=(g['dVol']-g0['dVol']).ravel(); x2=(g['dReg']-g0['dReg']).ravel()
    c=x1@x2/np.sqrt((x1@x1)*(x2@x2)); X=np.stack([x1/np.linalg.norm(x1),x2/np.linalg.norm(x2)],1)
    print(f"   {name:>16}  {c:+.6f}   {np.linalg.norm(x2)/np.linalg.norm(x1):.3e}   "
          f"{np.linalg.cond(X):8.2f}")
