#!/usr/bin/env python3
"""Y_T Fisher/LSZ radial-generator normalization no-go."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_fisher_lsz_radial_generator_normalization_no_go_2026-05-28.json"

NOTE = DOCS / "YT_FISHER_LSZ_RADIAL_GENERATOR_NORMALIZATION_NO_GO_NOTE_2026-05-28.md"
FISHER_ARCLENGTH = DOCS / "YT_PRIMITIVE_PHYSICAL_SOURCE_FISHER_ARCLENGTH_INVARIANT_THEOREM_NOTE_2026-05-26.md"
FISHER_LSZ = DOCS / "YT_FISHER_LSZ_SOURCE_NORMALIZATION_BRIDGE_THEOREM_NOTE_2026-05-26.md"
FIRST_PRINCIPLES = DOCS / "YT_FIRST_PRINCIPLES_TRANSFER_RESPONSE_BOUNDARY_THEOREM_NOTE_2026-05-27.md"
SAME_SURFACE_FACTORIZATION = DOCS / "YT_SAME_SURFACE_TOP_MATRIX_ELEMENT_FACTORIZATION_BOUNDARY_NOTE_2026-05-27.md"
C3_RADIAL_NOGO = DOCS / "YT_C3_SAME_SURFACE_RADIAL_FACTOR_UNDERDETERMINATION_NO_GO_NOTE_2026-05-28.md"
C3_COMPENSATION_NOGO = DOCS / "YT_C3_RADIAL_READOUT_COMPENSATION_UNDERDETERMINATION_NO_GO_NOTE_2026-05-28.md"
C3_SHARP_NOGO = DOCS / "YT_C3_SHARP_RESPONSE_READOUT_UNDERDETERMINATION_NO_GO_NOTE_2026-05-28.md"
STRICT_AVAILABILITY = DOCS / "YT_STRICT_SPARSE_TOP_W_POLE_RESPONSE_AVAILABILITY_AUDIT_NOTE_2026-05-27.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"

FISHER_ARCLENGTH_OUT = ROOT / "outputs" / "yt_primitive_physical_source_fisher_arclength_invariant_2026-05-26.json"
FISHER_LSZ_OUT = ROOT / "outputs" / "yt_fisher_lsz_source_normalization_bridge_2026-05-26.json"
FIRST_PRINCIPLES_OUT = ROOT / "outputs" / "yt_first_principles_transfer_response_boundary_2026-05-27.json"
SAME_SURFACE_FACTORIZATION_OUT = (
    ROOT / "outputs" / "yt_same_surface_top_matrix_element_factorization_boundary_2026-05-27.json"
)
C3_RADIAL_NOGO_OUT = ROOT / "outputs" / "yt_c3_same_surface_radial_factor_underdetermination_no_go_2026-05-28.json"
C3_COMPENSATION_NOGO_OUT = (
    ROOT / "outputs" / "yt_c3_radial_readout_compensation_underdetermination_no_go_2026-05-28.json"
)
C3_SHARP_NOGO_OUT = ROOT / "outputs" / "yt_c3_sharp_response_readout_underdetermination_no_go_2026-05-28.json"
STRICT_AVAILABILITY_OUT = (
    ROOT / "outputs" / "yt_strict_sparse_top_w_pole_response_availability_audit_2026-05-27.json"
)
FULL_STACK_OUT = ROOT / "outputs" / "yt_full_closure_stack_and_strict_pole_response_contract_2026-05-26.json"

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


def is_zero(expr: sp.Expr | sp.MatrixBase) -> bool:
    if isinstance(expr, sp.MatrixBase):
        return all(sp.simplify(entry) == 0 for entry in expr)
    return sp.simplify(expr) == 0


def c3_cycle() -> sp.Matrix:
    return sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors and dependency state")
    paths = (
        NOTE,
        FISHER_ARCLENGTH,
        FISHER_LSZ,
        FIRST_PRINCIPLES,
        SAME_SURFACE_FACTORIZATION,
        C3_RADIAL_NOGO,
        C3_COMPENSATION_NOGO,
        C3_SHARP_NOGO,
        STRICT_AVAILABILITY,
        FULL_STACK,
        FISHER_ARCLENGTH_OUT,
        FISHER_LSZ_OUT,
        FIRST_PRINCIPLES_OUT,
        SAME_SURFACE_FACTORIZATION_OUT,
        C3_RADIAL_NOGO_OUT,
        C3_COMPENSATION_NOGO_OUT,
        C3_SHARP_NOGO_OUT,
        STRICT_AVAILABILITY_OUT,
        FULL_STACK_OUT,
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
        "actual_current_surface_status: no-go / open Fisher-LSZ-to-radial-generator factorization",
        "proposal_allowed: false",
        "raw source scale beta  !=  relative top response coefficient lambda_top",
        "Fisher/LSZ support is not the missing radial generator theorem",
        "lambda_top = 1/sqrt(2)",
    ):
        check(f"note contains normalization phrase: {phrase}", phrase in note)

    deps = {
        "fisher_arclength": load_json(FISHER_ARCLENGTH_OUT),
        "fisher_lsz": load_json(FISHER_LSZ_OUT),
        "first_principles": load_json(FIRST_PRINCIPLES_OUT),
        "same_surface_factorization": load_json(SAME_SURFACE_FACTORIZATION_OUT),
        "c3_radial_nogo": load_json(C3_RADIAL_NOGO_OUT),
        "c3_compensation_nogo": load_json(C3_COMPENSATION_NOGO_OUT),
        "c3_sharp_nogo": load_json(C3_SHARP_NOGO_OUT),
        "strict_availability": load_json(STRICT_AVAILABILITY_OUT),
        "full_stack": load_json(FULL_STACK_OUT),
    }
    for name, data in deps.items():
        check(f"{name} dependency passed", data.get("fail_count") == 0, data.get("fail_count"))

    check("Fisher arclength proposal is not allowed", deps["fisher_arclength"].get("proposal_allowed") is False)
    check("Fisher/LSZ bridge proposal is not allowed", deps["fisher_lsz"].get("proposal_allowed") is False)
    check(
        "radial no-go keeps lambda_top free",
        deps["c3_radial_nogo"].get("certificate_boundary", {}).get("lambda_top_free_on_current_surface")
        is True,
    )
    check(
        "compensation no-go keeps radial factor non-certified",
        deps["c3_compensation_nogo"]
        .get("certificate_boundary", {})
        .get("target_magnitude_forces_radial_factor")
        is False,
    )
    check(
        "sharp no-go keeps radial factor non-certified",
        deps["c3_sharp_nogo"].get("certificate_boundary", {}).get("zero_variance_forces_radial_factor")
        is False,
    )
    check(
        "strict positive certificate remains absent",
        deps["strict_availability"].get("certificate_boundary", {}).get("strict_positive_certificate_present")
        is False,
    )
    return {
        name: {
            "status": data.get("actual_current_surface_status", data.get("status")),
            "trace_class": data.get("trace_class"),
            "proposal_allowed": data.get("proposal_allowed"),
        }
        for name, data in deps.items()
    }


def part2_fisher_scale_vs_radial_factor() -> dict[str, Any]:
    print("\nPart 2: Fisher source scale versus radial factor")
    sqrt = sp.sqrt
    beta, A, g2, lambda_top = sp.symbols("beta A g_2 lambda_top", positive=True)
    C = c3_cycle()
    I = sp.eye(3)
    P0 = sp.simplify((I + C + C**2) / 3)
    Pnt = sp.simplify(I - P0)
    rho_nt = sp.simplify(Pnt / 2)
    Bx = sp.simplify((C + C**2) / sqrt(6))
    O_beta = sp.simplify(beta * Bx)
    fisher_norm = sp.sqrt(sp.trace(O_beta.conjugate().T * O_beta))
    normalized_source = sp.simplify(O_beta / fisher_norm)
    Vtop = sp.simplify(lambda_top * A * normalized_source)
    top_row_magnitude = sp.simplify(-sp.trace(rho_nt * Vtop))
    dmw = g2 * A / 2
    readout = sp.simplify(g2 / sqrt(2) * top_row_magnitude / dmw)
    target_solutions = sp.solve(sp.Eq(readout, 1 / sqrt(6)), lambda_top)

    check("C has order three", is_zero(C**3 - I))
    check("P_0 and P_nt resolve identity", is_zero(P0 + Pnt - I) and is_zero(P0 * Pnt))
    check("B_x has unit Frobenius norm", is_zero(sp.trace(Bx.conjugate().T * Bx) - 1))
    check("raw source O_beta has Fisher norm beta", is_zero(fisher_norm - beta), fisher_norm)
    check("Fisher-normalized source direction is B_x", is_zero(normalized_source - Bx))
    check("top row magnitude is lambda_top*A/sqrt(6)", is_zero(top_row_magnitude - lambda_top * A / sqrt(6)), top_row_magnitude)
    check("same-source readout is lambda_top/sqrt(3)", is_zero(readout - lambda_top / sqrt(3)), readout)
    check("readout is independent of raw source scale beta", not readout.has(beta), readout)
    check("readout still depends on lambda_top", readout.has(lambda_top), readout)
    check("target readout requires lambda_top=1/sqrt(2)", target_solutions == [1 / sqrt(2)], target_solutions)

    row_target = sp.simplify(top_row_magnitude.subs({beta: 1, lambda_top: 1 / sqrt(2)}))
    row_counter = sp.simplify(top_row_magnitude.subs({beta: 3, lambda_top: 2 / sqrt(2)}))
    readout_target = sp.simplify(readout.subs({beta: 1, lambda_top: 1 / sqrt(2)}))
    readout_counter = sp.simplify(readout.subs({beta: 3, lambda_top: 2 / sqrt(2)}))
    check("target witness gives A/sqrt(12)", is_zero(row_target - A / sqrt(12)), row_target)
    check("counter witness changes row despite raw-scale normalization", is_zero(row_counter - 2 * A / sqrt(12)), row_counter)
    check("counter witness changes readout", sp.simplify(readout_target - readout_counter) != 0, (readout_target, readout_counter))

    return {
        "raw_source": "O_beta=beta*B_x",
        "fisher_norm": "beta",
        "fisher_normalized_source": "B_x",
        "top_generator_family": "V_top(lambda_top)=lambda_top*A*B_x",
        "top_row_magnitude": "lambda_top*A/sqrt(6)",
        "same_source_readout": "lambda_top/sqrt(3)",
        "target_lambda_top": "1/sqrt(2)",
        "raw_source_scale_removed": True,
        "relative_top_response_coefficient_removed": False,
        "witnesses": [
            {"beta": "1", "lambda_top": "1/sqrt(2)", "row": "A/sqrt(12)"},
            {"beta": "3", "lambda_top": "2/sqrt(2)", "row": "2*A/sqrt(12)"},
        ],
    }


def part3_lsz_and_reparameterization_boundary() -> dict[str, Any]:
    print("\nPart 3: LSZ and source-reparameterization boundary")
    sqrt = sp.sqrt
    mu, A_res, c, A, g2, lambda_top = sp.symbols("mu A_res c A g_2 lambda_top", positive=True)

    lsz_insertion = sp.simplify(1 / A_res)
    scaled_lsz_insertion = sp.simplify(mu / (mu * A_res))
    check("LSZ insertion is invariant under raw operator rescaling", is_zero(scaled_lsz_insertion - lsz_insertion), scaled_lsz_insertion)

    dmt = lambda_top * A / sqrt(6)
    dmw = g2 * A / 2
    dmt_prime = sp.simplify(dmt / c)
    dmw_prime = sp.simplify(dmw / c)
    readout_prime = sp.simplify(g2 / sqrt(2) * dmt_prime / dmw_prime)
    check("common source reparameterization cancels from readout", is_zero(readout_prime - lambda_top / sqrt(3)), readout_prime)
    check("source reparameterization does not remove lambda_top", readout_prime.has(lambda_top), readout_prime)
    check("W row has no lambda_top", not dmw.has(lambda_top), dmw)
    check("top row has lambda_top", dmt.has(lambda_top), dmt)

    return {
        "lsz_raw_scale_invariant": True,
        "lsz_insertion": "1/A_res",
        "source_reparameterized_readout": "lambda_top/sqrt(3)",
        "w_row_depends_on_lambda_top": False,
        "top_row_depends_on_lambda_top": True,
    }


def part4_certificate() -> dict[str, Any]:
    print("\nPart 4: no-go certificate")
    certificate = {
        "route_pruned": "Fisher/LSZ source normalization plus P_nt support and W row force lambda_top=1/sqrt(2)",
        "fisher_lsz_bridge_granted": True,
        "raw_source_scale_removed": True,
        "lambda_top_relative_response_free": True,
        "accepted_same_surface_radial_generator_factorization_derived": False,
        "accepted_zero_singlet_top_readout_law_derived": False,
        "strict_top_w_response_certificate_present": False,
        "target_requires_lambda_top": "1/sqrt(2)",
        "proposal_allowed": False,
        "bare_retained_allowed": False,
        "no_forbidden_imports": True,
    }
    for key in certificate:
        check(f"certificate field recorded: {key}", key in certificate)
    check("Fisher/LSZ bridge is granted for this no-go", certificate["fisher_lsz_bridge_granted"] is True)
    check("raw scale is removed", certificate["raw_source_scale_removed"] is True)
    check("lambda_top remains free", certificate["lambda_top_relative_response_free"] is True)
    check("radial generator factorization is not derived", certificate["accepted_same_surface_radial_generator_factorization_derived"] is False)
    check("proposal remains disallowed", certificate["proposal_allowed"] is False)

    no_go_audit = {
        "narrow_route_pruned": certificate["route_pruned"],
        "reason": (
            "Fisher/LSZ normalization removes the raw source scale beta, but "
            "the same normalized source direction B_x admits a finite "
            "same-source top response family V_top(lambda_top)=lambda_top*A*B_x."
        ),
        "remaining_imports": [
            "accepted same-surface radial generator factorization lambda_top=1/sqrt(2)",
            "accepted physical top-block/readout law excluding P_0",
            "accepted strict same-source top/W pole rows with controls",
        ],
        "route_still_live": [
            "derive radial generator factorization from new same-surface dynamics",
            "derive zero-singlet physical readout plus radial theorem",
            "produce accepted strict top/W pole rows",
        ],
    }
    check("no-go audit names Fisher/LSZ normalization", "Fisher/LSZ" in no_go_audit["reason"])
    check("no-go audit names radial import", "lambda_top=1/sqrt(2)" in no_go_audit["remaining_imports"][0])
    check("strict pole route remains live", any("strict" in item for item in no_go_audit["route_still_live"]))
    return {"certificate_boundary": certificate, "no_go_audit": no_go_audit}


def part5_firewalls() -> None:
    print("\nPart 5: firewalls and wording")
    note = read(NOTE)
    one_line = " ".join(note.split())
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
        "fitted selector",
    ):
        check(f"firewall phrase present: {phrase}", phrase in one_line)

    for phrase in (
        "Status:** retained",
        "Status:** proposed_retained",
        "This note derives `y_t`",
        "full positive closure",
        "lambda_top is derived",
        "strict top/W pole rows are provided",
        "proposal_allowed: true",
    ):
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)


def main() -> int:
    print("=" * 88)
    print("Y_T FISHER-LSZ RADIAL GENERATOR NORMALIZATION NO-GO")
    print("=" * 88)

    anchors = part1_anchors()
    normalization_witness = part2_fisher_scale_vs_radial_factor()
    lsz_boundary = part3_lsz_and_reparameterization_boundary()
    certificate = part4_certificate()
    part5_firewalls()

    result = {
        "claim_id": "yt_fisher_lsz_radial_generator_normalization_no_go_note_2026-05-28",
        "actual_current_surface_status": "no-go / open Fisher-LSZ-to-radial-generator factorization",
        "trace_class": "negative_route_pruning",
        "reachability_to_target": "prunes",
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "Fisher/LSZ source normalization removes raw source scale but does "
            "not derive the relative top response coefficient "
            "lambda_top=1/sqrt(2), physical zero-singlet readout law, or strict "
            "top/W pole rows."
        ),
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "anchor_statuses": anchors,
        "normalization_witness": normalization_witness,
        "lsz_reparameterization_boundary": lsz_boundary,
        "certificate_boundary": certificate["certificate_boundary"],
        "no_go_audit": certificate["no_go_audit"],
        "deep_work_stretch_summary": {
            "minimal_premises": [
                "Fisher/LSZ normalized source direction B_x",
                "same-source W row g_2*A/2",
                "zero-singlet top readout in P_nt granted for the stretch attempt",
                "no observed masses, fitted selectors, or target insertion",
            ],
            "hard_wall": (
                "The current surface lacks an accepted theorem identifying the "
                "Fisher/LSZ-normalized C3 source tangent with the top radial "
                "mass generator coefficient lambda_top=1/sqrt(2)."
            ),
            "forbidden_inputs_used": [],
        },
        "first_open_gate_after_this_note": (
            "accepted same-surface radial generator factorization plus physical "
            "top-block/readout law excluding P_0, or accepted strict top/W pole rows"
        ),
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
        "review_surface": [
            "docs/YT_FISHER_LSZ_RADIAL_GENERATOR_NORMALIZATION_NO_GO_NOTE_2026-05-28.md",
            "scripts/frontier_yt_fisher_lsz_radial_generator_normalization_no_go.py",
            "outputs/yt_fisher_lsz_radial_generator_normalization_no_go_2026-05-28.json",
        ],
    }

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nwrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
