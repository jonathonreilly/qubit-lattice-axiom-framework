"""Independent referee for tight-sibling-vacuity a2.

Own realization of the one-sided majority rule and own level-by-level dynamic program.
Does not call the author's check.py or probes/lib.
"""
import itertools
import sys
from collections import defaultdict
from fractions import Fraction as F

import sympy as sp

FAILS = []


def want(label, ok):
    if not ok:
        FAILS.append(label)
    print(("PASS " if ok else "FAIL ") + label, flush=True)


MARKS = {
    (0, 0, 0), (0, 0, 1), (0, 1, 0), (1, 0, 0),
    (0, 2, 1), (1, 0, 2), (2, 1, 0),
    (1, 1, 3), (1, 3, 1), (3, 1, 1),
}
PI = {(0, 1, 1), (1, 0, 1), (1, 1, 0), (1, 1, 2), (1, 2, 1), (2, 1, 1)}
AMP_ABOVE = {
    (0, 2, 1): (0, 1, 1),
    (1, 0, 2): (1, 0, 1),
    (2, 1, 0): (1, 1, 0),
    (1, 1, 3): (1, 1, 2),
    (1, 3, 1): (1, 2, 1),
    (3, 1, 1): (2, 1, 1),
}


def preds(x):
    return [tuple(x[j] - 1 if j == i else x[j] for j in range(3)) for i in range(3)]


def realize(lo, hi):
    sites = list(itertools.product(range(lo, hi + 1), repeat=3))
    sites.sort(key=sum)
    eta = {}
    for x in sites:
        live = sum(eta.get(p, 0) for p in preds(x))
        eta[x] = 1 if live >= 2 or x in MARKS else 0
    return eta


def ones_of(eta):
    return [x for x, v in eta.items() if v == 1]


def kind_of(eta, x):
    k = sum(eta.get(p, 0) for p in preds(x))
    return "s" if k == 0 else "a" if k == 1 else "p"


# ---------------------------------------------------------------- realization
small = realize(0, 3)
mid = realize(-1, 4)
wide = realize(-2, 6)
ones = ones_of(small)
ok = set(ones_of(mid)) == set(ones) == set(ones_of(wide))
ok = ok and len(ones) == 37 and all(0 <= c <= 3 for x in ones for c in x)
want("S1-S2 the same 37 one-sites appear in [0,3]^3, [-1,4]^3 and [-2,6]^3, all inside the unit box", ok)

by_level = defaultdict(list)
for x in ones:
    by_level[sum(x)].append(x)
for L in by_level:
    by_level[L].sort()
quoted_sizes = [1, 3, 3, 4, 3, 6, 7, 6, 3, 1]
ok = [len(by_level[L]) for L in range(10)] == quoted_sizes
ok = ok and kind_of(small, (0, 0, 0)) == "s"
ok = ok and sum(kind_of(small, x) == "a" for x in ones) == 9
ok = ok and sum(kind_of(small, x) == "p" for x in ones) == 27
ok = ok and [p for p in preds((3, 3, 3)) if small.get(p, 0) == 1] == [(2, 3, 3), (3, 2, 3), (3, 3, 2)]
ok = ok and all(kind_of(small, p) == "p" for p in ((2, 3, 3), (3, 2, 3), (3, 3, 2)))
want("S2 one seed, nine amplified, 27 processed; 333 has three processed 1-predecessors", ok)


def shift(x):
    a, b, c = x
    return (c, a, b)


ok = {shift(x) for x in MARKS} == MARKS and {shift(x) for x in ones} == set(ones)
want("S2 the marks and the one-set are invariant under (a,b,c) -> (c,a,b)", ok)

# ---------------------------------------------------------------- dynamic program: achievable (E, A) by subset of each level
rows = [by_level[L] for L in range(10)]
state = {1: {(0, 0)}}  # the seed, cost (E, A) = (0, 0)
front = {0: state}
for L in range(9):
    prev_row = rows[L]
    row = rows[L + 1]
    new = defaultdict(set)
    n = len(row)
    for pmask, pairs in state.items():
        prev_set = {prev_row[i] for i in range(len(prev_row)) if pmask >> i & 1}
        for mask in range(1 << n):
            e = a = 0
            good = True
            for i in range(n):
                if not (mask >> i & 1):
                    continue
                x = row[i]
                live = [p for p in preds(x) if small.get(p, 0) == 1]
                if not any(p in prev_set for p in live):
                    good = False
                    break
                kd = kind_of(small, x)
                if kd == "p":
                    e += 1
                elif kd == "a":
                    a += 1
            if good:
                bucket = new[mask]
                for E, A in pairs:
                    bucket.add((E + e, A + a))
    state = new
    front[L + 1] = state


def min_cost(level, target):
    row = rows[level]
    bit = row.index(target)
    best = None
    for mask, pairs in front[level].items():
        if mask >> bit & 1:
            for E, A in pairs:
                best = E - A if best is None else min(best, E - A)
    return best


quoted = {
    (0, 0, 0): 0,
    (0, 0, 1): -3, (0, 1, 0): -3, (1, 0, 0): -3,
    (0, 1, 1): -2, (1, 0, 1): -2, (1, 1, 0): -2,
    (0, 2, 1): -3, (1, 0, 2): -3, (1, 1, 1): -2, (2, 1, 0): -3,
    (1, 1, 2): -2, (1, 2, 1): -2, (2, 1, 1): -2,
    (1, 1, 3): -3, (1, 2, 2): -2, (1, 3, 1): -3, (2, 1, 2): -2, (2, 2, 1): -2, (3, 1, 1): -3,
    (1, 2, 3): -2, (1, 3, 2): -2, (2, 1, 3): -2, (2, 2, 2): -1, (2, 3, 1): -2, (3, 1, 2): -2, (3, 2, 1): -2,
    (1, 3, 3): -1, (2, 2, 3): -1, (2, 3, 2): -1, (3, 1, 3): -1, (3, 2, 2): -1, (3, 3, 1): -1,
    (2, 3, 3): 0, (3, 2, 3): 0, (3, 3, 2): 0,
    (3, 3, 3): 1,
}
ok = len(quoted) == 37 and all(min_cost(sum(z), z) == v for z, v in quoted.items())
want("S4 rooted values v(z) match the 37-site table; the only tight sites are 233, 323, 332, and v(333)=1", ok)

# ---------------------------------------------------------------- hand bound premises
ok = set(AMP_ABOVE) <= set(ones) and set(AMP_ABOVE.values()) == PI
for src, dst in AMP_ABOVE.items():
    live = [p for p in preds(src) if small.get(p, 0) == 1]
    ok = ok and live == [dst] and kind_of(small, src) == "a" and kind_of(small, dst) == "p"
for L in (6, 7, 8, 9):
    ok = ok and all(kind_of(small, x) == "p" and x not in PI for x in rows[L])
ok = ok and len(PI) == 6
want("S5 the six upper amplified sites inject into Pi, and levels 6..9 are processed and disjoint from Pi", ok)

# ---------------------------------------------------------------- explicit trees
def tree_ok(nodes, arrows, root, expect):
    nodes = set(nodes)
    if root not in nodes or (0, 0, 0) not in nodes:
        return False
    if len(arrows) != len(nodes) - 1:
        return False
    seen = {(0, 0, 0)}
    for y, p in arrows.items():
        if y not in nodes or p not in nodes or p not in preds(y) or small.get(p, 0) != 1:
            return False
        if kind_of(small, y) == "a":
            only = [q for q in preds(y) if small.get(q, 0) == 1]
            if only != [p]:
                return False
        if sum(y) > sum(root):
            return False
    # every non-seed has one arrow and the arrows reach the seed
    incoming = {y: p for y, p in arrows.items()}
    if set(incoming) != nodes - {(0, 0, 0)}:
        return False
    for y in nodes:
        x = y
        guard = 0
        while x != (0, 0, 0):
            x = incoming[x]
            guard += 1
            if guard > len(nodes):
                return False
    E = sum(kind_of(small, y) == "p" for y in nodes)
    A = sum(kind_of(small, y) == "a" for y in nodes)
    return (E, A, E - A) == expect


t233 = [
    (0, 0, 0), (0, 0, 1), (0, 1, 0), (1, 0, 0), (1, 0, 1), (1, 0, 2),
    (1, 1, 2), (1, 1, 3), (1, 2, 3), (1, 3, 3), (2, 3, 3),
]
a233 = {
    (0, 0, 1): (0, 0, 0), (0, 1, 0): (0, 0, 0), (1, 0, 0): (0, 0, 0),
    (1, 0, 1): (1, 0, 0), (1, 0, 2): (1, 0, 1), (1, 1, 2): (1, 0, 2),
    (1, 1, 3): (1, 1, 2), (1, 2, 3): (1, 1, 3), (1, 3, 3): (1, 2, 3),
    (2, 3, 3): (1, 3, 3),
}
t333 = [
    (0, 0, 0), (0, 0, 1), (0, 1, 0), (1, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0),
    (0, 2, 1), (1, 0, 2), (2, 1, 0), (1, 1, 2), (1, 2, 1), (2, 1, 1),
    (1, 1, 3), (1, 3, 1), (3, 1, 1), (1, 2, 3), (1, 3, 3), (2, 3, 3), (3, 3, 3),
]
a333 = {
    (0, 0, 1): (0, 0, 0), (0, 1, 0): (0, 0, 0), (1, 0, 0): (0, 0, 0),
    (0, 1, 1): (0, 0, 1), (1, 0, 1): (1, 0, 0), (1, 1, 0): (0, 1, 0),
    (0, 2, 1): (0, 1, 1), (1, 0, 2): (1, 0, 1), (2, 1, 0): (1, 1, 0),
    (1, 1, 2): (1, 0, 2), (1, 2, 1): (0, 2, 1), (2, 1, 1): (2, 1, 0),
    (1, 1, 3): (1, 1, 2), (1, 3, 1): (1, 2, 1), (3, 1, 1): (2, 1, 1),
    (1, 2, 3): (1, 1, 3), (1, 3, 3): (1, 2, 3), (2, 3, 3): (1, 3, 3),
    (3, 3, 3): (2, 3, 3),
}
ok = tree_ok(t233, a233, (2, 3, 3), (5, 5, 0)) and tree_ok(t333, a333, (3, 3, 3), (10, 9, 1))
want("S6 the exhibited trees are legal: cost 0 at 233 with (E,A)=(5,5), cost 1 at 333 with (E,A)=(10,9)", ok)

# ---------------------------------------------------------------- c* at this root
pairs = set()
for mask, ps in front[9].items():
    if mask & 1:
        pairs |= ps
ratios = [F(E, A) for E, A in pairs if A >= 1]
ok = len(pairs) == 184 and min(ratios) == F(10, 9) and (10, 9) in pairs
ok = ok and min(E - F(10, 9) * A for E, A in pairs if A >= 1) == 0
c = F(10, 9) - F(1, 1000)
ok = ok and min(E - c * A for E, A in pairs if A >= 1) > 0
ok = ok and all(E - A >= 1 for E, A in pairs)
want("S8 over all 184 attainable pairs at 333, min E/A = 10/9, so the budget E <= c A holds iff c >= 10/9", ok)

# ---------------------------------------------------------------- T4.2 floor, inputs assumed, arithmetic checked
t = sp.symbols("t", positive=True)
glog = sp.Rational(10, 9) * sp.log(t) + sp.log(sp.Rational(4, 27) - t)
d2 = sp.simplify(sp.diff(glog, t, 2))
target = -sp.Rational(10, 9) / t ** 2 - 1 / (sp.Rational(4, 27) - t) ** 2
ok = sp.simplify(d2 - target) == 0
t_star = F(40, 513)
ok = ok and F(10, 9) * (F(4, 27) - t_star) == t_star
ok = ok and F(4, 27) - t_star == F(36, 513)
# d3' numerator is -2p^2 - 22p
p = sp.symbols("p", positive=True)
d3 = (2 * p + 11) / (p ** 2 + 2 * p + 11)
num, den = sp.fraction(sp.together(sp.diff(d3, p)))
ok = ok and sp.simplify(num - (-2 * p ** 2 - 22 * p)) == 0
ok = ok and sp.simplify(den - (p ** 2 + 2 * p + 11) ** 2) == 0
want("S9 g is strictly log-concave, the maximum is at t=40/513, and d3 is strictly decreasing for p>0", ok)


def below_h(p):
    left = (2 * p + 11) ** 9 * 513 ** 19
    right = 40 ** 10 * 36 ** 9 * (p * p + 2 * p + 11) ** 9
    return left < right


def below_c1(p):
    return (2 * p + 11) * 729 < 4 * (p * p + 2 * p + 11)


ok = (not any(below_h(p) for p in range(1, 489))) and all(below_h(p) for p in range(489, 5001))
ok = ok and (not below_c1(367)) and below_c1(368)
ok = ok and F(2, 27) * (F(4, 27) - F(2, 27)) == F(4, 729)
want("S9 on the assumed T4.2 inputs, c>=10/9 fails for every p<=488 and holds for 489..5000; the c=1 control crosses between 367 and 368", ok)

print(f"TOTAL FAIL={len(FAILS)}")
if FAILS:
    print("SUMMARY: fails at " + FAILS[0])
    sys.exit(1)
print(
    "HIT: confirmed - (Q) is false. Marks {000,001,010,100,021,102,210,113,131,311} give a one-seed realization "
    "whose site 333 is processed with three tight processed 1-predecessors (v=0) and rooted value v(333)=1. "
    "Every one-seed tree there has E/A >= 10/9, attained at (E,A,S)=(10,9,1), so c*(eta,333)=10/9 and the unit budget fails. "
    "Conditional on block 32 T4.2's inputs the (p,1,2) floor moves from 367 to 488."
)
print(
    "SUMMARY: confirmed the counterexample to (Q), the tight-sibling lemma, and (H). "
    "The 37 rooted values and the ratio 10/9 were recomputed by an independent dynamic program. "
    "Block 30's upper bound c*=2 and the T4.2 inputs eps2 >= d3 stay assumed. Coexistence thresholds were not re-derived."
)
