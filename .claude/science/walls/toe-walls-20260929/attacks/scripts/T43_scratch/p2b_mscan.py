import numpy as np
from stag import *
out=[]
def rep(s): print(s); out.append(s)
rep("2D U(1), Gamma_f: coefficient c(m) = arg det / (-2 Q arctan(m5/m)), m5/m = 0.1, Q=1,2")
for L in (8,12,16):
    lat=Lat(L,2)
    for Q in (1,2):
        U=u1_flux_links_2d(lat,Q); D=stag_D(lat,U).toarray(); Gf=gamma_f_2d(lat,U).toarray()
        w=np.linalg.eigvals(D); lam0=np.sort(np.abs(w))[:2*Q].max()
        row=[]
        for m in (0.05,0.1,0.2,0.5,1.0):
            r=0.1
            a,_=argdet(D+m*np.eye(lat.V)+1j*r*m*Gf)
            row.append(f"m={m}:{-a/(2*Q*np.arctan(r)):.4f}")
        rep(f"L={L:2d} Q={Q} lifted-mode |lam|={lam0:.1e}  "+"  ".join(row))
open("p2b_out.txt","w").write("\n".join(out)+"\n")
