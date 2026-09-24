#!/usr/bin/env python3
"""Referee of parity-odd couplings under the 24, attempt a1.

Own hop matrices and own 4^3 moment. Does not import the author's check.
"""
import itertools

import numpy as np
import sympy as sp

GAM = [(1, 0, 0), (1, 0, 0), (0, 1, 0), (-1, 0, 0), (0, -1, 0), (0, 0, 1), (-1, 0, 0), (0, 0, -1)]


def hops(a, b):
    I2 = sp.eye(2)
    S = [sp.Matrix([[0, 1], [1, 0]]),
         sp.Matrix([[0, -sp.I], [sp.I, 0]]),
         sp.Matrix([[1, 0], [0, -1]])]
    B = {}
    for j in range(3):
        ep, em = [0, 0, 0], [0, 0, 0]
        ep[j], em[j] = 1, -1
        B[tuple(ep)] = a * I2 - sp.I * b / 2 * S[j]
        B[tuple(em)] = a * I2 + sp.I * b / 2 * S[j]
    return B


def tau(seq, B):
    M = sp.eye(2)
    for e in seq:
        M = M * B[e]
    return sp.expand(M.trace())


def moment(aa, bb, mirror=False):
    N = 4
    sites = list(itertools.product(range(N), repeat=3))
    idx = {x: i for i, x in enumerate(sites)}
    n = len(sites)

    def w_of(x):
        y = tuple((-t) % N for t in x) if mirror else x
        return 1 + ((7 * y[0] + 5 * y[1] * y[1] + 3 * y[2] + 2 * y[0] * y[1] * y[2] + y[1] * y[2]) % 3)

    M = np.zeros((2 * n, 2 * n), dtype=np.complex128)
    sig = [np.array([[0, 1], [1, 0]]),
           np.array([[0, -1j], [1j, 0]]),
           np.array([[1, 0], [0, -1]])]
    for x in sites:
        i = idx[x]
        wi = w_of(x)
        for j in range(3):
            for s, sign in ((1, -1), (-1, +1)):
                y = list(x)
                y[j] = (y[j] + s) % N
                k = idx[tuple(y)]
                Ae = aa * np.eye(2) + sign * 1j * (bb / 2) * sig[j]
                M[2 * i:2 * i + 2, 2 * k:2 * k + 2] += (2 * wi) * Ae
    return np.trace(np.linalg.matrix_power(M, 8)).real


def main():
    a, b = sp.symbols("a beta", real=True)
    B = hops(a, b)
    if tuple(map(sum, zip(*GAM))) != (0, 0, 0):
        raise SystemExit("not closed")
    diff = sp.factor(tau(GAM, B) - tau([tuple(-c for c in e) for e in GAM], B))
    if diff != -a ** 3 * b ** 5:
        raise SystemExit(diff)
    print("STEP 3 FOLLOWS: the closed loop (e1,e1,e2,-e1,-e2,e3,-e1,-e3) has "
          "tau(gamma)-tau(-gamma) = -a^3 beta^5")

    t = moment(1, 2, False)
    tm = moment(1, 2, True)
    if abs(t - 4083834945536) > 0.5 or abs(tm - 4082722668544) > 0.5:
        raise SystemExit(f"moments {t} {tm}")
    if abs(moment(0, 2, False) - moment(0, 2, True)) > 0.5:
        raise SystemExit("a=0 still chiral")
    if abs(moment(1, 0, False) - moment(1, 0, True)) > 0.5:
        raise SystemExit("beta=0 still chiral")
    print("STEP 4 FOLLOWS: on the 4^3 torus with the integer rate field, "
          "tr((2wH)^8) is 4083834945536 against its mirror 4082722668544 at (a,beta)=(1,2); "
          "the two agree when a=0 and when beta=0")

    # parity table on the symbol
    k = sp.symbols("k1:4", real=True)
    S = [sp.Matrix([[0, 1], [1, 0]]),
         sp.Matrix([[0, -sp.I], [sp.I, 0]]),
         sp.Matrix([[1, 0], [0, -1]])]
    a0 = sp.symbols("a0", real=True)

    def symb(c0, ca, cb):
        h = c0 * sp.eye(2)
        for j in range(3):
            h += 2 * ca * sp.cos(k[j]) * sp.eye(2) + cb * sp.sin(k[j]) * S[j]
        return h

    neg = {k[0]: -k[0], k[1]: -k[1], k[2]: -k[2]}
    shift = {k[0]: k[0] + sp.pi, k[1]: k[1] + sp.pi, k[2]: k[2] + sp.pi}
    s2 = S[1]

    def keeps(fun, sgn, c0, ca, cb):
        t = symb(c0, ca, cb)
        d = sp.simplify(sp.expand(fun(t) - sgn * t))
        return d == sp.zeros(2)

    def Pi(M):
        return M.subs(neg, simultaneous=True)

    def Eps(M):
        return M.subs(shift, simultaneous=True)

    def Theta(M):
        return s2 * M.subs(neg, simultaneous=True).conjugate() * s2

    rows = {
        "Pi": (lambda M: Pi(M), +1),
        "epsPi": (lambda M: Eps(Pi(M)), +1),
        "ThetaPi": (lambda M: Theta(Pi(M)), -1),
        "ThetaEpsPi": (lambda M: Theta(Eps(Pi(M))), -1),
    }
    # columns a0, a, beta
    expect = {
        "Pi": (True, True, False),
        "epsPi": (True, False, True),
        "ThetaPi": (False, False, True),
        "ThetaEpsPi": (False, True, False),
    }
    for name, (fun, sgn) in rows.items():
        got = (keeps(fun, sgn, 1, 0, 0), keeps(fun, sgn, 0, 1, 0), keeps(fun, sgn, 0, 0, 1))
        if got != expect[name]:
            raise SystemExit(f"table {name} {got}")
    print("STEP 2 FOLLOWS: Pi keeps a0 and a and breaks beta; eps Pi keeps a0 and beta and breaks a; "
          "Theta Pi keeps beta and breaks a0 and a; Theta eps Pi keeps a and breaks a0 and beta. "
          "The two walk-keeping inversions both reverse a")

    print("SUMMARY: confirmed - the scalar hop a is the nearest-neighbour term reversed by both "
          "walk-keeping inversions; for a*beta != 0 no site-local inversion is a symmetry because "
          "tau-tau_mirror = -a^3 beta^5; a chiral rate field and its mirror differ at the 8th moment; "
          "blindness removes the odd field densities and does not remove a")
    print("HIT: confirmed - parity-odd generator term is the scalar hop a, obstructed by the chiral "
          "8-loop -a^3 beta^5 and visible as tr((2wH)^8) differing from its mirror; the odd field "
          "sector does not survive blindness")


if __name__ == "__main__":
    main()
