"""Refuting pass, block 39 (machinery disjoint from the runner's detailed-balance checks): the STATIONARY LAW of each transit reading by an
exact linear solve on the 2x3 window, two-valued menu with weights (3, 1) and (6, 2) (the same rule at twice the scale), with one vacancy
(five records) and with two (four records); compared with the static law on the occupied set; and the chance that four records form a
2x2 clump (12 of the 90 arrangements, 0.1333, if placed at random).  Exact rational arithmetic (sympy nullspace)."""
from fractions import Fraction
from itertools import permutations
import sympy as sp
sites = list(range(6)); edges = [(0,1),(1,2),(3,4),(4,5),(0,3),(1,4),(2,5)]
nb = {x: [] for x in sites}
for a, b in edges: nb[a].append(b); nb[b].append(a)
def run(p, q, contents, reading):
    W = [[Fraction(p), Fraction(q)], [Fraction(q), Fraction(p)]]
    states = sorted(set(permutations(contents)), key=str); ix = {s: i for i, s in enumerate(states)}; n = len(states)
    def weight(s, x, c, excl):
        w = Fraction(1)
        for z in nb[x]:
            if z != excl and s[z] is not None: w *= W[c][s[z]]
        return w
    P = [[Fraction(0)] * n for _ in range(n)]
    for s in states:
        i = ix[s]
        for a, b in edges:
            for x, y in ((a, b), (b, a)):
                if s[x] is not None and s[y] is None:
                    c = s[x]; t = list(s); t[y], t[x] = c, None; t = tuple(t)
                    if reading == "normalized":
                        ws = [weight(s, y, v, x) for v in (0, 1)]; acc = ws[c] / sum(ws)
                    else:
                        wy, wx = weight(s, y, c, x), weight(s, x, c, y); acc = wy / (wy + wx)
                    P[i][ix[t]] += Fraction(1, 7) * acc
        P[i][i] = 1 - sum(P[i])
    A = sp.Matrix([[P[j][i] - (1 if i == j else 0) for j in range(n)] for i in range(n)]); ns = A.nullspace(); pi = ns[0] / sum(ns[0])
    def static(s):
        w = Fraction(1)
        for a, b in edges:
            if s[a] is not None and s[b] is not None: w *= W[s[a]][s[b]]
        return w
    st = sp.Matrix([static(s) for s in states]); st = st / sum(st)
    tv = sum(abs(pi[i] - st[i]) for i in range(n)) / 2
    db = all(pi[i] * P[i][j] == pi[j] * P[j][i] for i in range(n) for j in range(n))
    blocks = ({0, 1, 3, 4}, {1, 2, 4, 5}); clump = sum(pi[ix[s]] for s in states if {x for x in sites if s[x] is not None} in blocks)
    return n, len(ns), tv, db, clump
for contents, label in (((0, 0, 0, 1, 1, None), "one vacancy"), ((0, 0, 1, 1, None, None), "two vacancies")):
    for (p, q) in ((3, 1), (6, 2)):
        for reading in ("normalized", "pair-weight"):
            n, k, tv, db, clump = run(p, q, contents, reading)
            print(f"{label}, weights ({p},{q}), {reading} reading: {n} states, stationary laws {k}; total variation to the static law {tv} = {float(tv):.4f}; detailed balance {db}" + (f"; P(2x2 clump) = {float(clump):.4f}" if "two" in label else ""))
