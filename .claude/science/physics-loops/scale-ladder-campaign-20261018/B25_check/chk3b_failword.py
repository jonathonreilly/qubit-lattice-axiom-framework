#!/usr/bin/env python3
"""B25_check 3b: B25's Fourier-FAIL word S2.P7.S4.H00 -- do its off-grid (3-adic) spectral tastes have k-independent U
intertwiners?  Independent build and solver (out-of-sample validated).  Prints PASS/FAIL, TOTAL."""
import numpy as np, itertools, corelib as cl
W1 = lambda w, k: cl.Wc(w, np.asarray(k, float)[None])[0]
w = cl.build(('S2', 'p', 'S4', 'o'), ('P7', 'H00'))
def U_inter(t):
    r = np.random.default_rng(3); ks = r.uniform(-np.pi, np.pi, (5, 3))
    rows = [np.kron(W1(w, k + t), np.eye(12)) - np.kron(np.eye(12), W1(w, k).T) for k in ks]
    _, s, vh = np.linalg.svd(np.vstack(rows)); null = vh[np.sum(s > 1e-9 * s[0]):].conj()
    if not len(null): return False
    V = ((r.normal(size=len(null)) + 1j * r.normal(size=len(null))) @ null).reshape(12, 12)
    if np.linalg.svd(V, compute_uv=False)[-1] < 1e-6 * np.linalg.norm(V, 2): return False
    return all(np.allclose(W1(w, k + t) @ V, V @ W1(w, k), atol=1e-8) for k in r.uniform(-np.pi, np.pi, (4, 3)))
def spectral(t):
    ks = np.random.default_rng(4).uniform(-np.pi, np.pi, (3, 3))
    f = lambda k: np.sort(np.mod(np.angle(np.linalg.eigvals(W1(w, k))), 2 * np.pi))
    return all(np.abs(np.exp(1j * f(k + t)) - np.exp(1j * f(k))).max() < 1e-7 for k in ks)
ts = [np.pi / 3 * np.array([1, 0, 0]), np.pi / 6 * np.ones(3), 2 * np.pi / 3 * np.ones(3), np.pi / 3 * np.array([1, 1, 0]), np.pi / 6 * np.array([1, 0, 0])]
res = [(np.round(t / np.pi, 4).tolist(), spectral(t), U_inter(t)) for t in ts]
for r in res: print("  t/pi", r[0], "spectral", r[1], "U", r[2])
ok = all(s == u for _, s, u in res) and sum(s for _, s, _ in res) >= 3
print(f"[{'PASS' if ok else 'FAIL'}] every tested off-grid spectral taste of S2.P7.S4.H00 has a k-independent U intertwiner (and non-tastes have none)")
print(f"\nTOTAL: PASS={int(ok)} FAIL={int(not ok)}")
