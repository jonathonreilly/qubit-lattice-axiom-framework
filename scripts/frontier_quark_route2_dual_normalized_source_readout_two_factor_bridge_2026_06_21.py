#!/usr/bin/env python3
"""Route-2 dual-normalized source/readout two-factor bridge.

This runner checks an exact conditional support theorem, not an endpoint
closure. A Riesz dual normalization of a local arm functional contributes one
reciprocal local projector-weight factor. Two independent source/readout dual
legs therefore supply the total reciprocal degree two needed for the Route-2
endpoint value lambda = 9/4. The runner also checks that current Route-2 notes
do not yet license those two independent legs.
"""

from __future__ import annotations

from fractions import Fraction as F
import itertools
from pathlib import Path

import numpy as np


PASS = 0
FAIL = 0
ROOT = Path(__file__).resolve().parents[1]


def check(label: str, condition: bool, detail: str = "") -> bool:
    global PASS, FAIL
    ok = bool(condition)
    PASS += ok
    FAIL += not ok
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f"\n       {detail}" if detail else ""))
    return ok


def read_text(relpath: str) -> str:
    return (ROOT / relpath).read_text(encoding="utf-8")


def normalized_text(relpath: str) -> str:
    return " ".join(read_text(relpath).split())


ARMS = [
    np.array(v)
    for v in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
]
NEG = {0: 1, 1: 0, 2: 3, 3: 2, 4: 5, 5: 4}


def oh_signed_perms() -> list[np.ndarray]:
    mats: list[np.ndarray] = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            matrix = np.zeros((3, 3), dtype=int)
            for row in range(3):
                matrix[row, perm[row]] = signs[row]
            mats.append(matrix)
    return mats


def arm_index(vector: np.ndarray) -> int:
    for index, arm in enumerate(ARMS):
        if np.array_equal(vector, arm):
            return index
    raise ValueError(vector)


def perm_of(matrix: np.ndarray) -> list[int]:
    return [arm_index(matrix @ arm) for arm in ARMS]


def perm_matrix(matrix: np.ndarray) -> np.ndarray:
    p = perm_of(matrix)
    out = np.zeros((6, 6))
    for col in range(6):
        out[p[col], col] = 1.0
    return out


def projectors() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    group = oh_signed_perms()
    reynolds = sum(perm_matrix(matrix) for matrix in group) / len(group)
    antipodal = np.zeros((6, 6))
    for col in range(6):
        antipodal[NEG[col], col] = 1.0
    p_a1 = reynolds
    p_t1 = (np.eye(6) - antipodal) / 2.0
    p_e = (np.eye(6) + antipodal) / 2.0 - p_a1
    return p_a1, p_e, p_t1


def frac(value: float) -> F:
    return F(float(value)).limit_denominator()


def q_from_rho(rho: F) -> F:
    return 1 + rho / 6


def endpoint_from_lambda(lam: F) -> tuple[F, F, F]:
    q_t = F(5, 6)
    q_e = lam * q_t
    rho_e = 6 * (q_e - 1)
    center_te = -2 * q_t / q_e
    return q_e, rho_e, center_te


def main() -> int:
    print("Route-2 dual-normalized source/readout two-factor bridge")
    print("=" * 84)
    print("Status: conditional-support; no endpoint triple or audit verdict is adopted.")

    group = oh_signed_perms()
    check("O_h signed-permutation group has order 48", len(group) == 48, f"|O_h|={len(group)}")

    p_a1, p_e, p_t1 = projectors()
    ranks = tuple(int(round(np.trace(p))) for p in (p_a1, p_e, p_t1))
    check("six-arm representation splits as A1 + E + T1 with ranks (1,2,3)", ranks == (1, 2, 3), str(ranks))

    w_a1, w_e, w_t1 = (frac(p[0, 0]) for p in (p_a1, p_e, p_t1))
    check(
        "per-arm projector weights are exact: w_A1=1/6, w_E=1/3, w_T1=1/2",
        (w_a1, w_e, w_t1) == (F(1, 6), F(1, 3), F(1, 2)),
        f"(w_A1,w_E,w_T1)=({w_a1},{w_e},{w_t1})",
    )
    kappa = w_t1 / w_e
    check("same-domain shell leverage kappa=w_T1/w_E=3/2", kappa == F(3, 2), f"kappa={kappa}")

    print("\n-- Finite-frame Riesz dual lemma --")
    arm = np.eye(6)[0]
    for name, projector, weight in (("E", p_e, w_e), ("T1", p_t1, w_t1)):
        v = projector @ arm
        ell = v / float(weight)
        response = float(ell @ arm)
        norm_sq = float(ell @ ell)
        check(
            f"{name} dual covector ell_X=P_X a/w_X has ell_X(a)=1",
            abs(response - 1.0) < 1.0e-12,
            f"ell_{name}(a)={response:.12f}",
        )
        check(
            f"{name} dual covector squared norm is 1/w_X",
            abs(norm_sq - float(1 / weight)) < 1.0e-12,
            f"||ell_{name}||^2={norm_sq:.12f}, 1/w_{name}={float(1 / weight):.12f}",
        )

    print("\n-- Source/readout factor degree --")
    single_factor_e = 1 / w_e
    single_factor_t = 1 / w_t1
    lambda_single = single_factor_e / single_factor_t
    q_e_single, rho_e_single, c_te_single = endpoint_from_lambda(lambda_single)
    check(
        "one dual-normalized source or readout leg gives lambda=3/2, not 9/4",
        lambda_single == F(3, 2),
        f"lambda_single={lambda_single}",
    )
    check(
        "one dual factor misses the endpoint: q_E=5/4, rho_E=3/2, center T/E=-4/3",
        (q_e_single, rho_e_single, c_te_single) == (F(5, 4), F(3, 2), F(-4, 3)),
        f"q_E={q_e_single}, rho_E={rho_e_single}, center T/E={c_te_single}",
    )

    double_factor_e = single_factor_e * single_factor_e
    double_factor_t = single_factor_t * single_factor_t
    lambda_double = double_factor_e / double_factor_t
    q_e_double, rho_e_double, c_te_double = endpoint_from_lambda(lambda_double)
    check(
        "two independent source/readout dual legs give lambda=(w_T1/w_E)^2=9/4",
        lambda_double == F(9, 4),
        f"lambda_double={lambda_double}",
    )
    check(
        "two dual factors conditionally give q_E=15/8, rho_E=21/4, center T/E=-8/9",
        (q_e_double, rho_e_double, c_te_double) == (F(15, 8), F(21, 4), F(-8, 9)),
        f"q_E={q_e_double}, rho_E={rho_e_double}, center T/E={c_te_double}",
    )

    print("\n-- Current-surface license checks --")
    prototype = normalized_text("docs/S3_TIME_TENSOR_PRIMITIVE_PROTOTYPE_NOTE.md")
    bilinear = normalized_text("docs/S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md")
    constructed = normalized_text("docs/S3_TIME_CONSTRUCTED_SUPPORT_TENSOR_PRIMITIVE_NOTE.md")
    coupling = normalized_text("docs/S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md")
    covariance = normalized_text("docs/QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md")
    note = normalized_text(
        "docs/QUARK_ROUTE2_DUAL_NORMALIZED_SOURCE_READOUT_TWO_FACTOR_BRIDGE_CONDITIONAL_NOTE_2026-06-21.md"
    )

    check(
        "prototype note leaves named inputs, reduced shell amplitude, and primitive bridge open",
        "derive the named inputs themselves" in prototype
        and "exact reduced anisotropic shell amplitude" in prototype
        and "bridge theorem identifying the support-block pair" in prototype,
    )
    check(
        "bilinear note remains class-A definition only and does not derive a physical tensor primitive",
        "class-A definition only" in bilinear and "physical tensor primitive" in bilinear,
    )
    check(
        "constructed support tensor note is bounded, not an exact endpoint coefficient theorem",
        "not an exact tensor observable" in constructed and "exact endpoint coefficient theorem" in constructed,
    )
    check(
        "theta-to-slice note still names the missing readout-map endpoint triple as the uniqueness blocker",
        "missing readout-map endpoint triple" in coupling
        and "unique-exact `Theta_R -> Lambda_R` coupling theorem **not** closed" in coupling,
    )
    check(
        "quadratic covariance no-go identifies inverse-square projector weighting as the sharp gap",
        "No named functional produces an inverse-square-of-projector-weight center lift." in covariance,
    )
    check(
        "new note marks actual current-surface status as conditional-support and forbids endpoint closure",
        "**Actual current-surface status:** conditional-support" in note
        and "does not derive `rho_E = 21/4`" in note
        and "Proposal allowed:** false" in note,
    )
    check(
        "new note states the exact remaining license target: two independent dual-normalized legs",
        "both the source leg and the readout leg are independently normalized as" in note
        and "local Riesz duals for the relevant projected channel" in note,
    )

    print("\n" + "=" * 84)
    print(f"PASS={PASS} FAIL={FAIL}")
    print(
        "\nVERDICT: conditional-support. Finite-frame Riesz dual normalization supplies one reciprocal\n"
        "local projector-weight factor. Two independent source/readout dual legs would supply the\n"
        "degree-two inverse-square law and hence the Route-2 endpoint algebra exactly. Current Route-2\n"
        "tensor/readout notes do not yet license those two independent legs, so rho_E remains open."
    )
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
