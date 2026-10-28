#!/usr/bin/env python3
"""r55u_3_interp.py -- REVIEW55_TUNIF check r55u_3 (criteria: checks/r55u_3_criteria.md, written first).
Nested multilinear interpolation of a coarse scalar on a torus; exact rationals; imports nothing from the lane."""
from fractions import Fraction as Fr
from itertools import product
import random, sys

def interp(mu, Tc, s, d):
    """Fine values on (Z/(s*Tc))^d of the multilinear interpolant of coarse mu on (Z/Tc)^d."""
    N = s * Tc
    lam = {}
    for x in product(range(N), repeat=d):
        X = [xi // s for xi in x]; t = [xi % s for xi in x]
        v = Fr(0)
        for eps in product((0, 1), repeat=d):
            w = Fr(1)
            for a in range(d):
                w *= Fr(t[a], s) if eps[a] else Fr(s - t[a], s)
            if w:
                v += w * mu[tuple((X[a] + eps[a]) % Tc for a in range(d))]
        lam[x] = v
    return lam

def grad(f, N, d):
    return {(x, a): f[tuple((x[b] + (1 if b == a else 0)) % N for b in range(d))] - f[x]
            for x in product(range(N), repeat=d) for a in range(d)}

def main():
    rng = random.Random(7171)
    Tc = 3
    okA = okB = okC = okD = True
    fireE = False
    print(" d  s  inst   sup ratio (<=1)   l1 ratio (<=1)   l1 vs s^(d-2)")
    for d in (2, 3):
        for s in (3, 9):
            insts = []
            for i in range(5):
                insts.append({X: Fr(rng.randint(-5, 5), rng.randint(1, 3)) for X in product(range(Tc), repeat=d)})
            insts.append({X: (Fr(1) if X == tuple([0] * d) else Fr(0)) for X in product(range(Tc), repeat=d)})
            for i, mu in enumerate(insts):
                lam = interp(mu, Tc, s, d)
                N = s * Tc
                for X in mu:
                    if lam[tuple(s * c for c in X)] != mu[X]: okA = False
                gf, gc = grad(lam, N, d), grad(mu, Tc, d)
                supf, supc = max(abs(v) for v in gf.values()), max(abs(v) for v in gc.values())
                l1f, l1c = sum(abs(v) for v in gf.values()), sum(abs(v) for v in gc.values())
                rs = supf / (supc / s) if supc else Fr(0)
                r1 = l1f / (s ** (d - 1) * l1c) if l1c else Fr(0)
                r2 = l1f / (s ** (d - 2) * l1c) if l1c else Fr(0)
                if rs > 1: okB = False
                if r1 > 1: okC = False
                if r2 > 1: fireE = True
                print(f" {d}  {s}  {i:4d}   {float(rs):12.6f}    {float(r1):12.6f}    {float(r2):12.6f}")
                if s == 9:
                    sub = {tuple(c // 3 for c in x): lam[x] for x in lam if all(c % 3 == 0 for c in x)}
                    lam2 = interp(sub, 3 * Tc, 3, d)
                    if any(lam2[x] != lam[x] for x in lam): okD = False
    print(f"r55u_3-A (exact at coarse sites): {'PASS' if okA else 'FAIL'}")
    print(f"r55u_3-B (sup <= s^-1 sup): {'PASS' if okB else 'FAIL'}")
    print(f"r55u_3-C (l1 <= s^(d-1) l1): {'PASS' if okC else 'FAIL'}")
    print(f"r55u_3-D (nested s=9 vs 3∘3): {'PASS' if okD else 'FAIL'}")
    print(f"r55u_3-E (control: s^(d-2) bound must fail somewhere): {'FIRED as designed' if fireE else 'DID NOT FIRE'}")
    print("(ratio columns are printed as floats for display only; every verdict above is decided on exact Fractions)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
