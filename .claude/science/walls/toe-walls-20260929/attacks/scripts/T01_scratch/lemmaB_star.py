#!/usr/bin/env python3
"""Lemma B check (T01): star-window projectivity of the pair order forces a constant hazard.

Window: star with centre c and m leaves l1..lm (m <= 6, the degree in Z^3).
Hazard of a site = f(k), k = number of already formed neighbours (records-only).
P_m(c before l1) is computed exactly by recursion over j = number of the other m-1 leaves formed.
In the two-site window {c, l1} the value is 1/2. Claim: P_m = 1/2 for all m <= 6 iff f(0)=...=f(5).
Also print strict monotonicity in f_j (d/df_j > 0) by finite differences.
Author: Claude Sonnet 5.5.
"""
from fractions import Fraction as F
import itertools, json, sys


def P_c_before_l1(m, f):
    """f: list f[0..5]. leaves other than l1: m-1 of them (rate f0 each until c forms)."""
    from functools import lru_cache

    @lru_cache(None)
    def go(j):
        # j other leaves formed; c rate f[j]; l1 rate f0 ; (m-1-j) unformed other leaves rate f0
        rc = f[j]
        rl1 = f[0]
        ro = (m - 1 - j) * f[0]
        tot = rc + rl1 + ro
        val = rc / tot
        if m - 1 - j > 0:
            val += (ro / tot) * go(j + 1)
        return val

    return go(0)


out = {}
# constant hazard gives 1/2 for every m
for m in range(1, 7):
    out[f'const_m{m}'] = str(P_c_before_l1(m, [F(3)] * 6))
# if f1 != f0 already m=2 breaks; if f_j deviates only at j=m-1 it is caught first at m = j+1
viol = []
base = [F(1)] * 6
for j in range(1, 6):
    for delta in (F(1, 2), F(2), F(3)):
        f = list(base)
        f[j] = delta
        vals = {m: P_c_before_l1(m, f) for m in range(1, 7)}
        firstbad = min((m for m, v in vals.items() if v != F(1, 2)), default=None)
        viol.append((j, str(delta), firstbad, {m: float(v) for m, v in vals.items()}))
out['single_deviation'] = viol
# strict monotonicity in f_j for m = j+1 (state j reachable): P increases with f_j
mono = []
for j in range(1, 6):
    m = j + 1
    ps = []
    for x in (F(1, 2), F(1), F(2), F(4)):
        f = list(base)
        f[j] = x
        ps.append(float(P_c_before_l1(m, f)))
    mono.append((j, ps, all(a < b for a, b in zip(ps, ps[1:]))))
out['monotone_in_fj'] = mono
# compensating deviations: can two deviations cancel in a single m?  yes for one m, but not for all m
cancel = []
f = [F(1), F(1), F(1), F(1), F(1), F(1)]
for x1 in (F(1, 2), F(2)):
    # choose f2 to cancel deviation f1 at m=3 exactly, by bisection on Fractions
    lo, hi = F(1, 100), F(100)
    tgt = F(1, 2)
    for _ in range(60):
        mid = (lo + hi) / 2
        ff = [F(1), x1, mid, F(1), F(1), F(1)]
        v = P_c_before_l1(3, ff)
        if v < tgt:
            lo = mid
        else:
            hi = mid
    ff = [F(1), x1, (lo + hi) / 2, F(1), F(1), F(1)]
    cancel.append((str(x1), float((lo + hi) / 2), [float(P_c_before_l1(m, ff)) for m in range(1, 7)]))
out['cancellation_at_m3_only'] = cancel
print(json.dumps(out, indent=1))
json.dump(out, open('lemmaB_star_results.json', 'w'), indent=1)
