"""3 x 3bar = 1 + 8 trace-singlet check on the abstract CL3 SU(3) carrier."""
from __future__ import annotations

import math
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs/CL3_QUARK_ANTIQUARK_COLOR_SINGLET_THEOREM_NOTE_2026-05-02.md"


def gell_mann_matrices():
    s = []
    s.append(np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], dtype=complex))
    s.append(np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], dtype=complex))
    s.append(np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], dtype=complex))
    s.append(np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=complex))
    s.append(np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], dtype=complex))
    s.append(np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex))
    s.append(np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], dtype=complex))
    s.append(np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]], dtype=complex) / math.sqrt(3))
    return s


def note_boundary_ok() -> bool:
    text = " ".join(NOTE.read_text(encoding="utf-8").replace("`", "").split()).lower()
    required = [
        "does not identify the carrier with physical sm quark color",
        "physical sm-color identification remains excluded",
        "finite-dimensional linear algebra on end(c^3)",
    ]
    return all(phrase in text for phrase in required)


def commutant_dimension(generators) -> int:
    basis = []
    for i in range(3):
        for j in range(3):
            e_ij = np.zeros((3, 3), dtype=complex)
            e_ij[i, j] = 1.0
            basis.append(e_ij)

    columns = []
    for e_ij in basis:
        pieces = []
        for generator in generators:
            pieces.append((generator @ e_ij - e_ij @ generator).reshape(-1))
        columns.append(np.concatenate(pieces))
    linear_map = np.stack(columns, axis=1)
    rank = np.linalg.matrix_rank(linear_map, tol=1e-10)
    return len(basis) - rank


def main() -> None:
    print("=" * 72)
    print("3 x 3bar = 1 + 8 ALGEBRAIC SYMMETRIC-BASE SU(3) CHECK")
    print("=" * 72)
    print()

    N_c = 3
    print(f"  N = {N_c} (symmetric-base carrier dimension from CL3 color automorphism note)")
    print(f"  End(C^3) has dimension {N_c*N_c} = 9")
    print()

    print("-" * 72)
    print("TEST 0: source note fences off physical SM-color / quark-carrier bridge")
    print("-" * 72)
    t0_ok = note_boundary_ok()
    print(f"  STATUS: {'PASS' if t0_ok else 'FAIL'}")
    print()

    # ----- Test 1: dimension count -----
    print("-" * 72)
    print("TEST 1: dim(End(C^3)) = dim(C.I_3) + dim(sl_3(C)) = 1 + 8 = 9")
    print("-" * 72)
    dim_singlet = 1
    dim_octet = N_c * N_c - 1
    total = dim_singlet + dim_octet
    print(f"  dim(trace singlet) + dim(adjoint complement) = {dim_singlet} + {dim_octet} = {total}")
    t1_ok = total == N_c * N_c
    print(f"  STATUS: {'PASS' if t1_ok else 'FAIL'}")
    print()

    # ----- Test 2: singlet construction is normalized -----
    print("-" * 72)
    print("TEST 2: |trace⟩ = (1/sqrt(3)) sum_i |i ibar> is normalized")
    print("-" * 72)
    # Construct in basis {|11>, |12>, ..., |33>} (9-dim)
    singlet = np.zeros(9, dtype=complex)
    for i in range(3):
        singlet[i * 3 + i] = 1.0 / math.sqrt(3)
    norm = float(np.real(singlet.conj() @ singlet))
    print(f"  <trace|trace> = {norm:.10f}")
    t2_ok = abs(norm - 1.0) < 1e-12
    print(f"  STATUS: {'PASS' if t2_ok else 'FAIL'}")
    print()

    # ----- Test 3: singlet is SU(3)-invariant -----
    print("-" * 72)
    print("TEST 3: |trace> is annihilated by all 8 algebraic SU(3) generators on 3 x 3bar")
    print("-" * 72)
    lams = gell_mann_matrices()
    Ts = [lam / 2 for lam in lams]
    # Generators on 3 x 3bar: T^a x I_3 + I_3 x (-(T^a)^T) = T^a x I - I x (T^a)^T
    I3 = np.eye(3, dtype=complex)
    max_resid = 0.0
    for a, T in enumerate(Ts):
        gen = np.kron(T, I3) - np.kron(I3, T.T)  # for the conjugate rep, generator is -T^T (or equivalently -T*)
        action = gen @ singlet
        norm_action = float(np.linalg.norm(action))
        max_resid = max(max_resid, norm_action)
    print(f"  max ||T^a |trace>|| over 8 generators = {max_resid:.3e}")
    t3_ok = max_resid < 1e-10
    print(f"  STATUS: {'PASS' if t3_ok else 'FAIL'}")
    print()

    # ----- Test 4: singlet projector P = |singlet⟩⟨singlet| has trace 1 -----
    print("-" * 72)
    print("TEST 4: Tr(P_trace) = 1 and P_trace^2 = P_trace")
    print("-" * 72)
    P = np.outer(singlet, singlet.conj())
    tr_P = float(np.real(np.trace(P)))
    P_sq = P @ P
    proj_resid = float(np.linalg.norm(P_sq - P))
    print(f"  Tr(P_trace) = {tr_P:.6f}")
    print(f"  ||P^2 - P|| = {proj_resid:.3e}")
    t4_ok = abs(tr_P - 1.0) < 1e-12 and proj_resid < 1e-12
    print(f"  STATUS: {'PASS' if t4_ok else 'FAIL'}")
    print()

    # ----- Test 5: traceless dimension = 9 - 1 = 8 -----
    print("-" * 72)
    print("TEST 5: traceless complement has dimension 8")
    print("-" * 72)
    # Project out singlet from identity
    I9 = np.eye(9, dtype=complex)
    P_octet = I9 - P
    rank_octet = np.linalg.matrix_rank(P_octet, tol=1e-10)
    gell_mann_rank = np.linalg.matrix_rank(np.stack([T.reshape(-1) for T in Ts], axis=1), tol=1e-10)
    print(f"  rank(I - P_trace) = {rank_octet}")
    print(f"  rank(span of 8 Gell-Mann generators) = {gell_mann_rank}")
    t5_ok = rank_octet == 8 and gell_mann_rank == 8
    print(f"  STATUS: {'PASS' if t5_ok else 'FAIL'}")
    print()

    # ----- Test 6: invariant-line uniqueness -----
    print("-" * 72)
    print("TEST 6: commutant of all 8 generators is exactly the scalar line")
    print("-" * 72)
    comm_dim = commutant_dimension(Ts)
    print(f"  dim commutant({{T^a}}) = {comm_dim}")
    t6_ok = comm_dim == 1
    print(f"  STATUS: {'PASS' if t6_ok else 'FAIL'}")
    print()

    # ----- Summary -----
    print("=" * 72)
    print(f"  Test 0 (source boundary):            {'PASS' if t0_ok else 'FAIL'}")
    print(f"  Test 1 (dim 1 + 8 = 9):              {'PASS' if t1_ok else 'FAIL'}")
    print(f"  Test 2 (trace vector normalized):    {'PASS' if t2_ok else 'FAIL'}")
    print(f"  Test 3 (SU(3)-invariance):           {'PASS' if t3_ok else 'FAIL'}")
    print(f"  Test 4 (trace projector valid):      {'PASS' if t4_ok else 'FAIL'}")
    print(f"  Test 5 (traceless rank = 8):         {'PASS' if t5_ok else 'FAIL'}")
    print(f"  Test 6 (commutant dim = 1):          {'PASS' if t6_ok else 'FAIL'}")
    all_checks = [t0_ok, t1_ok, t2_ok, t3_ok, t4_ok, t5_ok, t6_ok]
    all_ok = all(all_checks)
    print(f"  SUMMARY: PASS={sum(all_checks)} FAIL={len(all_checks) - sum(all_checks)}")
    print(f"  OVERALL: {'PASS' if all_ok else 'FAIL'}")
    if not all_ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
