#!/usr/bin/env python3
"""C7_check C2: the k -> k + pi(1,1,1) spectral coincidence of 1c+11 and of the real 1011 control is not implemented by any
k-independent unitary or antiunitary 12x12 operator (Sylvester null-space test on 6 random k); it equals the exact
isospectrality t2 -> -t2.  Usage: python3 k7_C2_isospectral.py <dir of k7_geom.py>"""
import sys, itertools, numpy as np
sys.path.insert(0, sys.argv[1])
from k7_geom import *
L1=Lat(1); rng=np.random.default_rng(0)
base=maj_amp(L1,np.zeros(36,np.uint8),1,1)
x0=solve_gauge(L1,base,maj_targets(L1,1,'c+',1,1))
baseR=-np.ones(36,complex)
tgR=np.array([np.pi*{'square':1,'triangle':0,'plaquette':1,'tube':1}[k] for k,_,_ in L1.faces])
xR=solve_gauge(L1,baseR,tgR)
d=np.pi*np.ones(3)
for nm,A in (('1c+11',maj_amp(L1,x0,1,.37)),('1011',(-np.where(L1.onsite,-1.0,0.37)*(-1.0)**xR).astype(complex))):
    ks=rng.uniform(0,2*np.pi,(6,3))
    for kind in ('unitary k->k+pi111','antiunitary k->-k+pi111','unitary k->-k+pi111 with H->-H'):
        rows=[]
        for k in ks:
            if kind.startswith('unitary k->k'):
                Hs=L1.bloch(A,k[None])[0]; Ht=L1.bloch(A,(k+d)[None])[0]
            elif kind.startswith('anti'):
                Hs=L1.bloch(A,k[None])[0].conj(); Ht=L1.bloch(A,(-k+d)[None])[0]
            else:
                Hs=-L1.bloch(A,k[None])[0]; Ht=L1.bloch(A,(-k+d)[None])[0]
            # U Hs = Ht U  ->  (I kron Ht - Hs^T kron I) vec(U) = 0  (column-major vec)
            n=12; rows.append(np.kron(np.eye(n),Ht)-np.kron(Hs.T,np.eye(n)))
        Mx=np.vstack(rows); sv=np.linalg.svd(Mx,compute_uv=False)
        print(nm,kind,'null dim',int(np.sum(sv<1e-8)))
    # does the t2 -> -t2 map give the same spectrum?
    Ap=A.copy(); Ap[~L1.onsite]*=-1
    kk=rng.uniform(0,2*np.pi,(20,3))
    print(nm,'E_{t2}(k) vs E_{-t2}(k): %.1e'%np.abs(np.linalg.eigvalsh(L1.bloch(A,kk))-np.linalg.eigvalsh(L1.bloch(Ap,kk))).max())
    print(nm,'spec(H(k)) = -spec(H(k)) per k: %.1e'%np.abs(np.linalg.eigvalsh(L1.bloch(A,kk))+np.linalg.eigvalsh(L1.bloch(A,kk))[:,::-1]).max())
