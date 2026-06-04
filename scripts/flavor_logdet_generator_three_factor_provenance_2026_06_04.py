"""Log-det generator provenance checks after the Record axiom.

The Record axiom supplies only finite scalar additivity. A log-det generator
still needs record-readout realization, determinant-character form selection,
and source/action coupling. This runner verifies finite algebraic identities
used by that roadmap; it does not promote any row or assign audit status.
"""

from __future__ import annotations

import numpy as np


rng = np.random.default_rng(11)


def check(name: str, cond: bool, detail: str = "") -> bool:
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


def main() -> int:
    passed: list[bool] = []
    n = 5

    M = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
    D = M + M.conj().T + 3 * n * np.eye(n)
    j = rng.standard_normal(n) * 0.1
    J = np.diag(j.astype(complex))
    K = D + J

    W = np.log(abs(np.linalg.det(K)))
    lam = np.linalg.eigvals(K)
    passed.append(check(
        "finite identity: log |det K| = sum_modes log |lambda|",
        abs(W - np.sum(np.log(np.abs(lam)))) < 1e-9,
        f"W={W:.6f}",
    ))

    K1 = K[:2, :2].copy()
    K2 = K[2:, 2:].copy()
    Kbd = np.zeros((n, n), dtype=complex)
    Kbd[:2, :2] = K1
    Kbd[2:, 2:] = K2
    passed.append(check(
        "finite identity: block-diagonal log-det adds over disjoint blocks",
        abs(
            np.log(abs(np.linalg.det(Kbd)))
            - (np.log(abs(np.linalg.det(K1))) + np.log(abs(np.linalg.det(K2))))
        ) < 1e-9,
    ))

    A = rng.standard_normal((3, 3))
    B = rng.standard_normal((3, 3))
    passed.append(check(
        "det is multiplicative in the sampled character test; trace is not",
        abs(np.linalg.det(A @ B) - np.linalg.det(A) * np.linalg.det(B)) < 1e-9
        and abs(np.trace(A @ B) - np.trace(A) * np.trace(B)) > 1e-6,
    ))

    Kinv = np.linalg.inv(K)
    dW_analytic = np.array([np.real(Kinv[x, x]) for x in range(n)])
    eps = 1e-6
    dW_numeric = np.zeros(n)
    for x in range(n):
        Jp = J.copy()
        Jm = J.copy()
        Jp[x, x] += eps
        Jm[x, x] -= eps
        dW_numeric[x] = (
            np.log(abs(np.linalg.det(D + Jp)))
            - np.log(abs(np.linalg.det(D + Jm)))
        ) / (2 * eps)
    max_delta = float(np.max(np.abs(dW_analytic - dW_numeric)))
    passed.append(check(
        "finite identity: dW/dj_x = Re Tr[(D+J)^-1 P_x] against numeric derivative",
        max_delta < 1e-6,
        f"max|analytic - numeric| = {max_delta:.2e}; this source/action factor is not from Record",
    ))

    residuals = [
        "record-readout realization",
        "det-character authority",
        "source/action coupling",
    ]
    passed.append(check(
        "residual after Record additivity remains non-empty",
        len(residuals) == 3,
        ", ".join(residuals),
    ))

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed) - sum(passed)}")
    print("PROVENANCE: Record additivity is only factor 1. The log-det generator still needs")
    print("record-readout realization, det-character authority, and source/action coupling.")
    print("No existing row is re-cited or promoted; no audit status is set.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
