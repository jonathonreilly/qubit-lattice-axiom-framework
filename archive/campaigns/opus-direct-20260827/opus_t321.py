"""
T321 - second route to R201: the lattice vacuum energy, computed DIRECTLY.

R201 used the proper-time form |rho_vac| = N/(64 pi^2 tau0^2). But tau0 was
DEFINED (R73) by matching dW/dm^2 -- an a0-dominated quantity -- so using it to
get the a0 vacuum energy risks circularity. The lattice needs no cutoff at all:
    Gamma_E/V = (1/2N) sum_k log lambda(k)      (finite, exactly computable)
                = (1/2) int d^4k/(2pi)^4 log( sum_mu 2(1-cos k_mu) )
This is an independent route to the same number. The log singularity at k=0 is
integrable in d=4 (measure k^3 dk), which is why the lattice answer is finite.

Reported per real scalar so it can be compared with 1/(64 pi^2 tau0^2) = 0.9477.
Controls: convergence in L, and the same quantity by Gauss-Legendre quadrature.
"""
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.special import ive
from scipy.integrate import quad
W4=quad(lambda t: ive(0,2*t)**4,0,np.inf,limit=400)[0]
tau0=1/(16*np.pi**2*W4)
pt=1/(64*np.pi**2*tau0**2)
print(f"proper-time route (R201):  |rho| per scalar = 1/(64 pi^2 tau0^2) = {pt:.6f} a^-4\n")
print("direct lattice route:  (1/2N) sum_k log lambda(k)   [no cutoff]")
print("    L        value        (excluding k=0 zero mode)")
vals=[]
for L in (16,24,32,48,64):
    k=2*np.pi*np.arange(L)/L; c=2*(1-np.cos(k))
    lam=c[:,None,None,None]+c[None,:,None,None]+c[None,None,:,None]+c[None,None,None,:]
    lam=lam.ravel(); lam=lam[lam>1e-12]
    v=0.5*np.sum(np.log(lam))/L**4
    vals.append((L,v)); print(f"  {L:4d}   {v:.7f}")
x=np.array([1.0/v[0]**4 for v in vals]); y=np.array([v[1] for v in vals])
ext=np.polyfit(x,y,1)[1]
print(f"  extrapolated L->inf : {ext:.7f}")
nq=160; xg,wg=leggauss(nq); kk=np.pi*(xg+1)/2; ww=wg*np.pi/2
c=2*(1-np.cos(kk)); tot=0.0
for a in range(nq):
    for b in range(nq):
        s=c[a]+c[b]
        tot+=ww[a]*ww[b]*np.sum(ww[:,None]*ww[None,:]*np.log(s+c[:,None]+c[None,:]))
quadv=0.5*tot/np.pi**4
print(f"  Gauss-Legendre quad : {quadv:.7f}")
print(f"\n  proper-time         : {pt:.7f}")
print(f"  ratio direct/proper : {ext/pt:.5f}")
print()
N=6; G=12*np.pi*tau0/N
for nm,rho1 in (("proper-time",pt),("direct lattice",ext)):
    rho=N*rho1; R=32*np.pi*G*rho; rad=1/np.sqrt(abs(R))
    print(f"  {nm:16s} |rho|={rho:8.4f} a^-4   |R|={R:9.3f} a^-2   radius={rad:.5f} a")
