#!/usr/bin/env python3
"""Referee check for J:derive:constraint-algebra-closure-for-block-62s-kinetic-numbers:a2.

Independent of the author's check.py. Placement and R1 stencil are block 62's
(refuter W6): h_jj on sites, h_ij (i<j) on faces, xi_j on bonds from x to x+e_j.
R1(x) = (sum_j L_j h_jj + 2 sum_{i<j} S_ij h_ij) - Lap(tr), the real-space form
whose symbol is the note's R_1 = -(p_i p_j h_ij - p^2 h) up to the staggered phases.
Kinetic term is the note's alpha hdot_ij hdot_ij + beta hdot^2, summed over all
index pairs so each off-diagonal entry is counted twice.
"""
import itertools
import random
from fractions import Fraction as Fr

import sympy as sp

fails = []


def report(name, ok, detail):
    fails.append(name) if not ok else None
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)


def legendre_and_dewitt():
    a, b = sp.symbols("alpha beta", nonzero=True)
    v = sp.symbols("v1 v2 v3")
    w = sp.symbols("w12 w13 w23")
    S = sum(v)
    # hh = sum_{i,j} h_ij^2 with h symmetric: diagonal once, each off-diagonal twice.
    Lkin = a * (sum(x * x for x in v) + 2 * sum(x * x for x in w)) + b * S ** 2
    P = sp.Matrix([sp.diff(Lkin, x) for x in v])
    Q = sp.Matrix([sp.diff(Lkin, x) for x in w])
    Ps = sp.Matrix(sp.symbols("P1 P2 P3"))
    Qs = sp.Matrix(sp.symbols("Q12 Q13 Q23"))
    sols = sp.solve([P[i] - Ps[i] for i in range(3)] + [Q[i] - Qs[i] for i in range(3)], list(v) + list(w))
    H = sum(Ps[i] * sols[v[i]] for i in range(3)) + sum(Qs[i] * sols[w[i]] for i in range(3)) - Lkin.subs(sols)
    c = b / (a + 3 * b)
    T = sum(Ps)
    claim = (sum(Ps[i] ** 2 for i in range(3)) - c * T ** 2) / (4 * a) + sum(Qs[i] ** 2 for i in range(3)) / (8 * a)
    # task's pi: pi_jj = P_jj, pi_ij = P_ij/2 off the diagonal, pi.pi sums both off-diagonal slots.
    pi_dot = sum(Ps[i] ** 2 for i in range(3)) + sp.Rational(1, 2) * sum(Qs[i] ** 2 for i in range(3))
    task = (pi_dot - c * T ** 2) / (4 * a)
    ok = sp.simplify(sp.together(H - claim)) == 0 and sp.simplify(sp.together(claim - task)) == 0
    c_half = sp.simplify(c - sp.Rational(1, 2))
    # c = 1/2 iff b = -a, provided the kinetic metric is nondegenerate (a + 3b != 0).
    ok_iff = sp.simplify(c_half.subs(b, -a)) == 0 and sp.solve(sp.Eq(c, sp.Rational(1, 2)), b) == [-a]
    report(
        "legendre",
        bool(ok and ok_iff),
        "Legendre of alpha hh + beta (tr hdot)^2 is (1/(4 alpha))(sum P_jj^2 - c (sum P_jj)^2) + sum_{i<j} P_ij^2/(8 alpha), "
        "c = beta/(alpha+3 beta), equal to the task's (1/(4 alpha))(pi.pi - c pi^2) with pi_ij = P_ij/2 off diagonal; "
        "c = 1/2 iff beta = -alpha",
    )


def tt_speed_at_dewitt():
    """T4's travelling root does not use beta. At beta = -alpha the prefactor (alpha+beta) vanishes, but a TT mode still has X = p^2/(4 alpha)."""
    p = (sp.Integer(1), sp.Integer(2), sp.Integer(2))
    u = (sp.Integer(2), sp.Integer(-1), sp.Integer(0))  # orthogonal to p
    psq = sum(x * x for x in p)
    uu = sum(x * x for x in u)
    # transverse projector has rank 2, so removing the trace takes uu/2
    Pij = [[(1 if i == j else 0) - p[i] * p[j] / psq for j in range(3)] for i in range(3)]
    h = [[u[i] * u[j] - (uu / 2) * Pij[i][j] for j in range(3)] for i in range(3)]
    tr = sp.simplify(sum(h[i][i] for i in range(3)))
    hh = sp.simplify(sum(h[i][j] ** 2 for i in range(3) for j in range(3)))
    div = [sp.simplify(sum(p[i] * h[i][j] for i in range(3))) for j in range(3)]
    r1 = sp.simplify(-(sum(p[i] * p[j] * h[i][j] for i in range(3) for j in range(3)) - psq * tr))
    r2 = sp.simplify(
        -sp.Rational(1, 4) * psq * hh
        + sp.Rational(1, 2) * sum(d * d for d in div)
        - sp.Rational(1, 2) * sum(div[j] * p[j] for j in range(3)) * tr
        + sp.Rational(1, 4) * psq * tr ** 2
    )
    a, b, X = sp.symbols("alpha beta X")
    kinetic = a * hh + b * tr ** 2
    form = sp.simplify(X * kinetic - (-r2))
    root = sp.solve(sp.Eq(form, 0), X)[0]
    at = sp.simplify(root.subs(b, -a) - psq / (4 * a))
    report(
        "tt-speed",
        tr == 0 and all(d == 0 for d in div) and r1 == 0 and sp.simplify(r2 + psq * hh / 4) == 0 and at == 0,
        "a transverse traceless polarization at p=(1,2,2) has R1=0 and R2=-(1/4) p^2 hh, so X = p^2/(4 alpha) with beta absent; "
        "K/(4 alpha) is that speed squared when K = wbar = 1, including at beta = -alpha",
    )


def symbol_identity():
    """Bracket versus G[xi] as Laurent polynomials in e^{ik_j/2}, e^{ik'_j/2}. K=4, alpha=1 so the xi prefactor is 1."""
    lam = sp.symbols("lam")
    ui, uj, vi, vj = sp.symbols("ui uj vi vj", nonzero=True)
    s, t = sp.symbols("s t", nonzero=True)
    K, alpha = sp.Integer(4), sp.Integer(1)
    # (2 sin(theta/2))^2 = 2 - e^{i theta} - e^{-i theta}
    diag_bracket = (K / (2 * alpha)) * (-((2 - s - 1 / s) - (2 - t - 1 / t)))
    diag_G = 2 * (s - t) * (1 - 1 / (s * t))
    diag_ok = sp.factor(sp.together(sp.expand(diag_bracket - diag_G))) == 0

    def g(u, v):
        return 2 * (1 - u ** 2) * (1 - v ** 2)

    def gam(u, v):
        cu, su = (u + 1 / u) / 2, (u - 1 / u) / (2 * sp.I)
        cv, sv = (v + 1 / v) / 2, (v - 1 / v) / (2 * sp.I)
        return u * v * (cu * cv + lam * su * sv)

    face = sp.together(K * (g(ui, uj) * gam(vi, vj) - g(vi, vj) * gam(ui, uj)) / (4 * alpha))
    # xi_j(lc+e_i) - xi_j(lc), plus the swapped pair, phase at the lower corner removed
    face_G = ((ui * vi) ** 2 - 1) * (uj ** 2 - vj ** 2) + ((uj * vj) ** 2 - 1) * (ui ** 2 - vi ** 2)
    face_ok = sp.factor(sp.together(sp.expand(face - face_G))) == 0
    report(
        "symbols",
        bool(diag_ok and face_ok),
        "at c=1/2 the diagonal and face coefficients equal delta_xi h for every wave vector, "
        "with xi_j = (K/(4 alpha))(N_{x+e_j} M_x - N_x M_{x+e_j}), and for every face symbol "
        "cos(k_i/2)cos(k_j/2) + lam sin(k_i/2)sin(k_j/2); lam cancels when the bracket is antisymmetrized",
    )


# -------------------------------------------------------------------------------- lattice
def make_box(L):
    sites = list(itertools.product(range(L), repeat=3))
    pairs = ((0, 1), (0, 2), (1, 2))

    def shift(x, j, s):
        y = list(x)
        y[j] = (y[j] + s) % L
        return tuple(y)

    def r1_grad(N):
        g = {}

        def acc(key, val):
            g[key] = g.get(key, 0) + val

        for x, n in N.items():
            if n == 0:
                continue
            for j in range(3):
                for y, cf in ((shift(x, j, 1), 1), (shift(x, j, -1), 1), (x, -2)):
                    acc(("d", j, y), n * cf)
                    for kk in range(3):
                        acc(("d", kk, y), -n * cf)
            for i, j in pairs:
                corners = (
                    (x, 1),
                    (shift(x, i, -1), -1),
                    (shift(x, j, -1), -1),
                    (shift(shift(x, i, -1), j, -1), 1),
                )
                for lc, cf in corners:
                    acc(("o", (i, j), lc), 2 * n * cf)
        return g

    def face_clock(M, i, j, lc, mode):
        a = lc
        b = shift(lc, i, 1)
        c = shift(lc, j, 1)
        d = shift(b, j, 1)
        if mode == "mean4":
            return (M[a] + M[b] + M[c] + M[d]) / 4
        if mode == "opp":
            return (M[a] + M[d]) / 2
        if mode == "opp2":
            return (M[b] + M[c]) / 2
        if mode == "near":
            return M[a]
        if mode == "far":
            return M[d]
        raise ValueError(mode)

    def bracket(N, M, alpha, c, K, mode, gN=None, gM=None):
        out = {}

        def add(key, val):
            if val:
                out[key] = out.get(key, 0) + val

        for A, B, g, sgn in ((N, M, gN, 1), (M, N, gM, -1)):
            if g is None:
                g = r1_grad(A)
            for x in sites:
                gs = [g.get(("d", j, x), 0) for j in range(3)]
                sm = gs[0] + gs[1] + gs[2]
                Bx = B[x]
                if Bx == 0 and sm == 0:
                    continue
                for m in range(3):
                    add(("d", m, x), sgn * K * Bx * (gs[m] - c * sm) / (2 * alpha))
            for i, j in pairs:
                for x in sites:
                    gv = g.get(("o", (i, j), x), 0)
                    if gv:
                        add(("o", (i, j), x), sgn * K * gv * face_clock(B, i, j, x, mode) / (4 * alpha))
        return out

    def xi_field(N, M, alpha, K):
        pref = K / (4 * alpha)
        xi = {}
        for j in range(3):
            for x in sites:
                xp = shift(x, j, 1)
                xi[(j, x)] = pref * (N[xp] * M[x] - N[x] * M[xp])
        return xi

    def G(xi):
        out = {}

        def add(key, val):
            if val:
                out[key] = out.get(key, 0) + val

        for x in sites:
            for j in range(3):
                add(("d", j, x), 2 * (xi[(j, x)] - xi[(j, shift(x, j, -1))]))
            for i, j in pairs:
                add(
                    ("o", (i, j), x),
                    (xi[(j, shift(x, i, 1))] - xi[(j, x)]) + (xi[(i, shift(x, j, 1))] - xi[(i, x)]),
                )
        return out

    return sites, pairs, r1_grad, bracket, xi_field, G


def same(a, b):
    keys = set(a) | set(b)
    return all(a.get(k, 0) == b.get(k, 0) for k in keys)


def lapse_delta(sites, z):
    return {x: Fr(1 if x == z else 0) for x in sites}


def exhaustive_4():
    sites, pairs, r1_grad, bracket, xi_field, G = make_box(4)
    alpha, K, c = Fr(1), Fr(4), Fr(1, 2)
    grads = {z: r1_grad(lapse_delta(sites, z)) for z in sites}
    ok = True
    checked = 0
    for z, w in itertools.product(sites, repeat=2):
        N, M = lapse_delta(sites, z), lapse_delta(sites, w)
        b = bracket(N, M, alpha, c, K, "mean4", grads[z], grads[w])
        g = G(xi_field(N, M, alpha, K))
        ok = ok and same(b, g)
        checked += 1
        if not ok:
            break
    # opposite-corner means reproduce the four-corner bracket on a basis of lapses
    same_timing = True
    for z, w in itertools.product(sites, repeat=2):
        N, M = lapse_delta(sites, z), lapse_delta(sites, w)
        b4 = bracket(N, M, alpha, c, K, "mean4", grads[z], grads[w])
        if not same(b4, bracket(N, M, alpha, c, K, "opp", grads[z], grads[w])):
            same_timing = False
            break
        if not same(b4, bracket(N, M, alpha, c, K, "opp2", grads[z], grads[w])):
            same_timing = False
            break
    report(
        "torus-4",
        ok and same_timing,
        f"EXACT on the 4^3 torus, all {checked} pairs of site-basis lapses, alpha=1, K=4, c=1/2: "
        "the linear bracket equals G[xi] with xi_j = (K/(4 alpha))(N at x+e_j times M at x, minus N at x times M at x+e_j); "
        "either opposite-corner mean equals the four-corner mean on every pair",
    )


def other_sizes():
    random.seed(20260924)
    ok = True
    for L in (3, 5):
        sites, pairs, r1_grad, bracket, xi_field, G = make_box(L)
        alpha, K = Fr(3, 7), Fr(5, 11)
        for _ in range(4):
            N = {x: Fr(random.randint(-2, 2)) for x in sites}
            M = {x: Fr(random.randint(-2, 2)) for x in sites}
            b = bracket(N, M, alpha, Fr(1, 2), K, "mean4")
            g = G(xi_field(N, M, alpha, K))
            ok = ok and same(b, g)
    report(
        "other-tori",
        ok,
        "EXACT on 3^3 and 5^3, four random integer lapse pairs each, alpha=3/7, K=5/11, c=1/2, four-corner clocks: the same identity",
    )


def rank_mod(rows, mod):
    m = [row[:] for row in rows]
    nrows = len(m)
    ncols = len(m[0]) if nrows else 0
    r = 0
    col = 0
    while r < nrows and col < ncols:
        piv = None
        for i in range(r, nrows):
            if m[i][col] % mod:
                piv = i
                break
        if piv is None:
            col += 1
            continue
        m[r], m[piv] = m[piv], m[r]
        inv = pow(m[r][col], -1, mod)
        rr = [(m[r][j] * inv) % mod for j in range(col, ncols)]
        m[r][col:] = rr
        for i in range(nrows):
            if i == r or m[i][col] % mod == 0:
                continue
            f = m[i][col]
            for j, t in enumerate(range(col, ncols)):
                m[i][t] = (m[i][t] - f * rr[j]) % mod
        r += 1
        col += 1
    return r


def necessity_and_corners():
    sites, pairs, r1_grad, bracket, xi_field, G = make_box(4)
    # one lapse pair whose (1-2c) piece is nonzero: N at 0, M at e_1
    N = lapse_delta(sites, (0, 0, 0))
    M = lapse_delta(sites, (1, 0, 0))
    alpha, K = Fr(1), Fr(1)
    b_half = bracket(N, M, alpha, Fr(1, 2), K, "mean4")
    b_zero = bracket(N, M, alpha, Fr(0), K, "mean4")
    b1 = {k: b_zero.get(k, 0) - b_half.get(k, 0) for k in set(b_zero) | set(b_half)}
    iso = all(b1.get(("o", pr, x), 0) == 0 for pr in pairs for x in sites)
    iso = iso and all(b1.get(("d", 0, x), 0) == b1.get(("d", 1, x), 0) == b1.get(("d", 2, x), 0) for x in sites)
    nonzero = any(b1.get(k, 0) != 0 for k in b1)

    bonds = [(j, x) for j in range(3) for x in sites]
    variables = [("d", j, x) for j in range(3) for x in sites] + [("o", pr, x) for pr in pairs for x in sites]
    mod = 1_000_003

    def column(xi_unit):
        g = G(xi_unit)
        return [int(g.get(v, 0)) % mod for v in variables]

    cols = []
    for j, x in bonds:
        unit = {bb: Fr(0) for bb in bonds}
        unit[(j, x)] = Fr(1)
        cols.append(column(unit))
    # clear the denominator of b1 (quarters from nothing here at alpha=K=1, c in {0,1/2}: halves)
    den = 1
    for val in b1.values():
        den = den * val.denominator // math_gcd(den, val.denominator)
    b1_col = [int(b1.get(v, 0) * den) % mod for v in variables]
    rows = [list(col) for col in zip(*cols)]
    rG = rank_mod(rows, mod)
    rows_aug = [row + [b1_col[i]] for i, row in enumerate(rows)]
    rA = rank_mod(rows_aug, mod)

    corner_up = True
    details = []
    for mode in ("near", "far"):
        bb = bracket(N, M, alpha, Fr(1, 2), K, mode)
        den_c = 1
        for val in bb.values():
            den_c = den_c * val.denominator // math_gcd(den_c, val.denominator)
        extra = [int(bb.get(v, 0) * den_c) % mod for v in variables]
        rr = rank_mod([row + [extra[i]] for i, row in enumerate(rows)], mod)
        corner_up = corner_up and rr == rG + 1
        details.append(f"{mode}:{rG}->{rr}")
    report(
        "necessity",
        iso and nonzero and rA == rG + 1 and corner_up,
        "the bracket is affine in c: b(c)=b(1/2)+(1-2c) b1, and b1 is equal on the three diagonal momenta, "
        f"zero on faces, and outside the relabelling span (rank mod {mod}: {rG} -> {rA}); "
        f"one-corner clocks at c=1/2 are also outside ({', '.join(details)}). Closure onto G for every lapse holds only at c=1/2, i.e. beta=-alpha, and only for an inversion-symmetric face clock",
    )


def math_gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)


def main():
    legendre_and_dewitt()
    tt_speed_at_dewitt()
    symbol_identity()
    exhaustive_4()
    other_sizes()
    necessity_and_corners()
    print(f"TOTAL: PASS={6 - len(fails)} FAIL={len(fails)}")
    if fails:
        print("SUMMARY: fails at step " + fails[0] + " - independent check did not reproduce the attempt")
        return
    print(
        "SUMMARY: confirmed at linear order — on the lattice {C[N],C[M]} equals G[xi] with "
        "xi_j=(K/(4 alpha))(N_{x+e_j} M_x - N_x M_{x+e_j}) for every lapse iff beta=-alpha, "
        "when face terms are timed inversion-symmetrically; no O(p^2) remainder (symbolic, all wave vectors, and exhaustive on 4^3). "
        "The structure constant is the TT speed squared. The walker's own bracket is not part of the confirmed claim."
    )
    print(
        "HIT: confirmed - linear-order closure on the lattice survives: beta=-alpha is necessary and sufficient "
        "for {K R1[N], kin[M]}-(N<->M) to equal the strain relabelling G[xi], xi the bond field "
        "(K/(4 alpha))(N_{x+e} M - N M_{x+e}), for inversion-symmetric face clocks "
        "(four-corner mean and either opposite-corner mean); verified by an independent Legendre transform, "
        "the trig identity at every wave vector, every pair of site lapses on the 4^3 torus, samples on 3^3 and 5^3, "
        "and a modular rank obstruction for every other c and for a one-corner clock. "
        "Quadratic order and the walker's bracket stay open, as the attempt marked them."
    )


if __name__ == "__main__":
    main()
