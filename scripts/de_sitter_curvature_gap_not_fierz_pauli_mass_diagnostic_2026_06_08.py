#!/usr/bin/env python3
"""Curvature-gap diagnostic for the graviton-mass branch.

This runner checks only that a spectral scale proportional to 1/R is an
infrared curvature gap that vanishes in the flat limit. It does not prove
spin-2 gauge invariance, diffeomorphism closure, lambda=1, or the gravity sign.
"""
from __future__ import annotations

import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "DE_SITTER_CURVATURE_GAP_NOT_FIERZ_PAULI_MASS_DIAGNOSTIC_BOUNDED_THEOREM_NOTE_2026-06-08.md"

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS, FAIL
    print(f"[{'PASS' if condition else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    PASS += int(condition)
    FAIL += int(not condition)
    return condition


def mass_energy_ev(radius_m: float) -> float:
    hbar_c_ev_m = 197.3269804e-9
    return math.sqrt(6.0) * hbar_c_ev_m / radius_m


def note_has_guardrails() -> tuple[bool, list[str]]:
    text = NOTE.read_text(encoding="utf-8")
    required = [
        "diagnostic distinction, not a proof",
        "What Remains Open",
        "stress-conservation",
        "lambda=1",
        "sign of the gravitational coupling",
        "No new axiom, primitive, or Tier-A admission",
        "sets no audit status",
        "not a scale-independent Fierz-Pauli mass",
    ]
    missing = [phrase for phrase in required if phrase not in text]
    return not missing, missing


def main() -> int:
    print("DE SITTER CURVATURE GAP NOT FIERZ-PAULI MASS DIAGNOSTIC")
    print("=" * 72)

    c_m_s = 2.99792458e8
    h0_s_inv = 2.2e-18
    radius = c_m_s / h0_s_inv

    mass_at_radius = mass_energy_ev(radius)
    mass_at_larger_radius = mass_energy_ev(1000.0 * radius)
    check(
        "curvature spectral scale is proportional to 1/R and vanishes in the flat limit",
        mass_at_radius > 0.0 and abs(mass_at_larger_radius / mass_at_radius - 1.0e-3) < 1.0e-12,
        f"E_gap(R)={mass_at_radius:.2e} eV; E_gap(1000R)={mass_at_larger_radius:.2e} eV",
    )

    compton_length = radius / math.sqrt(6.0)
    check(
        "Hubble-radius comparator gives a Compton length of order the curvature radius",
        0.1 * radius < compton_length < radius,
        f"R={radius:.2e} m; lambda_C=R/sqrt(6)={compton_length:.2e} m",
    )

    scales = {
        "lab": 1.0,
        "1 AU": 1.495978707e11,
        "galaxy": 1.0e21,
        "cluster": 1.0e23,
        "curvature radius": radius,
    }
    deviations = {name: 1.0 - math.exp(-distance / compton_length) for name, distance in scales.items()}
    check(
        "Yukawa factor from the curvature scale is negligible below cosmological distances",
        deviations["lab"] < 1.0e-9
        and deviations["1 AU"] < 1.0e-6
        and deviations["curvature radius"] > 0.5,
        "deviations: " + ", ".join(f"{name}={value:.2e}" for name, value in deviations.items()),
    )

    guardrails_ok, missing = note_has_guardrails()
    check(
        "source note guardrails block broader gravity-chain closure readings",
        guardrails_ok,
        "missing guardrails: " + ", ".join(missing) if missing else "all required guardrails present",
    )

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    print(
        "SCOPE: a 1/R curvature gap is not a scale-independent Fierz-Pauli mass; "
        "no spin-2, diffeomorphism, lambda, or gravity-sign closure is claimed."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
