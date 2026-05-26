"""Finite tensor-product local-operator translation covariance.

This runner checks the repaired scope of
TRANSLATION_COVARIANCE_LOCAL_OP_THEOREM_NOTE_2026-05-02.md.  The
load-bearing dependency is the retained tensor-product translation /
fermion-operator bridge, not the older lattice-Noether row.

The tests construct a small periodic 3D block, its tensor-product Fock
space, and tensor-permutation translations.  They then verify that
single-site matrices, finite-support monomials, density sums, and hopping
monomials shift by site-label relabeling.
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


def add_coord(L: int, x: tuple[int, int, int], a: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple((x[i] + a[i]) % L for i in range(3))


def sub_coord(L: int, x: tuple[int, int, int], a: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple((x[i] - a[i]) % L for i in range(3))


def int_to_bits(value: int, n_bits: int) -> list[int]:
    return [(value >> (n_bits - 1 - i)) & 1 for i in range(n_bits)]


def bits_to_int(bits: list[int]) -> int:
    value = 0
    for bit in bits:
        value = (value << 1) | int(bit)
    return value


def kron_chain(matrices: list[np.ndarray]) -> np.ndarray:
    result = matrices[0]
    for matrix in matrices[1:]:
        result = np.kron(result, matrix)
    return result


def at_site(local_op: np.ndarray, site: int, n_sites: int) -> np.ndarray:
    identity = np.eye(2, dtype=complex)
    return kron_chain([local_op if i == site else identity for i in range(n_sites)])


def build_translation(L: int, shift: tuple[int, int, int]) -> np.ndarray:
    """Tensor-permutation translation from the retained bridge."""
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


def max_norm(values: list[float]) -> float:
    return max(values) if values else 0.0


def main() -> None:
    print("=" * 72)
    print("FINITE TENSOR-PRODUCT LOCAL-OPERATOR TRANSLATION COVARIANCE")
    print("=" * 72)
    print()

    print("-" * 72)
    print("TEST 0: load-bearing tensor-product bridge is retained-grade")
    print("-" * 72)
    ledger = json.loads(Path("docs/audit/data/audit_ledger.json").read_text())
    bridge_row = ledger["rows"][BRIDGE_CLAIM_ID]
    bridge_status = bridge_row.get("effective_status")
    t0_ok = bridge_status in RETAINED_GRADE
    print(f"  {BRIDGE_CLAIM_ID}")
    print(f"  bridge ledger effective-status field: {bridge_status}")
    print(f"  STATUS: {'PASS' if t0_ok else 'FAIL'}")
    print()

    L = 2
    sites = list(itertools.product(range(L), repeat=3))
    n_sites = len(sites)
    dim = 2**n_sites
    shift = (1, 0, 1)
    translation = build_translation(L, shift)
    translation_dag = translation.conj().T

    identity_2 = np.eye(2, dtype=complex)
    annihilate = np.array([[0, 1], [0, 0]], dtype=complex)
    create = annihilate.conj().T
    number = create @ annihilate
    pauli_x = annihilate + create
    generic = 2 * identity_2 - 3 * annihilate + 5 * create + 7 * number

    print(f"  finite block: {L}x{L}x{L}, sites = {n_sites}, dim(H) = {dim}")
    print(f"  shift a = {shift}")
    print()

    print("-" * 72)
    print("TEST 1: T_a is unitary on the tensor-product Fock basis")
    print("-" * 72)
    unit_dev = np.linalg.norm(translation @ translation_dag - np.eye(dim))
    inverse_dev = np.linalg.norm(translation_dag @ translation - np.eye(dim))
    t1_ok = unit_dev < 1e-12 and inverse_dev < 1e-12
    print(f"  ||T T^dag - I|| = {unit_dev:.3e}")
    print(f"  ||T^dag T - I|| = {inverse_dev:.3e}")
    print(f"  STATUS: {'PASS' if t1_ok else 'FAIL'}")
    print()

    print("-" * 72)
    print("TEST 2: single-site M_2(C) generators shift by x -> x+a")
    print("-" * 72)
    generator_devs: list[float] = []
    generators = [
        ("a", annihilate),
        ("a^dag", create),
        ("n", number),
        ("sigma_x", pauli_x),
        ("generic", generic),
    ]
    for name, local_matrix in generators:
        for coord in sites:
            site = site_index(L, coord)
            shifted_coord = add_coord(L, coord, shift)
            shifted_site = site_index(L, shifted_coord)
            actual = translation @ at_site(local_matrix, site, n_sites) @ translation_dag
            expected = at_site(local_matrix, shifted_site, n_sites)
            generator_devs.append(float(np.linalg.norm(actual - expected)))
    max_generator_dev = max_norm(generator_devs)
    t2_ok = max_generator_dev < 1e-12
    print(f"  checked {len(generators)} generators/matrices across {n_sites} sites")
    print(f"  max ||T M_x T^dag - M_(x+a)|| = {max_generator_dev:.3e}")
    print(f"  STATUS: {'PASS' if t2_ok else 'FAIL'}")
    print()

    print("-" * 72)
    print("TEST 3: finite-support two-site monomials shift both labels")
    print("-" * 72)
    monomial_cases = [
        ((0, 0, 0), (0, 1, 0)),
        ((1, 1, 0), (0, 1, 1)),
        ((1, 0, 1), (1, 1, 1)),
    ]
    monomial_devs: list[float] = []
    for x_coord, y_coord in monomial_cases:
        x = site_index(L, x_coord)
        y = site_index(L, y_coord)
        x_shift = site_index(L, add_coord(L, x_coord, shift))
        y_shift = site_index(L, add_coord(L, y_coord, shift))
        monomial = at_site(create, x, n_sites) @ at_site(annihilate, y, n_sites)
        expected = at_site(create, x_shift, n_sites) @ at_site(annihilate, y_shift, n_sites)
        actual = translation @ monomial @ translation_dag
        deviation = float(np.linalg.norm(actual - expected))
        monomial_devs.append(deviation)
        print(f"  x={x_coord}, y={y_coord}: deviation = {deviation:.3e}")
    max_monomial_dev = max_norm(monomial_devs)
    t3_ok = max_monomial_dev < 1e-12
    print(f"  STATUS: {'PASS' if t3_ok else 'FAIL'}")
    print()

    print("-" * 72)
    print("TEST 4: translation-invariant density sum commutes with T_a")
    print("-" * 72)
    q_total = sum(at_site(number, site, n_sites) for site in range(n_sites))
    q_shifted = translation @ q_total @ translation_dag
    q_dev = np.linalg.norm(q_shifted - q_total)
    comm_dev = np.linalg.norm(translation @ q_total - q_total @ translation)
    t4_ok = q_dev < 1e-12 and comm_dev < 1e-12
    print(f"  ||T Q_total T^dag - Q_total|| = {q_dev:.3e}")
    print(f"  ||[T, Q_total]|| = {comm_dev:.3e}")
    print(f"  STATUS: {'PASS' if t4_ok else 'FAIL'}")
    print()

    print("-" * 72)
    print("TEST 5: hopping-family sum over a translation orbit is invariant")
    print("-" * 72)
    hop_sum = np.zeros((dim, dim), dtype=complex)
    for coord in sites:
        neighbor = add_coord(L, coord, (1, 0, 0))
        x = site_index(L, coord)
        y = site_index(L, neighbor)
        hop_sum += at_site(create, x, n_sites) @ at_site(annihilate, y, n_sites)
    hop_dev = np.linalg.norm(translation @ hop_sum @ translation_dag - hop_sum)
    t5_ok = hop_dev < 1e-12
    print(f"  ||T H_orbit T^dag - H_orbit|| = {hop_dev:.3e}")
    print(f"  STATUS: {'PASS' if t5_ok else 'FAIL'}")
    print()

    print("=" * 72)
    print(f"  Test 0 (bridge retained-grade):                    {'PASS' if t0_ok else 'FAIL'}")
    print(f"  Test 1 (T_a unitary):                              {'PASS' if t1_ok else 'FAIL'}")
    print(f"  Test 2 (single-site covariance):                   {'PASS' if t2_ok else 'FAIL'}")
    print(f"  Test 3 (two-site monomial covariance):             {'PASS' if t3_ok else 'FAIL'}")
    print(f"  Test 4 (density sum invariant):                    {'PASS' if t4_ok else 'FAIL'}")
    print(f"  Test 5 (hopping orbit invariant):                  {'PASS' if t5_ok else 'FAIL'}")
    all_ok = all([t0_ok, t1_ok, t2_ok, t3_ok, t4_ok, t5_ok])
    print(f"  OVERALL: {'PASS' if all_ok else 'FAIL'}")
    if not all_ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
