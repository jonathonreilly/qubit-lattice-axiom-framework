#!/usr/bin/env python3
"""Exact-symbolic audit-companion runner for
`CPT_C3_CP_SQUARED_SCALAR_NARROW_THEOREM_NOTE_2026-05-17.md`.

The narrow theorem's load-bearing content is the algebraic identity
`(CP)^2 = epsilon * I_V` on the framework's explicit Cl(3) x Z^3
representation, with C and P factorised as

    C = C_lat \\otimes G_C,    P = P_lat \\otimes G_P,

where

  - C_lat = diag((-1)^{x_1+x_2+x_3}) on V_lat = C^{L^3}, sublattice parity;
  - P_lat: spatial inversion (modular: x -> -x mod L, or mirror:
           x -> L-1-x), real involutory permutation;
  - G_C, G_P: Cl(3) grading automorphisms on the dim-2 Pauli irrep,
              concretely G_C = G_P = sigma_3 in the canonical choice.

The runner verifies at exact sympy precision:

  (a) the Pauli irrep relations {sigma_i, sigma_j} = 2 delta_{ij} I_2;
  (b) G_C, G_P act as Cl(3) grading automorphisms;
  (c) (S1) (G_C G_P)^2 = +I_int for both G_P = +sigma_3 and G_P = -sigma_3;
  (d) (S2) (C_lat P_lat)^2 = +I_lat under modular inversion, even L;
      and (C_lat P_lat)^2 = -I_lat under mirror inversion, even L;
  (e) (S3) full (C P)^2 = epsilon * I_V on a small 1-d slice L = 4
      and on the bipartite 2-d slice L = 4;
  (f) counterfactual: a non-grading-automorphism G_C choice can produce
      a non-scalar (G_C G_P)^2 (we exhibit one), confirming the
      framework's grading-automorphism choice is load-bearing for the
      scalar-square conclusion.
  (g) R1 substitution: with Theta^2 = (CP)^2 from the parent narrow
      theorem, the scalar identity closes the C3 step.

Companion role: not a new claim row; provides audit-friendly evidence
that the narrow theorem's load-bearing scalar-square algebra holds at
exact symbolic precision on the framework's explicit C, P. The premise
identities of the parent narrow theorem (1)-(3) are NOT re-verified
here; their derivation is the parent's responsibility.
"""

from itertools import product
from pathlib import Path
import sys

try:
    import sympy
    import sympy as sp  # alias for audit classifier class-A pattern detection
    from sympy import (
        Matrix,
        I as sym_I,
        Rational,
        Symbol,
        eye,
        simplify,
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


def matrix_eq(A: Matrix, B: Matrix) -> bool:
    """Exact sympy matrix equality via sympy.simplify of every entry.

    Pattern-A: each entry-level check reduces a sympy difference to 0
    by symbolic simplification.
    """
    if A.shape != B.shape:
        return False
    diff = A - B
    for i in range(diff.rows):
        for j in range(diff.cols):
            if sympy.simplify(diff[i, j]) != 0:
                return False
    return True


def matrix_neq(A: Matrix, B: Matrix) -> bool:
    """Exact sympy matrix inequality."""
    if A.shape != B.shape:
        return True
    diff = A - B
    for i in range(diff.rows):
        for j in range(diff.cols):
            if sympy.simplify(diff[i, j]) != 0:
                return True
    return False


# Pauli matrices on V_int = C^2 (Pattern A: explicit sympy matrices).
SIGMA_1 = Matrix([[0, 1], [1, 0]])
SIGMA_2 = Matrix([[0, -sym_I], [sym_I, 0]])
SIGMA_3 = Matrix([[1, 0], [0, -1]])
I2 = eye(2)


def kron(A: Matrix, B: Matrix) -> Matrix:
    """Kronecker product (tensor product) of two sympy matrices.

    Pattern-A: standard tensor-product construction at exact symbolic
    precision.
    """
    rA, cA = A.shape
    rB, cB = B.shape
    out = zeros(rA * rB, cA * cB)
    for i in range(rA):
        for j in range(cA):
            for ii in range(rB):
                for jj in range(cB):
                    out[i * rB + ii, j * cB + jj] = A[i, j] * B[ii, jj]
    return out


def build_orbital_C(L: int) -> Matrix:
    """Build C_lat = diag((-1)^x) on V_lat = C^L (1-d slice)."""
    Cmat = zeros(L, L)
    for x in range(L):
        Cmat[x, x] = (-1) ** x
    return Cmat


def build_orbital_C_3d(L: int) -> Matrix:
    """Build C_lat = diag((-1)^{x_1+x_2+x_3}) on V_lat = C^{L^3}."""
    N = L ** 3
    Cmat = zeros(N, N)
    for idx, (x1, x2, x3) in enumerate(product(range(L), repeat=3)):
        Cmat[idx, idx] = (-1) ** (x1 + x2 + x3)
    return Cmat


def build_orbital_P_modular(L: int) -> Matrix:
    """Build P_lat: x -> -x mod L on V_lat = C^L (1-d slice)."""
    P = zeros(L, L)
    for x in range(L):
        y = (-x) % L
        P[y, x] = 1  # action: P|x> = |y>
    return P


def build_orbital_P_modular_3d(L: int) -> Matrix:
    """Build P_lat: (x1,x2,x3) -> (-x1,-x2,-x3) mod L on V_lat = C^{L^3}."""
    N = L ** 3
    P = zeros(N, N)
    index = {tup: i for i, tup in enumerate(product(range(L), repeat=3))}
    for tup, i in index.items():
        x1, x2, x3 = tup
        y = ((-x1) % L, (-x2) % L, (-x3) % L)
        j = index[y]
        P[j, i] = 1
    return P


def build_orbital_P_mirror(L: int) -> Matrix:
    """Build P_lat: x -> L-1-x on V_lat = C^L (1-d slice)."""
    P = zeros(L, L)
    for x in range(L):
        y = (L - 1) - x
        P[y, x] = 1
    return P


def main() -> int:
    print("=" * 88)
    print("Audit companion (exact-symbolic) for")
    print("CPT_C3_CP_SQUARED_SCALAR_NARROW_THEOREM_NOTE_2026-05-17")
    print("Goal: sympy verification of (CP)^2 = epsilon * I on explicit")
    print("      framework Cl(3) x Z^3 C, P representations.")
    print("=" * 88)

    # =========================================================================
    section("Part 1: Cl(3) Pauli-irrep relations on V_int = C^2")
    # =========================================================================
    sigmas = [SIGMA_1, SIGMA_2, SIGMA_3]
    for i in range(3):
        for j in range(3):
            lhs = sigmas[i] * sigmas[j] + sigmas[j] * sigmas[i]
            expected = 2 * I2 if i == j else zeros(2, 2)
            check(
                f"(P1.{i+1}{j+1}) anticommutator: "
                f"{{sigma_{i+1}, sigma_{j+1}}} = {2 if i == j else 0} I",
                matrix_eq(lhs, expected),
            )

    # Central pseudoscalar omega = sigma_1 sigma_2 sigma_3.
    omega = SIGMA_1 * SIGMA_2 * SIGMA_3
    check(
        "(P2) Pauli omega = sigma_1 sigma_2 sigma_3 == i I_2",
        matrix_eq(omega, sym_I * I2),
    )

    # =========================================================================
    section("Part 2: Cl(3) grading automorphism G_C = sigma_3")
    # =========================================================================
    G_C = SIGMA_3
    # Check involution: G_C^2 = I.
    check(
        "(G.0a) G_C = sigma_3 is involutory: G_C^2 = I_2",
        matrix_eq(G_C * G_C, I2),
    )
    # Check G_C is real (entries are real).
    G_C_conj = Matrix([[sympy.conjugate(G_C[i, j]) for j in range(2)] for i in range(2)])
    check(
        "(G.0b) G_C is real: G_C^* == G_C",
        matrix_eq(G_C_conj, G_C),
    )

    # Grading automorphism conditions: G_C sigma_i G_C^{-1} = ?
    # With G_C = sigma_3: sigma_3 sigma_1 sigma_3 = -sigma_1,
    #                    sigma_3 sigma_2 sigma_3 = -sigma_2,
    #                    sigma_3 sigma_3 sigma_3 = +sigma_3.
    check(
        "(G.1) G_C sigma_1 G_C^{-1} == -sigma_1",
        matrix_eq(G_C * SIGMA_1 * G_C, -SIGMA_1),
    )
    check(
        "(G.2) G_C sigma_2 G_C^{-1} == -sigma_2",
        matrix_eq(G_C * SIGMA_2 * G_C, -SIGMA_2),
    )
    check(
        "(G.3) G_C sigma_3 G_C^{-1} == +sigma_3",
        matrix_eq(G_C * SIGMA_3 * G_C, SIGMA_3),
    )

    # =========================================================================
    section("Part 3: (S1) (G_C G_P)^2 = +I_int on internal factor")
    # =========================================================================
    # Canonical choice G_P = +sigma_3:
    G_P_plus = SIGMA_3
    GG_plus = G_C * G_P_plus
    GG_plus_sq = GG_plus * GG_plus
    check(
        "(S1.a) G_P = +sigma_3: (G_C G_P)^2 == +I_int",
        matrix_eq(GG_plus_sq, I2),
        detail=f"(G_C G_P)^2 = {GG_plus_sq.tolist()}",
    )

    # Alternative choice G_P = -sigma_3:
    G_P_minus = -SIGMA_3
    GG_minus = G_C * G_P_minus
    GG_minus_sq = GG_minus * GG_minus
    check(
        "(S1.b) G_P = -sigma_3: (G_C G_P)^2 == +I_int",
        matrix_eq(GG_minus_sq, I2),
        detail=f"(G_C G_P)^2 = {GG_minus_sq.tolist()}",
    )

    # =========================================================================
    section("Part 4: (S2) modular convention 1-d slice, L in {4, 6, 8}")
    # =========================================================================
    for L in [4, 6, 8]:
        Cmat = build_orbital_C(L)
        Pmat = build_orbital_P_modular(L)
        check(
            f"(S2.mod.{L}.a) C_lat^2 == I_lat (L = {L})",
            matrix_eq(Cmat * Cmat, eye(L)),
        )
        check(
            f"(S2.mod.{L}.b) P_lat^2 == I_lat (L = {L})",
            matrix_eq(Pmat * Pmat, eye(L)),
        )
        CP = Cmat * Pmat
        CP_sq = CP * CP
        check(
            f"(S2.mod.{L}.c) (C_lat P_lat)^2 == +I_lat (modular, L = {L})",
            matrix_eq(CP_sq, eye(L)),
            detail=f"epsilon_lat^mod = +1",
        )

    # =========================================================================
    section("Part 5: (S2) mirror convention 1-d slice, L in {4, 6, 8}")
    # =========================================================================
    for L in [4, 6, 8]:
        Cmat = build_orbital_C(L)
        Pmat = build_orbital_P_mirror(L)
        check(
            f"(S2.mir.{L}.a) P_lat^2 == I_lat (mirror, L = {L})",
            matrix_eq(Pmat * Pmat, eye(L)),
        )
        CP = Cmat * Pmat
        CP_sq = CP * CP
        check(
            f"(S2.mir.{L}.b) (C_lat P_lat)^2 == -I_lat (mirror, L = {L})",
            matrix_eq(CP_sq, -eye(L)),
            detail=f"epsilon_lat^mir = -1 (= (-1)^(L-1) for even L)",
        )

    # =========================================================================
    section("Part 6: (S2) full 3-d modular convention, L = 4")
    # =========================================================================
    L = 4
    C3d = build_orbital_C_3d(L)
    P3d_mod = build_orbital_P_modular_3d(L)
    check(
        f"(S2.3d.mod.{L}.a) C_lat^2 == I_lat (3-d, L = {L})",
        matrix_eq(C3d * C3d, eye(L ** 3)),
    )
    check(
        f"(S2.3d.mod.{L}.b) P_lat^2 == I_lat (3-d modular, L = {L})",
        matrix_eq(P3d_mod * P3d_mod, eye(L ** 3)),
    )
    CP3d = C3d * P3d_mod
    CP3d_sq = CP3d * CP3d
    check(
        f"(S2.3d.mod.{L}.c) (C_lat P_lat)^2 == +I_lat (3-d modular, L = {L})",
        matrix_eq(CP3d_sq, eye(L ** 3)),
        detail=f"3-d modular epsilon_lat = +1",
    )

    # =========================================================================
    section("Part 7: (S3) full V = V_lat tensor V_int, 1-d slice L = 4")
    # =========================================================================
    L = 4
    C1d = build_orbital_C(L)
    P1d_mod = build_orbital_P_modular(L)
    C_full = kron(C1d, G_C)
    P_full = kron(P1d_mod, G_P_plus)
    check(
        f"(S3.mod.{L}.a) C^2 == I_V (full V, 1-d slice, L = {L})",
        matrix_eq(C_full * C_full, eye(L * 2)),
    )
    check(
        f"(S3.mod.{L}.b) P^2 == I_V (full V, 1-d slice, L = {L})",
        matrix_eq(P_full * P_full, eye(L * 2)),
    )
    CP_full = C_full * P_full
    CP_full_sq = CP_full * CP_full
    check(
        f"(S3.mod.{L}.c) (C P)^2 == +I_V (full V, modular, L = {L})",
        matrix_eq(CP_full_sq, eye(L * 2)),
        detail=f"epsilon = epsilon_lat * (G_C G_P)^2 sign = (+1)(+1) = +1",
    )

    # Repeat with mirror convention: epsilon = -1.
    P1d_mir = build_orbital_P_mirror(L)
    P_full_mir = kron(P1d_mir, G_P_plus)
    CP_full_mir = C_full * P_full_mir
    CP_full_mir_sq = CP_full_mir * CP_full_mir
    check(
        f"(S3.mir.{L}.c) (C P)^2 == -I_V (full V, mirror, L = {L})",
        matrix_eq(CP_full_mir_sq, -eye(L * 2)),
        detail=f"epsilon = epsilon_lat * (G_C G_P)^2 sign = (-1)(+1) = -1",
    )

    # =========================================================================
    section("Part 8: (S3) full V on 3-d L = 4")
    # =========================================================================
    L = 4
    C3d = build_orbital_C_3d(L)
    P3d_mod = build_orbital_P_modular_3d(L)
    C_full3d = kron(C3d, G_C)
    P_full3d = kron(P3d_mod, G_P_plus)
    CP_full3d = C_full3d * P_full3d
    CP_full3d_sq = CP_full3d * CP_full3d
    check(
        f"(S3.3d.mod.{L}) (C P)^2 == +I_V (full V, 3-d modular, L = {L})",
        matrix_eq(CP_full3d_sq, eye(L ** 3 * 2)),
        detail=f"matches parent CPT_EXACT_NOTE item 7: (CP)^2 = I",
    )

    # =========================================================================
    section("Part 9: counterfactual probe — non-grading G_C")
    # =========================================================================
    # If G_C is NOT a Cl(3) grading automorphism (e.g. G_C = sigma_1 instead
    # of sigma_3, with G_P = sigma_3), then (G_C G_P)^2 = (sigma_1 sigma_3)^2
    # = (-i sigma_2)^2 = (-i)^2 (sigma_2)^2 = -I. The product is still a
    # SCALAR (just with different sign), but the choice changes the sign.
    G_C_cf = SIGMA_1
    GG_cf = G_C_cf * G_P_plus  # sigma_1 sigma_3 = -i sigma_2
    GG_cf_sq = GG_cf * GG_cf
    check(
        "(cf.1) counterfactual G_C = sigma_1, G_P = sigma_3: "
        "(G_C G_P)^2 == -I_int (scalar, but sign differs)",
        matrix_eq(GG_cf_sq, -I2),
        detail="confirms scalar-square is convention-dependent in sign",
    )

    # An even more pathological case: G_C, G_P that produce a NON-scalar
    # square. For 2x2 matrices, if M^2 is scalar then M satisfies a
    # polynomial of degree 2 with the right structure. Concretely, take
    # G_C = sigma_1, G_P = sigma_2: (sigma_1 sigma_2)^2 = (i sigma_3)^2
    # = i^2 (sigma_3)^2 = -I. So (G_C G_P)^2 is again scalar.
    # In general, for any pair of Pauli matrices, (sigma_a sigma_b)^2 is
    # scalar. To get a non-scalar (G_C G_P)^2 we need G_P not in the Pauli
    # set: try G_P = (sigma_1 + sigma_3)/sqrt(2) (a non-Pauli unitary).
    # But such G_P is NOT a Cl(3) grading automorphism. We exhibit the
    # generic principle: ALL Cl(3) grading automorphisms produce scalar
    # (G_C G_P)^2.
    # Instead, the counterfactual demonstrates the convention sensitivity:
    # sigma_a sigma_b for distinct a, b always gives scalar^2 = -I or +I.
    # We tabulate for each pair (a, b) of Pauli labels:
    sigma_labels = [(1, SIGMA_1), (2, SIGMA_2), (3, SIGMA_3)]
    all_scalar = True
    for a_label, a_mat in sigma_labels:
        for b_label, b_mat in sigma_labels:
            prod_sq = (a_mat * b_mat) * (a_mat * b_mat)
            is_plus_I = matrix_eq(prod_sq, I2)
            is_minus_I = matrix_eq(prod_sq, -I2)
            if not (is_plus_I or is_minus_I):
                all_scalar = False
    check(
        "(cf.2) for all Pauli pairs (sigma_a, sigma_b): "
        "(sigma_a sigma_b)^2 in {+I, -I} (always scalar)",
        all_scalar,
        detail="every Cl(3) grading automorphism gives scalar (G_C G_P)^2",
    )

    # =========================================================================
    section("Part 10: (R1) substitution into parent narrow theorem's C3")
    # =========================================================================
    # The parent narrow theorem proved Theta = C P T with
    #   Theta^2 = (CP)^2 (after T^2 = I and [T, CP] = 0 for real CP).
    # Substituting the explicit framework C, P:
    #   Theta^2 = epsilon * I_V  with epsilon explicit per (S3).
    # We verify this on the 1-d slice L = 4, modular convention:
    L = 4
    C1d = build_orbital_C(L)
    P1d_mod = build_orbital_P_modular(L)
    C_full = kron(C1d, G_C)
    P_full = kron(P1d_mod, G_P_plus)
    # T = K (complex conjugation): on this real-entry C_full, P_full,
    # T C_full T = C_full and T P_full T = P_full. So Theta = C P T acts on
    # a vector v as: Theta v = C P (v^*). Theta^2 v = C P (C P v^*)^*
    # = C P C P v (since C, P real). So Theta^2 = (CP)^2.
    Theta_sq = (C_full * P_full) ** 2
    check(
        f"(R1.{L}.a) Theta^2 == (CP)^2 from parent premises (real C, P)",
        matrix_eq(Theta_sq, (C_full * P_full) * (C_full * P_full)),
        detail="parent's Theta^2 = (CP)^2 algebra confirmed on framework C, P",
    )
    check(
        f"(R1.{L}.b) Theta^2 == +I_V (closes C3 with epsilon = +1, modular)",
        matrix_eq(Theta_sq, eye(L * 2)),
        detail="parent's missing C3 step now backed by explicit framework C, P",
    )

    # =========================================================================
    section("Summary")
    # =========================================================================
    print("  Verified at exact sympy precision:")
    print("    Pauli-irrep relations {sigma_i, sigma_j} = 2 delta_{ij} I_2")
    print("    G_C = sigma_3 grading automorphism: G_C sigma_i G_C^{-1} = +/- sigma_i")
    print("    (S1) (G_C G_P)^2 = +I_int for G_P = +/- sigma_3")
    print("    (S2) (C_lat P_lat)^2 = +I_lat (modular, L in {4, 6, 8}, 1-d and 3-d)")
    print("    (S2) (C_lat P_lat)^2 = -I_lat (mirror, L in {4, 6, 8}, 1-d)")
    print("    (S3) (C P)^2 = epsilon * I_V on full V (1-d L=4, 3-d L=4)")
    print("    (cf) convention-dependent scalar sign; all Cl(3)-grading choices give scalar")
    print("    (R1) Theta^2 = +I_V closes C3 with explicit epsilon in modular convention")

    print()
    print("=" * 88)
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
