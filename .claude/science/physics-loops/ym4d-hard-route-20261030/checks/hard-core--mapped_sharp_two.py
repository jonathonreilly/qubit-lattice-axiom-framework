#!/usr/bin/env python3
"""Theorem F and F-D at two levels, and with a frozen layer at each level. Consumer: `library/fibre-propagator.md`, steps (iv), (v), and the upper chain's (MD*_j) on this map.

Written before running. All earlier checks were at one level, so steps (iv), (v) with a composite Q^o, and the reading of the chart through Q^{o,(k)}, were tested only with k = 0. The upper chain now freezes data on a thin layer at every level, which no check has seen.

Field. d = 2, L = 3, fine torus N = 36, level-1 torus 12, level-2 torus 4, constant flux m on the fine torus, charged components. The multiplier vanishes at constant flux, and the level-1 field is again a constant flux, given by the phases of the level-0 step.

Objects. Level 0 -> 1: Q0 (true), Qo0, r0, Phi0. Level 1 -> 2: Q1 (true), Qo1, r1, Phi1, on the level-1 links. Composite Qo2 := Qo1 Qo0, r2 := r1 r0. bK: the true Hessian on fine bonds.

Direct problem, with the true maps only, no Q^o and no P_r. Unknown fine H. Constraints: (Q0 H) vanishes on the tree bonds of level 1, and Q1 Q0 H = 0. Objective: (1/2) bK[H, H] - Re eta^dagger (Q0 H) on the free level-1 bonds. A gauge term with omega vanishing at level-1 centres makes it unique. Output xi_direct := (Q0 H) on the free level-1 bonds. This is M^-1 eta, for M the Hessian of A_1 on its fibre, in the tree chart of level 1, by the Schur step.

Sharp problem. K# := bK + D P_r2 D^dagger, constraint Qo2, source J := Qo0^dagger (adjoint of the level-1 chart map)(eta). Chart map: X^o := Qo0 H, a^o := Phi1 X^o, X := X^o - D1 ev1^dagger a^o, then the tree representative at level 1. Output xi_sharp.

PRE-STATED criteria.

Part K, the torus, m = 0, 1, 2 (level-2 flux a' = 0.39 m).
 K0. ||Qo2 D0 omega - D'_2 r2 omega|| <= 1e-10 ||omega||, random omega.
 K1. ||xi_direct - xi_sharp|| <= 1e-7 ||xi_direct||, a random source local to a level-2 box.
 K2. ||P_r2 D0^dagger H|| <= 1e-8 ||H|| on the sharp solution.
 K3. lam# := min on ker Qo2 of 81 (bK + ||P_r2 phi||^2) / (81 (||d H||^2 + ||phi||^2) + ||H||^2) is at least 0.5 of its value at m = 0. In level-2 units.
FAIL if any fails. K1 failing means steps (iv), (v) are wrong at k >= 1.

Part N, frozen data at two levels, m = 0, 1. Level-2 boxes with first index below w := 2 are Y, the others Omega. E_Om: level-1 bonds with both ends in Omega. Layer at level 0: fine bonds with both ends in the fine strip x_0 in {26, 27}, inside the shadow of Omega; H vanishes there. Sites touched by those bonds carry no gauge parameter.
 Direct: as above, with (Q0 H) = 0 also on E_Om, the tree on Y boxes only, and H = 0 on the frozen fine bonds.
 Sharp: constraints (Qo0 on E_Om ; Qo2 on parents with a free level-1 bond). r_N: r0 on level-1 sites of Omega, r2 on blocks of Y, evaluation on sites touched by frozen fine bonds. P_N: the orthogonal projector on its kernel. K#_N := bK + D P_N D^dagger. Chart map as above, with the tree on Y boxes.
 N1. ||xi_direct - xi_sharp|| <= 1e-7 ||xi_direct||.
 N2. ||P_N D^dagger H|| <= 1e-8 ||H||.
 N3. cn := min on the constraint space of 81 (bK + ||P_N phi||^2) / ||H||^2 is at least 0.5 of 81 * 4 sin^2(pi/18) = 9.77, the Neumann gap of a level-2 box. Also reported without the fine layer.
FAIL if any fails. N3 failing means a layer at a lower level lowers the coercivity, which Lemma D-coer in its extension to several levels says it does not.

Result of the first run, recorded here: Part K PASS (K1 to 3e-13). N1, N2 PASS (to 2e-14). N3 FAIL: with the fine layer cn = 0.000 at m = 0, and 0.173 at m = 1; with no fine layer cn = 9.78 and 10.40. So a thin layer breaks the coercivity.

Diagnosis, written before the second run. The strip x_0 in {26, 27} lies inside level-1 blocks and contains no whole block. At flat data a constant rotation of the strip keeps its bonds fixed, with omega' = s on the strip, compensated inside each block so that r0 omega' = 0. This is an exact gauge direction with a stabiliser of the frozen data, so it is not removed by evaluating omega at touched sites; hence the zero. At flux it is no longer exact: D_U omega' on the strip is of size [F, s], giving an eigenvalue of order a'^2. This is the "hole inside a box" of (H1) in the ball, Text 5.3, and it is excluded for the upper chain's layers, whose thickness is at least 3 L: a layer made of whole parent blocks has r0 omega = 0 on each frozen block, so omega vanishes there.

PRE-STATED for the second run.
 N3a. With the fine layer made of whole level-1 blocks, columns x_0 in [24, 33) (thickness 3 L = 9) and x_0 in [24, 27) (one block): cn >= 4.885, m = 0, 1, and N1 <= 1e-7, N2 <= 1e-8.
 N3b. The thin strip, m = 1, 2: cn(m = 2)/cn(m = 1) in [3, 5.5], that is, close to the factor 4 of a'^2. Failure means the diagnosis of the soft mode is wrong.
FAIL if N3a or N3b fails.

Limits. L = 3 only, one size, so no statement on the dependence on L. Constant flux, so no multiplier at two levels. Rates are not measured: the torus is too small, and at the trivial background the composite at two levels with L = 3 is the one-level operator with L = 9, which the earlier checks covered. RSS guard 2 GB.
"""
import importlib.util
import os
import resource
import sys

import numpy as np


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


def levels(m):
    g0, D0, d0, Q0, Qo0, Dc0, ev0, r0, Phi0, Pr0, centres0 = sh.build_sharp(3, 12, m)
    g1 = RealBg(3, 4, 0)
    u1 = np.ones((2, 12, 12), dtype=complex)
    for i in range(12):
        for j in range(12):
            ci = i * 12 + j
            for mu in range(2):
                ni, nj = (i + (mu == 0)) % 12, (j + (mu == 1)) % 12
                u1[mu, i, j] = Dc0[ci + mu * 144, ni * 12 + nj]
    g1.u = u1
    tp.Bg = lambda L_, nc_, m_: g1
    try:
        _, D1, d1, Q1, Qo1, Dc1, ev1, r1, Phi1, Pr1, centres1 = sh.build_sharp(3, 4, 0)
    finally:
        tp.Bg = RealBg
    return dict(g0=g0, D0=D0, d0=d0, Q0=Q0, Qo0=Qo0, Dc0=Dc0, ev0=ev0, r0=r0, Phi0=Phi0, g1=g1, D1=D1, Q1=Q1, Qo1=Qo1, Dc1=Dc1, ev1=ev1, r1=r1, Phi1=Phi1, centres1=centres1, centres0=centres0)


def projector_kernel(R):
    """Orthogonal projector on the kernel of the rows R."""
    u, s, vh = np.linalg.svd(R, full_matrices=False)
    rk = int(np.sum(s > 1e-10 * s[0]))
    V = vh[:rk]
    return np.eye(R.shape[1], dtype=complex) - V.conj().T @ V


def part_k(m, rng):
    S = levels(m)
    g0, g1 = S["g0"], S["g1"]
    D0, d0, Q0, Qo0, ev0, r0 = S["D0"], S["d0"], S["Q0"], S["Qo0"], S["ev0"], S["r0"]
    D1, Q1, Qo1, Dc1, ev1, r1, Phi1 = S["D1"], S["Q1"], S["Qo1"], S["Dc1"], S["ev1"], S["r1"], S["Phi1"]
    Qo2 = Qo1 @ Qo0
    r2 = r1 @ r0
    N = g0.N
    nb = 2 * N * N
    om = rng.standard_normal(N * N) + 1j * rng.standard_normal(N * N)
    k0 = np.linalg.norm(Qo2 @ (D0 @ om) - Dc1 @ (r2 @ om)) / np.linalg.norm(om)
    Pr2 = projector_kernel(r2)
    K = bg.true_hessian(g0).toarray()
    guard()
    # Level-1 chart.
    n1 = 2 * g1.N**2
    tree1 = tp.comb_bonds(g1)
    keep1 = np.setdiff1d(np.arange(n1), tree1)
    idx_c1 = [g1.idx(*y) for y in S["centres1"]]
    free1 = np.setdiff1d(np.arange(g1.N**2), idx_c1)
    Dfs1 = D1[:, free1]
    Gt1 = np.linalg.solve(Dfs1[tree1, :], np.eye(len(tree1), dtype=complex))
    evd1 = ev1.conj().T

    def chart(Xo):
        v2 = Xo - D1 @ (evd1 @ (Phi1 @ Xo))
        return v2 - Dfs1 @ (Gt1 @ v2[tree1])

    def chart_adj(u_):
        u2 = u_.copy()
        u2[tree1] -= Gt1.conj().T @ (Dfs1.conj().T @ u_)
        return u2 - Phi1.conj().T @ (evd1.conj().T @ (D1.conj().T @ u2))

    # A random source on free level-1 bonds of the level-2 box 0.
    eta = np.zeros(n1, dtype=complex)
    box = [b for b in keep1.tolist() if (b % g1.N**2) // g1.N // 3 == 0 and (b % g1.N**2) % g1.N // 3 == 0]
    eta[box] = rng.standard_normal(len(box)) + 1j * rng.standard_normal(len(box))
    # Direct.
    Pev = np.eye(N * N, dtype=complex)
    for y in S["centres0"]:
        Pev[g0.idx(*y), g0.idx(*y)] = 0
    C = np.vstack([Q0[tree1, :], Q1 @ Q0])
    Kd = K + D0 @ Pev @ D0.conj().T
    mc = C.shape[0]
    Sd = np.zeros((nb + mc, nb + mc), dtype=complex)
    Sd[:nb, :nb] = Kd
    Sd[:nb, nb:] = C.conj().T
    Sd[nb:, :nb] = C
    rhs = np.concatenate([Q0[keep1, :].conj().T @ eta[keep1], np.zeros(mc)])
    Hd = np.linalg.lstsq(Sd, rhs, rcond=1e-12)[0][:nb]
    xi_d = np.zeros(n1, dtype=complex)
    xi_d[keep1] = (Q0 @ Hd)[keep1]
    del Sd
    guard()
    # Sharp.
    J = Qo0.conj().T @ chart_adj(eta)
    Ks = K + D0 @ Pr2 @ D0.conj().T
    m2 = Qo2.shape[0]
    Ss = np.zeros((nb + m2, nb + m2), dtype=complex)
    Ss[:nb, :nb] = Ks
    Ss[:nb, nb:] = Qo2.conj().T
    Ss[nb:, :nb] = Qo2
    Hs = np.linalg.solve(Ss, np.concatenate([J, np.zeros(m2)]))[:nb]
    del Ss
    xi_s = chart(Qo0 @ Hs)
    k1 = np.linalg.norm(xi_d - xi_s) / np.linalg.norm(xi_d)
    k2 = np.linalg.norm(Pr2 @ (D0.conj().T @ Hs)) / np.linalg.norm(Hs)
    guard()
    # lam#.
    Z = sh.null_basis(Qo2)
    pZ = D0.conj().T @ Z
    dZ = d0 @ Z
    A = 81 * (Z.conj().T @ (Ks @ Z))
    B = 81 * (dZ.conj().T @ dZ + pZ.conj().T @ pZ) + np.eye(Z.shape[1])
    A, B = 0.5 * (A + A.conj().T), 0.5 * (B + B.conj().T)
    Ci = np.linalg.inv(np.linalg.cholesky(B))
    lm = float(np.linalg.eigvalsh(Ci @ A @ Ci.conj().T)[0])
    guard()
    return k0, k1, k2, lm


def part_n(m, rng, columns=()):
    S = levels(m)
    g0, g1 = S["g0"], S["g1"]
    D0, Q0, Qo0, ev0, r0 = S["D0"], S["Q0"], S["Qo0"], S["ev0"], S["r0"]
    D1, Q1, Qo1, ev1, r1, Phi1 = S["D1"], S["Q1"], S["Qo1"], S["ev1"], S["r1"], S["Phi1"]
    Qo2 = Qo1 @ Qo0
    r2 = r1 @ r0
    N, N1 = g0.N, g1.N
    nb = 2 * N * N
    n1 = 2 * N1 * N1
    w = 2
    in_y1 = np.array([(s // N1) // 3 < w for s in range(N1 * N1)])  # level-1 sites in Y boxes
    # Level-1 bonds with both ends in Omega are frozen.
    E_om, free1b = [], []
    for s in range(N1 * N1):
        x0, x1 = s // N1, s % N1
        for mu in range(2):
            t = g1.idx(x0 + (mu == 0), x1 + (mu == 1))
            b = s + mu * N1 * N1
            (free1b if (in_y1[s] or in_y1[t]) else E_om).append(b)
    E_om, free1b = np.array(E_om), np.array(free1b)
    # Fine layer: bonds with both ends in the strip x_0 in {26, 27}.
    strip = np.zeros(N * N, dtype=bool)
    for x0 in columns:
        for x1 in range(N):
            strip[g0.idx(x0, x1)] = True
    frozen0 = []
    for s in range(N * N):
        x0, x1 = s // N, s % N
        for mu in range(2):
            t = g0.idx(x0 + (mu == 0), x1 + (mu == 1))
            if strip[s] and strip[t]:
                frozen0.append(s + mu * N * N)
    frozen0 = np.array(frozen0, dtype=int)
    free0 = np.setdiff1d(np.arange(nb), frozen0)
    touched = sorted({int(b % (N * N)) for b in frozen0.tolist()} | {g0.idx((b % (N * N)) // N + (b // (N * N) == 0), (b % (N * N)) % N + (b // (N * N) == 1)) for b in frozen0.tolist()})
    K = bg.true_hessian(g0)[free0][:, free0].toarray()
    Df = D0[free0, :]
    Q0f = Q0[:, free0]
    Qo0f = Qo0[:, free0]
    Qo2f = Qo2[:, free0]
    guard()
    # Level-1 chart on Y boxes.
    tree_all = tp.comb_bonds(g1)
    tree1 = np.array([b for b in tree_all.tolist() if in_y1[b % (N1 * N1)] and in_y1[g1.idx((b % (N1 * N1)) // N1 + (b // (N1 * N1) == 0), (b % (N1 * N1)) % N1 + (b // (N1 * N1) == 1))]])
    tset = set(tree1.tolist())
    keep1 = np.array([b for b in free1b.tolist() if b not in tset])
    idx_c1 = [g1.idx(*y) for y in S["centres1"] if in_y1[g1.idx(*y)]]
    y_sites1 = np.where(in_y1)[0]
    free_s1 = np.setdiff1d(y_sites1, idx_c1)
    Dfs1 = D1[:, free_s1]
    Gt1 = np.linalg.solve(Dfs1[tree1, :], np.eye(len(tree1), dtype=complex))
    evd1 = ev1.conj().T

    def chart(Xo):
        v2 = Xo - D1 @ (evd1 @ (Phi1 @ Xo))
        return v2 - Dfs1 @ (Gt1 @ v2[tree1])

    def chart_adj(u_):
        u2 = u_.copy()
        u2[tree1] -= Gt1.conj().T @ (Dfs1.conj().T @ u_)
        return u2 - Phi1.conj().T @ (evd1.conj().T @ (D1.conj().T @ u2))

    eta = np.zeros(n1, dtype=complex)
    box = [b for b in keep1.tolist() if (b % N1**2) // N1 // 3 == 0 and (b % N1**2) % N1 // 3 == 0]
    eta[box] = rng.standard_normal(len(box)) + 1j * rng.standard_normal(len(box))
    # Direct: the true maps.
    Pev = np.eye(N * N, dtype=complex)
    for y in S["centres0"]:
        Pev[g0.idx(*y), g0.idx(*y)] = 0
    for s in touched:
        Pev[s, s] = 0
    nf = len(free0)
    rows_par = np.where(np.max(np.abs(Q1[:, free1b]), axis=1) > 1e-12)[0]
    C = np.vstack([Q0f[tree1, :], Q0f[E_om, :], Q1[rows_par][:, free1b] @ Q0f[free1b, :]])
    Kd = K + Df @ Pev @ Df.conj().T
    mc = C.shape[0]
    Sd = np.zeros((nf + mc, nf + mc), dtype=complex)
    Sd[:nf, :nf] = Kd
    Sd[:nf, nf:] = C.conj().T
    Sd[nf:, :nf] = C
    rhs = np.concatenate([Q0f[keep1, :].conj().T @ eta[keep1], np.zeros(mc)])
    Hd = np.linalg.lstsq(Sd, rhs, rcond=1e-12)[0][:nf]
    del Sd
    xi_d = np.zeros(n1, dtype=complex)
    xi_d[keep1] = (Q0f @ Hd)[keep1]
    guard()
    # Sharp.
    r_om = np.array([s for s in range(N1 * N1) if not in_y1[s]])
    y_blocks = [c for c in range(r2.shape[0]) if (c // 4) < w]
    Rows = [r0[r_om, :], r2[y_blocks, :]]
    if touched:
        E_t = np.zeros((len(touched), N * N), dtype=complex)
        for i_, s in enumerate(touched):
            E_t[i_, s] = 1
        Rows.append(E_t)
    PN = projector_kernel(np.vstack(Rows))
    rows_par2 = np.where(np.max(np.abs(Qo1[:, free1b]), axis=1) > 1e-12)[0]
    bC = np.vstack([Qo0f[E_om, :], Qo2f[rows_par2, :]])
    Ks = K + Df @ PN @ Df.conj().T
    m2 = bC.shape[0]
    Ss = np.zeros((nf + m2, nf + m2), dtype=complex)
    Ss[:nf, :nf] = Ks
    Ss[:nf, nf:] = bC.conj().T
    Ss[nf:, :nf] = bC
    J = Qo0f.conj().T @ chart_adj(eta)
    Hs = np.linalg.lstsq(Ss, np.concatenate([J, np.zeros(m2)]), rcond=1e-12)[0][:nf]
    del Ss
    xi_s = chart(Qo0f @ Hs)
    n1_ = np.linalg.norm(xi_d - xi_s) / np.linalg.norm(xi_d)
    n2_ = np.linalg.norm(PN @ (Df.conj().T @ Hs)) / np.linalg.norm(Hs)
    guard()
    Z = sh.null_basis(bC)
    A = 81 * (Z.conj().T @ (Ks @ Z))
    A = 0.5 * (A + A.conj().T)
    cn = float(np.linalg.eigvalsh(A)[0])
    guard()
    return n1_, n2_, cn


def main():
    ok = True
    rng = np.random.default_rng(303)
    print("Part K", flush=True)
    base = None
    for m in (0, 1, 2):
        k0, k1, k2, lm = part_k(m, rng)
        if base is None:
            base = lm
        good = k0 <= 1e-10 and k1 <= 1e-7 and k2 <= 1e-8 and lm >= 0.5 * base
        ok = ok and good
        print(f" K m={m} a'={0.3927 * m:.3f}: K0={k0:.1e} K1={k1:.2e} K2={k2:.1e} lam#={lm:.4f}: {good} rss={rss_gb():.2f}GB", flush=True)
    print("Part N, second run", flush=True)
    target = 0.5 * 81 * 4 * np.sin(np.pi / 18) ** 2
    for name, cols in (("3 L", tuple(range(24, 33))), ("one block", (24, 25, 26))):
        for m in (0, 1):
            n1_, n2_, cn = part_n(m, rng, cols)
            good = n1_ <= 1e-7 and n2_ <= 1e-8 and cn >= target
            ok = ok and good
            print(f" N3a layer {name} m={m}: N1={n1_:.2e} N2={n2_:.1e} cn={cn:.4f} (criterion {target:.3f}): {good} rss={rss_gb():.2f}GB", flush=True)
    vals = {}
    for m in (1, 2):
        n1_, n2_, cn = part_n(m, rng, (26, 27))
        vals[m] = cn
        print(f" thin strip m={m}: N1={n1_:.2e} N2={n2_:.1e} cn={cn:.4f} rss={rss_gb():.2f}GB", flush=True)
    ratio = vals[2] / vals[1]
    good = 3 <= ratio <= 5.5
    ok = ok and good
    print(f" N3b ratio cn(2)/cn(1) = {ratio:.3f}: {good}", flush=True)
    print("PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
