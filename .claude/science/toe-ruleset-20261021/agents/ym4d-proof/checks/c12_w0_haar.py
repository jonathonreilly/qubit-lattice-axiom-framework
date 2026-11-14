#!/usr/bin/env python3
"""Diagnostic for E7.0' (PROOF.md, session 3): w_0(K) = E_Haar[1 - (1/2) Re tr V^(0)_p] for SU(2) at beta = 0, under the
everywhere-defined map S4'' (order-averaged over the 24 orders) and its fixed-order variant, L = 3, d = 4, coarse torus
side 2 (fine side 2*3^K), K = 1, 2. Monte Carlo over i.i.d. Haar links; all 96 resolution-0 plaquettes of each sample.
FINITE DIAGNOSTIC: two values of K say nothing about liminf_K. Also reported: the fraction of first-step Z outside the
domain ||Z - 1|| < 1 (expected large at beta = 0, which is why S4'' is needed).
Pass criterion (pre-registered): w_0(K) > 0.5 for every case measured (a sanity floor, not a uniformity test).
"""
import os
os.environ.update(OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1")
import time, itertools as it, numpy as np
AUDIT_TIMEOUT_SEC = 120
T0 = time.time(); NP = NF = 0; rng = np.random.default_rng(12); d = 4; L = 3
def check(n, ok, s=""):
    global NP, NF
    NP += bool(ok); NF += not ok; print(("PASS " if ok else "FAIL ") + n + (" | " + s if s else ""))
def qmul(p, q):
    a1, v1 = p[..., :1], p[..., 1:]; a2, v2 = q[..., :1], q[..., 1:]
    return np.concatenate([a1 * a2 - np.sum(v1 * v2, -1, keepdims=True), a1 * v2 + a2 * v1 + np.cross(v1, v2)], -1)
conj = lambda q: q * np.array([1, -1, -1, -1])
def qlog(q):
    a = np.clip(q[..., 0], -1, 1); v = q[..., 1:]; nv = np.linalg.norm(v, axis=-1, keepdims=True)
    return np.where(nv > 1e-15, v / np.maximum(nv, 1e-300) * np.arccos(a)[..., None], 0.0)
def qexp(w):
    nw = np.linalg.norm(w, axis=-1, keepdims=True); return np.concatenate([np.cos(nw), np.where(nw > 1e-15, np.sin(nw) / np.maximum(nw, 1e-300), 1.0) * w], -1)
E = np.eye(d, dtype=int)
def block(U, orders):
    S = U.shape[1]; Tc = S // L; Xs = np.array(list(it.product(range(Tc), repeat=d))); out = np.zeros((d, Tc, Tc, Tc, Tc, 4)); bad = []
    def link(m, x, sg):
        if sg > 0: x = x % S; return U[m][x[:, 0], x[:, 1], x[:, 2], x[:, 3]]
        x = (x - E[m]) % S; return conj(U[m][x[:, 0], x[:, 1], x[:, 2], x[:, 3]])
    def path(a, b, order):  # a, b arrays (nb, d); offsets uniform across blocks
        P = np.tile([1.0, 0, 0, 0], (len(a), 1)); cur = a.copy(); diff = (b - a)[0]
        for m in order:
            sg = int(np.sign(diff[m]))
            for _ in range(abs(diff[m])): P = qmul(P, link(m, cur, sg)); cur = cur + sg * E[m]
        return P
    def straight(y, m):
        P = np.tile([1.0, 0, 0, 0], (len(y), 1)); cur = y.copy()
        for _ in range(L): P = qmul(P, link(m, cur, 1)); cur = cur + E[m]
        return P
    for m in range(d):
        cX = Xs * L + 1; cY = cX + L * E[m]; Sc = straight(cX, m); acc = np.zeros((len(Xs), 3))
        for o in orders:
            for off in it.product(range(L), repeat=d):
                y = Xs * L + np.array(off); Z = qmul(conj(Sc), qmul(qmul(path(cX, y, o), straight(y, m)), conj(path(cY, y + L * E[m], o))))
                acc += qlog(Z); bad.append(np.linalg.norm(Z - np.array([1.0, 0, 0, 0]), axis=-1) >= 1)
        V = qmul(Sc, qexp(acc / (len(orders) * L ** d)))
        out[m][Xs[:, 0], Xs[:, 1], Xs[:, 2], Xs[:, 3]] = V
    return out, np.mean(np.concatenate(bad))
def w_plaq(V):
    Tc = V.shape[1]; ws = []
    for a, b in it.combinations(range(d), 2):
        P = qmul(qmul(V[a], np.roll(V[b], -1, axis=a)), qmul(conj(np.roll(V[a], -1, axis=b)), conj(V[b]))); ws.append(1 - P[..., 0].ravel())
    return np.concatenate(ws)
def haar(shape):
    q = rng.normal(size=shape + (4,)); return q / np.linalg.norm(q, axis=-1, keepdims=True)
ORD = list(it.permutations(range(d)))
res = []
for K, orders, name, ns in ((1, ORD, "S4''", 8), (1, ORD[:1], "S4'' fixed order", 40), (2, ORD[:1], "S4'' fixed order", 10), (2, ORD, "S4''", 2)):
    S = 2 * L ** K; vals = []; badf = []
    for _ in range(ns):
        V = haar((d, S, S, S, S))
        for k in range(K): V, bf = block(V, orders); badf.append(bf) if k == 0 else None
        vals.append(np.mean(w_plaq(V)))
    vals = np.array(vals); res.append((K, name, vals.mean(), vals.std(ddof=1) / np.sqrt(ns), np.mean(badf)))
    print(f"INFO K={K} {name}: w_0 = {vals.mean():.4f} +- {vals.std(ddof=1) / np.sqrt(ns):.4f} ({ns} samples x 96 plaquettes); "
          f"first-step fraction of Z outside ||Z-1||<1: {np.mean(badf):.3f}; t={time.time() - T0:.0f}s")
check("w_0(K) > 0.5 in every measured case (sanity floor; not a uniformity statement)", all(r[2] > 0.5 for r in res),
      ", ".join(f"K{r[0]} {r[1]}: {r[2]:.3f}" for r in res))
print(f"runtime {time.time() - T0:.0f} s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
