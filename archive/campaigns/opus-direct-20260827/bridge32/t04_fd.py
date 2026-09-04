"""T04 - tight FD validation of dVol and dS_Regge (absolute error vs RMS scale)."""
import numpy as np, sys; sys.path.insert(0,".")
from bridge_geom import *
L=8; AMP=0.05; S=edge_s(L,AMP,1,[0,1,-1,0]); g=geometry(S,L)
rmsV=np.sqrt((g['dVol']**2).mean()); rmsR=np.sqrt((g['dReg']**2).mean())
print(f"T04 L={L} amp={AMP}:  rms dVol={rmsV:.4e}  rms dReg={rmsR:.4e}")
for h in (1e-4,1e-5):
    eV=eR=0.0
    rng=np.random.default_rng(7)
    for _ in range(10):
        c=int(rng.integers(NE)); x=int(rng.integers(L))
        Sp=S.copy(); Sp[c,x]+=h; Sm=S.copy(); Sm[c,x]-=h
        gp=geometry(Sp,L); gm=geometry(Sm,L)
        eV=max(eV,abs((gp['Vol']-gm['Vol'])/(2*h)/L**3 - g['dVol'][c,x])/rmsV)
        eR=max(eR,abs((gp['Reg']-gm['Reg'])/(2*h)/L**3 - g['dReg'][c,x])/rmsR)
    print(f"    h={h:g}:  max |ana-fd|/rms   dVol {eV:.3e}   dS_Regge {eR:.3e}")
