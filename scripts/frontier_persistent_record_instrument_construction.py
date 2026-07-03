#!/usr/bin/env python3
"""Exact-symbolic + numerical audit-companion runner for
`PERSISTENT_RECORD_INSTRUMENT_CONSTRUCTION_NARROW_THEOREM_NOTE_2026-05-22.md`.

Constructs the Stinespring isometry V: H_sys -> H_record (x) H_sys
explicitly as a block matrix from framework-side measurement-instrument
data {K_r} on the qubit-lattice substrate, and verifies V^dagger V =
Sigma_r K_r^dagger K_r = 1_sys for multiple concrete instrument
families.

The reviewer's specific objection on PR #1634 was:

  "Step 3 of this PR takes total probability preservation as inherited
   from standard QM, but that is precisely the missing carrier/instrument
   construction at issue."

This runner addresses the objection by exhibiting V as an explicit
matrix and verifying V^dagger V = 1 symbolically (no inheritance from
standard QM, just direct algebra on framework-supplied K_r matrices).

Companion role: source-side construction with explicit verification.
Not a new claim row, not a status promotion. Provides audit-friendly
exact-algebra evidence that the persistent-record instrument-construction
narrow theorem holds on the qubit-lattice substrate.

Upstream authorities/statuses (verified on docs/audit/data/audit_ledger.json):

  - cl3_complexification_split_narrow_theorem_note_2026-05-10: retained
    (supplies per-site M_2(C) ~= Cl(3,0))
  - kraus_choi_representation_on_qubit_lattice_narrow_theorem_note_2026-05-20:
    retained_pending_chain (supplies {K_r} with Sigma_r K_r^dagger K_r = 1)
  - busch_povm_extension_on_qubit_lattice_narrow_theorem_note_2026-05-20:
    retained_pending_chain (supplies the POVM E_r = K_r^dagger K_r side)
"""

from pathlib import Path
import sys

try:
    import sympy
    from sympy import (
        Rational, Symbol, sqrt, simplify, Matrix, eye, zeros, I, ZeroMatrix,
        BlockMatrix, conjugate, Abs, sin, cos, pi, Add, Mul, expand,
        nsimplify, re, im, sympify,
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
    """Print a single test result and update counters."""
    global PASS, FAIL
    status = "PASS" if ok else "FAIL"
    print(f"  [{status}] {label}{(': ' + detail) if detail else ''}")
    if ok:
        PASS += 1
    else:
        FAIL += 1


# --------------------------------------------------------------------------
# Framework primitives: per-site qubit, multi-qubit tensor algebra
# --------------------------------------------------------------------------

def pauli_matrices():
    """Per-site Pauli matrices for M_2(C) on H_x = C^2.

    These come from the one-qubit operator algebra in
    MINIMAL_AXIOMS_2026-05-20.md.
    """
    I2 = eye(2)
    sx = Matrix([[0, 1], [1, 0]])
    sy = Matrix([[0, -I], [I, 0]])
    sz = Matrix([[1, 0], [0, -1]])
    return I2, sx, sy, sz


def kron(A: Matrix, B: Matrix) -> Matrix:
    """Sympy Kronecker product wrapper.

    A (x) B builds the tensor-product matrix on H_A (x) H_B.
    Tensor composition on the Z^3 lattice is realized this way.
    """
    rows_a, cols_a = A.shape
    rows_b, cols_b = B.shape
    result = zeros(rows_a * rows_b, cols_a * cols_b)
    for i in range(rows_a):
        for j in range(cols_a):
            for k in range(rows_b):
                for l in range(cols_b):
                    result[i * rows_b + k, j * cols_b + l] = A[i, j] * B[k, l]
    return result


# --------------------------------------------------------------------------
# Stinespring isometry construction
# --------------------------------------------------------------------------

def build_stinespring_isometry(kraus_list):
    """Build V: H_sys -> H_record (x) H_sys from a Kraus family {K_r}.

    Given K_1, ..., K_R operators on H_sys (dim d) with
    Sigma_r K_r^dagger K_r = 1_sys, V is defined by

        V |psi> = Sigma_r |r> (x) (K_r |psi>)

    Concretely, V is the (R*d) x d block-column matrix with K_r stacked.
    Rows are ordered first by record label r and then by system row i, so
    zero-based row index alpha = r*d + i.  In one-based theorem notation this is
    alpha = (r-1)*d + i.  A downstream H_sys (x) H_record convention is obtained
    by the fixed tensor swap, which preserves V^dagger V.
    """
    if not kraus_list:
        raise ValueError("empty Kraus family")
    d = kraus_list[0].shape[0]
    R = len(kraus_list)
    V = zeros(R * d, d)
    for r, Kr in enumerate(kraus_list):
        if Kr.shape != (d, d):
            raise ValueError(f"K_{r} has shape {Kr.shape}; expected ({d},{d})")
        for i in range(d):
            for j in range(d):
                V[r * d + i, j] = Kr[i, j]
    return V


def verify_resolution_of_identity(kraus_list, label: str):
    """Check Sigma_r K_r^dagger K_r = 1_sys symbolically."""
    d = kraus_list[0].shape[0]
    accum = zeros(d, d)
    for Kr in kraus_list:
        accum = accum + Kr.H * Kr
    diff = simplify(accum - eye(d))
    is_zero = all(diff[i, j] == 0 for i in range(d) for j in range(d))
    _report(
        f"{label}: Sigma_r K_r^dagger K_r = 1_sys (symbolic)",
        is_zero,
        "" if is_zero else f"residual = {diff}",
    )
    return is_zero


def verify_stinespring_isometry(kraus_list, label: str):
    """Check V^dagger V = 1_sys for V built from {K_r} symbolically.

    V^dagger V = Sigma_r K_r^dagger K_r, so this is the resolution-of-
    identity check after the block-matrix construction. The point of
    exhibiting V explicitly is to show that the block-matrix algebra
    works out — total probability preservation is a property of the
    matrix V, not inherited from standard QM.
    """
    V = build_stinespring_isometry(kraus_list)
    d = kraus_list[0].shape[0]
    VdagV = simplify(V.H * V)
    target = eye(d)
    diff = simplify(VdagV - target)
    is_zero = all(diff[i, j] == 0 for i in range(d) for j in range(d))
    _report(
        f"{label}: V^dagger V = 1_sys (explicit block matrix)",
        is_zero,
        "" if is_zero else f"residual = {diff}",
    )
    return is_zero


def verify_block_structure(kraus_list, label: str):
    """Check that V as built has the documented block-column structure.

    V has R*d rows, d columns. Row block r contains K_r.
    """
    V = build_stinespring_isometry(kraus_list)
    d = kraus_list[0].shape[0]
    R = len(kraus_list)
    ok = V.shape == (R * d, d)
    if not ok:
        _report(f"{label}: V shape", False, f"got {V.shape}, expected {(R*d, d)}")
        return False
    for r in range(R):
        block = V[r * d:(r + 1) * d, :]
        block_diff = simplify(block - kraus_list[r])
        block_ok = all(block_diff[i, j] == 0 for i in range(d) for j in range(d))
        if not block_ok:
            _report(
                f"{label}: V row-block {r} = K_{r}",
                False,
                f"residual = {block_diff}",
            )
            return False
    _report(f"{label}: V row-blocks match K_r (R={R} blocks of size {d}x{d})", True)
    return True


# --------------------------------------------------------------------------
# Test 1 — Projective measurement on a single qubit (sigma_z eigenbasis)
# --------------------------------------------------------------------------

def test_single_qubit_projective_z():
    """Standard {|0><0|, |1><1|} projective measurement on a single qubit."""
    print("\n[T1] Single qubit projective measurement in sigma_z eigenbasis")
    P0 = Matrix([[1, 0], [0, 0]])
    P1 = Matrix([[0, 0], [0, 1]])
    kraus = [P0, P1]
    verify_resolution_of_identity(kraus, "T1.a")
    verify_block_structure(kraus, "T1.b")
    verify_stinespring_isometry(kraus, "T1.c")
    # Sanity: V|0> = |0_record> (x) |0_sys> in the record-first convention.
    psi_0 = Matrix([[1], [0]])
    psi_1 = Matrix([[0], [1]])
    V = build_stinespring_isometry(kraus)
    V_psi0 = V * psi_0
    V_psi1 = V * psi_1
    # Expected: V|0> has support only in row 0 (first block), V|1> in row 3 (second block)
    expected_0 = Matrix([[1], [0], [0], [0]])
    expected_1 = Matrix([[0], [0], [0], [1]])
    ok_0 = all(simplify(V_psi0[i] - expected_0[i]) == 0 for i in range(4))
    ok_1 = all(simplify(V_psi1[i] - expected_1[i]) == 0 for i in range(4))
    _report("T1.d: V|0> = |0_record> (x) |0_sys> (single record component)", ok_0)
    _report("T1.e: V|1> = |1_record> (x) |1_sys> (single record component)", ok_1)


# --------------------------------------------------------------------------
# Test 2 — Projective measurement in a rotated basis
# --------------------------------------------------------------------------

def test_single_qubit_projective_rotated():
    """Projective measurement in (cos t |0> + sin t |1>) basis, symbolic in t."""
    print("\n[T2] Single qubit projective measurement in rotated basis (symbolic t)")
    t = Symbol('t', real=True)
    c = cos(t)
    s = sin(t)
    # |+t> = c|0> + s|1>; |-t> = -s|0> + c|1>
    plus = Matrix([[c], [s]])
    minus = Matrix([[-s], [c]])
    Pp = plus * plus.T  # real-valued
    Pm = minus * minus.T
    kraus = [Pp, Pm]
    verify_resolution_of_identity(kraus, "T2.a")
    verify_stinespring_isometry(kraus, "T2.b")
    # Idempotent: Pp^2 = Pp
    Pp_sq = simplify(Pp * Pp)
    diff = simplify(Pp_sq - Pp)
    ok = all(diff[i, j] == 0 for i in range(2) for j in range(2))
    _report("T2.c: P_+t is idempotent (P^2 = P)", ok)


# --------------------------------------------------------------------------
# Test 3 — Non-projective POVM (single qubit, 3-outcome SIC-like)
# --------------------------------------------------------------------------

def test_single_qubit_three_outcome_povm():
    """Symmetric 3-outcome POVM on a single qubit.

    E_r = (2/3) |psi_r><psi_r| for three Bloch-sphere directions in a plane.
    Kraus K_r = sqrt(E_r). The standard SIC-POVM has 4 outcomes; we use a
    planar 3-outcome variant for symbolic compactness.
    """
    print("\n[T3] Single qubit 3-outcome planar POVM (K_r = sqrt(E_r))")
    # Three Bloch-vectors in xz-plane at 0, 2pi/3, 4pi/3
    theta_list = [Rational(0), Rational(2, 3) * pi, Rational(4, 3) * pi]
    # |psi_r> = cos(theta/2) |0> + sin(theta/2) |1>
    kraus = []
    for th in theta_list:
        c = cos(th / 2)
        s = sin(th / 2)
        ket = Matrix([[c], [s]])
        E_r = (Rational(2, 3)) * (ket * ket.T)
        # K_r = sqrt(E_r); for rank-1 E_r = lambda |psi><psi|, sqrt = sqrt(lambda) |psi><psi|
        # Compute symbolically via eigendecomposition: E_r has eigenvalue 2/3 with eigenvector ket and 0 with orthogonal.
        # So sqrt(E_r) = sqrt(2/3) |psi><psi|.
        Kr = sqrt(Rational(2, 3)) * (ket * ket.T)
        kraus.append(simplify(Kr))
    verify_resolution_of_identity(kraus, "T3.a")
    verify_stinespring_isometry(kraus, "T3.b")
    verify_block_structure(kraus, "T3.c")


# --------------------------------------------------------------------------
# Test 4 — Two-qubit projective measurement (Bell basis)
# --------------------------------------------------------------------------

def test_two_qubit_bell_measurement():
    """Bell-basis projective measurement on two qubits (4-dim H_sys)."""
    print("\n[T4] Two-qubit Bell-basis projective measurement")
    half = Rational(1, 2)
    sq2 = sqrt(2)
    # |Phi+> = (|00> + |11>)/sqrt(2)
    # |Phi-> = (|00> - |11>)/sqrt(2)
    # |Psi+> = (|01> + |10>)/sqrt(2)
    # |Psi-> = (|01> - |10>)/sqrt(2)
    phi_plus = Matrix([1, 0, 0, 1]) / sq2
    phi_minus = Matrix([1, 0, 0, -1]) / sq2
    psi_plus = Matrix([0, 1, 1, 0]) / sq2
    psi_minus = Matrix([0, 1, -1, 0]) / sq2
    bell_kets = [phi_plus, phi_minus, psi_plus, psi_minus]
    kraus = []
    for ket in bell_kets:
        ket_col = Matrix(ket).reshape(4, 1)
        P = ket_col * ket_col.T  # all entries real
        kraus.append(simplify(P))
    verify_resolution_of_identity(kraus, "T4.a")
    verify_block_structure(kraus, "T4.b")
    verify_stinespring_isometry(kraus, "T4.c")
    # The Stinespring V has shape (4*4, 4) = (16, 4); document this
    V = build_stinespring_isometry(kraus)
    ok_shape = V.shape == (16, 4)
    _report("T4.d: V shape (16, 4) for 4-outcome measurement on 2-qubit H_sys", ok_shape)


# --------------------------------------------------------------------------
# Test 5 — Asymmetric biased POVM (different probabilities per outcome)
# --------------------------------------------------------------------------

def test_biased_povm():
    """Biased 2-outcome POVM with parameter p in (0, 1)."""
    print("\n[T5] Biased 2-outcome POVM, K_r built from generalized measurement")
    p = Rational(1, 3)
    q = 1 - p
    # K_1 = sqrt(p) * sigma_z_proj, K_2 needs to complete identity
    # Use Kraus: K_1 = [[sqrt(p), 0], [0, sqrt(q)]], K_2 = [[sqrt(q), 0], [0, sqrt(p)]]
    K1 = Matrix([[sqrt(p), 0], [0, sqrt(q)]])
    K2 = Matrix([[sqrt(q), 0], [0, sqrt(p)]])
    kraus = [K1, K2]
    verify_resolution_of_identity(kraus, "T5.a")
    verify_stinespring_isometry(kraus, "T5.b")


# --------------------------------------------------------------------------
# Test 6 — Continuous family parametrized by lambda, V^dagger V = 1 for all
# --------------------------------------------------------------------------

def test_continuous_family():
    """Parametrized one-parameter family K_r(lambda), check V^dagger V = 1 holds for all lambda."""
    print("\n[T6] Continuous parametric family lambda in [0, 1]")
    # Use real positive lam in (0, 1), and a second real positive symbol for 1-lam
    # to keep sympy's conjugate from re-introducing it
    lam = Symbol('lam', positive=True, real=True)
    one_minus_lam = Symbol('mu', positive=True, real=True)  # mu := 1 - lam, treated independently
    # K_1 = sqrt(lam) * I, K_2 = sqrt(mu) * I; constraint lam + mu = 1 imposed at verification
    K1 = sqrt(lam) * eye(2)
    K2 = sqrt(one_minus_lam) * eye(2)
    kraus = [K1, K2]
    # Check Sigma_r K_r^dagger K_r = (lam + mu) * I; with mu = 1 - lam this gives I
    d = 2
    accum = zeros(d, d)
    for Kr in kraus:
        accum = accum + Kr.H * Kr
    # Substitute mu -> 1 - lam to enforce the constraint
    accum_constrained = accum.subs(one_minus_lam, 1 - lam)
    accum_simplified = simplify(accum_constrained)
    diff = simplify(accum_simplified - eye(d))
    is_zero = all(diff[i, j] == 0 for i in range(d) for j in range(d))
    _report(
        "T6.a (parametric in lambda, with mu = 1 - lam constraint): "
        "Sigma_r K_r^dagger K_r = 1_sys (symbolic)",
        is_zero,
        "" if is_zero else f"residual = {diff}",
    )
    # Same for V^dagger V
    V = build_stinespring_isometry(kraus)
    VdagV = simplify(V.H * V).subs(one_minus_lam, 1 - lam)
    VdagV_simp = simplify(VdagV)
    diff2 = simplify(VdagV_simp - eye(d))
    is_zero2 = all(diff2[i, j] == 0 for i in range(d) for j in range(d))
    _report(
        "T6.b (parametric in lambda, with mu = 1 - lam constraint): "
        "V^dagger V = 1_sys (explicit block matrix)",
        is_zero2,
        "" if is_zero2 else f"residual = {diff2}",
    )
    # K_r^dagger K_r is positive semidefinite for the parameter range
    K1dK1 = simplify(K1.H * K1)
    expected = lam * eye(2)
    ok = all(simplify(K1dK1[i, j] - expected[i, j]) == 0 for i in range(2) for j in range(2))
    _report("T6.c: K_1^dagger K_1 = lam * I (analytic check)", ok)


# --------------------------------------------------------------------------
# Test 7 — Numerical sanity: <V psi | V psi> = <psi | psi> for random states
# --------------------------------------------------------------------------

def test_numerical_isometry():
    """Numerical check: for random complex |psi>, ||V|psi>||^2 = |||psi>||^2."""
    print("\n[T7] Numerical isometry check on random states (5 trials, 3 instrument families)")
    # T1 instrument: projective sigma_z
    P0_np = np.array([[1.0, 0.0], [0.0, 0.0]])
    P1_np = np.array([[0.0, 0.0], [0.0, 1.0]])
    V_T1 = np.vstack([P0_np, P1_np])  # (4, 2)
    # T4-style instrument numerical: Bell basis on 2 qubits
    sq2 = np.sqrt(2.0)
    phi_p = np.array([1.0, 0.0, 0.0, 1.0]) / sq2
    phi_m = np.array([1.0, 0.0, 0.0, -1.0]) / sq2
    psi_p = np.array([0.0, 1.0, 1.0, 0.0]) / sq2
    psi_m = np.array([0.0, 1.0, -1.0, 0.0]) / sq2
    Bell_K = [np.outer(k, k) for k in [phi_p, phi_m, psi_p, psi_m]]
    V_T4 = np.vstack(Bell_K)  # (16, 4)
    # T5 biased POVM
    p = 1.0/3.0; q = 2.0/3.0
    K1_T5 = np.diag([np.sqrt(p), np.sqrt(q)])
    K2_T5 = np.diag([np.sqrt(q), np.sqrt(p)])
    V_T5 = np.vstack([K1_T5, K2_T5])  # (4, 2)

    rng = np.random.default_rng(seed=20260522)
    all_pass = True
    for trial in range(5):
        # Random 2-dim complex state for T1, T5
        psi2 = rng.standard_normal(2) + 1j * rng.standard_normal(2)
        psi2 /= np.linalg.norm(psi2)
        # Random 4-dim complex state for T4
        psi4 = rng.standard_normal(4) + 1j * rng.standard_normal(4)
        psi4 /= np.linalg.norm(psi4)
        # ||V|psi>||^2 vs |||psi>||^2 for each
        for label, V_np, psi in [
            (f"T7.{trial}.T1", V_T1, psi2),
            (f"T7.{trial}.T4", V_T4, psi4),
            (f"T7.{trial}.T5", V_T5, psi2),
        ]:
            V_psi = V_np @ psi
            norm_V_psi = np.abs(V_psi @ V_psi.conj())
            norm_psi = np.abs(psi @ psi.conj())
            ok = np.isclose(norm_V_psi, norm_psi, rtol=1e-12, atol=1e-12)
            if not ok:
                all_pass = False
                _report(label, False, f"||V psi||^2 = {norm_V_psi}, ||psi||^2 = {norm_psi}")
    if all_pass:
        _report("T7: 15 random states (3 instruments x 5 trials): ||V|psi>||^2 = |||psi>||^2", True)


# --------------------------------------------------------------------------
# Test 8 — Source-note boundary string checks
# --------------------------------------------------------------------------

def test_source_boundary_strings():
    """Check the note's source-side boundary declarations are present.

    Protects against accidental promotion language or missing scope
    declarations.
    """
    print("\n[T8] Source-note boundary string checks")
    note_path = Path(__file__).resolve().parent.parent / "docs" / (
        "PERSISTENT_RECORD_INSTRUMENT_CONSTRUCTION_NARROW_THEOREM_NOTE_2026-05-22.md"
    )
    if not note_path.exists():
        _report("T8.a: source note exists", False, f"not found: {note_path}")
        return
    text = note_path.read_text()
    required_strings = [
        "source-side proposal",
        "independent audit lane owns the verdict",
        "Status authority",
        "does not by itself",
    ]
    forbidden_strings = [
        "Status: retained",
        "Status: promoted",
        "we have retained",
        "this PR retains",
    ]
    for s in required_strings:
        present = s in text
        _report(f"T8.required: '{s}'", present)
    for s in forbidden_strings:
        absent = s not in text
        _report(f"T8.forbidden-absent: '{s}'", absent)


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

def main():
    print("=" * 70)
    print("Persistent-record instrument construction (Stinespring V) runner")
    print("=" * 70)
    print()
    print("Verifies the Stinespring isometry V: H_sys -> H_record (x) H_sys")
    print("for multiple framework-side measurement-instrument families on the")
    print("qubit-lattice substrate. Total probability preservation V^dagger V = 1")
    print("is checked by explicit block-matrix algebra, NOT inherited from")
    print("standard QM.")
    print()
    test_single_qubit_projective_z()
    test_single_qubit_projective_rotated()
    test_single_qubit_three_outcome_povm()
    test_two_qubit_bell_measurement()
    test_biased_povm()
    test_continuous_family()
    test_numerical_isometry()
    test_source_boundary_strings()
    print()
    print("=" * 70)
    print(f"PASS={PASS} FAIL={FAIL}")
    print("=" * 70)
    sys.exit(0 if FAIL == 0 else 1)


if __name__ == "__main__":
    main()
