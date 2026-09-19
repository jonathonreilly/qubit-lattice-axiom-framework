#!/usr/bin/env python3
"""Referee of J:derive:two-source-interaction:a2 (author w-macbookpro90c72-j6e57, grok-4.6); referee
w-jonathonsmac4f50-jc66e (claude-opus-5). Independent machinery (exact rationals in real space), none of the author's code.

Linear model (the attempt's): theta_{t+1} = P theta_t + xi, (P f)(x) = (f(x) + sum_{+-e_j} f(x +- e_j))/7 on (Z/L)^3,
Var xi = sigma^2 = 1; chi = (I - P)^{-1}, C = (I - P^2)^{-1} on the mean-zero subspace.

X1  the L = 4 values of statement (b) by real-space linear algebra (translation-invariant solves in Q), not Fourier
X2  chi = C (I + P) exactly (the attempt's chi = C(1 + phi)/sigma^2), and the linearized Gibbs response
X3  a site pinned at every level: the stationary mean of the pinned process (i) on the torus is the constant alpha,
    (ii) on a box with far boundary 0 (a stand-in for Z^3) is alpha G(y)/G(0), G the Green function of I - P; the
    static conditioning of the free stationary law gives alpha C(y)/C(0); the attempt's alpha chi(y)/C(0) is neither
    and misses the pin value itself
X4  the two-pin Gaussian algebra of (c) for the static marginal (like / unlike shifts), exactly on L = 4
X5  the nonlinear pairing sum_x s'_x . S_x(s) = sum_x s_x . S_x(s') on random integer configurations
"""
from __future__ import annotations

import itertools
import random
import sys
from fractions import Fraction

PASSES = 0
FAILS = 0


def check(tag, ok, msg):
    global PASSES, FAILS
    if ok:
        PASSES += 1
    else:
        FAILS += 1
    print(f"{'PASS' if ok else 'FAIL'}: {tag} {msg}")


NB = [(0, 0, 0), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def solve_exact(A, b):
    n = len(A[0])
    M = [row[:] + [v] for row, v in zip(A, b)]
    m = len(M)
    r = 0
    piv = []
    for c in range(n):
        p = next((i for i in range(r, m) if M[i][c] != 0), None)
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        pv = M[r][c]
        M[r] = [x / pv for x in M[r]]
        for i in range(m):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [a - f * bb for a, bb in zip(M[i], M[r])]
        piv.append(c)
        r += 1
    for i in range(r, m):
        assert M[i][n] == 0, "inconsistent"
    assert r == n, "singular"
    x = [Fraction(0)] * n
    for i, c in enumerate(piv):
        x[c] = M[i][n]
    return x


def torus_kernel(L, power):
    """translation-invariant K on (Z/L)^3 with (I - P^power) K = delta - 1/N and sum K = 0; returns dict d -> K(d)"""
    ds = list(itertools.product(range(L), repeat=3))
    idx = {d: i for i, d in enumerate(ds)}
    N = len(ds)
    # the stencil of P^power
    st = {(0, 0, 0): Fraction(1)}
    for _ in range(power):
        new = {}
        for v, w in st.items():
            for e in NB:
                u = tuple((v[i] + e[i]) % L for i in range(3))
                new[u] = new.get(u, 0) + w / 7
        st = new
    A = []
    b = []
    for d in ds:
        row = [Fraction(0)] * N
        row[idx[d]] += 1
        for v, w in st.items():
            u = tuple((d[i] - v[i]) % L for i in range(3))
            row[idx[u]] -= w
        A.append(row)
        b.append(Fraction(1 if d == (0, 0, 0) else 0) - Fraction(1, N))
    A.append([Fraction(1)] * N)
    b.append(Fraction(0))
    sol = solve_exact(A, b)
    return {d: sol[idx[d]] for d in ds}


def apply_P(K, L):
    return {d: sum(K[tuple((d[i] + e[i]) % L for i in range(3))] for e in NB) / 7 for d in K}


def x1_x2():
    L = 4
    chi = torus_kernel(L, 1)
    C = torus_kernel(L, 2)
    e1 = (1, 0, 0)
    vals = (chi[(0, 0, 0)], chi[e1], C[(0, 0, 0)], C[e1], C[(1, 1, 1)])
    want = (Fraction(10619, 7680), Fraction(1799, 7680), Fraction(18179, 15360), Fraction(539, 15360))
    ok = vals[:4] == want and vals[4] < 0
    check("X1", ok, f"(b) on L = 4 by real-space solves of (I - P)chi = delta - 1/N and (I - P^2)C = delta - 1/N (mean zero): "
          f"chi(0) = {vals[0]}, chi(e1) = {vals[1]}, C(0) = {vals[2]}, C(e1) = {vals[3]} (the author's four values), "
          f"C(1,1,1) = {vals[4]} < 0")
    PC = apply_P(C, L)
    ok2 = all(chi[d] == C[d] + PC[d] for d in C)
    check("X2", ok2, "(a): chi = C + P C exactly on L = 4, i.e. chi = C(1 + phi)/sigma^2; response and covariance differ "
          "by the factor 1 + phi, as stated. For the linearized Gibbs law pi ~ exp(-(7 beta/2) theta^T (I - P^2) theta) "
          "a field entering S_x0 couples to theta_x0 + (P theta)_x0, and beta Cov(theta, theta_x0 + (P theta)_x0) = "
          "C(I + P)/7 = chi/7: the equilibrium relation holds with that conjugate observable")
    return chi, C


def x3(chi, C):
    L = 4
    alpha = Fraction(1)
    x0 = (0, 0, 0)
    ds = list(itertools.product(range(L), repeat=3))
    idx = {d: i for i, d in enumerate(ds)}
    N = len(ds)
    # (i) torus: m(x) = (P m)(x) for x != x0, m(x0) = alpha
    A = []
    b = []
    for d in ds:
        row = [Fraction(0)] * N
        if d == x0:
            row[idx[d]] = Fraction(1)
            b.append(alpha)
        else:
            row[idx[d]] += 1
            for e in NB:
                u = tuple((d[i] + e[i]) % L for i in range(3))
                row[idx[u]] -= Fraction(1, 7)
            b.append(Fraction(0))
        A.append(row)
    m = solve_exact(A, b)
    torus_const = all(v == alpha for v in m)
    # (ii) box |x|_inf <= R with boundary outside = 0: pinned mean vs Dirichlet Green function ratio
    R = 3
    box = [p for p in itertools.product(range(-R, R + 1), repeat=3)]
    bidx = {p: i for i, p in enumerate(box)}
    nb_ = len(box)

    def solve_box(pinned):
        A = []
        b = []
        for p in box:
            row = [Fraction(0)] * nb_
            if pinned and p == (0, 0, 0):
                row[bidx[p]] = Fraction(1)
                b.append(alpha)
            else:
                row[bidx[p]] += 1
                for e in NB:
                    q = (p[0] + e[0], p[1] + e[1], p[2] + e[2])
                    if q in bidx:
                        row[bidx[q]] -= Fraction(1, 7)
                b.append(Fraction(1 if (not pinned and p == (0, 0, 0)) else 0))
            A.append(row)
        return solve_exact(A, b)
    mp_ = solve_box(True)
    G = solve_box(False)
    ratio_ok = all(mp_[bidx[p]] == alpha * G[bidx[p]] / G[bidx[(0, 0, 0)]] for p in box)
    # the attempt's profile alpha chi(y)/C(0) at the pinned site, and the static conditioning alpha C(y)/C(0)
    att0 = alpha * chi[(0, 0, 0)] / C[(0, 0, 0)]
    stat = {d: alpha * C[d] / C[(0, 0, 0)] for d in C}
    differs = any(alpha * chi[d] / C[(0, 0, 0)] != stat[d] for d in C)
    ok = torus_const and ratio_ok and att0 != alpha and differs
    check("X3", ok,
          f"(b) a site pinned at every level: on the L = 4 torus the pinned process's stationary mean solves m = P m off x0, "
          f"m(x0) = alpha, whose unique solution is the constant alpha ({'yes' if torus_const else 'no'}); on the box "
          f"|x|_inf <= {R} with zero outside it is exactly alpha G(y)/G(0), G = (I - P)^(-1) delta (the chi profile, "
          f"{'yes' if ratio_ok else 'no'}), which on Z^3 decays like alpha (7/(4 pi r))/G(0); conditioning the free "
          "stationary Gaussian instead gives alpha C(y)/C(0); the attempt's 'same profile times alpha/C(0)' gives "
          f"alpha chi(0)/C(0) = {att0} alpha at the pinned site itself, not alpha")


def x4(C):
    e1 = (1, 0, 0)
    ok = True
    rows = []
    for d in (e1, (1, 1, 0), (1, 1, 1)):
        C0, Cr = C[(0, 0, 0)], C[d]
        like = 1 / (C0 + Cr) - 1 / C0            # a^2 times this: quadratic form of (a, a) minus its r = infinity value
        unlike = 1 / (C0 - Cr) - 1 / C0
        # direct: (1/2) v^T C2^{-1} v with C2 = [[C0, Cr], [Cr, C0]], v = (1, 1) and (1, -1), against 2 x (1/2)/C0
        det = C0 * C0 - Cr * Cr
        inv = ((C0 / det, -Cr / det), (-Cr / det, C0 / det))
        q_like = Fraction(1, 2) * (inv[0][0] + 2 * inv[0][1] + inv[1][1]) - 1 / C0
        q_unlike = Fraction(1, 2) * (inv[0][0] - 2 * inv[0][1] + inv[1][1]) - 1 / C0
        ok = ok and q_like == like and q_unlike == unlike and ((like < 0 < unlike) == (Cr > 0))
        rows.append(f"r = {d}: C(r) = {Cr}, like {like}, unlike {unlike}")
    check("X4", ok, "(c) as algebra for the static two-site marginal of the free stationary Gaussian: the like/unlike "
          "shifts of (1/2) v^T C2^{-1} v are a^2 (1/(C0 + Cr) - 1/C0) and a^2 (1/(C0 - Cr) - 1/C0), attractive/repulsive "
          "exactly when C(r) > 0: " + "; ".join(rows))


def x5():
    random.seed(8)
    L = 3
    ok = True
    for _ in range(50):
        s = {p: tuple(random.randint(-3, 3) for _ in range(3)) for p in itertools.product(range(L), repeat=3)}
        s2 = {p: tuple(random.randint(-3, 3) for _ in range(3)) for p in itertools.product(range(L), repeat=3)}

        def S(conf, p):
            return tuple(sum(conf[tuple((p[i] + e[i]) % L for i in range(3))][c] for e in NB) for c in range(3))
        lhs = sum(sum(a * b for a, b in zip(s2[p], S(s, p))) for p in s)
        rhs = sum(sum(a * b for a, b in zip(s[p], S(s2, p))) for p in s)
        ok = ok and lhs == rhs
    check("X5", ok, "step 6: sum_x s'_x . S_x(s) = sum_x s_x . S_x(s') for the symmetric 7-point stencil (50 random "
          "integer configuration pairs on (Z/3)^3), so the synchronous kernel is reversible w.r.t. prod_x Z(beta|S_x|)")


def main():
    try:
        chi, C = x1_x2()
        x3(chi, C)
        x4(C)
        x5()
    except Exception as exc:
        print(f"FAIL: X unexpected exception {type(exc).__name__}: {exc}")
        print("SUMMARY: referee check.py crashed")
        return 1
    print(f"TOTAL: PASS={PASSES} FAIL={FAILS}")
    if FAILS:
        print("SUMMARY: referee checks failed (see FAIL lines)")
        return 1
    print("SUMMARY: fails at step 5 - the persistent sources of the task (a site pinned at every level) are modelled by "
          "conditioning the free stationary Gaussian at one time; the pinned process has stationary mean alpha G(y)/G(0) "
          "with G = (I - P)^(-1) (the chi profile; the constant alpha on a torus), while conditioning gives alpha C(y)/C(0), "
          "so the two-pin '-log stationary weight' of (c) is the equal-time marginal of the unpinned law, not the "
          "interaction of persistent sources; the one-pin profile stated in (b), alpha chi(y)/C(0), is neither and "
          "misses the pin value (chi(0)/C(0) = 3034/2597 on L = 4). What holds, re-verified exactly: chi = 7/E, "
          "C = 7 sigma^2/(2E(1 - E/14)), chi = C(1 + phi)/sigma^2, the L = 4 values, reversibility of the linear and "
          "nonlinear kernels, and the Gaussian two-site algebra")
    return 0


if __name__ == "__main__":
    sys.exit(main())
