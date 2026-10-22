AUDIT_INPUT_PATHS = ('docs/THE_CUBE_FILTERED_MIRROR_TERM_IS_MOMENTUM_SELECTIVE_BUT_THE_SU4_TOY_K_MIRROR_IS_ANOMALOUS_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
"""Momentum-selective mirror: SU(4) cube-filtered quartic on the mirror of a K/R Weyl band, light paired at R only.
Self-contained (numpy/scipy). Production numbers are recorded data, printed as such; no PASS depends on them."""
AUDIT_TIMEOUT_SEC = 120
import os, sys, time, itertools
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'
import numpy as np
SX = np.array([[0, 1], [1, 0]], complex); SY = np.array([[0, -1j], [1j, 0]]); SZ = np.array([[1, 0], [0, -1]], complex); SIG = [SX, SY, SZ]
def dvec(p, r):
    """Karsten-Wilczek-type Weyl d(k) = (sin k1, sin k2, sin k3 + r(2 - cos k1 - cos k2)), nodes k = 0, (0,0,pi) only (r > 1/2),
    composed with the unimodular map k = (p1 - p2, p2 - p3, p3): nodes at p = 0 and p = R = pi(1,1,1) only."""
    p = np.asarray(p, float); k = np.stack([p[..., 0] - p[..., 1], p[..., 1] - p[..., 2], p[..., 2]], -1); s = np.sin(k); c = np.cos(k)
    return np.stack([s[..., 0], s[..., 1], s[..., 2] + r * (2 - c[..., 0] - c[..., 1])], -1)
def realify(Hc):
    A, B = Hc.real, Hc.imag; return np.block([[A, -B], [B, A]])
def build(L, t, r, w):
    S = np.array(list(itertools.product(range(L), repeat=3))); N = len(S); idx = {tuple(v): i for i, v in enumerate(S)}
    ks = 2 * np.pi * S / L; Fm = np.exp(1j * ks @ S.T) / np.sqrt(N)      # Fm[k, x]
    hk = np.einsum('ki,iab->kab', dvec(ks, r), np.array(SIG)) * t        # 2x2 per k
    fR = np.prod(np.sin(ks / 2) ** 2, 1)
    Hk = np.zeros((N, 4, 4), complex); Hk[:, :2, :2] = -hk; Hk[:, 2:, 2:] = hk   # comp (layer m=0/l=1, spin)
    Hk[:, :2, 2:] = w * fR[:, None, None] * np.eye(2); Hk[:, 2:, :2] = w * fR[:, None, None] * np.eye(2)
    Hc = np.einsum('kx,kab,ky->xayb', Fm.conj(), Hk, Fm).reshape(N * 4, N * 4)   # complex real-space, orbital x*4+(layer*2+spin)
    assert np.abs(Hc - Hc.conj().T).max() < 1e-12
    # reorder complex orbitals to (layer, x, spin) then realify: real orbital index = part*(2*N*2)+layer*N*2+x*2+spin ; regroup
    perm = np.array([x * 4 + l * 2 + s for l in range(2) for x in range(N) for s in range(2)]); Hc = Hc[np.ix_(perm, perm)]
    Hr = realify(Hc)   # index = p*(4N) + l*2N + x*2 + s
    # final order: layer, x, alpha with alpha = p*2+s (4 real orbitals per site per layer)
    order = np.array([p * 4 * N + l * 2 * N + x * 2 + s for l in range(2) for x in range(N) for p in range(2) for s in range(2)])
    H = Hr[np.ix_(order, order)]
    return S, idx, H, Hk
J4 = np.kron(np.array([[0, -1], [1, 0]]), np.eye(2))   # complex structure on alpha = p*2+s
class Lat:
    def __init__(s, L, t, r, w, beta, h=0.01):
        s.L, s.beta = L, beta; S, idx, H, Hk = build(L, t, r, w); N = len(S); s.S, s.N, s.H = S, N, H; s.NO = H.shape[0]
        e, U = np.linalg.eigh(H); lz = np.logaddexp(0.0, -beta * e); s.e, s.U, s.lz = e, U, lz
        D = np.array(list(itertools.product((0, 1), repeat=3)))
        s.dif = np.array([[idx[tuple((S[b] - S[a]) % L)] for b in range(N)] for a in range(N)])      # dif[c,c'] = index of c'-c
        s.shf = np.array([[idx[tuple((S[x] - S[c]) % L)] for x in range(N)] for c in range(N)])       # shf[c,x] = x - c
        Uf = np.array([sum(U[idx[tuple(d)] * 4 + a] for d in D) / np.sqrt(8) for a in range(4)])                # filtered rows, cube 0
        PK = np.zeros((s.NO, 4)); PR = np.zeros((s.NO, 4)); eR = (-1.0) ** S.sum(1)
        for a in range(4): PK[np.arange(N) * 4 + a, a] = 1 / np.sqrt(N); PR[np.arange(N) * 4 + a, a] = eR / np.sqrt(N)
        s.PK, s.PR = PK, PR
        Mg = int(round(beta / h)); s.h = beta / Mg; dl = np.arange(Mg + 1) * s.h; dl[0] = 1e-13
        F = np.empty((Mg + 1, 4, s.NO)); UK = PK.T @ U; UR = PR.T @ U
        s.GKK = np.empty((Mg + 1, 4, 4)); s.GRR = np.empty((Mg + 1, 4, 4)); s.GKKl = np.empty((Mg + 1, 4, 4))
        PKl = np.zeros((s.NO, 4)); PKl[N * 4 + np.arange(N) * 4 + np.arange(4)[:, None], np.arange(4)[:, None]] = 1 / np.sqrt(N); UKl = PKl.T @ U; s.PKl = PKl
        PRl = np.zeros((s.NO, 4)); PRl[N * 4 + np.arange(N) * 4 + np.arange(4)[:, None], np.arange(4)[:, None]] = eR / np.sqrt(N); UR_l = PRl.T @ U
        s.GRRl = np.empty((Mg + 1, 4, 4))
        for m in range(Mg + 1):
            W = np.exp(-dl[m] * e - lz); F[m] = (Uf * W) @ U.T
            s.GKK[m] = (UK * W) @ UK.T; s.GRR[m] = (UR * W) @ UR.T; s.GKKl[m] = (UKl * W) @ UKl.T; s.GRRl[m] = (UR_l * W) @ UR_l.T
        s.F = F                                                                                    # F[m, alpha_v, o] (cube 0)
        Fm = F[:, :, :4 * N].reshape(Mg + 1, 4, N, 4)                                              # mirror part [m, a, x, b]
        V = np.zeros((Mg + 1, 4, N, 4))
        for d in D:
            sh = np.array([idx[tuple((S[c] + d) % L)] for c in range(N)]); V += Fm[:, :, sh, :] / np.sqrt(8)   # V[m,a,c',b]
        s.V = np.ascontiguousarray(V.reshape(Mg + 1, 4, N * 4))
        s.FK = F[:, :, :4 * N].reshape(Mg + 1, 4, N, 4).sum(2) / np.sqrt(N)                         # G0(v-filter row a; K mode b)
        s.FR = np.einsum('mafb,f->mab', F[:, :, :4 * N].reshape(Mg + 1, 4, N, 4), eR) / np.sqrt(N)
        s.M = 4 * N; s.Fm = np.ascontiguousarray(Fm.transpose(0, 1, 3, 2))                         # Fm[m,a,b,x]
    def _ip(s, T, Dp, i, j):
        f = Dp / s.h; m = np.minimum(f.astype(int), T.shape[0] - 2); f = f - m
        return (1 - f) * T[m, i, j] + f * T[m + 1, i, j]
    def S0(s, Dp, v, u):
        c, a = v // 4, v % 4; c2, b = u // 4, u % 4; return s._ip(s.V, Dp, a, s.dif[c, c2] * 4 + b)
    def g0(s, xs, ts, ys, tps):
        xs = np.atleast_1d(xs); ys = np.atleast_1d(ys); ts = np.atleast_1d(ts); tps = np.atleast_1d(tps)
        D = np.subtract.outer(ts, tps); sg = np.where(D > 0, 1.0, -1.0); Dp = np.where(D > 0, D, D + s.beta)
        X, Y = np.broadcast_arrays(xs[:, None], ys[None, :]); return sg * s.S0(Dp, X, Y)
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
    def _side(s, T1, idxs, times, tab):
        """sign * tab[Dp](a_v, b) for vertex rows: returns [len(idxs), 4] for D = T1 - times (mode at T1, vertices at times)."""
        D = T1 - times; sg = np.where(D > 0, 1.0, -1.0); Dp = np.where(D > 0, D, D + s.lat.beta); a = idxs % 4
        f = Dp / s.lat.h; m = np.minimum(f.astype(int), tab.shape[0] - 2); f = f - m
        return sg[:, None] * ((1 - f)[:, None] * tab[m, a] + f[:, None] * tab[m + 1, a])
    def mode_G(s, taus, tab, G0tab):
        """per-flavour mode propagator Tr G(mode, t0+tau; mode, t0)/4 for the 4 modes defined by tab (FK or FR)."""
        lat = s.lat; b = lat.beta; t0 = s.rng.random() * b * (1 - 1e-9); out = []

        for tau in taus:
            tt = min(max(tau, 1e-10), b - 1e-10); m = tt / lat.h; mi = min(int(m), G0tab.shape[0] - 2); f = m - mi
            G = (1 - f) * G0tab[mi] + f * G0tab[mi + 1]
            if s.n:
                t1 = (t0 + tt) % b; sg = -1.0 if t0 + tt >= b else 1.0
                Lf = s._side(t1, s.ys, s.tps, tab)            # G0(mode,t1; ys,tps): D = t1 - tps
                G = G - sg * (Lf.T @ s.Minv @ Rr(s, t0, t1, tab))
            out.append(np.trace(G) / 4)
        return np.array(out)
def Rr(q, t0, t1, tab):
    # G0(xs, ts; mode, t0) with the same wrapping convention as t1 (t1 measured from t0, times in [0,beta))
    D = q.ts - t0; sg = np.where(D > 0, 1.0, -1.0); Dp = np.where(D > 0, D, D + q.lat.beta); a = q.xs % 4
    f = Dp / q.lat.h; m = np.minimum(f.astype(int), tab.shape[0] - 2); f = f - m
    return sg[:, None] * ((1 - f)[:, None] * tab[m, a] + f[:, None] * tab[m + 1, a])
RECORDED = [
 "beta = 8, L = 4 (g = 1, w = t/2): mirror K G(beta/2) and midpoint gap: g/t 0.25: 0.0134(11), 0.90(2); 2: -0.0004(7), > 1.5 (G(beta/2) consistent with 0); 4: 0.0045(23), 1.18(13); 6: 0.0044(35), 1.18(19)",
 "beta = 8, L = 4: filtered pair S_pair/N (free) and xi/L: g/t 0.25: 0.115 (0.090), 0.175; 2: 0.199 (0.089), 0.263; 4: 0.336 (0.085), 0.382; 6: 0.382 (0.078), 0.424",
 "beta = 8, L = 4: Z4_J-odd on-site mass S_B/N, 4 channels vs free: g/t 0.25: 1.57-7.27 vs 1.65-7.26; 2: 1.18,1.65,1.18,6.94 vs 1.66,1.66,1.66,7.25; 4: 1.03,1.89,1.03,6.46 vs 1.77,..,7.02; 6: 1.14,2.23,1.14,5.99 vs 2.03,..,6.60",
 "beta = 4, g/t = 2, L = 4 -> 6: mirror K gap 2.18(16) -> 1.53(5); S_pair/N 0.188 -> 0.039 (ratio 4.8, volume ratio 3.375); xi/L 0.250 -> 0.116; S_B/N channel 2: 1.73 -> 1.69 (free 1.77, 1.78)",
 "exact at every g (A3): light K gap 0; light = mirror R midpoint gap = (2/beta) ln cosh(beta w/2): 0.108, 0.030, 0.014 at g/t 2, 4, 6 (beta = 8)",
]
T0 = time.time(); NP = [0, 0]
def rep(ok, tag, kind, text, val):
    NP[0 if ok else 1] += 1; print(f"[{'PASS' if ok else 'FAIL'}] {tag} {kind} {text} | {val}")
print("== A. exact: band, decoupling, symmetry, anomaly count")
from scipy.optimize import minimize
r = 1.0; rng = np.random.default_rng(7); best = 9.0
for _ in range(120):
    res = minimize(lambda k: np.sum(dvec(k, r) ** 2), rng.uniform(-np.pi, np.pi, 3)); kk = (res.x + np.pi) % (2 * np.pi) - np.pi
    if np.linalg.norm(kk) > 0.3 and np.linalg.norm(np.abs(kk) - np.pi) > 0.3: best = min(best, np.sqrt(res.fun))
def jac(p0):
    h = 1e-6; return np.array([(dvec(p0 + h * e, r) - dvec(p0 - h * e, r)) / (2 * h) for e in np.eye(3)]).T
chK, chR = np.sign(np.linalg.det(jac(np.zeros(3)))), np.sign(np.linalg.det(jac(np.pi * np.ones(3))))
rep(best > 0.9 and chK == -chR and np.linalg.norm(dvec(np.pi * np.ones(3), r)) < 1e-12, "A1", "THEOREM",
    "the Weyl band d(p).sigma (KW form composed with the unimodular map k = (p1-p2, p2-p3, p3), r = 1) vanishes only at K = 0 and R = pi(1,1,1), with opposite chiralities; realified it is a real band with complex structure J", f"min|d| at off-node local minima {best:.3f}; chirality K {chK:+.0f}, R {chR:+.0f}")
L, t, w, beta = 4, 4.0, 2.0, 4.0     # live run: g/t = 0.25, w = t/2
lat = Lat(L, t, r, w, beta); N = lat.N; H = lat.H
JJ = np.kron(np.eye(2 * N), J4); e0 = np.sort(np.abs(np.linalg.eigvalsh(H)))
rep(np.abs(H - H.T).max() < 1e-12 and np.abs(JJ @ H - H @ JJ).max() < 1e-12 and np.sum(e0 < 1e-9) == 8 and abs(e0[8] - w) < 1e-9, "A2", "THEOREM",
    "with mirror h_m = -h, light h_l = h and light-mirror pairing w f_R(k), f_R = prod sin^2(k_i/2) (1 at R, 0 at K): H is real, commutes with J, H(k)^2 = d^2 + w^2 f_R^2; at L = 4 the only zeros are the 8 (light + mirror) K modes and the R sector sits at exactly w",
    f"zeros {np.sum(e0 < 1e-9)}; next level {e0[8]:.4f} (w = {w})")
def fgap(T): return -(2 / beta) * np.log(2 * np.trace(T[len(T) // 2]) / (np.trace(T[0]) + np.trace(T[-1])))
rep(np.abs(lat.FR).max() < 1e-12 and fgap(lat.GKKl) < 1e-9 and abs(fgap(lat.GRRl) - fgap(lat.GRR)) < 1e-12, "A3", "THEOREM",
    "exact decoupling: the cube filter (form factor 8 prod cos^2(k_i/2)) is exactly 0 on the mirror R modes and the pairing is exactly 0 at K, so the light K modes and the whole R sector never enter H_int: light gap at K = 0 and light/mirror gap at R = the free paired value at EVERY g (finite volume, all orders)",
    f"max|filter-R overlap| {np.abs(lat.FR).max():.1e}; free light-K gap {fgap(lat.GKKl):.1e}; R gap {fgap(lat.GRRl):.4f} (beta = 4 midpoint of w)")
# Z4_J and anomaly count
rowsJ = np.abs(J4) @ np.arange(4); okJ = sorted(rowsJ.astype(int).tolist()) == [0, 1, 2, 3]
J2 = np.array([[0, -1], [1, 0]]); Bs = [np.kron(np.diag([1, -1]), np.eye(2)), np.kron(np.array([[0, 1], [1, 0]]), np.eye(2))]
odd = all(np.abs(B @ J4 + J4 @ B).max() < 1e-12 for B in Bs)
# LH-Weyl Z4_J charges at K per flavour: sector J = +i carries complex h (light) / -h (mirror); J = -i the conjugate copy (chirality flipped)
nu = {}
for lay, sgn in (("light", 1), ("mirror", -1)):
    c = np.sign(np.linalg.det(sgn * jac(np.zeros(3)))); nu[lay] = 4 * (c * (+1) + (-c) * (-1))   # LH charge = chirality * J-charge
rep(okJ and odd and nu["mirror"] % 16 == 8 and (nu["light"] + nu["mirror"]) == 0, "A4", "THEOREM",
    "Z4_J (c -> J c) maps the filtered vertex rows to +-rows, so H_int keeps Z4_J x Z4_N x SU(4); every on-site Dirac mass at K (J-odd) and every pair (N-odd) is forbidden; the mirror K content is 8 Weyl of one Z4_J charge: Z16 index 8 != 0, so a symmetric TRIVIAL gap of the K mirror alone is anomaly-forbidden (light K carries the opposite 8)",
    f"Z16 index at K: mirror {nu['mirror']:+.0f}, light {nu['light']:+.0f}")
print("== B. engine checks (CT-INT of block-quartic-smg with cube-filtered vertex tables)")
q = CTINT(lat, 1.0, 11)
while q.n < 0.15 * lat.beta * lat.M and time.time() - T0 < 25: q.sweep()
for _ in range(5): q.sweep()
taus = [0.0, 1.0, 2.0, beta / 2, beta - 2.0, beta - 1.0, beta]; GK = []; SB = []; Nm = 4 * N; ox = np.arange(Nm) // 4; ob = np.arange(Nm) % 4
Um = lat.U[:Nm]; G0m = (Um / (1 + np.exp(-beta * lat.e))) @ Um.T; Bf = Bs
def sB(B, G):
    # 4 flavours x Tr[B G B (1 - G)] / N with B on-site (block diagonal), O(N^2)
    Gr = G.reshape(N, 4, N, 4); BGB = np.einsum('ab,xbyc,cd->xayd', B, Gr, B).reshape(4 * N, 4 * N)
    return 4 * np.sum(BGB * (np.eye(4 * N) - G).T) / N
def side(times, vs, T1, fv):
    D = (times - T1) if fv else (T1 - times); sg = np.where(D > 0, 1.0, -1.0); Dp = np.where(D > 0, D, D + beta)
    f = Dp / lat.h; m = np.minimum(f.astype(int), lat.F.shape[0] - 2); f = f - m
    a = vs % 4; c = vs // 4; col = lat.shf[c[:, None], ox[None, :]] * 4 + ob[None, :]
    return sg[:, None] * ((1 - f)[:, None] * lat.F[m[:, None], a[:, None], col] + f[:, None] * lat.F[m[:, None] + 1, a[:, None], col])
ns = 0
while time.time() - T0 < 55:
    q.sweep(); ns += 1
    if ns % 2 == 0:
        GK.append(q.mode_G(taus, lat.FK, lat.GKK)); t0 = q.rng.random() * beta * (1 - 1e-9)
        Gm = G0m - side(q.tps, q.ys, t0 + 1e-10, False).T @ q.Minv @ side(q.ts, q.xs, t0, True)
        SB.append([sB(B, Gm) for B in Bf])
drift = q.recompute(); GK = np.array(GK); SB = np.array(SB); SBf = [sB(B, G0m) for B in Bf]
w_ok = abs((GK[:, 0] + GK[:, 6]).mean() - 1) < 1e-8
M_ = q.lat.g0(q.xs, q.ts, q.ys, q.tps)
rep(w_ok and drift < 1e-8 and np.isrealobj(M_), "B1", "THEOREM+CHECK",
    "sign: every configuration weight is g^2n det(M)^4 with M real (the 4 flavours see the same real M); engine: sum rule G_K(0+) + G_K(beta-) = 1 and no inverse drift",
    f"<2n> {2 * q.n}; sum rule err {abs((GK[:, 0] + GK[:, 6]).mean() - 1):.1e}; drift {drift:.1e}")
m = GK.mean(0); gm = -(2 / beta) * np.log(max(2 * m[3], 1e-12) / (m[0] + m[6]))
print("== C. live seeded run: L = 4, g/t = 0.25 (weak), beta = 4, w = t/2", f"({ns} sweeps, {len(GK)} measurements)")
rep(gm > 0.3 and np.all(SB.mean(0) < 1.05 * np.array(SBf)), "C1", "FINITE DIAGNOSTIC",
    "finite-size caveat: already at weak coupling the L = 4 K-mirror midpoint gap is O(g) (the K zero modes form an atom on which the filtered quartic acts with strength 64 g / L^3), with no Z4_J-odd mass enhancement; so an L = 4 K gap is NOT by itself a bulk symmetric gap",
    f"mirror K gap {gm:.3f}; S_B/N {np.round(SB.mean(0), 3)} vs free {np.round(SBf, 3)}")
print("== D. recorded production values (prod.py, 82 s segments, L = 4; recorded, not recomputed; no PASS depends on them)")
for s_ in RECORDED: print("   recorded production value (not recomputed):", s_)
print("supplied: SU(4) toy, K/R Weyl band (r = 1, unimodular map), w = t/2, f_R = prod sin^2(k/2), filter 8^-1/2 cube rows, L, beta, seeds")
print("cited: light-partner-gap (requirement), block-quartic-smg (engine, light release), qmc-face-gapped, toy-qmc")
print(f"elapsed {time.time() - T0:.1f} s"); print(f"TOTAL: PASS={NP[0]} FAIL={NP[1]}")
