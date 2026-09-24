#!/usr/bin/env python3
"""Independent referee for the persistent-record threshold in 3D, attempt a1.

The mode matrix is rebuilt from E(k) T. Characteristic polynomials are compared
to the factored forms. The author's check.py is not called.
"""

import sympy as sp

FAILS = []


def require(cond, msg):
    if cond:
        print("ok:", msg)
    else:
        FAILS.append(msg)
        print("FAIL:", msg)


def mode_matrix(phases, p):
    q = (1 - p) / 5
    a = p - q
    n = len(phases)
    E = sp.diag(*phases)
    J = sp.ones(n)
    T = a * sp.eye(n) + q * J
    return sp.simplify(E * T), a, q


def main():
    p, lam, c, s, eps = sp.symbols("p lam c s eps", real=True)
    q = (1 - p) / 5
    a = (6 * p - 1) / 5
    require(sp.simplify(a - (p - q)) == 0, "a = p - q = (6p-1)/5")
    require(sp.simplify(a + 6 * q - 1) == 0, "a + 6q = 1")

    z = sp.symbols("z")
    # Axis k = (kappa, 0, 0): phases e^{-i kappa}, e^{i kappa}, and 1 four times.
    axis_ph = [z, 1 / z, 1, 1, 1, 1]
    M_axis, _, _ = mode_matrix(axis_ph, p)
    det_axis = sp.simplify(sp.factor((lam * sp.eye(6) - M_axis).det()))
    # Claimed cubic in lambda, with c = cos kappa = (z + 1/z)/2.
    P = (lam ** 3
         - ((10 * c * p + 2 * p + 3) / 5) * lam ** 2
         + (6 * p - 1) * (2 * c * p + 8 * c + 4 * p + 1) * lam / 25
         - (6 * p - 1) ** 2 / 25)
    claimed_axis = sp.together((lam - a) ** 3 * P)
    diff_axis = sp.simplify(det_axis - claimed_axis.subs(c, (z + 1 / z) / 2))
    require(sp.together(diff_axis) == 0,
            "on the axis, det(lam I - M) = (lam - a)^3 P(lam)")

    # Body diagonal: three phases z and three 1/z.
    diag_ph = [z, z, z, 1 / z, 1 / z, 1 / z]
    M_diag, _, _ = mode_matrix(diag_ph, p)
    det_diag = sp.simplify(sp.factor((lam * sp.eye(6) - M_diag).det()))
    Q = lam ** 2 - 2 * lam * c * (3 * p + 2) / 5 + (6 * p - 1) / 5
    claimed_diag = (lam - a * z) ** 2 * (lam - a / z) ** 2 * Q
    diff_diag = sp.simplify(det_diag - claimed_diag.subs(c, (z + 1 / z) / 2))
    require(sp.together(diff_diag) == 0,
            "on the body diagonal, det = (lam - a z)^2 (lam - a/z)^2 Q(lam)")

    # Quarter discriminant of Q.
    disc4 = sp.expand((c * (3 * p + 2) / 5) ** 2 - (6 * p - 1) / 5)
    target = (9 * (1 - p) ** 2 - s ** 2 * (3 * p + 2) ** 2) / 25
    require(sp.expand(disc4.subs(c ** 2, 1 - s ** 2) - target) == 0,
            "diagonal quarter-discriminant is [9(1-p)^2 - sin^2 (3p+2)^2]/25")
    require(sp.factor(sp.expand((3 * p + 2) ** 2 - 5 * (6 * p - 1) - 9 * (1 - p) ** 2)) == 0,
            "(3p+2)^2 - 5(6p-1) = 9(1-p)^2")
    # Threshold below the zone edge iff 3(1-p)/(3p+2) < 1 iff p > 1/6.
    thr = 3 * (1 - p) / (3 * p + 2)
    require(sp.simplify(thr - 1) == sp.together((1 - 6 * p) / (3 * p + 2)),
            "the diagonal threshold is below 1 exactly when p > 1/6")
    line_thr = (1 - p) / p
    require(sp.simplify(line_thr - thr) == sp.together(2 * (1 - p) / (p * (3 * p + 2))),
            "for p in (0,1) the diagonal threshold is strictly below the line threshold (1-p)/p")

    # Line model: mu^2 - 2 p c mu + (2p - 1).
    mu = sp.symbols("mu")
    line = mu ** 2 - 2 * p * c * mu + (2 * p - 1)
    line_disc = sp.expand((p * c) ** 2 - (2 * p - 1))
    require(sp.expand(line_disc.subs(c ** 2, 1 - s ** 2) - ((1 - p) ** 2 - p ** 2 * s ** 2)) == 0,
            "line quarter-discriminant is (1-p)^2 - p^2 sin^2, so non-real iff |sin| > (1-p)/p")

    require(sp.simplify(Q.subs(lam, 0) - a) == 0, "product of the diagonal quadratic roots is a")

    # Concrete counterexample to "the algebraically larger root is at least sqrt(a)" when cos < 0.
    # p = 1/2, c = -1: roots -1 and -2/5. sqrt(a) = sqrt(2/5) > 2/5.
    Qc = sp.Poly(Q.subs({p: sp.Rational(1, 2), c: -1}), lam)
    roots = sp.roots(Qc)
    larger = max(roots)
    a_half = sp.Rational(2, 5)
    require(larger == sp.Rational(-2, 5) and larger < sp.sqrt(a_half),
            "at p=1/2, kappa=pi the algebraically larger root is -2/5, below sqrt(a)")
    mods = sorted((abs(r) for r in roots), reverse=True)
    require(mods[0] == 1 and mods[0] > sp.sqrt(a_half) > a_half,
            "the root of larger modulus is still at least sqrt(a) > a, and it is real")

    # G' bound ingredients.
    D = lam ** 2 - 2 * a * lam * c + a ** 2
    N = lam ** 2 * c - 2 * a * lam + a ** 2 * c
    require(sp.factor(sp.expand(D ** 2 - N ** 2 - (1 - c ** 2) * (lam ** 2 - a ** 2) ** 2)) == 0,
            "D^2 - N^2 = (1-c^2)(lam^2 - a^2)^2, so |N| <= D when |c|<=1 and lam>a>0")
    require(sp.factor(sp.expand(D - ((lam - a) ** 2 + 2 * a * lam * (1 - c)))) == 0,
            "D = (lam-a)^2 + 2 a lam (1-c) >= (lam-a)^2")

    # Series of the diagonal threshold.
    f = sp.asin(3 * eps / (5 - 3 * eps))
    series = f.series(eps, 0, 4).removeO()
    expect = sp.Rational(3, 5) * eps + sp.Rational(9, 25) * eps ** 2 + sp.Rational(63, 250) * eps ** 3
    require(sp.expand(series - expect) == 0,
            "kappa* = 3 eps/5 + 9 eps^2/25 + 63 eps^3/250 + O(eps^4)")
    require(sp.simplify(3 * eps / (5 - 3 * eps) - 3 * (1 - (1 - eps)) / (3 * (1 - eps) + 2)) == 0,
            "3(1-p)/(3p+2) = 3 eps/(5-3 eps)")

    # Block 96 point: p=9/10, kappa=pi/2, c=0.
    P0 = sp.Poly(sp.simplify(P.subs({p: sp.Rational(9, 10), c: 0})), lam)
    require(P0.subs(lam, sp.Rational(9, 10)) < 0 < P0.subs(lam, 1),
            "at p=9/10, kappa=pi/2: P(9/10) < 0 < P(1)")
    require(sp.discriminant(P0) < 0,
            "at that point the cubic discriminant is negative, so one real root and two non-real")

    # kappa = pi discriminant formula.
    Ppi = sp.Poly(sp.factor(P.subs(c, -1)), lam)
    disc_pi = sp.factor(sp.discriminant(Ppi))
    claimed_disc = 64 * (1 - p) ** 2 * (6 * p - 1) ** 2 * (p ** 2 + 28 * p - 4) / 15625
    require(sp.factor(sp.together(disc_pi - claimed_disc)) == 0,
            "at kappa=pi the cubic discriminant is 64(1-p)^2(6p-1)^2(p^2+28p-4)/15625")

    # Density value at k=0 is 1, and it is simple.
    M0, a0, q0 = mode_matrix([1, 1, 1, 1, 1, 1], p)
    ev = M0.eigenvals()
    require(ev.get(1, 0) == 1 and ev.get(a, 0) == 5,
            "at k=0 the spectrum is 1 once and a five times")

    print("TOTAL FAIL =", len(FAILS))
    if FAILS:
        print("SUMMARY: fails at a finite check - " + "; ".join(FAILS[:6]))
        return 1
    print(
        "HIT: confirmed - on the body diagonal the quadratic factor has quarter-discriminant "
        "[9(1-p)^2 - sin^2 kappa (3p+2)^2]/25, so its roots leave the real line exactly when "
        "|sin kappa| > 3(1-p)/(3p+2). Their modulus is sqrt(a) when they are non-real, which "
        "exceeds the modulus a of the other four multipliers. On the axes the characteristic "
        "polynomial is (lam-a)^3 times the printed cubic, and the line threshold is |sin k| > (1-p)/p."
    )
    print(
        "SUMMARY: confirmed - the diagonal threshold and the axis factorisation survive. "
        "When cos kappa < 0 and the diagonal roots are real, the algebraically larger root can "
        "lie below sqrt(a); the root of larger modulus is still at least sqrt(a), so the leading "
        "multiplier is real on that side of the threshold. Face diagonals and p <= 1/6 were not claimed."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
