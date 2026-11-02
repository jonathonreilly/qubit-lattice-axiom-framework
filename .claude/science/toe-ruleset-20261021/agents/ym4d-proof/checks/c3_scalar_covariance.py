#!/usr/bin/env python3
"""Check for Lemma L3s (PROOF.md): multi-scale scalar Balaban-type covariance in SU(2) backgrounds.

Operator (physical units, spacing eps = 1/n, unit blocks of n^4 sites, torus side T blocks):
  H_A = -Lap_A + a Q_A^dag Q_A,   <phi,-Lap_A phi> = eps^2 sum_b |phi_x - U_b phi_y|^2  (weight eps^4 per site)
  (Q_A phi)(X) = eps^4 sum_{y in B(X)} P(c_X -> y) phi(y),  P = transport along the complete-axial tree path
Proven in PROOF.md (L3s):
  (i)  A_max := max_{intra-block b} |1 - U_b^axial| / eps <= (d-1) F / 2, F := max_p |1 - U_p| / eps^2
  (ii) H_A >= m_lb := min(2, a) - d * A_max^2   (uniform in eps, T, N)
  (iii) ||1_D G 1_D'|| <= (2/m) exp(-mu rho_inf(D, D')) whenever (1-eta) m - 1.55 d mu^2 - a (eta + eta^2) >= m/2,
        eta = e^mu - 1, mu <= 1/eps.
This runner checks (i)-(iii) numerically on finite tori. A finite check, not a proof.
"""
import os
os.environ.update(OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1")
import time, itertools as it, numpy as np, scipy.sparse as sp, scipy.sparse.linalg as sl
AUDIT_TIMEOUT_SEC = 120
T0 = time.time(); NP = NF = 0; rng = np.random.default_rng(20261026); d = 4; A_COEF = 1.0
def check(name, ok, s=""):
    global NP, NF
    NP += bool(ok); NF += not ok; print(("PASS " if ok else "FAIL ") + name + (" | " + s if s else ""))
SIG = np.array([[[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]], complex)
def su2exp(a):  # exp(i a.sigma), a shape (...,3)
    th = np.linalg.norm(a, axis=-1); n = a / np.where(th > 0, th, 1)[..., None]
    return np.cos(th)[..., None, None] * np.eye(2) + 1j * np.sin(th)[..., None, None] * np.einsum("...k,kij->...ij", n, SIG)
def opnorm1(M):  # ||1 - M|| for SU(2) M (normal): 2 sin(theta/2)
    c = np.clip(np.real(np.trace(M, axis1=-2, axis2=-1)) / 2, -1, 1); return 2 * np.sin(np.arccos(c) / 2)
dag = lambda M: np.conj(np.swapaxes(M, -1, -2))
class Lat:
    def __init__(s, n, T):
        s.n, s.T, s.S = n, T, n * T; s.eps = 1.0 / n; s.V = s.S ** d
        s.X = np.array(list(it.product(range(s.S), repeat=d))); s.fl = lambda Y: np.ravel_multi_index(tuple((Y % s.S).T), (s.S,) * d)
        s.nb = np.array([s.fl(s.X + np.eye(d, dtype=int)[m]) for m in range(d)])
        s.blk = s.fl(s.X // n * n); bc = s.X // n; s.bid = np.ravel_multi_index(tuple(bc.T), (T,) * d)
        s.root = s.X // n * n + (n - 1) // 2  # near-centre root, offset r = ceil((n-1)/2) <= n/2
    def links(s, amp=0.0, rough=0.0, modes=3, seed=7):
        rng = np.random.default_rng(seed); x = s.X * s.eps; U = []
        K = rng.integers(-1, 2, size=(modes, d)); K[np.all(K == 0, 1)] = 1; ph = rng.uniform(0, 2 * np.pi, (modes, d, 3)); C = rng.normal(size=(modes, d, 3))
        for m in range(d):
            xm = x + 0.5 * s.eps * np.eye(d)[m]; a = np.zeros((s.V, 3))
            for j in range(modes): a += C[j, m][None, :] * np.cos(2 * np.pi * (xm @ K[j])[:, None] / s.T + ph[j, m][None, :])
            U.append(su2exp(amp * s.eps * a + rough * rng.normal(size=(s.V, 3))))
        return np.array(U)
    def plaqF(s, U):
        f = 0.0
        for m in range(d):
            for v in range(m + 1, d):
                P = U[m] @ U[v][s.nb[m]] @ dag(U[m][s.nb[v]]) @ dag(U[v]); f = max(f, opnorm1(P).max())
        return f / s.eps ** 2
    def paths(s, U):  # P(root -> y) along complete axial path: dirs 0..3 in order
        P = np.broadcast_to(np.eye(2, dtype=complex), (s.V, 2, 2)).copy(); cur = s.root.copy()
        for m in range(d):
            for _ in range(s.n):
                go = cur[:, m] != s.X[:, m]; up = s.X[:, m] > cur[:, m]
                c = s.fl(cur); cm = s.fl(cur - np.eye(d, dtype=int)[m])
                step = np.where(up[:, None, None], U[m][c], dag(U[m][cm]))
                P[go] = P[go] @ step[go]; cur[go, m] += np.where(up[go], 1, -1)
        return P
    def amax(s, U, P):
        out = 0.0
        for m in range(d):
            y = s.nb[m]; same = s.bid[y] == s.bid
            Ua = P[same] @ U[m][same] @ dag(P[y[same]]); out = max(out, opnorm1(Ua).max(initial=0.0))
        return out / s.eps
    def H(s, U, P):
        V, e = s.V, s.eps; R, C, D = [], [], []
        def add(r, c, blocks):
            for i in range(2):
                for j in range(2): R.append(2 * r + i); C.append(2 * c + j); D.append(blocks[:, i, j])
        I = np.broadcast_to(np.eye(2), (V, 2, 2)); ar = np.arange(V)
        add(ar, ar, 2 * d * I / e ** 2)
        for m in range(d):
            add(ar, s.nb[m], -U[m] / e ** 2); add(s.nb[m], ar, -dag(U[m]) / e ** 2)
        order = np.argsort(s.bid, kind="stable"); nb4 = s.n ** d
        for b in range(s.T ** d):
            idx = order[b * nb4:(b + 1) * nb4]; Pb = P[idx]
            blk = A_COEF * e ** 4 * np.einsum("xji,yjk->xyik", np.conj(Pb), Pb)
            rr, cc = np.meshgrid(idx, idx, indexing="ij"); add(rr.ravel(), cc.ravel(), blk.reshape(-1, 2, 2))
        return sp.csr_matrix((np.concatenate(D), (np.concatenate(R), np.concatenate(C))), shape=(2 * V, 2 * V))
def gap(H): return sl.eigsh(H, k=1, which="SA", tol=1e-7, return_eigenvectors=False)[0]
def tune(l, Ftarget, rough_only=False):
    mk = (lambda t: l.links(0, t)) if rough_only else (lambda t: l.links(t))
    lo, hi = 0.0, 1e-3
    while l.plaqF(mk(hi)) < Ftarget: lo, hi = hi, 2 * hi
    for _ in range(25):
        mid = (lo + hi) / 2
        if l.plaqF(mk(mid)) < Ftarget: lo = mid
        else: hi = mid
    return mk(lo)
def ct_mu(m, a=A_COEF):
    mu = 0.0
    while True:
        t = mu + 1e-3; eta = np.exp(t) - 1
        if (1 - eta) * m - 1.55 * d * t ** 2 - a * (eta + eta ** 2) < m / 2: return mu
        mu = t
print(f"setup: SU(2) fundamental scalar, d={d}, a={A_COEF}; lemma bound m_lb = min(2,a) - d A_max^2, A_max <= (d-1)F/2")
ok_i = ok_ii = ok_gi = True; rows = []
for (n, T) in ((1, 6), (2, 4), (3, 3)):
    print(f'  lattice n={n} T={T} start {time.time()-T0:.0f}s', flush=True); l = Lat(n, T); cases = [("free", None), ("smooth F=.1", .1), ("smooth F=.2", .2), ("smooth F=.3", .3), ("rough F=.2", -.2), ("large (rough 3.0)", "L")]
    for nm, F in cases:
        U = l.links() if F is None else (l.links(0, 3.0) if F == "L" else tune(l, abs(F), rough_only=F < 0))
        P = l.paths(U); Fm = l.plaqF(U); Am = l.amax(U, P); H = l.H(U, P); g = gap(H)
        mlb = min(2, A_COEF) - d * Am ** 2; mlbF = min(2, A_COEF) - d * ((d - 1) * Fm / 2) ** 2
        ok_i &= Am <= (d - 1) * Fm / 2 + 1e-9
        if mlb > 0: ok_ii &= g >= mlb - 1e-6
        rows.append(f"[{time.time()-T0:.0f}s] n{n} {nm}: F {Fm:.3f} Amax {Am:.3f} (<= {(d-1)*Fm/2:.3f}) gap {g:.4f} m_lb {mlb:.3f}/{mlbF:.3f}")
        if nm == "smooth F=.2":
            gg = su2exp(rng.normal(size=(l.V, 3)))
            Ug = np.array([gg @ U[m] @ dag(gg[l.nb[m]]) for m in range(d)]); g2 = gap(l.H(Ug, l.paths(Ug)))
            ok_gi &= abs(g2 - g) < 1e-5
            if n == 2: keep = (l, U, P, H, mlb)
for r in rows: print("  " + r, flush=True)
check("1 [L3s-i] axial-gauge link bound A_max <= (d-1)F/2 (complete axial tree, near-centre root), all n, all backgrounds", ok_i)
check("2 [L3s-ii] gap(H_A) >= min(2,a) - d A_max^2 whenever the bound is positive (n = 1,2,3)", ok_ii)
check("3 gauge invariance of the spectrum (random SU(2) gauge transform, smooth F=.2)", ok_gi)
fg = [float(r.split("gap ")[1].split()[0]) for r in rows if "free" in r]
check("4 free gap >= min(2,a) = 1 for n = 1,2,3 (uniform discrete Poincare, PROOF.md eq. P)", min(fg) >= 1 - 1e-6, "free gaps " + ", ".join(f"{x:.4f}" for x in fg))
l, U, P, H, mlb = keep; mu = ct_mu(mlb); D0 = np.where(l.bid == 0)[0]; cols = np.concatenate([2 * D0, 2 * D0 + 1])
Gc = np.zeros((2 * l.V, len(cols)), complex); its = 0
for k, c in enumerate(cols):
    b = np.zeros(2 * l.V, complex); b[c] = 1; x, info = sl.cg(H, b, rtol=1e-12, maxiter=5000); its += info; Gc[:, k] = x
Sx = l.X * l.eps; worst = 0.0; data = []
for b in range(l.T ** d):
    Db = np.where(l.bid == b)[0]; rr = np.concatenate([2 * Db, 2 * Db + 1]); nrm = np.linalg.norm(Gc[rr], 2)
    dd = np.abs(Sx[Db][:, None, :] - Sx[D0][None, :, :]); dd = np.minimum(dd, l.T - dd).max(-1).min()
    bound = 2 / mlb * np.exp(-mu * dd); worst = max(worst, nrm / bound); data.append((dd, nrm))
data = np.array(data); u = np.unique(np.round(data[:, 0], 6)); env = np.array([data[np.round(data[:, 0], 6) >= x, 1].max() for x in u])
rate = -np.polyfit(u[u > 0.6], np.log(env[u > 0.6]), 1)[0]
check("5 [L3s-iii] block-block ||1_D G 1_D'|| <= (2/m_lb) exp(-mu rho_inf), n=2 T=4 smooth F=.2", worst <= 1 and its == 0,
      f"m_lb {mlb:.3f}, proven mu {mu:.3f}, max ratio to bound {worst:.3f}, measured envelope rate {rate:.2f}/unit (proven >= {mu:.3f})")
print(f"runtime {time.time() - T0:.0f} s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
