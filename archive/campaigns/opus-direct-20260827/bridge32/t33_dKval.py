"""T33 - validate dK(s)/ds_e (per-edge heat-trace gradient) against finite
differences of the exactly-computed trace."""
import numpy as np, sys; sys.path.insert(0,".")
from bridge_fit import *
from bridge_spec import dK_multi, local_Hmatrix
L=6; AMP=0.08; AL=[1,1,-1,0]; SL=[2.0,5.0]
S=edge_s(L,AMP,1,AL); g=geometry(S,L)
dK=dK_multi(S,L,SL,geom=g)
def Ktr(S_,s):
    gg=geometry(S_,L)
    _,lam=local_Hmatrix(S_,L,{'z':lambda w:w*0},ret_spec=True,geom=gg)
    mu=lam+lam*lam/24.0
    return float(np.exp(-s*mu).sum())
rng=np.random.default_rng(5); h=1e-5
for t,s in enumerate(SL):
    rms=np.sqrt((dK[t]**2).mean()); e=[]
    for _ in range(4):
        c=int(rng.integers(NE)); x=int(rng.integers(L))
        Sp=S.copy(); Sp[c,x]+=h; Sm=S.copy(); Sm[c,x]-=h
        fd=(Ktr(Sp,s)-Ktr(Sm,s))/(2*h)/L**3
        e.append(abs(fd-dK[t][c,x])/rms)
        print(f"  s={s}  (c={c},x0={x}):  ana {dK[t][c,x]:+.10e}  fd {fd:+.10e}  d/rms {e[-1]:.2e}")
    print(f"T33 s={s}: max |ana-fd|/rms = {max(e):.2e}   [rms {rms:.3e}]")
