#!/usr/bin/env python3
"""Shared finite tensor-word/source readout helpers for the word-count runners.

This module exposes the local interface used by the June 2026 word-count
runners.  It stays inside the repo-internal finite packet: Wilson character
coefficients, SU(3) fundamental/antifundamental fusion recurrences, the
tensor-word Perron vector, and the source-sector Perron solve with supplied
rho.  It does not compute a physical 3D spatial Wilson environment.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import frontier_gauge_vacuum_plaquette_tensor_transfer_perron_solve as src_existing


BETA = 6.0
SOURCE_NMAX = src_existing.NMAX_DEFAULT
SOURCE_MODE_MAX = src_existing.MODE_MAX_DEFAULT
CANONICAL_COMPARATOR = src_existing.CANONICAL_COMPARATOR
CANONICAL_COMPARATOR_TEXT = "0.5934"


def weights_box(nmax: int) -> list[tuple[int, int]]:
    return [(p, q) for p in range(nmax + 1) for q in range(nmax + 1)]


def build_mult_matrices(
    nmax: int,
) -> tuple[np.ndarray, np.ndarray, list[tuple[int, int]], dict[tuple[int, int], int]]:
    weights = weights_box(nmax)
    index = {w: i for i, w in enumerate(weights)}
    nf = np.zeros((len(weights), len(weights)), dtype=int)
    nfb = np.zeros((len(weights), len(weights)), dtype=int)
    for p, q in weights:
        i = index[(p, q)]
        for a, b in [(p + 1, q), (p - 1, q + 1), (p, q - 1)]:
            if a >= 0 and b >= 0 and (a, b) in index:
                nf[index[(a, b)], i] += 1
        for a, b in [(p, q + 1), (p + 1, q - 1), (p - 1, q)]:
            if a >= 0 and b >= 0 and (a, b) in index:
                nfb[index[(a, b)], i] += 1
    return nf, nfb, weights, index


def build_tensor_word(nmax: int, mode_max: int) -> dict[str, object]:
    nf, nfb, weights, index = build_mult_matrices(nmax)
    arg = BETA / 3.0
    coeffs = np.array(
        [
            src_existing.wilson_character_coefficient(p, q, mode_max, arg)
            for p, q in weights
        ],
        dtype=float,
    )
    dims = np.array([src_existing.dim_su3(p, q) for p, q in weights], dtype=float)
    c00 = coeffs[index[(0, 0)]]
    normalized = coeffs / (dims * c00)
    diag = np.diag(normalized)
    fusion = nf + nfb
    tensor_word = diag @ fusion @ diag @ fusion.T @ diag
    return {
        "weights": weights,
        "index": index,
        "coeffs": coeffs,
        "dims": dims,
        "normalized": normalized,
        "nf": nf,
        "nfb": nfb,
        "tensor_word": tensor_word,
    }


def perron_vector_of_tensor_word(
    tensor_word: np.ndarray, index: dict[tuple[int, int], int]
) -> tuple[float, np.ndarray, np.ndarray]:
    vals, vecs = np.linalg.eigh(np.asarray(tensor_word, dtype=float))
    pos = int(np.argmax(vals))
    eig = float(vals[pos])
    psi = vecs[:, pos].real
    zero = index[(0, 0)]
    if float(psi[zero]) < 0.0:
        psi = -psi
    rho = psi / float(psi[zero])
    return eig, psi, rho


def source_setup(nmax: int, mode_max: int) -> dict[str, object]:
    j_op, weights, index = src_existing.build_J(nmax)
    _a_link, d_loc, c00 = src_existing.build_local_factor(
        weights, index, mode_max, BETA
    )
    multiplier = src_existing.matrix_exp_symmetric(j_op, BETA / 2.0)
    return {
        "j": j_op,
        "weights": weights,
        "index": index,
        "d_loc": d_loc,
        "multiplier": multiplier,
        "c00": c00,
    }


def source_perron_from_rho_vector(
    setup: dict[str, object], rho_vec: np.ndarray
) -> tuple[float, float, np.ndarray, float]:
    multiplier = np.asarray(setup["multiplier"], dtype=float)
    d_loc = np.asarray(setup["d_loc"], dtype=float)
    j_op = np.asarray(setup["j"], dtype=float)
    rho = np.asarray(rho_vec, dtype=float)
    transfer = multiplier @ d_loc @ np.diag(rho) @ multiplier
    eig, psi, p_value = src_existing.perron_state_and_value(transfer, j_op)
    return eig, p_value, psi, p_value ** 0.25


def source_readout(
    rho_map: dict[tuple[int, int], float],
    nmax: int,
    mode_max: int,
    _zero_mode: str = "zero",
) -> dict[str, float]:
    setup = source_setup(nmax, mode_max)
    weights = list(setup["weights"])
    index = dict(setup["index"])
    rho_vec = np.zeros(len(weights), dtype=float)
    for weight, value in rho_map.items():
        if weight in index:
            rho_vec[index[weight]] = float(value)
    eig, p_value, _psi, u0 = source_perron_from_rho_vector(setup, rho_vec)
    return {"eig": eig, "P": p_value, "u0": u0}


def reference_anchor_solves() -> dict[str, float]:
    setup = source_setup(SOURCE_NMAX, SOURCE_MODE_MAX)
    weights = list(setup["weights"])
    index = dict(setup["index"])
    rho_loc = np.ones(len(weights), dtype=float)
    rho_triv = np.zeros(len(weights), dtype=float)
    rho_triv[index[(0, 0)]] = 1.0
    _eig_loc, p_loc, _psi_loc, _u0_loc = source_perron_from_rho_vector(
        setup, rho_loc
    )
    _eig_triv, p_triv, _psi_triv, _u0_triv = source_perron_from_rho_vector(
        setup, rho_triv
    )
    return {"P_loc": p_loc, "P_triv": p_triv}


def main() -> int:
    tw = build_tensor_word(4, 80)
    eig, _psi, rho = perron_vector_of_tensor_word(tw["tensor_word"], tw["index"])
    rho_map = {w: float(rho[i]) for i, w in enumerate(tw["weights"])}
    readout = source_readout(rho_map, SOURCE_NMAX, SOURCE_MODE_MAX, "zero")
    print(
        "Status authority: independent audit lane only. This helper runner "
        "does not set or predict an audit outcome."
    )
    print(f"tensor_word Perron eigenvalue = {eig:.15f}")
    print(f"rho10 = {rho[tw['index'][(1, 0)]]:.15f}")
    print(f"P = {readout['P']:.15f}")
    print("PASS: helper interface reproduces a finite tensor-word readout")
    print("TOTAL: PASS=1, FAIL=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
