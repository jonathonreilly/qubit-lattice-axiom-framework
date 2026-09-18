#!/usr/bin/env python3
"""J:attack:PR8150 - block 16 (PR #8150), attack pattern (c) EXECUTED NUMBERS: every executed count and value named in the claim scope
and the note's executed statements, recomputed independently and compared with the note, the runner's cached stdout and the two control
outputs on the PR branch (supervisor_control_block16_flip_monotonicity.out.txt, supervisor_control_block16_refuter.out.txt):
  * X1 on every (order, site) pair of the plaquette (96; 48 strict), 2x3 (4320; 2592 strict) and the cube (322560 order-site pairs;
    230400 strict in the control; 542 multiset classes, 4336 class-site pairs, 3184 strict in the runner), the flip ratio computed from
    the FULL sequential laws mu_sigma(v^z)/mu_sigma(v) times the edge-product ratio (p/q)^deg(z) (not from the note's weight formula),
    strictness against the criterion z in a recorded set of size >= 2;
  * the qualifying orders (every site records at most one neighbour) of the path of three (4 of 6) and the four-leaf star (48 of 120) by
    a direct search, the uniform mixture over them against the static law exactly, and a mixture charging one non-qualifying order;
  * the 2x3 uniform mixture's total-variation distance from the static law, 372254646387017/12790481418000000, recomputed exactly;
  * the number of multiset classes (the runner's key: the multiset of recorded sets of size >= 2) of the plaquette (4), 2x3 (28) and the
    cube (542), with the number of distinct recorded-set structures (acyclic orientations) for reference;
  * the domino in the all-+x environment: the second site's normalizer at first = +x vs -x, 493/1492992 and 251/1492992.
Six-axis menu, product rule (p, q, r) = (3, 1, 2), Z_1 = 12, exact rational arithmetic.  HIT if a recomputed number differs from the
stated one.
"""
import itertools
import math
import sys
import time
from fractions import Fraction as F

P_, Q_, R_ = 3, 1, 2
M = 6


def phi(s, t):
    if s == t:
        return P_
    if s // 2 == t // 2:
        return Q_
    return R_


Z1 = sum(phi(0, t) for t in range(M))
_C = {}


def cond(rec, a):
    """r(a | recorded values rec) = prod phi(a, v_y) / sum_s prod phi(s, v_y); 1/M with no recorded neighbour."""
    key = (rec, a)
    if key not in _C:
        if not rec:
            _C[key] = F(1, M)
        else:
            num = math.prod(phi(a, y) for y in rec)
            den = sum(math.prod(phi(s, y) for y in rec) for s in range(M))
            _C[key] = F(num, den)
    return _C[key]


def graph(pos):
    sites = sorted(pos)
    nb = {i: [j for j in sites if sum(abs(pos[i][k] - pos[j][k]) for k in range(3)) == 1] for i in sites}
    edges = [(i, j) for i in sites for j in nb[i] if i < j]
    return sites, nb, edges


def seq_prob(order, nb, v):
    seen, pr = set(), F(1)
    for x in order:
        pr *= cond(tuple(sorted(v[y] for y in nb[x] if y in seen)), v[x])
        seen.add(x)
    return pr


def recorded(order, nb):
    seen, out = set(), {}
    for x in order:
        out[x] = tuple(sorted(y for y in nb[x] if y in seen))
        seen.add(x)
    return out


def mkey(order, nb):
    return tuple(sorted(A for A in recorded(order, nb).values() if len(A) >= 2))


def static(sites, edges):
    w = {v: math.prod(phi(v[i], v[j]) for i, j in edges) for v in itertools.product(range(M), repeat=len(sites))}
    Z = sum(w.values())
    return {v: F(x, Z) for v, x in w.items()}


WIN = {
    "plaquette": {0: (0, 0, 0), 1: (1, 0, 0), 2: (1, 1, 0), 3: (0, 1, 0)},
    "2x3": {i: (i // 3, i % 3, 0) for i in range(6)},
    "cube": {i: (i & 1, (i >> 1) & 1, (i >> 2) & 1) for i in range(8)},
    "path3": {0: (0, 0, 0), 1: (1, 0, 0), 2: (2, 0, 0)},
    "star4": {0: (0, 0, 0), 1: (1, 0, 0), 2: (-1, 0, 0), 3: (0, 1, 0), 4: (0, -1, 0)},
}


def flip_census(name):
    sites, nb, edges = graph(WIN[name])
    b, mb = 0, 1                                   # +x and -x (p != q)
    v = {x: b for x in sites}
    pairs = strict = bad = 0
    keys, orients = set(), set()
    key_strict = {}
    for order in itertools.permutations(sites):
        base = seq_prob(order, nb, v)
        rec = recorded(order, nb)
        union = set().union(*[set(A) for A in rec.values() if len(A) >= 2]) if any(len(A) >= 2 for A in rec.values()) else set()
        k = mkey(order, nb)
        keys.add(k)
        orients.add(tuple(rec[x] for x in sites))
        for z in sites:
            vz = dict(v)
            vz[z] = mb
            ratio = seq_prob(order, nb, vz) / base * F(P_, Q_) ** len(nb[z])
            pairs += 1
            s = ratio > 1
            strict += s
            if ratio < 1 or s != (z in union):
                bad += 1
            key_strict[(k, z)] = s
    return pairs, strict, bad, len(keys), len(orients), len(key_strict), sum(key_strict.values())


def main():
    t0 = time.time()
    hits = []
    stated = {"plaquette": (96, 48, 4, None, None), "2x3": (4320, 2592, 28, None, None), "cube": (322560, 230400, 542, 4336, 3184)}
    for name in ("plaquette", "2x3", "cube"):
        pairs, strict, bad, nkeys, norient, kpairs, kstrict = flip_census(name)
        sp, ss, sk, skp, sks = stated[name]
        print(f"[X1] {name}: {pairs} order-site pairs, {strict} strict, {bad} failures of monotonicity or of the strictness criterion; "
              f"{nkeys} multiset classes ({norient} distinct recorded-set structures), {kpairs} class-site pairs, {kstrict} strict  "
              f"({time.time() - t0:.0f}s)")
        if bad:
            hits.append(f"X1 fails on {bad} pairs of the {name}")
        if (pairs, strict, nkeys) != (sp, ss, sk):
            hits.append(f"{name}: recomputed ({pairs}, {strict}, {nkeys}) vs stated ({sp}, {ss}, {sk})")
        if skp is not None and (kpairs, kstrict) != (skp, sks):
            hits.append(f"{name}: class-site pairs ({kpairs}, {kstrict}) vs stated ({skp}, {sks})")
    # qualifying orders and mixtures on the path and the star
    for name, want in (("path3", (4, 6)), ("star4", (48, 120))):
        sites, nb, edges = graph(WIN[name])
        orders = list(itertools.permutations(sites))
        good = [o for o in orders if all(len(A) <= 1 for A in recorded(o, nb).values())]
        st = static(sites, edges)
        mix = {v: sum(seq_prob(o, nb, v) for o in good) / len(good) for v in st}
        eq = all(mix[v] == st[v] for v in st)
        badord = next(o for o in orders if o not in good)
        mix2 = {v: (F(999, 1000) * sum(seq_prob(o, nb, v) for o in good) / len(good) + F(1, 1000) * seq_prob(badord, nb, v)) for v in st}
        diff = sum(abs(mix2[v] - st[v]) for v in st) / 2
        print(f"[X2] {name}: {len(good)} of {len(orders)} orders qualify (direct search); uniform mixture over them equals the static law: {eq}; "
              f"a mixture giving weight 1/1000 to the non-qualifying order {badord} is at TV {float(diff):.3e}")
        if (len(good), len(orders)) != want or not eq or diff == 0:
            hits.append(f"{name}: qualifying {len(good)}/{len(orders)} (stated {want[0]}/{want[1]}), equality {eq}, TV {diff}")
    # 2x3 uniform mixture distance
    sites, nb, edges = graph(WIN["2x3"])
    orders = list(itertools.permutations(sites))
    cls = {}
    for o in orders:
        cls.setdefault(mkey(o, nb), []).append(o)
    st = static(sites, edges)
    mix = {v: F(0) for v in st}
    for k, os_ in cls.items():
        rep = os_[0]
        for v in st:
            mix[v] += len(os_) * seq_prob(rep, nb, v)
    tvd = sum(abs(mix[v] / len(orders) - st[v]) for v in st) / 2
    want = F(372254646387017, 12790481418000000)
    # the class reduction is itself tested: two orders of one class give the same law on 200 patterns
    same = all(seq_prob(os_[0], nb, v) == seq_prob(os_[-1], nb, v) for os_ in cls.values() for v in list(st)[:: 233])
    print(f"[X2] 2x3: uniform mixture over 720 orders ({len(cls)} classes; class laws coincide within a class: {same}): TV from the static law "
          f"= {tvd} = {float(tvd):.12f}; stated {want}: equal {tvd == want}  ({time.time() - t0:.0f}s)")
    if tvd != want or not same:
        hits.append(f"2x3 uniform-mixture distance recomputed as {tvd} vs {want}")
    # domino in the all-+x environment
    b, mb = 0, 1
    K6 = lambda first: sum(F(phi(s, first), Z1) * F(phi(s, b), Z1) ** 5 for s in range(M))
    k_same, k_opp = K6(b), K6(mb)
    print(f"[X3] domino in the all-+x environment: K_6(first, five +x) = {k_same} (first = +x) vs {k_opp} (first = -x); stated 493/1492992 and 251/1492992")
    if (k_same, k_opp) != (F(493, 1492992), F(251, 1492992)):
        hits.append(f"domino normalizers {k_same}, {k_opp}")
    print(f"[time] {time.time() - t0:.0f}s")
    for h in hits:
        print("HIT: " + h)
    print(f"SUMMARY: attack pattern (c) EXECUTED NUMBERS - block 16's executed counts and values recomputed independently (flip ratios from the "
          f"full sequential laws; direct searches; exact rationals): plaquette 96/48, 2x3 4320/2592, cube 322560/230400 with 542 classes, "
          f"4336 class-site pairs, 3184 strict; path 4/6, star 48/120 with exact equality of the qualifying mixtures; 2x3 uniform-mixture TV "
          f"372254646387017/12790481418000000; domino 493/1492992 vs 251/1492992; {len(hits)} discrepancies; attack {'FIRES' if hits else 'does not fire'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
