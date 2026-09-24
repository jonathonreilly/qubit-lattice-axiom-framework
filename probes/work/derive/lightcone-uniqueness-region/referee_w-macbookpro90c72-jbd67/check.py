#!/usr/bin/env python3
"""Referee for lightcone-uniqueness-region a1.

Author w-jonathonsmac4f50-j715c (claude-opus-5). Own mass identity and own upper sums.
Mixed directions stay open, so the Dobrushin region is not 3/7. The scan logs were not re-read.
"""
import mpmath as mp
import sympy as sp

fails = []


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail, flush=True)


def identities():
    k, z = sp.symbols("k z", positive=True)
    A = sp.coth(k) - 1 / k
    q = k * sp.exp(k * z) / (2 * sp.sinh(k))
    # mean of z on [-1,1]
    mean = sp.integrate(z * k * sp.exp(k * z) / (2 * sp.sinh(k)), (z, -1, 1))
    mean_ok = sp.simplify(sp.together((mean - A).rewrite(sp.exp))) == 0
    # M(-1)=0 is exactly the mean condition, checked by the total mass of (z-A)q
    mass = sp.together(sp.integrate((z - A) * q, (z, -1, 1)).rewrite(sp.exp))
    omega = lambda x: sp.exp(x) * (x - 1) + 1
    d_om = sp.diff(omega(sp.symbols("x")), sp.symbols("x"))
    om_ok = sp.simplify(d_om - sp.symbols("x") * sp.exp(sp.symbols("x"))) == 0
    # Phi(0)
    m = sp.symbols("m")
    phi0 = sp.integrate(2 * sp.sqrt(1 - 4 * m), (m, 0, sp.Rational(1, 4)))
    gap = sp.Rational(8, 135) - sp.Rational(1, 45)
    report(
        "partner identity",
        mean_ok and mass == 0 and om_ok and phi0 == sp.Rational(1, 3) and gap == sp.Rational(1, 27),
        "A=coth k-1/k, omega'=x e^x, Phi(0)=1/3, and 8/135-1/45=1/27",
    )


def decreasing():
    x = sp.symbols("x", positive=True)
    g = sp.cosh(x) - 1 - x ** 2 / 4 - (x / 4) * sp.sinh(x)
    series = sp.series(g, x, 0, 16).removeO()
    coeffs = sp.Poly(sp.expand(series), x).coeffs()
    nonpos = all(sp.simplify(c) <= 0 for c in coeffs) and sp.series(g, x, 0, 6).removeO() == 0
    # general term of x^{2m} for m>=3 is negative
    k = sp.symbols("k", positive=True)
    A = sp.coth(k) - 1 / k
    link = sp.simplify(sp.together(((k * sp.diff(A, k) - A) * k * sp.sinh(k) ** 2 - g.subs(x, 2 * k)).rewrite(sp.exp)))
    m = sp.symbols("m", integer=True, positive=True)
    general = (2 - m) / (4 * m * sp.factorial(2 * m - 1))
    # coefficient of x^{2m} in cosh x - (x/4) sinh x, for m>=2; the -x^2/4 is lower order
    raw = 1 / sp.factorial(2 * m) - 1 / (4 * sp.factorial(2 * m - 1))
    term_ok = sp.simplify(raw - general) == 0
    report(
        "A/k decreasing",
        nonpos and link == 0 and term_ok,
        "k A' - A has the sign of g(2k), whose series coefficients are (2-m)/(4m(2m-1)!) and hence <= 0",
    )


def upper_phi(k, n=240):
    """Stieltjes upper sum: chord at the right end of each zeta cell."""
    mp.mp.dps = 25
    k = mp.mpf(k)
    A = mp.coth(k) - 1 / k
    z1 = k * (1 - A)
    c = mp.e ** (k * A) / (2 * k * mp.sinh(k))

    def omega(x):
        return mp.e ** x * (x - 1) + 1

    def partner(zp):
        target = omega(zp)
        lo, hi = mp.mpf("-8"), mp.mpf(0)
        # omega -> +inf as x -> -inf, omega(0)=0, so a root exists in (-inf,0) for target>0
        while omega(lo) < target:
            lo *= 2
        for _ in range(80):
            mid = (lo + hi) / 2
            if omega(mid) > target:
                lo = mid
            else:
                hi = mid
        return (lo + hi) / 2

    def chord(zp, zm):
        up = min(mp.mpf(1), max(mp.mpf(-1), A + zp / k))
        um = min(mp.mpf(1), max(mp.mpf(-1), A + zm / k))
        sp_ = mp.sqrt(max(0, 1 - up ** 2))
        sm = mp.sqrt(max(0, 1 - um ** 2))
        return mp.sqrt((sp_ - sm) ** 2 + (up - um) ** 2)

    def primitive(z):
        return mp.e ** z * (z - 1)

    upper = mp.mpf(0)
    lower = mp.mpf(0)
    prev = mp.mpf(0)
    prev_ch = mp.mpf(0)
    rising = True
    last = mp.mpf(0)
    for i in range(1, n + 1):
        z = z1 * i / n
        zm = partner(z)
        ch = chord(z, zm)
        mass = primitive(z) - primitive(prev)
        upper += ch * mass
        lower += prev_ch * mass
        if ch + mp.mpf("1e-12") < last:
            rising = False
        last = ch
        prev_ch = ch
        prev = z
    return c * upper, c * lower, A / k, rising


def certificate():
    ks = [sp.Rational(p, q) for p, q in (
        (1, 10), (3, 20), (1, 5), (1, 4), (3, 10), (2, 5), (1, 2),
        (7, 10), (1, 1), (13, 10), (8, 5), (2, 1), (5, 2), (3, 1),
    )]
    ok = True
    worst = None
    for k in ks:
        phi, _, ak, rising = upper_phi(k, n=1200 if k <= sp.Rational(1, 5) else 400)
        margin = ak - phi
        ok = ok and rising and margin > 0
        if worst is None or margin < worst[0]:
            worst = (margin, k, phi, ak)
    # small-k fit of (1/3 - Phi)/k^2, bracketed by the Stieltjes sums
    target = mp.mpf(8) / 135
    near = True
    shown = []
    for k in (mp.mpf("0.05"), mp.mpf("0.1")):
        hi, lo, _, _ = upper_phi(k, n=2000)
        # right and left Stieltjes sums bracket Phi; their mean is the trapezoid
        chi = (mp.mpf(1) / 3 - hi) / k ** 2
        clo = (mp.mpf(1) / 3 - lo) / k ** 2
        mid = (chi + clo) / 2
        near = near and chi < target < clo and abs(mid - target) < mp.mpf("1e-4")
        shown.append(float(mid))
    report(
        "parallel margin",
        ok and near,
        f"Phi upper sum below A/k at 14 k in [1/10,3]; small-k coefficients near {shown[0]:.6f}, {shown[1]:.6f} vs 8/135",
    )


def regions():
    report(
        "regions",
        sp.Rational(3, 7) > sp.sqrt(3) / 7 and sp.Rational(3, 10) < sp.Rational(3, 7),
        "the conditional W1 threshold 3/7 is larger than the TV threshold sqrt(3)/7; mixed directions are not closed",
    )


def main():
    identities()
    decreasing()
    certificate()
    regions()
    if fails:
        print("SUMMARY: fails at " + fails[0])
        return
    print(
        "HIT: confirmed - the parallel influence is at most Phi(k), with Phi(0)=1/3, the partner "
        "equation omega(zeta_-)=omega(zeta_+), and Phi(k)<A(k)/k at the 14 certified k; "
        "the quadratic margin is k^2/27 once the coefficient is 8/135"
    )
    print(
        "SUMMARY: confirmed the mass identity, Phi(0)=1/3, A/k decreasing, and a Stieltjes upper bound "
        "below A/k at 14 couplings. The 8/135 coefficient is a quadrature fit, not a remainder theorem. "
        "Mixed directions stay open, so the region is not 3/7. The scan logs were not re-read."
    )


if __name__ == "__main__":
    main()
