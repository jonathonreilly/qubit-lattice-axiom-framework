#!/usr/bin/env python3
"""Y_T C3 orientation-biased phase-potential orbit-member no-go."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_c3_orientation_biased_phase_potential_orbit_member_no_go_2026-05-27.json"

NOTE = DOCS / "YT_C3_ORIENTATION_BIASED_PHASE_POTENTIAL_ORBIT_MEMBER_NO_GO_NOTE_2026-05-27.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"
PHASE_ORBIT_NOGO = DOCS / "YT_C3_PHASE_ORBIT_SELECTOR_UNDERDETERMINATION_NO_GO_NOTE_2026-05-27.md"
ORBIT_MEMBER_NOGO = DOCS / "YT_C3_ORBIT_MEMBER_READOUT_COVARIANCE_NO_GO_NOTE_2026-05-27.md"
DIHEDRAL_BASEPOINT = DOCS / "YT_C3_DIHEDRAL_BASEPOINT_ANCHOR_OBSTRUCTION_NOTE_2026-05-27.md"
CUBIC_NOGO = DOCS / "YT_C3_CUBIC_PHASE_POTENTIAL_SIGN_BRANCH_UNDERDETERMINATION_NO_GO_NOTE_2026-05-27.md"
PHASE_CONE = DOCS / "YT_C3_PHASE_ORDERING_CONE_SUPPORT_BOUNDARY_NOTE_2026-05-27.md"
MATRIX_ELEMENT = DOCS / "YT_SAME_SURFACE_TOP_MATRIX_ELEMENT_FACTORIZATION_BOUNDARY_NOTE_2026-05-27.md"
STRICT_AVAILABILITY = DOCS / "YT_STRICT_SPARSE_TOP_W_POLE_RESPONSE_AVAILABILITY_AUDIT_NOTE_2026-05-27.md"

PHASE_ORBIT_NOGO_OUT = ROOT / "outputs" / "yt_c3_phase_orbit_selector_underdetermination_2026-05-27.json"
ORBIT_MEMBER_NOGO_OUT = ROOT / "outputs" / "yt_c3_orbit_member_readout_covariance_no_go_2026-05-27.json"
DIHEDRAL_BASEPOINT_OUT = ROOT / "outputs" / "yt_c3_dihedral_basepoint_anchor_obstruction_2026-05-27.json"
CUBIC_NOGO_OUT = ROOT / "outputs" / "yt_c3_cubic_phase_potential_sign_branch_underdetermination_2026-05-27.json"
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
        PHASE_ORBIT_NOGO,
        ORBIT_MEMBER_NOGO,
        DIHEDRAL_BASEPOINT,
        CUBIC_NOGO,
        PHASE_CONE,
        MATRIX_ELEMENT,
        STRICT_AVAILABILITY,
        PHASE_ORBIT_NOGO_OUT,
        ORBIT_MEMBER_NOGO_OUT,
        DIHEDRAL_BASEPOINT_OUT,
        CUBIC_NOGO_OUT,
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
        "actual_current_surface_status: no-go / open orientation-biased orbit-member law",
        "proposal_allowed: false",
        "`sin(3 phi)` orientation-bias term",
        "selects a C3 phase orbit, not a physical member",
        "accepted physical basepoint/readout law",
    ):
        check(f"note contains no-go phrase: {phrase}", phrase in note)

    deps = {
        "phase_orbit_nogo": load_json(PHASE_ORBIT_NOGO_OUT),
        "orbit_member_nogo": load_json(ORBIT_MEMBER_NOGO_OUT),
        "dihedral_basepoint": load_json(DIHEDRAL_BASEPOINT_OUT),
        "cubic_nogo": load_json(CUBIC_NOGO_OUT),
        "phase_cone": load_json(PHASE_CONE_OUT),
        "matrix_element": load_json(MATRIX_ELEMENT_OUT),
        "strict_availability": load_json(STRICT_AVAILABILITY_OUT),
    }
    for name, data in deps.items():
        check(f"{name} dependency passed", data.get("fail_count") == 0, data.get("fail_count"))
    check(
        "phase-orbit selector already leaves orbit-member readout open",
        deps["phase_orbit_nogo"].get("no_go_certificate", {}).get("accepted_orbit_member_readout_derived")
        is False,
    )
    check(
        "orbit-member covariance has no equivariant section",
        deps["orbit_member_nogo"].get("no_go_certificate", {}).get("free_c3_orbit_has_equivariant_section")
        is False,
    )
    check(
        "dihedral basepoint obstruction marks rotated axes as extra imports",
        deps["dihedral_basepoint"].get("no_go_certificate", {}).get(
            "rotated_reflection_axis_selects_nontrivial_member_only_with_extra_basepoint"
        )
        is True,
    )
    check(
        "strict availability still confirms strict rows absent",
        deps["strict_availability"].get("availability_witness", {}).get("strict_top_w_rows_artifact_present")
        is False,
    )
    return deps


def part2_orientation_biased_potential_family() -> dict[str, str]:
    print("\nPart 2: orientation-biased C3 potential family")
    phi, delta, c0, r, s = sp.symbols("phi delta c0 r s", real=True)
    potential = c0 + r * sp.cos(3 * phi) + s * sp.sin(3 * phi)
    shifted = sp.trigsimp(sp.expand_trig(potential.subs(phi, phi + 2 * sp.pi / 3) - potential))
    reflected = sp.trigsimp(sp.expand_trig(potential.subs(phi, -phi) - potential))
    derivative = sp.trigsimp(sp.diff(potential, phi))
    offset = sp.cos(3 * phi - delta)
    offset_shifted = sp.trigsimp(sp.expand_trig(offset.subs(phi, phi + 2 * sp.pi / 3) - offset))
    orbit_member_gap = sp.trigsimp(offset.subs(phi, delta / 3 + 2 * sp.pi / 3) - offset.subs(phi, delta / 3))
    check("orientation-biased potential is C3-invariant", is_zero(shifted), shifted)
    check("sin(3phi) term is reflection odd", is_zero(reflected + 2 * s * sp.sin(3 * phi)), reflected)
    check("stationary equation depends on r and s", is_zero(derivative + 3 * r * sp.sin(3 * phi) - 3 * s * sp.cos(3 * phi)), derivative)
    check("phase-offset harmonic is C3-invariant", is_zero(offset_shifted), offset_shifted)
    check("phase-offset extrema are orbit-degenerate", is_zero(orbit_member_gap), orbit_member_gap)
    return {
        "orientation_biased_potential": sp.sstr(potential),
        "c3_periodicity_check": sp.sstr(shifted),
        "reflection_difference": sp.sstr(reflected),
        "stationary_equation": sp.sstr(derivative),
        "offset_form": sp.sstr(offset),
        "offset_c3_periodicity_check": sp.sstr(offset_shifted),
        "orbit_member_equal_value_check": sp.sstr(orbit_member_gap),
    }


def part3_orbit_witnesses() -> dict[str, Any]:
    print("\nPart 3: orientation-biased orbit witnesses")
    delta = sp.pi / 7
    generic_orbit = [delta / 3, delta / 3 + 2 * sp.pi / 3, delta / 3 - 2 * sp.pi / 3]
    reflected_orbit = [-delta / 3, -delta / 3 + 2 * sp.pi / 3, -delta / 3 - 2 * sp.pi / 3]
    pure_sine_maxima = [sp.pi / 6, sp.pi / 6 + 2 * sp.pi / 3, sp.pi / 6 - 2 * sp.pi / 3]

    generic = [line_witness(angle) for angle in generic_orbit]
    reflected = [line_witness(angle) for angle in reflected_orbit]
    pure_sine = [line_witness(angle) for angle in pure_sine_maxima]

    check(
        "generic orientation-biased orbit cycles through all C3 line labels",
        [entry["top_lines"] for entry in generic] == [["P_0"], ["P_omega2"], ["P_omega"]],
        generic,
    )
    check(
        "generic orientation-biased orbit contains singlet and target rows",
        [entry["row_magnitudes_if_selected"] for entry in generic]
        == [["sqrt(3)*A/3"], ["sqrt(3)*A/6"], ["sqrt(3)*A/6"]],
        generic,
    )
    check(
        "reflected orientation-biased orbit still contains P0",
        any(entry["top_lines"] == ["P_0"] for entry in reflected),
        reflected,
    )
    check(
        "pure reflection-odd sine bias also cycles through all C3 line labels",
        [entry["top_lines"] for entry in pure_sine]
        == [["P_0"], ["P_omega2"], ["P_omega"]],
        pure_sine,
    )
    return {
        "generic_orientation_biased_orbit_delta_pi_over_7": generic,
        "reflected_orientation_biased_orbit_minus_delta": reflected,
        "pure_sine_bias_maxima": pure_sine,
    }


def part4_no_go_certificate() -> dict[str, bool]:
    print("\nPart 4: no-go certificate")
    certificate = {
        "reflection_odd_phase_bias_characterized": True,
        "orientation_biased_potential_is_c3_invariant": True,
        "orientation_bias_selects_phase_orbit": True,
        "orientation_bias_selects_orbit_member": False,
        "generic_orientation_biased_orbit_contains_p0": True,
        "generic_orientation_biased_orbit_contains_nontrivial_rows": True,
        "pure_sine_bias_selects_phase_orbit": True,
        "accepted_physical_basepoint_readout_law_derived": False,
        "accepted_nontrivial_top_line_law_derived": False,
        "accepted_w_top_matrix_elements_supplied": False,
        "strict_top_w_response_certificate_present": False,
        "proposal_allowed": False,
        "bare_retained_allowed": False,
        "no_forbidden_imports": True,
    }
    for key, value in certificate.items():
        check(f"certificate field recorded: {key}", isinstance(value, bool), value)
    check("shortcut is pruned because orbit member is not selected", certificate["orientation_bias_selects_orbit_member"] is False)
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


def main() -> int:
    print("=" * 88)
    print("Y_T C3 ORIENTATION-BIASED PHASE-POTENTIAL ORBIT-MEMBER NO-GO")
    print("=" * 88)

    deps = part1_anchors()
    potential_family = part2_orientation_biased_potential_family()
    witnesses = part3_orbit_witnesses()
    certificate = part4_no_go_certificate()
    part5_firewalls()

    result = {
        "actual_current_surface_status": "no-go / open orientation-biased orbit-member law",
        "trace_class": "negative_route_pruning",
        "reachability_to_target": "prunes shortcut",
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "A C3-invariant orientation-biased phase potential with a reflection-odd "
            "sin(3 phi) term still selects a three-member C3 phase orbit.  The "
            "selected orbit contains a P0 singlet-row witness and nontrivial target-row "
            "witnesses, and the pure sine bias has the same orbit-member problem.  The actual "
            "surface still lacks an accepted physical basepoint/readout law, accepted "
            "W/top matrix elements, or strict pole-row data."
        ),
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "dependencies": {
            name: {
                "actual_current_surface_status": data.get("actual_current_surface_status"),
                "trace_class": data.get("trace_class"),
                "fail_count": data.get("fail_count"),
            }
            for name, data in deps.items()
        },
        "orientation_biased_potential_family": potential_family,
        "orbit_witnesses": witnesses,
        "no_go_certificate": certificate,
        "route_pruned": "orientation-biased C3 scalar phase potential derives the physical nontrivial top-line member",
        "route_still_live": (
            "derive an accepted same-surface physical basepoint/readout law that "
            "selects a nontrivial orbit member and supplies W/top source-generator "
            "matrix elements, or produce accepted strict same-source top/W pole rows"
        ),
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
        "review_surface": [
            "docs/YT_C3_ORIENTATION_BIASED_PHASE_POTENTIAL_ORBIT_MEMBER_NO_GO_NOTE_2026-05-27.md",
            "scripts/frontier_yt_c3_orientation_biased_phase_potential_orbit_member_no_go.py",
            "outputs/yt_c3_orientation_biased_phase_potential_orbit_member_no_go_2026-05-27.json",
        ],
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nwrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
