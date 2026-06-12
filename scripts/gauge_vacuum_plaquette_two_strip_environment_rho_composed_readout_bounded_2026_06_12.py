#!/usr/bin/env python3
"""Two-strip support surface for the finite plaquette window runners.

This module restores the repo-local support API used by the W53/W54
window-displacement runners: the B4 packet, exact small SU(3) product
decomposition by finite character peeling, the dimension-stripped internal
strip factor, and the source-sector readout adapter.

No random inputs, runtime dates, external tables, or fitted constants are
used.
"""

from __future__ import annotations

import itertools
import sys
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

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


@dataclass(frozen=True)
class Packet:
    weights: tuple[tuple[int, int], ...]
    index: dict[tuple[int, int], int]
    conjugate_index: np.ndarray
    d_coeff: np.ndarray
    dim: np.ndarray
    word_bond: np.ndarray
    tensor_word: np.ndarray
    source_setup: dict[str, object]


def dim_su3(weight: tuple[int, int]) -> int:
    return one_word.src_existing.dim_su3(*weight)


def conjugate(weight: tuple[int, int]) -> tuple[int, int]:
    return (weight[1], weight[0])


def build_packet() -> Packet:
    tw = one_word.build_tensor_word(TW_NMAX, TW_MODE_MAX)
    weights = tuple(tw["weights"])
    index = dict(tw["index"])
    conjugate_index = np.array([index[conjugate(w)] for w in weights], dtype=int)
    return Packet(
        weights=weights,
        index=index,
        conjugate_index=conjugate_index,
        d_coeff=np.asarray(tw["normalized"], dtype=float),
        dim=np.array([dim_su3(w) for w in weights], dtype=float),
        word_bond=np.asarray(tw["nf"] + tw["nfb"], dtype=float),
        tensor_word=np.asarray(tw["tensor_word"], dtype=float),
        source_setup=one_word.source_setup(SOURCE_NMAX, SOURCE_MODE_MAX),
    )


def source_p(packet: Packet, rho25: np.ndarray) -> tuple[float, float, float]:
    source_weights = list(packet.source_setup["weights"])
    source_index = dict(packet.source_setup["index"])
    rho_vec = np.zeros(len(source_weights), dtype=float)
    for pos, weight in enumerate(packet.weights):
        if weight in source_index:
            rho_vec[source_index[weight]] = float(rho25[pos])
    _eig, p_value, _psi, u0 = one_word.source_perron_from_rho_vector(
        packet.source_setup, rho_vec
    )
    alpha_s = 1.0 / (u0 * u0)
    return float(p_value), float(u0), float(alpha_s)


@lru_cache(maxsize=None)
def character_partition(
    partition: tuple[int, int, int],
) -> tuple[tuple[tuple[int, int, int], int], ...]:
    """Return the GL(3) Schur character monomial table for a partition."""
    part = tuple(int(x) for x in partition)
    cells: list[tuple[int, int]] = []
    for row, length in enumerate(part):
        for col in range(length):
            cells.append((row, col))

    grid: dict[tuple[int, int], int] = {}
    counts: dict[tuple[int, int, int], int] = {}

    def rec(pos: int, c1: int, c2: int, c3: int) -> None:
        if pos == len(cells):
            key = (c1, c2, c3)
            counts[key] = counts.get(key, 0) + 1
            return

        row, col = cells[pos]
        low = 1
        if col > 0:
            low = max(low, grid[(row, col - 1)])
        if row > 0 and col < part[row - 1]:
            low = max(low, grid[(row - 1, col)] + 1)

        for value in range(low, 4):
            grid[(row, col)] = value
            if value == 1:
                rec(pos + 1, c1 + 1, c2, c3)
            elif value == 2:
                rec(pos + 1, c1, c2 + 1, c3)
            else:
                rec(pos + 1, c1, c2, c3 + 1)
            del grid[(row, col)]

    rec(0, 0, 0, 0)
    return tuple(sorted(counts.items()))


def char_dict(partition: tuple[int, int, int]) -> dict[tuple[int, int, int], int]:
    return dict(character_partition(partition))


@lru_cache(maxsize=None)
def su3_character(
    weight: tuple[int, int],
) -> tuple[tuple[tuple[int, int, int], int], ...]:
    p, q = weight
    return character_partition((p + q, q, 0))


def multiply_characters(
    left: dict[tuple[int, int, int], int],
    right: dict[tuple[int, int, int], int],
) -> dict[tuple[int, int, int], int]:
    out: dict[tuple[int, int, int], int] = {}
    for e_left, c_left in left.items():
        for e_right, c_right in right.items():
            exp = (
                e_left[0] + e_right[0],
                e_left[1] + e_right[1],
                e_left[2] + e_right[2],
            )
            out[exp] = out.get(exp, 0) + c_left * c_right
    return out


@lru_cache(maxsize=None)
def decompose_su3_product(
    left: tuple[int, int], right: tuple[int, int]
) -> tuple[tuple[tuple[int, int], int], ...]:
    """Exact SU(3) tensor-product decomposition by GL(3) character peeling."""
    remainder = multiply_characters(
        dict(su3_character(left)), dict(su3_character(right))
    )
    out: dict[tuple[int, int], int] = {}

    while remainder:
        remainder = {key: val for key, val in remainder.items() if val != 0}
        if not remainder:
            break
        highest = max(remainder.keys())
        coeff = remainder[highest]
        if coeff <= 0 or not (highest[0] >= highest[1] >= highest[2] >= 0):
            raise RuntimeError(
                f"character decomposition failed at {left} x {right}: "
                f"highest={highest}, coeff={coeff}"
            )
        su3_weight = (highest[0] - highest[1], highest[1] - highest[2])
        out[su3_weight] = out.get(su3_weight, 0) + coeff

        for exp, char_coeff in char_dict(highest).items():
            next_val = remainder.get(exp, 0) - coeff * char_coeff
            if next_val == 0:
                remainder.pop(exp, None)
            elif next_val < 0:
                raise RuntimeError(
                    f"negative character remainder at {left} x {right}: "
                    f"exp={exp}, value={next_val}"
                )
            else:
                remainder[exp] = next_val

    return tuple(sorted(out.items()))


def build_fusion_table(packet: Packet) -> np.ndarray:
    n = len(packet.weights)
    table = np.zeros((n, n, n), dtype=int)
    for i, left in enumerate(packet.weights):
        for j, right in enumerate(packet.weights):
            dec = dict(decompose_su3_product(left, right))
            for k, out in enumerate(packet.weights):
                table[i, j, k] = int(dec.get(out, 0))
    return table


def validate_fundamental_fusion(
    packet: Packet, fusion: np.ndarray
) -> tuple[int, int]:
    tw = one_word.build_tensor_word(TW_NMAX, TW_MODE_MAX)
    nf = np.asarray(tw["nf"], dtype=int)
    nfb = np.asarray(tw["nfb"], dtype=int)
    f = packet.index[FUND]
    fb = packet.index[ANTIFUND]
    fund_err = 0
    anti_err = 0
    for source_pos, _source in enumerate(packet.weights):
        for out_pos, _out in enumerate(packet.weights):
            if int(fusion[source_pos, f, out_pos]) != int(nf[out_pos, source_pos]):
                fund_err += 1
            if int(fusion[source_pos, fb, out_pos]) != int(nfb[out_pos, source_pos]):
                anti_err += 1
    return fund_err, anti_err


def pair_indices(packet: Packet) -> list[tuple[int, int]]:
    n = len(packet.weights)
    return list(itertools.product(range(n), repeat=2))


def internal_factor(
    packet: Packet,
    fusion: np.ndarray,
    coeff_kind: str,
    orientation: str,
) -> np.ndarray:
    """Full environment-link factor on pair states."""
    pairs = pair_indices(packet)
    out = np.ones(len(pairs), dtype=float)
    z = packet.index[ZERO]
    if coeff_kind == "full_character":
        channel_coeff = packet.dim * packet.d_coeff
    elif coeff_kind == "dimension_stripped":
        channel_coeff = packet.d_coeff.copy()
    else:
        raise ValueError(f"unknown coeff_kind: {coeff_kind}")

    for pos, (left, right) in enumerate(pairs):
        if orientation == "product":
            right_for_fusion = right
        elif orientation == "conjugate":
            right_for_fusion = int(packet.conjugate_index[right])
        else:
            raise ValueError(f"unknown orientation: {orientation}")
        total = 1.0
        for channel in range(len(packet.weights)):
            if channel == z:
                continue
            mult = int(fusion[left, right_for_fusion, channel])
            if mult:
                total += float(channel_coeff[channel]) * mult
        out[pos] = total
    return out


def strip_transfer(packet: Packet, internal: np.ndarray) -> np.ndarray:
    pairs = pair_indices(packet)
    m_pair = np.kron(packet.word_bond, packet.word_bond)
    d_pair = np.array(
        [packet.d_coeff[left] * packet.d_coeff[right] for left, right in pairs],
        dtype=float,
    )
    d_pair = d_pair * internal
    mid = m_pair * d_pair[None, :]
    core = mid @ m_pair.T
    return d_pair[:, None] * core * d_pair[None, :]


def perron_symmetric(matrix: np.ndarray) -> tuple[float, np.ndarray, float, float]:
    vals, vecs = np.linalg.eigh(matrix)
    pos = int(np.argmax(vals))
    vec = vecs[:, pos].real
    if float(vec[0]) < 0.0:
        vec = -vec
    eig = float(vals[pos])
    residual = float(np.linalg.norm(matrix @ vec - eig * vec, ord=np.inf))
    return eig, vec, residual, float(np.min(vec))
