import numpy as np, itertools, math
from stag import *
L=6; lat=Lat(L,4)
for name,U in [("free",np.ones((lat.V,4,1,1),complex)),("flux(1,1)",u1_flux_links_4d(lat,1,1))]:
    C=[]
    for mu in range(4):
        T=fwd_shift(lat,U,mu); C.append(0.5*(T+T.conj().T))
    S=None
    for perm in itertools.permutations(range(4)):
        P=C[perm[0]]
        for m_ in perm[1:]: P=P@C[m_]
        S=P if S is None else S+P
    S=S/24
    z=(-1.0)**(lat.coords@np.array([1,0,1,0]))
    G=(sp.diags(z)@S).toarray()
    Os=singlet_op(lat,U,True).toarray()
    dev=min(np.abs(G-Os).max(),np.abs(G+Os).max())
    print(name,"Gamma_f(4D, zeta=(-1)^{x1+x3}) == +-spin-taste singlet: dev=",f"{dev:.2e}")
