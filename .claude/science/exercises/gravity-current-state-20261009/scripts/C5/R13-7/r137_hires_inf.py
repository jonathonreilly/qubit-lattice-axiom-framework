"""R13-7: high-resolution closed form dc_e(inf)*U = (U/4) <A(q_x) (D + lam^2)/(d_x^2 W^3)>, D = d_y^2 + d_z^2:
q_x on a fine 1D grid (A depends on q_x only), q_perp on an N_perp^2 midpoint grid. Resolves steep plateaus."""
import sys; sys.path.insert(0,'.')
import numpy as np
from r137_onshell import Law, kgrid1, deriv, U
def hires(law,Nx=8000,Np=160,lam=0.0):
    qx=kgrid1(Nx); A=deriv(lambda k: law.S(k)**2,qx,2)/2-1; dx2=law.d(qx)**2
    q1=kgrid1(Np); QY,QZ=np.meshgrid(q1,q1,indexing='ij'); D=(law.d(QY)**2+law.d(QZ)**2).ravel()+lam**2
    m=np.abs(A)>1e-14; tot=0.0
    for Ai,d2 in zip(A[m],dx2[m]):
        tot+=Ai*np.mean(D/(d2*(d2+D)**1.5))
    return 0.25*tot/Nx*U
for eb,pb in [((1.0,2.0),(1.0,2.0)),((2.0,3.0),(2.0,3.0)),((2.5,3.1),(None,None)),((2.5,3.1),(0.5,1.0)),((2.5,3.1),(2.5,3.1)),((2.5,3.1),(2.276578,2.876578)),((2.8,3.1),(None,None)),((2.8,3.1),(2.8,3.1)),((2.8,3.1),(2.5,3.1))]:
    law=Law(eb[0],eb[1],0.0,pb[0],pb[1],1.0)
    v1=hires(law,4000,96); v2=hires(law,8000,160)
    print('e-box %-11s photon-box %-22s  dc_inf*U = %+9.4f (Nx=4000,Np=96)  %+9.4f (Nx=8000,Np=160)'%(str(eb),str(pb),v1,v2),flush=True)
