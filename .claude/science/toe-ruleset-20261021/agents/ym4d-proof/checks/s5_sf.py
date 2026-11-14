#!/usr/bin/env python3
"""s5 (lane F, session 5): checks for Lemma MSG_0, Lemma GF-dec, Lemma BCH-L, Proposition FP-uniq, Lemma KF, and the
arithmetic of the shrunk-chart radius chain. Criteria: checks/s5_criteria.md (written before this script)."""
import itertools, math, sys, time
import numpy as np
from scipy.linalg import expm

T0 = time.time()
rng = np.random.default_rng(20261028)
RES = {}
def verdict(name, ok, msg):
    RES[name] = bool(ok)
    print(f"{name}: {'PASS' if ok else 'FAIL'}  {msg}")

# ---------------------------------------------------------------- SU(2) helpers (2x2 complex)
SIG = np.array([[[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]], dtype=complex)
I2 = np.eye(2, dtype=complex)
def su2_exp(a):  # a: (...,3) coefficients of i a.sigma
    a = np.asarray(a, float); th = np.linalg.norm(a, axis=-1)
    s = np.where(th > 1e-300, np.sin(th) / np.where(th > 0, th, 1), 1.0)
    M = np.cos(th)[..., None, None] * I2 + 1j * (s[..., None, None] * np.einsum('...a,aij->...ij', a, SIG))
    return M
def su2_log(U):  # principal log coefficients
    c = np.clip(np.real(np.trace(U, axis1=-2, axis2=-1)) / 2, -1, 1); th = np.arccos(c)
    v = np.stack([np.imag(np.trace(U @ SIG[a], axis1=-2, axis2=-1)) / 2 for a in range(3)], axis=-1)  # = sin th * n_a
    s = np.sin(th); f = np.where(s > 1e-14, th / np.where(s > 1e-14, s, 1), 1.0)
    return v * f[..., None]
def haar_su2(shape):
    q = rng.normal(size=tuple(shape) + (4,)); q /= np.linalg.norm(q, axis=-1, keepdims=True)
    return q[..., 0, None, None] * I2 + 1j * np.einsum('...a,aij->...ij', q[..., 1:], SIG)
def adj(U):  # Ad(U) as 3x3 real: (Ad U)_{ab} = 1/2 tr(sigma_a U sigma_b U^+)
    Ud = np.conj(np.swapaxes(U, -1, -2))
    return np.real(np.stack([np.stack([np.trace(SIG[a] @ U @ SIG[b] @ Ud, axis1=-2, axis2=-1) / 2 for b in range(3)], -1)
                             for a in range(3)], -2))
def opn(M):
    return np.linalg.norm(M, ord=2)
dag = lambda M: np.conj(np.swapaxes(M, -1, -2))

# ---------------------------------------------------------------- lattice
class Lat:
    def __init__(s, d, T, L=3):
        s.d, s.T, s.L, s.n, s.h = d, T, L, T * L, (L - 1) // 2
        s.sites = list(itertools.product(range(s.n), repeat=d))
        s.sidx = {x: i for i, x in enumerate(s.sites)}
        s.blocks = list(itertools.product(range(T), repeat=d))
        s.bidx = {X: i for i, X in enumerate(s.blocks)}
    def add(s, x, mu, k=1):
        y = list(x); y[mu] = (y[mu] + k) % s.n; return tuple(y)
    def blk(s, x): return tuple(c // s.L for c in x)
    def centre(s, X): return tuple(s.L * c + s.h for c in X)
    def link(s, U, x, mu, sgn):  # W(x -> x + sgn e_mu)
        return U[x + (mu,)] if sgn > 0 else dag(U[s.add(x, mu, -1) + (mu,)])
    def axial_steps(s, c, x, order=None):  # block-internal axial path from c to x (no wrap inside a block)
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

def rand_field(lat, amp):
    return su2_exp(amp * rng.normal(size=(lat.n,) * lat.d + (lat.d, 3)) / math.sqrt(3))
def gauge_apply(lat, g, U):  # (g.U)_b = g(x) U_b g(y)^-1
    V = np.empty_like(U)
    for x in lat.sites:
        for mu in range(lat.d):
            V[x + (mu,)] = g[x] @ U[x + (mu,)] @ dag(g[lat.add(x, mu)])
    return V
def rand_GV(lat, amp=None):
    g = haar_su2((lat.n,) * lat.d) if amp is None else su2_exp(amp * rng.normal(size=(lat.n,) * lat.d + (3,)))
    for X in lat.blocks: g[lat.centre(X)] = I2
    return g

A_d = lambda d, L: (d - 1) * L * (L - 1) / 2

# ================================================================ A. Lemma MSG_0
print("== A. Lemma MSG_0 ==")
def gax(lat, U0, U, root=None):
    g = np.empty((lat.n,) * lat.d + (2, 2), complex)
    for x in lat.sites:
        X = lat.blk(x); c = lat.centre(X) if root is None else root(X)
        st = lat.axial_steps(c, x)
        g[x] = dag(lat.hol(U, st)) @ lat.hol(U0, st)
    return g
def block_plaq_max(lat, W, blocks):
    bs = set(blocks); m = 0.0
    for x in lat.sites:
        for mu in range(lat.d):
            for nu in range(mu + 1, lat.d):
                vs = [x, lat.add(x, mu), lat.add(x, nu), lat.add(lat.add(x, mu), nu)]
                if all(lat.blk(v) in bs for v in vs):
                    m = max(m, opn(I2 - lat.plaq(W, x, mu, nu)))
    return m
A1v = A2v = A3e = 0; A1r = A2r = 0.0; nA1 = nA2 = 0; A4e = 0.0; A5e = 0.0
for (d, T) in [(2, 4), (3, 2)]:
    lat = Lat(d, T); Ad = A_d(d, 3)
    for trial in range(3 if d == 2 else 2):
        eps = [1e-3, 5e-3, 2e-2][trial % 3]
        Ub = gauge_apply(lat, haar_su2((lat.n,) * d), rand_field(lat, eps))     # background: random gauge of small field
        U0 = gauge_apply(lat, rand_GV(lat), su2_exp(eps * rng.normal(size=(lat.n,) * d + (d, 3))) @ Ub)
        g = gax(lat, U0, Ub); G = gauge_apply(lat, g, U0)
        bp0 = {X: block_plaq_max(lat, U0, [X]) for X in lat.blocks}; bpU = {X: block_plaq_max(lat, Ub, [X]) for X in lat.blocks}
        pairc = {}
        for x in lat.sites:
            for mu in range(d):
                y = lat.add(x, mu); X, Y = lat.blk(x), lat.blk(y)
                diff = opn(G[x + (mu,)] - Ub[x + (mu,)])
                if X == Y:
                    tp = max(bp0[X], bpU[X]); nA1 += 1
                    if diff > 2 * Ad * tp + 1e-13: A1v += 1
                    if tp > 0: A1r = max(A1r, diff / (2 * Ad * tp))
                else:
                    if (X, Y) not in pairc:
                        pairc[(X, Y)] = (block_plaq_max(lat, U0, [X, Y]), block_plaq_max(lat, Ub, [X, Y]))
                    t0, tU = pairc[(X, Y)]
                    cX, cY = lat.centre(X), lat.centre(Y)
                    gx, gy = lat.axial_steps(cX, x), lat.axial_steps(cY, y)
                    Sc = [(lat.add(cX, mu, k), mu, 1) for k in range(lat.L)]
                    for W, tp in [(U0, t0), (Ub, tU)]:
                        hp = lat.hol(W, gx) @ W[x + (mu,)] @ dag(lat.hol(W, gy)); hs = lat.hol(W, Sc)
                        dd = opn(hp - hs); nA2 += 1
                        if dd > Ad * tp + 1e-13: A2v += 1
                        if tp > 0: A2r = max(A2r, dd / (Ad * tp))
                    hp0 = lat.hol(U0, gx) @ U0[x + (mu,)] @ dag(lat.hol(U0, gy))
                    hpU = lat.hol(Ub, gx) @ Ub[x + (mu,)] @ dag(lat.hol(Ub, gy))
                    A3e = max(A3e, abs(diff - opn(hp0 - hpU)))
        # A4 locality (d = 2 only, 20 trials total)
        if d == 2 and trial == 0:
            for t4 in range(20):
                x = lat.sites[rng.integers(len(lat.sites))]; mu = int(rng.integers(d)); y = lat.add(x, mu)
                inside = {lat.blk(x), lat.blk(y)}
                U1 = U0.copy()
                for z in lat.sites:
                    for nu in range(d):
                        if not (lat.blk(z) in inside and lat.blk(lat.add(z, nu)) in inside and
                                (lat.blk(z) == lat.blk(lat.add(z, nu)) or {lat.blk(z), lat.blk(lat.add(z, nu))} == inside)):
                            U1[z + (nu,)] = haar_su2(())
                g1 = gax(lat, U1, Ub)
                b1 = g1[x] @ U1[x + (mu,)] @ dag(g1[y]); b0 = g[x] @ U0[x + (mu,)] @ dag(g[y])
                A4e = max(A4e, opn(b1 - b0))
        # A5 orbit invariance
        gp = rand_GV(lat); U0p = gauge_apply(lat, gp, U0); Gp = gauge_apply(lat, gax(lat, U0p, Ub), U0p)
        A5e = max(A5e, max(opn(Gp[x + (mu,)] - G[x + (mu,)]) for x in lat.sites for mu in range(d)))
        if d == 2 and trial == 0:
            corner = lambda X: tuple(lat.L * c for c in X)
            Gc = gauge_apply(lat, gax(lat, U0, Ub, root=corner), U0); Gcp = gauge_apply(lat, gax(lat, U0p, Ub, root=corner), U0p)
            A7 = max(opn(Gcp[x + (mu,)] - Gc[x + (mu,)]) for x in lat.sites for mu in range(d))
verdict("A1", A1v == 0, f"intra-block links {nA1}, violations {A1v}, max ratio {A1r:.3f}")
verdict("A2", A2v == 0, f"ladder tests {nA2}, violations {A2v}, max ratio {A2r:.3f}")
verdict("A3", A3e <= 1e-12, f"identity max error {A3e:.2e}")
verdict("A4", A4e <= 1e-12, f"locality max change {A4e:.2e} (20 trials)")
verdict("A5", A5e <= 1e-10, f"orbit invariance max change {A5e:.2e}")
verdict("A6", min(A1r, A2r) >= 0.05, f"non-vacuity: max ratios A1 {A1r:.3f}, A2 {A2r:.3f}")
verdict("A7", A7 >= 1e-3, f"negative control (corner root): max change {A7:.3e}")

# ================================================================ B. Lemma GF-dec
print("== B. Lemma GF-dec ==")
def build_ops(lat, U):
    d, n = lat.d, lat.n; NS = len(lat.sites); links = [(x, mu) for x in lat.sites for mu in range(d)]
    lidx = {l: i for i, l in enumerate(links)}
    AdU = {l: adj(U[l[0] + (l[1],)]) for l in links}
    D = np.zeros((3 * len(links), 3 * NS))
    for i, (x, mu) in enumerate(links):
        y = lat.add(x, mu)
        D[3 * i:3 * i + 3, 3 * lat.sidx[y]:3 * lat.sidx[y] + 3] += AdU[(x, mu)]
        D[3 * i:3 * i + 3, 3 * lat.sidx[x]:3 * lat.sidx[x] + 3] -= np.eye(3)
    NB = len(lat.blocks); Mm = np.zeros((3 * NB, 3 * NS)); H = np.zeros((3 * NB, 3 * len(links)))
    orders = list(itertools.permutations(range(d)))
    for X in lat.blocks:
        c = lat.centre(X); bi = lat.bidx[X]
        bsites = [z for z in lat.sites if lat.blk(z) == X]; w = 1.0 / (len(bsites) * len(orders))
        for yv in bsites:
            for od in orders:
                st = lat.axial_steps(c, yv, od); Tm = I2.copy()
                for (z, mu, sgn) in st:
                    li = lidx[(z, mu)] if sgn > 0 else lidx[(lat.add(z, mu, -1), mu)]
                    blkmat = adj(Tm) if sgn > 0 else -adj(Tm) @ AdU[links[li]].T
                    H[3 * bi:3 * bi + 3, 3 * li:3 * li + 3] += w * blkmat
                    Tm = Tm @ lat.link(U, z, mu, sgn)
                Mm[3 * bi:3 * bi + 3, 3 * lat.sidx[yv]:3 * lat.sidx[yv] + 3] += w * adj(Tm)
    cen = set(lat.centre(X) for X in lat.blocks)
    lam_cols = [3 * lat.sidx[z] + a for z in lat.sites if z not in cen for a in range(3)]
    return dict(D=D, M=Mm, H=H, cols=np.array(lam_cols), links=links)
def gf_analysis(lat, U, want_inverse=False):
    ops = build_ops(lat, U); D, M, cols = ops['D'], ops['M'], ops['cols']
    G = D[:, cols]; Mc = M[:, cols]; d, L = lat.d, lat.L
    cD = 1.0 / (d * lat.h * L ** d)
    lam_min = np.linalg.eigvalsh(G.T @ G)[0]; Dn = np.linalg.norm(D, 2) ** 2
    # per-block structure: columns of block X
    blk_of_col = np.array([lat.bidx[lat.blk(lat.sites[c // 3])] for c in cols])
    smin = min(np.linalg.svd(Mc[3 * lat.bidx[X]:3 * lat.bidx[X] + 3][:, blk_of_col == lat.bidx[X]], compute_uv=False)[-1]
               for X in lat.blocks)
    # block-diagonality of M on Lambda
    offb = max(np.abs(Mc[3 * bi:3 * bi + 3][:, blk_of_col != bi]).max() for bi in range(len(lat.blocks)))
    # Lambda_res basis Q (block-structured)
    Qcols = []; Qblk = []
    for X in lat.blocks:
        bi = lat.bidx[X]; idx = np.where(blk_of_col == bi)[0]; m = Mc[3 * bi:3 * bi + 3][:, idx]
        _, s, vt = np.linalg.svd(m); ns = vt[3:].T
        for k in range(ns.shape[1]):
            q = np.zeros(len(cols)); q[idx] = ns[:, k]; Qcols.append(q); Qblk.append(bi)
    Q = np.array(Qcols).T; Qblk = np.array(Qblk)
    Gres = Q.T @ G.T @ G @ Q; Ginv = np.linalg.inv(Gres)
    q = (4 * d - cD) / (4 * d + cD)
    def bdist(i, j):
        Xi, Xj = lat.blocks[i], lat.blocks[j]
        return max(min((a - b) % lat.T, (b - a) % lat.T) for a, b in zip(Xi, Xj))
    NB = len(lat.blocks); worst = 0.0; bydist = {}
    for i in range(NB):
        for j in range(NB):
            nr = np.linalg.norm(Ginv[np.ix_(Qblk == i, Qblk == j)], 2); Dd = bdist(i, j)
            worst = max(worst, nr * cD / q ** Dd); bydist[Dd] = max(bydist.get(Dd, 0), nr)
    out = dict(lam_min=lam_min, cD=cD, Dn=Dn, smin=smin, offb=offb, worst=worst, bydist=bydist, q=q)
    # B5 inverse formula + h_U(D lam) = M lam check
    Mp = Mc.T @ np.linalg.inv(Mc @ Mc.T)
    res = 0.0
    for t in range(5):
        eta = rng.normal(size=Mc.shape[0]); om = rng.normal(size=Q.shape[1])
        lam = Mp @ eta + Q @ (Ginv @ (om - Q.T @ G.T @ G @ (Mp @ eta)))
        r1 = np.linalg.norm(Mc @ lam - eta) / np.linalg.norm(eta); r2 = np.linalg.norm(Q.T @ G.T @ G @ lam - om) / np.linalg.norm(om)
        res = max(res, r1, r2)
    out['res'] = res
    lam = rng.normal(size=len(cols)); out['hDM'] = np.linalg.norm(ops['H'] @ (G @ lam) - Mc @ lam) / np.linalg.norm(Mc @ lam)
    if want_inverse:
        CG = np.vstack([Mc, Q.T @ G.T @ G]); CGi = np.linalg.inv(CG)   # target blocks: eta rows (3 per block) then omega rows
        tblk = np.concatenate([np.repeat(np.arange(NB), 3), Qblk]); isom = np.concatenate([np.zeros(3 * NB, bool), np.ones(len(Qblk), bool)])
        rows = []
        for i in range(NB):   # row sum of (||A_XY|| + ||B_XY||): A acts on eta_Y, B on omega_Y (GF-dec (e))
            rs = sum(np.linalg.norm(CGi[np.ix_(blk_of_col == i, (tblk == j) & ~isom)], 2) +
                     np.linalg.norm(CGi[np.ix_(blk_of_col == i, (tblk == j) & isom)], 2) for j in range(NB)); rows.append(rs)
        out['Gmeas'] = max(rows)
        out.update(ops=ops, G=G, Mc=Mc, Q=Q, CG=CG, CGi=CGi, cols=cols, blk_of_col=blk_of_col, Qblk=Qblk, tblk=tblk)
    return out
def smooth_bg(lat, amp):
    a = np.zeros((lat.n,) * lat.d + (lat.d, 3))
    for x in lat.sites:
        for mu in range(lat.d):
            a[x + (mu,)] = amp * np.array([math.sin(2 * math.pi * (x[0] + 2 * x[-1]) / lat.n + k + mu) for k in range(3)])
    return gauge_apply(lat, haar_su2((lat.n,) * lat.d), su2_exp(a))
B = {}
for T in [5, 4]:
    lat = Lat(2, T)
    for name, U in [("trivial", np.broadcast_to(I2, (lat.n, lat.n, 2, 2, 2)).copy()), ("Haar", haar_su2((lat.n, lat.n, 2))),
                    ("smooth", smooth_bg(lat, 0.05))]:
        B[(T, name)] = gf_analysis(lat, U)
ok1 = all(b['lam_min'] >= b['cD'] - 1e-12 for b in B.values()); ok2 = all(b['Dn'] <= 8 + 1e-9 for b in B.values())
ok3 = all(b['smin'] >= 1 / 9 - 1e-12 and b['offb'] < 1e-14 for b in B.values())
ok4 = all(b['worst'] <= 1 + 1e-9 for b in B.values()); ok5 = all(b['res'] <= 1e-9 for b in B.values())
verdict("B1", ok1, "lambda_min(Gamma^T Gamma) / c_D: " + ", ".join(f"{k[1]}{k[0]} {b['lam_min'] / b['cD']:.2f}" for k, b in B.items()))
verdict("B2", ok2, "||D_U||^2: " + ", ".join(f"{b['Dn']:.3f}" for b in B.values()) + " (<= 4d = 8)")
verdict("B3", ok3, "sigma_min(M_X) * L^d: " + ", ".join(f"{9 * b['smin']:.3f}" for b in B.values()) + "; off-block max "
        + f"{max(b['offb'] for b in B.values()):.1e}")
verdict("B4", ok4, "max_{X,Y} ||G^-1(X,Y)|| c_D / q^|X-Y|: " + ", ".join(f"{b['worst']:.3e}" for b in B.values()))
verdict("B5", ok5, f"inverse formula max relative residual {max(b['res'] for b in B.values()):.1e}; [not a criterion] "
        f"h_U(D lam) = M lam rel. error {max(b['hDM'] for b in B.values()):.1e}")
for k, b in B.items():
    bd = b['bydist']; ks = sorted(bd)
    rate = -(math.log(bd[ks[-1]]) - math.log(bd[ks[1]])) / (ks[-1] - ks[1]) if len(ks) > 2 else float('nan')
    print(f"B6 (REPORT) {k[1]} T={k[0]}: max||G^-1|| by block distance " + ", ".join(f"{D}:{bd[D]:.3e}" for D in ks)
          + f"; measured rate {rate:.3f} vs m_FP {-math.log(b['q']):.3e}")

# ================================================================ C. Lemma BCH-L
print("== C. Lemma BCH-L ==")
def Gs(s): return s - math.log(2 - math.exp(s))
c_g = Gs(0.6) / 0.09
def rand_su(N, size):
    Z = rng.normal(size=(N, N)) + 1j * rng.normal(size=(N, N)); A = (Z - dag(Z)) / 2; A -= np.trace(A) / N * np.eye(N)
    return A / opn(A) * size
def logu(U):
    w, V = np.linalg.eig(U); return V @ np.diag(np.log(w)) @ np.linalg.inv(V)
def gfun(P): X, Y, Z = P; return logu(expm(X) @ expm(Y) @ expm(Z)) - X - Y - Z
Cv = 0; Cmax = 0.0; nC = 0
for N in [2, 3]:
    for r in [1e-3, 1e-2, 0.1, 0.3]:
        for t in range(260):
            w = rng.dirichlet(np.ones(3)) * r * rng.uniform(0.3, 0.99); P = [rand_su(N, wi) for wi in w]
            if t % 2 == 0:
                Pp = [p + rand_su(N, r * 1e-3) for p in P]
            else:
                w2 = rng.dirichlet(np.ones(3)) * r * rng.uniform(0.3, 0.99); Pp = [rand_su(N, wi) for wi in w2]
            sz = max(sum(opn(p) for p in P), sum(opn(p) for p in Pp))
            if sz > r: continue
            dist = sum(opn(a - b) for a, b in zip(P, Pp)); lhs = opn(gfun(P) - gfun(Pp)); nC += 1
            if lhs > c_g * r * dist * (1 + 1e-9) + 1e-15: Cv += 1
            if dist > 0: Cmax = max(Cmax, lhs / (r * dist))
verdict("C1", Cv == 0 and nC >= 2000, f"pairs {nC}, violations {Cv}, c_g = {c_g:.3f}")
print(f"C2 (REPORT): max ||g(P)-g(P')||/(r|P-P'|) = {Cmax:.4f} (bound c_g = {c_g:.2f})")

# ================================================================ D. Proposition FP-uniq (Newton)
print("== D. Proposition FP-uniq ==")
lat = Lat(2, 4); Ubg = smooth_bg(lat, 0.05); FD = gf_analysis(lat, Ubg, want_inverse=True)
ops = FD['ops']; links = ops['links']; Hm = ops['H']; G = FD['G']; Q = FD['Q']; cols = FD['cols']; CGi = FD['CGi']
NS = len(lat.sites); Gmeas = FD['Gmeas']; Xinf = 2 * 2 * 3 ** (2 / 2)
Ubl = np.array([Ubg[x + (mu,)] for (x, mu) in links])
xi = np.array([lat.sidx[x] for (x, mu) in links]); yi = np.array([lat.sidx[lat.add(x, mu)] for (x, mu) in links])
def A_of(lam_cols, A0):
    lam = np.zeros((NS, 3)); lam.reshape(-1)[cols] = lam_cols
    U0 = su2_exp(A0) @ Ubl
    W = su2_exp(lam[xi]) @ U0 @ su2_exp(-lam[yi]) @ dag(Ubl)
    return su2_log(W)
def Phi(lam_cols, A0, om):
    a = A_of(lam_cols, A0).reshape(-1)
    return np.concatenate([Hm @ a, Q.T @ (G.T @ a) - om])
site_links = {i: [] for i in range(NS)}
for k, (x, mu) in enumerate(links): site_links[lat.sidx[x]].append(k); site_links[lat.sidx[lat.add(x, mu)]].append(k)
def jac(lam_cols, A0, h=1e-7):
    base = A_of(lam_cols, A0); J = np.zeros((3 * len(links), len(cols)))
    for j, c in enumerate(cols):
        lp = lam_cols.copy(); lp[j] += h
        s = c // 3; ks = site_links[s]
        lam = np.zeros((NS, 3)); lam.reshape(-1)[cols] = lp
        U0 = su2_exp(A0[ks]) @ Ubl[ks]
        Wk = su2_exp(lam[xi[ks]]) @ U0 @ su2_exp(-lam[yi[ks]]) @ dag(Ubl[ks])
        dA = (su2_log(Wk) - base[ks]) / h
        for t, k in enumerate(ks): J[3 * k:3 * k + 3, j] = dA[t]
    return np.vstack([Hm @ J, Q.T @ (G.T @ J)])
def newton(l0, A0, om, iters=40, tol=1e-11, full=True):
    lam = l0.copy()
    for it in range(iters):
        F = Phi(lam, A0, om); nf = np.linalg.norm(F)
        if nf < tol: return lam, nf, True
        J = jac(lam, A0) if full else -FD['CG']
        try: step = np.linalg.solve(J, -F)
        except np.linalg.LinAlgError: return lam, nf, False
        t = 1.0
        while t > 1e-4:
            ln = lam + t * step
            if np.linalg.norm(Phi(ln, A0, om)) < (1 - 1e-4 * t) * nf: break
            t /= 2
        lam = ln
    nf = np.linalg.norm(Phi(lam, A0, om)); return lam, nf, nf < tol
def Bnorm(lam_cols):
    v = np.zeros((NS, 3)); v.reshape(-1)[cols] = lam_cols
    return max(math.sqrt(sum(np.sum(v[lat.sidx[z]] ** 2) for z in lat.sites if lat.blk(z) == X)) for X in lat.blocks)
D1ok = True; D2ok = True; D1msg = []; D2max = 0.0; sols = {}
for s0 in [1e-3, 1e-2]:
    A0 = rng.normal(size=(len(links), 3)); A0 *= s0 / np.linalg.norm(A0, axis=1).max()
    om = rng.normal(size=Q.shape[1]); omv = Q @ om
    ob = Bnorm(omv); om *= s0 / ob
    lam_s, nf, conv = newton(np.zeros(len(cols)), A0, om)
    bound = 2 * Gmeas * (Xinf * s0 + s0); ln = Bnorm(lam_s)
    D1ok &= conv and ln <= bound; D1msg.append(f"s0={s0:g}: conv {conv} res {nf:.1e} ||lam*||_B {ln:.3e} <= {bound:.3e}")
    sols[s0] = (A0, om, lam_s)
    for t in range(10):
        st = rng.normal(size=len(cols)); st *= rng.uniform(0, 5) * ln / Bnorm(st)
        l2, nf2, c2 = newton(st, A0, om)
        D2ok &= c2; D2max = max(D2max, np.abs(l2 - lam_s).max() if c2 else np.inf)
verdict("D1", D1ok, "; ".join(D1msg) + f"  (G_meas = {Gmeas:.3e}, X_inf = {Xinf:g})")
verdict("D2", D2ok and D2max <= 1e-9, f"10 small-ball starts per s0: all converge, max |difference| {D2max:.1e}")
A0, om, lam_s = sols[1e-2]; found = 0; ntry = 0; conv_far = 0; maxA = 0.0
for t in range(12):
    st = rng.normal(size=len(cols)) * rng.uniform(0.6, 1.4); ntry += 1
    l3, nf3, c3 = newton(st, A0, om, iters=60)
    if c3:
        conv_far += 1; Af = np.linalg.norm(A_of(l3, A0), axis=1).max(); dif = np.abs(l3 - lam_s).max()
        if dif >= 1e-2 and Af >= 0.1: found += 1; maxA = max(maxA, Af)
verdict("D3", found >= 1, f"O(1) starts {ntry}, converged {conv_far}, distinct zeros with |A| >= 0.1: {found} (max |A| {maxA:.3f})")

# ================================================================ E. Lemma KF
print("== E. Lemma KF ==")
def haar_sun(N):
    Z = (rng.normal(size=(N, N)) + 1j * rng.normal(size=(N, N))) / math.sqrt(2); Qm, R = np.linalg.qr(Z)
    Qm = Qm @ np.diag(np.diag(R) / np.abs(np.diag(R))); return Qm / np.linalg.det(Qm) ** (1 / N)
def Pi(Z, N): A = (Z - dag(Z)) / 2; return A - np.trace(A) / N * np.eye(N)
def W0(M, N):
    X = np.zeros((N, N), complex)
    for it in range(200):
        r = Pi(expm(-X) @ M, N); X = X + r
        if opn(r) < 1e-15: break
    return expm(X), opn(Pi(expm(-X) @ M, N))
E1v = E2v = E3v = 0; nE = 0; stat_max = 0.0
for N in [2, 3]:
    for y in [1e-3, 1e-2, 1 / 20]:
        for t in range(700):
            S = haar_sun(N); w = rng.dirichlet(np.ones(4)); Ys = [rand_su(N, 1) * y * rng.uniform(0.2, 1) / math.sqrt(N) for _ in range(4)]
            # |Y|_HS <= y: scale by HS norm
            Ys = [Yj / np.linalg.norm(Yj) * y * rng.uniform(0.2, 1) for Yj in Ys]
            Mp = sum(wj * expm(Yj) for wj, Yj in zip(w, Ys)); W, sres = W0(Mp, N); stat_max = max(stat_max, sres)
            M = S @ Mp; Wf = S @ W
            if t % 2 == 0: V = haar_sun(N)
            else: V = Wf @ expm(rand_su(N, 1) * 10 ** rng.uniform(-4, 0))
            phi = (np.real(np.trace(dag(Wf) @ M)) - np.real(np.trace(dag(V) @ M))) / N
            dv = opn(V - Wf); nE += 1
            if phi < dv ** 2 / (4 * N) - 1354.3 * y ** 4 - 1e-14: E1v += 1
            if phi > dv + 1e-14: E2v += 1
            if phi < dv ** 2 / (4 * N) - 1e-14: E3v += 1
verdict("E1", E1v == 0 and nE >= 4000, f"samples {nE}, violations {E1v} (W_0 stationarity residual max {stat_max:.1e})")
verdict("E2", E2v == 0, f"violations of phi <= ||V - W_0||: {E2v}")
print(f"E3 (REPORT): violations of the uncorrected phi >= ||V-W_0||^2/(4N): {E3v} of {nE}")

# ================================================================ F. Arithmetic
print("== F. Arithmetic (ARITHMETIC labels) ==")
d, L, N = 4, 3, 3; h = (L - 1) / 2; Ad4 = A_d(d, L); C0 = 1.011 * (4 * Ad4 + 4)
cD = 1 / (d * h * L ** d); q = (4 * d - cD) / (4 * d + cD); mFP = -math.log(q)
Dmax = int(60 / mFP); Dv = np.arange(0, Dmax + 1, dtype=float)
cnt = (2 * Dv + 1) ** d - np.where(Dv > 0, (2 * Dv - 1) ** d, 0.0)
S4 = float(np.sum(cnt * np.exp(-mFP * Dv)))
Ginf = L ** d + S4 / cD * (1 + 4 * d * 3 ** d * L ** d); Xinf4 = 2 * d * L ** (d / 2); cgH = math.sqrt(N) * c_g
CW = L + 3.8 * math.sqrt(N) * (6 * L - 4); nR = d * 3 ** d * L ** d; n1 = 2 * (d - 1) * nR
print(f"F1: A_d {Ad4:g}, C_0 {C0:.2f}, c_D {cD:.6f}, q {q:.9f}, m_FP {mFP:.4e}, S_4(q) {S4:.4e}, G_inf <= {Ginf:.4e}, X_inf {Xinf4:g},"
      f" c_g {c_g:.3f} (HS {cgH:.3f}), C_W {CW:.2f}, n_R {nR}, n_1 {n1}")
qinf = Ginf * Xinf4; K4 = 1.011 * math.sqrt(N) * L ** (d / 2) * d * h
# r := rho*Ginf*zeta; r_* = 4 Ginf zeta (s0 = zeta/Xinf); r_sol ~ (s0 + 2 r_*)(1+small); (I4): K4 (r_sol + s0) <= r
rho = max(4.0, K4 * (2 / (Xinf4 * Ginf) + 8.0) * 1.01 + 1e-9)
z1 = 0.5 / (2 * cgH * qinf * (1 / Xinf4 + 2 * rho * Ginf)); z3 = 0.3 / (1 / Xinf4 + 2 * rho * Ginf); zeta = 0.999 * min(z1, z3)
s0 = zeta / Xinf4; r = rho * Ginf * zeta; rstar = 2 * Ginf * (Xinf4 * s0 + zeta); rsol = (s0 + 2 * rstar) * (1 + cgH * (s0 + 2 * r))
I1 = 2 * cgH * qinf * (s0 + 2 * r) <= 0.5; I2 = rstar <= r; I3 = s0 + 2 * r <= 0.3; I4 = K4 * (rsol + s0) <= r and d * h * (rsol + s0) <= 0.5
tau_c = s0 / (math.sqrt(N) * C0); S0 = (4 * Ad4 + 4) * tau_c <= 0.5 and 18.8 * N * Ad4 ** 2 * tau_c <= 1 and 1.011 * math.sqrt(N) * Ad4 * tau_c <= 1 / 20
rho_band = min(tau_c / (2 * CW), s0 / (math.sqrt(N) * Xinf4)); epsbg = min(tau_c / 2, math.sqrt(tau_c ** 2 / (2 * N) / n1))
print(f"F2: rho {rho:.2f}, zeta {zeta:.4e}, s_0 {s0:.4e}, r {r:.4e}, r_* {rstar:.4e}, r_sol {rsol:.4e}, tau_c {tau_c:.4e}, rho_band {rho_band:.4e},"
      f" eps_bg max (TH-bg, a_p entry only) {epsbg:.4e}")
verdict("F2", I1 and I2 and I3 and I4 and S0, f"(I1) {I1} (I2) {I2} (I3) {I3} (I4) {I4} (S0) {S0}")
k0, kt0 = 151.315, 217.0472; v = k0 + 3 * kt0 + 5
verdict("F3", abs(v - 807.46) < 0.01, f"kappa_0 + 3 kappa~_0 + 5 = {v:.4f}")

ev = [k for k in RES]; npass = sum(RES[k] for k in ev)
print(f"OVERALL {'PASS' if npass == len(ev) else 'FAIL'} {npass}/{len(ev)}  runtime {time.time() - T0:.1f} s")
