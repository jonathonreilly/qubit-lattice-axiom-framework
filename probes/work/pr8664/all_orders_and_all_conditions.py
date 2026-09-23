#!/usr/bin/env python3
"""J:attack-e:PR8664 - pattern (e), sampled evidence: complete order sets and a complete condition search.

The runner of PR #8664 backs several "every order" statements of Theorem 3 with order samples:
  - forcing exclusion on the 7-site cross, "the same two completed configurations with equal mass" for all 5040 orders:
    checked on CROSS_ORDERS[::97] (52 orders), and only that each sub-law has two atoms of equal mass;
  - the soft pair rule on the 8-site path, completion (3/4)^7 "for every order", completed law = the static pair measure
    2^(agreeing bonds), c(0, d) = 3^-d: checked on four declared orders;
  - binary rejection on the 8-site path, completion 1/128, two staggered patterns: checked on one order;
  - six-axis rejection on a 4-site path, agreement 1/5 at d = 2 and 4/25 at d = 3, completion (5/6)^3: one order.
Here each is run over the COMPLETE order set (8! = 40320, 7! = 5040, 4! = 24) by literal sequential formation
(completed histories kept, failed ones dropped), with exact arithmetic and machinery disjoint from the runner.
Adversarial window beyond the note's trees: the soft rule on the 2x2x2 cube (four-cycles), all 40320 orders.
The one extremal statement, "sub-probability rule on every neighbour condition (worst case 65/128)", rests in the runner
on a single evaluated condition (six equal values); here every neighbour condition (0 to 6 formed neighbours) is searched.
Rules, values +-1, r0 uniform: soft r(a|N) = (1/2) prod_b (3/4)(1 + ab/3); binary rejection r(a|N) = (1/2) prod_b 1[a != b];
forcing: fair coin with no formed neighbour, the opposite of unanimous formed neighbours, fail if they disagree.
"""
import math
import sys
from fractions import Fraction as Fr
from itertools import permutations, product

FAILS, DEFECTS = [], []


def ok(tag, good, msg):
    print(("ok " if good else "FAIL ") + tag + ": " + msg)
    if not good:
        FAILS.append(tag)


SCALE = 40  # binary-alphabet masses are dyadic: integers in units of 2^-SCALE (every mass here is >= 2^-21)
ONE, HALF_U = 1 << SCALE, 1 << (SCALE - 1)


def soft(a, vals):
    return HALF_U >> sum(1 for b in vals if b != a)  # (3/4)(1 + ab/3) = 1 if a == b else 1/2


def reject(a, vals):
    return 0 if a in vals else HALF_U


def forcing(a, vals):
    if not vals:
        return HALF_U
    return ONE if all(b == -a for b in vals) else 0


def finished(order, nb, rule, alphabet=(1, -1), unit=ONE):
    """finished sub-law of one order by literal sequential formation; keyed by site-sorted configuration."""
    layer = {(): unit}
    for step, s in enumerate(order):
        idx = [i for i in range(step) if order[i] in nb[s]]
        nxt = {}
        for part, mass in layer.items():
            vals = [part[i] for i in idx]
            for a in alphabet:
                m = rule(a, vals)
                if m:
                    nxt[part + (a,)] = mass * m // unit if unit == ONE else mass * m
        layer = nxt
    where = {s: i for i, s in enumerate(order)}
    return {tuple(part[where[s]] for s in sorted(order)): m for part, m in layer.items()}


def nbrs(sites):
    return {s: {t for t in sites if sum(abs(x - y) for x, y in zip(s, t)) == 1} for s in sites}


def one_law(sites, rule, **kw):
    nb, ref, count = nbrs(sites), None, 0
    for o in permutations(sites):
        law = finished(o, nb, rule, **kw)
        count += 1
        if ref is None:
            ref = law
        elif law != ref:
            return None, count
    return ref, count


# 1. soft pair rule, 8-site path, all orders
PATH8 = tuple((0, 0, z) for z in range(8))
law, n = one_law(PATH8, soft)
Z = Fr(sum(law.values()), ONE) if law else None
w = {c: 2 ** sum(c[i] == c[i + 1] for i in range(7)) for c in product((1, -1), repeat=8)}
cond = {c: Fr(m, sum(law.values())) for c, m in law.items()} if law else {}
good = (law is not None and n == 40320 and Z == Fr(3, 4) ** 7 == Fr(2187, 16384)
        and all(cond.get(c, 0) == Fr(v, sum(w.values())) for c, v in w.items())
        and all(sum(p * c[i] for c, p in cond.items()) == 0 for i in range(8))
        and [sum(p * c[0] * c[d] for c, p in cond.items()) for d in range(1, 8)] == [Fr(1, 3 ** d) for d in range(1, 8)])
ok("P1", good, f"soft pair rule, 8-site path, all {n} orders (runner: 4): one finished sub-law, completion {Z} = (3/4)^7, "
   "completed law = 2^(agreeing bonds)/Z atom by atom, means 0, c(0,d) = 3^-d for d = 1..7")

# 2. binary rejection, 8-site path, all orders
law, n = one_law(PATH8, reject)
stag = {tuple((-1) ** i for i in range(8)), tuple(-(-1) ** i for i in range(8))}
good = law is not None and n == 40320 and Fr(sum(law.values()), ONE) == Fr(1, 128) and set(law) == stag \
    and len(set(law.values())) == 1 and all(c[0] * c[7] == -1 for c in law)
ok("P2", good, f"binary rejection, 8-site path, all {n} orders (runner: 1): one sub-law, completion 1/128, the two "
   "staggered patterns with equal mass, end-to-end correlation -1")

# 3. forcing exclusion, 7-site cross, all orders
O = (0, 0, 0)
CROSS = (O,) + tuple(tuple(s * (i == j) for j in range(3)) for i in range(3) for s in (1, -1))
nbc = nbrs(CROSS)
configs, masses, kmatch, n = set(), set(), True, 0
for o in permutations(CROSS):
    law = finished(o, nbc, forcing)
    n += 1
    configs.add(tuple(sorted(law)))
    masses.add(tuple(sorted(set(law.values()))))
    k = o.index(O)  # leaves formed before the centre
    comp = Fr(sum(law.values()), ONE)
    kmatch &= comp == (1 if k <= 1 else Fr(1, 2 ** (k - 1)))
cstar = sorted(CROSS).index(O)
good = n == 5040 and len(configs) == 1 and all(len(set(c)) == 2 for c in configs) and all(len(m) == 1 for m in masses) \
    and all(cfg[cstar] == -cfg[j] for c in configs for cfg in c for j in range(7) if j != cstar) and kmatch
vals = sorted({Fr(1) if k <= 1 else Fr(1, 2 ** (k - 1)) for k in range(7)}, reverse=True)
ok("P3", good, f"forcing exclusion, 7-site cross, all {n} orders (runner: 52, atom count only): the same two completed "
   "configurations (centre c, every leaf -c) with equal mass in every order; completion = 1 if at most one leaf "
   f"precedes the centre, else 2^(1-k) for k leaves first: {len(vals)} values {', '.join(map(str, vals))}")

# 4. six-axis rejection, 4-site path, all orders (alphabet of 6, r0 = 1/6: Fractions)
SIX = tuple(range(6))
P4 = tuple((0, 0, z) for z in range(4))
law, n = one_law(P4, lambda a, vals: 0 if a in vals else Fr(1, 6), alphabet=SIX, unit=Fr(1))
Z6 = sum(law.values()) if law else None
agree = [sum(m for c, m in law.items() if c[0] == c[d]) / Z6 for d in range(4)] if law else []
good = law is not None and n == 24 and Z6 == Fr(5, 6) ** 3 \
    and agree == [Fr(1, 6) * (1 + 5 * Fr(-1, 5) ** d) for d in range(4)] and agree[2:] == [Fr(1, 5), Fr(4, 25)]
ok("P4", good, f"six-axis rejection, 4-site path, all {n} orders (runner: 1): one sub-law, completion {Z6} = (5/6)^3, "
   f"agreement (1/6)(1 + 5(-1/5)^d) = {', '.join(map(str, agree))} for d = 0..3")

# 5. adversarial window with cycles (not in the note): soft rule on the 2x2x2 cube, all orders
CUBE = tuple(product((0, 1), repeat=3))
law, n = one_law(CUBE, soft)
bonds = [(i, j) for i in range(8) for j in range(i + 1, 8) if sum(abs(x - y) for x, y in zip(CUBE[i], CUBE[j])) == 1]
pair = {c: Fr(1, 2 ** (8 + sum(c[i] != c[j] for i, j in bonds))) for c in product((1, -1), repeat=8)}
good = law is not None and n == 40320 and len(bonds) == 12 and all(Fr(law.get(c, 0), ONE) == p for c, p in pair.items())
ok("P5", good, f"soft rule on the 2x2x2 cube (12 bonds, four-cycles), all {n} orders: one sub-law = prod r0 prod_bonds K "
   f"atom by atom, completion {sum(pair.values())}; the pair-form converse of Theorem 2 holds off trees")

# 6. the extremal label: every unsoldered neighbour condition (0 to 6 formed neighbours)
def soft_total(v):
    return sum(Fr(1, 2) * math.prod([Fr(3, 4) * (1 + Fr(a * b, 3)) for b in v]) for a in (1, -1))


tot = {v: soft_total(v) for k in range(7) for v in product((1, -1), repeat=k)}
hi, lo = max(tot.values()), min(tot.values())
hi1 = max(t for v, t in tot.items() if len(v) >= 1)
hi6 = max(t for v, t in tot.items() if len(v) == 6)
where_lo = sorted({(len(v), v.count(1)) for v, t in tot.items() if t == lo})
where_65 = sorted({(len(v), v.count(1)) for v, t in tot.items() if t == Fr(65, 128)})
ok("P6", len(tot) == 127 and hi == 1 == tot[()] and hi1 == Fr(3, 4) and lo == Fr(1, 8) and where_lo == [(6, 3)]
   and hi6 == Fr(65, 128) and where_65 == [(6, 0), (6, 6)],
   f"soft rule over all {len(tot)} neighbour value lists: a sub-probability everywhere (the note's claim holds); total "
   f"mass max {hi} (no formed neighbour), max {hi1} with a formed neighbour, min {lo} at three +1 and three -1 "
   f"(one-step hole {1 - lo}); 65/128 occurs only at six equal values, the max over six-neighbour lists")
if Fr(65, 128) not in (hi, lo, hi1):
    DEFECTS.append("worst case")

print(f"the sampled order statements: {'all hold over complete order sets' if not FAILS else 'FAIL at ' + ', '.join(FAILS)}")
if FAILS:
    print("SUMMARY: pattern (e) sampled evidence: complete order enumeration contradicts a sampled statement at " + ", ".join(FAILS))
    print("HIT: a sampled 'every order' statement of PR #8664 fails over the complete order set: " + ", ".join(FAILS))
    sys.exit(0)
print("SUMMARY: pattern (e) sampled evidence: every order statement the runner backs with samples (8-site path soft and "
      "rejection, forcing completed law on the cross, six-axis 4-site path) holds exactly over the complete order sets, "
      "and pair-form order-blindness holds on the cube with cycles; "
      + ("the single-condition 'worst case 65/128' is not an extremum over every neighbour condition" if DEFECTS
         else "the 'worst case 65/128' is an extremum over every neighbour condition"))
if DEFECTS:
    print("HIT: PR #8664 result 4 labels 65/128 the worst case of the soft pair rule K = (3/4)(1 + ab/3) on every "
          "neighbour condition, but over every condition its total mass runs from 1/8 (three formed neighbours at +1, "
          "three at -1: one-step hole 7/8) to 1 (none formed), 3/4 with one formed neighbour; 65/128 is the largest total "
          "among six-neighbour conditions only")
