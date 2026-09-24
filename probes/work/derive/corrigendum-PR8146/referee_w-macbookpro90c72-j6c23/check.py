"""Independent confirmation of corrigendum PR8146, attempt 2.

Re-derives the 2:1 majority condition and the failure band from the pair weights,
then reads block 12's pack file at the named commit. The author's script is not called.
"""
import itertools
import subprocess
import sys
from fractions import Fraction as F

import sympy as sp

FAILS = []


def want(label, ok):
    if not ok:
        FAILS.append(label)
    print(("PASS " if ok else "FAIL ") + label, flush=True)


p, q, r = sp.symbols("p q r", positive=True)
anti = {"v": p ** 2 * q, "-v": q ** 2 * p, "other": r ** 3}
orth = {"v": p ** 2 * r, "w": r ** 2 * p, "-v": q ** 2 * r, "-w": r ** 2 * q, "other": r ** 3}
ok = sp.factor(anti["v"] - anti["-v"]) == p * q * (p - q)
ok = ok and sp.factor(anti["v"] - anti["other"]) == p ** 2 * q - r ** 3
margins = {
    "w": sp.factor(orth["v"] - orth["w"]),
    "-v": sp.factor(orth["v"] - orth["-v"]),
    "-w": sp.factor(orth["v"] - orth["-w"]),
    "other": sp.factor(orth["v"] - orth["other"]),
}
ok = ok and margins["w"] == p * r * (p - r)
ok = ok and margins["-v"] == r * (p - q) * (p + q)
ok = ok and margins["-w"] == r * (p ** 2 - q * r)
ok = ok and margins["other"] == r * (p - r) * (p + r)
# sqrt(r^3/q) - r = r (sqrt(r/q) - 1), so the square root exceeds r exactly when r exceeds q
ok = ok and sp.simplify(sp.sqrt(r ** 3 / q) - r - r * (sp.sqrt(r / q) - 1)) == 0
want("U1 the eight 2:1 margins factor as stated, and sqrt(r^3/q) exceeds r exactly when r exceeds q", ok)


def unique_majority(pv, qv, rv):
    """True iff v is the unique heaviest output for both the antipodal pattern and an orthogonal one."""
    anti_w = {"v": pv * pv * qv, "-v": qv * qv * pv, "other": rv * rv * rv}
    orth_w = {
        "v": pv * pv * rv,
        "w": rv * rv * pv,
        "-v": qv * qv * rv,
        "-w": rv * rv * qv,
        "other": rv * rv * rv,
    }
    def wins(weights):
        top = max(weights.values())
        return weights["v"] == top and sum(val == top for val in weights.values()) == 1
    return wins(anti_w) and wins(orth_w)


def corrected(pv, qv, rv):
    return pv > qv and pv * pv * qv > rv * rv * rv


grid = []
for pv, qv, rv in itertools.product((F(1, 2), F(1), F(3, 2), F(2), F(5, 2), F(3), F(4), F(5)), repeat=3):
    if pv > 0 and qv > 0 and rv > 0:
        grid.append((pv, qv, rv))
ok = all(unique_majority(*t) == corrected(*t) for t in grid)
want(f"U1 on {len(grid)} positive rational triples, both patterns have a unique majority at v exactly under p > max(q, sqrt(r^3/q))", ok)

# the band is where the old condition holds and the new one fails
def old(pv, qv, rv):
    return pv > qv and pv > rv


def in_band(pv, qv, rv):
    return qv < rv < pv and pv * pv * qv <= rv * rv * rv


ok = all((old(*t) and not corrected(*t)) == in_band(*t) for t in grid)
# nonempty iff q < r: the upper end sqrt(r^3/q) exceeds r iff r > q, already the identity above
ok = ok and any(in_band(*t) for t in grid) and not any(in_band(pv, qv, rv) for pv, qv, rv in grid if qv >= rv)
want("U2 the old condition fails exactly on q < r < p <= sqrt(r^3/q), and that set is empty when q >= r", ok)

# campaign line (p, 1, 2): 2 < p <= sqrt(8) = 2 sqrt(2)
ok = sp.simplify(sp.sqrt(8) - 2 * sp.sqrt(2)) == 0
points = {
    (F(5), F(2), F(4)): True,
    (F(5, 2), F(1), F(2)): True,
    (F(3), F(1), F(2)): False,
    (F(5), F(2), F(3)): False,
}
ok = ok and all(in_band(*t) == flag for t, flag in points.items())
# documented weights at (5,2,4)
ok = ok and F(5) ** 2 * F(2) == 50 and F(2) ** 2 * F(5) == 20 and F(4) ** 3 == 64 and 64 > 50
ok = ok and not unique_majority(F(5, 2), F(1), F(2))
want("U3 (5,2,4) and (5/2,1,2) are in the band and the majority loses; (3,1,2) and (5,2,3) are outside", ok)

# the pack file
SHA = "3acd27d2fca8"
BRANCH = "physics-loop/admissibility-induced-law-block12-strong-coupling-phase-20260915"
PATH = ".claude/science/physics-loops/admissibility-induced-law-20260906/ASSUMPTIONS_AND_IMPORTS.md"
have = subprocess.run(["git", "cat-file", "-e", SHA + "^{commit}"], capture_output=True).returncode == 0
if not have:
    subprocess.run(["git", "fetch", "--quiet", "origin", BRANCH], capture_output=True)
body = subprocess.run(["git", "show", f"{SHA}:{PATH}"], capture_output=True, text=True).stdout
lines = body.split("\n")
cf = [i for i, line in enumerate(lines, 1) if "Counterfactual pass" in line]
block12 = [i for i in cf if "most likely output" in lines[i - 1]]
text = lines[block12[0] - 1] if block12 else ""
norm = text.replace("≥", ">=").replace("≤", "<=")
ok = bool(body) and len(cf) == 6 and block12 == [78]
ok = ok and "q >= p" in norm and "r >= p" in norm
# (5,2,4) fails the selector: not (q>=p or r>=p), but the majority is not unique
ok = ok and not (F(2) >= F(5) or F(4) >= F(5)) and not unique_majority(F(5), F(2), F(4))
want("U4 block 12's pack line 78 selects counterfactual menus by q >= p or r >= p, which misses the band", ok)

print(f"TOTAL FAIL={len(FAILS)}")
if FAILS:
    print("SUMMARY: fails at " + FAILS[0])
    sys.exit(1)
print(
    "HIT: confirmed - the 2:1 majority is the unique mode iff p > max(q, sqrt(r^3/q)), "
    "which is stricter than p > max(q, r) exactly on q < r < p <= sqrt(r^3/q). "
    "Block 12's counterfactual pass selects menus by the negation of the old condition, so it never enters that band, including (5,2,4)."
)
print(
    "SUMMARY: confirmed the corrected threshold and the missed pack line. "
    "On (p,1,2) the band is 2 < p <= 2 sqrt(2). "
    "At (5,2,4) the antipodal weights are 50, 20 and 64, so another value wins, "
    "while q >= p or r >= p is false."
)
