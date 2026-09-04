"""T21 - kill the volume term.  For g_mumu = 1 + alpha_mu f(x0),
   Delta Vol / Vol = [(1/8)S^2 - (1/4)Q] * amp^2/2,   S = sum alpha, Q = sum alpha^2,
so any alpha with S^2 = 2Q has NO volume response at O(amp^2).  Then
   P(s) = [K_pert - K_flat](4 pi s)^2  =  s * (Delta S_Regge/3) + s^2 a_2 + lattice
and the Einstein coefficient is read off with the huge a_0 term absent.
alpha = (0,1,1,0) and (0,1,1,4) are transverse (no g_00 modulation) and volume-free."""
import numpy as np, sys, os; sys.path.insert(0,".")
from bridge_fit import *
from bridge_spec import local_Hmatrix
L=int(sys.argv[1]); AMP=float(sys.argv[2]); NKW=int(sys.argv[3])
IMP=(len(sys.argv)<5) or sys.argv[4]!='plain'
POLS={'V0a(0,1,1,0)':[0,1,1,0],'V0b(0,1,1,4)':[0,1,1,4],'V0c(1,1,0,0)':[1,1,0,0],
      'TT (0,1,-1,0)':[0,1,-1,0]}
spec={}
for tag,al in [('flat',[0,0,0,0])]+list(POLS.items()):
    S=edge_s(L,0.0 if tag=='flat' else AMP,NKW,al); g=geometry(S,L)
    _,lam=local_Hmatrix(S,L,{'z':lambda w:w*0},ret_spec=True,geom=g)
    spec[tag]=(np.sort(lam),g['Vol'],g['Reg'])
lf,Vf,Rf=spec['flat']; muf=lf+lf*lf/24.0 if IMP else lf
k2=(2*np.pi*NKW/L)**2
print(f"T21 L={L} amp={AMP} nk={NKW} {'improved' if IMP else 'plain'}  k^2={k2:.5f}  Vol={Vf:.1f}")
for tag,al in POLS.items():
    lp,Vp,Rp=spec[tag]; dV=Vp-Vf; dR=Rp-Rf; mu=lp+lp*lp/24.0 if IMP else lp
    print(f"\n  {tag}:  dVol={dV:+.4e} ({dV/Vf:+.2e} rel)   dS_Regge={dR:+.5e}   dS/3={dR/3:+.5f}")
    print(f"    {'s':>6} {'P(s)':>13} {'(P-dVol)/s':>13} {'ratio':>9} {'s k^2':>7}")
    for s in (3,4,5,6,8,10,12,16,20,25,32,40):
        if s*k2>1.3: break
        P=(float(np.exp(-s*mu).sum())-float(np.exp(-s*muf).sum()))*(4*np.pi*s)**2
        v=(P-dV)/s
        print(f"    {s:6.1f} {P:13.5f} {v:13.5f} {v/(dR/3):9.4f} {s*k2:7.3f}")
