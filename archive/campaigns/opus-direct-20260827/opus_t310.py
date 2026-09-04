"""
T310 - verify tau0 = 0.04297 a^2 independently, hence ell_P/a as a DERIVED number.

R152's ell_P ~ 0.52a rests on tau0 = 0.04297 a^2, and R195 has now derived the
mode count N=6 that multiplies it. If tau0 is itself derived, then ell_P/a is a
parameter-free number the framework produces -- which bears on the axioms doc's
named open gate, "the framework's natural unit equals the Planck length".

Provenance (packet line 5451): matching dW/dm^2 for a massless scalar,
   lattice:   dW/dm^2 = -(1/2) sum_{lambda != 0} 1/lambda
   continuum: dW/dm^2 = (1/2) Vol/(16 pi^2 tau0)     [d=4 proper-time cutoff]
so tau0 = Vol / (16 pi^2 sum 1/lambda). In lattice units (a=1, Vol=N) this is
   tau0 = 1 / (16 pi^2 I),      I = (1/N) sum_{k != 0} 1/lambda(k)
i.e. I is the d=4 lattice Green's function at the origin -- a pure number, no
free parameters.

Computed three ways: direct BZ sum at several L (extrapolated), Gauss-Legendre
quadrature over the Brillouin zone, and the Bessel/proper-time integral
   I = int_0^inf dt [e^{-2t} I_0(2t)]^4 ,
which are independent representations of the same constant.
"""
import numpy as np
from scipy.special import ive
from scipy.integrate import quad
from numpy.polynomial.legendre import leggauss

print("route 1 - direct Brillouin-zone sum, extrapolated in 1/L^2")
vals=[]
for L in (24,32,48,64,80):
    k=2*np.pi*np.arange(L)/L; c=2*(1-np.cos(k))
    lam=c[:,None,None,None]+c[None,:,None,None]+c[None,None,:,None]+c[None,None,None,:]
    lam=lam.ravel(); lam=lam[lam>1e-12]
    I=np.sum(1.0/lam)/L**4
    vals.append((L,I)); print(f"    L={L:3d}   I = {I:.8f}   tau0 = {1/(16*np.pi**2*I):.6f}")
x=np.array([1.0/v[0]**2 for v in vals]); y=np.array([v[1] for v in vals])
I_ex=np.polyfit(x,y,1)[1]
print(f"    extrapolated L->inf:  I = {I_ex:.8f}   tau0 = {1/(16*np.pi**2*I_ex):.6f}")

print("\nroute 2 - proper-time / Bessel representation  I = int_0^inf [e^{-2t}I_0(2t)]^4 dt")
f=lambda t: ive(0,2*t)**4
I2=quad(f,0,np.inf,limit=400)[0]
print(f"    I = {I2:.8f}   tau0 = {1/(16*np.pi**2*I2):.6f}")

print("\nroute 3 - Gauss-Legendre quadrature over the BZ")
for nq in (200,400):
    xg,wg=leggauss(nq); kk=np.pi*(xg+1)/2; ww=wg*np.pi/2
    c=2*(1-np.cos(kk))
    tot=0.0
    for a in range(nq):
        for b in range(nq):
            s=c[a]+c[b]
            tot+=ww[a]*ww[b]*np.sum(ww[:,None]*ww[None,:]/(s+c[:,None]+c[None,:]))
    I3=tot/np.pi**4
    print(f"    nq={nq}   I = {I3:.8f}   tau0 = {1/(16*np.pi**2*I3):.6f}")

print(f"\n  packet value (R152): tau0 = 0.04297 a^2")
t0=1/(16*np.pi**2*I2)
print(f"  this computation:    tau0 = {t0:.6f} a^2      dev {t0/0.04297-1:+.3%}")
print(f"\n  with R195's N = 6:  G = 2 pi tau0 = {2*np.pi*t0:.6f} a^2")
print(f"                      ell_P = sqrt(G) = {np.sqrt(2*np.pi*t0):.4f} a")
