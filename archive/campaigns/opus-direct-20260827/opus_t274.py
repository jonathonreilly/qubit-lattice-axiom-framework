"""
T274 - a D-FREE estimator for b1, validated on exact p=1 data.

R184/R185 divided by a separately-measured D that was wrong by 3.6-5% even at
p=1 (where D=1 exactly).  Avoid it entirely: with no D in the prefactor,
    Rtil(s) = (4 pi s)^{3/2} K2/V2 = A + B s + ...,  A = D^{-3/2},  B = b1 k^2 A^{1/3}
so   D  = A^{-2/3}      and      b1 = B / (k^2 A^{1/3}).
D is recovered from the SAME fit, so no separate estimator can drift.

Fit in the SMALL-x window (tangent, not chord -- R188's named failure mode) at
large L (so s is still big and the 1/s artifact is small).
Calibration that must pass: at p=1 the fit must return A = 1.000 and b1 = 2/9.
"""
import numpy as np
from opus_t269 import heat3

def fit_b1(s, Rtil, kap, terms=('s','s2','inv')):
    cols=[np.ones_like(s)]
    if 's'   in terms: cols.append(s)
    if 's2'  in terms: cols.append(s**2)
    if 'inv' in terms: cols.append(1.0/s)
    M=np.vstack(cols).T
    co=np.linalg.lstsq(M,Rtil,rcond=None)[0]
    A,B=co[0],co[1]
    return A, A**(-2.0/3.0), B/(kap**2*A**(1.0/3.0))

print("D-free estimator, exact d=3 Bloch, p=1.  MUST give A=1.000, D=1.000, b1=2/9=0.22222\n")
print("   L     x window      A         D        b1        dev vs 2/9")
for L in (48,64,96,120):
    kap=2*np.pi/L; h=0.05
    xs=np.linspace(0.04,0.20,9); s=xs/kap**2
    Ks={};Vs={}
    for e in (-2,-1,0,1,2): Ks[e],Vs[e]=heat3(L,e*h,s)
    d2=lambda D:0.5*(-D[2]+16*D[1]-30*D[0]+16*D[-1]-D[-2])/(12*h*h)
    Rtil=(4*np.pi*s)**1.5*d2(Ks)/d2(Vs)
    A,D,b1=fit_b1(s,Rtil,kap)
    print(f"  {L:3d}  {xs[0]:.2f}-{xs[-1]:.2f} (s {s[0]:5.1f}-{s[-1]:5.1f})  {A:8.5f} {D:8.5f} {b1:9.5f}   {b1/(2/9)-1:+7.2%}")

print("\ncontrol: same fit on the WIDE window that produced R188's chord (should fail)")
L=96; kap=2*np.pi/L; h=0.05
xs=np.linspace(0.20,0.60,9); s=xs/kap**2
Ks={};Vs={}
for e in (-2,-1,0,1,2): Ks[e],Vs[e]=heat3(L,e*h,s)
d2=lambda D:0.5*(-D[2]+16*D[1]-30*D[0]+16*D[-1]-D[-2])/(12*h*h)
A,D,b1=fit_b1(s,(4*np.pi*s)**1.5*d2(Ks)/d2(Vs),kap)
print(f"  L= 96  0.20-0.60             {A:8.5f} {D:8.5f} {b1:9.5f}   {b1/(2/9)-1:+7.2%}")
