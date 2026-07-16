"""Total occupation parity (-1)^Q_hat on framework Fock space.

Define the total occupation-number operator directly on the finite
occupation/Fock space and define the occupation-parity operator

    (-1)^Q̂  :=  exp(i π Q̂)

acting on the framework's N-site Fock space H = ⊗_{x=1}^N C².

Then:
  (P1) (-1)^Q̂ is unitary and Hermitian (its own inverse): ((-1)^Q̂)² = I
  (P2) [H_dyn, F] = 0 is necessary and sufficient for parity conservation;
       [H_dyn, Q̂] = 0 is sufficient and, for N >= 2, not necessary in
       general; at N = 1 the two commutation conditions are equivalent
  (P3) Spec((-1)^Q̂) = {+1, -1}
  (P4) Z_2 grading: H = H_even ⊕ H_odd with dim H_even = dim H_odd = 2^{N-1}
  (P5) Local ladder operator a_x is Z_2-odd: (-1)^Q̂ a_x (-1)^Q̂ = -a_x
  (P6) Local bilinear a_x^† a_y is Z_2-even: invariant under (-1)^Q̂

This is the framework's algebraic occupation-parity grading: the proved
Z_2-even bilinears and number operators preserve parity sectors.

Tests:
  (T1) (-1)^Q̂ is Hermitian
  (T2) ((-1)^Q̂)² = I
  (T3) [(-1)^Q̂, n̂_x] = 0 for all x (since n̂ is Z_2-even)
  (T4) Spec((-1)^Q̂) = {+1, -1}
  (T5) Z_2-grading dim balance: dim H_even = dim H_odd = 2^{N-1}
  (T6) Z_2-odd action on a_x: {(-1)^Q̂, a_x} = 0
  (T7) Z_2-even action on bilinears: [(-1)^Q̂, a_x^† a_y] = 0
  (T8) [H_dyn, Q̂] = 0 implies [H_dyn, F] = 0 on a number-conserving H
  (T9) N = 1 equivalence and N >= 2 negative-converse pair control
  (T10) [H_dyn, F] = 0 iff the parity-mixing blocks (and dF/dt) vanish
"""
from __future__ import annotations

import numpy as np


def kron_chain(matrices: list[np.ndarray]) -> np.ndarray:
    result = matrices[0]
    for M in matrices[1:]:
        result = np.kron(result, M)
    return result


def main() -> None:
    print("=" * 72)
    print("FRAMEWORK OCCUPATION PARITY (-1)^Q̂ AND Z_2 GRADING")
    print("=" * 72)
    print()

    N = 4  # 4-site Fock space
    dim = 2 ** N
    print(f"  Toy model: N = {N} sites, dim = {dim}")
    print()

    a_op = np.array([[0, 1], [0, 0]], dtype=complex)  # σ_+
    a_dag = a_op.conj().T  # σ_-
    n_local = a_dag @ a_op  # diag(0, 1)
    sigma_3 = np.array([[1, 0], [0, -1]], dtype=complex)
    I2 = np.eye(2, dtype=complex)

    def at_site(local_op: np.ndarray, x: int) -> np.ndarray:
        factors = [local_op if i == x else I2 for i in range(N)]
        return kron_chain(factors)

    # Build Q̂_total
    Q_total = sum(at_site(n_local, x) for x in range(N))
    Iden = np.eye(dim, dtype=complex)

    # Build (-1)^Q̂ via spectral decomposition (since Q̂ is diagonal in Fock basis)
    # Easier: use σ_3-formula. n = (I - σ_3)/2, so Q = N/2 - (1/2) Σ σ_3,x
    # Then (-1)^Q = (-1)^{N/2 - (1/2) Σ σ_3} = (-1)^{N/2} · (-1)^{-(1/2) Σ σ_3}
    # = (-1)^{N/2} · ∏_x (-1)^{-σ_3,x / 2}
    # Hmm, easier: (-1)^Q is diagonal in Fock basis with value (-1)^{|ν|} on |ν⟩
    # = ∏_x (-1)^{ν_x} = ∏_x σ_3,x (with appropriate convention)
    # Specifically: ν_x = 0 ↔ σ_3 = +1, ν_x = 1 ↔ σ_3 = -1
    # So (-1)^{ν_x} = +1 if ν_x = 0 (σ_3 = +1), and -1 if ν_x = 1 (σ_3 = -1)
    # i.e. (-1)^{ν_x} = σ_3,x as an eigenvalue
    # So (-1)^Q = ∏_x σ_3,x (tensor product of σ_3's)
    F = kron_chain([sigma_3] * N)  # = ⊗ σ_3

    # Verify F = (-1)^Q on the diagonal
    print(f"  Computing (-1)^Q̂ via product of σ_3 over all sites")
    diag_Q = np.diag(Q_total).real.astype(int)
    diag_F = np.diag(F).real.astype(int)
    expected_F_diag = (-1) ** diag_Q
    formula_dev = np.linalg.norm(diag_F - expected_F_diag)
    print(f"  ||diag((-1)^Q̂) - diag(⊗ σ_3)|| = {formula_dev:.3e}")
    if formula_dev > 1e-10:
        # If formula doesn't match, build directly via spectral decomposition
        print("  (Falling back to direct construction via diag.)")
        F = np.diag((-1.0) ** diag_Q).astype(complex)
    print()

    # ----- Test 1: (-1)^Q̂ is Hermitian -----
    print("-" * 72)
    print("TEST 1: (-1)^Q̂ is Hermitian")
    print("-" * 72)
    dev1 = np.linalg.norm(F - F.conj().T)
    print(f"  ||F - F†|| = {dev1:.3e}")
    t1_ok = dev1 < 1e-12
    print(f"  STATUS: {'PASS' if t1_ok else 'FAIL'}")
    print()

    # ----- Test 2: F² = I (involution) -----
    print("-" * 72)
    print("TEST 2: ((-1)^Q̂)² = I  (involution)")
    print("-" * 72)
    F_sq = F @ F
    dev2 = np.linalg.norm(F_sq - Iden)
    print(f"  ||F² - I|| = {dev2:.3e}")
    t2_ok = dev2 < 1e-12
    print(f"  STATUS: {'PASS' if t2_ok else 'FAIL'}")
    print()

    # ----- Test 3: [F, n̂_x] = 0 (since n̂ is Z_2-even) -----
    print("-" * 72)
    print("TEST 3: [(-1)^Q̂, n̂_x] = 0  for all x  (n̂ is Z_2-even)")
    print("-" * 72)
    max_comm = 0.0
    for x in range(N):
        n_x = at_site(n_local, x)
        comm = F @ n_x - n_x @ F
        d = np.linalg.norm(comm)
        max_comm = max(max_comm, d)
    print(f"  max ||[F, n̂_x]|| = {max_comm:.3e}")
    t3_ok = max_comm < 1e-12
    print(f"  STATUS: {'PASS' if t3_ok else 'FAIL'}")
    print()

    # ----- Test 4: Spec(F) = {+1, -1} -----
    print("-" * 72)
    print("TEST 4: Spec((-1)^Q̂) = {+1, -1}")
    print("-" * 72)
    eigs = sorted(set(np.round(np.linalg.eigvalsh(F).real, 8)))
    print(f"  Distinct eigenvalues: {eigs}")
    t4_ok = eigs == [-1.0, 1.0]
    print(f"  STATUS: {'PASS' if t4_ok else 'FAIL'}")
    print()

    # ----- Test 5: Z_2 grading dim balance -----
    print("-" * 72)
    print(f"TEST 5: dim H_even = dim H_odd = 2^{{N-1}} = {2 ** (N - 1)}")
    print("-" * 72)
    eigvals = np.linalg.eigvalsh(F).real
    n_pos = sum(1 for e in eigvals if e > 0)
    n_neg = sum(1 for e in eigvals if e < 0)
    print(f"  dim H_even (eigenvalue +1) = {n_pos}")
    print(f"  dim H_odd  (eigenvalue -1) = {n_neg}")
    t5_ok = n_pos == 2 ** (N - 1) and n_neg == 2 ** (N - 1)
    print(f"  STATUS: {'PASS' if t5_ok else 'FAIL'}")
    print()

    # ----- Test 6: {F, a_x} = 0 (a_x is Z_2-odd) -----
    print("-" * 72)
    print("TEST 6: {(-1)^Q̂, a_x} = 0  for all x  (ladder operator is Z_2-odd)")
    print("-" * 72)
    max_anti = 0.0
    for x in range(N):
        # On a tensor product, a_x acting at site x might need Jordan-Wigner-like
        # phases for a true CAR. But the σ_+ at site x without JW string is what
        # we use here (matches the per-site occupation convention; Q̂ is built from
        # n̂_x = a_x^† a_x without JW).
        a_x_op = at_site(a_op, x)
        anti = F @ a_x_op + a_x_op @ F
        d = np.linalg.norm(anti)
        max_anti = max(max_anti, d)
    print(f"  max ||{{F, a_x}}|| = {max_anti:.3e}")
    t6_ok = max_anti < 1e-12
    print(f"  STATUS: {'PASS' if t6_ok else 'FAIL'}")
    print()

    # ----- Test 7: [F, a_x^† a_y] = 0 (bilinears are Z_2-even) -----
    print("-" * 72)
    print("TEST 7: [(-1)^Q̂, a_x^† a_y] = 0  (bilinears are Z_2-even)")
    print("-" * 72)
    max_comm_bil = 0.0
    for x in range(N):
        for y in range(N):
            a_x_dag = at_site(a_dag, x)
            a_y = at_site(a_op, y)
            bil = a_x_dag @ a_y
            comm = F @ bil - bil @ F
            d = np.linalg.norm(comm)
            max_comm_bil = max(max_comm_bil, d)
    print(f"  max ||[F, a_x^† a_y]|| = {max_comm_bil:.3e}")
    t7_ok = max_comm_bil < 1e-12
    print(f"  STATUS: {'PASS' if t7_ok else 'FAIL'}")
    print()

    # ----- Test 8: number conservation is sufficient for parity conservation -----
    print("-" * 72)
    print("TEST 8: [H_dyn, Q̂] = 0 implies [H_dyn, F] = 0")
    print("-" * 72)
    a_at = [at_site(a_op, x) for x in range(N)]
    a_dag_at = [at_site(a_dag, x) for x in range(N)]
    H_number = a_dag_at[0] @ a_at[1] + a_dag_at[1] @ a_at[0]
    number_q_comm = np.linalg.norm(H_number @ Q_total - Q_total @ H_number)
    number_f_comm = np.linalg.norm(H_number @ F - F @ H_number)
    print(f"  ||[H_number, Q̂]|| = {number_q_comm:.3e}")
    print(f"  ||[H_number, F]|| = {number_f_comm:.3e}")
    t8_ok = number_q_comm < 1e-12 and number_f_comm < 1e-12
    print(f"  STATUS: {'PASS' if t8_ok else 'FAIL'}")
    print()

    # ----- Test 9: parity conservation does not imply number conservation -----
    print("-" * 72)
    print("TEST 9: N = 1 equivalence; N >= 2 converse counterexample")
    print("-" * 72)
    H_one = a_op + a_dag
    one_q_comm = H_one @ n_local - n_local @ H_one
    one_f_comm = H_one @ sigma_3 - sigma_3 @ H_one
    one_affine_dev = np.linalg.norm(sigma_3 - (I2 - 2.0 * n_local))
    one_comm_relation_dev = np.linalg.norm(one_f_comm + 2.0 * one_q_comm)
    print(f"  N = 1 ||F - (I - 2 Q̂)|| = {one_affine_dev:.3e}")
    print(f"  N = 1 ||[H, F] + 2[H, Q̂]|| = {one_comm_relation_dev:.3e}")
    H_pair = a_dag_at[0] @ a_dag_at[1] + a_at[1] @ a_at[0]
    pair_f_comm = np.linalg.norm(H_pair @ F - F @ H_pair)
    pair_q_comm = np.linalg.norm(H_pair @ Q_total - Q_total @ H_pair)
    pair_herm_dev = np.linalg.norm(H_pair - H_pair.conj().T)
    print(f"  ||H_pair - H_pair†|| = {pair_herm_dev:.3e}")
    print(f"  ||[H_pair, F]|| = {pair_f_comm:.3e}")
    print(f"  ||[H_pair, Q̂]|| = {pair_q_comm:.3e}  (nonzero)")
    t9_ok = (
        one_affine_dev < 1e-12
        and one_comm_relation_dev < 1e-12
        and pair_herm_dev < 1e-12
        and pair_f_comm < 1e-12
        and pair_q_comm > 1e-10
    )
    print(f"  STATUS: {'PASS' if t9_ok else 'FAIL'}")
    print()

    # ----- Test 10: exact necessary-and-sufficient parity criterion -----
    print("-" * 72)
    print("TEST 10: [H_dyn, F] = 0 iff parity-mixing blocks vanish")
    print("-" * 72)
    P_even = 0.5 * (Iden + F)
    P_odd = 0.5 * (Iden - F)
    rng = np.random.default_rng(20260715)
    raw = rng.standard_normal((dim, dim)) + 1j * rng.standard_normal((dim, dim))
    H_trial = 0.5 * (raw + raw.conj().T)
    even_to_odd = P_even @ H_trial @ P_odd
    odd_to_even = P_odd @ H_trial @ P_even
    trial_comm = H_trial @ F - F @ H_trial
    block_identity_dev = np.linalg.norm(
        trial_comm - 2.0 * (odd_to_even - even_to_odd)
    )
    H_parity = P_even @ H_trial @ P_even + P_odd @ H_trial @ P_odd
    projected_cross_norm = np.linalg.norm(
        P_even @ H_parity @ P_odd + P_odd @ H_parity @ P_even
    )
    projected_comm_norm = np.linalg.norm(H_parity @ F - F @ H_parity)
    trial_cross_norm = np.linalg.norm(even_to_odd + odd_to_even)
    heisenberg_derivative_norm = np.linalg.norm(1j * trial_comm)
    print(f"  commutator/block identity deviation = {block_identity_dev:.3e}")
    print(f"  parity-projected cross-block norm = {projected_cross_norm:.3e}")
    print(f"  parity-projected ||[H, F]|| = {projected_comm_norm:.3e}")
    print(f"  generic cross-block norm = {trial_cross_norm:.3e}  (nonzero)")
    print(f"  generic ||dF/dt|| = ||i[H, F]|| = {heisenberg_derivative_norm:.3e}")
    t10_ok = (
        block_identity_dev < 1e-12
        and projected_cross_norm < 1e-12
        and projected_comm_norm < 1e-12
        and trial_cross_norm > 1e-10
        and heisenberg_derivative_norm > 1e-10
    )
    print(f"  STATUS: {'PASS' if t10_ok else 'FAIL'}")
    print()

    print("=" * 72)
    print(f"  Test 1 ((-1)^Q̂ Hermitian):                       {'PASS' if t1_ok else 'FAIL'}")
    print(f"  Test 2 (((-1)^Q̂)² = I involution):                {'PASS' if t2_ok else 'FAIL'}")
    print(f"  Test 3 ([F, n̂_x] = 0):                            {'PASS' if t3_ok else 'FAIL'}")
    print(f"  Test 4 (Spec = {{+1, -1}}):                         {'PASS' if t4_ok else 'FAIL'}")
    print(f"  Test 5 (Z_2 grading dim balance):                 {'PASS' if t5_ok else 'FAIL'}")
    print(f"  Test 6 (ladder operator is Z_2-odd: {{F, a_x}} = 0): {'PASS' if t6_ok else 'FAIL'}")
    print(f"  Test 7 (bilinear a_x^† a_y is Z_2-even):           {'PASS' if t7_ok else 'FAIL'}")
    print(f"  Test 8 (number conservation implies parity):         {'PASS' if t8_ok else 'FAIL'}")
    print(f"  Test 9 (N=1 equivalence; N>=2 converse false):        {'PASS' if t9_ok else 'FAIL'}")
    print(f"  Test 10 ([H, F] iff no parity-mixing blocks):         {'PASS' if t10_ok else 'FAIL'}")
    all_ok = all([
        t1_ok,
        t2_ok,
        t3_ok,
        t4_ok,
        t5_ok,
        t6_ok,
        t7_ok,
        t8_ok,
        t9_ok,
        t10_ok,
    ])
    print(f"  OVERALL: {'PASS' if all_ok else 'FAIL'}")
    if not all_ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
