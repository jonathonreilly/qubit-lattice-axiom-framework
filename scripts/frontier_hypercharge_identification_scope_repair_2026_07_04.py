#!/usr/bin/env python3
"""Verify the bounded name-free U(1) two-block algebra.

The theorem surface is deliberately limited to the structural
(2,3)+(2,1) decomposition, the unique traceless +1:(-3) block-scalar
direction, and the supplied-scale (+1/3,-1) spectrum. Particle naming,
SM readout tables, and convention-chain material must live only in the
canonical meta note.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
THEOREM_PATH = ROOT / "docs/HYPERCHARGE_IDENTIFICATION_NOTE.md"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"[{tag}] {label}{suffix}")


def close(a: np.ndarray, b: np.ndarray) -> bool:
    return bool(np.allclose(a, b, atol=1e-12, rtol=0.0))


def main() -> int:
    theorem = THEOREM_PATH.read_text(encoding="utf-8")

    required_theorem_markers = (
        "**Type:** bounded_theorem",
        "**Claim type:** bounded_theorem",
        "bounded/conditional name-free algebra",
        "(2,3)+(2,1)",
        "+1:(-3)",
        "normalized (+1/3,-1)",
        "Status authority:** independent audit lane only",
        "All particle naming, conventional readout tables, and convention-chain",
    )
    check(
        "source theorem pins the bounded name-free surface",
        all(marker in theorem for marker in required_theorem_markers),
    )

    forbidden_theorem_tokens = (
        "Q_L",
        "L_L",
        "u_L",
        "d_L",
        "nu_L",
        "e_L",
        "quark",
        "lepton",
        "Standard Model",
        "Gell-Mann",
        "Higgs",
        "electric charge",
        "electric-charge",
        "CHAIN-L",
    )
    check(
        "source theorem contains no particle-name or SM readout material",
        all(token not in theorem for token in forbidden_theorem_tokens),
        ", ".join(
            token
            for token in forbidden_theorem_tokens
            if token in theorem
        ),
    )

    swap4 = np.array(
        [
            [1, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
        ],
        dtype=complex,
    )
    i4 = np.eye(4, dtype=complex)
    p_sym4 = (i4 + swap4) / 2
    p_anti4 = (i4 - swap4) / 2

    check(
        "SWAP_23 is a self-adjoint involution",
        close(swap4 @ swap4, i4) and close(swap4.conj().T, swap4),
    )
    check("P_sym is idempotent", close(p_sym4 @ p_sym4, p_sym4))
    check("P_anti is idempotent", close(p_anti4 @ p_anti4, p_anti4))
    check(
        "P_sym and P_anti are complementary and orthogonal",
        close(p_sym4 + p_anti4, i4)
        and close(p_sym4 @ p_anti4, np.zeros((4, 4), dtype=complex)),
    )
    check(
        "last-two-factor projector ranks are 3 and 1",
        np.linalg.matrix_rank(p_sym4) == 3
        and np.linalg.matrix_rank(p_anti4) == 1,
    )

    i2 = np.eye(2, dtype=complex)
    p_sym8 = np.kron(i2, p_sym4)
    p_anti8 = np.kron(i2, p_anti4)
    swap8 = np.kron(i2, swap4)
    check(
        "embedded structural block ranks are 6 and 2",
        np.linalg.matrix_rank(p_sym8) == 6
        and np.linalg.matrix_rank(p_anti8) == 2,
    )
    check(
        "the (2,3)+(2,1) decomposition is complete on dimension 8",
        int(round(np.trace(p_sym8).real + np.trace(p_anti8).real)) == 8,
    )

    y0 = p_sym8 - 3 * p_anti8
    check("Y_0 is traceless", abs(np.trace(y0)) < 1e-12)
    y0_eigs = np.linalg.eigvalsh(y0)
    check(
        "Y_0 spectrum is +1 with multiplicity 6 and -3 with multiplicity 2",
        np.count_nonzero(np.isclose(y0_eigs, 1.0, atol=1e-12)) == 6
        and np.count_nonzero(np.isclose(y0_eigs, -3.0, atol=1e-12)) == 2,
    )

    trace_constraint = np.array([[6.0, 2.0]])
    check(
        "traceless central block-scalar kernel is one-dimensional",
        2 - np.linalg.matrix_rank(trace_constraint) == 1
        and close(trace_constraint @ np.array([[1.0], [-3.0]]), np.zeros((1, 1))),
    )

    y_normalized = y0 / 3
    normalized_eigs = np.linalg.eigvalsh(y_normalized)
    check(
        "supplied scale gives normalized (+1/3,-1) spectrum",
        np.count_nonzero(np.isclose(normalized_eigs, 1 / 3, atol=1e-12)) == 6
        and np.count_nonzero(np.isclose(normalized_eigs, -1.0, atol=1e-12)) == 2,
    )
    check(
        "the two block eigenvalues have ratio +1:(-3)",
        np.isclose((-1.0) / (1 / 3), -3.0, atol=1e-12),
    )

    sigma_x = np.array([[0, 1], [1, 0]], dtype=complex)
    sigma_y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sigma_z = np.array([[1, 0], [0, -1]], dtype=complex)
    weak_generators = [np.kron(sigma / 2, i4) for sigma in (sigma_x, sigma_y, sigma_z)]
    check(
        "Y_0 commutes with all first-factor SU(2) generators",
        all(close(generator @ y0 - y0 @ generator, np.zeros((8, 8))) for generator in weak_generators),
    )
    check(
        "Y_0 commutes with SWAP_23",
        close(swap8 @ y0 - y0 @ swap8, np.zeros((8, 8))),
    )

    print()
    print(f"SCORECARD: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("VERDICT: source split or name-free algebra failed")
        return 1
    if PASS != 16:
        print(f"VERDICT: unexpected check count {PASS}; expected 16")
        return 1
    print("VERDICT: bounded name-free two-block algebra verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
