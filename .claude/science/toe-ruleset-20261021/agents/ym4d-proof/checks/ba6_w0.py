"""ba6 (BFT lane A, session 6): checks of BFT_A §26 (dualities, Lemma CS, Theorem YH numerics, Lemma LE ratio).

Matrix-free chain of checks/ba5_y.py (read-only import): L = 3, kappa = 1, d = 4, c26 axial template.
Criteria: checks/ba6_criteria.md (written before this file).  Usage: python3 ba6_w0.py PART   (PART in A K)
"""
import sys
import time

import numpy as np

sys.path.insert(0, "/Users/jonreilly/Projects/Physics/.claude/worktrees/peaceful-heisenberg-e2d2a0/.claude/science/"
                   "toe-ruleset-20261021/agents/ym4d-proof/checks")
import ba5_y as b5  # noqa: E402

L = b5.L; ALPHA = 0.25
T0 = time.time()
Chain, dT, dform, dot, axpy, mx, l1 = b5.Chain, b5.dT, b5.dform, b5.dot, b5.axpy, b5.mx, b5.l1


def stamp():
    return f"({time.time() - T0:.0f} s, RSS {b5.rss():.0f} MB)"


def dinf(M):
    dv = np.abs(b5.disp(M))
    return np.maximum(np.maximum(dv[:, None, None, None], dv[None, :, None, None]),
                      np.maximum(dv[None, None, :, None], dv[None, None, None, :]))


def cube_rand(rng, M, side, off, ncomp):
    out = [np.zeros((M,) * 4) for _ in range(ncomp)]
    sl = (slice(off, off + side),) * 4
    for a in out:
        a[sl] = rng.standard_normal((side,) * 4)
    return out


def div1(v):
    return sum(b5.bwd(v[m], m) for m in range(4))


def qstr(v, s):
    """direct straight average of side s: level-l 1-form -> level-m 1-form (own units of level m)."""
    S = v[0].shape[0]; Sm = S // s; out = []
    for nu in range(4):
        line = sum(np.roll(v[nu], -t, axis=nu) for t in range(s))
        out.append(line.reshape(Sm, s, Sm, s, Sm, s, Sm, s).sum(axis=(1, 3, 5, 7)) / s ** 4)
    return out


def rel(a, b):
    return abs(a - b) / max(abs(a), abs(b), 1e-300)


# ---------------------------------------------------------------- part A: E1, E4
def part_A():
    rng = np.random.default_rng(6)
    ok1 = True
    print("E1 (dualities)", flush=True)
    for (k, T) in [(1, 3), (2, 2)]:
        ch = Chain(k, T); M = ch.S[0]
        Y, rY, _ = ch.solve(ch.rhs(cur={0: dT(b5.delta_p(M))}))
        Y0 = ch.lev(Y, 0); dY0 = dform(Y0)
        G0 = cube_rand(rng, M, 5, 2, 6)
        j0 = b5.coulomb(cube_rand(rng, M, 5, 2, 4))
        X, rX, _ = ch.solve(ch.rhs(cur={0: axpy(1.0, dT(G0), j0)}))
        lhs = dform(ch.lev(X, 0))[0][0, 0, 0, 0]
        rhs = dot(G0, dY0) + dot(j0, Y0)
        e_a = rel(lhs, rhs); ok1 &= e_a <= 1e-8
        print(f"  (a) k={k} T={T}: dx_0(p) = {lhs:.6e}, <G,dY> + <j,Y> = {rhs:.6e}, rel {e_a:.1e}; CG res {rY:.0e}/{rX:.0e} "
              f"{stamp()}", flush=True)
        if k == 2:
            G1 = cube_rand(rng, ch.S[1], 3, 1, 6)
            X1, rX1, _ = ch.solve(ch.rhs(cur={1: dT(G1)}))
            lhs1 = dform(ch.lev(X1, 0))[0][0, 0, 0, 0]
            rhs1 = dot(G1, dform(ch.lev(Y, 1)))
            e_b = rel(lhs1, rhs1); ok1 &= e_b <= 1e-8
            print(f"  (b) k=2 T=2 level-1 G_1: dx_0(p) = {lhs1:.6e}, <G_1, dY_1> = {rhs1:.6e}, rel {e_b:.1e} {stamp()}",
                  flush=True)
        if k == 1:
            sb = ch.zero(k); site = (1, 1, 1, 1); sb[0][site] = 1.0
            Yb, rYb, _ = ch.solve(ch.rhs(resid={k - 1: sb}))
            r_top = ch.res(X)[k - 1][0][site]
            rhs_c = dot(G0, dform(ch.lev(Yb, 0))) + dot(j0, ch.lev(Yb, 0))
            e_c = rel(r_top, rhs_c); ok1 &= e_c <= 1e-8
            print(f"  (c) TOPD k=1 T=3: r_(k-1)(b) = {r_top:.6e}, pairing = {rhs_c:.6e}, rel {e_c:.1e} {stamp()}", flush=True)
        del Y, X
    print(f"E1 {'PASS' if ok1 else 'FAIL'}", flush=True)

    print("E4 (Lemma CS inequalities), k = 2, T = 2", flush=True)
    ch = Chain(2, 2); ok4 = True
    for l in (0, 1):
        for c in range(3):
            G = [rng.standard_normal((ch.S[l],) * 4) for _ in range(6)]
            v = dT(G); g = mx(G)
            cc = max(float(np.max(np.abs(div1(v)))), 0.0) / mx(v)
            r0 = mx(v) / g
            ok4 &= (r0 <= 6 * (1 + 1e-12)) and (cc <= 1e-12)
            line = f"  l={l} case {c}: max|d*G|/max|G| = {r0:.4f}, co-closed {cc:.1e}"
            for m in range(l + 1, 3):
                rq = mx(qstr(v, L ** (m - l))) / g
                ok4 &= rq <= 6 * (1 + 1e-12)
                line += f"; m={m}: max|Q_str d*G|/max|G| = {rq:.4f}"
            print(line, flush=True)
    print(f"E4 {'PASS' if ok4 else 'FAIL'} {stamp()}", flush=True)


# ---------------------------------------------------------------- part K: E2, E3, E4 (designed), E5
def run_k(k, T, do_design):
    ch = Chain(k, T); M = ch.S[0]; n = L ** k
    Y, rY, itY = ch.solve(ch.rhs(cur={0: dT(b5.delta_p(M))}))
    Y0 = ch.lev(Y, 0); dY0 = dform(Y0)
    d = dinf(M); w = np.where(d <= n, (d / n) ** ALPHA, 2.0)
    UH = sum(float(np.sum(np.abs(a) * w)) for a in dY0)
    S1 = l1(dY0)
    out = {"UH": UH, "S1": S1}
    msg = f"  k={k} T={T}: U_H {UH:.4f}, S1 {S1:.4f}"
    if do_design:
        u = b5.coulomb(Y0)
        j = b5.coulomb(b5.tsign(u))
        DN = abs(dot(j, Y0)) / (n * mx(j))
        out["DN"] = DN
        msg += f", D_N {DN:.4f}, ||Pi_cc Y_0||_1/n {l1(u) / n:.4f}"
        del u, j
        if k == 2:
            dY1 = dform(ch.lev(Y, 1))
            Gs = b5.tsign(dY1)
            ratio = n ** 2 * abs(dot(Gs, dY1)) / (L ** (2 * (k - 1)) * mx(Gs))
            msg += f", GU designed ratio {ratio:.4f}"
    if k == 1:
        Bp = dT([b5.lap_inv(a) for a in dY0])
        side = max(2, int(np.ceil(n / 4)))
        grads = [b5.fwd(Bp[nu], a) * n ** 2 for nu in range(4) for a in range(4)]
        best = 0.0
        for X in np.ndindex(T, T, T, T):
            c0 = [x * n + n // 2 - side // 2 for x in X]
            idx = np.ix_(*[(np.arange(side) + c) % M for c in c0])
            tot = 0.0
            for g in grads:
                gr = g[idx]
                tot += float(np.sum((gr - gr.mean()) ** 2))
            best = max(best, tot / n ** 4)
        del grads
        LE = np.sqrt(best) / (n ** 2 * mx(dY0))
        out["LE"] = LE
        msg += f", LE ratio {LE:.4f} (box side {side})"
        del Bp
    print(msg + f"; CG res {rY:.0e} ({itY} it) {stamp()}", flush=True)
    del Y, dY0
    return out


def part_K():
    print("E2/E3/E5 at k = 1", flush=True)
    R1 = {T: run_k(1, T, True) for T in [2, 3, 4, 5, 6]}
    print("E2/E3/E4-designed at k = 2", flush=True)
    R2 = {T: run_k(2, T, T <= 3) for T in [2, 3, 4]}
    U1 = [R1[T]["UH"] for T in (4, 5, 6)]
    H1 = (U1[2] - U1[1]) <= (U1[1] - U1[0]) + 0.02 * U1[0]
    mU1 = max(R1[T]["UH"] for T in R1)
    H2 = all(R2[T]["UH"] <= 2 * mU1 for T in (2, 3, 4))
    D1 = [R1[T]["DN"] for T in (4, 5, 6)]
    N1 = (D1[2] - D1[1]) <= (D1[1] - D1[0]) + 0.02 * D1[0]
    mD1 = max(R1[T]["DN"] for T in R1)
    N2 = all(R2[T]["DN"] <= 2 * mD1 for T in (2, 3))
    LE1 = R1[6]["LE"] <= 1.1 * R1[4]["LE"]
    for name, v in [("H1", H1), ("H2", H2), ("N1", N1), ("N2", N2), ("LE1", LE1)]:
        print(f"{name} {'PASS' if v else 'FAIL'}", flush=True)


if __name__ == "__main__":
    {"A": part_A, "K": part_K}[sys.argv[1]]()
