#!/usr/bin/env python3
"""J:attack-g:PR8145 — brute-force Part II.1 inequality (2) on small clock complexes.

Note: R(S)^{-1} W(K) <= W(J) <= R(S) W(K) when J-K = d1*S, with
R(S)=prod_p max_k c_k/c_{k+S_p}, c_k the Villain Fourier coefficients.
One-plaquette complexes, N=2 (exact tanh/coth) and N=3,4 (sympy DFT).
"""
from __future__ import annotations

import sys

import sympy as sp

PASSES = 0
FAILS = 0


def check(tag, ok, msg):
    global PASSES, FAILS
    if ok:
        PASSES += 1
        print(f"PASS: {tag} {msg}")
    else:
        FAILS += 1
        print(f"FAIL: {tag} {msg}")


def villain_c(N, beta):
    """c_k = (1/N) sum_m exp(beta cos(2 pi m/N) - 2 pi i m k / N)."""
    out = []
    for k in range(N):
        s = 0
        for m in range(N):
            s += sp.exp(beta * sp.cos(2 * sp.pi * m / N) - 2 * sp.I * sp.pi * m * k / N)
        ck = sp.simplify(sp.re(sp.expand(s / N)))
        out.append(ck)
    return out


def section_n2():
    b = sp.symbols("b", positive=True)
    c0, c1 = sp.cosh(b), sp.sinh(b)
    W = sp.simplify(c1 / c0)  # tanh
    R = sp.simplify(sp.Max(c0 / c1, c1 / c0))  # coth since coth>1
    # at a positive numerical point, and the identity W = 1/R
    ok = sp.simplify(c1 / c0 - sp.tanh(b)) == 0
    ok = ok and sp.simplify(c0 / c1 - sp.coth(b)) == 0
    # W = tanh, R = coth, W * R = 1, so W = R^{-1} and W <= R
    ok = ok and sp.simplify(sp.tanh(b) * sp.coth(b) - 1) == 0
    check("N2", ok, "N=2 one plaquette: c0=cosh b, c1=sinh b; W(J=1)=tanh b = R(S)^{-1}=coth^{-1} b; "
          "inequality (2) holds with equality on the lower side")


def section_n(N, beta=sp.Integer(1)):
    c = villain_c(N, beta)
    pos = all(sp.N(ck) > 0 for ck in c)
    even = all(sp.simplify(c[k] - c[(-k) % N]) == 0 or abs(complex(sp.N(c[k] - c[(-k) % N]))) < 1e-12 for k in range(N))
    ok = pos and even
    for q in range(N):
        W = sp.N(c[q] / c[0])
        R = max(float(sp.N(c[k] / c[(k + q) % N])) for k in range(N))
        lo = 1 / R
        ok = ok and (lo - 1e-10 <= float(W) <= R + 1e-10)
    check(f"N{N}", ok,
          f"N={N} one plaquette, beta=1: c_k>0, c_k=c_{{-k}}, and R^{{-1}}<=W(q)<=R for every q")


def main():
    section_n2()
    section_n(3)
    section_n(4)
    print(f"TOTAL: PASS={PASSES} FAIL={FAILS}")
    if FAILS:
        print("HIT: Part II.1 inequality (2) fails on a one-plaquette clock complex")
        print(f"SUMMARY: HIT - Villain current comparison fails ({FAILS} FAIL tags)")
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note: Part II.1 inequality (2) "
        "holds with equality on the N=2 one-plaquette (W=tanh b = R^{-1}), and holds "
        "on N=3,4 one-plaquette complexes at beta=1 (c_k>0, even, R^{-1}<=W<=R); "
        "U_l U_k=U_{l+k} and U_{Nl}=I are the clock algebra, not a finite defect"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
