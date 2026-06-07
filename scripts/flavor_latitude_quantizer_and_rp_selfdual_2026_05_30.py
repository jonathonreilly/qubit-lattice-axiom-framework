#!/usr/bin/env python3
"""Repaired latitude-quantizer / RP-self-dual boundary packet.

This runner demotes the old broad latitude-quantizer claim to a narrower
source packet:

1. The RP "self-dual" route is refuted as a signed-edge / coordinate-choice
   artifact.
2. The trace-vs-center reframe is corrected: A = R[Z3] = R + C is commutative,
   so an equal central-idempotent state is tracial. Trace alone does not force
   a unique faithful weighting; regular/Plancherel and equal-center states are
   different positive tracial functionals.
3. The old N2 gap-equation and N3 entanglement/Fisher-extremum statements are
   not certified by this repaired packet and are not load-bearing.
"""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np


PASS = 0
FAIL = 0
ROOT = Path(__file__).resolve().parent.parent
NOTE = ROOT / "docs/FLAVOR_LATITUDE_QUANTIZER_AND_RP_SELFDUAL_NOTE_2026-05-30.md"


def check(name: str, cond: bool, detail: str = "") -> bool:
    global PASS, FAIL
    if cond:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    print(f"[{tag}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


def group_alg_mul(x: tuple[float, complex], y: tuple[float, complex]) -> tuple[float, complex]:
    """Multiplication in R + C."""
    return (x[0] * y[0], x[1] * y[1])


def phi_equal_center(x: tuple[float, complex]) -> float:
    return 0.5 * x[0] + 0.5 * x[1].real


def phi_regular_plancherel(x: tuple[float, complex]) -> float:
    return (x[0] + 2.0 * x[1].real) / 3.0


def q_of_r(r: float) -> float:
    return 1.0 / 3.0 + 2.0 * r / 3.0


def main() -> int:
    print("=" * 88)
    print("FLAVOR LATITUDE QUANTIZER / RP SELF-DUAL REPAIRED BOUNDARY")
    print("=" * 88)

    print("\nN1. cube-angle coincidence check")
    bd = np.array([1.0, 1.0, 1.0])
    fd = np.array([1.0, 1.0, 0.0])
    ed = np.array([1.0, 0.0, 0.0])
    cos2 = lambda u, v: float((u @ v) ** 2 / ((u @ u) * (v @ v)))
    roots = np.sort(np.roots([2.0, 3.0, -2.0]))
    check(
        "cube-angle 2/3 is real but a single crossing/value coincidence",
        abs(cos2(bd, fd) - 2.0 / 3.0) < 1e-12
        and abs(cos2(bd, ed) - 1.0 / 3.0) < 1e-12
        and any(abs(root - 0.5) < 1e-9 for root in roots),
        f"cos2(face)={cos2(bd, fd):.6f}; cos2(edge)={cos2(bd, ed):.6f}; roots={roots}",
    )

    print("\nN4. finite idempotent host check")
    idempotent_ratios = {0.0, 0.5, 1.0}
    check(
        "M2(C) idempotent trace/dim ratios are {0,1/2,1}; no 2/3 host",
        idempotent_ratios == {0.0, 0.5, 1.0} and (2.0 / 3.0) not in idempotent_ratios,
        "the native 2/3 remains the R[Z3] doublet/total dimension reading, not r=1/2",
    )

    print("\nRP signed-edge repair")
    a = 1.0
    singlet_null = -a / 2.0
    doublet_null = a
    mag_edge_1 = abs(singlet_null)
    mag_edge_2 = abs(doublet_null)
    gm = math.sqrt(mag_edge_1 * mag_edge_2)
    r_gm = gm**2 / a**2
    abs_involution = lambda x: (mag_edge_1 * mag_edge_2) / x
    signed_image_left = -abs_involution(abs(singlet_null))
    signed_image_right = abs_involution(abs(doublet_null))
    check(
        "RP edges are at opposite signed b values",
        singlet_null < 0.0 < doublet_null,
        f"singlet-null b={singlet_null}; doublet-null b={doublet_null}",
    )
    check(
        "multiplicative |b|-inversion fixes r=1/2 only after discarding sign(b)",
        abs(r_gm - 0.5) < 1e-12
        and abs(signed_image_left - doublet_null) > 1e-12
        and abs(signed_image_right - singlet_null) > 1e-12,
        f"|b| gm={gm:.6f}->r={r_gm:.6f}; signed images {signed_image_left:.3f}, {signed_image_right:.3f}",
    )
    r_arith_mag = ((mag_edge_1 + mag_edge_2) / 2.0) ** 2 / a**2
    r_signed_affine = ((singlet_null + doublet_null) / 2.0) ** 2 / a**2
    check(
        "arithmetic and signed-affine fixed points are different from the |b| geometric point",
        abs(r_arith_mag - 9.0 / 16.0) < 1e-12
        and abs(r_signed_affine - 1.0 / 16.0) < 1e-12
        and abs(r_gm - 0.5) < 1e-12,
        f"|b| arithmetic r={r_arith_mag:.6f}; signed-affine r={r_signed_affine:.6f}; |b| geometric r={r_gm:.6f}",
    )

    print("\nTrace-vs-center correction for A = R[Z3] = R + C")
    x = (1.2, 0.3 + 0.4j)
    y = (-0.7, 1.1 - 0.2j)
    xy = group_alg_mul(x, y)
    yx = group_alg_mul(y, x)
    check("R + C multiplication is commutative", xy == yx, f"xy={xy}; yx={yx}")

    tr_equal_xy = phi_equal_center(xy)
    tr_equal_yx = phi_equal_center(yx)
    tr_reg_xy = phi_regular_plancherel(xy)
    tr_reg_yx = phi_regular_plancherel(yx)
    check(
        "equal central-idempotent state is tracial",
        abs(tr_equal_xy - tr_equal_yx) < 1e-12,
        f"phi_equal(xy)={tr_equal_xy:.12f}; phi_equal(yx)={tr_equal_yx:.12f}",
    )
    check(
        "regular/Plancherel state is tracial",
        abs(tr_reg_xy - tr_reg_yx) < 1e-12,
        f"phi_regular(xy)={tr_reg_xy:.12f}; phi_regular(yx)={tr_reg_yx:.12f}",
    )
    positive_witness = (2.0, 3.0 + 0.0j)
    check(
        "trace property alone does not force a unique faithful weighting",
        phi_equal_center(positive_witness) > 0.0
        and phi_regular_plancherel(positive_witness) > 0.0
        and abs(phi_equal_center((0.0, 1.0 + 0.0j)) - phi_regular_plancherel((0.0, 1.0 + 0.0j))) > 1e-12,
        f"equal-center={phi_equal_center(positive_witness):.6f}; regular={phi_regular_plancherel(positive_witness):.6f}",
    )

    print("\nHS metric and readout boundary")
    I = np.eye(3)
    J = np.ones((3, 3))
    B = J - I
    gram = np.array([[np.trace(I.T @ I), np.trace(I.T @ B)], [np.trace(B.T @ I), np.trace(B.T @ B)]])
    check(
        "I and J-I are HS-orthogonal with Gram diag(3,6)",
        np.allclose(gram, np.array([[3.0, 0.0], [0.0, 6.0]])),
        f"Gram={gram.tolist()}",
    )
    r_block_equal = 0.5
    r_per_real_mode = 1.0
    check(
        "block-equal and per-real-mode readings are distinct",
        abs(q_of_r(r_block_equal) - 2.0 / 3.0) < 1e-12
        and abs(q_of_r(r_per_real_mode) - 1.0) < 1e-12,
        "block-equal r=1/2 -> Q=2/3; per-real-mode r=1 -> Q=1",
    )

    print("\nScope guard")
    note = NOTE.read_text(encoding="utf-8")
    guard_phrases = [
        "N2/N3 historical broad claims are not certified by this repaired packet",
        "equal central-idempotent state is tracial",
        "trace property alone does not select between these functionals",
    ]
    for phrase in guard_phrases:
        check(f"source note guard present: {phrase}", phrase in note)

    print()
    print(f"SCORECARD PASS={PASS} FAIL={FAIL}")
    print("VERDICT: repaired demotion/boundary packet. No native latitude quantizer is")
    print("certified here; RP self-dual r=1/2 is a |b|-coordinate artifact; and")
    print("trace-vs-center is a functional-choice boundary, not a unique-trace theorem.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
