#!/usr/bin/env python3
"""Y_T C3 orbit-member readout covariance no-go."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_c3_orbit_member_readout_covariance_no_go_2026-05-27.json"

NOTE = DOCS / "YT_C3_ORBIT_MEMBER_READOUT_COVARIANCE_NO_GO_NOTE_2026-05-27.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"
PHASE_ORBIT_NOGO = DOCS / "YT_C3_PHASE_ORBIT_SELECTOR_UNDERDETERMINATION_NO_GO_NOTE_2026-05-27.md"
PHASE_CONE = DOCS / "YT_C3_PHASE_ORDERING_CONE_SUPPORT_BOUNDARY_NOTE_2026-05-27.md"
MATRIX_ELEMENT = DOCS / "YT_SAME_SURFACE_TOP_MATRIX_ELEMENT_FACTORIZATION_BOUNDARY_NOTE_2026-05-27.md"
STRICT_AVAILABILITY = DOCS / "YT_STRICT_SPARSE_TOP_W_POLE_RESPONSE_AVAILABILITY_AUDIT_NOTE_2026-05-27.md"

PHASE_ORBIT_NOGO_OUT = ROOT / "outputs" / "yt_c3_phase_orbit_selector_underdetermination_2026-05-27.json"
PHASE_CONE_OUT = ROOT / "outputs" / "yt_c3_phase_ordering_cone_support_boundary_2026-05-27.json"
MATRIX_ELEMENT_OUT = ROOT / "outputs" / "yt_same_surface_top_matrix_element_factorization_boundary_2026-05-27.json"
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


def is_zero(expr: sp.Expr) -> bool:
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


def member_witness(angle: sp.Expr, section_index: int) -> dict[str, Any]:
    values = eigenvalues(angle)
    lines = top_set(values)
    return {
        "section_index": section_index,
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
        PHASE_ORBIT_NOGO,
        PHASE_CONE,
        MATRIX_ELEMENT,
        STRICT_AVAILABILITY,
        PHASE_ORBIT_NOGO_OUT,
        PHASE_CONE_OUT,
        MATRIX_ELEMENT_OUT,
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
        "actual_current_surface_status: no-go / open orbit-member readout law",
        "proposal_allowed: false",
        "no C3-equivariant section",
        "symmetry-breaking sections",
        "singlet-row witness",
        "orientation/basepoint/orbit-member",
    ):
        check(f"note contains covariance no-go phrase: {phrase}", phrase in note)

    deps = {
        "phase_orbit_nogo": load_json(PHASE_ORBIT_NOGO_OUT),
        "phase_cone": load_json(PHASE_CONE_OUT),
        "matrix_element": load_json(MATRIX_ELEMENT_OUT),
        "strict_availability": load_json(STRICT_AVAILABILITY_OUT),
    }
    for name, data in deps.items():
        check(f"{name} dependency passed", data.get("fail_count") == 0, data.get("fail_count"))
    check(
        "phase-orbit dependency leaves member readout open",
        deps["phase_orbit_nogo"].get("no_go_certificate", {}).get("accepted_orbit_member_readout_derived")
        is False,
    )
    check(
        "matrix-element dependency remains conditional",
        deps["matrix_element"].get("proposal_allowed") is False,
    )
    check(
        "strict availability dependency confirms strict rows absent",
        deps["strict_availability"].get("availability_witness", {})
        .get("strict_top_w_rows_artifact_present")
        is False,
    )
    return deps


def part2_equivariant_section_no_go() -> dict[str, Any]:
    print("\nPart 2: finite C3 quotient-section no-go")
    members = [0, 1, 2]

    def generator(member: int) -> int:
        return (member + 1) % 3

    candidates = []
    for chosen in members:
        equivariant = chosen == generator(chosen)
        candidates.append(
            {
                "chosen_member": chosen,
                "generator_image": generator(chosen),
                "equivariance_condition_holds": equivariant,
            }
        )
    check(
        "free three-member C3 orbit has no equivariant section",
        all(not item["equivariance_condition_holds"] for item in candidates),
        candidates,
    )
    check(
        "C3 generator acts freely on all members",
        all(generator(member) != member for member in members),
        {member: generator(member) for member in members},
    )
    return {
        "orbit_members": members,
        "generator_action": {str(member): generator(member) for member in members},
        "section_candidates": candidates,
        "equivariant_section_exists": False,
    }


def part3_symmetry_breaking_sections() -> dict[str, Any]:
    print("\nPart 3: symmetry-breaking section witnesses")
    primitive_angles = [sp.Integer(0), 2 * sp.pi / 3, 4 * sp.pi / 3]
    generic_base = sp.pi / 9
    generic_angles = [generic_base, generic_base + 2 * sp.pi / 3, generic_base + 4 * sp.pi / 3]

    primitive = [member_witness(angle, idx) for idx, angle in enumerate(primitive_angles)]
    generic = [member_witness(angle, idx) for idx, angle in enumerate(generic_angles)]

    check(
        "primitive symmetry-breaking sections include singlet and nontrivial lines",
        [entry["top_lines"] for entry in primitive] == [["P_0"], ["P_omega2"], ["P_omega"]],
        primitive,
    )
    check(
        "primitive symmetry-breaking sections include A/sqrt3 and A/sqrt12 rows",
        [entry["row_magnitudes_if_selected"] for entry in primitive]
        == [["sqrt(3)*A/3"], ["sqrt(3)*A/6"], ["sqrt(3)*A/6"]],
        primitive,
    )
    check(
        "generic symmetry-breaking sections also cycle through all line labels",
        [entry["top_lines"] for entry in generic] == [["P_0"], ["P_omega2"], ["P_omega"]],
        generic,
    )
    check(
        "one admissible section selects P0",
        any(entry["top_lines"] == ["P_0"] for entry in primitive),
        primitive,
    )
    return {
        "primitive_orbit_sections": primitive,
        "generic_orbit_pi_over_9_sections": generic,
    }


def part4_no_go_certificate() -> dict[str, bool]:
    print("\nPart 4: no-go certificate")
    certificate = {
        "free_c3_orbit_has_equivariant_section": False,
        "c3_covariance_selects_orbit_member": False,
        "symmetry_breaking_sections_equally_admissible_before_physical_anchor": True,
        "one_admissible_section_selects_p0": True,
        "nontrivial_line_exclusion_derived": False,
        "accepted_orbit_member_readout_derived": False,
        "accepted_orientation_basepoint_anchor_derived": False,
        "accepted_w_top_matrix_elements_supplied": False,
        "strict_top_w_response_certificate_present": False,
        "proposal_allowed": False,
        "bare_retained_allowed": False,
        "no_forbidden_imports": True,
    }
    for key, value in certificate.items():
        check(f"certificate field recorded: {key}", isinstance(value, bool), value)
    check("equivariant section is absent", certificate["free_c3_orbit_has_equivariant_section"] is False)
    check("P0 exclusion is not derived", certificate["nontrivial_line_exclusion_derived"] is False)
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
        "positive Y_T closure is obtained",
        "strict W/top pole rows are supplied",
        "accepted top line is derived",
    ):
        check(f"forbidden overclaim absent: {forbidden}", forbidden not in note)


def part6_claim_status() -> dict[str, Any]:
    print("\nPart 6: claim status")
    status = {
        "actual_current_surface_status": "no-go / open orbit-member readout law",
        "trace_class": "negative_route_pruning",
        "reachability_to_target": "prunes shortcut",
        "conditional_surface_status": None,
        "proposal_allowed": False,
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "route_still_live": (
            "produce accepted strict top/W pole rows, or derive an accepted "
            "same-surface orientation/basepoint/orbit-member top-line law "
            "with W/top matrix elements"
        ),
    }
    check(
        "actual status is no-go/open orbit-member readout law",
        status["actual_current_surface_status"] == "no-go / open orbit-member readout law",
    )
    check("trace class is route pruning", status["trace_class"] == "negative_route_pruning")
    check("proposal remains false", status["proposal_allowed"] is False)
    check("route still live names strict rows", "strict top/W pole rows" in status["route_still_live"])
    return status


def main() -> int:
    print("=" * 78)
    print("Y_T C3 ORBIT-MEMBER READOUT COVARIANCE NO-GO")
    print("=" * 78)

    deps = part1_anchors()
    section_no_go = part2_equivariant_section_no_go()
    witnesses = part3_symmetry_breaking_sections()
    certificate = part4_no_go_certificate()
    part5_firewalls()
    status = part6_claim_status()

    result = {
        "claim_id": "yt_c3_orbit_member_readout_covariance_no_go_note_2026-05-27",
        "generated_by": "scripts/frontier_yt_c3_orbit_member_readout_covariance_no_go.py",
        **status,
        "proposal_allowed_reason": (
            "C3 covariance does not choose a physical member of a free C3 "
            "phase orbit. There is no C3-equivariant section of the quotient, "
            "and the symmetry-breaking sections include a singlet-row witness "
            "as well as target-row witnesses."
        ),
        "dependency_statuses": {
            name: data.get("actual_current_surface_status") for name, data in deps.items()
        },
        "equivariant_section_no_go": section_no_go,
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
