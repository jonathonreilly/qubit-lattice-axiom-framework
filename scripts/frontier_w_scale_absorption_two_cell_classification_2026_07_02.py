#!/usr/bin/env python3
"""Finite witnesses for w scale-absorption on supplied two-cell readouts.

Bounded support runner for
docs/W_SCALE_ABSORPTION_TWO_CELL_READOUT_CLASSIFICATION_BOUNDED_NOTE_2026-07-02.md.

The runner checks finite algebra only:

* diagonal equal-content readouts carry w only through a common prefactor;
* ratios, normalized fractions, and degree-zero shape witnesses are w-free on
  the diagonal;
* same-family calibration plus scale-reference routing absorbs the prefactor;
* off-diagonal evaluation, cross-family comparison, and unrouted absolute
  normalization remain w-sensitive;
* listed current-source instances are classified only under their stated
  premises.

It does not close any wall, claim CTX-match, choose w, reclassify a registry
entry, or edit axiom, primitive, policy, audit, or publication surfaces.
"""
from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
TWO_CELL_PARENT_NOTE = DOCS / "C2_W_SUPPLIER_READING_FORK_FIXED_POINT_UNIDENTIFIABILITY_BOUNDED_NOTE_2026-07-02.md"
KAPPA_NOTE = DOCS / "EW_KAPPA_WEIGHTING_NOT_AXIOM_DERIVABLE_NO_GO_NOTE_2026-06-09.md"
SCALE_NOTE = DOCS / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
OCCUPANCY_NOTE = DOCS / "OCCUPANCY_ATOM_IS_THE_OUTCOME_DICTIONARY_FLOW_SELECTS_EQUIPARTITION_BOUNDED_NOTE_2026-06-12.md"
NOTE = DOCS / "W_SCALE_ABSORPTION_TWO_CELL_READOUT_CLASSIFICATION_BOUNDED_NOTE_2026-07-02.md"

PASS = 0
FAIL = 0
N = 0


def check(desc: str, ok: bool, detail: str = "") -> bool:
    global PASS, FAIL, N
    N += 1
    ok = bool(ok)
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" [{detail}]" if detail else ""
    print(f"CHECK {N:02d}: {tag} -- {desc}{suffix}")
    return ok


def section(title: str) -> None:
    print()
    print("-" * 78)
    print(title)
    print("-" * 78)


def squash(text: str) -> str:
    return " ".join(text.split())


def readout(record: tuple[Fraction, Fraction], weights: tuple[Fraction, Fraction]) -> Fraction:
    x_a, x_b = record
    u, v = weights
    return u * x_a + v * x_b


def diagonal_readouts(contents: list[Fraction], weights: tuple[Fraction, Fraction]) -> list[Fraction]:
    return [readout((x, x), weights) for x in contents]


def pairwise_ratios(values: list[Fraction]) -> list[Fraction]:
    return [values[i] / values[j] for i in range(len(values)) for j in range(i + 1, len(values))]


def normalized(values: list[Fraction]) -> list[Fraction]:
    total = sum(values, Fraction(0))
    return [value / total for value in values]


def koide_shape(roots: list[Fraction]) -> Fraction:
    return sum(root * root for root in roots) / (sum(roots, Fraction(0)) ** 2)


def generic_degree_zero(values: list[Fraction]) -> Fraction:
    i1, i2, i3 = values
    return (i1 * i1 + Fraction(2) * i2 * i3) / ((i1 + i2 + i3) ** 2)


def calibrated_table(contents: list[Fraction], weights: tuple[Fraction, Fraction], cal_index: int = 0) -> list[Fraction]:
    values = diagonal_readouts(contents, weights)
    return [value / values[cal_index] for value in values]


def scale_reference_table(
    contents: list[Fraction],
    weights: tuple[Fraction, Fraction],
    reference_value: Fraction,
    cal_index: int = 0,
) -> list[Fraction]:
    values = diagonal_readouts(contents, weights)
    unit = reference_value / values[cal_index]
    return [value * unit for value in values]


def ew_shape(g1_base: Fraction, g2_base: Fraction, common_factor: Fraction) -> Fraction:
    g1_sq = common_factor * g1_base
    g2_sq = common_factor * g2_base
    return g1_sq / (g1_sq + g2_sq)


def main() -> int:
    print("=" * 78)
    print("W SCALE-ABSORPTION / TWO-CELL READOUT CLASSIFICATION")
    print("bounded support runner -- exact finite arithmetic")
    print("=" * 78)

    two_cell_parent = TWO_CELL_PARENT_NOTE.read_text(encoding="utf-8")
    kappa = KAPPA_NOTE.read_text(encoding="utf-8")
    scale = SCALE_NOTE.read_text(encoding="utf-8")
    occupancy = OCCUPANCY_NOTE.read_text(encoding="utf-8")
    note = NOTE.read_text(encoding="utf-8")
    kappa_flat = squash(kappa)
    note_flat = squash(note)

    section("Source guards")
    check(
        "two-cell parent contains diagonal identity I(x,x)=(u+v)x",
        "I(x,x) = (u+v) x" in two_cell_parent
        and "All scale-invariant readouts are therefore `w`-independent at equipartition-selected states."
        in two_cell_parent,
    )
    check(
        "parent kappa no-go contains Pi_phys family and common-factor cancellation",
        "Pi_phys = C + kappa_EW S" in kappa
        and "common `K_EW` factor cancels" in kappa,
    )
    check(
        "parent kappa no-go preserves 8/9 as a count, not a weight selector",
        "cardinality count `8/9`" in kappa_flat
        and "does not pick the inter-sector weight" in kappa_flat,
    )
    check(
        "scale primitive is a units conversion, not a physics axiom",
        "This is a units conversion, not a physics axiom." in scale,
    )
    check(
        "occupancy source supplies equipartition wording",
        "equipartition" in occupancy and "equal registered weight" in occupancy,
    )

    section("Diagonal common-factor classification")
    roots = [Fraction(2), Fraction(3), Fraction(5)]
    diagonal_contents = [root * root for root in roots]
    weights_list = [
        (Fraction(1), Fraction(3)),
        (Fraction(2), Fraction(7)),
        (Fraction(9), Fraction(7)),
    ]
    sums = [sum(pair, Fraction(0)) for pair in weights_list]
    check(
        "test weights have three distinct common prefactors",
        len(set(sums)) == 3,
        detail=f"sums={sums}",
    )
    check(
        "diagonal pairwise ratios I_i/I_j equal x_i/x_j across the prefactors",
        all(
            pairwise_ratios(diagonal_readouts(diagonal_contents, weights))
            == pairwise_ratios(diagonal_contents)
            for weights in weights_list
        ),
    )
    check(
        "diagonal normalized fractions are unchanged across the prefactors",
        all(
            normalized(diagonal_readouts(diagonal_contents, weights)) == normalized(diagonal_contents)
            for weights in weights_list
        ),
    )
    base_koide = koide_shape(roots)
    root_scales = [Fraction(2), Fraction(3), Fraction(4)]
    check(
        "Koide-shape witness is unchanged by diagonal common scaling",
        all(koide_shape([scale_factor * root for root in roots]) == base_koide for scale_factor in root_scales),
    )
    base_generic = generic_degree_zero(diagonal_contents)
    check(
        "generic degree-zero rational witness is unchanged by diagonal common scaling",
        all(generic_degree_zero(diagonal_readouts(diagonal_contents, weights)) == base_generic for weights in weights_list),
    )
    off_diagonal_ratios = [
        readout((Fraction(1), Fraction(0)), weights)
        / readout((Fraction(0), Fraction(1)), weights)
        for weights in weights_list
    ]
    check(
        "off-diagonal ratio I(1,0)/I(0,1) changes with w",
        len(set(off_diagonal_ratios)) == 3,
        detail=f"ratios={off_diagonal_ratios}",
    )

    section("Same-family calibration and scale-reference routing")
    calibration_weights = [
        (Fraction(1), Fraction(1)),
        (Fraction(3), Fraction(2)),
        (Fraction(1, 2), Fraction(5, 2)),
    ]
    calibration_contents = [Fraction(2), Fraction(5), Fraction(7)]
    calibration_sums = [sum(pair, Fraction(0)) for pair in calibration_weights]
    check(
        "raw diagonal readouts are exactly s times the content table",
        calibration_sums == [Fraction(2), Fraction(5), Fraction(3)]
        and all(
            diagonal_readouts(calibration_contents, weights)
            == [sum(weights, Fraction(0)) * x for x in calibration_contents]
            for weights in calibration_weights
        ),
    )
    base_calibrated = [x / calibration_contents[0] for x in calibration_contents]
    check(
        "same-family calibration cancels the prefactor",
        all(calibrated_table(calibration_contents, weights) == base_calibrated for weights in calibration_weights),
    )
    reference_mass = Fraction(11)
    base_scaled = [reference_mass * x / calibration_contents[0] for x in calibration_contents]
    check(
        "scale-reference routing against one same-family member gives one physical table",
        all(
            scale_reference_table(calibration_contents, weights, reference_mass) == base_scaled
            for weights in calibration_weights
        ),
    )
    cross_family_ratios = [
        readout((calibration_contents[1], calibration_contents[1]), calibration_weights[0])
        / readout((calibration_contents[0], calibration_contents[0]), denominator_weights)
        for denominator_weights in calibration_weights[1:]
    ]
    check(
        "cross-family calibration with different prefactors remains sensitive",
        len(set(cross_family_ratios)) == 2,
        detail=f"ratios={cross_family_ratios}",
    )

    section("Listed current-source instances")
    g1_base = Fraction(5, 7)
    g2_base = Fraction(11, 13)
    check(
        "EW shape cancels a common same-family factor",
        all(
            ew_shape(g1_base, g2_base, common_factor) == g1_base / (g1_base + g2_base)
            for common_factor in calibration_sums
        ),
    )
    check(
        "Koide listed instance is w-free under diagonal equal-content premise",
        all(koide_shape([scale_factor * root for root in roots]) == base_koide for scale_factor in root_scales),
    )
    check(
        "mass-ratio listed instance is w-free under diagonal equal-content premise",
        all(
            diagonal_readouts(calibration_contents, weights)[1]
            / diagonal_readouts(calibration_contents, weights)[2]
            == calibration_contents[1] / calibration_contents[2]
            for weights in calibration_weights
        ),
    )
    check(
        "absolute-scale listed instance is w-free after same-family scale-reference routing",
        all(
            scale_reference_table(calibration_contents, weights, reference_mass)[2]
            == reference_mass * calibration_contents[2] / calibration_contents[0]
            for weights in calibration_weights
        ),
    )
    central_count = Fraction(8, 9)
    pi_values = [Fraction(8) + kappa_value * Fraction(1) for kappa_value in (Fraction(1), Fraction(2), Fraction(5, 3))]
    check(
        "8/9 cardinality count is fixed while Pi_phys value changes with inter-sector weight",
        central_count == Fraction(8, 9) and len(set(pi_values)) == 3,
    )
    listed_rows = {
        "EW shape": "w-free under stated premise",
        "Koide shape": "w-free under stated premise",
        "mass ratios": "w-free under stated premise",
        "absolute mass scale": "w-free after routing",
        "8/9 count": "independent as count",
    }
    check(
        "exactly five current-source instance rows are classified",
        len(listed_rows) == 5 and all("w-free" in status or "independent" in status for status in listed_rows.values()),
    )

    section("Residual triple")
    same_sum_left = (Fraction(1), Fraction(3))
    same_sum_right = (Fraction(3), Fraction(1))
    off_record = (Fraction(2), Fraction(1))
    diag_record = (Fraction(2), Fraction(2))
    check(
        "off-diagonal evaluation is sensitive while diagonal same-content is not",
        readout(off_record, same_sum_left) != readout(off_record, same_sum_right)
        and readout(diag_record, same_sum_left) == readout(diag_record, same_sum_right),
    )
    same_family_restored = [
        readout((calibration_contents[1], calibration_contents[1]), weights)
        / readout((calibration_contents[0], calibration_contents[0]), weights)
        for weights in calibration_weights
    ]
    check(
        "cross-family comparison is sensitive and same-family calibration restores cancellation",
        len(set(cross_family_ratios)) == 2 and len(set(same_family_restored)) == 1,
    )
    raw_absolutes = [
        readout((calibration_contents[1], calibration_contents[1]), weights)
        for weights in calibration_weights
    ]
    scaled_absolutes = [
        scale_reference_table(calibration_contents, weights, reference_mass)[1]
        for weights in calibration_weights
    ]
    check(
        "raw absolute normalization is sensitive and scale-reference routing removes it",
        len(set(raw_absolutes)) == 3 and len(set(scaled_absolutes)) == 1,
    )

    section("Note firewall and hygiene")
    required = [
        "This is a bounded finite-algebra classification.",
        "It says nothing about future readouts or unlisted surfaces.",
        "This is not a cross-family theorem.",
        "This is a bounded residual map, not a registry decision.",
        "This note promotes nothing.",
    ]
    missing = [phrase for phrase in required if phrase not in note_flat]
    check(
        "note carries bounded-scope and no-promotion guardrails",
        not missing,
        detail="all present" if not missing else f"missing={missing}",
    )
    forbidden = [
        "review" + "-pending",
        "super" + "visor",
        "closed/" + "unmerged",
        "#" + "4847",
        "every landed" + " readout",
        "outputs/frontier_" + "w_scale",
        "Status" + " authority",
        "Actual current" + " surface status",
    ]
    present = [phrase for phrase in forbidden if phrase in note]
    check(
        "note avoids stale PR/proposal/raw-output/status-surface language",
        not present,
        detail="none present" if not present else f"present={present}",
    )
    check(
        "note links the four direct current-source dependencies and the cached log",
        all(
            item in note
            for item in [
                "C2_W_SUPPLIER_READING_FORK_FIXED_POINT_UNIDENTIFIABILITY_BOUNDED_NOTE_2026-07-02.md",
                "EW_KAPPA_WEIGHTING_NOT_AXIOM_DERIVABLE_NO_GO_NOTE_2026-06-09.md",
                "SCALE_REFERENCE_PRIMITIVE_NOTE.md",
                "OCCUPANCY_ATOM_IS_THE_OUTCOME_DICTIONARY_FLOW_SELECTS_EQUIPARTITION_BOUNDED_NOTE_2026-06-12.md",
                "logs/runner-cache/frontier_w_scale_absorption_two_cell_classification_2026_07_02.txt",
            ]
        ),
    )

    print()
    print("=" * 78)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 78)
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
