#!/usr/bin/env python3
"""Bridge assessment for the s3-time readout primitive question.

The runner verifies the checkable parts of the scope-limited assessment:

* the one-hop source notes still contain the quoted admissibility clauses;
* the live endpoint-fitted eta-floor affine map is a channelwise restricted
  bright readout on the carrier coordinates;
* the live endpoint-fitted map is not the exact normalized Route-2 target
  triple at exact tolerance;
* the normalized target family retains the exact rho_E selection freedom;
* the time-channel factorization is unaffected by that spatial prefactor.

No status verdict is emitted here; the final line is deliberately machine
checkable for the runner cache.
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
from frontier_quark_up_amplitude_tensor_endpoint_bridge import tensor_endpoint_data
from frontier_s3_time_theta_to_slice_coupling_factor_rigidity import (
    route2_slice_backbone,
    v_r,
    xi_p,
)

AUDIT_TIMEOUT_SEC = 120

REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS = REPO_ROOT / "docs"

PASS_COUNT = 0
FAIL_COUNT = 0
BRIDGE_RATIO_TOL = 1.0e-9


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        prefix = "PASS"
    else:
        FAIL_COUNT += 1
        prefix = "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"{prefix}: {name}{suffix}")


def note_text(name: str) -> str:
    return (DOCS / name).read_text(encoding="utf-8")


def contains_all(text: str, needles: tuple[str, ...]) -> bool:
    return all(needle in text for needle in needles)


def exact_p_apply(rho_e: Fraction, column: tuple[Fraction, Fraction, Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    x0, x1, x2, x3 = column
    return (x0 + rho_e * x2, -2 * x1 + 2 * x3)


def main() -> int:
    primitive_note = note_text("S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md")
    time_note = note_text("QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md")
    rigidity_note = note_text("S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md")
    readout_note = note_text("QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md")

    check(
        "primitive note names the physical tensor-primitive bridge as open work",
        contains_all(
            primitive_note,
            (
                "A bridge theorem identifying the bilinear carrier `K_R(q)` with any",
                "physical tensor primitive in the GR-readout chain",
                "is the third upstream gap and is **not** closed by the readout",
            ),
        ),
    )
    check(
        "primitive note identifies eta-floor coefficients as endpoint-fitted",
        contains_all(
            primitive_note,
            (
                "fixed by the two endpoint\nvalues measured from the old `eta_floor_tf` pipeline",
                "endpoint-fitted, not first-principles",
            ),
        ),
    )
    check(
        "time-coupling note requires a supplied admissible P_R",
        contains_all(
            time_note,
            (
                "Given any admissible readout map `P_R`",
                "Xi_P(t ; c) = (P_R c) \u2297 exp(-t Lambda_R) u_*",
                "lacks is a theorem that selects one unique `P_R`",
            ),
        ),
    )
    check(
        "rigidity note localizes ambiguity in the spatial prefactor",
        contains_all(
            rigidity_note,
            (
                "structurally localized in the spatial prefactor",
                "time-channel structure is universal",
                "P(rho_E) = [[1, 0, rho_E, 0],",
            ),
        ),
    )
    check(
        "readout-map note states the restricted bright channelwise form",
        contains_all(
            readout_note,
            (
                "any admissible bright-preserving linear readout",
                "P_R = [[alpha_E, 0, beta_E, 0],",
                "beta_E / alpha_E",
            ),
        ),
    )

    data = restricted_readout_data()
    tensor_data = tensor_endpoint_data()

    target_e_shell = np.array([1.0, 0.0, 0.0, 0.0])
    target_e_center = np.array([1.0, 0.0, 1.0 / 6.0, 0.0])
    target_t_shell = np.array([0.0, 1.0, 0.0, 0.0])
    target_t_center = np.array([0.0, 1.0, 0.0, 1.0 / 6.0])

    carrier_err = max(
        float(np.max(np.abs(data.carrier_e_shell - target_e_shell))),
        float(np.max(np.abs(data.carrier_e_center - target_e_center))),
        float(np.max(np.abs(data.carrier_t_shell - target_t_shell))),
        float(np.max(np.abs(data.carrier_t_center - target_t_center))),
    )
    check(
        "live carrier columns match the restricted endpoint basis",
        carrier_err < EXACT_TOL,
        f"max carrier residual={carrier_err:.3e}",
    )

    readout = admissible_readout_matrix(data.alpha_e, data.beta_e, data.alpha_t, data.beta_t)
    channelwise = (
        abs(readout[0, 1]) < EXACT_TOL
        and abs(readout[0, 3]) < EXACT_TOL
        and abs(readout[1, 0]) < EXACT_TOL
        and abs(readout[1, 2]) < EXACT_TOL
        and abs(data.alpha_e) > EXACT_TOL
        and abs(data.alpha_t) > EXACT_TOL
    )
    check(
        "eta-floor endpoint affine map is a channelwise restricted bright readout",
        channelwise,
        "P_eta=[[a_E,0,b_E,0],[0,a_T,0,b_T]] with nonzero shell coefficients",
    )

    endpoint_residual = max(
        float(np.max(np.abs(readout @ data.carrier_e_shell - np.array([data.gamma_e_shell, 0.0])))),
        float(np.max(np.abs(readout @ data.carrier_e_center - np.array([data.gamma_e_center, 0.0])))),
        float(np.max(np.abs(readout @ data.carrier_t_shell - np.array([0.0, data.gamma_t_shell])))),
        float(np.max(np.abs(readout @ data.carrier_t_center - np.array([0.0, data.gamma_t_center])))),
    )
    check(
        "eta-floor endpoint affine map reproduces the live endpoint coefficients",
        endpoint_residual < EXACT_TOL,
        f"max endpoint residual={endpoint_residual:.3e}",
    )

    t_balance_err = abs(tensor_data.t_balance - abs(data.rho_t))
    check(
        "t_balance is the absolute live T-channel slope/intercept ratio",
        t_balance_err < BRIDGE_RATIO_TOL,
        f"t_balance={tensor_data.t_balance:.12f}, |beta_T/alpha_T|={abs(data.rho_t):.12f}",
    )

    q_t = Fraction(1, 1) + Fraction(-1, 1) / Fraction(6, 1)
    q_e = Fraction(1, 1) + Fraction(21, 4) / Fraction(6, 1)
    c_te = Fraction(-2, 1) * q_t / q_e
    check(
        "target triple gives the rational endpoint ratios exactly",
        q_t == Fraction(5, 6) and q_e == Fraction(15, 8) and c_te == Fraction(-8, 9),
        f"q_T={q_t}, q_E={q_e}, c_TE={c_te}",
    )

    live_misses_target = (
        abs(data.rho_t + 1.0) > EXACT_TOL
        and abs(data.mu + 2.0) > EXACT_TOL
        and abs(data.rho_e - (21.0 / 4.0)) > EXACT_TOL
    )
    check(
        "live eta-floor endpoint affine map is not the exact normalized target triple",
        live_misses_target,
        f"rho_T={data.rho_t:+.12f}, mu={data.mu:+.12f}, rho_E={data.rho_e:+.12f}",
    )

    e_shell = (Fraction(1), Fraction(0), Fraction(0), Fraction(0))
    e_center = (Fraction(1), Fraction(0), Fraction(1, 6), Fraction(0))
    shell_0 = exact_p_apply(Fraction(0), e_shell)
    shell_21 = exact_p_apply(Fraction(21, 4), e_shell)
    center_0 = exact_p_apply(Fraction(0), e_center)
    center_21 = exact_p_apply(Fraction(21, 4), e_center)
    check(
        "rho_E is an exact selection freedom after T-side normalization",
        shell_0 == shell_21 and center_0 == (Fraction(1), Fraction(0)) and center_21 == (Fraction(15, 8), Fraction(0)),
        f"P(0)E_shell={shell_0}, P(21/4)E_shell={shell_21}, P(21/4)E_center={center_21}",
    )

    backbone = route2_slice_backbone()
    p_0 = admissible_readout_matrix(1.0, 0.0, -2.0, 2.0)
    p_21 = admissible_readout_matrix(1.0, 21.0 / 4.0, -2.0, 2.0)
    time_seed = v_r(backbone, 0.5)
    xi_diff = xi_p(p_0, data.carrier_e_center, time_seed) - xi_p(p_21, data.carrier_e_center, time_seed)
    predicted = np.outer((p_0 - p_21) @ data.carrier_e_center, time_seed)
    factor_err = float(np.max(np.abs(xi_diff - predicted)))
    singular_values = np.linalg.svd(xi_diff, compute_uv=False)
    rank_tail = float(singular_values[1:].sum() / singular_values[0]) if singular_values[0] > 0.0 else 0.0
    check(
        "rho_E ambiguity factors through the spatial prefactor in Xi_P",
        factor_err < EXACT_TOL and rank_tail < 1.0e-9,
        f"factor residual={factor_err:.3e}, rank-tail={rank_tail:.3e}",
    )

    check(
        "one-hop notes do not supply a uniqueness theorem for eta-floor as the gate primitive",
        contains_all(
            primitive_note + time_note + readout_note,
            (
                "not first-principles",
                "selects one unique `P_R`",
                "does\n**not** derive the endpoint ratio chain",
            ),
        ),
    )

    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
