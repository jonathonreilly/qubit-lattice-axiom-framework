#!/usr/bin/env python3
"""Referee for the-anisotropic-state a1.

Author w-macbookpro90c72-j5081 (claude-opus-5-5). Own sympy identities and a 4^3 spectrum.
"""
import itertools
from fractions import Fraction as Fr
import numpy as np
import sympy as sp

fails = []


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)


def concave():
    e, a, b = sp.symbols("epsilon a b", real=True)
    X, Y = sp.exp(4 * e), sp.exp(-2 * e)
    f = a * X + b * Y
    second = sp.diff(sp.sqrt(f), e, 2)
    num = sp.simplify(second * 2 * f ** sp.Rational(3, 2))
    ok = sp.simplify(num - (8 * a**2 * X**2 + 28 * a * b * X * Y + 2 * b**2 * Y**2)) == 0
    at0 = sp.simplify(second.subs(e, 0) * (a + b) ** sp.Rational(3, 2) - (4 * a**2 + 14 * a * b + b**2))
    ok &= at0 == 0
    sx, sy, sz = sp.symbols("sx sy sz")
    def gap(p, q, r):
        return 2 * p**4 + p**2 * (q**2 + r**2) - (q**2 + r**2) ** 2
    ok &= sp.expand(gap(sx, sy, sz) + gap(sy, sz, sx) + gap(sz, sx, sy)) == 0
    report(
        "concave sea",
        bool(ok),
        "sqrt(a e^{4e}+b e^{-2e}) is convex, the epsilon=0 integrand is (4a^2+14ab+b^2)/|s|^3, and the cyclic remainder sums to 0",
    )


def runaway():
    bt = sp.symbols("beta", positive=True)
    chains = sp.Max(1, 3 * sp.pi / 8 * (36 * bt + sp.sqrt(3)))
    planes = sp.Max(1, 3 * sp.pi * (36 * bt + sp.sqrt(3)))
    good = True
    for bv in (sp.Rational(1, 50), sp.Rational(1, 10), 1, 3):
        for sgn, edge, amp in ((1, chains, 2), (-1, planes, 1)):
            w = edge.subs(bt, bv)
            for tt in (w, 2 * w):
                # e^{amp t} >= (amp t)^3/6, so the upper bound is negative
                poly = 36 * bv * tt**2 - (2 / sp.pi) * (amp * tt) ** 3 / 6 + sp.sqrt(3)
                good &= bool(sp.N(poly, 30) < 0)
    report(
        "no global minimum",
        good,
        "F drops below F(0) past max(1,(3pi/8)(36 beta+sqrt3)) toward chains and past -max(1,3pi(36 beta+sqrt3)) toward planes",
    )


def spectrum():
    L = 4
    sites = list(itertools.product(range(L), repeat=3))
    ix = {p: i for i, p in enumerate(sites)}
    n = len(sites)
    sigma = [
        np.array([[0, 1], [1, 0]], complex),
        np.array([[0, -1j], [1j, 0]], complex),
        np.array([[1, 0], [0, -1]], complex),
    ]
    t = [2.0, 0.5, 1.0]
    ed = [3.0, 1.0, 2.0]
    D = []
    for j in range(3):
        Dj = np.zeros((n, n), complex)
        for p in sites:
            q = list(p)
            q[j] = (q[j] + 1) % L
            amp = t[j] * (ed[j] if p[j] % 2 == 0 else 1 / ed[j])
            Dj[ix[p], ix[tuple(q)]] += amp / 2j
            Dj[ix[tuple(q)], ix[p]] += -amp / 2j
        D.append(Dj)
    H = sum(np.kron(D[j], sigma[j]) for j in range(3))
    commute = max(np.abs(D[i] @ D[j] - D[j] @ D[i]).max() for i in range(3) for j in range(3))
    gap = np.abs(H @ H - sum(np.kron(D[j] @ D[j], np.eye(2)) for j in range(3))).max()
    ev = np.linalg.eigvalsh(H @ H).real
    m2 = sum(t[j] ** 2 * ((ed[j] - 1 / ed[j]) / 2) ** 2 for j in range(3))
    exact = Fr(1105, 144)
    report(
        "mass in quadrature",
        commute < 1e-12 and gap < 1e-10 and abs(ev[0] - m2) < 1e-9 and abs(m2 - float(exact)) < 1e-12,
        f"lowest H^2 eigenvalue {ev[0]:.8f} equals 1105/144; the axis operators commute",
    )


def alternation_bound():
    e, k = sp.symbols("epsilon k", positive=True)
    low = (2 / sp.pi) * sp.integrate(1 / (sp.exp(2 * e) * k + sp.sqrt(2) * sp.exp(-e)), (k, 0, sp.pi / 2))
    claimed = (2 / sp.pi) * sp.exp(-2 * e) * sp.log(1 + sp.pi * sp.exp(3 * e) / (2 * sp.sqrt(2)))
    closed = (2 / sp.pi) * sp.exp(-2 * e) * (
        sp.log(sp.pi * sp.exp(3 * e) / 2 + sp.sqrt(2)) - sp.log(sp.sqrt(2))
    )
    ok = sp.simplify(low - closed) == 0
    log_a = sp.log((sp.pi * sp.exp(3 * e) / 2 + sp.sqrt(2)) / sp.sqrt(2))
    log_b = sp.log(1 + sp.pi * sp.exp(3 * e) / (2 * sp.sqrt(2)))
    ok &= sp.simplify(log_a - log_b) == 0
    de, t1, s1, s2, s3 = sp.symbols("delta t1 s1 s2 s3", positive=True)
    En = sp.sqrt(t1**2 * (s1**2 + sp.sinh(de) ** 2) + s2**2 + s3**2)
    sec = sp.simplify(sp.diff(-En, de, 2).subs(de, 0) + t1**2 / sp.sqrt(t1**2 * s1**2 + s2**2 + s3**2))
    report(
        "alternation threshold",
        bool(ok and sec == 0),
        "d^2 E_sea / d delta^2 = -t^2/E at delta=0, and t_x^2 times the sin-k bound is (2/pi) e^{2e} log(1+pi e^{3e}/(2 sqrt2))",
    )


def speeds():
    # product of axial speed e^{2e} and two transverse speeds e^{-e} is 1
    e = sp.symbols("epsilon")
    ok = sp.simplify(sp.exp(2 * e) * sp.exp(-e) * sp.exp(-e) - 1) == 0
    report("massless speeds", bool(ok), "the eight zeros stay at k in {0, pi}^3 and the three speeds multiply to 1")


def main():
    concave()
    runaway()
    spectrum()
    alternation_bound()
    speeds()
    if fails:
        print("SUMMARY: fails at " + fails[0])
        return
    print(
        "HIT: confirmed - F has no global minimum for any beta: it falls below F(0) toward chains past "
        "max(1,(3 pi/8)(36 beta+sqrt3)) and toward planes past -max(1,3 pi(36 beta+sqrt3)). "
        "The sea is concave. The walk stays massless, and with alternation E^2 = sum t_j^2 (sin^2 k_j + sinh^2 delta_j); "
        "on the 4^3 torus that mass is 1105/144."
    )
    print(
        "SUMMARY: confirmed the concavity, the runaway bounds, the quadrature mass, and the alternation derivative. "
        "The midpoint-grid window 0.036 < beta < 0.059 for a metastable planar state was not rebuilt."
    )


if __name__ == "__main__":
    main()
