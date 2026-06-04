"""Conditional log-det form sanity checks.

Record supplies finite scalar additivity only after a record-readout surface is
specified. The determinant-character authority is separate. This runner checks
the finite algebra behind the conditional statement:

    specified scalar-record additivity + separate det-character form
    => additive image W = c log |det|.

It does not prove the determinant-character theorem, does not identify a
source/action bridge, and sets no audit status.
"""

from __future__ import annotations

import numpy as np


rng = np.random.default_rng(7)


def check(name: str, cond: bool, detail: str = "") -> bool:
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


def rand(n: int) -> np.ndarray:
    return rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))


def block_diag(*blocks: np.ndarray) -> np.ndarray:
    size = sum(block.shape[0] for block in blocks)
    out = np.zeros((size, size), dtype=complex)
    cursor = 0
    for block in blocks:
        n = block.shape[0]
        out[cursor:cursor + n, cursor:cursor + n] = block
        cursor += n
    return out


def main() -> int:
    passed: list[bool] = []

    A, B, C = rand(3), rand(3), rand(2)

    passed.append(check(
        "det is multiplicative on sampled invertible matrices; trace is not",
        abs(np.linalg.det(A @ B) - np.linalg.det(A) * np.linalg.det(B)) < 1e-9
        and abs(np.trace(A @ B) - np.trace(A) * np.trace(B)) > 1e-6,
    ))

    powers = (0.5, 1.0, 2.0, 3.0)
    passed.append(check(
        "sample determinant powers multiply, illustrating the separate det-character family",
        all(
            abs(np.linalg.det(A @ B) ** p
                - (np.linalg.det(A) ** p) * (np.linalg.det(B) ** p)) < 1e-6
            for p in powers
        ),
        "uniqueness of this family is cited from the separate det-character note, not proved here",
    ))

    ab = block_diag(A, B)
    passed.append(check(
        "det(A (+) B) = det(A) det(B) over disjoint blocks",
        abs(np.linalg.det(ab) - np.linalg.det(A) * np.linalg.det(B)) < 1e-9,
    ))

    pow_multiplies = all(
        abs(abs(np.linalg.det(ab)) ** p
            - (abs(np.linalg.det(A)) ** p) * (abs(np.linalg.det(B)) ** p)) < 1e-6
        for p in (0.5, 1.0, 2.0, 3.7)
    )
    log_adds = abs(
        np.log(abs(np.linalg.det(ab)))
        - (np.log(abs(np.linalg.det(A))) + np.log(abs(np.linalg.det(B))))
    ) < 1e-9
    passed.append(check(
        "raw |det|^p multiplies across blocks, while log |det| is additive",
        pow_multiplies and log_adds,
        "Record supplies only the additivity rule for an already specified scalar record functional",
    ))

    abc = block_diag(A, B, C)
    additive_three = abs(
        np.log(abs(np.linalg.det(abc)))
        - sum(np.log(abs(np.linalg.det(M))) for M in (A, B, C))
    ) < 1e-9
    passed.append(check(
        "log |det| additivity holds over three disjoint blocks",
        additive_three,
    ))

    H = A + A.conj().T
    lam = np.linalg.eigvalsh(H)
    passed.append(check(
        "log |det H| equals sum_modes log |lambda| for a finite Hermitian example",
        abs(np.log(abs(np.linalg.det(H))) - np.sum(np.log(np.abs(lam)))) < 1e-9,
    ))

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed) - sum(passed)}")
    print("CONDITIONAL FORM: once a finite scalar record surface and separate det-character")
    print("authority are supplied, Record-compatible additivity selects W = c log |det|.")
    print("Record alone supplies no log-det, source/action, Born weight, value, or bounded status.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
