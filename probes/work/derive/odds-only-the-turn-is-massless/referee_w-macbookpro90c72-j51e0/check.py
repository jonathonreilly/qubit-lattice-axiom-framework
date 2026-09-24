#!/usr/bin/env python3
"""Referee for odds-only-the-turn-is-massless a2.

Author w-macbookpro9927a-j6622 (claude-opus-5-5). Own series, own Gaussian moments.
Jentzsch, Soni, and the turn eigenvalue 1/6 stay assumed. The 320-node table was not re-run.
"""
import sympy as sp

fails = []


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail, flush=True)


def bessel():
    # (z+z^{-1})^n contributes binom(n,(n-m)/2) z^m when n-m is even, so the angular
    # average of cos^n psi cos(m psi) is that binomial over 2^n, which is I_m's coefficient.
    ok = True
    for m in range(5):
        for n in range(13):
            k = n - m
            if k < 0 or k % 2:
                continue
            k //= 2
            ang = sp.binomial(n, k) / 2 ** n
            bess = sp.factorial(n) / (sp.factorial(k) * sp.factorial(k + m) * 2 ** n)
            ok = ok and sp.simplify(ang - bess) == 0
    report(
        "sector kernel",
        ok,
        "angular coefficients of e^{x cos psi} cos(m psi) match I_m through x^12 for m=0..4",
    )


def reflection():
    theta = sp.symbols("theta", real=True)
    b1, b2, b3 = sp.symbols("b1 b2 b3", real=True)
    b = sp.Matrix([b1, b2, b3])
    s = sp.Matrix([sp.sin(theta), 0, sp.cos(theta)])
    et = sp.Matrix([sp.cos(theta), 0, -sp.sin(theta)])
    n = sp.Matrix([0, 0, 1])
    Rb = b - 2 * et.dot(b) * et
    same = sp.simplify(s.dot(Rb) - s.dot(b)) == 0
    lift = sp.simplify(Rb.dot(n) - b.dot(n) - 2 * et.dot(b) * sp.sin(theta)) == 0
    tangent = sp.simplify(s.dot(et)) == 0
    report(
        "reflection",
        same and lift and tangent,
        "s.Rb = s.b and Rb.n - b.n = 2 (e_theta.b) sin theta, so a non-decreasing sea is sent to a strictly increasing one",
    )


def gaussian():
    beta, a = sp.symbols("beta a", positive=True)
    # K1 of e^{-a |x|^2} has curvature a*beta/(2a+beta); F ~ g^6 fixes a = 5 beta/2
    curv = sp.simplify(a * beta / (2 * a + beta))
    fixed = sp.solve(sp.Eq(a, 6 * curv), a)[0]
    rho = sp.simplify(beta / (beta + 2 * fixed))
    var = sp.simplify(1 / (beta + 2 * fixed))
    # Mehler: Y|x ~ N(rho x, sig2), stationary variance v = sig2/(1-rho^2)
    rho_s, sig2, x = sp.symbols("rho sig2 x", real=True)
    v = sig2 / (1 - rho_s ** 2)
    mean = rho_s * x
    # n=2: Var(y|x)+mean^2 - stationary variance = rho^2 (x^2 - v)
    ey2 = sig2 + (rho_s * x) ** 2
    quad = sp.simplify(ey2 - v - rho_s ** 2 * (x ** 2 - v))
    mass30 = sp.Rational(1, 36)
    mass210 = sp.Rational(1, 216)
    m2 = lambda mu: sp.simplify((1 - 6 * mu) / mu)
    report(
        "gaussian limit",
        fixed == sp.Rational(5, 2) * beta and rho == sp.Rational(1, 6) and var == 1 / (6 * beta)
        and sp.simplify(mean - rho_s * x) == 0 and quad == 0
        and m2(mass30) == 30 and m2(mass210) == 210 and m2(sp.Rational(1, 6)) == 0,
        "a=5 beta/2, chain N(x/6, 1/(6 beta)), eigenvalues 6^{-n}; m_L^2 -> 30 and the next odd level -> 210",
    )


def main():
    bessel()
    reflection()
    gaussian()
    if fails:
        print("SUMMARY: fails at " + fails[0])
        return
    print(
        "HIT: confirmed - for a non-decreasing leaning sea the turn is the Perron vector of order one "
        "if Jentzsch and the eigenvalue 1/6 are granted, and |m|>=2 is strictly below it if Soni's inequality is granted; "
        "the Gaussian chain has m_L^2 = 30"
    )
    print(
        "SUMMARY: confirmed the Bessel sector kernels through order 12, the reflection identities, and the Mehler masses 30 and 210. "
        "Jentzsch, Soni, and block 103's turn eigenvalue stay assumed. The 320-node sea was not re-executed. Order m=0 stays open."
    )


if __name__ == "__main__":
    main()
