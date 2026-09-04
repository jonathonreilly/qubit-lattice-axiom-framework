import numpy as np, sys; sys.path.insert(0,".")
from bridge_geom import *
L=8; AMP=0.05; NKW=1; AL=[0.0,1.0,-1.0,0.0]
S0 = edge_s(L,0.0,NKW,AL); g0 = geometry(S0,L)
print(f"T02 flat L={L}: Vol={g0['Vol']:.10f} (exact L^4={L**4})  "
      f"max|deficit|={np.abs(g0['dfc']).max():.3e}  S_Regge={g0['Reg']:.3e}")
print(f"    triangle classes: {NT};  areas on flat: {np.unique(np.round(g0['A'],12))}")
S = edge_s(L,AMP,NKW,AL); g = geometry(S,L)
print(f"T02 curved amp={AMP}: Vol={g['Vol']:.8f}  S_Regge={g['Reg']:.8e}  "
      f"max|deficit|={np.abs(g['dfc']).max():.3e}")
# finite-difference check of the reduced gradients
rng=np.random.default_rng(1); h=1e-6; ok=[]
for _ in range(6):
    c=rng.integers(NE); x=rng.integers(L)
    Sp=S.copy(); Sp[c,x]+=h; Sm=S.copy(); Sm[c,x]-=h
    gp=geometry(Sp,L); gm=geometry(Sm,L)
    fdV=(gp['Vol']-gm['Vol'])/(2*h)/L**3; fdR=(gp['Reg']-gm['Reg'])/(2*h)/L**3
    ok.append((abs(fdV-g['dVol'][c,x])/abs(g['dVol'][c,x]), abs(fdR-g['dReg'][c,x])/abs(g['dReg'][c,x])))
    print(f"    edge(c={c},x0={x}):  dVol ana {g['dVol'][c,x]:+.10e} fd {fdV:+.10e} |"
          f"  dReg ana {g['dReg'][c,x]:+.10e} fd {fdR:+.10e}")
ok=np.array(ok); print(f"T02 max rel err:  dVol {ok[:,0].max():.2e}   dS_Regge {ok[:,1].max():.2e}")
