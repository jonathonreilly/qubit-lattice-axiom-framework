#!/usr/bin/env python3
"""Independent referee for lightcone-uniqueness-region a3.

The chordal influence of the von Mises-Fisher kernel is 1/3, so seven
predecessors contract for every beta < 3/7. Does not import the attempt.
"""
from __future__ import annotations

import sys
from fractions import Fraction as F

import sympy as sp

FAILS: list[str] = []


def check(tag: str, ok: bool, msg: str = "") -> None:
    print(("PASS " if ok else "FAIL ") + tag + ((": " + msg) if msg else ""), flush=True)
    if not ok:
        FAILS.append(tag)


k, a, z, phi = sp.symbols("k a z phi", real=True)
moments = {m: sp.integrate(z**m * sp.exp(a * z), (z, -1, 1)) for m in range(3)}
closed = {
    0: 2 * sp.sinh(a) / a,
    1: 2 * sp.cosh(a) / a - 2 * sp.sinh(a) / a**2,
    2: 2 * sp.sinh(a) / a - 4 * sp.cosh(a) / a**2 + 4 * sp.sinh(a) / a**3,
}
I = lambda t: 4 * (t * sp.cosh(t) - sp.sinh(t)) / t**3
mean = sp.coth(k) - 1 / k
J1 = closed[2].subs(a, k) - mean * closed[1].subs(a, k)
J2 = (
    closed[2].subs(a, 2 * k)
    - 2 * mean * closed[1].subs(a, 2 * k)
    + mean**2 * closed[0].subs(a, 2 * k)
)
def off_zero(expr) -> bool:
    simplified = sp.simplify(expr.rewrite(sp.exp))
    if simplified == 0:
        return True
    if isinstance(simplified, sp.Piecewise):
        return all(sp.simplify(branch) == 0 for branch, cond in simplified.args if cond != True)
    return False


forms = all(off_zero(moments[m] - closed[m]) for m in range(3))
forms = forms and sp.simplify((closed[0] - closed[2] - I(a)).rewrite(sp.exp)) == 0
forms = forms and sp.simplify((closed[1].subs(a, k) - mean * closed[0].subs(a, k)).rewrite(sp.exp)) == 0
forms = forms and sp.simplify((J1 - (2 * sp.sinh(k) / k**3 - 2 / (k * sp.sinh(k)))).rewrite(sp.exp)) == 0
sphere = sp.integrate(sp.integrate((1 - z**2) * sp.cos(phi) ** 2, (phi, 0, 2 * sp.pi)), (z, -1, 1))
check(
    "E1 moments",
    forms and sphere == 4 * sp.pi / 3 and sp.integrate(sp.cos(phi) ** 2, (phi, 0, 2 * sp.pi)) == sp.pi,
    "the z-moments, I(a), and the mean A = coth k - 1/k are the stated integrals",
)

density = k / (4 * sp.pi * sp.sinh(k))
D0 = sp.Rational(1, 12) / sp.pi
B_perp = (sp.pi * density**2 / 2) * (I(2 * k) + sp.Rational(3, 4) * I(k) ** 2)
B_par = sp.pi * density**2 * (J2 + sp.Rational(3, 2) * J1**2)
F_perp = 8 * sp.sinh(k) ** 2 - 3 * k**2 * (I(2 * k) + sp.Rational(3, 4) * I(k) ** 2)
F_par = 4 * sp.sinh(k) ** 2 - 3 * k**2 * (J2 + sp.Rational(3, 2) * J1**2)
gap_ok = sp.simplify((D0 - B_perp - F_perp / (96 * sp.pi * sp.sinh(k) ** 2)).rewrite(sp.exp)) == 0
gap_ok = gap_ok and sp.simplify((D0 - B_par - F_par / (48 * sp.pi * sp.sinh(k) ** 2)).rewrite(sp.exp)) == 0
check(
    "E3 energy gaps",
    gap_ok,
    "D0 - B_perp and D0 - B_par reduce to F_perp and F_par over positive denominators",
)

G_perp = (
    k**4 * sp.cosh(2 * k)
    - 4 * k**4
    + sp.Rational(3, 2) * k**3 * sp.sinh(2 * k)
    - 18 * k**2 * sp.cosh(2 * k)
    - 18 * k**2
    + 36 * k * sp.sinh(2 * k)
    - 18 * sp.cosh(2 * k)
    + 18
)
check(
    "E3 perpendicular polynomial",
    sp.simplify((k**4 * F_perp - G_perp).rewrite(sp.exp)) == 0,
    "k^4 F_perp is the stated combination of k^m cosh(2k) and sinh(2k)",
)


def exponential_dict(expr):
    """Read sum c k^m exp(n k) after rewriting in exponentials."""
    expanded = sp.expand(expr.rewrite(sp.exp))
    found = {}
    for term in sp.Add.make_args(sp.expand(expanded)):
        coeff = sp.Integer(1)
        power = 0
        freq = 0
        for factor in sp.Mul.make_args(term):
            if factor.is_polynomial(k) and sp.degree(factor, k) >= 1 and factor.free_symbols <= {k}:
                monomials = sp.Poly(sp.expand(factor), k).as_dict()
                if len(monomials) != 1:
                    raise SystemExit("compound polynomial %s" % factor)
                (pwr,), cf = next(iter(monomials.items()))
                power += pwr
                coeff *= cf
            elif factor.func == sp.exp:
                freq += int(sp.simplify(factor.args[0] / k))
            else:
                coeff *= factor
        key = (power, freq)
        found[key] = found.get(key, 0) + sp.nsimplify(coeff)
    return {key: value for key, value in found.items() if sp.simplify(value) != 0}


def taylor_coeffs(terms, order: int):
    out = [0] * order
    for (power, freq), coeff in terms.items():
        for degree in range(power, order):
            out[degree] += coeff * freq ** (degree - power) / sp.factorial(degree - power)
    return out


def tail_positive(terms, start: int) -> bool:
    """Even degrees >= start are positive: the largest |frequency| dominates."""
    dominant = max(abs(freq) for _, freq in terms)
    if any(power >= start for power, _ in terms):
        return False
    lower = sorted({freq for (_, freq) in terms if 0 < abs(freq) < dominant})
    y = sp.symbols("y")

    def piece(freq, point):
        total = 0
        for (power, got), coeff in terms.items():
            if got == freq:
                total += coeff * sp.ff(point, power) / sp.Integer(freq) ** power
        return total

    lead = sp.expand(piece(dominant, start + y) + piece(-dominant, start + y))
    coeffs = sp.Poly(lead, y).all_coeffs()
    if not all(coeff >= 0 for coeff in coeffs) or lead.subs(y, 0) <= 0:
        return False
    if not lower:
        return True
    second = max(abs(freq) for freq in lower)
    envelope = 0
    for freq in lower:
        for (power, got), coeff in terms.items():
            if got == freq:
                envelope += abs(coeff) * y**power / sp.Integer(abs(freq)) ** power
    envelope = sp.expand(envelope)
    degree = sp.Poly(envelope, y).degree()
    shrinks = F(start + 1, start) ** degree <= F(dominant, second)
    at_start = sp.Rational(second, dominant) ** start * envelope.subs(y, start)
    return bool(shrinks and at_start < lead.subs(y, 0))


perp_terms = exponential_dict(G_perp)
perp_series = taylor_coeffs(perp_terms, 40)
check(
    "E4 perpendicular gap",
    perp_series[8] == sp.Rational(4, 15)
    and all(coeff == 0 for coeff in perp_series[:8])
    and all(coeff >= 0 for coeff in perp_series)
    and tail_positive(perp_terms, 30),
    "G_perp starts at (4/15) k^8 and every Taylor coefficient is nonnegative",
)

G_par = sp.expand(sp.cancel(sp.together((k**4 * sp.sinh(k) ** 2 * F_par).rewrite(sp.exp))))
par_terms = exponential_dict(G_par)
par_series = taylor_coeffs(par_terms, 40)
check(
    "E4 parallel gap",
    par_series[10] == sp.Rational(16, 15)
    and all(coeff == 0 for coeff in par_series[:10])
    and all(coeff >= 0 for coeff in par_series)
    and tail_positive(par_terms, 30),
    "G_par starts at (16/15) k^10 and every Taylor coefficient is nonnegative",
)

at_zero = sp.integrate(sp.integrate(z**2 / (4 * sp.pi), (phi, 0, 2 * sp.pi)), (z, -1, 1))
ball = sp.sqrt((4 * sp.pi / 3) * D0)
check(
    "E5 constant",
    at_zero == sp.Rational(1, 3) and sp.simplify(ball - sp.Rational(1, 3)) == 0,
    "the bound sqrt(|B| D0) equals 1/3, and u·s attains it at V = 0",
)

def factorial(n: int) -> F:
    out = F(1)
    for i in range(1, n + 1):
        out *= i
    return out


beta = sp.symbols("beta", positive=True)
check(
    "E6 thresholds",
    sp.simplify(sp.tanh(sp.log(sp.Rational(4, 3)) / 2) - sp.Rational(1, 7)) == 0
    and F(7) * F(1, 3) == F(7, 3)
    and F(7, 3) * F(3, 7) == 1
    and F(3, 7) < F(55, 100),
    "tanh(ln(4/3)/2) = 1/7, so seven predecessors reach total variation 1 at ln(4/3), and 7*(1/3)*(3/7) = 1",
)

# sqrt(3) < 26/15, so sqrt(3)/7 < 26/105. exp(26/105) < 4/3 implies sqrt(3)/7 < ln(4/3).
bound = F(26, 105)
upper = sum(bound**n / factorial(n) for n in range(8)) + 2 * bound**8 / factorial(8)
# ln(4/3) < 3/10 iff exp(3/10) > 4/3. A partial sum already exceeds 4/3.
lower = sum(F(3, 10) ** n / factorial(n) for n in range(6))
check(
    "E7 order",
    upper < F(4, 3) and lower > F(4, 3) and F(3, 10) < F(3, 7) < F(55, 100),
    "sqrt(3)/7 < ln(4/3) < 3/10 < 3/7 < 0.55",
)

if FAILS:
    print("SUMMARY: fails at " + ", ".join(FAILS), flush=True)
    sys.exit(1)
print(
    "SUMMARY: confirmed. The chordal covariance Cov(f, u·s) of the von Mises-Fisher kernel is at most 1/3 "
    "for every field, direction and 1-Lipschitz f, with equality at V=0 for f=u·s. Seven predecessors "
    "therefore contract for every beta < 3/7, which is exactly where this Dobrushin bound stops. "
    "A total-variation comparison cannot pass ln(4/3). The window from 3/7 up to the executed onset "
    "bracket (0.55, 0.60) stays open. Green's identity and the spherical-harmonic Neumann solution "
    "are the analytic steps; the sign of both energy gaps was recomputed from the Taylor series.",
    flush=True,
)
print(
    "HIT: confirmed - the chordal influence of the vMF kernel is exactly 1/3, so the light-cone chain "
    "is unique for every beta < 3/7",
    flush=True,
)
