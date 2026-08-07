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
It excludes one named class of candidate supplies, subject to FOUR walls that
are stated in the note and echoed in Part D.

Novelty boundary.  The qualitative content of Part A -- that one universal value
of r cannot reproduce the distinct sector dials -- is PRIOR ART in this repo
(FOURTH_AXIOM_RG_SCALE_DYNAMICS_SCOPING_2026-06-05, section 2.1, which already
computes a best single universal value and reports that it misses a sector).
What is new here is only the quantification: exact 5-sigma interval arithmetic,
an exact minimax, and the common-scale comparators.  See the note's "Prior art"
section.
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

# the weakest possible single value: the one minimising the largest pull.
#
# EXACT MINIMAX, not a grid scan.  P(r) = max_i |c_i - r| / s_i is a maximum of
# V-shaped piecewise-linear functions, hence convex and piecewise linear, so its
# minimum is attained at a breakpoint of the upper envelope.  Every breakpoint is
# a crossing of a rising branch of one sector with a falling branch of another:
#     (r - c_i)/s_i = (c_j - r)/s_j   =>   r = (s_i*c_j + s_j*c_i)/(s_i + s_j).
# Enumerating all such crossings and taking the least value of P is therefore the
# exact minimax, not an upper bound on it.  (A grid scan would only ever give an
# UPPER bound, which is the wrong direction for an exclusion claim.)
print()
print("  Best-case single r*: minimise the largest pull over the three sectors.")
print("  Exact minimax over all real r* (envelope-breakpoint enumeration).")
best = None
for (ca, sa), (cb, sb) in combinations(SECTORS.values(), 2):
    rstar = (sa * cb + sb * ca) / (sa + sb)
    worst = max(abs(c - rstar) / s for c, s in SECTORS.values())
    if best is None or worst < best[1]:
        best = (rstar, worst)
check(
    "even the best single r* is excluded by at least one sector",
    best[1] > K,
    f"exact argmin r* = {float(best[0]):.7f}, largest pull there = "
    f"{float(best[1]):.4f} sigma",
)
check(
    "the exclusion does not depend on the choice of K",
    best[1] > K,
    f"T1 holds for every K < {float(best[1]):.4f}; K = {K} is far inside that range",
)

# ---------------------------------------------------------------------------
# ROBUSTNESS: the input uncertainties are SYMMETRIC Gaussian linear propagations
# of PDG inputs, several of which (m_u, m_d, m_s) have strongly ASYMMETRIC
# published errors.  Symmetrising is only safe if the conclusion has margin
# against inflating sigma.  These checks report the exact factor by which the
# quoted sigmas would have to grow before T1 fails, so a reader can compare that
# factor against the published asymmetry directly instead of trusting the
# symmetrisation.
# ---------------------------------------------------------------------------
print()
print("  Robustness of T1 to inflated (e.g. asymmetric-error) uncertainties:")
for (n1, (c1, s1)), (n2, (c2, s2)) in combinations(SECTORS.items(), 2):
    factor = abs(c1 - c2) / (K * (s1 + s2))
    check(
        f"{n1} / {n2} stay disjoint under uniform sigma inflation up to x{float(factor):.2f}",
        factor > 1,
        f"exact break-even inflation factor = {float(factor):.3f}",
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

# same asymmetric-error robustness question as Part A, for the ladder distances
print()
print("  Robustness of the 'strictly between rungs' finding to inflated sigma:")
for name in ("down-type quark", "up-type quark"):
    c, s = SECTORS[name]
    nearest = min(RUNGS.values(), key=lambda v: abs(v - c))
    factor = abs(c - nearest) / (K * s)
    check(
        f"{name} stays off-rung under sigma inflation up to x{float(factor):.2f}",
        factor > 1,
        f"exact break-even inflation factor = {float(factor):.3f}",
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

# The existence proof is only meaningful if the one rule genuinely needs THREE
# DIFFERENT inputs; if the three required weights coincided, the "rule" would be
# a disguised sector-independent value and Part A would exclude it after all.
w_required = [1 / (1 + 2 * c) for c, _ in SECTORS.values()]
check(
    "the surviving rule-level route needs three DISTINCT sector inputs",
    len(set(w_required)) == 3,
    "so it is genuinely outside the class Part A excludes, not a disguised "
    "single value; this is the N5 narrowing and is load-bearing on the wording",
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
    "W3 energy dictionary (Part B only)":
        "Part B's weight-to-dial coordinate rides on an explicitly unadopted "
        "energy dictionary; Part A is independent of THIS dictionary",
    "W4 mass-to-dial dictionary (Part A too)":
        "the comparators are not measured r; they are computed from PDG masses "
        "through the C_3-circulant (Brannen) ansatz and the sqrt(m) one-leg "
        "amplitude identification, which the quark circulant source-law "
        "boundary note records as NON-RETAINED inputs.  Part A escapes W3 but "
        "rides W4, which is a dictionary of the same kind",
}
for k, v in WALLS.items():
    print(f"  {k}: {v}")
    check(f"wall stated in the source note: {k.split()[0]}",
          NOTE.exists() and k.split()[0] in NOTE.read_text(encoding="utf-8"))

print()
print("  Part A is independent of W3 (it uses no weight-to-dial coordinate at")
print("  all), but is NOT independent of W1, W2 or W4.  All three are stated in")
print("  the note as load-bearing conditions of the claim, not as caveats.")
print("  'T1 survives if T2 falls' therefore means only that T1 escapes W3 --")
print("  it does NOT mean T1 is free of dictionary dependence.")


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
        ("FOURTH_AXIOM_RG_SCALE_DYNAMICS_SCOPING_2026-06-05",
         "note credits the prior art that already states Part A qualitatively"),
        ("W4", "note names the mass-to-dial dictionary wall that Part A rides"),
        ("does not resolve on this branch",
         "note is explicit that its comparator source is not present yet"),
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
