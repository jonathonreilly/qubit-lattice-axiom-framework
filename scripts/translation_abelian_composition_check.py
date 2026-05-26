"""Finite tensor-product translation group composition checks.

This runner checks the repaired scope of
TRANSLATION_ABELIAN_COMPOSITION_THEOREM_NOTE_2026-05-02.md.  It uses the
retained tensor-product translation / fermion-operator bridge as the
load-bearing dependency and constructs the same finite tensor-permutation
translations on a small periodic block.
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


def main() -> None:
    print("=" * 72)
    print("FINITE TENSOR-PRODUCT TRANSLATION GROUP COMPOSITION")
    print("=" * 72)
    print()

    print("-" * 72)
    print("TEST 0: load-bearing tensor-product bridge is retained-grade")
    print("-" * 72)
    ledger = json.loads(Path("docs/audit/data/audit_ledger.json").read_text())
    bridge_status = ledger["rows"][BRIDGE_CLAIM_ID].get("effective_status")
    t0_ok = bridge_status in RETAINED_GRADE
    print(f"  {BRIDGE_CLAIM_ID}")
    print(f"  bridge ledger effective-status field: {bridge_status}")
    print(f"  STATUS: {'PASS' if t0_ok else 'FAIL'}")
    print()

    L = 2
    n_sites = L**3
    dim = 2**n_sites
    identity = np.eye(dim, dtype=complex)
    zero = (0, 0, 0)
    e1 = (1, 0, 0)
    e2 = (0, 1, 0)
    e3 = (0, 0, 1)
    print(f"  finite block: {L}x{L}x{L}, sites = {n_sites}, dim(H) = {dim}")
    print()

    print("-" * 72)
    print("TEST 1: identity and unitarity")
    print("-" * 72)
    t_zero = build_translation(L, zero)
    identity_dev = np.linalg.norm(t_zero - identity)
    unitarity_devs: list[float] = []
    for shift in [e1, e2, e3, (1, 1, 0), (1, 1, 1)]:
        t_shift = build_translation(L, shift)
        unitarity_devs.append(float(np.linalg.norm(t_shift @ t_shift.conj().T - identity)))
        unitarity_devs.append(float(np.linalg.norm(t_shift.conj().T @ t_shift - identity)))
    max_unitarity_dev = max(unitarity_devs)
    t1_ok = identity_dev < 1e-12 and max_unitarity_dev < 1e-12
    print(f"  ||T_0 - I|| = {identity_dev:.3e}")
    print(f"  max unitarity deviation = {max_unitarity_dev:.3e}")
    print(f"  STATUS: {'PASS' if t1_ok else 'FAIL'}")
    print()

    print("-" * 72)
    print("TEST 2: closure T_a T_b = T_(a+b)")
    print("-" * 72)
    closure_devs: list[float] = []
    shifts = list(itertools.product(range(L), repeat=3))
    for a, b in itertools.product(shifts, repeat=2):
        t_a = build_translation(L, a)
        t_b = build_translation(L, b)
        t_sum = build_translation(L, add_coord(L, a, b))
        closure_devs.append(float(np.linalg.norm(t_a @ t_b - t_sum)))
    max_closure_dev = max(closure_devs)
    t2_ok = max_closure_dev < 1e-12
    print(f"  checked {len(closure_devs)} ordered pairs")
    print(f"  max ||T_a T_b - T_(a+b)|| = {max_closure_dev:.3e}")
    print(f"  STATUS: {'PASS' if t2_ok else 'FAIL'}")
    print()

    print("-" * 72)
    print("TEST 3: commutativity [T_a,T_b] = 0")
    print("-" * 72)
    comm_devs: list[float] = []
    for a, b in itertools.product(shifts, repeat=2):
        t_a = build_translation(L, a)
        t_b = build_translation(L, b)
        comm_devs.append(float(np.linalg.norm(t_a @ t_b - t_b @ t_a)))
    max_comm_dev = max(comm_devs)
    t3_ok = max_comm_dev < 1e-12
    print(f"  max ||[T_a,T_b]|| = {max_comm_dev:.3e}")
    print(f"  STATUS: {'PASS' if t3_ok else 'FAIL'}")
    print()

    print("-" * 72)
    print("TEST 4: inverse T_-a = T_a^dag")
    print("-" * 72)
    inverse_devs: list[float] = []
    for a in shifts:
        t_a = build_translation(L, a)
        t_minus = build_translation(L, tuple((-a[i]) % L for i in range(3)))
        inverse_devs.append(float(np.linalg.norm(t_minus - t_a.conj().T)))
        inverse_devs.append(float(np.linalg.norm(t_a @ t_minus - identity)))
    max_inverse_dev = max(inverse_devs)
    t4_ok = max_inverse_dev < 1e-12
    print(f"  max inverse deviation = {max_inverse_dev:.3e}")
    print(f"  STATUS: {'PASS' if t4_ok else 'FAIL'}")
    print()

    print("-" * 72)
    print("TEST 5: finite quotient faithfulness")
    print("-" * 72)
    kernel = []
    distinct = set()
    for a in shifts:
        t_a = build_translation(L, a)
        if np.linalg.norm(t_a - identity) < 1e-12:
            kernel.append(a)
        distinct.add(tuple(np.round(t_a.real.flatten(), 6).tolist()))
    t5_ok = kernel == [zero] and len(distinct) == L**3
    print(f"  kernel = {kernel}")
    print(f"  distinct translations = {len(distinct)}")
    print(f"  expected distinct translations = {L ** 3}")
    print(f"  STATUS: {'PASS' if t5_ok else 'FAIL'}")
    print()

    print("=" * 72)
    print(f"  Test 0 (bridge retained-grade):                    {'PASS' if t0_ok else 'FAIL'}")
    print(f"  Test 1 (identity/unitarity):                       {'PASS' if t1_ok else 'FAIL'}")
    print(f"  Test 2 (closure):                                  {'PASS' if t2_ok else 'FAIL'}")
    print(f"  Test 3 (commutativity):                            {'PASS' if t3_ok else 'FAIL'}")
    print(f"  Test 4 (inverse):                                  {'PASS' if t4_ok else 'FAIL'}")
    print(f"  Test 5 (finite quotient faithfulness):             {'PASS' if t5_ok else 'FAIL'}")
    all_ok = all([t0_ok, t1_ok, t2_ok, t3_ok, t4_ok, t5_ok])
    print(f"  OVERALL: {'PASS' if all_ok else 'FAIL'}")
    if not all_ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
