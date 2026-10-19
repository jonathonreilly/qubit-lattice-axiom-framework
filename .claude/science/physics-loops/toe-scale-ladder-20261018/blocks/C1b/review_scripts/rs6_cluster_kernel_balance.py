#!/usr/bin/env python3
"""Follow-up to rs5 (no autocorrelation): with all vertex positions frozen as in rs5, estimate the block's one-sweep
kernel K(i->j) row by row from M INDEPENDENT single sweeps started at each configuration i, then test global
balance  sum_i pi_i K_ij = pi_j  with pi ∝ exp(-g beta Ibar) (Ibar from own code), and, separately, detailed
balance pi_i K_ij = pi_j K_ji pair by pair.  usage: rs6_cluster_kernel_balance.py SEED BETA M [DISCOVER_SWEEPS]"""
import os, sys
os.environ.setdefault("NUMBA_CACHE_DIR", os.path.join(os.path.dirname(os.path.abspath(__file__)), "__pycache__", "numba"))
sys.dont_write_bytecode = True
import numpy as np
from scipy import stats
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "scripts"))
import ctqmc
from sim import PT
seed, beta, M = int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3])
NDISC = int(sys.argv[4]) if len(sys.argv) > 4 else 50000
pt = PT(2, [beta], seed=seed)
for _ in range(500): pt.sweep_all()
r = pt.reps[0]; A = pt.A; pl = A[0]
s0 = r.s0.copy(); ft = r.ft[:r.nF].copy(); fp = r.fp[:r.nF].copy(); nF = r.nF
ctqmc.nb_seed(seed + 5)
ftn, fpn, nF, st, _, mt, mp, nM = ctqmc.sweep(s0, ft, fp, nF, beta, 1.0, 0.0, pl, A[2], A[3], A[4], A[5], A[6], 0, 0.5)
ft, fp, mt, mp = ftn[:nF].copy(), fpn[:nF].copy(), mt[:nM].copy(), mp[:nM].copy()
print(f"[INFO] L=2 beta={beta} seed={seed}: frozen vertices nF+nP = {nF}+{nM}")

def own_ibar(s0, ft, fp):
    o = np.argsort(ft); ts = np.concatenate([[0.0], ft[o], [1.0]]); s = s0.copy(); I = 0.0
    for i in range(len(ts) - 1):
        a = s[pl]; I += np.sum(np.abs(a[:, 0] + a[:, 1] - a[:, 2] - a[:, 3]) == 4) * (ts[i+1] - ts[i])
        if i < len(o): s[pl[fp[o[i]]]] *= -1
    assert np.array_equal(s, s0)
    return I
def key(s0, ft, fp):
    o = np.argsort(ft)
    return (tuple(s0.tolist()), tuple(np.round(ft[o], 12).tolist()), tuple(fp[o].tolist()))
def step(cfg):
    s0, ft, fp, mt, mp = (x.copy() for x in cfg)
    a, b, n2, _s, _i, c, d, m2 = ctqmc.sweep(s0, ft, fp, len(ft), beta, 1.0, 0.0, pl, A[2], A[3], A[4], A[5], A[6],
                                           0, 0.5, True, mt, mp, len(mt))
    return (s0, a[:n2].copy(), b[:n2].copy(), c[:m2].copy(), d[:m2].copy())
cfgs = {}; cfg = (s0, ft, fp, mt, mp)
ctqmc.nb_seed(seed + 77)
for _ in range(NDISC):
    cfg = step(cfg); k = key(cfg[0], cfg[1], cfg[2])
    if k not in cfgs: cfgs[k] = cfg
keys = list(cfgs); idx = {k: i for i, k in enumerate(keys)}; n = len(keys)
Ib = np.array([own_ibar(cfgs[k][0], cfgs[k][1], cfgs[k][2]) for k in keys])
pi = np.exp(-beta * (Ib - Ib.min())); pi /= pi.sum()
C = np.zeros((n, n))
new = 0
for i, k in enumerate(keys):
    for _ in range(M):
        y = step(cfgs[k]); ky = key(y[0], y[1], y[2])
        if ky not in idx: new += 1; continue
        C[i, idx[ky]] += 1
Kh = C / C.sum(1, keepdims=True)
print(f"[INFO] states: {n}; transitions to undiscovered states: {new}")
res = pi @ Kh - pi
var = np.array([(pi**2 * Kh[:, j] * (1 - Kh[:, j]) / C.sum(1)).sum() for j in range(n)])
z = res / np.sqrt(np.maximum(var, 1e-300))
chi2 = float((z**2).sum())
npass = nfail = 0
def chk(name, ok, extra=""):
    global npass, nfail
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {extra}"); npass += bool(ok); nfail += (not ok)
chk("global balance pi K = pi with pi ∝ exp(-g beta Ibar)", np.abs(z).max() < 4.0 and stats.chi2.sf(chi2, n - 1) > 1e-3,
    f"max|z|={np.abs(z).max():.2f} chi2={chi2:.1f}/{n-1} (diag. approx) p={stats.chi2.sf(chi2, n - 1):.3f}")
zs = []
for i in range(n):
    for j in range(i + 1, n):
        a, b = pi[i] * Kh[i, j], pi[j] * Kh[j, i]
        va = pi[i]**2 * Kh[i, j] * (1 - Kh[i, j]) / C[i].sum(); vb = pi[j]**2 * Kh[j, i] * (1 - Kh[j, i]) / C[j].sum()
        if C[i, j] + C[j, i] >= 50: zs.append((a - b) / np.sqrt(va + vb))
zs = np.array(zs)
chi2d = float((zs**2).sum())
chk("detailed balance pi_i K_ij = pi_j K_ji (pairs with >= 50 counts)", stats.chi2.sf(chi2d, len(zs)) > 1e-3 and np.abs(zs).max() < 4.5,
    f"pairs={len(zs)} chi2={chi2d:.1f} max|z|={np.abs(zs).max():.2f} p={stats.chi2.sf(chi2d, len(zs)):.3f}")
# stationary distribution of the estimated kernel vs pi
w, V = np.linalg.eig(Kh.T); v = np.real(V[:, np.argmin(np.abs(w - 1))]); v /= v.sum()
print(f"[INFO] TV(stationary(K_hat), pi) = {0.5 * np.abs(v - pi).sum():.4f}")
print(f"TOTAL: PASS={npass} FAIL={nfail}")
