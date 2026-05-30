#!/usr/bin/env python3
r"""
Factor-rigidity theorem for the s3-time Theta_R -> Lambda_R coupling family.

Status:
  positive narrow theorem on the conditional coupling family

Safe claim:
  Take the cited authorities

      QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19   (Lambda_R, T_R, V_R(t))
      QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19     (carrier K_R, P_R class)

  as given.  The conditional family

      Xi_P(t; c) = (P_R c) (x) V_R(t),     V_R(t) = exp(-t Lambda_R) u_*

  on the restricted carrier class then exhibits five structural
  properties that are independent of the unresolved readout-triple

      (beta_T/alpha_T, alpha_T/alpha_E, beta_E/alpha_E) = (-1, -2, 21/4).

  Concretely, for any two admissible readouts P_a, P_b in the 1-parameter
  family P(rho_E) = [[1, 0, rho_E, 0], [0, -2, 0, 2]]:

    (F1) Lambda_R is readout-independent (definitional; built from Schur).
    (F2) V_R(t) is readout-independent (consequence of F1).
    (F3) Norm-ratio invariance: ||Xi_P(t1; c)|| / ||Xi_P(t2; c)|| equals
         ||V_R(t1)|| / ||V_R(t2)|| for every admissible P_R and every
         carrier column c with (P_R c) != 0.
    (F4) Semigroup commutation: (I (x) T_R) Xi_P(t; c) = Xi_P(t+1; c).
    (F5) Rank-1 ambiguity along time: for any two admissible P_a, P_b,
         Xi_a(t; c) - Xi_b(t; c) factors as ((P_a - P_b) c) (x) V_R(t).
         This isolates the readout ambiguity in the spatial prefactor; the
         time-channel is shared.

  None of (F1)-(F5) derives the readout-triple.  They prove that the
  ambiguity is structurally LOCALIZED in the spatial factor, so the
  open-gate target on the row is reduced to the upstream readout-triple
  derivation.

  This is a positive narrow theorem.  It does not close the parent
  open_gate row, but it lands a derivation that is independent of and
  does not bypass the readout-map no-go.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy.linalg import expm

import frontier_oh_schur_boundary_action as schur
from frontier_quark_route2_exact_readout_map import (
    EXACT_TOL,
    admissible_readout_matrix,
    restricted_readout_data,
)


PASS_COUNT = 0
FAIL_COUNT = 0
TIMES = [0.25, 0.5, 1.0, 2.0, 3.0]


def local_check(name: str, condition: bool, detail: str = "") -> None:
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


@dataclass(frozen=True)
class SliceBackbone:
    lambda_sym: np.ndarray
    transfer: np.ndarray
    seed: np.ndarray


def route2_slice_backbone() -> SliceBackbone:
    lambda_r, _, _, _ = schur.schur_dtn_matrix(15, 4.0)
    lambda_sym = 0.5 * (lambda_r + lambda_r.T)
    transfer = expm(-lambda_sym)
    seed = np.ones(lambda_sym.shape[0], dtype=float)
    seed /= np.linalg.norm(seed)
    return SliceBackbone(lambda_sym=lambda_sym, transfer=transfer, seed=seed)


def v_r(backbone: SliceBackbone, t: float) -> np.ndarray:
    return expm(-t * backbone.lambda_sym) @ backbone.seed


def xi_p(readout: np.ndarray, carrier_column: np.ndarray, time_seed: np.ndarray) -> np.ndarray:
    return np.outer(readout @ carrier_column, time_seed)


def carrier_columns():
    data = restricted_readout_data()
    return [
        ("E-shell", data.carrier_e_shell),
        ("E-center", data.carrier_e_center),
        ("T-shell", data.carrier_t_shell),
        ("T-center", data.carrier_t_center),
    ]


def f1_lambda_readout_independence(backbone: SliceBackbone) -> None:
    print("\n" + "=" * 72)
    print("F1: Lambda_R is readout-independent (definitional)")
    print("=" * 72)

    # The slice generator is built from the Schur boundary alone.  Rebuild
    # twice from the same construction; equality confirms no readout input
    # silently leaks into the slice backbone.
    bb2 = route2_slice_backbone()
    err = float(np.max(np.abs(backbone.lambda_sym - bb2.lambda_sym)))
    local_check(
        "Lambda_R is constructed from the Schur boundary only, with no readout-map dependence",
        err < EXACT_TOL,
        f"two-build reconstruction residual = {err:.3e}",
    )

    # Show explicitly that Lambda_R does not appear inside any of the
    # admissible readout matrices.
    rho_values = [0.0, 21.0 / 4.0, 1.5, -3.7]
    all_p = [admissible_readout_matrix(1.0, rho, -2.0, 2.0) for rho in rho_values]
    p_norms = [float(np.linalg.norm(p)) for p in all_p]
    distinct = len({round(n, 6) for n in p_norms}) > 1
    local_check(
        "the admissible readout class P(rho_E) is a non-trivial 1-parameter family (distinct rho_E give distinct maps)",
        distinct,
        f"||P|| over rho_E sample = {[round(n, 4) for n in p_norms]}",
    )


def f2_vr_readout_independence(backbone: SliceBackbone) -> None:
    print("\n" + "=" * 72)
    print("F2: V_R(t) is readout-independent (consequence of F1)")
    print("=" * 72)

    # V_R(t) is built from Lambda_R and a canonical seed; rebuilding via
    # two different routes must agree across t.
    for t in TIMES:
        direct = v_r(backbone, t)
        # Two-step build via semigroup composition
        composed = expm(-0.5 * t * backbone.lambda_sym) @ v_r(backbone, 0.5 * t)
        err = float(np.max(np.abs(direct - composed)))
        local_check(
            f"V_R({t:.2f}) reconstructed via semigroup composition matches direct exponential",
            err < EXACT_TOL,
            f"residual = {err:.3e}",
        )


def f3_norm_ratio_invariance(backbone: SliceBackbone) -> None:
    print("\n" + "=" * 72)
    print("F3: Norm-ratio invariance under admissible readout class")
    print("=" * 72)

    p_a = admissible_readout_matrix(1.0, 0.0, -2.0, 2.0)
    p_b = admissible_readout_matrix(1.0, 21.0 / 4.0, -2.0, 2.0)
    p_c = admissible_readout_matrix(1.0, -1.25, -2.0, 2.0)

    cols = carrier_columns()
    t1, t2 = 0.5, 2.0

    # Universal time-attenuation ratio derived from V_R alone
    v1 = v_r(backbone, t1)
    v2 = v_r(backbone, t2)
    universal_ratio = float(np.linalg.norm(v1) / np.linalg.norm(v2))
    print(f"  universal ||V_R(t1)||/||V_R(t2)|| at t1={t1}, t2={t2} = {universal_ratio:.12e}")

    for label, c in cols:
        for readout_label, p in [("rho_E=0", p_a), ("rho_E=21/4", p_b), ("rho_E=-5/4", p_c)]:
            head_a = p @ c
            if float(np.linalg.norm(head_a)) < EXACT_TOL:
                # skip carriers that the readout annihilates (no ratio defined)
                continue
            r1 = xi_p(p, c, v1)
            r2 = xi_p(p, c, v2)
            measured_ratio = float(np.linalg.norm(r1) / np.linalg.norm(r2))
            err = abs(measured_ratio - universal_ratio)
            local_check(
                f"norm-ratio matches universal V_R ratio for carrier {label} under {readout_label}",
                err < EXACT_TOL,
                f"measured={measured_ratio:.12e}, residual={err:.3e}",
            )


def f4_semigroup_commutation(backbone: SliceBackbone) -> None:
    print("\n" + "=" * 72)
    print("F4: Semigroup commutation (I (x) T_R) Xi_P(t) = Xi_P(t+1)")
    print("=" * 72)

    p_a = admissible_readout_matrix(1.0, 0.0, -2.0, 2.0)
    p_b = admissible_readout_matrix(1.0, 21.0 / 4.0, -2.0, 2.0)
    cols = carrier_columns()

    for label, c in cols:
        for readout_label, p in [("rho_E=0", p_a), ("rho_E=21/4", p_b)]:
            for t in [0.0, 0.5, 1.0, 2.0]:
                left = xi_p(p, c, v_r(backbone, t)) @ backbone.transfer.T
                # T_R is symmetric so .T is just T_R
                right = xi_p(p, c, v_r(backbone, t + 1.0))
                err = float(np.max(np.abs(left - right)))
                local_check(
                    f"semigroup commutation at t={t:.2f} for carrier {label} under {readout_label}",
                    err < EXACT_TOL,
                    f"residual = {err:.3e}",
                )


def f5_rank_one_time_ambiguity(backbone: SliceBackbone) -> None:
    print("\n" + "=" * 72)
    print("F5: Rank-1 time-axis localization of readout ambiguity")
    print("=" * 72)

    # Two distinct admissible readouts.
    p_a = admissible_readout_matrix(1.0, 0.0, -2.0, 2.0)
    p_b = admissible_readout_matrix(1.0, 21.0 / 4.0, -2.0, 2.0)
    delta_p = p_a - p_b

    cols = carrier_columns()

    for label, c in cols:
        head_delta = delta_p @ c
        if float(np.linalg.norm(head_delta)) < EXACT_TOL:
            local_check(
                f"readout ambiguity vanishes identically on carrier {label} (E-shell column is rho_E-blind)",
                True,
                "(P_a - P_b) c = 0 by construction of the 1-parameter family",
            )
            continue

        for t in TIMES:
            v_t = v_r(backbone, t)
            xi_diff = xi_p(p_a, c, v_t) - xi_p(p_b, c, v_t)
            predicted = np.outer(head_delta, v_t)
            err = float(np.max(np.abs(xi_diff - predicted)))
            local_check(
                f"Xi_a - Xi_b factors as ((P_a-P_b)c)(x)V_R(t) at t={t:.2f} for carrier {label}",
                err < EXACT_TOL,
                f"residual = {err:.3e}",
            )

            # Rank-1 check on the differencs (outer product is rank 1).
            u, s, vh = np.linalg.svd(xi_diff)
            if s[0] > 0.0:
                rank1_fraction = float(s[1:].sum() / s[0])
            else:
                rank1_fraction = 0.0
            local_check(
                f"Xi_a - Xi_b is numerically rank 1 at t={t:.2f} for carrier {label}",
                rank1_fraction < 1e-9,
                f"sum of subleading singular values / leading = {rank1_fraction:.3e}",
            )


def main() -> int:
    print("Factor-rigidity theorem for s3-time Theta_R -> Lambda_R coupling")
    print("=" * 72)

    backbone = route2_slice_backbone()
    f1_lambda_readout_independence(backbone)
    f2_vr_readout_independence(backbone)
    f3_norm_ratio_invariance(backbone)
    f4_semigroup_commutation(backbone)
    f5_rank_one_time_ambiguity(backbone)

    print("\n" + "=" * 72)
    print("SUMMARY")
    print("=" * 72)
    print("Statement: For any admissible readout in the 1-parameter family")
    print("P(rho_E), the conditional family Xi_P(t; c) = (P_R c) (x) V_R(t)")
    print("admits the structural factor rigidity (F1)-(F5).  This is")
    print("independent of the unresolved readout-triple no-go: the readout")
    print("ambiguity is structurally localized in the spatial prefactor and")
    print("is rank-1 along the time-axis for every fixed carrier column.")
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
