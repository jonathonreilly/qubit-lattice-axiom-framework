#!/usr/bin/env python3
"""plane-memory-loss-2, attempt a1 (w-jonathonsmac4f50-jd237): the checks behind ATTEMPT.md.

Object (block 26, PR #8170): records s_(x,t) in S^2 on Z^2 x {0, 1, 2, ...}, level 0 aligned (s = e3), each later record drawn from
vMF(beta S), S = s_(x,t-1) + s_(x-e1,t-1) + s_(x-e2,t-1) (the three predecessors); in Z^3 coordinates X = (i, j, t - i - j) the
predecessors of X are X - e_a.  A(k) = coth k - 1/k.  The claim tested: route A's step 'the path-space relative entropy of a
space-time twist is <= C beta theta0^2 / sum_{k<T} P_k' (which would give m_t -> 0).  Result: for every deterministic site-wise rotation
field the path-space relative entropy is bounded BELOW by c_beta times the space-time XY energy of the twist, and that energy is
>= theta0^2/(pi^2 E_T) with E_T < 2 (a Polya-urn flow on the backward cone): the route's bound fails for large T.

 F1  vMF: log-normalizer psi(eta) = log(4 pi sinh k / k), k = |eta|; f = log(sinh k/k) has f' = A, f'' = A'; (radial Hessian: eigenvalues A' along eta, A/k across)
 F2  A(k)/k is decreasing: sign of (A/k)' = sign of cosh u - 1 - u^2/4 - (u/4) sinh u (u = 2k), whose u^{2m} coefficient is 0 (m = 1) and
     (1/(2m-1)!)(1/(2m) - 1/4) < 0 (m >= 2)
 F3  A' is decreasing: A'' = 2(k^3 cosh k - sinh^3 k)/(k^3 sinh^3 k) and sinh^3 k - k^3 cosh k = sum_m c_m k^{2m+1}, c_1 = c_2 = 0, c_m > 0 (m >= 3)
     (closed form; induction 3^{2m+3} - 3 >= 9(3^{2m+1} - 3) and 32m^2 - 28m - 6 >= 0)
 F4  the equal-concentration identity KL(vMF(k u) || vMF(k u')) = k A(k)(1 - u.u') (Bregman form), and M = I - R_w (axis e1):
     M^T M = 4 sin^2(w/2) (projection onto span(e2, e3))
 G1  the Polya urn (one ball per colour) is uniform on the compositions of each depth, and its edge flows form a unit flow from the apex
     of the backward cone to level 0 (exact, T <= 30)
 G2  the flow's energy E_T exactly, T = 1..40, and E_T <= 2T/(T+1) < 2
 G3  the exact effective resistance R_T between the apex and level 0 in the backward cone (T <= 9): R_T <= E_T (Thomson)
 G4  the constants: c_beta = 2 beta^2 A'(3b)(A(3b)/(3b) + A'(3b)) against 2 beta A(3 beta) (level 1) and 2 beta^2 (the upper bound)
 N1  (numerical, labelled) a Monte Carlo of the exact per-site relative entropies for two twists on the T = 3 cone at beta = 1.5, 3:
     c_beta X <= H <= 2 beta^2 X holds for the estimates
"""
import itertools
import math
import random
import sys
import time
from fractions import Fraction as F
from math import comb

import sympy as sp

FAILS = []
T0 = time.time()


def check(label, ok, detail):
    print(f"{'ok  ' if ok else 'FAIL'} {label}: {detail}")
    if not ok:
        FAILS.append(label)


# ================================================================================================ F: the Langevin function
def section_F():
    print("=" * 110)
    print("F  the von Mises-Fisher facts used")
    k, u, w = sp.symbols("k u w", positive=True)
    A = sp.coth(k) - 1 / k
    Ap = 1 / k ** 2 - 1 / sp.sinh(k) ** 2
    f = sp.log(sp.sinh(k) / k)
    ok1 = sp.simplify(sp.diff(f, k) - A) == 0 and sp.simplify(sp.diff(A, k) - Ap) == 0
    phi = sp.symbols("phi", positive=True)
    Z = sp.integrate(sp.exp(k * sp.cos(phi)) * 2 * sp.pi * sp.sin(phi), (phi, 0, sp.pi))
    ok1 &= sp.simplify(Z - 4 * sp.pi * sp.sinh(k) / k) == 0
    check("F1", ok1, "int_{S^2} e^{k s.e} ds = 4 pi sinh k / k; f = log(sinh k/k) has f' = A = coth k - 1/k and f'' = A' = 1/k^2 - 1/sinh^2 k "
          "(so the Hessian of the log-normalizer is A'(|eta|) along eta and A(|eta|)/|eta| across)")
    # F2
    lhs = sp.simplify((k * sp.diff(A, k) - A) * k * sp.sinh(k) ** 2 - (2 * sp.sinh(k) ** 2 - k ** 2 - k * sp.sinh(k) * sp.cosh(k)))
    ok2 = sp.simplify(sp.expand(sp.expand_trig(lhs.rewrite(sp.exp)))) == 0
    g = sp.cosh(u) - 1 - u ** 2 / 4 - (u / 4) * sp.sinh(u)
    ok2 &= sp.simplify((2 * sp.sinh(k) ** 2 - k ** 2 - k * sp.sinh(k) * sp.cosh(k)) - g.subs(u, 2 * k)).rewrite(sp.exp).simplify() == 0
    ser = sp.series(g, u, 0, 42).removeO()
    coeffs_ok = all(sp.Rational(ser.coeff(u, 2 * m)) == (0 if m == 1 else sp.Rational(1, sp.factorial(2 * m - 1)) * (sp.Rational(1, 2 * m) - sp.Rational(1, 4)))
                    for m in range(1, 21)) and all(ser.coeff(u, 2 * m + 1) == 0 for m in range(0, 20))
    ok2 &= coeffs_ok
    check("F2", ok2, "(A/k)' has the sign of 2 sinh^2 k - k^2 - k sinh k cosh k = g(2k), g(u) = cosh u - 1 - u^2/4 - (u/4) sinh u, whose u^{2m} "
          "coefficient is 0 at m = 1 and (1/(2m-1)!)(1/(2m) - 1/4) < 0 for m >= 2 (checked through u^40, general by the closed form): A(k)/k "
          "decreases from 1/3; hence A'(k) <= A(k)/k and A(k) <= k/3")
    # F3
    App = sp.diff(Ap, k)
    ok3 = sp.simplify((App - 2 * (k ** 3 * sp.cosh(k) - sp.sinh(k) ** 3) / (k ** 3 * sp.sinh(k) ** 3)).rewrite(sp.exp)) == 0
    h = sp.sinh(k) ** 3 - k ** 3 * sp.cosh(k)
    serh = sp.series(h, k, 0, 62).removeO()

    def c_m(m):
        return sp.Rational(3 ** (2 * m + 1) - 3, 4 * sp.factorial(2 * m + 1)) - (sp.Rational(1, sp.factorial(2 * m - 2)) if m >= 1 else 0)
    ok3 &= all(serh.coeff(k, 2 * m + 1) == c_m(m) for m in range(0, 30)) and all(serh.coeff(k, 2 * m) == 0 for m in range(0, 31))
    ok3 &= c_m(1) == 0 and c_m(2) == 0 and all(c_m(m) > 0 for m in range(3, 30))
    mm = sp.Symbol("m", positive=True, integer=True)
    q = 4 * (2 * mm + 1) * (2 * mm) * (2 * mm - 1)
    ok3 &= sp.expand(9 * q - q.subs(mm, mm + 1) - 4 * (2 * mm + 1) * (32 * mm ** 2 - 28 * mm - 6)) == 0
    ok3 &= all(32 * m ** 2 - 28 * m - 6 > 0 for m in range(2, 4)) and (3 ** 7 - 3) >= 4 * 7 * 6 * 5
    check("F3", ok3, "A'' = 2(k^3 cosh k - sinh^3 k)/(k^3 sinh^3 k) and sinh^3 k - k^3 cosh k = sum_m c_m k^{2m+1} with c_m = (3^{2m+1} - 3)/(4(2m+1)!) "
          "- 1/(2m-2)!: c_1 = c_2 = 0, c_m > 0 for m >= 3 (through m = 29 exactly; in general 3^{2m+1} - 3 >= 4(2m+1)(2m)(2m-1) =: q(m) by "
          "induction from m = 3 (2184 >= 840), since 9q(m) - q(m+1) = 4(2m+1)(32m^2 - 28m - 6) > 0): A' decreases from A'(0) = 1/3")
    # F4
    kk = sp.Symbol("kappa", positive=True)
    th = sp.Symbol("theta", real=True)
    AA = sp.coth(kk) - 1 / kk
    psi = lambda v: sp.log(sp.sinh(sp.sqrt(v.dot(v))) / sp.sqrt(v.dot(v)))
    a = sp.Matrix([0, 0, kk])
    b = sp.Matrix([kk * sp.sin(th), 0, kk * sp.cos(th)])
    breg = psi(b) - psi(a) - (AA * a / kk).dot(b - a)
    ok4 = sp.simplify(sp.expand(sp.simplify(breg - kk * AA * (1 - sp.cos(th))))) == 0
    R = sp.Matrix([[1, 0, 0], [0, sp.cos(w), -sp.sin(w)], [0, sp.sin(w), sp.cos(w)]])
    M = sp.eye(3) - R
    ok4 &= sp.simplify(M.T * M - 4 * sp.sin(w / 2) ** 2 * sp.diag(0, 1, 1)) == sp.zeros(3, 3)
    check("F4", ok4, "KL(vMF(k u) || vMF(k u')) = psi(k u') - psi(k u) - grad psi(k u).(k u' - k u) = k A(k)(1 - u.u') (the GIVEN (3)); and for R_w "
          "the rotation about e1, (I - R_w)^T (I - R_w) = 4 sin^2(w/2) diag(0, 1, 1): I - R_w is 2|sin(w/2)| times an orthogonal map on span(e2, e3)")


# ================================================================================================ G: the flow and the capacity of the cone
def compositions(d):
    return [(a, b, d - a - b) for a in range(d + 1) for b in range(d + 1 - a)]


def polya_flow_energy(T, check_flow=False):
    E = F(0)
    ok = True
    for d in range(T):
        Pd = F(1, comb(d + 2, 2))
        for n in compositions(d):
            out = [F(n[a] + 1, d + 3) * Pd for a in range(3)]
            E += sum(x * x for x in out)
            if check_flow:
                ok &= sum(out) == Pd
                if d >= 1:
                    inflow = sum(F(n[a], d + 2) * F(1, comb(d + 1, 2)) for a in range(3) if n[a] >= 1)
                    ok &= inflow == Pd
    return E, ok


def urn_uniform(dmax):
    law = {(0, 0, 0): F(1)}
    ok = True
    for d in range(dmax):
        new = {}
        for n, p in law.items():
            for a in range(3):
                m = list(n); m[a] += 1
                new[tuple(m)] = new.get(tuple(m), F(0)) + p * F(n[a] + 1, d + 3)
        law = new
        ok &= all(v == F(1, comb(d + 3, 2)) for v in law.values()) and len(law) == comb(d + 3, 2)
    return ok


def cone_resistance(T):
    """exact effective resistance between the apex n = 0 and the level |n| = T of the backward cone {n in Z^3_{>=0}, |n| <= T}, edges n ~ n + e_a"""
    verts = [n for d in range(T) for n in compositions(d)]
    idx = {n: i for i, n in enumerate(verts)}
    N = len(verts)
    rows = [dict() for _ in range(N)]
    rhs = [F(0)] * N
    for n in verts:
        i = idx[n]
        nb = [tuple(n[b] + (1 if b == a else 0) for b in range(3)) for a in range(3)]
        nb += [tuple(n[b] - (1 if b == a else 0) for b in range(3)) for a in range(3) if n[a] >= 1]
        rows[i][i] = F(len(nb))
        for m in nb:
            if sum(m) < T:
                j = idx[m]
                rows[i][j] = rows[i].get(j, F(0)) - 1
    rhs[idx[(0, 0, 0)]] = F(1)
    # sparse Gaussian elimination
    for c in range(N):
        piv = rows[c][c]
        for r in range(c + 1, N):
            if c in rows[r]:
                fac = rows[r][c] / piv
                for j, v in rows[c].items():
                    rows[r][j] = rows[r].get(j, F(0)) - fac * v
                    if rows[r][j] == 0:
                        del rows[r][j]
                rhs[r] -= fac * rhs[c]
    x = [F(0)] * N
    for c in range(N - 1, -1, -1):
        s = rhs[c] - sum(v * x[j] for j, v in rows[c].items() if j > c)
        x[c] = s / rows[c][c]
    return x[idx[(0, 0, 0)]]


def section_G():
    print("=" * 110)
    print("G  the Polya-urn flow on the backward cone and its energy; exact effective resistances")
    ok1 = urn_uniform(30)
    okf = all(polya_flow_energy(T, check_flow=True)[1] for T in (1, 2, 5, 12, 30))
    check("G1", ok1 and okf, "the Polya urn with one ball of each colour is uniform on the C(d+2, 2) compositions of every depth d <= 30, and the "
          "edge flows f(n -> n + e_a) = (n_a + 1)/((d + 3) C(d + 2, 2)) conserve flow at every vertex (T = 1, 2, 5, 12, 30): a unit flow from the "
          "apex p = (0, T) of the backward cone to level 0 along predecessor steps X -> X - e_a")
    Es = {T: polya_flow_energy(T)[0] for T in range(1, 41)}
    ok2 = all(Es[T] <= F(2 * T, T + 1) for T in Es) and all(Es[T] < Es[T + 1] for T in range(1, 40))
    check("G2", ok2, f"the flow's energy E_T (exact) increases with T and satisfies E_T <= 2T/(T + 1) < 2: E_1 = {Es[1]}, E_2 = {Es[2]}, E_3 = {Es[3]}, "
          f"E_10 = {float(Es[10]):.6f}, E_40 = {float(Es[40]):.6f} (the depth-d term is at most 1/C(d + 2, 2))")
    Rs = {}
    for T in range(1, 10):
        Rs[T] = cone_resistance(T)
    ok3 = all(Rs[T] <= Es[T] for T in Rs) and all(Rs[T] < Rs[T + 1] for T in range(1, 9))
    check("G3", ok3, "the exact effective resistance R_T between the apex and level 0 of the backward cone (unit conductances) satisfies R_T <= E_T "
          "(Thomson) and increases: " + ", ".join(f"R_{T} = {float(Rs[T]):.6f}" for T in (1, 2, 3, 5, 7, 9)) + f" (R_1 = {Rs[1]}, R_2 = {Rs[2]})")
    return Es, Rs


# ================================================================================================ constants
def Afun(x):
    return 1 / math.tanh(x) - 1 / x


def Apfun(x):
    return 1 / x ** 2 - 1 / math.sinh(x) ** 2


def c_beta(b):
    k = 3 * b
    return 2 * b * b * Apfun(k) * (Afun(k) / k + Apfun(k))


def section_const():
    print("=" * 110)
    print("G4  the constants of the two-sided bound")
    rows = []
    ok = True
    for b in (0.1, 0.5, 1, 1.5, 3, 6, 12, 24):
        cb = c_beta(b)
        lev1 = 2 * b * Afun(3 * b)
        ok &= cb <= (4 / 9) * Afun(3 * b) ** 2 * (1 + 1e-12) and cb < lev1 and lev1 <= 2 * b * b * (1 + 1e-12)
        rows.append(f"beta = {b}: c_beta = {cb:.6g} (2/(27 beta) = {2 / (27 * b):.4g}), level-1 coefficient 2 beta A(3 beta) = {lev1:.4g}, upper 2 beta^2 = {2 * b * b:.4g}")
    check("G4", ok, "(evaluated in floating point; the inequalities themselves are proved in ATTEMPT.md S5 from F2-F3) c_beta <= (4/9) A(3 beta)^2 "
          "< 2 beta A(3 beta) <= 2 beta^2: " + "; ".join(rows))


# ================================================================================================ N1: Monte Carlo (numerical, labelled)
def vmf_sample(rng, eta):
    kap = math.sqrt(eta[0] ** 2 + eta[1] ** 2 + eta[2] ** 2)
    if kap < 1e-12:
        z = 2 * rng.random() - 1
    else:
        U = rng.random()
        z = 1 + math.log(U + (1 - U) * math.exp(-2 * kap)) / kap
    ph = 2 * math.pi * rng.random()
    r = math.sqrt(max(0.0, 1 - z * z))
    loc = (r * math.cos(ph), r * math.sin(ph), z)
    if kap < 1e-12:
        return loc
    m = (eta[0] / kap, eta[1] / kap, eta[2] / kap)
    # rotate e3 to m
    a = (-m[1], m[0], 0.0)
    s = math.sqrt(a[0] ** 2 + a[1] ** 2)
    c = m[2]
    if s < 1e-12:
        return loc if c > 0 else (loc[0], -loc[1], -loc[2])
    ax = (a[0] / s, a[1] / s, 0.0)
    v = loc
    dotp = ax[0] * v[0] + ax[1] * v[1]
    cr = (ax[1] * v[2], -ax[0] * v[2], ax[0] * v[1] - ax[1] * v[0])
    return tuple(v[i] * c + cr[i] * s + ax[i] * dotp * (1 - c) for i in range(3))


def logZ(kap):
    if kap < 1e-8:
        return kap * kap / 6
    return kap + math.log1p(-math.exp(-2 * kap)) - math.log(2 * kap)   # log(sinh k / k)


def kl_vmf(a, b):
    ka = math.sqrt(sum(x * x for x in a)); kb = math.sqrt(sum(x * x for x in b))
    Aa = (1 / math.tanh(ka) - 1 / ka) if ka > 1e-8 else ka / 3
    grad = [Aa * x / ka for x in a] if ka > 1e-8 else [x / 3 for x in a]
    return logZ(kb) - logZ(ka) - sum(g * (y - x) for g, x, y in zip(grad, a, b))


def rot1(w, v):
    c, s = math.cos(w), math.sin(w)
    return (v[0], c * v[1] - s * v[2], s * v[1] + c * v[2])


def section_N(Es):
    print("=" * 110)
    print("N1  (numerical, labelled) Monte Carlo of the path relative entropy of two twists on the T = 3 cone")
    T = 3
    verts = [n for d in range(T + 1) for n in compositions(d)]         # depth d = T - level
    rng = random.Random(20260919)
    out = []
    ok = True
    for beta in (1.5, 3.0):
        for name, prof in (("apex only", lambda n: 1.0 if sum(n) == 0 else 0.0), ("linear in level", lambda n: (T - sum(n)) / T)):
            th0 = 1.0
            theta = {n: th0 * prof(n) for n in verts}
            X = 0.0
            for n in verts:
                if sum(n) < T:
                    for a in range(3):
                        m = tuple(n[b] + (1 if b == a else 0) for b in range(3))
                        X += math.sin((theta[n] - theta[m]) / 2) ** 2
            nsamp = 20000
            acc = 0.0
            for _ in range(nsamp):
                s = {n: (0.0, 0.0, 1.0) for n in verts if sum(n) == T}
                for d in range(T - 1, -1, -1):
                    for n in compositions(d):
                        preds = [tuple(n[b] + (1 if b == a else 0) for b in range(3)) for a in range(3)]
                        S = [sum(s[m][i] for m in preds) for i in range(3)]
                        s[n] = vmf_sample(rng, [beta * x for x in S])
                        aa = [beta * x for x in rot1(theta[n], S)]
                        bsum = [0.0, 0.0, 0.0]
                        for m in preds:
                            r = rot1(theta[m], s[m])
                            bsum = [bsum[i] + r[i] for i in range(3)]
                        acc += kl_vmf(aa, [beta * x for x in bsum])
            H = acc / nsamp
            lo, hi = c_beta(beta) * X, 2 * beta * beta * X
            ok &= lo <= H <= hi
            out.append(f"beta {beta}, {name}: X = {X:.4f}, c_beta X = {lo:.4f} <= H = {H:.4f} <= 2 beta^2 X = {hi:.3f}")
    check("N1", ok, "(Monte Carlo, 20000 paths each, labelled numerical) " + "; ".join(out))


def main():
    section_F()
    Es, Rs = section_G()
    section_const()
    section_N(Es)
    print("=" * 110)
    print(f"runtime {time.time() - T0:.0f}s")
    if FAILS:
        print(f"SUMMARY: ROUTE FAILS AT {FAILS[0]} (check failures: {FAILS})")
        return 0
    core = ("route A's step A2 (a path-space relative-entropy bound C beta theta0^2/sum_{k<T} P_k for a space-time twist) is false: for every "
            "beta > 0, T >= 1 and every twist theta(x, t) about an axis orthogonal to e3 with theta = 0 on level 0 and theta(0, T) = theta0 in "
            "[-pi, pi], the relative entropy H of the rotated formation law on the backward cone C(p), p = (0, T), satisfies c_beta X <= H <= "
            "2 beta^2 X, X = sum over predecessor edges of sin^2(dtheta/2), c_beta = 2 beta^2 A'(3 beta)(A(3 beta)/(3 beta) + A'(3 beta)) "
            "(~ 2/(27 beta) at large beta, ~ 4 beta^2/9 at small beta); and X >= theta0^2/(pi^2 E_T), E_T <= 2T/(T+1) < 2 the energy of the "
            "Polya-urn flow on C(p) (the space-time graph is Z^3; exact cone resistances R_1..R_9 = 1/3 .. 0.626). Hence H >= c_beta theta0^2/(2 pi^2) "
            "for every T while the proposed bound tends to 0; the lower bound extends to every deterministic SO(3)-valued rotation field with "
            "theta0 the tilt of R_p e3. m_t -> 0 itself is not decided here")
    print("SUMMARY: ROUTE FAILS AT A2 (the path-space relative-entropy bound of route A); " + core)
    print("HIT: " + core)
    return 0


if __name__ == "__main__":
    sys.exit(main())
