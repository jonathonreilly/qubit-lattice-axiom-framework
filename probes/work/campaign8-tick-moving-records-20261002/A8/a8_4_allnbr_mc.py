"""A8 check 4: the purely content-based stop rule (no held/free distinction in the conditions).

Same toy as a8_3, but the menu of EVERY record (seed or wanderer) is set by ALL its recorded neighbours,
re-evaluated each tick:   locked  <=>  >= 1 recorded neighbour and all recorded neighbours carry its content.
Locked records stay; unlocked records hop (lazy 1/2, exclusion, contention, no swaps).
Contents carried with the record (rule 'all-carried') or redrawn on arrival (rule 'all-reformed').
Question: is the void still inert?  Agreeing wanderers that meet lock each other (nucleation), and a
disagreeing arrival unlocks a surface record of the seed (erosion).
Reports: fraction of interior records locked away from the seed, seed-cluster size, free-record profile.
Usage: python a8_4_allnbr_mc.py rule k u_inf T seed
"""
import os
for kk in ["OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "MKL_NUM_THREADS"]:
    os.environ[kk] = "1"
import sys
import time
import numpy as np
from scipy import ndimage

t0 = time.time()
RULE = sys.argv[1] if len(sys.argv) > 1 else "all-carried"
KC = int(sys.argv[2]) if len(sys.argv) > 2 else 4
U_INF = float(sys.argv[3]) if len(sys.argv) > 3 else 0.004
T = int(sys.argv[4]) if len(sys.argv) > 4 else 20000
SEED = int(sys.argv[5]) if len(sys.argv) > 5 else 20261002
rng = np.random.default_rng(SEED)
L, C = 31, 15
N = L ** 3
I, J, K = np.meshgrid(np.arange(L), np.arange(L), np.arange(L), indexing="ij")
FI, FJ, FK = I.ravel(), J.ravel(), K.ravel()
res = ((I == 0) | (I == L - 1) | (J == 0) | (J == L - 1) | (K == 0) | (K == L - 1)).ravel()
res_idx = np.flatnonzero(res); interior = ~res
DI = np.array([1, -1, 0, 0, 0, 0]); DJ = np.array([0, 0, 1, -1, 0, 0]); DK = np.array([0, 0, 0, 0, 1, -1])
OFF = DI * L * L + DJ * L + DK
idx = np.arange(N).reshape(L, L, L)
rr = np.sqrt((FI - C) ** 2 + (FJ - C) ** 2 + (FK - C) ** 2)

rec = np.zeros(N, dtype=bool)
cont = rng.integers(0, KC, size=N).astype(np.int8)
seed = np.zeros(N, dtype=bool)
for i in range(C - 1, C + 2):
    for j in range(C - 1, C + 2):
        for k in range(C - 1, C + 2):
            seed[idx[i, j, k]] = True
rec |= seed; cont[seed] = 0
rec |= (rng.random(N) < U_INF) & ~seed


def locked_mask():
    f = np.flatnonzero(rec & interior)
    nb = f[:, None] + OFF[None, :]
    rn = rec[nb]
    nr = rn.sum(1)
    ag = ((cont[nb] == cont[f][:, None]) & rn).sum(1)
    lk = np.zeros(N, dtype=bool)
    lk[f[(nr >= 1) & (ag == nr)]] = True
    return lk


hist = []
free_occ = np.zeros(N); n_meas = 0
for it in range(T):
    lk = locked_mask()
    p = np.flatnonzero(rec & ~lk)
    p = p[rng.random(len(p)) < 0.5]
    d = rng.integers(0, 6, size=len(p))
    ti = FI[p] + DI[d]; tj = FJ[p] + DJ[d]; tk = FK[p] + DK[d]
    inb = (ti >= 0) & (ti < L) & (tj >= 0) & (tj < L) & (tk >= 0) & (tk < L)
    p, ti, tj, tk = p[inb], ti[inb], tj[inb], tk[inb]
    t = (ti * L + tj) * L + tk
    ok = ~rec[t]
    p, t = p[ok], t[ok]
    perm = rng.permutation(len(t)); p, t = p[perm], t[perm]
    _, first = np.unique(t, return_index=True); p, t = p[first], t[first]
    c = cont[p].copy()
    rec[p] = False; rec[t] = True
    cont[t] = rng.integers(0, KC, size=len(t)).astype(np.int8) if RULE == "all-reformed" else c
    rec[res_idx] = rng.random(len(res_idx)) < U_INF
    cont[res_idx] = rng.integers(0, KC, size=len(res_idx)).astype(np.int8)
    if it % 2000 == 1999 or it == T - 1:
        lk = locked_mask()
        lab, nl = ndimage.label((lk & interior).reshape(L, L, L))
        labs = lab.ravel()
        cl = labs[idx[C, C, C]]
        seed_cluster = int((labs == cl).sum()) if cl > 0 else 0
        far = interior & (rr > 6)
        n_far = int((rec & far).sum()); n_far_lk = int((rec & lk & far).sum())
        hist.append((it + 1, seed_cluster, int(seed.sum() - (rec & seed & lk).sum()), n_far, n_far_lk, nl))
    if it >= T // 2:
        free_occ += rec & ~locked_mask() & interior
        n_meas += 1

print(f"rule={RULE} k={KC} u_inf={U_INF} T={T} seed={SEED} [{time.time()-t0:.1f} s]")
print(" tick   seed-cluster  seed-sites-unlocked/vacated   records(r>6)  locked(r>6)  frac   n_locked_clusters")
for (tt, sc, sv, nf, nfl, nl) in hist:
    print(f"{tt:6d}   {sc:6d}         {sv:4d}                         {nf:6d}       {nfl:6d}   {nfl/max(nf,1):.3f}   {nl}")
fo = free_occ / max(n_meas, 1) / U_INF
print("free-record density / u_inf (second half), radial bins:")
print("  " + " ".join(f"r{lo+0.5:.0f}:{fo[interior & (rr >= lo) & (rr < lo + 1)].mean():.3f}" for lo in [3.5, 5.5, 7.5, 9.5, 11.5, 13.5]))
print(f"elapsed {time.time()-t0:.1f} s")
