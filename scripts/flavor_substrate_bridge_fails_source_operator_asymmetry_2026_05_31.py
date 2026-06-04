#!/usr/bin/env python3
"""Finite 3x3 operator-collapse algebra for the flavor substrate row.

This repaired runner checks only the explicit matrix identities used by the
narrowed source note. It does not audit single-axiom notes, derive locality,
or close the substrate-necessity bridge.
"""

from __future__ import annotations

import numpy as np

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS, FAIL
    if condition:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    print(f"[{status}] {name}")
    if detail:
        print(f"       {detail}")
    return condition


def q_signed(lams: np.ndarray) -> float:
    lams = np.array(lams, dtype=float)
    return float((lams**2).sum() / (lams.sum() ** 2))


def e_loc(x: np.ndarray) -> np.ndarray:
    return float(np.trace(x) / 3.0) * np.eye(3)


def main() -> int:
    I = np.eye(3)
    C = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=float)
    J = np.ones((3, 3))
    Z = 2.0 * (J / 3.0) - I

    print("=" * 76)
    print("Flavor substrate operator-collapse finite algebra")
    print("=" * 76)
    print("Claim boundary: explicit 3x3 matrices only; no source-domain bridge closure.")
    print()

    source_free = I + 0.0 * Z
    ev0 = np.sort(np.linalg.eigvalsh(source_free))
    check(
        "literal source-free S=I has degenerate spectrum and Q=1/3",
        np.allclose(ev0, [1.0, 1.0, 1.0]) and abs(q_signed(ev0) - 1.0 / 3.0) < 1e-10,
        detail=f"eig={np.round(ev0, 6)}, Q={q_signed(ev0):.6f}",
    )

    b = 1.0 / np.sqrt(2.0)
    H = I + b * C + b * C.T
    ev_h = np.sort(np.linalg.eigvalsh(H))
    check(
        "split circulant H at b=1/sqrt(2) has signed Q=2/3",
        abs(q_signed(ev_h) - 2.0 / 3.0) < 1e-10,
        detail=f"eig={np.round(ev_h, 6)}, Q_signed={q_signed(ev_h):.6f}",
    )

    diag_h = np.diag(np.diag(H))
    ev_diag = np.sort(np.linalg.eigvalsh(diag_h))
    check(
        "onsite projection Diag(H)=I collapses the split operator to Q=1/3",
        np.allclose(diag_h, I) and abs(q_signed(ev_diag) - 1.0 / 3.0) < 1e-10,
        detail=f"Diag(H) eig={np.round(ev_diag, 6)}, Q={q_signed(ev_diag):.6f}",
    )

    z = 0.6
    source_z = I + z * Z
    expected_scalar = (1.0 - z / 3.0) * I
    check(
        "E_loc(I+zZ)=(1-z/3)I is scalar for displayed Z",
        np.allclose(e_loc(source_z), expected_scalar),
        detail=f"z={z}, scalar={1.0 - z / 3.0:.6f}",
    )

    check(
        "operator-collapse contrast is exactly Q=2/3 before projection and Q=1/3 after projection",
        abs(q_signed(ev_h) - 2.0 / 3.0) < 1e-10 and abs(q_signed(ev_diag) - 1.0 / 3.0) < 1e-10,
    )

    print()
    print(f"SCORECARD PASS={PASS} FAIL={FAIL}")
    print("VERDICT: bounded finite-algebra support only. The source-domain carrier/readout")
    print("bridge and broader substrate-necessity conclusion remain outside this packet.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
