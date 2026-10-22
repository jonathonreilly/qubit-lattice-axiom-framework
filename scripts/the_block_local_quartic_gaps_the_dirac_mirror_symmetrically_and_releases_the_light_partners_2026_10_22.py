AUDIT_INPUT_PATHS = ('docs/THE_BLOCK_LOCAL_QUARTIC_GAPS_THE_DIRAC_MIRROR_SYMMETRICALLY_AND_RELEASES_THE_LIGHT_PARTNERS_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""block-quartic-smg: the block-local (on-block) SU(4) quartic on a real Dirac sea, with and without a mixed light layer. Sign-free CT-INT.
Block lattice L^3 (block units); each block holds the mirror family's 4 flavour modes (one per fine site of the role block).
H = -t sum eta_mu(x)(a_x^+ a_{x+mu} + h.c.) [pi-flux Dirac band; PBC L = 4, APBC L = 6]  - g sum_b (m1 m2 m3 m4 + h.c.)_b
optional light layer l (same band) mixed by w eps_x (l_x^+ m_x + h.c.); the quartic acts on the mirror only. Supplied toy, NOT Spin(10).
 A theorems (sign, uniqueness counts incl. Spin(10), block-term symmetries, Dirac band, light-release algebra)  B engine vs ED
 C live seeded runs  D recorded production values (not recomputed; no PASS depends on them). Self-contained, reads no files."""
AUDIT_TIMEOUT_SEC = 120
import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'
import itertools
import numpy as np
def stag_band(L, t, apbc):
    S = np.array(list(itertools.product(range(L), repeat=3))); N = len(S); idx = {tuple(v): i for i, v in enumerate(S)}
    H = np.zeros((N, N))
    for i, v in enumerate(S):
        eta = (1, (-1) ** v[0], (-1) ** (v[0] + v[1]))
        for d in range(3):
            w = list(v); w[d] += 1; s = 1.0
            if w[d] == L: w[d] = 0; s = -1.0 if apbc else 1.0
            j = idx[tuple(w)]; H[i, j] -= t * eta[d] * s; H[j, i] -= t * eta[d] * s
    return S, H, idx

class Lattice:
    def __init__(s, L, t, beta, w=None, h=0.002, Hcustom=None, nv=None):
        s.L, s.t, s.beta = L, t, beta
        if Hcustom is not None:                           # small clusters: generic path (no table)
            s.H = Hcustom; s.N = nv; s.NO = Hcustom.shape[0]; s.tab = None
        else:
            s.apbc = (L % 4 == 2); S, Hs, idx = stag_band(L, t, s.apbc); N = len(S); s.S = S; s.N = N
            e0, U0 = np.linalg.eigh(Hs); s.P0 = U0[:, np.abs(e0) < 1e-9]; s.eps_site = (-1.0) ** S.sum(1)
            if w is None: H = Hs; s.NO = N
            else: H = np.block([[Hs, w * np.diag(s.eps_site)], [w * np.diag(s.eps_site), Hs]]); s.NO = 2 * N
            s.H = H
        e, U = np.linalg.eigh(s.H); s.e, s.U = e, U; s.lz = np.logaddexp(0.0, -beta * e)
        s.M = s.N; s.w = np.ones(s.N)                     # vertex orbitals = mirror sites 0..N-1, coupling weight 1
        if Hcustom is not None: return
        NO = s.NO; nl = NO // N
        cls = np.array([int(v[0] % 2) * 4 + int(v[1] % 2) * 2 + int(v[2] % 2) for v in S])
        reps = [idx[(a, b, c)] for a in (0, 1) for b in (0, 1) for c in (0, 1)]
        s.cls = cls; Mg = int(round(beta / h)); s.h = beta / Mg
        dl = np.arange(Mg + 1) * s.h; dl[0] = 1e-13
        s.tab = np.empty((8, Mg + 1, NO))
        for c, r in enumerate(reps):
            for a in range(0, Mg + 1, 500):
                W = np.exp(-dl[a:a + 500, None] * e[None, :] - s.lz[None, :])
                s.tab[c, a:a + 500] = (W * U[r]) @ U.T
        s.tab = np.ascontiguousarray(s.tab.transpose(0, 2, 1))   # [class, orbital, m]
        # maps: for mirror x and any orbital y: G(x,y) = sgn * S(rep(x), rmap)
        s.rmap = np.empty((N, NO), np.int32); s.sgn = np.empty((N, NO))
        for x in range(N):
            d = S[x] - S[x] % 2; u = S - d; wr = (u < 0).sum(1); u %= L
            ui = np.array([idx[tuple(q)] for q in u]); sg = (-1.0) ** wr if s.apbc else np.ones(N)
            for l in range(nl): s.rmap[x, l * N:(l + 1) * N] = ui + l * N; s.sgn[x, l * N:(l + 1) * N] = sg
    def S0(s, Dp, x, y):
        """S_{x y}(Dp) with x mirror (vector), y any orbital (vector), Dp in (0, beta) (array broadcast)."""
        if s.tab is None:
            W = np.exp(-Dp[..., None] * s.e - s.lz); return np.einsum('...k,...k,...k->...', s.U[x], s.U[y], W)
        f = Dp / s.h; m = np.minimum(f.astype(int), s.tab.shape[2] - 2); f -= m
        c = s.cls[x]; r = s.rmap[x, y]; T = s.tab
        return s.sgn[x, y] * ((1 - f) * T[c, r, m] + f * T[c, r, m + 1])
    def g0(s, xs, ts, ys, tps):
        xs = np.atleast_1d(xs); ys = np.atleast_1d(ys); ts = np.atleast_1d(ts); tps = np.atleast_1d(tps)
        D = np.subtract.outer(ts, tps); sg = np.where(D > 0, 1.0, -1.0); Dp = np.where(D > 0, D, D + s.beta)
        X, Y = np.broadcast_arrays(xs[:, None], ys[None, :])
        return sg * s.S0(Dp, X, Y)
    def g0_any(s, Xs, T1, ys, tps):
        """G0(X_i, T1; y_j, t'_j), X any orbitals at one time, y mirror: uses S symmetric."""
        D = T1 - np.atleast_1d(tps); sg = np.where(D > 0, 1.0, -1.0); Dp = np.where(D > 0, D, D + s.beta)
        Y, X = np.broadcast_arrays(np.atleast_1d(ys)[None, :], np.asarray(Xs)[:, None])
        return sg[None, :] * s.S0(np.broadcast_to(Dp[None, :], X.shape).copy(), Y, X)
    def g0_full(s, D):
        sg = 1.0 if D > 0 else -1.0; Dp = D if D > 0 else D + s.beta
        return sg * (s.U * np.exp(-Dp * s.e - s.lz)) @ s.U.T

class CTINT:
    def __init__(s, lat, g, seed, cap=64):
        s.lat, s.g = lat, g; s.rng = np.random.default_rng(seed); s._n = 0; s.cap = 0
        s.c = (g * lat.M * lat.beta) ** 2; s.acc = np.zeros(4); s.prop = np.zeros(4); s._alloc(cap)
    def _alloc(s, cap):
        n = s._n; B = np.zeros((cap, cap)); T = np.zeros((cap, cap))
        V = [np.zeros(cap, int), np.zeros(cap), np.zeros(cap, int), np.zeros(cap)]
        if s.cap:
            B[:n, :n] = s._B[:n, :n]
            for new, old in zip(V, (s._xs, s._ts, s._ys, s._tps)): new[:n] = old[:n]
        s._B, s._T = B, T; s._xs, s._ts, s._ys, s._tps = V; s.cap = cap
    n = property(lambda s: s._n)
    xs = property(lambda s: s._xs[:s._n]); ts = property(lambda s: s._ts[:s._n])
    ys = property(lambda s: s._ys[:s._n]); tps = property(lambda s: s._tps[:s._n])
    Minv = property(lambda s: s._B[:s._n, :s._n])
    def load(s, xs, ts, ys, tps):
        n = len(xs)
        if s.cap < n + 1: s._alloc(int(1.15 * n) + 32)
        s._xs[:n], s._ts[:n], s._ys[:n], s._tps[:n] = xs, ts, ys, tps; s._n = n; s._B[:n, :n] = 0; s.recompute()
    def recompute(s):
        n = s._n
        if n == 0: return 0.0
        M = s.lat.g0(s.xs, s.ts, s.ys, s.tps); Mi = np.linalg.inv(M); del M
        B = s._B[:n, :n]; B -= Mi; err = np.abs(B).max(); B[...] = Mi; return err
    DW = 1.0
    def _nloc(s, x, t):
        d = np.abs(s.tps - t); d = np.minimum(d, s.lat.beta - d); return (s.ys == x) & (d < s.DW / 2)
    def insert(s, local=False):
        lat = s.lat; N, b = lat.M, lat.beta; n = s._n
        x = s.rng.integers(N); t = s.rng.random() * b
        if local: y = x; tp = (t + (s.rng.random() - 0.5) * s.DW) % b
        else: y = s.rng.integers(N); tp = s.rng.random() * b
        sv = lat.g0(x, t, y, tp)[0, 0]
        if n:
            Mi = s.Minv; u = lat.g0(s.xs, s.ts, y, tp)[:, 0]; v = lat.g0(x, t, s.ys, s.tps)[0]
            Mu = Mi @ u; vM = v @ Mi; S = sv - v @ Mu
        else: S = sv
        s.prop[0] += 1
        if local: fac = s.g ** 2 * N * b * s.DW / ((n + 1) * (1 + s._nloc(x, t).sum()))
        else: fac = s.c / (n + 1) ** 2
        if s.rng.random() < fac * S ** 4:
            s.acc[0] += 1
            if n + 1 >= s.cap: s._alloc(int(1.25 * s.cap) + 16)
            B = s._B
            if n:
                np.multiply.outer(Mu, vM / S, out=s._T[:n, :n]); B[:n, :n] += s._T[:n, :n]
                B[:n, n] = -Mu / S; B[n, :n] = -vM / S
            B[n, n] = 1.0 / S
            s._xs[n], s._ts[n], s._ys[n], s._tps[n] = x, t, y, tp; s._n = n + 1
    def remove(s, local=False):
        n = s._n
        if n == 0: return
        i = s.rng.integers(n)
        if local:
            ok = np.nonzero(s._nloc(s._xs[i], s._ts[i]))[0]
            if len(ok) == 0: return
            j = ok[s.rng.integers(len(ok))]; fac = n * len(ok) / (s.g ** 2 * s.lat.M * s.lat.beta * s.DW)
        else:
            j = s.rng.integers(n); fac = n ** 2 / s.c
        B = s._B; R = B[j, i]
        s.prop[1] += 1
        if s.rng.random() < fac * R ** 4:
            s.acc[1] += 1; ci = B[:n, i].copy(); rj = B[j, :n] / R
            np.multiply.outer(ci, rj, out=s._T[:n, :n]); B[:n, :n] -= s._T[:n, :n]
            l = n - 1; B[j, :n] = B[l, :n]; B[:n, i] = B[:n, l]
            s._xs[i], s._ts[i] = s._xs[l], s._ts[l]; s._ys[j], s._tps[j] = s._ys[l], s._tps[l]; s._n = l
    def shift(s):
        n = s._n; lat = s.lat
        if n == 0: return
        B = s._B; Mi = s.Minv
        if s.rng.random() < 0.5:
            i = s.rng.integers(n); x = s.rng.integers(lat.M); t = s.rng.random() * lat.beta
            vnew = lat.g0(x, t, s.ys, s.tps)[0]; R = vnew @ Mi[:, i]; s.prop[2] += 1
            if s.rng.random() < R ** 4:
                s.acc[2] += 1; dv = vnew - lat.g0(s._xs[i], s._ts[i], s.ys, s.tps)[0]
                ci = Mi[:, i].copy(); np.multiply.outer(ci, (dv @ Mi) / R, out=s._T[:n, :n]); B[:n, :n] -= s._T[:n, :n]
                s._xs[i] = x; s._ts[i] = t
        else:
            j = s.rng.integers(n); y = s.rng.integers(lat.M); tp = s.rng.random() * lat.beta
            unew = lat.g0(s.xs, s.ts, y, tp)[:, 0]; R = Mi[j, :] @ unew; s.prop[3] += 1
            if s.rng.random() < R ** 4:
                s.acc[3] += 1; du = unew - lat.g0(s.xs, s.ts, s._ys[j], s._tps[j])[:, 0]
                rj = Mi[j, :] / R; np.multiply.outer(Mi @ du, rj, out=s._T[:n, :n]); B[:n, :n] -= s._T[:n, :n]
                s._ys[j] = y; s._tps[j] = tp
    def sweep(s, nmoves=None):
        k = nmoves or max(20, 2 * s.n)
        for _ in range(k):
            r = s.rng.random()
            if r < 0.2: s.insert()
            elif r < 0.4: s.remove()
            elif r < 0.55: s.insert(True)
            elif r < 0.7: s.remove(True)
            else: s.shift()
    def counts(s):
        N = s.lat.N; return np.bincount(s.xs, minlength=N) + np.bincount(s.ys, minlength=N)
    def greens(s, taus):
        """full-orbital G(X, t0 + tau; Y, t0) for tau in taus (0 <= tau <= beta; tau=0 -> 0+, beta -> beta-)."""
        lat = s.lat; b = lat.beta; t0 = s.rng.random() * b * (1 - 1e-9); NO = lat.NO; allo = np.arange(NO)
        right = s._right(t0) if s.n else None
        out = []
        for tau in taus:
            t1 = t0 + tau + (1e-10 if tau == 0 else 0.0) - (1e-10 if tau == b else 0.0); sg = 1.0
            if t1 >= b: t1 -= b; sg = -1.0
            G = lat.g0_full(t1 - t0)
            if s.n:
                left = lat.g0_any(allo, t1, s.ys, s.tps)                 # G0(all, t1; ys, tps)
                G = G - left @ (s.Minv @ right)
            out.append(sg * G)
        return out
    def _right(s, t0):
        lat = s.lat; allo = np.arange(lat.NO)
        D = s.ts - t0; sg = np.where(D > 0, 1.0, -1.0); Dp = np.where(D > 0, D, D + lat.beta)
        X, Y = np.broadcast_arrays(s.xs[:, None], allo[None, :])
        return sg[:, None] * lat.S0(np.broadcast_to(Dp[:, None], X.shape).copy(), X, Y)

REC = [
 'mirror alone, beta = 8, Dirac-point gap, cosh band L = 4; L = 6: g/t 0.5 [0.07,0.08];[0.01,0.04], 1 [0.07,0.09];[0.00,0.05], 2 [0.10,0.12];[0.05,0.09], 4 [0.34,0.39];[0.27,0.30], 8 [0.87,0.91];[0.85,0.90], 16 [0.92,0.99];[0.87,0.98]; inf = g exactly',
 'same, midpoint (lower-bound style) band: g/t <= 2 <= 0.02 at both L; 4 [0.16,0.20];[0.11,0.13]; 8 [0.67,0.72];[0.60,0.68]; 16 [0.75,0.80];[0.63,0.77]',
 'pair (6, charge 2) xi/L L = 4 -> 6 at beta = 8: g/t 0.5 0.082->0.053, 1 0.085->0.053, 2 0.093->0.058, 4 0.158->0.101, 8 0.038->0.037, 16 0.021->0.008',
 'S/N(L=4)/S/N(L=6), min-max over 7 channels (site pair, adjoint, singlet density; bond pair sym/antisym, bond adjoint, bond singlet; peak Q): beta = 8 g/t 0.5..16: 3.06-3.38, 3.06-3.38, 3.05-3.35, 2.95-3.72, 2.80-3.41, 2.61-3.53 (volume ratio 3.375)',
 'beta = 4, cosh gap L = 4; L = 6: g/t 2 [0.16,0.18];[0.13,0.15], 4 [0.42,0.43];[0.40,0.42], 8 [0.66,0.71];[0.68,0.71]; S/N ratios 3.07-3.44; chi_h max <= 1.44 in all runs',
 'light release (t = 0.125, w = 0.25, beta = 8, L = 4): light cosh gap at g/t 1, 2, 4, 8, 16 = 0.249, 0.248, 0.239, 0.135, 0.054 (L = 6 at 8: 0.141); mirror 0.251, 0.256, 0.281, 0.69, 1.84 (L = 6: 0.66)',
]
# ================================================================== runner body
import os, time
from math import sqrt
import scipy.sparse as sp
from scipy.linalg import expm
from scipy.optimize import brentq
T00 = time.time(); NP = [0, 0]
def check(name, ok, detail=''):
    NP[0 if ok else 1] += 1; print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ''))
def jw(nmod):
    D = 1 << nmod; out = []
    for p in range(nmod):
        r, c, v = [], [], []
        for st in range(D):
            if st >> p & 1: r.append(st ^ (1 << p)); c.append(st); v.append((-1) ** bin(st & ((1 << p) - 1)).count('1'))
        out.append(sp.csr_matrix((np.array(v, float), (r, c)), shape=(D, D)))
    return out
rng = np.random.default_rng(1)

print('== A. theorems: sign, block term, Dirac band, light release')
# A1: exact time-ordered traces = det(M)^4 for a real band with a light orbital mixed to a mirror orbital (vertices on the mirror only)
no = 2; a = jw(4 * no); op = lambda f, o: a[f * no + o]
def traces(H0, nconf=10):
    h0 = sum(H0[i, j] * op(f, i).conj().T @ op(f, j) for f in range(4) for i in range(no) for j in range(no) if H0[i, j] != 0).toarray()
    C = (op(0, 0) @ op(1, 0) @ op(2, 0) @ op(3, 0)).toarray(); beta = 1.3; Z0 = np.trace(expm(-beta * h0)); e, U = np.linalg.eigh(H0)
    lz = np.logaddexp(0, -beta * e); res = []
    def g0(t1, t2):
        D = t1 - t2; return (1 if D > 0 else -1) * np.sum(U[0] * U[0].conj() * np.exp(-(D if D > 0 else D + beta) * e - lz))
    for n in (1, 2, 3):
        for _ in range(nconf // 3 + 1):
            ts = rng.random(n) * beta; tps = rng.random(n) * beta
            V = sorted([(t, C) for t in ts] + [(t, C.conj().T) for t in tps], key=lambda z: -z[0])
            M = expm(-(beta - V[0][0]) * h0)
            for k, (t, O) in enumerate(V): M = M @ O @ expm(-(t - (V[k + 1][0] if k + 1 < len(V) else 0.0)) * h0)
            res.append((np.trace(M) / Z0, np.linalg.det(np.array([[g0(x, y) for y in tps] for x in ts])) ** 4))
    return res
res = traces(np.array([[0.3, 0.7], [0.7, -0.2]]))
check('A1 THEOREM (toy-qmc A1 + light layer) any real band incl. a real light-mirror mixing, vertices on mirror blocks only: '
      'every weight is det(M)^4 >= 0 (M real); the Dirac mirror, block quartic and light layer are sign-free',
      max(abs(x - y) for x, y in res) < 1e-12 and min(x.real for x, y in res) > -1e-14, f"max|trace - det^4| {max(abs(x - y) for x, y in res):.1e}")
Hf = np.array([[0, -0.6 * np.exp(0.7j), -0.5], [-0.6 * np.exp(-0.7j), 0, -0.4], [-0.5, -0.4, 0.2]]); ef, Uf = np.linalg.eigh(Hf); bf = 1.3
def g0f(x, t1, y, t2):
    D = t1 - t2; return (1 if D > 0 else -1) * np.sum(Uf[x] * Uf[y].conj() * np.exp(-(D if D > 0 else D + bf) * ef - np.logaddexp(0, -bf * ef)))
wf = []
for _ in range(6):
    xs = rng.integers(2, size=2); ys = rng.integers(2, size=2); ts = rng.random(2) * bf; tps = rng.random(2) * bf
    wf.append(np.linalg.det(np.array([[g0f(x, t1, y, t2) for y, t2 in zip(ys, tps)] for x, t1 in zip(xs, ts)])) ** 4)
rI = max(abs(np.imag(x)) / abs(x) for x in wf)
check('A2 THEOREM with a flux (complex band) through a loop holding two vertex blocks the weights det(M)^4 are complex: realness is load-bearing',
      rI > 1e-2, f"max |Im w|/|w| {rI:.2f}")
# A3: uniqueness of the block term (count of G-singlet charge-4 operators on n orbitals per flavour, weight-zero Casimir)
def count(X, wt, norb, k=4):
    import itertools as it
    V = X[0].shape[0] * norb; Xs = [np.kron(x, np.eye(norb)) for x in X]; W = np.kron(wt, np.ones((norb, 1)))
    basis = [b for b in it.combinations(range(V), k) if np.allclose(W[list(b)].sum(0), 0)]; C = 0
    for Y in Xs:
        keys = {}; rows, cols, vals = [], [], []
        for j, b in enumerate(basis):
            for slot in range(k):
                for m in np.nonzero(Y[:, b[slot]])[0]:
                    if m in b and m != b[slot]: continue
                    nb = list(b); nb[slot] = m; s = sorted(nb); sg = (-1) ** sum(1 for p in range(k) for q in range(p + 1, k) if nb[p] > nb[q])
                    rows.append(keys.setdefault(tuple(s), len(keys))); cols.append(j); vals.append(sg * Y[m, b[slot]])
        M = sp.csr_matrix((vals, (rows, cols)), shape=(len(keys), len(basis))); C = C + (M.conj().T @ M).toarray()
    return len(basis), int(np.sum(np.abs(np.linalg.eigvalsh(C)) < 1e-8))
def su4():
    X = []
    for i in range(4):
        for j in range(i + 1, 4):
            A_ = np.zeros((4, 4), complex); A_[i, j] = 1; A_[j, i] = -1; B_ = np.zeros((4, 4), complex); B_[i, j] = B_[j, i] = 1j; X += [A_, B_]
    for k in range(3):
        D = np.zeros((4, 4), complex); D[k, k] = 1j; D[k + 1, k + 1] = -1j; X.append(D)
    return X, np.array([[1 if i == k else (-1 if i == k + 1 else 0) for k in range(3)] for i in range(4)], float)
def spin10():
    c = [m.toarray() for m in jw(5)]; G = []
    for p in range(5): G += [c[p] + c[p].T, 1j * (c[p].T - c[p])]
    ev = [s for s in range(32) if bin(s).count('1') % 2 == 0]
    X = [((G[a_] @ G[b_] - G[b_] @ G[a_]) / 4)[np.ix_(ev, ev)] for a_ in range(10) for b_ in range(a_ + 1, 10)]
    return X, np.array([[(s >> k & 1) - 0.5 for k in range(5)] for s in ev])
cnt = {('SU(4)', n): count(*su4(), n)[1] for n in (1, 2)}; cnt[('Spin(10)', 1)] = count(*spin10(), 1)[1]
SP10_2 = True
if SP10_2: cnt[('Spin(10)', 2)] = count(*spin10(), 2)[1]
check('A3 THEOREM (uniqueness) the SU(4)-singlet charge-4 operators on a block with one mode per flavour span exactly one line '
      '(m1 m2 m3 m4); two orbitals give 5 (not unique); for Spin(10) on the Weyl 16 one orbital gives NONE'
      + (' and two orbitals give exactly one (the pair square)' if SP10_2 else ' (two orbitals: register, one pair square)'),
      cnt[('SU(4)', 1)] == 1 and cnt[('SU(4)', 2)] == 5 and cnt[('Spin(10)', 1)] == 0 and (not SP10_2 or cnt[('Spin(10)', 2)] == 1),
      ', '.join(f"{g_} n={n}: {v}" for (g_, n), v in cnt.items()) + f"  [{time.time() - T00:.0f} s]")
# A4: the block term's symmetries on two blocks (8 modes)
b2 = jw(8); m_ = lambda f, blk: b2[4 * blk + f]
Q = [m_(0, k) @ m_(1, k) @ m_(2, k) @ m_(3, k) for k in (0, 1)]
gens = [sum(X[f, f2] * m_(f, 0).T @ m_(f2, 0) for f in range(4) for f2 in range(4) if X[f, f2] != 0) for X in su4()[0]]
e1 = max(abs((Gn @ Q[0] - Q[0] @ Gn)).max() for Gn in gens)
ePH = abs(m_(0, 0).T @ m_(1, 0).T @ m_(2, 0).T @ m_(3, 0).T - Q[0].T).max()   # a -> (+-) a^+ sends Q to Q^+
e2 = max(abs(Q[0] @ Q[1] - Q[1] @ Q[0]).max(), abs(Q[0] @ Q[1].T - Q[1].T @ Q[0]).max())
Hb = (-(Q[0] + Q[0].T)).toarray()[:16, :16]; eb = np.linalg.eigvalsh(Hb)
check('A4 THEOREM the block term is invariant under SU(4) gauge rotations of its own block (charge 4, det = 1), commutes with every other '
      "block's term and its conjugate, maps to its conjugate under the sublattice particle-hole map, and alone has a unique ground state "
      '(-g, gap g)', e1 < 1e-12 and e2 < 1e-12 and ePH < 1e-12 and abs(eb[0] + 1) < 1e-12 and eb[1] > -1e-12,
      f"max|[T,Q]| {e1:.0e}; PH {ePH:.0e}; max|[Q_b,Q_b']| {e2:.0e}; block levels {np.round(eb[:3], 3)}")
# A5: Dirac band and mixings
S4, H4, _ = stag_band(4, 1.0, False); S6, H6, _ = stag_band(6, 1.0, True)
z4 = np.linalg.eigvalsh(H4); z6 = np.linalg.eigvalsh(H6); ep4 = np.diag((-1.0) ** S4.sum(1)); ep6 = np.diag((-1.0) ** S6.sum(1))
ac = max(abs(H4 @ ep4 + ep4 @ H4).max(), abs(H6 @ ep6 + ep6 @ H6).max())
HH = np.block([[H6, 0.25 * ep6], [0.25 * ep6, H6]]); emix = np.abs(np.linalg.eigvalsh(HH)).min()
Hq = np.block([[H6, 0.25 * (np.eye(216) + ep6) / 2], [0.25 * (np.eye(216) + ep6) / 2, H6]]); eq = np.sort(np.abs(np.linalg.eigvalsh(Hq)))
check('A5 THEOREM the real pi-flux band (eta phases; PBC at L = 4, APBC at L = 6) has exactly 8 zero modes per flavour (2 tastes x 4, the Dirac point '
      'on the grid), first levels 2t, sqrt3 t, and anticommutes with eps_x; the mixing w eps_x (l^+ m + h.c.) gaps every mode by exactly w '
      '((H +- w eps)^2 = H^2 + w^2); the half mixing w (1 + eps)/2 is no mass: 8 zeros stay, branch sqrt(h^2 + w^2/4) - w/2 ~ h^2/w (quadratic)',
      np.sum(abs(z4) < 1e-9) == 8 and np.sum(abs(z6) < 1e-9) == 8 and abs(np.abs(z4[abs(z4) > 1e-9]).min() - 2) < 1e-9
      and abs(np.abs(z6[abs(z6) > 1e-9]).min() - sqrt(3)) < 1e-9 and ac < 1e-12 and abs(emix - 0.25) < 1e-12 and np.sum(eq < 1e-9) == 8 and np.min(np.abs(eq - (sqrt(3 + 0.25 ** 2 / 4) - 0.125))) < 1e-9,
      f"zeros 8, 8; |{{H,eps}}| {ac:.0e}; mixed gap {emix:.4f}")
# A6: light release (Golterman-Shamir / far-end algebra) on the 8-dim Dirac space: G_l^-1 = i w_n - w^2 / (i w_n - Sigma_m(i w_n))
wmix = 0.25; om = np.array([1e-3, 1e-2, 0.1])
Gl_free = 1 / np.abs(1j * om - wmix ** 2 / (1j * om)); Gl_smg = 1 / np.abs(1j * om - wmix ** 2 / (1j * om - 1.0 / (1j * om)))
check('A6 THEOREM at the Dirac point G_l = [i w - w_mix^2 G_m^0(i w)]^-1, G_m^0 = (i w - Sigma_m)^-1: free it is bounded (gap w_mix); '
      'if the symmetric mirror has a propagator zero (Sigma_m ~ Delta^2 / i w) the light gets a POLE at w = 0: paired light modes are released', Gl_free[0] < 0.1 and Gl_smg[0] > 100,
      f"|G_l(i w = 1e-3)| free {Gl_free[0]:.3f}, SMG mirror {Gl_smg[0]:.0f}")

print(f'== B. engine vs exact: mirror pair (2 blocks, hop 0.4) + light orbital mixed by 0.5, g = 1, beta = 2  [{time.time() - T00:.0f} s]')
t_, w_, beta, g_ = 0.4, 0.5, 2.0, 1.0
H0 = np.array([[0, -t_, w_], [-t_, 0, 0], [w_, 0, 0.]]); no3 = 3; a3 = jw(12); op3 = lambda f, o: a3[f * no3 + o]
h0 = sum(H0[i, j] * op3(f, i).T @ op3(f, j) for f in range(4) for i in range(3) for j in range(3) if H0[i, j] != 0)
Cq = [op3(0, x) @ op3(1, x) @ op3(2, x) @ op3(3, x) for x in range(2)]; Hint = -g_ * sum(X + X.T for X in Cq); H = (h0 + Hint).tocsr()
nt = np.array([bin(s_).count('1') for s_ in range(1 << 12)]); secs = [np.nonzero(nt % 4 == q_)[0] for q_ in range(4)]; E, Us = {}, {}
for q_, ii in enumerate(secs): E[q_], Us[q_] = np.linalg.eigh(H[ii][:, ii].toarray())
em = min(E[q_].min() for q_ in range(4)); Z = sum(np.exp(-beta * (E[q_] - em)).sum() for q_ in range(4))
eH = sum(np.sum(np.exp(-beta * (E[q_] - em)) * np.einsum('ij,ik,kj->j', Us[q_], Hint[secs[q_]][:, secs[q_]].toarray(), Us[q_])) for q_ in range(4)) / Z
def Gex(orb, tau):
    c = op3(0, orb); tot = 0
    for q_ in range(4):
        qq = (q_ - 1) % 4; Mq = Us[qq].T @ c[secs[qq]][:, secs[q_]].toarray() @ Us[q_]
        tot += np.sum(np.exp(-(beta - tau) * (E[q_][None, :] - em)) * np.exp(-tau * (E[qq][:, None] - em)) * Mq ** 2)
    return tot / Z
q = CTINT(Lattice(0, t_, beta, Hcustom=H0, nv=2), g_, 3)
for _ in range(300): q.sweep()
Es, Gl = [], []
for k in range(9000):
    q.sweep(); Es.append(-2 * q.n / beta)
    if k % 4 == 0: Gl.append(q.greens([beta / 2])[0][2, 2])
    if k % 100 == 0: q.recompute()
def mse(x, nb=16):
    x = np.asarray(x); b = len(x) // nb; m = x[:nb * b].reshape(nb, b).mean(1); return m.mean(), m.std() / sqrt(nb - 1)
e1_, e2_ = mse(Es), mse(Gl); gx = Gex(2, beta / 2)
check('B1 FINITE CHECK CT-INT reproduces the exact <H_int> and the LIGHT propagator G_l(beta/2) of the mixed model within 4 sigma',
      abs(e1_[0] - eH) < 4 * e1_[1] + 3e-3 and abs(e2_[0] - gx) < 4 * e2_[1] + 1e-3,
      f"<H_int> {e1_[0]:.4f}+-{e1_[1]:.4f} vs {eH:.4f}; G_l {e2_[0]:.4f}+-{e2_[1]:.4f} vs {gx:.4f}")

print(f'== C. live seeded runs: block quartic on the Dirac sea (g = 1 unless stated; beta in units of 1/g)  [{time.time() - T00:.0f} s]')
def run(L, t, g, w, beta, nsw, seed):
    lat = Lattice(L, t, beta, w=w); N = lat.N; q = CTINT(lat, g, seed); k = 0
    while q.n < 0.2 * g * beta * N and k < 200: q.sweep(); k += 1
    for _ in range(nsw // 5): q.sweep()
    q.recompute(); S = lat.S; P0 = lat.P0; v1 = [np.exp(2j * np.pi * S[:, a_] / L) for a_ in range(3)]; taus = [0, beta / 4, beta / 2, 3 * beta / 4, beta]
    TD, TL, PA, PB = [], [], [], []
    for s_ in range(nsw):
        if s_ % 30 == 0: q.recompute()
        q.sweep()
        if s_ % 2 == 0:
            Gs = q.greens(taus); F = Gs[0][:N, :N] ** 2; PA.append(F.sum() / N); PB.append(np.mean([np.real(v @ F @ v.conj()) / N for v in v1]))
            TD.append([np.trace(P0.T @ X[:N, :N] @ P0) / 8 for X in Gs])
            if w is not None: TL.append([np.trace(P0.T @ X[N:, N:] @ P0) / 8 for X in Gs])
    B = lambda x: np.array(x)[:len(x) // 8 * 8].reshape(8, -1, *np.shape(x)[1:]).mean(1)
    def jk(b, f):
        v = np.array([f(np.delete(b, i, 0).mean(0)) for i in range(8)]); return f(b.mean(0)), sqrt(7 * v.var())
    def mid(m): return -2 / beta * np.log(min(max(2 * m[2] / (m[0] + m[4]), 1e-6), 1.0))
    def cq(m):
        r = 2 * m[1] / (m[0] + m[4]); f = lambda d: np.cosh(d * beta / 4) / np.cosh(d * beta / 2) - r
        return 0.0 if r >= 1 else brentq(f, 1e-9, 50.0)
    pa, pb = B(PA), B(PB); xi = lambda m: sqrt(max(m[0] / m[1] - 1, 0)) / (2 * np.sin(np.pi / L)) / L
    o = dict(SN=pa.mean() / N, xiL=jk(np.stack([pa, pb], 1), xi)[0], gD=jk(B(TD), mid), cD=jk(B(TD), cq), n2=2 * q.n)
    if w is not None: o['cL'] = jk(B(TL), cq)
    return o
def show(tag, o):
    print(f"   {tag:10s} S_pair/N {o['SN']:.4f} xi/L {o['xiL']:.3f} | Dirac gap: midpoint {o['gD'][0]:.3f}({o['gD'][1]:.3f}) cosh {o['cD'][0]:.3f}({o['cD'][1]:.3f})"
          + (f" | LIGHT cosh gap {o['cL'][0]:.3f}({o['cL'][1]:.3f})" if 'cL' in o else '') + f"  [{time.time() - T00:.0f} s]")
R = {}
for tag, args in (('m_g1_L4', (4, 1.0, 1.0, None, 8.0, 800, 61)), ('m_g8_L4', (4, 0.125, 1.0, None, 8.0, 400, 62)),
                  ('m_g8_L4b4', (4, 0.125, 1.0, None, 4.0, 800, 63)), ('m_g8_L6b4', (6, 0.125, 1.0, None, 4.0, 250, 64)),
                  ('gs_weak', (4, 0.125, 0.125, 0.25, 8.0, 1000, 65)), ('gs_g8', (4, 0.125, 1.0, 0.25, 8.0, 500, 66))):
    R[tag] = run(*args); show(tag, R[tag])
a_, b_, c_, d_, e_, f_ = (R[k] for k in ('m_g1_L4', 'm_g8_L4', 'm_g8_L4b4', 'm_g8_L6b4', 'gs_weak', 'gs_g8'))
check('C1 FINITE DIAGNOSTIC weak coupling g/t = 1 (L = 4, beta = 8): the Dirac mirror stays massless (midpoint gap at the Dirac point < 0.05) and unpaired',
      a_['gD'][0] < 0.05 and a_['xiL'] < 0.15, f"gap {a_['gD'][0]:.3f}; pair xi/L {a_['xiL']:.3f}")
check('C2 FINITE DIAGNOSTIC strong coupling g/t = 8 (L = 4, beta = 8): the Dirac mirror is gapped (midpoint lower end >= 0.4) with no pair order (xi/L < 0.1)',
      b_['gD'][0] - 2 * b_['gD'][1] >= 0.4 and b_['xiL'] < 0.1, f"gap {b_['gD'][0]:.3f}({b_['gD'][1]:.3f}); xi/L {b_['xiL']:.3f}")
check('C3 FINITE DIAGNOSTIC g/t = 8 at beta = 4: S_pair/N falls about as the volume from L = 4 to 6 (ratio > 2.5; 3.375 = no order) and the Dirac gap '
      'is L-independent (cosh estimates within 0.1)', c_['SN'] / d_['SN'] > 2.5 and abs(c_['cD'][0] - d_['cD'][0]) < 0.1 and d_['gD'][0] > 0.25,
      f"S/N ratio {c_['SN'] / d_['SN']:.2f}; cosh gap {c_['cD'][0]:.3f} vs {d_['cD'][0]:.3f}")
check('C4 FINITE DIAGNOSTIC light release: light mixed by w eps (free gap w = 0.25) keeps w at g/t = 1 (within 0.03); at g/t = 8, mirror '
      'symmetric and gapped (> 0.5), the light gap falls below 0.2: the mirror gap does NOT keep the partners gapped', abs(e_['cL'][0] - 0.25) < 0.03 and f_['cD'][0] > 0.5 and f_['cL'][0] + 2 * f_['cL'][1] < 0.2,
      f"light gap {e_['cL'][0]:.3f} -> {f_['cL'][0]:.3f}({f_['cL'][1]:.3f}); mirror gap {f_['cD'][0]:.3f}")

print('== D. recorded production values (prod.py, 85 s segments; recorded, not recomputed; no PASS depends on them)')
for line in REC: print('   recorded production value (not recomputed): ' + line)
print('supplied: SU(4) toy, one mode per flavour per block, real pi-flux band, BCs, w eps mixing, sizes, betas, seeds')
print('cited: qmc-face-gapped (#9983), toy-qmc (#9965), register CL-1 far-end and SMG items, smg-literature (Ayyar-Chandrasekharan)')
print(f'elapsed {time.time() - T00:.1f} s')
print(f'TOTAL: PASS={NP[0]} FAIL={NP[1]}')
