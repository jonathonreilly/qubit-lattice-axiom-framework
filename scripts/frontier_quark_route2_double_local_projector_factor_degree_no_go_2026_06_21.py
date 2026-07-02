#!/usr/bin/env python3
r"""Route-2 double-local projector factor-degree no-go.

This block attacks the remaining positive target exposed by the Route-2
endpoint no-go stack: derive the inverse-square local projector normalization

    q_X proportional to w_X^-2.

It does not derive that primitive.  It proves the exact factor-degree gate:
zero or one reciprocal local projector-weight factors miss the endpoint, while
two reciprocal factors are necessary and sufficient within the integer
reciprocal-degree grammar.  Current source/readout notes still leave those two
factors as an open primitive.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
import itertools

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "QUARK_ROUTE2_DOUBLE_LOCAL_PROJECTOR_FACTOR_DEGREE_NO_GO_NOTE_2026-06-21.md"
PROTOTYPE_NOTE = DOCS / "S3_TIME_TENSOR_PRIMITIVE_PROTOTYPE_NOTE.md"
CONSTRUCTED_NOTE = DOCS / "S3_TIME_CONSTRUCTED_SUPPORT_TENSOR_PRIMITIVE_NOTE.md"
BILINEAR_NOTE = DOCS / "S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md"
READOUT_NOTE = DOCS / "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"
COVARIANCE_NOTE = DOCS / "QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md"

ARMS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
AIDX = {arm: i for i, arm in enumerate(ARMS)}

TARGET_QT = Fraction(5, 6)
TARGET_QE = Fraction(15, 8)
TARGET_LAMBDA = Fraction(9, 4)
TARGET_RHO_E = Fraction(21, 4)
TARGET_CENTER_TE = Fraction(-8, 9)

PASS_COUNT = 0
FAIL_COUNT = 0


@dataclass(frozen=True)
class DegreeResult:
    degree: int
    lambda_value: Fraction
    q_e: Fraction
    rho_e: Fraction
    center_te: Fraction


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    line = f"  [{status}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def oh_group() -> list[np.ndarray]:
    matrices: list[np.ndarray] = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            matrix = np.zeros((3, 3), dtype=int)
            for row in range(3):
                matrix[row, perm[row]] = signs[row]
            matrices.append(matrix)
    return matrices


def arm_rep(matrix: np.ndarray) -> np.ndarray:
    rep = np.zeros((6, 6), dtype=float)
    for arm in ARMS:
        image = tuple(int(x) for x in matrix @ np.array(arm))
        rep[AIDX[image], AIDX[arm]] = 1.0
    return rep


def frac(value: float) -> Fraction:
    return Fraction(value).limit_denominator(10_000)


def projector_weights() -> tuple[Fraction, Fraction, Fraction]:
    reps = [arm_rep(matrix) for matrix in oh_group()]
    p_a1 = sum(reps) / len(reps)
    antipodal = arm_rep(-np.eye(3, dtype=int))
    p_t1 = (np.eye(6) - antipodal) / 2.0
    p_e = (np.eye(6) + antipodal) / 2.0 - p_a1
    return frac(p_a1[0, 0]), frac(p_e[0, 0]), frac(p_t1[0, 0])


def reciprocal_factor_result(degree: int, w_e: Fraction, w_t: Fraction) -> DegreeResult:
    """Return endpoint consequences for degree reciprocal factors.

    degree=0 is channel-blind.  degree=1 is a single reciprocal local
    projector-weight factor.  degree=2 is the double-local candidate.
    """
    leverage = w_t / w_e
    lambda_value = leverage**degree
    q_e = lambda_value * TARGET_QT
    rho_e = 6 * (q_e - 1)
    center_te = Fraction(-2, 1) * TARGET_QT / q_e
    return DegreeResult(
        degree=degree,
        lambda_value=lambda_value,
        q_e=q_e,
        rho_e=rho_e,
        center_te=center_te,
    )


def part1_note_boundary() -> None:
    print("\n" + "=" * 72)
    print("PART 1: current-source boundary")
    print("=" * 72)

    note = text(NOTE)
    prototype = text(PROTOTYPE_NOTE)
    constructed = text(CONSTRUCTED_NOTE)
    bilinear = text(BILINEAR_NOTE)
    readout = text(READOUT_NOTE)
    covariance = text(COVARIANCE_NOTE)

    check(
        "block09 note declares no-go/exact-support boundary rather than endpoint closure",
        "**Actual current-surface status:** no-go" in note
        and "does not derive `rho_E = 21/4`" in note
        and "two reciprocal factors remain an open primitive" in note,
        "status and open primitive are explicit",
    )
    check(
        "prototype source note leaves endpoint coefficient inputs underived",
        "This note **does not**\nderive the named inputs themselves" in prototype
        and "exact reduced anisotropic shell amplitude" in prototype
        and "bridge theorem identifying the support-block pair" in prototype,
        "source/readout staging object is not a normalization theorem",
    )
    check(
        "constructed support-response note excludes exact endpoint coefficient closure",
        "not an exact tensor observable" in constructed
        and "an exact endpoint coefficient theorem" in constructed,
        "bounded response Jacobian is not the missing endpoint primitive",
    )
    check(
        "bilinear carrier note is definition-only under named inputs",
        "class-A definition only" in bilinear
        and "This note **does not** derive" in bilinear
        and "physical tensor primitive" in bilinear,
        "carrier algebra does not select the readout direction",
    )
    check(
        "exact readout-map note names rho_E as the remaining missing map entry",
        "beta_E / alpha_E = 21/4" in readout
        and "exact missing-map obstruction" in readout,
        "endpoint map entry remains open",
    )
    check(
        "quadratic covariance no-go already identifies inverse-square as the sharp gap",
        "q_X∝w_X⁻²" in covariance
        and "No named functional produces an\n  inverse-square-of-projector-weight center lift." in covariance,
        "block09 narrows the factor-degree requirement, not a new endpoint value",
    )


def part2_projector_weights() -> tuple[Fraction, Fraction, Fraction]:
    print("\n" + "=" * 72)
    print("PART 2: exact six-arm O_h projector weights")
    print("=" * 72)

    w_a1, w_e, w_t = projector_weights()
    kappa = w_t / w_e
    print(f"  w_A1={w_a1}, w_E={w_e}, w_T1={w_t}, kappa={kappa}")
    check(
        "six-arm O_h per-arm weights are exact and give kappa=3/2",
        (w_a1, w_e, w_t, kappa) == (
            Fraction(1, 6),
            Fraction(1, 3),
            Fraction(1, 2),
            Fraction(3, 2),
        ),
        "weights are recomputed from the signed-permutation action",
    )
    return w_a1, w_e, w_t


def part3_reciprocal_factor_degree_gate(w_e: Fraction, w_t: Fraction) -> None:
    print("\n" + "=" * 72)
    print("PART 3: reciprocal factor-degree gate")
    print("=" * 72)

    rows = [reciprocal_factor_result(degree, w_e, w_t) for degree in range(0, 5)]
    print("  degree  lambda  q_E   rho_E  center T/E")
    for row in rows:
        print(
            f"  {row.degree:>6}  {str(row.lambda_value):>6}  {str(row.q_e):>5}  "
            f"{str(row.rho_e):>6}  {str(row.center_te):>10}"
        )

    one_factor = reciprocal_factor_result(1, w_e, w_t)
    two_factor = reciprocal_factor_result(2, w_e, w_t)
    zero_factor = reciprocal_factor_result(0, w_e, w_t)

    check(
        "zero reciprocal factors miss the endpoint",
        (
            zero_factor.lambda_value,
            zero_factor.q_e,
            zero_factor.rho_e,
            zero_factor.center_te,
        )
        != (TARGET_LAMBDA, TARGET_QE, TARGET_RHO_E, TARGET_CENTER_TE),
        f"degree 0 gives lambda={zero_factor.lambda_value}, rho_E={zero_factor.rho_e}",
    )
    check(
        "one reciprocal source/readout factor misses the endpoint",
        (
            one_factor.lambda_value,
            one_factor.q_e,
            one_factor.rho_e,
            one_factor.center_te,
        )
        != (TARGET_LAMBDA, TARGET_QE, TARGET_RHO_E, TARGET_CENTER_TE),
        f"degree 1 gives lambda={one_factor.lambda_value}, q_E={one_factor.q_e}, rho_E={one_factor.rho_e}",
    )
    check(
        "two reciprocal local projector-weight factors close the endpoint conditionally",
        (
            two_factor.lambda_value,
            two_factor.q_e,
            two_factor.rho_e,
            two_factor.center_te,
        )
        == (TARGET_LAMBDA, TARGET_QE, TARGET_RHO_E, TARGET_CENTER_TE),
        "degree 2 gives lambda=9/4, q_E=15/8, rho_E=21/4, center T/E=-8/9",
    )
    check(
        "three or more reciprocal factors overshoot the endpoint in the checked degree range",
        all(
            (
                row.lambda_value,
                row.q_e,
                row.rho_e,
                row.center_te,
            )
            != (TARGET_LAMBDA, TARGET_QE, TARGET_RHO_E, TARGET_CENTER_TE)
            for row in rows
            if row.degree >= 3
        ),
        "degrees 3 and 4 miss after passing the target degree",
    )

    target_degrees = [
        degree
        for degree in range(-6, 7)
        if reciprocal_factor_result(degree, w_e, w_t).lambda_value == TARGET_LAMBDA
    ]
    check(
        "within integer reciprocal degrees |d|<=6, d=2 is the unique endpoint degree",
        target_degrees == [2],
        f"target degrees: {target_degrees}",
    )


def part4_stuck_fanout(w_e: Fraction, w_t: Fraction) -> None:
    print("\n" + "=" * 72)
    print("PART 4: first-principles stuck fan-out synthesis")
    print("=" * 72)

    frames = {
        "raw carrier/readout degree": 0,
        "source-normalized single reciprocal": 1,
        "readout-normalized single reciprocal": 1,
        "Schur-dual single reciprocal": 1,
        "source times readout reciprocal": 2,
    }
    hits: dict[str, bool] = {}
    for name, degree in frames.items():
        result = reciprocal_factor_result(degree, w_e, w_t)
        hit = result.lambda_value == TARGET_LAMBDA
        hits[name] = hit
        print(f"  {name:<38s} degree={degree} lambda={result.lambda_value} hit={hit}")

    check(
        "all one-factor fan-out frames miss lambda=9/4",
        not hits["source-normalized single reciprocal"]
        and not hits["readout-normalized single reciprocal"]
        and not hits["Schur-dual single reciprocal"],
        "single-factor frames all give lambda=3/2",
    )
    check(
        "the only fan-out frame that hits is the two-factor source-times-readout frame",
        hits == {
            "raw carrier/readout degree": False,
            "source-normalized single reciprocal": False,
            "readout-normalized single reciprocal": False,
            "Schur-dual single reciprocal": False,
            "source times readout reciprocal": True,
        },
        "the positive route needs two independent reciprocal factors",
    )


def main() -> int:
    print("Route-2 double-local projector factor-degree no-go")
    print("=" * 72)

    part1_note_boundary()
    _, w_e, w_t = part2_projector_weights()
    part3_reciprocal_factor_degree_gate(w_e, w_t)
    part4_stuck_fanout(w_e, w_t)

    print("\n" + "=" * 72)
    print("SUMMARY")
    print("=" * 72)
    print("Status: no-go for zero/one-factor normalizations; two-factor primitive remains open.")
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
