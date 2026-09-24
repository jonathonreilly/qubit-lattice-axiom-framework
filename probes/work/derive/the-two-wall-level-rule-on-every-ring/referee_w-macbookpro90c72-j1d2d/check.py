#!/usr/bin/env python3
"""Referee for the two-wall level rule on every ring, a2.

Author w-macbookpro90c72-jc6ba (claude-opus-5-5). Own Chebyshev and ring spectra.
The floating sea on M=32 was not rebuilt.
"""
from collections import Counter

import sympy as sp

fails = []
lam, z, eps = sp.symbols("lambda z epsilon")
B = sp.Matrix([[2 * z, -1], [1, 0]])
E11 = sp.Matrix([[1, 0], [0, 0]])


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)


def U(k):
    return sp.Integer(0) if k == -1 else sp.chebyshevu(k, z)


def chebyshev():
    powers = all(
        sp.expand(B ** k - sp.Matrix([[U(k), -U(k - 1)], [U(k - 1), -U(k - 2)]])) == sp.zeros(2)
        and sp.expand(sp.trace(B ** k) - 2 * sp.chebyshevt(k, z)) == 0
        for k in range(1, 13)
    )
    trace = True
    for length in range(3, 9):
        for gap in range(1, length):
            left = sp.trace(B ** (gap - 1) * (B + eps * E11) * B ** (length - gap - 1) * (B - eps * E11)) - 2
            right = 2 * (sp.chebyshevt(length, z) - 1) - eps ** 2 * U(gap - 1) * U(length - gap - 1)
            trace &= sp.expand(left - right) == 0
    pell = all(sp.expand(sp.chebyshevt(2 * n, z) - 1 - 2 * (z ** 2 - 1) * U(n - 1) ** 2) == 0 for n in range(1, 9))
    strong, weak = sp.symbols("t_s t_w", positive=True)
    diagonal = (strong ** 2 + weak ** 2) / 4
    coupling = strong * weak / 4
    defect = (strong ** 2 - weak ** 2) / 4
    algebra = (
        sp.expand(diagonal ** 2 - 4 * coupling ** 2 - defect ** 2) == 0
        and sp.simplify(diagonal - 2 * coupling - (strong - weak) ** 2 / 4) == 0
        and sp.simplify(diagonal + 2 * coupling - (strong + weak) ** 2 / 4) == 0
    )
    report(
        "chebyshev",
        powers and trace and pell and algebra,
        "B^k matches the Chebyshev block through k=12, the two-defect trace holds for M=3..8, and D^2-4C^2=eta^2",
    )


def bonds(length, strong, weak, walls=True):
    cut = length // 2
    out = []
    for site in range(length):
        sign = 1 if site < cut or not walls else -1
        out.append(strong if sign * ((-1) ** site) == 1 else weak)
    return out


def block(rates, parity):
    length = len(rates)
    sites = [site for site in range(length) if site % 2 == parity]
    size = len(sites)
    matrix = sp.zeros(size)
    for index, site in enumerate(sites):
        matrix[index, index] = (rates[site] ** 2 + rates[(site + 1) % length] ** 2) / 4
        nxt = (index + 1) % size
        hop = -rates[(site + 1) % length] * rates[(site + 2) % length] / 4
        matrix[index, nxt] += hop
        matrix[nxt, index] += hop
    return matrix


def axis(rates):
    length = len(rates)
    shift = sp.zeros(length)
    for site in range(length):
        shift[site, (site + 1) % length] = 1
    weight = sp.diag(*rates)
    return (weight * shift - shift.T * weight) / (2 * sp.I)


def levels():
    ok = True
    for strong, weak, limit in ((sp.Rational(13, 10), sp.Rational(7, 10), 16), (sp.Rational(7, 4), sp.Rational(2, 5), 16)):
        defect = (strong ** 2 - weak ** 2) / 4
        for length in range(4, limit + 1, 4):
            walled = bonds(length, strong, weak, True)
            plain = bonds(length, strong, weak, False)
            odd, even, bare = block(walled, 1), block(walled, 0), block(plain, 1)
            size = length // 2
            bump = sp.zeros(size)
            bump[(length - 1) // 2, (length - 1) // 2] = defect
            bump[(length // 2 - 1) // 2, (length // 2 - 1) // 2] = -defect
            ok &= odd - bare - bump == sp.zeros(size)
            walled_poly, bare_poly = odd.charpoly(lam).as_expr(), bare.charpoly(lam).as_expr()
            ok &= sp.expand(even.charpoly(lam).as_expr() - walled_poly) == 0
            ok &= sp.expand(
                walled_poly * (lam - (strong - weak) ** 2 / 4) * (lam - (strong + weak) ** 2 / 4)
                - bare_poly * lam * (lam - (strong ** 2 + weak ** 2) / 2)
            ) == 0
            if length <= 8 and strong == sp.Rational(13, 10):
                full = axis(walled)
                ok &= sp.expand((full ** 2).charpoly(lam).as_expr() - walled_poly ** 2) == 0
    report(
        "levels",
        ok,
        "on rings of length 4, 8, 12 and 16 the odd block is the bare ring plus antipodal defects, and only the band edges move",
    )


def off_multiple():
    strong, weak = sp.Rational(13, 10), sp.Rational(7, 10)
    ok = True
    detail = ""
    for length in (6, 10, 14):
        walled = bonds(length, strong, weak, True)
        plain = bonds(length, strong, weak, False)
        walls = [site for site in range(length) if walled[site] == walled[(site + 1) % length]]
        walled_poly = block(walled, 1).charpoly(lam).as_expr()
        bare_poly = block(plain, 1).charpoly(lam).as_expr()
        ok &= bare_poly.subs(lam, 1) != 0
        ok &= len(walls) == 2 and walls[1] - walls[0] == length // 2
        ok &= walled_poly.subs(lam, 0) == 0
        ok &= sp.degree(sp.gcd(sp.Poly(walled_poly, lam), sp.Poly(bare_poly, lam))) == 0
        if length == 6:
            lost = {key: 2 * val for key, val in sp.roots(sp.Poly(bare_poly, lam)).items()}
            gained = {key: 2 * val for key, val in sp.roots(sp.Poly(walled_poly, lam)).items()}
            from collections import Counter
            lost_only = Counter(lost) - Counter(gained)
            gained_only = Counter(gained) - Counter(lost)
            detail = f"L=6 loses {dict(lost_only)} and gains {dict(gained_only)}"
            ok &= lost_only == Counter({sp.Rational(9, 100): 2, sp.Rational(309, 400): 4})
            ok &= gained_only == Counter({sp.Rational(387, 400): 4, 0: 2})
    delta = sp.symbols("delta", positive=True)
    plus, minus = sp.exp(delta), sp.exp(-delta)
    hyperbolic = all(
        sp.simplify((left - right).rewrite(sp.exp)) == 0
        for left, right in (
            ((plus - minus) ** 2 / 4, sp.sinh(delta) ** 2),
            ((plus + minus) ** 2 / 4, sp.cosh(delta) ** 2),
            ((plus ** 2 + minus ** 2) / 2, sp.cosh(2 * delta)),
            ((plus ** 2 - minus ** 2) / 4, sp.sinh(2 * delta) / 2),
        )
    )
    report(
        "mod4",
        ok and hyperbolic,
        "lengths 6, 10 and 14 have no bare level 1, two strong walls, and no surviving squared level; "
        + detail
        + "; t=e^(+-delta) sends sinh^2 and cosh^2 to 0 and cosh 2 delta",
    )


def main():
    chebyshev()
    levels()
    off_multiple()
    if fails:
        print("SUMMARY: fails at " + fails[0])
        return
    print(
        "HIT: confirmed - on rings whose length is a multiple of 4, the two antipodal walls are opposite defects on one sublattice, "
        "and the squared spectrum replaces (t_s-t_w)^2/4 and (t_s+t_w)^2/4 by 0 and (t_s^2+t_w^2)/2. "
        "For t=e^(+-delta) those edges are sinh^2 and cosh^2, sent to 0 and cosh 2 delta. "
        "When the length is 2 mod 4 there is no bare level 1, both walls are strong, and every squared level moves."
    )
    print(
        "SUMMARY: confirmed the Chebyshev trace, the level rule on lengths 4, 8, 12 and 16, and the 2 mod 4 obstruction. "
        "The M=32 sea and the random-bond determinant survey were not rebuilt."
    )


if __name__ == "__main__":
    main()
