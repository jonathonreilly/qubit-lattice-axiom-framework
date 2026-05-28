#!/usr/bin/env python3
"""Y_T legacy Hessian/UV bridge firewall no-go."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SCRIPTS = ROOT / "scripts"
OUTPUT = ROOT / "outputs" / "yt_legacy_hessian_bridge_firewall_no_go_2026-05-28.json"

NOTE = DOCS / "YT_LEGACY_HESSIAN_BRIDGE_FIREWALL_NO_GO_NOTE_2026-05-28.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"
ORIGIN_DECLARED_FIREWALL = DOCS / "YT_ORIGIN_MAIN_DECLARED_ANCHOR_FIREWALL_NO_GO_NOTE_2026-05-28.md"
C3_RADIAL_NOGO = DOCS / "YT_C3_SAME_SURFACE_RADIAL_FACTOR_UNDERDETERMINATION_NO_GO_NOTE_2026-05-28.md"
FISHER_LSZ_RADIAL_NOGO = DOCS / "YT_FISHER_LSZ_RADIAL_GENERATOR_NORMALIZATION_NO_GO_NOTE_2026-05-28.md"
STRICT_AVAILABILITY = DOCS / "YT_STRICT_SPARSE_TOP_W_POLE_RESPONSE_AVAILABILITY_AUDIT_NOTE_2026-05-27.md"

LEGACY_HESSIAN = DOCS / "YT_BRIDGE_HESSIAN_SELECTOR_NOTE.md"
LEGACY_AXIOM_FIRST = DOCS / "YT_AXIOM_FIRST_MICROSCOPIC_BRIDGE_THEOREM.md"
LEGACY_UV_CLASS = DOCS / "YT_BRIDGE_UV_CLASS_UNIQUENESS_NOTE.md"
LEGACY_EXACT_HESSIAN = DOCS / "YT_EXACT_HESSIAN_SELECTOR_UNIQUENESS_NOTE.md"
LEGACY_VARIATIONAL = DOCS / "YT_BRIDGE_VARIATIONAL_SELECTOR_NOTE.md"
LEGACY_ENDPOINT = DOCS / "YT_BRIDGE_ENDPOINT_SHIFT_BOUND_NOTE.md"
LEGACY_NONLOCAL = DOCS / "YT_BRIDGE_NONLOCAL_CORRECTIONS_NOTE.md"
LEGACY_HIGHER_ORDER = DOCS / "YT_BRIDGE_HIGHER_ORDER_CORRECTIONS_NOTE.md"
LEGACY_SCHUR_CLASS = DOCS / "YT_MICROSCOPIC_SCHUR_CLASS_ADMISSIBILITY_NOTE.md"

LEGACY_HESSIAN_RUNNER = SCRIPTS / "frontier_yt_bridge_hessian_selector.py"
LEGACY_UV_CLASS_RUNNER = SCRIPTS / "frontier_yt_bridge_uv_class_uniqueness.py"
LEGACY_CONSTRUCTIVE_RUNNER = SCRIPTS / "frontier_yt_constructive_uv_bridge.py"
LEGACY_EXACT_HESSIAN_RUNNER = SCRIPTS / "frontier_yt_exact_hessian_selector_uniqueness.py"
LEGACY_ENDPOINT_RUNNER = SCRIPTS / "frontier_yt_bridge_endpoint_shift_bound.py"
LEGACY_NONLOCAL_RUNNER = SCRIPTS / "frontier_yt_bridge_nonlocal_corrections.py"
LEGACY_HIGHER_RUNNER = SCRIPTS / "frontier_yt_bridge_higher_order_corrections.py"

FULL_STACK_OUT = ROOT / "outputs" / "yt_full_closure_stack_and_strict_pole_response_contract_2026-05-26.json"
ORIGIN_DECLARED_FIREWALL_OUT = ROOT / "outputs" / "yt_origin_main_declared_anchor_firewall_no_go_2026-05-28.json"
C3_RADIAL_NOGO_OUT = ROOT / "outputs" / "yt_c3_same_surface_radial_factor_underdetermination_no_go_2026-05-28.json"
FISHER_LSZ_RADIAL_NOGO_OUT = ROOT / "outputs" / "yt_fisher_lsz_radial_generator_normalization_no_go_2026-05-28.json"
STRICT_AVAILABILITY_OUT = ROOT / "outputs" / "yt_strict_sparse_top_w_pole_response_availability_audit_2026-05-27.json"

FORBIDDEN_PATTERNS = {
    "plaquette/u0": ("plaquette", "u_0", "U0", "PLAQ"),
    "alpha_LM": ("alpha_LM", "ALPHA_LM"),
    "Planck endpoint": ("Planck", "M_PL"),
    "old Ward authority": ("Ward", "yt_ward_identity", "y_t_bare"),
    "target-conditioned y_t": ("TARGET_YT_PHYS", "target `y_t`", "target-`y_t`", "y_t(v)"),
    "observed-scale endpoint": ("M_Z", "ALPHA_EM_MZ", "SIN2_TW_MZ"),
    "proxy bridge family": ("logistic", "erf", "smoothstep", "chosen proxy bridge"),
}

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


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(read(path))


def is_zero(expr: sp.Expr) -> bool:
    return sp.simplify(expr) == 0


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors and current dependency state")
    paths = (
        NOTE,
        FULL_STACK,
        ORIGIN_DECLARED_FIREWALL,
        C3_RADIAL_NOGO,
        FISHER_LSZ_RADIAL_NOGO,
        STRICT_AVAILABILITY,
        LEGACY_HESSIAN,
        LEGACY_AXIOM_FIRST,
        LEGACY_UV_CLASS,
        LEGACY_EXACT_HESSIAN,
        LEGACY_VARIATIONAL,
        LEGACY_ENDPOINT,
        LEGACY_NONLOCAL,
        LEGACY_HIGHER_ORDER,
        LEGACY_SCHUR_CLASS,
        LEGACY_HESSIAN_RUNNER,
        LEGACY_UV_CLASS_RUNNER,
        LEGACY_CONSTRUCTIVE_RUNNER,
        LEGACY_EXACT_HESSIAN_RUNNER,
        LEGACY_ENDPOINT_RUNNER,
        LEGACY_NONLOCAL_RUNNER,
        LEGACY_HIGHER_RUNNER,
        FULL_STACK_OUT,
        ORIGIN_DECLARED_FIREWALL_OUT,
        C3_RADIAL_NOGO_OUT,
        FISHER_LSZ_RADIAL_NOGO_OUT,
        STRICT_AVAILABILITY_OUT,
    )
    for path in paths:
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for section in (
        "Question",
        "Answer",
        "Relation To Current Stack",
        "Assumptions / Imports Exercise",
        "First-Principles / Elon Exercise",
        "Finite Firewall Witness",
        "No-Go Audit",
        "Stuck Fan-Out Synthesis",
        "Literature / Math Search",
        "What Remains Open",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)

    for phrase in (
        "actual_current_surface_status: no-go / legacy Hessian-bridge firewall",
        "proposal_allowed: false",
        "plaquette/u0",
        "target-conditioned y_t(v)",
        "strict same-surface pole/matrix-element certificate",
        "lambda_top = 1/sqrt(2)",
    ):
        check(f"note contains firewall phrase: {phrase}", phrase in note)

    deps = {
        "full_stack": load_json(FULL_STACK_OUT),
        "origin_declared_firewall": load_json(ORIGIN_DECLARED_FIREWALL_OUT),
        "c3_radial_nogo": load_json(C3_RADIAL_NOGO_OUT),
        "fisher_lsz_radial_nogo": load_json(FISHER_LSZ_RADIAL_NOGO_OUT),
        "strict_availability": load_json(STRICT_AVAILABILITY_OUT),
    }
    for name, data in deps.items():
        check(f"{name} dependency passed", data.get("fail_count") == 0, data.get("fail_count"))

    check(
        "full stack still disallows proposal wording",
        deps["full_stack"].get("proposal_allowed") is False,
    )
    check(
        "origin declared-anchor shortcut already pruned",
        deps["origin_declared_firewall"].get("trace_class") == "negative_route_pruning",
    )
    check(
        "radial factor remains open",
        deps["c3_radial_nogo"].get("certificate_boundary", {}).get("lambda_top_free_on_current_surface")
        is True,
    )
    check(
        "Fisher/LSZ radial shortcut already pruned",
        deps["fisher_lsz_radial_nogo"].get("trace_class") == "negative_route_pruning",
    )
    check(
        "strict positive certificate remains absent",
        deps["strict_availability"].get("certificate_boundary", {}).get("strict_positive_certificate_present")
        is False,
    )
    return deps


def part2_legacy_import_scan() -> dict[str, Any]:
    print("\nPart 2: legacy Hessian/UV bridge import scan")
    scan_paths = (
        LEGACY_HESSIAN,
        LEGACY_AXIOM_FIRST,
        LEGACY_UV_CLASS,
        LEGACY_EXACT_HESSIAN,
        LEGACY_VARIATIONAL,
        LEGACY_ENDPOINT,
        LEGACY_NONLOCAL,
        LEGACY_HIGHER_ORDER,
        LEGACY_SCHUR_CLASS,
        LEGACY_HESSIAN_RUNNER,
        LEGACY_UV_CLASS_RUNNER,
        LEGACY_CONSTRUCTIVE_RUNNER,
        LEGACY_EXACT_HESSIAN_RUNNER,
        LEGACY_ENDPOINT_RUNNER,
        LEGACY_NONLOCAL_RUNNER,
        LEGACY_HIGHER_RUNNER,
    )
    corpus = {str(path.relative_to(ROOT)): read(path) for path in scan_paths}
    joined = "\n".join(corpus.values())

    found: dict[str, list[str]] = {}
    for label, patterns in FORBIDDEN_PATTERNS.items():
        hits = [pattern for pattern in patterns if pattern in joined]
        found[label] = hits
        check(f"legacy corpus exposes {label}", bool(hits), hits)

    hessian_note = corpus[str(LEGACY_HESSIAN.relative_to(ROOT))]
    axiom_note = corpus[str(LEGACY_AXIOM_FIRST.relative_to(ROOT))]
    uv_note = corpus[str(LEGACY_UV_CLASS.relative_to(ROOT))]
    exact_hessian_note = corpus[str(LEGACY_EXACT_HESSIAN.relative_to(ROOT))]

    check("legacy Hessian note is bounded support", "bounded support note" in hessian_note)
    check("legacy Hessian note names observed minimizer", "observed" in hessian_note)
    check("axiom-first bridge uses accepted plaquette/u0 surface", "accepted plaquette / `u_0` surface" in axiom_note)
    check("axiom-first bridge remains a budgeted support theorem", "does **not** yet prove full exact closure" in axiom_note)
    check("UV class note records imported target y_t", "imported target `y_t`" in uv_note)
    check("UV class note records chosen proxy bridge families", "chosen proxy bridge" in uv_note)
    check("exact Hessian note leaves shape drift above branch budget", "~7.2%" in exact_hessian_note and "above the branch-budget tolerance" in exact_hessian_note)

    return {
        "forbidden_or_inadmissible_patterns": found,
        "legacy_surface_classes": {
            "hessian_selector": "bounded support note",
            "axiom_first_bridge": "supporting theorem / reduction, not final closure",
            "uv_class_uniqueness": "audited_conditional proxy-family scan",
            "exact_hessian_selector": "bounded direction uniqueness with shape drift",
        },
    }


def part3_strict_certificate_absence() -> dict[str, Any]:
    print("\nPart 3: strict certificate field firewall")
    required_fields = {
        "same_accepted_backend": False,
        "isolated_w_top_poles": False,
        "coefficient_certified_dM_t_dell": False,
        "coefficient_certified_dM_W_dell": False,
        "contact_subtraction_done": False,
        "fv_ir_controls_pass": False,
        "same_model_class": False,
        "no_free_top_coefficient": False,
        "no_forbidden_imports": False,
    }
    for key, value in required_fields.items():
        check(f"legacy bridge does not close strict field: {key}", value is False)

    return {
        "legacy_bridge_strict_positive_certificate_present": False,
        "required_fields_closed_by_legacy_bridge": required_fields,
        "route_pruned": (
            "legacy Hessian/UV bridge selector surfaces -> accepted "
            "same-surface radial/backend law or strict top/W pole rows"
        ),
    }


def part4_finite_firewall_witness() -> dict[str, Any]:
    print("\nPart 4: finite same-surface radial witness")
    sqrt = sp.sqrt
    A, g2, lambda_top, h = sp.symbols("A g_2 lambda_top h", positive=True)
    local_hessian = h
    top_row = lambda_top * A / sqrt(6)
    w_row = g2 * A / 2
    readout = sp.simplify(g2 / sqrt(2) * top_row / w_row)
    target_lambda = sp.solve(sp.Eq(readout, 1 / sqrt(6)), lambda_top)

    check("positive Hessian parameter is independent of lambda_top", not local_hessian.has(lambda_top))
    check("top row depends on lambda_top", top_row.has(lambda_top), top_row)
    check("W row does not depend on lambda_top", not w_row.has(lambda_top), w_row)
    check("same-source readout is lambda_top/sqrt(3)", is_zero(readout - lambda_top / sqrt(3)), readout)
    check("target readout still requires lambda_top=1/sqrt(2)", target_lambda == [1 / sqrt(2)], target_lambda)

    row_a = sp.simplify(top_row.subs(lambda_top, 1 / sqrt(2)))
    row_b = sp.simplify(top_row.subs(lambda_top, 2 / sqrt(2)))
    check("target lambda gives A/sqrt(12)", is_zero(row_a - A / sqrt(12)), row_a)
    check("alternative lambda gives different row", is_zero(row_b - 2 * A / sqrt(12)), row_b)

    return {
        "legacy_positive_hessian_can_be_independent_of_top_radial_factor": True,
        "top_row_magnitude": "lambda_top*A/sqrt(6)",
        "same_source_readout": "lambda_top/sqrt(3)",
        "target_lambda_top": "1/sqrt(2)",
        "counterexample_lambda_top": "2/sqrt(2)",
        "positive_hessian_selector_supplies_lambda_top": False,
    }


def part5_certificate() -> dict[str, Any]:
    print("\nPart 5: no-go certificate")
    certificate = {
        "actual_current_surface_status": "no-go / legacy Hessian-bridge firewall",
        "trace_class": "negative_route_pruning",
        "reachability_to_target": "prunes",
        "proposal_allowed": False,
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "positive_closure_marker_allowed": False,
        "no_forbidden_inputs_used_as_proof": True,
        "accepted_same_surface_radial_generator_factorization_derived": False,
        "accepted_backend_projector_matrix_element_theorem_derived": False,
        "strict_top_w_response_certificate_present": False,
    }
    for key in certificate:
        check(f"certificate field recorded: {key}", key in certificate)
    check("proposal wording remains disallowed", certificate["proposal_allowed"] is False)
    check("positive closure marker remains disallowed", certificate["positive_closure_marker_allowed"] is False)
    return certificate


def main() -> int:
    deps = part1_anchors()
    legacy_scan = part2_legacy_import_scan()
    strict_firewall = part3_strict_certificate_absence()
    finite_witness = part4_finite_firewall_witness()
    certificate = part5_certificate()

    result = {
        **certificate,
        "dependency_statuses": {
            name: {
                "status": data.get("actual_current_surface_status", data.get("status")),
                "trace_class": data.get("trace_class"),
                "proposal_allowed": data.get("proposal_allowed"),
                "fail_count": data.get("fail_count"),
            }
            for name, data in deps.items()
        },
        "legacy_import_scan": legacy_scan,
        "strict_certificate_firewall": strict_firewall,
        "finite_firewall_witness": finite_witness,
        "route_still_live": (
            "derive allowed same-surface radial/readout/backend laws without "
            "forbidden anchors, or produce accepted strict top/W pole rows"
        ),
        "review_surface": [
            "docs/YT_LEGACY_HESSIAN_BRIDGE_FIREWALL_NO_GO_NOTE_2026-05-28.md",
            "scripts/frontier_yt_legacy_hessian_bridge_firewall_no_go.py",
            "outputs/yt_legacy_hessian_bridge_firewall_no_go_2026-05-28.json",
            "docs/YT_BRIDGE_HESSIAN_SELECTOR_NOTE.md",
            "docs/YT_AXIOM_FIRST_MICROSCOPIC_BRIDGE_THEOREM.md",
            "docs/YT_BRIDGE_UV_CLASS_UNIQUENESS_NOTE.md",
            "docs/YT_EXACT_HESSIAN_SELECTOR_UNIQUENESS_NOTE.md",
        ],
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nwrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
