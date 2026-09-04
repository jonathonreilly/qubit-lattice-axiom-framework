"""T29 - amplitude independence of r(s) (linear-response check on the heat trace)."""
import numpy as np, sys; sys.path.insert(0,".")
from bridge_fit import *
from bridge_spec import local_Hmatrix
L=32; NKW=1
S0=edge_s(L,0.0,NKW,[0,0,0,0]); g0=geometry(S0,L)
_,lf=local_Hmatrix(S0,L,{'z':lambda w:w*0},ret_spec=True,geom=g0); muf=lf+lf*lf/24.0
print("T29  r(s) vs amplitude, L=32 improved")
for al,nm in (([0,1,-1,0],'TT'),([1,1,1,1],'conf')):
    print(f"  {nm}: "+ " ".join(f"{'s=%g'%s:>9}" for s in (6,8,12,16,20)))
    for amp in (0.02,0.06,0.12):
        S=edge_s(L,amp,NKW,al); g=geometry(S,L)
        _,lp=local_Hmatrix(S,L,{'z':lambda w:w*0},ret_spec=True,geom=g); mu=lp+lp*lp/24.0
        dV=g['Vol']-g0['Vol']; dR=g['Reg']-g0['Reg']
        row=f"   amp={amp:4.2f} "
        for s in (6,8,12,16,20):
            P=(float(np.exp(-s*mu).sum())-float(np.exp(-s*muf).sum()))*(4*np.pi*s)**2
            row+=f"{((P-dV)/s)/(dR/3):9.4f}"
        print(row,flush=True)
