"""Refuting pass, block 28 (independent machinery): (a) the six-axis formation law at (p,1,2) from a RANDOM start (spontaneous order:
fraction of the majority value), a different observable and start from the control's aligned-start memory; (b) the six-axis static law by
single-site Metropolis (a different algorithm from the control's heat-bath), from an aligned start; (c) the sphere static law from a
random start with the heat bath; (d) the healing bound tested directly: islands of size D in the noisy automaton at eps = 10^-3, the
survival frequency against 18 (D+1)^3 eps."""
import numpy as np, sys, time
rng = np.random.default_rng(31)
def phi_of(p, q=1.0, r=2.0):
    phi = np.full((6, 6), r)
    for v in range(6): phi[v, v] = p; phi[v, v ^ 1] = q
    return phi
print("(a) six-axis formation law at (p,1,2), L=128, T=4000, random start: fraction of the majority value over the last half")
for p in (9, 10, 11, 12, 13, 15):
    phi = phi_of(p); L, T = 128, 4000; s = rng.integers(0, 6, (L, L)); fr = []; t0 = time.time()
    for t in range(1, T + 1):
        W = phi[:, s] * phi[:, np.roll(s, 1, 0)] * phi[:, np.roll(s, 1, 1)]
        C = np.cumsum(W / W.sum(0, keepdims=True), axis=0); s = np.minimum((rng.random((L, L))[None] > C).sum(0), 5)
        if t > T // 2: fr.append(np.bincount(s.ravel(), minlength=6).max() / L**2)
    print(f"  p={p:4d}: majority fraction {np.mean(fr):.4f}   ({time.time()-t0:.0f}s)")
print("(b) six-axis static law at (p,1,2), L=16, Metropolis single-site proposals (2000 sweeps), aligned start: fraction of the majority value over the last half")
for p in (3.4, 3.6, 3.8, 4.0, 4.5):
    phi = phi_of(p); L = 16; s = np.zeros((L, L, L), dtype=np.int64); logphi = np.log(phi); ords = []; t0 = time.time()
    idx = np.indices((L, L, L)).sum(0) % 2
    for sw in range(2000):
        for par in (0, 1):
            prop = rng.integers(0, 6, (L, L, L))
            dE = np.zeros((L, L, L))
            for ax in range(3):
                for sh in (1, -1):
                    nb = np.roll(s, sh, ax); dE += logphi[prop, nb] - logphi[s, nb]
            acc = (rng.random((L, L, L)) < np.exp(np.minimum(0, dE))) & (idx == par)
            s = np.where(acc, prop, s)
        if sw >= 1000: ords.append(np.bincount(s.ravel(), minlength=6).max() / L**3)
    print(f"  p={p:4.1f}: order {np.mean(ords):.4f}   ({time.time()-t0:.0f}s)")
print("(c) sphere static law, L=16, heat bath, RANDOM start (1500 sweeps): |m| over the last half")
def vmf(V):
    n = np.linalg.norm(V, axis=-1); kap = np.maximum(n, 1e-12); u = V / kap[..., None]
    U = rng.random(n.shape); w = np.clip(1 + np.log(U + (1 - U) * np.exp(-2 * kap)) / kap, -1, 1); ph = 2 * np.pi * rng.random(n.shape)
    a = np.where((np.abs(u[..., 0]) < 0.9)[..., None], np.array([1.0, 0, 0]), np.array([0, 1.0, 0]))
    e1 = a - (a * u).sum(-1)[..., None] * u; e1 /= np.linalg.norm(e1, axis=-1)[..., None]; e2 = np.cross(u, e1)
    rr = np.sqrt(np.clip(1 - w * w, 0, 1)); s = w[..., None] * u + rr[..., None] * (np.cos(ph)[..., None] * e1 + np.sin(ph)[..., None] * e2)
    zero = n <= 1e-12
    if zero.any():
        g = rng.normal(size=s[zero].shape); s[zero] = g / np.linalg.norm(g, axis=-1)[..., None]
    return s
L = 16; idx = np.indices((L, L, L)).sum(0) % 2
for beta in (0.6, 0.66, 0.7, 0.74, 0.8):
    g = rng.normal(size=(L, L, L, 3)); s = g / np.linalg.norm(g, axis=-1)[..., None]; ms = []; t0 = time.time()
    for sw in range(1500):
        for par in (0, 1):
            V = sum(np.roll(s, sh, ax) for ax in range(3) for sh in (1, -1))
            s = np.where((idx == par)[..., None], vmf(beta * V), s)
        if sw >= 750: ms.append(np.linalg.norm(s.mean((0, 1, 2))))
    print(f"  beta={beta:4.2f}: |m| = {np.mean(ms):.4f}   ({time.time()-t0:.0f}s)")
print("(d) healing: the noisy majority automaton at eps = 10^-3 from an island (a filled triangle of side k at level 0) on a 64x64 plane; survival = a one in the island's forward cone at level D+1; 400 trials each")
def run_island(k, eps, trials):
    L = 64; surv = 0
    for tr in range(trials):
        eta = np.zeros((L, L), dtype=np.int64)
        pts = [(a, b) for a in range(k) for b in range(k) if a + b < k]   # triangle in (x1, x2) with x3 = -(x1+x2)
        for a, b in pts: eta[(20 + a) % L, (20 + b) % L] = 1
        M1 = max(a for a, b in pts); M2 = max(b for a, b in pts); M3 = max(-a - b for a, b in pts); D = M1 + M2 + M3
        for t in range(1, D + 2):
            maj = ((eta + np.roll(eta, 1, 0) + np.roll(eta, 1, 1)) >= 2).astype(np.int64)
            eta = np.maximum(maj, (rng.random((L, L)) < eps).astype(np.int64))
        # forward cone of the island at level D+1 in plane coordinates: x1 >= 20, x2 >= 20 (the x3-shift is absorbed), within reach
        cone = eta[20:20 + k + D + 2, 20:20 + k + D + 2]
        surv += int(cone.any())
    return surv / trials, D
for k in (1, 2, 3, 4):
    f, D = run_island(k, 1e-3, 400); print(f"  triangle side {k} (D = {D}): survival frequency {f:.3f} against the bound 18 (D+1)^3 eps = {18*(D+1)**3*1e-3:.3f}")
