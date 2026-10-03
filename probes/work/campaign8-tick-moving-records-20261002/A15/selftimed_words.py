#!/usr/bin/env python3
"""A15: self-timed (handshake-wait) beats for A10 layer words in 1D, 2D, 3D (supplied toys), plus rigid-clock
handshake cut check in 3D.

A word is a list of layers (axis, parity). A site s at counter c with offset phi uses layer word[(c+phi) % p];
its partner is s + e_a if s_a = parity (mod 2), else s - e_a. A pair fires when both sites name each other; then
both counters advance (self-timed). Torus of even side. Reported: deadlock, stuck sites, uniform final beat."""
import os, signal
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
signal.alarm(55)
import numpy as np, itertools

def make(word, L, d):
    p = len(word)
    grids = np.meshgrid(*[np.arange(L)] * d, indexing='ij')
    coords = np.stack([g.ravel() for g in grids], axis=1)          # (n, d)
    n = coords.shape[0]
    idx = lambda cs: np.ravel_multi_index(tuple((cs % L).T), (L,) * d)
    # partner table: part[j, s] for layer j
    part = np.zeros((p, n), int)
    for j, (a, par) in enumerate(word):
        step = np.zeros(d, int); step[a] = 1
        plus = coords[:, a] % 2 == par
        target = np.where(plus[:, None], coords + step, coords - step)
        part[j] = idx(target)
    return coords, part

def selftimed(word, L, d, phi, rounds):
    coords, part = make(word, L, d)
    n = coords.shape[0]; p = len(word)
    c = np.zeros(n, int)
    last = -np.ones(n, int)
    fpr = []
    ar = np.arange(n)
    for r in range(rounds):
        j = (c + phi) % p
        sel = part[j, ar]
        ready = sel[sel] == ar
        c[ready] += 1
        last[ready] = r
        fpr.append(int(ready.sum()))
    return c, last, fpr

def rigid_cut_check(word, L, d, phi, th=0.7, steps=60, seed=1):
    """rigid clocks + handshake: evolve a single excitation; report weight that ever crosses region labels."""
    coords, part = make(word, L, d)
    n = coords.shape[0]; p = len(word)
    region = phi.copy()
    rng = np.random.default_rng(seed)
    psi = np.zeros(n, complex)
    src = np.where(region == region.min())[0]
    psi[src] = rng.normal(size=src.size) + 1j * rng.normal(size=src.size)
    psi /= np.linalg.norm(psi)
    w0 = np.sum(np.abs(psi[region != region.min()]) ** 2)
    c, s = np.cos(th), np.sin(th)
    u = np.exp(1j * th) * np.array([[c, -1j * s], [-1j * s, c]])
    ar = np.arange(n)
    maxleak = 0.0
    for t in range(steps):
        sel = part[(t + phi) % p, ar]
        mutual = (sel[sel] == ar) & (ar < sel)
        a = ar[mutual]; b = sel[mutual]
        pa, pb = psi[a].copy(), psi[b].copy()
        psi[a] = u[0, 0] * pa + u[0, 1] * pb
        psi[b] = u[1, 0] * pa + u[1, 1] * pb
        maxleak = max(maxleak, np.sum(np.abs(psi[region != region.min()]) ** 2))
    return w0, maxleak

if __name__ == '__main__':
    words = {
        '1D A10 (e,o)': ([(0, 0), (0, 1)], 1, 64),
        '2D A10 (xe,xo,ye,yo)': ([(0, 0), (0, 1), (1, 0), (1, 1)], 2, 16),
        '3D A10 (xe,xo,ye,yo,ze,zo)': ([(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)], 3, 8),
    }
    R = 300
    for name, (word, d, L) in words.items():
        p = len(word)
        coords, _ = make(word, L, d)
        n = coords.shape[0]
        print("== %s, torus L=%d (%d sites), %d rounds ==" % (name, L, n, R))
        cases = [("uniform", np.zeros(n, int))]
        centre = np.ravel_multi_index(tuple([L // 2] * d), (L,) * d)
        for k in range(1, p):
            phi = np.zeros(n, int); phi[centre] = k
            cases.append(("single site offset %d" % k, phi))
        for k in range(1, p):
            phi = np.zeros(n, int); phi[(coords[:, 0] >= L // 4) & (coords[:, 0] < 3 * L // 4)] = k
            cases.append(("slab normal to x, offset %d" % k, phi))
        if d >= 2:
            for k in range(1, p):
                phi = np.zeros(n, int); phi[(coords[:, 1] >= L // 4) & (coords[:, 1] < 3 * L // 4)] = k
                cases.append(("slab normal to y, offset %d" % k, phi))
        for label, phi in cases:
            c, last, fpr = selftimed(word, L, d, phi, R)
            stuck = int((last < R - 3 * p).sum())
            beat = (c + phi) % p
            print("  %-30s deadlock=%-5s stuck=%4d/%d  uniform beat at end=%s" % (label, fpr[-1] == 0, stuck, n,
                  len(set(beat.tolist())) == 1))
    # rigid-clock handshake: any nonzero offset slab is a perfect cut (3D A10 word)
    word, d, L = words['3D A10 (xe,xo,ye,yo,ze,zo)']
    coords, _ = make(word, L, d)
    n = coords.shape[0]
    print("== rigid clocks + handshake, 3D A10 word, L=8: weight ever found across the wall (start: all on one side) ==")
    for axis in (0, 1, 2):
        for k in range(1, 6):
            phi = np.zeros(n, int); phi[(coords[:, axis] >= 2) & (coords[:, axis] < 6)] = k
            w0, leak = rigid_cut_check(word, L, d, phi)
            print("  slab normal to axis %d offset %d: initial %.1e, max over 60 sub-steps %.1e" % (axis, k, w0, leak))
