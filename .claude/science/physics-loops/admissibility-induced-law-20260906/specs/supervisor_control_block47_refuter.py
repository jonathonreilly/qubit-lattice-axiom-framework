#!/usr/bin/env python3
"""Block 47 refuting pass: machinery disjoint from the runner's.

W1  <max(0, s_z)> over the uniform sphere by symbolic integration; the kinetic capture rate (sqrt 3/2) rho
W2  exposed faces by a different count: 6 N minus twice the number of adjacent pairs inside the body (site, pairs, cube, balls of radius 2 to 5)
W3  the coefficient G = K_0 q_1^2 = 3 sqrt3 rho/(16 pi (1 - rho)) symbolically
W4  six axes: the capture rate of one site by enumeration of the 7^6 states of its six neighbours in the product state
Exact arithmetic (Fractions, sympy).
"""
import sys
from fractions import Fraction as F
from itertools import product

import sympy as sp

fails = 0


def report(tag, ok, msg):
    global fails
    fails += 0 if ok else 1
    print(("PASS" if ok else "FAIL") + f": {tag} {msg}")


def w1():
    th, rho = sp.symbols("theta rho", positive=True)
    half = sp.integrate(sp.cos(th) * sp.sin(th), (th, 0, sp.pi / 2)) * 2 * sp.pi / (4 * sp.pi)
    q1 = 6 * rho * half / sp.sqrt(3)
    report("W1", half == sp.Rational(1, 4) and sp.simplify(q1 - sp.sqrt(3) * rho / 2) == 0, "symbolic integration: <max(0, s_z)> = 1/4 and q_1 = (sqrt 3/2) rho")


def w2():
    def faces(body):
        body = set(body)
        pairs = sum(1 for s in body for i in range(3) if tuple(s[j] + (1 if j == i else 0) for j in range(3)) in body)
        return 6 * len(body) - 2 * pairs
    ball = lambda r: [s for s in product(range(-r - 1, r + 2), repeat=3) if sum(t * t for t in s) <= r * r]
    got = [faces([(0, 0, 0)]), faces([(0, 0, 0), (5, 0, 0)]), faces([(0, 0, 0), (1, 0, 0)]), faces(list(product(range(2), repeat=3)))] + [faces(ball(r)) for r in (2, 3, 4, 5)]
    report("W2", got == [6, 12, 10, 24, 78, 174, 294, 486], f"exposed faces as 6 N minus twice the adjacent pairs: {got}")


def w3():
    rho = sp.Symbol("rho", positive=True)
    k0 = sp.sqrt(3) / (4 * sp.pi * rho * (1 - rho))
    q1 = sp.sqrt(3) * rho / 2
    report("W3", sp.simplify(k0 * q1 ** 2 - 3 * sp.sqrt(3) * rho / (16 * sp.pi * (1 - rho))) == 0, "symbolically K_0 q_1^2 = 3 sqrt3 rho/(16 pi (1 - rho))")


def w4():
    rho = F(3, 10)
    states = [None] + list(range(6))
    prob = lambda s: (1 - rho) if s is None else rho / 6
    rate = F(0)
    for nbrs in product(states, repeat=6):                         # neighbour k sits at -e_k and captures if its content is k
        w = F(1)
        for s in nbrs:
            w *= prob(s)
        rate += w * sum(1 for k in range(6) if nbrs[k] == k)
    report("W4", rate == rho, f"six axes: the expected number of neighbours pointing at the site, over all 7^6 neighbour states of the product state at density 3/10, is {rate}")


if __name__ == "__main__":
    for fn in (w1, w2, w3, w4):
        fn()
    print(f"REFUTER TOTAL: FAIL={fails}")
    sys.exit(1 if fails else 0)
