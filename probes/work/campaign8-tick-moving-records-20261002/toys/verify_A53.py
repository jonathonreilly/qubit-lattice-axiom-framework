"""Coordinator check of A53's wrapping geometry, from scratch.
16-site cluster: sublattice {even (a,b,c) with a+b+c = 0 mod 4} (lattice vectors 2(1,1,0), 2(1,0,1), 2(0,1,1)).
24-site cluster: lattice vectors 2(1,-1,0), 2(0,1,-1), 2(1,1,1).
For each displacement class, count unordered wrapped pairs by multiplicity (how many displacements of the class join
the same pair).  A53: 16 -> (001)x1 48, (011)x2 48, (111)x4 16, (002)x6 8;
24 -> (001)x1 72, (011)x1 72 + x2 36, (002)x3 24, (111)x2 12 + x3 24; shortest wrap length^2 8 for both."""
import itertools
import numpy as np
from collections import Counter
def cluster(vecs):
    A = np.array(vecs).T
    Ainv = np.linalg.inv(A)
    def canon(x):
        c = np.floor(Ainv @ np.array(x) + 1e-9)
        return tuple(int(v) for v in (np.array(x) - A @ c).round())
    N = round(abs(np.linalg.det(A)))
    sites = sorted({canon(x) for x in itertools.product(range(-8, 9), repeat=3)})
    assert len(sites) == N, (len(sites), N)
    return N, sites, canon
CLASSES = {"(001)": (0, 0, 1), "(011)": (0, 1, 1), "(111)": (1, 1, 1), "(002)": (0, 0, 2)}
def disps(rep):
    out = set()
    for p in itertools.permutations(rep):
        for s in itertools.product((1, -1), repeat=3):
            out.add(tuple(a * b for a, b in zip(s, p)))
    return out
def table(vecs):
    N, sites, canon = cluster(vecs)
    res = {}
    for name, rep in CLASSES.items():
        mult = Counter()
        for x in sites:
            for d in disps(rep):
                y = canon(tuple(np.add(x, d)))
                if y != x: mult[frozenset((x, y))] += 1
        # each unordered pair is reached from both ends; multiplicity per pair = count/2
        res[name] = dict(sorted(Counter(v // 2 for v in mult.values()).items()))
    short = min(sum(v * v for v in np.array(vecs).T @ np.array(c)) for c in itertools.product(range(-2, 3), repeat=3) if any(c))
    return N, res, short
for name, vecs, expect in (("16-site", [(2, 2, 0), (2, 0, 2), (0, 2, 2)],
                            {"(001)": {1: 48}, "(011)": {2: 48}, "(111)": {4: 16}, "(002)": {6: 8}}),
                           ("24-site", [(2, -2, 0), (0, 2, -2), (2, 2, 2)],
                            {"(001)": {1: 72}, "(011)": {1: 72, 2: 36}, "(111)": {2: 12, 3: 24}, "(002)": {3: 24}})):
    N, res, short = table(vecs)
    flat = {k: {m: c for m, c in v.items()} for k, v in res.items()}
    print(f"{name}: N = {N}, shortest wrap length^2 = {short}")
    for k in CLASSES:
        print(f"   {k}: multiplicity -> pairs {flat[k]}  (A53 {expect[k]}) {'OK' if flat[k] == expect[k] else 'DIFF'}")
