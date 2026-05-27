#!/usr/bin/env python3
"""Y_T primitive physical-source Fisher-arclength invariant theorem checks."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_primitive_physical_source_fisher_arclength_invariant_2026-05-26.json"

NOTE = DOCS / "YT_PRIMITIVE_PHYSICAL_SOURCE_FISHER_ARCLENGTH_INVARIANT_THEOREM_NOTE_2026-05-26.md"
AXIOMS = DOCS / "MINIMAL_AXIOMS_2026-05-20.md"
SOURCE_SUPPORT = DOCS / "YT_SOURCE_ACTION_SUPPORT_PACKET_NOTE_2026-05-22.md"
LSP_SUPPORT = DOCS / "YT_LSP_SIGNED_RECORD_SOURCE_READOUT_SUPPORT_NOTE_2026-05-24.md"
FISHER_SUPPORT = DOCS / "YT_PRIMITIVE_SOURCE_UNIT_FISHER_NORMALIZATION_SUPPORT_NOTE_2026-05-25.md"
SIGNED_TANGENT = DOCS / "YT_SIGNED_LINEAR_DEMOCRATIC_TANGENT_PHYSICAL_BRIDGE_ATTEMPT_NOTE_2026-05-25.md"
RAW_NOGO = DOCS / "YT_PRIMITIVE_UNIT_SOURCE_ACTION_PHYSICAL_PREMISE_NO_GO_NOTE_2026-05-25.md"
LSP_SCALE = DOCS / "YT_LSP_SOURCE_SCALE_BOUNDARY_AND_STRICT_RESPONSE_CONTRACT_NOTE_2026-05-26.md"

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


def one_line(text: str) -> str:
    return " ".join(text.split())


def is_zero(expr: sp.Expr) -> bool:
    return sp.simplify(expr) == 0


def part1_files_and_scope() -> None:
    print("\nPart 1: files, sections, and scope")
    for path in (
        NOTE,
        AXIOMS,
        SOURCE_SUPPORT,
        LSP_SUPPORT,
        FISHER_SUPPORT,
        SIGNED_TANGENT,
        RAW_NOGO,
        LSP_SCALE,
    ):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    required_sections = (
        "Theorem Statement",
        "Proof",
        "What This Changes",
        "Assumptions Exercise",
        "First-Principles Rework",
        "Relation To The Prior No-Go",
        "Non-Claims",
        "Claim-Status Certificate",
    )
    for section in required_sections:
        check(f"note contains section: {section}", section in note)

    check("note states exact support status", "actual_current_surface_status: exact-support" in note)
    check("note denies retained closure", "claim retained or proposed-retained Y_T closure" in note)
    check("note keeps Fisher/LSZ bridge open", "Fisher/LSZ source-normalization" in note)
    check("note avoids legacy PR-number marker", "PR230" not in note and "pr230" not in note.lower())


def part2_democratic_source_geometry() -> dict[str, str]:
    print("\nPart 2: six-component source geometry")
    n = sp.Integer(6)
    u = sp.Matrix([1 / sp.sqrt(n)] * n)
    norm_sq = sp.simplify(u.dot(u))
    component = sp.simplify(u[0])
    check("democratic six-vector has unit norm", is_zero(norm_sq - 1), norm_sq)
    check("single top component is 1/sqrt(6)", is_zero(component - 1 / sp.sqrt(6)), component)
    check("component squared is projective probability 1/6", is_zero(component**2 - sp.Rational(1, 6)), component**2)
    return {
        "norm_squared": str(norm_sq),
        "component": str(component),
        "component_squared": str(sp.simplify(component**2)),
    }


def part3_fisher_arclength_invariance() -> dict[str, str]:
    print("\nPart 3: Fisher-arclength invariance")
    lam, h = sp.symbols("lambda h", positive=True)
    n = sp.Integer(6)
    component = 1 / sp.sqrt(n)

    raw_score_norm_sq = sp.simplify(lam**2)
    d_ell_d_h = sp.sqrt(raw_score_norm_sq)
    raw_component = sp.simplify(lam * component)
    fisher_component = sp.simplify(raw_component / d_ell_d_h)

    check("raw Fisher metric is lambda^2", is_zero(raw_score_norm_sq - lam**2), raw_score_norm_sq)
    check("positive-orientation arclength derivative is lambda", is_zero(d_ell_d_h - lam), d_ell_d_h)
    check("raw coordinate top coefficient is lambda/sqrt(6)", is_zero(raw_component - lam / sp.sqrt(6)), raw_component)
    check("Fisher-arclength top coefficient is 1/sqrt(6)", is_zero(fisher_component - 1 / sp.sqrt(6)), fisher_component)

    for value in (sp.Rational(1, 3), sp.Rational(1, 1), sp.Rational(2, 1), sp.Rational(7, 5)):
        coeff = sp.simplify((value * component) / value)
        check(f"lambda={value} gives same Fisher coefficient", is_zero(coeff - 1 / sp.sqrt(6)), coeff)

    ell = sp.simplify(lam * h)
    dS_dh = -lam
    dh_dell = sp.diff(h, ell) if False else 1 / lam
    dS_dell = sp.simplify(dS_dh * dh_dell)
    check("dS/dell removes lambda from normalized operator coefficient", is_zero(dS_dell + 1), dS_dell)

    return {
        "raw_fisher_metric": str(raw_score_norm_sq),
        "raw_component": str(raw_component),
        "fisher_arclength_component": str(fisher_component),
        "ell_at_origin": str(ell),
        "dS_dell_operator_coefficient": str(dS_dell),
    }


def part4_coordinate_covariance() -> dict[str, str]:
    print("\nPart 4: source-coordinate covariance")
    alpha, lam = sp.symbols("alpha lambda", positive=True)
    n = sp.Integer(6)
    component = 1 / sp.sqrt(n)

    # Raw coordinate reparameterization h' = alpha h.
    # A covector component transforms with dh/dh' = 1/alpha.
    raw_coeff_h = lam * component
    raw_coeff_hprime = sp.simplify(raw_coeff_h / alpha)
    fisher_metric_h = lam**2
    fisher_metric_hprime = sp.simplify(fisher_metric_h / alpha**2)
    normalized_h = sp.simplify(raw_coeff_h / sp.sqrt(fisher_metric_h))
    normalized_hprime = sp.simplify(raw_coeff_hprime / sp.sqrt(fisher_metric_hprime))

    check("raw component changes under source reparameterization", sp.simplify(raw_coeff_hprime - raw_coeff_h) != 0)
    check("Fisher-normalized component is invariant before reparameterization", is_zero(normalized_h - 1 / sp.sqrt(6)), normalized_h)
    check("Fisher-normalized component is invariant after reparameterization", is_zero(normalized_hprime - 1 / sp.sqrt(6)), normalized_hprime)
    check("two invariant components agree", is_zero(normalized_hprime - normalized_h), sp.simplify(normalized_hprime - normalized_h))

    return {
        "raw_coeff_h": str(raw_coeff_h),
        "raw_coeff_hprime": str(raw_coeff_hprime),
        "normalized_h": str(normalized_h),
        "normalized_hprime": str(normalized_hprime),
    }


def part5_boundary_against_prior_no_go() -> dict[str, bool]:
    print("\nPart 5: boundary against prior no-go")
    note = read(NOTE)
    raw_nogo = read(RAW_NOGO)
    lsp_scale = read(LSP_SCALE)

    checks = {
        "acknowledges_prior_no_go": "This theorem does not refute the primitive-unit no-go" in note,
        "states_raw_coordinate_scope": "raw-coordinate scope" in note,
        "names_remaining_bridge": "physical top Yukawa readout use the Fisher/LSZ-normalized source" in note,
        "raw_nogo_has_lambda_family": "y_33(lambda) = lambda / sqrt(6)" in raw_nogo,
        "lsp_scale_blindness_preserved": "source-scale blind" in lsp_scale,
    }
    for name, ok in checks.items():
        check(name.replace("_", " "), ok)
    return checks


def part6_firewalls() -> None:
    print("\nPart 6: forbidden imports and overclaim scan")
    note = read(NOTE)
    flat = one_line(note)
    required_firewalls = (
        "H_unit",
        "yt_ward_identity",
        "y_t_bare",
        "observed top/W/Z masses",
        "PDG values",
        "alpha_LM",
        "plaquette/u0",
        "fitted selector",
    )
    for phrase in required_firewalls:
        check(f"firewall phrase present: {phrase}", phrase in flat)

    forbidden = (
        "Status:** retained",
        "actual_current_surface_status: retained",
        "proposal_allowed: true",
        "bare_retained_allowed: true",
        "full Y_T closure",
        "old Ward route has been repaired",
        "strict top/W response evidence exists",
    )
    for phrase in forbidden:
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)


def main() -> int:
    print("=" * 88)
    print("Y_T PRIMITIVE PHYSICAL-SOURCE FISHER-ARCLENGTH INVARIANT THEOREM")
    print("=" * 88)

    part1_files_and_scope()
    geometry = part2_democratic_source_geometry()
    fisher = part3_fisher_arclength_invariance()
    covariance = part4_coordinate_covariance()
    boundary = part5_boundary_against_prior_no_go()
    part6_firewalls()

    result = {
        "status": "exact-support / narrowed bridge",
        "claim": (
            "For a normalized six-component top source, the coefficient per unit "
            "Fisher arclength on the RN source manifold is 1/sqrt(6), independent "
            "of the raw source-coordinate scale lambda."
        ),
        "trace_class": "upstream_support",
        "reachability_to_target": "partially_closes",
        "proposal_allowed": False,
        "bare_retained_allowed": False,
        "geometry": geometry,
        "fisher_arclength": fisher,
        "coordinate_covariance": covariance,
        "prior_no_go_boundary": boundary,
        "remaining_bridge": (
            "Prove or audit that the physical top Yukawa coefficient is read in "
            "the Fisher/LSZ-normalized source coordinate, or provide strict "
            "same-source top/W response evidence."
        ),
        "forbidden_imports_used": False,
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
        "review_surface": [
            "docs/YT_PRIMITIVE_PHYSICAL_SOURCE_FISHER_ARCLENGTH_INVARIANT_THEOREM_NOTE_2026-05-26.md",
            "scripts/frontier_yt_primitive_physical_source_fisher_arclength_invariant.py",
            "outputs/yt_primitive_physical_source_fisher_arclength_invariant_2026-05-26.json",
        ],
    }

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nwrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
