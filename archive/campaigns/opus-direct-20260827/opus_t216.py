"""
T216 - does the record field have MASSLESS modes at the Born point lam = 1?

A continuum limit needs scale-free (massless) excitations.  Criticality is one
route; a broken continuous symmetry is another -- Goldstone modes are massless
throughout the ordered phase.  Decisive test on the structure factor:

    massless :  S(k) ~ 1/k^2   as k -> 0   =>  S(k)*k^2 approaches a constant
    massive  :  S(k) ~ 1/(k^2+m^2)         =>  S(k) itself approaches a constant

Measured at lam = 0.50 (disordered), 0.70 (near lam_c) and 1.00 (Born point).
"""
import numpy as np, sys

def sweep(v, lam, rng, mask, ncone):
    nb = (np.roll(v,1,0), np.roll(v,-1,0), np.roll(v,1,1),
          np.roll(v,-1,1), np.roll(v,1,2), np.roll(v,-1,2))
    prop = v + ncone*rng.normal(size=v.shape)
    prop /= np.linalg.norm(prop, axis=-1, keepdims=True)
    wold = np.ones(v.shape[:3]); wnew = np.ones(v.shape[:3])
    for n in nb:
        wold *= 1 + lam*np.sum(v*n, axis=-1)
        wnew *= 1 + lam*np.sum(prop*n, axis=-1)
    acc = (rng.random(v.shape[:3]) < np.clip(wnew/np.maximum(wold,1e-300),0,1)) & mask
    v[acc] = prop[acc]
    return acc[mask].mean()

def structure(L, lam, nwarm=4000, nmeas=8000, seed=5):
    rng = np.random.default_rng(seed)
    v = rng.normal(size=(L,L,L,3)); v /= np.linalg.norm(v,axis=-1,keepdims=True)
    i,j,k = np.indices((L,L,L)); A = ((i+j+k)%2==0); B=~A
    ncone = 1.0
    for t in range(nwarm):
        a = 0.5*(sweep(v,lam,rng,A,ncone)+sweep(v,lam,rng,B,ncone))
        if t%100==99:
            ncone *= 1.15 if a>0.55 else (0.87 if a<0.35 else 1.0)
            ncone = min(max(ncone,0.05),4.0)
    S = np.zeros((L,L,L)); n=0
    for t in range(nmeas):
        sweep(v,lam,rng,A,ncone); sweep(v,lam,rng,B,ncone)
        if t%4==0:
            f = np.fft.fftn(v, axes=(0,1,2))
            S += np.sum(np.abs(f)**2, axis=-1); n+=1
    return S/(n*L**3)

L = int(sys.argv[1]) if len(sys.argv)>1 else 12
print(f"L = {L};  k_n = 2 pi n / L along one axis;  khat^2 = 4 sin^2(k/2) (lattice)")
for lam in (0.50, 0.70, 1.00):
    S = structure(L, lam)
    print(f"\n lam = {lam:4.2f}   (S(0)/L^3 = {S[0,0,0]/L**3:.4f}  <- order parameter)")
    print("   n    k        khat^2       S(k)        S(k)*khat^2")
    for nn in (1,2,3,4,5):
        k = 2*np.pi*nn/L; kh2 = 4*np.sin(k/2)**2
        s = (S[nn,0,0]+S[0,nn,0]+S[0,0,nn])/3
        print(f"   {nn}  {k:6.3f}   {kh2:9.5f}  {s:11.3f}   {s*kh2:11.4f}")
