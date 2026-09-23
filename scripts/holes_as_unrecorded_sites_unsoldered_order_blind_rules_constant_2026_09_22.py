#!/usr/bin/env python3
"""Holes as unrecorded sites: under the Record text, every unsoldered
order-blind nearest-neighbour rule is constant, so every admissible
unsoldered rule makes the formation order visible.  Exact and finite.

Next-steps campaign after the TOE derivation campaign by underdetermination
witnesses.  Exact rational arithmetic; no floating point.

Declared objects
  * the Record and Qualification text: a record locks exactly one
    admissible possibility when present; a site with no record cannot be
    read; a state is a configuration of records; a law gives exactly one
    answer where its supplied condition (domain) holds;
  * finished states over the alphabet plus an unrecorded mark h: a site
    whose neighbour condition lies outside the rule's domain (no admissible
    possibility), or which fails formation with the deficit of a
    sub-probability rule, carries no record, and formation continues; its
    neighbours cannot read it;
  * domain rules (normalised on every condition of the domain, holes
    exactly outside it) and deficit rules (sub-probabilities, the previous
    block's model), under the unsoldered reading (unchanged when neighbour
    positions rotate with values fixed; the examples are direction-blind);
  * windows: two adjacent sites, the bent path, the 4-site star and the
    7-site cross; example rules: binary rejection and soft pair rules
    (deficit), binary and six-axis exclusion normalised on their domain,
    and a constant erasure rule.

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import sys
from fractions import Fraction as Fr
from itertools import permutations

RESULTS = []


def check(label, ok, detail=""):
    ok = bool(ok)
    RESULTS.append(ok)
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {label}" + (f" :: {detail}" if detail else ""))
    return ok


def vadd(a, b):
    return tuple(x + y for x, y in zip(a, b))


H = "h"
EX, EY, EZ = (1, 0, 0), (0, 1, 0), (0, 0, 1)
DIRS = (EX, (-1, 0, 0), EY, (0, -1, 0), EZ, (0, 0, -1))
O0 = (0, 0, 0)
PAIR = (O0, EX)
BENT = (O0, EX, EY)
STAR4 = (O0, EX, EY, EZ)
CROSS = (O0,) + DIRS


def nbr_values(site, formed):
    return tuple(sorted(formed[vadd(site, d)] for d in DIRS if vadd(site, d) in formed))


def finished_states(sites, alphabet, rule, order, drop=False):
    """Exact law of finished states (records or h per site) for one order.
    drop=True keeps only histories with no unrecorded site (the previous block's convention)."""
    layer = {(): Fr(1)}
    for s in order:
        nxt = {}
        for part, mass in layer.items():
            formed = {order[i]: part[i] for i in range(len(part)) if part[i] != H}
            probs = rule(nbr_values(s, formed))
            tot = Fr(0)
            for a in alphabet:
                p = probs.get(a, Fr(0))
                if p:
                    nxt[part + (a,)] = nxt.get(part + (a,), Fr(0)) + mass * p
                    tot += p
            if tot < 1 and not drop:
                nxt[part + (H,)] = nxt.get(part + (H,), Fr(0)) + mass * (1 - tot)
        layer = nxt
    pos = {s: i for i, s in enumerate(order)}
    out = {}
    for part, mass in layer.items():
        key = tuple(part[pos[s]] for s in sites)
        out[key] = out.get(key, Fr(0)) + mass
    return out


B2 = (1, -1)
HALF = Fr(1, 2)
SIX = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))


def rejection_deficit(vals):
    return {a: HALF for a in B2 if a not in vals}


def soft_deficit(vals):
    out = {}
    for a in B2:
        p = HALF
        for b in vals:
            p *= Fr(3, 4) * (1 + Fr(a * b, 3))
        out[a] = p
    return out


def exclusion_domain(alphabet):
    """Normalised on the admissible values; no admissible value means outside the domain."""
    def rule(vals):
        allowed = [a for a in alphabet if a not in vals]
        return {a: Fr(1, len(allowed)) for a in allowed}
    return rule


EXCL2 = exclusion_domain(B2)
EXCL6 = exclusion_domain(SIX)
DELTA0 = Fr(1, 3)


def erasure(vals):
    return {a: (1 - DELTA0) / 2 for a in B2}


print("== 1. Two sites: order-blindness forces a constant hole rate and a full domain ==")
XY = finished_states(PAIR, B2, rejection_deficit, PAIR)
YX = finished_states(PAIR, B2, rejection_deficit, tuple(reversed(PAIR)))
check("deficit rejection, holes unrecorded: the hole sits at the later site, so the two orders differ",
      sum(m for c, m in XY.items() if c[1] == H) == HALF and sum(m for c, m in XY.items() if c[0] == H) == 0
      and sum(m for c, m in YX.items() if c[0] == H) == HALF and XY != YX,
      "P(x = a, y = h) = r0(a) delta(a) in one order and delta0 r0(a) in the other: order-blind forces delta(a) = delta0")
check("hole rates: rejection has delta(a) = 1/2, soft pair delta(a) = 1/4, against delta0 = 0 at an empty condition",
      1 - sum(rejection_deficit((1,)).values()) == HALF and 1 - sum(soft_deficit((1,)).values()) == Fr(1, 4)
      and sum(rejection_deficit(()).values()) == 1 == sum(soft_deficit(()).values())
      and soft_deficit((1,))[1] == Fr(1, 2) and soft_deficit((-1,))[1] == Fr(1, 4),
      "any gap delta(a) != delta0 is a difference between the two orders of an adjacent pair")
DXY = finished_states(PAIR, B2, rejection_deficit, PAIR, drop=True)
DYX = finished_states(PAIR, B2, rejection_deficit, tuple(reversed(PAIR)), drop=True)
check("the same rule under the drop convention is order-blind on the pair: the escape lives in the convention",
      DXY == DYX and sum(DXY.values()) == HALF)
EXY = finished_states(PAIR, B2, EXCL2, PAIR)
check("binary exclusion normalised on its domain has no hole on the pair: every one-neighbour condition admits a value",
      all(c[0] != H and c[1] != H for c in EXY) and EXY == finished_states(PAIR, B2, EXCL2, tuple(reversed(PAIR))))

print()
print("== 2. The bent path, star and cross: every varying rule shows the order ==")
BENT_ORDERS = list(permutations(BENT))


def distinct_laws(sites, alphabet, rule, orders, drop=False):
    laws = []
    for o in orders:
        L = finished_states(sites, alphabet, rule, o, drop)
        if L not in laws:
            laws.append(L)
    return laws


L_EX2 = distinct_laws(BENT, B2, EXCL2, BENT_ORDERS)
hole_centre = {sum(m for c, m in finished_states(BENT, B2, EXCL2, o).items() if c[0] == H) for o in BENT_ORDERS}
check("binary exclusion on its domain, bent path: 2 distinct finished-state laws; the centre is unrecorded w.p. 1/2 or 0",
      len(L_EX2) == 2 and hole_centre == {HALF, Fr(0)},
      "leaves first: they disagree half the time and the centre then has no admissible value")
CROSS_ORDERS = [tuple(CROSS[1:k + 1]) + (CROSS[0],) + tuple(CROSS[k + 1:]) for k in range(7)]
for name, rule in (("deficit rejection", rejection_deficit), ("soft pair", soft_deficit), ("domain exclusion", EXCL2)):
    n_unrec = len(distinct_laws(CROSS, B2, rule, CROSS_ORDERS))
    n_drop = len(distinct_laws(CROSS, B2, rule, CROSS_ORDERS, drop=True))
    check(f"{name} on the 7-site cross, centre formed k-th (k = 1..7): distinct laws, unrecorded-site {n_unrec}",
          n_unrec > 1,
          f"under the drop convention: {n_drop} law(s)")
L_EX6 = distinct_laws(STAR4, SIX, EXCL6, list(permutations(STAR4))[:12])
check("six-axis exclusion on its domain, 4-site star: order-sensitive (the domain is never left, the values show it)",
      len(L_EX6) > 1
      and all(all(v != H for v in c) for L in L_EX6 for c in L))
ER_LAWS = distinct_laws(STAR4, B2, erasure, list(permutations(STAR4)))
check("constant erasure (delta0 = 1/3, values fair) is order-blind on all 24 star orders, and it does not vary",
      len(ER_LAWS) == 1 and all(erasure(v) == erasure(()) for v in ((1,), (-1,), (1, -1), (1, 1, 1))),
      "the only order-blind unsoldered rules under the Record text: constant values, constant hole rate")

print()
print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
