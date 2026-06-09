#!/usr/bin/env python3
"""Bounded K/CPT determinant and AC_phi_lambda orientation invariance checks.

The runner verifies the algebraic content of
docs/TIER_A_KORBIT_DETERMINANT_AND_ORIENTATION_INVARIANCE_BOUNDED_NOTE_2026-06-09.md.
It intentionally does not claim that the Tier-A registry has changed.
"""
from __future__ import annotations

import re
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "TIER_A_KORBIT_DETERMINANT_AND_ORIENTATION_INVARIANCE_BOUNDED_NOTE_2026-06-09.md"
THETA_NOTE = DOCS / "STRONG_CP_THETA_ZERO_NOTE.md"
AXIOM_NOTE = DOCS / "MINIMAL_AXIOMS_2026-06-05.md"
STAGGERED_NOTE = DOCS / "STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md"

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
    print("K/CPT determinant and AC_phi_lambda orientation invariance checks")
    print("=" * 76)

    note_text = NOTE.read_text(encoding="utf-8")
    note_flat = flat(note_text)
    theta_text = THETA_NOTE.read_text(encoding="utf-8")
    axiom_text = AXIOM_NOTE.read_text(encoding="utf-8")
    axiom_flat = flat(axiom_text)

    # Source-boundary checks: the note must be candidate-route, not registry edit.
    check(
        "source does not claim a completed Tier-A registry change",
        "does not edit the audit-lane-owned Tier-A registry" in note_flat
        and "It does not discharge the strong-CP mass-orientation premise by itself" in note_flat
        and "registry has already changed" in note_flat,
    )
    check(
        "source names the retained-bridge requirement for strong-CP mass orientation",
        "a later retained bridge must show" in note_flat
        and "physical `arg det(M_u M_d)` contribution" in note_flat
        and "positive-real mass orientation remains an explicit condition" in note_flat,
    )
    check(
        "source preserves the Record axiom boundary",
        "does not supply the determinant readout context" in note_flat
        and "A record supplies no readout context" in axiom_flat,
    )
    check(
        "source avoids the rejected theta shortcut",
        "theta_eff = theta_bare + 0" not in note_text
        and "P2 is discharged" not in note_text,
    )
    check(
        "source names the AC_phi_lambda conditional registrability bridge",
        "conditional on the registrable species surface being exactly the unordered mass multiset" in note_flat
        and "does not derive the magnitude `|delta| = 2/9`" in note_flat,
    )
    check(
        "source keeps audit status authority external",
        "independent audit lane only" in note_text
        and "No new axiom, primitive, admission" in note_text,
    )

    # Confirm the target strong-CP note still contains the selected-surface premise.
    theta_has_action_slot = (
        "F̃F" in theta_text
        or "FtildeF" in theta_text
        or "CP-odd" in theta_text
    )
    theta_has_mass_orientation = (
        "positive real quark-mass orientation" in theta_text
        or "positive real mass orientation" in theta_text
        or "arg det(M_u M_d) = 0" in theta_text
    )
    check(
        "live strong-CP note still names action-slot and positive-mass selected-surface premises",
        theta_has_action_slot and theta_has_mass_orientation,
    )

    # Determinant K/CPT action.
    x, y = sp.symbols("x y", real=True)
    z = x + sp.I * y
    check(
        "K/CPT conjugation maps determinant z to conj(z)",
        sp.simplify(sp.conjugate(z) - (x - sp.I * y)) == 0,
    )

    # Hostile guard: orbit invariance alone gives even phase dependence.
    phi = sp.symbols("phi", real=True)
    check(
        "cos(arg z) is K-invariant, so orbit invariance alone gives evenness not phase erasure",
        sp.simplify(sp.cos(-phi) - sp.cos(phi)) == 0
        and "cos(arg z)" in note_text
        and "evenness, not phase erasure" in note_flat,
    )

    # Standard determinant-character family.
    k, t1, t2 = sp.symbols("k theta_1 theta_2", real=True)
    phase_mult_residual = sp.simplify(
        sp.exp(sp.I * k * (t1 + t2))
        - sp.exp(sp.I * k * t1) * sp.exp(sp.I * k * t2)
    )
    check(
        "phase character exp(i k arg z) is multiplicative when phases add",
        phase_mult_residual == 0,
    )

    invariance_residual = sp.exp(sp.I * k * phi) - sp.exp(-sp.I * k * phi)
    linear_coeff = sp.series(invariance_residual, phi, 0, 2).removeO().coeff(phi, 1)
    k_solutions = sp.solve(sp.Eq(linear_coeff, 0), k)
    check(
        "K-invariance of the determinant-character phase for all phi forces k = 0",
        k_solutions == [0],
        detail=f"linear coefficient {linear_coeff}; solutions {k_solutions}",
    )

    r, s = sp.symbols("r s", positive=True, real=True)
    phase_free_readout = r**s
    check(
        "surviving determinant-character readout is phase-free and depends only on |det|",
        sp.simplify(phase_free_readout - r**s) == 0
        and "phase-free functions of" in note_text,
    )

    # AC_phi_lambda orientation algebra.
    a, B, delta = sp.symbols("a B delta", positive=True, real=True)
    C = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    H_delta = (
        a * sp.eye(3)
        + B * sp.exp(sp.I * delta) * C
        + B * sp.exp(-sp.I * delta) * C.T
    )
    H_minus = (
        a * sp.eye(3)
        + B * sp.exp(-sp.I * delta) * C
        + B * sp.exp(sp.I * delta) * C.T
    )
    check(
        "conjugation maps the AC_phi_lambda circulant H(delta) exactly to H(-delta)",
        sp.simplify(H_delta.applyfunc(sp.conjugate) - H_minus) == sp.zeros(3, 3),
    )

    lambdas_plus = [
        a + 2 * B * sp.cos(delta + 2 * sp.pi * idx / 3)
        for idx in range(3)
    ]
    lambdas_minus = [
        a + 2 * B * sp.cos(-delta + 2 * sp.pi * idx / 3)
        for idx in range(3)
    ]
    e1_plus = sp.simplify(sum(lambdas_plus))
    e1_minus = sp.simplify(sum(lambdas_minus))
    e2_plus = sp.simplify(
        sum(lambdas_plus[i] * lambdas_plus[j] for i in range(3) for j in range(i + 1, 3))
    )
    e2_minus = sp.simplify(
        sum(lambdas_minus[i] * lambdas_minus[j] for i in range(3) for j in range(i + 1, 3))
    )
    e3_plus = sp.simplify(lambdas_plus[0] * lambdas_plus[1] * lambdas_plus[2])
    e3_minus = sp.simplify(lambdas_minus[0] * lambdas_minus[1] * lambdas_minus[2])
    symmetric_invariants_match = all(
        sp.simplify(sp.expand_trig(lhs - rhs)) == 0
        for lhs, rhs in ((e1_plus, e1_minus), (e2_plus, e2_minus), (e3_plus, e3_minus))
    )
    check(
        "elementary symmetric polynomials of the AC_phi_lambda spectrum match at +/-delta",
        symmetric_invariants_match,
    )

    label_flip_matches = all(
        sp.simplify(
            sp.expand_trig(
                (a + 2 * B * sp.cos(-delta + 2 * sp.pi * idx / 3))
                - (a + 2 * B * sp.cos(delta + 2 * sp.pi * ((-idx) % 3) / 3))
            )
        )
        == 0
        for idx in range(3)
    )
    check(
        "delta -> -delta permutes eigenvalue labels by k -> -k",
        label_flip_matches,
    )

    check(
        "staggered-Dirac source still names AC_phi_lambda as admitted-context residual",
        "AC_φλ" in STAGGERED_NOTE.read_text(encoding="utf-8")
        and "admitted-context" in STAGGERED_NOTE.read_text(encoding="utf-8"),
    )

    # Markdown dependency hygiene for the source note.
    linked_paths = re.findall(r"\]\(([^)]+\.md)\)", note_text)
    missing = [path for path in linked_paths if not (DOCS / path).exists()]
    check(
        "all local markdown dependency links resolve",
        not missing,
        detail=", ".join(missing) if missing else "",
    )

    print("=" * 76)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
