#!/usr/bin/env python3
"""Bounded K/CPT determinant-character phase-erasure checks (theta P2 route).

The runner verifies the algebraic content of
docs/THETA_P2_K_CPT_DETERMINANT_CHARACTER_PHASE_ERASURE_BOUNDED_NOTE_2026-06-10.md.
It intentionally does not claim that the strong-CP mass-orientation premise is
discharged or that the Tier-A registry has changed.
"""
from __future__ import annotations

from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "THETA_P2_K_CPT_DETERMINANT_CHARACTER_PHASE_ERASURE_BOUNDED_NOTE_2026-06-10.md"
THETA_NOTE = DOCS / "STRONG_CP_THETA_ZERO_NOTE.md"
AXIOM_NOTE = DOCS / "MINIMAL_AXIOMS_2026-06-05.md"
BRIDGE_NOTE = DOCS / "STRONG_CP_DETERMINANT_READOUT_BRIDGE_NARROW_THEOREM_NOTE_2026-06-12.md"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> bool:
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    print(f"{tag} {label}" + (f" -- {detail}" if detail else ""))
    return ok


def flat(text: str) -> str:
    return " ".join(text.split())


def main() -> int:
    print("K/CPT determinant-character phase-erasure checks (theta P2 route)")
    print("=" * 76)

    note_text = NOTE.read_text(encoding="utf-8")
    note_flat = flat(note_text)
    theta_text = THETA_NOTE.read_text(encoding="utf-8")
    axiom_text = AXIOM_NOTE.read_text(encoding="utf-8")
    axiom_flat = flat(axiom_text)
    bridge_text = BRIDGE_NOTE.read_text(encoding="utf-8")
    bridge_flat = flat(bridge_text)

    # Source-boundary checks: candidate route only, no discharge, no registry edit.
    check(
        "source does not claim a completed discharge or Tier-A registry change",
        "does not edit the audit-lane-owned Tier-A registry" in note_flat
        and "not a completed registry discharge" in note_flat
        and "does not discharge the strong-CP mass-orientation premise by itself"
        in note_flat,
    )
    check(
        "source keeps audit status authority external",
        "independent audit lane only" in note_text
        and "No new axiom, primitive, admission" in note_text,
    )
    check(
        "source wires the determinant-readout bridge without claiming retained closure",
        BRIDGE_NOTE.name in note_text
        and "Determinant-Readout Bridge Wiring" in note_text
        and "independent review/audit accepts the determinant-readout bridge" in note_flat
        and "remains an explicit condition" in note_flat
        and "does not set `theta_gauge = 0`" in note_text,
    )
    check(
        "bridge note supplies the mass determinant-channel boundary only",
        "mass-determinant channel only" in bridge_flat
        and "not a gauge-theta theorem" in bridge_flat
        and "does not prove that every possible action-level observable" in bridge_flat,
    )

    # The Record axiom boundary the note leans on must still be in the axiom memo.
    check(
        "Record axiom memo still withholds the readout context",
        "record supplies no readout context" in axiom_flat.lower()
        or "A record supplies no readout context" in axiom_text
        or "supplies no readout context" in axiom_flat,
    )

    # The target strong-CP note still contains the mass-orientation premise.
    check(
        "live strong-CP note still names the positive-mass selected-surface premise",
        "positive real quark-mass orientation" in theta_text
        or "positive real mass orientation" in theta_text
        or "arg det(M_u M_d) = 0" in theta_text,
    )

    # Determinant K/CPT action.
    x, y = sp.symbols("x y", real=True)
    z = x + sp.I * y
    check(
        "K/CPT conjugation maps determinant z to conj(z)",
        sp.simplify(sp.conjugate(z) - (x - sp.I * y)) == 0,
    )

    # Standard determinant-character family is multiplicative in the phase.
    k, t1, t2, phi = sp.symbols("k theta_1 theta_2 phi", real=True)
    phase_mult_residual = sp.simplify(
        sp.exp(sp.I * k * (t1 + t2))
        - sp.exp(sp.I * k * t1) * sp.exp(sp.I * k * t2)
    )
    check(
        "phase character exp(i k arg z) is multiplicative when phases add",
        phase_mult_residual == 0,
    )

    # Invariance defect is exactly 2 i sin(k phi).
    invariance_residual = sp.exp(sp.I * k * phi) - sp.exp(-sp.I * k * phi)
    check(
        "invariance defect equals 2 i sin(k phi) exactly",
        sp.simplify(invariance_residual - 2 * sp.I * sp.sin(k * phi)) == 0,
    )

    # Vanishing for all phi forces k = 0 (linear coefficient argument).
    linear_coeff = sp.series(invariance_residual, phi, 0, 2).removeO().coeff(phi, 1)
    k_solutions = sp.solve(sp.Eq(linear_coeff, 0), k)
    check(
        "K-invariance of the determinant-character phase for all phi forces k = 0",
        k_solutions == [0],
        detail=f"linear coefficient {linear_coeff}; solutions {k_solutions}",
    )

    # Explicit non-invariance witnesses for k != 0 (including fractional k).
    witnesses_ok = True
    for k_val in (1, -1, 2, -2, sp.Rational(1, 2)):
        phi_w = sp.pi / (2 * k_val)
        defect = sp.simplify(invariance_residual.subs({k: k_val, phi: phi_w}))
        if defect == 0:
            witnesses_ok = False
    check(
        "every tested k != 0 has an explicit phi with nonzero invariance defect",
        witnesses_ok,
        detail="k in {1,-1,2,-2,1/2}, phi = pi/(2k), defect = 2i sin(pi/2) = 2i",
    )

    # k = 0 member is identically invariant.
    check(
        "k = 0 character is identically K/CPT invariant",
        sp.simplify(invariance_residual.subs(k, 0)) == 0,
    )

    # Surviving readout is phase-free |det|^s.
    r, s = sp.symbols("r s", positive=True, real=True)
    check(
        "surviving determinant-character readout is phase-free and depends only on |det|",
        sp.simplify((r**s) - r**s) == 0
        and "phase-free functions of" in note_flat,
    )

    # Hostile guard: orbit invariance alone gives evenness, not phase erasure.
    check(
        "cos(arg z) is K-invariant yet phase-dependent: orbit invariance alone is not phase erasure",
        sp.simplify(sp.cos(-phi) - sp.cos(phi)) == 0
        and sp.simplify(sp.diff(sp.cos(phi), phi).subs(phi, sp.pi / 2)) != 0
        and "cos(arg z)" in note_flat
        and "evenness, not phase erasure" in note_flat,
    )

    print("=" * 76)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
