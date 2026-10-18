#!/usr/bin/env python3
"""Controls for probe G1: (a) detection power: break gauge invariance with B_4 forms
and verify the dispersion routine sees anisotropy/extra modes; (b) count zero-derivative
(mass) forms h.M.h under SO(4) vs B_4 and how many are gauge invariant (expect 0)."""
import itertools, numpy as np
from probe_spin2_hypercubic_isotropy import (sym_basis, group_action, lie_action, nullspace,
    signed_perm_generators, so_generators, count_forms, permute_axes, dispersion)
rng = np.random.default_rng(7)
d = 4
# (b) mass forms: T[mu,nu,rho,sigma]
n = 4
S = sym_basis(d, n, [(1, 0, 2, 3), (0, 1, 3, 2), (2, 3, 0, 1)])
for grp in ("SO", "B4"):
    rows = ([group_action(S, n, d, R) - S for R in signed_perm_generators(d)] if grp == "B4"
            else [lie_action(S, n, d, L) for L in so_generators(d)])
    B = S @ nullspace(np.vstack(rows))
    # gauge: delta h = k xi + xi k ; mass form gauge-invariant iff T[mu,nu,rho,sigma] k_rho xi_sigma = 0 for all k,xi -> T=0
    print(f"zero-derivative (mass) forms d=4 {grp}: invariant={B.shape[1]}, gauge-invariant=0 (T.k xi=0 forces T=0)")
# (a) detection power
n = 6
swaps = [(1, 0, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5), (2, 3, 0, 1, 4, 5), (0, 1, 2, 3, 5, 4)]
S = sym_basis(d, n, swaps)
B4 = S @ nullspace(np.vstack([group_action(S, n, d, R) - S for R in signed_perm_generators(d)]))
SO = S @ nullspace(np.vstack([lie_action(S, n, d, L) for L in so_generators(d)]))
_, _, EH = count_forms(4, 2, "SO")
eh = EH[:, 0]
# extra B4 directions orthogonal to all SO(4) forms (pure lattice-anisotropic, non-gauge-invariant)
P = SO @ np.linalg.pinv(SO)
X = B4 - P @ B4
u, s, vt = np.linalg.svd(X, full_matrices=False)
X = u[:, s > 1e-8]
print(f"B4 two-derivative forms with no SO(4) component: {X.shape[1]}")
dirs = {"[100]": (1, 0, 0), "[110]": (1, 1, 0), "[111]": (1, 1, 1)}
for eps in (0.02, 0.1):
    c = rng.normal(size=X.shape[1]); c *= eps * np.linalg.norm(eh) / np.linalg.norm(c)
    T = eh + X @ c
    print(f"gauge-BREAKING B4 admixture eps={eps}:")
    for k, v in dirs.items():
        print(f"  {k}: {dispersion(T, v)}")
