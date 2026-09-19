#!/usr/bin/env python3
"""J:attack-g:PR8080 — brute-force the Q_tau spectral-residual identity.

Note: Q_tau(lambda)-lambda^{-2}
  = (lambda-delta)(lambda-tau)^2 [(tau+2 delta)lambda + delta tau] / (delta^2 tau^3 lambda^2)
and ||H^{-1} r||^2 <= A rho2 + B rho1 + C rho0 with the stated A,B,C.
"""
from __future__ import annotations

import sys

import sympy as sp


def main():
    lam, tau, d = sp.symbols("lam tau delta", positive=True)
    A = (tau + 2 * d) / (d ** 2 * tau ** 3)
    Q = (3 * tau - 2 * lam) / tau ** 3 + A * (lam - tau) ** 2
    lhs = sp.together(Q - 1 / lam ** 2)
    rhs = (lam - d) * (lam - tau) ** 2 * ((tau + 2 * d) * lam + d * tau) / (d ** 2 * tau ** 3 * lam ** 2)
    ok_fac = sp.simplify(lhs - rhs) == 0
    B = -2 / tau ** 3 - 2 * tau * A
    C = 3 / tau ** 2 + tau ** 2 * A
    ok_quad = sp.simplify(sp.expand(Q) - (A * lam ** 2 + B * lam + C)) == 0
    print(f"factorization identity: {ok_fac}")
    print(f"Q = A lam^2 + B lam + C: {ok_quad}")
    if not (ok_fac and ok_quad):
        print("HIT: Q_tau factorization or A,B,C quadratic form fails as written")
        print("SUMMARY: HIT - spectral-residual identity does not hold identically")
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note: Q_tau(lambda)-1/lambda^2 equals "
        "the stated nonnegative factorization identically, and Q_tau is exactly "
        "A lambda^2 + B lambda + C with the stated A,B,C"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
