#!/usr/bin/env python3
"""Independent referee for odds-field-additive-sources attempt a3.

The author's check.py is not called. Screened capacities are recomputed by an
orbit-reduced Laplacian solve. The massless ratio at separation 4 is an exact
walk count plus the Bessel tail used for the return series.
"""

from fractions import Fraction
from itertools import product
import sympy as sp

FAILS = []
NB = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))


def require(cond, msg):
    if cond:
        print("ok:", msg)
    else:
        FAILS.append(msg)
        print("FAIL:", msg)


def gelu(A, b):
    n = len(b)
    M = [A[i][:] + [b[i]] for i in range(n)]
    for c in range(n):
        piv = max(range(c, n), key=lambda r: abs(float(M[r][c])))
        if M[piv][c] == 0:
            raise ZeroDivisionError("singular Laplacian")
        M[c], M[piv] = M[piv], M[c]
        div = M[c][c]
        for r in range(c + 1, n):
            if M[r][c] == 0:
                continue
            f = M[r][c] / div
            row_r, row_c = M[r], M[c]
            for k in range(c, n + 1):
                row_r[k] -= f * row_c[k]
    x = [Fraction(0)] * n
    for i in range(n - 1, -1, -1):
        s = M[i][n]
        for k in range(i + 1, n):
            s -= M[i][k] * x[k]
        x[i] = s / M[i][i]
    return x


def rep(x, L):
    return tuple(sorted(min(c % L, (-c) % L) for c in x))


def green_orbits(L, m2):
    orbs = sorted({rep(x, L) for x in product(range(L), repeat=3)})
    idx = {o: i for i, o in enumerate(orbs)}
    n = len(orbs)
    A = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    b = [Fraction(0) for _ in range(n)]
    for o in orbs:
        i = idx[o]
        A[i][i] += 6 + m2
        for d in NB:
            y = tuple((o[k] + d[k]) % L for k in range(3))
            A[i][idx[rep(y, L)]] -= 1
        if o == (0, 0, 0):
            b[i] = Fraction(1)
    g = gelu(A, b)
    table = {o: g[idx[o]] for o in orbs}
    return lambda x: table[rep(x, L)]


def green_full(L, m2):
    sites = list(product(range(L), repeat=3))
    idx = {s: i for i, s in enumerate(sites)}
    n = len(sites)
    A = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    b = [Fraction(0) for _ in range(n)]
    for s in sites:
        i = idx[s]
        A[i][i] = 6 + m2
        for d in NB:
            y = tuple((s[k] + d[k]) % L for k in range(3))
            A[i][idx[y]] -= 1
    b[idx[(0, 0, 0)]] = Fraction(1)
    g = gelu(A, b)
    table = {s: g[idx[s]] for s in sites}
    return lambda x: table[tuple(c % L for c in x)]


def capacity(G, sites):
    n = len(sites)
    M = [[G(tuple(sites[i][k] - sites[j][k] for k in range(3)))
          for j in range(n)] for i in range(n)]
    c = gelu(M, [Fraction(1) for _ in range(n)])
    return sum(c), c


def m2_of(p, q, r):
    T = p + q + 4 * r
    l1 = Fraction(p - q, T)
    return (1 - 6 * l1) / l1


def isqrt(n):
    x = 1 << ((n.bit_length() + 1) // 2)
    while True:
        y = (x + n // x) // 2
        if y >= x:
            return x
        x = y


def sqrt_bounds(val):
    n, d = val.numerator, val.denominator
    s = isqrt(n * d)
    lo0 = Fraction(s, d) if s else Fraction(1, d + 1)
    hi = val / lo0
    for _ in range(3):
        hi = (hi + val / hi) / 2
    lo = val / hi
    require(lo * lo <= val <= hi * hi, "square-root bracket")
    return lo, hi


def atan_bounds(x, n_terms):
    s = Fraction(0)
    x2 = x * x
    term = x
    for k in range(n_terms):
        s += term
        term = -term * x2 * Fraction(2 * k + 1, 2 * k + 3)
    if term >= 0:
        return s, s + term
    return s + term, s


def return_tail(M):
    """Upper bound for sum_{m>M} p_{2m}(0), the massless return tail."""
    a_lo, _ = atan_bounds(Fraction(1, 5), 12)
    _, b_hi = atan_bounds(Fraction(1, 239), 12)
    pi_lo = 16 * a_lo - 4 * b_hi
    A0 = Fraction(2 * M + 2, 3)
    require(A0.denominator == 1, "A0 integer")
    A0 = A0.numerator
    alpha = (sqrt_bounds(Fraction(2))[1] - 1) / 2
    two_pi = 2 * pi_lo
    pref = (1 / two_pi) * (1 / sqrt_bounds(two_pi)[0])
    inv = 1 / sqrt_bounds(Fraction(A0))[0]
    term = (2 * inv + 2 * alpha * inv / A0
            + Fraction(6, 5) * alpha ** 2 * inv / A0 ** 2
            + Fraction(2, 7) * alpha ** 3 * inv / A0 ** 3)
    return 6 * (pref * term + Fraction(1, 10 ** 18))


def massless_axis_ratio(M=251):
    """Upper bound of G_rw(4,0,0) / G_rw(0). The ratio is normalization-free."""
    fac = [1]
    for i in range(1, 2 * M + 1):
        fac.append(fac[-1] * i)
    b = [1, 6]
    for n in range(2, M + 1):
        right = (2 * (2 * n - 1) * (10 * n * n - 10 * n + 3) * b[n - 1]
                 - 36 * (n - 1) * (2 * n - 1) * (2 * n - 3) * b[n - 2])
        if right % (n ** 3) != 0:
            raise RuntimeError("return recurrence")
        b.append(right // (n ** 3))
    walks = [0] * (M + 1)
    for m in range(2, M + 1):
        total = 0
        rem0 = m - 2
        fN = fac[2 * m]
        for left in range(rem0 + 1):
            denx = fac[left + 4] * fac[left]
            rem = rem0 - left
            for d in range(rem + 1):
                bb = rem - d
                total += fN // (denx * fac[d] * fac[d] * fac[bb] * fac[bb])
        walks[m] = total
    num0 = numr = 0
    p36 = 1
    for m in range(M, -1, -1):
        num0 += b[m] * p36
        numr += walks[m] * p36
        if m:
            p36 *= 36
    S0 = Fraction(num0, p36)
    Sr = Fraction(numr, p36)
    T = return_tail(M)
    return (Sr + T) / S0, S0, Sr, T


def main():
    flat = " ".join(open("docs/MINIMAL_AXIOMS_2026-06-29.md", encoding="utf-8").read().split())
    require("determined by, and varies with, the nearest-neighbor conditions" in flat,
            "Admissibility conditions a site on its neighbours")
    require("Finite additivity, a named scalar collection functional `I`, and an assigned value `I(empty)=0` are not Record axiom content" in flat,
            "finite additivity is not Record content")
    require("removed the named scalar functional `I`, finite additivity over disjoint record collections" in flat,
            "the 2026-08-13 revision removed finite additivity")
    require("A site with no record cannot be read" in flat,
            "a site with no record cannot be read")

    p, q, r = sp.symbols("p q r", positive=True)
    T = p + q + 4 * r
    l1 = (p - q) / T
    numer = sp.together(1 - 6 * l1)
    require(sp.simplify(sp.numer(sp.together(numer)) - (7 * q + 4 * r - 5 * p)) == 0,
            "1-6 l1 has numerator 7q+4r-5p")
    require(m2_of(3, 1, 2) == 0, "(3,1,2) is massless")
    screened = {(2, 1, 2): Fraction(5), (3, 1, 3): Fraction(2),
                (5, 2, 4): Fraction(5, 3), (7, 3, 5): Fraction(3, 2)}
    for t, expect in screened.items():
        got = m2_of(*t)
        require(got == expect and got > 1, f"{t}: m^2 = {got} > 1, so the screening length is below one spacing")

    # Two-point algebra, independent of the lattice.
    G0, Gd = sp.symbols("G0 Gd", positive=True)
    cap2 = 2 / (G0 + Gd)
    cap1 = 1 / G0
    ratio = sp.simplify(cap2 / (2 * cap1))
    require(sp.simplify(ratio - G0 / (G0 + Gd)) == 0, "C2/(2 C1) = G(0)/(G(0)+G(d))")
    require(sp.simplify(sp.together(ratio - sp.Rational(9, 10))
                        - (G0 - 9 * Gd) / (10 * (G0 + Gd))) == 0,
            "the ratio is at least 9/10 exactly when G(d)/G(0) <= 1/9")

    D, d, c1, kap = sp.symbols("D d c1 kappa", positive=True)
    root = sp.solve(sp.Eq(D ** 3 * c1 / d ** 3, kap * D), D)
    nonzero = [s for s in root if sp.simplify(s) != 0][0]
    require(sp.simplify(nonzero - sp.sqrt(kap) * d ** sp.Rational(3, 2) / sp.sqrt(c1)) == 0,
            "D* = sqrt(kappa) d^(3/2) / sqrt(c1), given a conductor capacity kappa D")

    print("screened tori at m^2 = 5")
    full4 = green_full(4, 5)
    orb4 = green_orbits(4, 5)
    sample = [(0, 0, 0), (1, 0, 0), (2, 0, 0), (1, 1, 0), (1, 1, 1), (2, 1, 0)]
    require(all(full4(x) == orb4(x) for x in sample),
            "L=4 orbit reduction matches the full 64-site solve")
    greens = {}
    for L in (5, 6, 7):
        G = green_orbits(L, 5)
        greens[L] = G
        C1, _ = capacity(G, [(0, 0, 0)])
        require(C1 == 1 / G((0, 0, 0)), f"L={L}: one record has capacity 1/G(0)")
        for dist in range(1, L // 2 + 1):
            C2, _ = capacity(G, [(0, 0, 0), (dist, 0, 0)])
            ident = G((0, 0, 0)) / (G((0, 0, 0)) + G((dist, 0, 0)))
            require(C2 / (2 * C1) == ident,
                    f"L={L} d={dist}: two-record identity, G(d)/G(0) = {float(G((dist, 0, 0)) / G((0, 0, 0))):.6f}")
        require(G((1, 0, 0)) / G((0, 0, 0)) < Fraction(1, 9),
                f"L={L}: adjacent screened records already meet the 10 percent test")

    G7 = greens[7]
    sites = [(i * 2, j * 2, k * 2) for i in range(3) for j in range(3) for k in range(3)]
    CN, charges = capacity(G7, sites)
    C1 = 1 / G7((0, 0, 0))
    require(CN < 27 * C1, f"L=7 N=3 spacing 2: capacity {float(CN / (27 * C1)):.4f} of 27 C1")
    center = charges[sites.index((2, 2, 2))]
    require(max(charges) > min(charges) and center == min(charges),
            "the interior record carries strictly less charge than an outer one")

    print("massless ratio at (4,0,0)")
    upper, S0, Sr, T = massless_axis_ratio(251)
    print(f"S0 = {float(S0):.6f}  Sr = {float(Sr):.6f}  T = {float(T):.6f}  upper = {float(upper):.6f}")
    require(upper <= Fraction(1, 9),
            f"massless G(4,0,0)/G(0) <= {float(upper):.4f} <= 1/9")

    print("TOTAL FAIL =", len(FAILS))
    if not FAILS:
        # The massless require passing means the author's universal sentence is false,
        # which is recorded as the verdict rather than as a passing check of their claim.
        pass
    massless_false = upper <= Fraction(1, 9) and not any("massless" in f for f in FAILS)
    other = [f for f in FAILS if "massless" not in f]
    if other or not massless_false:
        print("SUMMARY: fails at an earlier finite check - " + "; ".join((other or FAILS)[:6]))
        return 1
    print(
        "SUMMARY: fails at the massless clause of (c) - on the infinite cubic lattice "
        f"G(4,0,0)/G(0) <= {float(upper):.4f} <= 1/9, so two records four steps apart already "
        "add to within 10 percent. The axiom memo does remove finite additivity, the identity "
        "C2/(2 C1) = G(0)/(G(0)+G(d)) is exact, and at m^2 = 5 every torus L = 5, 6, 7 meets "
        "the test at separation 1. The conductor form of D* was not given a value of kappa."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
