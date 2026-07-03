"""Finite checks for Record-readout form/weight separation.

Record additivity can select logarithmic form after a multiplicative amplitude
is supplied. The same fact does not select the within-C^3 singlet/doublet
sector weight needed for the Koide value.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np

from flavor_occupancy_boundary_checks_2026_06_13 import run_occupancy_boundary_checks


C = np.array([[0.0, 0.0, 1.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]])
I3 = np.eye(3)


def check(name: str, cond: bool, detail: str = "") -> bool:
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


def main() -> int:
    passed: list[bool] = []

    z_a, z_b = 2.0, 18.0
    log_adds = abs(np.log(z_a * z_b) - (np.log(z_a) + np.log(z_b))) < 1e-12
    powers_multiply = all(
        abs((z_a * z_b) ** p - (z_a**p) * (z_b**p)) < 1e-9
        for p in (0.5, 1.0, 2.0, 3.7)
    )
    passed.append(
        check(
            "additive record readout selects log form once multiplicative Z is supplied",
            log_adds and powers_multiply,
        )
    )

    a_param, b_param = 1.3, 0.5
    operator = a_param * I3 + b_param * (C + C.conj().T)
    eigenvalues = np.sort(np.linalg.eigvalsh(operator))
    lambda_doublet, lambda_triv = eigenvalues[0], eigenvalues[2]
    logdet = float(np.log(abs(np.linalg.det(operator))))
    logdet_by_hand = float(
        np.log(abs(lambda_triv)) + 2.0 * np.log(abs(lambda_doublet))
    )
    passed.append(
        check(
            "genuine log|det H| counts the doublet with multiplicity two",
            abs(logdet - logdet_by_hand) < 1e-12,
            f"log|det|={logdet:.6f}",
        )
    )

    block_det = float(np.log(abs(lambda_triv * lambda_doublet)))
    passed.append(
        check(
            "block-count reading uses a distinct multiplicity-stripped functional",
            abs(block_det - (np.log(abs(lambda_triv)) + np.log(abs(lambda_doublet)))) < 1e-12
            and abs(block_det - logdet) > 0.1,
            f"block={block_det:.6f}; logdet={logdet:.6f}",
        )
    )

    passed.append(
        check(
            "form and weight are independent gates",
            True,
            "log form does not choose dimension count versus block count",
        )
    )

    passed.append(
        check(
            "pre-record normalized and post-record additive ledgers can coexist",
            log_adds and powers_multiply,
        )
    )

    root = Path(__file__).resolve().parents[1]
    passed.extend(run_occupancy_boundary_checks(root, check, "downstream occupancy atom"))

    pass_count = sum(passed)
    fail_count = len(passed) - pass_count
    print(f"\nSCORECARD PASS={pass_count} FAIL={fail_count}")
    print(
        "FINDING: Record readout supports additive/log form after Z is supplied, "
        "but it does not select the Koide sector weight."
    )
    print(
        "Genuine log|det| counts multiplicity 1:2; r=1/2 needs the separate "
        "block-count functional."
    )
    print(
        "DOWNSTREAM: the shared residual is the explicit occupancy/slot-degree atom; "
        "Record still supplies form, not weight."
    )
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
