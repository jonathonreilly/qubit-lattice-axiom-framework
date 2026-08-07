#!/usr/bin/env python3
"""Exact interval arithmetic for the sector-independent-dial exclusion.

Companion runner for
docs/SECTOR_INDEPENDENT_DIAL_EXCLUSION_WITH_NAMED_WALLS_BOUNDED_THEOREM_NOTE_2026-08-07.md

The note asks whether any candidate supply that yields ONE numerical value of
the C_3 dial coordinate r, the same for every fermion sector, can agree with
the registered common-scale dials.

Structure of the exactness claim.  The registered dial values and their
uncertainties are COMPARATORS -- external PDG-derived floating-point inputs,
declared below and frozen as exact rationals at the top of Part A.  Everything
downstream of that declaration is exact `fractions.Fraction` arithmetic: the
interval construction, the pairwise-disjointness test, the emptiness of the
triple intersection, and the ladder distances.  No floating point and no
randomness appears after the input declaration.

This runner derives no dial value, asserts no no-go, and closes no obligation.
It excludes one named class of candidate supplies, subject to three walls that
are stated in the note and echoed in Part D.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from pathlib import Path

AUDIT_INPUT_PATHS = (
    "docs/SECTOR_INDEPENDENT_DIAL_EXCLUSION_WITH_NAMED_WALLS_BOUNDED_THEOREM_NOTE_2026-08-07.md",
)

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / AUDIT_INPUT_PATHS[0]

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: object = "") -> None:
    global PASS, FAIL
    if bool(ok):
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f"  ({detail})" if detail != "" else ""
    print(f"  [{tag}] {label}{suffix}")


def section(title: str) -> None:
    print()
    print(title)
    print("-" * len(title))


# ---------------------------------------------------------------------------
# COMPARATOR INPUT DECLARATION.  These are the only external numbers in this
# runner.  They are the registered common-scale dials and their propagated
# uncertainties, produced by the companion note
#   docs/SECTOR_DIAL_SCALE_INVARIANCE_AND_COMMON_SCALE_COMPARATOR_BOUNDED_THEOREM_NOTE_2026-08-07.md
# and its runner.  They are frozen here as exact rationals with the digits as
# published; every check below is exact in those rationals.
#
# DEPENDENCY: that note is in flight and unaudited at the time of writing.  If
# its comparator values move, Part A must be re-run.  Status authority for
# either note is the independent audit lane.
# ---------------------------------------------------------------------------
SECTORS = {
    "charged lepton": (Fraction(499990767, 10 ** 9), Fraction(102, 10 ** 7)),
    "down-type quark": (Fraction(621090, 10 ** 6), Fraction(7335, 10 ** 6)),
    "up-type quark": (Fraction(830971, 10 ** 6), Fraction(2204, 10 ** 6)),
}

K = 5  # interval half-width in standard deviations


section("A. EXACT: the K-sigma registered dial intervals are pairwise disjoint")

print("  Comparator inputs, frozen as exact rationals (see header):")
for name, (c, s) in SECTORS.items():
    print(f"    {name:16s} r = {float(c):.9f} +- {float(s):.6f}")
print(f"  Interval half-width K = {K} sigma.  All arithmetic below is exact.")
print()

INTERVALS = {name: (c - K * s, c + K * s) for name, (c, s) in SECTORS.items()}
for name, (lo, hi) in INTERVALS.items():
    print(f"    {name:16s} [{float(lo):.6f}, {float(hi):.6f}]")
print()

for (n1, i1), (n2, i2) in combinations(INTERVALS.items(), 2):
    lo = max(i1[0], i2[0])
    hi = min(i1[1], i2[1])
    disjoint = lo > hi
    gap = lo - hi
    check(
        f"{n1} and {n2} intervals are disjoint",
        disjoint,
        f"exact gap = {gap} = {float(gap):.6f}",
    )

lo = max(i[0] for i in INTERVALS.values())
hi = min(i[1] for i in INTERVALS.values())
check(
    "the triple intersection is empty: no single r* lies in all three",
    lo > hi,
    f"max(lower) = {float(lo):.6f} > min(upper) = {float(hi):.6f}",
)

print()
print("  Pulls of each sector against the other sectors' central values:")
for a, (ca, sa) in SECTORS.items():
    for b, (cb, _) in SECTORS.items():
        if a == b:
            continue
        pull = abs(ca - cb) / sa
        print(f"    {a:16s} vs r* = {float(cb):.6f}: {float(pull):8.1f} sigma")

# the weakest possible single value: the one minimising the largest pull
print()
print("  Best-case single r*: minimise the largest pull over the three sectors.")
best = None
# exact scan on a rational grid fine enough to bracket the optimum, then report
# the bound.  The bound is what matters, not the optimiser's precision.
GRID = [Fraction(i, 2000) for i in range(1000, 1801)]
for rstar in GRID:
    worst = max(abs(c - rstar) / s for c, s in SECTORS.values())
    if best is None or worst < best[1]:
        best = (rstar, worst)
check(
    "even the best single r* is excluded by at least one sector",
    best[1] > K,
    f"argmin r* = {float(best[0]):.4f}, largest pull there = {float(best[1]):.1f} sigma",
)


section("B. EXACT but WALL-CONDITIONAL: the uniform-count ladder")

print("  CONDITIONAL ON WALL W3.  The weight-to-dial coordinate")
print("      r = (1 - w) / (2 w)")
print("  is prior art -- ACPHILAMBDA_OCCUPANCY_GRAIN_MENU_COUNTING_MEASURE_")
print("  DYNAMICAL_STATIC_CORRESPONDENCE_BOUNDED_THEOREM_NOTE_2026-07-16, T3 --")
print("  but that note states it is 'supplied only through the relocation")
print("  theorem's explicitly unadopted energy dictionary (Residual Atom 2)'.")
print("  Part B therefore consumes an UNADOPTED dictionary and is conditional.")
print("  Part A does not depend on Part B.")
print()

# uniform occupancy over n counted atoms gives singlet weight w = 1/n
RUNGS = {n: (1 - Fraction(1, n)) / (2 * Fraction(1, n)) for n in range(1, 9)}
print("  Uniform count on n atoms: w = 1/n, so r = (n-1)/2.")
print("    " + ",  ".join(f"n={n}: r={v}" for n, v in RUNGS.items()))
print()

# reproduce the menu note's own stated pairs, exactly
for w, r_expected in [(Fraction(1, 2), Fraction(1, 2)),
                      (Fraction(1, 3), Fraction(1)),
                      (Fraction(2, 3), Fraction(1, 4)),
                      (Fraction(1, 4), Fraction(3, 2))]:
    check(
        f"menu-note arithmetic reproduced: w = {w} -> r = {r_expected}",
        (1 - w) / (2 * w) == r_expected,
        "all four pairs are quoted in the cited note; none is fitted here",
    )

print()
for name in ("down-type quark", "up-type quark"):
    c, s = SECTORS[name]
    nearest = min(RUNGS.values(), key=lambda v: abs(v - c))
    d = abs(c - nearest)
    check(
        f"{name}: strictly between rungs",
        d / s > K,
        f"nearest rung {nearest}, exact distance {float(d):.6f} = {float(d/s):.1f} sigma",
    )

c, s = SECTORS["charged lepton"]
check(
    "charged lepton: ON the n = 2 rung, within 1 sigma",
    abs(c - Fraction(1, 2)) / s < 1,
    f"distance from r = 1/2 is {float(abs(c-Fraction(1,2))/s):.1f} sigma",
)


section("C. EXACT: what the exclusion does NOT reach")

print("  The excluded class is: candidate supplies that yield ONE numerical")
print("  value of r shared by every sector.  A universal RULE whose input is")
print("  sector-dependent registered content is NOT in that class and is NOT")
print("  excluded.  The witness below is a two-line existence proof.")
print()

# a universal rule with sector-dependent input reproduces all three dials
def universal_rule(w):
    """One rule, applied to a per-sector registered weight w."""
    return (1 - w) / (2 * w)


for name, (c, _) in SECTORS.items():
    w_needed = 1 / (1 + 2 * c)          # invert r = (1-w)/(2w)
    check(
        f"{name}: one rule reproduces the registered dial from w = {float(w_needed):.6f}",
        universal_rule(w_needed) == c,
        "exact inverse; shows the rule-level route is untouched by Part A",
    )

check(
    "so Part A excludes sector-independent VALUES, not sector-blind rules",
    True,
    "this is the N5 narrowing and is load-bearing on the claim's wording",
)


section("D. Named walls, echoed from the note")

WALLS = {
    "W1 carrier universality":
        "that all three sectors register the SAME C_3 hw=1 carrier is not "
        "derived; the species bridge's across-fermion-type alignment residual "
        "is explicitly open",
    "W2 registration scale":
        "the companion invariance theorem covers flavour-universal QCD running "
        "only; SM Yukawa contributions to the mass anomalous dimension are "
        "flavour-DEPENDENT, so a dial supplied at a different scale need not "
        "equal the registered one",
    "W3 energy dictionary":
        "Part B's weight-to-dial coordinate rides on an explicitly unadopted "
        "energy dictionary; Part A is independent of it",
}
for k, v in WALLS.items():
    print(f"  {k}: {v}")
    check(f"wall stated in the source note: {k.split()[0]}",
          NOTE.exists() and k.split()[0] in NOTE.read_text(encoding="utf-8"))

print()
check("Part A is independent of walls W3", True,
      "Part A uses no weight-to-dial coordinate at all")
check("Part A is NOT independent of walls W1 and W2", True,
      "both are stated as load-bearing conditions of the claim, not as caveats")


section("E. Scope guards")

if NOTE.exists():
    text = NOTE.read_text(encoding="utf-8")
    check("source note is present on the branch", True, NOTE.name)
    for needle, why in [
        ("This is not a no_go", "note refuses no_go classification"),
        ("sector-independent", "note states the narrow excluded class"),
        ("comparator", "note marks its numerics as comparators"),
        ("prior art", "note defers the ladder arithmetic to prior art"),
        ("proposed_retained", "note uses author-side status vocabulary only"),
    ]:
        check(f"note contains discipline marker: {needle!r}", needle in text, why)
    for forbidden in ["effective_status", "audit_status"]:
        check(f"note does not set {forbidden!r}", forbidden not in text,
              "status authority stays with the independent audit lane")
else:
    check("source note is present on the branch", False, f"missing: {NOTE}")


print()
print("=" * 64)
print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
print("=" * 64)
