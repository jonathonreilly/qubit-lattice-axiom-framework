"""T36 - JOINT per-edge fit across polarisation channels.  Within one channel
dVol/ds_e and dS_Regge/ds_e are 0.57-0.997 correlated, so a small off-span
residual moves B a lot.  Different channels have different dVol:dS ratios, so
stacking them (no per-channel rescaling -- the prediction has no free scale)
breaks the degeneracy."""
import numpy as np, sys; sys.path.insert(0,".")
from bridge_fit import *
from bridge_spec import dK_multi
L=int(sys.argv[1]); SL=[float(x) for x in sys.argv[2].split(',')]
POLS={'TT':[0,1,-1,0],'conf':[1,1,1,1],'V0a':[0,1,1,0],'tran':[0,1,0,0],
      'gauge':[1,0,0,0],'m1':[0,2,1,0],'m2':[2,1,1,1],'m3':[0,1,1,1]}
if L>=64: POLS={k:POLS[k] for k in ('TT','conf','V0a','tran')}
AMP=0.06; NKW=1; k2=(2*np.pi*NKW/L)**2
S0=edge_s(L,0.0,NKW,[0,0,0,0]); g0=geometry(S0,L); dK0=dK_multi(S0,L,SL,geom=g0)
D={}
for nm,al in POLS.items():
    S=edge_s(L,AMP,NKW,al); g=geometry(S,L); dK=dK_multi(S,L,SL,geom=g)
    D[nm]=([(dK[t]-dK0[t]).ravel() for t in range(len(SL))],
           (g['dVol']-g0['dVol']).ravel(), (g['dReg']-g0['dReg']).ravel())
print(f"# T36 joint per-edge fit, L={L} amp={AMP} nk={NKW} improved, {len(POLS)} channels")
print(f"{'s':>6} {'s k^2':>7} {'A/Apred':>9} {'B/Bpred':>9} {'part r':>8} {'corr12':>7} "
      f"{'res/y':>9} {'res/Bx2':>9} {'dB(sys)':>8}")
for t,s in enumerate(SL):
    y=np.concatenate([D[n][0][t] for n in POLS]); x1=np.concatenate([D[n][1] for n in POLS])
    x2=np.concatenate([D[n][2] for n in POLS])
    A,B,pr,R2=fit2(y,x1,x2); Ap=(4*np.pi*s)**-2.0; Bp=Ap*s/3.0
    res=y-A*x1-B*x2; c12=float(x1@x2/np.sqrt((x1@x1)*(x2@x2)))
    dB=np.linalg.norm(res)/np.linalg.norm(B*x2)/np.sqrt(1-c12**2)
    print(f"{s:6.1f} {s*k2:7.3f} {A/Ap:9.4f} {B/Bp:9.4f} {pr:8.4f} {c12:7.4f} "
          f"{np.linalg.norm(res)/np.linalg.norm(y):9.3e} "
          f"{np.linalg.norm(res)/np.linalg.norm(B*x2):9.3e} {dB:8.3f}",flush=True)
