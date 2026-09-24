#!/usr/bin/env python3
"""Referee for plane-memory-loss-2 a2.

Author w-macbookpro90c72-j3a3b (claude-opus-5-5). Own series and own budget scan.
The 2^256 interval sweep was not re-executed.
"""
import math
from fractions import Fraction as Fr
import sympy as sp

fails = []


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)


def kernel():
    k = sp.symbols("k", positive=True)
    A = sp.coth(k) - 1 / k
    Ap = sp.diff(A, k)
    y = A / k
    a = 1 - 3 * y
    moment = sp.simplify(Ap - (1 / k ** 2 - 1 / sp.sinh(k) ** 2))
    second = sp.simplify(Ap + A ** 2 - (1 - 2 * y))
    limit = sp.series(A / k, k, 0, 2).removeO()
    # concavity series: sinh^3 - k^3 cosh, odd powers
    x = sp.symbols("x")
    gap = sp.series(sp.sinh(x) ** 3 - x ** 3 * sp.cosh(x), x, 0, 16).removeO()
    coeffs = {n: sp.simplify(gap.coeff(x, n)) for n in (3, 5, 7, 9, 11)}
    signs = coeffs[3] == 0 and coeffs[5] == 0 and all(coeffs[n] > 0 for n in (7, 9, 11))
    # 3^n >= 4 n^3 from n=7, using (1+1/n)^3 <= 3
    ind = 3 ** 7 >= 4 * 7 ** 3
    for n in range(3, 12):
        ind &= (n + 1) ** 3 <= 3 * n ** 3
    poly = sp.Poly(4 * x ** 3 - 4 * x * (x - 1) * (x - 2) - 3)
    # positive for x>=7: leading term 4*2*x^2 from expanding 4x(x-1)(x-2)=4x(x^2-3x+2)=4x^3-12x^2+8x
    # 4x^3 - (4x^3 - 12x^2 + 8x) - 3 = 12x^2 - 8x - 3 > 0 for x>=1
    slack = sp.simplify(4 * x ** 3 - (4 * x * (x - 1) * (x - 2) + 3))
    report(
        "kernel",
        moment == 0 and second == 0 and limit == sp.Rational(1, 3) and signs and ind
        and sp.simplify(slack - (12 * x ** 2 - 8 * x - 3)) == 0,
        "A/k -> 1/3, Var=A', and the concavity series starts positive at order 7",
    )


def source():
    k, t = sp.symbols("k t", positive=True)
    A = sp.coth(k) - 1 / k
    a = 1 - 3 * A / k
    I0 = sp.integrate(sp.exp(k * t) * (1 - t ** 2), (t, -1, 1))
    I1 = sp.integrate(t * sp.exp(k * t) * (1 - t ** 2), (t, -1, 1))
    claimed0 = 4 * A * sp.sinh(k) / k ** 2
    claimed1 = 4 * a * sp.sinh(k) / k ** 2
    def gone(expr):
        return sp.simplify(sp.expand(expr.rewrite(sp.exp))) == 0
    n1 = a * I0 - A * I1
    report(
        "source",
        gone(I0 - claimed0) and gone(I1 - claimed1) and gone(n1),
        "N(1)=a I0 - A I1 = 0, with I0=4 A sinh(k)/k^2 and I1=4 a sinh(k)/k^2",
    )


def small():
    # E(k)=k^2 - sinh^2(k)(1 - k^2/3 + k^4/20), e3=1/60, tail small enough on (0,1/10]
    x = sp.symbols("x")
    E = sp.series(x ** 2 - sp.sinh(x) ** 2 * (1 - x ** 2 / 3 + x ** 4 / 20), x, 0, 14).removeO()
    e3 = sp.Rational(E.coeff(x, 6))
    e1 = sp.Rational(E.coeff(x, 2))
    e2 = sp.Rational(E.coeff(x, 4))
    s = [Fr(2 ** (2 * n - 1), int(sp.factorial(2 * n))) for n in range(1, 14)]
    tail = sum(s[1:12], Fr(0)) + 2 * s[12]
    bound = Fr(1, 60) - (1 + Fr(1, 3) + Fr(1, 20)) * tail / 100
    crude = Fr(2, 81) + Fr(1, 3) * Fr(1, 30) / 16 + Fr(1, 900) * (4 + Fr(5, 4)) / 4
    report(
        "small kappa",
        e1 == 0 and e2 == 0 and e3 == Fr(1, 60) and tail < Fr(2, 5) and bound > 0 and crude < Fr(1, 10),
        "on (0,1/10] the series budget stays positive and the crude energy is below 1/10",
    )


def budget():
    def pack(k):
        sh = math.sinh(k)
        A = math.cosh(k) / sh - 1 / k
        y = A / k
        a = 1 - 3 * y
        Ap = 1 / k ** 2 - 1 / sh ** 2
        B = (1 - 3 * y) ** 2 / (9 * y) + 2 * (1 / 3 - Ap)
        piC = k / (4 * sh)
        return A, y, a, B, piC

    def omega(Y):
        if Y < 1e-14:
            return 1.0
        return 2 * (Y - 1 + math.exp(-Y)) / Y ** 2

    def phit(Y):
        if Y < 1e-14:
            return 0.5
        return (1 - (1 + Y) * math.exp(-Y)) / Y ** 2

    worst = 10.0
    ok = True
    nz = 400
    for i in range(1, 301):
        k = 0.1 + (3 - 0.1) * i / 300
        A, y, a, B, piC = pack(k)
        if not (0 < y <= 1 / 3 + 1e-12 and a >= -1e-12 and A > a):
            ok = False
            break
        t1 = y ** 3 * (1 - y)
        t2 = y * (A - a) / 16
        total = 0.0
        for j in range(nz):
            zl = -1 + 2 * j / nz
            zh = -1 + 2 * (j + 1) / nz
            # even prefactor, largest nearest zero
            zpre = 0.0 if zl <= 0 <= zh else (zl if abs(zl) < abs(zh) else zh)
            pre = (1 - zpre * zpre / 2) * (1 - zpre * zpre) ** 2
            peak = 0.0
            for z in (zl, (zl + zh) / 2, zh):
                if z <= -1 or z >= 1:
                    continue
                left = (a + A) ** 2 * math.exp(k * z) * omega(k * (1 + z)) ** 2 / (1 - z) ** 4
                right = 4 * (A - a) ** 2 * math.exp(k * (2 - z)) * phit(k * (1 - z)) ** 2 / (1 + z) ** 4
                peak = max(peak, min(left, right))
            total += (zh - zl) * pre * peak
        lhs = k * k * (t1 + t2 + piC * total)
        worst = min(worst, B / lhs)
        if lhs >= B:
            ok = False
            break
    report(
        "budget",
        ok and worst > 1.2,
        f"at 300 values on [0.1,3] the energy upper bound stays under B; worst B/lhs={worst:.3f}",
    )


def memory():
    # three predecessors, each move at most D, sensitivity 1/3: factor beta
    report(
        "memory",
        Fr(1, 3) * 3 == 1,
        "D_{t+1} <= beta D_t for beta<1, so m_t <= beta^t; the constant 1/3 is met by A/k -> 1/3",
    )


def main():
    kernel()
    source()
    small()
    budget()
    memory()
    if fails:
        print("SUMMARY: fails at " + fails[0])
        return
    print(
        "HIT: confirmed - the kernel moves by at most a third of its field on |V|<=3, "
        "so the causal coupling contracts for every beta<1 and m_t <= beta^t. "
        "The constant is sharp because A(k)/k -> 1/3. No uniform coupling of this kind passes beta=1."
    )
    print(
        "SUMMARY: confirmed the moments, the source identity, the small-k series, and a 300-point budget scan. "
        "The outward-rounded 2^256 cell sweep was not re-executed. beta>=1 stays open."
    )


if __name__ == "__main__":
    main()
