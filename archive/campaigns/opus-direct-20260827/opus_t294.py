"""
T294 - how big is the finite-difference systematic in h?  (exact, p=1)

Raising h from 0.05 to 0.10 to buy signal-to-noise moved the L=48 control by 6%
at the largest x. The 5-point stencil is O(h^4), but the eps-expansion's
effective parameter is eps^2 * s -- s multiplies the perturbation inside
exp(-s lambda(eps)) -- and at s ~ 27 with eps_max = 2h = 0.2 that is O(1).
So h buys S/N (as h^2) and pays a systematic; this measures the exchange rate
EXACTLY, using the d=3 Bloch operator (no stochastic noise at all).
"""
import numpy as np
from opus_t269 import heat3
def Rtil_h(L,h,xs):
    kap=2*np.pi/L; s=xs/kap**2
    Ks={};Vs={}
    for e in (-2,-1,0,1,2): Ks[e],Vs[e]=heat3(L,e*h,s)
    d2=lambda D:0.5*(-D[2]+16*D[1]-30*D[0]+16*D[-1]-D[-2])/(12*h*h)
    return (4*np.pi*s)**1.5*d2(Ks)/d2(Vs)
xs=np.array([0.10,0.16,0.24,0.34,0.46])
for L in (40,48,56):
    print(f"--- L={L}   s = "+" ".join(f"{v:.1f}" for v in xs/(2*np.pi/L)**2))
    ref=Rtil_h(L,0.0125,xs)
    for h in (0.0125,0.025,0.05,0.10):
        r=Rtil_h(L,h,xs)
        print(f"   h={h:.4f}  "+" ".join(f"{v:7.4f}" for v in r)
              +"   dev vs h=0.0125: "+" ".join(f"{v:+6.2%}" for v in r/ref-1))
