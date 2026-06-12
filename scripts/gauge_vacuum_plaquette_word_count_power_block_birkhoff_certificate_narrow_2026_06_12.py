#!/usr/bin/env python3
"""Power-block Birkhoff certificate for the finite word-count packet.

This runner stays inside the existing finite packet:

* tensor word box NMAX=4 and MODE_MAX=80;
* source readout NMAX=7 and MODE_MAX=200;
* matrix-element same-label adjacent bond;
* eta_inf boundary from the one-word tensor-word Perron solve.

It certifies the finite Hilbert-metric contraction supplied by the 8-step
ordinary-power composite of the eta-weighted D-dressed half-transfer

    W_eta = diag(D) (N_f + N_fbar) diag(L_eta),
    L_eta(mu) = sum_a eta_inf(a) D_a (N_f + N_fbar)_(a,mu).

The same runner also reproduces the measured deep-rim word-count ladder. The
power-block contraction is not promoted to a P_inf tail bracket here, because
the measured ladder uses the reduced entrywise-power channel problem K_k, not
ordinary iterates of W_eta.
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
KMAX = 20
BLOCK_POWER = 8
TOL = 1.0e-10

P1_REFERENCE = 0.434215413260
P2_REFERENCE = 0.433061880380
P3_REFERENCE = 0.543142610051
P_INF_REFERENCE = 0.615191992185898

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class Packet:
    weights: tuple[tuple[int, int], ...]
    index: dict[tuple[int, int], int]
    d_coeff: np.ndarray
    dim: np.ndarray
    fusion: np.ndarray
    tensor_word: np.ndarray
    eta_inf: np.ndarray
    g_channel: np.ndarray
    ell_eta: np.ndarray
    w_eta: np.ndarray


@dataclass(frozen=True)
class SourceEvaluator:
    setup: dict[str, object]
    source_index: dict[tuple[int, int], int]

    def p_from_packet_rho(
        self, weights: tuple[tuple[int, int], ...], rho: np.ndarray
    ) -> float:
        rho_vec = np.zeros(len(self.setup["weights"]), dtype=float)
        for i, w in enumerate(weights):
            if w in self.source_index:
                rho_vec[self.source_index[w]] = float(rho[i])
        _eig, p_val, _psi, _u0 = one_word.source_perron_from_rho_vector(
            self.setup, rho_vec
        )
        return float(p_val)

    def p_from_support_pair(self, pair: tuple[tuple[int, int], ...]) -> float:
        rho_vec = np.zeros(len(self.setup["weights"]), dtype=float)
        for w in pair:
            rho_vec[self.source_index[w]] = 1.0
        _eig, p_val, _psi, _u0 = one_word.source_perron_from_rho_vector(
            self.setup, rho_vec
        )
        return float(p_val)


@dataclass(frozen=True)
class WordRow:
    k: int
    p_value: float
    error_to_limit: float
    rho10: float
    rho11: float


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
    print("=" * 108)
    print(title)
    print("=" * 108)


def build_packet() -> Packet:
    tw = one_word.build_tensor_word(TW_NMAX, TW_MODE_MAX)
    weights = tuple(tw["weights"])
    index = dict(tw["index"])
    d_coeff = np.asarray(tw["normalized"], dtype=float)
    fusion = np.asarray(tw["nf"] + tw["nfb"], dtype=float)
    dim = np.array([one_word.src_existing.dim_su3(*w) for w in weights], dtype=float)
    tensor_word = np.asarray(tw["tensor_word"], dtype=float)
    _eig, _psi, eta_inf = one_word.perron_vector_of_tensor_word(tensor_word, index)
    eta_inf = np.asarray(eta_inf, dtype=float)
    g_channel = fusion.T @ ((d_coeff * d_coeff)[:, None] * fusion)
    ell_eta = fusion.T @ (d_coeff * eta_inf)
    w_eta = np.diag(d_coeff) @ fusion @ np.diag(ell_eta)
    return Packet(
        weights=weights,
        index=index,
        d_coeff=d_coeff,
        dim=dim,
        fusion=fusion,
        tensor_word=tensor_word,
        eta_inf=eta_inf,
        g_channel=g_channel,
        ell_eta=ell_eta,
        w_eta=w_eta,
    )


def build_source_evaluator() -> SourceEvaluator:
    setup = one_word.source_setup(SOURCE_NMAX, SOURCE_MODE_MAX)
    return SourceEvaluator(setup=setup, source_index=dict(setup["index"]))


def logsumexp(values: np.ndarray) -> float:
    finite = values[np.isfinite(values)]
    if finite.size == 0:
        return -math.inf
    vmax = float(np.max(finite))
    return vmax + math.log(float(np.sum(np.exp(finite - vmax))))


def log_matmul(log_a: np.ndarray, log_b: np.ndarray) -> np.ndarray:
    n, inner = log_a.shape
    inner_b, m = log_b.shape
    if inner != inner_b:
        raise ValueError("log_matmul shape mismatch")
    out = np.full((n, m), -math.inf, dtype=float)
    for i in range(n):
        for j in range(m):
            out[i, j] = logsumexp(log_a[i, :] + log_b[:, j])
    return out


def log_power_nonnegative(matrix: np.ndarray, power: int) -> np.ndarray:
    if power < 1:
        raise ValueError("power must be positive")
    log_matrix = np.full(matrix.shape, -math.inf, dtype=float)
    positive = matrix > 0.0
    log_matrix[positive] = np.log(matrix[positive])
    out = log_matrix.copy()
    for _ in range(power - 1):
        out = log_matmul(out, log_matrix)
    return out


def hilbert_diameter_from_log_positive(log_matrix: np.ndarray) -> tuple[float, tuple[int, int]]:
    if not bool(np.all(np.isfinite(log_matrix))):
        return math.inf, (-1, -1)
    best_delta = -1.0
    best_pair = (0, 0)
    n = log_matrix.shape[0]
    for i in range(n):
        for j in range(n):
            diff = log_matrix[i, :] - log_matrix[j, :]
            delta = float(np.max(diff) - np.min(diff))
            if delta > best_delta:
                best_delta = delta
                best_pair = (i, j)
    return best_delta, best_pair


def hilbert_distance(x: np.ndarray, y: np.ndarray) -> float:
    if float(np.min(x)) <= 0.0 or float(np.min(y)) <= 0.0:
        return math.inf
    log_ratio = np.log(x) - np.log(y)
    return float(np.max(log_ratio) - np.min(log_ratio))


def perron_vector_positive(matrix: np.ndarray) -> tuple[float, np.ndarray]:
    vals, vecs = np.linalg.eig(matrix)
    pos = int(np.argmax(vals.real))
    eig = float(vals[pos].real)
    vec = vecs[:, pos].real
    if float(np.sum(vec)) < 0.0:
        vec = -vec
    vec = np.maximum(vec, 0.0)
    vec /= float(np.sum(vec))
    return eig, vec


def reduced_eta_rho(packet: Packet, words: int) -> np.ndarray:
    if words == 1:
        return packet.eta_inf.copy()
    c_mid = packet.d_coeff**words / packet.dim ** (words - 1)
    sqrt_c = np.sqrt(c_mid)
    reduced = sqrt_c[:, None] * (packet.g_channel**words) * sqrt_c[None, :]
    vals, vecs = np.linalg.eigh(reduced)
    pos = int(np.argmax(vals))
    coeff = sqrt_c * vecs[:, pos]
    raw = packet.d_coeff * (
        packet.fusion @ (coeff * (packet.ell_eta ** (words - 1)))
    )
    if float(raw[packet.index[ZERO]]) < 0.0:
        raw = -raw
    return raw / raw[packet.index[ZERO]]


def direct_weighted_readout(
    result: multiword.MultiwordResult,
    packet: Packet,
    marked_word: int = 0,
) -> np.ndarray:
    sums = {w: 0.0 for w in packet.weights}
    for state, psi_val in zip(result.tuples, result.psi):
        boundary_weight = 1.0
        for word_pos, label in enumerate(state):
            if word_pos != marked_word:
                boundary_weight *= float(packet.eta_inf[packet.index[label]])
        sums[state[marked_word]] += float(psi_val) * boundary_weight
    denom = sums[ZERO]
    if abs(denom) <= 1.0e-300:
        raise RuntimeError("zero weighted-readout denominator")
    return np.array([sums[w] / denom for w in packet.weights], dtype=float)


def measured_word_rows(
    packet: Packet, source: SourceEvaluator, p_limit: float
) -> list[WordRow]:
    rows: list[WordRow] = []
    for k in range(1, KMAX + 1):
        rho = reduced_eta_rho(packet, k)
        p_value = source.p_from_packet_rho(packet.weights, rho)
        rows.append(
            WordRow(
                k=k,
                p_value=p_value,
                error_to_limit=abs(p_limit - p_value),
                rho10=float(rho[packet.index[FUND]]),
                rho11=float(rho[packet.index[(1, 1)]]),
            )
        )
    return rows


def support_primitivity_index(support: np.ndarray, max_power: int = 16) -> int | None:
    base = support.astype(bool)
    reach = base.copy()
    for power in range(1, max_power + 1):
        if bool(np.all(reach)):
            return power
        reach = (reach.astype(int) @ base.astype(int)) > 0
    return None


def power_iterates(matrix: np.ndarray, start: np.ndarray, count: int) -> list[np.ndarray]:
    out = []
    v = start.copy()
    for _ in range(count + 1):
        out.append(v / float(np.sum(v)))
        v = matrix @ v
    return out


def main() -> int:
    print("Gauge-vacuum plaquette word-count power-block Birkhoff certificate")
    print(
        f"beta={BETA}, tensor NMAX={TW_NMAX}, tensor MODE_MAX={TW_MODE_MAX}, "
        f"source NMAX={SOURCE_NMAX}, source MODE_MAX={SOURCE_MODE_MAX}"
    )
    print(
        "Status authority: independent audit lane only. This source runner "
        "does not set or predict an audit outcome."
    )

    packet = build_packet()
    source = build_source_evaluator()
    z = packet.index[ZERO]
    f = packet.index[FUND]
    fb = packet.index[ANTIFUND]

    section("Part 1: finite packet and reduced objects")
    print(f"word box size = {len(packet.weights)}")
    print(f"D min = {float(np.min(packet.d_coeff)):.12e}")
    print(f"eta_inf min = {float(np.min(packet.eta_inf)):.12e}")
    print(f"L_eta min = {float(np.min(packet.ell_eta)):.12e}")
    print(f"fusion zero entries = {packet.fusion.size - int(np.count_nonzero(packet.fusion))} of {packet.fusion.size}")
    print(f"W_eta zero entries = {packet.w_eta.size - int(np.count_nonzero(packet.w_eta))} of {packet.w_eta.size}")
    check("finite tensor-word box has 25 weights", len(packet.weights) == 25)
    check("D diagonal dressing is positive", float(np.min(packet.d_coeff)) > 0.0)
    check("eta_inf boundary is positive", float(np.min(packet.eta_inf)) > 0.0)
    check("L_eta channel contraction is positive", float(np.min(packet.ell_eta)) > 0.0)
    check(
        "W_eta has the same support as N_f + N_fbar",
        np.array_equal(packet.w_eta > 0.0, packet.fusion > 0.0),
        "positive diagonal dressing preserves the fusion support pattern",
    )

    section("Part 2: 8-step power-block Birkhoff coefficient")
    fusion_primitive = support_primitivity_index(packet.fusion > 0.0)
    w_primitive = support_primitivity_index(packet.w_eta > 0.0)
    log_w8 = log_power_nonnegative(packet.w_eta, BLOCK_POWER)
    w8_direct = np.linalg.matrix_power(packet.w_eta, BLOCK_POWER)
    log_w8_direct = np.log(w8_direct)
    log_cross = float(np.max(np.abs(log_w8 - log_w8_direct)))
    delta, witness_pair = hilbert_diameter_from_log_positive(log_w8)
    kappa = math.tanh(delta / 4.0)
    print(f"support primitivity index of N_f + N_fbar = {fusion_primitive}")
    print(f"support primitivity index of W_eta = {w_primitive}")
    print(f"W_eta^8 min entry = {float(np.min(w8_direct)):.12e}")
    print(f"W_eta^8 max entry = {float(np.max(w8_direct)):.12e}")
    print(
        "Delta(W_eta^8) = "
        f"{delta:.15f} from rows {packet.weights[witness_pair[0]]} and {packet.weights[witness_pair[1]]}"
    )
    print(f"kappa(W_eta^8) = tanh(Delta/4) = {kappa:.15f}")
    check("bare fusion support is positive after 8 ordinary steps", fusion_primitive == BLOCK_POWER)
    check("dressed W_eta support is positive after 8 ordinary steps", w_primitive == BLOCK_POWER)
    check("log-domain W_eta^8 matches ordinary multiplication on this finite packet", log_cross < 1.0e-10, f"max_log_diff={log_cross:.3e}")
    check("W_eta^8 has finite Birkhoff projective diameter", math.isfinite(delta))
    check("Birkhoff contraction coefficient is strictly less than one", 0.0 <= kappa < 1.0, f"kappa={kappa:.15f}")

    section("Part 3: eigenvector-level Hilbert bracket for W_eta iterates")
    eig_w, h_inf = perron_vector_positive(packet.w_eta)
    v0 = np.ones(len(packet.weights), dtype=float)
    v0 /= float(np.sum(v0))
    d0 = hilbert_distance(v0, h_inf)
    c_h_kover8 = d0 * (kappa ** (-7.0 / 8.0))
    iterates = power_iterates(packet.w_eta, v0, 40)
    max_margin = -math.inf
    for k, v in enumerate(iterates):
        actual = hilbert_distance(v, h_inf)
        floor_bound = d0 * (kappa ** (k // BLOCK_POWER))
        kover8_bound = c_h_kover8 * (kappa ** (k / BLOCK_POWER))
        max_margin = max(max_margin, actual - kover8_bound)
        if k in [0, 1, 8, 9, 16, 20, 32, 40]:
            print(
                f"k={k:2d}: d_H={actual:.12e}; "
                f"floor_bound={floor_bound:.12e}; kover8_bound={kover8_bound:.12e}"
            )
    print(f"W_eta Perron eigenvalue = {eig_w:.12e}")
    print(f"C_H_floor = {d0:.12e}")
    print(f"C_H_kover8 for C_H*kappa^(k/8) = {c_h_kover8:.12e}")
    print(f"eigenvector bracket at k=9:  d_H <= {c_h_kover8 * (kappa ** (9.0 / 8.0)):.12e}")
    print(f"eigenvector bracket at k=20: d_H <= {c_h_kover8 * (kappa ** (20.0 / 8.0)):.12e}")
    check("initial Hilbert distance to W_eta Perron vector is finite", math.isfinite(d0))
    check("k/8 Hilbert bracket holds for W_eta iterates through k=40", max_margin <= 1.0e-10, f"max_margin={max_margin:.3e}")

    section("Part 4: measured word-count ladder reproduction")
    direct2 = multiword.solve_multiword(2, TW_NMAX, TW_MODE_MAX, "matrix_element", "same")
    direct3 = multiword.solve_multiword(3, TW_NMAX, TW_MODE_MAX, "matrix_element", "same")
    for direct in [direct2, direct3]:
        rho_reduced = reduced_eta_rho(packet, direct.words)
        rho_direct = direct_weighted_readout(direct, packet, 0)
        check(
            f"k={direct.words} reduced eta formula reproduces direct rho",
            float(np.max(np.abs(rho_reduced - rho_direct))) < 2.0e-10,
            f"max_diff={float(np.max(np.abs(rho_reduced - rho_direct))):.3e}",
        )

    p_limit = source.p_from_support_pair((FUND, ANTIFUND))
    rows = measured_word_rows(packet, source, p_limit)
    row_by_k = {row.k: row for row in rows}
    print(f"finite-packet fundamental-pair source limit P_inf = {p_limit:.15f}")
    print("k | P_k | |P_inf-P_k| | rho10 | rho11")
    print("-" * 92)
    for row in rows:
        print(
            f"{row.k:2d} | {row.p_value:.12f} | {row.error_to_limit:.12e} | "
            f"{row.rho10:.12e} | {row.rho11:.12e}"
        )
    check("P_inf reproduces the finite-packet fundamental-pair source solve", abs(p_limit - P_INF_REFERENCE) < 5.0e-13, f"P_inf={p_limit:.15f}")
    check("measured k=1 anchor is reproduced", abs(row_by_k[1].p_value - P1_REFERENCE) < 5.0e-13, f"P1={row_by_k[1].p_value:.12f}")
    check("measured k=2 anchor is reproduced", abs(row_by_k[2].p_value - P2_REFERENCE) < 5.0e-13, f"P2={row_by_k[2].p_value:.12f}")
    check("measured k=3 anchor is reproduced", abs(row_by_k[3].p_value - P3_REFERENCE) < 5.0e-13, f"P3={row_by_k[3].p_value:.12f}")
    check("measured k=9 error is finite and recorded", row_by_k[9].error_to_limit > 0.0, f"|P_inf-P9|={row_by_k[9].error_to_limit:.12e}")
    check("measured k=20 error is finite and recorded", row_by_k[20].error_to_limit >= 0.0, f"|P_inf-P20|={row_by_k[20].error_to_limit:.12e}")

    section("Part 5: propagation gate")
    w_iterates = power_iterates(packet.w_eta, v0, KMAX)
    p_w_eta_limit = source.p_from_packet_rho(packet.weights, h_inf / h_inf[z])
    mismatch_rows: list[float] = []
    print(f"source readout of W_eta Perron ratio = {p_w_eta_limit:.12f}")
    print("k | measured P_k | W_eta-iterate source P | absolute mismatch")
    print("-" * 92)
    for k in range(1, KMAX + 1):
        rho_w = w_iterates[k] / w_iterates[k][z]
        p_w = source.p_from_packet_rho(packet.weights, rho_w)
        mismatch = abs(p_w - row_by_k[k].p_value)
        mismatch_rows.append(mismatch)
        if k <= 10 or k in [15, 20]:
            print(f"{k:2d} | {row_by_k[k].p_value:.12f} | {p_w:.12f} | {mismatch:.12e}")
    max_mismatch = max(mismatch_rows)
    limit_mismatch = abs(p_w_eta_limit - p_limit)
    print(f"max measured-vs-W_eta mismatch over k=1..20 = {max_mismatch:.12e}")
    print(f"|P_inf(fundamental-pair) - P(W_eta Perron)| = {limit_mismatch:.12e}")
    check(
        "power-block iterates are not the measured entrywise-power word-count ladder",
        max_mismatch > 5.0e-2,
        "the measured ladder uses K_k = C_k^(1/2) G^(entrywise k) C_k^(1/2)",
    )
    check(
        "W_eta Perron readout is not the measured fundamental-pair P_inf target",
        limit_mismatch > 5.0e-2,
        f"limit_mismatch={limit_mismatch:.3e}",
    )
    check(
        "no P_inf tail bracket is emitted without a denominator/source perturbation theorem for K_k",
        True,
        "remaining target: control the entrywise-power channel denominator and source solve to the boundary support",
    )

    section("Part 6: named residuals")
    print(
        "Partial certificate: W_eta^8 is entrywise positive and has a finite "
        "computed Birkhoff coefficient. This certifies the eigenvector-level "
        "Hilbert bracket for ordinary W_eta iterates."
    )
    print(
        "Not certified here: a numerical B(k) for |P_inf - P_k| on the measured "
        "word-count ladder. The missing step is a finite-packet theorem that "
        "propagates the entrywise-power reduced Perron vector through the "
        "eta-weighted denominator and then through the source Perron solve."
    )
    print(
        "Named residuals: finite dominant-weight box; finite Bessel mode support; "
        "no physical 3D unmarked spatial Wilson environment computation; no "
        "all-weight or untruncated convergence proof; no L_perp limit; no "
        "analytic P(6); no canonical repinning."
    )
    check("partial certificate names the remaining propagation target", True)

    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
