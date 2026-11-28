#!/usr/bin/env python3
"""The fibre problem at flux with the true Hessian, and with a frozen exterior. Consumer: `library/fibre-propagator.md`.

Written before running, after `hard-core--mapped_sharp.py` failed A1, A2 at m != 0 and passed everything else. Diagnosis to be tested here: ||d_U H||^2 is not gauge invariant at flux, since d_U D_U omega = [F, omega]. So D omega is not a null direction of d^dagger d, and the two problems differ. The true Hessian of the Wilson action at a critical background has D omega as a null direction, by differentiating gauge invariance.

True Hessian on charged components at a Cartan background. Plaquette base x, legs h_1 := H_0(x), h_2 := u_0(x) H_1(x + e_0), h_3 := -e^{i t} u_1(x) H_0(x + e_1), h_4 := -e^{i t} H_1(x), with e^{i t} the adjoint plaquette phase and alpha := t/2. With y := sum h_i, expanding Re tr[e^{i H_1} ... e^{i H_4} Phi] to second order, H_i := h_i sigma_+ + conj(h_i) sigma_-:
 2 x (second-order part of 1 - (1/2) Re tr) = cos(alpha) |y|^2 - 2 sin(alpha) sum_{i<j} Im(h_i conj(h_j)).
Call this form bK. At alpha = 0 it is |d H|^2.

PRE-STATED criteria.

Part T, controls.
 T0. ||bK D omega|| <= 1e-10 ||omega|| at m = 0, 1, 2, L = 3, 5, random omega.
 T1. Finite difference of the SU(2) Wilson action at the even flux m = 2, L = 3, nc = 2, with fundamental links from u: relative error of the second difference against bK, at t = 1e-3, random charged H: <= 1e-4.
FAIL if T0 or T1 fails: the formula would be wrong.

Part A', the identification at flux. As A0-A2 of the earlier check, with bK in place of d^dagger d in both the tree-gauge system and Sad#. L = 3, 5, nc = 4, m = 0, 1, 2. Thresholds: A1' <= 1e-7, A2' <= 1e-8.
FAIL if either fails: the diagnosis would be wrong, and the class identification at flux false.

Part D', coercivity and rate with bK. L = 3, nc = 12, m = 0, 1, 2, 4, 8; L = 5, nc = 8, m = 0, 1, 2, 4.
 lam#t(m) := min on ker Q^o of L^2 (bK + ||P_r phi||^2) / (L^2 (||d H||^2 + ||phi||^2) + ||H||^2). Rate of H from S1 := d^dagger e_p.
 D1'. lam#t(m) >= 0.5 lam#t(0) for a' <= 0.2.
 D2'. rate >= 0.5 rate(0) for a' <= 0.2.
 Larger a' reported with no criterion.

Part E, a frozen exterior, d = 2, real space. Boxes with first index in 0..w-1 are Y, the others Omega. Free bonds: at least one end in Y. Constraints: Q^o rows with support on free bonds. Gauge: omega on Y sites only, with r omega = 0 on Y blocks. P_N := that projector. This is the Dirichlet problem of the consumer's shell, at level k = 0.
 Parameters (L, nc, w), m = 0: (3, 8, 5), (5, 6, 4), (7, 6, 4), (9, 6, 4). At flux: (3, 8, 5) with m = 1, 2; (5, 6, 4) with m = 1.
 E1. Identification: M_Y^-1 eta by tree gauge on Y, against Sad#_N, as A1: <= 1e-7.
 E2. Control P_N: on the Sad#_N solution, ||P_N phi|| <= 1e-8 ||H||.
 E3. cn(L) := min on the constraint space of L^2 (bK + ||P_N phi||^2) / ||H||^2. This is the L^2 coercivity with no H^1 norm. cn(L) >= 0.5 cn(3), m = 0; cn(m) >= 0.5 cn(0) at flux.
 E4. Rate across the strip. Source: a free bond next to the inner wall. A(D) := largest l^2 norm of xi on a box of first index D, D = 1 .. w - 1; the slope of -log A. rate >= 0.7, and >= 0.5 rate(L = 3).
 E5. Rate along the wall, from the same source: boxes of first index 0, second index distance D, up to nc/2 - 1. Same thresholds.
 FAIL if any fails. E3 failing would mean that the frozen problem has L-dependent coercivity, and that the rate near a wall is not proved by this route.

Part F, a frozen exterior at the trivial background, d = 3, 4, with Bloch sums in the directions along the wall. d = 3: L = 3, 5 with w = 4, L = 7 with w = 3 (memory); d = 4: L = 3, w = 4. Momenta along the wall: a short list.
 F1. cn(L) := min over the list of cn(p) as in E3. cn(L) >= 0.5 cn(3), and >= 0.02 in level-1 units.
 F2. Across rate of H in the gauge P_N phi = 0, from the source d^dagger e_p next to the inner wall, at each listed momentum: the smallest is >= 0.7, and >= 0.5 of the value at L = 3.
FAIL if F1 or F2 fails.

Limitations: one level, k = 0; constant flux; flat walls only; no re-entrant corner; d = 3, 4 at the trivial background only. RSS guard 2 GB.
"""
import importlib.util
import itertools
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
spec = importlib.util.spec_from_file_location("sharp", os.path.join(HERE, "hard-core--mapped_sharp.py"))
sh = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sh)
tp = sh.tp


def true_hessian(g):
    N = g.N
    nb = 2 * N * N
    I, J, V = [], [], []
    for x0 in range(N):
        for x1 in range(N):
            xp0, xp1 = (x0 + 1) % N, (x1 + 1) % N
            u0, u1 = g.u[0, x0, x1], g.u[1, x0, x1]
            eit = u0 * g.u[1, xp0, x1] * np.conj(g.u[0, x0, xp1]) * np.conj(u1)
            al = np.angle(eit) / 2
            bonds = [g.idx(x0, x1), g.idx(xp0, x1) + N * N, g.idx(x0, xp1), g.idx(x0, x1) + N * N]
            cs = [1.0 + 0j, u0, -eit * u1, -eit]
            ca, sa = np.cos(al), np.sin(al)
            for i in range(4):
                for j in range(4):
                    I.append(bonds[i])
                    J.append(bonds[j])
                    V.append(ca * np.conj(cs[i]) * cs[j])
            # -2 sin(al) sum_{i<j} Im(h_i conj h_j): matrix element H-bar_i H_j gets -i s conj(c_i) c_j, and H-bar_j H_i gets +i s conj(c_j) c_i, i < j.
            for i in range(4):
                for j in range(i + 1, 4):
                    I.append(bonds[i])
                    J.append(bonds[j])
                    V.append(-1j * sa * np.conj(cs[i]) * cs[j])
                    I.append(bonds[j])
                    J.append(bonds[i])
                    V.append(1j * sa * np.conj(cs[j]) * cs[i])
    return sp.csr_matrix((V, (I, J)), shape=(nb, nb), dtype=complex)


def wilson(links):
    """links: dict-free array (2, N, N, 2, 2) of SU(2) matrices. Sum over plaquettes of 1 - (1/2) Re tr."""
    N = links.shape[1]
    s = 0.0
    for x0 in range(N):
        for x1 in range(N):
            a = links[0, x0, x1]
            b = links[1, (x0 + 1) % N, x1]
            c = links[0, x0, (x1 + 1) % N].conj().T
            d = links[1, x0, x1].conj().T
            s += 1 - 0.5 * np.trace(a @ b @ c @ d).real
    return s


def expm_su2(B):
    """exp(i B) for Hermitian traceless 2 x 2."""
    w, v = np.linalg.eigh(B)
    return (v * np.exp(1j * w)) @ v.conj().T


def control_t1(L, nc, m, rng):
    g = tp.Bg(L, nc, m)
    N = g.N
    K = true_hessian(g)
    nb = 2 * N * N
    H = rng.standard_normal(nb) + 1j * rng.standard_normal(nb)
    H /= np.linalg.norm(H)
    t = 1e-3
    fund = np.zeros((2, N, N, 2, 2), dtype=complex)
    sq = np.exp(0.5j * np.angle(g.u))
    # Fundamental phases from the adjoint phases, keeping the plaquette half-angle small: at even m this is periodic.
    theta = g.theta
    a = np.arange(N)
    ca = np.where(a < N // 2, a, a - N)
    for x0 in range(N):
        for x1 in range(N):
            ph1 = np.exp(0.5j * theta * ca[x0])
            ph0 = np.exp(-0.5j * theta * N * x1) if x0 == N // 2 - 1 else 1.0
            sq[0, x0, x1], sq[1, x0, x1] = ph0, ph1
            fund[0, x0, x1] = np.diag([ph0, np.conj(ph0)])
            fund[1, x0, x1] = np.diag([ph1, np.conj(ph1)])
    chk = np.max(np.abs(sq**2 - g.u))

    def field(sign):
        out = np.zeros_like(fund)
        for mu in range(2):
            for x0 in range(N):
                for x1 in range(N):
                    h = H[g.idx(x0, x1) + mu * N * N] * t * sign
                    B = np.array([[0, h], [np.conj(h), 0]], dtype=complex)
                    out[mu, x0, x1] = expm_su2(B) @ fund[mu, x0, x1]
        return out

    A0, Ap, Am = wilson(fund), wilson(field(1)), wilson(field(-1))
    second = (Ap + Am - 2 * A0) / t**2
    # A(t) = A0 + t^2 * (second-order part), so second = 2 (second-order part) = H^dagger bK H.
    form = (H.conj() @ (K @ H)).real
    return abs(second - form) / abs(form), chk


def part_a_true(L, nc, m, rng):
    g, D, d, Q, Qo, Dc, ev, r, Phi, Pr, centres = sh.build_sharp(L, nc, m)
    N = g.N
    nb = 2 * N * N
    K = true_hessian(g)
    om = rng.standard_normal(N**2) + 1j * rng.standard_normal(N**2)
    t0 = np.linalg.norm(K @ (D @ om)) / np.linalg.norm(om)
    tree = tp.comb_bonds(g)
    keep = np.setdiff1d(np.arange(nb), tree)
    kset = set(keep.tolist())
    box = [g.idx(g.h + r0, g.h + r1) + mu * N * N for r0 in range(-g.h, g.h + 1) for r1 in range(-g.h, g.h + 1) for mu in range(2) if g.idx(g.h + r0, g.h + r1) + mu * N * N in kset]
    eta = np.zeros(nb, dtype=complex)
    eta[box] = rng.standard_normal(len(box)) + 1j * rng.standard_normal(len(box))
    Kff = K[keep][:, keep].toarray()
    Qf = Q[:, keep]
    n1, m1 = Kff.shape[0], Qf.shape[0]
    S = np.zeros((n1 + m1, n1 + m1), dtype=complex)
    S[:n1, :n1] = Kff
    S[:n1, n1:] = Qf.conj().T
    S[n1:, :n1] = Qf
    sol = np.linalg.lstsq(S, np.concatenate([eta[keep], np.zeros(m1)]), rcond=1e-12)[0]
    xi_tree = np.zeros(nb, dtype=complex)
    xi_tree[keep] = sol[:n1]
    idx_c = [g.idx(*y) for y in centres]
    free_sites = np.setdiff1d(np.arange(N * N), idx_c)
    Gt = np.linalg.solve(D[tree, :][:, free_sites], np.eye(len(tree), dtype=complex))
    Om = np.zeros((N * N, len(tree)), dtype=complex)
    Om[free_sites, :] = Gt
    TreeProj = np.eye(nb, dtype=complex) - D @ Om @ np.eye(nb, dtype=complex)[tree, :]
    Tilde = np.eye(nb, dtype=complex) - D @ (ev.conj().T @ Phi)
    Xi = TreeProj @ Tilde
    J = Xi.conj().T @ eta
    Ks = K.toarray() + D @ Pr @ D.conj().T
    S2 = np.zeros((nb + m1, nb + m1), dtype=complex)
    S2[:nb, :nb] = Ks
    S2[:nb, nb:] = Qo.conj().T
    S2[nb:, :nb] = Qo
    H = np.linalg.lstsq(S2, np.concatenate([J, np.zeros(m1)]), rcond=1e-12)[0][:nb]
    xi_sharp = Xi @ H
    a1 = np.linalg.norm(xi_tree - xi_sharp) / np.linalg.norm(xi_tree)
    a2 = np.linalg.norm(Pr @ (D.conj().T @ H)) / np.linalg.norm(H)
    guard()
    return t0, a1, a2


def lam_true(L, nc, m):
    g, D, d, Q, Qo, Dc, ev, r, Phi, Pr, centres = sh.build_sharp(L, nc, m)
    K = true_hessian(g)
    Z = sh.null_basis(Qo)
    guard()
    pZ = D.conj().T @ Z
    A = L**2 * (Z.conj().T @ (K @ Z) + pZ.conj().T @ (Pr @ pZ))
    dZ = d @ Z
    B = L**2 * (dZ.conj().T @ dZ + pZ.conj().T @ pZ) + np.eye(Z.shape[1])
    A, B = 0.5 * (A + A.conj().T), 0.5 * (B + B.conj().T)
    Ci = np.linalg.inv(np.linalg.cholesky(B))
    w = np.linalg.eigvalsh(Ci @ A @ Ci.conj().T)
    # Rate from S1.
    nb = 2 * g.N**2
    e_p = np.zeros(g.N**2, dtype=complex)
    e_p[g.idx(g.h, g.h)] = 1
    J = d.conj().T @ e_p
    m1 = Qo.shape[0]
    S = np.zeros((nb + m1, nb + m1), dtype=complex)
    S[:nb, :nb] = K.toarray() + D @ Pr @ D.conj().T
    S[:nb, nb:] = Qo.conj().T
    S[nb:, :nb] = Qo
    H = np.linalg.solve(S, np.concatenate([J, np.zeros(m1)]))[:nb]
    prof = box_profile(g, H, nc)
    guard()
    return float(w[0]), prof


def box_profile(g, H, nc):
    N, L = g.N, g.L
    a = np.arange(N)
    AA, BB = np.meshgrid(a, a, indexing="ij")
    boxes = np.stack([AA // L, BB // L], axis=-1).reshape(-1, 2)
    bb = np.vstack([boxes, boxes])
    idx = bb[:, 0] * nc + bb[:, 1]
    norms = np.bincount(idx, weights=np.abs(H) ** 2, minlength=nc * nc)
    bx = np.array(np.unravel_index(np.arange(nc * nc), (nc, nc))).T
    dd = np.minimum(bx, nc - bx).max(axis=1)
    return [float(np.sqrt(norms[dd == k].max())) for k in range(nc // 2 + 1)]


def solve_or_lstsq(S, rhs):
    x = np.linalg.solve(S, rhs)
    res = np.linalg.norm(S @ x - rhs) / np.linalg.norm(rhs)
    if res > 1e-8:
        x = np.linalg.lstsq(S, rhs, rcond=1e-12)[0]
    return x


def part_e(L, nc, w, m, rng):
    g, D, d, Q, Qo, Dc, ev, r, Phi, Pr, centres = sh.build_sharp(L, nc, m)
    del d, Dc, r
    N = g.N
    K = true_hessian(g)
    in_y = np.zeros(N * N, dtype=bool)
    for x0 in range(N):
        for x1 in range(N):
            if x0 // L < w:
                in_y[g.idx(x0, x1)] = True
    free = []
    for x0 in range(N):
        for x1 in range(N):
            for mu in range(2):
                a = g.idx(x0, x1)
                b = g.idx(x0 + (mu == 0), x1 + (mu == 1))
                if in_y[a] or in_y[b]:
                    free.append(a + mu * N * N)
    free = np.array(sorted(free))
    fset = set(free.tolist())
    pos = {b: i for i, b in enumerate(free.tolist())}
    nf = len(free)
    Ky = K[free][:, free].toarray()
    del K
    Dy = D[free, :]
    del D
    y_sites = np.where(in_y)[0]
    # Projector on { omega on Y sites, r omega = 0 on Y blocks }: P_r restricted to Y sites; blocks are disjoint and wholly in Y or Omega.
    PNy = Pr[np.ix_(y_sites, y_sites)]
    del Pr
    Dyy = Dy[:, y_sites]
    keep_rows = np.where(np.max(np.abs(Qo[:, free]), axis=1) > 1e-12)[0]
    Qoy = Qo[keep_rows][:, free]
    del Qo
    keep_rows_t = np.where(np.max(np.abs(Q[:, free]), axis=1) > 1e-12)[0]
    Qy = Q[keep_rows_t][:, free]
    del Q
    Phiy = Phi[:, free]
    guard()
    # Tree gauge on Y.
    y_centres = [g.idx(*c) for c in centres if in_y[g.idx(*c)]]
    tree_all = tp.comb_bonds(g)
    tree = np.array([b for b in tree_all.tolist() if b in fset and in_y[(b % (N * N))] and bond_other_in_y(g, b, in_y)])
    tset = set(tree.tolist())
    keep = np.array([i for i, b in enumerate(free.tolist()) if b not in tset])
    tree_pos = np.array([pos[b] for b in tree.tolist()])
    free_sites = np.setdiff1d(y_sites, y_centres)
    Dfs = Dy[:, free_sites]
    Gt = np.linalg.solve(Dfs[tree_pos, :], np.eye(len(tree), dtype=complex))
    evd = ev.conj().T

    def xi_of(v):
        """Tree-gauge free bonds of H~, from a bond field v on free bonds."""
        v2 = v - Dy @ (evd @ (Phiy @ v))
        return v2 - Dfs @ (Gt @ v2[tree_pos])

    def xi_adj(u):
        u2 = u.copy()
        u2[tree_pos] -= Gt.conj().T @ (Dfs.conj().T @ u)
        return u2 - Phiy.conj().T @ (evd.conj().T @ (Dy.conj().T @ u2))

    # Source: a non-tree free bond next to the inner wall, inside box (0, nc // 2).
    src = None
    for x1 in range(g.L * (nc // 2), g.L * (nc // 2) + g.L):
        for mu in (0, 1):
            b = g.idx(0, x1) + mu * N * N
            if b in fset and b not in tset:
                src = pos[b]
                break
        if src is not None:
            break
    eta = np.zeros(nf, dtype=complex)
    eta[src] = 1
    n1, m1 = len(keep), Qy.shape[0]
    S = np.zeros((n1 + m1, n1 + m1), dtype=complex)
    S[:n1, :n1] = Ky[np.ix_(keep, keep)]
    S[:n1, n1:] = Qy[:, keep].conj().T
    S[n1:, :n1] = Qy[:, keep]
    sol = solve_or_lstsq(S, np.concatenate([eta[keep], np.zeros(m1)]))
    del S
    xi_tree = np.zeros(nf, dtype=complex)
    xi_tree[keep] = sol[:n1]
    guard()
    Ks = Ky + Dyy @ PNy @ Dyy.conj().T
    del Ky
    J = xi_adj(eta)
    m2 = Qoy.shape[0]
    S2 = np.zeros((nf + m2, nf + m2), dtype=complex)
    S2[:nf, :nf] = Ks
    S2[:nf, nf:] = Qoy.conj().T
    S2[nf:, :nf] = Qoy
    H = solve_or_lstsq(S2, np.concatenate([J, np.zeros(m2)]))[:nf]
    del S2
    xi_sharp = xi_of(H)
    e1 = np.linalg.norm(xi_tree - xi_sharp) / np.linalg.norm(xi_tree)
    e2 = np.linalg.norm(PNy @ (Dyy.conj().T @ H)) / np.linalg.norm(H)
    del Dy, Dfs, Dyy, Gt, Phiy, PNy
    guard()
    # Coercivity on the constraint space.
    Z = sh.null_basis(Qoy)
    guard()
    A = L**2 * (Z.conj().T @ (Ks @ Z))
    del Z, Ks
    A = 0.5 * (A + A.conj().T)
    cn = float(np.linalg.eigvalsh(A)[0])
    guard()
    # Profiles of xi from the tree-gauge solution.
    nz = {}
    for i, b in enumerate(free.tolist()):
        site = b % (N * N)
        x0, x1 = site // N, site % N
        k = (x0 // L, x1 // L)
        nz[k] = nz.get(k, 0.0) + abs(xi_tree[i]) ** 2
    across = [np.sqrt(max(v for k, v in nz.items() if k[0] == D)) for D in range(w)]
    i1 = nc // 2
    along = []
    for D in range(nc // 2):
        vals = [v for k, v in nz.items() if k[0] == 0 and min((k[1] - i1) % nc, (i1 - k[1]) % nc) == D]
        along.append(np.sqrt(max(vals)))
    return e1, e2, cn, across, along


def bond_other_in_y(g, b, in_y):
    N = g.N
    site = b % (N * N)
    mu = b // (N * N)
    x0, x1 = site // N, site % N
    return bool(in_y[g.idx(x0 + (mu == 0), x1 + (mu == 1))])


def slope(prof, lo=1, hi=None):
    hi = len(prof) if hi is None else hi
    ds = [k for k in range(lo, hi) if prof[k] > 1e-11 * max(prof)]
    if len(ds) < 2:
        return float("nan")
    return float(np.polyfit(ds, -np.log([prof[k] for k in ds]), 1)[0])


class Strip:
    """Trivial background, frozen exterior across axis 0, Bloch in the other axes. Coarse boxes 0 .. w - 1 of first index in Y.
    Fine sites: x_0 in -1 .. w L (the two outer layers are Omega sites touched by free bonds), x_perp in {0 .. L - 1}^(d-1)."""

    def __init__(self, d, L, w):
        self.d, self.L, self.w, self.h = d, L, w, (L - 1) // 2
        self.perp = list(itertools.product(range(L), repeat=d - 1))
        self.np = len(self.perp)
        self.pindex = {s: i for i, s in enumerate(self.perp)}
        self.x0s = list(range(-1, w * L + 1))
        self.n0 = len(self.x0s)
        self.nsite = self.n0 * self.np
        # Bonds: axis-0 bonds from x_0 = -1 .. w L - 1; other-axis bonds at x_0 = 0 .. w L - 1.
        self.bonds = {}
        for x0 in range(-1, w * L):
            for s in self.perp:
                self.bonds[(0, x0, s)] = len(self.bonds)
        for mu in range(1, d):
            for x0 in range(0, w * L):
                for s in self.perp:
                    self.bonds[(mu, x0, s)] = len(self.bonds)
        self.nb = len(self.bonds)

    def site(self, x0, s):
        return (x0 + 1) * self.np + self.pindex[s]

    def shift(self, s, mu, p):
        """s + e_mu in the perpendicular block, with its Bloch phase. mu >= 1."""
        t = list(s)
        t[mu - 1] += 1
        ph = np.exp(1j * p[mu - 1] / self.L)
        t[mu - 1] %= self.L
        return tuple(t), ph

    def ops(self, p):
        d, L, w = self.d, self.L, self.w
        Dm = np.zeros((self.nb, self.nsite), dtype=complex)  # D: site function to bond field, on free bonds
        for (mu, x0, s), b in self.bonds.items():
            if mu == 0:
                Dm[b, self.site(x0 + 1, s)] += 1
                Dm[b, self.site(x0, s)] -= 1
            else:
                t, ph = self.shift(s, mu, p)
                Dm[b, self.site(x0, t)] += ph
                Dm[b, self.site(x0, s)] -= 1
        # d: plaquettes with a free bond.
        plaq = []
        for mu, nu in itertools.combinations(range(d), 2):
            for x0 in range(-1, w * L + 1):
                for s in self.perp:
                    row = {}
                    # F_{mu nu}(x) = (T_mu - 1) H_nu (x) - (T_nu - 1) H_mu (x)
                    def add(mu2, x02, s2, c):
                        k = (mu2, x02, s2)
                        if k in self.bonds:
                            row[self.bonds[k]] = row.get(self.bonds[k], 0) + c
                    if mu == 0:
                        add(nu, x0 + 1, s, 1)
                        add(nu, x0, s, -1)
                        t, ph = self.shift(s, nu, p)
                        add(0, x0, t, -ph)
                        add(0, x0, s, 1)
                    else:
                        t, ph = self.shift(s, mu, p)
                        add(nu, x0, t, ph)
                        add(nu, x0, s, -1)
                        t2, ph2 = self.shift(s, nu, p)
                        add(mu, x0, t2, -ph2)
                        add(mu, x0, s, 1)
                    if row:
                        plaq.append(row)
        dm = np.zeros((len(plaq), self.nb), dtype=complex)
        for i, row in enumerate(plaq):
            for b, c in row.items():
                dm[i, b] = c
        # Q^o rows: parents along axis 0, y from box -1 .. w - 1; parents along mu >= 1, in boxes 0 .. w - 1.
        rows = []
        h = self.h
        V = L**d
        for i in range(-1, w):
            row = np.zeros(self.nb, dtype=complex)
            y0 = h + L * i
            # avg over x in B(y) of the line sum in axis 0: weight tri on axis 0, box on the others, centred on y_perp = (h, ..., h).
            for r0 in range(-h, h + 1):
                for s0 in range(L):
                    x0 = y0 + r0 + s0
                    for s in self.perp:
                        k = (0, x0, s)
                        if k in self.bonds:
                            t = np.array(s) - h
                            row[self.bonds[k]] += np.exp(1j * np.dot(p, t) / L) / V
            rows.append(row)
        for mu in range(1, d):
            for i in range(0, w):
                row = np.zeros(self.nb, dtype=complex)
                y0 = h + L * i
                for r0 in range(-h, h + 1):
                    x0 = y0 + r0
                    for s in self.perp:
                        base = np.array(s) - h
                        for s1 in range(L):
                            t = base.copy()
                            t[mu - 1] += s1
                            fine = tuple((t + h) % L)
                            row[self.bonds[(mu, x0, fine)]] += np.exp(1j * np.dot(p, t) / L) / V
                rows.append(row)
        Qo = np.array(rows)
        # r on Y blocks: one row per box; P_N: projector on functions on Y sites with these rows zero.
        rr = np.zeros((w, self.nsite), dtype=complex)
        for i in range(w):
            y0 = h + L * i
            for r0 in range(-h, h + 1):
                for s in self.perp:
                    t = np.array(s) - h
                    rr[i, self.site(y0 + r0, s)] = np.exp(1j * np.dot(p, t) / L) / V
        PN = np.zeros((self.nsite, self.nsite), dtype=complex)
        ysites = [self.site(x0, s) for x0 in range(0, w * L) for s in self.perp]
        PN[np.ix_(ysites, ysites)] = np.eye(len(ysites))
        for i in range(w):
            v = rr[i] / np.linalg.norm(rr[i])
            PN -= v.conj()[:, None] @ v[None, :]
        return Dm, dm, Qo, PN, plaq

    def analyse(self, p):
        L, w = self.L, self.w
        Dm, dm, Qo, PN, plaq = self.ops(p)
        Ks = dm.conj().T @ dm + Dm @ PN @ Dm.conj().T
        del Dm, PN
        _, s, vh = np.linalg.svd(Qo, full_matrices=True)
        Z = vh[int(np.sum(s > 1e-12)) :].conj().T
        del vh
        A = L**2 * (Z.conj().T @ (Ks @ Z))
        del Z
        A = 0.5 * (A + A.conj().T)
        cn = float(np.linalg.eigvalsh(A)[0])
        del A
        guard()
        # Across rate: source d^dagger e_p at the first plaquette next to the inner wall that has a free bond.
        ep = np.zeros(dm.shape[0], dtype=complex)
        # A plaquette in the plane (0, 1), at x_0 = 0, in the middle of the perpendicular block.
        target = None
        for i, row in enumerate(plaq):
            keys = set(row.keys())
            if (0, 0, tuple([self.h] * (self.d - 1))) in [k for k in self.bonds if self.bonds[k] in keys]:
                target = i
                break
        ep[target] = 1
        J = dm.conj().T @ ep
        m1 = Qo.shape[0]
        S = np.zeros((self.nb + m1, self.nb + m1), dtype=complex)
        S[: self.nb, : self.nb] = Ks
        S[: self.nb, self.nb :] = Qo.conj().T
        S[self.nb :, : self.nb] = Qo
        H = np.linalg.lstsq(S, np.concatenate([J, np.zeros(m1)]), rcond=1e-11)[0][: self.nb]
        nz = np.zeros(w)
        for (mu, x0, s), b in self.bonds.items():
            k = min(max(x0, 0) // L, w - 1)
            nz[k] += abs(H[b]) ** 2
        guard()
        return cn, np.sqrt(nz).tolist()


def momenta(d):
    base = [0.0, np.pi / 2, np.pi]
    return [np.array(q) for q in itertools.combinations_with_replacement(base, d - 1)]


def main():
    ok = True
    rng = np.random.default_rng(101)

    print("Part T, A'", flush=True)
    t1, chk = control_t1(3, 2, 2, rng)
    good = t1 <= 1e-4
    ok = ok and good
    print(f" T1 L=3 nc=2 m=2: relative error {t1:.2e}, fundamental check {chk:.1e}: {good}", flush=True)
    for L, nc in ((3, 4), (5, 4)):
        for m in (0, 1, 2):
            t0, a1, a2 = part_a_true(L, nc, m, rng)
            good = t0 <= 1e-10 and a1 <= 1e-7 and a2 <= 1e-8
            ok = ok and good
            print(f" A' L={L} nc={nc} m={m}: T0={t0:.1e} A1'={a1:.2e} A2'={a2:.1e}: {good} rss={rss_gb():.2f}GB", flush=True)

    print("Part D'", flush=True)
    for L, nc, ms in ((3, 12, (0, 1, 2, 4, 8)), (5, 8, (0, 1, 2, 4))):
        base, base_r = None, None
        for m in ms:
            v, prof = lam_true(L, nc, m)
            rt = sh.rate_of(prof)
            ap = L**2 * 2 * np.pi * m / (L * nc) ** 2
            if m == 0:
                base, base_r = v, rt
            good = True
            if ap <= 0.2:
                good = v >= 0.5 * base and rt >= 0.5 * base_r
                ok = ok and good
            print(f" D' L={L} nc={nc} m={m} a'={ap:.3f}: lam#t={v:.4f} rate={rt:.3f} prof={[f'{x:.1e}' for x in prof]}: {good} rss={rss_gb():.2f}GB", flush=True)

    print("Part E", flush=True)
    base_cn, base_a, base_w = None, None, None
    for L, nc, w in ((3, 8, 5), (5, 6, 4), (7, 6, 4), (9, 6, 4)):
        e1, e2, cn, across, along = part_e(L, nc, w, 0, rng)
        ra, rw = slope(across), slope(along)
        if base_cn is None:
            base_cn, base_a, base_w = cn, ra, rw
        good = e1 <= 1e-7 and e2 <= 1e-8 and cn >= 0.5 * base_cn and ra >= 0.7 and rw >= 0.7 and ra >= 0.5 * base_a and rw >= 0.5 * base_w
        ok = ok and good
        print(f" E L={L} nc={nc} w={w} m=0: E1={e1:.1e} E2={e2:.1e} cn={cn:.4f} across {ra:.3f} {[f'{v:.1e}' for v in across]} along {rw:.3f} {[f'{v:.1e}' for v in along]}: {good} rss={rss_gb():.2f}GB", flush=True)
    for L, nc, w, ms in ((3, 8, 5, (1, 2)), (5, 6, 4, (1,))):
        e1, e2, cn0, across, along = part_e(L, nc, w, 0, rng)
        ra0, rw0 = slope(across), slope(along)
        for m in ms:
            e1, e2, cn, across, along = part_e(L, nc, w, m, rng)
            ra, rw = slope(across), slope(along)
            ap = L**2 * 2 * np.pi * m / (L * nc) ** 2
            good = e1 <= 1e-7 and e2 <= 1e-8 and cn >= 0.5 * cn0 and ra >= 0.5 * ra0 and rw >= 0.5 * rw0
            ok = ok and good
            print(f" E L={L} nc={nc} w={w} m={m} a'={ap:.3f}: E1={e1:.1e} E2={e2:.1e} cn={cn:.4f} across {ra:.3f} along {rw:.3f}: {good} rss={rss_gb():.2f}GB", flush=True)

    print("Part F", flush=True)
    for d, Ls in ((3, ((3, 4), (5, 4), (7, 3))), (4, ((3, 4),))):
        base_c, base_r = None, None
        for L, w in Ls:
            T = Strip(d, L, w)
            cs, rs = [], []
            for p in momenta(d):
                c, prof = T.analyse(p)
                r = slope(prof)
                cs.append(c)
                rs.append(r)
                print(f"  F d={d} L={L} p={np.round(p, 2).tolist()}: cn={c:.4f} across {r:.3f} {[f'{v:.1e}' for v in prof]} rss={rss_gb():.2f}GB", flush=True)
            cmin, rmin = min(cs), min(rs)
            if base_c is None:
                base_c, base_r = cmin, rmin
            good = cmin >= 0.5 * base_c and cmin >= 0.02 and rmin >= 0.7 and rmin >= 0.5 * base_r
            ok = ok and good
            print(f" F d={d} L={L}: cn={cmin:.4f} across rate={rmin:.3f}: {good}", flush=True)

    print("PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
