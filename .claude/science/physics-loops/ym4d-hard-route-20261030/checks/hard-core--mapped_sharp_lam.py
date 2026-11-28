#!/usr/bin/env python3
"""Lemma Inv and Theorem F at a constrained minimiser with a non-zero multiplier. Consumer: `library/fibre-propagator.md`.

Written before running. All earlier checks had constant flux, so the multiplier vanished, and Lemma Inv's Lagrange term was never tested.

Field. SU(2), Cartan background, d = 2, one level. Fund phases theta on bonds, U = exp(i theta sigma_3), adjoint phase u = exp(2 i theta). A_C(theta) := sum_p (1 - cos theta_p). Parent phase: theta'(y, mu) = avg over x in B(y) of the fund phase of path_x =: Q_C theta, linear in this sector. Start from theta^0 with flux f_1 cos(2 pi x_1/N) + f_2 cos(2 pi x_2/N) and solve min A_C on { Q_C theta = Q_C theta^0 } by Newton: grad A_C = Q_C^T lambda. Then (U, lambda) is a constrained critical point of the full SU(2) problem, since a Cartan field has no charged first derivative.

Charged fluctuation H. e^{i B} U, B := H sigma_+ + conj(H) sigma_-. Along a path, with legs a in order, h_a := c_a H_{b_a}, the code's coefficients, the holonomy is exp(i (eps sigma_+ + h.c. + kappa sigma_3)) Omega, eps := sum h_a, kappa := - sum_{a<a'} Im(h_a conj h_a'), to second order.

Second-order Cartan phase of the parent, derived by hand before running. With v_x := adjoint phase of Omega_x / Omega_0, A := avg v_x, w := v/2, Psi(w) := (1/2)(cot w - w / sin^2 w), Psi(0) := 0, ell(v) := i v/(e^{i v} - 1), and
 u_ := dexp(A) avg_x ell(v_x) (eps_x - e^{i v_x} eps_0),
 B'_3 = avg_x [ kappa_x + Im(eps_x conj(e^{i v_x} eps_0)) + Psi(w_x) |eps_x - e^{i v_x} eps_0|^2 ] - Psi(A/2) |u_|^2 - Im(u_ conj(e^{i A} eps_0)).

Forms. bK: the true Hessian form on charged bonds, as in `hard-core--mapped_sharp_bg.py`, with local plaquette phases.
 HT[H] := bK[H] - 2 sum_c lambda(c) B'_3(c; H). The Hessian on the true fibre, on ker Q.
 HN[H] := HT[H] + 2 sum_c lambda(c) sum_{i<j} Im(p_i conj p_j), with p_1 := -alpha_y, p_2 := (Q H)(c), p_3 := Omega' alpha_y', alpha := -Phi H. The Hessian bH with the contour-free chain N := e^{-i alpha_y} M e^{i alpha_y'}.

PRE-STATED criteria. (L, nc) = (3, 8), (5, 8). Amplitudes: level-1 adjoint flux a' := L^2 max |adjoint plaquette phase| near 0.1, 0.2, 0.4, and a' = 0 as the reference.
 L0. KKT residual of the Cartan solve <= 1e-10. Ward: ||D'_C^T lambda|| <= 1e-9. Reported: |lambda|_max, and it must be above 1e-4 for a' >= 0.2, otherwise the test has no power.
 L1. Direct control of B'_3: the actual SU(2) block map on e^{i t H} U, t = 2e-3, random H, L = 3, nc = 4 at the same a' range: | (Cartan phase of parent minus base) - t^2 B'_3(c; H) | <= 1e-3 t^2 max|H|^2, for all c, after removing the even part by (+t, -t) and the first-order Cartan part, which is zero.
 L2. Hess on the fibre: ||Z^* HT D omega|| <= 1e-9 ||omega|| for random omega with ev omega = 0, Z a basis of ker Q. Sensitivity: the same with lambda omitted, reported, and it must exceed 1e-6 at a' >= 0.2.
 L3. Lemma Inv, the strong form: ||HN D omega|| <= 1e-9 ||omega||, for random omega in ker r_U, on all bonds, not only on ker Q^o. Sensitivity: the same with the chain's cross term omitted, reported.
 L4. Identification: M^-1 eta by the tree chart with HT and the true Q, against Sad# with HN and Q^o: <= 1e-7. A random source local to a box.
 L5. On that solution ||P_r phi|| <= 1e-8 ||H||.
 L6. lam# := min on ker Q^o of L^2 (HN + ||P_r phi||^2) / (L^2 (||d H||^2 + ||phi||^2) + ||H||^2); lam#(a') >= 0.5 lam#(0).
 L7. Rate of H from S1 := d^dagger e_p, a plaquette at the centre of box 0: rate(a') >= 0.5 rate(0).
FAIL if any fails. L2 failing means the formula for B'_3 is wrong. L3 failing with L2 passing means Lemma Inv is wrong. L4 failing with L2, L3 passing means the identification is wrong.

Limits. d = 2, one level, a smooth non-constant Cartan background; charged directions only. RSS guard 2 GB.
"""
import importlib.util
import os
import resource
import sys

import numpy as np
import scipy.sparse as sp


def rss_gb():
    r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return r / 1024**3 if sys.platform == "darwin" else r / 1024**2


def guard():
    if rss_gb() > 2:
        raise SystemExit("RSS above 2 GB")


HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("sharp_bg", os.path.join(HERE, "hard-core--mapped_sharp_bg.py"))
bg = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bg)
sh = bg.sh
tp = sh.tp
RealBg = tp.Bg


def plaquette_rows(N):
    """Fund plaquette phase as a sparse linear map on bonds."""
    I, J, V = [], [], []
    idx = lambda a, b: (a % N) * N + (b % N)
    for x0 in range(N):
        for x1 in range(N):
            p = idx(x0, x1)
            for b, s in ((idx(x0, x1), 1), (idx(x0 + 1, x1) + N * N, 1), (idx(x0, x1 + 1), -1), (idx(x0, x1) + N * N, -1)):
                I.append(p)
                J.append(b)
                V.append(s)
    return sp.csr_matrix((V, (I, J)), shape=(N * N, 2 * N * N), dtype=float)


def cartan_q(g):
    """Q_C: avg over x of the fund phase of path_x, from Bg.path, as a dense row per parent."""
    N, L, nc, h = g.N, g.L, g.nc, g.h
    nb = 2 * N * N
    Qc = np.zeros((2 * nc * nc, nb))
    for i in range(nc):
        for j in range(nc):
            y0 = (h + L * i, h + L * j)
            for mu in range(2):
                row = np.zeros(nb)
                for r0 in range(-h, h + 1):
                    for r1 in range(-h, h + 1):
                        for (site, nu, sg) in g.path(y0, (y0[0] + r0, y0[1] + r1), mu):
                            row[g.idx(site[0] % N, site[1] % N) + nu * N * N] += sg
                Qc[i * nc + j + mu * nc * nc] = row / L**2
    return Qc


def solve_field(L, nc, ap):
    """Returns the prepared Bg, theta, lambda, residual and Ward residual."""
    g = RealBg(L, nc, 0)
    N = g.N
    nb = 2 * N * N
    # Fund flux target: a' is the level-1 adjoint flux, so the fine fund flux has amplitude a'/(2 L^2) at most.
    f = ap / (2 * L**2) / 2
    th = np.zeros(nb)
    a = np.arange(N)
    amp = f * N / (2 * np.pi)
    for x0 in range(N):
        for x1 in range(N):
            # A_1(x0) gives flux f cos(2 pi x0/N); A_0(x1) gives flux f cos(2 pi x1/N) with the opposite sign of the bond's orientation.
            th[g.idx(x0, x1) + N * N] = amp * np.sin(2 * np.pi * x0 / N)
            th[g.idx(x0, x1)] = -amp * np.sin(2 * np.pi * x1 / N)
    P = plaquette_rows(N)
    Qc = cartan_q(g)
    m = Qc.shape[0]
    lam = np.zeros(m)
    th0 = th.copy()
    for it in range(30):
        tp_ = P @ th
        grad = P.T @ np.sin(tp_)
        res = grad - Qc.T @ lam
        if np.max(np.abs(res)) < 1e-12 and it > 0:
            break
        Hs = (P.T @ sp.diags(np.cos(tp_)) @ P).toarray()
        S = np.zeros((nb + m, nb + m))
        S[:nb, :nb] = Hs
        S[:nb, nb:] = Qc.T
        S[nb:, :nb] = Qc
        # Newton on (theta, lambda); the Cartan gauge directions are null, and lstsq takes the minimal step.
        sol = np.linalg.lstsq(S, np.concatenate([-res, np.zeros(m)]), rcond=1e-12)[0]
        th += sol[:nb]
        lam += -sol[nb:] if False else sol[nb:] * -1
        guard()
    tp_ = P @ th
    res = np.max(np.abs(P.T @ np.sin(tp_) - Qc.T @ lam))
    # Coarse gradient in the Cartan sector.
    Dc = np.zeros((m, nc * nc))
    for ci in range(nc * nc):
        i, j = ci // nc, ci % nc
        for mu in range(2):
            ni, nj = (i + (mu == 0)) % nc, (j + (mu == 1)) % nc
            Dc[ci + mu * nc * nc, ci] -= 1
            Dc[ci + mu * nc * nc, ni * nc + nj] += 1
    ward = np.linalg.norm(Dc.T @ lam)
    parent = np.max(np.abs(Qc @ (th - th0)))
    g.u = np.zeros((2, N, N), dtype=complex)
    for x0 in range(N):
        for x1 in range(N):
            for mu in range(2):
                g.u[mu, x0, x1] = np.exp(2j * th[g.idx(x0, x1) + mu * N * N])
    g.theta = 0.0
    g.th_fund = th
    return g, lam, res, ward, parent, float(np.max(np.abs(2 * tp_))) * L**2


def Psi(w):
    if abs(w) < 1e-6:
        return -w / 3
    return 0.5 * (1 / np.tan(w) - w / np.sin(w) ** 2)


def legs(g, y0, x, mu):
    """Ordered (bond, coefficient) along path_x, and the adjoint holonomy."""
    N = g.N
    out = []
    om = 1.0 + 0j
    for (site, nu, sg) in g.path(y0, x, mu):
        s0, s1 = site[0] % N, site[1] % N
        b = g.idx(s0, s1) + nu * N * N
        if sg > 0:
            out.append((b, om))
            om = om * g.u[nu, s0, s1]
        else:
            om = om * np.conj(g.u[nu, s0, s1])
            out.append((b, -om))
    return out, om


def im_form(a, b):
    """Hermitian matrix of Im(alpha conj beta), alpha = a^T H, beta = b^T H, as dict-free dense on the support."""
    return (np.outer(b.conj(), a) - np.outer(a.conj(), b)) / (2j)


def sq_form(a):
    return np.outer(a.conj(), a)


def parent_form(g, y0, mu):
    """Returns (support, matrix of B'_3 on the support, row u_, rows eps_0)."""
    h = g.h
    data = {}
    bonds = set()
    for r0 in range(-h, h + 1):
        for r1 in range(-h, h + 1):
            lg, om = legs(g, y0, (y0[0] + r0, y0[1] + r1), mu)
            data[(r0, r1)] = (lg, om)
            bonds.update(b for b, _ in lg)
    sup = np.array(sorted(bonds))
    pos = {b: i for i, b in enumerate(sup.tolist())}
    n = len(sup)

    def eps_row(lg):
        v = np.zeros(n, dtype=complex)
        for b, c in lg:
            v[pos[b]] += c
        return v

    om0 = data[(0, 0)][1]
    e0 = eps_row(data[(0, 0)][0])
    M = np.zeros((n, n), dtype=complex)
    vs = {}
    avgrow = np.zeros(n, dtype=complex)
    for k, (lg, om) in data.items():
        vs[k] = np.angle(om / om0)
    A = float(np.mean(list(vs.values())))
    cnt = len(data)
    for k, (lg, om) in data.items():
        v = vs[k]
        ex = eps_row(lg)
        # kappa_x
        Kx = np.zeros((n, n), dtype=complex)
        cs = [(pos[b], c) for b, c in lg]
        for a_i in range(len(cs)):
            ia, ca = cs[a_i]
            for b_i in range(a_i + 1, len(cs)):
                ib, cb = cs[b_i]
                # -Im(h_a conj h_b) = (i/2)(c_a conj(c_b) H_a conj(H_b) - conj(c_a) c_b conj(H_a) H_b)
                Kx[ia, ib] += -0.5j * np.conj(ca) * cb
                Kx[ib, ia] += 0.5j * ca * np.conj(cb)
        e0v = np.exp(1j * v) * e0
        M += Kx + im_form(ex, e0v) + Psi(v / 2) * sq_form(ex - e0v)
        ell = 1.0 if abs(v) < 1e-12 else 1j * v / (np.exp(1j * v) - 1)
        avgrow += ell * (ex - e0v)
    M /= cnt
    avgrow /= cnt
    dex = 1.0 if abs(A) < 1e-12 else (np.exp(1j * A) - 1) / (1j * A)
    u_ = dex * avgrow
    M = M - Psi(A / 2) * sq_form(u_) - im_form(u_, np.exp(1j * A) * e0)
    return sup, M, u_, e0


def lagrange(g, lam, Q, Dc, Phi):
    """Returns sparse matrices: LT := sum lambda(c) B'_3 and LC := sum lambda(c) sum_{i<j} Im(p_i conj p_j)."""
    N, L, nc, h = g.N, g.L, g.nc, g.h
    nb = 2 * N * N
    IT, JT, VT = [], [], []
    LC = np.zeros((nb, nb), dtype=complex)
    for i in range(nc):
        for j in range(nc):
            y0 = (h + L * i, h + L * j)
            ci = i * nc + j
            for mu in range(2):
                c = ci + mu * nc * nc
                sup, M, _, _ = parent_form(g, y0, mu)
                lc = lam[c]
                ii, jj = np.meshgrid(sup, sup, indexing="ij")
                IT.append(ii.ravel())
                JT.append(jj.ravel())
                VT.append((lc * M).ravel())
                ni, nj = (i + (mu == 0)) % nc, (j + (mu == 1)) % nc
                cn = ni * nc + nj
                om_p = Dc[c, cn]
                p1 = Phi[ci, :]  # -alpha_y = Phi H
                p2 = Q[c, :]
                p3 = -om_p * Phi[cn, :]  # Omega' alpha_y' = -Omega' Phi H
                LC += lc * (im_form(p1, p2) + im_form(p1, p3) + im_form(p2, p3))
    LT = sp.csr_matrix((np.concatenate(VT), (np.concatenate(IT), np.concatenate(JT))), shape=(nb, nb), dtype=complex)
    return LT, LC


def setup(L, nc, ap):
    g, lam, res, ward, parent, ap_real = solve_field(L, nc, ap)
    tp.Bg = lambda L_, nc_, m_: g
    try:
        out = sh.build_sharp(L, nc, 0)
    finally:
        tp.Bg = RealBg
    return (g, lam, res, ward, parent, ap_real) + tuple(out[1:])


def control_l1(L, nc, ap, rng):
    g, lam, res, ward, parent, ap_real = solve_field(L, nc, ap)
    N = g.N
    th = g.th_fund
    nb = 2 * N * N
    H = rng.standard_normal(nb) + 1j * rng.standard_normal(nb)
    t = 2e-3

    def su2_link(b, sign):
        al = th[b]
        U = np.array([[np.exp(1j * al), 0], [0, np.exp(-1j * al)]], dtype=complex)
        h_ = H[b] * t * sign
        B = np.array([[0, h_], [np.conj(h_), 0]], dtype=complex)
        return bg.expm_su2(B) @ U

    def parent_phase(y0, mu, sign):
        """Actual log-average block map, on 2 x 2 matrices. Cartan component of the parent, relative to the bare one."""
        h = g.h
        paths = {}
        for r0 in range(-h, h + 1):
            for r1 in range(-h, h + 1):
                P_ = np.eye(2, dtype=complex)
                for (site, nu, sg) in g.path(y0, (y0[0] + r0, y0[1] + r1), mu):
                    s0, s1 = site[0] % N, site[1] % N
                    Ub = su2_link(g.idx(s0, s1) + nu * N * N, sign)
                    P_ = P_ @ (Ub if sg > 0 else Ub.conj().T)
                paths[(r0, r1)] = P_
        O0 = paths[(0, 0)]
        S = np.zeros((2, 2), dtype=complex)
        for k, P_ in paths.items():
            Z = P_ @ O0.conj().T
            w_, v_ = np.linalg.eig(Z)
            S += (v_ * np.log(w_)) @ np.linalg.inv(v_)
        S /= len(paths)
        w_, v_ = np.linalg.eig(S)
        V = ((v_ * np.exp(w_)) @ np.linalg.inv(v_)) @ O0
        return V

    def bare(y0, mu):
        h = g.h
        phases = []
        for r0 in range(-h, h + 1):
            for r1 in range(-h, h + 1):
                s = 0.0
                for (site, nu, sg) in g.path(y0, (y0[0] + r0, y0[1] + r1), mu):
                    s += sg * th[g.idx(site[0] % N, site[1] % N) + nu * N * N]
                phases.append(s)
        return float(np.mean(phases))

    worst = 0.0
    for i in range(nc):
        for j in range(nc):
            y0 = (g.h + g.L * i, g.h + g.L * j)
            for mu in range(2):
                b0 = bare(y0, mu)
                sup, M, _, _ = parent_form(g, y0, mu)
                form = (H[sup].conj() @ (M @ H[sup])).real
                tot = 0.0
                for sign in (1, -1):
                    V = parent_phase(y0, mu, sign)
                    # V = exp(i B') exp(i b0 sigma_3). Cartan part of B', from the log of V exp(-i b0 sigma_3).
                    Z = V @ np.array([[np.exp(-1j * b0), 0], [0, np.exp(1j * b0)]])
                    w_, v_ = np.linalg.eig(Z)
                    Lg = (v_ * np.log(w_)) @ np.linalg.inv(v_)
                    tot += (Lg[0, 0] / 1j).real
                val = tot / 2 / t**2
                worst = max(worst, abs(val - form))
    return worst, float(np.max(np.abs(H)) ** 2)


def run_case(L, nc, ap, rng):
    g, lam, res, ward, parent, ap_real, D, d, Q, Qo, Dc, ev, r, Phi, Pr, centres = setup(L, nc, ap)
    N = g.N
    nb = 2 * N * N
    bK = bg.true_hessian(g)
    LT, LC = lagrange(g, lam, Q, Dc, Phi)
    HT = bK.toarray() - 2 * LT.toarray()
    HN = HT + 2 * LC
    herm = np.linalg.norm(HN - HN.conj().T)
    guard()
    # L2.
    idx_c = [g.idx(*y) for y in centres]
    om = rng.standard_normal(N**2) + 1j * rng.standard_normal(N**2)
    om[idx_c] = 0
    Z = sh.null_basis(Q)
    Dom = D @ om
    l2 = np.linalg.norm(Z.conj().T @ (HT @ Dom)) / np.linalg.norm(om)
    l2s = np.linalg.norm(Z.conj().T @ (bK @ Dom)) / np.linalg.norm(om)
    guard()
    # L3.
    om2 = rng.standard_normal(N**2) + 1j * rng.standard_normal(N**2)
    om2 = Pr @ om2
    Dom2 = D @ om2
    l3 = np.linalg.norm(HN @ Dom2) / np.linalg.norm(om2)
    l3s = np.linalg.norm(HT @ Dom2) / np.linalg.norm(om2)
    # L4.
    tree = tp.comb_bonds(g)
    keep = np.setdiff1d(np.arange(nb), tree)
    kset = set(keep.tolist())
    box = [g.idx(g.h + r0, g.h + r1) + mu * N * N for r0 in range(-g.h, g.h + 1) for r1 in range(-g.h, g.h + 1) for mu in range(2) if g.idx(g.h + r0, g.h + r1) + mu * N * N in kset]
    eta = np.zeros(nb, dtype=complex)
    eta[box] = rng.standard_normal(len(box)) + 1j * rng.standard_normal(len(box))
    n1, m1 = len(keep), Q.shape[0]
    S = np.zeros((n1 + m1, n1 + m1), dtype=complex)
    S[:n1, :n1] = HT[np.ix_(keep, keep)]
    S[:n1, n1:] = Q[:, keep].conj().T
    S[n1:, :n1] = Q[:, keep]
    sol = np.linalg.solve(S, np.concatenate([eta[keep], np.zeros(m1)]))
    del S
    xi_tree = np.zeros(nb, dtype=complex)
    xi_tree[keep] = sol[:n1]
    free_sites = np.setdiff1d(np.arange(N * N), idx_c)
    Dfs = D[:, free_sites]
    Gt = np.linalg.solve(Dfs[tree, :], np.eye(len(tree), dtype=complex))
    evd = ev.conj().T

    def xi_of(v):
        v2 = v - D @ (evd @ (Phi @ v))
        return v2 - Dfs @ (Gt @ v2[tree])

    def xi_adj(u_):
        u2 = u_.copy()
        u2[tree] -= Gt.conj().T @ (Dfs.conj().T @ u_)
        return u2 - Phi.conj().T @ (evd.conj().T @ (D.conj().T @ u2))

    J = xi_adj(eta)
    Ks = HN + D @ Pr @ D.conj().T
    S2 = np.zeros((nb + m1, nb + m1), dtype=complex)
    S2[:nb, :nb] = Ks
    S2[:nb, nb:] = Qo.conj().T
    S2[nb:, :nb] = Qo
    H = np.linalg.solve(S2, np.concatenate([J, np.zeros(m1)]))[:nb]
    xi_sh = xi_of(H)
    l4 = np.linalg.norm(xi_tree - xi_sh) / np.linalg.norm(xi_tree)
    l5 = np.linalg.norm(Pr @ (D.conj().T @ H)) / np.linalg.norm(H)
    guard()
    # L7.
    e_p = np.zeros(N * N, dtype=complex)
    e_p[g.idx(g.h, g.h)] = 1
    J1 = d.conj().T @ e_p
    H1 = np.linalg.solve(S2, np.concatenate([J1, np.zeros(m1)]))[:nb]
    del S2
    prof = bg.box_profile(g, H1, nc)
    guard()
    # L6.
    Z2 = sh.null_basis(Qo)
    pZ = D.conj().T @ Z2
    A = L**2 * (Z2.conj().T @ (HN @ Z2) + pZ.conj().T @ (Pr @ pZ))
    dZ = d @ Z2
    B = L**2 * (dZ.conj().T @ dZ + pZ.conj().T @ pZ) + np.eye(Z2.shape[1])
    A, B = 0.5 * (A + A.conj().T), 0.5 * (B + B.conj().T)
    Ci = np.linalg.inv(np.linalg.cholesky(B))
    lm = float(np.linalg.eigvalsh(Ci @ A @ Ci.conj().T)[0])
    guard()
    return dict(res=res, ward=ward, parent=parent, ap=ap_real, lam=float(np.max(np.abs(lam))), herm=herm, l2=l2, l2s=l2s, l3=l3, l3s=l3s, l4=l4, l5=l5, lm=lm, prof=prof)


def main():
    ok = True
    rng = np.random.default_rng(211)

    print("L1", flush=True)
    for ap in (0.2, 0.4):
        worst, hm = control_l1(3, 4, ap, rng)
        good = worst <= 1e-3 * hm * 1.0
        ok = ok and good
        print(f" L1 L=3 nc=4 a'~{ap}: worst difference per t^2 {worst:.2e}, max|H|^2 {hm:.2f}: {good}", flush=True)

    print("Cases", flush=True)
    for L, nc in ((3, 8), (5, 8)):
        base = None
        for ap in (0.0, 0.1, 0.2, 0.4):
            r_ = run_case(L, nc, ap, rng)
            rt = sh.rate_of(r_["prof"])
            if base is None:
                base = (r_["lm"], rt)
            good = r_["res"] <= 1e-10 and r_["ward"] <= 1e-9 and r_["l2"] <= 1e-9 and r_["l3"] <= 1e-9 and r_["l4"] <= 1e-7 and r_["l5"] <= 1e-8 and r_["lm"] >= 0.5 * base[0] and rt >= 0.5 * base[1]
            if ap >= 0.2:
                good = good and r_["lam"] > 1e-4 and r_["l2s"] > 1e-6
            ok = ok and good
            print(f" L={L} nc={nc} a'={r_['ap']:.3f}: res={r_['res']:.1e} ward={r_['ward']:.1e} parent={r_['parent']:.1e} lam={r_['lam']:.2e} herm={r_['herm']:.1e} L2={r_['l2']:.1e} (no lam {r_['l2s']:.1e}) L3={r_['l3']:.1e} (no cross {r_['l3s']:.1e}) L4={r_['l4']:.1e} L5={r_['l5']:.1e} lam#={r_['lm']:.4f} rate={rt:.3f} {[f'{v:.1e}' for v in r_['prof']]}: {good} rss={rss_gb():.2f}GB", flush=True)

    print("PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
