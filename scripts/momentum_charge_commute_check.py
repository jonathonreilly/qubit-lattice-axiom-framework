"""Tensor-product translation generators commute with Q_total.

This runner checks the repaired scope of
MOMENTUM_CHARGE_COMMUTE_THEOREM_NOTE_2026-05-02.md.  It does not claim a
full physical framework momentum operator.  It verifies that the retained
finite tensor-product translations commute with total number and that
finite-block spectral generators of axial translations commute with total
number as functions of those unitaries.
"""
from __future__ import annotations

import itertools
import json
from pathlib import Path

import numpy as np


RETAINED_GRADE = {"retained", "retained_bounded", "retained_no_go"}
BRIDGE_CLAIM_ID = "tensor_product_translation_fermion_operator_bridge_narrow_theorem_note_2026-05-25"


def site_index(L: int, coord: tuple[int, int, int]) -> int:
    return coord[0] * L * L + coord[1] * L + coord[2]


def sub_coord(L: int, x: tuple[int, int, int], a: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple((x[i] - a[i]) % L for i in range(3))


def int_to_bits(value: int, n_bits: int) -> list[int]:
    return [(value >> (n_bits - 1 - i)) & 1 for i in range(n_bits)]


def bits_to_int(bits: list[int]) -> int:
    value = 0
    for bit in bits:
        value = (value << 1) | int(bit)
    return value


def build_translation(L: int, shift: tuple[int, int, int]) -> np.ndarray:
    sites = list(itertools.product(range(L), repeat=3))
    n_sites = len(sites)
    dim = 2**n_sites
    translation = np.zeros((dim, dim), dtype=complex)
    for col in range(dim):
        bits_in = int_to_bits(col, n_sites)
        bits_out = [0] * n_sites
        for out_coord in sites:
            in_coord = sub_coord(L, out_coord, shift)
            bits_out[site_index(L, out_coord)] = bits_in[site_index(L, in_coord)]
        row = bits_to_int(bits_out)
        translation[row, col] = 1.0
    return translation


def build_q_total(n_sites: int) -> np.ndarray:
    dim = 2**n_sites
    diag = [sum(int_to_bits(state, n_sites)) for state in range(dim)]
    return np.diag(diag).astype(complex)


def order_two_generator(unitary: np.ndarray) -> np.ndarray:
    """Exact spectral generator for an order-two translation.

    On the L=2 block each axial translation has spectrum {+1,-1}; the
    principal-branch Hermitian generator is pi on the -1 eigenspace and
    0 on the +1 eigenspace, i.e. K = pi/2 * (I - T).
    """
    identity = np.eye(unitary.shape[0], dtype=complex)
    generator = 0.5 * np.pi * (identity - unitary)
    return 0.5 * (generator + generator.conj().T)


def offdiag_norm(matrix: np.ndarray) -> float:
    return float(np.linalg.norm(matrix - np.diag(np.diag(matrix))))


def main() -> None:
    print("=" * 72)
    print("TENSOR-PRODUCT TRANSLATION GENERATORS COMMUTE WITH Q_TOTAL")
    print("=" * 72)
    print()

    print("-" * 72)
    print("TEST 0: load-bearing tensor-product bridge is retained-grade")
    print("-" * 72)
    ledger = json.loads(Path("docs/audit/data/audit_ledger.json").read_text())
    bridge_status = ledger["rows"][BRIDGE_CLAIM_ID].get("effective_status")
    t0_ok = bridge_status in RETAINED_GRADE
    print(f"  {BRIDGE_CLAIM_ID}")
    print(f"  effective_status = {bridge_status}")
    print(f"  STATUS: {'PASS' if t0_ok else 'FAIL'}")
    print()

    L = 2
    n_sites = L**3
    dim = 2**n_sites
    q_total = build_q_total(n_sites)
    shifts = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1)]
    print(f"  finite block: {L}x{L}x{L}, sites = {n_sites}, dim(H) = {dim}")
    print()

    print("-" * 72)
    print("TEST 1: Q_total is Hermitian and integer-valued")
    print("-" * 72)
    q_herm = np.linalg.norm(q_total - q_total.conj().T)
    q_diag = np.diag(q_total).real
    q_integer = max(abs(value - round(value)) for value in q_diag)
    t1_ok = q_herm < 1e-12 and q_integer < 1e-12
    print(f"  ||Q - Q^dag|| = {q_herm:.3e}")
    print(f"  max integer deviation on spectrum = {q_integer:.3e}")
    print(f"  STATUS: {'PASS' if t1_ok else 'FAIL'}")
    print()

    print("-" * 72)
    print("TEST 2: each retained translation commutes with Q_total")
    print("-" * 72)
    translation_comm_devs: list[float] = []
    for shift in shifts:
        translation = build_translation(L, shift)
        comm = translation @ q_total - q_total @ translation
        covariance = translation @ q_total @ translation.conj().T - q_total
        comm_norm = float(np.linalg.norm(comm))
        cov_norm = float(np.linalg.norm(covariance))
        translation_comm_devs.extend([comm_norm, cov_norm])
        print(f"  shift={shift}: ||[T,Q]||={comm_norm:.3e}, ||TQT^dag-Q||={cov_norm:.3e}")
    max_translation_comm = max(translation_comm_devs)
    t2_ok = max_translation_comm < 1e-12
    print(f"  STATUS: {'PASS' if t2_ok else 'FAIL'}")
    print()

    print("-" * 72)
    print("TEST 3: finite-block spectral generators K_mu commute with Q_total")
    print("-" * 72)
    generator_comm_devs: list[float] = []
    generator_herm_devs: list[float] = []
    generators = []
    for shift in shifts[:3]:
        translation = build_translation(L, shift)
        generator = order_two_generator(translation)
        generators.append(generator)
        generator_herm_devs.append(float(np.linalg.norm(generator - generator.conj().T)))
        generator_comm_devs.append(float(np.linalg.norm(generator @ q_total - q_total @ generator)))
        print(
            f"  shift={shift}: ||K-K^dag||={generator_herm_devs[-1]:.3e}, "
            f"||[K,Q]||={generator_comm_devs[-1]:.3e}"
        )
    t3_ok = max(generator_herm_devs) < 1e-9 and max(generator_comm_devs) < 1e-9
    print(f"  STATUS: {'PASS' if t3_ok else 'FAIL'}")
    print()

    print("-" * 72)
    print("TEST 4: axial spectral generators commute pairwise")
    print("-" * 72)
    generator_pair_devs: list[float] = []
    for i, j in itertools.combinations(range(len(generators)), 2):
        comm_norm = float(np.linalg.norm(generators[i] @ generators[j] - generators[j] @ generators[i]))
        generator_pair_devs.append(comm_norm)
        print(f"  pair=({i},{j}): ||[K_i,K_j]||={comm_norm:.3e}")
    t4_ok = max(generator_pair_devs) < 1e-9
    print(f"  STATUS: {'PASS' if t4_ok else 'FAIL'}")
    print()

    print("-" * 72)
    print("TEST 5: common finite-block eigenbasis for Q_total and K_mu")
    print("-" * 72)
    combined = 1000.0 * q_total
    weight = 100.0
    for generator in generators:
        combined = combined + weight * generator
        weight *= 0.1
    combined = 0.5 * (combined + combined.conj().T)
    _, eigenvectors = np.linalg.eigh(combined)
    q_off = offdiag_norm(eigenvectors.conj().T @ q_total @ eigenvectors)
    k_offs = [offdiag_norm(eigenvectors.conj().T @ generator @ eigenvectors) for generator in generators]
    max_k_off = max(k_offs)
    t5_ok = q_off < 1e-8 and max_k_off < 1e-7
    print(f"  offdiag(Q) in common basis = {q_off:.3e}")
    print(f"  max offdiag(K_mu) in common basis = {max_k_off:.3e}")
    print(f"  STATUS: {'PASS' if t5_ok else 'FAIL'}")
    print()

    print("=" * 72)
    print(f"  Test 0 (bridge retained-grade):                    {'PASS' if t0_ok else 'FAIL'}")
    print(f"  Test 1 (Q_total Hermitian/integer):                 {'PASS' if t1_ok else 'FAIL'}")
    print(f"  Test 2 ([T_a,Q_total] = 0):                         {'PASS' if t2_ok else 'FAIL'}")
    print(f"  Test 3 ([K_mu,Q_total] = 0):                        {'PASS' if t3_ok else 'FAIL'}")
    print(f"  Test 4 ([K_mu,K_nu] = 0):                           {'PASS' if t4_ok else 'FAIL'}")
    print(f"  Test 5 (common finite-block eigenbasis):            {'PASS' if t5_ok else 'FAIL'}")
    all_ok = all([t0_ok, t1_ok, t2_ok, t3_ok, t4_ok, t5_ok])
    print(f"  OVERALL: {'PASS' if all_ok else 'FAIL'}")
    if not all_ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
