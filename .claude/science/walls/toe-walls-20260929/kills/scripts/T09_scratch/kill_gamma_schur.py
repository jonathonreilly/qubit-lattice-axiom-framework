"""Schur check: for an irreducible carrier, any covariant H(k=0) is a scalar -> the bands are degenerate at Gamma (no mass gap).
Also at R=(pi,pi,pi).  Compute, for random covariant Hermitian H in the attack's basis, the eigenvalue spread of H(0) and H(pi,pi,pi)."""
import numpy as np
from kill_gap import herm_basis, Hk
from common import *
rng = np.random.default_rng(2)
for names in (['H1'], ['H2'], ['E'], ['G'], ['H1','H1'], ['H1','H2']):
    s,n0,nN,N,b0,bN = herm_basis(names); nb = n0+nN
    sp0=[];spR=[]
    for _ in range(20):
        v = N@rng.normal(size=N.shape[1]); c = v[0::2]+1j*v[1::2]
        e0 = np.linalg.eigvalsh(Hk(c,s,n0,b0,bN,np.zeros(3))); eR = np.linalg.eigvalsh(Hk(c,s,n0,b0,bN,np.pi*np.ones(3)))
        sp0.append(np.ptp(e0)); spR.append(np.ptp(eR))
    print(f"{'+'.join(names):6s} s={s}: max eigenvalue spread of H(Gamma) over 20 random covariant H = {max(sp0):.2e};  H(R=(pi,pi,pi)) = {max(spR):.2e}")
