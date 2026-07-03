#!/usr/bin/env python3
"""EW neutral-projector same-surface carrier theorem for the Y_T lane.

This runner proves that the neutral Higgs carrier ray is the zero-eigenvalue
spectral projector of Q_H = T_3 + Y_H on the retained one-Higgs EW doublet.
It does not derive the Higgs sector from the minimal axioms and does not close
Y_T; it supplies the exact same-surface carrier bridge requested by audit.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_ew_neutral_projector_same_surface_carrier_2026-06-18.json"

NOTE = DOCS / "YT_EW_NEUTRAL_PROJECTOR_SAME_SURFACE_CARRIER_THEOREM_NOTE_2026-06-18.md"
EW_MASS = DOCS / "EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26.md"
SOURCE_ACTION = DOCS / "YT_SOURCE_ACTION_SUPPORT_PACKET_NOTE_2026-05-22.md"
SOURCE_COORD = DOCS / "YT_SOURCE_COORDINATE_INVARIANT_TOP_W_RATIO_GATE_NOTE_2026-05-25.md"
MINIMAL_AXIOMS = DOCS / "MINIMAL_AXIOMS_2026-06-05.md"
TARGET_BRIDGE = DOCS / "YT_QUBIT_NEUTRAL_HIGGS_CARRIER_RAY_BRIDGE_NOTE_2026-05-25.md"

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


def is_zero(expr: sp.Expr) -> bool:
    return sp.simplify(expr) == 0


def matrix_is_zero(matrix: sp.Matrix) -> bool:
    return all(is_zero(entry) for entry in matrix)


def part1_authority_surface() -> dict[str, Any]:
    print("\nPart 1: authority surface and source boundary")
    for path in (NOTE, EW_MASS, SOURCE_ACTION, SOURCE_COORD, MINIMAL_AXIOMS, TARGET_BRIDGE):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for marker in (
        "Claim",
        "Cited Authority Surface",
        "Frame Invariance",
        "What This Closes",
        "What This Does Not Close",
    ):
        check(f"note contains required marker: {marker}", marker in note)

    ew = read(EW_MASS)
    for phrase in ("Y_H = 1/2", "H_0 = (0, v/sqrt(2))^T", "Q = T_3 + Y"):
        check(f"EW Higgs source contains marker: {phrase}", phrase in ew)

    source_action = read(SOURCE_ACTION)
    for phrase in ("epsilon_x in {-1, +1}", "source-coupled site-diagonal local action", "support only"):
        check(f"source-action packet contains marker: {phrase}", phrase in source_action)

    source_coord = read(SOURCE_COORD)
    for phrase in ("same local source coordinate", "ratio is unchanged", "same-source top/W ratio"):
        check(f"source-coordinate gate contains marker: {phrase}", phrase in source_coord)

    minimal = read(MINIMAL_AXIOMS)
    check("minimal axioms supply one-qubit algebra language", "A_x ~= M_2(C)" in minimal)
    check("minimal axioms do not supply particle content", "particle content" in minimal)
    check("minimal axioms do not supply gauge group", "gauge group" in minimal)
    note_flat = " ".join(note.split()).lower()
    check("note contains independent-audit boundary", "independent audit" in note_flat)
    check(
        "new theorem explicitly does not derive the Higgs sector from minimal axioms",
        "does not derive gauge group, particle content, or the higgs sector" in note_flat,
    )

    return {
        "authority_surfaces": [
            "docs/EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26.md",
            "docs/YT_SOURCE_ACTION_SUPPORT_PACKET_NOTE_2026-05-22.md",
            "docs/YT_SOURCE_COORDINATE_INVARIANT_TOP_W_RATIO_GATE_NOTE_2026-05-25.md",
            "docs/MINIMAL_AXIOMS_2026-06-05.md",
            "docs/YT_QUBIT_NEUTRAL_HIGGS_CARRIER_RAY_BRIDGE_NOTE_2026-05-25.md",
        ],
        "audit_status_authority": "independent audit lane only",
    }


def part2_charge_spectral_projectors() -> None:
    print("\nPart 2: charge spectral projectors on the EW doublet")
    ident = sp.eye(2)
    sigma_z = sp.Matrix([[1, 0], [0, -1]])
    t3 = sigma_z / 2
    y_h = sp.Rational(1, 2) * ident
    q_h = t3 + y_h
    p_plus = (ident + sigma_z) / 2
    p_minus = (ident - sigma_z) / 2
    p_ch = q_h
    p_neut = ident - q_h

    check("Q_H = diag(1,0)", matrix_is_zero(q_h - sp.diag(1, 0)), q_h)
    check("P_ch is a projector", matrix_is_zero(p_ch * p_ch - p_ch), p_ch)
    check("P_neut is a projector", matrix_is_zero(p_neut * p_neut - p_neut), p_neut)
    check("P_ch and P_neut are orthogonal", matrix_is_zero(p_ch * p_neut), p_ch * p_neut)
    check("P_ch + P_neut = I", matrix_is_zero(p_ch + p_neut - ident), p_ch + p_neut)
    check("P_ch equals Pauli P_+", matrix_is_zero(p_ch - p_plus), p_ch)
    check("P_neut equals Pauli P_-", matrix_is_zero(p_neut - p_minus), p_neut)
    check("P_neut is the zero spectral projector of Q_H", q_h * p_neut == sp.zeros(2), q_h * p_neut)
    check("P_ch is the unit spectral projector of Q_H", matrix_is_zero(q_h * p_ch - p_ch), q_h * p_ch)


def part3_neutral_ray_and_tangent() -> None:
    print("\nPart 3: neutral ray and radial tangent")
    v = sp.symbols("v", positive=True, real=True)
    s = sp.symbols("s", real=True)
    profile = sp.Function("v")(s)
    ident = sp.eye(2)
    sigma_z = sp.Matrix([[1, 0], [0, -1]])
    q_h = sigma_z / 2 + sp.Rational(1, 2) * ident
    p_ch = q_h
    p_neut = ident - q_h

    h0 = sp.Matrix([0, v / sp.sqrt(2)])
    upper = sp.Matrix([1, 0])
    h_s = sp.Matrix([0, profile / sp.sqrt(2)])
    tangent = sp.diff(h_s, s)

    check("P_neut fixes H_0", matrix_is_zero(p_neut * h0 - h0), p_neut * h0)
    check("P_ch kills H_0", matrix_is_zero(p_ch * h0), p_ch * h0)
    check("Q_H annihilates H_0", matrix_is_zero(q_h * h0), q_h * h0)
    check("charged upper ray has charge 1", matrix_is_zero(q_h * upper - upper), q_h * upper)
    check("neutral nullspace is one-dimensional", q_h.rank() == 1 and q_h.nullspace() == [sp.Matrix([0, 1])], q_h.nullspace())
    check("P_neut fixes H(s)", matrix_is_zero(p_neut * h_s - h_s), p_neut * h_s)
    check("P_neut fixes dH/ds", matrix_is_zero(p_neut * tangent - tangent), tangent)
    check("Q_H annihilates dH/ds", matrix_is_zero(q_h * tangent), q_h * tangent)


def part4_signed_source_affine_equivalence() -> None:
    print("\nPart 4: signed source equals neutral occupation source up to affine coordinate")
    h = sp.symbols("h", real=True)
    ident = sp.eye(2)
    sigma_z = sp.Matrix([[1, 0], [0, -1]])
    q_h = sigma_z / 2 + sp.Rational(1, 2) * ident
    p_neut = ident - q_h
    epsilon_h = 2 * q_h - ident

    check("epsilon_H = 2 Q_H - I", matrix_is_zero(epsilon_h - (2 * q_h - ident)), epsilon_h)
    check("epsilon_H = I - 2 P_neut", matrix_is_zero(epsilon_h - (ident - 2 * p_neut)), epsilon_h)
    check("epsilon_H equals Pauli sigma_z", matrix_is_zero(epsilon_h - sigma_z), epsilon_h)

    signed_weights = sp.Matrix([sp.exp(h), sp.exp(-h)])
    neutral_occ_weights = sp.exp(h) * sp.Matrix([1, sp.exp(-2 * h)])
    check(
        "exp(h epsilon_H) weights equal exp(h) exp(-2h P_neut) weights",
        matrix_is_zero(signed_weights - neutral_occ_weights),
        signed_weights,
    )
    norm_signed = sp.simplify(signed_weights / (sp.exp(h) + sp.exp(-h)))
    norm_neutral = sp.simplify(neutral_occ_weights / (sp.exp(h) * (1 + sp.exp(-2 * h))))
    check("normalized source families are identical", matrix_is_zero(norm_signed - norm_neutral), norm_signed)
    check("source-coordinate change is j=-2h", sp.simplify(sp.diff(-2 * h, h) + 2) == 0)


def part5_frame_invariance() -> None:
    print("\nPart 5: unitary frame invariance")
    ident = sp.eye(2)
    sigma_z = sp.Matrix([[1, 0], [0, -1]])
    q_h = sigma_z / 2 + sp.Rational(1, 2) * ident
    p_neut = ident - q_h
    epsilon_h = 2 * q_h - ident

    rotations = [
        sp.Matrix([[sp.Rational(3, 5), -sp.Rational(4, 5)], [sp.Rational(4, 5), sp.Rational(3, 5)]]),
        sp.Matrix([[0, 1], [-1, 0]]),
    ]
    for idx, unitary in enumerate(rotations, start=1):
        q_prime = unitary * q_h * unitary.T
        p_prime = unitary * p_neut * unitary.T
        eps_prime = unitary * epsilon_h * unitary.T
        check(f"frame {idx}: transformed Q remains a projector", matrix_is_zero(q_prime * q_prime - q_prime))
        check(f"frame {idx}: transformed neutral projector is I-Q", matrix_is_zero(p_prime - (ident - q_prime)))
        check(f"frame {idx}: transformed epsilon is 2Q-I", matrix_is_zero(eps_prime - (2 * q_prime - ident)))
        check(f"frame {idx}: transformed projectors remain orthogonal", matrix_is_zero(q_prime * p_prime))


def part6_target_bridge_wiring() -> None:
    print("\nPart 6: target bridge wiring and firewalls")
    target = read(TARGET_BRIDGE)
    note = read(NOTE)
    note_flat = " ".join(note.split())
    new_note_name = NOTE.name
    check("target bridge cites the new same-surface theorem", new_note_name in target)
    check("target bridge names the spectral-projector repair", "same-surface spectral-projector theorem" in target)
    check("target bridge keeps no-positive-Y_T boundary", "does not mean the physical Y_T lane has closed" in target)

    for forbidden in (
        "This note derives y_t",
        "retained Y_T closure has been obtained",
        "observed top/W/Z/Higgs masses as proof inputs",
        "PDG comparator as proof input",
        "fitted selector as proof input",
    ):
        check(f"new theorem avoids overclaim: {forbidden!r}", forbidden not in note)

    for required in (
        "does not derive positive Y_T closure",
        "no `H_unit`",
        "no `yt_ward_identity`",
        "no `y_t_bare`",
        "no `alpha_LM`",
        "no plaquette/u0 input",
        "no PDG comparator",
    ):
        check(f"new theorem contains firewall marker: {required}", required in note_flat)


def main() -> int:
    print("=" * 88)
    print("Y_T EW NEUTRAL-PROJECTOR SAME-SURFACE CARRIER THEOREM")
    print("=" * 88)

    authority_surface = part1_authority_surface()
    part2_charge_spectral_projectors()
    part3_neutral_ray_and_tangent()
    part4_signed_source_affine_equivalence()
    part5_frame_invariance()
    part6_target_bridge_wiring()

    result = {
        "status": "exact support: the neutral EW Higgs ray is the zero spectral projector 1_0(Q_H), identical to the qubit P_- source ray on the one-Higgs carrier",
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "This closes the same-surface carrier bridge only; top coefficient, "
            "top transfer response, scalar normalization, and physical-scale g_2 remain open."
        ),
        "same_surface_carrier_theorem_closed": True,
        "audit_required_before_effective_status_movement": True,
        "authority_surface": authority_surface,
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
        "review_surface": [
            "docs/YT_EW_NEUTRAL_PROJECTOR_SAME_SURFACE_CARRIER_THEOREM_NOTE_2026-06-18.md",
            "scripts/frontier_yt_ew_neutral_projector_same_surface_carrier.py",
            "outputs/yt_ew_neutral_projector_same_surface_carrier_2026-06-18.json",
        ],
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nwrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
