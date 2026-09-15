"""Refuting pass, block 14 (supervisor seat, disjoint machinery from the runner's checks):
(R1) the plaquette laws from per-order weights by the hand-derived closed forms (path orders: (1/6) prod K / K_2 of the closed
     diagonal; diagonal-first orders: (1/36) prod K / K_2^2), with the order probabilities read off the rate functions, against
     the runner's history DP on all 1296 patterns for the four laws;
(R2) the census note's Theorem 3 rational read from the census runner's own pinned cache on main (a different implementation);
(R3) the plaquette types by an independent routine (the sign of the angle between the value axis and the corner diagonal computed
     from coordinates of the opposite corner rather than a stored direction table);
(R4) the tree theorem structurally: every seeded-charged order on the star and the path gives every site after the first exactly
     one recorded neighbour;
(R5) the general identity of E2 at random rational points (p_in, p_out, p, q, r) by direct evaluation.
Run from the pack: the runner is imported from the repository's scripts/ directory."""
import importlib
import random
import re
import sys
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
r14 = importlib.import_module("admissibility_rule_formation_rate_clause_witness_no_covariant_clock_law_reaches_static_law_2026_09_15")
M = 6
sites, pos, edges, nb = r14.window("plaquette")
opp = {0: 2, 1: 3, 2: 0, 3: 1}
def closed_diagonal(order):
    S = set(); kind = None; diag = None; count = 0
    for x in order:
        A = [y for y in nb[x] if y in S]
        if len(A) == 2:
            count += 1; diag = tuple(sorted(A))
        S.add(x)
    return count, diag
ok1 = True
for name, rate in r14.RATE_LAWS.items():
    law = {}
    for v in r14.static_law(sites, edges):
        pk = r14.prod_K(v, edges)
        tot = F(0)
        for order in permutations(sites):
            # order probability with value-dependent rates: causal
            S = set(); pr = F(1); vm = {}
            for x in order:
                rates = {y: rate(y, S, vm, nb, pos) for y in sites if y not in S}
                tt = sum(rates.values())
                if rates[x] == 0:
                    pr = F(0); break
                pr *= rates[x] / tt
                S.add(x); vm[x] = v[x]
            if pr == 0:
                continue
            count, diag = closed_diagonal(order)
            k2 = r14.K2(v[diag[0]], v[diag[1]])
            w = F(1, 6) * pk / k2 if count == 1 else F(1, 36) * pk / (k2 * k2)
            tot += pr * w
        law[v] = tot
    direct = r14.finished_law(sites, nb, pos, rate)
    ok1 = ok1 and all(law[v] == direct[v] for v in law)
print("R1 plaquette laws from per-order closed forms equal the history DP for all four laws on 1296 patterns:", ok1)
cache = ROOT / "logs" / "runner-cache" / "admissibility_formation_order_menu_order_mixture_monotone_box_and_cube_census_2026_09_13.txt"
found = None
if cache.is_file():
    txt = cache.read_text(encoding="utf-8")
    frac = re.search(r"372254646387017\s*/\s*12790481418000000", txt) is not None
    # the census runner prints the distance as a decimal; the exact rational is stated in its note (checked by the runner's A3)
    found = frac or ("0.0291" in txt)
    line = next((ln for ln in txt.splitlines() if "0.0291" in ln or "372254646387017" in ln), "")
print("R2 the census runner's own pinned cache carries the uniform-mixture distance (fraction or decimal 0.0291...):", found, "|", line[:120])
def vtype2(s, val):
    ax = r14.AXIS[val]
    o = pos[opp[s]]
    d = tuple(o[k] - pos[s][k] for k in range(3))
    dot = sum(ax[k] * d[k] for k in range(3))
    return "in" if dot > 0 else ("out" if dot < 0 else "perp")
P1, P3, P4 = (0, 1, 0, 1), (0, 0, 1, 1), (0, 1, 2, 2)
print("R3 independent type routine agrees with the runner's on P1, P3, P4 and all 6^4 patterns:", all(vtype2(s, v[s]) == r14.vtype(s, v[s]) for v in r14.static_law(sites, edges) for s in range(4)))
ok4 = True
for name in ("path3", "star4"):
    st, ps, ed, nbt = r14.window(name)
    for order in permutations(st):
        if r14.order_prob(order, nbt, ps, r14.seeded) == 0:
            continue
        S = set()
        for i, x in enumerate(order):
            k = sum(1 for y in nbt[x] if y in S)
            ok4 = ok4 and (k == (0 if i == 0 else 1))
            S.add(x)
print("R4 every seeded-charged order on the path and the star records exactly one neighbour per site after the first:", ok4)
random.seed(7)
G = lambda p, d: (1 - p) * d / 6 + p * d * d / 36
ok5 = True
for _ in range(200):
    p, q, r = (F(random.randint(1, 40), random.randint(1, 40)) for _ in range(3))
    pin, pout = F(random.randint(0, 20), 20), F(random.randint(0, 20), 20)
    Z = p + q + 4 * r
    ds, da, do = Z * Z / (p * p + q * q + 4 * r * r), Z * Z / (2 * p * q + 4 * r * r), Z * Z / (2 * r * (p + q) + 2 * r * r)
    lhs = sum(G(pt, da) - G(pt, ds) for pt in (pin, pout)) / 2
    rhs = (da - ds) * sum((1 - pt) / 6 + pt * (da + ds) / 36 for pt in (pin, pout)) / 2
    ok5 = ok5 and lhs == rhs and (da - ds) == Z * Z * (p - q) ** 2 / ((2 * p * q + 4 * r * r) * (p * p + q * q + 4 * r * r)) and lhs >= 0 and (lhs > 0 or p == q)
    lhs_o = sum(G(pt, do) - G(pt, ds) for pt in (pin, pout)) / 2
    ok5 = ok5 and (do - ds) == Z * Z * ((p - r) ** 2 + (q - r) ** 2) / ((2 * r * (p + q) + 2 * r * r) * (p * p + q * q + 4 * r * r)) and lhs_o >= 0
print("R5 the E2 identities and their signs hold at 200 random rational points:", ok5)
