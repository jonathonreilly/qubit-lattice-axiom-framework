"""A1 qubit occupation-count operator has integer spectrum.

The repaired theorem is not a physical electric-charge derivation.  It
works directly in the A1 local algebra M_2(C): choose any rank-one local
readout projection n.  In a representative Pauli basis, n = diag(0, 1).
On an N-site finite tensor block, Q_total = sum_x n_x has spectrum
{0, 1, ..., N}, multiplicity C(N, k).

Tests:
  (T0) source note uses A1/M_2(C) and no old per-site uniqueness dependency
  (T1) representative ladder has canonical single-qubit anticommutation
  (T2) n = a^† a has eigenvalues exactly {0, 1}
  (T3) Multi-site n_x are pairwise commuting (tensor product structure)
  (T4) Q_total = Σ_x n_x has integer spectrum {0, 1, ..., N}
  (T5) Multiplicity at occupation count k is C(N, k)
  (T6) Q_total = N*I/2 - Σ_x σ_3,x/2 for the representative readout basis
"""
from __future__ import annotations

import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "Q_INTEGER_SPECTRUM_THEOREM_NOTE_2026-05-02.md"
OLD_DEP = "AXIOM_FIRST_" + "CL3_PER_SITE_UNIQUENESS"


def kron_chain(matrices: list[np.ndarray]) -> np.ndarray:
    """Compute the Kronecker product of a list of matrices."""
    result = matrices[0]
    for M in matrices[1:]:
        result = np.kron(result, M)
    return result


def n_at_site(N: int, x: int) -> np.ndarray:
    """n_x = I ⊗ ... ⊗ n ⊗ ... ⊗ I  with n at position x (0-indexed)."""
    # Representative rank-one qubit readout projection in the basis
    # |0>=(1,0)^T, |1>=(0,1)^T.
    a_op = np.array([[0, 1], [0, 0]], dtype=complex)
    a_dag = a_op.conj().T
    n_local = a_dag @ a_op  # = diag(0, 1)
    I2 = np.eye(2, dtype=complex)
    factors = [n_local if i == x else I2 for i in range(N)]
    return kron_chain(factors)


def note_firewall() -> bool:
    text = NOTE.read_text()
    lowered = text.lower()
    checks = {
        "cites minimal axioms A1": "minimal_axioms_2026-05-20" in lowered
        or "MINIMAL_AXIOMS_2026-05-20.md" in text,
        "uses rank-one qubit projection": "rank-one" in lowered and "projection" in lowered,
        "rules out physical charge identification": "does not identify" in lowered
        and "physical electric charge" in lowered,
        "no old uniqueness node in YAML": OLD_DEP not in text,
        "classified as positive theorem": "claim_type_author_hint: positive_theorem" in text,
    }
    for label, ok in checks.items():
        print(f"  {label}: {'PASS' if ok else 'FAIL'}")
    return all(checks.values())


def main() -> None:
    print("=" * 72)
    print("A1 QUBIT OCCUPATION-COUNT INTEGER SPECTRUM")
    print("=" * 72)
    print()

    print("-" * 72)
    print("SOURCE FIREWALL: A1-local occupation count, not physical charge")
    print("-" * 72)
    t0_ok = note_firewall()
    print(f"  STATUS: {'PASS' if t0_ok else 'FAIL'}")
    print()

    # First verify single-site structure
    a_op = np.array([[0, 1], [0, 0]], dtype=complex)
    a_dag = a_op.conj().T
    n_local = a_dag @ a_op
    I2 = np.eye(2, dtype=complex)

    # ----- Test 1: Single-mode CCR-fermion: {a, a^†} = I -----
    print("-" * 72)
    print("TEST 1: {a, a^†} = I for a representative single-qubit ladder")
    print("-" * 72)
    anti = a_op @ a_dag + a_dag @ a_op
    dev1 = np.linalg.norm(anti - I2)
    print(f"  ||{{a, a^†}} - I|| = {dev1:.3e}")
    # Also check {a, a} = 0 and {a^†, a^†} = 0
    aa = a_op @ a_op + a_op @ a_op
    aada = a_dag @ a_dag + a_dag @ a_dag
    dev1b = np.linalg.norm(aa) + np.linalg.norm(aada)
    print(f"  ||{{a, a}} + {{a^†, a^†}}|| = {dev1b:.3e}  (Grassmann nilpotency)")
    t1_ok = dev1 < 1e-12 and dev1b < 1e-12
    print(f"  STATUS: {'PASS' if t1_ok else 'FAIL'}")
    print()

    # ----- Test 2: n = a^† a has eigenvalues exactly {0, 1} -----
    print("-" * 72)
    print("TEST 2: n = a^† a has eigenvalues exactly {0, 1}")
    print("-" * 72)
    eigs_n = sorted(np.linalg.eigvalsh(n_local).tolist())
    print(f"  n eigenvalues = {eigs_n}")
    t2_ok = abs(eigs_n[0] - 0.0) < 1e-12 and abs(eigs_n[1] - 1.0) < 1e-12
    print(f"  STATUS: {'PASS' if t2_ok else 'FAIL'}")
    print()

    # Now multi-site
    N = 4  # 4 sites for explicit Fock space
    dim = 2 ** N
    print(f"  Multi-site Fock space: N = {N} sites, dim = {dim}")
    print()

    # ----- Test 3: Multi-site n_x mutually commute -----
    print("-" * 72)
    print(f"TEST 3: Multi-site n_x mutually commute  (x = 0, ..., {N-1})")
    print("-" * 72)
    n_ops = [n_at_site(N, x) for x in range(N)]
    max_comm = 0.0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            comm = n_ops[i] @ n_ops[j] - n_ops[j] @ n_ops[i]
            d = np.linalg.norm(comm)
            max_comm = max(max_comm, d)
    print(f"  max ||[n_x, n_y]|| = {max_comm:.3e}")
    t3_ok = max_comm < 1e-12
    print(f"  STATUS: {'PASS' if t3_ok else 'FAIL'}")
    print()

    # ----- Test 4: Q̂_total = Σ n_x has integer spectrum {0, 1, ..., N} -----
    print("-" * 72)
    print(f"TEST 4: Q_total = Σ_x n_x has integer spectrum {{0, 1, ..., {N}}}")
    print("-" * 72)
    Q_total = sum(n_ops)
    eigs_Q = sorted(np.linalg.eigvalsh(Q_total).tolist())
    print(f"  Q_total eigenvalues (sorted): {eigs_Q}")
    distinct = sorted(set(round(e, 10) for e in eigs_Q))
    print(f"  Distinct values: {distinct}")
    expected = list(range(N + 1))
    t4_ok = all(any(abs(d - k) < 1e-10 for d in distinct) for k in expected) and len(distinct) == len(expected)
    print(f"  Expected: {expected}")
    print(f"  STATUS: {'PASS' if t4_ok else 'FAIL'}")
    print()

    # ----- Test 5: Multiplicity at occupation count k is C(N, k) -----
    print("-" * 72)
    print(f"TEST 5: Multiplicity at occupation count k is C({N}, k) = binomial(N, k)")
    print("-" * 72)
    multiplicities = {}
    for e in eigs_Q:
        k = int(round(e))
        multiplicities[k] = multiplicities.get(k, 0) + 1
    expected_mult = {k: math.comb(N, k) for k in range(N + 1)}
    print(f"  observed multiplicities: {multiplicities}")
    print(f"  expected (C(N, k)):      {expected_mult}")
    t5_ok = multiplicities == expected_mult
    print(f"  STATUS: {'PASS' if t5_ok else 'FAIL'}")
    print()

    # ----- Test 6: Equivalent formula via σ_3 -----
    print("-" * 72)
    print(f"TEST 6: Q_total = N/2 · I + (1/2) Σ_x (-σ_{{3,x}})  (since n = (I - σ_3)/2)")
    print(f"        Note: with |0⟩ being eigenvector of +1 of σ_3 and |1⟩ being -1,")
    print(f"        n = a^† a has eigenvalue 0 on |0⟩ and 1 on |1⟩, so n = (I - σ_3)/2.")
    print("-" * 72)
    sigma_3 = np.array([[1, 0], [0, -1]], dtype=complex)

    def sigma_3_at_site(N, x):
        factors = [sigma_3 if i == x else I2 for i in range(N)]
        return kron_chain(factors)

    # n = (I - σ_3) / 2 ⇒ Σ n_x = N/2 · I - (1/2) Σ σ_3,x
    Q_alt = (N / 2) * np.eye(dim, dtype=complex) - 0.5 * sum(sigma_3_at_site(N, x) for x in range(N))
    dev6 = np.linalg.norm(Q_total - Q_alt)
    print(f"  ||Q_total - (N/2 I - (1/2)Σ σ_3,x)|| = {dev6:.3e}")
    t6_ok = dev6 < 1e-12
    print(f"  STATUS: {'PASS' if t6_ok else 'FAIL'}")
    print()

    print("=" * 72)
    print(f"  Source firewall (A1 occupation count):              {'PASS' if t0_ok else 'FAIL'}")
    print(f"  Test 1 ({{a, a^†}} = I and Grassmann nilpotency):    {'PASS' if t1_ok else 'FAIL'}")
    print(f"  Test 2 (n eigenvalues = {{0, 1}}):                    {'PASS' if t2_ok else 'FAIL'}")
    print(f"  Test 3 (multi-site n_x commute):                    {'PASS' if t3_ok else 'FAIL'}")
    print(f"  Test 4 (Q_total integer spectrum {{0,...,N}}):       {'PASS' if t4_ok else 'FAIL'}")
    print(f"  Test 5 (multiplicity = binomial(N,k)):              {'PASS' if t5_ok else 'FAIL'}")
    print(f"  Test 6 (Q_total = N/2*I - (1/2)Σ σ_3 formula):       {'PASS' if t6_ok else 'FAIL'}")
    all_ok = all([t0_ok, t1_ok, t2_ok, t3_ok, t4_ok, t5_ok, t6_ok])
    print(f"  OVERALL: {'PASS' if all_ok else 'FAIL'}")
    if not all_ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
