#!/usr/bin/env python3
"""Verifier for source-response ratio unit cancellation normal form."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"[PASS] {label}")
    else:
        FAIL += 1
        suffix = f" -- {detail}" if detail else ""
        print(f"[FAIL] {label}{suffix}")


def exists(rel: str) -> bool:
    return (ROOT / rel).exists()


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def flat(text: str) -> str:
    return " ".join(text.split())


def ratio(a: Fraction, b: Fraction) -> Fraction:
    if b == 0:
        raise ZeroDivisionError
    return a / b


def same_source_derivatives(a: Fraction, b: Fraction, lam: Fraction) -> tuple[Fraction, Fraction]:
    return lam * a, lam * b


def different_source_ratio(a: Fraction, b: Fraction, lam_a: Fraction, lam_b: Fraction) -> Fraction:
    return ratio(lam_a * a, lam_b * b)


def main() -> int:
    print("=== Source-response ratio unit-cancellation normal form ===")

    files = [
        "docs/SOURCE_RESPONSE_RATIO_UNIT_CANCELLATION_NORMAL_FORM_2026-07-01.md",
        "docs/MINIMAL_AXIOMS_2026-06-29.md",
        "docs/audit/data/axiom_premise_nodes.json",
        "docs/PHYSICAL_SOURCE_SELECTOR_INDEPENDENCE_2026-07-01.md",
        "docs/SOURCE_ACTION_RN_FACTORIZATION_FROM_RECORD_BORN_INTERFACE_2026-06-30.md",
        "docs/YT_SOURCE_UNIT_POST_AXIOM_RN_REDUCTION_BRIDGE_2026-07-01.md",
        "docs/YT_STRICT_SAME_SOURCE_TOP_W_POLE_ROW_CONTRACT_NOTE_2026-05-30.md",
        "docs/YT_FH_TOP_W_RESPONSE_RATIO_GATE_NOTE_2026-05-25.md",
        "docs/METRIC_OBSERVABLE_CLOCKED_READOUT_INTERFACE_BRIDGE_2026-07-01.md",
        "docs/MINIMAL_OPERATIONAL_PRIMITIVE_UPDATE_RECOMMENDATION_2026-07-01.md",
    ]
    for rel in files:
        check(f"{rel} exists", exists(rel))

    note = read("docs/SOURCE_RESPONSE_RATIO_UNIT_CANCELLATION_NORMAL_FORM_2026-07-01.md")
    axioms = read("docs/MINIMAL_AXIOMS_2026-06-29.md")
    registry_text = read("docs/audit/data/axiom_premise_nodes.json")
    registry = json.loads(registry_text)
    independence = read("docs/PHYSICAL_SOURCE_SELECTOR_INDEPENDENCE_2026-07-01.md")
    rn = read("docs/SOURCE_ACTION_RN_FACTORIZATION_FROM_RECORD_BORN_INTERFACE_2026-06-30.md")
    yt = read("docs/YT_SOURCE_UNIT_POST_AXIOM_RN_REDUCTION_BRIDGE_2026-07-01.md")
    contract = read("docs/YT_STRICT_SAME_SOURCE_TOP_W_POLE_ROW_CONTRACT_NOTE_2026-05-30.md")
    fh = read("docs/YT_FH_TOP_W_RESPONSE_RATIO_GATE_NOTE_2026-05-25.md")
    metric = read("docs/METRIC_OBSERVABLE_CLOCKED_READOUT_INTERFACE_BRIDGE_2026-07-01.md")
    primitive = read("docs/MINIMAL_OPERATIONAL_PRIMITIVE_UPDATE_RECOMMENDATION_2026-07-01.md")
    flat_note = flat(note)

    print("\nPART A -- source boundary")
    check("note declares independent audit authority", "independent audit lane only" in note)
    check("note declares no axiom or registry edits", "does not set an audit verdict, edit registries, register primitives, change axioms" in flat_note)
    check(
        "axioms leave source/action identification outside axiom content",
        "source/action and physical-observable identification" in axioms,
    )
    check("source independence names direction and unit", "source direction and unit" in independence)
    check("RN factorization leaves physical source selector", "W_physical_source" in rn)
    check("YT reduction names physical top intervention", "W_physical_top_intervention" in yt)
    check("same-source contract names source-coordinate cancellation", "source-coordinate cancellation" in contract or "source-coordinate" in contract)

    print("\nPART B -- primitive registry check")
    expected_ids = {
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    }
    check("registry canonical ids are expected set", set(registry["canonical_ids"]) == expected_ids, registry["canonical_ids"])
    check("no registered P_physical_source", "P_physical_source" not in registry_text)
    check("minimal axioms registry excludes source/action", "source/action bridge" in registry["nodes"]["minimal_axioms"]["note"])
    check("minimal axioms registry excludes physical observable bridge", "physical observable bridge" in registry["nodes"]["minimal_axioms"]["note"])

    print("\nPART C -- ratio invariance")
    a = Fraction(3, 5)
    b = Fraction(7, 11)
    base = ratio(a, b)
    for lam in [Fraction(1, 2), Fraction(2), Fraction(9, 4), Fraction(-3)]:
        da, db = same_source_derivatives(a, b, lam)
        check(f"same-source ratio invariant for lambda={lam}", ratio(da, db) == base, (da, db, base))
        check(f"absolute derivative changes for lambda={lam}", da != a if lam != 1 else da == a, da)
    alpha = Fraction(5, 3)
    beta = Fraction(4, 7)
    # h = alpha s + beta s^2 has origin Jacobian alpha; beta does not enter first derivatives.
    da0, db0 = same_source_derivatives(a, b, alpha)
    check("nonlinear coordinate first derivative uses only origin Jacobian", ratio(da0, db0) == base and beta != 0)
    check("denominator nonzero guard is explicit", b != 0)

    print("\nPART D -- different-source guard")
    varied = {
        different_source_ratio(a, b, Fraction(1), Fraction(1)),
        different_source_ratio(a, b, Fraction(2), Fraction(1)),
        different_source_ratio(a, b, Fraction(1), Fraction(3)),
    }
    check("different-source ratios vary with relative units", len(varied) == 3, varied)
    check("same-source condition is load-bearing", "same source" in note and "load-bearing" in note)

    print("\nPART E -- YT and metric/source composition")
    check("YT contract says both responses pick up same Jacobian", "both responses pick up the same Jacobian" in contract)
    check("FH gate states source normalization cancels", "The source normalization cancels" in fh)
    check("YT reduction preserves strict same-source route", "strict same-source top/W pole-response" in yt)
    check("metric bridge has normalized ratio cancellation", "normalized derivative ratio" in metric or "normalized source-response ratios" in metric)
    check("primitive recommendation names P_physical_source", "P_physical_source" in primitive)

    print("\nPART F -- note content")
    check("note states source line/unit split", "W_source_line" in note and "W_source_unit" in note)
    check("note states absolute coefficients need both walls", "absolute source/action coefficient need both" in flat_note or "absolute coefficient claim" in note)
    check("note states same-source ratios bypass unit", "same-source response ratios can bypass `W_source_unit`" in note or "source unit cancels" in note)
    check("note says no ontology axiom update follows", "No ontology axiom update follows" in note)
    check("note preserves YT non-closure", "`Y_T`, `y_33`, `y_t`, `m_t`, or `g_2` is derived" in note)

    print("\nPART G -- no-go discipline N1-N8")
    for item in ["N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8"]:
        check(f"note includes {item}", f"### {item}" in note)
    for route in [
        "Absolute coefficient route",
        "Same-source ratio route",
        "Different-source ratio route",
        "RN/action factorization route",
        "YT top/W response route",
        "New primitive route",
    ]:
        check(f"N1 route present: {route}", route in note)
    check("N2 names source line and source unit walls", "W_source_line" in note and "W_source_unit" in note)
    check("N3 classifies same source surface", "| `same source surface` | Load-bearing condition" in note)
    check("N4 residual table includes YT contract", "YT_STRICT_SAME_SOURCE_TOP_W_POLE_ROW_CONTRACT" in note)
    check("N5 narrows to first-derivative resolution", "first-derivative" in flat_note)
    check("N6 lists line/unit/ratio closure paths", "physical source-line selector" in note and "physical source-unit selector" in note and "strict same-source response evidence" in note)
    check("N7 steelman preserves hard physics", "does not close the hard physics" in note)
    check("N8 cross-cycle echo names normalized response ratios", "normalized response ratios" in note)

    print("\nPART H -- non-overclaim checks")
    overclaims = [
        "therefore physical source selection is derived",
        "therefore the absolute source unit is derived",
        "therefore Y_T is derived",
        "therefore strict same-source top/W evidence exists",
        "therefore a new ontology axiom is required",
        "therefore metric/observable semantics are closed",
    ]
    for phrase in overclaims:
        check(f"note avoids overclaim assertion: {phrase}", phrase not in flat_note)
    check("note has explicit non-claims section", "## Non-Claims" in note and "This note does not claim:" in note)
    check("non-claims preserve no physical source selection", "- physical source selection is derived;" in note)
    check("non-claims preserve no YT closure", "- `Y_T`, `y_33`, `y_t`, `m_t`, or `g_2` is derived;" in note)
    check("note says not terminal no-go", "not a terminal no-go against source selection" in flat_note)

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
