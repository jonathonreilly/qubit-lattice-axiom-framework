#!/usr/bin/env python3
"""Finite checks for the supplied-rho conditional interface theorem.

The runner stays inside repo-internal finite packets:

* tensor word box NMAX=4 and MODE_MAX=80;
* source readout NMAX=7 and MODE_MAX=200;
* existing source Perron machinery with rho supplied as input.

It checks readouts after rho has explicitly been supplied as a diagonal input.
The off-diagonal perturbation is a hostile control: a diag-only helper erases
that direction, so unchanged projected output is evidence of information loss,
not a proof that a physical Wilson residual is character-diagonal.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import gauge_vacuum_plaquette_tensor_word_perron_derived_rho_composed_readout_2026_06_11 as one_word
from frontier_gauge_vacuum_plaquette_source_sector_matrix_element_factorization import (
    exact_small_case as source_factorization_exact_small_case,
)


AUDIT_TIMEOUT_SEC = 600

ZERO = (0, 0)
FUND = (1, 0)
ADJOINT = (1, 1)
TW_NMAX = 4
TW_MODE_MAX = 80
SOURCE_NMAX = one_word.SOURCE_NMAX
SOURCE_MODE_MAX = one_word.SOURCE_MODE_MAX
P_PACKET_REFERENCE = 0.434215413259920
P_TRIV_REFERENCE = 0.422531739647131

NOTE_PATH = (
    REPO_ROOT
    / "docs"
    / "GAUGE_VACUUM_PLAQUETTE_COMPRESSION_SCOPE_RHO_COMPLETE_INTERFACE_NARROW_THEOREM_NOTE_2026-06-12.md"
)

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


def source_p(setup: dict[str, object], rho_vec: np.ndarray) -> float:
    _eig, p_value, _psi, _u0 = one_word.source_perron_from_rho_vector(
        setup, rho_vec
    )
    return float(p_value)


def embed_tensor_rho_in_source(
    tensor_weights: list[tuple[int, int]],
    rho_tensor: np.ndarray,
    setup: dict[str, object],
) -> np.ndarray:
    source_weights = list(setup["weights"])
    source_index = dict(setup["index"])
    rho_source = np.zeros(len(source_weights), dtype=float)
    for i, weight in enumerate(tensor_weights):
        if weight in source_index:
            rho_source[source_index[weight]] = float(rho_tensor[i])
    return rho_source


def diagonal_interface(environment_operator: np.ndarray) -> np.ndarray:
    return np.diag(environment_operator).copy()


def off_diagonal_perturbation(
    size: int,
    pairs: list[tuple[int, int, float]],
) -> np.ndarray:
    perturb = np.zeros((size, size), dtype=float)
    for i, j, value in pairs:
        if i == j:
            raise ValueError("off-diagonal perturbation pair used a diagonal slot")
        perturb[i, j] = value
        perturb[j, i] = value
    return perturb


def main() -> int:
    print("Gauge-vacuum plaquette compression-scope rho-complete interface runner")
    print(
        "Status authority: independent audit lane only. This source runner "
        "does not set or predict an audit outcome."
    )
    print("No new imports: repo-internal finite packet quantities only.")
    print(
        f"tensor NMAX={TW_NMAX}, tensor MODE_MAX={TW_MODE_MAX}, "
        f"source NMAX={SOURCE_NMAX}, source MODE_MAX={SOURCE_MODE_MAX}"
    )

    section("Part 1: build finite source and packet interfaces")
    setup = one_word.source_setup(SOURCE_NMAX, SOURCE_MODE_MAX)
    source_weights = list(setup["weights"])
    source_index = dict(setup["index"])
    tw = one_word.build_tensor_word(TW_NMAX, TW_MODE_MAX)
    tensor_weights = list(tw["weights"])
    tensor_index = dict(tw["index"])
    tensor_word = np.asarray(tw["tensor_word"], dtype=float)
    tw_eig, psi_tw, rho_packet = one_word.perron_vector_of_tensor_word(
        tensor_word, tensor_index
    )
    psi_residual = float(np.linalg.norm(tensor_word @ psi_tw - tw_eig * psi_tw, ord=np.inf))
    rho_packet_source = embed_tensor_rho_in_source(
        tensor_weights, rho_packet, setup
    )
    print(f"tensor packet size = {len(tensor_weights)}")
    print(f"source packet size = {len(source_weights)}")
    print(f"tensor Perron residual = {psi_residual:.12e}")
    check("finite tensor packet has 25 character weights", len(tensor_weights) == 25)
    check("finite source packet has 64 character weights", len(source_weights) == 64)
    check("tensor Perron residual is small", psi_residual < 1.0e-12, f"residual={psi_residual:.3e}")
    check("packet rho is normalized at the trivial coefficient", rho_packet[tensor_index[ZERO]] == 1.0)

    section("Part 2: finite rail trivial-channel collapse")
    rho_delta = np.zeros(len(source_weights), dtype=float)
    rho_delta[source_index[ZERO]] = 1.0
    p_triv = source_p(setup, rho_delta)
    anchors = one_word.reference_anchor_solves()
    print("one-line consequence: rho = delta_(0,0) => P = P_triv")
    print(f"P_triv direct delta = {p_triv:.15f}")
    print(f"P_triv existing Perron reference = {anchors['P_triv']:.15f}")
    check(
        "delta rho readout equals the existing Perron-solve P_triv value",
        p_triv == float(anchors["P_triv"]),
        f"direct={p_triv:.17g}, anchor={float(anchors['P_triv']):.17g}",
    )
    check(
        "delta rho readout agrees with the printed P_triv anchor",
        abs(p_triv - P_TRIV_REFERENCE) < 5.0e-13,
        f"delta={abs(p_triv - P_TRIV_REFERENCE):.3e}",
    )

    section("Part 3: one-word rho_packet to source readout")
    p_packet = source_p(setup, rho_packet_source)
    rho10 = float(rho_packet[tensor_index[FUND]])
    rho11 = float(rho_packet[tensor_index[ADJOINT]])
    print(f"rho_packet(1,0) = {rho10:.15f}")
    print(f"rho_packet(1,1) = {rho11:.15f}")
    print(f"P_packet = {p_packet:.15f}")
    check(
        "one-word rho_packet to P chain reproduces the composed-readout value",
        abs(p_packet - P_PACKET_REFERENCE) < 5.0e-13,
        f"delta={abs(p_packet - P_PACKET_REFERENCE):.3e}",
    )
    check(
        "packet readout lies between the trivial and local rho=1 anchors",
        anchors["P_triv"] < p_packet < anchors["P_loc"],
        f"P_triv={anchors['P_triv']:.15f}, P_packet={p_packet:.15f}, P_loc={anchors['P_loc']:.15f}",
    )

    section("Part 4: hostile control for a lossy diag-only interface")
    env_central = np.diag(rho_packet)
    f_idx = tensor_index[FUND]
    adj_idx = tensor_index[ADJOINT]
    w02_idx = tensor_index[(0, 2)]
    w20_idx = tensor_index[(2, 0)]
    perturb = off_diagonal_perturbation(
        len(tensor_weights),
        [
            (f_idx, adj_idx, 0.125),
            (w02_idx, w20_idx, -0.0625),
        ],
    )
    env_perturbed = env_central + perturb
    rho_from_central = diagonal_interface(env_central)
    rho_from_perturbed = diagonal_interface(env_perturbed)
    rho_perturbed_source = embed_tensor_rho_in_source(
        tensor_weights, rho_from_perturbed, setup
    )
    p_perturbed = source_p(setup, rho_perturbed_source)
    print("explicit perturbation entries:")
    print(f"  E[(1,0),(1,1)] = {perturb[f_idx, adj_idx]:.6f}")
    print(f"  E[(0,2),(2,0)] = {perturb[w02_idx, w20_idx]:.6f}")
    print(f"max off-diagonal perturbation magnitude = {float(np.max(np.abs(perturb))):.6f}")
    print(f"P after central interface projection = {p_perturbed:.15f}")
    check(
        "perturbation is a nonzero off-diagonal environment direction",
        float(np.max(np.abs(perturb))) > 0.0
        and np.count_nonzero(np.diag(perturb)) == 0,
    )
    check(
        "diag-only extraction leaves every tensor rho coefficient fixed",
        np.array_equal(rho_from_central, rho_from_perturbed),
    )
    check(
        "the raw environment operators are nevertheless different",
        not np.array_equal(env_central, env_perturbed),
    )
    check(
        "the embedded rho vector is unchanged only after the lossy diagonal projection",
        np.array_equal(rho_packet_source, rho_perturbed_source),
    )
    check(
        "unchanged projected readout demonstrates helper information loss rather than raw-operator completeness",
        p_packet == p_perturbed and not np.array_equal(env_central, env_perturbed),
        f"base={p_packet:.17g}, perturbed={p_perturbed:.17g}",
    )

    section("Part 5: durable interface semantics")
    source_exact = source_factorization_exact_small_case()
    check("paired theorem note exists as a durable repository file", NOTE_PATH.is_file())
    check(
        "copying an equal supplied rho vector leaves the operator readout unchanged",
        source_p(setup, rho_packet_source.copy()) == p_packet,
    )
    check(
        "diagonal extraction is idempotent on an already diagonal supplied operator",
        np.array_equal(diagonal_interface(env_central), rho_packet),
    )
    check(
        "the hostile raw operator cannot be reconstructed from its diagonal interface",
        not np.array_equal(np.diag(diagonal_interface(env_perturbed)), env_perturbed),
    )
    check(
        "the primary exact supplied-diagonal theorem verifies its contraction, Gram, and rank/kernel outputs",
        bool(source_exact["formula_exact"])
        and bool(source_exact["gram_exact"])
        and bool(source_exact["rank_kernel_exact"]),
    )

    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
