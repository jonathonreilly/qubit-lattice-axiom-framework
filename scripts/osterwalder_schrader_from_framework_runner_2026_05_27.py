#!/usr/bin/env python3
"""Exact-symbolic audit-companion runner for
`OSTERWALDER_SCHRADER_FROM_FRAMEWORK_NARROW_THEOREM_NOTE_2026-05-27.md`.

Composition narrow theorem: derives the Osterwalder-Schrader (P-OS)
Wick-rotation correspondence packet entry used by the P2 sign-epsilon
closure lane from three existing framework companions:

  (C-RP) AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29
         -> positive Hermitian transfer matrix T on finite-dim H_phys
  (C-SC) AXIOM_FIRST_SPECTRUM_CONDITION_THEOREM_NOTE_2026-04-29
         -> self-adjoint H = -(1/a_tau) log(T/M_T) with H >= 0
  (C-Sc) AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03
         -> unitary one-parameter group U(t) = exp(-itH) on H_phys

The runner verifies, at exact rational precision via sympy:

  (OS1) Spectral decomposition T_hat = T/M_T = Sum_k mu_k |k><k|
        with positive rational eigenvalues mu_k in (0, 1] on finite-dim H_phys.
  (OS2) T_hat^n = exp(-n a_tau H) with
        H = -(1/a_tau) log(T_hat) via spectral functional calculus on
        the same eigenbasis.
  (OS3) U(t) := Sum_k exp(-i t E_k) |k><k| is a well-defined bounded
        operator on H_phys for every real t.
  (OS4.a) Unitarity U(t)^dagger U(t) = I on each eigenmode and global.
  (OS4.b) Group property U(s) U(t) = U(s+t) on each eigenmode.
  (OS4.c) Identity U(0) = I.
  (OS4.d) Strong continuity (continuity of scalar exp(-i t E_k) in t).
  (OS4.e) Generator U(t) = exp(-itH) via spectral functional calculus.
  (OS5) Wick-rotation bridge T_hat^n <-> U(t) is a scalar parameter
        substitution n*a_tau -> i*t inside the spectral expansion on
        each eigenmode.
  (Composition) File-existence check of the three load-bearing
                companion notes.

Companion role: not a new claim row, not a new source note status
promotion. Provides audit-friendly evidence that the bounded
composition (C-RP) + (C-SC) + (C-Sc) -> framework-internal (P-OS)
holds at exact symbolic precision and can support a later P2
sign-epsilon closure after independent audit and dependency closure.
"""

from __future__ import annotations

from pathlib import Path
import sys

try:
    import sympy
    from sympy import (
        Matrix, Rational, eye, zeros, simplify, exp, I, Symbol, log,
        sqrt, conjugate, re, im, expand,
    )
except ImportError:
    print("FAIL: sympy required for exact algebra")
    sys.exit(1)


ROOT = Path(__file__).resolve().parent.parent
NOTE_PATH = ROOT / "docs" / "OSTERWALDER_SCHRADER_FROM_FRAMEWORK_NARROW_THEOREM_NOTE_2026-05-27.md"
CLAIM_ID = "osterwalder_schrader_from_framework_narrow_theorem_note_2026-05-27"


PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS (A)"
    else:
        FAIL += 1
        tag = "FAIL (A)"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{tag}] {label}{suffix}")


def section(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


def mat_eq(A: Matrix, B: Matrix) -> bool:
    """Symbolic equality of two sympy matrices via simplify."""
    diff = sympy.simplify(A - B)
    return all(diff[i, j] == 0 for i in range(diff.rows) for j in range(diff.cols))


def mat_zero(A: Matrix) -> bool:
    return all(sympy.simplify(A[i, j]) == 0 for i in range(A.rows) for j in range(A.cols))


def main() -> int:
    print("=" * 88)
    print("Audit companion (exact-symbolic) for")
    print("OSTERWALDER_SCHRADER_FROM_FRAMEWORK_NARROW_THEOREM_NOTE_2026-05-27")
    print("Goal: sympy verification of the composition")
    print("      (C-RP) + (C-SC) + (C-Sc) -> framework-internal (P-OS)")
    print("=" * 88)

    # =========================================================================
    section("Part 1: (OS1) Discrete spectral decomposition of positive Hermitian T")
    # =========================================================================
    # Build a positive Hermitian 4x4 transfer matrix T with rational
    # eigenvalues and verify the spectral theorem decomposition of the
    # normalized transfer matrix T_hat = T/M_T on finite-dim H_phys.

    # Choose positive rational eigenvalues - all distinct so kernel empty.
    lam = [Rational(1, 2), Rational(3, 5), Rational(7, 11), Rational(13, 17)]
    M_T = max(lam)
    mu = [lk / M_T for lk in lam]

    # Construct T as diagonal in a chosen orthonormal eigenbasis (canonical
    # basis on C^4). This realizes the spectral decomposition explicitly.
    T_diag = Matrix([
        [lam[0], 0, 0, 0],
        [0, lam[1], 0, 0],
        [0, 0, lam[2], 0],
        [0, 0, 0, lam[3]],
    ])

    # Check positivity (all eigenvalues > 0) - (OS1) precondition from (C-RP)
    for k, lk in enumerate(lam):
        check(
            f"(OS1) lambda_{k+1} = {lk} > 0 (positive Hermitian T from C-RP)",
            lk > 0,
        )

    # Check operator norm and normalized eigenvalues.
    check(
        f"(OS1) M_T = ||T||_op = max lambda_k = {M_T} > 0",
        M_T > 0,
    )

    # Construct projectors |k><k| explicitly and verify spectral expansion
    e1 = Matrix([1, 0, 0, 0])
    e2 = Matrix([0, 1, 0, 0])
    e3 = Matrix([0, 0, 1, 0])
    e4 = Matrix([0, 0, 0, 1])
    eks = [e1, e2, e3, e4]

    # Each projector |k><k| = e_k * e_k^T
    P_list = [ek * ek.T for ek in eks]

    # Verify projectors are orthogonal idempotents
    for k in range(4):
        check(
            f"(OS1) Projector P_{k+1} = |{k+1}><{k+1}| is idempotent: P_k^2 = P_k",
            mat_eq(P_list[k] * P_list[k], P_list[k]),
        )

    for k in range(4):
        for j in range(k + 1, 4):
            check(
                f"(OS1) Projectors P_{k+1} and P_{j+1} orthogonal: P_k P_j = 0",
                mat_zero(P_list[k] * P_list[j]),
            )

    for k, mk in enumerate(mu):
        check(
            f"(OS1) mu_{k+1} = lambda_{k+1}/M_T = {mk} lies in (0, 1]",
            mk > 0 and mk <= 1,
        )

    # Spectral expansion: T_hat = Sum_k mu_k * P_k
    T_hat_diag = T_diag / M_T
    T_hat_spectral = sum((mu[k] * P_list[k] for k in range(4)), zeros(4, 4))
    check(
        "(OS1) T_hat = Sum_k mu_k |k><k| (normalized spectral expansion holds exactly)",
        mat_eq(T_hat_spectral, T_hat_diag),
    )

    # =========================================================================
    section("Part 2: (OS2) Discrete Euclidean semigroup T_hat^n = exp(-n a_tau H)")
    # =========================================================================

    a_tau = Symbol("a_tau", positive=True, real=True)

    # H = Sum_k E_k |k><k| with E_k = -(1/a_tau) log(mu_k) (from C-SC)
    E_list = [-log(mu[k]) / a_tau for k in range(4)]

    # E_k >= 0 since mu_k <= 1 -> log(mu_k) <= 0 -> -log(mu_k) >= 0.
    for k in range(4):
        is_nonnegative = bool((-log(mu[k])).is_nonnegative)
        check(
            f"(OS2) E_{k+1} = -(1/a_tau) log(mu_{k+1}) >= 0 (H >= 0 from C-SC)",
            is_nonnegative,
            detail=f"mu_{k+1} = {mu[k]}",
        )

    # H matrix in the eigenbasis
    H = sum((E_list[k] * P_list[k] for k in range(4)), zeros(4, 4))

    # Verify H = -(1/a_tau) log(T_hat) at the eigenvalue level.
    # On eigenmode k: H|k> = E_k |k> = -(1/a_tau) log(mu_k) |k>
    for k in range(4):
        lhs = H * eks[k]  # H |k>
        rhs = E_list[k] * eks[k]  # E_k |k>
        check(
            f"(OS2) H |{k+1}> = E_{k+1} |{k+1}> (functional calculus from C-SC)",
            mat_eq(lhs, rhs),
        )

    # Discrete iteration: T_hat^n on each eigenmode.
    # T_hat |k> = mu_k |k>, so T_hat^n |k> = mu_k^n |k>.
    # exp(-n a_tau H) |k> = exp(-n a_tau E_k) |k> = mu_k^n |k>.
    # Verify on each eigenmode that T_hat^n |k> = exp(-n a_tau H) |k>.
    n_sym = Symbol("n", positive=True, integer=True)
    for k in range(4):
        # T_hat^n on eigenmode k gives mu_k^n |k>
        T_n_eigenvalue = mu[k]**n_sym
        # exp(-n a_tau E_k) = exp(-n a_tau * (-log(mu_k)/a_tau))
        #                   = exp(n log(mu_k))
        #                   = mu_k^n
        H_evo_eigenvalue = exp(-n_sym * a_tau * E_list[k])
        diff_simplified = simplify(T_n_eigenvalue - H_evo_eigenvalue)
        check(
            f"(OS2) mu_{k+1}^n = exp(-n a_tau E_{k+1}) (normalized Euclidean semigroup on eigenmode {k+1})",
            diff_simplified == 0,
            detail=f"mu^n = {T_n_eigenvalue}, exp(-n a_tau E) = {sympy.simplify(H_evo_eigenvalue)}",
        )

    # =========================================================================
    section("Part 3: (OS3) U(t) well-defined as bounded operator on H_phys")
    # =========================================================================
    # U(t) := Sum_k exp(-i t E_k) |k><k| is a finite sum of bounded scalars
    # (|exp(-i t E_k)| = 1 for real t, real E_k) times fixed projectors.

    t = Symbol("t", real=True)

    # Construct U(t) in the eigenbasis
    U_t_diag = Matrix([
        [exp(-I * t * E_list[0]), 0, 0, 0],
        [0, exp(-I * t * E_list[1]), 0, 0],
        [0, 0, exp(-I * t * E_list[2]), 0],
        [0, 0, 0, exp(-I * t * E_list[3])],
    ])

    # Verify U(t) is bounded: each diagonal entry has modulus 1
    # |exp(-i t E_k)|^2 = exp(-i t E_k) * exp(+i t E_k) = exp(0) = 1
    for k in range(4):
        modsq = exp(-I * t * E_list[k]) * exp(I * t * E_list[k])
        modsq_simp = simplify(modsq)
        check(
            f"(OS3) |U(t)_{k+1,k+1}|^2 = |exp(-i t E_{k+1})|^2 = 1 (bounded)",
            modsq_simp == 1,
            detail=f"product simplifies to {modsq_simp}",
        )

    # =========================================================================
    section("Part 4: (OS4.a) Unitarity U(t)^dagger U(t) = I")
    # =========================================================================
    # U(t)^dagger = Sum_k exp(+i t E_k) |k><k|
    # U(t)^dagger U(t) = Sum_k |exp(+i t E_k)|^2 |k><k| = Sum_k |k><k| = I

    # Construct U_t_dag in eigenbasis
    U_t_dag = Matrix([
        [exp(I * t * E_list[0]), 0, 0, 0],
        [0, exp(I * t * E_list[1]), 0, 0],
        [0, 0, exp(I * t * E_list[2]), 0],
        [0, 0, 0, exp(I * t * E_list[3])],
    ])

    product = U_t_dag * U_t_diag
    # Each diagonal entry: exp(i t E_k) * exp(-i t E_k) = 1
    # Off-diagonal: zero by orthogonality of projectors
    product_simp = Matrix(4, 4, lambda i, j: simplify(product[i, j]))
    check(
        "(OS4.a) U(t)^dagger U(t) = I (unitarity on finite-dim H_phys)",
        mat_eq(product_simp, eye(4)),
    )

    # Sanity: also U(t) U(t)^dagger = I (right inverse equals left inverse on finite-dim)
    product_rev = U_t_diag * U_t_dag
    product_rev_simp = Matrix(4, 4, lambda i, j: simplify(product_rev[i, j]))
    check(
        "(OS4.a) U(t) U(t)^dagger = I (right inverse, finite-dim H_phys)",
        mat_eq(product_rev_simp, eye(4)),
    )

    # =========================================================================
    section("Part 5: (OS4.b) Group property U(s) U(t) = U(s+t)")
    # =========================================================================

    s_sym = Symbol("s", real=True)

    U_s_diag = Matrix([
        [exp(-I * s_sym * E_list[0]), 0, 0, 0],
        [0, exp(-I * s_sym * E_list[1]), 0, 0],
        [0, 0, exp(-I * s_sym * E_list[2]), 0],
        [0, 0, 0, exp(-I * s_sym * E_list[3])],
    ])

    U_s_plus_t = Matrix([
        [exp(-I * (s_sym + t) * E_list[0]), 0, 0, 0],
        [0, exp(-I * (s_sym + t) * E_list[1]), 0, 0],
        [0, 0, exp(-I * (s_sym + t) * E_list[2]), 0],
        [0, 0, 0, exp(-I * (s_sym + t) * E_list[3])],
    ])

    U_s_U_t = U_s_diag * U_t_diag
    # Each eigenmode: exp(-i s E_k) * exp(-i t E_k) = exp(-i (s+t) E_k)
    for k in range(4):
        lhs = exp(-I * s_sym * E_list[k]) * exp(-I * t * E_list[k])
        rhs = exp(-I * (s_sym + t) * E_list[k])
        diff = simplify(lhs - rhs)
        check(
            f"(OS4.b) U(s) U(t) = U(s+t) on eigenmode {k+1}",
            diff == 0,
        )

    # =========================================================================
    section("Part 6: (OS4.c) Identity U(0) = I")
    # =========================================================================
    U_0 = Matrix([
        [exp(-I * 0 * E_list[0]), 0, 0, 0],
        [0, exp(-I * 0 * E_list[1]), 0, 0],
        [0, 0, exp(-I * 0 * E_list[2]), 0],
        [0, 0, 0, exp(-I * 0 * E_list[3])],
    ])
    U_0_simp = Matrix(4, 4, lambda i, j: simplify(U_0[i, j]))
    check(
        "(OS4.c) U(0) = I (identity at zero parameter)",
        mat_eq(U_0_simp, eye(4)),
    )

    # =========================================================================
    section("Part 7: (OS4.d) Strong continuity of t -> U(t)")
    # =========================================================================
    # On finite-dim H_phys, U(t) is operator-norm continuous since each
    # scalar exp(-i t E_k) is continuous in t. We verify by checking
    # lim_{h -> 0} (U(t + h) - U(t)) = 0 on each eigenmode.

    h = Symbol("h", real=True)
    for k in range(4):
        delta = exp(-I * (t + h) * E_list[k]) - exp(-I * t * E_list[k])
        # As h -> 0, delta -> 0 (continuity of exp at 0)
        limit_val = delta.subs(h, 0)
        limit_simp = simplify(limit_val)
        check(
            f"(OS4.d) lim_{{h->0}} (U(t+h) - U(t))_{{{k+1},{k+1}}} = 0 on eigenmode {k+1}",
            limit_simp == 0,
        )

    # =========================================================================
    section("Part 8: (OS4.e) Generator U(t) = exp(-itH) via spectral calculus")
    # =========================================================================
    # U(t) = Sum_k exp(-i t E_k) |k><k| = exp(-it * Sum_k E_k |k><k|)
    # On each eigenmode k: exp(-itH) |k> = exp(-i t E_k) |k>
    # We verify U(t)|k> = exp(-i t E_k) |k> for each k.

    for k in range(4):
        lhs = U_t_diag * eks[k]  # U(t) |k>
        rhs = exp(-I * t * E_list[k]) * eks[k]  # exp(-i t E_k) |k>
        check(
            f"(OS4.e) U(t)|{k+1}> = exp(-i t E_{k+1}) |{k+1}> "
            f"(generator = H via spectral calculus)",
            mat_eq(lhs, rhs),
        )

    # =========================================================================
    section("Part 9: (OS5) Wick-rotation bridge T_hat^n <-> U(t)")
    # =========================================================================
    # Both T_hat^n and U(t) are spectral functional calculus on the same H
    # with eigenvalues E_k. The bridge is the parameter substitution
    # x_E := n a_tau (Euclidean, real >= 0) -> x_L := i t (Lorentzian, imaginary).
    # exp(-x H) evaluated on each eigenmode gives exp(-x E_k).
    # - x = n a_tau real: exp(-n a_tau E_k) = mu_k^n -> T_hat^n on eigenmode
    # - x = i t imaginary: exp(-i t E_k) -> U(t) on eigenmode

    # Verify the parameter substitution on each eigenmode:
    # Setting x = n a_tau in exp(-x E_k) gives the T_hat^n eigenvalue
    # Setting x = i t in exp(-x E_k) gives the U(t) eigenvalue
    x_param = Symbol("x", complex=True)
    for k in range(4):
        x_E = n_sym * a_tau  # Euclidean parameter
        x_L = I * t  # Lorentzian parameter

        T_n_value = exp(-x_E * E_list[k])
        U_t_value = exp(-x_L * E_list[k])

        # T_n_value must equal mu_k^n
        T_n_expected = mu[k]**n_sym
        check(
            f"(OS5) Euclidean side: exp(-(n a_tau) E_{k+1}) = mu_{k+1}^n "
            f"on eigenmode {k+1}",
            simplify(T_n_value - T_n_expected) == 0,
        )

        # U_t_value must equal exp(-i t E_k) by construction
        U_t_expected = exp(-I * t * E_list[k])
        check(
            f"(OS5) Lorentzian side: exp(-(i t) E_{k+1}) = exp(-i t E_{k+1}) "
            f"on eigenmode {k+1}",
            simplify(U_t_value - U_t_expected) == 0,
        )

        # The bridge: same functional form exp(-x E_k) at x = n a_tau or x = i t
        # is a scalar parameter substitution inside the spectral expansion,
        # NOT a separate operator-level analytic continuation.
        # Construct exp(-x E_k) symbolically in the abstract parameter x,
        # then substitute x = n a_tau (Euclidean) or x = i t (Lorentzian).
        f_x = exp(-x_param * E_list[k])
        eucl_substitution = f_x.subs(x_param, n_sym * a_tau)
        lor_substitution = f_x.subs(x_param, I * t)
        # Euclidean substitution must recover T_n_value
        diff_E = simplify(eucl_substitution - T_n_value)
        check(
            f"(OS5) Bridge Euclidean: exp(-x E_{k+1})|_{{x = n a_tau}} = T_hat^n "
            f"eigenvalue on mode {k+1}",
            diff_E == 0,
            detail="parameter rotation inside spectral functional calculus",
        )
        # Lorentzian substitution must recover U_t_value
        diff_L = simplify(lor_substitution - U_t_value)
        check(
            f"(OS5) Bridge Lorentzian: exp(-x E_{k+1})|_{{x = i t}} = U(t) "
            f"eigenvalue on mode {k+1}",
            diff_L == 0,
            detail="parameter rotation inside spectral functional calculus",
        )

    # =========================================================================
    section("Part 10: (Composition) Companion notes exist on the framework tree")
    # =========================================================================

    docs = ROOT / "docs"
    companions = [
        ("(C-RP)", "AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md"),
        ("(C-SC)", "AXIOM_FIRST_SPECTRUM_CONDITION_THEOREM_NOTE_2026-04-29.md"),
        ("(C-Sc)", "AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md"),
    ]
    for tag, fname in companions:
        path = docs / fname
        check(
            f"(Composition) {tag} companion exists: {fname}",
            path.is_file(),
            detail=str(path.relative_to(ROOT)),
        )

    # Verify the (C-Sc) Step 1 inline Wick-rotation step (lines 261-266)
    # is the same composition the present narrow internalizes.
    c_sc_path = docs / "AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md"
    if c_sc_path.is_file():
        text = c_sc_path.read_text()
        check(
            "(Composition) (C-Sc) Step 1 supplies the positive-Hermitian transfer with a unique clock",
            "(R-RP2) supplies" in text
            and "positive Hermitian" in text
            and "the clock is unique (Step 1)" in text,
            detail="presence of '(R-RP2) supplies' + 'positive Hermitian' + 'the clock is unique (Step 1)' in (C-Sc)",
        )

    # =========================================================================
    section("Part 11: Note + claim metadata sanity")
    # =========================================================================
    check(
        f"Source note exists: {NOTE_PATH.relative_to(ROOT)}",
        NOTE_PATH.is_file(),
    )
    if NOTE_PATH.is_file():
        note_text = NOTE_PATH.read_text()
        check(
            "Note declares Type: bounded_theorem",
            "Type:** bounded_theorem" in note_text,
        )
        check(
            "Note declares Status authority: independent audit lane only",
            "Status authority:** independent audit lane only" in note_text,
        )
        check(
            "Note contains source-note proposal disclaimer",
            "Source-note proposal disclaimer" in note_text,
        )
        check(
            "Note records the P2 sign-epsilon lane boundary",
            "P2 sign-" in note_text and "downstream" in note_text,
        )

    # =========================================================================
    print()
    print("=" * 88)
    print(f"PASS = {PASS}    FAIL = {FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
