"""T16 - INDEPENDENT test of A_pred/B_pred and of S_Regge, using the ACTION rather
than the per-edge gradients.  Delta W(tau0) must equal
   A_pred(tau0) * Delta Vol  +  B_pred(tau0) * Delta S_Regge
with A_pred = -E_3(m^2 tau0)/(32 pi^2 tau0^2), B_pred = -E_2(m^2 tau0)/(96 pi^2 tau0).
Fitting Delta W(tau0) to those two KNOWN functions of tau0 returns coefficients that
must reproduce the geometrically computed Delta Vol and Delta S_Regge.
This uses no gradient, no Schlaefli identity, no per-edge fit: an independent path."""
import numpy as np, sys, scipy.special as sp; sys.path.insert(0,".")
from bridge_fit import *
from bridge_spec import local_Hmatrix
L=int(sys.argv[1]) if len(sys.argv)>1 else 32
M2=float(sys.argv[2]) if len(sys.argv)>2 else 0.2
AMP=float(sys.argv[3]) if len(sys.argv)>3 else 0.12
NKW=int(sys.argv[4]) if len(sys.argv)>4 else 1
spec={}
for tag,amp,al in (('flat',0.0,[0,0,0,0]),('conf',AMP,[1,1,1,1]),('TT',AMP,[0,1,-1,0])):
    S=edge_s(L,amp,NKW,al); g=geometry(S,L)
    _,lam=local_Hmatrix(S,L,{'z':lambda w:w*0},ret_spec=True,geom=g)
    spec[tag]=(np.sort(lam),g['Vol'],g['Reg'])
TAUS=np.array([3.,4.,5.,6.,8.,10.,12.,16.])
def W(lam,t): mu=lam+lam*lam/24.0; return -0.5*float(np.sum(sp.exp1(t*(mu+M2))))
print(f"T16 L={L} m^2={M2} amp={AMP} nk={NKW} improved.   Fit dW(tau0) = cA*Apred + cB*Bpred")
for tag in ('conf','TT'):
    lp,Vp,Rp=spec[tag]; lf,Vf,Rf=spec['flat']
    dV=Vp-Vf; dR=Rp-Rf
    dW=np.array([W(lp,t)-W(lf,t) for t in TAUS])
    M=np.stack([[preds(t,M2)[0] for t in TAUS],[preds(t,M2)[1] for t in TAUS]],1)
    coef,*_=np.linalg.lstsq(M,dW,rcond=None)
    res=dW-M@coef
    print(f"  {tag}:  geometry   dVol={dV:+.6e}   dS_Regge={dR:+.6e}")
    print(f"        spectrum   cA  ={coef[0]:+.6e}   cB      ={coef[1]:+.6e}"
          f"   |  cA/dVol={coef[0]/dV:.4f}  cB/dS={coef[1]/dR:.4f}"
          f"   fit resid {np.linalg.norm(res)/np.linalg.norm(dW):.2e}")
    # two-point solves, to expose tau0 drift
    for i in range(len(TAUS)-1):
        c,*_=np.linalg.lstsq(M[i:i+2],dW[i:i+2],rcond=None)
        print(f"        tau0=({TAUS[i]:.0f},{TAUS[i+1]:.0f}): cA/dVol={c[0]/dV:8.4f}  cB/dS={c[1]/dR:8.4f}")
