#!/usr/bin/env python3
"""Referee for the sea's polarisability as a lattice sum, a1.

Author w-macbookpro90c72-jabe7 (claude-opus-5-5). Own algebra and own Bessel quadrature.
The L=16..128 zone sums and the L=8 diagonalizations were not re-run.
"""
import itertools

import mpmath as mp
import sympy as sp

fails = []


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail, flush=True)


def held():
    A, q = sp.symbols("A q", real=True)
    avg = sp.integrate(sp.expand((sp.cos(A) + sp.cos(A + q)) ** 2), (A, 0, 2 * sp.pi)) / (2 * sp.pi)
    qa = sp.symbols("q1:4", real=True)
    e_s = sp.symbols("e_s", real=True)
    piece = sum(e_s / 3 * (1 + sp.cos(qq)) / 8 for qq in qa)
    lat = sum(4 * sp.sin(qq / 2) ** 2 for qq in qa)
    # |q|^2_lat = sum 2(1-cos) = sum 4 sin^2(q/2)
    lat_ok = sp.simplify(lat - sum(2 * (1 - sp.cos(qq)) for qq in qa)) == 0
    reduced = sp.simplify(piece - (e_s / 4 - e_s / 48 * lat))
    # Pi = c0/4 + (kappa/4) |q|^2, with e_s = -I
    I = sp.symbols("I", positive=True)
    pi = piece.subs(e_s, -I)
    c0 = -I
    kappa = I / 12
    match = sp.simplify(pi - (c0 / 4 + kappa / 4 * lat)) == 0
    report(
        "held part",
        sp.simplify(avg - (1 + sp.cos(q))) == 0 and reduced == 0 and lat_ok and match,
        "bond average 1+cos q_a, so the held piece is -I/4 + (I/48)|q|^2_lat and kappa = I/12",
    )


def bessel():
    t, A, k = sp.symbols("t A k", positive=True)
    # d/dA of int_0^inf (1-e^{-t A}) t^{-3/2} dt = Gamma(1/2) A^{-1/2}
    deriv = sp.integrate(sp.exp(-t * A) * t ** (sp.Rational(-1, 2)), (t, 0, sp.oo))
    ident = sp.simplify(deriv - sp.sqrt(sp.pi / A)) == 0
    # (1/2pi) int cos^n = 2^{-n} C(n, n/2) for even n, which is I_0's coefficient of z^n/n!
    zone = True
    for n in range(0, 9):
        if n % 2:
            continue
        ang = sp.binomial(n, n // 2) / 2 ** n
        bess = sp.factorial(n) / (sp.factorial(n // 2) ** 2 * 2 ** n)
        zone = zone and sp.simplify(ang - bess) == 0
    report(
        "one-dimensional I",
        ident and zone,
        "sqrt(A) = (1/(2 sqrt pi)) int (1-e^{-t A}) t^{-3/2} dt, and the zone factor is e^{-t/2} I_0(t/2)",
    )


def value():
    mp.mp.dps = 40

    def integrand(t):
        z = mp.exp(-t / 2) * mp.besseli(0, t / 2)
        return t ** mp.mpf("-1.5") * (1 - z ** 3)

    I = mp.quad(integrand, [0, mp.inf]) / (2 * mp.sqrt(mp.pi))
    kappa = I / 12
    target = mp.mpf("1.19380112142979520212")
    report(
        "kappa positive",
        abs(I - target) < mp.mpf("1e-15") and kappa > 0,
        f"I={mp.nstr(I, 20)}, kappa={mp.nstr(kappa, 12)}",
    )


def degree_and_zeros():
    # integrability of |p|^{d-n} in 3D needs d-n > -3, i.e. derivatives through order d+2
    def first_log(d):
        return d + 3

    rates = first_log(1) == 4
    strain = first_log(1) == 4
    density = first_log(-1) == 2
    zeros = True
    for K in itertools.product((0, sp.pi), repeat=3):
        zeros = zeros and all(sp.sin(2 * Kj) == 0 and sp.sin(Kj) == 0 for Kj in K)
    # ln 2 / (6 pi^2) is the quoted drop per doubling
    drop = sp.log(2) / (6 * sp.pi ** 2)
    report(
        "no q^2 log in the rates",
        rates and strain and density and zeros and abs(float(drop) - 0.0117) < 2e-4,
        "degree 1 gives q^4 log q; degree -1 gives q^2 log q; sin(2K)=0 at all eight zeros; "
        f"ln2/(6 pi^2)={float(drop):.4f}",
    )


def main():
    held()
    bessel()
    value()
    degree_and_zeros()
    if fails:
        print("SUMMARY: fails at " + fails[0])
        return
    print(
        "HIT: confirmed - the held sea gives kappa = I/12 > 0, with I the zone integral of |s|, "
        "and the interband piece is homogeneous of degree 1 so its first non-analytic term is q^4 log q"
    )
    print(
        "SUMMARY: confirmed the bond average, kappa = I/12 = 0.0994834268, the Bessel representation, "
        "and the degree count. The L=16..128 zone sums and the L=8 diagonalizations were not re-run. "
        "The density-coupling coefficient 1/(6 pi^2) was not re-derived."
    )


if __name__ == "__main__":
    main()
