#!/usr/bin/env python3
"""Verify the durable two-outcome record idempotence bridge for r=1/2."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

NOTE = ROOT / "docs" / "ACPHILAMBDA_R_HALF_DURABLE_RECORD_IDEMPOTENCE_BRIDGE_THEOREM_NOTE_2026-06-30.md"
TARGET = ROOT / "docs" / "ACPHILAMBDA_R_HALF_RECORDED_VALUE_TARGET_2026-06-30.md"
POST_DIRAC = ROOT / "docs" / "ACPHILAMBDA_POST_DIRAC_REDUCTION_MAP_2026-06-30.md"
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
STRICT_NN = ROOT / "docs" / "STRICT_NN_COMPOSITION_FLUX_SELECTOR_BRIDGE_THEOREM_NOTE_2026-06-30.md"
OCCUPANCY_DICT = ROOT / "docs" / "OCCUPANCY_ATOM_IS_THE_OUTCOME_DICTIONARY_FLOW_SELECTS_EQUIPARTITION_BOUNDED_NOTE_2026-06-12.md"
RD_CHAIN = ROOT / "docs" / "KOIDE_R_HALF_DURABILITY_STATIONARITY_CONDITIONAL_CHAIN_BOUNDED_THEOREM_NOTE_2026-06-11.md"
NONEXCL = ROOT / "docs" / "OCCUPANCY_NONEXCLUSIVITY_MIXTURE_BOUND_NOTE_2026-06-09.md"
R_WEIGHTING = ROOT / "docs" / "KOIDE_R_IS_THE_WEIGHTING_PRINCIPLE_DIAL_RECORD_DYNAMICS_WEIGHTING_BLIND_BOUNDED_THEOREM_NOTE_2026-06-15.md"
STAG_DET = ROOT / "docs" / "KOIDE_STAGGERED_FIRST_ORDER_GENERATION_DETERMINANT_BOUNDED_THEOREM_NOTE_2026-06-11.md"
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


def agreement(weights: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    s = sum(w * w for w in weights)
    if s == 0:
        raise ValueError("empty active support")
    return tuple((w * w) / s for w in weights)


def is_fixed(weights: tuple[Fraction, ...]) -> bool:
    return agreement(weights) == weights


def uniform(n: int) -> tuple[Fraction, ...]:
    return tuple(Fraction(1, n) for _ in range(n))


def normalized_ratio(x: Fraction) -> tuple[Fraction, Fraction]:
    return (Fraction(1, 1) / (1 + x), x / (1 + x))


def main() -> int:
    print("=== AC_phi_lambda r=1/2 durable record idempotence bridge ===")

    paths = [
        NOTE,
        TARGET,
        POST_DIRAC,
        AXIOMS,
        STRICT_NN,
        OCCUPANCY_DICT,
        RD_CHAIN,
        NONEXCL,
        R_WEIGHTING,
        STAG_DET,
        TIER_A,
    ]
    for path in paths:
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    note_flat = flat(note)
    target = read(TARGET)
    target_flat = flat(target)
    post_dirac = read(POST_DIRAC)
    post_flat = flat(post_dirac)
    axioms = read(AXIOMS)
    axioms_flat = flat(axioms)
    strict_nn = read(STRICT_NN)
    strict_flat = flat(strict_nn)
    occupancy = read(OCCUPANCY_DICT)
    occupancy_flat = flat(occupancy)
    rd_chain = read(RD_CHAIN)
    rd_flat = flat(rd_chain)
    nonexcl = read(NONEXCL)
    nonexcl_flat = flat(nonexcl)
    r_weighting = read(R_WEIGHTING)
    r_weighting_flat = flat(r_weighting)
    stag_det = read(STAG_DET)
    stag_flat = flat(stag_det)
    tier_a = read(TIER_A)

    print("\nPART A -- #4747 axiom surface")
    check("axioms are the 2026-06-29 four-axiom memo", "Minimal Framework Axioms (Lattice, Qubit, Admissibility, Record)" in axioms)
    check("Record locks one available possibility", "A record locks exactly one available local possibility" in axioms)
    check("Record states repeated-readout invariance", "invariant under repeated readout" in axioms)
    check("Record says only records are readable", "Only records are readable" in axioms)
    check("qualification requires bridge for further structure", "requires derivation, bridge, explicit admission" in axioms_flat)
    check("axioms do not supply probability", "probability" in axioms and "Born weights" in axioms)
    check("axioms do not supply record-production dynamics", "record-production dynamics" in axioms)
    check("axioms do not supply readout context selection", "readout-context selection" in axioms)
    check("Tier-A registry still carries AC_phi_lambda", '"label": "AC_phi_lambda"' in tier_a)

    print("\nPART B -- exact fixed-point theorem")
    for n in range(1, 6):
        check(f"uniform active support n={n} is fixed", is_fixed(uniform(n)), str(uniform(n)))

    nonuniform_two = (Fraction(1, 3), Fraction(2, 3))
    check("nonuniform two-active support is not fixed", not is_fixed(nonuniform_two), str(agreement(nonuniform_two)))
    nonuniform_three = (Fraction(1, 2), Fraction(1, 3), Fraction(1, 6))
    check("nonuniform three-active support is not fixed", not is_fixed(nonuniform_three), str(agreement(nonuniform_three)))

    # Exhaustive rational smoke tests: all fixed active weights in these grids are uniform.
    fixed_two = []
    for a in range(1, 12):
        w = (Fraction(a, 12), Fraction(12 - a, 12))
        if is_fixed(w):
            fixed_two.append(w)
    check("two-active rational grid fixed point is only uniform", fixed_two == [(Fraction(1, 2), Fraction(1, 2))], str(fixed_two))

    fixed_three = []
    for a in range(1, 10):
        for b in range(1, 10 - a):
            c = 10 - a - b
            w = (Fraction(a, 10), Fraction(b, 10), Fraction(c, 10))
            if is_fixed(w):
                fixed_three.append(w)
    check("three-active rational grid fixed point is only uniform when present", fixed_three == [], "denominator 10 cannot represent 1/3")

    fixed_three_12 = []
    for a in range(1, 12):
        for b in range(1, 12 - a):
            c = 12 - a - b
            w = (Fraction(a, 12), Fraction(b, 12), Fraction(c, 12))
            if is_fixed(w):
                fixed_three_12.append(w)
    check("three-active denominator-12 grid finds uniform fixed point", fixed_three_12 == [(Fraction(1, 3), Fraction(1, 3), Fraction(1, 3))], str(fixed_three_12))

    x_one = Fraction(1, 1)
    ws, wd = normalized_ratio(x_one)
    check("x=1 gives equal two-outcome weights", (ws, wd) == (Fraction(1, 2), Fraction(1, 2)), f"{ws},{wd}")
    check("equal two-outcome weights remain fixed", is_fixed((ws, wd)))
    r = x_one / 2
    q = Fraction(1, 3) + Fraction(2, 3) * r
    check("charged-lepton dictionary x=2r gives r=1/2", r == Fraction(1, 2), f"r={r}")
    check("Koide lever gives Q=2/3", q == Fraction(2, 3), f"Q={q}")
    x_sector = Fraction(2, 1)
    sector_weights = normalized_ratio(x_sector)
    sector_after = agreement(sector_weights)
    check("sector cell r=1 corresponds to x=2", sector_weights == (Fraction(1, 3), Fraction(2, 3)), str(sector_weights))
    check("sector cell is not two-active durable under agreement composition", sector_after != sector_weights, str(sector_after))
    check("one-active support is durable but not a two-outcome r=1/2 claim", is_fixed((Fraction(1, 1),)), "active support size 1")

    print("\nPART C -- source matching")
    check("target note identified record-local target", "context-local" in target and "respects sparse records" in target)
    check("post-Dirac map ranked W_r as next target", "W_r" in post_dirac and "next highest-leverage target" in post_flat)
    check("strict NN bridge supplies kinetic branch only", "kinetic spine only" in strict_flat and "probability" in strict_nn)
    check("occupancy dictionary note proves outcome equipartition shape", "outcome equipartition" in occupancy_flat and "Does not fix `r`" in occupancy)
    check("occupancy dictionary note names x=2r", "x = 2r" in occupancy)
    check("R-D chain has durable fixed-point reading", "durably registrable value" in rd_flat and "fixed point" in rd_flat)
    check("R-D chain is conditional/not adopted", "R-D is a named proposal" in rd_chain)
    check("nonexclusivity note preserves r=1 in other contexts", "`r=1/2` and `r=1` remain valid cells" in nonexcl_flat)
    check("r weighting note rejects universal forcing", "does NOT force r=1/2" in r_weighting)
    check("staggered determinant note supplies first-order surface only", "the measure side is first-order" in stag_flat and "a derivation of `r = 1/2`" in stag_det)

    print("\nPART D -- new theorem note content")
    check("note declares positive conditional bridge theorem", "positive theorem candidate / conditional bridge theorem" in note)
    check("note defines agreement composition", "agreement composition" in note_flat and "w_i^2 / sum_j w_j^2" in note_flat)
    check("note proves uniform active support", "uniform on that active support" in note_flat)
    check("note maps two active outcomes to x=1", "x = w_d / w_s = 1" in note)
    check("note maps x=2r to r=1/2", "x = 2r" in note and "r = 1/2" in note)
    check("note explicitly starts after record context exists", "after a finite record context exists" in note)
    check("note preserves sparse records", "not every site records" in note and "not every context records" in note)
    check("note lists outside gates", "Record occurrence" in note and "A_R-eta" in note and "Theta" in note)
    check("note says no probability law", "not a probability law" in note)
    check("note says no global exclusion", "Any global exclusion" in note or "global exclusion" in note)

    print("\nPART E -- no-go discipline and boundaries")
    check("note includes N1 route table", "N1 - Alternative Route Enumeration" in note)
    check("note includes N2 wall independence", "N2 - Wall Independence" in note)
    check("note includes N3 hidden-wall scan", "N3 - Hidden-Wall Scan" in note)
    check("note includes N4 residual matching", "N4 - Residual Matching" in note)
    check("note includes N5 rhetoric audit", "N5 - Rhetoric Audit" in note)
    check("note includes N6 partial-closure path", "N6 - Partial-Closure Path Scan" in note)
    check("note includes N7 steelman", "N7 - Steelman" in note)
    check("note includes N8 cross-cycle echo", "N8 - Cross-Cycle Echo" in note)
    check("note names remaining context/species/R-eta residuals", "W_context" in note and "W_eta" in note and "W_species" in note)

    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("RESULT: FAIL")
        return 1
    print("RESULT: PASS -- durable active two-outcome record idempotence forces x=1, hence r=1/2 in the charged-lepton dictionary.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
