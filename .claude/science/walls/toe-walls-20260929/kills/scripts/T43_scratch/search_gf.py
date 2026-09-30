import numpy as np, itertools
from stag import *
def symprod(lat,U,order=None):
    d=lat.d; Nc=U.shape[-1]
    C=[]
    for mu in range(d):
        T=fwd_shift(lat,U,mu); C.append(0.5*(T+T.conj().T))
    S=None
    for perm in itertools.permutations(range(d)):
        P=C[perm[0]]
        for m in perm[1:]: P=P@C[m]
        S=P if S is None else S+P
    import math
    return S/math.factorial(d)
for d,L in [(4,6)]:
    lat=Lat(L,d); U0=np.ones((lat.V,d,1,1),complex)
    S=symprod(lat,U0).toarray(); D=stag_D(lat,U0).toarray()
    found=[]
    for a in itertools.product((0,1),repeat=d):
        for ph in (1,1j):
            z=ph*(-1.0)**(lat.coords@np.array(a))
            G=np.diag(z)@S
            herm=np.abs(G-G.conj().T).max(); anti=np.abs(G@D+D@G).max()
            if herm<1e-12 and anti<1e-12: found.append((a,ph))
    print(d,L,found)
