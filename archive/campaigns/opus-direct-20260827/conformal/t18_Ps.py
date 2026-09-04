"""T18 - look directly at P(s) = [K_pert(s)-K_flat(s)](4 pi s)^2.
For the PURE-GAUGE channel (g_00 = 1+f(x0), which is flat space in disguise:
R=0 exactly, all a_n=0 for n>=1) the continuum answer is P(s) = Delta Vol,
a CONSTANT.  Whatever s-dependence appears there is pure lattice artifact and
sets the floor for measuring the a_1 (Einstein) coefficient of any other channel."""
import numpy as np, sys; sys.path.insert(0,".")
from bridge_fit import *
from bridge_spec import local_Hmatrix
L=int(sys.argv[1]) if len(sys.argv)>1 else 32
AMP=float(sys.argv[2]) if len(sys.argv)>2 else 0.06
NKW=int(sys.argv[3]) if len(sys.argv)>3 else 1
POLS={'gauge':[1,0,0,0],'TT':[0,1,-1,0],'conf':[1,1,1,1]}
spec={}
for tag,al in [('flat',[0,0,0,0])]+list(POLS.items()):
    S=edge_s(L,0.0 if tag=='flat' else AMP,NKW,al); g=geometry(S,L)
    _,lam=local_Hmatrix(S,L,{'z':lambda w:w*0},ret_spec=True,geom=g)
    spec[tag]=(lam,g['Vol'],g['Reg'])
lf,Vf,Rf=spec['flat']
SS=[2.0,2.7,3,4,5,6,8,10,12,16,20,25,32]
print(f"T18 L={L} amp={AMP} nk={NKW}  k^2={(2*np.pi*NKW/L)**2:.5f}")
for imp in (True,False):
    muf=lf+lf*lf/24.0 if imp else lf
    print(f"\n  {'improved' if imp else 'plain'}: P(s) = [K_p-K_f](4 pi s)^2   "
          f"(continuum: dVol + s*dS/3 + O(s^2))")
    print(f"    {'s':>6}"+"".join(f"{t:>26}" for t in POLS))
    print(f"    {'':>6}"+"".join(f"{'dVol=%.2f'%(spec[t][1]-Vf):>13}{'dS/3=%.3f'%((spec[t][2]-Rf)/3):>13}" for t in POLS))
    for s in SS:
        row=f"    {s:6.1f}"
        for t in POLS:
            lp=spec[t][0]; mu=lp+lp*lp/24.0 if imp else lp
            P=(float(np.exp(-s*mu).sum())-float(np.exp(-s*muf).sum()))*(4*np.pi*s)**2
            dV=spec[t][1]-Vf; dR=spec[t][2]-Rf
            row+=f"{P:>13.4f}{(P-dV)/s:>13.4f}"
        print(row)
    print(f"    [second column per channel = (P(s)-dVol)/s, which must -> dS_Regge/3]")
