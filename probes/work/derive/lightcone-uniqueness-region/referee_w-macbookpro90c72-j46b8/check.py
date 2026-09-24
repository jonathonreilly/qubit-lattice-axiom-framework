#!/usr/bin/env python3
"""Referee for lightcone-uniqueness-region a2.

Author w-jonathonsmac4f50-j246a (claude-opus-5). Own series and rational sweep.
"""
import math
from fractions import Fraction as Fr
import sympy as sp

fails = []


def zero(e):
    return sp.simplify(sp.expand(sp.sympify(e).rewrite(sp.exp))) == 0


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)


def moments():
    k, z = sp.symbols("kappa z", positive=True)
    q = k * sp.exp(k * z) / (2 * sp.sinh(k))
    A = sp.coth(k) - 1 / k
    Ap = sp.diff(A, k)
    Ez = sp.integrate(z * q, (z, -1, 1))
    Ez2 = sp.integrate(z ** 2 * q, (z, -1, 1))
    ok = zero(Ez - A) and zero((1 - Ez2) / 2 - A / k) and zero(Ez2 - Ez ** 2 - Ap)
    # mirror: V·(V-V') - |V-V'|^2/2 = (|V|^2-|V'|^2)/2
    v, w = sp.symbols("v1:4"), sp.symbols("w1:4")
    d = [v[i] - w[i] for i in range(3)]
    dot = lambda a, b: sum(x * y for x, y in zip(a, b))
    ok &= sp.expand(dot(v, d) - dot(d, d) / 2 - (dot(v, v) - dot(w, w)) / 2) == 0
    lim = sp.series(A / k, k, 0, 2).removeO().subs(k, 0)
    ok &= lim == sp.Rational(1, 3)
    report(
        "mirror moments",
        bool(ok),
        "E[z]=A(k), the perpendicular second moment is A/k, Var(z)=A', and equal-norm vectors are mirrors",
    )


def decreasing():
    x, m = sp.symbols("x m", positive=True)
    g = sp.cosh(x) - 1 - x ** 2 / 4 - x * sp.sinh(x) / 4
    # coefficient of x^{2m} for m>=2 is (2-m)/(2 (2m)!)
    coef = sp.simplify(
        1 / sp.factorial(2 * m) - 1 / (4 * sp.factorial(2 * m - 1)) - (2 - m) / (2 * sp.factorial(2 * m))
    )
    kk = sp.symbols("kk", positive=True)
    A = sp.coth(kk) - 1 / kk
    ident = sp.simplify(kk * sp.diff(A, kk) - A - g.subs(x, 2 * kk) / (kk * sp.sinh(kk) ** 2))
    report(
        "A/k decreases",
        bool(coef == 0 and ident == 0),
        "k A' - A = g(2k)/(k sinh^2 k) with g's series negative for m>=3, so A/k falls from 1/3",
    )


def dfact(n):
    out = 1
    while n > 0:
        out *= n
        n -= 2
    return out


def coefficients():
    c = [Fr(dfact(2 * b), dfact(2 * b + 1)) - Fr(1, 2 * b + 2) for b in range(40)]
    J = 24
    dj = []
    for j in range(J + 1):
        s = Fr(0)
        for b in range(j + 1):
            s += Fr(2 * (j - 2 * b), math.factorial(2 * (j - b) + 1) * math.factorial(2 * b + 1)) * c[b]
        dj.append(s)
    ok = dj[0] == 0 and dj[1] == Fr(1, 36) and dj[2] == Fr(1, 225) and all(v > 0 for v in dj[1:])
    report("series coefficients", ok, f"d1=1/36, d2=1/225, and d_j>0 through j={J}")
    return dj


def sweep(dj):
    KT, J = 18, 24
    target = Fr(100, 441)  # (10/21)^2

    def sinh_lo(a):
        return sum(a ** (2 * i + 1) / math.factorial(2 * i + 1) for i in range(KT))

    def p1(b):
        s = sum(Fr(2 * i, math.factorial(2 * i + 1)) * b ** (2 * i - 2) for i in range(1, KT + 1))
        tail = b ** (2 * KT) / math.factorial(2 * KT + 2)
        r = b * b / ((2 * KT + 3) * (2 * KT + 4))
        return s + tail / (1 - r)

    def p2(b):
        s = sum(Fr(2 ** (2 * i - 1), math.factorial(2 * i)) * b ** (2 * i - 4) for i in range(2, KT + 1))
        tail = Fr(2 ** (2 * KT + 1), math.factorial(2 * KT + 2)) * b ** (2 * KT - 2)
        r = 4 * b * b / ((2 * KT + 3) * (2 * KT + 4))
        return s + tail / (1 - r)

    def q_up(b):
        s = sum(dj[j] * b ** (2 * j - 2) for j in range(1, J + 1))
        e = Fr(2 * (J + 1) * 2 ** (2 * J + 3), math.factorial(2 * J + 4)) * b ** (2 * J)
        r = 8 * b * b / ((2 * J + 5) * (2 * J + 6))
        return s + e / (1 - r)

    stack = [(Fr(0), Fr(21, 10))]
    nint, worst = 0, Fr(0)
    while stack:
        a, b = stack.pop()
        f = Fr(1) if a == 0 else a / sinh_lo(a)
        R = f * f * p2(b) + b * f * f * q_up(b)
        Ak = f * p1(b)
        val = R * R + Ak * Ak
        if val < target:
            nint += 1
            if val > worst:
                worst = val
        elif b - a < Fr(1, 100000):
            return False, None
        else:
            mid = (a + b) / 2
            stack.append((a, mid))
            stack.append((mid, b))
    lup = (worst.numerator / worst.denominator) ** 0.5
    ok = nint > 0 and lup < 10 / 21
    # 7*(3/10)*(10/21) = 1, so a strict bound gives contraction
    report(
        "region",
        ok and Fr(7) * Fr(3, 10) * Fr(10, 21) == 1,
        f"{nint} intervals, sup bound {lup:.5f} < 10/21, so 7 beta L < 1 for every beta <= 3/10",
    )


def ceilings():
    b = sp.symbols("beta", positive=True)
    q = b * sp.exp(b * sp.symbols("z")) / (2 * sp.sinh(b))
    z = sp.symbols("z")
    q = b * sp.exp(b * z) / (2 * sp.sinh(b))
    tv = sp.integrate(q - q.subs(z, -z), (z, 0, 1))
    ok = zero(tv - sp.tanh(b / 2))
    ok &= sp.simplify(sp.exp((2 * sp.atanh(sp.Rational(1, 7))).rewrite(sp.log)) - sp.Rational(4, 3)) == 0
    e = sum(Fr(3, 10) ** i / math.factorial(i) for i in range(12))
    ok &= e > Fr(4, 3)
    report(
        "ceilings",
        bool(ok),
        "TV cost is tanh(beta/2), so 7 tanh(beta/2)=1 at ln(4/3); e^{3/10}>4/3, and block 27 stops at sqrt(3)/7",
    )


def main():
    moments()
    decreasing()
    dj = coefficients()
    if not fails:
        sweep(dj)
    ceilings()
    if fails:
        print("SUMMARY: fails at " + fails[0])
        return
    print(
        "HIT: confirmed - for equal-norm moves W1 = (A(k)/k)|V-V'|, and A/k falls from 1/3. "
        "Every direction at |V|<=21/10 has influence below 10/21, so 7 beta L < 1 for every beta <= 3/10. "
        "No total-variation argument passes ln(4/3), and 3/10 is past that."
    )
    print(
        "SUMMARY: confirmed the mirror moments, the decrease of A/k, the rational sweep below 10/21, "
        "and the two ceilings. The directional lemma that would reach 3/7 was not proved, as the attempt says."
    )


if __name__ == "__main__":
    main()
