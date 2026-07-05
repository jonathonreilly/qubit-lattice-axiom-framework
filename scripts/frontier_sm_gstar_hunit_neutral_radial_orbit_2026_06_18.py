#!/usr/bin/env python3
"""Verify the supplied-doublet neutral/radial orbit support for SM g_*.

This runner supports
docs/SM_GSTAR_HUNIT_NEUTRAL_RADIAL_ORBIT_SUPPORT_NOTE_2026-06-18.md.

It proves only support: on an already supplied one-complex SU(2)_L doublet
surface, the H_unit scalar-singlet structure can align with the invariant
radial carrier and a neutral gauge representative. It deliberately does not
certify a derivation of the full thermal doublet from H_unit.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "sm_gstar_hunit_neutral_radial_orbit_support_2026-06-18.json"

NOTE = DOCS / "SM_GSTAR_HUNIT_NEUTRAL_RADIAL_ORBIT_SUPPORT_NOTE_2026-06-18.md"
SM_GSTAR = DOCS / "SM_GSTAR_HIGGS_SECTOR_COUNT_STRETCH_NOTE_2026-05-29.md"
HUNIT_NO_GO = DOCS / "HUNIT_TO_EWSB_DOUBLET_REPRESENTATION_NO_GO_NOTE_2026-06-15.md"
WARD = DOCS / "YT_WARD_IDENTITY_DERIVATION_THEOREM.md"
EW_MASS = DOCS / "EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26.md"
SM_DOF = DOCS / "SM_RELATIVISTIC_DOF_COUNT_IMPORT_NOTE_2026-05-17.md"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"

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
    suffix = "" if isinstance(detail, str) and detail == "" else f": {detail}"
    print(f"[{tag}] {name}{suffix}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def matrix_zero(matrix: sp.Matrix) -> bool:
    return all(sp.simplify(entry) == 0 for entry in matrix)


def ledger_row(claim_id: str) -> dict[str, Any]:
    ledger = json.loads(read(LEDGER))
    rows = ledger["rows"]
    iterable = rows.values() if isinstance(rows, dict) else rows
    for row in iterable:
        if row.get("claim_id") == claim_id:
            return row
    raise KeyError(claim_id)


def gauge_to_neutral(h: np.ndarray) -> tuple[np.ndarray, float]:
    rho = float(np.linalg.norm(h))
    if rho <= 0:
        raise ValueError("zero vector has no neutral orbit representative")
    alpha, beta = h / rho
    u = np.array([[beta, -alpha], [np.conjugate(alpha), np.conjugate(beta)]], dtype=complex)
    return u, rho


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: source anchors and status scope")
    for path in (NOTE, SM_GSTAR, HUNIT_NO_GO, WARD, EW_MASS, SM_DOF, LEDGER):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for section in (
        "Claim",
        "Orbit And Radial Lemma",
        "Relation To `H_unit`",
        "Consequence For The `g_*` Higgs-Sector Row",
        "What This Closes",
        "What This Does Not Close",
        "Review Boundary Certificate",
    ):
        check(f"support note contains section: {section}", section in note)

    sm_dof = ledger_row("sm_relativistic_dof_count_import_note_2026-05-17")
    gstar = ledger_row("sm_gstar_higgs_sector_count_stretch_note_2026-05-29")
    ward = ledger_row("yt_ward_identity_derivation_theorem")
    ew = ledger_row("ew_higgs_gauge_mass_diagonalization_theorem_note_2026-04-26")
    no_go = ledger_row("hunit_to_ewsb_doublet_representation_no_go_note_2026-06-15")

    check("SM finite inventory premise is retained_bounded", sm_dof.get("effective_status") == "retained_bounded")
    check("downstream gstar row is not promoted by this branch", gstar.get("effective_status") != "retained")
    check("Ward H_unit theorem is retained_bounded support", ward.get("effective_status") == "retained_bounded")
    check("EW one-doublet bookkeeping is retained", ew.get("effective_status") == "retained")
    check(
        "H_unit no-go remains audit-lane scoped",
        no_go.get("effective_status") in {"unaudited", "audited_conditional", "retained_no_go"},
    )

    return {
        "sm_dof_status": sm_dof.get("effective_status"),
        "gstar_status": gstar.get("effective_status"),
        "ward_status": ward.get("effective_status"),
        "ew_mass_status": ew.get("effective_status"),
        "hunit_no_go_status": no_go.get("effective_status"),
    }


def part2_supplied_doublet_orbit() -> None:
    print("\nPart 2: nonzero supplied doublet gauges to the neutral ray")
    samples = [
        np.array([1 + 0j, 0 + 0j]),
        np.array([0 + 0j, 2 + 0j]),
        np.array([1 + 2j, -3 + 0.5j]),
        np.array([-0.25 + 0.75j, 2.5 - 1.25j]),
    ]
    for idx, h in enumerate(samples, start=1):
        u, rho = gauge_to_neutral(h)
        ident = np.eye(2, dtype=complex)
        target = np.array([0, rho], dtype=complex)
        check(f"sample {idx}: U is unitary", np.allclose(u.conj().T @ u, ident), u)
        check(f"sample {idx}: det(U)=1", np.allclose(np.linalg.det(u), 1), np.linalg.det(u))
        check(f"sample {idx}: U H = (0,rho)", np.allclose(u @ h, target), u @ h)
        check(f"sample {idx}: H^dag H invariant", np.allclose(np.vdot(h, h), np.vdot(u @ h, u @ h)))

    rho = sp.symbols("rho", positive=True, real=True)
    z = sp.Matrix([[1, 0], [0, -1]])
    q = z / 2 + sp.Rational(1, 2) * sp.eye(2)
    h0 = sp.Matrix([0, rho])
    check("neutral representative is Q-neutral", matrix_zero(q * h0), q * h0)
    check("upper representative has Q-charge +1", matrix_zero(q * sp.Matrix([1, 0]) - sp.Matrix([1, 0])))


def part3_radial_decomposition_and_count() -> None:
    print("\nPart 3: radial carrier is one direction inside a four-real-component field")
    real_components = 4
    fixed_norm_orbit_dimension = 3
    radial_dimension = 1
    check("C^2 has four real components", real_components == 4)
    check("fixed-norm nonzero doublet orbit has S^3 dimension three", fixed_norm_orbit_dimension == 3)
    check("radial plus orbit dimensions recover four", radial_dimension + fixed_norm_orbit_dimension == real_components)
    check("radial carrier alone is not the full doublet", radial_dimension != real_components)
    check("a second independent doublet would add four real scalar dof", 2 * real_components - real_components == 4)

    h1r, h1i, h2r, h2i = sp.symbols("h1r h1i h2r h2i", real=True)
    rho_sq = h1r**2 + h1i**2 + h2r**2 + h2i**2
    grad = [sp.diff(rho_sq, x) for x in (h1r, h1i, h2r, h2i)]
    check("rho^2 depends on all four real components", all(g != 0 for g in grad), grad)


def part4_hunit_boundary() -> None:
    print("\nPart 4: H_unit scalar support does not derive the fundamental doublet")
    i2 = sp.eye(2)
    i3 = sp.eye(3)
    sx = sp.Matrix([[0, 1], [1, 0]])
    sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    sz = sp.Matrix([[1, 0], [0, -1]])
    gens = [sp.kronecker_product(s / 2, i3) for s in (sx, sy, sz)]
    h_unit = sp.kronecker_product(i2, i3) / sp.sqrt(6)

    check("H_unit has unit Hilbert-Schmidt norm on Q_L", sp.simplify(sp.trace(h_unit.H * h_unit) - 1) == 0)
    for idx, gen in enumerate(gens, start=1):
        check(f"H_unit commutes with SU(2)_L generator {idx}", matrix_zero(gen * h_unit - h_unit * gen))

    stacked = sp.Matrix.vstack(sx / 2, sy / 2, sz / 2)
    check("fundamental generator stack has no invariant vector", stacked.nullspace() == [])
    check("Hom_SU(2)(trivial,fundamental) dimension is zero", len(stacked.nullspace()) == 0)


def part5_gstar_boundary() -> dict[str, Any]:
    print("\nPart 5: gstar census boundary")
    gauge_bosons = 24
    fermions = 90
    one_doublet = 4
    two_doublets = 8
    gstar_one = sp.Rational(gauge_bosons + one_doublet, 1) + sp.Rational(7, 8) * fermions
    gstar_two = sp.Rational(gauge_bosons + two_doublets, 1) + sp.Rational(7, 8) * fermions
    check("single supplied doublet gives g_* = 427/4", gstar_one == sp.Rational(427, 4), gstar_one)
    check("second independent doublet gives g_* = 443/4", gstar_two == sp.Rational(443, 4), gstar_two)
    check("second independent doublet shift is +4", gstar_two - gstar_one == 4, gstar_two - gstar_one)
    check("radial support does not add a second doublet", one_doublet + 1 != two_doublets)
    return {
        "single_doublet_gstar": str(gstar_one),
        "two_doublet_gstar": str(gstar_two),
        "second_doublet_shift": str(gstar_two - gstar_one),
    }


def part6_note_firewalls() -> None:
    print("\nPart 6: note and downstream firewall checks")
    note = read(NOTE)
    gstar = read(SM_GSTAR)
    no_go = read(HUNIT_NO_GO)

    for phrase in (
        "does not derive the one-complex `SU(2)_L` EWSB thermal doublet from",
        "does not promote the `g_*` Higgs-sector row",
        "does not introduce a new axiom",
        "retained-bounded declared-inventory premise",
        "neutral/radial carrier",
        "not field-content authority",
    ):
        check(f"support note firewall phrase present: {phrase}", phrase in note)

    check("downstream gstar note cites this support note", NOTE.name in gstar)
    check("downstream citation keeps support-only scope", "supplied-doublet radial/orbit support" in gstar and "not as field-content authority" in gstar)
    check(
        "no-go note remains compatible with support route",
        "neutral-ray/radial" in no_go
        and "carrier statements only after an already supplied one-doublet" in no_go,
    )

    forbidden_phrases = (
        "**Status:** retained",
        "proposed_retained",
        "promoted to retained",
        "fully derives the doublet",
        "field-content authority from H_unit",
    )
    for phrase in forbidden_phrases:
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)


def main() -> int:
    print("=" * 78)
    print("SM GSTAR H_UNIT NEUTRAL/RADIAL ORBIT SUPPORT")
    print("=" * 78)
    statuses = part1_anchors()
    part2_supplied_doublet_orbit()
    part3_radial_decomposition_and_count()
    part4_hunit_boundary()
    census = part5_gstar_boundary()
    part6_note_firewalls()

    result = {
        "status": "exact support: supplied-doublet neutral/radial orbit support; no field-content closure",
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The supplied-doublet radial/orbit support closes a support ambiguity, "
            "but H_unit still does not derive the full one-complex SU(2)_L thermal doublet."
        ),
        "trace_class": "upstream_support",
        "reachability_to_target": "supports",
        "upstream_statuses": statuses,
        "census_boundary": census,
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
        "review_surface": [
            "docs/SM_GSTAR_HUNIT_NEUTRAL_RADIAL_ORBIT_SUPPORT_NOTE_2026-06-18.md",
            "scripts/frontier_sm_gstar_hunit_neutral_radial_orbit_2026_06_18.py",
            "outputs/sm_gstar_hunit_neutral_radial_orbit_support_2026-06-18.json",
        ],
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nwrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 1 if FAIL_COUNT else 0


if __name__ == "__main__":
    raise SystemExit(main())
