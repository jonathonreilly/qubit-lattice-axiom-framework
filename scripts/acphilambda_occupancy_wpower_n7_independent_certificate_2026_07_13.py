#!/usr/bin/env python3
"""Independent N7 certificate for the occupancy determinant-power wall."""

from __future__ import annotations

from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "ACPHILAMBDA_RECORD_OUTCOME_ORBIT_OCCUPANCY_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md"
)
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

PASS = 0
FAIL = 0


def check(label: str, condition: bool) -> None:
    global PASS, FAIL
    if bool(condition):
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    print(f"[{status}] {label}")


def realification(matrix: sp.Matrix) -> sp.Matrix:
    real = matrix.applyfunc(sp.re)
    imag = matrix.applyfunc(sp.im)
    return sp.Matrix.vstack(
        sp.Matrix.hstack(real, -imag),
        sp.Matrix.hstack(imag, real),
    )


def main() -> int:
    print("Independent W_power normalization-steelman certificate")
    print("=" * 60)

    carrier = sp.Matrix([[2 + sp.I, 1], [0, 3 - sp.I]])
    det_c = sp.expand(carrier.det())
    det_abs_sq = sp.expand(det_c * sp.conjugate(det_c))
    det_r = sp.expand(realification(carrier).det())
    f_c = sp.log(det_abs_sq) / 2
    f_r = sp.log(det_r)

    check("finite carrier is invertible", det_c != 0)
    check("realification determinant equals squared complex modulus", det_r == det_abs_sq)
    check(
        "normalization identity F_R/2=F_C holds exactly",
        sp.simplify(f_r / 2 - f_c) == 0,
    )
    check(
        "raw determinant powers remain distinct before normalization",
        det_abs_sq != 1 and sp.simplify(f_r - f_c) != 0,
    )

    note = NOTE.read_text(encoding="utf-8")
    axioms = AXIOMS.read_text(encoding="utf-8")
    check(
        "source declares W_power as the raw determinant-power wall",
        "one wall: `W_power`, the choice of raw determinant power" in note,
    )
    check(
        "accepted axioms withhold source/action identification",
        "source/action and physical-observable identification" in axioms,
    )
    check(
        "accepted axioms require a separate log-det or action bridge",
        "P2/modulus, log-det, source/action, measurement" in axioms,
    )

    if FAIL == 0:
        print(
            "N7_STEELMAN_RESOLUTION W_power remains underdetermined on the "
            "current axiom surface: F_R/2=F_C removes the coordinate factor "
            "two, but the accepted axioms explicitly withhold source/action "
            "and physical-observable identification, so the normalization "
            "convention does not select the physical determinant power."
        )

    print("=" * 60)
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
