#!/usr/bin/env python3
"""Boundary runner for the narrowed Yukawa color-projection theorem.

The row intentionally proves only the SU(N_c) representation channel fraction

    dim(adj) / dim(N_c tensor N_c-bar) = (N_c^2 - 1) / N_c^2,

and explicitly does not claim a dynamical trace ratio, Higgs wave-function
factor, physical Yukawa correction, or top-mass prediction. This runner checks
both the finite-dimensional Fierz algebra and the source-note boundary.
"""

from __future__ import annotations

import math
from fractions import Fraction
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "YUKAWA_COLOR_PROJECTION_THEOREM.md"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{status}] {name}{suffix}")


def section(name: str) -> None:
    print()
    print("-" * 88)
    print(name)
    print("-" * 88)


def read_note() -> str:
    return NOTE.read_text(encoding="utf-8")


def su_n_generators(n: int) -> list[np.ndarray]:
    """Standard SU(N) generators with Tr[t^A t^B] = delta_AB/2."""
    gens: list[np.ndarray] = []

    for j in range(n):
        for k in range(j + 1, n):
            t = np.zeros((n, n), dtype=complex)
            t[j, k] = 0.5
            t[k, j] = 0.5
            gens.append(t)

    for j in range(n):
        for k in range(j + 1, n):
            t = np.zeros((n, n), dtype=complex)
            t[j, k] = -0.5j
            t[k, j] = 0.5j
            gens.append(t)

    for ell in range(1, n):
        diag = [1.0] * ell + [-float(ell)] + [0.0] * (n - ell - 1)
        norm = 1.0 / math.sqrt(2.0 * ell * (ell + 1))
        gens.append(np.diag([norm * value for value in diag]).astype(complex))

    return gens


def part1_source_boundary() -> None:
    section("Part 1: source boundary")
    note = read_note()
    note_flat = " ".join(note.split())
    check(
        "new source-boundary title is present",
        "# Yukawa Color-Projection Channel-Fraction Theorem" in note,
    )
    check(
        "dedicated runner is named",
        "scripts/frontier_yukawa_color_projection_boundary.py" in note,
    )
    check(
        "claim scope is representation-dimension fraction only",
        "representation-dimension fraction" in note
        and "not a dynamical trace fraction" in note_flat
        and "not a physical Yukawa" in note_flat,
    )
    check(
        "explicit non-claims section is present",
        "## Explicit Non-Claims" in note,
    )
    check(
        "physical matching bridge is explicitly out of scope",
        "must separately derive the physical readout/matching map" in note,
    )


def part2_dependency_boundary() -> None:
    section("Part 2: dependency boundary")
    note = read_note()
    required_links = [
        "EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md",
        "NATIVE_GAUGE_CLOSURE_NOTE.md",
        "GRAPH_FIRST_SU3_INTEGRATION_NOTE.md",
    ]
    for link in required_links:
        check(f"required dependency is linked: {link}", f"]({link})" in note)

    excluded = [
        "RCONN_DERIVED_NOTE.md",
        "YT_EW_COLOR_PROJECTION_THEOREM.md",
        "EW_CURRENT_MATCHING_OZI_SUPPRESSION_THEOREM_NOTE_2026-04-27.md",
    ]
    for name in excluded:
        check(
            f"excluded historical node is not markdown-linked: {name}",
            f"]({name})" not in note,
        )


def part3_no_physical_yukawa_assertions() -> None:
    section("Part 3: no physical matching assertions")
    note = read_note()
    forbidden_positive_claims = [
        "y_t^{phys} =",
        "Z_phi =",
        "Z_phi^{phys} / Z_phi^{lattice}",
        "m_t(pole",
        "172.57",
        "Ward BC",
        "sqrt(Z_phi)",
    ]
    for phrase in forbidden_positive_claims:
        check(f"forbidden positive-claim phrase absent: {phrase}", phrase not in note)


def part4_su_n_generators() -> None:
    section("Part 4: SU(N_c) generator normalization")
    for n in (2, 3, 4, 5):
        gens = su_n_generators(n)
        check(f"N_c={n}: generator count is N_c^2 - 1", len(gens) == n * n - 1)
        max_diag = 0.0
        max_offdiag = 0.0
        max_trace = 0.0
        max_hermitian = 0.0
        for a, ta in enumerate(gens):
            max_trace = max(max_trace, abs(np.trace(ta)))
            max_hermitian = max(max_hermitian, float(np.max(np.abs(ta - ta.conj().T))))
            for b, tb in enumerate(gens):
                tr = np.trace(ta @ tb)
                if a == b:
                    max_diag = max(max_diag, abs(tr - 0.5))
                else:
                    max_offdiag = max(max_offdiag, abs(tr))
        check(
            f"N_c={n}: traceless Hermitian generators",
            max_trace < 1e-12 and max_hermitian < 1e-12,
            f"trace={max_trace:.2e}, herm={max_hermitian:.2e}",
        )
        check(
            f"N_c={n}: Tr[tA tB] = delta_AB/2",
            max_diag < 1e-12 and max_offdiag < 1e-12,
            f"diag={max_diag:.2e}, offdiag={max_offdiag:.2e}",
        )


def part5_fierz_completeness() -> None:
    section("Part 5: Fierz completeness")
    rng = np.random.default_rng(20260524)
    for n in (2, 3, 4, 5):
        gens = su_n_generators(n)
        max_err = 0.0
        for _ in range(20):
            m = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
            lhs = float(np.real(np.trace(m.conj().T @ m)))
            singlet = abs(np.trace(m)) ** 2 / n
            adjoint = 2.0 * sum(abs(np.trace(m @ t)) ** 2 for t in gens)
            max_err = max(max_err, abs(lhs - (singlet + adjoint)))
        close = math.isclose(max_err, 0.0, abs_tol=1e-10)
        check(
            f"N_c={n}: Tr[M†M] decomposes into singlet plus adjoint",
            close,
            f"max_err={max_err:.2e}",
        )


def part6_exact_fraction() -> None:
    section("Part 6: exact channel fractions")
    for n in (2, 3, 4, 5):
        adj = Fraction(n * n - 1, n * n)
        singlet = Fraction(1, n * n)
        check(
            f"N_c={n}: singlet + adjoint fractions sum to 1",
            singlet + adj == 1,
            f"{singlet} + {adj}",
        )
    check("N_c=3: adjoint fraction is exactly 8/9", Fraction(8, 9) == Fraction(3 * 3 - 1, 3 * 3))
    check("N_c=3: singlet fraction is exactly 1/9", Fraction(1, 9) == Fraction(1, 3 * 3))


def main() -> int:
    print("=" * 88)
    print("Yukawa color-projection channel-fraction boundary verification")
    print("=" * 88)
    part1_source_boundary()
    part2_dependency_boundary()
    part3_no_physical_yukawa_assertions()
    part4_su_n_generators()
    part5_fierz_completeness()
    part6_exact_fraction()
    print()
    print("=" * 88)
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print("=" * 88)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
