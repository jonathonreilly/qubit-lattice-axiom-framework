"""K2b: 4D U(1) extras: Q=2 at L=8; C-parity check (-1,-1) vs (1,1); extrapolation of 1-c ~ A/L^2 at m=0.02."""
import numpy as np, scipy.sparse as sp, warnings
warnings.simplefilter("ignore")
from k2_4d import build4, detphase
r=0.1
out=[]
def rep(s): print(s,flush=True); out.append(s)
for (Q1,Q2,L) in [(2,1,8),(-1,-1,6),(1,1,6),(-1,1,6)]:
    D,G,f1,f2=build4(L,Q1,Q2); V=L**4; I=sp.identity(V,format="csr"); Q=Q1*Q2
    row=[]
    for m in (0.02,0.1,0.5):
        a,_=detphase(D+m*I+1j*r*m*G); row.append(f"m={m}: arg={a:+.5f} c={-a/(4*Q*np.arctan(r)):.4f}")
    rep(f"(Q1,Q2)=({Q1:+d},{Q2:+d}) Q={Q:+d} L={L}: "+"  ".join(row))
open("k2b_out.txt","w").write("\n".join(out)+"\n")
