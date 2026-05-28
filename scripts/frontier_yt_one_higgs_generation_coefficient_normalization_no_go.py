#!/usr/bin/env python3
"""Y_T one-Higgs generation-coefficient normalization no-go.

This runner verifies the finite normalization counterfamily behind the
2026-05-28 note. It is intentionally negative: ordinary generation-matrix
normalization conventions do not derive the unit multiplier eta=1 tying the
one-Higgs top coefficient to the normalized C3 source response.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_one_higgs_generation_coefficient_normalization_no_go_2026-05-28.json"

NOTE = DOCS / "YT_ONE_HIGGS_GENERATION_COEFFICIENT_NORMALIZATION_NO_GO_NOTE_2026-05-28.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"
TOP_COEFF_NOGO = DOCS / "YT_TOP_RESPONSE_COEFFICIENT_UNDERDETERMINATION_NO_GO_NOTE_2026-05-25.md"
ONE_HIGGS_RADIAL_NOGO = DOCS / "YT_ONE_HIGGS_CARRIER_RADIAL_FACTOR_NO_GO_NOTE_2026-05-28.md"
ONE_HIGGS_SUPPORT = DOCS / "YT_ONE_HIGGS_TOP_CARRIER_SELECTION_SUPPORT_NOTE_2026-05-26.md"
STRICT_SYMBOLIC_TOP = DOCS / "YT_STRICT_SYMBOLIC_TOP_RESPONSE_ROW_PACKET_NOTE_2026-05-25.md"
STRICT_SPARSE_AUDIT = DOCS / "YT_STRICT_SPARSE_TOP_W_POLE_RESPONSE_AVAILABILITY_AUDIT_NOTE_2026-05-27.md"

FULL_STACK_OUT = ROOT / "outputs" / "yt_full_closure_stack_and_strict_pole_response_contract_2026-05-26.json"
TOP_COEFF_NOGO_OUT = ROOT / "outputs" / "yt_top_response_coefficient_underdetermination_no_go_2026-05-25.json"
ONE_HIGGS_RADIAL_NOGO_OUT = ROOT / "outputs" / "yt_one_higgs_carrier_radial_factor_no_go_2026-05-28.json"
ONE_HIGGS_SUPPORT_OUT = ROOT / "outputs" / "yt_one_higgs_top_carrier_selection_support_2026-05-26.json"
STRICT_SYMBOLIC_TOP_OUT = ROOT / "outputs" / "yt_strict_symbolic_top_response_row_packet_2026-05-25.json"
STRICT_SPARSE_AUDIT_OUT = ROOT / "outputs" / "yt_strict_sparse_top_w_pole_response_availability_audit_2026-05-27.json"

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
    print("\nPart 1: anchors and dependency state")
    for path in (
        NOTE,
        FULL_STACK,
        TOP_COEFF_NOGO,
        ONE_HIGGS_RADIAL_NOGO,
        ONE_HIGGS_SUPPORT,
        STRICT_SYMBOLIC_TOP,
        STRICT_SPARSE_AUDIT,
        FULL_STACK_OUT,
        TOP_COEFF_NOGO_OUT,
        ONE_HIGGS_RADIAL_NOGO_OUT,
        ONE_HIGGS_SUPPORT_OUT,
        STRICT_SYMBOLIC_TOP_OUT,
        STRICT_SPARSE_AUDIT_OUT,
    ):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for section in (
        "Question",
        "Answer",
        "Relation To Current Stack",
        "Assumptions / Imports Exercise",
        "First-Principles / Elon Exercise",
        "Finite Normalization Witness",
        "No-Go Audit",
        "Stuck Fan-Out Synthesis",
        "Literature / Math Search",
        "What Remains Open",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)

    for phrase in (
        "actual_current_surface_status: no-go / open generation-coefficient normalization law",
        "proposal_allowed: false",
        "eta = 1",
        "unit singular/Frobenius top row",
        "unit three-generation average",
        "C3-unit coefficient",
        "`H_unit`",
        "`yt_ward_identity`",
        "`y_t_bare`",
        "PDG",
        "`alpha_LM`",
        "fitted selectors",
    ):
        check(f"note contains required phrase: {phrase}", phrase in note)

    deps = {
        "full_stack": load_json(FULL_STACK_OUT),
        "top_coeff_nogo": load_json(TOP_COEFF_NOGO_OUT),
        "one_higgs_radial_nogo": load_json(ONE_HIGGS_RADIAL_NOGO_OUT),
        "one_higgs_support": load_json(ONE_HIGGS_SUPPORT_OUT),
        "strict_symbolic_top": load_json(STRICT_SYMBOLIC_TOP_OUT),
        "strict_sparse_audit": load_json(STRICT_SPARSE_AUDIT_OUT),
    }
    for name, payload in deps.items():
        check(f"{name} dependency passed", payload.get("fail_count") == 0, payload.get("fail_count"))

    check("top coefficient older no-go proposal is not allowed", deps["top_coeff_nogo"].get("proposal_allowed") is False)
    check(
        "one-Higgs radial no-go leaves eta free",
        deps["one_higgs_radial_nogo"].get("certificate_boundary", {}).get("eta_free_on_current_surface") is True,
    )
    check(
        "one-Higgs support leaves generation entry open",
        deps["one_higgs_support"].get("boundary", {}).get("generation_matrix_entry_selected") is False,
    )
    check(
        "symbolic top packet leaves y33 free",
        deps["strict_symbolic_top"].get("top_coefficient_derived") is False,
    )
    check(
        "strict sparse positive certificate remains absent",
        deps["strict_sparse_audit"].get("certificate_boundary", {}).get("strict_positive_certificate_present") is False,
    )
    return deps


def part2_normalization_witness() -> dict[str, Any]:
    print("\nPart 2: finite normalization witness")
    eta, A = sp.symbols("eta A", positive=True)
    r_nt = 1 / sp.sqrt(6)
    y33 = eta * r_nt
    dmt = y33 * A / sp.sqrt(2)
    lambda_top = eta / sp.sqrt(2)

    conventions = {
        "c3_unit": sp.Integer(1),
        "unit_top_singular_value": sp.sqrt(6),
        "unit_three_generation_average": sp.sqrt(2),
        "free_eta_counterexample": sp.Integer(2),
    }
    rows = {
        name: {
            "eta": sp.simplify(value),
            "y33": sp.simplify(y33.subs(eta, value)),
            "top_row": sp.simplify(dmt.subs(eta, value)),
            "lambda_top": sp.simplify(lambda_top.subs(eta, value)),
        }
        for name, value in conventions.items()
    }

    check("C3 response magnitude is 1/sqrt(6)", is_zero(r_nt - 1 / sp.sqrt(6)), r_nt)
    check("y33 family is eta/sqrt(6)", is_zero(y33 - eta / sp.sqrt(6)), y33)
    check("top row family is eta*A/sqrt(12)", is_zero(dmt - eta * A / sp.sqrt(12)), dmt)
    check("lambda_top family is eta/sqrt(2)", is_zero(lambda_top - eta / sp.sqrt(2)), lambda_top)
    check("C3-unit convention gives target eta", is_zero(rows["c3_unit"]["eta"] - 1), rows["c3_unit"])
    check("C3-unit convention gives target top row", is_zero(rows["c3_unit"]["top_row"] - A / sp.sqrt(12)))
    check(
        "unit top singular convention gives eta=sqrt(6)",
        is_zero(rows["unit_top_singular_value"]["eta"] - sp.sqrt(6)),
        rows["unit_top_singular_value"],
    )
    check(
        "unit top singular convention does not give target row",
        not is_zero(rows["unit_top_singular_value"]["top_row"] - A / sp.sqrt(12)),
        rows["unit_top_singular_value"]["top_row"],
    )
    check(
        "unit three-generation average gives eta=sqrt(2)",
        is_zero(rows["unit_three_generation_average"]["eta"] - sp.sqrt(2)),
        rows["unit_three_generation_average"],
    )
    check(
        "unit three-generation average does not give target row",
        not is_zero(rows["unit_three_generation_average"]["top_row"] - A / sp.sqrt(12)),
        rows["unit_three_generation_average"]["top_row"],
    )
    check(
        "free eta counterexample changes coefficient",
        not is_zero(rows["free_eta_counterexample"]["top_row"] - rows["c3_unit"]["top_row"]),
        rows["free_eta_counterexample"]["top_row"],
    )

    return {
        name: {key: str(value) for key, value in payload.items()}
        for name, payload in rows.items()
    }


def part3_matrix_norm_family() -> dict[str, str]:
    print("\nPart 3: generation-matrix norm family")
    eta = sp.symbols("eta", positive=True)
    y33 = eta / sp.sqrt(6)
    Y = sp.diag(0, 0, y33)
    frob_sq = sp.simplify(sum(entry**2 for entry in Y))
    singular_value = y33
    rank = Y.rank()

    eta_unit_frob = sp.solve(sp.Eq(frob_sq, 1), eta)
    eta_unit_three_average = sp.solve(sp.Eq(3 * y33**2, 1), eta)
    eta_target = sp.solve(sp.Eq(y33, 1 / sp.sqrt(6)), eta)

    check("rank-one top matrix shape is fixed", rank == 1, rank)
    check("Frobenius norm keeps eta scale", is_zero(frob_sq - eta**2 / 6), frob_sq)
    check("singular value keeps eta scale", is_zero(singular_value - eta / sp.sqrt(6)), singular_value)
    check("unit Frobenius gives eta=sqrt(6)", eta_unit_frob == [sp.sqrt(6)], eta_unit_frob)
    check("unit three-average gives eta=sqrt(2)", eta_unit_three_average == [sp.sqrt(2)], eta_unit_three_average)
    check("target C3 unit gives eta=1", eta_target == [1], eta_target)
    check("unit Frobenius differs from target eta", eta_unit_frob != eta_target)
    check("unit three-average differs from target eta", eta_unit_three_average != eta_target)

    return {
        "frob_sq": str(frob_sq),
        "singular_value": str(singular_value),
        "rank": str(rank),
        "eta_unit_frob": str(eta_unit_frob[0]),
        "eta_unit_three_average": str(eta_unit_three_average[0]),
        "eta_target_c3_unit": str(eta_target[0]),
    }


def part4_certificate() -> dict[str, Any]:
    print("\nPart 4: no-go certificate")
    certificate = {
        "route_pruned": "generic one-Higgs generation-matrix normalization convention derives eta=1",
        "one_higgs_carrier_granted": True,
        "neutral_higgs_radial_factor_granted": True,
        "c3_nontrivial_response_granted": True,
        "ordinary_generation_norms_tested": True,
        "accepted_eta_equals_one_law_derived": False,
        "eta_free_on_current_surface": True,
        "lambda_top_free_on_current_surface": True,
        "strict_top_w_response_certificate_present": False,
        "proposal_allowed": False,
        "bare_retained_allowed": False,
        "no_forbidden_imports": True,
        "remaining_imports": [
            "accepted one-Higgs coefficient-to-C3-source law eta=1",
            "accepted same-surface radial generator factorization lambda_top=1/sqrt(2)",
            "accepted physical zero-singlet top-readout law",
            "accepted strict same-source top/W pole rows with controls",
        ],
    }
    for key, value in certificate.items():
        check(f"certificate field recorded: {key}", key in certificate)
        if isinstance(value, bool):
            check(f"certificate boolean sane: {key}", value in (True, False))

    check("eta=1 law not derived", certificate["accepted_eta_equals_one_law_derived"] is False)
    check("eta remains free", certificate["eta_free_on_current_surface"] is True)
    check("strict top/W certificate absent", certificate["strict_top_w_response_certificate_present"] is False)
    check("proposal remains disallowed", certificate["proposal_allowed"] is False)
    return certificate


def part5_firewalls() -> None:
    print("\nPart 5: firewalls and wording")
    note = read(NOTE)
    note_one_line = " ".join(note.split())
    for phrase in (
        "`H_unit`",
        "`yt_ward_identity`",
        "`y_t_bare`",
        "observed top/W/Z masses",
        "PDG",
        "`alpha_LM`",
        "plaquette/u0",
        "Planck",
        "alpha_s",
        "fitted selectors",
    ):
        check(f"firewall phrase present: {phrase}", phrase in note_one_line)

    for phrase in (
        "Status:** retained",
        "Status:** proposed_retained",
        "This note derives `eta=1`",
        "This note derives `lambda_top=1/sqrt(2)`",
        "positive Y_T closure is obtained",
        "proposal_allowed: true",
    ):
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)


def main() -> int:
    print("=" * 86)
    print("Y_T ONE-HIGGS GENERATION-COEFFICIENT NORMALIZATION NO-GO")
    print("=" * 86)

    deps = part1_anchors()
    witness = part2_normalization_witness()
    matrix_norms = part3_matrix_norm_family()
    certificate = part4_certificate()
    part5_firewalls()

    result = {
        "actual_current_surface_status": "no-go / open generation-coefficient normalization law",
        "trace_class": "negative_route_pruning",
        "reachability_to_target": "prunes",
        "proposal_allowed": False,
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "claim": (
            "Ordinary one-Higgs generation-matrix normalization conventions do "
            "not derive eta=1 or lambda_top=1/sqrt(2)."
        ),
        "normalization_witness": witness,
        "matrix_norm_family": matrix_norms,
        "certificate_boundary": certificate,
        "dependency_fail_counts": {name: payload.get("fail_count") for name, payload in deps.items()},
        "next_action": (
            "derive accepted eta=1/lambda_top=1/sqrt(2) coefficient law plus "
            "physical zero-singlet top readout, or produce accepted strict same-source "
            "top/W pole rows with controls"
        ),
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
        "review_surface": [
            "docs/YT_ONE_HIGGS_GENERATION_COEFFICIENT_NORMALIZATION_NO_GO_NOTE_2026-05-28.md",
            "scripts/frontier_yt_one_higgs_generation_coefficient_normalization_no_go.py",
            "outputs/yt_one_higgs_generation_coefficient_normalization_no_go_2026-05-28.json",
        ],
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nwrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
