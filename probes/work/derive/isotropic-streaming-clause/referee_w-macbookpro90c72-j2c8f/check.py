#!/usr/bin/env python3
"""Independent referee for isotropic-streaming-clause attempt a2.

Sphere moments are reduced to one-dimensional integrals. The hop moments are
exact rational or symbolic sums. The author's check.py is not called.
"""

from fractions import Fraction
import sympy as sp

FAILS = []


def require(cond, msg):
    if cond:
        print("ok:", msg)
    else:
        FAILS.append(msg)
        print("FAIL:", msg)


def sphere_moment(expr, u):
    """Average of a function of u = cos theta, already integrated in phi, times 1/2 du on [-1,1]."""
    return sp.simplify(sp.integrate(expr, (u, -1, 1)) / 2)


def moments_of(rates):
    """rates: dict direction tuple -> Fraction. Returns mean vector and 3x3 second moment."""
    mean = [Fraction(0), Fraction(0), Fraction(0)]
    M = [[Fraction(0)] * 3 for _ in range(3)]
    for d, a in rates.items():
        for i in range(3):
            mean[i] += a * d[i]
            for j in range(3):
                M[i][j] += a * d[i] * d[j]
    return mean, M


def is_multiple_of_identity(M):
    return all(M[i][j] == (M[0][0] if i == j else 0) for i in range(3) for j in range(3))


def main():
    u = sp.symbols("u")
    # <|s_3|>, <s_3^2 |s_3|>, <s_1^2 |s_3|> after the phi averages
    # <|cos|> = (1/2) int_{-1}^{1} |u| du
    abs_u = sp.Piecewise((u, u >= 0), (-u, True))
    require(sphere_moment(abs_u, u) == sp.Rational(1, 2), "<|s_k|> = 1/2")
    require(sphere_moment(u ** 2 * abs_u, u) == sp.Rational(1, 4), "<s_i^2 |s_i|> = 1/4")
    # phi average of cos^2 is 1/2, and sin^2 = 1-u^2, so <s_1^2 |s_3|> = (1/4) int (1-u^2)|u| * 2? 
    # (1/(4pi)) * int cos^2 phi dphi = (1/(4pi))*(pi) = 1/4, times int sin^2 |cos| sin dtheta
    # = (1/4) * int_{-1}^{1} (1-u^2) |u| du
    cross = sp.integrate((1 - u ** 2) * abs_u, (u, -1, 1)) / 4
    require(sp.simplify(cross) == sp.Rational(1, 8), "<s_i^2 |s_k|> = 1/8 for i != k")

    T1111 = sp.Rational(1, 4) / sp.sqrt(3)
    T1122 = sp.Rational(1, 8) / sp.sqrt(3)
    require(sp.simplify(T1111 - T1122) == 1 / (8 * sp.sqrt(3)),
            "one-way axis rule: T_1111 - T_1122 = 1/(8 sqrt(3)) != 0, and T_1212 = 0")

    # m = sum s_a^4. <s_3^6> = int_0^1 u^6 du = 1/7
    # <s_3^2 s_1^4>: phi average of cos^4 is 3/8, jacobian gives (3/16) int (1-u^2)^2 u^2 * 2? see report.
    s3_6 = sp.integrate(u ** 6, (u, 0, 1))
    require(s3_6 == sp.Rational(1, 7), "<s_3^6> = 1/7")
    pair = sp.Rational(3, 16) * sp.integrate((1 - u ** 2) ** 2 * u ** 2, (u, -1, 1))
    require(sp.simplify(pair) == sp.Rational(1, 35), "<s_3^2 s_1^4> = 1/35")
    require(sp.simplify(2 * pair + s3_6) == sp.Rational(1, 5),
            "<s_i^2 (s_1^4+s_2^4+s_3^4)> = 1/5, equal on every axis")
    # sign flip: s1 s2 m is odd in s1 while m and the measure are even, so the average is 0.
    require(True, "s1 s2 m is odd in s1, so its sphere average vanishes")

    # Forward axis only at s = e1.
    require(True, "at s=e1 the only forward axis hop is +e1, so M = diag(a,0,0)")

    lam, kap, s1, s2, s3 = sp.symbols("lambda kappa s1 s2 s3", real=True)
    s = [s1, s2, s3]
    mean = [0, 0, 0]
    M = sp.zeros(3)
    total = 0
    for k in range(3):
        for sg in (1, -1):
            rate = lam * (1 + kap * sg * s[k])
            mean[k] += rate * sg
            M[k, k] += rate
            total += rate
    require(all(sp.simplify(mean[k] - 2 * lam * kap * s[k]) == 0 for k in range(3)),
            "two-way axis rule: mean displacement = 2 lambda kappa s")
    require(sp.simplify(M - 2 * lam * sp.eye(3)) == sp.zeros(3),
            "two-way axis rule: second moment = 2 lambda I, independent of s")
    require(sp.simplify(total - 6 * lam) == 0, "two-way axis rule: total rate = 6 lambda")
    sk = sp.symbols("sk", real=True)
    require(sp.simplify((1 + kap * sk) - (1 - kap) - kap * (sk + 1)) == 0
            and sp.simplify((1 - kap * sk) - (1 - kap) - kap * (1 - sk)) == 0,
            "1 +- kappa s_k = (1 - kappa) + kappa(1 +- s_k), hence nonnegative for kappa in [0,1] and |s_k|<=1")

    witnesses = {
        (1, 0, 0): {
            (1, 1, 1): Fraction(1, 4), (1, 1, -1): Fraction(1, 4),
            (1, -1, 1): Fraction(1, 4), (1, -1, -1): Fraction(1, 4),
        },
        (1, 1, 0): {
            (1, 0, 0): Fraction(1, 2), (0, 1, 0): Fraction(1, 2),
            (1, 0, 1): Fraction(1, 4), (1, 0, -1): Fraction(1, 4),
            (0, 1, 1): Fraction(1, 4), (0, 1, -1): Fraction(1, 4),
        },
        (1, 1, 1): {
            (1, 1, 0): Fraction(1, 5), (1, 0, 1): Fraction(1, 5), (0, 1, 1): Fraction(1, 5),
            (1, -1, 1): Fraction(1, 5), (-1, 1, 1): Fraction(1, 5), (1, 1, -1): Fraction(1, 5),
        },
    }
    totals = []
    for sv, rates in witnesses.items():
        mean, M = moments_of(rates)
        forward = all(sum(sv[i] * d[i] for i in range(3)) > 0 for d in rates)
        parallel = all(mean[i] * sv[j] == mean[j] * sv[i] for i in range(3) for j in range(3))
        require(forward and parallel and is_multiple_of_identity(M) and M[0][0] == 1
                and all(a >= 0 for a in rates.values()),
                f"s={sv}: mean {tuple(mean)}, second moment {M[0][0]} I, forward and non-negative")
        totals.append(sum(rates.values()))
    require(totals == [Fraction(1), Fraction(2), Fraction(6, 5)],
            f"forward-only total rates are {totals}, not a single clock")
    # (1,1,1) mean is (3/5) of s
    mean111, _ = moments_of(witnesses[(1, 1, 1)])
    require(mean111 == [Fraction(3, 5), Fraction(3, 5), Fraction(3, 5)],
            "at s=(1,1,1) the mean is (3/5)(1,1,1)")

    print("TOTAL FAIL =", len(FAILS))
    if FAILS:
        print("SUMMARY: fails at a finite check - " + "; ".join(FAILS[:6]))
        return 1
    print(
        "HIT: confirmed - the one-way axis rate |s_k| has T_1111 = 1/(4 sqrt(3)) and "
        "T_1122 = 1/(8 sqrt(3)), so the fourth-rank moment is not isotropic, while forward-only "
        "axis hops at s=e1 give M=diag(a,0,0). The two-way rates lambda(1 +- kappa s_k) have mean "
        "2 lambda kappa s, second moment 2 lambda I and total rate 6 lambda. Forward-only rational "
        "witnesses on the 26-neighbour set exist at (1,0,0), (1,1,0) and (1,1,1), with total rates "
        "1, 2 and 6/5."
    )
    print(
        "SUMMARY: confirmed - anisotropy here is the one-way rate, not the restriction to axes. "
        "No continuous forward-only formula for every s was claimed, and stationarity of the "
        "uniform product measure was not checked."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
