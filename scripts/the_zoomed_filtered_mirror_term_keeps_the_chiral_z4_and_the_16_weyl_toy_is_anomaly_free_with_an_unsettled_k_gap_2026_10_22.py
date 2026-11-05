AUDIT_INPUT_PATHS = ('docs/THE_ZOOMED_FILTERED_MIRROR_TERM_KEEPS_THE_CHIRAL_Z4_AND_THE_16_WEYL_TOY_IS_ANOMALY_FREE_WITH_AN_UNSETTLED_K_GAP_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""AX-7 chirality test with 16 Weyl at K: two tastes per flavour of a K/R Weyl band, taste-mixing cube-filtered SU(4) quartic
on the mirror (SU(4) is a MODEL, not a rule), light paired at R only; plus the CL-1 tick checks (Z4 inside U(1)_eps, zoomed filter,
corner pairing). Seeded, self-contained (numpy/scipy). Production numbers are recorded data; no PASS depends on them."""
AUDIT_TIMEOUT_SEC = 120
import os, sys, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'
import itertools, numpy as np
SX = np.array([[0, 1], [1, 0]], complex); SY = np.array([[0, -1j], [1j, 0]]); SZ = np.array([[1, 0], [0, -1]], complex); SIG = np.array([SX, SY, SZ])
def dvec(p, r=1.0):
    p = np.asarray(p, float); k = np.stack([p[..., 0] - p[..., 1], p[..., 1] - p[..., 2], p[..., 2]], -1); s = np.sin(k); c = np.cos(k)
    return np.stack([s[..., 0], s[..., 1], s[..., 2] + r * (2 - c[..., 0] - c[..., 1])], -1)
J4 = np.kron(np.array([[0., -1], [1, 0]]), np.eye(2))           # complex structure on alpha = p*2 + s
J8 = np.kron(np.eye(2), J4)                                      # diagonal in taste
def rows8():
    R = np.zeros((8, 8))
    for al in range(4):
        p, s = divmod(al, 2); sal = p * 2 + (1 - s)
        R[2 * al, al] = R[2 * al, 4 + sal] = 1 / np.sqrt(2)
        R[2 * al + 1, al] = 1 / np.sqrt(2); R[2 * al + 1, 4 + sal] = -1 / np.sqrt(2)
    return R
def hk_real(ks, t, r=1.0):
    """realified 4x4 per k for complex h(k) = t d(k).sigma: [[A, -B], [B, A]], A = (h(k) + conj h(-k))/2, B = (h(k) - conj h(-k))/(2i)"""
    h = t * np.einsum('ki,iab->kab', dvec(ks, r), SIG); hm = t * np.einsum('ki,iab->kab', dvec(-ks, r), SIG).conj()
    A = (h + hm) / 2; B = (h - hm) / 2j
    return np.block([[A, -B], [B, A]])
def Hk_full(ks, t, w, r=1.0):
    """16x16 per k: (layer m/l) x taste x alpha; mirror -h, light +h, pairing w f_R."""
    h4 = hk_real(ks, t, r); fR = np.prod(np.sin(ks / 2) ** 2, -1); n = len(ks); I2 = np.eye(2)
    H = np.zeros((n, 16, 16), complex)
    H[:, :8, :8] = -np.einsum('ab,kcd->kacbd', I2, h4).reshape(n, 8, 8)
    H[:, 8:, 8:] = np.einsum('ab,kcd->kacbd', I2, h4).reshape(n, 8, 8)
    H[:, :8, 8:] = H[:, 8:, :8] = w * fR[:, None, None] * np.eye(8)
    return H
class Lat:
    def __init__(s, L, t, w, beta, h=0.01, r=1.0):
        s.L, s.beta, s.t, s.w = L, beta, t, w; S = np.array(list(itertools.product(range(L), repeat=3))); N = len(S); s.S, s.N = S, N
        idx = {tuple(v): i for i, v in enumerate(S)}; s.idx = idx; NR = 8; s.NR = NR
        ks = 2 * np.pi * S / L; s.ks = ks; Hk = Hk_full(ks, t, w, r); e, U = np.linalg.eigh(Hk); s.Hk = Hk
        R = rows8(); s.R = R
        phi = np.prod(1 + np.exp(1j * ks), 1); ff = np.abs(phi) ** 2 / 8                       # |filter|^2/8
        Mg = int(round(beta / h)); s.h = beta / Mg; dl = np.arange(Mg + 1) * s.h; dl[0] = 1e-13
        lz = np.logaddexp(0.0, -beta * e)
        s.dif = np.array([[idx[tuple((S[b] - S[a]) % L)] for b in range(N)] for a in range(N)])
        V = np.empty((Mg + 1, NR, N, NR)); s.GKK = np.empty((Mg + 1, 8, 8)); s.FK = np.empty((Mg + 1, NR, 8))
        s.GKKl = np.empty((Mg + 1, 8, 8)); s.GRR = np.empty((Mg + 1, 16, 16))
        iK = idx[(0, 0, 0)]; iR = idx[(L // 2,) * 3]
        ph = np.exp(-1j * ks @ S.T)                                                               # [k, d]
        for m in range(Mg + 1):
            W = np.exp(-dl[m] * e - lz); G = np.einsum('kan,kn,kbn->kab', U, W, U.conj())        # <m_k(tau) m_k^+>
            Gm = G[:, :8, :8]; RGR = np.einsum('ab,kbc,dc->kad', R, Gm, R) * ff[:, None, None]
            V[m] = np.einsum('kad,kx->axd', RGR, ph).real / N
            s.GKK[m] = Gm[iK].real; s.GKKl[m] = G[iK, 8:, 8:].real; s.GRR[m] = G[iR].real
            s.FK[m] = (8 / np.sqrt(8 * N)) * (R @ Gm[iK]).real
        s.imagV = 0.0
        s.V = np.ascontiguousarray(V.reshape(Mg + 1, NR, N * NR)); s.M = NR * N
        s.phiR = abs(np.prod(1 + np.exp(1j * ks[iR]))); s.e = e
        ov = np.zeros((N, N))                                                                     # cube overlap / 8 (anticommutator of filtered fields)
        D = np.array(list(itertools.product((0, 1), repeat=3)))
        for d in D:
            for d2 in D:
                dd = d2 - d; j = idx[tuple(dd % L)]; ov[0, j] += 1 / 8
        s.ovrow = ov[0]
    def S0(s, Dp, v, u):
        c, a = v // s.NR, v % s.NR; c2, b = u // s.NR, u % s.NR
        f = Dp / s.h; m = np.minimum(f.astype(int), s.V.shape[0] - 2); f = f - m; col = s.dif[c, c2] * s.NR + b
        return (1 - f) * s.V[m, a, col] + f * s.V[m + 1, a, col]
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
        D = T1 - times; sg = np.where(D > 0, 1.0, -1.0); Dp = np.where(D > 0, D, D + s.lat.beta); a = idxs % s.lat.NR
        f = Dp / s.lat.h; m = np.minimum(f.astype(int), tab.shape[0] - 2); f = f - m
        return sg[:, None] * ((1 - f)[:, None] * tab[m, a] + f[:, None] * tab[m + 1, a])
    def mode_G(s, taus, tab, G0tab):
        """K-mode propagator Tr G(K, t0+tau; K, t0)/8 over the 8 mirror K orbitals."""
        lat = s.lat; b = lat.beta; t0 = s.rng.random() * b * (1 - 1e-9); out = []
        for tau in taus:
            tt = min(max(tau, 1e-10), b - 1e-10); m = tt / lat.h; mi = min(int(m), G0tab.shape[0] - 2); f = m - mi
            G = (1 - f) * G0tab[mi] + f * G0tab[mi + 1]
            if s.n:
                t1 = (t0 + tt) % b; sg = -1.0 if t0 + tt >= b else 1.0
                Lf = s._side(t1, s.ys, s.tps, tab)                       # G0(K, t1; vertex rows ys, tps)  (uses tab symmetry, see note)
                D = s.ts - t0; sgr = np.where(D > 0, 1.0, -1.0); Dp = np.where(D > 0, D, D + b); a = s.xs % lat.NR
                fr = Dp / lat.h; mr = np.minimum(fr.astype(int), tab.shape[0] - 2); fr = fr - mr
                Rr = sgr[:, None] * ((1 - fr)[:, None] * tab[mr, a] + fr[:, None] * tab[mr + 1, a])
                G = G - sg * (Lf.T @ s.Minv @ Rr)
            out.append(np.trace(G) / 8)
        return np.array(out)
    def eq_G(s, G0eq):
        """equal-time filtered-row propagator <psi_i psi_j^+> over all vertex rows."""
        lat = s.lat; t0 = s.rng.random() * lat.beta * (1 - 1e-9); allv = np.arange(lat.M)
        if s.n == 0: return G0eq.copy()
        A = lat.g0(allv, np.full(lat.M, t0 + 1e-10), s.ys, s.tps); Bm = lat.g0(s.xs, s.ts, allv, np.full(lat.M, t0))
        return G0eq - A @ s.Minv @ Bm

RECORDED = ['beta = 4, w = t/2, g = 1; mirror K midpoint gap (jackknife), pair S_pair/N (free), xi/L, J-odd mass S/N (free); 82 s, seeds 1 (2)',
    'L = 4: g/t 2: gap 2.26(22), S_pair/N 1.98 (0.169), xi/L 0.71, S_Jodd/N 409 (532); g/t 4: gap 3.4 (unresolved, G(beta/2) 0.0006(33)), 2.02 (0.146), 0.74, 411 (532); g/t 8: 2.20(51), 1.12 (0.122), 0.54, 446 (536)',
    'L = 6 seed 1: g/t 2: 2.14(35), 1.69 (0.054), 0.89, 404 (547); g/t 4: 1.05(8), 0.46 (0.044), 0.47, 463 (538); g/t 8: 1.05(3), 0.141 (0.036), 0.24, 475 (538)',
    'L = 6 seed 2: g/t 2: 1.34(19), 1.33, 0.82, 425; g/t 4: 1.24(17), 0.90, 0.61, 445; g/t 8: 0.93(5), 0.106, 0.18, 476',
    'L = 6 runs are short (77-101 sweeps, 38-50 measurements, <2n> ~ 1850-2020); seed spread at g/t = 4 exceeds the jackknife error',
    'S_pair/N ratio L4/L6 (volume ratio 3.375): g/t 2: 1.2-1.5 (no volume suppression); g/t 4: 2.2-4.4 (undecided); g/t 8: 7.9-10.6 (falls faster than volume)',
    'exact at every g: light K gap 0; R gap = (2/beta) ln cosh(beta w/2) = 0.060, 0.016, 0.004 at g/t 2, 4, 8']

# ---------------------------------------------------------------- runner body
from scipy.linalg import null_space
T0 = time.time(); NP = [0, 0]
def rep(ok, tag, kind, text, val):
    NP[0 if ok else 1] += 1; print(f"[{'PASS' if ok else 'FAIL'}] {tag} {kind} {text} | {val}")
rng = np.random.default_rng(20261022)
print("== A. 16-Weyl toy: band, rows, symmetry search, Z16 index (exact)")
def jac(p0, h=1e-6): return np.array([(dvec(p0 + h * e) - dvec(p0 - h * e)) / (2 * h) for e in np.eye(3)]).T
gr = np.linspace(-np.pi, np.pi, 25)[:-1]; P = np.array(list(itertools.product(gr, repeat=3)))
far = np.minimum(np.linalg.norm((P + np.pi) % (2 * np.pi) - np.pi, axis=1), np.linalg.norm(P % (2 * np.pi) - np.pi, axis=1)) > 0.7
mind = np.linalg.norm(dvec(P[far]), axis=1).min(); chK, chR = np.sign(np.linalg.det(jac(np.zeros(3)))), np.sign(np.linalg.det(jac(np.pi * np.ones(3))))
L, t, w, beta = 4, 0.5, 0.25, 4.0; lat = Lat(L, t, w, beta); N = lat.N
Hk = lat.Hk; ks = lat.ks; Hm_ = Hk_full(-ks, t, w); J16 = np.kron(np.eye(2), J8)
real_ok = np.abs(Hm_ - Hk.conj()).max(); jc = np.abs(np.einsum('ab,kbc->kac', J16, Hk) - np.einsum('kab,bc->kac', Hk, J16)).max()
ea = np.abs(lat.e); iR = lat.idx[(2, 2, 2)]
rep(mind > 0.3 and chK == -chR and real_ok < 1e-12 and jc < 1e-12 and np.sum(ea < 1e-9) == 16 and np.allclose(np.sort(ea[iR]), w),
    "A1", "THEOREM", "two tastes of the realified K/R Weyl band (mirror -h, light +h, pairing w prod sin^2(k/2)): nodes only at K, R with opposite chirality; real-space real (H(-k) = H(k)*); [J, H] = 0; at L = 4 the only zeros are the 16 K modes (8 mirror + 8 light per flavour); every R mode at exactly w",
    f"off-node min|d| {mind:.2f}; chir K {chK:+.0f} R {chR:+.0f}; zeros {np.sum(ea < 1e-9)}; R levels {np.round(np.sort(ea[iR])[[0, -1]], 3)}")
Rw = rows8(); orth = np.abs(Rw @ Rw.T - np.eye(8)).max()
def rowmap(U, R):
    """for each row r_a: best |<r_b, U r_a>| over b, and the phase"""
    O = R.conj() @ U @ R.T; b = np.abs(O).argmax(0); return np.abs(O).max(0), O[b, np.arange(len(R))]
JT1 = np.kron(np.diag([1., 0]), J4) + np.kron(np.diag([0., 1]), np.eye(4))
okJ = rowmap(J8, Rw)[0].min(); brk = rowmap(JT1, Rw)[0].min()
rep(orth < 1e-12 and abs(okJ - 1) < 1e-12 and brk < 0.8 and lat.phiR < 1e-12, "A2", "THEOREM",
    "taste-mixing spin-twisted rows r_(alpha,+-) = (e_(alpha,1) +- e_(sigma alpha,2))/sqrt2 are orthonormal; the diagonal J maps rows to +-rows (H_int keeps Z4_J); J on one taste alone does not (broken); the cube filter vanishes at R and the rows sit on the mirror only, so light K and the whole R sector never enter H_int (light K gap 0, R gap w at every g)",
    f"|R R^T - 1| {orth:.0e}; J8 row-overlap min {okJ:.3f}; one-taste J min overlap {brk:.3f}; filter at R {lat.phiR:.0e}")
# symmetry search inside the commutant of the mirror band
Kr = rng.uniform(-np.pi, np.pi, (6, 3)); hm = [-np.kron(np.eye(2), hk_real(k[None], 1.0)[0]) for k in Kr]
com = null_space(np.vstack([np.kron(h, np.eye(8)) - np.kron(np.eye(8), h.T) for h in hm])); Cb = [com[:, i].reshape(8, 8) for i in range(com.shape[1])]
def vel(h=1e-5): return [(-np.kron(np.eye(2), hk_real((h * e)[None], 1.0)[0]) + np.kron(np.eye(2), hk_real((-h * e)[None], 1.0)[0])) / (2 * h) for e in np.eye(3)]
vv = vel(); Om = sum(np.linalg.det(np.eye(3)[list(p)]) * vv[p[0]] @ vv[p[1]] @ vv[p[2]] for p in itertools.permutations(range(3))) / 6
def nu_of(U):
    """Z16 index of the K mirror (4 flavours) under the Z4 generated by U (U^2 = -1): sum over charge-q eigenspaces of chirality x w(q)."""
    e, V = np.linalg.eig(U); out = 0.0
    for q, wq in ((1, 1), (3, -1)):
        Pq = V[:, np.abs(e - 1j ** q) < 1e-6]
        if Pq.shape[1] == 0: continue
        Qo, _ = np.linalg.qr(Pq); ev = np.linalg.eigvals(-1j * Qo.conj().T @ Om @ Qo); out += wq * np.sum(np.sign(ev.real)) / 2
    return 4 * out
def search(R):
    """all unitary U in the band commutant mapping every row to i^k x a row (so sum_a Q_a is invariant)."""
    found = []; A = np.array([np.concatenate([C @ R[0], C @ R[4]]) for C in Cb]).T
    for j1, j2 in itertools.product(range(8), repeat=2):
        for l1, l2 in itertools.product(range(4), repeat=2):
            bvec = np.concatenate([1j ** l1 * R[j1], 1j ** l2 * R[j2]]); x, *_ = np.linalg.lstsq(A, bvec, rcond=None)
            if np.abs(A @ x - bvec).max() > 1e-8: continue
            U = sum(xi * C for xi, C in zip(x, Cb))
            if np.abs(U.conj().T @ U - np.eye(8)).max() > 1e-8: continue
            mx, phs = rowmap(U, R)
            if mx.min() < 1 - 1e-8 or np.abs(phs ** 4 - 1).max() > 1e-8: continue
            if not any(np.abs(U - F).max() < 1e-8 for F in found): found.append(U)
    return found
Gmix = search(Rw); Gdiag = search(np.eye(8))
z4m = [U for U in Gmix if np.abs(U @ U + np.eye(8)).max() < 1e-8]; z4d = [U for U in Gdiag if np.abs(U @ U + np.eye(8)).max() < 1e-8]
num = sorted(set(int(round(nu_of(U))) % 16 for U in z4m)); nud = sorted(set(int(round(nu_of(U))) % 16 for U in z4d))
nuJ = nu_of(J8); nuN = nu_of(1j * np.eye(8))
rep(com.shape[1] == 8 and num == [0] and 8 in nud and int(round(nuJ)) == 0 and abs(nuN) == 16, "A3", "THEOREM",
    "exhaustive search inside the band commutant (dim 8): every unitary symmetry of the taste-mixing H_int with U^2 = (-1)^F has Z16 index 0 mod 16 on the K mirror. The two J sectors are time-reversal partners (same chirality, J-charges +-1), so Z4_J is vector-like (index 0); the chiral one is Z4_N (mode number), index 16 = 0 with two tastes (8 with one: the obstruction of the one-taste toy is Z4_N, not Z4_J). With taste-diagonal rows an index-8 symmetry survives (mode phase on one taste only): the taste mixing removes it",
    f"mixing: |G| = {len(Gmix)}, {len(z4m)} Z4-type, indices mod 16 {num}; taste-diagonal rows: |G| = {len(Gdiag)}, indices {nud}; nu(Z4_J) = {nuJ:.0f}, nu(Z4_N) = {nuN:+.0f}")
Vi = 0.0
for m in (0, 37, 200):
    W = np.exp(-lat.h * m * lat.e - np.logaddexp(0.0, -beta * lat.e)); Ue = np.linalg.eigh(Hk)[1]
    G = np.einsum('kan,kn,kbn->kab', Ue, W, Ue.conj())[:, :8, :8]; ff = np.abs(np.prod(1 + np.exp(1j * ks), 1)) ** 2 / 8
    RGR = np.einsum('ab,kbc,dc->kad', Rw, G, Rw) * ff[:, None, None]; Vi = max(Vi, np.abs(np.einsum('kad,kx->axd', RGR, np.exp(-1j * ks @ lat.S.T)) / N).imag.max())
rep(Vi < 1e-12, "A4", "THEOREM", "sign: the filtered-row propagator tables are real (rows real, band real), the 4 flavours see the same real matrix M, so every CT-INT weight is g^2n det(M)^4 >= 0",
    f"max |Im| of the row tables {Vi:.0e}")
# zero-mode atom baseline: the K-projected interaction is -g (64/N) sum_rows (Q + Q^+) on the 32 K mirror modes = 4 identical 8-mode blocks
def fock(n):
    I2, Z, a = np.eye(2), np.diag([1., -1.]), np.array([[0, 1], [0, 0.]]); out = []
    for j in range(n):
        mm = np.array([[1.]])
        for k in range(n): mm = np.kron(mm, Z if k < j else (a if k == j else I2))
        out.append(mm)
    return out
cm = fock(8)                                                                            # modes (orbital o in {1,2}) x flavour f: index o*4+f
def atom_gap(Lx, bt=4.0):
    gp = 64.0 / Lx ** 3; Hs = 0
    for sg in (1, -1):
        ps = [(cm[f] + sg * cm[4 + f]) / np.sqrt(2) for f in range(4)]; Qr = ps[0] @ ps[1] @ ps[2] @ ps[3]; Hs = Hs - gp * (Qr + Qr.T)
    e, V = np.linalg.eigh(Hs); e = e - e[0]
    def Gt(tau): return np.trace(V @ np.diag(np.exp(-(bt - tau) * e)) @ V.T @ cm[0] @ V @ np.diag(np.exp(-tau * e)) @ V.T @ cm[0].T) / np.exp(-bt * e).sum()
    return -(2 / bt) * np.log(2 * Gt(bt / 2) / (Gt(1e-9) + Gt(bt - 1e-9))), e[np.abs(e) > 1e-9].min()
ag4, ae4 = atom_gap(4); ag6, ae6 = atom_gap(6)
rep(ag4 > 1.5 * ag6 and ag6 > 0, "A5", "FINITE DIAGNOSTIC (exact ED)",
    "zero-mode atom baseline: the K-projected quartic alone (strength 64 g/L^3 on the 32 K mirror modes, 4 blocks of 8, exact ED) gives a K midpoint gap that falls with L; a bulk symmetric gap must exceed this and stay L-independent",
    f"atom K midpoint gap (beta = 4): L = 4 {ag4:.3f}, L = 6 {ag6:.3f} g; atom level gaps {ae4:.3f}, {ae6:.3f} g")
print("== B. live seeded CT-INT (L = 4, g/t = 2, beta = 4, w = t/2)")
q = CTINT(lat, 1.0, 5); taus = [0.0, 1.0, 2.0, beta / 2, beta - 2.0, beta - 1.0, beta]; GK = []
while q.n < 0.15 * beta * lat.M and time.time() - T0 < 30: q.sweep()
for _ in range(5): q.sweep()
while time.time() - T0 < 52:
    q.sweep(); GK.append(q.mode_G(taus, lat.FK, lat.GKK))
drift = q.recompute(); GK = np.array(GK); Mm = lat.g0(q.xs, q.ts, q.ys, q.tps); sr = abs((GK[:, 0] + GK[:, 6]).mean() - 1)
mK = GK.mean(0); gK = -(2 / beta) * np.log(max(2 * mK[3], 1e-12) / (mK[0] + mK[6]))
rep(np.isrealobj(Mm) and drift < 1e-8 and sr < 1e-8, "B1", "THEOREM+CHECK", "engine: M real (sign-free), sum rule G_K(0+) + G_K(beta-) = 1, no inverse drift",
    f"<2n> {2 * q.n}; sum-rule err {sr:.0e}; drift {drift:.0e}; live K midpoint gap {gK:.2f} ({len(GK)} meas; atom baseline {ag4:.2f})")
print("== C. the CL-1 tick (step-pi/2 generator H' = (i/2)[R_o, R_e], 8-site cells, cell momentum K)")
Cc = [tuple(c) for c in itertools.product((0, 1), repeat=3)]; ix = {c: a for a, c in enumerate(Cc)}; I8 = np.eye(8)
EPS = np.diag([(-1.0) ** sum(c) for c in Cc])
def eta(i, c): return (-1.0) ** sum(c[:i])
def Ri_e(i):
    Mx = np.zeros((8, 8))
    for c in Cc:
        if c[i] == 0:
            d = list(c); d[i] = 1; d = tuple(d); Mx[ix[d], ix[c]] = Mx[ix[c], ix[d]] = eta(i, c)
    return Mx
def Ri_o(i, K):
    Mx = np.zeros((8, 8), complex)
    for c in Cc:
        if c[i] == 1:
            d = list(c); d[i] = 0; d = tuple(d); Mx[ix[d], ix[c]] = eta(i, c) * np.exp(1j * K[i]); Mx[ix[c], ix[d]] = eta(i, c) * np.exp(-1j * K[i])
    return Mx
RE = [Ri_e(i) for i in range(3)]; Re = sum(RE) / np.sqrt(3)
def Ro(K): return sum(Ri_o(i, K) for i in range(3)) / np.sqrt(3)
Scopy = 1j * RE[0] @ RE[1] @ RE[2] @ Re
def Hp(K): A_ = Ro(K); return 0.5j * (A_ @ Re - Re @ A_)
def Bt(K): A_ = Ro(K); return 0.5 * (A_ @ Re + Re @ A_)
GAM, RR = np.zeros(3), np.pi * np.ones(3)
# C1: the fine cube filter. In cell orbitals, a fine 2x2x2 cube holds 4 eps = +1 and 4 eps = -1 sites.
th = np.linspace(0, 2 * np.pi, 9)[:-1]; ovl = []
for o in Cc:
    sites = [tuple((np.array(o) + np.array(d))) for d in Cc]; r = np.ones(8) / np.sqrt(8); ep = np.array([(-1.0) ** sum(s) for s in sites])
    ovl.append([abs(np.sum(r * np.exp(1j * a * ep) * r)) for a in th])
ovl = np.array(ovl); kept = th[np.all(np.abs(ovl - 1) < 1e-12, 0)]
rep(np.allclose(kept, [0, np.pi]) and np.abs(ovl[:, 2]).max() < 1e-12, "C1", "THEOREM",
    "the fine cube-filtered row (every fine cube, every alignment) holds 4 sites of each sublattice sign, so e^(i theta eps) maps it to a row of the same support with relative phases e^(+-i theta): it is a row (and the quartic is invariant) only for theta = 0, pi. The fine cube filter keeps NO Z4 inside U(1)_eps (only fermion parity); at theta = pi/2 the row goes to the eps-twisted row, orthogonal to it",
    f"kept theta/pi {np.round(kept / np.pi, 2)}; |<r, U_(pi/2) r>| = {np.abs(ovl[:, 2]).max():.0e}")
# C2: the cell-rung filter on eps-pure mirror orbitals
Pm = (I8 - Scopy) / 2; dims = {}; U_ = {}
for e in (1, -1):
    Pe = Pm @ (I8 + e * EPS) / 2; ev, vec = np.linalg.eigh((Pe + Pe.conj().T) / 2); U_[e] = vec[:, ev > 0.5]; dims[e] = U_[e].shape[1]
comm = np.abs(EPS @ Scopy - Scopy @ EPS).max(); z0 = np.abs(Hp(GAM)).max()
Pp = (I8 + Scopy) / 2; ovK = max(np.abs(Pp @ U_[e]).max() for e in (1, -1))
ffR = abs(np.prod(1 + np.exp(1j * RR))); z4c = max(np.abs(np.diag(np.exp(1j * np.pi / 2 * np.diag(EPS))) @ U_[e] - 1j ** (1 if e > 0 else 3) * U_[e]).max() for e in (1, -1))
rep(dims == {1: 2, -1: 2} and comm < 1e-12 and z0 < 1e-12 and ovK < 1e-12 and ffR < 1e-12 and z4c < 1e-12, "C2", "THEOREM",
    "zoomed (cell-rung) filter: rows 8^-1/2 sum over the 8 cells of a cell cube of one eps-pure mirror cell orbital (s = -1, eps fixed: 2 per sign per cell). Each row is Z4_eps-covariant (phase i^eps), so a charge-4 product of such rows keeps Z4_eps (U(1)_eps -> Z4); its cell form factor prod(1 + e^(iK_j)) vanishes at R, and at K it lies in s = -1, orthogonal to the light copy (H'(K=0) = 0, s exact there)",
    f"dim(s=-1, eps=+-) {dims[1]},{dims[-1]}; [eps, s] {comm:.0e}; |P_+ rows| {ovK:.0e}; filter at R {ffR:.0e}; Z4 covariance {z4c:.0e}")
# C3: corner pairing on the tick
alR = [(Hp(RR + 1e-6 * e) - Hp(RR - 1e-6 * e)) / 2e-6 for e in np.eye(3)]
nsR = null_space(np.vstack([np.kron(EPS, I8) - np.kron(I8, EPS.T)] + [np.kron(x, I8) + np.kron(I8, x.T) for x in alR]))
cand = []
for j in range(nsR.shape[1]):
    X = nsR[:, j].reshape(8, 8); cand += [X + X.conj().T, 1j * (X - X.conj().T)]
cand = [X / np.sqrt(np.trace(X @ X).real / 8) for X in cand if np.abs(X).max() > 1e-8]
grid = [np.array(k) for k in itertools.product(np.linspace(-np.pi, np.pi, 13)[:-1], repeat=3)]
def near(K, P0): return np.linalg.norm((K - P0 + np.pi) % (2 * np.pi) - np.pi) < 0.3
wc = 0.3; best = None
for Y in cand[:4]:
    def Hc(K): F = (I8 - Bt(K)) / 2; return Hp(K) + wc * (F @ Y + Y @ F) / 2
    gR = np.min(np.abs(np.linalg.eigvalsh(Hc(RR)))); zK = np.sum(np.abs(np.linalg.eigvalsh(Hc(GAM))) < 1e-12)
    mo = min(np.min(np.abs(np.linalg.eigvalsh(Hc(K)))) for K in grid if not near(K, GAM)); ep_ = max(np.abs(EPS @ Hc(K) - Hc(K) @ EPS).max() for K in Kr)
    lm = np.abs(Pp @ Y @ Pp).max() + np.abs(Pm @ Y @ Pm).max()
    if best is None or mo > best[2]: best = (gR, zK, mo, ep_, lm)
gR, zK, mo, ep_, lm = best
rep(gR > 0.1 * wc and zK == 8 and mo > 0.01 and ep_ < 1e-12 and lm < 1e-12, "C3", "THEOREM (free band)",
    "corner pairing on the tick: w (1 - B)/2 Y (symmetrised; B = (R_oR_e + R_eR_o)/2, Y cell-local, eps-even, light-mirror, a mass at R) keeps eps exactly, leaves the 8 K zero modes untouched (form factor 0 at K) and gaps R with no new zero elsewhere",
    f"w = {wc}: R gap {gR:.3f}; K zeros {zK}; min |E| off K (12^3 grid) {mo:.3f}; [eps, H] {ep_:.0e}; light-light/mirror-mirror part {lm:.0e}")
chi = {}
alK = [(Hp(GAM + 1e-6 * e) - Hp(GAM - 1e-6 * e)) / 2e-6 for e in np.eye(3)]
gK5 = sum(np.linalg.det(np.eye(3)[list(p)]) * alK[p[0]] @ alK[p[1]] @ alK[p[2]] for p in itertools.permutations(range(3))) / 6
for e in (1, -1):
    Qo = U_[e]; ev = np.linalg.eigvals(-1j * Qo.conj().T @ gK5 @ Qo); chi[e] = np.sum(np.sign(ev.real)) / 2
nu_m = chi[1] * 1 + chi[-1] * (-1)
rep(abs(abs(nu_m) - 2) < 1e-9, "C4", "THEOREM", "Z16 count on the tick: per mode member the K mirror is one Weyl per eps sector, both of one Z4_eps charge, index 2 per member; the K mirror can gap symmetrically under this term only if the member count n has 2n = 0 mod 16, i.e. n = 0 mod 8 (16 passes, 15 fails)",
    f"chirality (s = -1) eps+ {chi[1]:+.0f}, eps- {chi[-1]:+.0f}; index per member {nu_m:+.0f}")
print("== D. recorded production values (prod3.py, 82 s segments, seeded; recorded, not recomputed; no PASS depends on them)")
for s_ in RECORDED: print("  recorded:", s_)
print("supplied: SU(4) model (not a rule), K/R Weyl band, taste-mixing rows, w = t/2, sizes, betas, seeds; cited: momentum-selective-mirror, light-partner-gap, block-quartic-smg")
print(f"elapsed {time.time() - T0:.1f} s"); print(f"TOTAL: PASS={NP[0]} FAIL={NP[1]}")
