#!/usr/bin/env python3
"""Balaban one-step covariance (-Lap_A + Q^+Q)^-1, U(1): D4 vs Z^4."""
import os; os.environ.update(OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1")
import itertools as it, time, numpy as N, scipy.sparse as sp, scipy.sparse.linalg as sl
from numpy import concatenate as cat
CSR = sp.csr_matrix
IP = it.product
J = "; ".join
AUDIT_TIMEOUT_SEC = 120
T0 = time.time(); NP = NF = 0; rng = N.random.default_rng(20261026); L = 12; a_ = 1; ar = N.array; CG = []
def check(n, ok, s=""):
    global NP, NF
    NP += ok; NF += not ok; print(("PASS " if ok else "FAIL ") + n + (" | " + s if s else ""))
P4 = list(IP([-1, 0, 1], repeat=4))
class Lat:
    def __init__(s, d4):
        s.d4 = d4; ok = lambda x: not d4 or sum(x) % 2 == 0
        s.S = ar([x for x in IP(range(L), repeat=4) if ok(x)]); s.n = len(s.S)
        s.idx = -N.ones((L,) * 4, int); s.idx[tuple(s.S.T)] = N.arange(s.n)
        s.D = [ar(v) for v in P4 if sum(map(abs, v)) == 1 + d4]; s.di = {tuple(v): k for k, v in enumerate(s.D)}
        s.nb = ar([s.look(s.S + v) for v in s.D]); s.cS = ar([x for x in IP(range(L // 2), repeat=4) if ok(x)])
    def look(s, Y): return s.idx[tuple((Y % L).T)]
    def k(s, d): return s.di[tuple(d)]
    def links(s, n=0, sc=0.0, nz=None, uni=False, lam=None):
        f = 2 * N.pi * n / L**2; th = N.zeros((len(s.D), s.n)); a = s.S.astype(float)
        for k, d in enumerate(s.D):
            if tuple(-d) < tuple(d): continue
            Y = a + d; m = N.floor(Y / L); W = Y - L * m
            t = f * (d[1] * (a[:, 0] + d[0] / 2) + d[3] * (a[:, 2] + d[2] / 2) - L * (m[:, 0] * W[:, 1] + m[:, 2] * W[:, 3]))
            if nz is not None: t = t + sc * nz[k]
            if uni: t = rng.uniform(-N.pi, N.pi, s.n)
            if lam is not None: t = t + lam - lam[s.nb[k]]
            th[k] = t; th[s.k(-d), s.nb[k]] = -t
        return th
    def plaq(s, th):
        o = []
        for p, q in IP(s.D, s.D):
            j = s.nb[s.k(p)]
            if s.d4 and tuple(p + q) in s.di: o.append(th[s.k(p)] + th[s.k(q), j] - th[s.k(p + q)])
            elif not s.d4 and N.argmax(abs(p)) < N.argmax(abs(q)) and p.sum() > 0 < q.sum():
                o.append(th[s.k(p)] + th[s.k(q), j] - th[s.k(p), s.nb[s.k(q)]] - th[s.k(q)])
        return abs(1 - N.exp(1j * cat(o))).max()
def kernel(l, nm):
    if nm == "D4": E = [(ar(v), {0: 1, 2: .5, 4: .125}[N.dot(v, v)]) for v in IP(range(-2, 3), repeat=4) if N.dot(v, v) <= 4 and sum(v) % 2 == 0]
    elif nm == "Z4-sym": E = [(ar(v), .5**sum(map(abs, v))) for v in P4]
    else: E = [(ar(v), 1.0) for v in IP([0, 1], repeat=4)]
    out = []
    for e, w in E:
        if l.d4: P = [[]] if not e.any() else [[e]] if e @ e == 2 else [[r, e - r] for r in l.D if tuple(e - r) in l.di]
        else: P = [list(map(ar, p)) for p in set(it.permutations([tuple(int(N.sign(x)) * N.eye(4, dtype=int)[m]) for m, x in enumerate(e) if x]))]
        out.append((e, w, P))
    return out
def M(l, K, th):
    R, C, V = [], [], []; b = l.look(2 * l.cS); nc = len(l.cS)
    for e, w, P in K:
        ang = N.zeros(nc)
        for p in P:
            c = b.copy()
            for d in p: ang += th[l.k(d), c] / len(P); c = l.nb[l.k(d), c]
        R.append(N.arange(nc)); C.append(l.look(2 * l.cS + e)); V.append(w / 16 * N.exp(1j * ang))
    Q = CSR((cat(V), (cat(R), cat(C))), shape=(nc, l.n)); n = len(l.D)
    Lap = (n * sp.identity(l.n) - CSR((N.exp(1j * th).ravel(), (N.tile(N.arange(l.n), n), l.nb.ravel())), shape=(l.n,) * 2)) / (1 + 5 * l.d4)
    return (Lap + a_ * (Q.conj().T @ Q)).tocsr(), Q
def col(X):
    b = N.zeros(X.shape[0], complex); b[0] = 1; x, i = sl.cg(X, b, rtol=1e-11, maxiter=4000); CG.append(i); return x
def rate(l, v):
    dX = l.S - L * N.round(l.S / L); ds = N.round(N.sqrt((dX**2).sum(1)), 6); u = N.unique(ds)
    env = ar([N.abs(v[ds >= d]).max() for d in u]); sel = (u > 1.5) & (u < L / 2); return -N.polyfit(u[sel], N.log(env[sel]), 1)[0]
gap = lambda X: sl.eigsh(X, k=1, which="SA", tol=1e-8, return_eigenvectors=0)[0].real
def tune(l, n, nz, E):
    f = lambda s: l.plaq(l.links(n, s, nz)); lo, hi = 0, 1e-3
    while f(hi) < E: lo, hi = hi, hi * 2
    for _ in range(40): m = (lo + hi) / 2; lo, hi = (m, hi) if f(m) < E else (lo, m)
    return lo
RES = {}
for nm in ("D4", "Z4-sym", "Z4-cube"):
    l = Lat(nm == "D4"); K = kernel(l, nm); nz = rng.normal(size=(len(l.D), l.n)); lam = rng.normal(size=l.n)
    _, Q0 = M(l, K, l.links()); pu = abs(Q0 @ N.ones(l.n) - 1).max(); s1 = tune(l, 1, nz, 1.0)
    Ma, _ = M(l, K, l.links(1, s1, nz)); Mb, _ = M(l, K, l.links(1, s1, nz, lam=lam))
    cov = abs(col(Mb) - N.exp(1j * (lam - lam[0])) * col(Ma)).max(); her = sp.linalg.norm(Ma - Ma.conj().T)
    check(f"0 [{nm}] Q1=1, covariant, hermitian", pu < 1e-12 and cov < 1e-8 and her < 1e-12, f"{pu:.0e}, {cov:.0e}, {her:.0e}")
    r = {}
    for b, n, e in zip(("free", "e1/30", "e.3", "e1", "Q1", "Q1e1"), (0, 0, 0, 0, 1, 1), (0, 1 / 30, .3, 1, 0, 1)):
        th = l.links(n, tune(l, n, nz, e) if e else 0.0, nz); X, _ = M(l, K, th); r[b] = (rate(l, col(X)), gap(X), l.plaq(th))
    th = l.links(uni=True); X, _ = M(l, K, th); r["LARGE"] = (rate(l, col(X)), gap(X), l.plaq(th)); RES[nm] = r
    f = r["free"]; sm = list(r.values())[:6]
    print(f"  {nm} rate/gap: " + J(f"{k} (eps{v[2]:.2f}) {v[0]:.3f}/{v[1]:.4f}" for k, v in r.items()))
    check(f"{1 if l.d4 else 2} [{nm}] rate >= .8 free, eps<=1", (mr := min(v[0] for v in sm) / f[0]) >= .8, f"min/free {mr:.3f}")
    check(f"3 [{nm}] gap >= .5 free; free=a/16", (mg := min(v[1] for v in sm) / f[1]) >= .5 and abs(f[1] - a_ / 16) < 1e-6,
          f"min/free {mg:.3f}, free {f[1]:.7f}")
fr = {k: v["free"][0] for k, v in RES.items()}
check("4 free rates > 0; CG converged", all(N.isfinite(x) and x > 0 for x in fr.values()) and not any(CG),
      J(f"{k} {x:.3f}" for k, x in fr.items()) + "; large field " + J(f"{k} {v['LARGE'][0]:.3f}/{v['LARGE'][1]:.3f}" for k, v in RES.items()))
print(f"runtime {time.time() - T0:.0f} s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
