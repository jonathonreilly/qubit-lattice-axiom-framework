#!/usr/bin/env python3
"""Compatibility layer for tensor-word Perron rho and source readout.

This module supplies the one-word helper surface consumed by the W30/W31
word-count runners.  It wraps the repo-local source-sector Perron machinery in
``frontier_gauge_vacuum_plaquette_tensor_transfer_perron_solve.py`` and builds
the finite tensor-word matrix from the already documented packet:

    T = diag(D) (N_f + N_fbar) diag(D) (N_f + N_fbar)^T diag(D),

where D_(p,q) = c_(p,q)(6) / (d_(p,q) c_(0,0)(6)).

No comparator value is used in construction; the canonical comparator is
exposed only for downstream fenced distance reporting.
"""

from __future__ import annotations

from functools import lru_cache

import numpy as np

import frontier_gauge_vacuum_plaquette_tensor_transfer_perron_solve as src_existing


AUDIT_TIMEOUT_SEC = 600

BETA = src_existing.BETA
SOURCE_NMAX = src_existing.NMAX_DEFAULT
SOURCE_MODE_MAX = src_existing.MODE_MAX_DEFAULT
CANONICAL_COMPARATOR = src_existing.CANONICAL_COMPARATOR
CANONICAL_COMPARATOR_TEXT = "0.5934"


def _fundamental_targets(p: int, q: int) -> tuple[tuple[int, int], ...]:
    out: list[tuple[int, int]] = []
    for a, b in [(p + 1, q), (p - 1, q + 1), (p, q - 1)]:
        if a >= 0 and b >= 0:
            out.append((a, b))
    return tuple(out)


def _antifundamental_targets(p: int, q: int) -> tuple[tuple[int, int], ...]:
    out: list[tuple[int, int]] = []
    for a, b in [(p, q + 1), (p + 1, q - 1), (p - 1, q)]:
        if a >= 0 and b >= 0:
            out.append((a, b))
    return tuple(out)


def _fusion_matrix(
    weights: list[tuple[int, int]],
    index: dict[tuple[int, int], int],
    *,
    antifundamental: bool,
) -> np.ndarray:
    mat = np.zeros((len(weights), len(weights)), dtype=float)
    target_fn = _antifundamental_targets if antifundamental else _fundamental_targets
    for p, q in weights:
        col = index[(p, q)]
        for target in target_fn(p, q):
            if target in index:
                mat[index[target], col] += 1.0
    return mat


@lru_cache(maxsize=None)
def _cached_build_tensor_word(nmax: int, mode_max: int) -> tuple[
    tuple[tuple[int, int], ...],
    tuple[tuple[tuple[int, int], int], ...],
    np.ndarray,
    np.ndarray,
    np.ndarray,
    np.ndarray,
]:
    weights = tuple(src_existing.weights_box(nmax))
    index = {w: i for i, w in enumerate(weights)}
    coeffs = np.array(
        [
            src_existing.wilson_character_coefficient(p, q, mode_max, BETA / 3.0)
            for p, q in weights
        ],
        dtype=float,
    )
    dims = np.array([src_existing.dim_su3(p, q) for p, q in weights], dtype=float)
    c00 = float(coeffs[index[(0, 0)]])
    normalized = coeffs / (dims * c00)
    nf = _fusion_matrix(list(weights), index, antifundamental=False)
    nfb = _fusion_matrix(list(weights), index, antifundamental=True)
    fusion = nf + nfb
    diag = np.diag(normalized)
    tensor_word = diag @ fusion @ diag @ fusion.T @ diag
    return (
        weights,
        tuple(index.items()),
        normalized,
        nf,
        nfb,
        tensor_word,
    )


def build_tensor_word(nmax: int, mode_max: int) -> dict[str, object]:
    weights, index_items, normalized, nf, nfb, tensor_word = _cached_build_tensor_word(
        int(nmax), int(mode_max)
    )
    index = dict(index_items)
    boundary0 = np.zeros(len(weights), dtype=float)
    boundary0[index[(0, 0)]] = 1.0
    return {
        "weights": list(weights),
        "index": index,
        "normalized": normalized.copy(),
        "nf": nf.copy(),
        "nfb": nfb.copy(),
        "tensor_word": tensor_word.copy(),
        "boundary0": boundary0,
        "amp": tensor_word @ boundary0,
    }


def perron_vector_of_tensor_word(
    tensor_word: np.ndarray,
    index: dict[tuple[int, int], int],
) -> tuple[float, np.ndarray, np.ndarray]:
    vals, vecs = np.linalg.eigh(np.asarray(tensor_word, dtype=float))
    pos = int(np.argmax(vals))
    eig = float(vals[pos])
    psi = np.asarray(vecs[:, pos], dtype=float)
    zero = index[(0, 0)]
    if float(psi[zero]) < 0.0:
        psi = -psi
    rho = psi / float(psi[zero])
    return eig, psi, rho


@lru_cache(maxsize=None)
def _cached_source_setup(nmax: int, mode_max: int) -> tuple[
    tuple[tuple[int, int], ...],
    tuple[tuple[tuple[int, int], int], ...],
    np.ndarray,
    np.ndarray,
    np.ndarray,
]:
    j_op, weights, index = src_existing.build_J(int(nmax))
    _a_link, d_loc, _c00 = src_existing.build_local_factor(
        weights, index, int(mode_max), BETA
    )
    multiplier = src_existing.matrix_exp_symmetric(j_op, BETA / 2.0)
    return tuple(weights), tuple(index.items()), multiplier, np.diag(d_loc), j_op


def source_setup(nmax: int, mode_max: int) -> dict[str, object]:
    weights, index_items, multiplier, d_loc, j_op = _cached_source_setup(
        int(nmax), int(mode_max)
    )
    return {
        "weights": list(weights),
        "index": dict(index_items),
        "multiplier": multiplier.copy(),
        "d_loc": d_loc.copy(),
        "j": j_op.copy(),
    }


def source_perron_from_rho_vector(
    setup: dict[str, object],
    rho_vec: np.ndarray,
) -> tuple[float, float, np.ndarray, float]:
    multiplier = np.asarray(setup["multiplier"], dtype=float)
    d_loc = np.asarray(setup["d_loc"], dtype=float)
    j_op = np.asarray(setup["j"], dtype=float)
    rho = np.asarray(rho_vec, dtype=float)
    if rho.shape != d_loc.shape:
        raise ValueError("rho vector shape does not match source setup")
    transfer = multiplier @ np.diag(d_loc * rho) @ multiplier
    eig, psi, p_value = src_existing.perron_state_and_value(transfer, j_op)
    return eig, p_value, psi, p_value**0.25


def source_readout(
    rho_map: dict[tuple[int, int], float],
    nmax: int,
    mode_max: int,
    missing: str = "zero",
) -> dict[str, object]:
    setup = source_setup(nmax, mode_max)
    weights = setup["weights"]
    index = setup["index"]
    rho_vec = np.zeros(len(weights), dtype=float)
    if missing == "one":
        rho_vec.fill(1.0)
    elif missing != "zero":
        raise ValueError(f"unknown missing convention: {missing}")
    for w, val in rho_map.items():
        if w in index:
            rho_vec[index[w]] = float(val)
    eig, p_value, psi, u0 = source_perron_from_rho_vector(setup, rho_vec)
    return {
        "P": p_value,
        "eig": eig,
        "psi": psi,
        "u0": u0,
        "rho": rho_vec,
    }


def reference_anchor_solves(
    nmax: int = SOURCE_NMAX,
    mode_max: int = SOURCE_MODE_MAX,
) -> dict[str, float]:
    setup = source_setup(nmax, mode_max)
    weights = setup["weights"]
    index = setup["index"]
    rho_loc = np.ones(len(weights), dtype=float)
    rho_triv = np.zeros(len(weights), dtype=float)
    rho_triv[index[(0, 0)]] = 1.0
    _eig_loc, p_loc, _psi_loc, _u0_loc = source_perron_from_rho_vector(
        setup, rho_loc
    )
    _eig_triv, p_triv, _psi_triv, _u0_triv = source_perron_from_rho_vector(
        setup, rho_triv
    )
    return {"P_loc": float(p_loc), "P_triv": float(p_triv)}

