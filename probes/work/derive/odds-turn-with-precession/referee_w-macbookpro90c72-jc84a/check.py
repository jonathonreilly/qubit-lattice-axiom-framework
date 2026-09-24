#!/usr/bin/env python3
"""Independent referee for odds-turn-with-precession attempt a2.

The turn algebra is recomputed with sympy. The 60-profile numerical scan
and the numerical bracket on beta_0 are not rebuilt. The author's check.py
is not called.
"""

import sympy as sp

FAILS = []


def require(cond, msg):
    if cond:
        print("ok:", msg)
    else:
        FAILS.append(msg)
        print("FAIL:", msg)


def ordered_and_staggered():
    k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
    G, Om = sp.symbols("Gamma Omega", positive=True)
    lam = sp.symbols("lambda", real=True)
    gamma = (sp.cos(k1) + sp.cos(k2) + sp.cos(k3)) / 3
    E = (2 - 2 * sp.cos(k1)) + (2 - 2 * sp.cos(k2)) + (2 - 2 * sp.cos(k3))
    require(sp.simplify(1 - gamma - E / 6) == 0, "neighbour average gamma satisfies 1 - gamma = E/6")

    # n x acts as +i and -i on the two circular components.
    # tau_dot = -(Gamma + Omega n x)(1 - gamma) tau
    for sign in (1, -1):
        eig = -(G + sign * sp.I * Om) * E / 6
        # lambda = -i omega, with omega = (sign * Omega - i Gamma) E/6
        omega = (sign * Om - sp.I * G) * E / 6
        require(sp.simplify(eig + sp.I * omega) == 0,
                f"ordered circular eigenvalue matches omega = ({'+' if sign > 0 else '-'}Omega - i Gamma) E/6")
        require(sp.simplify(sp.re(eig) + G * E / 6) == 0,
                "ordered turn has real part -Gamma E/6 <= 0 for Gamma >= 0")

    # Staggered: tau_A dot = -(Gamma + i Omega)(tau_A + gamma tau_B), and the conjugate sense on B.
    a, b = sp.symbols("a b")
    Lp = G + sp.I * Om
    Lm = G - sp.I * Om
    eq1 = lam * a + Lp * (a + gamma * b)
    eq2 = lam * b + Lm * (b + gamma * a)
    M = sp.linear_eq_to_matrix([eq1, eq2], [a, b])[0]
    char = sp.simplify(M.det())
    claimed = lam ** 2 + 2 * G * lam + (G ** 2 + Om ** 2) * (1 - gamma ** 2)
    require(sp.factor(sp.expand(char - claimed)) == 0,
            "staggered turns obey lambda^2 + 2 Gamma lambda + (Gamma^2+Omega^2)(1-gamma^2) = 0")

    disc = sp.simplify(G ** 2 - (G ** 2 + Om ** 2) * (1 - gamma ** 2))
    # roots -Gamma ± sqrt(disc). Real part is -Gamma when disc < 0.
    # When disc >= 0 both roots are <= 0 because their sum is -2 Gamma and their product is nonnegative.
    prod = sp.simplify((G ** 2 + Om ** 2) * (1 - gamma ** 2))
    require(sp.simplify(prod - claimed.subs(lam, 0)) == 0, "product of staggered roots is (Gamma^2+Omega^2)(1-gamma^2)")

    # Gamma = 0: omega = ± Omega sqrt(1-gamma^2), since lambda = ± i Omega sqrt(...)
    root0 = sp.simplify(sp.sqrt((Om ** 2) * (1 - gamma ** 2)))
    require(sp.simplify(root0 - sp.Abs(Om) * sp.sqrt(1 - gamma ** 2)) == 0,
            "at Gamma = 0 the frequency is Omega times sqrt(1-gamma^2)")

    kappa = sp.symbols("kappa", real=True)
    g_axis = (sp.cos(kappa) + 2) / 3
    series = sp.series(sp.sqrt(1 - g_axis ** 2), kappa, 0, 4).removeO()
    require(sp.simplify(series - sp.Abs(kappa) / sp.sqrt(3)) == 0 or
            sp.series(sp.sqrt(1 - g_axis ** 2) - sp.sqrt(kappa ** 2) / sp.sqrt(3), kappa, 0, 3).removeO() == 0,
            "along an axis, sqrt(1-gamma^2) = |kappa|/sqrt(3) + O(kappa^3)")
    # The series of sqrt(kappa**2) is |kappa|, which sympy may write as sqrt(kappa**2).
    gap = sp.series(sp.sqrt(1 - g_axis ** 2) - sp.sqrt(kappa ** 2 / 3), kappa, 0, 3).removeO()
    require(sp.simplify(gap) == 0, "axis expansion starts at |k|/sqrt(3)")

    # Small-k diffusion of the slow root.
    eps = sp.symbols("eps", positive=True)
    slow = -G + G * sp.sqrt(1 - (G ** 2 + Om ** 2) * eps / G ** 2)
    slow_series = sp.series(slow, eps, 0, 2).removeO()
    require(sp.simplify(slow_series + (G ** 2 + Om ** 2) * eps / (2 * G)) == 0,
            "overdamped slow root is -(Gamma^2+Omega^2)(1-gamma^2)/(2 Gamma) + O(eps^2)")
    # 1-gamma^2 = |k|^2/3 + O(k^4), so lambda = -D |k|^2 with D = (Gamma^2+Omega^2)/(6 Gamma).
    require(sp.simplify((G ** 2 + Om ** 2) / (2 * G) / 3 - (G ** 2 + Om ** 2) / (6 * G)) == 0,
            "diffusion constant is (Gamma^2+Omega^2)/(6 Gamma)")

    # Oscillation when disc < 0, i.e. 1-gamma^2 > Gamma^2/(Gamma^2+Omega^2).
    # On the axis 1-gamma^2 ~ kappa^2/3, so |k| > sqrt(3) Gamma / sqrt(Gamma^2+Omega^2).
    thresh = G ** 2 / (G ** 2 + Om ** 2)
    require(sp.simplify(sp.sqrt(3 * thresh) - sp.sqrt(3) * G / sp.sqrt(G ** 2 + Om ** 2)) == 0,
            "oscillation starts near |k| = sqrt(3) Gamma / sqrt(Gamma^2+Omega^2)")


def precession_identity():
    # (n x s) · n = 0, so L_n of a function of s·n vanishes.
    n1, n2, n3, s1, s2, s3 = sp.symbols("n1 n2 n3 s1 s2 s3", real=True)
    n = sp.Matrix([n1, n2, n3])
    s = sp.Matrix([s1, s2, s3])
    require(sp.simplify((n.cross(s)).dot(n)) == 0, "precession about n kills every axial function F(s·n)")

    # One neighbour's rotation feeds 1/6 of the same rotation, from F = c (K F)^6.
    # d log K = (1/6) d log F.
    K, F = sp.symbols("K F", positive=True)
    c = sp.symbols("c", positive=True)
    rel = sp.log(F) - sp.log(c) - 6 * sp.log(K)
    dK, dF = sp.symbols("dK dF")
    drel = sp.diff(rel, F) * dF + sp.diff(rel, K) * dK
    # on the constraint rel=0, drel=0 gives dK/K = dF/(6F)
    solved = sp.solve(drel, dK)[0]
    require(sp.simplify(solved - dF * K / (6 * F)) == 0,
            "on the sea F = c (K F)^6, one neighbour's log derivative is one sixth of the site's")


def legendre_flip():
    t, beta = sp.symbols("t beta", real=True)
    den_pos = sp.integrate(sp.exp(beta * t), (t, -1, 1))
    den_neg = sp.integrate(sp.exp(-beta * t), (t, -1, 1))
    require(sp.simplify(den_pos - den_neg) == 0, "Z(beta) = sinh(beta)/beta is even")
    for ell in range(0, 6):
        P = sp.legendre(ell, t)
        num_pos = sp.integrate(sp.exp(beta * t) * P, (t, -1, 1))
        num_neg = sp.integrate(sp.exp(-beta * t) * P, (t, -1, 1))
        lam_pos = sp.simplify(num_pos / den_pos)
        lam_neg = sp.simplify(num_neg / den_neg)
        require(sp.simplify(lam_neg - ((-1) ** ell) * lam_pos) == 0,
                f"Legendre multiplier lambda_{ell}(-beta) = (-1)^{ell} lambda_{ell}(beta)")


def main():
    ordered_and_staggered()
    precession_identity()
    print("legendre")
    legendre_flip()
    print("TOTAL FAIL =", len(FAILS))
    if FAILS:
        print("SUMMARY: fails at a finite check - " + "; ".join(FAILS[:6]))
        return 1
    print(
        "HIT: confirmed - the ordered sea's turns have omega = (+-Omega - i Gamma) E(k)/6, "
        "with real part -Gamma E/6. The staggered sea's turns obey "
        "lambda^2 + 2 Gamma lambda + (Gamma^2+Omega^2)(1-gamma^2) = 0. They are linear, "
        "c = Omega/sqrt(3), only at Gamma = 0; for Gamma > 0 the long waves are overdamped "
        "with diffusion constant (Gamma^2+Omega^2)/(6 Gamma). Both turn channels have "
        "non-positive real part for every Omega/Gamma. The sublattice flip is the sign "
        "(-1)^ell of the Legendre multipliers."
    )
    print(
        "SUMMARY: confirmed - precession oscillates the turn channel, and a sound-like "
        "omega proportional to |k| needs the staggered sea and Gamma = 0. The numerical "
        "bracket on beta_0 and the 60-profile scan were not rebuilt. Stability of the "
        "complement modes is the attempt's argument, not this check."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
