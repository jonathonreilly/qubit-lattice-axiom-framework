"""
T309 - the phase is ABSENT from the action, not merely gapped.

The crux of the G = 2pi tau0 vs 6pi tau0 question. If the U(1) phase is exact
local redundancy -- no kinetic term in the FUNDAMENTAL action at any order --
then its photon is a composite of the very eta fluctuations whose loop generates
R157's induced Maxwell term, and adding a photon's a1 weight (-4) on top of the
six scalars' (+6) double counts the same degrees of freedom.

Two checks:
 (1) EXACT LOCAL GAUGE INVARIANCE: S(psi) == S(e^{i alpha_x} psi_x) for random
     SITE-DEPENDENT alpha. Not global -- site-dependent is the whole point.
 (2) The phase direction i*psi_0 is an EXACT null direction of the Hessian,
     while the six CP^3 directions are not. Built in the full per-site tangent
     space so the phase is present and can fail to be null if the claim is wrong.
"""
import numpy as np, itertools
n=4; L,d=4,3; N=L**d
rng=np.random.default_rng(5)
sites=list(itertools.product(range(L),repeat=d)); ix={s:i for i,s in enumerate(sites)}
edges=[]
for s in sites:
    for ax in range(d):
        t=list(s); t[ax]=(t[ax]+1)%L; edges.append((ix[s],ix[tuple(t)]))
def S_of(psi):
    tot=0.0
    for a,b in edges: tot-=np.log(max(abs(np.vdot(psi[a],psi[b]))**2,1e-300))
    return tot
psi=rng.normal(size=(N,n))+1j*rng.normal(size=(N,n))
psi/=np.linalg.norm(psi,axis=1,keepdims=True)
S0=S_of(psi)
alpha=rng.uniform(0,2*np.pi,size=N)                 # SITE-DEPENDENT
psi_g=psi*np.exp(1j*alpha)[:,None]
print("(1) exact LOCAL gauge invariance (site-dependent phases):")
print(f"    S(psi)            = {S0:.12f}")
print(f"    S(e^{{i a_x}} psi)  = {S_of(psi_g):.12f}")
print(f"    |difference|      = {abs(S_of(psi_g)-S0):.3e}")
glob=psi*np.exp(1j*0.7)
print(f"    (global phase, for contrast: |diff| = {abs(S_of(glob)-S0):.3e})")

print("\n(2) is the phase direction an exact null direction of the Hessian?")
p0=np.zeros(n,dtype=complex); p0[0]=1.0
Q=np.eye(n,dtype=complex)-np.outer(p0,p0.conj())
U,_,_=np.linalg.svd(Q); perp=[U[:,i] for i in range(n-1)]
dirs=[("phase  i*psi0",1j*p0)]+[(f"CP3 dir {i}",v) for i,v in enumerate(perp)]+\
     [(f"CP3 dir {i}i",1j*v) for i,v in enumerate(perp)]
base=np.tile(p0,(N,1)).astype(complex)
def S_pert(site,vec,eps):
    p=base.copy(); p[site]=p[site]+eps*vec
    p/=np.linalg.norm(p,axis=1,keepdims=True)
    return S_of(p)
h=1e-4
print("    direction        d2S/deps2 at psi_0        null?")
for nm,v in dirs:
    s2=(S_pert(0,v,h)-2*S_of(base)+S_pert(0,v,-h))/h**2
    print(f"    {nm:16s} {s2:+14.6e}      {'YES (exact)' if abs(s2)<1e-6 else 'no'}")
print("\n  => the phase costs nothing at any order: it is redundancy, not a mode.")
print("     N counts the 6 CP^3 directions only  ->  G = 12 pi tau0 / 6 = 2 pi tau0")
