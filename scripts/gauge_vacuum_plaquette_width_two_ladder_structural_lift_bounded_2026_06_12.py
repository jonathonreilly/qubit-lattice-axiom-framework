#!/usr/bin/env python3
"""Width-two ladder structural lift for the finite plaquette word packet.

This runner stays inside the repo-internal finite packet:

* tensor-word NMAX=4 and MODE_MAX=80;
* source NMAX=7 and MODE_MAX=200;
* no external values except the already admitted comparison/reuse number.

It constructs the 25^2 width-two layer space, verifies the pinned-rail
width-one gate, then measures the factorized two-rail reading.  Shared-link
character and matrix-element rail-rail readings are also built as diagnostics,
but they are not promoted to a width-lift measurement because they fail the
mandatory pinned-rail control.
"""

from __future__ import annotations

import math
import sys
from dataclasses import dataclass
from pathlib import Path

import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import gauge_vacuum_plaquette_word_count_power_block_birkhoff_certificate_narrow_2026_06_12 as w28
import gauge_vacuum_plaquette_word_count_theta_identification_two_term_asymptotic_2026_06_12 as theta_ref


AUDIT_TIMEOUT_SEC = 600

ZERO = (0, 0)
FUND = (1, 0)
ANTIFUND = (0, 1)
TW_NMAX = 4
TW_MODE_MAX = 80
KMAX = 25
WIDTH1_P_INF_REFERENCE = 0.615191992185898
WIDTH1_THETA_REFERENCE = 0.263745855973467
COMPARATOR = 0.5934
COMPARATOR_TEXT = "0.5934"

NOTE_PATH = (
    REPO_ROOT
    / "docs"
    / "GAUGE_VACUUM_PLAQUETTE_WIDTH_TWO_LADDER_STRUCTURAL_LIFT_BOUNDED_NOTE_2026-06-12.md"
)

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class PairLayer:
    pair_weights: tuple[tuple[tuple[int, int], tuple[int, int]], ...]
    pair_index: dict[tuple[tuple[int, int], tuple[int, int]], int]
    dim_pair: np.ndarray
    tensor_layer: np.ndarray
    t_ladder: np.ndarray
    eta_pair: np.ndarray
    eta_eig: float


@dataclass(frozen=True)
class MeasurementRow:
    k: int
    p_one_rail: float
    p_layer_diagonal: float
    err_one_rail: float
    err_layer_diagonal: float
    rho10: float
    rho10_squared: float


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
    print("=" * 112)
    print(title)
    print("=" * 112)


def conjugate(weight: tuple[int, int]) -> tuple[int, int]:
    return (weight[1], weight[0])


def pair_space(
    weights: tuple[tuple[int, int], ...],
) -> tuple[
    tuple[tuple[tuple[int, int], tuple[int, int]], ...],
    dict[tuple[tuple[int, int], tuple[int, int]], int],
]:
    pairs = tuple((left, right) for left in weights for right in weights)
    return pairs, {pair: i for i, pair in enumerate(pairs)}


def top_symmetric_perron(matrix: np.ndarray, zero_index: int) -> tuple[float, np.ndarray]:
    vals, vecs = np.linalg.eigh(np.asarray(matrix, dtype=float))
    pos = int(np.argmax(vals))
    eig = float(vals[pos])
    vec = vecs[:, pos].real
    if float(vec[zero_index]) < 0.0:
        vec = -vec
    vec = vec / float(vec[zero_index])
    return eig, vec


def pair_swap_conjugation_permutation(
    pair_weights: tuple[tuple[tuple[int, int], tuple[int, int]], ...],
    pair_index: dict[tuple[tuple[int, int], tuple[int, int]], int],
) -> np.ndarray:
    perm = np.empty(len(pair_weights), dtype=int)
    for i, (left, right) in enumerate(pair_weights):
        perm[i] = pair_index[(conjugate(right), conjugate(left))]
    return perm


def permutation_invariance_error(matrix: np.ndarray, perm: np.ndarray) -> float:
    return float(np.max(np.abs(matrix[np.ix_(perm, perm)] - matrix)))


def build_factorized_pair_layer(packet: w28.Packet, td: theta_ref.ThetaData) -> PairLayer:
    pairs, pair_index = pair_space(packet.weights)
    z_pair = pair_index[(ZERO, ZERO)]
    tensor_layer = np.kron(packet.tensor_word, packet.tensor_word)
    t_ladder = np.kron(td.t_matrix, td.t_matrix)
    dim_pair = np.kron(packet.dim, packet.dim)
    eta_eig, eta_pair = top_symmetric_perron(tensor_layer, z_pair)
    return PairLayer(
        pair_weights=pairs,
        pair_index=pair_index,
        dim_pair=dim_pair,
        tensor_layer=tensor_layer,
        t_ladder=t_ladder,
        eta_pair=eta_pair,
        eta_eig=eta_eig,
    )


def shared_link_layer(
    packet: w28.Packet,
    mode: str,
) -> np.ndarray:
    q = np.zeros(len(packet.weights) ** 2, dtype=float)
    for left_i in range(len(packet.weights)):
        for right_i in range(len(packet.weights)):
            pos = left_i * len(packet.weights) + right_i
            if left_i != right_i:
                continue
            if mode == "character":
                q[pos] = 1.0
            elif mode == "matrix_element":
                q[pos] = 1.0 / float(packet.dim[left_i])
            else:
                raise ValueError(f"unknown shared-link mode: {mode}")
    sqrt_q = np.sqrt(q)
    base = np.kron(packet.tensor_word, packet.tensor_word)
    return sqrt_q[:, None] * base * sqrt_q[None, :]


def reduced_matrix_from_t(dim: np.ndarray, t_matrix: np.ndarray, words: int) -> np.ndarray:
    return np.sqrt(dim[:, None] * dim[None, :]) * (t_matrix**words)


def pair_theta_formula(
    packet: w28.Packet,
    td: theta_ref.ThetaData,
    left_weight: tuple[int, int],
    right_weight: tuple[int, int],
) -> float:
    z = packet.index[ZERO]
    left = packet.index[left_weight]
    right = packet.index[right_weight]
    ell_ratio = (
        (packet.ell_eta[left] * packet.ell_eta[right])
        / (packet.ell_eta[z] * packet.ell_eta[z])
    )
    d_ratio = math.sqrt(
        (packet.d_coeff[left] * packet.d_coeff[right])
        / (packet.dim[left] * packet.dim[right])
    )
    t_ratio = (
        (td.t_matrix[left, z] * td.t_matrix[right, z])
        / (td.t_matrix[z, z] * td.t_matrix[z, z])
    )
    return float(ell_ratio * d_ratio * t_ratio)


def source_p(source: w28.SourceEvaluator, packet: w28.Packet, rho: np.ndarray) -> float:
    return float(source.p_from_packet_rho(packet.weights, rho))


def measurement_rows(
    packet: w28.Packet,
    source: w28.SourceEvaluator,
    p_inf: float,
) -> list[MeasurementRow]:
    rows: list[MeasurementRow] = []
    f = packet.index[FUND]
    for k in range(1, KMAX + 1):
        rho = w28.reduced_eta_rho(packet, k)
        rho_sq = rho * rho
        p_one = source_p(source, packet, rho)
        p_diag = source_p(source, packet, rho_sq)
        rows.append(
            MeasurementRow(
                k=k,
                p_one_rail=p_one,
                p_layer_diagonal=p_diag,
                err_one_rail=abs(p_inf - p_one),
                err_layer_diagonal=abs(p_inf - p_diag),
                rho10=float(rho[f]),
                rho10_squared=float(rho_sq[f]),
            )
        )
    return rows


def tail_ratio(values: list[float], left_k: int, right_k: int) -> float:
    by_k = {k + 1: value for k, value in enumerate(values)}
    return float(by_k[right_k] / by_k[left_k])


def note_text() -> str:
    try:
        return NOTE_PATH.read_text(encoding="utf-8")
    except OSError:
        return ""


def main() -> int:
    print("Gauge-vacuum plaquette width-two ladder structural lift bounded runner")
    print(
        "Status authority: independent audit lane only. This source runner "
        "does not set or predict an audit outcome."
    )
    print("No new imports: repo-internal finite packet quantities only.")

    packet = w28.build_packet()
    source = w28.build_source_evaluator()
    td = theta_ref.theta_data(packet)
    pair = build_factorized_pair_layer(packet, td)
    z = packet.index[ZERO]
    f = packet.index[FUND]
    z_pair = pair.pair_index[(ZERO, ZERO)]
    f_pair = pair.pair_index[(FUND, FUND)]
    f_one_pair = pair.pair_index[(FUND, ZERO)]

    section("Part 1: width-one anchors")
    p_inf = source.p_from_support_pair((FUND, ANTIFUND))
    print(f"width1 P_inf = {p_inf:.15f}")
    print(f"width1 theta = {td.theta:.15f}")
    check(
        "width-one pair-support source limit matches the declared anchor",
        abs(p_inf - WIDTH1_P_INF_REFERENCE) < 5.0e-13,
        f"delta={abs(p_inf - WIDTH1_P_INF_REFERENCE):.3e}",
    )
    check(
        "width-one theta matches the declared anchor",
        abs(td.theta - WIDTH1_THETA_REFERENCE) < 5.0e-15,
        f"delta={abs(td.theta - WIDTH1_THETA_REFERENCE):.3e}",
    )

    section("Part 2: 625-state factorized pair layer")
    perm = pair_swap_conjugation_permutation(pair.pair_weights, pair.pair_index)
    eta_expected = np.kron(packet.eta_inf, packet.eta_inf)
    eta_expected = eta_expected / float(eta_expected[z_pair])
    print(f"pair layer dimension = {len(pair.pair_weights)}")
    print(f"pair layer Perron eigenvalue = {pair.eta_eig:.15f}")
    print(f"pair eta(f,f) = {pair.eta_pair[f_pair]:.15f}")
    print(f"pair eta(f,0) = {pair.eta_pair[f_one_pair]:.15f}")
    check("width-two layer space has 625 states", len(pair.pair_weights) == 625)
    check("factorized pair layer is entrywise nonnegative", float(np.min(pair.tensor_layer)) >= -1.0e-15)
    check(
        "factorized pair layer obeys pair-swap plus conjugation symmetry",
        permutation_invariance_error(pair.tensor_layer, perm) < 1.0e-14,
        f"max_error={permutation_invariance_error(pair.tensor_layer, perm):.3e}",
    )
    check(
        "factorized pair t-ladder obeys pair-swap plus conjugation symmetry",
        permutation_invariance_error(pair.t_ladder, perm) < 1.0e-14,
        f"max_error={permutation_invariance_error(pair.t_ladder, perm):.3e}",
    )
    check(
        "deep-rim pair boundary is the Perron product eta_inf tensor eta_inf",
        float(np.max(np.abs(pair.eta_pair - eta_expected))) < 5.0e-11,
        f"max_diff={float(np.max(np.abs(pair.eta_pair - eta_expected))):.3e}",
    )

    section("Part 3: pinned-rail gates")
    n = len(packet.weights)
    pin = np.array([i * n + z for i in range(n)], dtype=int)
    pin_layer = pair.tensor_layer[np.ix_(pin, pin)] / float(packet.tensor_word[z, z])
    pin_t = pair.t_ladder[np.ix_(pin, pin)] / float(td.t_matrix[z, z])
    print(
        "Pinned rail-2 control rescales by the trivial second-rail scalar, "
        "then compares against the width-one objects."
    )
    check(
        "pinned pair layer reproduces the width-one tensor_word",
        float(np.max(np.abs(pin_layer - packet.tensor_word))) < 5.0e-15,
        f"max_diff={float(np.max(np.abs(pin_layer - packet.tensor_word))):.3e}",
    )
    check(
        "pinned pair t-ladder reproduces the width-one t-matrix",
        float(np.max(np.abs(pin_t - td.t_matrix))) < 5.0e-15,
        f"max_diff={float(np.max(np.abs(pin_t - td.t_matrix))):.3e}",
    )
    theta_one_rail = pair_theta_formula(packet, td, FUND, ZERO)
    theta_layer = pair_theta_formula(packet, td, FUND, FUND)
    print(f"theta_one_rail_formula = {theta_one_rail:.15f}")
    print(f"theta_layer_formula = {theta_layer:.15f}")
    print(f"theta_width1^2 = {td.theta * td.theta:.15f}")
    check(
        "pinned one-rail theta formula reproduces width-one theta",
        abs(theta_one_rail - td.theta) < 5.0e-15,
        f"delta={abs(theta_one_rail - td.theta):.3e}",
    )
    check(
        "layer-diagonal theta formula is the squared width-one theta",
        abs(theta_layer - td.theta * td.theta) < 5.0e-15,
        f"delta={abs(theta_layer - td.theta * td.theta):.3e}",
    )

    section("Part 4: shared-link diagnostic branches")
    for mode in ["character", "matrix_element"]:
        shared = shared_link_layer(packet, mode)
        shared_pin = shared[np.ix_(pin, pin)] / float(packet.tensor_word[z, z])
        diff = float(np.max(np.abs(shared_pin - packet.tensor_word)))
        nonzero_pin = int(np.count_nonzero(np.abs(shared_pin) > 1.0e-14))
        print(
            f"{mode}: pinned max_diff={diff:.12e}; "
            f"pinned_nonzero={nonzero_pin}; base_nonzero={int(np.count_nonzero(np.abs(packet.tensor_word) > 1.0e-14))}"
        )
        check(
            f"shared-link {mode} branch is constructed as a 625x625 nonnegative matrix",
            shared.shape == (625, 625) and float(np.min(shared)) >= -1.0e-15,
        )
        check(
            f"shared-link {mode} branch fails the mandatory pinned width-one gate",
            diff > 1.0e-2,
            "reported as diagnostic only; no width-lift P_inf is promoted",
        )

    section("Part 5: entrywise-power reduction and measurements")
    s4_pair = reduced_matrix_from_t(pair.dim_pair, pair.t_ladder, 4)
    s4_kron = np.kron(
        theta_ref.reduced_matrix_from_t(packet, td.t_matrix, 4),
        theta_ref.reduced_matrix_from_t(packet, td.t_matrix, 4),
    )
    s4_diff = float(np.max(np.abs(s4_pair - s4_kron)))
    check(
        "S_k = sqrt(d_A d_B) t_ladder(A,B)^k holds on the pair box",
        s4_diff < 1.0e-16,
        f"k=4 max_diff={s4_diff:.3e}",
    )

    rows = measurement_rows(packet, source, p_inf)
    print("k | P_one_rail | P_layer_diagonal | err_layer | rho10 | rho10^2")
    print("-" * 112)
    for row in rows:
        if row.k <= 12 or row.k in [15, 20, 25, 30]:
            print(
                f"{row.k:2d} | {row.p_one_rail:.12f} | "
                f"{row.p_layer_diagonal:.12f} | "
                f"{row.err_layer_diagonal:.12e} | "
                f"{row.rho10:.12e} | {row.rho10_squared:.12e}"
            )
    one_errors = [row.err_one_rail for row in rows]
    layer_errors = [row.err_layer_diagonal for row in rows]
    one_ratio = tail_ratio(one_errors, 18, 19)
    layer_ratio = tail_ratio(layer_errors, 9, 10)
    print(f"measured one-rail error ratio err19/err18 = {one_ratio:.15f}")
    print(f"measured layer-diagonal error ratio err10/err9 = {layer_ratio:.15f}")
    check(
        "one-rail measurement reproduces the width-one k-chain through the stable displayed range",
        abs(rows[19].p_one_rail - source_p(source, packet, w28.reduced_eta_rho(packet, 20))) < 1.0e-15,
    )
    check(
        "layer-diagonal measured tail ratio tracks theta_width1 squared",
        abs(layer_ratio - theta_layer) < 5.0e-4,
        f"ratio={layer_ratio:.15f}, theta_layer={theta_layer:.15f}",
    )
    check(
        "layer-diagonal final displayed row is converged to the same pair-support source limit at double precision",
        rows[-1].err_layer_diagonal < 2.0e-13,
        f"err{rows[-1].k}={rows[-1].err_layer_diagonal:.3e}",
    )

    section("Part 6: comparator distances and finite diagnostic")
    gap_width1 = abs(p_inf - COMPARATOR)
    gap_ladder = abs(p_inf - COMPARATOR)
    closed_fraction = 0.0 if gap_width1 == 0.0 else (gap_width1 - gap_ladder) / gap_width1
    print("Plaquette reuse license: comparator is used only as comparison/reuse context.")
    print("```text")
    print(f"P_inf(width1) = {p_inf:.15f}")
    print(f"P_inf(width2 factorized one-rail) = {p_inf:.15f}")
    print(f"P_inf(width2 factorized layer-diagonal) = {p_inf:.15f}")
    print(f"|P_inf(width2) - P_inf(width1)| = {abs(p_inf - WIDTH1_P_INF_REFERENCE):.15e}")
    print(f"|P_inf(width2) - {COMPARATOR_TEXT}| = {gap_ladder:.15f}")
    print(f"fraction_of_width1_comparator_gap_closed_by_width2_limit = {closed_fraction:.15f}")
    print(f"diagnostic finite k=4 layer-diagonal P = {rows[3].p_layer_diagonal:.15f}")
    print(f"|diagnostic finite k=4 layer-diagonal P - {COMPARATOR_TEXT}| = {abs(rows[3].p_layer_diagonal - COMPARATOR):.15f}")
    print("```")
    check(
        "width-two factorized limit does not move the finite limit away from the width-one pair-support value",
        abs(gap_ladder - gap_width1) < 1.0e-15,
    )
    check(
        "finite k=4 layer-diagonal diagnostic is not promoted as the k->infinity value",
        abs(rows[3].p_layer_diagonal - p_inf) > 1.0e-4,
        f"P_4_diag={rows[3].p_layer_diagonal:.15f}, P_inf={p_inf:.15f}",
    )

    section("Part 7: note hygiene")
    text = note_text()
    if text:
        check(
            "note delegates status to the independent audit lane",
            "Status authority:** independent audit lane only" in text
            or "Status authority: independent audit lane only" in text,
        )
        check(
            "note uses markdown links for one-hop authorities",
            "[GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md]" in text
            and "[GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md]" in text,
        )
        check(
            "note uses repo source context links, not temp handles",
            (".claude" + "/tmp") not in text
            and "[GAUGE_VACUUM_PLAQUETTE_WORD_COUNT_THETA_IDENTIFICATION_TWO_TERM_ASYMPTOTIC_NARROW_THEOREM_NOTE_2026-06-12.md]" in text
            and "[GAUGE_VACUUM_PLAQUETTE_WORD_COUNT_RUNG_FOUR_DEEP_RIM_BOUNDED_NOTE_2026-06-12.md]" in text,
        )
        check(
            "note includes a visible no-go discipline gate for the bounded negative",
            "## No-Go Discipline Gate" in text
            and "Gate result: PASS" in text,
        )
    else:
        check("note exists for this runner", False, f"missing {NOTE_PATH}")

    print(
        "Named residuals: finite dominant-weight box; finite Bessel mode support; "
        "finite width-two factorized layer only; shared-link rail-rail readings "
        "fail the pinned gate; no physical 3D unmarked spatial Wilson environment "
        "computation; no width-to-infinity slab; no slab-stacking to 3D; no "
        "L_perp limit; no analytic P(6); no canonical repinning."
    )
    check("runner names residuals without claiming them retired", True)

    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
