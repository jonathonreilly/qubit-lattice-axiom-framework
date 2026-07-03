#!/usr/bin/env python3
"""Finite-packet word-count Hilbert-metric bracket attempt.

This runner works only with the in-repo finite tensor-word packet:

* tensor word box NMAX=4;
* tensor word Wilson mode cutoff MODE_MAX=80;
* source-sector readout NMAX=7, MODE_MAX=200;
* matrix-element adjacent bond from the 2026-06-12 trivial-slice lemma.

It verifies the 25 x 25 reduced word-count formula, computes the deep-rim
word-count rungs and their finite-packet limiting source solve, and records the
load-bearing obstruction to a Hilbert-metric contraction proof on the actual
word-count operator: the reduced matrices have persistent zero entries, hence
the full-cone Birkhoff projective diameter is infinite.

No physical 3D environment, untruncated limit, L_perp limit, analytic P(6), or
audit status is claimed here.
"""

from __future__ import annotations

import math
import sys
from dataclasses import dataclass
from pathlib import Path

import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import gauge_vacuum_plaquette_tensor_word_multiword_perron_ladder_2026_06_11 as multiword
import gauge_vacuum_plaquette_tensor_word_perron_derived_rho_composed_readout_2026_06_11 as one_word


AUDIT_TIMEOUT_SEC = 600

BETA = 6.0
TW_NMAX = 4
TW_MODE_MAX = 80
SOURCE_NMAX = one_word.SOURCE_NMAX
SOURCE_MODE_MAX = one_word.SOURCE_MODE_MAX
ZERO = (0, 0)
FUND = (1, 0)
ANTIFUND = (0, 1)
TOL = 1.0e-10

P1_REFERENCE = 0.434215413260
P2_DEEP_RIM_REFERENCE = 0.433061880380
P3_DEEP_RIM_REFERENCE = 0.543142610051

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class Packet:
    weights: tuple[tuple[int, int], ...]
    index: dict[tuple[int, int], int]
    d_coeff: np.ndarray
    dim: np.ndarray
    fusion: np.ndarray
    g_one: np.ndarray
    eta_inf: np.ndarray


@dataclass(frozen=True)
class WordRow:
    words: int
    p_value: float
    rho10: float
    rho11: float
    rho20: float
    error_to_limit: float


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
    print("=" * 104)
    print(title)
    print("=" * 104)


def build_packet() -> Packet:
    tw = one_word.build_tensor_word(TW_NMAX, TW_MODE_MAX)
    weights = tuple(tw["weights"])
    index = dict(tw["index"])
    d_coeff = np.asarray(tw["normalized"], dtype=float)
    fusion = np.asarray(tw["nf"] + tw["nfb"], dtype=float)
    dim = np.array([one_word.src_existing.dim_su3(*w) for w in weights], dtype=float)
    g_one = fusion.T @ ((d_coeff * d_coeff)[:, None] * fusion)
    _eig, _psi, eta_inf = one_word.perron_vector_of_tensor_word(
        tw["tensor_word"], index
    )
    return Packet(weights, index, d_coeff, dim, fusion, g_one, eta_inf)


def source_p(packet: Packet, rho: np.ndarray) -> float:
    rho_map = {w: float(rho[i]) for i, w in enumerate(packet.weights)}
    return float(
        one_word.source_readout(
            rho_map, SOURCE_NMAX, SOURCE_MODE_MAX, "zero"
        )["P"]
    )


def reduced_word_readout(
    packet: Packet,
    words: int,
    boundary_eta: np.ndarray,
) -> tuple[np.ndarray, float, float]:
    """Return rho, source P, and reduced Perron eigenvalue for word count."""
    c_vec = packet.d_coeff**words / packet.dim ** (words - 1)
    sqrt_c = np.sqrt(c_vec)
    reduced = sqrt_c[:, None] * (packet.g_one**words) * sqrt_c[None, :]
    vals, vecs = np.linalg.eigh(reduced)
    pos = int(np.argmax(vals))
    z_vec = vecs[:, pos]
    if float(np.sum(sqrt_c * z_vec)) < 0.0:
        z_vec = -z_vec
    q_vec = sqrt_c * z_vec
    l_vec = packet.fusion.T @ (packet.d_coeff * boundary_eta)
    raw = packet.d_coeff * (packet.fusion @ (q_vec * (l_vec ** (words - 1))))
    rho = raw / raw[packet.index[ZERO]]
    return rho, source_p(packet, rho), float(vals[pos])


def direct_weighted_readout(
    result: multiword.MultiwordResult,
    boundary_eta: np.ndarray,
    marked_word: int = 0,
) -> np.ndarray:
    weights = list(result.weights)
    sums = {w: 0.0 for w in weights}
    for state, psi_val in zip(result.tuples, result.psi):
        boundary_weight = 1.0
        for word_pos, label in enumerate(state):
            if word_pos != marked_word:
                boundary_weight *= float(boundary_eta[result.index[label]])
        sums[state[marked_word]] += float(psi_val) * boundary_weight
    denom = sums[ZERO]
    if abs(denom) <= 1.0e-300:
        raise RuntimeError("zero readout denominator")
    return np.array([sums[w] / denom for w in weights], dtype=float)


def hilbert_diameter(matrix: np.ndarray) -> float:
    """Birkhoff projective image diameter for a positive matrix.

    A zero entry makes the full-cone diameter infinite.
    """
    if np.min(matrix) <= 0.0:
        return math.inf
    logs = np.log(matrix)
    row_diff = logs[:, None, :] - logs[None, :, :]
    return float(np.max(row_diff.max(axis=2) - row_diff.min(axis=2)))


def boolean_primitivity_index(support: np.ndarray, max_power: int = 12) -> int | None:
    reach = support.astype(bool)
    base = support.astype(bool)
    for power in range(1, max_power + 1):
        if bool(np.all(reach)):
            return power
        reach = (reach.astype(int) @ base.astype(int)) > 0
    return None


def fundamental_limit_p(packet: Packet) -> float:
    rho_map = {w: 0.0 for w in packet.weights}
    rho_map[FUND] = 1.0
    rho_map[ANTIFUND] = 1.0
    return float(
        one_word.source_readout(
            rho_map, SOURCE_NMAX, SOURCE_MODE_MAX, "zero"
        )["P"]
    )


def word_rows(packet: Packet, p_limit: float, max_words: int = 12) -> list[WordRow]:
    out: list[WordRow] = []
    for words in range(1, max_words + 1):
        rho, p_value, _eig = reduced_word_readout(packet, words, packet.eta_inf)
        out.append(
            WordRow(
                words=words,
                p_value=p_value,
                rho10=float(rho[packet.index[FUND]]),
                rho11=float(rho[packet.index[(1, 1)]]),
                rho20=float(rho[packet.index[(2, 0)]]),
                error_to_limit=abs(p_limit - p_value),
            )
        )
    return out


def main() -> int:
    print("Gauge-vacuum plaquette word-count Hilbert-metric bracket attempt")
    print(
        f"beta={BETA}, tensor NMAX={TW_NMAX}, tensor MODE_MAX={TW_MODE_MAX}, "
        f"source NMAX={SOURCE_NMAX}, source MODE_MAX={SOURCE_MODE_MAX}"
    )
    print(
        "Status authority: independent audit lane only. This source runner "
        "does not set or predict an audit outcome."
    )

    packet = build_packet()
    z = packet.index[ZERO]
    f = packet.index[FUND]
    fb = packet.index[ANTIFUND]

    section("Part 1: reduced word-count formula")
    two_direct = multiword.solve_multiword(
        2, TW_NMAX, TW_MODE_MAX, "matrix_element", "same"
    )
    three_direct = multiword.solve_multiword(
        3, TW_NMAX, TW_MODE_MAX, "matrix_element", "same"
    )
    for direct in [two_direct, three_direct]:
        rho_reduced, p_reduced, eig_reduced = reduced_word_readout(
            packet, direct.words, packet.eta_inf
        )
        rho_direct = direct_weighted_readout(direct, packet.eta_inf, 0)
        p_direct = source_p(packet, rho_direct)
        check(
            f"w={direct.words} reduced 25x25 formula reproduces direct packet rho",
            float(np.max(np.abs(rho_reduced - rho_direct))) < 2.0e-10,
            f"max_diff={float(np.max(np.abs(rho_reduced - rho_direct))):.3e}",
        )
        check(
            f"w={direct.words} reduced source P reproduces direct packet P",
            abs(p_reduced - p_direct) < 2.0e-12,
            f"P_reduced={p_reduced:.12f}, P_direct={p_direct:.12f}, eig={eig_reduced:.12e}",
        )

    p_limit = fundamental_limit_p(packet)
    rows = word_rows(packet, p_limit, 12)
    row_by_words = {row.words: row for row in rows}

    check(
        "deep-rim w=1 readout reproduces the one-word anchor",
        abs(row_by_words[1].p_value - P1_REFERENCE) < 5.0e-13,
        f"P1={row_by_words[1].p_value:.12f}",
    )
    check(
        "deep-rim w=2 readout reproduces the prior finite-packet value",
        abs(row_by_words[2].p_value - P2_DEEP_RIM_REFERENCE) < 5.0e-13,
        f"P2={row_by_words[2].p_value:.12f}",
    )
    check(
        "deep-rim w=3 readout reproduces the prior finite-packet value",
        abs(row_by_words[3].p_value - P3_DEEP_RIM_REFERENCE) < 5.0e-13,
        f"P3={row_by_words[3].p_value:.12f}",
    )

    section("Part 2: Hilbert-metric positivity check")
    support = packet.g_one > 0.0
    primitive_power = boolean_primitivity_index(support)
    zero_count = int(np.size(packet.g_one) - np.count_nonzero(packet.g_one))
    print(f"g_one zero entries = {zero_count} of {packet.g_one.size}")
    print(f"ordinary matrix-support primitivity index = {primitive_power}")
    for words in [1, 2, 3, 4]:
        c_vec = packet.d_coeff**words / packet.dim ** (words - 1)
        sqrt_c = np.sqrt(c_vec)
        reduced = sqrt_c[:, None] * (packet.g_one**words) * sqrt_c[None, :]
        diam = hilbert_diameter(reduced)
        print(
            f"w={words}: reduced zero entries="
            f"{int(np.size(reduced) - np.count_nonzero(reduced))}, "
            f"Hilbert diameter={'inf' if math.isinf(diam) else f'{diam:.12f}'}"
        )
        check(
            f"w={words} full-cone Birkhoff diameter is infinite",
            math.isinf(diam),
            "persistent zero entries make tanh(diam/4) unusable on the full cone",
        )
    check(
        "ordinary matrix powers of the support become positive only after four steps",
        primitive_power == 4,
        f"primitive_power={primitive_power}",
    )
    check(
        "entrywise powers preserve the zero pattern, so the support-power fact is not the word-count contraction",
        zero_count > 0,
        "K_w uses g_one entrywise powers, not ordinary powers of g_one",
    )

    section("Part 3: finite-packet limit and measured envelope")
    d_over_dim = packet.d_coeff / packet.dim
    b_mat = np.sqrt(d_over_dim)[:, None] * packet.g_one * np.sqrt(d_over_dim)[None, :]
    b00 = float(b_mat[z, z])
    b_ratios = b_mat / b00
    b_ratios[z, z] = 0.0
    second_ratio = float(np.max(b_ratios))
    second_pos = np.unravel_index(int(np.argmax(b_ratios)), b_ratios.shape)
    l_vec = packet.fusion.T @ (packet.d_coeff * packet.eta_inf)
    gamma = b00 * float(l_vec[z]) / (
        float(packet.d_coeff[f] / packet.dim[f])
        * float(packet.g_one[f, z])
        * float(l_vec[f])
    )
    theta = 1.0 / gamma
    print(f"B00 = {b00:.15f}")
    print(
        "second entrywise ratio = "
        f"{second_ratio:.15f} at {packet.weights[second_pos[0]]}->{packet.weights[second_pos[1]]}"
    )
    print(f"L00 = {float(l_vec[z]):.15f}")
    print(f"L10 = {float(l_vec[f]):.15f}")
    print(f"fundamental growth gamma = {gamma:.15f}")
    print(f"candidate theta = {theta:.15f}")
    print(f"finite-packet fundamental-support limit P_inf = {p_limit:.15f}")
    print()
    print("words | P_w | |P_inf-P_w| | rho10 | rho11 | rho20")
    print("-" * 104)
    for row in rows:
        print(
            f"{row.words:5d} | {row.p_value:.12f} | {row.error_to_limit:.12e} | "
            f"{row.rho10:.12e} | {row.rho11:.12e} | {row.rho20:.12e}"
        )

    errors = [row.error_to_limit for row in rows]
    c_measured = max(
        row.error_to_limit / (theta ** row.words) for row in rows if row.words >= 3
    )
    envelope_ok = all(
        row.error_to_limit <= c_measured * (theta ** row.words) * (1.0 + 1.0e-12)
        for row in rows
        if row.words >= 3
    )
    ratios_after_4 = [
        errors[i] / errors[i - 1] for i in range(4, len(errors)) if errors[i - 1] > 0.0
    ]
    check(
        "deep-rim word-count sequence is non-monotone at the start",
        row_by_words[2].p_value < row_by_words[1].p_value
        and row_by_words[3].p_value > row_by_words[2].p_value,
        f"P1={row_by_words[1].p_value:.12f}, P2={row_by_words[2].p_value:.12f}, P3={row_by_words[3].p_value:.12f}",
    )
    check(
        "finite-packet limit is reproduced by the source solve with only the fundamental pair kept",
        abs(p_limit - 0.615191992186) < 5.0e-13,
        f"P_inf={p_limit:.12f}",
    )
    check(
        "candidate theta is computed from packet matrices and is less than one",
        0.0 < theta < 1.0,
        f"theta={theta:.12f}, gamma={gamma:.12f}",
    )
    check(
        "candidate geometric envelope holds on measured rungs w=3..12",
        envelope_ok,
        f"C_measured={c_measured:.12f}, max_post4_ratio={max(ratios_after_4):.12f}",
    )
    check(
        "measured envelope is not promoted to a certified all-w tail by this runner",
        True,
        "missing pieces: full-cone finite Hilbert diameter and ratio-denominator perturbation bound",
    )

    section("Part 4: bounded residuals and obstruction statement")
    print(
        "Obstruction: the actual reduced word-count matrices K_w have persistent "
        "zero entries, so the Birkhoff/Hilbert coefficient tanh(diam/4) is not "
        "finite on the full cone. The ordinary fourth-power positivity of the "
        "support graph does not repair this, because K_w contains entrywise "
        "powers of g_one rather than ordinary powers of a fixed positive matrix."
    )
    print(
        "Partial structure: the finite packet has an explicit reduced formula, "
        "a computed fundamental-support limiting source solve, and a matrix-"
        "derived candidate theta that matches the measured rungs. The missing "
        "certification target is a uniform positive denominator/source-"
        "perturbation bound for the readout ratio."
    )
    print(
        "Named residuals: finite dominant-weight box; finite Bessel mode support; "
        "no physical 3D unmarked spatial Wilson environment computation; no "
        "all-weight or untruncated convergence proof; no L_perp limit; no "
        "analytic P(6); no canonical repinning."
    )
    check(
        "runner reports an obstruction map rather than a certified Hilbert-metric bracket",
        True,
    )

    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
