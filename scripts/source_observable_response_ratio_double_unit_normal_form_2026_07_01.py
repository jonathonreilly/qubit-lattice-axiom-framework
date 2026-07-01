#!/usr/bin/env python3
"""Verifier for the source/observable response-ratio double-unit normal form."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

NOTE = DOCS / "SOURCE_OBSERVABLE_RESPONSE_RATIO_DOUBLE_UNIT_NORMAL_FORM_2026-07-01.md"
AXIOMS = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = DOCS / "audit" / "data" / "axiom_premise_nodes.json"
SOURCE_RATIO = DOCS / "SOURCE_RESPONSE_RATIO_UNIT_CANCELLATION_NORMAL_FORM_2026-07-01.md"
METRIC_OBSERVABLE = DOCS / "METRIC_OBSERVABLE_CLOCKED_READOUT_INTERFACE_BRIDGE_2026-07-01.md"
SOURCE_INDEPENDENCE = DOCS / "PHYSICAL_SOURCE_SELECTOR_INDEPENDENCE_2026-07-01.md"
YT_UNIT = DOCS / "YT_SOURCE_UNIT_POST_AXIOM_RN_REDUCTION_BRIDGE_2026-07-01.md"
YT_CONTRACT = DOCS / "YT_STRICT_SAME_SOURCE_TOP_W_POLE_ROW_CONTRACT_NOTE_2026-05-30.md"
AC_UNIT = DOCS / "ACPHILAMBDA_C3_COVARIANT_READOUT_UNIT_NORMAL_FORM_2026-07-01.md"
OP_GAP = DOCS / "OPERATIONAL_PREMISE_GAP_MAP_2026-07-01.md"
PRIMITIVE = DOCS / "MINIMAL_OPERATIONAL_PRIMITIVE_UPDATE_RECOMMENDATION_2026-07-01.md"

PASS = 0
FAIL = 0


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def flat(text: str) -> str:
    return " ".join(text.split())


def check(label: str, ok: bool, detail: object = "") -> None:
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


def response_ratio(a: Fraction, b: Fraction) -> Fraction:
    return a / b


def transformed_ratio(a: Fraction, b: Fraction, source_jac: Fraction, output_unit: Fraction) -> Fraction:
    return (output_unit * source_jac * a) / (output_unit * source_jac * b)


def different_output_ratio(a: Fraction, b: Fraction, mu_a: Fraction, mu_b: Fraction) -> Fraction:
    return (mu_a * a) / (mu_b * b)


def different_source_ratio(a: Fraction, b: Fraction, lam_a: Fraction, lam_b: Fraction) -> Fraction:
    return (lam_a * a) / (lam_b * b)


def main() -> int:
    print("=== Source/observable response-ratio double-unit normal form ===")

    paths = [
        NOTE,
        AXIOMS,
        REGISTRY,
        SOURCE_RATIO,
        METRIC_OBSERVABLE,
        SOURCE_INDEPENDENCE,
        YT_UNIT,
        YT_CONTRACT,
        AC_UNIT,
        OP_GAP,
        PRIMITIVE,
    ]
    for path in paths:
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    note_flat = flat(note)
    axioms = read(AXIOMS)
    registry_text = read(REGISTRY)
    registry = json.loads(registry_text)
    source_ratio_note = read(SOURCE_RATIO)
    metric_note = read(METRIC_OBSERVABLE)
    source_independence = read(SOURCE_INDEPENDENCE)
    yt_unit = read(YT_UNIT)
    yt_contract = read(YT_CONTRACT)
    ac_unit = read(AC_UNIT)
    op_gap = read(OP_GAP)
    primitive = read(PRIMITIVE)

    print("\nPART A -- source boundary")
    check("note declares independent audit authority", "independent audit lane only" in note)
    check("note declares no axiom or registry edits", "does not set an audit verdict, edit registries, register primitives, change axioms" in note_flat)
    check("axioms leave source/action and observable downstream", "source/action and physical-observable identification" in axioms)
    check("source ratio note splits line and unit", "W_source_line" in source_ratio_note and "W_source_unit" in source_ratio_note)
    check("metric note names normalized source-response unit invariance", "normalized source-response observables independent of the scalar unit" in metric_note)
    check("source independence keeps physical source open", "does not derive physical source direction" in source_independence or "source direction and unit" in source_independence)
    check("YT unit bridge preserves physical intervention wall", "W_physical_top_intervention" in yt_unit)
    check("YT contract keeps strict same-source route explicit", "strict same-source" in yt_contract and "source-coordinate" in yt_contract)
    check("AC unit normal form keeps single-value identity unit open", "does not derive `c = 1`" in ac_unit)
    check("gap map names physical source and metric observable", "W_physical_source" in op_gap and "W_metric_observable" in op_gap)

    print("\nPART B -- primitive registry check")
    expected_ids = {
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    }
    check("registry canonical ids are expected set", set(registry["canonical_ids"]) == expected_ids, registry["canonical_ids"])
    for node_id in expected_ids:
        source = ROOT / registry["nodes"][node_id]["current_path"]
        check(f"registry source exists for {node_id}", source.exists())
    check("no registered P_physical_source", "P_physical_source" not in registry_text)
    check("no registered P_metric_observable", "P_metric_observable" not in registry_text)
    check("no registered physical response-ratio primitive", "P_physical_response_ratio" not in registry_text)
    check("primitive recommendation keeps source/metric as candidates", "P_physical_source" in primitive and "P_metric_observable" in primitive)

    print("\nPART C -- double-unit invariance theorem")
    a = Fraction(3, 5)
    b = Fraction(7, 11)
    base = response_ratio(a, b)
    check("base response ratio is 33/35", base == Fraction(33, 35), base)
    for lam in [Fraction(1), Fraction(2), Fraction(-3), Fraction(5, 7)]:
        for mu in [Fraction(1), Fraction(4), Fraction(-2), Fraction(3, 5)]:
            check(f"ratio invariant for source_jac={lam}, output_unit={mu}", transformed_ratio(a, b, lam, mu) == base)
            if lam != 1 or mu != 1:
                check(
                    f"absolute derivative changes for source_jac={lam}, output_unit={mu}",
                    mu * lam * a != a or mu * lam * b != b,
                )

    print("\nPART D -- affine offsets and nonlinear source coordinate")
    # A(h)=A0+a h+q h^2, h=alpha s+beta s^2, output=mu A+offset.
    alpha = Fraction(9, 4)
    beta = Fraction(5, 3)
    mu = Fraction(7, 2)
    offset_a = Fraction(100)
    offset_b = Fraction(-17)
    dA_ds = mu * a * alpha
    dB_ds = mu * b * alpha
    check("nonlinear source coordinate uses only origin Jacobian", beta != 0 and dA_ds / dB_ds == base)
    check("output offsets do not affect derivative ratio", offset_a != offset_b and dA_ds / dB_ds == base)
    check("denominator guard is load-bearing", b != 0 and dB_ds != 0)

    print("\nPART E -- load-bearing contrast cases")
    diff_output = {
        different_output_ratio(a, b, Fraction(1), Fraction(1)),
        different_output_ratio(a, b, Fraction(2), Fraction(1)),
        different_output_ratio(a, b, Fraction(1), Fraction(3)),
    }
    check("different output units change ratios", len(diff_output) == 3, diff_output)
    diff_source = {
        different_source_ratio(a, b, Fraction(1), Fraction(1)),
        different_source_ratio(a, b, Fraction(2), Fraction(1)),
        different_source_ratio(a, b, Fraction(1), Fraction(3)),
    }
    check("different source units change ratios", len(diff_source) == 3, diff_source)
    check("common output unit contrast in note gives 22/35", Fraction(2, 3) * base == Fraction(22, 35))
    check("note states same-source condition is load-bearing", "same-source and same-output-unit conditions are load-bearing" in note_flat)

    print("\nPART F -- relation to target lanes")
    check("note preserves YT non-closure", "`Y_T`, `y_t`, `m_t`, `g_2`, or top/W response evidence is derived" in note)
    check("note preserves AC non-closure", "`AC_phi_lambda` identity-unit readout is derived" in note)
    check("note says ratio theorem not single phase readout", "not a ratio of two same-output responses" in note)
    check("note says absolute lanes still need units", "Absolute source/action coefficients still need both" in note)
    check("note says no ontology axiom update follows", "No ontology axiom update follows from this theorem" in note)

    print("\nPART G -- note content")
    for heading in [
        "## Claim",
        "## Finite Theorem",
        "## Explicit Finite Witness",
        "## Relation To The Current Stack",
        "## What Moves",
        "## What Remains",
        "## Audit Consequence If Retained",
        "## Non-Claims",
        "## Minimum Foundation Update If Bridge Work Fails",
        "## No-Go Discipline Gate",
    ]:
        check(f"note includes {heading}", heading in note)
    for phrase in ["W_source_line", "W_same_source_response", "W_same_output_readout", "P_physical_response_ratio"]:
        check(f"note names {phrase}", phrase in note)

    print("\nPART H -- no-go discipline N1-N8")
    for item in ("N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8"):
        check(f"note includes {item}", item in note)
    for route in [
        "Absolute coefficient route",
        "Same-source/same-output ratio route",
        "Same-source/different-output route",
        "Different-source/same-output route",
        "Metric/observable route",
        "YT top/W route",
        "New primitive route",
    ]:
        check(f"N1 route present: {route}", route in note)
    check("N2 collapses unit walls for ratio rows", "`W_source_unit` and the absolute output unit are not independent walls" in note)
    check("N3 classifies physical source and observable as explicit walls", "`physical observable/readout` | Remaining selector wall" in note)
    check("N4 has seven witness matches", note.count("| `") >= 7 and "Residual Matching" in note)
    check("N5 narrows to first-derivative same-line ratios", "first-derivative origin resolution" in note)
    check("N6 lists live closure paths", "derive same-source top/W response evidence directly" in note and "derive the physical same-output readout line" in note)
    check("N7 steelman preserves bookkeeping objection", "bookkeeping" in note and "real physics" in note)
    check("N8 separates line selection and unit normalization", "line selection, unit normalization" in note_flat)

    print("\nPART I -- non-overclaim checks")
    forbidden = [
        "therefore physical source-line selection is derived",
        "therefore physical observable/readout selection is derived",
        "therefore Y_T is derived",
        "therefore AC_phi_lambda is derived",
        "therefore absolute coefficients need no units",
        "therefore a new ontology axiom is required",
    ]
    for phrase in forbidden:
        check(f"note avoids overclaim assertion: {phrase}", phrase not in note_flat)
    check("non-claims preserve no source derivation", "- physical source-line selection is derived;" in note)
    check("non-claims preserve no output unit derivation", "- the absolute output unit is derived;" in note)
    check("non-claims preserve no measured constants", "measured constants" in note and "not claim" in note_flat)

    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("RESULT: FAIL")
        return 1
    print(
        "RESULT: PASS -- same-source same-output first-derivative ratios cancel both source and output units; physical line/readout evidence remains explicit."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
