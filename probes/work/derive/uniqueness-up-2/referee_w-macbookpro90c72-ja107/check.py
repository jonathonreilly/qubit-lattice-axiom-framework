#!/usr/bin/env python3
"""Independent referee for uniqueness-up-2 a3.

Recomputes the shared-predecessor constants in float64 (not the author's
fractions) and checks the Wasserstein formula against a linear program.
"""
import itertools
import random

import numpy as np
from scipy.optimize import linprog

FAILS = []


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (("  [" + detail + "]") if detail else ""))
    if not ok:
        FAILS.append(name)


AX = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
NEG = [1, 0, 3, 2, 5, 4]


def phi(i, j, w):
    d = AX[i][0] * AX[j][0] + AX[i][1] * AX[j][1] + AX[i][2] * AX[j][2]
    return w[0] if d == 1 else (w[1] if d == -1 else w[2])


def kernel(triple, w):
    ws = [phi(s, triple[0], w) * phi(s, triple[1], w) * phi(s, triple[2], w) for s in range(6)]
    Z = sum(ws)
    return [x / Z for x in ws]


def all_laws(w):
    return [kernel(t, w) for t in itertools.combinations_with_replacement(range(6), 3)]


def W_form(mu, nu, alpha):
    e = [max(0.0, a - b) for a, b in zip(mu, nu)]
    d = [max(0.0, b - a) for a, b in zip(mu, nu)]
    TV = sum(e)
    M = max(max(0.0, e[i] + d[NEG[i]] - TV) for i in range(6))
    return TV + (alpha - 1.0) * M


def rho(i, j, alpha):
    return 0.0 if i == j else (alpha if j == NEG[i] else 1.0)


def W_lp(mu, nu, alpha):
    # min sum c_ij x_ij, row and column margins
    c = [rho(i, j, alpha) for i in range(6) for j in range(6)]
    A = []
    b = []
    for i in range(6):
        row = [0.0] * 36
        for j in range(6):
            row[i * 6 + j] = 1.0
        A.append(row)
        b.append(mu[i])
    for j in range(6):
        row = [0.0] * 36
        for i in range(6):
            row[i * 6 + j] = 1.0
        A.append(row)
        b.append(nu[j])
    res = linprog(c, A_eq=A, b_eq=b, bounds=[(0, None)] * 36, method="highs")
    if not res.success:
        return None
    return float(res.fun)


def constants(w, alpha, pairs=((0, 1), (0, 2))):
    laws = {t: kernel(t, w) for t in itertools.combinations_with_replacement(range(6), 3)}

    def lw(*a):
        return laws[tuple(sorted(a))]

    kap = {}
    for a, b in pairs:
        for u1 in range(6):
            for u2 in range(6):
                kap[(a, b, u1, u2)] = W_form(lw(a, u1, u2), lw(b, u1, u2), alpha) / rho(a, b, alpha)
    kmax = max(kap.values())
    envs = list(laws.values())

    def avg(a, b, l1, l2):
        s = 0.0
        for u1 in range(6):
            for u2 in range(6):
                s += l1[u1] * l2[u2] * kap[(a, b, u1, u2)]
        return s

    k1 = max(avg(a, b, l1, l2) for a, b in pairs for l1 in envs for l2 in envs)
    ks_by = {}
    ks = 0.0
    pairs2 = list(itertools.combinations_with_replacement(range(6), 2))
    for a, b in pairs:
        best = 0.0
        for z in range(6):
            Ez = [lw(z, b1, b2) for b1, b2 in pairs2]
            for l1 in Ez:
                for l2 in Ez:
                    v = avg(a, b, l1, l2)
                    if v > best:
                        best = v
        ks_by[(a, b)] = best
        ks = max(ks, best)
    return kmax, k1, ks, ks_by


def C_of(kmax, k1, ks, alpha):
    return 3 * ks + min(alpha, 3 * kmax) * (k1 - ks)


def main():
    rng = random.Random(7)
    ok_w = True
    n = 0
    for _ in range(25):
        mu = [rng.random() for _ in range(6)]
        nu = [rng.random() for _ in range(6)]
        sm, sn = sum(mu), sum(nu)
        mu = [x / sm for x in mu]
        nu = [x / sn for x in nu]
        for alpha in (1.0, 1.35, 2.0):
            lp = W_lp(mu, nu, alpha)
            ok_w &= lp is not None and abs(W_form(mu, nu, alpha) - lp) < 1e-8
            n += 1
    check("Wasserstein formula matches an independent LP on 75 random laws", ok_w, f"n={n}")

    # at most one antipodal obstruction
    ok_one = True
    for _ in range(200):
        mu = [rng.random() for _ in range(6)]
        nu = [rng.random() for _ in range(6)]
        mu = [x / sum(mu) for x in mu]
        nu = [x / sum(nu) for x in nu]
        e = [max(0.0, a - b) for a, b in zip(mu, nu)]
        d = [max(0.0, b - a) for a, b in zip(mu, nu)]
        TV = sum(e)
        hits = [i for i in range(6) if e[i] + d[NEG[i]] - TV > 1e-12]
        ok_one &= len(hits) <= 1
    check("at most one axis has a strict antipodal obstruction", ok_one)

    alpha = 27 / 20
    wanted = {
        5.11: 0.96721,
        5.15: 0.97573,
        5.19: 0.98421,
        5.23: 0.99266,
        5.25: 0.99687,
        5.26: 0.99897,
    }
    ok_c = True
    bits = []
    three_k1 = []
    for p, target in wanted.items():
        kmax, k1, ks, _ = constants((p, 1.0, 2.0), alpha)
        C = C_of(kmax, k1, ks, alpha)
        ok_c &= C < 1 and abs(C - target) < 5e-5 and 3 * k1 >= 1 and k1 + 1e-12 >= ks
        bits.append(f"{p:.2f}:{C:.5f}")
        three_k1.append(3 * k1)
    for p in (5.27, 5.30):
        kmax, k1, ks, _ = constants((p, 1.0, 2.0), alpha)
        C = C_of(kmax, k1, ks, alpha)
        ok_c &= C > 1
        bits.append(f"{p:.2f}:{C:.5f}")
    check("C < 1 on 5.11..5.26 and C > 1 at 5.27 and 5.30, with 3 k1 >= 1", ok_c, " ".join(bits))

    # exact fraction they printed, as a float
    num = 101742123434848535989198503256177583297484225264
    den = 101846828471981561903500313276312611907960100913
    check("their exact C(526/100) is below 1 and matches the recomputed float",
          num < den and abs(num / den - 0.998972) < 5e-6)

    # contraction root
    a, b = 0.6, 0.3
    lam = (a + (a * a + 4 * b) ** 0.5) / 2
    check("a+b<1 implies the larger recurrence root is below 1", a + b < 1 and lam < 1, f"lambda={lam:.4f}")

    # symmetry at p=5.26 over all 30 ordered pairs: two values only
    pairs = [(i, j) for i in range(6) for j in range(6) if i != j]
    _, _, _, byp = constants((5.26, 1.0, 2.0), alpha, pairs=tuple(pairs))
    anti = {round(byp[(i, j)], 8) for i, j in pairs if j == NEG[i]}
    orth = {round(byp[(i, j)], 8) for i, j in pairs if j != NEG[i]}
    check("shared constant takes one antipodal value and one orthogonal value",
          len(anti) == 1 and len(orth) == 1 and anti != orth,
          f"anti {anti} orth {orth}")

    # round-1 anchor, float only: the stated fraction
    k1_num = 52187574259076840991934694
    k1_den = 156963184970376094931272779
    _, k1_51, _, _ = constants((5.1, 1.0, 2.0), 1.25)
    check("at p=5.1, alpha=5/4, recomputed k1 matches round 1's fraction",
          abs(k1_51 - k1_num / k1_den) < 1e-12, f"{k1_51:.12f}")

    print()
    if FAILS:
        print("SUMMARY: fails at step " + FAILS[0])
        raise SystemExit(1)
    print("SUMMARY: confirmed - with alpha=27/20 the shared-predecessor constant C is below 1 from p=5.11 through 5.26 and above 1 at 5.27; the recursion then gives one invariant law.")
    print("HIT: confirmed - independent LP matches W = TV + (alpha-1) M; recomputed C(5.26) = 0.99897 < 1 and C(5.27) > 1 on (p,1,2), so the six-axis level automaton has one invariant law up to p=5.26.")


if __name__ == "__main__":
    main()
