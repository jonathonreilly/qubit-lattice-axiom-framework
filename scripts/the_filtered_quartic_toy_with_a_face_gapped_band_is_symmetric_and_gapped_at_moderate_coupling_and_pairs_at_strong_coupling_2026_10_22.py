AUDIT_INPUT_PATHS = ('docs/THE_FILTERED_QUARTIC_TOY_WITH_A_FACE_GAPPED_BAND_IS_SYMMETRIC_AND_GAPPED_AT_MODERATE_COUPLING_AND_PAIRS_AT_STRONG_COUPLING_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""qmc-face-gapped: sign-free CT-INT of the cube-filtered SU(4) toy with a REAL free band whose Fermi set avoids the zone faces.
H = sum_k eps_k a+a - g sum_x [(1 - lam)(c1c2c3c4)(cube x) + lam (a1a2a3a4)(site x) + h.c.],  eps_k = t sum_i (1 - cos k_i)/2
(face-gapped band of composite-band-3d: zero only at Gamma; X, M, R at t, 2t, 3t). Supplied toy, NOT Spin(10); g = 1.
 A  sign theorem (mixed vertices)  B  engine vs ED  C  live seeded runs (beta = 4): g/t = 2, 8 at L = 4, 6; lam = 1 control
 D  recorded production values (prod.py; NOT recomputed, no PASS depends on them). Self-contained, reads no files."""
AUDIT_TIMEOUT_SEC = 120
import itertools, time
import numpy as np

class Lattice:
    def __init__(s, L, t, beta, A=None, H=None, band='nn', lam=0.0):
        s.L, s.t, s.beta = L, t, beta
        if A is None:
            S = list(itertools.product(range(L), repeat=3)); s.S = np.array(S); N = len(S)
            idx = {v: i for i, v in enumerate(S)}
            A = np.zeros((N, N)); H = np.zeros((N, N))
            for i, v in enumerate(S):
                for c in itertools.product((0, 1), repeat=3):
                    A[i, idx[tuple((a + b) % L for a, b in zip(v, c))]] += 8 ** -0.5
                for d in range(3):
                    w = list(v); w[d] = (w[d] + 1) % L; j = idx[tuple(w)]
                    if band == 'nn': H[i, j] -= t; H[j, i] -= t
                    else: H[i, j] -= t / 4; H[j, i] -= t / 4; H[i, i] += t / 2   # face-gapped: eps = t sum_i (1 - cos k_i)/2
            s.Q = np.array(list(itertools.product(range(L), repeat=3))) * 2 * np.pi / L
            s.P = np.exp(1j * s.Q @ s.S.T)                          # P[Q, x]
        s.N = A.shape[0]
        blocks, wts = [], []                                        # vertex orbitals: cube-filtered (weight 1 - lam), on-site (weight lam)
        if lam < 1: blocks.append(A); wts.append(1.0 - lam)
        if lam > 0: blocks.append(np.eye(A.shape[1])); wts.append(lam)
        A = np.vstack(blocks); s.nt = len(blocks); s.M = A.shape[0]; s.w = np.repeat(wts, s.N)
        s.A = A; s.K = A @ A.T
        e, U = np.linalg.eigh(H); s.eps = e; s.Bm = A @ U           # c_o = sum_k Bm[o,k] a_k
        s.lz = np.logaddexp(0.0, -beta * e)
        s.free = bool(np.allclose(H, 0)); s.tab = None
        if not s.free and s.N == L ** 3 and L > 0:     # translation-invariant torus: tabulate G0(type a at 0 -> type b at r, Delta)
            M = 8000; s.h = beta / M; dl = np.arange(M + 1) * s.h; dl[0] = 1e-13; N = s.N
            W = np.exp(-dl[:, None] * e[None, :] - s.lz[None, :])
            s.tab = np.array([[(W * s.Bm[a * N]) @ s.Bm[b * N:(b + 1) * N].T for b in range(s.nt)] for a in range(s.nt)])
            idx = {tuple(v): i for i, v in enumerate(s.S)}
            s.dmap = np.array([[idx[tuple((s.S[y] - s.S[x]) % L)] for y in range(s.N)] for x in range(s.N)])
    def g0(s, xs, ts, ys, tps):
        """G0(x_i t_i ; y_j t'_j) matrix (real)."""
        xs = np.atleast_1d(xs); ys = np.atleast_1d(ys); ts = np.atleast_1d(ts); tps = np.atleast_1d(tps)
        if s.free:
            out = s.K[np.ix_(xs, ys)]; out *= 0.5; out[np.less_equal.outer(ts, tps)] *= -1.0; return out
        D = np.subtract.outer(ts, tps); sg = np.where(D > 0, 1.0, -1.0)
        if s.tab is not None:
            Dp = np.where(D > 0, D, D + s.beta) / s.h; m = np.minimum(Dp.astype(int), s.tab.shape[2] - 2); f = Dp - m
            N = s.N; ta = (xs // N)[:, None]; tb = (ys // N)[None, :]; r = s.dmap[np.ix_(xs % N, ys % N)]
            return sg * ((1 - f) * s.tab[ta, tb, m, r] + f * s.tab[ta, tb, m + 1, r])
        Dp = np.where(D > 0, D, D + s.beta); out = np.empty(D.shape); Bx = s.Bm[xs]; By = s.Bm[ys]
        ch = max(1, int(2e6 // (D.shape[1] * s.N)))
        for a in range(0, D.shape[0], ch):
            W = np.exp(-Dp[a:a + ch, :, None] * s.eps - s.lz)       # (chunk, ny, N)
            out[a:a + ch] = np.einsum('ik,jk,ijk->ij', Bx[a:a + ch], By, W)
        return sg * out

class CTINT:
    """vertex arrays and M^-1 live in fixed-capacity buffers (constant memory); rows of M^-1 = C^+ vertices, columns = C."""
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
    DW = 1.0   # local-pair time window
    def _nloc(s, x, t, excl=-1):
        d = np.abs(s.tps - t); d = np.minimum(d, s.lat.beta - d); ok = (s.ys == x) & (d < s.DW / 2)
        if excl >= 0: ok[excl] = False
        return ok
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
        if local: fac = s.g ** 2 * lat.w[x] ** 2 * N * b * s.DW / ((n + 1) * (1 + s._nloc(x, t).sum()))
        else: fac = s.c * lat.w[x] * lat.w[y] / (n + 1) ** 2
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
            j = ok[s.rng.integers(len(ok))]; fac = n * len(ok) / (s.g ** 2 * s.lat.w[s._xs[i]] ** 2 * s.lat.M * s.lat.beta * s.DW)
        else:
            j = s.rng.integers(n); fac = n ** 2 / (s.c * s.lat.w[s._xs[i]] * s.lat.w[s._ys[j]])
        B = s._B; R = B[j, i]
        s.prop[1] += 1
        if s.rng.random() < fac * R ** 4:
            s.acc[1] += 1; ci = B[:n, i].copy(); rj = B[j, :n] / R
            np.multiply.outer(ci, rj, out=s._T[:n, :n]); B[:n, :n] -= s._T[:n, :n]
            l = n - 1; B[j, :n] = B[l, :n]; B[:n, i] = B[:n, l]
            s._xs[i], s._ts[i] = s._xs[l], s._ts[l]; s._ys[j], s._tps[j] = s._ys[l], s._tps[l]; s._n = l
    def shift(s):
        """move one C vertex (column of M^-1) or one C^+ vertex (row) to a new random site/time."""
        n = s._n; lat = s.lat
        if n == 0: return
        B = s._B; Mi = s.Minv
        if s.rng.random() < 0.5:
            i = s.rng.integers(n); x = s.rng.integers(lat.M); t = s.rng.random() * lat.beta
            vnew = lat.g0(x, t, s.ys, s.tps)[0]; R = vnew @ Mi[:, i]; s.prop[2] += 1
            if s.rng.random() < lat.w[x] / lat.w[s._xs[i]] * R ** 4:
                s.acc[2] += 1; dv = vnew - lat.g0(s._xs[i], s._ts[i], s.ys, s.tps)[0]
                ci = Mi[:, i].copy(); np.multiply.outer(ci, (dv @ Mi) / R, out=s._T[:n, :n]); B[:n, :n] -= s._T[:n, :n]
                s._xs[i] = x; s._ts[i] = t
        else:
            j = s.rng.integers(n); y = s.rng.integers(lat.M); tp = s.rng.random() * lat.beta
            unew = lat.g0(s.xs, s.ts, y, tp)[:, 0]; R = Mi[j, :] @ unew; s.prop[3] += 1
            if s.rng.random() < lat.w[y] / lat.w[s._ys[j]] * R ** 4:
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
    # ---------------------------------------------------------------- measurements
    def counts(s):
        N = s.lat.N; return np.bincount(s.xs % N, minlength=N) + np.bincount(s.ys % N, minlength=N)
    def greens(s, nsl, full=False):
        """G(x, tau0 + k beta/nsl ; y, tau0), k = 0..nsl/2 (k = 0: equal time, x just after y); wrap sign removed."""
        lat = s.lat; t0 = s.rng.random() * lat.beta * (1 - 1e-9); allx = np.arange(lat.N)
        for k in range(nsl + 1 if full else nsl // 2 + 1):
            t1 = t0 + k * lat.beta / nsl + (1e-10 if k == 0 else 0.0) - (1e-10 if k == nsl else 0.0); sg = 1.0
            if t1 >= lat.beta: t1 -= lat.beta; sg = -1.0
            T1 = np.full(lat.N, t1); T0 = np.full(lat.N, t0)
            G = lat.g0(allx, T1, allx, T0)
            if s.n:
                G = G - lat.g0(allx, T1, s.ys, s.tps) @ s.Minv @ lat.g0(s.xs, s.ts, allx, T0)
            G *= sg; yield G

# ================================================================== runner body
import os
from math import sqrt
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'
import scipy.sparse as sp
from scipy.linalg import expm
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
def ops(A, H0):
    ns = A.shape[1]; a = jw(4 * ns)
    c = [[sum(A[x, j] * a[f * ns + j] for j in range(ns)) for x in range(A.shape[0])] for f in range(4)]
    h0 = sum(H0[i, j] * a[f * ns + i].conj().T @ a[f * ns + j] for f in range(4) for i in range(ns) for j in range(ns) if H0[i, j] != 0)
    return c, h0, [c[0][x] @ c[1][x] @ c[2][x] @ c[3][x] for x in range(A.shape[0])]
def mse(x, nb=8):
    x = np.asarray(x, float); b = len(x) // nb; m = x[:nb * b].reshape(nb, b, *x.shape[1:]).mean(1); return m.mean(0), m.std(0) / sqrt(nb - 1)
rng = np.random.default_rng(1)

print('== A. sign with the face-gapped band and mixed (cube-filtered + on-site) vertices')
A2 = np.array([[0.9, 0.3], [0.2, 0.95]]); Am = np.vstack([A2, np.eye(2)]); beta = 1.7
H0r = np.array([[0.5, -0.125], [-0.125, 0.5]])          # real band, eps >= 0 (two-site face-gapped analogue)
c, h0, C = ops(Am, H0r); h0d = h0.toarray(); Z0 = np.trace(expm(-beta * h0d)); lat = Lattice(0, 0, beta, A=Am, H=H0r, lam=0.0)   # vertex orbitals = the 4 rows of Am
res = []
for n in (1, 2, 3):
    for _ in range(4):
        xs = rng.integers(4, size=n); ys = rng.integers(4, size=n); ts = rng.random(n) * beta; tps = rng.random(n) * beta
        V = sorted([(t, C[x].toarray()) for x, t in zip(xs, ts)] + [(t, C[y].conj().T.toarray()) for y, t in zip(ys, tps)], key=lambda z: -z[0])
        M = expm(-(beta - V[0][0]) * h0d)
        for k, (t, O) in enumerate(V): M = M @ O @ expm(-(t - (V[k + 1][0] if k + 1 < len(V) else 0.0)) * h0d)
        res.append((np.trace(M) / Z0, np.linalg.det(lat.g0(xs, ts, ys, tps)) ** 4))
check('A1 THEOREM (toy-qmc A1, extended) with any real band and any real vertex orbitals (filtered and on-site rows mixed, each '
      'vertex weighted by its real coupling) the exact time-ordered trace of every configuration is det(M)^4 >= 0: the face-gapped '
      'band and the on-site/filtered interpolation stay sign-free', max(abs(a - b) for a, b in res) < 1e-12 and min(a.real for a, b in res) > -1e-14,
      f"max|trace - det^4| {max(abs(a - b) for a, b in res):.1e}; min trace {min(a.real for a, b in res):.1e}")

print(f'== B. engine (local + global pair moves, mixed vertices) vs exact: 3-site ring, lam = 0.5, t = 0.3, beta = 3  [{time.time() - T00:.0f} s]')
A3 = np.zeros((3, 3)); H3 = np.zeros((3, 3))
for x in range(3): A3[x, x] += 2 ** -0.5; A3[x, (x + 1) % 3] += 2 ** -0.5; H3[x, (x + 1) % 3] -= 0.3; H3[(x + 1) % 3, x] -= 0.3
_, h0, C = ops(A3, H3); _, _, Cs = ops(np.eye(3), H3); beta = 3.0
Hint = -0.5 * sum(X + X.conj().T for X in C) - 0.5 * sum(X + X.conj().T for X in Cs); H = (h0 + Hint).tocsr()
nt = np.array([bin(s_).count('1') for s_ in range(1 << 12)]); Z = 0.0; ex = 0.0
for q4 in range(4):
    ii = np.nonzero(nt % 4 == q4)[0]; e, U = np.linalg.eigh(H[ii][:, ii].toarray()); w = np.exp(-beta * (e + 6)); Z += w.sum()
    ex += np.sum(w * np.einsum('ij,ik,kj->j', U, Hint[ii][:, ii].toarray(), U))
ex /= Z; q = CTINT(Lattice(0, 0.3, beta, A=A3, H=H3, lam=0.5), 1.0, 5); Es = []
for _ in range(300): q.sweep()
for k in range(16000):
    q.sweep(); Es.append(-2 * q.n / beta)
    if k % 100 == 0: q.recompute()
eH = mse(Es, 16)
check('B1 FINITE CHECK CT-INT reproduces the exact <H_int> of the mixed model within 4 sigma', abs(eH[0] - ex) < 4 * eH[1] + 3e-3,
      f"{eH[0]:.4f}+-{eH[1]:.4f} vs exact {ex:.4f}")

print(f'== C. live seeded 3D runs: face-gapped band eps = t sum_i (1 - cos k_i)/2 (Fermi set = Gamma only), g = 1, beta = 4  [{time.time() - T00:.0f} s]')
def run(L, t, beta, nsw, seed, lam=0.0, me=2):
    lat = Lattice(L, t, beta, band='fg', lam=lam); N = lat.N; q = CTINT(lat, 1.0, seed); k = 0
    while q.n < 0.3 * beta * N and k < 300: q.sweep(); k += 1
    for _ in range(nsw // 5): q.sweep()
    q.recompute(); S = lat.S; v1 = [np.exp(2j * np.pi * S[:, a] / L) for a in range(3)]
    CH, P0, P1, GP, GE = [], [], [], [], []
    for s_ in range(nsw):
        if s_ % 20 == 0: q.recompute()
        q.sweep(); nq = lat.P @ q.counts(); CH.append((np.abs(nq[1:]) ** 2 - 2 * q.n) / (beta * N))
        if s_ % me == 0:
            Gs = list(q.greens(2, full=True)); F = Gs[0] ** 2
            P0.append(F.sum() / N); P1.append(np.mean([np.real(v @ F @ v.conj()) / N for v in v1]))
            GP.append([(G ** 2).sum() / N for G in Gs]); GE.append([G.sum() / N for G in Gs])
    B = lambda x: np.array(x)[:len(x) // 8 * 8].reshape(8, -1, *np.shape(x)[1:]).mean(1)
    p0, p1, gp, ge, ch = B(P0), B(P1), B(GP), B(GE), B(CH)
    xi = lambda a, b: np.sqrt(a / b - 1) / (2 * np.sin(np.pi / L)) / L
    jk = np.array([xi(np.delete(p0, i).mean(), np.delete(p1, i).mean()) for i in range(8)])
    def gap(g):   # midpoint estimator -(2/beta) ln(2 G(beta/2)/(G(0+) + G(beta-))), lower end of a 2-sigma band; a zero mode gives 0
        r = 2 * g[:, 1] / (g[:, 0] + g[:, 2]); rm, re = r.mean(), r.std() / sqrt(7); return -2 / beta * np.log(min(max(rm + 2 * re, re, 1e-6), 1.0))
    return dict(xiL=xi(p0.mean(), p1.mean()), dxi=sqrt(7 * jk.var()), SN=p0.mean() / N, gp=gap(gp), ge=gap(ge),
                chimax=ch.mean(0).max(), chimean=ch.mean(), L=L, nsw=nsw)
cfg = [('g2_L4', 4, 0.5, 900, 0.0), ('g2_L6', 6, 0.5, 400, 0.0), ('g8_L4', 4, 0.125, 900, 0.0), ('g8_L6', 6, 0.125, 400, 0.0),
       ('lam1_L4', 4, 0.125, 500, 1.0)]
R = {}
for tag, L, t, nsw, lam in cfg:
    R[tag] = o = run(L, t, 4.0, nsw, seed=31 + L, lam=lam)
    print(f"   {tag:8s} L={L} g/t={1 / t:.0f} lam={lam:.0f} {nsw} sweeps: S_pair/N {o['SN']:.4f} xi/L {o['xiL']:.3f}({o['dxi']:.3f}) | "
          f"gap lower ends: pair(Q=0) {o['gp']:.2f} elem(Gamma) {o['ge']:.2f} | chi_h max {o['chimax']:.2f} mean {o['chimean']:.2f}  [{time.time() - T00:.0f} s]")
a, b, c_, d, e_ = (R[k] for k in ('g2_L4', 'g2_L6', 'g8_L4', 'g8_L6', 'lam1_L4'))
check('C1 FINITE DIAGNOSTIC g/t = 2 (filtered, lam = 0) is pair-disordered and gapped: S_pair/N falls > 2x from L = 4 to 6, '
      'xi/L falls, and the pair and Gamma-elementary gap lower ends stay >= 0.2 at both sizes',
      a['SN'] / b['SN'] > 2 and b['xiL'] < a['xiL'] and min(a['gp'], b['gp'], a['ge'], b['ge']) >= 0.2,
      f"S_pair/N ratio {a['SN'] / b['SN']:.2f}; xi/L {a['xiL']:.3f} -> {b['xiL']:.3f}")
check('C2 FINITE DIAGNOSTIC g/t = 8 (lam = 0) is not disordering: xi/L does not fall by more than 0.03 from L = 4 to 6 and S_pair/N falls '
      'by less than 2.5x (pair order at strong coupling survives the face-gapped band)',
      d['xiL'] > c_['xiL'] - 0.03 and c_['SN'] / d['SN'] < 2.5, f"S_pair/N ratio {c_['SN'] / d['SN']:.2f}; xi/L {c_['xiL']:.3f} -> {d['xiL']:.3f}")
check('C3 FINITE DIAGNOSTIC no translation order in the filtered runs: Q-averaged chi_h <= 0.4 and largest <= 1.5',
      all(o['chimean'] <= 0.4 and o['chimax'] <= 1.5 for o in (a, b, c_, d)), 'max chi_h ' + ', '.join(f"{o['chimax']:.2f}" for o in (a, b, c_, d)))
check('C4 FINITE DIAGNOSTIC control lam = 1 (on-site quartic, same band, g/t = 8): no pair correlations (xi/L < 0.1) and a gapped '
      'Gamma elementary (lower end >= 0.3): the on-site model is symmetric and gapped where the filtered one pairs',
      e_['xiL'] < 0.1 and e_['ge'] >= 0.3, f"xi/L {e_['xiL']:.3f}; gap lower end {e_['ge']:.2f}")

print('== D. recorded production values (prod.py, beta = 8; recorded, not recomputed; no PASS depends on them)')
for line in ('lam=0 xi/L L=4 -> L=6: g/t=1 0.184->0.116, 2 0.241->0.179, 4 0.335->0.349, 8 0.370->0.426, 16 0.393->0.464, inf 0.407->0.501',
             'lam=0 S_pair/N L=4 -> L=6: g/t=1 0.055->0.016, 2 0.063->0.021, 4 0.080->0.043, 8 0.081->0.052, 16 0.085->0.054, inf 0.082->0.056',
             'lam=0 pair-gap band (L=4; L=6): g/t=1 [1.42,1.55]; [1.41,1.54], 2 [0.50,0.61]; [0.33,0.51], 4 [0.25,0.28]; [0.07,0.15], 8 [0.16,0.20]; [0.05,0.09]',
             'g/t=8 lam=0.5: xi/L 0.284->0.279, S_pair/N 0.064->0.030; lam=1: xi/L 0.004->0.003, pair gap [0.84,0.92]; [0.77,0.87]'):
    print('   recorded production value (not recomputed): ' + line)
print('supplied: toy content (4 modes, SU(4)-singlet quartic, not Spin(10)), the face-gapped band, lam, sizes, betas, seeds, g = 1')
print('cited: toy-qmc (#9965) A1/E1, smg-ladder (face Fermi lines, 1D window), composite-band-3d (band (1 - cos q)/2)')
print(f'elapsed {time.time() - T00:.1f} s')
print(f'TOTAL: PASS={NP[0]} FAIL={NP[1]}')
