"""Free scalar point-split Ward identity and seagull diagnostic.

This runner is intentionally narrow. It checks a finite nearest-neighbor
free-scalar lattice identity and verifies that the source note carries
guardrails against reading that identity as framework stress-tensor,
cubic-seagull, Belinfante, diffeomorphism, or gravity-sign closure.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "FREE_SCALAR_POINT_SPLIT_WARD_SEAGULL_DIAGNOSTIC_BOUNDED_THEOREM_NOTE_2026-06-08.md"

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


def inverse_propagator(momentum: np.ndarray, mass_squared: float) -> float:
    lattice_momentum = 2.0 * np.sin(momentum / 2.0)
    return float(mass_squared + np.sum(lattice_momentum**2))


def ward_identity_error_count(seed: int = 0) -> tuple[float, int]:
    rng = np.random.default_rng(seed)
    dimension = 4
    mass_squared = 0.37
    max_error = 0.0
    samples = 20_000

    for _ in range(samples):
        p = rng.uniform(-np.pi, np.pi, dimension)
        q = rng.uniform(-np.pi, np.pi, dimension)
        qhat = 2.0 * np.sin(q / 2.0)
        point_split_vertex = 2.0 * np.sin(p + q / 2.0)

        lhs = float(np.dot(qhat, point_split_vertex))
        rhs = inverse_propagator(p + q, mass_squared) - inverse_propagator(p, mass_squared)
        max_error = max(max_error, abs(lhs - rhs))

    return max_error, samples


def seagull_error_count(seed: int = 1) -> tuple[bool, float, int]:
    rng = np.random.default_rng(seed)
    dimension = 4
    mass_squared = 0.37
    max_seagull_error = 0.0
    naive_vertex_fails = False
    samples = 5_000

    for _ in range(samples):
        p = rng.uniform(-np.pi, np.pi, dimension)
        q = rng.uniform(-np.pi, np.pi, dimension)
        qhat = 2.0 * np.sin(q / 2.0)
        point_split_vertex = 2.0 * np.sin(p + q / 2.0)
        naive_vertex = 2.0 * np.sin(p)

        rhs = inverse_propagator(p + q, mass_squared) - inverse_propagator(p, mass_squared)
        naive_residual = float(np.dot(qhat, naive_vertex)) - rhs
        seagull = float(np.dot(qhat, point_split_vertex - naive_vertex))

        naive_vertex_fails = naive_vertex_fails or abs(naive_residual) > 1e-9
        max_seagull_error = max(max_seagull_error, abs(naive_residual + seagull))

    return naive_vertex_fails, max_seagull_error, samples


def note_has_guardrails() -> tuple[bool, list[str]]:
    text = NOTE.read_text(encoding="utf-8")
    required = [
        "Framework-native stress tensor conservation for the actual interacting",
        "explicit cubic three-point Noether seagull",
        "Belinfante symmetrization or emergent rotation invariance",
        "Spin-2 gauge invariance, diffeomorphism closure",
        "exact `Z^3` lattice structure alone supplies a conserved",
    ]
    missing = [phrase for phrase in required if phrase not in text]
    return not missing, missing


def main() -> int:
    print("FREE SCALAR POINT-SPLIT WARD SEAGULL DIAGNOSTIC")
    print("=" * 68)

    ward_error, ward_samples = ward_identity_error_count()
    check(
        "T1: point-split vertex satisfies the free-scalar lattice Ward identity",
        ward_error < 1e-12,
        f"max error over {ward_samples} random momenta = {ward_error:.2e}",
    )

    naive_fails, seagull_error, seagull_samples = seagull_error_count()
    check(
        "T2: naive-current residual equals minus the point-split-minus-naive seagull",
        naive_fails and seagull_error < 1e-12,
        f"naive fails={naive_fails}; max residual+seagull error over {seagull_samples} samples = {seagull_error:.2e}",
    )

    guardrails_ok, missing_guardrails = note_has_guardrails()
    check(
        "T3: source note guardrails prevent reading this as full framework closure",
        guardrails_ok,
        "missing guardrails: " + ", ".join(missing_guardrails) if missing_guardrails else "all required guardrails present",
    )

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    print(
        "SCOPE: free-scalar lattice Ward identity and point-split seagull diagnostic only; "
        "no framework stress-tensor, cubic-seagull, Belinfante, diffeomorphism, or gravity-sign closure is claimed."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
