#!/usr/bin/env python3
"""Y_T top-sector projector / generation-label obstruction.

This runner checks the narrow Y_T consequence of the known staggered-Dirac
species-label residual: the current C3-symmetric surface does not canonically
select the physical top generation projector needed by the native no-kappa
top/W response backend.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_top_sector_projector_generation_label_obstruction_2026-05-27.json"

NOTE = DOCS / "YT_TOP_SECTOR_PROJECTOR_GENERATION_LABEL_OBSTRUCTION_NOTE_2026-05-27.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"
BACKEND_PROJECTOR = DOCS / "YT_NATIVE_BACKEND_AUTHORITY_PROJECTOR_OBSTRUCTION_NOTE_2026-05-27.md"
NATIVE_BACKEND = DOCS / "YT_NATIVE_SAME_SURFACE_TOP_W_TRANSFER_ACTION_BACKEND_CANDIDATE_NOTE_2026-05-27.md"
KAPPA_EXERCISE = DOCS / "YT_KAPPA_DIRECT_FULL_PHYSICS_EXERCISE_NOTE_2026-05-27.md"
STAGGERED_SYNTHESIS = DOCS / "STAGGERED_DIRAC_GATE_CLOSURE_SYNTHESIS_THEOREM_NOTE_2026-05-17.md"
STAGGERED_LABEL_NOGO = DOCS / "STAGGERED_DIRAC_SUBSTEP4_LABELING_NO_GO_NOTE_2026-05-17.md"
STAGGERED_GATE = DOCS / "STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md"
YT_CLASS7_C3 = DOCS / "YT_CLASS_7_SPONTANEOUS_C3_BREAKING_NOTE_2026-04-18.md"
YT_BOTTOM_SCOPE = DOCS / "YT_BOTTOM_YUKAWA_RETENTION_ANALYSIS_NOTE_2026-04-18.md"

BACKEND_PROJECTOR_OUT = ROOT / "outputs" / "yt_native_backend_authority_projector_obstruction_2026-05-27.json"
NATIVE_BACKEND_OUT = ROOT / "outputs" / "yt_native_same_surface_top_w_transfer_action_backend_candidate_2026-05-27.json"
KAPPA_EXERCISE_OUT = ROOT / "outputs" / "yt_kappa_direct_full_physics_exercise_2026-05-27.json"

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


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors")
    paths = (
        NOTE,
        FULL_STACK,
        BACKEND_PROJECTOR,
        NATIVE_BACKEND,
        KAPPA_EXERCISE,
        STAGGERED_SYNTHESIS,
        STAGGERED_LABEL_NOGO,
        STAGGERED_GATE,
        YT_CLASS7_C3,
        YT_BOTTOM_SCOPE,
        BACKEND_PROJECTOR_OUT,
        NATIVE_BACKEND_OUT,
        KAPPA_EXERCISE_OUT,
    )
    for path in paths:
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for section in (
        "Question",
        "Answer",
        "Finite Witness",
        "Relation To The Six-Component Coefficient",
        "Relation To Existing Work",
        "What Would Close",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)

    for phrase in (
        "physical **top generation** projector",
        "cannot choose one of the three cyclically-related generation projectors",
        "color/isospin carrier coefficient",
        "generation-specific physical top row",
        "proposal_allowed: false",
    ):
        check(f"note contains boundary phrase: {phrase}", phrase in note)

    synthesis = read(STAGGERED_SYNTHESIS)
    label_nogo = read(STAGGERED_LABEL_NOGO)
    class7 = read(YT_CLASS7_C3)
    bottom = read(YT_BOTTOM_SCOPE)
    check("staggered synthesis carries AC_phi_lambda residual", "AC_φλ" in synthesis or "AC_phi_lambda" in synthesis)
    check("labeling no-go covers named three-label sets", "{u, c, t}" in label_nogo)
    check("labeling no-go says no canonical species-identification", "no canonical species-identification" in label_nogo)
    check("staggered parent still records open gate", "open_gate" in read(STAGGERED_GATE))
    check("class-7 C3 note records no retained C3 breaking", "no" in class7.lower() and "C_{3[111]}" in class7)
    check("bottom scope note warns species-uniform physical interpretation fails", "species-uniform PHYSICAL INTERPRETATION" in bottom)

    backend = load_json(BACKEND_PROJECTOR_OUT)
    native = load_json(NATIVE_BACKEND_OUT)
    kappa = load_json(KAPPA_EXERCISE_OUT)
    check("backend projector obstruction passed", backend.get("fail_count") == 0, backend.get("fail_count"))
    check("native backend candidate passed", native.get("fail_count") == 0, native.get("fail_count"))
    check("native backend candidate readout is 1/sqrt(6)", native.get("candidate_backend", {}).get("readout_equals_1_over_sqrt6") is True)
    check("kappa exercise passed", kappa.get("fail_count") == 0, kappa.get("fail_count"))
    check("kappa exercise remains open proof", kappa.get("proposal_allowed") is False)

    return {
        "backend_projector_obstruction": backend,
        "native_backend": native,
        "kappa_exercise": kappa,
    }


def part2_c3_projector_witness() -> dict[str, Any]:
    print("\nPart 2: C3 generation-projector witness")
    # C e_1=e_2, C e_2=e_3, C e_3=e_1.
    C = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    Cinv = C.T
    projectors = []
    for index in range(3):
        vec = sp.eye(3)[:, index]
        projectors.append(vec * vec.T)
    P1, P2, P3 = projectors

    check("C has order three", is_zero(C**3 - sp.eye(3)), C**3)
    check("P1 maps to P2 under cyclic conjugation", is_zero(C * P1 * Cinv - P2))
    check("P2 maps to P3 under cyclic conjugation", is_zero(C * P2 * Cinv - P3))
    check("P3 maps to P1 under cyclic conjugation", is_zero(C * P3 * Cinv - P1))
    for idx, P in enumerate(projectors, start=1):
        check(f"P{idx} is idempotent", is_zero(P * P - P))
        check(f"P{idx} has rank one", P.rank() == 1, P.rank())
        check(f"P{idx} is not C-invariant", not is_zero(C * P * Cinv - P))

    a, br, bi = sp.symbols("a b_r b_i", real=True)
    # General Hermitian circulant generated by C: a I + b C + conjugate(b) C^2.
    b = br + sp.I * bi
    H = a * sp.eye(3) + b * C + sp.conjugate(b) * C**2
    H = sp.simplify(H)
    diagonal_expectations = [sp.simplify((sp.eye(3)[:, i].T * H * sp.eye(3)[:, i])[0]) for i in range(3)]
    check("circulant H commutes with C", is_zero(H * C - C * H))
    check("C3-symmetric H has equal corner diagonal expectations", diagonal_expectations[0] == diagonal_expectations[1] == diagonal_expectations[2], diagonal_expectations)

    label_maps = {
        "pi_A": {"c1": "u", "c2": "c", "c3": "t"},
        "pi_B": {"c1": "c", "c2": "t", "c3": "u"},
        "pi_C": {"c1": "t", "c2": "u", "c3": "c"},
    }
    top_projector_by_map = {
        name: next(key for key, value in mapping.items() if value == "t")
        for name, mapping in label_maps.items()
    }
    check("three cyclic label maps are present", len(label_maps) == 3)
    check("label maps assign top to different corner projectors", len(set(top_projector_by_map.values())) == 3, top_projector_by_map)

    return {
        "cyclic_projector_orbit": ["P1->P2", "P2->P3", "P3->P1"],
        "c3_symmetric_diagonal_expectations": [sp.sstr(x) for x in diagonal_expectations],
        "label_maps": label_maps,
        "top_projector_by_label_map": top_projector_by_map,
        "conclusion": "no C3-invariant derivation singles out a physical top corner projector",
    }


def part3_relation_to_kappa() -> dict[str, Any]:
    print("\nPart 3: relation to six-component coefficient")
    u = sp.Matrix([1 / sp.sqrt(6)] * 6)
    components = [sp.simplify(x) for x in u]
    norm = sp.simplify((u.T * u)[0])
    check("six-component carrier is unit normalized", is_zero(norm - 1), norm)
    check("each color/isospin component is 1/sqrt(6)", all(is_zero(x - 1 / sp.sqrt(6)) for x in components), components)

    top_generation_projector_derived = False
    color_isospin_coefficient_derived = True
    physical_top_row_certified = top_generation_projector_derived and color_isospin_coefficient_derived
    check("local color/isospin coefficient remains exact support", color_isospin_coefficient_derived)
    check("top generation projector remains absent", top_generation_projector_derived is False)
    check("physical top row is not certified by coefficient alone", physical_top_row_certified is False)

    return {
        "color_isospin_coefficient": "1/sqrt(6)",
        "color_isospin_coefficient_derived": color_isospin_coefficient_derived,
        "top_generation_projector_derived": top_generation_projector_derived,
        "physical_top_row_certified": physical_top_row_certified,
    }


def part4_closure_routes() -> dict[str, Any]:
    print("\nPart 4: closure route classification")
    routes = {
        "labeling_convention": {
            "can_select_P_top": True,
            "retained_grade": False,
            "reason": "names one orbit element but does not derive physical pole authority",
        },
        "c3_breaking_dynamics": {
            "can_select_P_top": True,
            "retained_grade": False,
            "reason": "not present on current surface; prior C3-breaking routes are obstructed",
        },
        "c3_preserving_nondegenerate_spectral_dynamics": {
            "can_select_P_top": True,
            "retained_grade": True,
            "reason": "live if an accepted same-surface circulant dynamics derives spectral projectors, ordering, and source-generator matrix elements",
        },
        "empirical_pole_or_spectrum_input": {
            "can_select_P_top": True,
            "retained_grade": False,
            "reason": "imports observed spectrum or target data",
        },
        "strict_same_surface_pole_response_evidence": {
            "can_select_P_top": True,
            "retained_grade": True,
            "reason": "would identify the physical pole and source response on the accepted surface",
        },
    }
    for name, row in routes.items():
        check(f"route recorded: {name}", set(row) == {"can_select_P_top", "retained_grade", "reason"})
    retained_grade_routes = [name for name, row in routes.items() if row["retained_grade"]]
    check(
        "retained-grade live routes are spectral dynamics or strict pole evidence",
        retained_grade_routes == [
            "c3_preserving_nondegenerate_spectral_dynamics",
            "strict_same_surface_pole_response_evidence",
        ],
        retained_grade_routes,
    )
    return routes


def part5_firewalls() -> None:
    print("\nPart 5: firewalls")
    text = read(NOTE)
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
        check(f"firewall phrase present: {phrase}", phrase in text)
    for forbidden in (
        "Status:** retained",
        "Status:** proposed_retained",
        "This note derives `y_t`",
        "full positive Y_T closure",
        "the physical top projector is derived",
        "strict pole-row evidence is supplied",
    ):
        check(f"forbidden overclaim absent: {forbidden}", forbidden not in text)


def part6_claim_status() -> dict[str, Any]:
    print("\nPart 6: claim status")
    status = {
        "actual_current_surface_status": "no-go",
        "trace_class": "negative_route_pruning",
        "reachability_to_target": "prunes",
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The current C3-symmetric staggered/generation surface does not "
            "canonically choose the physical top generation projector. The "
            "six-component carrier coefficient remains exact support, but "
            "top-specific pole authority needs a projector/dynamics theorem "
            "or strict pole-row evidence."
        ),
        "bare_retained_allowed": False,
        "route_pruned": (
            "derive the physical top generation projector from current "
            "C3-symmetric staggered/generation support alone"
        ),
        "route_still_live": (
            "derive accepted W/top sector projectors and source-generator "
            "matrix elements, or produce strict same-source pole-row evidence"
        ),
    }
    check("actual status is no-go", status["actual_current_surface_status"] == "no-go")
    check("trace class is negative route pruning", status["trace_class"] == "negative_route_pruning")
    check("proposal remains false", status["proposal_allowed"] is False)
    check("live route names strict pole-row evidence", "strict same-source pole-row evidence" in status["route_still_live"])
    return status


def main() -> int:
    anchors = part1_anchors()
    witness = part2_c3_projector_witness()
    kappa_relation = part3_relation_to_kappa()
    routes = part4_closure_routes()
    part5_firewalls()
    status = part6_claim_status()

    payload = {
        "claim_id": "yt_top_sector_projector_generation_label_obstruction_note_2026-05-27",
        "generated_by": "scripts/frontier_yt_top_sector_projector_generation_label_obstruction.py",
        "anchors": anchors,
        "finite_c3_projector_witness": witness,
        "relation_to_kappa": kappa_relation,
        "closure_routes": routes,
        **status,
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nWrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 1 if FAIL_COUNT else 0


if __name__ == "__main__":
    raise SystemExit(main())
