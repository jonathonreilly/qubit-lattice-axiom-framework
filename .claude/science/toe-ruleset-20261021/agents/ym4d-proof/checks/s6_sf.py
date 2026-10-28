#!/usr/bin/env python3
"""s6 (lane F, session 6): checks for Lemmas CD, CHEB, RINV, Proposition GF-A, Lemma KKT, Proposition GF-B (computer-assisted
certificate), Corollary CHAIN-6, Lemma FH, and the STEP-1 arithmetic. Criteria: checks/s6_criteria.md (written before this script).
Rigour conventions are those of the criteria file (exact Fractions; floats with a priori rounding bounds; mpmath >= 50 digits)."""
import itertools, math, sys, time
from fractions import Fraction
import numpy as np
import scipy.sparse as sp
from mpmath import mp, mpf, sqrt as msqrt, log as mlog, acosh as macosh, cosh as mcosh, exp as mexp

T0 = time.time()
rng = np.random.default_rng(20261028 + 6)
RES = {}
def verdict(name, ok, msg):
    RES[name] = bool(ok)
    print(f"{name}: {'PASS' if ok else 'FAIL'}  {msg}", flush=True)
U_RND = 2.0 ** -53
def gamma(n): return n * U_RND / (1 - n * U_RND)
INFL = 1 + 1e-9

# ============================================================== cell geometry (any d, L = 3)
def cell(d, L=3):
    sites = list(itertools.product(range(L), repeat=d)); idx = {s: i for i, s in enumerate(sites)}
    h = (L - 1) // 2; ic = idx[(h,) * d]; nS = len(sites)
    I0 = np.zeros((nS, nS)); hop = [np.zeros((nS, nS)) for _ in range(d)]
    for s in sites:
        for mu in range(d):
            t = list(s); t[mu] += 1; cross = False
            if t[mu] == L: t[mu] = 0; cross = True
            i, j = idx[s], idx[tuple(t)]
            I0[i, i] += 1; I0[j, j] += 1
            if cross: hop[mu][i, j] -= 1
            else: I0[i, j] -= 1; I0[j, i] -= 1
    keep = [i for i in range(nS) if i != ic]
    nl = nS - 1; m = nS
    K0 = np.zeros((m, m)); K0[:nl, :nl] = I0[np.ix_(keep, keep)]; K0[:nl, nl] = -1; K0[nl, :nl] = 1
    Kp = []
    for mu in range(d):
        A = np.zeros((m, m)); A[:nl, :nl] = hop[mu][np.ix_(keep, keep)]; Kp.append(A)
    # block-internal Kato matrix (intra-block links only), restricted to non-centre sites
    Hb = np.zeros((nS, nS), dtype=np.int64)
    for s in sites:
        for mu in range(d):
            if s[mu] < L - 1:
                t = list(s); t[mu] += 1; i, j = idx[s], idx[tuple(t)]
                Hb[i, i] += 1; Hb[j, j] += 1; Hb[i, j] -= 1; Hb[j, i] -= 1
    Hb = Hb[np.ix_(keep, keep)]
    return dict(d=d, L=L, h=h, sites=sites, idx=idx, keep=keep, nl=nl, m=m, K0=K0, Kp=Kp, Hb=Hb)

def ldl_pivots_exact(Hint, c):
    n = Hint.shape[0]
    A = [[Fraction(int(Hint[i, j])) - (c if i == j else 0) for j in range(n)] for i in range(n)]
    piv = []
    for k in range(n):
        p = A[k][k]; piv.append(p)
        if p <= 0: return piv, False
        for i in range(k + 1, n):
            if A[i][k] != 0:
                f = A[i][k] / p
                Ai, Ak = A[i], A[k]
                for j in range(k + 1, n):
                    if Ak[j] != 0: Ai[j] -= f * Ak[j]
    return piv, True

# ============================================================== A1 / A1n
print("== A. every-background tier ==", flush=True)
C4 = cell(4)
cDK = Fraction(2663, 31250)
piv, okA1 = ldl_pivots_exact(C4['Hb'], cDK)
verdict("A1", okA1 and all(p > 0 for p in piv), f"exact LDL^T of H - (2663/31250)I (80x80): min pivot {float(min(piv)):.6e}, "
        f"float lambda_min(H) = {np.linalg.eigvalsh(C4['Hb'].astype(float))[0]:.10f}")
piv_n, okn = ldl_pivots_exact(C4['Hb'], Fraction(853, 10000))
verdict("A1n", not okn, f"negative control c = 0.0853: a pivot <= 0 found at step {len(piv_n)} (value {float(piv_n[-1]):.3e})")

# ============================================================== d = 2 lattice machinery (SU(2) adjoint)
SIG = np.array([[[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]], dtype=complex)
I2 = np.eye(2, dtype=complex)
dag = lambda M: np.conj(np.swapaxes(M, -1, -2))
def su2_exp(a):
    a = np.asarray(a, float); th = np.linalg.norm(a, axis=-1)
    s = np.where(th > 1e-300, np.sin(th) / np.where(th > 0, th, 1), 1.0)
    return np.cos(th)[..., None, None] * I2 + 1j * (s[..., None, None] * np.einsum('...a,aij->...ij', a, SIG))
def haar_su2(shape):
    q = rng.normal(size=tuple(shape) + (4,)); q /= np.linalg.norm(q, axis=-1, keepdims=True)
    return q[..., 0, None, None] * I2 + 1j * np.einsum('...a,aij->...ij', q[..., 1:], SIG)
def adj(U):
    Ud = dag(U)
    return np.real(np.stack([np.stack([np.trace(SIG[a] @ U @ SIG[b] @ Ud, axis1=-2, axis2=-1) / 2 for b in range(3)], -1)
                             for a in range(3)], -2))
class Lat:
    def __init__(s, d, T, L=3):
        s.d, s.T, s.L, s.n, s.h = d, T, L, T * L, (L - 1) // 2
        s.sites = list(itertools.product(range(s.n), repeat=d)); s.sidx = {x: i for i, x in enumerate(s.sites)}
        s.blocks = list(itertools.product(range(T), repeat=d)); s.bidx = {X: i for i, X in enumerate(s.blocks)}
    def add(s, x, mu, k=1):
        y = list(x); y[mu] = (y[mu] + k) % s.n; return tuple(y)
    def blk(s, x): return tuple(c // s.L for c in x)
    def centre(s, X): return tuple(s.L * c + s.h for c in X)
    def link(s, U, x, mu, sgn): return U[x + (mu,)] if sgn > 0 else dag(U[s.add(x, mu, -1) + (mu,)])
    def axial_steps(s, c, x, order=None):
        order = range(s.d) if order is None else order
        steps = []; cur = list(c)
        for mu in order:
            while cur[mu] != x[mu]:
                sgn = 1 if x[mu] > cur[mu] else -1
                steps.append((tuple(cur), mu, sgn)); cur[mu] += sgn
        return steps
    def hol(s, U, steps):
        M = I2.copy()
        for (x, mu, sgn) in steps: M = M @ s.link(U, x, mu, sgn)
        return M
    def plaq(s, U, x, mu, nu):
        return U[x + (mu,)] @ U[s.add(x, mu) + (nu,)] @ dag(U[s.add(x, nu) + (mu,)]) @ dag(U[x + (nu,)])
def gauge_apply(lat, g, U):
    V = np.empty_like(U)
    for x in lat.sites:
        for mu in range(lat.d): V[x + (mu,)] = g[x] @ U[x + (mu,)] @ dag(g[lat.add(x, mu)])
    return V
def max_plaq(lat, U):
    m = 0.0
    for x in lat.sites:
        for mu in range(lat.d):
            for nu in range(mu + 1, lat.d): m = max(m, np.linalg.norm(I2 - lat.plaq(U, x, mu, nu), 2))
    return m
def build(lat, U, hole=(), dense_Q=True):
    """sparse D, dense GtG on Lambda (minus hole blocks), M' = L^d M on Lambda, Q per block (Lambda_res), R (RINV)."""
    d, L = lat.d, lat.L; NS = len(lat.sites); links = [(x, mu) for x in lat.sites for mu in range(d)]
    rows, cols_, vals = [], [], []
    for i, (x, mu) in enumerate(links):
        y = lat.add(x, mu); A = adj(U[x + (mu,)]); iy, ix = lat.sidx[y], lat.sidx[x]
        for a in range(3):
            for b in range(3):
                rows.append(3 * i + a); cols_.append(3 * iy + b); vals.append(A[a, b])
            rows.append(3 * i + a); cols_.append(3 * ix + a); vals.append(-1.0)
    Dm = sp.csr_matrix((vals, (rows, cols_)), shape=(3 * len(links), 3 * NS))
    cen = set(lat.centre(X) for X in lat.blocks); hole = set(hole)
    cols = [3 * lat.sidx[z] + a for z in lat.sites if z not in cen and lat.blk(z) not in hole for a in range(3)]
    cols = np.array(cols); colpos = {c: k for k, c in enumerate(cols)}
    G = Dm[:, cols]; GtG = (G.T @ G).toarray()
    blocks = [X for X in lat.blocks if X not in hole]; NB = len(blocks); bpos = {X: k for k, X in enumerate(blocks)}
    Mp = np.zeros((3 * NB, len(cols))); orders = list(itertools.permutations(range(d)))
    R = np.zeros((len(cols), 3 * NB))
    for X in blocks:
        c = lat.centre(X); bi = bpos[X]
        bsites = [z for z in lat.sites if lat.blk(z) == X]; w = 1.0 / (len(bsites) * len(orders))
        for yv in bsites:
            if yv == c: continue
            for od in orders:
                Tm = lat.hol(U, lat.axial_steps(c, yv, od))
                for a in range(3):
                    Mp[3 * bi:3 * bi + 3, colpos[3 * lat.sidx[yv] + a]] += (L ** d) * w * adj(Tm)[:, a]
            if sum(abs(yv[k] - c[k]) for k in range(d)) == 1:   # centre-adjacent: single-link transport
                Tm = lat.hol(U, lat.axial_steps(c, yv))
                A = adj(Tm).T * (L ** d) / (2 * d)
                for a in range(3): R[colpos[3 * lat.sidx[yv] + a], 3 * bi:3 * bi + 3] = A[a]
    blk_of_col = np.array([bpos[lat.blk(lat.sites[c // 3])] for c in cols])
    Qlist = []
    for X in blocks:
        bi = bpos[X]; idx = np.where(blk_of_col == bi)[0]; mm = Mp[3 * bi:3 * bi + 3][:, idx]
        _, s, vt = np.linalg.svd(mm); Qlist.append((idx, vt[3:].T))
    out = dict(GtG=GtG, Mp=Mp, R=R, Qlist=Qlist, boc=blk_of_col, blocks=blocks, NB=NB, cols=cols)
    if dense_Q:
        nq = sum(Qj.shape[1] for _, Qj in Qlist); Q = np.zeros((len(cols), nq)); Qblk = []; k = 0
        for bi, (idx, Qj) in enumerate(Qlist):
            for j in range(Qj.shape[1]):
                Q[idx, k] = Qj[:, j]; Qblk.append(bi); k += 1
        out.update(Q=Q, Qblk=np.array(Qblk))
    return out
def tdist(lat, X, Y): return max(min((a - b) % lat.T, (b - a) % lat.T) for a, b in zip(X, Y))

# ============================================================== A2/A2b/A2n/A3 (d = 2, 6x6 torus)
C2 = cell(2)
cD2 = np.linalg.eigvalsh(C2['Hb'].astype(float))[0]
a2 = cD2 * (1 - 1e-12); b2 = 8.0; sig2 = (b2 + a2) / (b2 - a2); th2 = math.acosh(sig2)
cR2 = (9 / 4) * (math.sqrt(8 * 8 + 8 * 2 * 1) + 4)
lat6 = Lat(2, 6)
def smooth_bg(lat, amp):
    a = np.zeros((lat.n,) * lat.d + (lat.d, 3))
    for x in lat.sites:
        for mu in range(lat.d):
            a[x + (mu,)] = amp * np.array([math.sin(2 * math.pi * (x[0] + 2 * x[-1]) / lat.n + k + mu) for k in range(3)])
    return gauge_apply(lat, haar_su2((lat.n,) * lat.d), su2_exp(a))
bgs = [("trivial", np.broadcast_to(I2, (18, 18, 2, 2, 2)).copy()), ("Haar1", haar_su2((18, 18, 2))), ("Haar2", haar_su2((18, 18, 2))),
       ("smooth", smooth_bg(lat6, 0.05))]
okA2 = okA2b = True; violA2n = False; okA3 = True; msgs = []; ratA3 = []
for name, U in bgs:
    o = build(lat6, U); Q, Qb, GtG = o['Q'], o['Qblk'], o['GtG']
    Gres = Q.T @ GtG @ Q; ev = np.linalg.eigvalsh(Gres); Gi = np.linalg.inv(Gres)
    okA2b &= (ev[0] >= a2) and (ev[-1] <= b2 + 1e-9)
    worst = 0.0; worstn = 0.0
    for i, X in enumerate(o['blocks']):
        for j, Y in enumerate(o['blocks']):
            nr = np.linalg.norm(Gi[np.ix_(Qb == i, Qb == j)], 2); D = tdist(lat6, X, Y)
            r = nr * a2 * (math.cosh(D * th2) if D > 0 else 1.0); worst = max(worst, r)
            rn = nr * a2 * (math.cosh(D * 10 * th2) if D > 0 else 1.0); worstn = max(worstn, rn)
    okA2 &= worst <= 1 + 1e-9; violA2n |= worstn > 1
    # A3
    Mc = o['Mp'] / 9.0; R = o['R']
    e1 = np.abs(Mc @ R - np.eye(Mc.shape[0])).max()
    nRX = max(abs(np.linalg.norm(R[np.ix_(o['boc'] == i, np.arange(3 * i, 3 * i + 3))], 2) - 9 / 2) for i in range(o['NB']))
    PDR = Q.T @ GtG @ R; rs = 0.0
    for i in range(o['NB']):
        rs = max(rs, sum(np.linalg.norm(PDR[np.ix_(Qb == i, np.arange(3 * j, 3 * j + 3))], 2) for j in range(o['NB'])))
    okA3 &= e1 <= 1e-12 and nRX <= 1e-12 and rs <= cR2 * (1 + 1e-12); ratA3.append(rs / cR2)
    msgs.append(f"{name}: spec [{ev[0]:.4f},{ev[-1]:.4f}] max CHEB ratio {worst:.3e}, 10theta ratio {worstn:.3e}; "
                f"||MR-1|| {e1:.1e}, ||R(X,X)||-4.5 {nRX:.1e}, |||PDR||| {rs:.3f}")
for s_ in msgs: print("   ", s_)
verdict("A2b", okA2b, f"spectrum of G_res within [a, 8], a = d=2 Kato gap {cD2:.6f}")
verdict("A2", okA2, f"Lemma CHEB ratio <= 1 for all pairs, all backgrounds (theta = {th2:.4f})")
verdict("A2n", violA2n, "negative control: claimed rate 10 theta is violated")
verdict("A3", okA3, f"RINV identities and |||P_res D^*D R||| <= c_R(2) = {cR2:.3f}; ratios {', '.join(f'{r:.3f}' for r in ratA3)}")

# ============================================================== A4 (mpmath)
mp.dps = 60
d4, L4 = 4, 3
aK = mpf(2663) / 31250; bK = mpf(4 * d4)
sigA = (bK + aK) / (bK - aK); thA = macosh(sigA)
S = mpf(0)
for D in range(1, 20001):
    ND = (2 * D + 1) ** d4 - (2 * D - 1) ** d4
    S += ND / mcosh(D * thA)
Dm = 20000
tail = mpf(0); q = mexp(-thA)
# N_D/T_D <= 2 (2D+1)^4 e^{-theta D}; sum_{D>Dm} <= 2 sum_{D>Dm} (2D+1)^4 q^D <= 2 (2Dm+3)^4 q^{Dm+1} / (1 - q ((2Dm+5)/(2Dm+3))^4)
tail = 2 * (2 * Dm + 3) ** 4 * q ** (Dm + 1) / (1 - q * (mpf(2 * Dm + 5) / (2 * Dm + 3)) ** 4)
Gam1 = (1 + S + tail) / aK
cR4 = mpf(L4 ** d4) / (2 * d4) * (msqrt(8 * d4 ** 3 + 8 * d4 * (d4 - 1)) + 2 * d4)
GA = mpf(L4 ** d4) / msqrt(2 * d4) + Gam1 * (1 + cR4)
GA = GA * (1 + mpf('1e-30'))
verdict("A4", tail < mpf('1e-30') * Gam1 and GA < mpf('5.8954e23'),
        f"sigma {float(sigA):.8f}, theta = m_FP^A {float(thA):.6f}/block, Gamma_1 {float(Gam1):.6e}, c_R {float(cR4):.4f}, "
        f"G^A {float(GA):.6e} (tail {float(tail):.1e}); improvement over 5.8954e23: {float(mpf('5.8954e23') / GA):.3e}")

# ============================================================== B. certificate machinery
def reps_of(d, R):
    return [z for z in itertools.product(range(R + 1), repeat=d) if all(z[i] <= z[i + 1] for i in range(d - 1))]
def orbit_size(z):
    d = len(z); cnt = math.factorial(d)
    for v in set(z): cnt //= math.factorial(z.count(v))
    return cnt * 2 ** sum(1 for v in z if v != 0)
def torus_kernel(C, n, Zlist, chunk=512):
    d, m = C['d'], C['m']; K0, Kp = C['K0'], C['Kp']
    Za = np.array(Zlist, float); acc = np.zeros((len(Zlist), m * m), complex)
    grid = 2 * np.pi * np.arange(n) / n
    ks = np.array(list(itertools.product(range(n), repeat=d)))
    for s0 in range(0, len(ks), chunk):
        kk = grid[ks[s0:s0 + chunk]]
        A = np.broadcast_to(K0.astype(complex), (len(kk), m, m)).copy()
        for mu in range(d):
            e = np.exp(1j * kk[:, mu])[:, None, None]
            A += Kp[mu][None] * e + Kp[mu].T[None] * np.conj(e)
        Ai = np.linalg.inv(A).reshape(len(kk), m * m)
        ph = np.exp(1j * (Za @ kk.T))
        acc += ph @ Ai
    return (acc.real / n ** d).reshape(len(Zlist), m, m), np.abs(acc.imag).max() / n ** d
_RL = {}
def relabel_info(C, Z):
    key = (C['d'], tuple(Z))
    if key in _RL: return _RL[key]
    _RL[key] = _relabel_info(C, Z); return _RL[key]
def _relabel_info(C, Z):
    d, L, h = C['d'], C['L'], C['h']
    Z = np.array(Z); s = np.where(Z < 0, -1, 1); a = np.abs(Z); p = np.argsort(a, kind='stable'); rep = tuple(int(v) for v in a[p])
    def g(v): return tuple(int(s[p[j]] * v[p[j]]) for j in range(d))
    keep = C['keep']; kpos = {c: k for k, c in enumerate(keep)}; perm = np.zeros(C['m'], int)
    for k, site_i in enumerate(keep):
        u = C['sites'][site_i]; v = tuple(x - h for x in u); gv = g(v); t = tuple(x + h for x in gv)
        perm[k] = kpos[C['idx'][t]]
    perm[C['nl']] = C['nl']
    return rep, perm
def opbound(B):
    """rigorous upper bound for ||B||_op of a NONNEGATIVE float matrix (entrywise upper bound of |A|)."""
    f = math.sqrt(float(np.sum(B * B))) * (1 + gamma(B.size + 2))
    BtB = B.T @ B
    r = BtB.sum(axis=1).max() * (1 + gamma(B.shape[0] + B.shape[1] + 2))
    return min(f, math.sqrt(r) * (1 + 4 * U_RND))
def certificate(C, Rt, n, ws, extra_Z=()):
    d, m, nl, L = C['d'], C['m'], C['nl'], C['L']
    reps = reps_of(d, Rt); Zall = list(reps) + list(extra_Z)
    Kt, im = torus_kernel(C, n, Zall)
    Krep = {z: Kt[i] for i, z in enumerate(reps)}
    direct = {z: Kt[len(reps) + i] for i, z in enumerate(extra_Z)}
    def Ktil(Z):
        if max(abs(v) for v in Z) > Rt: return None
        rep, perm = relabel_info(C, Z); return Krep[rep][np.ix_(perm, perm)]
    # K~ norms via orbit sizes (K~(Z) is a row/column permutation of K~(rep))
    sums = {w: dict(k0=[], k1=[], k3=[], k4=[]) for w in ws}; Gest = []
    Qs = np.linalg.qr(np.column_stack([np.ones(nl)] + [np.eye(nl)[:, i] for i in range(nl - 1)]))[0][:, 1:]
    Ld = L ** d
    for z in reps:
        K = np.abs(Krep[z]); osz = orbit_size(z)
        lamom = opbound(K[:nl, :nl]); lameta = math.sqrt(math.fsum(K[:nl, nl] ** 2)) * (1 + gamma(nl + 2))
        allom = opbound(K[:, :nl]); alleta = math.sqrt(math.fsum(K[:, nl] ** 2)) * (1 + gamma(m + 2))
        Gest.append(osz * (Ld * np.linalg.norm(Krep[z][:nl, nl]) + np.linalg.norm(Krep[z][:nl, :nl] @ Qs, 2)))
        for w in ws:
            Kw = K.copy(); Kw[:, nl] /= w
            sums[w]['k0'].append(osz * (lamom + Ld * lameta)); sums[w]['k1'].append(osz * opbound(Kw[:nl, :]))
            sums[w]['k3'].append(osz * opbound(Kw)); sums[w]['k4'].append(osz * (allom + Ld * alleta))
    # residual E for every |Z| <= Rt+1
    K0, Kp = C['K0'], C['Kp']; aK0 = np.abs(K0); aKp = [np.abs(A) for A in Kp]
    g_E = gamma(m * (2 * d + 1) + 1)
    esum = {w: dict(e1=[], e2=[]) for w in ws}; Emax = 0.0; Einner = 0.0
    eye = np.eye(m)
    for Z in itertools.product(range(-Rt - 1, Rt + 2), repeat=d):
        E = np.zeros((m, m)); A = np.zeros((m, m))
        Kc = Ktil(Z)
        if Kc is not None: E += K0 @ Kc; A += aK0 @ np.abs(Kc)
        for mu in range(d):
            for sgn in (1, -1):
                Zw = list(Z); Zw[mu] += sgn; Kw_ = Ktil(tuple(Zw))
                if Kw_ is None: continue
                M_ = Kp[mu] if sgn > 0 else Kp[mu].T; aM = aKp[mu] if sgn > 0 else aKp[mu].T
                E += M_ @ Kw_; A += aM @ np.abs(Kw_)
        if all(v == 0 for v in Z): E -= eye; A += eye
        B = np.abs(E) + g_E * A * (1 + g_E)
        Emax = max(Emax, B.max())
        if max(abs(v) for v in Z) <= Rt - 1: Einner = max(Einner, B.max())
        for w in ws:
            Bw = B.copy(); Bw[nl, :] *= w; Bw[:, nl] /= w; Bw *= (1 + 4 * U_RND)
            esum[w]['e1'].append(opbound(Bw))
            Br = B.copy(); Br[nl, :] *= w; Br *= (1 + 4 * U_RND)
            esum[w]['e2'].append(opbound(Br[:, :nl]) + Ld * math.sqrt(math.fsum(Br[:, nl] ** 2)) * (1 + gamma(m + 2)))
    out = {}
    for w in ws:
        k0 = math.fsum(sums[w]['k0']) * INFL; k1 = math.fsum(sums[w]['k1']) * INFL; k3 = math.fsum(sums[w]['k3']) * INFL
        k4 = math.fsum(sums[w]['k4']) * INFL; e1 = math.fsum(esum[w]['e1']) * INFL; e2 = math.fsum(esum[w]['e2']) * INFL
        out[w] = dict(k0=k0, k1=k1, k3=k3, k4=k4, e1=e1, e2=e2)
    relerr = 0.0
    for z, Kd in direct.items():
        relerr = max(relerr, np.abs(Ktil(z) - Kd).max() / np.abs(Krep[(0,) * d]).max())
    return out, math.fsum(Gest), relerr, im, Emax, Einner
def Gsharp(c, delta, cD):
    if c['e1'] + cD * delta * c['k3'] >= 1: return None
    return c['k0'] + c['k1'] * (c['e2'] + cD * delta * c['k4']) / (1 - c['e1'] - cD * delta * c['k3'])
def cDelta(d, L, h, w): return (2 * d + 1) * 4 * d + 2 * d * h * math.sqrt(L ** d - 1) * (1 + w)
WS = [1, 10, 100, 1000]

print("== B. locally small backgrounds: certificate (d = 4, R_t = 5, torus 11) ==", flush=True)
tB = time.time()
extra = [(-3, 1, 0, 2), (0, -5, 2, 1), (4, -4, 1, -2), (1, 2, 3, -1), (-2, 0, 0, 0), (5, -1, -3, 2)]
cert4, Gest4, relerr4, im4, Emax4, Einner4 = certificate(C4, 5, 11, WS, extra)
verdict("B1", relerr4 <= 1e-12, f"relabelling vs direct torus kernel: max rel. difference {relerr4:.2e} (imag part max {im4:.1e})")
best = None
for w in WS:
    c = cert4[w]; g0 = Gsharp(c, 0.0, 0.0)
    print(f"    w={w}: k0 {c['k0']:.6f} k1 {c['k1']:.6f} k3 {c['k3']:.6f} k4 {c['k4']:.6f} e1 {c['e1']:.4e} e2 {c['e2']:.4e} "
          f"G#(0) {g0 if g0 is None else f'{g0:.6f}'}")
    if g0 is not None and (best is None or g0 < best[1]): best = (w, g0)
wB, G0 = best
verdict("B2", cert4[wB]['e1'] < 0.5 and G0 <= 1000, f"certified G^sharp(0) = {G0:.6f} at w = {wB}, e_1 = {cert4[wB]['e1']:.3e} "
        f"(max residual entry bound {Emax4:.2e}; inner |Z|<=4 max {Einner4:.2e}); {time.time() - tB:.1f} s")
verdict("B3", G0 >= Gest4, f"float estimate of the U = 1 value (|Z|<=5) G_est = {Gest4:.6f}; G^sharp(0)/G_est = {G0 / Gest4:.4f}")

print("== B4. end-to-end test of GF-B at d = 2 ==", flush=True)
cert2, Gest2, relerr2, im2, _, _ = certificate(C2, 5, 11, WS, [(-3, 1), (2, -5)])
for w in WS:
    c = cert2[w]; print(f"    d=2 w={w}: k0 {c['k0']:.5f} k1 {c['k1']:.5f} k3 {c['k3']:.5f} k4 {c['k4']:.5f} e1 {c['e1']:.3e} e2 {c['e2']:.3e}")
lat13 = Lat(2, 13)
def Gmeas(lat, U, hole=()):
    o = build(lat, U, hole, dense_Q=False); nlam = len(o['cols']); NB = o['NB']
    Kmat = np.zeros((nlam + 3 * NB, nlam + 3 * NB))
    Kmat[:nlam, :nlam] = o['GtG']; Kmat[:nlam, nlam:] = -o['Mp'].T; Kmat[nlam:, :nlam] = o['Mp']
    del o['GtG'], o['R']
    Ki = np.linalg.inv(Kmat); del Kmat
    Qb = {j: o['Qlist'][j] for j in range(NB)}
    best_ = 0.0
    for i in range(NB):
        ri = Qb[i][0]; s_ = 0.0
        for j in range(NB):
            cj, Qj = Qb[j]
            s_ += 9 * np.linalg.norm(Ki[np.ix_(ri, nlam + np.arange(3 * j, 3 * j + 3))], 2) + np.linalg.norm(Ki[np.ix_(ri, cj)] @ Qj, 2)
        best_ = max(best_, s_)
    return best_, o
tB4 = time.time()
U1 = np.broadcast_to(I2, (39, 39, 2, 2, 2)).copy()
G1, o1 = Gmeas(lat13, U1)
gR = haar_su2((39, 39)); Us = gauge_apply(lat13, gR, su2_exp(1e-6 * rng.normal(size=(39, 39, 2, 3)) / math.sqrt(3)))
eps2 = max_plaq(lat13, Us); delta2 = 1 * (3 * 6 + 1) * eps2
Gs_, os_ = Gmeas(lat13, Us)
cands = [(w, Gsharp(cert2[w], delta2, cDelta(2, 3, 1, w))) for w in WS]
okB4 = any(g is not None and Gs_ <= g for w, g in cands)
verdict("B4", okB4, f"eps = {eps2:.2e}, delta = {delta2:.2e}; G_meas(U) = {Gs_:.6f}; G^sharp(delta) per w: "
        + ", ".join(f"{w}:{'n/a' if g is None else f'{g:.5f}'}" for w, g in cands) + f"; G_meas(1) = {G1:.6f}; {time.time() - tB4:.1f} s")
verdict("B4b", abs(Gs_ - G1) <= 1e-3 * G1, f"|G_meas(U) - G_meas(1)|/G_meas(1) = {abs(Gs_ - G1) / G1:.2e}")
dK = np.abs(os_['Mp'] - o1['Mp']).max()   # entries of the eta'-rows / mu'-columns of K_U vs K_1
verdict("B4c", dK >= 0.1, f"max entry |K_U - K_1| in the original gauge = {dK:.3f} (a naive perturbation would fail)")
Ur = haar_su2((39, 39, 2)); Gr, _ = Gmeas(lat13, Ur)
print(f"B4n (REPORT): rough Haar background on the 13x13 torus: G_meas = {Gr:.4f} (GF-B hypothesis fails there); "
      f"d=2 float estimate G_est(U=1, |Z|<=5) = {Gest2:.5f}", flush=True)
del os_, o1

# ============================================================== C. chain arithmetic (mpmath)
print("== C. Corollary CHAIN-6 ==", flush=True)
mp.dps = 60
N, d, L, h = 3, 4, 3, 1
A_d = mpf((d - 1) * L * (L - 1)) / 2; C0 = mpf('1.011') * (4 * A_d + 4); Xinf = 2 * d * L ** (d // 2)
cg = (mpf('0.6') - mlog(2 - mexp(mpf('0.6')))) / mpf('0.09'); cgp = msqrt(N) * cg
def feas(G, zeta, rho):
    s0 = zeta / Xinf; r = rho * G * zeta
    I1 = 2 * cgp * G * Xinf * (s0 + 2 * r); rs = 2 * G * (Xinf * s0 + zeta)
    rsol = (s0 + 2 * rs) * (1 + cgp * (s0 + 2 * r)); tau = s0 / (msqrt(N) * C0)
    I4 = mpf('1.011') * msqrt(N) * L ** (mpf(d) / 2) * d * h * (rsol + s0)
    ok = (I1 <= mpf('0.5') and rs <= r and s0 + 2 * r <= mpf('0.3') and I4 <= r and d * h * (rsol + s0) <= mpf('0.5')
          and (4 * A_d + 4) * tau <= mpf('0.5') and mpf('18.8') * N * A_d ** 2 * tau <= 1 and mpf('1.011') * msqrt(N) * A_d * tau <= mpf(1) / 20)
    return ok, dict(s0=s0, r=r, rs=rs, rsol=rsol, tau=tau, I1=I1, I4r=I4 / r)
def solve_chain(G):
    bestz = (mpf(0), None)
    for k in range(0, 81):
        rho = mpf(500) + k * mpf('0.5')
        lo, hi = mpf(0), mpf('1e-2') / G ** 2
        if feas(G, hi, rho)[0]: continue
        for _ in range(150):
            mid = (lo + hi) / 2
            if feas(G, mid, rho)[0]: lo = mid
            else: hi = mid
        if lo > bestz[0]: bestz = (lo, rho)
    zmax, rho = bestz; z = mpf('0.99') * zmax; ok, v = feas(G, z, rho)
    return zmax, rho, z, ok, v
cbest = cert4[wB]
G = mpf(G0)
for it in range(5):
    zmax, rho, z, okc, v = solve_chain(G)
    eps = v['tau'] / 2; delta = (d - 1) * (L * 6 + h) * eps
    gs = Gsharp(cbest, float(delta), cDelta(4, 3, 1, wB))
    Gn = mpf(gs) * (1 + mpf('1e-12'))
    if abs(Gn - G) < mpf('1e-9') * G: G = Gn; break
    G = Gn
zmax, rho, z, okc, v = solve_chain(G)
eps = v['tau'] / 2; delta = (d - 1) * (L * 6 + h) * eps
hyp = cbest['e1'] + cDelta(4, 3, 1, wB) * float(delta) * cbest['k3'] < 1
CW = L + mpf('3.8') * msqrt(N) * (6 * L - 4)
def derived(v, z, label):
    tau = v['tau']; s0 = v['s0']
    rho_band = min(tau / (2 * CW), s0 / (msqrt(N) * Xinf))
    n_R = d * 4 ** d * L ** d; n1 = 2 * (d - 1) * n_R; n_K = d * 4 ** d
    ebg = tau / msqrt(2 * N * n1)
    cinf = mpf('2.0e37'); pL = 5 * L - 4
    Cbg = mpf('1.011') * msqrt(N) * max(1 + 48 * cinf, 36 * pL * cinf)
    e1 = min(tau, tau / (2 * Cbg), ebg / Cbg)
    print(f"  [{label}] zeta {float(z):.6e} s_0 {float(s0):.6e} r_* {float(v['rs']):.6e} r_sol {float(v['rsol']):.6e} "
          f"tau_c {float(tau):.6e}; (I1) {float(v['I1']):.4f}, (I4)/r {float(v['I4r']):.4f}")
    print(f"  [{label}] rho_band {float(rho_band):.4e}; eps_bg^(TH-bg) (a_p entry) {float(ebg):.4e}; C_bg {float(Cbg):.4e}; "
          f"(TH-ch') eps_1 <= {float(e1):.4e}")
    ns = 382 * (mpf('0.5') / e1) ** 2
    print(f"  [{label}] n_* SU(2) {float(ns):.3e}, SU(3) {float(255 * (mpf('0.5') / e1) ** 2):.3e}; n_sharp joint "
          f"{float(mpf('5e11') * (mpf('0.5') / e1) ** 2):.1e}-{float(mpf('4e15') * (mpf('0.5') / e1) ** 2):.1e}, RS "
          f"{float(mpf('4e13') * (mpf('0.5') / e1) ** 4):.1e}-{float(mpf('3e17') * (mpf('0.5') / e1) ** 4):.1e}; HW a_bad "
          f"{float(mpf('1.0e-123') * (e1 / mpf('4.3386e-59')) ** 2):.2e}; final levels {float(mlog(ns) / (4 * mlog(3))):.1f}; "
          f"eta_1 {float(min(e1 / (2 * L * L), e1 ** 2 / (512 * N * 9))):.3e}")
    # C3: DX'-1 / hole / FS-1 / band window rescaled
    mu = mpf('4.83e-11'); a_sh = rho_band / (16 * L ** 4)
    Rsh = mlog(v['rsol'] / a_sh) / mu; msh = (2 * Rsh / L + 3) ** d; OmB = 4 * (2 * Rsh + L) ** d
    gl = [a_sh ** 2 / (8 * N * (1 / lam) * msh) / OmB for lam in (mpf('6.6e-10'), mpf('7e-82'))]
    P = (N * N - 1) * (n_K + mpf(n_R) / 2); ap = tau ** 2 / (2 * N); x = 2 * P / ap; u = x * mlog(x)
    for _ in range(60): u = x * mlog(u)
    mX = (L ** d - 2) * (N * N - 1); ut = 4 * N * (mpf(mX) / 2 * mlog(2) + mlog(2)) / z ** 2
    win = rho_band / (4 * msqrt(N) * mpf('6.45e4'))
    print(f"  [{label}] C3: a_sh N' {float(a_sh):.3e}; R_sh {float(Rsh):.3e}; g_DX'^2 C_Omega N'^2 {float(gl[0]):.3e} (RW-l2) / "
          f"{float(gl[1]):.3e} (product rule); hole ceiling g_0^2 {float(1 / u):.3e}; FS-1 g_0^2 {float(1 / ut):.3e}; band window "
          f"g_0 max{{N_r,2N_mu}} {float(win):.3e}; a_*^B N_r^2 {float((rho_band / (4 * msqrt(N))) ** 2):.3e}")
    return e1
e1B = derived(v, z, "G^sharp")
print(f"  [G^sharp] G = {float(G):.6f} (w = {wB}, delta = {float(delta):.2e}); GF-B hypothesis e_1 + c_Delta delta k_3 = "
      f"{cbest['e1'] + cDelta(4, 3, 1, wB) * float(delta) * cbest['k3']:.4e}")
verdict("C1", okc and hyp, f"chain holds at 0.99 zeta_max (rho = {float(rho):.1f}) with G^sharp; GF-B hypothesis at eps = tau_c/2: {hyp}")
zmaxA, rhoA, zA, okA, vA = solve_chain(GA)
e1A = derived(vA, zA, "G^A")
verdict("C2", okA, f"chain holds at 0.99 zeta_max (rho = {float(rhoA):.1f}) with G^A = {float(GA):.4e}")
# FD-1 with Tier A decay (every background): prefactor (1 + c_R)(2/c_D^K)
pref = (1 + cR4) * 2 / aK; kap_c = mpf('2938.18')
ML = (kap_c + mlog(pref) + 1) / thA
print(f"C (REPORT) FD-1 with m_FP^A = {float(thA):.5f}/block, prefactor {float(pref):.3e}: M/L >= {float(ML):.4e} blocks, "
      f"M >= {float(L * ML):.4e} fine spacings (session 5: fails at M <~ 1e8)", flush=True)

# ============================================================== D. Lemma FH (d = 2)
print("== D. Lemma FH ==", flush=True)
hole = [(1, 1), (1, 2), (4, 4)]
okD = True; md = []
for name, U in bgs[:2]:
    o = build(lat6, U, hole); Q, Qb, GtG = o['Q'], o['Qblk'], o['GtG']
    Gres = Q.T @ GtG @ Q; ev = np.linalg.eigvalsh(Gres); Gi = np.linalg.inv(Gres); worst = 0.0
    for i, X in enumerate(o['blocks']):
        for j, Y in enumerate(o['blocks']):
            nr = np.linalg.norm(Gi[np.ix_(Qb == i, Qb == j)], 2); D = tdist(lat6, X, Y)
            worst = max(worst, nr * a2 * (math.cosh(D * th2) if D > 0 else 1.0))
    okD &= ev[0] >= a2 and ev[-1] <= 8 + 1e-9 and worst <= 1 + 1e-9
    md.append(f"{name}: spec [{ev[0]:.4f},{ev[-1]:.4f}], CHEB ratio {worst:.3e}")
verdict("D1", okD, "frozen hole (3 blocks): " + "; ".join(md))
lat6b = Lat(2, 6)
Gh, _ = Gmeas(lat6b, bgs[0][1], hole); Gn_, _ = Gmeas(lat6b, bgs[0][1])
print(f"D2 (REPORT): U = 1, 6x6 torus: G_meas without hole {Gn_:.5f}, with the 3-block frozen hole {Gh:.5f}", flush=True)

# ============================================================== F1. STEP-1 arithmetic
print("== F. STEP-1 arithmetic ==", flush=True)
mp.dps = 40
tau5 = mpf('4.3386e-59'); zeta5 = mpf('2.1880e-55'); rsol5 = mpf('1.0319e-30')
rb = tau5 / (2 * CW); ash = rb / (16 * L ** 4); Rsh5 = mlog(rsol5 / ash) / mpf('4.83e-11')
msh5 = (2 * Rsh5 / L + 3) ** 4; Om5 = 4 * (2 * Rsh5 + L) ** 4
g1 = ash ** 2 / (8 * N * (1 / mpf('6.6e-10')) * msh5) / Om5; g2 = ash ** 2 / (8 * N * (1 / mpf('7e-82')) * msh5) / Om5
nR = 82944; P5 = 8 * (1024 + mpf(nR) / 2); ap5 = tau5 ** 2 / 6; x5 = 2 * P5 / ap5; u5 = x5 * mlog(x5)
for _ in range(60): u5 = x5 * mlog(u5)
fs1 = 1 / (4 * N * (mpf(632) / 2 * mlog(2) + mlog(2)) / zeta5 ** 2)
win5 = rb / (4 * msqrt(3) * mpf('6.45e4')); asb = (rb / (4 * msqrt(3))) ** 2
Cbg5 = mpf('1.011') * msqrt(3) * max(1 + 48 * mpf('2.0e37'), 36 * 11 * mpf('2.0e37'))
eb5 = tau5 / msqrt(6 * 497664); e15 = min(tau5, tau5 / (2 * Cbg5), eb5 / Cbg5); ns5 = 382 * (mpf('0.5') / e15) ** 2
lev5 = mlog(ns5) / (4 * mlog(3))
def m3(x, ref, n=3): return f"{float(x):.{n - 1}e}" == f"{ref:.{n - 1}e}"
checks = [(rb, 2.280e-61, 4), (ash, 1.759e-64, 4), (Rsh5, 1.610e12, 4), (g1, 1.49e-237, 3), (g2, 1.58e-309, 3), (1 / u5, 1.6e-126, 2),
          (fs1, 1.8e-113, 2), (win5, 5.1e-67, 2), (asb, 1.08e-123, 3), (Cbg5, 1.39e40, 3), (e15, 1.81e-102, 3), (ns5, 2.9e205, 2)]
okF = all(m3(x, r, n) for x, r, n in checks) and int(lev5) in (107, 108)
verdict("F1", okF, "; ".join(f"{float(x):.4e}" for x, _, _ in checks) + f"; levels {float(lev5):.2f}")

print(f"OVERALL {'PASS' if all(RES.values()) else 'FAIL'} {sum(RES.values())}/{len(RES)}; failed: "
      f"{[k for k, v in RES.items() if not v]}; time {time.time() - T0:.1f} s")
