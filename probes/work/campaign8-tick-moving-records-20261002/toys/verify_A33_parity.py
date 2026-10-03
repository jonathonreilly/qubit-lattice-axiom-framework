#!/usr/bin/env python3
"""Coordinator's check of A33's parity formula: for a one-state-per-site excitation on a plaquette (x, a, c, b) with a
symmetry g fixing x and c and swapping a <-> b, acting as U_g|y> = p(y)|g y>, any g-invariant Hermitian hopping has
plaquette flux t(x,a) t(a,c) t(c,b) t(b,x) = |t(x,a)|^2 |t(a,c)|^2 p(x) p(c)  (so pi flux iff p(x) p(c) = -1)."""
import numpy as np
rng = np.random.default_rng(9)
x, a, c, b = 0, 1, 2, 3
perm = {x: x, a: b, c: c, b: a}
worst = 0.0; signs = {}
for trial in range(2000):
    p = rng.choice([1, -1], size=4)
    U = np.zeros((4, 4))
    for y in range(4):
        U[perm[y], y] = p[y]
    H = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4)); H = H + H.conj().T
    Hs = sum(np.linalg.matrix_power(U, k) @ H @ np.linalg.matrix_power(U, k).T for k in range(4)) / 4   # invariant under <U> (U^4 = 1)
    assert np.allclose(U @ Hs @ U.T, Hs)
    t = lambda i, j: Hs[j, i]              # amplitude i -> j
    flux = t(x, a) * t(a, c) * t(c, b) * t(b, x)
    pred = abs(t(x, a))**2 * abs(t(a, c))**2 * p[x] * p[c]
    worst = max(worst, abs(flux - pred) / max(1e-12, abs(pred)))
    key = int(p[x] * p[c])
    if abs(flux) > 1e-8:
        signs.setdefault(key, set()).add(int(np.sign(flux.real)))
    else:
        signs.setdefault('zero (an amplitude vanishes by symmetry)', set()).add(key)
print("max relative deviation of flux from |t_xa|^2 |t_ac|^2 p(x) p(c): %.2e" % worst)
print("sign of the (real) flux by p(x)p(c):", {k: sorted(v) for k, v in signs.items()})
