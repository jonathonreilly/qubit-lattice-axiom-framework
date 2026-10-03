"""A46 ed16_def: exact (enumeration) dual-frame (e_J', e_K', ring) on the 16-site cubic cluster for the
soldered ansatz with face-diagonal deformations t2 / lam2 (validation of vmc_def.py)."""
import sys, signal, numpy as np
signal.alarm(200)
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from a46lib import *
cl = Cluster([[2, 2, 0], [2, 0, 2], [0, 2, 2]]); N = cl.N; bits = bits_table(N); plaq = plaquettes(cl)
mats = sparse_terms(cl); HJ, HK = mats["J"], mats["K"]; del mats; HR = ring_sparse(cl, plaq)
for t2, l2 in ((0., 0.), (0.2, 0.), (0.4, 0.), (0., 0.2), (0., 0.4)):
    Phi, gap = mf_dual(cl, 0., 1., t2=t2, lam2=l2)
    if gap < 1e-8: print(f"t2={t2} lam2={l2}: open shell"); continue
    p = projected_vector(Phi, bits); p /= np.linalg.norm(p)
    v = [np.vdot(p, M @ p).real / (3 * N) for M in (HJ, HK, HR)]
    print(f"t2={t2} lam2={l2}: gap {gap:.3f}; exact (e_J', e_K', ring) = ({v[0]:+.5f}, {v[1]:+.5f}, {v[2]:+.5f})")
