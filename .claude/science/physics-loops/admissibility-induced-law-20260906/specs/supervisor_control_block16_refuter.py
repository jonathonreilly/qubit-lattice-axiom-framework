"""Refuting pass, block 16 (supervisor seat, disjoint machinery from the runner's checks):
(R1) the flip comparison from the full sequential laws (mu_sigma(v^z)/prod K(v^z) against mu_sigma(v)/prod K(v)) instead of the
     weight formula, on every order of the plaquette and 2x3 and every class of the cube;
(R2) the qualifying orders of the path and the star by a direct search for a site with two recorded neighbours at formation time,
     against the runner's bad_union;
(R3) the 2x3 uniform mixture's distance from the census runner's own pinned cache (decimal) against the runner's exact value;
(R4) X3's environment claim on the domino by hand: the second site records the first plus five outside sites, so its normalizer
     K_6 depends on the first site's value — evaluated exactly at (3,1,2) for the two flips.
Run from the pack: the runner is imported from the repository's scripts/ directory."""
import importlib
import sys
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
r16 = importlib.import_module("admissibility_rule_static_law_not_a_mixture_of_formation_laws_flip_monotonicity_2026_09_15")
M = 6
ok1 = True
for name in ("plaquette", "2x3", "cube"):
    sites, edges, nb = r16.window(r16.WINDOWS[name])
    n = len(sites)
    seen = set()
    for order in permutations(sites):
        key = r16.multiset_key(order, nb)
        if key in seen:
            continue
        seen.add(key)
        v = tuple([0] * n)
        # ratio mu_sigma / prod K at v and at the flips, from the product of conditionals directly (single-pattern evaluation)
        def ratio(pat):
            S = set(); pr = F(1)
            for x in order:
                rec = tuple(sorted(pat[y] for y in nb[x] if y in S))
                pr *= r16.cond(rec, pat[x]); S.add(x)
            pk = F(1)
            for (i, j) in edges:
                pk *= F(r16.PHI[pat[i]][pat[j]], r16.Z1)
            return pr / pk
        r0 = ratio(v)
        bad = r16.bad_union(order, nb)
        for z in sites:
            v2 = list(v); v2[z] = 1
            r1 = ratio(tuple(v2))
            ok1 = ok1 and r1 >= r0 and ((r1 > r0) == (z in bad))
print("R1 flip comparison from the full sequential laws agrees with the weight formula on every class of the plaquette, 2x3 and the cube:", ok1)
ok2 = True
for name in ("path3", "star4"):
    sites, edges, nb = r16.window(r16.WINDOWS[name])
    for order in permutations(sites):
        S = set(); has_two = False
        for x in order:
            if sum(1 for y in nb[x] if y in S) >= 2:
                has_two = True
            S.add(x)
        ok2 = ok2 and (has_two == bool(r16.bad_union(order, nb)))
print("R2 direct search for a site with two recorded neighbours agrees with the runner's qualifying-order test on the path and the star:", ok2)
cache = ROOT / "logs" / "runner-cache" / "admissibility_formation_order_menu_order_mixture_monotone_box_and_cube_census_2026_09_13.txt"
txt = cache.read_text(encoding="utf-8") if cache.is_file() else ""
line = next((ln for ln in txt.splitlines() if "TV(mix,static) (3, 1, 2)" in ln), "")
exact = F(372254646387017, 12790481418000000)
dec12 = exact.numerator * 10 ** 12 // exact.denominator
print("R3 the census runner's cache line:", line.strip()[:80], "| exact value to 12 digits: 0." + str(dec12).zfill(12), "| match:", ("0." + str(dec12).zfill(12)) in line)
U, O = r16.make_unit([(0, 0, 0), (1, 0, 0)])
vO = {y: 0 for y in O}
others = tuple(sorted([0] * 5))
k6_same = r16.Kk(tuple(sorted(others + (0,))))
k6_anti = r16.Kk(tuple(sorted(others + (1,))))
print("R4 domino in the all-+x environment: the second site's normalizer K_6(first, five outside +x) at first = +x vs -x:", k6_same, k6_anti, "differ:", k6_same != k6_anti)
