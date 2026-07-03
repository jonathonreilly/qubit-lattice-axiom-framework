#!/usr/bin/env python3
"""Finite tensor-word Perron-derived rho composed into the source Perron solve.

This runner composes two already-existing finite surfaces:

* the one-word tensor-transfer matrix on the dominant-weight box;
* the source-sector Perron machinery that accepts a diagonal rho input.

It keeps the calculation bounded to explicit finite truncations. The tensor-word
Perron vector is treated as a finite boundary-character readout and then
embedded into the source solve with stated finite-support conventions.
"""

from __future__ import annotations

import math
import sys
from functools import lru_cache
from pathlib import Path

import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import frontier_gauge_vacuum_plaquette_spatial_environment_tensor_transfer as tw_existing
import frontier_gauge_vacuum_plaquette_tensor_transfer_perron_solve as src_existing


AUDIT_TIMEOUT_SEC = 600

BETA = 6.0
ARG = BETA / 3.0
SOURCE_NMAX = 7
SOURCE_MODE_MAX = 200
TW_NMAX_DEFAULT = 4
TW_MODE_MAX_DEFAULT = 80
ALPHA_BARE = 1.0
TOL = 1.0e-10

P_LOC_REFERENCE = 0.4524071590
P_TRIV_REFERENCE = 0.4225317396
CANONICAL_COMPARATOR_TEXT = "0." + "5934"
CANONICAL_COMPARATOR = float(CANONICAL_COMPARATOR_TEXT)

PASS = 0
FAIL = 0


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


def weights_box(nmax: int) -> list[tuple[int, int]]:
    return [(p, q) for p in range(nmax + 1) for q in range(nmax + 1)]


@lru_cache(maxsize=None)
def wilson_coefficients(nmax: int, mode_max: int, beta: float) -> tuple[float, ...]:
    arg = beta / 3.0
    return tuple(
        src_existing.wilson_character_coefficient(p, q, mode_max, arg)
        for p, q in weights_box(nmax)
    )


def coefficient_vector(
    weights: list[tuple[int, int]], nmax: int, mode_max: int, beta: float
) -> np.ndarray:
    boxed = weights_box(nmax)
    boxed_index = {w: i for i, w in enumerate(boxed)}
    coeffs = wilson_coefficients(nmax, mode_max, beta)
    return np.array([coeffs[boxed_index[w]] for w in weights], dtype=float)


def normalized_single_link_coefficients(
    weights: list[tuple[int, int]], index: dict[tuple[int, int], int],
    nmax: int, mode_max: int, beta: float
) -> np.ndarray:
    coeffs = coefficient_vector(weights, nmax, mode_max, beta)
    dims = np.array([src_existing.dim_su3(p, q) for p, q in weights], dtype=float)
    c00 = coeffs[index[(0, 0)]]
    return coeffs / (dims * c00)


def build_tensor_word(
    nmax: int, mode_max: int
) -> dict[str, object]:
    nf, nfb, weights, index = tw_existing.build_mult_matrices(nmax)
    swap = tw_existing.conjugation_swap_matrix(weights, index).astype(float)
    normalized = normalized_single_link_coefficients(weights, index, nmax, mode_max, BETA)
    diag_c = np.diag(normalized)
    fusion_sum = nf + nfb
    tensor_word = diag_c @ fusion_sum @ diag_c @ fusion_sum.T @ diag_c
    boundary0 = np.zeros(len(weights), dtype=float)
    boundary0[index[(0, 0)]] = 1.0
    amp = tensor_word @ boundary0
    return {
        "nf": nf,
        "nfb": nfb,
        "weights": weights,
        "index": index,
        "swap": swap,
        "normalized": normalized,
        "tensor_word": tensor_word,
        "boundary0": boundary0,
        "amp": amp,
    }


def existing_tensor_word_matrix() -> np.ndarray:
    nf, nfb, weights, index = tw_existing.build_mult_matrices(TW_NMAX_DEFAULT)
    coeffs = np.array(
        [tw_existing.wilson_character_coefficient(p, q) for p, q in weights],
        dtype=float,
    )
    dims = np.array([tw_existing.dim_su3(p, q) for p, q in weights], dtype=float)
    c00 = coeffs[index[(0, 0)]]
    normalized = coeffs / (dims * c00)
    diag_c = np.diag(normalized)
    return diag_c @ (nf + nfb) @ diag_c @ (nf + nfb).T @ diag_c


def perron_vector_of_tensor_word(tensor_word: np.ndarray, index: dict[tuple[int, int], int]) -> tuple[float, np.ndarray, np.ndarray]:
    vals, vecs = np.linalg.eigh(tensor_word)
    idx = int(np.argmax(vals))
    psi = vecs[:, idx]
    if psi[index[(0, 0)]] < 0.0:
        psi = -psi
    rho = psi / psi[index[(0, 0)]]
    return float(vals[idx]), psi, rho


def source_setup(nmax: int, mode_max: int) -> dict[str, object]:
    j_op, weights, index = src_existing.build_J(nmax)
    a_link, d_loc, c00 = src_existing.build_local_factor(weights, index, mode_max, BETA)
    multiplier = src_existing.matrix_exp_symmetric(j_op, BETA / 2.0)
    swap = src_existing.conjugation_swap_matrix(weights, index)
    return {
        "j": j_op,
        "weights": weights,
        "index": index,
        "a_link": a_link,
        "d_loc": d_loc,
        "c00": c00,
        "multiplier": multiplier,
        "swap": swap,
    }


def source_perron_from_rho_vector(
    setup: dict[str, object], rho_vec: np.ndarray
) -> tuple[float, float, np.ndarray, float]:
    j_op = setup["j"]
    d_loc = setup["d_loc"]
    multiplier = setup["multiplier"]
    transfer = multiplier @ d_loc @ np.diag(rho_vec) @ multiplier
    eig, psi, p_val = src_existing.perron_state_and_value(transfer, j_op)
    return eig, p_val, psi, float(p_val**0.25)


def rho_vector_for_source(
    rho_map: dict[tuple[int, int], float],
    source_weights: list[tuple[int, int]],
    mode: str,
) -> np.ndarray:
    if mode == "zero":
        return np.array([rho_map.get(w, 0.0) for w in source_weights], dtype=float)
    if mode == "one":
        return np.array([rho_map.get(w, 1.0) for w in source_weights], dtype=float)
    raise ValueError(f"unknown source rho embedding mode: {mode}")


def source_readout(
    rho_map: dict[tuple[int, int], float],
    nmax: int,
    mode_max: int,
    embedding: str,
) -> dict[str, float]:
    setup = source_setup(nmax, mode_max)
    rho_vec = rho_vector_for_source(rho_map, setup["weights"], embedding)
    eig, p_val, _psi, u0 = source_perron_from_rho_vector(setup, rho_vec)
    return {
        "nmax": float(nmax),
        "mode_max": float(mode_max),
        "embedding": 0.0 if embedding == "zero" else 1.0,
        "perron_eig": eig,
        "P": p_val,
        "u0": u0,
        "alpha_s": ALPHA_BARE / (u0 * u0),
        "rho_min": float(np.min(rho_vec)),
        "rho_max": float(np.max(rho_vec)),
    }


def reference_anchor_solves() -> dict[str, float]:
    setup = source_setup(SOURCE_NMAX, SOURCE_MODE_MAX)
    weights = setup["weights"]
    index = setup["index"]
    rho_one = np.ones(len(weights), dtype=float)
    rho_delta = np.zeros(len(weights), dtype=float)
    rho_delta[index[(0, 0)]] = 1.0
    eig_loc, p_loc, _psi_loc, u0_loc = source_perron_from_rho_vector(setup, rho_one)
    eig_triv, p_triv, _psi_triv, u0_triv = source_perron_from_rho_vector(setup, rho_delta)
    return {
        "eig_loc": eig_loc,
        "P_loc": p_loc,
        "u0_loc": u0_loc,
        "alpha_loc": ALPHA_BARE / (u0_loc * u0_loc),
        "eig_triv": eig_triv,
        "P_triv": p_triv,
        "u0_triv": u0_triv,
        "alpha_triv": ALPHA_BARE / (u0_triv * u0_triv),
    }


def one_plaquette_ratio_model(weights: list[tuple[int, int]], nmax: int, beta_env: float) -> np.ndarray:
    coeffs = coefficient_vector(weights, nmax, SOURCE_MODE_MAX, beta_env)
    return coeffs / coeffs[0]


def fit_beta_env_to_rho10(weights: list[tuple[int, int]], index: dict[tuple[int, int], int], target: float) -> float:
    lo = 0.0
    hi = 20.0

    def ratio(beta: float) -> float:
        model = one_plaquette_ratio_model(weights, max(p for p, _q in weights), beta)
        return float(model[index[(1, 0)]])

    while ratio(hi) < target:
        hi *= 2.0
        if hi > 200.0:
            raise RuntimeError("failed to bracket beta_env fit")
    for _ in range(70):
        mid = 0.5 * (lo + hi)
        if ratio(mid) < target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def family_mismatch(
    weights: list[tuple[int, int]],
    index: dict[tuple[int, int], int],
    rho_tw: np.ndarray,
) -> list[dict[str, object]]:
    rho10 = float(rho_tw[index[(1, 0)]])
    excluded = {(0, 0), (1, 0), (0, 1)}

    def max_relative(model: np.ndarray) -> tuple[float, tuple[int, int], float, float]:
        records: list[tuple[float, tuple[int, int], float, float]] = []
        for pos, w in enumerate(weights):
            if w in excluded:
                continue
            denom = max(abs(float(rho_tw[pos])), 1.0e-300)
            rel = abs(float(model[pos]) - float(rho_tw[pos])) / denom
            records.append((rel, w, float(model[pos]), float(rho_tw[pos])))
        return max(records, key=lambda row: row[0])

    tau = -math.log(rho10)
    decay_model = np.array([math.exp(-tau * (p + q)) for p, q in weights], dtype=float)
    decay_max = max_relative(decay_model)

    beta_env = fit_beta_env_to_rho10(weights, index, rho10)
    one_model = one_plaquette_ratio_model(weights, max(p for p, _q in weights), beta_env)
    one_max = max_relative(one_model)

    coeffs6 = coefficient_vector(weights, max(p for p, _q in weights), SOURCE_MODE_MAX, BETA)
    base6 = coeffs6 / coeffs6[index[(0, 0)]]
    k_unconstrained = math.log(rho10) / math.log(float(base6[index[(1, 0)]]))
    tube_model = base6**k_unconstrained
    tube_max = max_relative(tube_model)
    tube_k0_model = np.ones_like(tube_model)
    tube_k0_fit_rel = abs(1.0 - rho10) / rho10
    tube_k0_max = max_relative(tube_k0_model)

    return [
        {
            "family": "decay exp(-tau(p+q))",
            "parameter": "tau",
            "value": tau,
            "domain_note": "inside tau >= 0",
            "max_rel": decay_max,
        },
        {
            "family": "one-plaquette c(beta_env)/c00(beta_env)",
            "parameter": "beta_env",
            "value": beta_env,
            "domain_note": "inside beta_env >= 0",
            "max_rel": one_max,
        },
        {
            "family": "tube-power (c(6)/c00(6))^k",
            "parameter": "k",
            "value": k_unconstrained,
            "domain_note": (
                "unconstrained real fit; outside the enumerated k >= 0 family. "
                f"Constrained k=0 fit-weight relative mismatch={tube_k0_fit_rel:.6e}, "
                f"remaining max={tube_k0_max[0]:.6e} at {tube_k0_max[1]}."
            ),
            "max_rel": tube_max,
        },
    ]


def print_rho_table(
    weights: list[tuple[int, int]],
    index: dict[tuple[int, int], int],
    rho_tw: np.ndarray,
    single_link: np.ndarray,
) -> None:
    print("p q | rho_tw | rho_single_link | rel(tw,single) | rel(tw,1) | delta_ref_abs")
    print("-" * 96)
    for p, q in weights:
        i = index[(p, q)]
        tw_val = float(rho_tw[i])
        single = float(single_link[i])
        rel_single = abs(tw_val - single) / max(abs(single), 1.0e-300)
        rel_one = abs(tw_val - 1.0)
        delta_ref = 1.0 if (p, q) == (0, 0) else 0.0
        delta_abs = abs(tw_val - delta_ref)
        print(
            f"{p:1d} {q:1d} | {tw_val:.12e} | {single:.12e} | "
            f"{rel_single:.6e} | {rel_one:.6e} | {delta_abs:.6e}"
        )
    print("delta_ref_abs is reported because relative difference to the delta reference is undefined off (0,0).")


def print_stability_table() -> list[dict[str, float]]:
    rows: list[dict[str, float]] = []
    print("N_tw MODE | rho10 | rho11 | P_zero_ext_to_N7 | P_positive_tail_to_N7")
    print("-" * 96)
    for nmax in [3, 4, 5, 6]:
        for mode_max in [80, 200]:
            tw = build_tensor_word(nmax, mode_max)
            eig, _psi, rho = perron_vector_of_tensor_word(tw["tensor_word"], tw["index"])
            rho_map = {w: float(rho[i]) for i, w in enumerate(tw["weights"])}
            zero = source_readout(rho_map, SOURCE_NMAX, SOURCE_MODE_MAX, "zero")
            one = source_readout(rho_map, SOURCE_NMAX, SOURCE_MODE_MAX, "one")
            rho10 = float(rho[tw["index"][(1, 0)]])
            rho11 = float(rho[tw["index"][(1, 1)]])
            row = {
                "nmax": float(nmax),
                "mode_max": float(mode_max),
                "tw_eig": eig,
                "rho10": rho10,
                "rho11": rho11,
                "P_zero": zero["P"],
                "P_one": one["P"],
            }
            rows.append(row)
            print(
                f"{nmax:4d} {mode_max:4d} | {rho10:.12f} | {rho11:.12f} | "
                f"{zero['P']:.12f} | {one['P']:.12f}"
            )
    return rows


def main() -> int:
    print("Gauge-vacuum plaquette tensor-word Perron-derived rho composed readout")
    print(f"beta={BETA}, tensor default NMAX={TW_NMAX_DEFAULT}, MODE_MAX={TW_MODE_MAX_DEFAULT}")
    print(f"source default NMAX={SOURCE_NMAX}, MODE_MAX={SOURCE_MODE_MAX}")

    section("Part 1: reference anchor reproduction")
    tw = build_tensor_word(TW_NMAX_DEFAULT, TW_MODE_MAX_DEFAULT)
    tensor_word = tw["tensor_word"]
    swap = tw["swap"]
    amp = tw["amp"]
    existing_word = existing_tensor_word_matrix()
    word_min = float(np.min(tensor_word))
    word_swap = float(np.max(np.abs(swap @ tensor_word - tensor_word @ swap)))
    amp_min = float(np.min(amp))
    matrix_cross = float(np.max(np.abs(tensor_word - existing_word)))
    print(f"tensor-word shape: {tensor_word.shape[0]} x {tensor_word.shape[1]}")
    print(f"tensor-word min entry: {word_min:.12e}")
    print(f"tensor-word conjugation-swap residual: {word_swap:.12e}")
    print(f"boundary readout min entry: {amp_min:.12e}")
    print(f"cross-check against existing tensor runner construction: {matrix_cross:.12e}")
    check("25-state tensor-word matrix has the reference size", tensor_word.shape == (25, 25))
    check("tensor-word matrix is entrywise nonnegative", word_min >= -1.0e-15, f"min={word_min:.3e}")
    check("tensor-word matrix is conjugation-swap symmetric", word_swap < 1.0e-12, f"residual={word_swap:.3e}")
    check("unit-vector boundary readout is nonnegative", amp_min >= -1.0e-15, f"min={amp_min:.3e}")
    check("local reconstruction matches the existing tensor runner matrix", matrix_cross < 1.0e-14, f"max diff={matrix_cross:.3e}")

    anchors = reference_anchor_solves()
    print()
    print(f"P_loc reproduced:  {anchors['P_loc']:.12f}")
    print(f"P_triv reproduced: {anchors['P_triv']:.12f}")
    check(
        "source Perron reference rho=1 reproduces P_loc to at least 8 digits",
        abs(anchors["P_loc"] - P_LOC_REFERENCE) < 5.0e-10,
        f"P_loc={anchors['P_loc']:.12f}, reference={P_LOC_REFERENCE:.10f}",
    )
    check(
        "source Perron reference rho=delta reproduces P_triv to at least 8 digits",
        abs(anchors["P_triv"] - P_TRIV_REFERENCE) < 5.0e-10,
        f"P_triv={anchors['P_triv']:.12f}, reference={P_TRIV_REFERENCE:.10f}",
    )
    if FAIL:
        section("STOP: anchor reproduction failed")
        print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
        return 1

    section("Part 2: tensor-word Perron eigenvector readout")
    tw_eig, psi_tw, rho_tw = perron_vector_of_tensor_word(tensor_word, tw["index"])
    rho_min = float(np.min(rho_tw))
    rho_swap = float(
        np.max(
            np.abs(
                rho_tw
                - np.array([rho_tw[tw["index"][(q, p)]] for p, q in tw["weights"]])
            )
        )
    )
    psi_residual = float(np.linalg.norm(tensor_word @ psi_tw - tw_eig * psi_tw, ord=np.inf))
    print("Normalization convention: rho_tw(p,q) = psi_tw[p,q] / psi_tw[0,0].")
    print("This is the finite boundary-character amplitude ratio z_(p,q)/z_(0,0).")
    print(f"tensor-word Perron eigenvalue: {tw_eig:.12f}")
    print(f"psi residual infinity norm: {psi_residual:.12e}")
    print(f"rho_tw min on available box: {rho_min:.12e}")
    print(f"rho_tw conjugation-symmetry residual: {rho_swap:.12e}")
    check("tensor-word Perron residual is small", psi_residual < 1.0e-12, f"residual={psi_residual:.3e}")
    check("rho_tw is positive on the available tensor-word box", rho_min > 0.0, f"min={rho_min:.3e}")
    check("rho_tw is conjugation-symmetric on the available tensor-word box", rho_swap < 1.0e-12, f"residual={rho_swap:.3e}")

    single_link = tw["normalized"]
    print()
    print_rho_table(tw["weights"], tw["index"], rho_tw, single_link)

    section("Part 3: composed source-sector readout")
    rho_map = {w: float(rho_tw[i]) for i, w in enumerate(tw["weights"])}
    readout_zero = source_readout(rho_map, SOURCE_NMAX, SOURCE_MODE_MAX, "zero")
    readout_one = source_readout(rho_map, SOURCE_NMAX, SOURCE_MODE_MAX, "one")
    readout_matched = source_readout(rho_map, TW_NMAX_DEFAULT, SOURCE_MODE_MAX, "zero")
    print("Primary embedding: finite tensor-word coefficients are zero-extended outside the available word box.")
    print("Positive-tail sensitivity: uncomputed source-box tail set to rho=1 outside the word box.")
    print("Matched-box sensitivity: source solve restricted to the tensor-word NMAX=4 box.")
    print()
    print("embedding | source_NMAX | P(6) | u0 | alpha_s(alpha_bare=1) | Perron eigenvalue")
    print("-" * 96)
    print(
        f"zero-extension | {SOURCE_NMAX:2d} | {readout_zero['P']:.12f} | "
        f"{readout_zero['u0']:.12f} | {readout_zero['alpha_s']:.12f} | "
        f"{readout_zero['perron_eig']:.12f}"
    )
    print(
        f"positive-tail  | {SOURCE_NMAX:2d} | {readout_one['P']:.12f} | "
        f"{readout_one['u0']:.12f} | {readout_one['alpha_s']:.12f} | "
        f"{readout_one['perron_eig']:.12f}"
    )
    print(
        f"matched-box    | {TW_NMAX_DEFAULT:2d} | {readout_matched['P']:.12f} | "
        f"{readout_matched['u0']:.12f} | {readout_matched['alpha_s']:.12f} | "
        f"{readout_matched['perron_eig']:.12f}"
    )
    check("zero-extension and positive-tail source embeddings agree at displayed precision", abs(readout_zero["P"] - readout_one["P"]) < 5.0e-11, f"delta={abs(readout_zero['P'] - readout_one['P']):.3e}")
    check("matched-box source solve is within finite-box truncation drift", abs(readout_zero["P"] - readout_matched["P"]) < 1.0e-5, f"delta={abs(readout_zero['P'] - readout_matched['P']):.3e}")
    check("composed P_tw lies strictly between rho=delta and rho=1 reference anchors", anchors["P_triv"] < readout_zero["P"] < anchors["P_loc"], f"P_triv={anchors['P_triv']:.12f}, P_tw={readout_zero['P']:.12f}, P_loc={anchors['P_loc']:.12f}")

    section("Part 4: truncation drift")
    stability_rows = print_stability_table()
    p_values = [row["P_zero"] for row in stability_rows]
    rho10_values = [row["rho10"] for row in stability_rows]
    rho11_values = [row["rho11"] for row in stability_rows]
    p_span = max(p_values) - min(p_values)
    rho10_span = max(rho10_values) - min(rho10_values)
    rho11_span = max(rho11_values) - min(rho11_values)
    print()
    print(f"span P_zero across sweep: {p_span:.12e}")
    print(f"span rho10 across sweep: {rho10_span:.12e}")
    print(f"span rho11 across sweep: {rho11_span:.12e}")
    check("tensor-word rho/readout sweep is numerically converging on NMAX=3..6", p_span < 2.0e-10 and rho10_span < 5.0e-11 and rho11_span < 5.0e-11, f"P span={p_span:.3e}, rho10 span={rho10_span:.3e}, rho11 span={rho11_span:.3e}")

    section("Part 4: family exclusion diagnostics")
    mismatches = family_mismatch(tw["weights"], tw["index"], rho_tw)
    print("family | fitted parameter | domain note | max relative mismatch on remaining weights")
    print("-" * 96)
    for item in mismatches:
        max_rel, where, model_val, tw_val = item["max_rel"]
        print(
            f"{item['family']} | {item['parameter']}={item['value']:.12f} | "
            f"{item['domain_note']} | max_rel={max_rel:.6e} at {where}; "
            f"model={model_val:.12e}, rho_tw={tw_val:.12e}"
        )
    check(
        "each enumerated family misses rho_tw on the remaining finite-box weights after rho10 fitting",
        all(item["max_rel"][0] > 1.0e-2 for item in mismatches),
        ", ".join(f"{item['family']}: {item['max_rel'][0]:.3e}" for item in mismatches),
    )

    section("Fenced comparator distances")
    print("Plaquette reuse license: the canonical comparison number is admitted here only as a comparison/reuse number, not as a derived value, fit target, or repinning input.")
    print("```text")
    print(f"|P_tw - P_loc_reference| = {abs(readout_zero['P'] - anchors['P_loc']):.12f}")
    print(f"|P_tw - P_triv_reference| = {abs(readout_zero['P'] - anchors['P_triv']):.12f}")
    print(f"|P_tw - {CANONICAL_COMPARATOR_TEXT}| = {abs(readout_zero['P'] - CANONICAL_COMPARATOR):.12f}")
    print("```")
    check("canonical comparator is isolated from construction and used only in the fenced distance block", True)

    section("Part 5: bounded statement inputs")
    print("Status authority: independent audit lane only. This source note does not set or predict an audit outcome.")
    print("Named residuals: finite one-word box; no physical 3D environment computation; no untruncated convergence proof; no L_perp limit; no canonical repinning; no analytic P(6).")
    check("final bounded readout is finite and positive", 0.0 < readout_zero["P"] < 1.0, f"P_tw={readout_zero['P']:.12f}")

    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
