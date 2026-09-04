"""
T316 - the field angular momentum of the framework's charge-monopole composite.

T315 measures the framework's monopole quantum g; R158 gives the matter charge
q = 1. The claim J = qg/(4 pi) should be MEASURED for the framework's own values,
not asserted from a textbook. Compute
      J = integral of  r x (E x B)  d^3r
for a unit charge at -d/2 and a monopole of flux g at +d/2, on a fine grid.
The classic statement is that J is independent of the separation d and points
along the separation axis -- so that independence is the control: if the computed
J drifts with d, the integration is wrong, not the physics.
"""
import numpy as np
def J_of(d,N=260,Lbox=26.0,g=2*np.pi,q=1.0):
    x=np.linspace(-Lbox/2,Lbox/2,N); h=x[1]-x[0]
    X,Y,Z=np.meshgrid(x,x,x,indexing='ij')
    # charge at -d/2 z-hat, monopole at +d/2 z-hat
    rc=np.stack([X,Y,Z+d/2],axis=-1); rm=np.stack([X,Y,Z-d/2],axis=-1)
    nc=np.linalg.norm(rc,axis=-1); nm=np.linalg.norm(rm,axis=-1)
    cut=0.45
    ok=(nc>cut)&(nm>cut)
    nc=np.where(ok,nc,1.0); nm=np.where(ok,nm,1.0)
    E=q/(4*np.pi)*rc/nc[...,None]**3
    B=g/(4*np.pi)*rm/nm[...,None]**3
    S=np.cross(E,B)                       # Poynting-like density
    r=np.stack([X,Y,Z],axis=-1)
    dens=np.cross(r,S)
    dens=np.where(ok[...,None],dens,0.0)
    return dens.sum(axis=(0,1,2))*h**3
print("J = int r x (E x B) for q=1 (R158) and g=2pi (T315: n=1)")
print("control: J must be independent of the separation d, and along z\n")
print("    d      J_x        J_y        J_z        J_z vs qg/4pi = 0.5")
for d in (1.0,2.0,3.0,4.0,6.0):
    J=J_of(d)
    print(f"  {d:4.1f}  {J[0]:+9.2e}  {J[1]:+9.2e}  {J[2]:+8.5f}     ratio {J[2]/0.5:.4f}")
print("\n  qg/(4 pi) with q=1, g=2pi  =  0.5   -> HALF-INTEGER")
