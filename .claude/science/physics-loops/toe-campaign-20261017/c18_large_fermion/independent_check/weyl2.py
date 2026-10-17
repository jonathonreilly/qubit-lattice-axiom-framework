"""For every O x T symmetrized second-neighbour term: Kramers splitting at random k and the
linear (Weyl) coefficient alpha at k*, with strength delta = 0.02 on the set (t1,t2,lam)=(-1,0.1,-0.5)."""
import numpy as np
from perturb import *
rng = np.random.default_rng(5)
res = candidates(rng)
p = (-1.0, 0.1, -0.5); delta = 0.02
ks_r = rng.uniform(-np.pi, np.pi, (100, 3))
for kinds, c2, sh, zn, nrm, ikb, hops in res:
    H = lambda k: bloch(u, k, *p) + delta * Xsym(hops, k)
    spl = max(np.max(np.abs(np.diff(np.linalg.eigvalsh(H(k)))[0::2])) for k in ks_r)
    a = np.linalg.eigvalsh(H(KP))[0]; b = np.linalg.eigvalsh(H(-KP))[0]; ks = KP if a < b else -KP
    q = 1e-4; e = np.linalg.eigvalsh(H(ks + q * np.array([1., 2, -0.5]) / np.linalg.norm([1, 2, -0.5])))
    print(f"{str(kinds):12s} 0->{str(CORN[c2]):7s}@{str(sh):11s} amp {zn}: I*K {'broken' if ikb>1e-9 else 'kept  '}  "
          f"max Kramers split (100 k) {spl:.1e}  alpha/delta at k* {(e[1]-e[0])/(2*q)/delta:.4f}")
