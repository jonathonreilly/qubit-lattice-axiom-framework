"""T17 - the cleanest form of the bridge test.  For the background-subtracted heat
trace the derivative expansion is a POLYNOMIAL in the proper time s:

   P(s) := [K_pert(s) - K_flat(s)] (4 pi s)^2
         = Delta int a_0 + s Delta int a_1 + s^2 Delta int a_2 + ...
         = Delta Vol      + s (Delta S_Regge / 3) + O(s^2)

because int sqrt(g) a_1 = (1/6) int sqrt(g) R = S_Regge/3.  Fitting P(s) to a
polynomial (plus 1/s, 1/s^2 terms that absorb the residual lattice error) and
reading off the LINEAR coefficient measures the Einstein coefficient directly,
with no per-edge fit, no Schlaefli gradient and no proper-time cutoff at all.
Everything here is exact to machine precision."""
import numpy as np, sys; sys.path.insert(0,".")
from bridge_fit import *
from bridge_spec import local_Hmatrix
L=int(sys.argv[1]) if len(sys.argv)>1 else 32
AMP=float(sys.argv[2]) if len(sys.argv)>2 else 0.06
NKW=int(sys.argv[3]) if len(sys.argv)>3 else 1
POLS={'conf':[1,1,1,1],'TT':[0,1,-1,0],'tran':[0,1,0,0],'gauge':[1,0,0,0]}
spec={}
for tag,al in [('flat',[0,0,0,0])]+list(POLS.items()):
    S=edge_s(L,0.0 if tag=='flat' else AMP,NKW,al); g=geometry(S,L)
    _,lam=local_Hmatrix(S,L,{'z':lambda w:w*0},ret_spec=True,geom=g)
    spec[tag]=(lam,g['Vol'],g['Reg'])
lf,Vf,Rf=spec['flat']
def P(lam,s,imp=True):
    mu=lam+lam*lam/24.0 if imp else lam
    muf=lf+lf*lf/24.0 if imp else lf
    return (float(np.exp(-s*mu).sum())-float(np.exp(-s*muf).sum()))*(4*np.pi*s)**2
print(f"T17 L={L} amp={AMP} nk={NKW} improved.  k={2*np.pi*NKW/L:.4f}  k^2={(2*np.pi*NKW/L)**2:.5f}")
for tag,al in POLS.items():
    lp,Vp,Rp=spec[tag]; dV=Vp-Vf; dR=Rp-Rf
    for smax,npow,nneg in ((8.0,3,1),(8.0,4,1),(12.0,4,1),(12.0,5,2),(16.0,5,2)):
        ss=np.linspace(2.7,smax,40)
        Pv=np.array([P(lp,s) for s in ss])
        Bs=[ss**j for j in range(npow+1)]+[ss**(-j) for j in range(1,nneg+1)]
        Mx=np.stack(Bs,1); c,*_=np.linalg.lstsq(Mx,Pv,rcond=None)
        res=np.linalg.norm(Pv-Mx@c)/np.linalg.norm(Pv)
        print(f"  {tag:>6} s in [2.7,{smax:4.1f}] poly{npow}+{nneg}neg: "
              f"a0 {c[0]:+.5e} (dVol {dV:+.5e}, ratio {c[0]/dV if dV!=0 else np.nan:7.4f})   "
              f"a1 {c[1]:+.5e} (dS/3 {dR/3:+.5e}, ratio {c[1]/(dR/3) if dR!=0 else np.nan:7.4f})"
              f"  resid {res:.1e}")
    print()
