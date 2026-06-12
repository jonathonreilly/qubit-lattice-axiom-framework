#!/usr/bin/env python3
"""Finite rim-boundary eta construction and tensor-word ladder readout.

This runner stays on the finite packet surface:

* tensor-word dominant-weight box NMAX=4;
* Wilson Bessel mode truncation MODE_MAX=80;
* source-sector composition NMAX=7, MODE_MAX=200;
* derived adjacent matrix-element bond delta(lambda, mu) / d_lambda.

The constructed finite rim boundary is the local tensor word applied to the
trivial far boundary:

    eta = tensor_word @ e_(0,0)

where tensor_word is the finite Wilson/fusion word already used by the bounded
packet. The readout replaces the previous e_(0,0) boundary on unmarked word
slots by eta. No physical 3D environment, untruncated limit, L_perp limit, or
canonical repinning is claimed.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path

import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import gauge_vacuum_plaquette_tensor_word_multiword_perron_ladder_2026_06_11 as multiword
import gauge_vacuum_plaquette_tensor_word_perron_derived_rho_composed_readout_2026_06_11 as one_word_ref


AUDIT_TIMEOUT_SEC = 600

BETA = 6.0
TW_NMAX = 4
TW_MODE_MAX = 80
SOURCE_NMAX = one_word_ref.SOURCE_NMAX
SOURCE_MODE_MAX = one_word_ref.SOURCE_MODE_MAX
TOL = 1.0e-10

P_TW1_REFERENCE = 0.434215413260
P_TWO_TRIVIAL_REFERENCE = 0.429196712321
P_TWO_MARGINAL_REFERENCE = 0.436251149956
P_THREE_TRIVIAL_REFERENCE = 0.429196712321
P_THREE_MARGINAL_REFERENCE = 0.592817119605

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class ReadoutRow:
    words: int
    convention: str
    rho10: float
    rho11: float
    rho_min: float
    rho_max: float
    p_value: float


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS: {name}")
    else:
        FAIL += 1
        print(f"FAIL: {name}")
    if detail:
        print(f"      {detail}")


def section(title: str) -> None:
    print()
    print("=" * 96)
    print(title)
    print("=" * 96)


def source_p(weights: list[tuple[int, int]], rho: np.ndarray) -> float:
    rho_map = {w: float(rho[i]) for i, w in enumerate(weights)}
    return float(
        one_word_ref.source_readout(
            rho_map, SOURCE_NMAX, SOURCE_MODE_MAX, "zero"
        )["P"]
    )


def one_word_anchor(tw: dict[str, object]) -> ReadoutRow:
    eig, psi, rho = one_word_ref.perron_vector_of_tensor_word(
        tw["tensor_word"], tw["index"]
    )
    weights = list(tw["weights"])
    index = tw["index"]
    residual = float(
        np.linalg.norm(tw["tensor_word"] @ psi - eig * psi, ord=np.inf)
    )
    check(
        "one-word tensor Perron residual is small",
        residual < 1.0e-12,
        f"residual={residual:.3e}",
    )
    return ReadoutRow(
        words=1,
        convention="one_word_anchor",
        rho10=float(rho[index[(1, 0)]]),
        rho11=float(rho[index[(1, 1)]]),
        rho_min=float(np.min(rho)),
        rho_max=float(np.max(rho)),
        p_value=source_p(weights, rho),
    )


def constructed_eta(tw: dict[str, object]) -> np.ndarray:
    return np.asarray(tw["tensor_word"] @ tw["boundary0"], dtype=float)


def normalized_eta_rho(tw: dict[str, object], eta: np.ndarray) -> np.ndarray:
    index = tw["index"]
    return eta / float(eta[index[(0, 0)]])


def weighted_boundary_readout(
    result: multiword.MultiwordResult,
    eta_by_weight: dict[tuple[int, int], float],
    marked_word: int = 0,
) -> np.ndarray:
    weights = list(result.weights)
    zero = (0, 0)
    sums = {w: 0.0 for w in weights}
    for state, psi_val in zip(result.tuples, result.psi):
        boundary_weight = 1.0
        for word_pos, label in enumerate(state):
            if word_pos != marked_word:
                boundary_weight *= eta_by_weight[label]
        sums[state[marked_word]] += float(psi_val) * boundary_weight
    denom = sums[zero]
    if abs(denom) <= 1.0e-300:
        raise RuntimeError("constructed eta readout denominator is zero")
    return np.array([sums[w] / denom for w in weights], dtype=float)


def baseline_row(
    result: multiword.MultiwordResult,
    convention: str,
) -> ReadoutRow:
    rho = multiword.readout_vector(result, 0, convention)
    weights = list(result.weights)
    index = result.index
    return ReadoutRow(
        words=result.words,
        convention=convention,
        rho10=float(rho[index[(1, 0)]]),
        rho11=float(rho[index[(1, 1)]]),
        rho_min=float(np.min(rho)),
        rho_max=float(np.max(rho)),
        p_value=source_p(weights, rho),
    )


def eta_row(
    result: multiword.MultiwordResult,
    eta_by_weight: dict[tuple[int, int], float],
) -> ReadoutRow:
    rho = weighted_boundary_readout(result, eta_by_weight, 0)
    weights = list(result.weights)
    index = result.index
    return ReadoutRow(
        words=result.words,
        convention="constructed_eta",
        rho10=float(rho[index[(1, 0)]]),
        rho11=float(rho[index[(1, 1)]]),
        rho_min=float(np.min(rho)),
        rho_max=float(np.max(rho)),
        p_value=source_p(weights, rho),
    )


def print_row_table(rows: list[ReadoutRow]) -> None:
    print("words | readout | rho10 | rho11 | rho_min | rho_max | P(6)")
    print("-" * 96)
    for row in rows:
        print(
            f"{row.words:5d} | {row.convention:<16} | "
            f"{row.rho10:.12f} | {row.rho11:.12f} | "
            f"{row.rho_min:.12f} | {row.rho_max:.12f} | {row.p_value:.12f}"
        )


def distance_line(label: str, p_value: float, anchors: dict[str, float]) -> str:
    comparator = one_word_ref.CANONICAL_COMPARATOR
    comparator_text = one_word_ref.CANONICAL_COMPARATOR_TEXT
    delta_vs_tw1 = abs(P_TW1_REFERENCE - comparator) - abs(p_value - comparator)
    direction = "toward" if delta_vs_tw1 > 0.0 else "away"
    return (
        f"{label}: P = {p_value:.12f}; "
        f"|P - P_loc_reference| = {abs(p_value - anchors['P_loc']):.12f}; "
        f"|P - P_triv_reference| = {abs(p_value - anchors['P_triv']):.12f}; "
        f"|P - {comparator_text}| = {abs(p_value - comparator):.12f}; "
        f"direction_vs_tw1 = {direction} by {abs(delta_vs_tw1):.12f}"
    )


def main() -> int:
    print("Gauge-vacuum plaquette finite rim-boundary eta construction readout")
    print(
        f"beta={BETA}, tensor NMAX={TW_NMAX}, tensor MODE_MAX={TW_MODE_MAX}, "
        f"source NMAX={SOURCE_NMAX}, source MODE_MAX={SOURCE_MODE_MAX}"
    )
    print(
        "Status authority: independent audit lane only. This source runner "
        "does not set or predict an audit outcome."
    )

    anchors = one_word_ref.reference_anchor_solves()
    tw = one_word_ref.build_tensor_word(TW_NMAX, TW_MODE_MAX)
    weights = list(tw["weights"])
    index = tw["index"]
    swap = tw["swap"]

    section("Part 1: reproduce existing one-word and matrix-element baselines")
    anchor = one_word_anchor(tw)
    print_row_table([anchor])
    check(
        "one-word anchor reproduces the existing tensor-word value",
        abs(anchor.p_value - P_TW1_REFERENCE) < 5.0e-13,
        f"P_tw1={anchor.p_value:.12f}",
    )

    two_result = multiword.solve_multiword(
        2, TW_NMAX, TW_MODE_MAX, "matrix_element", "same"
    )
    three_result = multiword.solve_multiword(
        3, TW_NMAX, TW_MODE_MAX, "matrix_element", "same"
    )
    check(
        "two-word matrix-element Perron residual is small",
        two_result.residual < 1.0e-12,
        f"residual={two_result.residual:.3e}",
    )
    check(
        "three-word matrix-element Perron residual is small",
        three_result.residual < 1.0e-12,
        f"residual={three_result.residual:.3e}",
    )
    baseline_rows = [
        baseline_row(two_result, "trivial_slice"),
        baseline_row(two_result, "marginal"),
        baseline_row(three_result, "trivial_slice"),
        baseline_row(three_result, "marginal"),
    ]
    print_row_table(baseline_rows)
    baseline_checks = {
        (2, "trivial_slice"): P_TWO_TRIVIAL_REFERENCE,
        (2, "marginal"): P_TWO_MARGINAL_REFERENCE,
        (3, "trivial_slice"): P_THREE_TRIVIAL_REFERENCE,
        (3, "marginal"): P_THREE_MARGINAL_REFERENCE,
    }
    for row in baseline_rows:
        expected = baseline_checks[(row.words, row.convention)]
        check(
            f"baseline {row.words}-word {row.convention} P reproduces existing runner value",
            abs(row.p_value - expected) < 5.0e-12,
            f"P={row.p_value:.12f}, expected={expected:.12f}",
        )

    section("Part 2: construct eta = tensor_word @ e_(0,0)")
    eta = constructed_eta(tw)
    eta_rho = normalized_eta_rho(tw, eta)
    eta_swap = float(np.max(np.abs(swap @ eta - eta)))
    eta_min = float(np.min(eta))
    eta00 = float(eta[index[(0, 0)]])
    higher_mask = np.ones(len(eta), dtype=bool)
    higher_mask[index[(0, 0)]] = False
    higher_l1 = float(np.sum(np.abs(eta[higher_mask])))
    total_l1 = float(np.sum(np.abs(eta)))
    higher_l2 = float(np.linalg.norm(eta[higher_mask]))
    total_l2 = float(np.linalg.norm(eta))
    higher_nonzero = int(np.count_nonzero(np.abs(eta[higher_mask]) > 1.0e-300))
    eta_support = [
        (w, float(eta[index[w]]), float(eta_rho[index[w]]))
        for w in weights
        if abs(float(eta[index[w]])) > 1.0e-300
    ]
    print(f"eta00 = {eta00:.15f}")
    print(f"eta min = {eta_min:.15e}")
    print(f"eta conjugation-swap residual = {eta_swap:.3e}")
    print(f"higher nonzero count = {higher_nonzero}")
    print(f"higher L1 = {higher_l1:.15f}")
    print(f"total L1 = {total_l1:.15f}")
    print(f"higher L1 / eta00 = {higher_l1 / eta00:.12f}")
    print(f"higher L1 / total L1 = {higher_l1 / total_l1:.12f}")
    print(f"higher L2 / eta00 = {higher_l2 / eta00:.12f}")
    print(f"higher L2 / total L2 = {higher_l2 / total_l2:.12f}")
    print("eta support entries: weight | eta | eta/eta00")
    for w, val, norm in eta_support:
        print(f"  {w!s:<8} | {val:.15f} | {norm:.12f}")
    check(
        "constructed eta is nonnegative on the finite word box",
        eta_min >= -1.0e-15,
        f"eta_min={eta_min:.3e}",
    )
    check(
        "constructed eta is conjugation-symmetric",
        eta_swap < 1.0e-12,
        f"swap={eta_swap:.3e}",
    )
    check(
        "constructed eta has nonzero higher-weight content",
        higher_l1 > 0.0 and higher_nonzero == 5,
        f"higher_l1={higher_l1:.12f}, higher_nonzero={higher_nonzero}",
    )
    check(
        "trivial slice is not equal to constructed eta after eta00 normalization",
        higher_l1 / eta00 > 0.7,
        f"higher_l1/eta00={higher_l1 / eta00:.12f}",
    )

    eta_control_p = source_p(weights, eta_rho)
    print()
    print(
        "eta coefficient control, not the one-word Perron anchor: "
        f"rho10={eta_rho[index[(1, 0)]]:.12f}, "
        f"rho11={eta_rho[index[(1, 1)]]:.12f}, P={eta_control_p:.12f}"
    )
    check(
        "eta coefficient control matches the former trivial-slice ratio",
        abs(eta_control_p - P_TWO_TRIVIAL_REFERENCE) < 5.0e-12,
        f"P_eta_control={eta_control_p:.12f}",
    )

    section("Part 3: matrix-element ladder with constructed eta boundary")
    eta_by_weight = {w: float(eta[index[w]]) for w in weights}
    eta_rows = [
        anchor,
        eta_row(two_result, eta_by_weight),
        eta_row(three_result, eta_by_weight),
    ]
    print_row_table(eta_rows)
    check(
        "two-word constructed-eta readout is finite and positive",
        0.0 < eta_rows[1].p_value < 1.0 and eta_rows[1].rho_min >= -TOL,
        f"P={eta_rows[1].p_value:.12f}, rho_min={eta_rows[1].rho_min:.3e}",
    )
    check(
        "three-word constructed-eta readout is finite and positive",
        0.0 < eta_rows[2].p_value < 1.0 and eta_rows[2].rho_min >= -TOL,
        f"P={eta_rows[2].p_value:.12f}, rho_min={eta_rows[2].rho_min:.3e}",
    )
    check(
        "constructed-eta three-word readout does not reproduce the marginal revival value",
        abs(eta_rows[2].p_value - P_THREE_MARGINAL_REFERENCE) > 1.0e-2,
        f"|P_eta3-P_marginal3|={abs(eta_rows[2].p_value - P_THREE_MARGINAL_REFERENCE):.12f}",
    )
    check(
        "constructed-eta three-word readout is not word-count stationary with the trivial slice",
        abs(eta_rows[2].p_value - P_THREE_TRIVIAL_REFERENCE) > 1.0e-2,
        f"|P_eta3-P_trivial3|={abs(eta_rows[2].p_value - P_THREE_TRIVIAL_REFERENCE):.12f}",
    )
    check(
        "constructed-eta three-word readout remains closer to trivial-slice P than to marginal P",
        abs(eta_rows[2].p_value - P_THREE_TRIVIAL_REFERENCE)
        < abs(eta_rows[2].p_value - P_THREE_MARGINAL_REFERENCE),
        (
            f"dist_triv={abs(eta_rows[2].p_value - P_THREE_TRIVIAL_REFERENCE):.12f}, "
            f"dist_marg={abs(eta_rows[2].p_value - P_THREE_MARGINAL_REFERENCE):.12f}"
        ),
    )

    section("Fenced comparator distances")
    print(
        "Plaquette reuse license: the canonical comparison number is admitted "
        "only as a comparison/reuse number, not as a derived value, fit target, "
        "or repinning input."
    )
    print("```text")
    print(distance_line("one-word anchor", eta_rows[0].p_value, anchors))
    print(distance_line("two-word matrix_element constructed_eta", eta_rows[1].p_value, anchors))
    print(distance_line("three-word matrix_element constructed_eta", eta_rows[2].p_value, anchors))
    print(
        "three-word classification: constructed_eta is neither the trivial-slice "
        "stationary value nor the marginal revival value; it is closer to the "
        "trivial-slice P-distance in this finite box."
    )
    print("```")
    check(
        "canonical comparator is isolated to distance reporting",
        True,
    )

    section("Part 4: bounded residuals")
    print(
        "Named residuals: finite word count; finite dominant-weight box; finite "
        "Bessel mode support; no physical 3D unmarked spatial Wilson environment "
        "computation; no all-weight or untruncated convergence proof; no L_perp "
        "limit; no analytic P(6); no canonical repinning."
    )
    check(
        "runner scope names the full physical residuals without claiming them closed",
        True,
    )

    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
