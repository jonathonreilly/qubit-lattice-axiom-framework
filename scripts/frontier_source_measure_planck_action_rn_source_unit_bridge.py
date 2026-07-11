#!/usr/bin/env python3
"""Planck-action to RN/Fisher source-unit bridge.

This runner verifies the exact algebra behind the bridge:

  exp(-S_h/kappa_Pl) / exp(-S_0/kappa_Pl)
    with S_h = S_0 - kappa_Pl h O
  equals the normalized RN source exp(h O) / E exp(h O).

It also checks the scaled family and the six-component Y_T consequence.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUT = ROOT / "outputs" / "source_measure_planck_action_rn_source_unit_bridge_2026-05-30.json"

NOTE = DOCS / "SOURCE_MEASURE_PLANCK_ACTION_RN_SOURCE_UNIT_BRIDGE_NOTE_2026-05-30.md"
BOUNDARY = DOCS / "SOURCE_MEASURE_LOG_SELECTION_BOUNDARY_THEOREM_NOTE_2026-05-30.md"
SCALE_PRIMITIVE = DOCS / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
PLANCK_UNIT = DOCS / "PLANCK_SOURCE_UNIT_NORMALIZATION_SUPPORT_THEOREM_NOTE_2026-04-25.md"
YT_FISHER = DOCS / "YT_PRIMITIVE_SOURCE_UNIT_FISHER_NORMALIZATION_SUPPORT_NOTE_2026-05-25.md"
YT_LSP = DOCS / "YT_LSP_SIGNED_RECORD_SOURCE_READOUT_SUPPORT_NOTE_2026-05-24.md"
YT_NOGO = DOCS / "YT_PRIMITIVE_UNIT_SOURCE_ACTION_PHYSICAL_PREMISE_NO_GO_NOTE_2026-05-25.md"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, ok: bool, detail: Any = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if ok:
        PASS_COUNT += 1
        tag = "PASS"
    else:
        FAIL_COUNT += 1
        tag = "FAIL"
    suffix = f": {detail}" if detail != "" else ""
    print(f"[{tag}] {name}{suffix}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def zero(expr: sp.Expr) -> bool:
    return sp.simplify(expr) == 0


def part1_document_boundary() -> dict[str, Any]:
    print("\nPart 1: document and dependency boundary")
    for path in (NOTE, BOUNDARY, SCALE_PRIMITIVE, PLANCK_UNIT, YT_FISHER, YT_LSP, YT_NOGO):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for phrase in (
        "Theorem",
        "What This Adds To The Boundary",
        "Consequence For Y_T",
        "Remaining Hinge",
        "Claim Boundary",
        "Non-Claims",
    ):
        check(f"note contains required section: {phrase}", phrase in note)

    check("note marks bounded theorem claim type", "claim_type_author_hint: bounded_theorem" in note)
    check("note forbids closure without top-source identification",
          "closure_claim_allowed_without_top_source_identification: false" in note)
    check("note names top-source hinge", "physical top Yukawa deformation" in note)

    boundary = read(BOUNDARY)
    check("boundary exposes lambda family", "lambda" in boundary and "lambda^2" in boundary)
    scale = read(SCALE_PRIMITIVE)
    check("approved scale primitive names Planck anchor", "a^{-1} = M_Pl" in scale)
    planck = read(PLANCK_UNIT)
    check("Planck source-unit support names lambda=1", "lambda = 1" in planck and "G_Newton,lat = 1" in planck)

    return {
        "claim_type_author_hint": "bounded_theorem",
        "depends_on": [
            "approved scale-reference primitive / natural Planck units",
            "finite source-action/RN support",
            "normalized signed-record top source support",
        ],
    }


def part2_action_to_rn_identity() -> dict[str, Any]:
    print("\nPart 2: Planck-action source equals RN natural parameter")
    h, kappa, o = sp.symbols("h kappa o", positive=True)
    s0 = sp.symbols("S0", real=True)
    s_h = s0 - kappa * h * o
    log_weight_ratio = sp.simplify(-(s_h - s0) / kappa)
    check("one Planck-action source gives log weight h O", zero(log_weight_ratio - h * o), log_weight_ratio)
    score = sp.diff(log_weight_ratio, h)
    check("RN score is O", zero(score - o), score)

    lam = sp.symbols("lambda", positive=True)
    s_lam = s0 - kappa * h * lam * o
    log_weight_ratio_lam = sp.simplify(-(s_lam - s0) / kappa)
    score_lam = sp.diff(log_weight_ratio_lam, h)
    check("lambda Planck-action source gives score lambda O", zero(score_lam - lam * o), score_lam)
    check("kappa cancels from dimensionless source coordinate", kappa not in score_lam.free_symbols, score_lam)

    return {
        "unit_action_source": "S_h=S_0-kappa_Pl h O",
        "unit_score": "O",
        "scaled_action_source": "S_h=S_0-kappa_Pl h lambda O",
        "scaled_score": "lambda O",
    }


def part3_binary_fisher_unit() -> dict[str, Any]:
    print("\nPart 3: binary signed-record Fisher unit")
    h, lam = sp.symbols("h lambda", positive=True)
    weights = {1: sp.Rational(1, 2), -1: sp.Rational(1, 2)}

    z = sum(weights[e] * sp.exp(h * e) for e in (-1, 1))
    r = {e: sp.exp(h * e) / z for e in (-1, 1)}
    score = {e: sp.diff(sp.log(r[e]), h).subs(h, 0) for e in (-1, 1)}
    fisher = sp.simplify(sum(weights[e] * score[e] ** 2 for e in (-1, 1)))
    check("unit Planck-action source score is signed record", score[1] == 1 and score[-1] == -1, score)
    check("unit Planck-action source Fisher norm is one", zero(fisher - 1), fisher)

    z_lam = sum(weights[e] * sp.exp(h * lam * e) for e in (-1, 1))
    r_lam = {e: sp.exp(h * lam * e) / z_lam for e in (-1, 1)}
    score_lam = {e: sp.diff(sp.log(r_lam[e]), h).subs(h, 0) for e in (-1, 1)}
    fisher_lam = sp.simplify(sum(weights[e] * score_lam[e] ** 2 for e in (-1, 1)))
    check("lambda-scaled Planck-action score is lambda times record", zero(score_lam[1] - lam) and zero(score_lam[-1] + lam))
    check("lambda-scaled Fisher norm is lambda^2", zero(fisher_lam - lam**2), fisher_lam)
    check("Fisher-unit condition selects lambda=1", sp.solve(sp.Eq(fisher_lam, 1), lam) == [1])

    return {
        "fisher_unit": "one Planck action quantum on signed record",
        "scaled_fisher": "lambda^2",
    }


def part4_six_component_top_consequence() -> dict[str, Any]:
    print("\nPart 4: six-component top source consequence")
    lam = sp.symbols("lambda", positive=True)
    u = sp.Matrix([1 / sp.sqrt(6)] * 6)
    norm = sp.simplify(u.dot(u))
    check("democratic top source has unit norm", zero(norm - 1), norm)
    check("all six components are 1/sqrt(6)", all(zero(component - 1 / sp.sqrt(6)) for component in u))
    fisher_lam = sp.simplify((lam * u).dot(lam * u))
    check("lambda-scaled top Planck-action source has Fisher lambda^2", zero(fisher_lam - lam**2), fisher_lam)
    check("one Planck-action top source selects lambda=1", sp.solve(sp.Eq(fisher_lam, 1), lam) == [1])
    y33 = sp.simplify(u[0])
    check("unit top source component is 1/sqrt(6)", zero(y33 - 1 / sp.sqrt(6)), y33)

    return {
        "top_direction": "(1,1,1,1,1,1)/sqrt(6)",
        "if_one_planck_action_unit": "y_33=1/sqrt(6)",
        "remaining_hinge": "physical top source must be this unit deformation",
    }


def part5_firewall() -> None:
    print("\nPart 5: firewall and overclaim checks")
    note = read(NOTE)
    for phrase in (
        "H_unit",
        "yt_ward_identity",
        "y_t_bare",
        "PDG",
        "alpha_LM",
        "plaquette/u0",
        "fitted selectors",
    ):
        check(f"note names forbidden route: {phrase}", phrase in note)

    for phrase in (
        "full Y_T closure is claimed",
        "closure_claim_allowed_without_top_source_identification: true",
        "old Ward chain is repaired",
        "SI decimal Planck scale is derived",
    ):
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)


def main() -> int:
    print("=" * 88)
    print("SOURCE/MEASURE PLANCK-ACTION RN SOURCE-UNIT BRIDGE")
    print("=" * 88)

    result = {
        "document_boundary": part1_document_boundary(),
        "action_to_rn_identity": part2_action_to_rn_identity(),
        "binary_fisher_unit": part3_binary_fisher_unit(),
        "top_consequence": part4_six_component_top_consequence(),
    }
    part5_firewall()

    result["summary"] = {
        "pass": PASS_COUNT,
        "fail": FAIL_COUNT,
        "claim_type_author_hint": "bounded_theorem",
        "trace_class": "upstream_support",
        "target_blocker": "Planck/action unit equals RN/Fisher source coordinate",
        "partially_closes": [
            "dimensionful source-action unit to RN coordinate",
            "lambda=1 inside one-Planck-action unit top source surface",
        ],
        "remaining_open_for_full_yt": [
            "physical top source equals one-Planck-action unit deformation along O_top",
            "canonical neutral Higgs/source surface and scalar LSZ/pole-row gates",
            "matching/running bridges",
        ],
        "closure_claim_allowed_without_top_source_identification": False,
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("\n" + "=" * 88)
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print(f"Wrote {OUT.relative_to(ROOT)}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
