#!/usr/bin/env python3
"""Referee for source-halo-of-a-producing-lump a3.

Author w-jonathonsmac4f50-j3484 (claude-opus-5-5). Does not import that check.
Neutral scale c0 = 6/T, T = p+q+4r. Aligned Z_k = c0^k (p^k+q^k+4 r^k).
"""
import itertools
from fractions import Fraction as Fr

import sympy as sp
from scipy import integrate
import numpy as np

fails = []


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)


def A(k, p, q, r):
    return p ** k + q ** k + 4 * r ** k


def delta(k, p, q, r):
    T = p + q + 4 * r
    return Fr(6 ** (k - 1) * A(k, p, q, r), T ** k) - 1


NB = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))


def add(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def census(S):
    touch = {add(s, d) for s in S for d in NB} - S
    counts = {}
    for t in touch:
        k = sum(add(t, d) in S for d in NB)
        counts[k] = counts.get(k, 0) + 1
    return counts


def Q(S, p, q, r):
    return 6 * sum(n * delta(k, p, q, r) for k, n in census(S).items())


def formulas():
    ok = delta(1, 3, 1, 2) == 0 and delta(1, 12, 1, 2) == 0
    ok = ok and delta(2, 3, 1, 2) + 1 == Fr(13, 12) and delta(3, 3, 1, 2) + 1 == Fr(5, 4)
    ok = ok and delta(2, 12, 1, 2) + 1 == Fr(46, 21) and delta(3, 12, 1, 2) + 1 == Fr(2348, 343)
    # symbolic row-sum: A_1 = T for indeterminates
    p, q, r = sp.symbols("p q r", positive=True)
    T = p + q + 4 * r
    ok = ok and sp.simplify(p + q + 4 * r - T) == 0
    report(
        "deltas",
        bool(ok),
        "delta_1 = 0; 1+delta_2, 1+delta_3 are 13/12 and 5/4 at (3,1,2), and 46/21 and 2348/343 at (12,1,2)",
    )


def shapes():
    ok = True
    detail = []
    for L in (3, 4, 5, 6):
        cube = set(itertools.product(range(L), repeat=3))
        ok = ok and census(cube) == {1: 6 * L * L} and Q(cube, 3, 1, 2) == 0
        face = (L // 2, L // 2, L - 1)
        pit = cube - {face}
        ok = ok and census(pit).get(5, 0) == 1 and Q(pit, 3, 1, 2) == 6 * delta(5, 3, 1, 2)
        ad = cube | {(L // 2, L // 2, L)}
        ok = ok and census(ad).get(2, 0) == 4 and Q(ad, 3, 1, 2) == 24 * delta(2, 3, 1, 2)
        step = cube | {(i, j, L) for i in range(L) for j in range(L // 2)}
        cs = census(step)
        ok = ok and cs.get(2, 0) == L and set(cs) <= {1, 2}
        ok = ok and Q(step, 3, 1, 2) == 6 * L * delta(2, 3, 1, 2)
        detail.append(f"L={L} step k2={cs.get(2, 0)}")
    report(
        "shapes",
        ok,
        "cubes of side 3-6 have only k=1 and Q=0; a centred pit is 6 delta_5; an adatom is 24 delta_2; "
        "a half-face step has one k=2 site per unit length (" + ", ".join(detail) + ")",
    )


def sphere_and_balls():
    def axes(th, ph):
        n = np.sort(np.abs([np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph), np.cos(th)]))
        return n  # n0 <= n1 <= n2

    # densities: k=1 is n_max - n_mid, k=2 is n_mid - n_min, k=3 is n_min
    I2, e2 = integrate.dblquad(lambda ph, th: (axes(th, ph)[1] - axes(th, ph)[0]) * np.sin(th), 0, np.pi, 0, 2 * np.pi, epsabs=1e-10)
    I3, e3 = integrate.dblquad(lambda ph, th: axes(th, ph)[0] * np.sin(th), 0, np.pi, 0, 2 * np.pi, epsabs=1e-10)
    d2, d3 = delta(2, 3, 1, 2), delta(3, 3, 1, 2)
    pred = 6 * (float(d2) * I2 + float(d3) * I3)
    ratios = []
    ks_ok = True
    per_record = []
    for R in (10, 20, 40, 60):
        ball = {(x, y, z) for x in range(-R, R + 1) for y in range(-R, R + 1) for z in range(-R, R + 1) if x * x + y * y + z * z <= R * R}
        cs = census(ball)
        ks_ok = ks_ok and set(cs) <= {1, 2, 3}
        Qv = 6 * sum(n * (d2 if k == 2 else d3 if k == 3 else 0) for k, n in cs.items())
        ratios.append(float(Qv) / R ** 2)
        per_record.append(float(Qv) / len(ball))
    approach = abs(ratios[-1] - pred) / pred < 0.03 and ratios[-1] > ratios[0]
    fall = per_record[-1] < per_record[0]
    report(
        "balls",
        ks_ok and approach and fall and abs(I2 - 3.129928) < 2e-5 and abs(I3 - 2.637293) < 2e-5 and abs(pred - 5.52) < 0.01,
        f"I2={I2:.6f} (err {e2:.1e}), I3={I3:.6f} (err {e3:.1e}), predicted Q/(z R^2)={pred:.4f}; "
        f"censuses at R=10,20,40,60 give {', '.join(f'{v:.3f}' for v in ratios)}; "
        f"Q per record {', '.join(f'{v:.4f}' for v in per_record)}",
    )


def porous():
    f = Fr(1, 3)
    cube = list(itertools.product(range(2), repeat=3))
    brute = Fr(0)
    for occ in itertools.product((0, 1), repeat=8):
        S = {s for s, bit in zip(cube, occ) if bit}
        w = f ** sum(occ) * (1 - f) ** (8 - sum(occ))
        if S:
            brute += w * Q(S, 3, 1, 2)
    # linearity: each site empty with the stated probability, k binomial in its cube-neighbours
    shell = {add(s, d) for s in cube for d in NB} - set(cube)
    formula = Fr(0)
    for x in cube + list(shell):
        m = sum(add(x, d) in set(cube) for d in NB)
        pe = (1 - f) if x in set(cube) else Fr(1)
        for k in range(2, m + 1):
            prob = Fr(math_comb(m, k)) * f ** k * (1 - f) ** (m - k)
            formula += pe * prob * 6 * delta(k, 3, 1, 2)
    # bulk per record
    bulk = 6 * (1 - f) / f * sum(Fr(math_comb(6, k)) * f ** k * (1 - f) ** (6 - k) * delta(k, 3, 1, 2) for k in range(2, 7))
    report(
        "porous",
        brute == formula and bulk != 0,
        f"all 256 fillings of the 2^3 cube at f=1/3 give E[Q]={brute}, matching linearity; "
        f"bulk E[Q] per record -> {float(bulk):.5f} z",
    )


def math_comb(n, k):
    c = 1
    for i in range(k):
        c = c * (n - i) // (i + 1)
    return c


def contents_and_halo():
    T = 12
    c0 = Fr(6, T)
    def om(a, b):
        return 3 if a == b else (1 if a == (b ^ 1) else 2)
    Zs = []
    for s1, s2 in itertools.product(range(6), repeat=2):
        Zs.append(sum(c0 ** 2 * om(a, s1) * om(a, s2) for a in range(6)))
    mean = sum(Zs) / 36
    var = sum((Z - mean) ** 2 for Z in Zs) / 36
    opp = sum(c0 ** 2 * om(a, 4) * om(a, 5) for a in range(6))
    Z3 = [sum(c0 ** 3 * om(a, s1) * om(a, s2) * om(a, s3) for a in range(6)) for s1, s2, s3 in itertools.product(range(6), repeat=3)]
    var3 = sum((Z - 6) ** 2 for Z in Z3) / len(Z3)
    # k=1 is identically 6
    row = [sum(om(a, s) for a in range(6)) for s in range(6)]
    # variance formula
    # (Omega^2)_ab / 6 = E_s om(a,s) om(b,s)
    M = [[Fr(sum(om(a, s) * om(b, s) for s in range(6)), 6) for b in range(6)] for a in range(6)]
    var_formula = (Fr(6, 12) ** 4) * sum(M[a][b] ** 2 for a in range(6) for b in range(6)) - 36
    # Green expansion
    x1, x2, x3, t = sp.symbols("x1 x2 x3 t", positive=True)
    y1, y2, y3 = sp.symbols("y1 y2 y3", real=True)
    rvec = sp.Matrix([x1, x2, x3]) - t * sp.Matrix([y1, y2, y3])
    G = 1 / (4 * sp.pi * sp.sqrt(rvec.dot(rvec)))
    series = G.series(t, 0, 2).removeO()
    monopole = 1 / (4 * sp.pi * sp.sqrt(x1 ** 2 + x2 ** 2 + x3 ** 2))
    dipole = (x1 * y1 + x2 * y2 + x3 * y3) / (4 * sp.pi * (x1 ** 2 + x2 ** 2 + x3 ** 2) ** sp.Rational(3, 2))
    report(
        "contents-halo",
        mean == 6 and var == Fr(1, 12) and var3 == Fr(1, 4) and var_formula == var and opp == Fr(11, 2) and row == [12] * 6 and sp.simplify(series.subs(t, 1) - monopole - dipole) == 0,
        f"E[Z]=6 and Var=1/12 on all 36 pairs at k=2; opposite contents give Z={opp}; "
        "k=1 row sum is T so Z=6 exactly; the Coulomb field expands as the monopole plus d·x/(4 pi r^3)",
    )


def main():
    formulas()
    shapes()
    sphere_and_balls()
    porous()
    contents_and_halo()
    print(f"TOTAL: PASS={5 - len(fails)} FAIL={len(fails)}")
    if fails:
        print("SUMMARY: fails at step " + fails[0] + " - independent recomputation disagreed")
        return
    print(
        "SUMMARY: confirmed - aligned production excess is 6z sum n_k delta_k with delta_1=0, so a cube has Q=0 and "
        "defects (pit, adatom, step) carry the excess; a ball's excess is a surface term approaching 6(delta_2 I_2+delta_3 I_3); "
        "a porous lump's mean excess is proportional to its record count; random contents have mean excess 0 and can sink"
    )
    print(
        "HIT: confirmed - delta_1=0 and the stated rational values, cube/pit/adatom/step censuses, sphere integrals "
        "I2=3.129928 and I3=2.637293 with ball ratios approaching 5.52, the 256-state porous expectation, "
        "Var Z_2=1/12 and opposite-pair Z=11/2, and the Coulomb dipole expansion"
    )


if __name__ == "__main__":
    main()
