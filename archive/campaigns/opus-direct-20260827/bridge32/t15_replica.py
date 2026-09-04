"""T15 - REPLICA TEST.  (L=16,nk=1) and (L=32,nk=2) are the SAME configuration
(same lattice spacing, same k, same amplitude); the second is two periodic copies
of the first.  dVol and dS_Regge are strictly local, so they must agree exactly.
dW/ds_e is a mode sum: with m=0 the kernel exp(-tau l)/l has a POWER-LAW tail
(massless propagator), so finite-volume differences are power-law, not exponential.
This measures them, and shows what a mass does."""
import numpy as np, sys; sys.path.insert(0,".")
from bridge_fit import *
from bridge_spec import dW_multi
AL=[1,1,1,1]; AMP=0.03
for M2 in (0.0, 0.05, 0.2):
    SET=[(4.0,M2,True),(8.0,M2,True)]
    dat={}
    for L,nk in ((16,1),(32,2)):
        S0=edge_s(L,0.0,nk,AL); g0=geometry(S0,L); S=edge_s(L,AMP,nk,AL); g=geometry(S,L)
        dW0=dW_multi(S0,L,SET,geom=g0); dW=dW_multi(S,L,SET,geom=g)
        dat[L]=dict(y=[(dW[t]-dW0[t])[:, :16] for t in range(len(SET))],
                    x1=(g['dVol']-g0['dVol'])[:, :16], x2=(g['dReg']-g0['dReg'])[:, :16],
                    g=g, g0=g0)
    a,b=dat[16],dat[32]
    print(f"m^2={M2}:  dVol replica diff {np.abs(b['x1']-a['x1']).max()/np.abs(a['x1']).max():.2e}"
          f"   dS_Regge {np.abs(b['x2']-a['x2']).max()/np.abs(a['x2']).max():.2e}")
    for t,(tau0,m2,_) in enumerate(SET):
        d32=np.abs(b['y'][t]-a['y'][t]).max()/np.abs(a['y'][t]).max()
        d48=float('nan')
        Bs=[]
        for L in (16,32):
            d=dat[L]; A,B,pr,_=fit2(d['y'][t].ravel(),d['x1'].ravel(),d['x2'].ravel())
            Ap,Bp=preds(tau0,m2); Bs.append((A/Ap,B/Bp))
        print(f"   tau0={tau0}:  |dW(L=32)-dW(L=16)|/|dW| = {d32:.3e}"
              f"   |  A/Ap,B/Bp: L16 {Bs[0][0]:.4f},{Bs[0][1]:.4f}  "
              f"L32 {Bs[1][0]:.4f},{Bs[1][1]:.4f}")
