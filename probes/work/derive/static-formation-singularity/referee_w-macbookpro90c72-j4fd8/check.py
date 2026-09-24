#!/usr/bin/env python3
"""Referee for static-formation-singularity a1.

Author w-macbookpro90c72-je8fe (claude-opus-5). Own enumerations.
The price sheet G is their reported test, not proved optimal.
"""
from fractions import Fraction as F
from itertools import combinations_with_replacement as cwr
from itertools import permutations, product
from math import factorial, prod

import sympy as sp

fails = []


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail, flush=True)


def phi(s, t):
    return 3 if s == t else (1 if t == (s ^ 1) else 2)


PH = [[phi(s, t) for t in range(6)] for s in range(6)]


def Zset(vals):
    return sum(prod(PH[s][y] for y in vals) for s in range(6))


EDGES = [(0, 1), (0, 2), (1, 3), (2, 3)]
NBR = {0: (1, 2), 1: (0, 3), 2: (0, 3), 3: (1, 2)}


def weight(v):
    return prod(PH[v[a]][v[b]] for a, b in EDGES)


def formation(order, v):
    p = F(1)
    for k, x in enumerate(order):
        A = [y for y in NBR[x] if y in order[:k]]
        num = prod((PH[v[x]][v[y]] for y in A), start=1)
        p *= F(num, Zset(tuple(v[y] for y in A)))
    return p


def classes(order):
    a0 = a1 = 0
    K = []
    for k, x in enumerate(order):
        A = tuple(y for y in NBR[x] if y in order[:k])
        if len(A) == 0:
            a0 += 1
        elif len(A) == 1:
            a1 += 1
        else:
            K.append(A)
    return a0, a1, tuple(sorted(K))


def identity():
    NT = [[Zset((a, b)) for b in range(6)] for a in range(6)]
    rows = all(NT[a][b] == (26 if a == b else 22 if b == (a ^ 1) else 24) for a in range(6) for b in range(6))
    configs = list(product(range(6), repeat=4))
    zw = sum(weight(v) for v in configs)
    orders = list(permutations(range(4)))
    ok = rows and Zset((0,)) == 12 and zw == 12 ** 4 + 3 * 2 ** 4 == 20784
    for order in orders:
        a0, a1, K = classes(order)
        for v in configs:
            den = 6 ** a0 * 12 ** a1
            for A in K:
                den *= Zset(tuple(v[y] for y in A))
            if formation(order, v) * den != weight(v):
                ok = False
                break
        if not ok:
            break
    kinds = {classes(o) for o in orders}
    report("likelihood", ok and len(kinds) == 4, f"Z_W={zw}, identity on 24 orders x 1296, {len(kinds)} laws")
    return configs, orders, zw, NT


def adaptive(G, NT):
    memo = {}

    def rec(state):
        if all(x is not None for x in state):
            i = (NT[state[0]][state[3]] - 22) // 2
            j = (NT[state[1]][state[2]] - 22) // 2
            return G[(min(i, j), max(i, j))]
        key = state
        if key in memo:
            return memo[key]
        best = None
        for x in range(4):
            if state[x] is not None:
                continue
            A = [y for y in NBR[x] if state[y] is not None]
            weights = []
            total = 0
            for s in range(6):
                w = prod((PH[s][state[y]] for y in A), start=1)
                weights.append(w)
                total += w
            val = sum(F(weights[s], total) * rec(state[:x] + (s,) + state[x + 1:]) for s in range(6))
            if best is None or val > best:
                best = val
        memo[key] = best
        return best

    return rec((None,) * 4)


def plaquette(configs, orders, zw, NT):
    keys = [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]
    mass = {k: 0 for k in keys}
    for v in configs:
        i = (NT[v[0]][v[3]] - 22) // 2
        j = (NT[v[1]][v[2]] - 22) // 2
        mass[(min(i, j), max(i, j))] += weight(v)
    mu = {k: F(n, zw) for k, n in mass.items()}
    G = {(0, 0): F(1), (0, 1): F(511, 500), (0, 2): F(1041, 1000),
         (1, 1): F(209, 200), (1, 2): F(533, 500), (2, 2): F(136, 125)}
    U = sum(mu[k] / G[k] for k in keys)
    V = adaptive(G, NT)
    UV = U * V
    target = F(13469160318500002341497, 13473230232438672696000)
    bound = F(7, 5) * (1 + UV) / (1 - UV)
    e_low = sum(F(1, factorial(k)) for k in range(14))
    log2 = e_low > F(2718, 1000) and 2718 ** 7 > 1024 * 1000 ** 7
    four_mu = F(6 * 81, zw)
    four_nu = sum(formation((0, 1, 2, 3), (s,) * 4) for s in range(6))
    best = None
    for mask in range(1, 64):
        chosen = [keys[i] for i in range(6) if mask >> i & 1]
        gap = sum(mu[k] for k in chosen) - adaptive({k: F(k in chosen) for k in keys}, NT)
        if best is None or gap > best[0]:
            best = (gap, tuple(chosen))
    report(
        "plaquette separation",
        UV == target and UV < 1 and log2 and bound < 9268 and F(80237, 9268) > F(865, 100)
        and four_mu - four_nu == F(315, 180128)
        and best[0] == F(30457, 2431728) and best[0] / (four_mu - four_nu) > F(716, 100),
        f"UV<1, threshold bound {float(bound):.2f}<9268, hull gap {best[0]}, four-point {four_mu - four_nu}",
    )


def converse(configs, zw, NT):
    rho = F(0)
    for j in range(3):
        n = sum(weight(v) for v in configs if (NT[v[1]][v[2]] - 22) // 2 == j)
        # sqrt(433/(18 N)) lowered by an integer square root at scale 10^9
        num, den = 433, 18 * (22 + 2 * j)
        # r/10^12 <= sqrt(num/den), and the ratio exceeds 1
        scale = 10 ** 12
        lo, hi = 0, 2 * scale
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if mid * mid * den <= num * scale * scale:
                lo = mid
            else:
                hi = mid - 1
        rho += F(n, zw) * F(lo, scale)
    delta = 1 - rho
    tail = sum(F(1, factorial(k)) for k in range(14)) + F(15, 14) / factorial(14)
    report(
        "converse",
        rho >= F(432875307883, 433000000000) and (1 - delta) / (7 * delta) > 495
        and tail < F(2719, 1000) and 2719 ** 2 * 2187 < 16384 * 10 ** 6,
        f"Hellinger >= {float(rho):.8f}, so m<=495 cannot reach TV 1/2",
    )


def inequalities():
    r = sp.symbols("r", positive=True)
    h = r * sp.log(r) - r + 1
    w1 = sp.diff(h - (r - 1) ** 2 / 2, r, 2)
    w2 = sp.diff(h - (r - 1) ** 2 / (2 * r), r, 2)
    x = sp.symbols("x", positive=True)
    w3 = sp.diff(sp.log(1 / x) - 2 * (1 - x) / (1 + x), x)
    mx = max(sum(prod(PH[s][b] for b in multi) for s in range(6)) for multi in cwr(range(6), 6))
    report(
        "divergence and energy",
        sp.simplify(w1 - (1 / r - 1)) == 0 and sp.simplify(w2 - (r ** 2 - 1) / r ** 3) == 0
        and sp.simplify(w3 + (1 - x) ** 2 / (x * (1 + x) ** 2)) == 0 and mx == 986,
        "the rational divergence bound holds, and the six-neighbour weight is at most 986",
    )


def cliques():
    def offsets(d):
        out = []
        for j in range(d):
            e = tuple(1 if i == j else 0 for i in range(d))
            out += [e, tuple(-a for a in e)]
        for j in range(d):
            for k in range(d):
                if j != k:
                    ej = tuple(1 if i == j else 0 for i in range(d))
                    ek = tuple(1 if i == k else 0 for i in range(d))
                    out.append(tuple(a - b for a, b in zip(ej, ek)))
        return set(out)

    def independent(pred, mod, d):
        pts = [p for p in product(range(mod), repeat=d) if pred(p)]
        off = offsets(d)
        ok = all(tuple((a - b) % mod for a, b in zip(p, q)) not in off
                 for p in pts for q in pts if p != q)
        # differences of the generating set, not of the points: check no two differ by an offset
        ok = all(not pred(tuple((p[i] + v[i]) % mod for i in range(d))) for p in pts for v in off)
        return ok and F(len(pts), mod ** d)

    d2 = independent(lambda p: (p[0] + 2 * p[1]) % 3 == 0, 3, 2)
    d3 = independent(lambda p: (p[0] + 2 * p[1] + 3 * p[2]) % 4 == 0, 4, 3)
    report("rates", d2 == F(1, 3) and d3 == F(1, 4), "independent-set densities 1/3 in Z^2 and 1/4 in Z^3")


def main():
    configs, orders, zw, NT = identity()
    plaquette(configs, orders, zw, NT)
    converse(configs, zw, NT)
    inequalities()
    cliques()
    if fails:
        print("SUMMARY: fails at " + fails[0])
        return
    print(
        "HIT: confirmed - the likelihood is W over the Z(v|A) factors, UV of the published plaquette "
        "test is below 1 so m=9268 disjoint 4-cycles give TV at least 1/2 against the hull, and the "
        "Hellinger bound leaves m<=495 powerless for the nearest fixed order"
    )
    print(
        "SUMMARY: confirmed the identity on every 4-cycle order, Z_W=20784, the UV fraction, "
        "the 9268 and 495 thresholds, the four-point gap 315/180128, and the factor 986. "
        "The price sheet is their reported test, not proved optimal. The Z^3 minimum and the cube TV were not re-summed."
    )


if __name__ == "__main__":
    main()
