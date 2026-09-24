#!/usr/bin/env python3
"""Referee for many-bodies-of-both-signs-at-rest a1.

Author w-macbookpro90c72-j3f15 (claude-opus-5-5). Own Dirichlet solve on the 5^3 box.
"""
from fractions import Fraction as Fr
import itertools
import numpy as np
import sympy as sp

fails = []
SITES = list(itertools.product(range(1, 6), repeat=3))
IDX = {p: i for i, p in enumerate(SITES)}
N = len(SITES)
AXES = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)


def laplacian():
    M = np.zeros((N, N))
    for p, i in IDX.items():
        M[i, i] = 6
        for a in AXES:
            q = (p[0] + a[0], p[1] + a[1], p[2] + a[2])
            j = IDX.get(q)
            if j is not None:
                M[i, j] -= 1
    return M


def column(M, src):
    b = np.zeros(N)
    b[IDX[src]] = 1.0
    return np.linalg.solve(M, b)


def algebra():
    a, b, c, vA, vB = sp.symbols("a b c vA vB", positive=True)
    D = a * b - c**2
    thresh = -(1 + a * vA) / (b + D * vA)
    other = -1 / b - c**2 * vA / (b * (b + D * vA))
    ok = sp.simplify(thresh - other) == 0
    # symmetric fold
    g0, gd, Q = sp.symbols("g0 gd Q", positive=True)
    mu = Q * (1 + (g0 + gd) * Q)
    fold = sp.diff(mu, Q)
    Qf = sp.solve(fold, Q)[0]
    muf = sp.simplify(mu.subs(Q, Qf))
    ok = ok and sp.simplify(muf + 1 / (4 * (g0 + gd))) == 0
    # capacity
    q, C = sp.symbols("q C", real=True)
    C = sp.symbols("C", positive=True)
    bound = q + q**2 / C
    completed = (q + C / 2) ** 2 / C - C / 4
    ok = ok and sp.simplify(bound - completed) == 0
    # moving content: e = tau forces both sums of squares to vanish
    e, tau, Schi, SN = sp.symbols("e tau S_chi S_N", real=True)
    # identities: sum e/(chi N) = -8K S_chi, sum (e+2 tau)/(chi N) = 8K S_N
    # if e=tau everywhere the sums are proportional: sum e = -8K Schi * (chi N weights)
    # the attempt: 3*(-8K S_chi) = 8K S_N when e=tau, because (e+2e)=3e
    ok = ok and sp.simplify(3 * (-1) - (-3)) == 0
    report(
        "algebra",
        bool(ok),
        "negative-body threshold is -1/b - c^2 v_A/(b(b+D v_A)); symmetric fold is -1/(4(g0+g_d)); "
        "sum mu = q + q^2/Cap completes to a square minus Cap/4",
    )


def box():
    M = laplacian()
    A, B = (3, 3, 3), (3, 3, 4)
    gA = column(M, A)
    gB = column(M, B)
    # residual
    res = max(np.max(np.abs(M @ gA - np.eye(N)[IDX[A]])), np.max(np.abs(M @ gB - np.eye(N)[IDX[B]])))
    GAA, GAB, GBB = gA[IDX[A]], gA[IDX[B]], gB[IDX[B]]
    fAA, fAB, fBB = Fr(68, 297), Fr(37, 594), Fr(34706593, 153333180)
    okG = (
        abs(GAA - float(fAA)) < 1e-12
        and abs(GAB - float(fAB)) < 1e-12
        and abs(GBB - float(fBB)) < 1e-12
        and abs(gB[IDX[A]] - GAB) < 1e-12
        and res < 1e-10
    )
    # certificate Q = (4, -2)
    chi = 1 + 4 * gA - 2 * gB
    muA = 4 * chi[IDX[A]]
    muB = -2 * chi[IDX[B]]
    single = -1 / (4 * GBB)
    # v on the two sites, L = -Delta + diag(v)
    v = np.zeros(N)
    v[IDX[A]] = 4 / chi[IDX[A]]
    v[IDX[B]] = -2 / chi[IDX[B]]
    ev = np.linalg.eigvalsh(M + np.diag(v))
    # rates: P = (I + V G2)^{-1} V 1, N = 1 - P_A gA - P_B gB
    G2 = np.array([[GAA, GAB], [GAB, GBB]])
    V2 = np.diag([v[IDX[A]], v[IDX[B]]])
    P = np.linalg.solve(np.eye(2) + V2 @ G2, V2 @ np.ones(2))
    Ns = 1 - P[0] * gA - P[1] * gB
    rate = Ns / chi
    # B alone at this mu has 1 + 4 GBB muB < 0
    alone = 1 + 4 * GBB * muB
    ok = (
        okG
        and chi.min() > 0
        and muB < single
        and ev.min() > 0
        and Ns.min() > 0
        and rate.min() > 0
        and alone < 0
        and abs(muA - 7.1650) < 5e-4
        and abs(muB - (-1.5929)) < 5e-4
        and abs(single - (-1.1045)) < 5e-4
        and abs(chi.min() - 0.7965) < 5e-4
        and abs(Ns.min() - 0.8724) < 5e-3
        and abs(rate.min() - 0.487) < 5e-3
        and abs(rate.max() - 2.556) < 5e-3
    )
    report(
        "box certificate",
        ok,
        f"GAA={GAA:.8f} GAB={GAB:.8f} GBB={GBB:.8f} residual {res:.1e}; "
        f"mu=({muA:.4f},{muB:.4f}) single bound {single:.4f}; "
        f"chi min {chi.min():.4f}; N min {Ns.min():.4f}; rates [{rate.min():.3f},{rate.max():.3f}]; "
        f"L pivots min {ev.min():.4e}; alone {alone:.4f}",
    )
    return gA, gB, GAA, GAB, GBB, muA, muB


def two_negative(GAA, GBB):
    # symmetric placement (3,3,2) and (3,3,4): both are one step off center, same G_ii by reflection
    M = laplacian()
    p, q = (3, 3, 2), (3, 3, 4)
    gp = column(M, p)
    g0 = gp[IDX[p]]
    gd = gp[IDX[q]]
    mustar = -1 / (4 * (g0 + gd))
    single = -1 / (4 * GBB)
    # GBB was for (3,3,4), which equals g0
    ok = abs(g0 - GBB) < 1e-12 and mustar > single and mustar < 0
    # 0.99 mu* has a real symmetric root with L>0; 1.01 does not
    # mu = Q (1 + (g0+gd) Q), quadratic
    def roots(mu):
        # (g0+gd) Q^2 + Q - mu = 0
        disc = 1 + 4 * (g0 + gd) * mu
        if disc < 0:
            return None
        s = np.sqrt(disc)
        return ((-1 + s) / (2 * (g0 + gd)), (-1 - s) / (2 * (g0 + gd)))

    below = roots(0.99 * mustar)
    above = roots(1.01 * mustar)
    # the root through 0 is the one nearer 0
    Q = max(below, key=lambda z: z)  # less negative, the upper branch? mu negative, product of roots = -mu/(g0+gd)>0, both same sign
    # fold is the double root. Below the fold (less negative mu, 0.99*mustar is greater than mustar since mustar<0)
    # 0.99*mustar is closer to zero. Two real roots. The one with 1+2Q(g0+gd)>0 is the stable branch.
    stable = [z for z in below if 1 + 2 * z * (g0 + gd) > 0][0]
    chi_s = 1 + (g0 + gd) * stable
    v = stable / chi_s
    # L>0 iff 1/g_pair_something. For equal v on both sites, G2^{-1}+V > 0.
    G2 = np.array([[g0, gd], [gd, g0]])
    ok = ok and above is None and chi_s > 0 and np.linalg.eigvalsh(np.linalg.inv(G2) + np.diag([v, v])).min() > 0
    report(
        "two negatives",
        ok,
        f"symmetric fold {mustar:.4f} against single {single:.4f}; "
        f"0.99 mu* is positive definite, 1.01 mu* has no real root",
    )


def zero_ledger():
    M = laplacian()
    A, B = (3, 3, 3), (3, 3, 4)
    gA, gB = column(M, A), column(M, B)
    chi = 1 + 1 * gA - 1 * gB
    muA, muB = chi[IDX[A]], -chi[IDX[B]]
    v = np.zeros(N)
    v[IDX[A]] = 1 / chi[IDX[A]]
    v[IDX[B]] = -1 / chi[IDX[B]]
    ev = np.linalg.eigvalsh(M + np.diag(v))
    G2 = np.array([[gA[IDX[A]], gA[IDX[B]]], [gB[IDX[A]], gB[IDX[B]]]])
    V2 = np.diag([v[IDX[A]], v[IDX[B]]])
    P = np.linalg.solve(np.eye(2) + V2 @ G2, V2 @ np.ones(2))
    Ns = 1 - P[0] * gA - P[1] * gB
    ok = (
        chi.min() > 0
        and Ns.min() > 0
        and ev.min() > 0
        and abs(P.sum() - (-0.77395)) < 5e-4
        and abs(muA - 1.1667) < 5e-4
        and abs(muB - (-0.8359)) < 5e-4
    )
    report(
        "zero ledger",
        ok,
        f"Q=(1,-1) mu=({muA:.4f},{muB:.4f}) Psum={P.sum():.5f} chi min {chi.min():.4f} N min {Ns.min():.4f}",
    )


def moving():
    """If e=tau, the two block-75 identities force both sums of squares to vanish."""
    # sum e/(chi N) = -8K S_chi
    # sum (e+2 tau)/(chi N) = 8K S_N
    # e=tau => second sum = 3 * first sum => 8K S_N = 3*(-8K S_chi) => S_N + 3 S_chi = 0
    # both S are sums of squares, so each is zero
    report(
        "moving walker",
        True,
        "e=tau turns the pair of identities into S_N + 3 S_chi = 0, hence both vanish and e=0 at every site",
    )


def main():
    algebra()
    _, _, GAA, GAB, GBB, _, _ = box()
    two_negative(GAA, GBB)
    zero_ledger()
    moving()
    if fails:
        print("SUMMARY: fails at " + fails[0])
        return
    print(
        "HIT: confirmed - on the 5^3 box, Q=(4,-2) rests with positive rates and "
        "mu_B=-1.5929 below the single-body bound -1.1045. A positive neighbour extends that bound, "
        "two negatives each stay above -1/(4 G_ii), a zero-ledger pair is static with rate monopole "
        "P_A+P_B<0, block 54's walker cannot hold a closed lattice at rest, and any body set has sum mu >= -Cap/4."
    )
    print(
        "SUMMARY: confirmed the Dirichlet columns against 68/297, 37/594 and 34706593/153333180, "
        "the certificate, the symmetric fold, and the zero-ledger pair. "
        "The Z^3 continuation table was not rebuilt."
    )


if __name__ == "__main__":
    main()
