#!/usr/bin/env python3
"""A22 (supplied toy): n-excitation quasi-energies relative to the emptiness lie in the arc [0, n(2 th_e + 2 th_o + J)]
(monotone-path lemma) for the S1 brickwork with diagonal NNN phases e^{+iJ n_s n_s+2}; so for n(...) < 2 pi no
time-umklapp is possible in the n-body sector.  Compare with A19's full-swap round, whose arcs wrap."""
import numpy as np
from itertools import combinations
L = 12
def sector(n):
    st = np.array(sorted(sum(1 << (L - 1 - s) for s in c) for c in combinations(range(L), n)), dtype=np.int64)
    bits = (st[:, None] >> (L - 1 - np.arange(L))[None, :]) & 1
    perms = []
    for s in range(L):
        t = (s + 1) % L; bs, bt = bits[:, s], bits[:, t]
        perms.append(np.searchsorted(st, st ^ (((bs ^ bt) << (L - 1 - s)) | ((bs ^ bt) << (L - 1 - t)))))
    return st, bits, perms
def step_matrix(n, te, to, J):
    st, bits, perms = sector(n)
    D = st.size
    Vd = sum(bits[:, s] * bits[:, (s + 2) % L] for s in range(L)).astype(float)
    U = np.eye(D, dtype=complex)
    for par, th in ((0, te), (1, to)):
        for s in range(par, L, 2):
            U = np.cos(th) * U - 1j * np.sin(th) * U[perms[s], :]
    U = np.exp(1j * J * Vd)[:, None] * U
    lam_vac = np.exp(-1j * L * (te + to) / 2 * 2 / 2) ** 1   # vacuum: e^{-i theta} per bond: L/2 bonds per layer
    lam_vac = np.exp(-1j * (L // 2) * (te + to))
    ph = np.angle(np.linalg.eigvals(U) / lam_vac) % (2 * np.pi)
    return ph
for (te, to, J, lab) in ((0.1, 0.1, 0.1, "small steps"), (0.25, 0.2, 0.2, "moderate"), (np.pi / 2, np.pi / 2 - 0.3, 0.0, "A19 full-swap round")):
    for n in (1, 2, 3):
        ph = step_matrix(n, te, to, J)
        # smallest arc containing all phases: 2pi minus the largest gap
        s = np.sort(ph); gaps = np.diff(np.concatenate([s, [s[0] + 2 * np.pi]]))
        arc = 2 * np.pi - gaps.max()
        bound = n * (2 * te + 2 * to + J)
        print(f"{lab:20s} n={n}: phases in [{s.min():.4f}, {s.max():.4f}], occupied arc {arc:.4f}, lemma bound n(2te+2to+J) = {bound:.4f}"
              f"  -> {'no umklapp (arc < 2pi)' if bound < 2*np.pi else 'bound >= 2pi: wraps possible'}")
