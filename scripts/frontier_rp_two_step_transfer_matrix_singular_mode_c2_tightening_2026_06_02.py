#!/usr/bin/env python3
"""Verifier for the RP two-step transfer-matrix singular-mode C2 tightening.

Pair runner for:
docs/RP_TWO_STEP_TRANSFER_MATRIX_SINGULAR_MODE_C2_TIGHTENING_NOTE_2026-06-02.md

This runner checks only the finite algebra at sin(p)=0:
  T_even(m) = [[-2m, 1], [1, 0]]
has one positive and one negative eigenvalue for m > 0, while T_even(m)^2 has
non-negative spectrum. It does not verify a Grassmann/Berezin bridge or claim
that the parent row's conditional audit status lifts.
"""

from __future__ import annotations

import math
import numpy as np


PASS = 0
FAIL = 0
LOG: list[str] = []


def record(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        LOG.append(f"[PASS] {name}" + (f" ({detail})" if detail else ""))
    else:
        FAIL += 1
        LOG.append(f"[FAIL] {name}" + (f" ({detail})" if detail else ""))


def t_even(m: float) -> np.ndarray:
    return np.array([[-2.0 * m, 1.0], [1.0, 0.0]], dtype=float)


def closed_form_eigs(m: float) -> tuple[float, float]:
    root = math.sqrt(m * m + 1.0)
    return (-m - root, -m + root)


def char_poly_value(m: float, lam: float) -> float:
    return lam * lam + 2.0 * m * lam - 1.0


def main() -> None:
    for m in (0.05, 0.1, 0.5, 1.0, 2.0):
        T = t_even(m)
        eigs = sorted(np.linalg.eigvalsh(T).tolist())
        expected = sorted(closed_form_eigs(m))
        max_err = max(abs(a - b) for a, b in zip(eigs, expected))
        record(
            f"closed_form_eigenvalues_m={m}",
            max_err < 1e-12,
            f"got={eigs}, expected={expected}",
        )

        residual = max(abs(char_poly_value(m, lam)) for lam in expected)
        record(
            f"characteristic_polynomial_roots_m={m}",
            residual < 1e-12,
            f"max_residual={residual:.3e}",
        )

        lower, upper = expected
        record(
            f"one_step_indefinite_m={m}",
            lower < 0.0 < upper,
            f"lower={lower:.6g}, upper={upper:.6g}",
        )

        T2 = T @ T
        eigs2 = sorted(np.linalg.eigvalsh(T2).tolist())
        squared_expected = sorted([lower * lower, upper * upper])
        max_sq_err = max(abs(a - b) for a, b in zip(eigs2, squared_expected))
        nonnegative = min(eigs2) >= -1e-12
        record(
            f"two_step_square_nonnegative_m={m}",
            nonnegative and max_sq_err < 1e-12,
            f"T2_eigs={eigs2}",
        )

    print("\n=== RP singular-mode C2 tightening ===\n")
    for line in LOG:
        print(line)
    print(f"\nPASS={PASS}  FAIL={FAIL}\n")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
