#!/usr/bin/env python3
"""Referee for gravity-node-with-the-formation-kernels a1.

Author w-jonathonsmac4f50-j0b23 (claude-opus-5). Own Bessel quadratures.
The local-limit error term is not proved here.
"""
import mpmath as mp
import sympy as sp

fails = []
mp.mp.dps = 25


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)


def gaussian():
    t, r = sp.symbols("t r", positive=True)
    integ = sp.integrate((4 * sp.pi * t) ** (sp.Rational(-3, 2)) * sp.exp(-(r ** 2) / (4 * t)), (t, 0, sp.oo))
    report(
        "gaussian tail",
        sp.simplify(integ - 1 / (4 * sp.pi * r)) == 0,
        "the heat kernel integrates to 1/(4 pi r)",
    )


def angles():
    def k4(n):
        s = sum(sp.Integer(v) ** 2 for v in n)
        return sum((sp.Integer(v) ** 2 / s) ** 2 for v in n) - sp.Rational(3, 5)

    report(
        "cubic harmonic",
        k4((1, 0, 0)) == sp.Rational(2, 5)
        and k4((1, 1, 0)) == sp.Rational(-1, 10)
        and k4((1, 1, 1)) == sp.Rational(-4, 15),
        "K4 is 2/5, -1/10 and -4/15 on the axis, the face diagonal and the body diagonal",
    )


def series():
    k = sp.symbols("k", positive=True)
    A = sp.coth(k) - 1 / k
    head = sp.series(A / k, k, 0, 6).removeO()
    head_ok = sp.simplify(head - (sp.Rational(1, 3) - k ** 2 / 45 + 2 * k ** 4 / 945)) == 0
    x = sp.symbols("x")
    f = sp.cosh(x) - 1 - x ** 2 / 4 - (x / 4) * sp.sinh(x)
    ser = sp.series(f, x, 0, 14).removeO()
    coeffs = [sp.simplify(ser.coeff(x, m)) for m in range(0, 12)]
    vanish = all(coeffs[m] == 0 for m in range(0, 6))
    neg = all(coeffs[m] < 0 for m in (6, 8, 10))
    report(
        "no partial fractions",
        head_ok and vanish and neg,
        "A/k = 1/3 - k^2/45 + ... and the concavity combination is negative from order 6",
    )


def watson():
    W = mp.sqrt(6) / (32 * mp.pi ** 3) * mp.gamma(mp.mpf(1) / 24) * mp.gamma(mp.mpf(5) / 24) * mp.gamma(mp.mpf(7) / 24) * mp.gamma(mp.mpf(11) / 24)
    g0 = W / 6
    quoted = mp.mpf("0.252731009858663003")
    # Bessel integral, split so the slow tail is explicit
    def integrand(t):
        t = mp.mpf(t)
        return mp.exp(-6 * t) * mp.besseli(0, 2 * t) ** 3

    quad = mp.quad(integrand, [0, 2, 20, mp.inf])
    report(
        "onsite",
        abs(g0 - quoted) < mp.mpf("1e-18") and abs(quad - g0) < mp.mpf("1e-12"),
        f"W/6 = {g0} and the Bessel integral agrees",
    )
    return g0


def green(xs):
    ax, ay, az = xs

    def integrand(t):
        t = mp.mpf(t)
        return mp.exp(-6 * t) * mp.besseli(ax, 2 * t) * mp.besseli(ay, 2 * t) * mp.besseli(az, 2 * t)

    r2 = ax * ax + ay * ay + az * az
    peak = mp.mpf(r2) / 6
    return mp.quad(integrand, [0, peak / 4, peak, 4 * peak, mp.inf])


def tails(g0):
    rows = []
    ok = True
    for n, direction in ((8, (8, 0, 0)), (8, (6, 6, 0)), (8, (5, 5, 5)), (12, (12, 0, 0))):
        g = green(direction)
        R = mp.sqrt(sum(v * v for v in direction))
        ratio = 4 * mp.pi * R * g
        rows.append(f"{direction}:{ratio}")
        ok &= abs(ratio - 1) < mp.mpf("0.02")
    # one correction sample on the axis, r=12: c = R^2 (R G - 1/(4pi)) / K4
    g = green((12, 0, 0))
    R = mp.mpf(12)
    K = mp.mpf(2) / 5
    c = R ** 2 * (R * g - 1 / (4 * mp.pi)) / K
    target = 5 / (32 * mp.pi)
    seven = 7 * g0
    report(
        "tails",
        ok and abs(c - target) < mp.mpf("0.002") and abs(seven - 7 * mp.mpf("0.252731009858663003")) < mp.mpf("1e-16"),
        "4 pi R G is near 1 (" + ", ".join(rows) + f"); axis c(12)={c}, 5/(32 pi)={target}; chi(0)=7W/6={seven}",
    )


def bessel_id():
    def left(m, t):
        return mp.quad(lambda k: mp.exp(mp.j * m * k + 2 * t * mp.cos(k)), [0, 2 * mp.pi]) / (2 * mp.pi)

    ok = True
    for m in (0, 1, 2, 3):
        for t in (mp.mpf("0.4"), mp.mpf("1.7")):
            ok &= abs(left(m, t) - mp.besseli(m, 2 * t)) < mp.mpf("1e-12")
    report("bessel", ok, "the Fourier transform of exp(2 t cos k) is I_m(2 t) for m=0..3")


def main():
    gaussian()
    angles()
    series()
    bessel_id()
    g0 = watson()
    tails(g0)
    if fails:
        print("SUMMARY: fails at " + fails[0])
        return
    print(
        "HIT: confirmed - G(0)=W/6 with Watson's gamma product, the heat kernel integrates to 1/(4 pi r), "
        "and 4 pi R G(R) approaches 1 on the axis, the face diagonal and the body diagonal. "
        "chi=7G multiplies every constant by 7. A/k decreases from 1/3 without partial fractions."
    )
    print(
        "SUMMARY: confirmed the on-site value to 18 digits, the Bessel representation, the Gaussian tail, "
        "the three K4 values, and the approach of 4 pi R G at r=8 and r=12. "
        "The r=30 extrapolation to 5/(32 pi) was not rebuilt; the axis value at r=12 is already within 0.002. "
        "The local-limit error term was not proved."
    )


if __name__ == "__main__":
    main()
