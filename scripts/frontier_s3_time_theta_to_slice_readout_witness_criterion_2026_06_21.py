#!/usr/bin/env python3
"""Verifier for the s3-time readout witness criterion.

The runner checks a narrow direct-consumer theorem for the conditional family
Xi_P(t; c) = (P_R c) tensor V_R(t). It does not derive the Route-2 endpoint
triple. It verifies that any downstream rank-one spacetime dual can
distinguish rho_E only through the E-center ambiguity vector.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

import numpy as np

from frontier_quark_route2_exact_readout_map import (
    EXACT_TOL,
    admissible_readout_matrix,
    restricted_readout_data,
)
from frontier_quark_route2_exact_time_coupling import (
    route2_slice_backbone,
    v_r,
    xi_p,
)


REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS = REPO_ROOT / "docs"
NOTE = DOCS / "S3_TIME_THETA_TO_SLICE_READOUT_WITNESS_CRITERION_NOTE_2026-06-21.md"
PARENT_NOTE = DOCS / "S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md"
FACTOR_NOTE = DOCS / "S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md"
READOUT_NOTE = DOCS / "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"{status}: {name}{suffix}")


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def p_rho(rho: Fraction) -> np.ndarray:
    return admissible_readout_matrix(1.0, float(rho), -2.0, 2.0)


def functional(h: np.ndarray, x: np.ndarray, w: np.ndarray) -> float:
    return float(h @ x @ w)


def main() -> int:
    print("s3-time readout witness criterion verifier")
    print("=" * 72)

    note = text(NOTE)
    parent_note = text(PARENT_NOTE)
    factor_note = text(FACTOR_NOTE)
    readout_note = text(READOUT_NOTE)

    check(
        "note is scoped as bounded support, not endpoint-triple closure",
        "does not derive the Route-2 endpoint triple" in note
        and "does not close the" in note
        and "parent `s3_time_theta_to_slice_coupling_note` open gate" in note,
    )
    check(
        "parent note still names the endpoint triple as the blocker",
        "readout-map endpoint triple" in parent_note
        and "not derived by the current exact stack" in parent_note,
    )
    check(
        "factor-rigidity note supplies the shared time-factor premise",
        "structurally localized in the spatial prefactor" in factor_note
        and "time-channel structure is universal" in factor_note,
    )
    check(
        "readout-map authority supplies the normalized one-parameter family",
        "P(rho_E)" in readout_note
        and "beta_E / alpha_E" in readout_note
        and "21/4" in readout_note,
    )

    data = restricted_readout_data()
    backbone = route2_slice_backbone()
    v = v_r(backbone, 0.75)
    p0 = p_rho(Fraction(0, 1))
    p21 = p_rho(Fraction(21, 4))
    rho_delta = Fraction(21, 4)

    columns = (
        ("E-shell", data.carrier_e_shell, Fraction(0, 1)),
        ("E-center", data.carrier_e_center, Fraction(1, 6)),
        ("T-shell", data.carrier_t_shell, Fraction(0, 1)),
        ("T-center", data.carrier_t_center, Fraction(0, 1)),
    )

    for label, carrier, c3 in columns:
        observed = xi_p(p21, carrier, v) - xi_p(p0, carrier, v)
        predicted_spatial = np.array([float(rho_delta * c3), 0.0])
        predicted = np.outer(predicted_spatial, v)
        resid = float(np.max(np.abs(observed - predicted)))
        check(
            f"{label} ambiguity vector matches (rho_delta*c3,0) tensor V",
            resid < EXACT_TOL,
            f"residual={resid:.3e}",
        )

    e_center = data.carrier_e_center
    xi_delta = xi_p(p21, e_center, v) - xi_p(p0, e_center, v)
    expected_delta = Fraction(7, 8)
    e_row = np.array([1.0, 0.0])
    t_row = np.array([0.0, 1.0])
    w_norm = v / float(v @ v)
    w_orth = np.zeros_like(v)
    w_orth[0] = v[1]
    w_orth[1] = -v[0]

    e_witness = functional(e_row, xi_delta, w_norm)
    t_witness = functional(t_row, xi_delta, w_norm)
    orth_witness = functional(e_row, xi_delta, w_orth)

    check(
        "normalized E-center witness reads the exact 7/8 increment",
        abs(e_witness - float(expected_delta)) < EXACT_TOL,
        f"increment={e_witness:.12f}",
    )
    check(
        "T-row witness is blind to rho_E",
        abs(t_witness) < EXACT_TOL,
        f"T-row response={t_witness:.3e}",
    )
    check(
        "slice dual orthogonal to V_R(t) is blind to rho_E",
        abs(orth_witness) < EXACT_TOL,
        f"orthogonal response={orth_witness:.3e}",
    )

    h = np.array([3.0, -4.0])
    w = v + 0.25 * w_norm
    lhs = functional(h, xi_delta, w)
    rhs = float(rho_delta * Fraction(1, 6)) * h[0] * float(v @ w)
    check(
        "rank-one dual formula holds for a mixed channel and slice witness",
        abs(lhs - rhs) < 5.0e-14,
        f"lhs={lhs:.12e}, rhs={rhs:.12e}",
    )

    shell_xi_0_t1 = xi_p(p0, data.carrier_e_center, v_r(backbone, 0.25))
    shell_xi_0_t2 = xi_p(p0, data.carrier_e_center, v_r(backbone, 1.25))
    shell_xi_21_t1 = xi_p(p21, data.carrier_e_center, v_r(backbone, 0.25))
    shell_xi_21_t2 = xi_p(p21, data.carrier_e_center, v_r(backbone, 1.25))
    ratio_0 = float(np.linalg.norm(shell_xi_0_t1) / np.linalg.norm(shell_xi_0_t2))
    ratio_21 = float(np.linalg.norm(shell_xi_21_t1) / np.linalg.norm(shell_xi_21_t2))
    check(
        "time-attenuation norm ratio is blind to rho_E",
        abs(ratio_0 - ratio_21) < EXACT_TOL,
        f"ratio_0={ratio_0:.12f}, ratio_21={ratio_21:.12f}",
    )

    xi_shell = xi_p(p21, data.carrier_e_shell, v)
    xi_center = xi_p(p21, data.carrier_e_center, v)
    shell_read = functional(e_row, xi_shell, w_norm)
    center_read = functional(e_row, xi_center, w_norm)
    check(
        "target readout witness gives shell 1 and center 15/8",
        abs(shell_read - 1.0) < EXACT_TOL and abs(center_read - 15.0 / 8.0) < EXACT_TOL,
        f"shell={shell_read:.12f}, center={center_read:.12f}",
    )

    q_t = Fraction(1, 1) + Fraction(-1, 1) / Fraction(6, 1)
    q_e = Fraction(1, 1) + Fraction(21, 4) / Fraction(6, 1)
    c_te = Fraction(-2, 1) * q_t / q_e
    rho_from_q = Fraction(6, 1) * (q_e - Fraction(1, 1))
    check(
        "witness target is equivalent to the Route-2 endpoint chain",
        q_t == Fraction(5, 6)
        and q_e == Fraction(15, 8)
        and c_te == Fraction(-8, 9)
        and rho_from_q == Fraction(21, 4),
        f"q_T={q_t}, q_E={q_e}, c_TE={c_te}, rho_E={rho_from_q}",
    )

    check(
        "current authorities do not supply the E-center witness value as a theorem",
        "not derived by the current exact stack" in parent_note
        and "irreducible missing map entry" in readout_note,
    )

    print("=" * 72)
    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
