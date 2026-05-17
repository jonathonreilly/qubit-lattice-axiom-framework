#!/usr/bin/env python3
"""Exact-symbolic audit-companion runner for the RH-completion-to-3bar
cubic anomaly index mapping narrow theorem.

Parent narrow note:
  docs/RH_COMPLETION_COLOR_ANTI_FUNDAMENTAL_NARROW_THEOREM_NOTE_2026-05-17.md

The parent narrow note's load-bearing content is the algebraic Lie-algebra
identity that, given the retained Gell-Mann SU(3) carrier of
`cl3_color_automorphism_theorem` and the retained anticommutator
decomposition `{T^a, T^b} = (1/3) delta_ab I + d^{abc} T^c` of
`su3_dabc_symmetric_theorem_note_2026-05-02`, the cubic anomaly index of
the complex-conjugate representation R̄ satisfies

  (M2)  A(R̄)  =  -A(R)              [pure Lie-algebra identity]
  (M3)  A(3̄)  =  -A(3)  =  -1       [specialization at fundamental]
  (M4)  2 · A(3̄)  =  -2             [two-fermion contribution]

This audit-companion runner verifies these identities at exact sympy
precision on the explicit Gell-Mann fundamental representation
T^a = lambda^a / 2 (Hermitian, 3x3, standard SU(3)), and additionally
cross-checks the result at multiple distinct nonzero d-triples and on the
adjoint and 6 representations as counterfactual/consistency probes.

Companion role: not a new claim row, not a new source note, no status
promotion. Provides audit-friendly evidence that the parent's
load-bearing class-A algebra holds at exact symbolic precision under the
cited retained SU(3) inputs. The cited Gell-Mann carrier and d^{abc}
decomposition themselves are imported from upstream retained authorities
and are not re-derived here.

Run:
  python3 scripts/audit_companion_rh_completion_color_anti_fundamental_exact_2026_05_17.py
"""

from __future__ import annotations

import sys

try:
    import sympy
    from sympy import (
        I,
        Matrix,
        Rational,
        conjugate,
        eye,
        sqrt,
        symbols,
        zeros,
    )
except ImportError:
    print("FAIL: sympy required for exact algebra")
    sys.exit(1)


PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{tag}] {label}{suffix}")


def section(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


def gell_mann_matrices():
    """Standard Gell-Mann matrices lambda^1 .. lambda^8 (exact rationals
    and sqrt(3) extension)."""
    L = [None] * 9  # 1-indexed
    L[1] = Matrix(
        [
            [0, 1, 0],
            [1, 0, 0],
            [0, 0, 0],
        ]
    )
    L[2] = Matrix(
        [
            [0, -I, 0],
            [I, 0, 0],
            [0, 0, 0],
        ]
    )
    L[3] = Matrix(
        [
            [1, 0, 0],
            [0, -1, 0],
            [0, 0, 0],
        ]
    )
    L[4] = Matrix(
        [
            [0, 0, 1],
            [0, 0, 0],
            [1, 0, 0],
        ]
    )
    L[5] = Matrix(
        [
            [0, 0, -I],
            [0, 0, 0],
            [I, 0, 0],
        ]
    )
    L[6] = Matrix(
        [
            [0, 0, 0],
            [0, 0, 1],
            [0, 1, 0],
        ]
    )
    L[7] = Matrix(
        [
            [0, 0, 0],
            [0, 0, -I],
            [0, I, 0],
        ]
    )
    L[8] = (Rational(1, 1) / sqrt(3)) * Matrix(
        [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, -2],
        ]
    )
    return L


def hermitian_conjugate(M: Matrix) -> Matrix:
    return M.H


def anticommutator(A: Matrix, B: Matrix) -> Matrix:
    return A * B + B * A


def commutator(A: Matrix, B: Matrix) -> Matrix:
    return A * B - B * A


def conj_mat(M: Matrix) -> Matrix:
    """Componentwise complex conjugate (no transpose)."""
    return M.applyfunc(conjugate)


def f_symbol(T_a: Matrix, T_b: Matrix, T_c: Matrix) -> sympy.Expr:
    """Compute f^{abc} from the bracket relation [T^a, T^b] = i f^{abc} T^c.

    Use: f^{abc} = -2 * I * Tr([T^a, T^b] · T^c) using
      Tr(T^c T^c') = (1/2) delta_{c c'}, so the projection onto T^c is
      2 · Tr([T^a, T^b] · T^c).
    Then divide by I (from the relation [T^a, T^b] = i f^{abc} T^c) to get
    f^{abc} = -2*I * Tr([T^a, T^b] · T^c).
    """
    return sympy.simplify(-2 * I * sympy.trace(commutator(T_a, T_b) * T_c))


def d_symbol(T_a: Matrix, T_b: Matrix, T_c: Matrix) -> sympy.Expr:
    """Compute d^{abc} from the anticommutator decomposition
    {T^a, T^b} = (1/3) delta_ab I + d^{abc} T^c.

    Use: d^{abc} = 2 * Tr({T^a, T^b} · T^c).
    """
    return sympy.simplify(2 * sympy.trace(anticommutator(T_a, T_b) * T_c))


def cubic_anomaly_trace(T_a: Matrix, T_b: Matrix, T_c: Matrix) -> sympy.Expr:
    """Compute Tr[T^a {T^b, T^c}], the load-bearing cubic anomaly trace."""
    return sympy.simplify(sympy.trace(T_a * anticommutator(T_b, T_c)))


def adjoint_generators():
    """Build the adjoint SU(3) generators (T^a_8)^{bc} = -i f^{abc}.

    For diagnostics: this gives an 8x8 generator matrix for each a; we
    verify A(adjoint) = 0 by direct trace evaluation.
    """
    L = gell_mann_matrices()
    T = [L[a] / 2 for a in range(1, 9)]  # T[0] = T^1, ..., T[7] = T^8

    # Compute f^{abc} table
    f_table = {}
    for a in range(8):
        for b in range(8):
            for c in range(8):
                val = sympy.simplify(
                    -2 * I * sympy.trace(commutator(T[a], T[b]) * T[c])
                )
                if val != 0:
                    f_table[(a, b, c)] = val

    # Build adjoint generators: (T^a_adj)^{bc} = -i f^{abc}
    T_adj = []
    for a in range(8):
        M = zeros(8, 8)
        for b in range(8):
            for c in range(8):
                M[b, c] = -I * f_table.get((a, b, c), 0)
        T_adj.append(M)
    return T_adj


def build_6_rep_generators(T_fund):
    """Build the SU(3) generators on the symmetric tensor square 6 = Sym^2(3).

    Basis ordering for the 6-dim sym^2(C^3):
      e_{11}, e_{22}, e_{33}, (e_{12}+e_{21})/sqrt(2), (e_{13}+e_{31})/sqrt(2),
      (e_{23}+e_{32})/sqrt(2)

    For an SU(3) generator T acting on C^3, the induced action on Sym^2(C^3)
    is given by T_sym(v . w) = (T v) . w + v . (T w) where v . w denotes the
    symmetric product. We construct T_sym in the orthonormal basis above.
    """
    # Basis vectors of C^3:
    # e1 = (1,0,0), e2 = (0,1,0), e3 = (0,0,1)
    # Sym^2 basis:
    #  s1 = e1 ⊗_s e1 = e_{11}
    #  s2 = e2 ⊗_s e2 = e_{22}
    #  s3 = e3 ⊗_s e3 = e_{33}
    #  s4 = (e1 ⊗_s e2 + e2 ⊗_s e1)/sqrt(2) = (e_{12} + e_{21})/sqrt(2)
    #  s5 = (e1 ⊗_s e3 + e3 ⊗_s e1)/sqrt(2)
    #  s6 = (e2 ⊗_s e3 + e3 ⊗_s e2)/sqrt(2)
    #
    # Equivalently, in 9x9 representation on C^3 ⊗ C^3, then project to sym
    # subspace and orthonormalize.

    # Build basis vectors of Sym^2(C^3) as 9-vectors in C^3 ⊗ C^3:
    def e(i):
        v = zeros(3, 1)
        v[i, 0] = 1
        return v

    def kron(v, w):
        return v.col_join(zeros(0, 1))  # placeholder, will use sympy.kronecker_product

    s = [None] * 6  # 1-indexed s[1] .. s[6]
    # 1-D blocks
    s[0] = sympy.Matrix(sympy.kronecker_product(e(0), e(0)))
    s[1] = sympy.Matrix(sympy.kronecker_product(e(1), e(1)))
    s[2] = sympy.Matrix(sympy.kronecker_product(e(2), e(2)))
    # off-diagonal blocks
    s[3] = (
        sympy.Matrix(sympy.kronecker_product(e(0), e(1)))
        + sympy.Matrix(sympy.kronecker_product(e(1), e(0)))
    ) / sqrt(2)
    s[4] = (
        sympy.Matrix(sympy.kronecker_product(e(0), e(2)))
        + sympy.Matrix(sympy.kronecker_product(e(2), e(0)))
    ) / sqrt(2)
    s[5] = (
        sympy.Matrix(sympy.kronecker_product(e(1), e(2)))
        + sympy.Matrix(sympy.kronecker_product(e(2), e(1)))
    ) / sqrt(2)

    # Build the 9x6 matrix V whose columns are s[i] (so x = V c is the embedding
    # of c in C^3 ⊗ C^3).
    V = sympy.Matrix.hstack(*s)
    # T_sym = V^† (T ⊗ I + I ⊗ T) V acts on the 6-dim Sym^2 space.

    T_sym_list = []
    for T in T_fund:
        TxI = sympy.Matrix(sympy.kronecker_product(T, sympy.eye(3)))
        IxT = sympy.Matrix(sympy.kronecker_product(sympy.eye(3), T))
        T_total = TxI + IxT
        T_sym = sympy.simplify(V.H * T_total * V)
        T_sym_list.append(T_sym)

    return T_sym_list


def main() -> int:
    print("=" * 88)
    print("Audit companion (exact-symbolic) for")
    print("RH_COMPLETION_COLOR_ANTI_FUNDAMENTAL_NARROW_THEOREM_NOTE_2026-05-17")
    print("Goal: sympy-symbolic verification of (M1)-(M4):")
    print("  A(R̄) = -A(R) on unitary SU(3) reps, specialized to A(3̄) = -1.")
    print("=" * 88)

    # ---------------------------------------------------------------------
    section("Part 0: cited Gell-Mann fundamental generators T^a = lambda^a / 2")
    # ---------------------------------------------------------------------
    L = gell_mann_matrices()
    # Generators T^a := lambda^a / 2 (Hermitian, 3x3)
    T = [None] + [L[a] / 2 for a in range(1, 9)]  # T[1] .. T[8]

    # Verify Hermiticity:
    all_herm = all(sympy.simplify(T[a] - T[a].H) == zeros(3, 3) for a in range(1, 9))
    check(
        "Part 0a: Hermiticity of cited fundamental generators T^a = T^{a†}",
        all_herm,
        detail="all 8 Gell-Mann generators are Hermitian",
    )

    # Verify trace normalization Tr[T^a T^b] = (1/2) δ^{ab}:
    norm_ok = True
    for a in range(1, 9):
        for b in range(1, 9):
            tr = sympy.simplify(sympy.trace(T[a] * T[b]))
            expected = Rational(1, 2) if a == b else 0
            if tr != expected:
                norm_ok = False
                break
        if not norm_ok:
            break
    check(
        "Part 0b: cited trace normalization Tr[T^a T^b] = (1/2) δ^{ab}",
        norm_ok,
        detail="all 64 entries match",
    )

    # ---------------------------------------------------------------------
    section("Part 1: cited bracket and anticommutator relations")
    # ---------------------------------------------------------------------

    # f^{abc} real, totally antisymmetric (sample test):
    f_table = {}
    for a in range(1, 9):
        for b in range(1, 9):
            for c in range(1, 9):
                f_val = sympy.simplify(
                    -2 * I * sympy.trace(commutator(T[a], T[b]) * T[c])
                )
                if f_val != 0:
                    f_table[(a, b, c)] = f_val

    # Check f^{abc} real (imaginary part zero):
    f_real_ok = all(sympy.im(v) == 0 for v in f_table.values())
    check(
        "Part 1a: f^{abc} real for all (a,b,c)",
        f_real_ok,
        detail=f"{len(f_table)} nonzero entries, all real",
    )

    # Check antisymmetry: f^{abc} = -f^{bac}:
    f_antisym_ok = all(
        sympy.simplify(v + f_table.get((b, a, c), 0)) == 0
        for (a, b, c), v in f_table.items()
    )
    check(
        "Part 1b: f^{abc} totally antisymmetric in (a,b)",
        f_antisym_ok,
        detail="f^{abc} = -f^{bac} on all nonzero entries",
    )

    # d^{abc} real, totally symmetric (sample test):
    d_table = {}
    for a in range(1, 9):
        for b in range(1, 9):
            for c in range(1, 9):
                d_val = sympy.simplify(
                    2 * sympy.trace(anticommutator(T[a], T[b]) * T[c])
                )
                if d_val != 0:
                    d_table[(a, b, c)] = d_val

    d_real_ok = all(sympy.im(v) == 0 for v in d_table.values())
    check(
        "Part 1c: d^{abc} real for all (a,b,c)",
        d_real_ok,
        detail=f"{len(d_table)} nonzero entries, all real",
    )

    # Symmetry: d^{abc} = d^{bac}:
    d_sym_ok = all(
        sympy.simplify(v - d_table.get((b, a, c), 0)) == 0
        for (a, b, c), v in d_table.items()
    )
    check(
        "Part 1d: d^{abc} totally symmetric in (a,b)",
        d_sym_ok,
        detail="d^{abc} = d^{bac} on all nonzero entries",
    )

    # Reference table: d^{118} = 1/sqrt(3):
    d_118 = sympy.simplify(d_table.get((1, 1, 8), 0))
    check(
        "Part 1e: cited reference value d^{118} = 1/sqrt(3)",
        sympy.simplify(d_118 - 1 / sqrt(3)) == 0,
        detail=f"d^{{118}} = {d_118}",
    )

    # Anticommutator decomposition: {T^a, T^b} = (1/3) δ_ab I + d^{abc} T^c
    # Check at (a, b) = (1, 1): {T^1, T^1} = 2 T^1 T^1, expand and check.
    ac_11 = anticommutator(T[1], T[1])
    rhs_11 = Rational(1, 3) * eye(3)
    for c_idx in range(1, 9):
        d_11c = sympy.simplify(2 * sympy.trace(anticommutator(T[1], T[1]) * T[c_idx]))
        rhs_11 = rhs_11 + d_11c * T[c_idx]
    diff_11 = sympy.simplify(ac_11 - rhs_11)
    check(
        "Part 1f: anticommutator decomposition at (a,b)=(1,1) reproduces {T^1, T^1}",
        sympy.simplify(diff_11) == zeros(3, 3),
        detail="d^{11c} T^c + (1/3) I = {T^1, T^1}",
    )

    # ---------------------------------------------------------------------
    section("Part 2: cubic anomaly index A(3) = 1 on the fundamental")
    # ---------------------------------------------------------------------

    # A(R) defined by Tr_R[T^a {T^b, T^c}] = (1/2) · A(R) · d^{abc}
    # (Peskin-Schroeder eq. 19.34 normalization).
    # At (a, b, c) = (1, 1, 8): d^{118} = 1/sqrt(3).
    # Tr_3[T^1 {T^1, T^8}] = (1/2) · A(3) · d^{118} = (1/2) · 1 · (1/sqrt(3)) = 1/(2*sqrt(3)).

    tr_118 = cubic_anomaly_trace(T[1], T[1], T[8])
    A_3 = sympy.simplify(2 * tr_118 / d_118)
    check(
        "Part 2a: A(3) = 2 · Tr_3[T^1 {T^1, T^8}] / d^{118} = 1 (Peskin-Schroeder norm.)",
        sympy.simplify(A_3 - 1) == 0,
        detail=f"A(3) = {A_3} (target: 1)",
    )

    # Cross-check at a different nonzero d-triple:
    # d^{146} = 1/2 (reference table). (a, b, c) = (1, 4, 6).
    d_146 = sympy.simplify(d_table.get((1, 4, 6), 0))
    check(
        "Part 2b: cited reference value d^{146} = 1/2",
        sympy.simplify(d_146 - Rational(1, 2)) == 0,
        detail=f"d^{{146}} = {d_146}",
    )

    tr_146 = cubic_anomaly_trace(T[1], T[4], T[6])
    A_3_b = sympy.simplify(2 * tr_146 / d_146)
    check(
        "Part 2c: A(3) cross-check at (1,4,6): A(3) = 1",
        sympy.simplify(A_3_b - 1) == 0,
        detail=f"A(3) = {A_3_b} (target: 1)",
    )

    # ---------------------------------------------------------------------
    section("Part 3: (M1) conjugate-rep generators on the fundamental")
    # ---------------------------------------------------------------------

    # T̄^a := -(T^a)^* (componentwise complex conjugate, then sign flip)
    T_bar = [None] + [-conj_mat(T[a]) for a in range(1, 9)]

    # Hermiticity:
    all_bar_herm = all(
        sympy.simplify(T_bar[a] - T_bar[a].H) == zeros(3, 3) for a in range(1, 9)
    )
    check(
        "Part 3a: (M1) conjugate-rep generators T̄^a Hermitian",
        all_bar_herm,
        detail="T̄^a = -(T^a)^* is Hermitian on the conjugate carrier",
    )

    # Bracket preservation: [T̄^a, T̄^b] = i f^{abc} T̄^c.
    # Test at (a, b) = (1, 2): standard SU(3) f^{123} = 1.
    f_123 = f_table.get((1, 2, 3), 0)
    bracket_12_bar = commutator(T_bar[1], T_bar[2])
    expected_12 = I * f_123 * T_bar[3]
    diff_12 = sympy.simplify(bracket_12_bar - expected_12)
    check(
        "Part 3b: (M1) bracket preservation [T̄^1, T̄^2] = i f^{123} T̄^3",
        sympy.simplify(diff_12) == zeros(3, 3),
        detail=f"f^{{123}} = {f_123} (target: 1)",
    )

    # Cross-check at (a, b) = (4, 5): f^{458} = sqrt(3)/2 (standard).
    f_458 = f_table.get((4, 5, 8), 0)
    bracket_45_bar = commutator(T_bar[4], T_bar[5])
    # Sum over all c: i f^{45c} T̄^c
    expected_45 = zeros(3, 3)
    for c_idx in range(1, 9):
        expected_45 = expected_45 + I * f_table.get((4, 5, c_idx), 0) * T_bar[c_idx]
    diff_45 = sympy.simplify(bracket_45_bar - expected_45)
    check(
        "Part 3c: (M1) bracket [T̄^4, T̄^5] = i f^{45c} T̄^c (sum over c)",
        sympy.simplify(diff_45) == zeros(3, 3),
        detail=f"f^{{458}} = {f_458} (target: sqrt(3)/2)",
    )

    # ---------------------------------------------------------------------
    section("Part 4: (M2)-(M3) sign-flip identity A(R̄) = -A(R), A(3̄) = -1")
    # ---------------------------------------------------------------------

    # A(3̄) computed by direct trace on conjugate generators T̄^a.
    tr_bar_118 = cubic_anomaly_trace(T_bar[1], T_bar[1], T_bar[8])
    A_3bar = sympy.simplify(2 * tr_bar_118 / d_118)
    check(
        "Part 4a: (M3) A(3̄) = 2 · Tr_3̄[T̄^1 {T̄^1, T̄^8}] / d^{118} = -1",
        sympy.simplify(A_3bar - (-1)) == 0,
        detail=f"A(3̄) = {A_3bar} (target: -1)",
    )

    # Cross-check at multiple distinct nonzero d-triples:
    triples_to_check = [
        (1, 1, 8),  # d = 1/sqrt(3)
        (1, 4, 6),  # d = 1/2
        (2, 4, 7),  # d = -1/2
        (8, 8, 8),  # d = -1/sqrt(3)
        (1, 5, 7),  # d = 1/2 -- check standard reference
        (3, 4, 4),  # d = 1/2
    ]

    all_ratios_consistent = True
    ratios = []
    for (a, b, c) in triples_to_check:
        d_abc = sympy.simplify(d_table.get((a, b, c), 0))
        if d_abc == 0:
            continue
        tr_R = cubic_anomaly_trace(T[a], T[b], T[c])
        tr_Rbar = cubic_anomaly_trace(T_bar[a], T_bar[b], T_bar[c])
        A_R = sympy.simplify(2 * tr_R / d_abc)
        A_Rbar = sympy.simplify(2 * tr_Rbar / d_abc)
        ratio_ok = sympy.simplify(A_Rbar + A_R) == 0
        ratios.append((a, b, c, A_R, A_Rbar, ratio_ok))
        if not ratio_ok:
            all_ratios_consistent = False

    check(
        "Part 4b: (M2) A(R̄) = -A(R) holds at multiple distinct nonzero d-triples",
        all_ratios_consistent,
        detail=f"{len(ratios)} triples tested, all consistent with sign-flip",
    )

    # Print the ratios for transparency:
    for (a, b, c, A_R, A_Rbar, ok) in ratios:
        print(
            f"      (a,b,c)=({a},{b},{c}): A(R)={A_R}, A(R̄)={A_Rbar}, "
            f"A(R̄)+A(R)={sympy.simplify(A_R + A_Rbar)}"
        )

    # ---------------------------------------------------------------------
    section("Part 5: (M4) two-fermion contribution 2 · A(3̄) = -2")
    # ---------------------------------------------------------------------

    two_fermion_contribution = sympy.simplify(2 * A_3bar)
    check(
        "Part 5: (M4) 2 · A(3̄) = -2 (two LH Weyl fermions in 3̄)",
        sympy.simplify(two_fermion_contribution - (-2)) == 0,
        detail=f"2 · A(3̄) = {two_fermion_contribution} (target: -2)",
    )

    # ---------------------------------------------------------------------
    section("Part 6: parity-argument restatement on abstract generators")
    # ---------------------------------------------------------------------
    # On any unitary rep, the cubic anomaly trace is real (Hermitian operators
    # inside trace), so it equals its complex conjugate.
    #
    # Pure algebra: Tr[(-X)*  · {(-Y)*, (-Z)*}] = Tr[ -X^* · (Y^* Z^* + Z^* Y^*) ]
    #             = -Tr[X^* (Y^* Z^* + Z^* Y^*)]
    #             = -Tr[(X (YZ + ZY))^*]
    #             = -(Tr[X{Y,Z}])^*  (conjugate commutes with trace)
    #             = -Tr[X{Y,Z}]  (trace is real for Hermitian arg)
    #
    # We verify this parity argument on the explicit fundamental at (1, 1, 8):
    tr_R_complex = sympy.trace(T[1] * anticommutator(T[1], T[8]))
    tr_R_conj = conjugate(tr_R_complex)
    check(
        "Part 6a: Tr[T^a {T^b, T^c}] is real (its complex conjugate equals itself)",
        sympy.simplify(tr_R_complex - tr_R_conj) == 0,
        detail=f"Tr=…, conj(Tr)=…, diff=0",
    )

    # Parity check: Tr[T̄ {T̄, T̄}] = -Tr[T {T, T}] for an odd-rank generator product.
    tr_R = cubic_anomaly_trace(T[1], T[1], T[8])
    tr_Rbar = cubic_anomaly_trace(T_bar[1], T_bar[1], T_bar[8])
    parity_check = sympy.simplify(tr_Rbar + tr_R)
    check(
        "Part 6b: parity identity Tr_{R̄}[T̄ {T̄, T̄}] = -Tr_R[T {T, T}]",
        parity_check == 0,
        detail=f"sum = {parity_check} (target: 0; odd-rank generator product flips sign)",
    )

    # ---------------------------------------------------------------------
    section("Part 7: counterfactual probe — adjoint rep R = 8")
    # ---------------------------------------------------------------------
    # The adjoint rep is self-conjugate (real), so A(8) = 0 = A(8̄).
    # (M2) gives A(8̄) = -A(8), so consistency requires A(8) = 0.
    print("  Building adjoint generators (T^a_adj)^{bc} = -i f^{abc}, 8x8 each ...")
    T_adj_list = adjoint_generators()

    # Hermiticity:
    adj_herm = all(
        sympy.simplify(T_adj_list[a] - T_adj_list[a].H) == zeros(8, 8)
        for a in range(8)
    )
    check(
        "Part 7a: adjoint generators Hermitian",
        adj_herm,
        detail="8 adjoint generators, all Hermitian",
    )

    # A(8) via trace at (a, b, c) = (1, 1, 8):
    # Note: T_adj_list is 0-indexed; T_adj_list[0] = T^1_adj, etc.
    tr_adj_118 = sympy.simplify(
        sympy.trace(
            T_adj_list[0] * anticommutator(T_adj_list[0], T_adj_list[7])
        )
    )
    # A(8) · (1/2) d^{118} = Tr_adj[T^1 {T^1, T^8}]:
    A_8 = sympy.simplify(2 * tr_adj_118 / d_118) if d_118 != 0 else 0
    check(
        "Part 7b: A(8) = 0 (adjoint is self-conjugate / real rep)",
        sympy.simplify(A_8) == 0,
        detail=f"A(8) = {A_8} (target: 0)",
    )

    # And A(8̄) = -A(8) = 0 trivially via (M2):
    A_8bar = sympy.simplify(-A_8)
    check(
        "Part 7c: (M2) consistency: A(8̄) = -A(8) = 0",
        sympy.simplify(A_8bar) == 0,
        detail=f"A(8̄) = {A_8bar} (target: 0)",
    )

    # ---------------------------------------------------------------------
    section("Part 8: cross-consistency at R = 6 (sym^2 of fundamental)")
    # ---------------------------------------------------------------------
    # Standard reference value: A(6) = +7. Construct 6 explicitly and check.

    print("  Building Sym^2(3) generators T^a_6 = T^a ⊗ I + I ⊗ T^a, projected ...")
    T_6_list = build_6_rep_generators(T[1:])  # pass T^1 .. T^8

    # Hermiticity (sanity):
    six_herm = all(
        sympy.simplify(T_6_list[a] - T_6_list[a].H) == zeros(6, 6)
        for a in range(8)
    )
    check(
        "Part 8a: Sym^2(3) generators T^a_6 Hermitian",
        six_herm,
        detail="6 generators, all Hermitian on Sym^2(3)",
    )

    # A(6) via trace at (a, b, c) = (1, 1, 8):
    tr_6_118 = sympy.simplify(
        sympy.trace(T_6_list[0] * anticommutator(T_6_list[0], T_6_list[7]))
    )
    A_6 = sympy.simplify(2 * tr_6_118 / d_118)
    check(
        "Part 8b: A(6) = +7 (standard reference; symmetric tensor square of fundamental)",
        sympy.simplify(A_6 - 7) == 0,
        detail=f"A(6) = {A_6} (target: 7)",
    )

    # A(6̄) by (M2):
    T_6bar_list = [-conj_mat(T_6_list[a]) for a in range(8)]
    tr_6bar_118 = sympy.simplify(
        sympy.trace(T_6bar_list[0] * anticommutator(T_6bar_list[0], T_6bar_list[7]))
    )
    A_6bar = sympy.simplify(2 * tr_6bar_118 / d_118)
    check(
        "Part 8c: (M2) A(6̄) = -A(6) = -7",
        sympy.simplify(A_6bar - (-7)) == 0,
        detail=f"A(6̄) = {A_6bar} (target: -7)",
    )

    # ---------------------------------------------------------------------
    section("Part 9: full parent arithmetic preview — +2 - 1 - 1 = 0")
    # ---------------------------------------------------------------------
    # The parent theorem's load-bearing arithmetic on retained LH-conjugate
    # content: Q_L : 3 with weak multiplicity 2 contributes 2·A(3) = +2.
    # u_R^c : 3̄ contributes A(3̄) = -1. d_R^c : 3̄ contributes A(3̄) = -1.
    # This narrow theorem provides the algebraic foundation for the -1 -1
    # terms (the rep-mapping side). It does NOT close the existence side.
    Q_L_contribution = sympy.simplify(2 * A_3)  # +2
    u_R_c_contribution = sympy.simplify(A_3bar)  # -1
    d_R_c_contribution = sympy.simplify(A_3bar)  # -1
    total = sympy.simplify(
        Q_L_contribution + u_R_c_contribution + d_R_c_contribution
    )
    check(
        "Part 9: parent arithmetic +2 - 1 - 1 = 0 (preview, conditional on parent's existence inputs)",
        sympy.simplify(total) == 0,
        detail=(
            f"Q_L (mult 2): {Q_L_contribution}, u_R^c: {u_R_c_contribution}, "
            f"d_R^c: {d_R_c_contribution}, total: {total}"
        ),
    )

    # ---------------------------------------------------------------------
    section("Summary")
    # ---------------------------------------------------------------------
    print("  Verified at exact sympy precision on the cited Gell-Mann carrier:")
    print("    (M1) Conjugate-rep generators T̄^a = -(T^a)^* are Hermitian")
    print("    (M1) SU(3) bracket relations preserved: [T̄^a, T̄^b] = i f^{abc} T̄^c")
    print("    (M2) Sign-flip identity A(R̄) = -A(R) holds at multiple d-triples")
    print("    (M3) Specialization: A(3) = 1, A(3̄) = -1 at exact rational precision")
    print("    (M4) Two-fermion contribution: 2 · A(3̄) = -2 as rational identity")
    print("    Parity argument: cubic-trace odd-rank sign flip Tr[T̄{T̄,T̄}] = -Tr[T{T,T}]")
    print("    Counterfactual: A(8) = 0 (adjoint self-conjugate, M2 trivially holds)")
    print("    Cross-rep: A(6) = +7, A(6̄) = -7 confirms (M2) on higher-dim irrep")
    print("    Parent arithmetic preview: +2 - 1 - 1 = 0 (representation-mapping side)")

    print()
    print("=" * 88)
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
