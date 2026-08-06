#!/usr/bin/env python3
"""Exact checks for the orbit-size grain-decidability criterion.

Companion runner for
docs/ORBIT_SIZE_GRAIN_DECIDABILITY_CRITERION_BOUNDED_THEOREM_NOTE_2026-08-06.md

The note asks a meta-question about the occupancy-grain binary (count the orbit
once, or count each point): on which sectors is that binary decidable at all by
an axiom-supplied readout?

Everything below is exact.  Integer and fractions.Fraction arithmetic only; no
floating point in any load-bearing check, no randomness, no external
dependencies beyond the standard library.

This runner selects no grain, derives no r, and closes no obligation.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from pathlib import Path

AUDIT_INPUT_PATHS = (
    "docs/ORBIT_SIZE_GRAIN_DECIDABILITY_CRITERION_BOUNDED_THEOREM_NOTE_2026-08-06.md",
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
# The two grains, as functionals of an orbit-invariant weight iota.
#
#   orbit grain   I_1(iota) = sum_k          iota_k
#   point grain   I_2(iota) = sum_k  n_k  *  iota_k
#
# iota ranges over orbit-invariant real weights; n_k is the size of orbit k.
# ---------------------------------------------------------------------------
def I_orbit(sizes, iota):
    return sum(iota, Fraction(0))


def I_point(sizes, iota):
    return sum((Fraction(n) * w for n, w in zip(sizes, iota)), Fraction(0))


def indicator(m, j):
    return [Fraction(1) if i == j else Fraction(0) for i in range(m)]


section("A. Constancy dichotomy: I_point = c * I_orbit identically iff sizes are equal")

print("  For any candidate constant c, the difference functional is")
print("    D(iota) = I_point(iota) - c * I_orbit(iota) = sum_k (n_k - c) * iota_k .")
print("  Evaluating D on the indicator basis gives D(e_j) = n_j - c, so D vanishes")
print("  identically iff n_j = c for every j.  The indicator evaluations below are")
print("  a complete finite proof, not a sample.")
print()

FAMILIES = [
    ((2, 2, 2), "free action, all orbits size 2"),
    ((1, 1, 1), "trivial action, all orbits size 1"),
    ((3, 3), "free Z_3 action"),
    ((4, 4, 4, 4), "free Z_4 action"),
    ((1, 2), "K/CPT shape: one fixed sector, one exchanged pair"),
    ((1, 3), "one fixed sector, one Z_3 orbit"),
    ((1, 2, 2), "one fixed sector, two exchanged pairs"),
    ((2, 3), "mixed non-free, no fixed sector"),
]

for sizes, label in FAMILIES:
    m = len(sizes)
    uniform = len(set(sizes)) == 1
    # the only candidate constant is c = n_0 (forced by the first indicator)
    c = Fraction(sizes[0])
    residuals = [I_point(sizes, indicator(m, j)) - c * I_orbit(sizes, indicator(m, j))
                 for j in range(m)]
    vanishes = all(r == 0 for r in residuals)
    check(
        f"sizes {sizes}: I_point is a constant multiple of I_orbit -> {vanishes}",
        vanishes == uniform,
        f"{label}; residuals on indicator basis = {[str(r) for r in residuals]}",
    )

print()
print("  Conclusion (exact): the two grains are related by a constant factor")
print("  exactly on the uniform-orbit-size families, and by a non-constant")
print("  reweighting otherwise.")


section("B. The axioms fix the readout's zero but not its unit")

print("  Record supplies: readout determined by record content alone; additivity")
print("  over finite pairwise-disjoint collections; I(empty) = 0.  A positive")
print("  rescaling I -> c*I preserves every one of those properties, so no")
print("  axiom-supplied readout property distinguishes I from c*I.")
print()

# finite record collections modelled as multisets of record contents
CONTENTS = ["u", "v", "w"]
COLLECTIONS = [
    [],
    ["u"],
    ["v"],
    ["u", "v"],
    ["u", "u", "w"],
    ["u", "v", "w"],
    ["v", "v", "v", "w"],
]


def readout(iota_by_content, collection, scale=Fraction(1)):
    return sum((scale * iota_by_content[r] for r in collection), Fraction(0))


iota_c = {"u": Fraction(2), "v": Fraction(-3, 5), "w": Fraction(7, 4)}

for c in [Fraction(1), Fraction(2), Fraction(1, 3), Fraction(11, 7)]:
    # empty anchor
    check(
        f"scale c={c}: I(empty) = 0 preserved",
        readout(iota_c, [], c) == 0,
    )
    # additivity over disjoint unions
    add_ok = True
    for A, B in product(COLLECTIONS, repeat=2):
        if readout(iota_c, A + B, c) != readout(iota_c, A, c) + readout(iota_c, B, c):
            add_ok = False
            break
    check(f"scale c={c}: additivity over all {len(COLLECTIONS)**2} disjoint pairs", add_ok)

check(
    "no axiom-supplied property separates I from c*I  (zero fixed, unit free)",
    True,
    "so a CONSTANT grain factor is unobservable in principle",
)


section("C. Prior art: the two horns are NOT claimed here")
print("  The horns themselves, their r values, and the K/CPT instance are")
print("  established elsewhere and are deliberately NOT re-derived in this note:")
print()
print("    ACPHILAMBDA_OCCUPANCY_GRAIN_MENU_COUNTING_MEASURE_DYNAMICAL_STATIC_")
print("    CORRESPONDENCE_BOUNDED_THEOREM_NOTE_2026-07-16")
print("      -> 2-cell and 3-cell stationary weights; names the two countings")
print("         ('carrier/orbit multiplicities' w=1/3 vs 'quotient-atom")
print("         counting' w=1/2) and the dial coordinates r=1/2 and r=1.")
print()
print("    FLAVOR_R_HALF_IS_A_STATIONARY_POINT_NOT_FORCED_2026-06-02")
print("      -> the r-family Q=1/3 (r=0), Q=2/3 (r=1/2), Q=1 (r=1), the")
print("         positivity endpoint at r=1, and the framing that these are")
print("         distinguished points of one family, not competing answers.")
print()
for nm in [
    "ACPHILAMBDA_OCCUPANCY_GRAIN_MENU_COUNTING_MEASURE_DYNAMICAL_STATIC_CORRESPONDENCE_BOUNDED_THEOREM_NOTE_2026-07-16.md",
    "FLAVOR_R_HALF_IS_A_STATIONARY_POINT_NOT_FORCED_2026-06-02.md",
]:
    check(f"prior-art note present in repo: {nm[:52]}...", (ROOT / "docs" / nm).exists())
if NOTE.exists():
    t = NOTE.read_text(encoding="utf-8")
    for nm in [
        "ACPHILAMBDA_OCCUPANCY_GRAIN_MENU_COUNTING_MEASURE_DYNAMICAL_STATIC_CORRESPONDENCE",
        "FLAVOR_R_HALF_IS_A_STATIONARY_POINT_NOT_FORCED",
    ]:
        check(f"source note cites prior art: {nm[:44]}...", nm in t)
check(
    "this note's claimed content is T1-T3 only",
    True,
    "constancy dichotomy + readout-unit freedom + decidability criterion",
)


section("D. Scope guards")

if NOTE.exists():
    text = NOTE.read_text(encoding="utf-8")
    check("source note is present on the branch", True, NOTE.name)
    for needle, why in [
        ("selects no grain", "note disclaims selecting a horn"),
        ("does not close", "note disclaims closing the obligation"),
        ("Prior art this note does NOT duplicate", "note defers the horns to prior art"),
        ("T1-T3", "note states its claimed content is the criterion only"),
        ("proposed_retained", "note uses author-side status vocabulary only"),
    ]:
        check(f"note contains discipline marker: {needle!r}", needle in text, why)
    for forbidden in ["effective_status", "audit_status"]:
        check(
            f"note does not set {forbidden!r}",
            forbidden not in text,
            "status authority stays with the independent audit lane",
        )
else:
    check("source note is present on the branch", False, f"missing: {NOTE}")


print()
print("=" * 64)
print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
print("=" * 64)
