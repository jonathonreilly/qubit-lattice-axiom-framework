AUDIT_INPUT_PATHS = ('docs/THE_CUBE_FILTERED_QUARTIC_TOY_IS_SIGN_FREE_AND_PAIRS_AT_STRONG_COUPLING_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""toy-qmc: sign-free CT-INT QMC of the cube-filtered SU(4) toy (composite-band-3d): is its 3D strong-coupling phase symmetric?
H = -t sum_<ij>,f a+a  - g sum_x (c1 c2 c3 c4 + h.c.)(x),  c_fx = 8^-1/2 sum_corners a_f  (supplied toy, NOT Spin(10)); g = 1.
 A  sign theorem (exact traces = det^4)   B  engine vs ED   C  1D control
 D  live seeded 3D runs (fixed sweep counts): L = 4, 6; beta = 4, 8; t = 0, 0.25   E  variational ladder
 F  recorded production values (prod.py, NOT recomputed; no PASS depends on them). Self-contained, reads no files."""
AUDIT_TIMEOUT_SEC = 120
import itertools, time
import numpy as np

class Lattice:
    def __init__(s, L, t, beta, A=None, H=None):
        s.L, s.t, s.beta = L, t, beta
        if A is None:
            S = list(itertools.product(range(L), repeat=3)); s.S = np.array(S); N = len(S)
            idx = {v: i for i, v in enumerate(S)}
            A = np.zeros((N, N)); H = np.zeros((N, N))
            for i, v in enumerate(S):
                for c in itertools.product((0, 1), repeat=3):
                    A[i, idx[tuple((a + b) % L for a, b in zip(v, c))]] += 8 ** -0.5
                for d in range(3):
                    w = list(v); w[d] = (w[d] + 1) % L; j = idx[tuple(w)]; H[i, j] -= t; H[j, i] -= t
            s.Q = np.array(list(itertools.product(range(L), repeat=3))) * 2 * np.pi / L
            s.P = np.exp(1j * s.Q @ s.S.T)                          # P[Q, x]
        s.N = A.shape[0]; s.A = A; s.K = A @ A.T
        e, U = np.linalg.eigh(H); s.eps = e; s.Bm = A @ U           # c_x = sum_k Bm[x,k] a_k
        s.lz = np.logaddexp(0.0, -beta * e)
        s.free = bool(np.allclose(H, 0)); s.tab = None
        if not s.free and A.shape[0] == L ** 3 and L > 0:     # translation-invariant torus: tabulate G0(0 -> r, Delta)
            M = 8000; s.h = beta / M; dl = np.arange(M + 1) * s.h; dl[0] = 1e-13
            W = np.exp(-dl[:, None] * e[None, :] - s.lz[None, :]); s.tab = (W * s.Bm[0]) @ s.Bm.T     # (M+1, N)
            idx = {tuple(v): i for i, v in enumerate(s.S)}
            s.dmap = np.array([[idx[tuple((s.S[y] - s.S[x]) % L)] for y in range(s.N)] for x in range(s.N)])
    def g0(s, xs, ts, ys, tps):
        """G0(x_i t_i ; y_j t'_j) matrix (real)."""
        xs = np.atleast_1d(xs); ys = np.atleast_1d(ys); ts = np.atleast_1d(ts); tps = np.atleast_1d(tps)
        if s.free:
            out = s.K[np.ix_(xs, ys)]; out *= 0.5; out[np.less_equal.outer(ts, tps)] *= -1.0; return out
        D = np.subtract.outer(ts, tps); sg = np.where(D > 0, 1.0, -1.0)
        if s.tab is not None:
            Dp = np.where(D > 0, D, D + s.beta) / s.h; m = np.minimum(Dp.astype(int), len(s.tab) - 2); f = Dp - m
            r = s.dmap[np.ix_(xs, ys)]; return sg * ((1 - f) * s.tab[m, r] + f * s.tab[m + 1, r])
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
        s.c = (g * lat.N * lat.beta) ** 2; s.acc = np.zeros(4); s.prop = np.zeros(4); s._alloc(cap)
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
    def insert(s):
        lat = s.lat; N, b = lat.N, lat.beta; n = s._n
        x = s.rng.integers(N); t = s.rng.random() * b; y = s.rng.integers(N); tp = s.rng.random() * b
        sv = lat.g0(x, t, y, tp)[0, 0]
        if n:
            Mi = s.Minv; u = lat.g0(s.xs, s.ts, y, tp)[:, 0]; v = lat.g0(x, t, s.ys, s.tps)[0]
            Mu = Mi @ u; vM = v @ Mi; S = sv - v @ Mu
        else: S = sv
        s.prop[0] += 1
        if s.rng.random() < s.c / (n + 1) ** 2 * S ** 4:
            s.acc[0] += 1
            if n + 1 >= s.cap: s._alloc(int(1.25 * s.cap) + 16)
            B = s._B
            if n:
                np.multiply.outer(Mu, vM / S, out=s._T[:n, :n]); B[:n, :n] += s._T[:n, :n]
                B[:n, n] = -Mu / S; B[n, :n] = -vM / S
            B[n, n] = 1.0 / S
            s._xs[n], s._ts[n], s._ys[n], s._tps[n] = x, t, y, tp; s._n = n + 1
    def remove(s):
        n = s._n
        if n == 0: return
        i = s.rng.integers(n); j = s.rng.integers(n); B = s._B; R = B[j, i]
        s.prop[1] += 1
        if s.rng.random() < n ** 2 / s.c * R ** 4:
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
            i = s.rng.integers(n); x = s.rng.integers(lat.N); t = s.rng.random() * lat.beta
            vnew = lat.g0(x, t, s.ys, s.tps)[0]; R = vnew @ Mi[:, i]; s.prop[2] += 1
            if s.rng.random() < R ** 4:
                s.acc[2] += 1; dv = vnew - lat.g0(s._xs[i], s._ts[i], s.ys, s.tps)[0]
                ci = Mi[:, i].copy(); np.multiply.outer(ci, (dv @ Mi) / R, out=s._T[:n, :n]); B[:n, :n] -= s._T[:n, :n]
                s._xs[i] = x; s._ts[i] = t
        else:
            j = s.rng.integers(n); y = s.rng.integers(lat.N); tp = s.rng.random() * lat.beta
            unew = lat.g0(s.xs, s.ts, y, tp)[:, 0]; R = Mi[j, :] @ unew; s.prop[3] += 1
            if s.rng.random() < R ** 4:
                s.acc[3] += 1; du = unew - lat.g0(s.xs, s.ts, s._ys[j], s._tps[j])[:, 0]
                rj = Mi[j, :] / R; np.multiply.outer(Mi @ du, rj, out=s._T[:n, :n]); B[:n, :n] -= s._T[:n, :n]
                s._ys[j] = y; s._tps[j] = tp
    def sweep(s, nmoves=None):
        k = nmoves or max(20, 2 * s.n)
        for _ in range(k):
            r = s.rng.random()
            if r < 0.35: s.insert()
            elif r < 0.7: s.remove()
            else: s.shift()
    # ---------------------------------------------------------------- measurements
    def counts(s):
        return np.bincount(s.xs, minlength=s.lat.N) + np.bincount(s.ys, minlength=s.lat.N)
    def greens(s, nsl):
        """G(x, tau0 + k beta/nsl ; y, tau0), k = 0..nsl/2 (k = 0: equal time, x just after y); wrap sign removed."""
        lat = s.lat; t0 = s.rng.random() * lat.beta * (1 - 1e-9); allx = np.arange(lat.N)
        for k in range(nsl // 2 + 1):
            t1 = t0 + k * lat.beta / nsl + (1e-10 if k == 0 else 0.0); sg = 1.0
            if t1 >= lat.beta: t1 -= lat.beta; sg = -1.0
            T1 = np.full(lat.N, t1); T0 = np.full(lat.N, t0)
            G = lat.g0(allx, T1, allx, T0)
            if s.n:
                G = G - lat.g0(allx, T1, s.ys, s.tps) @ s.Minv @ lat.g0(s.xs, s.ts, allx, T0)
            G *= sg; yield G

# ================================================================== runner body
import os, sys, json, itertools
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
def mse(x, nb=16):
    x = np.asarray(x, float); b = len(x) // nb; m = x[:nb * b].reshape(nb, b, *x.shape[1:]).mean(1); return m.mean(0), m.std(0) / sqrt(nb - 1)
rng = np.random.default_rng(1)

print('== A. sign: weight of a CT-INT configuration (n C-vertices, n C^+-vertices) = g^2n det(M)^4, M real')
A2 = np.array([[0.9, 0.3], [0.2, 0.95]]); beta = 1.7
def trace_vs_det(H0):
    c, h0, C = ops(A2, H0); h0d = h0.toarray(); Z0 = np.trace(expm(-beta * h0d)); res = []
    lat = Lattice(0, 0, beta, A=A2, H=H0.real) if np.isrealobj(H0) else None
    for n in (1, 2, 3):
        for _ in range(4):
            xs = rng.integers(2, size=n); ys = rng.integers(2, size=n); ts = rng.random(n) * beta; tps = rng.random(n) * beta
            V = sorted([(t, C[x].toarray()) for x, t in zip(xs, ts)] + [(t, C[y].conj().T.toarray()) for y, t in zip(ys, tps)], key=lambda z: -z[0])
            M = expm(-(beta - V[0][0]) * h0d)
            for k, (t, O) in enumerate(V): M = M @ O @ expm(-(t - (V[k + 1][0] if k + 1 < len(V) else 0.0)) * h0d)
            res.append((np.trace(M) / Z0, np.linalg.det(lat.g0(xs, ts, ys, tps)) ** 4 if lat else np.nan))
    return res
H0r = np.array([[0.3, -0.7], [-0.7, -0.2]]); r = trace_vs_det(H0r)
H0c = H0r.astype(complex); H0c[0, 1] = -0.7 * np.exp(0.9j); H0c[1, 0] = np.conj(H0c[0, 1]); rc = trace_vs_det(H0c)
check('A1 THEOREM the exact time-ordered trace of every sampled configuration (n = 1, 2, 3; generic real hopping, generic real '
      'non-orthogonal filter) equals det(M)^4 >= 0: four flavours share one real determinant, vertex reordering '
      'sign +1, so the SU(4) cube-filtered quartic plus any real free band is sign-free at every g, L, beta',
      max(abs(a - b) for a, b in r) < 1e-12 and min(a.real for a, b in r) > -1e-14,
      f"max|trace - det^4| {max(abs(a - b) for a, b in r):.1e}; min trace {min(a.real for a, b in r):.1e}")
check('A2 THEOREM-CHECK reality is load-bearing: with a complex (flux) hop the same traces are complex (det^4 of a complex matrix)',
      max(abs(a.imag) for a, b in rc) > 1e-3, f"max |Im trace| {max(abs(a.imag) for a, b in rc):.3f}")

print(f'== B. engine vs exact thermal values (3-site ring, 2-site filter, t = 0.3, beta = 3, 12 Fock modes)  [{time.time() - T00:.0f} s]')
A3 = np.zeros((3, 3)); H3 = np.zeros((3, 3))
for x in range(3): A3[x, x] += 2 ** -0.5; A3[x, (x + 1) % 3] += 2 ** -0.5; H3[x, (x + 1) % 3] -= 0.3; H3[(x + 1) % 3, x] -= 0.3
c, h0, C = ops(A3, H3); Hint = -sum(Cx + Cx.conj().T for Cx in C); H = (h0 + Hint).tocsr(); beta = 3.0
nt = np.array([bin(s).count('1') for s in range(1 << 12)]); O = {'H': Hint, 'P': c[0][0] @ c[1][0] @ c[1][1].conj().T @ c[0][1].conj().T}
ex = {k: 0.0 for k in O}; Z = 0.0
for qq in range(4):
    ii = np.nonzero(nt % 4 == qq)[0]; e, U = np.linalg.eigh(H[ii][:, ii].toarray()); w = np.exp(-beta * (e + 6)); Z += w.sum()
    for k, Ok in O.items(): ex[k] += np.sum(w * np.einsum('ij,ik,kj->j', U, Ok[ii][:, ii].toarray(), U))
ex = {k: v / Z for k, v in ex.items()}
q = CTINT(Lattice(0, 0.3, beta, A=A3, H=H3), 1.0, 5); T0 = time.time()
for _ in range(300): q.sweep()
Es, Ps = [], []
for _ in range(20000):
    q.sweep(); Es.append(-2 * q.n / beta); G = next(q.greens(2)); Ps.append(G[0, 1] ** 2)
    if len(Es) % 50 == 0: q.recompute()
eH, eP = mse(Es), mse(Ps)
check('B1 FINITE CHECK CT-INT reproduces exact ED: <H_int> and the pair correlator <D_0 D_1^+> (D = c1 c2, conditional estimator G^2) '
      'within 4 sigma', abs(eH[0] - ex['H']) < 4 * eH[1] + 2e-3 and abs(eP[0] - ex['P']) < 4 * eP[1] + 1e-3,
      f"<H_int> {eH[0]:.4f}+-{eH[1]:.4f} vs {ex['H']:.4f}; pair {eP[0]:.4f}+-{eP[1]:.4f} vs {ex['P']:.4f} ({len(Es)} sweeps)")

print(f'== C. control: 1D ring L = 16, 2-site filter, t = 0, beta = 16 (symmetric by composite-band-3d C5)  [{time.time() - T00:.0f} s]')
L1 = 16; A1 = np.zeros((L1, L1))
for x in range(L1): A1[x, x] += 2 ** -0.5; A1[x, (x + 1) % L1] += 2 ** -0.5
q = CTINT(Lattice(0, 0.0, 16.0, A=A1, H=np.zeros((L1, L1))), 1.0, 11); T0 = time.time()
while q.n < 0.3 * 16 * L1: q.sweep()
for _ in range(30): q.sweep()
pr = []
for _ in range(2500):
    if len(pr) % 20 == 0: q.recompute()
    q.sweep(); P = next(q.greens(2)) ** 2; pr.append([np.mean([P[x, (x + d) % L1] for x in range(L1)]) for d in (1, 2, 4, 8)])
m1, e1 = mse(pr, 8)
check('C1 DIAGNOSTIC the same estimator in 1D shows exponential pair decay (no plateau): the 3D plateau below is not an artefact',
      m1[3] < 0.15 * m1[1] and m1[2] < 0.5 * m1[1], 'pair(d = 1, 2, 4, 8) ' + ', '.join(f'{a:.4f}' for a in m1))


print(f'== D. live seeded 3D runs on L^3 tori (fixed sweep counts; g = 1, atom units)  [{time.time() - T00:.0f} s]')
def run(L, t, beta, nsw, seed, me=2, nb=8):
    lat = Lattice(L, t, beta); N = lat.N; q = CTINT(lat, 1.0, seed); k = 0
    while q.n < 0.3 * beta * N and k < 400: q.sweep(); k += 1
    for _ in range(nsw // 5): q.sweep()
    q.recompute(); dr = 0.0
    S = lat.S; idx = lambda d: np.array([np.ravel_multi_index(tuple((S[i] + d) % L), (L,) * 3) for i in range(N)])
    jr, j1 = idx(np.array([L // 2] * 3)), idx(np.array([1, 1, 1]))
    v1 = [np.exp(2j * np.pi * S[:, a] / L) for a in range(3)]
    E, CH, P0, P1, PR, P111 = [], [], [], [], [], []
    for s_ in range(nsw):
        if s_ % 20 == 0: dr = max(dr, q.recompute())
        q.sweep(); E.append(-2 * q.n / beta / N); nq = lat.P @ q.counts(); CH.append((np.abs(nq[1:]) ** 2 - 2 * q.n) / (beta * N))
        if s_ % me == 0:
            F = next(q.greens(2)) ** 2; P0.append(F.sum() / N); P1.append(np.mean([np.real(v @ F @ v.conj()) / N for v in v1]))
            PR.append(F[np.arange(N), jr].mean()); P111.append(F[np.arange(N), j1].mean())
    B = lambda x: np.array(x)[:len(x) // nb * nb].reshape(nb, -1, *np.shape(x)[1:]).mean(1)
    o = {k_: B(v) for k_, v in dict(E=E, CH=CH, P0=P0, P1=P1, PR=PR, P111=P111).items()}
    xi = lambda p0, p1: np.sqrt(p0 / p1 - 1) / (2 * np.sin(np.pi / L)) / L
    jk = np.array([xi(np.delete(o['P0'], i).mean(), np.delete(o['P1'], i).mean()) for i in range(nb)])
    o['xiL'] = (xi(o['P0'].mean(), o['P1'].mean()), sqrt((nb - 1) * jk.var())); o['drift'] = dr
    o['chimax'] = o['CH'].mean(0).max(); o['chimean'] = o['CH'].mean(); o['L'] = L; o['nsw'] = nsw
    return o
m = lambda o, k: (o[k].mean(), o[k].std() / sqrt(len(o[k]) - 1))
cfg = [('L4b4', 4, 0.0, 4.0, 1500), ('L4b8', 4, 0.0, 8.0, 1500), ('L6b4', 6, 0.0, 4.0, 900), ('L4b8t', 4, 0.25, 8.0, 1200)]
R = {}
for tag, L, t, beta, nsw in cfg:
    R[tag] = o = run(L, t, beta, nsw, seed=17 + L)
    print(f"   {tag:6s} L={L} t={t:.2f} beta={beta:.0f} {nsw} sweeps: E/term {m(o, 'E')[0]:.3f} | chi_h max {o['chimax']:.2f} mean {o['chimean']:.2f} | "
          f"pair(1,1,1) {m(o, 'P111')[0]:.3f} pair(rmax) {m(o, 'PR')[0]:.3f}({m(o, 'PR')[1]:.3f}) | xi/L {o['xiL'][0]:.3f}({o['xiL'][1]:.3f}) | drift {o['drift']:.0e}  [{time.time() - T00:.0f} s]")
a, b, c, d = R['L4b4'], R['L4b8'], R['L6b4'], R['L4b8t']
check('D1 FINITE DIAGNOSTIC (no translation order) in every t = 0 run the Q-average of chi_h is <= 0.4 and its largest Q value <= 1.5, '
      'and at L = 4 the Q-average falls from beta = 4 to 8; the best product pattern ordered at beta = 8 would give ~18 (beta N sigma^2 / 8 Q)',
      max(o['chimean'] for o in (a, b, c)) <= 0.4 and max(o['chimax'] for o in (a, b, c)) <= 1.5 and b['chimean'] < a['chimean'],
      f"Q-mean chi_h beta 4 -> 8: {a['chimean']:.2f} -> {b['chimean']:.2f}")
check('D2 FINITE DIAGNOSTIC (pair plateau) at t = 0 the pair correlation is flat beyond one cube: pair(r_max) >= 0.6 pair(1,1,1) and '
      '>= 0.025 in every t = 0 run (the 1D control, C1, falls 17-fold from d = 2 to d = 8)',
      all(m(o, 'PR')[0] > 0.6 * m(o, 'P111')[0] and m(o, 'PR')[0] > 0.025 for o in (a, b, c)),
      'pair(rmax)/pair(1,1,1) ' + ', '.join(f"{m(o, 'PR')[0] / m(o, 'P111')[0]:.2f}" for o in (a, b, c)))
check('D3 FINITE DIAGNOSTIC (ordering trend) at beta = 4 the pair correlation length grows faster than L: xi/L rises by >= 0.02 from L = 4 to 6',
      c['xiL'][0] - a['xiL'][0] >= 0.02, f"xi/L {a['xiL'][0]:.3f}({a['xiL'][1]:.3f}) -> {c['xiL'][0]:.3f}({c['xiL'][1]:.3f})")
check('D4 FINITE DIAGNOSTIC (g/t = 4 drop) at L = 4, beta = 8 a free band t = 0.25 cuts pair(r_max) by more than 1.5x',
      m(d, 'PR')[0] < m(b, 'PR')[0] / 1.5, f"pair(rmax) t = 0: {m(b, 'PR')[0]:.4f}, t = 0.25: {m(d, 'PR')[0]:.4f}")

print('== E. variational ladder at g -> infinity (energy per filtered term)')
def cubes(L):
    S = list(itertools.product(range(L), repeat=3)); ix = {s: i for i, s in enumerate(S)}; Cm = np.zeros((len(S),) * 2)
    for y, s in enumerate(S):
        for cc in itertools.product((0, 1), repeat=3): Cm[ix[tuple((a_ + b_) % L for a_, b_ in zip(s, cc))], y] += 1
    return Cm / sqrt(8)
Cm = cubes(4); best = 0
for U0 in [np.eye(64)] + [np.linalg.qr(rng.normal(size=(64, 64)))[0] for _ in range(3)]:
    U = U0
    for _ in range(250): W_, _s, Vt = np.linalg.svd(Cm @ ((U.T @ Cm) ** 3).T); U = W_ @ Vt
    best = max(best, np.sum((U.T @ Cm) ** 4, 0).mean())
Kd = np.diag(Cm.T @ Cm); Eq = m(b, 'E')
check('E1 THEOREM + DIAGNOSTIC best translation-breaking mode-product state (quartimax) > uniform pair state, -2 (K_xx/2)^2 = -1/2 '
      'exactly > live QMC thermal energy at L = 4, beta = 8 (an upper bound on the ground energy): products are not competitive',
      -best > -0.5 and np.allclose(Kd, 1) and Eq[0] + 3 * Eq[1] < -0.5, f"product {-best:.3f}; pair state -0.500; QMC {Eq[0]:.3f}({Eq[1]:.3f})")

print('== F. recorded production values (prod.py, 3.6e3-9e3 sweeps; recorded, not recomputed; no PASS depends on them)')
for line in ('xi/L t=0 beta=4: L=4 0.387(4), L=6 0.436(10), L=8 0.521(14); beta=8: 0.417(7), 0.509(9), 0.658(21)',
             'pair(rmax) t=0 beta=8: L=4 0.060(2), L=6 0.049(2), L=8 0.048(3); E/term L=4 beta=16 -0.6209(22)',
             'g/t=4 beta=8: xi/L L=4 0.451(6) -> L=6 0.299(14); pair(rmax) 0.0275(10) -> 0.0078(22)'):
    print('   recorded production value (not recomputed): ' + line)
print('supplied: toy content (4 modes, SU(4)-singlet quartic, not Spin(10)), real NN free band, sizes, betas, seeds, atom units g = 1')
print('cited: composite-band-3d A1/A3/B1/C5, smg-qmc A1')
print(f'elapsed {time.time() - T00:.1f} s')
print(f'TOTAL: PASS={NP[0]} FAIL={NP[1]}')
