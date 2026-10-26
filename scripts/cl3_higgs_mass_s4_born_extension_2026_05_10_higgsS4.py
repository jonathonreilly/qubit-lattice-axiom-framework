#!/usr/bin/env python3
"""Supplied finite expectation/curvature examples, not a physical Higgs-mass derivation."""
from __future__ import annotations
import sys
AUDIT_TIMEOUT_SEC = 120
PASS = 0
FAIL = 0

def report(label: str, ok: bool, detail: str='') -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f'[PASS] {label} -- {detail}' if detail else f'[PASS] {label}')
    else:
        FAIL += 1
        print(f'[FAIL] {label} -- {detail}' if detail else f'[FAIL] {label}')

def section_header(label: str) -> None:
    print()
    print('=' * 78)
    print(label)
    print('=' * 78)

def section1_trace_template_generality() -> None:
    """M1.1: For any density operator rho_hat and Hermitian operator O,
    <O> = Tr(rho_hat * O). Verify on toy lattice with multiple
    observables.
    """
    section_header('Section 1: M1.1 trace-template generality Tr(rho * O) = <O>')
    try:
        import numpy as np
    except ImportError:
        report('S1.0 numpy import', False, 'numpy required')
        return
    N = 4
    psi = np.array([0.6, 0.5, 0.4, 0.3], dtype=complex)
    psi /= np.linalg.norm(psi)
    rho = np.outer(psi, psi.conj())
    M2 = np.zeros((N, N), dtype=complex)
    M2[2, 2] = 1.0
    M1 = np.zeros((N, N), dtype=complex)
    M1[1, 1] = 1.0
    sx_op = np.diag(np.array([0.0, 1.0, 2.0, 3.0], dtype=complex))
    O_curv = np.zeros((N, N), dtype=complex)
    for i in range(N):
        O_curv[i, i] = 2.0
        O_curv[i, (i + 1) % N] = -1.0
        O_curv[i, (i - 1) % N] = -1.0
    for label, op in [('M_hat(x=2)', M2), ('M_hat(x=1)', M1), ('diagonal observable', sx_op), ('O_curv', O_curv)]:
        trace_value = np.trace(rho @ op).real
        direct_value = float((psi.conj() @ op @ psi).real)
        match = abs(trace_value - direct_value) < 1e-10
        report(f'S1.1 {label}: <O> = Tr(rho * O) = <psi|O|psi>', match, f'Tr value = {trace_value:.6f}, direct = {direct_value:.6f}')
    for label, op in [('M_hat(x=2)', M2), ('diagonal observable', sx_op), ('O_curv', O_curv)]:
        herm = np.allclose(op, op.conj().T)
        report(f'S1.2 {label}: Hermitian', herm, f'max |op - op^dagger| = {float(np.max(np.abs(op - op.conj().T))):.2e}')

def section2_distinct_observables() -> None:
    """The supplied coordinate projector and four-cycle Laplacian are distinct
    finite matrices; no physical curvature or mass operator is identified.
    """
    section_header('Section 2: supplied coordinate projector versus four-cycle Laplacian')
    import numpy as np
    N = 4
    M2 = np.zeros((N, N), dtype=complex)
    M2[2, 2] = 1.0
    O_curv = np.zeros((N, N), dtype=complex)
    for i in range(N):
        O_curv[i, i] = 2.0
        O_curv[i, (i + 1) % N] = -1.0
        O_curv[i, (i - 1) % N] = -1.0
    M2_rank = int(np.linalg.matrix_rank(M2))
    M2_idempotent = np.allclose(M2 @ M2, M2)
    M2_eigs = np.linalg.eigvalsh(M2)
    M2_psd = bool(np.all(M2_eigs >= -1e-12))
    report('S2.1 M_hat(x=2) is rank-1 (projector property)', M2_rank == 1, f'rank(M_hat) = {M2_rank}')
    report('S2.2 M_hat(x=2) is idempotent (M^2 = M)', M2_idempotent, 'rank-1 projector')
    report('S2.3 M_hat(x=2) is PSD', M2_psd, f'min eig = {float(np.min(M2_eigs)):.6e}')
    O_rank = int(np.linalg.matrix_rank(O_curv))
    O_idempotent = np.allclose(O_curv @ O_curv, O_curv)
    O_eigs = np.linalg.eigvalsh(O_curv)
    O_psd = bool(np.all(O_eigs >= -1e-12))
    report('S2.4 O_curv is rank > 1 (NOT a rank-1 projector)', O_rank > 1, f'rank(O_curv) = {O_rank} (N-1 = {N - 1} for Z_{N} periodic Laplacian)')
    report('S2.5 O_curv is NOT idempotent (NOT a projector)', not O_idempotent, f'max |O^2 - O| = {float(np.max(np.abs(O_curv @ O_curv - O_curv))):.6f}')
    diff_rank = M2_rank != O_rank
    report('S2.6 M_hat(x) and O_curv are structurally distinct (different ranks)', diff_rank, f'rank(M) = {M2_rank}, rank(O_curv) = {O_rank}')
    psi = np.array([0.6, 0.5, 0.4, 0.3], dtype=complex)
    psi /= np.linalg.norm(psi)
    rho = np.outer(psi, psi.conj())
    exp_M = float((psi.conj() @ M2 @ psi).real)
    exp_O = float((psi.conj() @ O_curv @ psi).real)
    diff_expectation = abs(exp_M - exp_O) > 0.001
    report('S2.7 different expectations on the same state (M_hat vs O_curv)', diff_expectation, f'<M_hat(x=2)> = {exp_M:.4f}, <O_curv> = {exp_O:.4f}')

def section3_state_selection_gap() -> None:
    """Supplied scalar quartic: compare derivatives at its origin and minimum.
    No framework vacuum state or physical mass observable is constructed.
    """
    section_header('Section 3: origin and minimum of a supplied scalar quartic')
    import numpy as np
    a = 1.0
    b = 0.1

    def V_double_prime(phi: float) -> float:
        return -2.0 * a + 12.0 * b * phi * phi
    V_pp_sym = V_double_prime(0.0)
    sym_tachyonic = V_pp_sym < 0
    report("S3.1 Supplied V''(phi=0) is negative (origin is a local maximum)", sym_tachyonic, f"V''(0) = {V_pp_sym:.4f} < 0")
    phi_star_sq = a / (2.0 * b)
    phi_star = float(np.sqrt(phi_star_sq))
    V_pp_v = V_double_prime(phi_star)
    post_ewsb_positive = V_pp_v > 0
    report("S3.2 V''(phi=v*) is positive (supplied quartic minimum)", post_ewsb_positive, f"v* = {phi_star:.4f}, V''(v*) = {V_pp_v:.4f} > 0")
    diff_curvatures = abs(abs(V_pp_sym) - V_pp_v) > 0.001 or V_pp_sym * V_pp_v < 0
    report("S3.3 supplied potential curvatures differ at origin and minimum", diff_curvatures, f"|V''(0)| = {abs(V_pp_sym):.4f}, V''(v*) = {V_pp_v:.4f}, signs differ")
    sign_flip = V_pp_sym * V_pp_v < 0
    report("S3.4 sign of supplied V'' differs at origin and quartic minimum", sign_flip, f"sign(V''(0)) = -, sign(V''(v*)) = +")

def additional_controls():
    import numpy as np
    # Same symmetric curvature, distinct minima: the curvature alone does not select b.
    a = 1.0
    bs = np.array([0.1, 0.4])
    minima = np.sqrt(a/(2*bs))
    report("Supplied quartic models share origin curvature but have distinct minima",
           abs(minima[0]-minima[1]) > 1e-3,
           f"Vpp(0)=-2; minima={minima.tolist()}")
    # Historical supplied comparators, not calculated masses or a causal error budget.
    predicted, comparator = 140.3, 125.25
    gap = predicted-comparator
    relative = gap/comparator
    report("Historical comparator difference is15.05GeV", abs(gap-15.05)<1e-12)
    report("Historical relative discrepancy is301/2505", abs(relative-301/2505)<1e-12)
    print("The discrepancy alone does not identify an approximation error or its cause.")

def main():
    print("Finite four-site matrices and supplied quartic-potential examples")
    section1_trace_template_generality()
    section2_distinct_observables()
    section3_state_selection_gap()
    additional_controls()
    print("Scope: toy matrix rank/expectation and potential arithmetic only; no physical mass observable, vacuum selection or pole-mass matching is supplied.")
    print(f"=== TOTAL: PASS={PASS}, FAIL={FAIL} ===")
    return 0 if FAIL == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
