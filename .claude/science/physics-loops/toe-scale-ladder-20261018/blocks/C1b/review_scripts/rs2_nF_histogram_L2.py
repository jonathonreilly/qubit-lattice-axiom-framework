#!/usr/bin/env python3
"""Reviewer check of the COMBINED update set (markers + super-clusters + ice loops + cube moves + PT) at L=2
against an exact distribution that is much finer than <E>: the expansion-order histogram.
At V=0, H = -g A (A = plaquette-flip adjacency on the Gauss sector), so in the CT expansion
   P(n_F = n, W) = beta^n Tr_W(A^n) / n! / Z ,   Z = Tr exp(beta A).
Exact side: own enumeration of the 2^24 link states, own adjacency, own components/eigenvalues (no block code).
Sampler side: the block's sim.PT (code under test), run in memory (nothing written to the block's data/).
usage: rs2_nF_histogram_L2.py CUBE_FRAC SEED MINUTES"""
import os, sys, time, math, itertools
os.environ.setdefault("NUMBA_CACHE_DIR", os.path.join(os.path.dirname(os.path.abspath(__file__)), "__pycache__", "numba"))
sys.dont_write_bytecode = True
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components
HERE = os.path.dirname(os.path.abspath(__file__))
cube_frac, seed, minutes = float(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3])
BETAS = [0.1, 0.18, 0.25, 0.35, 0.5, 0.7, 1.0, 1.4, 2.0, 2.8, 4.0]
TEST = [1.0, 2.0, 4.0]
# ---------------- exact (own code) ----------------
L = 2; nv = 8; nl = 24
def vid(x, y, z): return ((x % L) * L + y % L) * L + z % L
co = list(itertools.product(range(L), repeat=3)); E3 = np.eye(3, dtype=int)
tail = np.repeat(np.arange(nv), 3); head = np.array([vid(*(np.array(co[v]) + E3[a])) for v in range(nv) for a in range(3)])
pl = []
for v, c in enumerate(co):
    c = np.array(c)
    for a, b in ((0, 1), (1, 2), (0, 2)):
        pl.append([3*v+a, 3*vid(*(c+E3[a]))+b, 3*vid(*(c+E3[b]))+a, 3*v+b])
pl = np.array(pl)
codes = []
for ch in range(16):
    c = np.arange(ch << 20, (ch + 1) << 20, dtype=np.int64)
    s = ((c[:, None] >> np.arange(nl)) & 1) * 2 - 1
    d = np.zeros((len(c), nv), dtype=np.int64)
    for l in range(nl):
        d[:, tail[l]] += s[:, l]; d[:, head[l]] -= s[:, l]
    codes.append(c[np.all(d == 0, axis=1)])
codes = np.concatenate(codes)
S = ((codes[:, None] >> np.arange(nl)) & 1) * 2 - 1
n = len(codes)
circ = np.abs(S[:, pl[:, 0]] + S[:, pl[:, 1]] - S[:, pl[:, 2]] - S[:, pl[:, 3]]) == 4
pmask = np.array([sum(1 << int(l) for l in p) for p in pl], dtype=np.int64)
rows, cols = np.nonzero(circ)
nbr = codes[rows] ^ pmask[cols]
j = np.searchsorted(codes, nbr); assert np.all(codes[j] == nbr)
A = csr_matrix((np.ones(len(rows)), (rows, j)), shape=(n, n))
ncomp, lab = connected_components(A, directed=False)
wsel = [[l for l in range(nl) if l % 3 == a and co[tail[l]][a] == 0] for a in range(3)]
W = np.stack([S[:, wsel[a]].sum(1) // 2 for a in range(3)], 1)
W0 = np.all(W == 0, axis=1)
lam_all, lam_w0 = [], []
for c in range(ncomp):
    ii = np.flatnonzero(lab == c)
    assert len(set(map(tuple, W[ii]))) == 1
    e = np.linalg.eigvalsh(A[ii][:, ii].toarray())
    lam_all.append(e)
    if W0[ii[0]]: lam_w0.append(e)
lam_all = np.concatenate(lam_all); lam_w0 = np.concatenate(lam_w0)
print(f"[INFO] own enumeration: {n} Gauss states, {ncomp} flip components, E0 = {-lam_all.max():.10f}")
NMAX = 120
def exact_P(beta, lam):
    lam = lam.astype(np.float64)
    out = np.zeros(NMAX)
    for k in range(NMAX):
        tr = (lam ** k).sum()   # Tr A^k (>=0: closed walks)
        out[k] = tr * beta ** k / math.factorial(k)
    return out
exact = {}
for b in TEST:
    Z = np.exp(b * lam_all).sum()
    pa = exact_P(b, lam_all) / Z; pw = exact_P(b, lam_w0) / Z
    assert abs(pa.sum() - 1) < 1e-9
    exact[b] = (pa, pw)
# ---------------- sampler (code under test) ----------------
sys.path.insert(0, os.path.join(HERE, "..", "scripts"))
from sim import PT
pt = PT(2, BETAS, V=0.0, seed=seed, start="canonical")
pt.cube_frac = cube_frac
ki = [int(np.argmin(np.abs(np.array(BETAS) - b))) for b in TEST]
rec = {b: [] for b in TEST}
t0 = time.time(); therm = 2000
while time.time() - t0 < minutes * 60:
    pt.sweep_all(); pt.swaps()
    if pt.nsw > therm:
        for b, k in zip(TEST, ki):
            r = pt.reps[pt.where[k]]
            w = pt.lat.winding(r.s0)
            rec[b].append((r.nF, int(np.all(w == 0))))
assert pt.check() == 0
print(f"[INFO] cube_frac={cube_frac} seed={seed} sweeps={pt.nsw} round_trips={pt.trips} measured={len(rec[TEST[0]])}")
npass = nfail = 0
NB = 20
for b in TEST:
    x = np.array(rec[b]); nF = x[:, 0]; w0 = x[:, 1]
    m = len(nF) // NB
    pa, pw = exact[b]
    zs = []
    worst = (0, None)
    for label, ex, sel in (("all W", pa, np.ones_like(w0)), ("W=0", pw, w0)):
        for k in range(NMAX):
            if ex[k] < 0.005: continue
            ind = ((nF == k) & (sel == 1)).astype(float)
            bm = ind[: m * NB].reshape(NB, m).mean(1)
            mu, se = ind.mean(), bm.std(ddof=1) / np.sqrt(NB)
            se = max(se, 1e-4)
            z = (mu - ex[k]) / se
            zs.append(z)
            if abs(z) > abs(worst[0]): worst = (z, f"{label} n={k}: QMC {mu:.4f}+-{se:.4f} exact {ex[k]:.4f}")
    zs = np.array(zs)
    # Bonferroni-type rule over the bins tested: |z| <= 3.5 for all bins
    ok = np.all(np.abs(zs) <= 3.5)
    npass += ok; nfail += (not ok)
    mean_ex = (np.arange(NMAX) * pa).sum()
    bm = nF[: m * NB].reshape(NB, m).mean(1)
    zE = (nF.mean() - mean_ex) / (bm.std(ddof=1) / np.sqrt(NB))
    print(f"[{'PASS' if ok else 'FAIL'}] beta={b}: P(n_F=n) and P(n_F=n, W=0) in {len(zs)} bins, max|z|={np.abs(zs).max():.2f} "
          f"chi2/bin={np.mean(zs**2):.2f}; worst: {worst[1]}; <n_F> QMC {nF.mean():.3f} exact {mean_ex:.3f} z={zE:+.2f}")
print(f"TOTAL: PASS={npass} FAIL={nfail}")
