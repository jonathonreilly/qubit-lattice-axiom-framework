"""P1/P3 on the 4D U(1) staggered torus with fluxes F12 = 2 pi Q1/L^2, F34 = 2 pi Q2/L^2 (topological charge Q = Q1 Q2)."""
import numpy as np
from stag import *
out=[]
def rep(s): print(s); out.append(s)
r=0.1
for L in (4,6):
    lat=Lat(L,4); E=np.diag(lat.eps)
    rep(f"=== 4D U(1) L={L}, V={lat.V}")
    for (Q1,Q2) in [(0,0),(1,0),(1,1),(-1,1),(2,1),(1,-2)]:
        U=u1_flux_links_4d(lat,Q1,Q2)
        f12=total_flux_plane(lat,U,0,1)/(2*np.pi); f34=total_flux_plane(lat,U,2,3)/(2*np.pi)
        D=stag_D(lat,U).toarray(); G=singlet_op(lat,U,True).toarray()
        w=np.linalg.eigvals(D); nz=int((np.abs(w)<1e-8).sum())
        I=np.eye(lat.V)
        for m in (0.1,0.5):
            a_e,ld_e=argdet(D+m*I+1j*r*m*E)
            ref=np.linalg.slogdet(D+np.sqrt(1+r*r)*m*I)[1]
            a_g,_=argdet(D+m*I+1j*r*m*G)
            Q=Q1*Q2
            c = -a_g/(4*Q*np.arctan(r)) if Q!=0 else float('nan')
            rep(f"Q1,Q2=({Q1:+d},{Q2:+d}) Q={Q:+d} flux=({f12:.3f},{f34:.3f}) #zero modes={nz:3d} m={m}: arg det[eps]={a_e:+.1e} (dlog|det|={ld_e-ref:+.1e})  arg det[Gamma]={a_g:+.5f}  c=-arg/(4Q atan r)={c:+.4f}")
open("p3_out.txt","w").write("\n".join(out)+"\n")
