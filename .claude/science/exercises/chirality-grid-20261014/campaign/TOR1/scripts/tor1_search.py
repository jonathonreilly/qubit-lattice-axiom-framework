"""TOR-1 greedy W-matched witness search on the VECTOR-LIKE O kernel (m = 0.05; power reference), K2c V2 style: start with 3
random W-matched members; each step adds the best of 4 random + 4 perturbed (sigma 0.02-0.2, re-matched) candidates by lambda_min of
the normalised O kernel at level (2, 6).  usage: python3 tor1_search.py Lt k seed"""
import sys, time
import numpy as np
from tor1_geom import *
from lat2d import Geom, rand_half
Lt, K, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); T = Lt // 2
S = Torus(4, Lt); G = Geom(4, T, True, -1); rng = np.random.default_rng(seed); t0 = time.time()
fO = lambda A: vec_logdet(S, A, 0.05, 1)[0]


def match(u):
    ux = u['x'] - u['x'][0].sum() / 4; ux[T - 1, 0] -= ux[T - 1].sum()
    for t in range(T - 1):
        for x in range(4):
            if abs(wrap(ux[t, x] + u['t'][t, (x + 1) % 4] - ux[t + 1, x] - u['t'][t, x])) > 0.55: return None
    return {'x': ux, 't': u['t'].copy()}


def rand_member():
    while True:
        m = match(rand_half(rng, G, 0.3, 0.55))
        if m is not None: return m


def perturb(u):
    for _ in range(2000):
        s = rng.choice([0.02, 0.05, 0.1, 0.2])
        m = match({'x': u['x'] + rng.normal(0, s, u['x'].shape), 't': u['t'] + rng.normal(0, s, u['t'].shape)})
        if m is not None: return m
    return rand_member()


def lam(L):
    d = L.diagonal().real; Z = np.exp(L - 0.5 * (d[:, None] + d[None, :])); ev = np.linalg.eigvalsh(0.5 * (Z + Z.conj().T))
    return ev[0], ev[-1]


U = [rand_member() for _ in range(3)]; k = len(U)
L = np.zeros((k, k), complex)
for a in range(k):
    for b in range(a, k):
        L[a, b] = entry_log(S, U[a], U[b], 2, 6, fO)[0]; L[b, a] = np.conj(L[a, b])
print(f"# TOR-1 search Lt={Lt} K={K} seed={seed}: start k=3 lam_min(O) {lam(L)[0]:+.3e} [{time.time()-t0:.0f}s]", flush=True)
while len(U) < K:
    best = None
    cands = [rand_member() for _ in range(4)] + [perturb(U[rng.integers(len(U))]) for _ in range(4)]
    for c in cands:
        row = np.array([entry_log(S, a, c, 2, 6, fO)[0] for a in U] + [entry_log(S, c, c, 2, 6, fO)[0]])
        Ln = np.zeros((len(U) + 1, len(U) + 1), complex); Ln[:-1, :-1] = L; Ln[:-1, -1] = row[:-1]; Ln[-1, :-1] = np.conj(row[:-1]); Ln[-1, -1] = row[-1].real
        lm, lx = lam(Ln)
        if best is None or lm < best[0]: best = (lm, lx, c, Ln)
    U.append(best[2]); L = best[3]
    print(f"  k={len(U)}: lam_min(O) {best[0]:+.4e} (min/max {best[0]/best[1]:+.3e}) [{time.time()-t0:.0f}s]", flush=True)
np.savez(f"pool_TOR1_srch_Lt{Lt}_k{K}_s{seed}.npz", ux=np.array([u['x'] for u in U]), ut=np.array([u['t'] for u in U]))
print(f"saved; max |W(slice 1)| {max(abs(u['x'][0].sum()) for u in U):.1e} max |W(slice T)| {max(abs(u['x'][T-1].sum()) for u in U):.1e} done [{time.time()-t0:.0f}s]")
