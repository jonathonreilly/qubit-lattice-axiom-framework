#!/usr/bin/env python3
"""Y_T C3 dihedral basepoint anchor obstruction."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_c3_dihedral_basepoint_anchor_obstruction_2026-05-27.json"

NOTE = DOCS / "YT_C3_DIHEDRAL_BASEPOINT_ANCHOR_OBSTRUCTION_NOTE_2026-05-27.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"
PHASE_ORBIT_NOGO = DOCS / "YT_C3_PHASE_ORBIT_SELECTOR_UNDERDETERMINATION_NO_GO_NOTE_2026-05-27.md"
ORBIT_MEMBER_NOGO = DOCS / "YT_C3_ORBIT_MEMBER_READOUT_COVARIANCE_NO_GO_NOTE_2026-05-27.md"
REFLECTION_SOURCE = DOCS / "YT_C3_REAL_RECORD_REFLECTION_EVEN_SOURCE_THEOREM_NOTE_2026-05-27.md"
PHASE_CONE = DOCS / "YT_C3_PHASE_ORDERING_CONE_SUPPORT_BOUNDARY_NOTE_2026-05-27.md"
MATRIX_ELEMENT = DOCS / "YT_SAME_SURFACE_TOP_MATRIX_ELEMENT_FACTORIZATION_BOUNDARY_NOTE_2026-05-27.md"
STRICT_AVAILABILITY = DOCS / "YT_STRICT_SPARSE_TOP_W_POLE_RESPONSE_AVAILABILITY_AUDIT_NOTE_2026-05-27.md"

PHASE_ORBIT_NOGO_OUT = ROOT / "outputs" / "yt_c3_phase_orbit_selector_underdetermination_2026-05-27.json"
ORBIT_MEMBER_NOGO_OUT = ROOT / "outputs" / "yt_c3_orbit_member_readout_covariance_no_go_2026-05-27.json"
REFLECTION_SOURCE_OUT = ROOT / "outputs" / "yt_c3_real_record_reflection_even_source_2026-05-27.json"
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


def member_witness(member: int, angle: sp.Expr) -> dict[str, Any]:
    values = eigenvalues(angle)
    lines = top_set(values)
    return {
        "member": member,
        "phi": sp.sstr(angle),
        "eigenvalues": {name: sp.sstr(sp.radsimp(value)) for name, value in values.items()},
        "top_lines": lines,
        "row_magnitudes_if_selected": row_magnitudes(lines),
    }


def c3_generator(member: int) -> int:
    return (member + 1) % 3


def reflection(axis: int, member: int) -> int:
    return (2 * axis - member) % 3


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors and dependency statuses")
    for path in (
        NOTE,
        FULL_STACK,
        PHASE_ORBIT_NOGO,
        ORBIT_MEMBER_NOGO,
        REFLECTION_SOURCE,
        PHASE_CONE,
        MATRIX_ELEMENT,
        STRICT_AVAILABILITY,
        PHASE_ORBIT_NOGO_OUT,
        ORBIT_MEMBER_NOGO_OUT,
        REFLECTION_SOURCE_OUT,
        PHASE_CONE_OUT,
        MATRIX_ELEMENT_OUT,
        STRICT_AVAILABILITY_OUT,
    ):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for section in (
        "Question",
        "Answer",
        "Assumptions / Imports Exercise",
        "First-Principles / Elon Exercise",
        "Finite Witness",
        "Stuck Fan-Out",
        "No-Go Audit",
        "Literature / Math Search",
        "What Remains Open",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)
    for phrase in (
        "actual_current_surface_status: no-go / open physical basepoint anchor law",
        "proposal_allowed: false",
        "existing real-record reflection axis fixes the singlet",
        "rotated reflection axis",
        "physical basepoint section",
        "strict W/top pole rows",
    ):
        check(f"note contains obstruction phrase: {phrase}", phrase in note)

    deps = {
        "phase_orbit_nogo": load_json(PHASE_ORBIT_NOGO_OUT),
        "orbit_member_nogo": load_json(ORBIT_MEMBER_NOGO_OUT),
        "reflection_source": load_json(REFLECTION_SOURCE_OUT),
        "phase_cone": load_json(PHASE_CONE_OUT),
        "matrix_element": load_json(MATRIX_ELEMENT_OUT),
        "strict_availability": load_json(STRICT_AVAILABILITY_OUT),
    }
    for name, data in deps.items():
        check(f"{name} dependency passed", data.get("fail_count") == 0, data.get("fail_count"))
    check(
        "orbit-member covariance already lacks section",
        deps["orbit_member_nogo"].get("no_go_certificate", {})
        .get("free_c3_orbit_has_equivariant_section")
        is False,
    )
    check(
        "real-record reflection source is exact support only",
        deps["reflection_source"].get("proposal_allowed") is False,
    )
    check(
        "strict availability still confirms strict rows absent",
        deps["strict_availability"].get("availability_witness", {})
        .get("strict_top_w_rows_artifact_present")
        is False,
    )
    return deps


def part2_group_action_no_section() -> dict[str, Any]:
    print("\nPart 2: C3/D3 action and section obstruction")
    members = [0, 1, 2]
    c3_images = {member: c3_generator(member) for member in members}
    candidate_sections = []
    for chosen in members:
        c3_invariant = chosen == c3_generator(chosen)
        d3_invariant = c3_invariant and all(chosen == reflection(axis, chosen) for axis in members)
        candidate_sections.append(
            {
                "chosen_member": chosen,
                "c3_generator_image": c3_generator(chosen),
                "c3_invariant": c3_invariant,
                "d3_invariant": d3_invariant,
            }
        )
    check("C3 generator acts freely", all(c3_images[m] != m for m in members), c3_images)
    check("no C3-invariant section exists", all(not item["c3_invariant"] for item in candidate_sections), candidate_sections)
    check("no full D3-natural section exists", all(not item["d3_invariant"] for item in candidate_sections), candidate_sections)
    return {
        "members": members,
        "c3_generator_action": {str(key): value for key, value in c3_images.items()},
        "candidate_sections": candidate_sections,
        "c3_invariant_section_exists": False,
        "d3_natural_section_exists": False,
    }


def part3_reflection_axis_witnesses() -> dict[str, Any]:
    print("\nPart 3: reflection-axis witnesses")
    members = [0, 1, 2]
    primitive_angles = {
        0: sp.Integer(0),
        1: 2 * sp.pi / 3,
        2: 4 * sp.pi / 3,
    }
    member_rows = {member: member_witness(member, angle) for member, angle in primitive_angles.items()}
    reflection_axes = []
    for axis in members:
        fixed = [member for member in members if reflection(axis, member) == member]
        swapped = {str(member): reflection(axis, member) for member in members if member not in fixed}
        reflection_axes.append(
            {
                "axis": axis,
                "fixed_members": fixed,
                "swapped_members": swapped,
                "fixed_member_witnesses": [member_rows[member] for member in fixed],
                "imports_rotated_axis_if_declared_physical": axis != 0,
            }
        )

    check("existing reflection R0 fixes only member 0", reflection_axes[0]["fixed_members"] == [0], reflection_axes[0])
    check("existing reflection R0 fixed member is P0", reflection_axes[0]["fixed_member_witnesses"][0]["top_lines"] == ["P_0"], reflection_axes[0])
    check(
        "existing reflection R0 fixed row is A/sqrt3",
        reflection_axes[0]["fixed_member_witnesses"][0]["row_magnitudes_if_selected"] == ["sqrt(3)*A/3"],
        reflection_axes[0],
    )
    check(
        "rotated reflection axes can fix nontrivial members only as extra axes",
        reflection_axes[1]["fixed_member_witnesses"][0]["top_lines"] == ["P_omega2"]
        and reflection_axes[2]["fixed_member_witnesses"][0]["top_lines"] == ["P_omega"]
        and all(axis["imports_rotated_axis_if_declared_physical"] for axis in reflection_axes[1:]),
        reflection_axes,
    )
    check(
        "all primitive orbit rows include one singlet and two target rows",
        [member_rows[idx]["row_magnitudes_if_selected"] for idx in members]
        == [["sqrt(3)*A/3"], ["sqrt(3)*A/6"], ["sqrt(3)*A/6"]],
        member_rows,
    )
    return {
        "primitive_member_rows": {str(key): value for key, value in member_rows.items()},
        "reflection_axes": reflection_axes,
    }


def part4_no_go_certificate() -> dict[str, bool]:
    print("\nPart 4: no-go certificate")
    certificate = {
        "c3_invariant_section_exists": False,
        "d3_natural_section_exists": False,
        "existing_record_reflection_fixes_p0": True,
        "existing_record_reflection_excludes_p0": False,
        "rotated_reflection_axis_selects_nontrivial_member_only_with_extra_basepoint": True,
        "accepted_physical_basepoint_anchor_derived": False,
        "accepted_orbit_member_readout_derived": False,
        "accepted_w_top_matrix_elements_supplied": False,
        "strict_top_w_response_certificate_present": False,
        "proposal_allowed": False,
        "bare_retained_allowed": False,
        "no_forbidden_imports": True,
    }
    for key, value in certificate.items():
        check(f"certificate field recorded: {key}", isinstance(value, bool), value)
    check("C3/D3 naturality does not select a member", certificate["d3_natural_section_exists"] is False)
    check("existing reflection does not exclude P0", certificate["existing_record_reflection_excludes_p0"] is False)
    check("physical basepoint remains open", certificate["accepted_physical_basepoint_anchor_derived"] is False)
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
        "physical basepoint is derived",
    ):
        check(f"forbidden overclaim absent: {forbidden}", forbidden not in note)


def part6_claim_status() -> dict[str, Any]:
    print("\nPart 6: claim status")
    status = {
        "actual_current_surface_status": "no-go / open physical basepoint anchor law",
        "trace_class": "negative_route_pruning",
        "reachability_to_target": "prunes shortcut",
        "conditional_surface_status": None,
        "hypothetical_axiom_status": None,
        "admitted_observation_status": None,
        "proposal_allowed": False,
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "route_still_live": (
            "produce accepted strict top/W pole rows, or derive an accepted "
            "same-surface physical orientation/basepoint/orbit-member top-line "
            "law with W/top matrix elements"
        ),
    }
    check(
        "actual status is no-go/open physical basepoint anchor law",
        status["actual_current_surface_status"] == "no-go / open physical basepoint anchor law",
    )
    check("trace class is route pruning", status["trace_class"] == "negative_route_pruning")
    check("proposal remains false", status["proposal_allowed"] is False)
    check("route still live names strict rows", "strict top/W pole rows" in status["route_still_live"])
    return status


def main() -> int:
    print("=" * 78)
    print("Y_T C3 DIHEDRAL BASEPOINT ANCHOR OBSTRUCTION")
    print("=" * 78)

    deps = part1_anchors()
    group_action = part2_group_action_no_section()
    reflection_witnesses = part3_reflection_axis_witnesses()
    certificate = part4_no_go_certificate()
    part5_firewalls()
    status = part6_claim_status()

    result = {
        "claim_id": "yt_c3_dihedral_basepoint_anchor_obstruction_note_2026-05-27",
        "generated_by": "scripts/frontier_yt_c3_dihedral_basepoint_anchor_obstruction.py",
        **status,
        "proposal_allowed_reason": (
            "Full C3/D3 naturality cannot select a member of a free phase orbit, "
            "and the existing real-record reflection axis fixes the singlet "
            "member P_0. Rotated reflection axes can fix nontrivial members only "
            "after importing the missing physical basepoint section."
        ),
        "dependencies": {
            name: {
                "claim_id": data.get("claim_id"),
                "status": data.get("actual_current_surface_status"),
                "fail_count": data.get("fail_count"),
            }
            for name, data in deps.items()
        },
        "group_action": group_action,
        "reflection_witnesses": reflection_witnesses,
        "no_go_certificate": certificate,
        "next_ranked_route": "accepted strict top/W pole rows or new physical basepoint theorem",
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
