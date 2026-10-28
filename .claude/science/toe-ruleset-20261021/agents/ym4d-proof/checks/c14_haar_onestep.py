#!/usr/bin/env python3
"""Check c14 (PROOF.md, session 4): E7.0' one-step Haar lemma (Lemma H1) and a K-dependence diagnostic, SU(2), beta = 0.
Lemma H1 (one step from i.i.d. Haar links, S4'' with the odd branch rule): V'_b = W_b exp(Xbar_b), W_b = S_{c_X} (straight
transporter) i.i.d. Haar, and E ||Xbar_b||_HS^2 <= m_2 (L^{d-1} - 1) / L^{2(d-1)}, m_2 = E_Haar ||log U||_HS^2 = 2 pi^2/3 - 1.
Hence w_0(K=1) >= 1 - 4 sqrt(m_2 (L^{d-1}-1)) / L^{d-1} (useful only for L >= 5 in d = 4).
PRE-REGISTERED criteria:
  H1a  measured mean ||Xbar||_HS^2 <= bound, for (d, L) = (4, 3), (3, 3), (3, 5), (2, 3)  [K = 1].
  H1b  W_p (plaquette of the straight transporters) is Haar: |mean (1/2) tr W_p| <= 4 standard errors, for each case.
  H1c  measured w_0(1) >= the lemma's lower bound in each case (trivial consistency).
DIAGNOSTIC (no pass criterion; two-to-five K values say nothing about the liminf): d = 2, L = 3, w_0(K) for K = 1..5 and
the first two character moments of the resolution-0 links (Haar: 0, 0).
Checks test instances, not uniformity.
"""
import os
os.environ.update(OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1")
import time, itertools as it, math, numpy as np
AUDIT_TIMEOUT_SEC = 120
T0 = time.time(); NP = NF = 0; rng = np.random.default_rng(14)
def check(n, ok, s=""):
    global NP, NF
    NP += bool(ok); NF += not ok; print(("PASS " if ok else "FAIL ") + n + (" | " + s if s else ""))
def qmul(p, q):
    a1, v1 = p[..., :1], p[..., 1:]; a2, v2 = q[..., :1], q[..., 1:]
    return np.concatenate([a1 * a2 - np.sum(v1 * v2, -1, keepdims=True), a1 * v2 + a2 * v1 + np.cross(v1, v2)], -1)
conj = lambda q: q * np.array([1, -1, -1, -1])
def qlog(q):  # principal log; eigenvalue -1 (a = -1, v = 0) gives 0: the odd branch rule
    a = np.clip(q[..., 0], -1, 1); v = q[..., 1:]; nv = np.linalg.norm(v, axis=-1, keepdims=True)
    return np.where(nv > 1e-15, v / np.maximum(nv, 1e-300) * np.arccos(a)[..., None], 0.0)
def qexp(w):
    nw = np.linalg.norm(w, axis=-1, keepdims=True)
    return np.concatenate([np.cos(nw), np.where(nw > 1e-15, np.sin(nw) / np.maximum(nw, 1e-300), 1.0) * w], -1)
def haar(shape):
    q = rng.normal(size=shape + (4,)); return q / np.linalg.norm(q, axis=-1, keepdims=True)
def make(d, L):
    E = np.eye(d, dtype=int); ORD = list(it.permutations(range(d)))
    def block(U):
        S = U.shape[1]; Tc = S // L; Xs = np.array(list(it.product(range(Tc), repeat=d)))
        out = np.zeros((d,) + (Tc,) * d + (4,)); W = np.zeros_like(out); xb2 = []
        def link(m, x, sg):
            if sg > 0: x = x % S; return U[m][tuple(x.T)]
            x = (x - E[m]) % S; return conj(U[m][tuple(x.T)])
        def path(a, b, order):
            P = np.tile([1.0, 0, 0, 0], (len(a), 1)); cur = a.copy(); diff = (b - a)[0]
            for m in order:
                sg = int(np.sign(diff[m]))
                for _ in range(abs(diff[m])): P = qmul(P, link(m, cur, sg)); cur = cur + sg * E[m]
            return P
        def straight(y, m):
            P = np.tile([1.0, 0, 0, 0], (len(y), 1)); cur = y.copy()
            for _ in range(L): P = qmul(P, link(m, cur, 1)); cur = cur + E[m]
            return P
        h = (L - 1) // 2
        for m in range(d):
            cX = Xs * L + h; cY = cX + L * E[m]; Sc = straight(cX, m); acc = np.zeros((len(Xs), 3))
            for o in ORD:
                for off in it.product(range(L), repeat=d):
                    y = Xs * L + np.array(off)
                    Z = qmul(conj(Sc), qmul(qmul(path(cX, y, o), straight(y, m)), conj(path(cY, y + L * E[m], o))))
                    acc += qlog(Z)
            xb = acc / (len(ORD) * L ** d); xb2.append(2 * np.sum(xb ** 2, -1))  # ||X||_HS^2 = 2 |w|^2
            out[m][tuple(Xs.T)] = qmul(Sc, qexp(xb)); W[m][tuple(Xs.T)] = Sc
        return out, W, np.concatenate(xb2)
    def plaq_tr(V):
        r = []
        for a, b in it.combinations(range(d), 2):
            P = qmul(qmul(V[a], np.roll(V[b], -1, axis=a)), qmul(conj(np.roll(V[a], -1, axis=b)), conj(V[b]))); r.append(P[..., 0].ravel())
        return np.concatenate(r)
    return block, plaq_tr
m2 = 2 * math.pi ** 2 / 3 - 1
for d, L, ns in ((4, 3, 3), (3, 3, 30), (3, 5, 6), (2, 3, 300)):
    block, plaq_tr = make(d, L); S = 2 * L; xs, wp, vp = [], [], []
    for _ in range(ns):
        V, W, x2 = block(haar((d,) + (S,) * d)); xs.append(x2); wp.append(plaq_tr(W)); vp.append(plaq_tr(V))
    xs, wp, vp = np.concatenate(xs), np.concatenate(wp), np.concatenate(vp)
    bound = m2 * (L ** (d - 1) - 1) / L ** (2 * (d - 1)); lb = 1 - 4 * math.sqrt(bound); w0 = 1 - vp.mean()
    se = wp.std() / math.sqrt(len(wp))
    check(f"H1a d={d} L={L}: mean ||Xbar||_HS^2 <= m_2 (L^(d-1)-1)/L^(2(d-1))", xs.mean() <= bound, f"{xs.mean():.4f} <= {bound:.4f} ({len(xs)} links)")
    check(f"H1b d={d} L={L}: straight-transporter plaquette W_p is Haar (|mean tr/2| <= 4 se)", abs(wp.mean()) <= 4 * se, f"{wp.mean():+.4f}, se {se:.4f}")
    check(f"H1c d={d} L={L}: w_0(1) >= lemma bound", w0 >= lb, f"w_0 = {w0:.4f} >= {lb:.4f}; t={time.time() - T0:.0f}s")
# diagnostic: d = 2, L = 3, K = 1..5
block, plaq_tr = make(2, 3); res = []
for K in range(1, 6):
    ns = (400, 100, 60, 40, 12)[K - 1]  # first run: max(4, 400 // 9^(K-1)) (4 samples at K >= 3; kept as c14_out_firstrun.txt)
    wv, c1, c2 = [], [], []
    for _ in range(ns):
        V = haar((2,) + (2 * 3 ** K,) * 2)
        for _k in range(K): V, _, _ = block(V)
        wv.append(1 - plaq_tr(V).mean()); a = np.clip(V[..., 0], -1, 1).ravel(); c1.append(np.mean(2 * a)); c2.append(np.mean(4 * a ** 2 - 1))
    res.append((K, np.mean(wv), np.std(wv) / math.sqrt(ns), np.mean(c1), np.mean(c2), ns))
    print(f"INFO d=2 L=3 K={K}: w_0 = {np.mean(wv):.4f} +- {np.std(wv) / math.sqrt(ns):.4f}; <chi_1> = {np.mean(c1):+.4f}, <chi_2> = {np.mean(c2):+.4f} ({ns} samples); t={time.time() - T0:.0f}s")
print(f"runtime {time.time() - T0:.0f} s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
