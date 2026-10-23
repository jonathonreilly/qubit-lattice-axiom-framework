#!/usr/bin/env python3
"""Random connectivity (R-b) and an independent tick count (R-a) for the count-geometry rule.
(supplied model; finite diagnostic; no physical identification)

 A  exact: Voronoi closure and the exact isotropy of the affine cone tensor on ANY point set;
    exact k = 0 zero mode of the Voronoi Wilson-Dirac hop; linearised vacuum Ricci of the
    two-count static metric N = 1 - U, Omega = 1 + gamma U forces gamma = 1; a skip-tick chain
    carries delay and deflection proportional to (1 + gamma).
 B  finite: cut bonds per Euclidean area on periodic Poisson-Delaunay and jittered-lattice graphs;
    spectra of two-level and four-level hops on Poisson-Voronoi graphs (cone or not); slab
    entropy per cut bond of the Wilson-Dirac sea for (100), (110), (111) cuts over seeds, against
    the same hop on Z^3; a/l_P and the fluctuation scale against the orbit-anisotropy estimate.
"""
from __future__ import annotations
AUDIT_INPUT_PATHS = ('docs/RANDOM_CONNECTIVITY_MAKES_COUNT_AREA_ISOTROPIC_BUT_A_ONE_QUBIT_HOP_LOSES_ITS_CONE_AND_A_FREE_TICK_COUNT_CARRIES_LIGHT_BENDING_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')

AUDIT_TIMEOUT_SEC = 120
import os, signal, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'
os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('aggregate cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np
import sympy as sp
from scipy.spatial import Voronoi, Delaunay
from scipy.linalg import eigh, eigvalsh
from scipy.integrate import trapezoid
import scipy.sparse as sps
from scipy.sparse.linalg import eigsh

T0 = time.monotonic(); PASS = FAIL = 0
SEED = 20261022


def check(name, ok, detail=''):
    global PASS, FAIL
    if ok: PASS += 1
    else: FAIL += 1
    print(('PASS ' if ok else 'FAIL ') + name + (': ' + detail if detail else ''))


def pad(P, L, margin):
    N = len(P); X = [P]; I = [np.arange(N)]; S = [np.zeros((N, 3), int)]
    for a in (-1, 0, 1):
        for b in (-1, 0, 1):
            for c in (-1, 0, 1):
                if a == b == c == 0: continue
                s = np.array([a, b, c]); Q = P + s * L
                m = np.all((Q > -margin) & (Q < L + margin), axis=1)
                X.append(Q[m]); I.append(np.nonzero(m)[0]); S.append(np.tile(s, (m.sum(), 1)))
    return np.vstack(X), np.concatenate(I), np.vstack(S)


def voronoi_graph(P, L):
    """periodic Voronoi graph: edges (i,j), image shift s (neighbour at r_j + s L), face areas."""
    N = len(P); X, I, S = pad(P, L, 3.0); vor = Voronoi(X); out = {}
    for (p, q), rv in zip(vor.ridge_points, vor.ridge_vertices):
        if (p >= N and q >= N) or -1 in rv: continue
        i, j, s = I[p], I[q], S[q] - S[p]
        if i == j: continue
        if i > j: i, j, s = j, i, -s
        key = (i, j, tuple(s))
        if key in out: continue
        V = vor.vertices[rv]; n = X[q] - X[p]; n = n / np.linalg.norm(n); c = V.mean(0)
        u = V[0] - c; u -= n * (u @ n); u /= np.linalg.norm(u); v = np.cross(n, u)
        V = V[np.argsort(np.arctan2((V - c) @ v, (V - c) @ u))]
        out[key] = 0.5 * np.linalg.norm(np.cross(V - c, np.roll(V, -1, 0) - c), axis=1).sum()
    E = np.array([k[:2] for k in out]); Sh = np.array([k[2] for k in out]); A = np.array(list(out.values()))
    d = P[E[:, 1]] + Sh * L - P[E[:, 0]]
    return E, Sh, d, A / np.linalg.norm(d, axis=1) / 2          # Voronoi weight w = A/(2|d|)


def delaunay_edges(P, L):
    N = len(P); X, I, S = pad(P, L, 2.0); T = Delaunay(X).simplices
    e = np.vstack([T[:, [a, b]] for a in range(4) for b in range(a + 1, 4)]); e = e[(e[:, 0] < N) | (e[:, 1] < N)]
    i, j, s = I[e[:, 0]], I[e[:, 1]], S[e[:, 1]] - S[e[:, 0]]
    sw = i > j; i, j = np.where(sw, j, i), np.where(sw, i, j); s = np.where(sw[:, None], -s, s)
    k = np.unique(np.column_stack([i, j, s]), axis=0); return k[:, :2], k[:, 2:]


def canon(vs):
    vs = sorted(vs); s0 = np.array(vs[0][1:]); return tuple((v[0], *(np.array(v[1:]) - s0)) for v in vs)


def delaunay_complex(P, L):
    """periodic Delaunay simplicial complex; coboundaries d0 (V->E), d1 (E->F), d2 (F->T) with unit weights."""
    N = len(P); X, I, S = pad(P, L, 2.0); T = Delaunay(X).simplices; T = T[(T < N).any(1)]
    simp = [{} for _ in range(4)]
    for t in T: simp[3].setdefault(canon([(I[v], *S[v]) for v in t]), len(simp[3]))
    for k in (3, 2, 1):
        for key in list(simp[k]):
            for i in range(k + 1): simp[k - 1].setdefault(canon([key[j] for j in range(k + 1) if j != i]), len(simp[k - 1]))
    ds = []
    for k in (1, 2, 3):
        R, C, V = [], [], []
        for key, ix in simp[k].items():
            for i in range(k + 1):
                R.append(ix); C.append(simp[k - 1][canon([key[j] for j in range(k + 1) if j != i])]); V.append((-1) ** i)
        ds.append(sps.csr_matrix((V, (R, C)), shape=(len(simp[k]), len(simp[k - 1]))))
    return [len(x) for x in simp], ds


def cubic(Lc):
    g = np.arange(Lc); P = np.array(np.meshgrid(g, g, g, indexing='ij')).reshape(3, -1).T.astype(float)
    idx = lambda p: (p[:, 0] % Lc) * Lc * Lc + (p[:, 1] % Lc) * Lc + (p[:, 2] % Lc)
    E, Sh = [], []
    for a in range(3):
        q = P.astype(int) + np.eye(3, dtype=int)[a]; E.append(np.stack([np.arange(len(P)), idx(q)], 1)); Sh.append(q // Lc)
    E = np.vstack(E); Sh = np.vstack(Sh); d = P[E[:, 1]] + Sh * Lc - P[E[:, 0]]
    return P, E, Sh, d, np.full(len(E), 0.5)


MS = [np.array([1, 0, 0]), np.array([1, 1, 0]), np.array([1, 1, 1])]


def cut(P, E, Sh, L, m):
    u = P @ m; fs = np.floor(2 * u / L); fj = np.floor(2 * ((P[E[:, 1]] + Sh * L) @ m) / L)
    return np.nonzero(fs % 2 == 0)[0], np.abs(fs[E[:, 0]] - fj).sum(), 2 * np.linalg.norm(m) * L * L


SIG = np.array([[[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]], complex)
s0 = np.eye(2); sx = np.array([[0., 1], [1, 0]]); sz = np.array([[1., 0], [0, -1]]); sj = np.array([[0., -1], [1, 0]])
AL = [np.kron(sz, s0), np.kron(sx, s0), -np.kron(sj, sj)]       # real symmetric Dirac alphas
BM = np.kron(sj, sx)                                              # beta = i BM


def twist(Sh): return np.prod(np.where(Sh != 0, -1.0, 1.0), axis=1)  # antiperiodic torus


def weyl2(n, E, Sh, d, w, generic=None):
    """two-level hop: frame hop i w sigma.d, or a generic random 2x2 hop (no direction data)."""
    H = np.zeros((2 * n, 2 * n), complex); tw = twist(Sh)
    for k, (i, j) in enumerate(E):
        T = (1j * w[k] * np.einsum('a,aij->ij', d[k], SIG) if generic is None else generic[k]) * tw[k]
        H[2*i:2*i+2, 2*j:2*j+2] += T; H[2*j:2*j+2, 2*i:2*i+2] += T.conj().T
    return H


def wilsonA(n, E, Sh, d, w, r=1.0):
    """Wilson-Dirac hop i w alpha.d - r w beta (+ onsite r w beta) written as H = i A, A real antisym."""
    A = np.zeros((4 * n, 4 * n)); tw = twist(Sh)
    for k, (i, j) in enumerate(E):
        T = (w[k] * (d[k, 0] * AL[0] + d[k, 1] * AL[1] + d[k, 2] * AL[2]) - r * w[k] * BM) * tw[k]
        A[4*i:4*i+4, 4*j:4*j+4] += T; A[4*j:4*j+4, 4*i:4*i+4] -= T.T
        A[4*i:4*i+4, 4*i:4*i+4] += r * w[k] * BM; A[4*j:4*j+4, 4*j:4*j+4] += r * w[k] * BM
    return A


def wilson_sparse(n, E, Sh, d, w, r=1.0):
    """same hop as wilsonA, sparse complex Hermitian H = i A."""
    tw = twist(Sh); R, C, V = [], [], []
    def put(i, j, B):
        ii, jj = np.meshgrid(np.arange(4), np.arange(4), indexing='ij'); R.append((4 * i + ii).ravel()); C.append((4 * j + jj).ravel()); V.append(B.ravel())
    for k, (i, j) in enumerate(E):
        T = (w[k] * (d[k, 0] * AL[0] + d[k, 1] * AL[1] + d[k, 2] * AL[2]) - r * w[k] * BM) * tw[k]
        put(i, j, T); put(j, i, -T.T); put(i, i, r * w[k] * BM); put(j, j, r * w[k] * BM)
    A = sps.csc_matrix((np.concatenate(V), (np.concatenate(R), np.concatenate(C))), shape=(4 * n, 4 * n))
    return 1j * A


def hb(x):
    x = np.clip(x, 1e-15, 1 - 1e-15); return float(-(x * np.log(x) + (1 - x) * np.log(1 - x)).sum())


def slab_entropies(A, P, E, Sh, L):
    """complex-fermion half-filled sea of H = iA: Gamma = A |A|^-1, S = sum h((1+nu)/2) over Gamma_A^T Gamma_A."""
    e2, U = eigh(A.T @ A, overwrite_a=True, driver='evr'); W = A @ U; W /= np.sqrt(e2)   # Gamma = W U^T
    res = []
    for m in MS:
        s, nb, ae = cut(P, E, Sh, L, m); rows = (4 * s[:, None] + np.arange(4)).ravel()
        GA = W[rows] @ U[rows].T; nu = np.sqrt(np.clip(eigvalsh(GA.T @ GA), 0, 1))
        S = hb((1 + nu) / 2); res.append((S / nb, S / ae, nb / ae))
    return np.array(res), float(np.sqrt(e2.min()))


def poisson(N, sd):
    L = N ** (1 / 3); return np.random.default_rng([SEED, sd]).random((N, 3)) * L, L


# heavy dense step first (keeps the allocator high-water mark low); printed under B5
Pc, Ec, Sc, dc, wc = cubic(7); Zc, _ = slab_entropies(wilsonA(343, Ec, Sc, dc, wc), Pc, Ec, Sc, 7)
Zline = ('   Z^3 7^3 Wilson-Dirac: per bond ' + ', '.join('%.4f' % v for v in Zc[:, 0]) + ' | per area ' + ', '.join('%.4f' % v for v in Zc[:, 1]))
RS = []
for sd in range(6):
    Pp, Lp = poisson(343, 40 + sd); Ee, Ss, dd, ww = voronoi_graph(Pp, Lp)
    A = wilsonA(343, Ee, Ss, dd, ww); r, g1 = slab_entropies(A, Pp, Ee, Ss, Lp); del A; RS.append(r)

# ---------------------------------------------------------------- A exact
print('A. exact')
P, L = poisson(343, 0); E, Sh, d, w = voronoi_graph(P, L)
b = np.zeros((len(P), 3)); np.add.at(b, E[:, 0], w[:, None] * d); np.add.at(b, E[:, 1], -w[:, None] * d)
Mt = np.einsum('k,ka,kb->ab', w, d, d) / (L ** 3 / 2)
check('A1 Voronoi closure sum_j w_ij d_ij = 0 and affine cone tensor sum w d d^T = (V/2) 1 on a Poisson set',
      np.abs(b).max() < 1e-10 and np.abs(Mt - np.eye(3)).max() < 1e-10,
      'N = 343, deg %.2f; max closure %.1e; max |T - 1| %.1e (exact per realisation: divergence theorem on each cell)'
      % (2 * len(E) / len(P), np.abs(b).max(), np.abs(Mt - np.eye(3)).max()))
Ap = wilson_sparse(len(P), E, np.zeros_like(Sh), d, w); res = max(np.abs(Ap @ np.tile(np.eye(4)[c], len(P))).max() for c in range(4))
check('A2 Wilson-Dirac hop annihilates every constant spinor on a periodic Voronoi graph (massless k = 0, untuned)',
      res < 1e-10, 'max |H u_const| = %.1e over the 4 constant spinors' % res); del Ap

t, x, y, z, M, g = sp.symbols('t x y z M gamma', real=True); X4 = [t, x, y, z]
U = M / sp.sqrt(x**2 + y**2 + z**2); et = sp.diag(-1, 1, 1, 1); h = sp.diag(2 * U, *(3 * [2 * g * U])); hu = et * h
tr = sum(et[a, a] * h[a, a] for a in range(4))
Ric = lambda a, c: sp.simplify((sum(sp.diff(hu[e, c], X4[e], X4[a]) + sp.diff(hu[e, a], X4[e], X4[c])
                               - et[e, e] * sp.diff(h[a, c], X4[e], X4[e]) for e in range(4)) - sp.diff(tr, X4[a], X4[c])) / 2)
R00, Rxx, Rxy = Ric(0, 0), Ric(1, 1), Ric(1, 2)
check('A3 two counts (lapse N = 1 - U from skipped ticks, Omega = 1 + gamma U from site density): vacuum R_ab = 0 iff gamma = 1',
      R00 == 0 and sp.simplify(Rxy.subs(g, 1)) == 0 and sp.simplify(Rxx.subs(g, 1)) == 0 and sp.simplify(Rxy.subs(g, -1)) != 0,
      'R_00 = %s; R_xy = %s' % (R00, sp.factor(Rxy)))


def chain_delay(bimp, gam, Mm, Xh, a):
    """signal hops one site per TAKEN tick; sites at coordinate spacing a/Omega; site ticks at fraction N (accumulator)."""
    xs = [-Xh]; pos = -Xh
    while pos < Xh:
        Um = Mm / np.hypot(pos, bimp); pos += a / (1 + gam * Um); xs.append(pos)
    xs = np.array(xs); Nl = 1 - Mm / np.hypot(xs, bimp); ticks = 0; acc = 0.0
    for Ni in Nl[:-1]:
        while True:
            ticks += 1; acc += Ni
            if acc >= 1: acc -= 1; break
    return ticks - (xs[-1] - xs[0]) / a          # extra global ticks over the flat count of the same length


Mm, b0, Xh, a = 0.05, 1.0, 40.0, 0.002


def exact_delay(bimp, gam):
    xx = np.linspace(-Xh, Xh, 400001); Ux = Mm / np.hypot(xx, bimp)
    return trapezoid((1 + gam * Ux) / (1 - Ux) - 1, xx) / a


D = {(gm, bb): chain_delay(bb, gm, Mm, Xh, a) for gm in (1.0, -1.0) for bb in (b0, 2 * b0)}
ex = {bb: exact_delay(bb, 1.0) for bb in (b0, 2 * b0)}
dd1 = D[(1.0, b0)] - D[(1.0, 2 * b0)]; dde = ex[b0] - ex[2 * b0]
ok = abs(D[(1.0, b0)] / ex[b0] - 1) < 0.01 and abs(dd1 / dde - 1) < 0.03 and max(abs(D[(-1.0, b0)]), abs(D[(-1.0, 2 * b0)])) <= 2
check('A4 skip-tick chain (sites at spacing a/Omega, each ticking a fraction N): delay and its impact-parameter slope '
      '(deflection) carry (1 + gamma); tied tick N = Omega (gamma = -1) carries none',
      ok, 'M/b = 0.05: gamma=1 delay %.1f vs exact %.1f ticks (first order 2(1+gamma)M asinh(X/b)/a = %.1f); '
      'b -> 2b change %.1f vs %.1f; gamma=-1 delays %.0f, %.0f ticks'
      % (D[(1.0, b0)], ex[b0], 4 * Mm * np.arcsinh(Xh / b0) / a, dd1, dde, D[(-1.0, b0)], D[(-1.0, 2 * b0)]))

# ---------------------------------------------------------------- B finite
print('B. finite diagnostics (seeded Poisson point sets, density 1, antiperiodic tori)')


def counts(P, E, Sh, L): return np.array([cut(P, E, Sh, L, m)[1] / cut(P, E, Sh, L, m)[2] for m in MS])


cs = {}
for N in (500, 2000):
    R = []
    for sd in range(6):
        Pp, Lp = poisson(N, 10 + sd); Ee, Ss = delaunay_edges(Pp, Lp); R.append(counts(Pp, Ee, Ss, Lp))
    cs[N] = np.array(R)
r8 = cs[2000]; sem = r8.std(0, ddof=1) / np.sqrt(6); dev = np.abs(r8.mean(0) - r8.mean()) / sem
nc8 = r8.mean() * 2 * 2000 ** (2 / 3)
check('B1 Poisson-Delaunay: cut bonds per Euclidean area isotropic within seed error, against |n|_1 = 1, 1.414, 1.732 on Z^3',
      dev.max() < 3, 'N=500: %s; N=2000: %s (+- %s); max |dev|/sem %.1f; per-cut relative scatter %.3f at %d bonds (x sqrt = %.2f)'
      % (np.round(cs[500].mean(0), 3), np.round(r8.mean(0), 3), np.round(sem, 3), dev.max(),
         r8.std(0, ddof=1).mean() / r8.mean(), nc8, r8.std(0, ddof=1).mean() / r8.mean() * np.sqrt(nc8)))
Lc = 10; gq = np.arange(Lc); P0 = np.array(np.meshgrid(gq, gq, gq, indexing='ij')).reshape(3, -1).T + 0.5; jr = []
for sgm in (0.05, 0.3, 0.5):
    R = []
    for sd in range(3):
        Pj = (P0 + np.random.default_rng([SEED, 50 + sd]).normal(0, sgm, P0.shape)) % Lc
        Ee, Ss = delaunay_edges(Pj, Lc); R.append(counts(Pj, Ee, Ss, Lc))
    R = np.array(R); jr.append((sgm, (R[:, 1] / R[:, 0]).mean(), (R[:, 2] / R[:, 0]).mean()))
check('B2 jittered Z^3 + Delaunay: cubic count anisotropy survives small jitter and fades by sigma ~ 0.5 spacing',
      abs(jr[0][1] - 1) > 0.05 and abs(jr[2][1] - 1) < 0.02 and abs(jr[2][2] - 1) < 0.02,
      ' '.join('sigma %.2f: 110/100 %.3f, 111/100 %.3f;' % j for j in jr))

dos = {}
for N in (216, 343):
    Pp, Lp = poisson(N, 20); Ee, Ss, dd, ww = voronoi_graph(Pp, Lp)
    gen = (np.random.default_rng([SEED, 30]).normal(size=(len(Ee), 2, 2)) + 1j * np.random.default_rng([SEED, 31]).normal(size=(len(Ee), 2, 2))) * 0.3
    for lab in ('frame', 'generic'):
        H = weyl2(N, Ee, Ss, dd, ww, None if lab == 'frame' else gen)
        ae = np.abs(eigvalsh(H, overwrite_a=True, driver='ev')); del H; dos[(lab, N)] = (ae < 0.05 * ae.max()).mean()
Pc, Ec, Sc, dc, wc = cubic(6); aec = np.abs(eigvalsh(weyl2(216, Ec, Sc, dc, wc), overwrite_a=True, driver='ev')); fz = (aec < 0.05 * aec.max()).mean()
check('B3 two-level hops on a Poisson-Voronoi graph have a finite density of states at E = 0 (no cone), frame hop or generic',
      min(dos.values()) > 0.01 and fz == 0 and abs(dos[('frame', 343)] / dos[('frame', 216)] - 1) < 0.35,
      'fraction of states with |E| < 0.05 W: frame %.3f, %.3f; generic %.3f, %.3f (N = 216, 343); Z^3 frame hop 6^3: %.3f'
      % (dos[('frame', 216)], dos[('frame', 343)], dos[('generic', 216)], dos[('generic', 343)], fz))

gaps = {}
for N in (343, 729):
    Pp, Lp = poisson(N, 21); Ee, Ss, dd, ww = voronoi_graph(Pp, Lp)
    H = wilson_sparse(N, Ee, Ss, dd, ww); H2 = (H @ H).real.tocsc(); del H          # H^2 = -A^2, real and >= 0
    e = np.sort(np.sqrt(np.abs(eigsh(H2, k=20, which='SA', tol=1e-9, return_eigenvectors=False)))); del H2
    gaps[N] = (e[0], e[0] * Lp / (np.sqrt(3) * np.pi), np.std(e[:20]) / np.mean(e[:20]))
check('B4 four-level Wilson-Dirac hop on Poisson-Voronoi graphs keeps a cone: lowest level ~ v sqrt3 pi/L, scaling as 1/L',
      abs(gaps[729][1] / gaps[343][1] - 1) < 0.1 and min(gaps[343][1], gaps[729][1]) > 0.5,
      'E_1 = %.3f, %.3f -> v = E_1 L/(sqrt3 pi) = %.3f, %.3f (N = 343, 729; affine v = 1; a finite DOS would give E_1 ~ 1/N); '
      'lowest-20 spread %.3f, %.3f (Z^3: 0)' % (gaps[343][0], gaps[729][0], gaps[343][1], gaps[729][1], gaps[343][2], gaps[729][2]))
kd = {}
for N in (343, 729):
    Pp, Lp = poisson(N, 60); nk, (d0, d1, d2) = delaunay_complex(Pp, Lp); sq = abs(d1 @ d0).max() + abs(d2 @ d1).max()
    Lap = [(d0.T @ d0), (d0 @ d0.T + d1.T @ d1), (d1 @ d1.T + d2.T @ d2), (d2 @ d2.T)]
    ev = [np.sort(eigsh(Lk.tocsc(), k=16, which='SA', tol=1e-10, return_eigenvectors=False)) for Lk in Lap]
    betti = [int((e < 1e-8).sum()) for e in ev]
    spd = [np.sqrt(ev[0][ev[0] > 1e-8][:6]).mean() * Lp / (2 * np.pi),            # d0 branch (6-fold k = 2 pi/L shell)
           np.sqrt(ev[1][ev[1] > 1e-8][:6]).mean() * Lp / (2 * np.pi),            # lowest d1 (curl) branch
           np.sqrt(ev[3][ev[3] > 1e-8][:6]).mean() * Lp / (2 * np.pi)]            # d2 branch
    kd[N] = (nk, sq, betti, spd)
okk = all(kd[N][1] == 0 and kd[N][2] == [1, 3, 3, 1] for N in kd) and all(abs(kd[729][3][i] / kd[343][3][i] - 1) < 0.1 for i in range(3))
check('B5 metric-free Kaehler-Dirac D = d + d^T on the Delaunay complex: zero modes = Betti numbers (protected), low modes ~ 1/L (cones), '
      'but each form degree has its own speed', okk and max(kd[729][3]) / min(kd[729][3]) > 2,
      'N = 343, 729: simplices %s, %s; d^2 = 0; zero modes %s; speeds (d0, d1, d2 branches) %s, %s'
      % (kd[343][0], kd[729][0], kd[729][2], np.round(kd[343][3], 3), np.round(kd[729][3], 3)))
print(Zline)
RS = np.array(RS); mb = RS[:, :, 0].mean(0); sb = RS[:, :, 0].std(0, ddof=1) / np.sqrt(len(RS))
print('   Poisson 343, 6 seeds, per bond (100),(110),(111): ' + ', '.join('%.4f+-%.4f' % (m_, s_) for m_, s_ in zip(mb, sb))
      + ' | per area ' + ', '.join('%.4f' % v for v in RS[:, :, 1].mean(0)) + ' | bonds/area ' + ', '.join('%.3f' % v for v in RS[:, :, 2].mean(0)))
anis_r = abs(mb[2] / mb[0] - 1); err_r = np.hypot(sb[2] / mb[2], sb[0] / mb[0]); anis_z = Zc[0, 0] / Zc[2, 0] - 1
rel = RS[:, :, 0].std(ddof=1) / RS[:, :, 0].mean(); ncut = RS[:, :, 2].mean() * 2 * 343 ** (2 / 3)
check('B6 Wilson-Dirac sea: entropy per cut bond isotropic on Poisson graphs within seed error; Z^3 same hop is not',
      anis_r < 3 * err_r and anis_z > 0.2,
      '(111)/(100) - 1: Poisson %+.3f +- %.3f, Z^3 %+.3f (per bond), %+.3f (per area); per-cut scatter %.3f at %d bonds (x sqrt = %.2f)'
      % (mb[2] / mb[0] - 1, err_r, Zc[2, 0] / Zc[0, 0] - 1, Zc[2, 1] / Zc[0, 1] - 1, rel, ncut, rel * np.sqrt(ncut)))
eta = mb.mean(); kap = RS[:, :, 2].mean()
cfl = rel * np.sqrt(ncut); eps_orb = cfl * 1.6e-35 / 1.5e11   # scatter ~ c/sqrt(N_cut) for a 1 AU patch of Planck-size quanta
check('B7 estimates: count-Jacobson G = a^2/(4 eta) with a^2 the area per cut bond; orbit-scale anisotropy vs bound',
      eps_orb < 1e-10,
      'eta = %.4f per bond (Dirac = 2 Weyl; %.4f per Weyl), a/l_P = 2 sqrt(eta) = %.3f; %.3f bonds per spacing^2 -> mean spacing %.3f l_P; '
      'statistical anisotropy at 1 AU ~ %.0e vs ~1e-10 needed' % (eta, eta / 2, 2 * np.sqrt(eta), kap, 2 * np.sqrt(eta * kap), eps_orb))
print('elapsed %.1f s' % (time.monotonic() - T0))
print('TOTAL: PASS=%d FAIL=%d' % (PASS, FAIL))
