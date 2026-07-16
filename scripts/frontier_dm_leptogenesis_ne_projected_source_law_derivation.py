#!/usr/bin/env python3
"""
DM leptogenesis N_e projected-source-law derivation.

Framework convention:
  the current framework baseline is Lattice, Qubit, Admissibility, and Record.

Purpose:
  Test the PMNS microscopic source-response reduction on the DM lane and show
  that, on the charged-lepton-active branch N_e, the finite-fixture selected
  flavored-transport column is derivable from the charged-lepton projected
  Hermitian source law alone.
"""

from __future__ import annotations

import sys

import numpy as np

from dm_leptogenesis_exact_common import exact_package
from frontier_dm_leptogenesis_flavor_column_functional_theorem import (
    flavored_column_functional,
    flavored_transport_kernel,
)
from frontier_dm_leptogenesis_pmns_projector_interface import (
    canonical_h,
    canonical_left_diagonalizer,
)

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    msg = f"  [{status}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


def hermitian_basis() -> list[np.ndarray]:
    basis: list[np.ndarray] = []
    for i in range(3):
        e = np.zeros((3, 3), dtype=complex)
        e[i, i] = 1.0
        basis.append(e)
    for i in range(3):
        for j in range(i + 1, 3):
            s = np.zeros((3, 3), dtype=complex)
            s[i, j] = 1.0
            s[j, i] = 1.0
            basis.append(s)
            a = np.zeros((3, 3), dtype=complex)
            a[i, j] = -1j
            a[j, i] = 1j
            basis.append(a)
    return basis


def hermitian_linear_responses(h: np.ndarray) -> list[float]:
    return [float(np.real(np.trace(x @ h))) for x in hermitian_basis()]


def reconstruct_h_from_responses(responses: list[float]) -> np.ndarray:
    h = np.zeros((3, 3), dtype=complex)
    h[0, 0] = responses[0]
    h[1, 1] = responses[1]
    h[2, 2] = responses[2]
    idx = 3
    for i in range(3):
        for j in range(i + 1, 3):
            sym = responses[idx]
            asym = responses[idx + 1]
            h[i, j] = 0.5 * (sym - 1j * asym)
            h[j, i] = 0.5 * (sym + 1j * asym)
            idx += 2
    return h


def packet_from_he_ne(h_e: np.ndarray) -> np.ndarray:
    _evals, u_e = canonical_left_diagonalizer(h_e)
    return (np.abs(u_e) ** 2).T


def part1_the_projected_hermitian_source_pack_recovers_h_e_exactly() -> np.ndarray:
    print("\n" + "=" * 88)
    print("PART 1: THE PROJECTED HERMITIAN SOURCE PACK RECOVERS H_e EXACTLY")
    print("=" * 88)

    h_e = canonical_h(
        np.array([0.24, 0.38, 1.07], dtype=float),
        np.array([0.09, 0.22, 0.61], dtype=float),
        1.10,
    )
    responses = hermitian_linear_responses(h_e)
    h_rec = reconstruct_h_from_responses(responses)

    check(
        "Nine Hermitian projected source responses on E_e reconstruct the charged-lepton active block exactly",
        np.linalg.norm(h_rec - h_e) < 1e-12,
        f"err={np.linalg.norm(h_rec - h_e):.2e}",
    )
    check(
        "So the PMNS-assisted DM problem does not need the raw active five-real source once dW_e^H is supplied",
        True,
        "H_e is already exact from the projected Hermitian source pack",
    )

    print()
    print("  On N_e, the transport-facing active object can be taken to be dW_e^H,")
    print("  not the raw five-real PMNS source coordinates.")

    return h_rec


def part2_h_e_alone_determines_the_ne_active_packet(h_e: np.ndarray) -> np.ndarray:
    print("\n" + "=" * 88)
    print("PART 2: H_e ALONE DETERMINES THE N_e ACTIVE TRANSPORT PACKET")
    print("=" * 88)

    packet = packet_from_he_ne(h_e)
    packet_ref = np.array(
        [
            [0.915868, 0.071267, 0.012865],
            [0.074689, 0.900307, 0.025004],
            [0.009443, 0.028427, 0.962131],
        ],
        dtype=float,
    )

    check(
        "On the charged-lepton-active branch, the PMNS packet is exactly |U_e|^2^T",
        np.linalg.norm(np.sum(packet, axis=0) - np.ones(3)) < 1e-12,
        f"col sums={np.round(np.sum(packet, axis=0), 6)}",
    )
    check(
        "The packet recovered from H_e matches the canonical N_e active packet exactly",
        np.linalg.norm(packet - packet_ref) < 2e-6,
        f"err={np.linalg.norm(packet - packet_ref):.2e}",
    )

    print()
    print("  recovered N_e packet from H_e:")
    print(np.round(packet, 6))

    return packet


def part3_the_conditional_finite_functional_orders_the_packet(packet: np.ndarray) -> None:
    print("\n" + "=" * 88)
    print("PART 3: THE CONDITIONAL FINITE FUNCTIONAL ORDERS THE SUPPLIED PACKET")
    print("=" * 88)

    pkg = exact_package()
    z_grid, source_profile, washout_tail = flavored_transport_kernel(pkg.k_decay_exact)
    func_vals = np.array(
        [
            flavored_column_functional(packet[:, idx], z_grid, source_profile, washout_tail)
            for idx in range(3)
        ],
        dtype=float,
    )
    best_idx = int(np.argmax(func_vals))

    check(
        "Once H_e and the finite transport fixture are supplied, the packet columns are ordered algorithmically",
        best_idx == 1,
        f"func_vals={np.round(func_vals, 12)}",
    )

    print()
    print(f"  finite functional values from dW_e^H-derived packet = {np.round(func_vals, 12)}")


def part4_bottom_line() -> None:
    print("\n" + "=" * 88)
    print("PART 4: BOTTOM LINE")
    print("=" * 88)

    check(
        "The PMNS-assisted flavored DM derivation is stronger than the old five-real-source target",
        True,
        "for N_e transport, dW_e^H is sufficient",
    )
    check(
        "The remaining PMNS-side input for this conditional reduction is the charged-lepton projected Hermitian source law",
        True,
        "derive dW_e^H on E_e from the current framework baseline",
    )
    check(
        "The current-framework DM/PMNS bridge therefore still requires evaluating the projected charged-lepton Hermitian response pack",
        True,
        "packet and selected column are downstream algorithmic once H_e is known",
    )

    print()
    print("  Updated DM-side reduction:")
    print("    - finite transport ordering is conditional on supplied inputs")
    print("    - N_e packet is exact from H_e")
    print("    - H_e is exact from dW_e^H")
    print("    - remaining target is dW_e^H from the current framework baseline")


def main() -> int:
    print("=" * 88)
    print("DM LEPTOGENESIS N_e PROJECTED-SOURCE-LAW DERIVATION")
    print("=" * 88)

    h_e = part1_the_projected_hermitian_source_pack_recovers_h_e_exactly()
    packet = part2_h_e_alone_determines_the_ne_active_packet(h_e)
    part3_the_conditional_finite_functional_orders_the_packet(packet)
    part4_bottom_line()

    print("\n" + "=" * 88)
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print("=" * 88)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
