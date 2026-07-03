#!/usr/bin/env python3
"""Finite-packet trivial-slice eigen-identity check.

This runner verifies the narrow algebraic reason that the matrix-element
multi-word trivial-slice readout is word-count-stationary on the finite packet
used by the 2026-06-11 ladder runner.

No physical 3D environment, untruncated limit, L_perp limit, analytic P(6), or
audit status is claimed here.
"""

from __future__ import annotations

import itertools
import sys
from dataclasses import dataclass
from pathlib import Path

import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import gauge_vacuum_plaquette_tensor_word_multiword_perron_ladder_2026_06_11 as ladder
import gauge_vacuum_plaquette_tensor_word_perron_derived_rho_composed_readout_2026_06_11 as ref


AUDIT_TIMEOUT_SEC = 600

NMAX = 4
MODE_MAX = 80
ZERO = (0, 0)
FUND = (1, 0)
ANTIFUND = (0, 1)
MEASURED_RAW_SLICE_RATIO = 0.025986536153
TOL = 1.0e-12

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


def build_packet() -> Packet:
    tw = ref.build_tensor_word(NMAX, MODE_MAX)
    weights = tuple(tw["weights"])
    index = dict(tw["index"])
    d_coeff = np.asarray(tw["normalized"], dtype=float)
    fusion = np.asarray(tw["nf"] + tw["nfb"], dtype=float)
    dim = np.array([ref.src_existing.dim_su3(*w) for w in weights], dtype=float)
    g_one = fusion.T @ ((d_coeff * d_coeff)[:, None] * fusion)
    return Packet(weights, index, d_coeff, dim, fusion, g_one)


def slice_prediction(packet: Packet) -> np.ndarray:
    f = packet.index[FUND]
    fb = packet.index[ANTIFUND]
    z = packet.index[ZERO]
    numerator = packet.d_coeff * (packet.fusion[:, f] + packet.fusion[:, fb])
    denominator = packet.d_coeff[z] * (packet.fusion[z, f] + packet.fusion[z, fb])
    return numerator / denominator


def raw_trivial_slice(result: ladder.MultiwordResult) -> np.ndarray:
    raw = np.zeros(len(result.weights), dtype=float)
    for state, val in zip(result.tuples, result.psi):
        if all(state[pos] == ZERO for pos in range(1, result.words)):
            raw[result.index[state[0]]] = float(val)
    return raw


def normalized_trivial_slice(result: ladder.MultiwordResult) -> np.ndarray:
    raw = raw_trivial_slice(result)
    return raw / raw[result.index[ZERO]]


def channel_functional(result: ladder.MultiwordResult, packet: Packet, mu: tuple[int, int]) -> float:
    mu_i = packet.index[mu]
    total = 0.0
    for state, val in zip(result.tuples, result.psi):
        factor = float(val)
        for w in state:
            factor *= float(packet.d_coeff[packet.index[w]] * packet.fusion[packet.index[w], mu_i])
            if factor == 0.0:
                break
        total += factor
    return total


def eigen_rhs_slice_from_two_channels(result: ladder.MultiwordResult, packet: Packet) -> np.ndarray:
    f = packet.index[FUND]
    fb = packet.index[ANTIFUND]
    z = packet.index[ZERO]
    k = result.words
    h_f = channel_functional(result, packet, FUND)
    h_fb = channel_functional(result, packet, ANTIFUND)
    c_f = packet.d_coeff[f] ** k / packet.dim[f] ** (k - 1)
    c_fb = packet.d_coeff[fb] ** k / packet.dim[fb] ** (k - 1)
    out = np.zeros(len(packet.weights), dtype=float)
    for w in packet.weights:
        i = packet.index[w]
        out[i] = (
            packet.d_coeff[i]
            * packet.d_coeff[z] ** (k - 1)
            * (
                c_f * packet.fusion[i, f] * h_f
                + c_fb * packet.fusion[i, fb] * h_fb
            )
            / result.eigenvalue
        )
    return out


def reduced_slice(packet: Packet, words: int, mode: str = "matrix_element") -> tuple[float, np.ndarray, np.ndarray]:
    if mode == "matrix_element":
        middle_coeff = packet.d_coeff ** words / packet.dim ** (words - 1)
    elif mode == "character":
        middle_coeff = packet.d_coeff ** words
    elif mode == "perturbed_character":
        perturb = np.array([2.0 + p + 2.0 * q for p, q in packet.weights], dtype=float)
        middle_coeff = packet.d_coeff ** words * perturb ** (words - 1)
    else:
        raise ValueError(mode)

    sqrt_c = np.sqrt(middle_coeff)
    reduced = sqrt_c[:, None] * (packet.g_one ** words) * sqrt_c[None, :]
    vals, vecs = np.linalg.eigh(reduced)
    pos = int(np.argmax(vals))
    z_vec = vecs[:, pos]
    if float(np.sum(sqrt_c * z_vec)) < 0.0:
        z_vec = -z_vec
    coeff = sqrt_c * z_vec

    zero_i = packet.index[ZERO]
    raw = np.zeros(len(packet.weights), dtype=float)
    for w in packet.weights:
        i = packet.index[w]
        channel_sum = 0.0
        for mu_i in range(len(packet.weights)):
            channel_sum += (
                coeff[mu_i]
                * packet.fusion[i, mu_i]
                * packet.fusion[zero_i, mu_i] ** (words - 1)
            )
        raw[i] = packet.d_coeff[i] * packet.d_coeff[zero_i] ** (words - 1) * channel_sum
    rho = raw / raw[zero_i]
    return float(vals[pos]), raw, rho


def middle_support_check(packet: Packet, words: int) -> tuple[bool, float, int]:
    tuples = tuple(itertools.product(packet.weights, repeat=words))
    max_diff = 0.0
    nonzero = 0
    for state in tuples:
        d_prod = 1.0
        for w in state:
            d_prod *= float(packet.d_coeff[packet.index[w]])
        bond = 1.0
        for left, right in zip(state, state[1:]):
            if left != right:
                bond = 0.0
                break
            bond *= 1.0 / float(ref.src_existing.dim_su3(*left))
        middle = d_prod * bond
        if middle != 0.0:
            nonzero += 1
            lam = state[0]
            expected = (
                packet.d_coeff[packet.index[lam]] ** words
                / float(ref.src_existing.dim_su3(*lam)) ** (words - 1)
            )
            max_diff = max(max_diff, abs(middle - expected))
            if any(w != lam for w in state):
                return False, max_diff, nonzero
    return nonzero == len(packet.weights) and max_diff < 1.0e-15, max_diff, nonzero


def surviving_slice_channels(packet: Packet, words: int) -> set[tuple[int, int]]:
    zero_i = packet.index[ZERO]
    out: set[tuple[int, int]] = set()
    for mu in packet.weights:
        mu_i = packet.index[mu]
        if packet.fusion[zero_i, mu_i] ** (words - 1) != 0.0:
            out.add(mu)
    return out


def source_p(packet: Packet, rho: np.ndarray) -> float:
    rho_map = {w: float(rho[i]) for i, w in enumerate(packet.weights)}
    return float(ref.source_readout(rho_map, ref.SOURCE_NMAX, ref.SOURCE_MODE_MAX, "zero")["P"])


def main() -> int:
    print("Gauge-vacuum plaquette trivial-slice eigen-identity lemma runner")
    print(f"finite packet: NMAX={NMAX}, MODE_MAX={MODE_MAX}, words checked=2,3,4")

    packet = build_packet()
    pred = slice_prediction(packet)
    f = packet.index[FUND]
    fb = packet.index[ANTIFUND]
    z = packet.index[ZERO]
    adj_support = {w for w in packet.weights if abs(pred[packet.index[w]]) > 1.0e-15}

    section("Part 1: packet algebra identities")
    print(f"D(0,0)={packet.d_coeff[z]:.12f}")
    print(f"D(1,0)={packet.d_coeff[f]:.12f}")
    print(f"D(0,1)={packet.d_coeff[fb]:.12f}")
    print(f"dim(1,0)={packet.dim[f]:.0f}, dim(0,1)={packet.dim[fb]:.0f}")
    check(
        "fundamental and antifundamental packet coefficients match by conjugation",
        abs(packet.d_coeff[f] - packet.d_coeff[fb]) < 1.0e-15 and packet.dim[f] == packet.dim[fb],
        f"D_f-D_fb={packet.d_coeff[f] - packet.d_coeff[fb]:.3e}",
    )
    check(
        "trivial row of fusion sum sees exactly the fundamental pair",
        surviving_slice_channels(packet, 2) == {FUND, ANTIFUND},
        f"survivors={sorted(surviving_slice_channels(packet, 2))}",
    )
    check(
        "predicted slice support has six finite-box weights",
        adj_support == {ZERO, FUND, ANTIFUND, (1, 1), (2, 0), (0, 2)},
        f"support={sorted(adj_support)}",
    )
    for words in [2, 3]:
        ok, max_diff, nonzero = middle_support_check(packet, words)
        check(
            f"k={words} matrix-element middle support is the all-equal diagonal",
            ok,
            f"nonzero={nonzero}, max_diff={max_diff:.3e}",
        )
    check(
        "closed normalized formula gives the measured rho10 and rho11",
        abs(pred[f] - 0.2112658698249917) < 5.0e-15
        and abs(pred[packet.index[(1, 1)]] - 0.16225979947993815) < 5.0e-15,
        f"rho10={pred[f]:.12f}, rho11={pred[packet.index[(1, 1)]]:.12f}",
    )

    section("Part 2: two-word and three-word Perron slices")
    result2 = ladder.solve_multiword(2, NMAX, MODE_MAX, "matrix_element", "same")
    result3 = ladder.solve_multiword(3, NMAX, MODE_MAX, "matrix_element", "same")
    rho2 = normalized_trivial_slice(result2)
    rho3 = normalized_trivial_slice(result3)
    raw2 = raw_trivial_slice(result2)
    raw3 = raw_trivial_slice(result3)
    mask = np.abs(raw2) > 1.0e-14
    ratios = raw3[mask] / raw2[mask]
    spread = float(np.max(ratios) - np.min(ratios))
    common_ratio = float(np.mean(ratios))
    print(f"k=2 eig={result2.eigenvalue:.12f}, residual={result2.residual:.3e}")
    print(f"k=3 eig={result3.eigenvalue:.12f}, residual={result3.residual:.3e}")
    print(f"raw k=3/k=2 slice ratio={common_ratio:.12f}, spread={spread:.3e}")
    check(
        "two-word trivial slice equals the closed formula",
        float(np.max(np.abs(rho2 - pred))) < TOL,
        f"max_diff={float(np.max(np.abs(rho2 - pred))):.3e}",
    )
    check(
        "three-word trivial slice equals the closed formula",
        float(np.max(np.abs(rho3 - pred))) < TOL,
        f"max_diff={float(np.max(np.abs(rho3 - pred))):.3e}",
    )
    check(
        "measured raw two/three slice proportionality is reproduced",
        abs(common_ratio - MEASURED_RAW_SLICE_RATIO) < 5.0e-13 and spread < 2.0e-15,
        f"ratio={common_ratio:.12f}, reference={MEASURED_RAW_SLICE_RATIO:.12f}, spread={spread:.3e}",
    )
    svals = np.linalg.svd(result3.psi.reshape((25 * 25, 25)), compute_uv=False)
    singular_ratio = float(svals[1] / svals[0])
    check(
        "three-word full vector is not rank-one across the outer word",
        singular_ratio > 1.0e-2,
        f"second/top singular ratio={singular_ratio:.12f}",
    )

    section("Part 3: eigen-equation restriction checks")
    for result in [result2, result3]:
        rhs = eigen_rhs_slice_from_two_channels(result, packet)
        raw = raw_trivial_slice(result)
        h_f = channel_functional(result, packet, FUND)
        h_fb = channel_functional(result, packet, ANTIFUND)
        check(
            f"k={result.words} restricted eigen-equation is exactly the two-channel formula",
            float(np.max(np.abs(rhs - raw))) < 2.0e-13,
            f"max_diff={float(np.max(np.abs(rhs - raw))):.3e}",
        )
        check(
            f"k={result.words} Perron channel functionals are conjugation-equal",
            abs(h_f - h_fb) < 2.0e-13,
            f"h_f={h_f:.12e}, h_fb={h_fb:.12e}, diff={abs(h_f - h_fb):.3e}",
        )

    section("Part 4: k=4 finite-rank prediction")
    red2_eig, _red2_raw, red2_rho = reduced_slice(packet, 2, "matrix_element")
    red3_eig, _red3_raw, red3_rho = reduced_slice(packet, 3, "matrix_element")
    red4_eig, _red4_raw, red4_rho = reduced_slice(packet, 4, "matrix_element")
    print("The k=4 check uses the 25 x 25 finite-rank reduction of the same operator.")
    print(f"full k=4 dimension would be {len(packet.weights) ** 4}")
    print(f"k=4 reduced eig={red4_eig:.12f}")
    check(
        "finite-rank reduction reproduces the direct k=2 and k=3 eigenvalues",
        abs(red2_eig - result2.eigenvalue) < 2.0e-14 and abs(red3_eig - result3.eigenvalue) < 2.0e-14,
        f"k2_delta={abs(red2_eig - result2.eigenvalue):.3e}, k3_delta={abs(red3_eig - result3.eigenvalue):.3e}",
    )
    check(
        "finite-rank reduction reproduces the direct k=2 and k=3 slices",
        float(np.max(np.abs(red2_rho - rho2))) < TOL and float(np.max(np.abs(red3_rho - rho3))) < TOL,
        f"k2_diff={float(np.max(np.abs(red2_rho - rho2))):.3e}, k3_diff={float(np.max(np.abs(red3_rho - rho3))):.3e}",
    )
    check(
        "k=4 matrix-element trivial slice equals the k-independent formula",
        float(np.max(np.abs(red4_rho - pred))) < TOL,
        f"rho10={red4_rho[f]:.12f}, rho11={red4_rho[packet.index[(1, 1)]]:.12f}, max_diff={float(np.max(np.abs(red4_rho - pred))):.3e}",
    )
    p_val = source_p(packet, pred)
    check(
        "word-count-stationary trivial-slice source readout is reproduced",
        abs(p_val - 0.429196712321) < 5.0e-13,
        f"P={p_val:.12f}",
    )

    section("Part 5: falsification controls")
    char2_eig, _char2_raw, char2_rho = reduced_slice(packet, 2, "character")
    char3_eig, _char3_raw, char3_rho = reduced_slice(packet, 3, "character")
    pert2_eig, pert2_raw, pert2_rho = reduced_slice(packet, 2, "perturbed_character")
    pert3_eig, pert3_raw, pert3_rho = reduced_slice(packet, 3, "perturbed_character")
    pert_mask = np.abs(pert2_raw) > 1.0e-14
    pert_ratios = pert3_raw[pert_mask] / pert2_raw[pert_mask]
    pert_spread = float(np.max(pert_ratios) - np.min(pert_ratios))
    pert_norm_diff = float(np.max(np.abs(pert3_rho - pert2_rho)))
    print(f"symmetric character-control eigs: k2={char2_eig:.12f}, k3={char3_eig:.12f}")
    print(f"perturbed character-control eigs: k2={pert2_eig:.12f}, k3={pert3_eig:.12f}")
    print(f"perturbed normalized-slice max diff={pert_norm_diff:.3e}, raw-ratio spread={pert_spread:.3e}")
    check(
        "unperturbed character-level bond preserves this trivial-slice closure",
        float(np.max(np.abs(char2_rho - pred))) < TOL and float(np.max(np.abs(char3_rho - pred))) < TOL,
        f"k2_diff={float(np.max(np.abs(char2_rho - pred))):.3e}, k3_diff={float(np.max(np.abs(char3_rho - pred))):.3e}",
    )
    check(
        "conjugation-asymmetric character-level perturbation breaks slice proportionality",
        pert_norm_diff > 1.0e-2 and pert_spread > 1.0e-1,
        f"norm_diff={pert_norm_diff:.3e}, raw_spread={pert_spread:.3e}",
    )

    section("Part 6: bounded statement inputs")
    print(
        "Status authority: independent audit lane only. This source note does "
        "not set or predict an audit outcome."
    )
    print(
        "No new literature values, axioms, external citations, or comparator "
        "numbers are imported; all checks use the finite packet and landed "
        "runner construction."
    )
    print(
        "Named residuals: finite dominant-weight box; finite Bessel mode "
        "support; no full physical 3D environment computation; no all-weight "
        "or untruncated convergence proof; no L_perp limit; no evaluated full "
        "rim-boundary eta_beta^env; no analytic P(6)."
    )
    check(
        "closed formula is normalized at the trivial channel and nonnegative on the finite box",
        abs(pred[z] - 1.0) < 1.0e-15 and float(np.min(pred)) >= 0.0,
        f"min={float(np.min(pred)):.3e}, rho00={pred[z]:.12f}",
    )

    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
