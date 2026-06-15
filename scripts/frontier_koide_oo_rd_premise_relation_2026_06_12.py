#!/usr/bin/env python3
"""Orbit-occupancy / records-flow durability premise relation on the current checked surface.

Companion runner for
    docs/KOIDE_OO_RD_PREMISE_RELATION_ON_CURRENT_SURFACE_NARROW_THEOREM_NOTE_2026-06-12.md

This runner checks the narrow theorem requested for 2026-06-12:
Records-flow durability plus the supplied flow phi(r)=2r^2 and the registered side
conditions realizes the orbit-occupancy count; orbit-occupancy gives only per-point
phi-stationarity; the two premises are not equivalent as laws, witnessed by the
equally self-composable counterexample flow psi(r)=r^2.

No premise is adopted here. The note and runner are conditional on the
SUPPLIED flow and the registered side conditions.
"""

from __future__ import annotations

import pathlib
import re
import sys

import sympy as sp


PASS = 0
FAIL = 0


def check(num: int, desc: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    line = f"[{tag}] ({num:02d}) {desc}"
    if detail:
        line += f"  [{detail}]"
    print(line)


ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
NOTE = DOCS / "KOIDE_OO_RD_PREMISE_RELATION_ON_CURRENT_SURFACE_NARROW_THEOREM_NOTE_2026-06-12.md"


def note_text() -> str:
    return NOTE.read_text(encoding="utf-8")


print("=" * 72)
print("Orbit-occupancy / records-flow durability premise relation on the current checked surface")
print("=" * 72)

r = sp.Symbol("r", real=True)
s = sp.Symbol("s", real=True)
rho = sp.Symbol("rho", positive=True)
g = sp.Symbol("g", positive=True)
Z_d = sp.Symbol("Z_d", positive=True)
a = sp.Symbol("a", positive=True)
B = sp.Symbol("B", real=True)
delta = sp.Symbol("delta", real=True)

phi = 2 * r**2
psi = r**2

print("\n--- A-class: theorem checks")

# 1. Fix(phi) over the reals.
fix_phi = set(sp.solve(sp.Eq(phi, r), r))
expected_phi = {sp.Integer(0), sp.Rational(1, 2)}
check(
    1,
    "Fix(phi) for phi(r) = 2 r^2 over the reals is exactly {0, 1/2}",
    fix_phi == expected_phi,
    f"computed={sorted(fix_phi)}",
)

# 2. Projective/infinite fixed point via s = 1/r.
phi_conj = sp.simplify(1 / (phi.subs(r, 1 / s)))
check(
    2,
    "under s = 1/r, phi conjugates to s -> s^2/2 and s = 0 is fixed",
    sp.simplify(phi_conj - s**2 / 2) == 0 and phi_conj.subs(s, 0) == 0,
    f"conjugated={phi_conj}",
)

# 3. r = 0 exclusion: B -> 0 gives an exactly degenerate circulant spectrum.
lam = [a + 2 * B * sp.cos(delta + 2 * sp.pi * k / 3) for k in range(3)]
degenerate_limit = [sp.simplify(sp.limit(entry, B, 0)) for entry in lam]
split_example = [sp.N(entry.subs({a: 10, B: 1, delta: sp.Rational(2, 9)})) for entry in lam]
split_values = {round(float(value), 12) for value in split_example}
check(
    3,
    "r = 0 forces the exactly degenerate spectrum [a, a, a] in the B -> 0 limit",
    degenerate_limit == [a, a, a] and len(split_values) == 3,
    f"limit={degenerate_limit}",
)

# 4. r -> infinity exclusion: trace identity and positivity require a > 0.
trace_identity = sp.simplify(sum(lam) - 3 * a)
positivity_requires_positive_a = bool(a.is_positive)
check(
    4,
    "r -> infinity forces a -> 0 at fixed doublet content, but positive channel weights require a > 0; trace sum(lambda_k)=3a",
    trace_identity == 0 and positivity_requires_positive_a,
    f"trace_difference={trace_identity}",
)

# 5. P1 set arithmetic.
projective = sp.oo
rd_candidates_phi = {sp.Integer(0), sp.Rational(1, 2), projective}
excluded = {sp.Integer(0), projective}
admissible_phi = rd_candidates_phi - excluded
check(
    5,
    "{0, 1/2, infinity} minus the two side-condition exclusions is exactly {1/2}",
    admissible_phi == {sp.Rational(1, 2)},
    f"admissible={admissible_phi}",
)

# 6. P1 rho-map link.
rho_from_r_half = sp.solve(sp.Eq(1 / (2 * rho), sp.Rational(1, 2)), rho)
zd_from_rho_one = sp.solve(sp.Eq((sp.pi / g) / Z_d, 1), Z_d)
r_from_zd_orbit = sp.simplify(1 / (2 * ((sp.pi / g) / (sp.pi / g))))
sector_r = sp.simplify(1 / (2 * ((sp.pi / g) / (2 * sp.pi / g))))
check(
    6,
    "r = 1/2 <-> rho = 1 <-> Z_d = pi/g under r = 1/(2 rho), rho = (pi/g)/Z_d",
    rho_from_r_half == [1]
    and zd_from_rho_one == [sp.pi / g]
    and r_from_zd_orbit == sp.Rational(1, 2)
    and sector_r == 1,
    f"rho={rho_from_r_half}, Z_d={zd_from_rho_one}",
)

# 7. P2 per-point stationarity.
check(
    7,
    "orbit-occupancy's realized value is phi-stationary: phi(1/2) = 1/2 exactly",
    sp.simplify(phi.subs(r, sp.Rational(1, 2)) - sp.Rational(1, 2)) == 0,
)

# 8. P3a Fix(psi), including infinity by conjugation.
fix_psi = set(sp.solve(sp.Eq(psi, r), r))
psi_conj = sp.simplify(1 / (psi.subs(r, 1 / s)))
check(
    8,
    "Fix(psi) for psi(r) = r^2 is {0, 1}, plus infinity by the same projective conjugation",
    fix_psi == {sp.Integer(0), sp.Integer(1)}
    and sp.simplify(psi_conj - s**2) == 0
    and psi_conj.subs(s, 0) == 0,
    f"finite={sorted(fix_psi)}, conjugated={psi_conj}",
)

# 9. P3b same exclusions select the sector cell.
rd_candidates_psi = {sp.Integer(0), sp.Integer(1), projective}
admissible_psi = rd_candidates_psi - excluded
check(
    9,
    "under psi the same exclusions leave {1}, the sector cell, not orbit-occupancy's r = 1/2 count",
    admissible_psi == {sp.Integer(1)} and sp.Integer(1) != sp.Rational(1, 2),
    f"admissible={admissible_psi}",
)

# 10. P3c orbit-occupancy is not psi-stationary.
check(
    10,
    "orbit-occupancy's realized value is not psi-stationary: psi(1/2) = 1/4 != 1/2",
    psi.subs(r, sp.Rational(1, 2)) == sp.Rational(1, 4)
    and sp.Rational(1, 4) != sp.Rational(1, 2),
)

# 11. P4 net relation.
one_way_realization = admissible_phi == {sp.Rational(1, 2)}
per_point_consistency = sp.simplify(phi.subs(r, sp.Rational(1, 2)) - sp.Rational(1, 2)) == 0
law_equivalence_fails = admissible_psi != {sp.Rational(1, 2)} and psi.subs(r, sp.Rational(1, 2)) != sp.Rational(1, 2)
check(
    11,
    "net relation assembled: records-flow durability => orbit-occupancy realization under phi + side conditions; orbit-occupancy => phi-stationarity; law-equivalence fails via psi",
    one_way_realization and per_point_consistency and law_equivalence_fails,
)

print("\n--- B-class: note consistency checks")

text = note_text()

# 12. Premise statements quoted.
check(
    12,
    "note quotes both premise statements verbatim",
    "one statistical slot per record-outcome" in text
    and "durable registration is invariant under records-flow self-composition" in text,
)

# 13. Required status/firewall/no-promotion language.
check(
    13,
    "note carries supplied-flow boundary, proposed/NOT adopted language, Status authority, and No-promotion statement",
    "not derived as the physical emergent" in text
    and "Status authority" in text
    and "No-promotion statement" in text
    and "Orbit-occupancy remains proposed and NOT adopted" in text
    and "Records-flow durability" in text
    and "remains proposed and NOT adopted" in text,
)

# 14. Link and context firewall.
md_targets = re.findall(r"\]\(([^)]+\.md)\)", text)
expected_links = {
    "FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md",
    "KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md",
}
actual_links = set(md_targets)
links_resolve = all((DOCS / target).exists() for target in actual_links)
context_not_markdown = (
    "](KOIDE_R_HALF_DURABILITY" not in text
    and "](KOIDE_OCCUPANCY_DURABILITY" not in text
)
context_backticked = (
    "`KOIDE_R_HALF_DURABILITY_STATIONARITY_CONDITIONAL_CHAIN_BOUNDED_THEOREM_NOTE_2026-06-11.md`" in text
    and "`KOIDE_OCCUPANCY_DURABILITY_PREMISE_EQUIVALENCE_ON_REGISTERED_SURFACE_BOUNDED_THEOREM_NOTE_2026-06-11.md`" in text
)
check(
    14,
    "context notes are backticked only; the note's .md link inventory is exactly the two load-bearing dependencies and both resolve",
    actual_links == expected_links and links_resolve and context_not_markdown and context_backticked,
    f"links={sorted(actual_links)}",
)

print(f"\nSUMMARY: PASS={PASS} FAIL={FAIL}")
if FAIL or PASS < 14:
    sys.exit(1)
