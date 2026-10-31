#!/usr/bin/env python3 -I
"""ee1c_bound.py -- [POST-HOC, EE1-P2] the exact (C4) bound and its rounding direction.

Written AFTER ee1b_exec.py's POST-HOC block showed that EPS1_SWEEP 4.5's OWN
recommended value 9.38495112638e-45 also fails the clause at the 12-significant-
figure eta_flat that EPS1_SWEEP itself carries. Not pre-registered. Its job is
arithmetic only: find the exact bound sqrt(eta_flat/(4 C_3)) and the largest
correctly-truncated decimal below it, at each precision eta_flat is published at.

Exact integer arithmetic for the square root (isqrt on scaled integers); no
floating point decides anything.
"""
from fractions import Fraction as F
from decimal import Decimal, getcontext
from math import isqrt

getcontext().prec = 60


def D(x):
    return Decimal(x.numerator) / Decimal(x.denominator)


def exact_sqrt_floor_digits(frac, ndig):
    """Largest decimal with ndig significant digits whose value is <= sqrt(frac).

    Returns (digits_string, exponent) with value = 0.d1d2... x 10^exponent,
    computed by exact integer isqrt -- never by a float sqrt.
    """
    # sqrt(frac) = sqrt(num/den). Scale so that isqrt gives ndig+guard digits.
    num, den = frac.numerator, frac.denominator
    # find e with 10^(2e) * num/den >= 10^(2*ndig)  (so isqrt has >= ndig digits)
    e = 0
    while F(10) ** (2 * e) * frac < F(10) ** (2 * ndig):
        e += 1
    while F(10) ** (2 * e) * frac >= F(10) ** (2 * ndig + 2):
        e -= 1
    scaled = (F(10) ** (2 * e) * frac)
    r = isqrt(scaled.numerator // scaled.denominator)
    # r = floor(sqrt(10^(2e) * frac)) up to the floor of the inner division;
    # verify r^2 <= 10^(2e)*frac strictly by exact Fraction comparison, decrement if not
    while F(r) ** 2 > F(10) ** (2 * e) * frac:
        r -= 1
    return r, e


# -------------------------------------------------- the clause and its inputs
C3 = F(1)                                        # reference, TAUFLAT l.211; (a3-q) OPEN, HIST l.1669
E_PROP = F(938495112638, 10 ** 11) * F(10) ** -45     # EPS1_SWEEP 4.5
E_TAUFLAT = F(938496, 10 ** 5) * F(10) ** -45         # TAUFLAT l.408

ETAS = [
    ("TAUFLAT l.561            (3 s.f.)", F(352, 100) * F(10) ** -88),
    ("TAUFLAT l.196, l.213     (6 s.f.)", F(352310, 10 ** 5) * F(10) ** -88),
    ("EPS1_SWEEP 4.5          (12 s.f.)", F(352309230578, 10 ** 11) * F(10) ** -88),
]

print("=" * 86)
print("[POST-HOC, EE1-P2]  the exact bound eps_1 <= sqrt(eta_flat/(4 C_3)), C_3 = 1")
print("=" * 86)
print()
print("Clause (HIST l.1698 supplies the LHS, SQ's DESC-eps (iii) the RHS): 4 C_3 eps_1^2 <= eta_flat")
print()
hdr = f"{'eta_flat source':34s} {'exact bound (floor, 15 s.f.)':>34s} {'prop':>6s} {'TAUFLAT':>8s}"
print(hdr)
print("-" * len(hdr))
for nm, eb in ETAS:
    r, e = exact_sqrt_floor_digits(eb / (4 * C3), 15)
    bound_floor = F(r) * F(10) ** -e
    ok_p = 4 * C3 * E_PROP ** 2 <= eb
    ok_t = 4 * C3 * E_TAUFLAT ** 2 <= eb
    print(f"{nm:34s} {D(bound_floor):34.14E} {str(ok_p):>6s} {str(ok_t):>8s}")

print()
print("=" * 86)
print("At EPS1_SWEEP's own eta_flat, how far above the bound is each quoted value?")
print("=" * 86)
eb = ETAS[2][1]
r, e = exact_sqrt_floor_digits(eb / (4 * C3), 25)
bound = F(r) * F(10) ** -e           # a strict lower bound on sqrt(eta/(4C_3)), 25 s.f.
print()
print(f"  exact bound, truncated to 25 s.f. : {D(bound):.24E}")
for nm, v in (("EPS1_SWEEP 4.5  9.38495112638e-45", E_PROP),
              ("TAUFLAT l.408   9.38496e-45      ", E_TAUFLAT)):
    excess = v / bound - 1
    print(f"  {nm}: above the bound by {D(excess):+.4E} relative "
          f"({'FAILS' if 4 * C3 * v ** 2 > eb else 'holds'})")

print()
print("=" * 86)
print("The largest ADMISSIBLE decimal at each digit count (truncated DOWN, as a")
print("ceiling must be), at EPS1_SWEEP's 12-s.f. eta_flat:")
print("=" * 86)
print()
for nd in range(3, 14):
    r, e = exact_sqrt_floor_digits(eb / (4 * C3), nd)
    cand = F(r) * F(10) ** -e
    holds = 4 * C3 * cand ** 2 <= eb
    # display the TRUNCATED digits literally; a Decimal format would round to
    # nearest and so misreport the floor by one unit in the last place, which is
    # precisely the defect under examination here.
    ds = str(r)
    lit = f"{ds[0]}.{ds[1:]}E-45" if e - 45 + len(ds) - 1 == -45 else f"{ds[0]}.{ds[1:]}E{len(ds) - 1 - e}"
    print(f"  {nd:2d} s.f. : {lit:22s} clause {'HOLDS' if holds else 'FAILS'}"
          + ("   <-- EPS1_SWEEP 4.5 quotes ...638 here, one ulp ABOVE this floor"
             if nd == 12 else ""))

print()
print("=" * 86)
print("Why no decimal of a square root may be rounded to nearest here")
print("=" * 86)
print()
print("eps_1^cut is sqrt(eta_flat/(4 C_3)): an irrational of a 12-digit rational.")
print("A ceiling must be truncated DOWN. Rounding the 12th significant figure to")
print("nearest put TAUFLAT 9.46e-7 above its bound (EPS1_SWEEP 4.5's finding) and")
print("puts EPS1_SWEEP's own replacement above its bound too, by the amount above.")
print("The defect is not the digits; it is quoting a decimal for the thing at all.")
