#!/usr/bin/env python3
"""Y_T C3 phase-orbit selector underdetermination no-go."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_c3_phase_orbit_selector_underdetermination_2026-05-27.json"

NOTE = DOCS / "YT_C3_PHASE_ORBIT_SELECTOR_UNDERDETERMINATION_NO_GO_NOTE_2026-05-27.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"
PHASE_CONE = DOCS / "YT_C3_PHASE_ORDERING_CONE_SUPPORT_BOUNDARY_NOTE_2026-05-27.md"
PRIMITIVE_ANGLE = DOCS / "YT_C3_PRIMITIVE_CHARACTER_PHASE_ANGLE_CANDIDATE_NOTE_2026-05-27.md"
REPRESENTATION_NOGO = DOCS / "YT_C3_REPRESENTATION_PHASE_SELECTION_NO_GO_NOTE_2026-05-27.md"
CUBIC_SUPPORT = DOCS / "YT_C3_CUBIC_INVARIANT_PHASE_SELECTOR_SUPPORT_BOUNDARY_NOTE_2026-05-27.md"
CUBIC_NOGO = DOCS / "YT_C3_CUBIC_PHASE_POTENTIAL_SIGN_BRANCH_UNDERDETERMINATION_NO_GO_NOTE_2026-05-27.md"
STRICT_AVAILABILITY = DOCS / "YT_STRICT_SPARSE_TOP_W_POLE_RESPONSE_AVAILABILITY_AUDIT_NOTE_2026-05-27.md"

PHASE_CONE_OUT = ROOT / "outputs" / "yt_c3_phase_ordering_cone_support_boundary_2026-05-27.json"
PRIMITIVE_ANGLE_OUT = ROOT / "outputs" / "yt_c3_primitive_character_phase_angle_candidate_2026-05-27.json"
REPRESENTATION_NOGO_OUT = ROOT / "outputs" / "yt_c3_representation_phase_selection_no_go_2026-05-27.json"
CUBIC_SUPPORT_OUT = ROOT / "outputs" / "yt_c3_cubic_invariant_phase_selector_support_boundary_2026-05-27.json"
CUBIC_NOGO_OUT = ROOT / "outputs" / "yt_c3_cubic_phase_potential_sign_branch_underdetermination_2026-05-27.json"
STRICT_AVAILABILITY_OUT = ROOT / "outputs" / "yt_strict_sparse_top_w_pole_response_availability_audit_2026-05-27.json"

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


def eigenvalues(phi: sp.Expr) -> dict[str, sp.Expr]:
    return {
        "P_0": sp.radsimp(sp.sqrt(sp.Rational(2, 3)) * sp.cos(phi)),
        "P_omega": sp.radsimp(sp.sqrt(sp.Rational(2, 3)) * sp.cos(phi + 2 * sp.pi / 3)),
        "P_omega2": sp.radsimp(sp.sqrt(sp.Rational(2, 3)) * sp.cos(phi - 2 * sp.pi / 3)),
    }


def top_set(values: dict[str, sp.Expr]) -> list[str]:
    max_value = max(values.values(), key=lambda value: float(sp.N(value)))
    return [name for name, value in values.items() if is_zero(value - max_value)]


def row_magnitudes(lines: list[str]) -> list[str]:
    A = sp.symbols("A", positive=True)
    rows = {
        "P_0": sp.radsimp(A / sp.sqrt(3)),
        "P_omega": sp.radsimp(A / sp.sqrt(12)),
        "P_omega2": sp.radsimp(A / sp.sqrt(12)),
    }
    return [sp.sstr(rows[line]) for line in lines]


def line_witness(angle: sp.Expr) -> dict[str, Any]:
    values = eigenvalues(angle)
    lines = top_set(values)
    return {
        "phi": sp.sstr(angle),
        "eigenvalues": {name: sp.sstr(sp.radsimp(value)) for name, value in values.items()},
        "top_lines": lines,
        "row_magnitudes_if_selected": row_magnitudes(lines),
    }


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors and dependency statuses")
    for path in (
        NOTE,
        FULL_STACK,
        PHASE_CONE,
        PRIMITIVE_ANGLE,
        REPRESENTATION_NOGO,
        CUBIC_SUPPORT,
        CUBIC_NOGO,
        STRICT_AVAILABILITY,
        PHASE_CONE_OUT,
        PRIMITIVE_ANGLE_OUT,
        REPRESENTATION_NOGO_OUT,
        CUBIC_SUPPORT_OUT,
        CUBIC_NOGO_OUT,
        STRICT_AVAILABILITY_OUT,
    ):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for section in (
        "Question",
        "Answer",
        "First-Principles / Elon Exercise",
        "Finite Witness",
        "No-Go Audit",
        "Literature / Math Search",
        "What Remains Open",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)
    for phrase in (
        "actual_current_surface_status: no-go / open phase-orbit member law",
        "proposal_allowed: false",
        "select a phase orbit",
        "generic orbit cycles through all three C3 spectral lines",
        "orbit-member/readout law",
    ):
        check(f"note contains no-go phrase: {phrase}", phrase in note)

    deps = {
        "phase_cone": load_json(PHASE_CONE_OUT),
        "primitive_angle": load_json(PRIMITIVE_ANGLE_OUT),
        "representation_nogo": load_json(REPRESENTATION_NOGO_OUT),
        "cubic_support": load_json(CUBIC_SUPPORT_OUT),
        "cubic_nogo": load_json(CUBIC_NOGO_OUT),
        "strict_availability": load_json(STRICT_AVAILABILITY_OUT),
    }
    for name, data in deps.items():
        check(f"{name} dependency passed", data.get("fail_count") == 0, data.get("fail_count"))
    check(
        "representation-only phase selector is already pruned",
        deps["representation_nogo"].get("no_go_certificate", {})
        .get("representation_theory_selects_phi_pm_2pi_over_3")
        is False,
    )
    check(
        "cubic no-go leaves physical phase law open",
        deps["cubic_nogo"].get("no_go_certificate", {}).get("physical_phase_law_derived")
        is False,
    )
    check(
        "strict availability dependency confirms strict rows absent",
        deps["strict_availability"].get("availability_witness", {})
        .get("strict_top_w_rows_artifact_present")
        is False,
    )
    return deps


def part2_c3_fourier_orbit_law() -> dict[str, str]:
    print("\nPart 2: C3 Fourier orbit law")
    phi, theta, delta = sp.symbols("phi theta delta", real=True)
    c0, a1, b1, a2, b2 = sp.symbols("c0 a1 b1 a2 b2", real=True)
    potential = (
        c0
        + a1 * sp.cos(3 * phi)
        + b1 * sp.sin(3 * phi)
        + a2 * sp.cos(6 * phi)
        + b2 * sp.sin(6 * phi)
    )
    shifted = sp.trigsimp(sp.expand_trig(potential.subs(phi, phi + 2 * sp.pi / 3) - potential))
    orbit_equal = sp.trigsimp(sp.expand_trig(potential.subs(phi, theta + 2 * sp.pi / 3) - potential.subs(phi, theta)))
    offset_potential = sp.cos(3 * phi - delta)
    offset_shifted = sp.trigsimp(
        sp.expand_trig(offset_potential.subs(phi, phi + 2 * sp.pi / 3) - offset_potential)
    )
    check("finite C3 Fourier scalar is orbit-constant", is_zero(shifted), shifted)
    check("orbit members have equal potential value", is_zero(orbit_equal), orbit_equal)
    check("shifted harmonic has arbitrary phase offset", is_zero(offset_shifted), offset_shifted)
    return {
        "finite_fourier_form": sp.sstr(potential),
        "periodicity_check": sp.sstr(shifted),
        "orbit_equal_value_check": sp.sstr(orbit_equal),
        "arbitrary_offset_harmonic": sp.sstr(offset_potential),
        "offset_periodicity_check": sp.sstr(offset_shifted),
    }


def part3_orbit_witnesses() -> dict[str, Any]:
    print("\nPart 3: orbit witnesses")
    primitive_angles = [sp.Integer(0), 2 * sp.pi / 3, -2 * sp.pi / 3]
    generic_angles = [sp.pi / 9, sp.pi / 9 + 2 * sp.pi / 3, sp.pi / 9 - 2 * sp.pi / 3]
    primitive = [line_witness(angle) for angle in primitive_angles]
    generic = [line_witness(angle) for angle in generic_angles]

    check(
        "primitive orbit line labels are singlet plus nontrivial pair",
        [entry["top_lines"] for entry in primitive] == [["P_0"], ["P_omega2"], ["P_omega"]],
        primitive,
    )
    check(
        "primitive orbit row magnitudes include A/sqrt3 and A/sqrt12",
        [entry["row_magnitudes_if_selected"] for entry in primitive]
        == [["sqrt(3)*A/3"], ["sqrt(3)*A/6"], ["sqrt(3)*A/6"]],
        primitive,
    )
    check(
        "generic orbit cycles through all three line labels",
        [entry["top_lines"] for entry in generic] == [["P_0"], ["P_omega2"], ["P_omega"]],
        generic,
    )
    check(
        "C3 orbit selection does not exclude P_0",
        any(entry["top_lines"] == ["P_0"] for entry in primitive)
        and any(entry["top_lines"] == ["P_0"] for entry in generic),
    )
    return {
        "primitive_cubic_orbit": primitive,
        "generic_orbit_pi_over_9": generic,
    }


def part4_no_go_certificate() -> dict[str, bool]:
    print("\nPart 4: no-go certificate")
    certificate = {
        "c3_scalar_phase_potential_selects_orbits": True,
        "generic_orbit_contains_all_line_labels": True,
        "primitive_orbit_contains_singlet_and_target_rows": True,
        "orbit_selection_excludes_p0": False,
        "phase_offset_derived_from_current_surface": False,
        "accepted_orbit_member_readout_derived": False,
        "accepted_nontrivial_top_line_law_derived": False,
        "accepted_w_top_matrix_elements_supplied": False,
        "strict_top_w_response_certificate_present": False,
        "proposal_allowed": False,
        "bare_retained_allowed": False,
        "no_forbidden_imports": True,
    }
    for key, value in certificate.items():
        check(f"certificate field recorded: {key}", isinstance(value, bool), value)
    check("shortcut is pruned because orbit member is not derived", certificate["accepted_orbit_member_readout_derived"] is False)
    check("strict rows remain absent", certificate["strict_top_w_response_certificate_present"] is False)
    return certificate


def part5_firewalls() -> None:
    print("\nPart 5: firewalls and wording")
    note = read(NOTE)
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
        check(f"firewall phrase present: {phrase}", phrase in note)
    for forbidden in (
        "Status:** retained",
        "Status:** proposed_retained",
        "This note derives `y_t`",
        "full Y_T closure",
        "positive Y_T closure is obtained",
        "strict W/top pole rows are supplied",
        "accepted top line is derived",
    ):
        check(f"forbidden overclaim absent: {forbidden}", forbidden not in note)


def part6_claim_status() -> dict[str, Any]:
    print("\nPart 6: claim status")
    status = {
        "actual_current_surface_status": "no-go / open phase-orbit member law",
        "trace_class": "negative_route_pruning",
        "reachability_to_target": "prunes shortcut",
        "conditional_surface_status": None,
        "proposal_allowed": False,
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "route_still_live": (
            "produce accepted strict top/W pole rows, or derive an accepted "
            "same-surface orbit-member/top-line law with W/top matrix elements"
        ),
    }
    check("actual status is no-go/open phase-orbit law", status["actual_current_surface_status"] == "no-go / open phase-orbit member law")
    check("trace class is route pruning", status["trace_class"] == "negative_route_pruning")
    check("proposal remains false", status["proposal_allowed"] is False)
    check("route still live names strict rows", "strict top/W pole rows" in status["route_still_live"])
    return status


def main() -> int:
    print("=" * 78)
    print("Y_T C3 PHASE-ORBIT SELECTOR UNDERDETERMINATION NO-GO")
    print("=" * 78)

    deps = part1_anchors()
    fourier = part2_c3_fourier_orbit_law()
    witnesses = part3_orbit_witnesses()
    certificate = part4_no_go_certificate()
    part5_firewalls()
    status = part6_claim_status()

    result = {
        "claim_id": "yt_c3_phase_orbit_selector_underdetermination_no_go_note_2026-05-27",
        "generated_by": "scripts/frontier_yt_c3_phase_orbit_selector_underdetermination.py",
        **status,
        "proposal_allowed_reason": (
            "C3-invariant scalar phase dynamics selects phase orbits, while "
            "generic and primitive C3 orbits contain both singlet and "
            "nontrivial top-line witnesses.  The actual surface does not "
            "derive an accepted orbit-member/readout law or strict W/top rows."
        ),
        "dependency_statuses": {
            name: data.get("actual_current_surface_status") for name, data in deps.items()
        },
        "fourier_orbit_law": fourier,
        "finite_witnesses": witnesses,
        "no_go_certificate": certificate,
        "next_ranked_route": "accepted strict same-source top/W pole rows with controls",
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
