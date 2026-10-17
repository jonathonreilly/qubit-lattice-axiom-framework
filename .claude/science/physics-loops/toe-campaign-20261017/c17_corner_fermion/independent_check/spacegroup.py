"""Fermion level: do rotations about the origin and translations combine without extra signs?
Computes G_R G_Ta G_R^-1 = s * G_{T_{Ra}} for default flux."""
import numpy as np
from fermion import *
import sys; fl = [int(t) for t in sys.argv[1:5]] if len(sys.argv) > 4 else [-1, 1, -1, 1]
u, Gs, sq, comm = run_psg(dict(zip(['square','triangle','plaquette','tube'], fl)))
def inv(Gop):
    cm = [None]*nc; g = np.zeros(nc, complex)
    for j in range(nc):
        cm[Gop.cmap[j]] = j
    # A|j> = g[A j]|A j>;  A^-1 |A j> = 1/g[A j] |j>
    for j in range(nc):
        g[j] = 1 / Gop.g[Gop.cmap[j]]
    return SPOp(cm, g)
Ts = {}
for a in [(1,0,0),(0,1,0),(0,0,1),(-1,0,0),(0,-1,0),(0,0,-1)]:
    cm = corner_map(lambda c, a=a: lat.corner(add(lat.corner_info(c)[0], a), lat.corner_info(c)[1]))
    Ts[a] = SPOp(cm, psg_gauge(u, cm))
res = {}
for i, M in enumerate(Ms):
    for a in [(1,0,0),(0,1,0),(0,0,1)]:
        Ra = rot_vec(M, a)
        X = Gs[i].mul(Ts[a]).mul(inv(Gs[i]))
        s = X.scalar_ratio(Ts[Ra])
        res.setdefault(classify(M), set()).add(complex(np.round(s, 6)))
print({k: v for k, v in res.items()})
inv_res = {}
for i, M in enumerate(Ms):
    for a in [(1,0,0),(0,1,0),(0,0,1)]:
        Ra = rot_vec(M, a)
        X = Gs[i].mul(Ts[a]).mul(inv(Gs[i]))
        if Ra == a:
            s = X.mul(inv(Ts[a])).scalar_ratio(SPOp(range(nc), np.ones(nc)))
            inv_res.setdefault((classify(M), 'Ra=a'), set()).add(round(s.real))
        elif Ra == tuple(-t for t in a):
            s = X.mul(Ts[a]).scalar_ratio(SPOp(range(nc), np.ones(nc)))
            inv_res.setdefault((classify(M), 'Ra=-a'), set()).add(round(s.real))
print('gauge-invariant R T_a R^-1 T_{Ra}^-1 signs:', inv_res)
