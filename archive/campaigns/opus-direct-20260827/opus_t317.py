"""
T317 - J = qg/4pi, computed properly (T316's box was too small).

T316 integrated on a 26-unit cube and got J_z = 0.37..0.44, drifting with the
separation d -- and d-independence is the control, so that computation is void.
The reason: at large r the charge and monopole fields become PARALLEL, so
E x B -> 0 and the tail cancels delicately; truncating the box breaks the
cancellation.

Do it in spherical coordinates about the charge, integrating the angles exactly
by Gauss-Legendre and the radius out to a controlled cutoff, then check
convergence in that cutoff AND independence of d -- both controls, stated first.
"""
import numpy as np
from numpy.polynomial.legendre import leggauss
def Jz(d,Rmax,nr=4000,nt=200,np_=8,q=1.0,g=2*np.pi):
    # spherical about the CHARGE at origin; monopole at d*zhat
    xr,wr=leggauss(nr); r=Rmax*(xr+1)/2*0.5+1e-6; wrr=wr*Rmax/4
    r=np.exp(np.linspace(np.log(1e-3),np.log(Rmax),nr))          # log grid
    dr=np.gradient(r)
    xt,wt=leggauss(nt); ct=xt; st=np.sqrt(1-ct**2)
    tot=0.0
    for i,rr in enumerate(r):
        # position vectors
        z=rr*ct; rho=rr*st
        # E from charge at origin (radial), B from monopole at d zhat
        Ex=q/(4*np.pi)*rho/rr**3; Ez=q/(4*np.pi)*z/rr**3
        mx=rho; mz=z-d; mn=np.sqrt(mx**2+mz**2); mn=np.where(mn<1e-9,1e-9,mn)
        Bx=g/(4*np.pi)*mx/mn**3; Bz=g/(4*np.pi)*mz/mn**3
        # S = E x B ; with E,B in the (rho,z) plane, S is purely azimuthal
        Sphi=Ez*Bx-Ex*Bz
        # J_z = integral of (r x S)_z = rho * Sphi
        integ=rho*Sphi
        tot+=np.sum(wt*integ*rr**2)*2*np.pi*dr[i]
    return tot
print("J_z for q=1 (R158), g=2pi (T315).   target qg/4pi = 0.5")
print("controls: (a) converge in Rmax, (b) independent of the separation d\n")
print("    d        Rmax=50     Rmax=200    Rmax=1000   Rmax=5000")
for d in (1.0,2.0,4.0):
    vals=[Jz(d,R) for R in (50,200,1000,5000)]
    print(f"  {d:4.1f}   "+"   ".join(f"{v:9.6f}" for v in vals))
print("\n  (a) fixed d, rising Rmax -> the tail cancellation is captured")
print("  (b) fixed Rmax, varying d -> J must not move")
