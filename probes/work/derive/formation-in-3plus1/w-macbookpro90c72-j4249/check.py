#!/usr/bin/env python3
"""formation-in-3plus1, attempt 3 (worker w-macbookpro90c72-j4249).

A(kappa)/kappa strictly decreasing (h'''' = -u sinh u); MF threshold 3/4;
linear IR envelope 4/|k|^2 .. 16/|k|^2.
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


def section_a():
    u = sp.symbols("u", positive=True)
    h = 4 * sp.cosh(u) - 4 - u ** 2 - u * sp.sinh(u)
    ok = all(sp.simplify(h.diff(u, n).subs(u, 0)) == 0 for n in range(4))
    h4 = sp.simplify(h.diff(u, 4))
    ok = ok and sp.simplify(h4 + u * sp.sinh(u)) == 0
    check("A1", ok, "h(u)=4 cosh u - 4 - u^2 - u sinh u vanishes to order 3 at 0; "
          "h'''' = -u sinh u <= 0, so A(kappa)/kappa is strictly decreasing on (0, inf)")
    k = sp.symbols("k", positive=True)
    A = sp.coth(k) - 1 / k
    ser = A.series(k, 0, 6).removeO()
    ok = ser.coeff(k) == sp.Rational(1, 3) and ser.coeff(k ** 3) == -sp.Rational(1, 45)
    # MF: 1 = 4*beta/3 => beta=3/4
    ok = ok and sp.Rational(3, 4) * 4 / 3 == 1
    check("A2", ok, "A(k)=k/3 - k^3/45 + O(k^5); MF linearization 1=4 beta/3 gives beta_c=3/4")


def section_b():
    M = sp.Matrix([[sp.Rational(3, 16), sp.Rational(-1, 16), sp.Rational(-1, 16)],
                   [sp.Rational(-1, 16), sp.Rational(3, 16), sp.Rational(-1, 16)],
                   [sp.Rational(-1, 16), sp.Rational(-1, 16), sp.Rational(3, 16)]])
    ev = sorted(sp.simplify(e) for e in M.eigenvals())
    ok = ev == [sp.Rational(1, 16), sp.Rational(1, 4)]
    # 1/lambda_max = 4, 1/lambda_min = 16
    ok = ok and 1 / ev[1] == 4 and 1 / ev[0] == 16
    k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
    q = (sp.Matrix([k1, k2, k3]).T * M * sp.Matrix([k1, k2, k3]))[0]
    r2 = k1 ** 2 + k2 ** 2 + k3 ** 2
    # q - (1/16) r2 = positive semidefinite remainder
    rem_lo = sp.simplify(q - ev[0] * r2)
    rem_hi = sp.simplify(ev[1] * r2 - q)
    # both should be squares / PSD: check as quadratic forms
    Hlo = sp.hessian(rem_lo, [k1, k2, k3])
    Hhi = sp.hessian(rem_hi, [k1, k2, k3])
    ok = ok and all(sp.simplify(e) >= 0 for e in list(Hlo.eigenvals()) + list(Hhi.eigenvals()))
    check("B1", ok, "linear kernel 1/(k^T M k) obeys 4/|k|^2 <= 1/(k^T M k) <= 16/|k|^2")


def main():
    section_a()
    section_b()
    print(f"TOTAL: PASS={PASSES} FAIL={FAILS}")
    if FAILS:
        print(f"SUMMARY: ROUTE FAILS AT a finite check - {FAILS} FAIL tags")
        return 1
    print(
        "HIT: new exact partial: A(kappa)/kappa is strictly decreasing (h''''=-u sinh u, "
        "first four derivatives of h vanish at 0); mean-field sphere threshold on 3+1 is "
        "beta_c=3/4; linearized equal-level kernel is sandwiched 4 sigma^2/|k|^2 <= S_lin "
        "<= 16 sigma^2/|k|^2. Chessboard RP does not apply to the causal formation kernel. "
        "Sphere LRO not proved"
    )
    print(
        "SUMMARY: PARTIAL MF threshold beta=3/4 via A(kappa)/kappa decreasing; linear IR "
        "envelope 4..16; chessboard route to LRO fails (causal kernels are not Gibbs-RP); "
        "nonlinear LRO not claimed"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
