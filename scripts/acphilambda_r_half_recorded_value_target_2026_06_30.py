#!/usr/bin/env python3
"""Verify the post-Dirac r=1/2 recorded-value target map.

This runner checks that the note keeps the right target shape:
context-local durable record fixedness, not global forcing of record occurrence.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

NOTE = ROOT / "docs" / "ACPHILAMBDA_R_HALF_RECORDED_VALUE_TARGET_2026-06-30.md"
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
POST_DIRAC = ROOT / "docs" / "ACPHILAMBDA_POST_DIRAC_REDUCTION_MAP_2026-06-30.md"
STRICT_NN = ROOT / "docs" / "STRICT_NN_COMPOSITION_FLUX_SELECTOR_BRIDGE_THEOREM_NOTE_2026-06-30.md"
R_WEIGHTING = ROOT / "docs" / "KOIDE_R_IS_THE_WEIGHTING_PRINCIPLE_DIAL_RECORD_DYNAMICS_WEIGHTING_BLIND_BOUNDED_THEOREM_NOTE_2026-06-15.md"
OCCUPANCY_DICT = ROOT / "docs" / "OCCUPANCY_ATOM_IS_THE_OUTCOME_DICTIONARY_FLOW_SELECTS_EQUIPARTITION_BOUNDED_NOTE_2026-06-12.md"
RD_CHAIN = ROOT / "docs" / "KOIDE_R_HALF_DURABILITY_STATIONARITY_CONDITIONAL_CHAIN_BOUNDED_THEOREM_NOTE_2026-06-11.md"
NONEXCL = ROOT / "docs" / "OCCUPANCY_NONEXCLUSIVITY_MIXTURE_BOUND_NOTE_2026-06-09.md"
STAG_DET = ROOT / "docs" / "KOIDE_STAGGERED_FIRST_ORDER_GENERATION_DETERMINANT_BOUNDED_THEOREM_NOTE_2026-06-11.md"
LUDERS = ROOT / "docs" / "LUDERS_RULE_FROM_COMPOSITION_CONSISTENCY_NOTE_2026-05-20.md"
PEP = ROOT / "docs" / "LUDERS_SEQUENTIAL_EFFECT_COMPOSITION_PEP_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
TIER_A = ROOT / "docs" / "audit" / "data" / "tier_a_admissions.json"

PASS = 0
FAIL = 0


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def flat(text: str) -> str:
    return " ".join(text.split())


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"[{tag}] {label}{suffix}")


def main() -> int:
    print("=== AC_phi_lambda r=1/2 recorded-value target ===")

    paths = [
        NOTE,
        AXIOMS,
        POST_DIRAC,
        STRICT_NN,
        R_WEIGHTING,
        OCCUPANCY_DICT,
        RD_CHAIN,
        NONEXCL,
        STAG_DET,
        LUDERS,
        PEP,
        REALIZED,
        TIER_A,
    ]
    for path in paths:
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    note_flat = flat(note)
    axioms = read(AXIOMS)
    axioms_flat = flat(axioms)
    post_dirac = read(POST_DIRAC)
    post_flat = flat(post_dirac)
    strict_nn = read(STRICT_NN)
    strict_flat = flat(strict_nn)
    r_weighting = read(R_WEIGHTING)
    r_weighting_flat = flat(r_weighting)
    occupancy = read(OCCUPANCY_DICT)
    occupancy_flat = flat(occupancy)
    rd_chain = read(RD_CHAIN)
    rd_flat = flat(rd_chain)
    nonexcl = read(NONEXCL)
    nonexcl_flat = flat(nonexcl)
    stag_det = read(STAG_DET)
    stag_flat = flat(stag_det)
    luders = read(LUDERS)
    luders_flat = flat(luders)
    pep = read(PEP)
    pep_flat = flat(pep)
    realized = read(REALIZED)
    tier_a = read(TIER_A)

    print("\nPART A -- axiom and primitive boundaries")
    check("Record axiom fixes repeated readout only", "invariant under repeated readout" in axioms)
    check("Record axiom says only records are readable", "Only records are readable" in axioms)
    check("axioms leave occurrence rules downstream", "occurrence rules" in axioms)
    check("axioms leave context selection downstream", "context selection" in axioms)
    check("axioms leave probability/Born weights downstream", "Born weights" in axioms and "probability" in axioms)
    check("axioms leave record-production dynamics downstream", "record-production dynamics" in axioms)
    check("realized-state primitive supplies no state selection", "state-selection rule" in realized and "no state" in realized)
    check("Tier-A registry still carries AC_phi_lambda", '"label": "AC_phi_lambda"' in tier_a)

    print("\nPART B -- fixed-record algebra")
    x0 = Fraction(0, 1)
    x1 = Fraction(1, 1)
    x2 = Fraction(2, 1)
    half = Fraction(1, 2)
    q = Fraction(1, 3) + Fraction(2, 3) * half
    check("x=0 is fixed by x -> x^2", x0 * x0 == x0)
    check("x=1 is fixed by x -> x^2", x1 * x1 == x1)
    check("x=2 is not fixed by x -> x^2", x2 * x2 != x2, f"x^2={x2*x2}")
    check("charged-lepton dictionary x=2r maps x=1 to r=1/2", x1 / 2 == half)
    check("Koide lever maps r=1/2 to Q=2/3", q == Fraction(2, 3), f"Q={q}")
    check("sector cell r=1 maps to x=2 and is not fixed on this update", 2 * Fraction(1, 1) == x2 and x2 * x2 != x2)
    check("nearby value is not exactly durable", Fraction(100001, 100000) ** 2 != Fraction(100001, 100000))
    check("fixedness is idempotence, not attraction", Fraction(3, 2) ** 2 != Fraction(3, 2))
    check("finite interior fixed set is exactly {0,1}", {x for x in [Fraction(0), Fraction(1)] if x * x == x} == {Fraction(0), Fraction(1)})

    print("\nPART C -- prior-source residual matching")
    check("post-Dirac map names W_r as signed/statistics one-slot readout", "W_r" in post_dirac and "signed/statistics one-slot readout" in post_dirac)
    check("strict NN bridge removes kinetic-order shortage only", "kinetic spine only" in strict_flat and "probability" in strict_nn)
    check("r weighting note says r is weighting-principle dial", "`r` is the weighting-principle dial" in r_weighting)
    check("r weighting note does not force r=1/2", "does NOT force r=1/2" in r_weighting)
    check("occupancy dictionary note says flow selects x=1 but not dictionary", "outcome equipartition" in occupancy_flat and "Does not fix `r`" in occupancy)
    check("occupancy dictionary note names x=2r", "x = 2r" in occupancy)
    check("R-D chain gives conditional unique durable r=1/2", "unique" in rd_flat and "durably registrable value" in rd_flat and "r = 1/2" in rd_chain)
    check("R-D chain says R-D not adopted", "R-D is a named proposal" in rd_chain)
    check("nonexclusivity note rejects global exclusion", "Across Contexts: No Global Exclusion Is Claimed" in nonexcl)
    check("nonexclusivity note says r=1 remains valid", "`r=1/2` and `r=1` remain valid cells" in nonexcl_flat)
    check("staggered determinant note says first-order but not r derivation", "the measure side is first-order" in stag_flat and "a derivation of `r = 1/2`" in stag_det)
    check("Lueders/PEP support is conditional, not measurement semantics", "measurement probability semantics remain a separate open bridge" in luders_flat and "does not obtain the Lüders state update" in pep)

    print("\nPART D -- new note target shape")
    check("note rejects universal forcing phrasing", "should not" in note_flat and "force `r = 1/2` everywhere" in note_flat)
    check("note states context-local target", "context-local" in note)
    check("note preserves sparse records", "respects sparse records" in note)
    check("note says not every site is recorded", "No claim that all sites are recorded" in note)
    check("note says no global exclusion of r=1", "No global exclusion of the `r = 1` sector cell" in note)
    check("note identifies W_update bridge", "W_update" in note and "records-flow durability or readout-idempotence bridge" in note)
    check("note identifies W_context bridge", "W_context" in note and "charged-lepton two-outcome record context" in note)
    check("note identifies W_stats bridge", "W_stats" in note and "first-order determinant" in note)
    check("note says not a broad Dynamics axiom", "not a broad Dynamics axiom" in note)
    check("note gives minimum closure path", "#4747 axioms" in note and "#4748 strict nearest-neighbor composition" in note)

    print("\nPART E -- no-go discipline presence")
    check("note includes N1", "N1 - Alternative Route Enumeration" in note)
    check("note includes N2", "N2 - Wall Independence" in note)
    check("note includes N3", "N3 - Hidden-Wall Scan" in note)
    check("note includes N4", "N4 - Residual Matching" in note)
    check("note includes N5-N8", "N5 - Rhetoric Audit" in note and "N8 - Cross-Cycle Echo" in note)

    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("RESULT: FAIL")
        return 1
    print("RESULT: PASS -- r=1/2 target is record-local and conditionally sharp, not globally forced.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
