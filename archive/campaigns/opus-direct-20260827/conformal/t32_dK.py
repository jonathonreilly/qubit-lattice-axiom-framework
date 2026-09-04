"""T32 - THE PER-EDGE BRIDGE, CUTOFF-RESOLVED.
W = -(1/2) int_tau0^inf (dtau/tau) K(tau) mixes every proper time above tau0, so a
fit at fixed tau0 inherits the lattice error from the bottom of that integral and
can never plateau.  Differentiating the cutoff away, dW/dtau0 = K(tau0)/(2 tau0),
gives the same bridge at ONE proper time:
      dK(s)/ds_e  =  (4 pi s)^-2 [ dVol/ds_e + (s/3) dS_Regge/ds_e ]
so A'_pred = (4 pi s)^-2 and B'_pred = (4 pi s)^-2 s/3.  Same per-edge fit, same
partial correlation, but the two windows (a^2/s and s k^2) are now separated."""
import numpy as np, sys, time; sys.path.insert(0,".")
from bridge_fit import *
from bridge_spec import dK_multi
L=int(sys.argv[1]); SL=[float(x) for x in sys.argv[2].split(',')]
POLS={'TT':[0,1,-1,0],'conf':[1,1,1,1],'V0a':[0,1,1,0],'tran':[0,1,0,0]}
if len(sys.argv)>3: POLS={k:POLS[k] for k in sys.argv[3].split(',')}
AMP=0.06; NKW=1; k2=(2*np.pi*NKW/L)**2
S0=edge_s(L,0.0,NKW,[0,0,0,0]); g0=geometry(S0,L); t0=time.time()
dK0=dK_multi(S0,L,SL,geom=g0,verbose=True)
print(f"# T32 L={L} amp={AMP} nk={NKW} improved  k^2={k2:.6f}  (flat pass {time.time()-t0:.0f}s)")
print(f"{'pol':>5} {'s':>6} {'s k^2':>7} {'A/Apred':>9} {'B/Bpred':>9} {'part r':>8} "
      f"{'corr12':>7} {'res/y':>9} {'res/Bx2':>9}")
for nm,al in POLS.items():
    S=edge_s(L,AMP,NKW,al); g=geometry(S,L); dK=dK_multi(S,L,SL,geom=g)
    x1=(g['dVol']-g0['dVol']).ravel(); x2=(g['dReg']-g0['dReg']).ravel()
    c12=float(x1@x2/np.sqrt((x1@x1)*(x2@x2)))
    for t,s in enumerate(SL):
        y=(dK[t]-dK0[t]).ravel(); A,B,pr,R2=fit2(y,x1,x2)
        Ap=(4*np.pi*s)**-2.0; Bp=Ap*s/3.0; res=y-A*x1-B*x2
        print(f"{nm:>5} {s:6.1f} {s*k2:7.3f} {A/Ap:9.4f} {B/Bp:9.4f} {pr:8.4f} {c12:7.4f} "
              f"{np.linalg.norm(res)/np.linalg.norm(y):9.3e} "
              f"{np.linalg.norm(res)/np.linalg.norm(B*x2):9.3e}",flush=True)
