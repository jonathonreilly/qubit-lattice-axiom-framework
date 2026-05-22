#!/usr/bin/env python3
"""Exact-symbolic audit-companion runner for
`LUDERS_SEQUENTIAL_PRODUCT_CONDITIONAL_BRIDGE_NARROW_THEOREM_NOTE_2026-05-22.md`.

Verifies the conditional Lüders-bridge theorem:

  IF the framework's instrument for projective measurement of P is the
  Lüders Kraus operator K_P := P (the "square-root sequential product"
  with sqrt(P) = P for idempotent P), THEN the sequential-effect
  composition M_{P,E} := K_P^dagger E K_P equals P E P on the
  qubit-lattice operator algebra.

Reviewer's salvage path for the rejected PR #1626 was:

  "land an honest bounded/support note saying that PEP follows once the
   Lüders/Gudder square-root sequential product or equivalent
   instrument-selection premise is explicitly admitted."

This runner exhibits the conditional on multiple framework instrument
families and verifies the algebra symbolically. It does NOT claim to
remove the missing-bridge blocker from the Lüders audit verdict (the
reviewer said it wouldn't); it only lands the conditional support.

Companion role: source-side construction with explicit verification.
Not a new claim row, not a status promotion.
"""

from pathlib import Path
import sys

try:
    import sympy
    from sympy import (
        Rational, Symbol, sqrt, simplify, Matrix, eye, zeros, I, cos, sin, pi,
        nsimplify, conjugate, Add,
    )
except ImportError:
    print("FAIL: sympy required for exact algebra")
    sys.exit(1)

try:
    import numpy as np
except ImportError:
    print("FAIL: numpy required for numerical sanity checks")
    sys.exit(1)


PASS = 0
FAIL = 0


def _report(label: str, ok: bool, detail: str = ""):
    global PASS, FAIL
    status = "PASS" if ok else "FAIL"
    print(f"  [{status}] {label}{(': ' + detail) if detail else ''}")
    if ok:
        PASS += 1
    else:
        FAIL += 1


def kron(A: Matrix, B: Matrix) -> Matrix:
    rows_a, cols_a = A.shape
    rows_b, cols_b = B.shape
    result = zeros(rows_a * rows_b, cols_a * cols_b)
    for i in range(rows_a):
        for j in range(cols_a):
            for k in range(rows_b):
                for l in range(cols_b):
                    result[i * rows_b + k, j * cols_b + l] = A[i, j] * B[k, l]
    return result


def verify_projection_idempotent(P: Matrix, label: str):
    """A projection satisfies P^2 = P and P = P^dagger."""
    d = P.shape[0]
    diff_sq = simplify(P * P - P)
    diff_dag = simplify(P.H - P)
    is_idem = all(diff_sq[i, j] == 0 for i in range(d) for j in range(d))
    is_self = all(diff_dag[i, j] == 0 for i in range(d) for j in range(d))
    _report(f"{label}: P is idempotent (P^2 = P)", is_idem)
    _report(f"{label}: P is self-adjoint (P^dagger = P)", is_self)
    return is_idem and is_self


def verify_kraus_normalization(K_P: Matrix, P: Matrix, label: str):
    """For K_P = P (Lüders): K_P^dagger K_P = P^dagger P = P^2 = P.

    Note: for projection-valued measurement of P, the COMPLEMENTARY Kraus
    is K_{!P} = sqrt(I - P) = I - P (also a projection). So the full
    instrument is {P, I-P} with P + (I-P) = I.
    """
    d = K_P.shape[0]
    # K_P^dagger K_P = P (for K_P = P)
    KdK = simplify(K_P.H * K_P)
    diff = simplify(KdK - P)
    ok = all(diff[i, j] == 0 for i in range(d) for j in range(d))
    _report(f"{label}: K_P^dagger K_P = P (Lüders Kraus normalization)", ok)
    # Full instrument {P, I-P}: sum = I
    I_d = eye(d)
    KP_complement = I_d - P
    sum_KdK = simplify(P.H * P + KP_complement.H * KP_complement)
    diff_sum = simplify(sum_KdK - I_d)
    ok_sum = all(diff_sum[i, j] == 0 for i in range(d) for j in range(d))
    _report(f"{label}: K_P^dagger K_P + K_!P^dagger K_!P = I (resolution of identity)", ok_sum)


def verify_sequential_composition(K_P: Matrix, P: Matrix, E: Matrix, label: str):
    """Check M_{P, E} := K_P^dagger E K_P = P E P (the PEP composition)."""
    d = K_P.shape[0]
    M = simplify(K_P.H * E * K_P)
    target = simplify(P * E * P)
    diff = simplify(M - target)
    ok = all(diff[i, j] == 0 for i in range(d) for j in range(d))
    _report(f"{label}: M_{{P,E}} = K_P^dagger E K_P = P E P", ok)
    return ok


def verify_luders_state_update(P: Matrix, sigma: Matrix, label: str):
    """Lüders state update: sigma|_P = P sigma P / Tr(P sigma P).

    With K_P = P, post-measurement state is rho' = K_P sigma K_P^dagger / Tr(K_P sigma K_P^dagger)
                                              = P sigma P / Tr(P sigma P).
    """
    d = P.shape[0]
    PsP = simplify(P * sigma * P)
    norm = simplify(PsP.trace())
    if norm == 0:
        _report(f"{label}: Lüders update Tr(P sigma P) > 0", False, "norm vanishes")
        return False
    rho_prime = simplify(PsP / norm)
    # Verify Tr(rho') = 1
    trace_ok = simplify(rho_prime.trace() - 1) == 0
    _report(f"{label}: Lüders update Tr(rho') = 1", trace_ok)
    # Verify rho' has range in P: P rho' = rho' (assuming P is a projection)
    PrhoP_minus_rho = simplify(P * rho_prime - rho_prime)
    in_range = all(PrhoP_minus_rho[i, j] == 0 for i in range(d) for j in range(d))
    _report(f"{label}: Lüders update P rho' = rho' (post-measurement state in range of P)", in_range)
    return trace_ok and in_range


# --------------------------------------------------------------------------
# Test 1 — Single qubit, rank-1 projection |0><0|
# --------------------------------------------------------------------------

def test_single_qubit_rank1():
    print("\n[T1] Single qubit, rank-1 projection P = |0><0|")
    P = Matrix([[1, 0], [0, 0]])
    verify_projection_idempotent(P, "T1.a")
    K_P = P  # Lüders selection
    verify_kraus_normalization(K_P, P, "T1.b")
    # Try several effects E
    sigma_x = Matrix([[0, 1], [1, 0]])
    sigma_z = Matrix([[1, 0], [0, -1]])
    Ix2 = eye(2)
    for E_name, E in [("I", Ix2), ("|1><1|", Ix2 - P), ("sigma_x", sigma_x), ("sigma_z", sigma_z)]:
        verify_sequential_composition(K_P, P, E, f"T1.c (E = {E_name})")
    # Lüders state update on a sample density matrix
    sigma = Matrix([[Rational(1, 2), Rational(1, 4)], [Rational(1, 4), Rational(1, 2)]])
    verify_luders_state_update(P, sigma, "T1.d")


# --------------------------------------------------------------------------
# Test 2 — Single qubit, projection in rotated basis (symbolic angle)
# --------------------------------------------------------------------------

def test_single_qubit_rotated():
    print("\n[T2] Single qubit, rank-1 projection in rotated basis (symbolic angle t)")
    t = Symbol('t', real=True)
    c = cos(t)
    s = sin(t)
    ket = Matrix([[c], [s]])
    P = ket * ket.T
    P = simplify(P)
    verify_projection_idempotent(P, "T2.a")
    K_P = P
    verify_kraus_normalization(K_P, P, "T2.b")
    # Use a symbolic effect
    a, b, c1, d1 = sympy.symbols('a b c d', real=True)
    E_sym = Matrix([[a, b], [b, d1]])  # Hermitian
    verify_sequential_composition(K_P, P, E_sym, "T2.c (symbolic Hermitian E)")


# --------------------------------------------------------------------------
# Test 3 — Two qubits, projection onto Bell state |Phi+><Phi+|
# --------------------------------------------------------------------------

def test_two_qubit_bell():
    print("\n[T3] Two qubits, projection onto |Phi+><Phi+|")
    sq2 = sqrt(2)
    phi_plus_ket = Matrix([1, 0, 0, 1]) / sq2
    phi_plus_col = phi_plus_ket.reshape(4, 1)
    P = simplify(phi_plus_col * phi_plus_col.T)
    verify_projection_idempotent(P, "T3.a")
    K_P = P
    verify_kraus_normalization(K_P, P, "T3.b")
    # Effects: identity, single-qubit Z on first qubit, two-qubit X⊗X
    sigma_x = Matrix([[0, 1], [1, 0]])
    sigma_z = Matrix([[1, 0], [0, -1]])
    Ix2 = eye(2)
    Z_otimes_I = kron(sigma_z, Ix2)
    X_otimes_X = kron(sigma_x, sigma_x)
    for E_name, E in [("I_4", eye(4)), ("Z⊗I", Z_otimes_I), ("X⊗X", X_otimes_X)]:
        verify_sequential_composition(K_P, P, E, f"T3.c (E = {E_name})")


# --------------------------------------------------------------------------
# Test 4 — Higher-rank projection (rank-2 on 4-dim H_sys)
# --------------------------------------------------------------------------

def test_rank2_projection():
    print("\n[T4] Two qubits, rank-2 projection P = |00><00| + |11><11|")
    # P projects onto the "diagonal" subspace of 2-qubit Hilbert
    P = zeros(4, 4)
    P[0, 0] = 1
    P[3, 3] = 1
    verify_projection_idempotent(P, "T4.a")
    K_P = P
    verify_kraus_normalization(K_P, P, "T4.b")
    # Effects
    Ix4 = eye(4)
    # arbitrary Hermitian
    a, b, c, d, e, f = sympy.symbols('a b c d e f', real=True)
    E_diag = Matrix([
        [a, 0, 0, b],
        [0, c, 0, 0],
        [0, 0, d, 0],
        [b, 0, 0, e],
    ])
    for E_name, E in [("I_4", Ix4), ("E_diag (symbolic)", E_diag)]:
        verify_sequential_composition(K_P, P, E, f"T4.c (E = {E_name})")


# --------------------------------------------------------------------------
# Test 5 — Counterexample: non-Lüders K_P with U-twist
# --------------------------------------------------------------------------

def test_counterexample_u_twist():
    """Show that K_P = U·P (for some unitary U) gives a DIFFERENT sequential
    composition M_{P, E} = P U^dagger E U P, NOT P E P.

    This confirms that the Lüders selection K_P = P is the load-bearing
    framework rule — alternative Kraus give different (non-PEP) compositions.
    """
    print("\n[T5] Counterexample: alternative Kraus K_P = sigma_z · P gives different composition")
    P = Matrix([[1, 0], [0, 0]])
    sigma_z = Matrix([[1, 0], [0, -1]])
    K_P_twisted = sigma_z * P  # = P for this particular P, but in general different
    # Verify K_P_twisted^dagger K_P_twisted = P (still a valid Kraus, satisfies normalization)
    KdK = simplify(K_P_twisted.H * K_P_twisted)
    matches_P = all(simplify(KdK[i, j] - P[i, j]) == 0 for i in range(2) for j in range(2))
    _report("T5.a: alternative K_P with U-twist still satisfies K_P^dagger K_P = P", matches_P)
    # Use a more interesting twist: K_P = H * P where H is Hadamard (single-qubit)
    h = Rational(1, 1) / sqrt(2)
    H = h * Matrix([[1, 1], [1, -1]])
    # Choose P such that H · P ≠ P (so the twist is genuinely different)
    # If P = |0><0|, then H · |0><0| = (|0> + |1>)/sqrt(2) <0| = first col [1/sqrt(2); 1/sqrt(2)] · row [1, 0]
    # = Matrix([[1/sqrt(2), 0], [1/sqrt(2), 0]])
    K_P_hadamard = simplify(H * P)
    # K_P_hadamard^dagger K_P_hadamard = P^dagger H^dagger H P = P I P = P
    KdK_h = simplify(K_P_hadamard.H * K_P_hadamard)
    matches_P_h = all(simplify(KdK_h[i, j] - P[i, j]) == 0 for i in range(2) for j in range(2))
    _report("T5.b: K_P = H · P (Hadamard-twisted) satisfies K_P^dagger K_P = P", matches_P_h)
    # But the sequential composition is DIFFERENT
    E = Matrix([[0, 1], [1, 0]])  # sigma_x
    M_hadamard = simplify(K_P_hadamard.H * E * K_P_hadamard)
    M_luders = simplify(P * E * P)
    differs = not all(simplify(M_hadamard[i, j] - M_luders[i, j]) == 0
                      for i in range(2) for j in range(2))
    _report(
        "T5.c: Hadamard-twisted M_{P,E} ≠ Lüders P E P (alternative Kraus → different composition)",
        differs,
        f"Hadamard: {M_hadamard.tolist()}, Lüders: {M_luders.tolist()}",
    )


# --------------------------------------------------------------------------
# Test 6 — Source-note boundary string checks
# --------------------------------------------------------------------------

def test_source_boundary_strings():
    print("\n[T6] Source-note boundary string checks")
    note_path = Path(__file__).resolve().parent.parent / "docs" / (
        "LUDERS_SEQUENTIAL_PRODUCT_CONDITIONAL_BRIDGE_NARROW_THEOREM_NOTE_2026-05-22.md"
    )
    if not note_path.exists():
        _report("T6.a: source note exists", False, f"not found: {note_path}")
        return
    text = note_path.read_text()
    required_strings = [
        "source-side proposal",
        "independent audit lane owns the verdict",
        "conditional",
        "does not by itself remove",
    ]
    forbidden_strings = [
        "Status: retained",
        "Status: promoted",
        "uniqueness theorem forces",
        "Greechie/Gudder uniqueness alone",
    ]
    for s in required_strings:
        present = s in text
        _report(f"T6.required: '{s}'", present)
    for s in forbidden_strings:
        absent = s not in text
        _report(f"T6.forbidden-absent: '{s}'", absent)


def main():
    print("=" * 70)
    print("Lüders sequential-product conditional bridge runner")
    print("=" * 70)
    print()
    print("Verifies the conditional theorem: IF Lüders K_P = P (the")
    print("square-root sequential product applied to projections), THEN")
    print("M_{P, E} = K_P^dagger E K_P = P E P (the standard PEP composition).")
    print()
    print("Does NOT claim uniqueness of the sequential product (which is")
    print("known to fail in the literature — see PR #1626 review for refs).")
    print("Only lands the conditional algebra.")
    print()
    test_single_qubit_rank1()
    test_single_qubit_rotated()
    test_two_qubit_bell()
    test_rank2_projection()
    test_counterexample_u_twist()
    test_source_boundary_strings()
    print()
    print("=" * 70)
    print(f"PASS={PASS} FAIL={FAIL}")
    print("=" * 70)
    sys.exit(0 if FAIL == 0 else 1)


if __name__ == "__main__":
    main()
