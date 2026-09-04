"""
T295 - h is exactly neutral in the EXACT computation (T294), yet the stochastic
pipeline moved 5.6% when h went 0.05 -> 0.10. So the defect is inside the
stochastic/Chebyshev path, not the stencil. Isolate it at p=1, L=48, where the
exact answer is known (T294): Rtil = 1.2132 1.1516 1.1349 1.1435 1.1698.

Suspect: lmax = ||B||_inf (Gershgorin) grows with eps, and the Chebyshev order
is set from it as 1.35*s_max*lmax/2 + 70. If that order rule is too thin at the
larger lmax that eps = +-0.2 produces, the expansion is under-resolved -- and
the error would be systematic, not noise, exactly as observed.
"""
import numpy as np
from scipy.sparse import diags
from opus_t288 import build, giant, cheb_trace, K_pure
EX=np.array([1.2132,1.1516,1.1349,1.1435,1.1698])
L=48; xs=np.array([0.10,0.16,0.24,0.34,0.46]); kap=2*np.pi/L; s=xs/kap**2
g=giant(L,1.00,11); idx=np.where(g)[0]; n=len(idx)
def run(h,nz,omul):
    rng=np.random.default_rng(101); Z=rng.choice([-1.0,1.0],size=(n,nz))
    Ks={};Vs={};lm=[]
    for ei in (-2,-1,0,1,2):
        A,m=build(L,ei*h,g); ms=m[idx]
        Dm=diags(1.0/np.sqrt(ms)); B=(Dm@A[idx][:,idx]@Dm).tocsr()
        lmax=float(abs(B).sum(axis=1).max())*1.02; lm.append(lmax)
        Ks[ei]=cheb_trace(B,s,Z,lmax*omul); Vs[ei]=ms.sum()
    d2=lambda D:0.5*(-D[2]+16*D[1]-30*D[0]+16*D[-1]-D[-2])/(12*h*h)
    return (4*np.pi*s)**1.5*d2(Ks)/d2(Vs), lm
print("exact (T294):        "+" ".join(f"{v:7.4f}" for v in EX))
for h,nz in ((0.05,32),(0.05,96),(0.10,96)):
    r,lm=run(h,nz,1.0)
    print(f"h={h:.2f} nz={nz:3d}  "+" ".join(f"{v:7.4f}" for v in r)
          +"   dev "+" ".join(f"{v:+6.2%}" for v in r/EX-1)+f"   lmax {min(lm):.2f}-{max(lm):.2f}")
print("\nsame, with the Chebyshev order rule doubled (order *= 2 via lmax*2):")
for h,nz in ((0.10,96),):
    r,lm=run(h,nz,2.0)
    print(f"h={h:.2f} nz={nz:3d}  "+" ".join(f"{v:7.4f}" for v in r)
          +"   dev "+" ".join(f"{v:+6.2%}" for v in r/EX-1))
