"""f9: the root sector at constant Cartan curvature (lane C, session 6).

Criteria: checks/f9_criteria.md (written before this script). Tests FLOW.md §42-§46.
Parts: G0 (Lemma GH algebra), G1 (Lemma G-mag (iii)), G2 (G-mag (v), (vi)), G3 (Proposition GH-log),
V0 (SU(2) criticality and the §46 decomposition), V1 (scalar calibration), V2 ((V-heat)), V4 (Cartan block).
Set F9_SMOKE=1 for a reduced development run.
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS",
           "NUMEXPR_NUM_THREADS"):
    os.environ[_v] = "1"
import sys
import time
import resource
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
from scipy.special import ive

SMOKE = os.environ.get("F9_SMOKE", "0") == "1"
T0 = time.time()
CG = 1.0 / (96.0 * np.pi ** 2)
H_FD = 1e-3
RESULTS = []


def say(*a):
    print(*a, flush=True)


def verdict(name, ok, detail):
    RESULTS.append((name, ok))
    say(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")


def j(nu, t):
    return ive(nu, 2.0 * np.asarray(t, dtype=float))


def richardson(y0, yh, y2h, h):
    d1 = (yh - y0) / h ** 2
    d2 = (y2h - y0) / (2 * h) ** 2
    return (4 * d1 - d2) / 3.0


# ---------------------------------------------------------------- generic lattice helpers
def site_index(x, dims):
    return np.ravel_multi_index(tuple(np.mod(x[:, k], dims[k]) for k in range(len(dims))), dims)


def all_sites(dims):
    return np.array(np.unravel_index(np.arange(int(np.prod(dims))), dims)).T


def links_of(dims, periodic):
    """Return list of (site, mu, site_plus) for all links that exist, and a dict (site, mu) -> link index."""
    X = all_sites(dims)
    out = []
    for mu in range(len(dims)):
        ok = np.ones(len(X), bool) if periodic[mu] else (X[:, mu] + 1 < dims[mu])
        xs = X[ok]
        xp = xs.copy()
        xp[:, mu] += 1
        s = site_index(xs, dims)
        sp_ = site_index(xp, dims)
        for a, b in zip(s, sp_):
            out.append((int(a), mu, int(b)))
    out.sort()
    idx = {(a, mu): k for k, (a, mu, b) in enumerate(out)}
    return out, idx


def theta_landau(x, mu, f, dims, seam):
    """Cartan angle of link (x, mu): U_{x,2} = exp(i f x_1); seam on direction 1 if seam (torus)."""
    if mu == 1:
        return f * x[0]
    if mu == 0 and seam and x[0] == dims[0] - 1:
        return -f * dims[0] * x[1]
    return 0.0


# ---------------------------------------------------------------- Part G0: Lemma GH algebra (U(1) charge 1)
def g0_case(dims, ctl=False, rng=None):
    links, lidx = links_of(dims, [True] * len(dims))
    X = all_sites(dims)
    phi = 2 * np.pi / (dims[0] * dims[1])
    nS, nL = len(X), len(links)
    D = np.zeros((nL, nS), complex)
    for k, (a, mu, b) in enumerate(links):
        th = theta_landau(X[a], mu, phi, dims, True)
        D[k, b] += np.exp(1j * th)
        D[k, a] -= 1.0
    lev = np.all(X % 3 == 0, axis=1)
    In, Ip = np.where(lev)[0], np.where(~lev)[0]
    Del = D.conj().T @ D
    Dp = Del[np.ix_(Ip, Ip)]
    Sch = Del[np.ix_(In, In)] - Del[np.ix_(In, Ip)] @ np.linalg.solve(Dp, Del[np.ix_(Ip, In)])
    Dl = D[:, Ip]                          # D_0 Lambda'
    Pg = Dl @ np.linalg.solve(Dl.conj().T @ Dl, Dl.conj().T)
    PS0 = np.eye(nL) - Pg
    E = np.zeros((nS, len(In)))
    E[In, np.arange(len(In))] = 1.0
    DE = D @ E
    if not ctl:
        J = PS0 @ DE
    else:
        # non-orthogonal complement S_r = (1 + eps R) S_0; J_r = S_r-component of D_0 E along D_0 Lambda'
        w, V = np.linalg.eigh(PS0)
        B0 = V[:, w > 0.5]
        R = rng.standard_normal((nL, nL)) + 1j * rng.standard_normal((nL, nL))
        R /= np.linalg.norm(R, 2)
        Br = B0 + 0.3 * R @ B0
        M = np.hstack([Br, Dl])
        coef = np.linalg.solve(M, DE)
        J = Br @ coef[:Br.shape[1]]
    JJ = J.conj().T @ J
    ra = np.linalg.norm(JJ - Sch, 2) / np.linalg.norm(Sch, 2)
    if ctl:
        return ra
    ld = lambda A: np.linalg.slogdet(A)[1]
    rb = abs(ld(Del) - ld(Dp) - ld(Sch))
    PJ = J @ np.linalg.solve(JJ, J.conj().T)
    Pker = np.eye(nL) - D @ np.linalg.solve(Del, D.conj().T)
    rc = np.linalg.norm(PS0 - PJ - Pker, 2)
    return ra, rb, rc


def part_g0():
    say("Part G0 (Lemma GH: J^*J = Schur, det split, S_0 - J = ker D_0^*; charge-1 torus, one flux quantum, l = 3)")
    rng = np.random.default_rng(9)
    for dims in [(9, 9), (3, 3, 3, 3)]:
        ra, rb, rc = g0_case(dims)
        verdict(f"G0a {dims}", ra <= 1e-10, f"||J^*J - S||/||S|| = {ra:.2e}")
        verdict(f"G0b {dims}", rb <= 1e-9, f"|logdet D0 - logdet D' - logdet S| = {rb:.2e}")
        verdict(f"G0c {dims}", rc <= 1e-10, f"||P_S0 - P_J - P_ker|| = {rc:.2e}")
        rctl = g0_case(dims, ctl=True, rng=rng)
        verdict(f"G0-ctl {dims} (must FAIL G0a)", rctl >= 1e-3, f"non-orthogonal slice: ||J_r^*J_r - S||/||S|| = {rctl:.2e}")


# ---------------------------------------------------------------- Part G1: exact second moment (2D Harper, open box)
def harper_open(B, phi, q=1):
    dims = (B, B)
    links, _ = links_of(dims, [False, False])
    X = all_sites(dims)
    c = B // 2
    rows, cols, vals = [], [], []
    for k, (a, mu, b) in enumerate(links):
        th = q * phi * (X[a][0] - c) if mu == 1 else 0.0
        rows += [k, k]
        cols += [b, a]
        vals += [np.exp(1j * th), -1.0]
    D = sp.csr_matrix((vals, (rows, cols)), shape=(len(links), len(X)))
    return (D.conj().T @ D).tocsr(), int(site_index(np.array([[c, c]]), dims)[0])


def heat_diag(K, e, tmax, num):
    """<e, exp(-tK) e> on t = linspace(0, tmax, num)."""
    V = spla.expm_multiply(-K, e, start=0.0, stop=tmax, num=num, endpoint=True)
    return np.real(V @ e.conj()) if np.iscomplexobj(V) else V @ e


def part_g1():
    say("Part G1 (Lemma G-mag (iii): phi^2 coefficient of exp(-t Delta_phi)(x0,x0) = -(t^2/6) j_1^2, 2D)")
    B = 41 if SMOKE else 81
    ts = np.array([0.5, 1, 2, 4] if SMOKE else [0.5, 1, 2, 4, 8, 16])
    tmax = ts.max()
    num = int(round(tmax / 0.5)) + 1
    grid = np.linspace(0, tmax, num)
    pick = [int(np.argmin(abs(grid - t))) for t in ts]
    Y = []
    for ph in (0.0, H_FD, 2 * H_FD):
        K, c = harper_open(B, ph)
        e = np.zeros(K.shape[0], complex)
        e[c] = 1.0
        Y.append(heat_diag(K, e, tmax, num)[pick])
    cc = richardson(Y[0], Y[1], Y[2], H_FD)
    pred = -(ts ** 2 / 6.0) * j(1, ts) ** 2
    rel = np.abs(cc / pred - 1)
    for t, a, p, r in zip(ts, cc, pred, rel):
        say(f"    t = {t:5.1f}: coeff = {a:.10e}, predicted = {p:.10e}, rel = {r:.1e}")
    verdict("G1", bool(np.all(rel <= 1e-6)), f"max rel = {rel.max():.2e} (B = {B})")


# ---------------------------------------------------------------- Part G2/G3: psi(phi) from rational-flux Harper Bloch
def harper_bloch_eigs(Q, K):
    phi = 2 * np.pi / Q
    out = []
    jj = np.arange(Q)
    for i1 in range(K):
        th1 = 2 * np.pi * (i1 + 0.5) / K
        for i2 in range(K):
            k2 = (2 * np.pi / Q) * (i2 + 0.5) / K
            Hm = np.diag(4 - 2 * np.cos(k2 + phi * jj)).astype(complex)
            if Q == 1:
                Hm[0, 0] += -2 * np.cos(th1)
            else:
                Hm[jj[:-1], jj[1:]] += -1.0
                Hm[jj[1:], jj[:-1]] += -1.0
                Hm[Q - 1, 0] += -np.exp(1j * th1)
                Hm[0, Q - 1] += -np.exp(-1j * th1)
            out.append(np.linalg.eigvalsh(Hm))
    return np.concatenate(out), phi


def psi_of(Q, K=4, du=0.01):
    E, phi = harper_bloch_eigs(Q, K)
    u = np.arange(-8.0, 16.0 + du / 2, du)
    t = np.exp(u)
    tau = np.empty_like(t)
    nE = len(E)
    for i0 in range(0, len(t), 200):
        tt = t[i0:i0 + 200]
        tau[i0:i0 + 200] = np.exp(-np.outer(tt, E)).sum(axis=1) / nE
    j0 = j(0, t)
    integ = j0 ** 2 * (j0 ** 2 - tau)
    return np.trapezoid(integ, u) / phi ** 2, phi


def part_g2_g3():
    say("Part G2 (psi(phi) = c_g log(1/phi) + c'(phi), c_g = 1/(96 pi^2); rational flux 2 pi/Q, Bloch)")
    Qs = [16, 32, 64] if SMOKE else [16, 32, 64, 128, 256, 512]
    cache = {}

    def psi(Q):
        if Q not in cache:
            cache[Q] = psi_of(Q)[0]
        return cache[Q]

    Qacc = 32 if SMOKE else 128
    pa = psi(Qacc)
    pK8 = psi_of(Qacc, K=8)[0]
    pdu = psi_of(Qacc, du=0.02)[0]
    acc = max(abs(pa - pK8), abs(pa - pdu))
    verdict("G2-acc", acc <= 1e-8, f"Q = {Qacc}: |dK| = {abs(pa - pK8):.1e}, |ddu| = {abs(pa - pdu):.1e}")
    phis = np.array([2 * np.pi / Q for Q in Qs])
    ps = np.array([psi(Q) for Q in Qs])
    cp = ps - CG * np.log(1 / phis)
    for Q, ph, p, c in zip(Qs, phis, ps, cp):
        say(f"    Q = {Q:4d}: phi = {ph:.5f}, psi = {p:.9e}, c' = {c:.9e}")
    sl = np.polyfit(np.log(1 / phis[-3:]), ps[-3:], 1)[0]
    verdict("G2a", abs(sl / CG - 1) <= 0.02, f"slope/c_g = {sl / CG:.5f}")
    dl = np.diff(cp)
    say("    increments of c': " + ", ".join(f"{d:.3e}" for d in dl))
    ok = len(dl) >= 3 and all(abs(dl[k + 1]) <= 0.75 * abs(dl[k]) for k in range(len(dl) - 3, len(dl) - 1)) \
        and abs(dl[-1]) <= 1e-4
    verdict("G2b", ok, f"last ratios = {', '.join(f'{abs(dl[k + 1] / dl[k]):.3f}' for k in range(len(dl) - 3, len(dl) - 1))}, |d_last| = {abs(dl[-1]):.2e}")
    say("Part G3 (ghost group: psi(l^2 phi) - psi(phi) -> -2 c_g log l)")
    for l, Qps, pre in [(3, [16, 32] if SMOKE else [16, 32, 64], True), (9, [4] if SMOKE else [4, 8], False)]:
        target = -2 * CG * np.log(l)
        devs = []
        for Qp in Qps:
            d = psi(Qp) - psi(l * l * Qp)
            devs.append(abs(d / target - 1))
            say(f"    l = {l}, Q' = {Qp:3d} (fine Q = {l * l * Qp}): Delta = {d:.9e}, target = {target:.9e}, rel dev = {devs[-1]:.2e}")
        if pre:
            mono = all(devs[k + 1] < devs[k] for k in range(len(devs) - 1))
            verdict("G3a (l = 3)", devs[-1] <= 0.02 and mono, f"final rel dev = {devs[-1]:.2e}, monotone = {mono}")
        else:
            say(f"    G3b (l = 9) informational: rel devs = {', '.join(f'{x:.2e}' for x in devs)}")


# ---------------------------------------------------------------- Part V: SU(2) Wilson Hessian at a Cartan background
SIG = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]], complex), np.array([[1, 0], [0, -1]], complex)]
TA = [1j * s for s in SIG]          # orthonormal for -1/2 tr


def u3(th):
    th = np.asarray(th, float)
    U = np.zeros(th.shape + (2, 2), complex)
    U[..., 0, 0] = np.exp(1j * th)
    U[..., 1, 1] = np.exp(-1j * th)
    return U


def adinv(th):
    """matrix R_ca of Ad(U^{-1}) on the basis TA, U = exp(i th sigma_3)."""
    U = u3(th)
    Ui = np.conj(np.swapaxes(U, -1, -2))
    R = np.zeros(np.shape(th) + (3, 3))
    for a in range(3):
        Y = Ui @ TA[a] @ U
        for c in range(3):
            R[..., c, a] = np.real(-0.5 * np.einsum("...ij,ji->...", Y, TA[c]))
    return R


def build_su2(dims, periodic, f, seam):
    links, lidx = links_of(dims, periodic)
    X = all_sites(dims)
    nL, nS = len(links), len(X)
    th = np.array([theta_landau(X[a], mu, f, dims, seam) for (a, mu, b) in links])
    U = u3(th)
    Ui = np.conj(np.swapaxes(U, -1, -2))
    plaq = []
    for a in range(nS):
        x = X[a]
        for mu in range(len(dims)):
            for nu in range(mu + 1, len(dims)):
                if (a, mu) not in lidx or (a, nu) not in lidx:
                    continue
                xm = x.copy(); xm[mu] += 1
                xn = x.copy(); xn[nu] += 1
                if (not periodic[mu] and xm[mu] >= dims[mu]) or (not periodic[nu] and xn[nu] >= dims[nu]):
                    continue
                am = int(site_index(xm[None], dims)[0]); an = int(site_index(xn[None], dims)[0])
                if (am, nu) not in lidx or (an, mu) not in lidx:
                    continue
                plaq.append((lidx[(a, mu)], lidx[(am, nu)], lidx[(an, mu)], lidx[(a, nu)]))
    plaq = np.array(plaq)
    P = len(plaq)
    sgn = [1.0, 1.0, -1.0, -1.0]
    # gaps after slots 1..4: g1 = U2, g2 = 1, g3 = U3^{-1}, g4 = U4^{-1} U1
    g = [U[plaq[:, 1]], np.broadcast_to(np.eye(2, dtype=complex), (P, 2, 2)), Ui[plaq[:, 2]],
         Ui[plaq[:, 3]] @ U[plaq[:, 0]]]

    def chain(i, jx):  # product g_i ... g_{jx-1} (cyclic, 0-based slots), empty -> identity
        M = np.broadcast_to(np.eye(2, dtype=complex), (P, 2, 2)).copy()
        k = i
        while k != jx:
            M = M @ g[k]
            k = (k + 1) % 4
        return M

    def full(i):  # g_i g_{i+1} ... g_{i-1}
        M = np.broadcast_to(np.eye(2, dtype=complex), (P, 2, 2)).copy()
        for s in range(4):
            M = M @ g[(i + s) % 4]
        return M

    grad = np.zeros(3 * nL)
    rows, cols, vals = [], [], []
    for i in range(4):
        Fi = full(i)
        for a in range(3):
            gv = -0.5 * np.real(np.einsum("ij,pji->p", sgn[i] * TA[a], Fi))
            np.add.at(grad, 3 * plaq[:, i] + a, gv)
            for c in range(3):
                Y2 = 0.5 * (TA[a] @ TA[c] + TA[c] @ TA[a])
                hv = -0.5 * np.real(np.einsum("ij,pji->p", Y2, Fi))
                rows.append(3 * plaq[:, i] + a); cols.append(3 * plaq[:, i] + c); vals.append(hv)
        for jx in range(i + 1, 4):
            Mij, Mji = chain(i, jx), chain(jx, i)
            for a in range(3):
                for c in range(3):
                    Z = np.einsum("ij,pjk,kl,plm->pim", sgn[i] * TA[a], Mij, sgn[jx] * TA[c], Mji)
                    hv = -0.5 * np.real(np.einsum("pii->p", Z))
                    rows += [3 * plaq[:, i] + a, 3 * plaq[:, jx] + c]
                    cols += [3 * plaq[:, jx] + c, 3 * plaq[:, i] + a]
                    vals += [hv, hv]
    H = sp.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(3 * nL, 3 * nL))
    R = adinv(th)
    dr, dc, dv = [], [], []
    for k, (a, mu, b) in enumerate(links):
        for cc in range(3):
            for aa in range(3):
                if R[k, cc, aa] != 0.0:
                    dr.append(3 * k + cc); dc.append(3 * a + aa); dv.append(R[k, cc, aa])
            dr.append(3 * k + cc); dc.append(3 * b + cc); dv.append(-1.0)
    D0 = sp.csr_matrix((dv, (dr, dc)), shape=(3 * nL, 3 * nS))
    return dict(H=H, D0=D0, grad=grad, links=links, lidx=lidx, X=X, nS=nS, nL=nL)


def part_v0():
    say("Part V0 (SU(2) Wilson at U_f on the 4D torus (6,6,3,3), one flux quantum f = 2 pi/36)")
    dims4 = (6, 6, 3, 3)
    fq = 2 * np.pi / 36
    for label, f, must_pass in [("", fq, True), (" ctl (f = 1.3 x quantum)", 1.3 * fq, False)]:
        S = build_su2(dims4, [True] * 4, f, seam=True)
        H, D0 = S["H"], S["D0"]
        ga = np.abs(S["grad"]).max()
        hd = np.abs((H @ D0).toarray()).max()
        if must_pass:
            KF = (H + D0 @ D0.T).tocsr()
            Lap = (D0.T @ D0).tocsr()
            kc = np.abs((KF @ D0 - D0 @ Lap).toarray()).max()
            Hd = H.toarray()
            cart = np.arange(2, H.shape[0], 3)
            root = np.setdiff1d(np.arange(H.shape[0]), cart)
            cr = np.abs(Hd[np.ix_(cart, root)]).max()
            verdict("V0a", ga <= 1e-12, f"max |grad| = {ga:.1e}")
            verdict("V0b", hd <= 1e-11, f"max |H D_0| = {hd:.1e} (max |H| = {np.abs(Hd).max():.2f})")
            verdict("V0c", kc <= 1e-11, f"max |K_F D_0 - D_0 Delta_0| = {kc:.1e}")
            verdict("V0d", cr <= 1e-12, f"max |H_(Cartan,root)| = {cr:.1e}")
            # V0e: prediction from 2D objects
            S2 = build_su2((6, 6), [True, True], f, seam=True)
            K12 = (S2["H"] + S2["D0"] @ S2["D0"].T).toarray()
            L12 = (S2["D0"].T @ S2["D0"]).toarray()
            l2 = {(a, mu): k for k, (a, mu, b) in enumerate(S2["links"])}
            # free 3x3 Laplacian on the 34 torus
            d34 = (3, 3)
            L34 = np.zeros((9, 9))
            for s in range(9):
                x = np.array(np.unravel_index(s, d34))
                for mu in range(2):
                    for dlt in (1, -1):
                        y = x.copy(); y[mu] += dlt
                        L34[s, int(site_index(y[None], d34)[0])] -= 1.0
                L34[s, s] += 4.0
            nd = H.shape[0]
            Kp = np.zeros((nd, nd))
            X4 = S["X"]
            info = []
            for k, (a, mu, b) in enumerate(S["links"]):
                x = X4[a]
                s12 = int(site_index(x[None, :2], (6, 6))[0])
                s34 = int(site_index(x[None, 2:], (3, 3))[0])
                info.append((s12, s34, mu))
            byk = {v: k for k, v in enumerate(info)}
            # assemble block-wise (loop over 2D structure)
            for (s12, s34, mu), k in byk.items():
                for cc in range(3):
                    r = 3 * k + cc
                    if mu < 2:
                        r2 = 3 * l2[(s12, mu)] + cc
                        for (t12, nu), k2d in l2.items():
                            for ee in range(3):
                                v = K12[r2, 3 * k2d + ee]
                                if v != 0.0:
                                    Kp[r, 3 * byk[(t12, s34, nu)] + ee] += v
                    else:
                        for t12 in range(36):
                            for ee in range(3):
                                v = L12[3 * s12 + cc, 3 * t12 + ee]
                                if v != 0.0:
                                    Kp[r, 3 * byk[(t12, s34, mu)] + ee] += v
                    for t34 in range(9):
                        v = L34[s34, t34]
                        if v != 0.0:
                            Kp[r, 3 * byk[(s12, t34, mu)] + cc] += v
            de = np.abs(KF.toarray() - Kp).max()
            verdict("V0e", de <= 1e-12, f"max |K_F - prediction| = {de:.1e} (dof {nd})")
        else:
            verdict("V0-ctl (must FAIL V0a, V0b)", ga >= 1e-3 and hd >= 1e-3, f"max |grad| = {ga:.2e}, max |H D_0| = {hd:.2e}")


def part_v124():
    say("Part V1, V2, V4 (2D open box, SU(2) plane-12 operator K_12 = H + D_0 D_0^T at U_f, root charge q = 2)")
    B = 41 if SMOKE else 101
    ts = np.array([2, 3, 4, 6] if SMOKE else [2, 3, 4, 6, 8, 12, 16, 24], float)
    tmax = ts.max()
    num = int(round(tmax / 0.5)) + 1
    grid = np.linspace(0, tmax, num)
    pick = [int(np.argmin(abs(grid - t))) for t in ts]
    q = 2.0
    c = B // 2
    Yv, Yc, Ys = [], [], []
    for fv in (0.0, H_FD, 2 * H_FD):
        S = build_su2((B, B), [False, False], fv, seam=False)
        # U_{x,2} = exp(i sigma_3 f x_1) differs from the gauge centred at c by a gauge transformation; the diagonal
        # heat-kernel entries at the centre are gauge invariant
        K =(S["H"] + S["D0"] @ S["D0"].T).tocsr()
        Lap = (S["D0"].T @ S["D0"]).tocsr()
        sc = int(site_index(np.array([[c, c]]), (B, B))[0])
        rv, rc_ = 0.0, 0.0
        for mu in range(2):
            k = S["lidx"][(sc, mu)]
            for a in range(3):
                e = np.zeros(K.shape[0]); e[3 * k + a] = 1.0
                d = heat_diag(K, e, tmax, num)[pick]
                if a < 2:
                    rv = rv + d
                else:
                    rc_ = rc_ + d
        rs = 0.0
        for a in range(2):
            e = np.zeros(Lap.shape[0]); e[3 * sc + a] = 1.0
            rs = rs + heat_diag(Lap, e, tmax, num)[pick]
        Yv.append(0.5 * rv); Yc.append(rc_); Ys.append(0.5 * rs)
    j0, j1 = j(0, ts), j(1, ts)
    # V1
    cs = richardson(*Ys, H_FD)
    preds = -0.5 * q ** 2 * (ts ** 2 / 3.0) * j1 ** 2
    rel = np.abs(cs / preds - 1)
    verdict("V1", bool(np.all(rel <= 1e-6)), f"max rel = {rel.max():.2e} (B = {B})")
    # V2
    nrm = np.abs(Yv[0] / (2 * j0 ** 2) - 1).max()
    verdict("V2-norm", nrm <= 1e-10, f"max |Y(0)/(2 j_0^2) - 1| = {nrm:.1e}")
    cv = richardson(*Yv, H_FD)
    R12 = cv / (q ** 2 * ts ** 2 * j0 ** 2)
    RS = cs / (q ** 2 * ts ** 2 * j0 ** 2)
    for t, r, rs_ in zip(ts, R12, RS):
        say(f"    t = {t:4.0f}: R_12 = {r:.6f}, R_S = {rs_:.6f}, R_V4D = R_12 + 2R_S = {r + 2 * rs_:.6f}, R_12 + R_S = {r + rs_:.6f}")

    def fit(sel):
        A = np.vstack([np.ones(len(sel)), 1 / ts[sel], 1 / ts[sel] ** 2]).T
        return np.linalg.lstsq(A, R12[sel], rcond=None)[0]
    if SMOKE:
        selA, selB = np.arange(len(ts) - 3, len(ts)), np.arange(0, 3)
    else:
        selA = np.array([3, 4, 5, 6, 7]); selB = np.array([2, 3, 4, 5, 6])
    fa, fb = fit(selA), fit(selB)
    verdict("V2a", abs(fa[0] / (11 / 3) - 1) <= 0.02, f"R_inf = {fa[0]:.5f} (11/3 = {11 / 3:.5f}; a = {fa[1]:.4f}, b = {fa[2]:.4f})")
    verdict("V2b", abs(fb[0] - fa[0]) <= 0.02 * 11 / 3, f"R_inf (alt window) = {fb[0]:.5f}")
    say(f"    V2c (reported): R_V4D(t_max) = {R12[-1] + 2 * RS[-1]:.5f} (10/3 = {10 / 3:.5f}); R_12 + R_S at t_max = {R12[-1] + RS[-1]:.5f} (7/2)")
    # V4
    ccart = richardson(*Yc, H_FD)
    RC = ccart / (ts ** 2 * j0 ** 2)
    say("    R_C(t): " + ", ".join(f"t={t:.0f}: {r:.3e}" for t, r in zip(ts, RC)))
    i12 = int(np.argmin(abs(ts - (12 if not SMOKE else 4))))
    verdict("V4", abs(RC[-1]) <= 0.01 and abs(RC[-1]) <= 0.5 * abs(RC[i12]), f"|R_C(t_max)| = {abs(RC[-1]):.2e}, ratio to t = {ts[i12]:.0f}: {abs(RC[-1] / RC[i12]):.3f}")


if __name__ == "__main__":
    say(f"f9_root_sector.py  start {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} UTC  smoke={SMOKE}")
    for part in (part_g0, part_g1, part_g2_g3, part_v0, part_v124):
        t1 = time.time()
        part()
        say(f"  ({part.__name__}: {time.time() - t1:.1f} s)")
    npass = sum(ok for _, ok in RESULTS)
    say(f"SUMMARY: {npass}/{len(RESULTS)} verdict lines PASS (controls are counted as PASS when they fail as required)")
    say("  " + "; ".join(f"{n}: {'PASS' if ok else 'FAIL'}" for n, ok in RESULTS))
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6
    say(f"end {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} UTC  wall {time.time() - T0:.1f} s  peak RSS {rss:.0f} MB")
