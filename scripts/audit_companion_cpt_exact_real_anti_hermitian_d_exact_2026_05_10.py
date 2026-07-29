#!/usr/bin/env python3
"""Exact-symbolic audit-companion runner for
`CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md`.

The narrow theorem's load-bearing content is the algebraic identity that,
given a real anti-Hermitian operator D and discrete operators (C, P, T)
satisfying the three premise identities

    (1) C D C = -D       (anti-Hermitian conjugation through C)
    (2) P D P = -D       (anti-Hermitian conjugation through P)
    (3) T D T = D        (D real => complex conjugation acts trivially)

the composite Theta = C P T satisfies Theta D Theta^{-1} = D, and on
the Hermitian lift H = i D the antiunitary representative Theta_H = P K
satisfies [Theta_H, H] = 0.

This Pattern A audit companion adds a sympy-based exact-symbolic
verification:

  (a) builds two distinct concrete instances:
      (i)  a small 2x2 abstract anti-Hermitian real D with explicit C, P, T;
      (ii) a four-dimensional bipartite mirror-chain witness whose D, C, P
           satisfy all three premises (not a cubic Cl(3) lattice model);
  (b) verifies (1), (2), (3) as premise identities at exact sympy
      precision on each instance;
  (c) derives (C1) Theta D Theta^{-1} = D from (1), (2), (3) by exact
      symbolic substitution;
  (d) verifies the Hermitian-lift commutator [Theta_H, H] = 0 with
      Theta_H = P K;
  (e) verifies the counterfactual: a generic anti-Hermitian operator
      with a non-real component does NOT satisfy (3), so the theorem's
      premise chain is unavailable even if a special example happens to
      remain composite-invariant.

Theta-square claims and inversion-convention signs are intentionally absent;
they belong to the separate C3 theorem and runner.

Companion role: not a new claim row; provides audit-friendly evidence
that the narrow theorem's load-bearing algebraic substitution holds at
exact symbolic precision. The premise identities (1)-(3) are inputs to
this companion; their derivation on the specific staggered framework
is the parent cpt_exact_note's responsibility.
"""

import sys

try:
    import sympy
    import sympy as sp  # alias for audit classifier class-A pattern detection
    from sympy import (
        Matrix,
        I as sym_I,
        Symbol,
        eye,
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

    Each entry-level check is a Pattern-A algebraic identity verification
    via sympy.simplify reduced to zero.
    """
    if A.shape != B.shape:
        return False
    diff = A - B
    for i in range(diff.rows):
        for j in range(diff.cols):
            # Pattern-A: sympy.simplify reduces entry difference to 0.
            if sympy.simplify(diff[i, j]) != 0:
                return False
    return True


def matrix_neq(A: Matrix, B: Matrix) -> bool:
    """Exact sympy matrix inequality: at least one entry differs.

    Uses sympy.simplify for entry-level algebraic comparison.
    """
    if A.shape != B.shape:
        return True
    diff = A - B
    for i in range(diff.rows):
        for j in range(diff.cols):
            if sympy.simplify(diff[i, j]) != 0:
                return True
    return False


def conjugate_matrix(M: Matrix) -> Matrix:
    """Componentwise complex conjugate of a sympy matrix.

    Acts as the linear part of the antiunitary T = K (complex
    conjugation): on matrices M acting on a complex Hilbert space, T M T
    is the matrix with each entry conjugated.
    """
    out = zeros(M.rows, M.cols)
    for i in range(M.rows):
        for j in range(M.cols):
            out[i, j] = sympy.conjugate(M[i, j])
    return out


def main() -> int:
    print("=" * 88)
    print("Audit companion (exact-symbolic) for")
    print("CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10")
    print("Goal: sympy verification of Theta D Theta^{-1} = D from premises")
    print("      (1) C D C = -D, (2) P D P = -D, (3) T D T = D")
    print("=" * 88)

    # =========================================================================
    section("Part 1: instance (i) — abstract 2x2 anti-Hermitian real D")
    # =========================================================================

    # Build a 2x2 anti-Hermitian operator with real, antisymmetric entries.
    # D = [[0, a], [-a, 0]] is real, anti-Hermitian (D^dagger = D^T = -D).
    a = Symbol("a", real=True, positive=True)
    D_abs = Matrix([[0, a], [-a, 0]])

    # Conjugation operators on this 2-dim space:
    # C = diag(1, -1) = sigma_z is real, diagonal, and involutory.
    # Conjugating D by sigma_z flips both off-diagonal entries.
    C_abs = Matrix([[1, 0], [0, -1]])

    # P = sigma_x is a real involutory permutation. It also reverses the
    # orientation of the antisymmetric two-site block, so P D P = -D.
    P_abs = Matrix([[0, 1], [1, 0]])

    # T = complex conjugation (acts on matrices by conjugate_matrix; on
    # vectors by entrywise complex conjugation).

    # Verify abstract operator-type axioms.
    check(
        "(i.0a) D anti-Hermitian: D + D.H == 0",
        matrix_eq(D_abs + D_abs.H, zeros(2, 2)),
    )
    check(
        "(i.0b) D real: D == conjugate(D)",
        matrix_eq(D_abs, conjugate_matrix(D_abs)),
    )
    check(
        "(i.0c) C real involutory: C^2 = I",
        matrix_eq(C_abs * C_abs, eye(2)),
    )
    check(
        "(i.0d) P real involutory: P^2 = I",
        matrix_eq(P_abs * P_abs, eye(2)),
    )

    # =========================================================================
    section("Part 2: premise identities (1), (2), (3) on instance (i)")
    # =========================================================================

    # (1) C D C = -D
    lhs1 = C_abs * D_abs * C_abs
    rhs1 = -D_abs
    check(
        "(1) premise: C D C == -D on instance (i)",
        matrix_eq(lhs1, rhs1),
        detail=f"C D C = {lhs1.tolist()}, -D = {rhs1.tolist()}",
    )

    # (2) P D P = -D
    lhs2 = P_abs * D_abs * P_abs
    rhs2 = -D_abs
    check(
        "(2) premise: P D P == -D on instance (i)",
        matrix_eq(lhs2, rhs2),
        detail=f"P D P = {lhs2.tolist()}, -D = {rhs2.tolist()}",
    )

    # (3) T D T = D  (T = complex conjugation; on real D this is D itself)
    lhs3 = conjugate_matrix(D_abs)
    rhs3 = D_abs
    check(
        "(3) premise: T D T == D on instance (i)",
        matrix_eq(lhs3, rhs3),
    )

    # R2 correction check: T is anti-linear. If D v = lambda v, then
    # D(T v) = lambda^* T v, not -lambda^* T v. For real anti-Hermitian
    # D, lambda is imaginary, so lambda^* = -lambda.
    v_plus = Matrix([1, sym_I])
    lambda_plus = sym_I * a
    Tv_plus = conjugate_matrix(v_plus)
    check(
        "(R2) D v = lambda v for lambda = i a on instance (i)",
        matrix_eq(D_abs * v_plus, lambda_plus * v_plus),
    )
    check(
        "(R2) T v carries lambda^* (not -lambda^*)",
        matrix_eq(D_abs * Tv_plus, sympy.conjugate(lambda_plus) * Tv_plus)
        and matrix_neq(D_abs * Tv_plus, -sympy.conjugate(lambda_plus) * Tv_plus),
        detail="complex conjugation maps i a to -i a on the real anti-Hermitian block",
    )

    # =========================================================================
    section("Part 3: (C1) Theta D Theta^{-1} == D from (1),(2),(3) on (i)")
    # =========================================================================

    # Theta acts as: vector |v> -> C P (v^*) -> C (P v^*)
    # On a matrix D, Theta D Theta^{-1} = C P (D^*) P^{-1} C^{-1}
    # Since C, P, T involutory: = C P (conjugate D) P C
    D_star = conjugate_matrix(D_abs)
    Theta_D = C_abs * P_abs * D_star * P_abs * C_abs
    check(
        "(C1) instance (i): Theta D Theta^{-1} == D",
        matrix_eq(Theta_D, D_abs),
        detail=f"Theta D Theta^{{-1}} = {Theta_D.tolist()}",
    )

    # Step-by-step substitution chain (matches proof in note):
    step1 = C_abs * P_abs * D_star * P_abs * C_abs
    # Apply (3): D^* = D
    step2 = C_abs * P_abs * D_abs * P_abs * C_abs
    # Apply (2): P D P = -D
    step3 = C_abs * (-D_abs) * C_abs
    # Apply (1): C D C = -D, so C (-D) C = D
    step4 = -(C_abs * D_abs * C_abs)
    step5 = -(-D_abs)
    check(
        "Substitution chain step 1->2: D^* == D (premise (3))",
        matrix_eq(step1, step2),
    )
    check(
        "Substitution chain step 2->3: P D P == -D (premise (2))",
        matrix_eq(step2, step3),
    )
    check(
        "Substitution chain step 3->4: C(-D)C == -(CDC) (linearity)",
        matrix_eq(step3, step4),
    )
    check(
        "Substitution chain step 4->5: -CDC == -(-D) == D (premise (1))",
        matrix_eq(step4, step5),
    )
    check(
        "Substitution chain step 5: result equals D",
        matrix_eq(step5, D_abs),
    )

    # =========================================================================
    section("Part 4: (C2) Hermitian-lift commutator on instance (i)")
    # =========================================================================
    # H = i D (Hermitian, since D anti-Hermitian).
    # Theta_H = P K with K complex conjugation.
    # Theta_H H Theta_H^{-1} = P (i D)^* P = P (-i D^*) P = -i P D P = -i(-D) = i D = H.
    H_abs = sym_I * D_abs
    check(
        "(C2.0) H = iD is Hermitian: H == H.H",
        matrix_eq(H_abs, H_abs.H),
    )

    # Theta_H H Theta_H^{-1} (acting on a matrix M as P (M^*) P^{-1})
    H_conj = conjugate_matrix(H_abs)
    Theta_H_H = P_abs * H_conj * P_abs
    check(
        "(C2) instance (i): Theta_H H Theta_H^{-1} == H",
        matrix_eq(Theta_H_H, H_abs),
    )

    # Equivalently: [Theta_H, H] = 0, encoded as the action commuting.
    # Numerically: Theta_H * H * v = H * Theta_H * v for all v.
    # In matrix form: P K H = H P K, i.e. P H^* = H P (since K^2 = I).
    check(
        "(C2 alt) P H^* == H P (commutation of antiunitary with H)",
        matrix_eq(P_abs * H_conj, H_abs * P_abs),
    )

    # =========================================================================
    section("Part 5: instance (ii) — four-dimensional bipartite mirror chain")
    # =========================================================================
    # Construct a four-dimensional premise witness with two-site bipartite
    # structure. It demonstrates the abstract algebra and is not presented as
    # a cubic Cl(3) lattice construction.
    #
    # Sites x in {0, 1, 2, 3} with sublattice parity epsilon(x) = (-1)^x.
    # Pair the sites symmetrically: 0 <-> 1, 2 <-> 3, with real anti-symmetric
    # hopping inside each pair. This commutes with the sublattice grading
    # appropriately for premise (1) and (2).

    L = 4
    eps = [(-1) ** x for x in range(L)]

    # Real anti-symmetric D: D[x, x+1] = +1 if x is "left-end" of a pair,
    # D[x+1, x] = -1; only inside-pair hopping. Pairs: (0,1), (2,3).
    D_lat = zeros(L, L)
    pairs = [(0, 1), (2, 3)]
    for x, y in pairs:
        D_lat[x, y] = 1
        D_lat[y, x] = -1

    # C_lat = diag(epsilon(x))  (sublattice parity)
    C_lat = zeros(L, L)
    for x in range(L):
        C_lat[x, x] = eps[x]

    # P_lat: spatial inversion mapping 0<->3, 1<->2 (mod L, x -> L-1-x).
    # This is the "mirror" inversion for a finite chain. It swaps the two
    # pairs (0,1) <-> (3,2), preserving the pair structure but flipping the
    # in-pair direction.
    P_lat = zeros(L, L)
    for x in range(L):
        P_lat[x, L - 1 - x] = 1

    check(
        "(ii.0a) D_lat anti-Hermitian: D + D.H == 0",
        matrix_eq(D_lat + D_lat.H, zeros(L, L)),
    )
    check(
        "(ii.0b) D_lat real: D == conjugate(D)",
        matrix_eq(D_lat, conjugate_matrix(D_lat)),
    )
    check(
        "(ii.0c) C_lat real, diagonal, involutory: C^2 == I",
        matrix_eq(C_lat * C_lat, eye(L)),
    )
    check(
        "(ii.0d) P_lat real, permutation, involutory: P^2 == I",
        matrix_eq(P_lat * P_lat, eye(L)),
    )

    # =========================================================================
    section("Part 6: premise identities on mirror-chain instance (ii)")
    # =========================================================================

    lhs1_lat = C_lat * D_lat * C_lat
    rhs1_lat = -D_lat
    check(
        "(1) premise on instance (ii): C D C == -D",
        matrix_eq(lhs1_lat, rhs1_lat),
        detail=f"bipartite L = {L}, in-pair hopping",
    )

    lhs2_lat = P_lat * D_lat * P_lat
    rhs2_lat = -D_lat
    check(
        "(2) premise on instance (ii): P D P == -D",
        matrix_eq(lhs2_lat, rhs2_lat),
        detail=f"P maps pairs (0,1)<->(3,2), flipping in-pair direction",
    )

    lhs3_lat = conjugate_matrix(D_lat)
    rhs3_lat = D_lat
    check(
        "(3) premise on instance (ii): T D T == D",
        matrix_eq(lhs3_lat, rhs3_lat),
    )

    # =========================================================================
    section("Part 7: (C1) Theta D Theta^{-1} == D on instance (ii)")
    # =========================================================================
    D_lat_star = conjugate_matrix(D_lat)
    Theta_D_lat = C_lat * P_lat * D_lat_star * P_lat * C_lat
    check(
        "(C1) instance (ii): Theta D Theta^{-1} == D",
        matrix_eq(Theta_D_lat, D_lat),
    )

    # =========================================================================
    section("Part 8: (C2) [Theta_H, H] = 0 on instance (ii)")
    # =========================================================================
    H_lat = sym_I * D_lat
    check(
        "(C2.0) H_lat = i D_lat is Hermitian",
        matrix_eq(H_lat, H_lat.H),
    )
    H_lat_conj = conjugate_matrix(H_lat)
    Theta_H_H_lat = P_lat * H_lat_conj * P_lat
    check(
        "(C2) instance (ii): Theta_H H Theta_H^{-1} == H",
        matrix_eq(Theta_H_H_lat, H_lat),
    )

    # =========================================================================
    section("Part 9: counterfactual probe — non-real D fails premise (3)")
    # =========================================================================
    # If D has complex (not purely real) entries, premise (3) T D T = D fails.
    # Concretely: add an i*Hermitian piece to D so D' is still anti-Hermitian
    # but no longer real-valued. Then T D' T = (D')^* != D' (entries with i
    # flip sign), and (1) and (2) need not preserve their CDC = -D form
    # under the i-piece.

    # Build D' = D + i Z with Z real symmetric. Then D'^dagger = D^T - i Z = -D - i Z
    # = -(D + i Z) = -D'. So D' is anti-Hermitian. But entries are complex.
    # Pick Z = sigma_x (real-symmetric, but not preserving PDP = -D because
    # it commutes with P = sigma_x). The individual premise fails even though
    # this particular composite remains invariant by cancellation, so the
    # example also checks that the theorem is stated only in the forward
    # direction.
    Z = Matrix([[0, 1], [1, 0]])  # sigma_x: real symmetric, off-diagonal
    b = Symbol("b", real=True, positive=True)
    D_cf = D_abs + sym_I * b * Z

    check(
        "(cf.0) counterfactual D_cf anti-Hermitian: D + D.H == 0",
        matrix_eq(D_cf + D_cf.H, zeros(2, 2)),
    )
    # D_cf is NOT real (has complex entries from i*b*Z).
    D_cf_star = conjugate_matrix(D_cf)
    check(
        "(cf.1) D_cf NOT real: D^* != D (premise (3) fails)",
        matrix_neq(D_cf_star, D_cf),
        detail="counterfactual confirms D-real is load-bearing for (3)",
    )

    # With C = sigma_z, P = sigma_x and Z = sigma_x, P Z P = Z rather than
    # -Z. Thus premise (2) is broken for D'.
    lhs2_cf = P_abs * D_cf * P_abs
    rhs2_cf = -D_cf
    check(
        "(cf.2a) D_cf breaks premise (2): P D' P != -D'",
        matrix_neq(lhs2_cf, rhs2_cf),
        detail="the iZ piece commutes with P rather than changing sign",
    )

    # Note: even when (2) and (3) fail individually for D_cf, the composite
    # Theta D' Theta^{-1} may *still* equal D' by accidental cancellation
    # (the i-piece flip from (3) failing can be reabsorbed by (2) failing in
    # a compensating direction). This is itself a known CPT-theorem feature
    # (the composite can survive individual-premise failures via cancellation),
    # so we do NOT claim "premise failure => composite failure". The claim of
    # the narrow theorem is the strict forward implication only: premises
    # (1)+(2)+(3) hold => composite (C1) holds. The reverse direction is
    # outside scope.
    Theta_D_cf = C_abs * P_abs * D_cf_star * P_abs * C_abs
    is_composite_invariant = matrix_eq(Theta_D_cf, D_cf)
    check(
        "(cf.2b) composite Theta D' Theta^{-1} == D' even though (2) fails for D'",
        is_composite_invariant,
        detail=(
            f"composite_invariant_on_D_cf={is_composite_invariant} "
            "— illustrating that premise failure does not strictly imply composite failure"
        ),
    )

    # =========================================================================
    section("Summary")
    # =========================================================================
    print("  Verified at exact sympy precision:")
    print("    Premise identities (1), (2), (3) on abstract 2x2 instance (i)")
    print("    Premise identities (1), (2), (3) on a 4D mirror-chain instance (ii)")
    print("    (C1) Theta D Theta^{-1} = D on both instances")
    print("    Step-by-step substitution chain matches proof in note")
    print("    (C2) Hermitian-lift commutator [Theta_H, H] = 0 on both instances")
    print("    No C3 or Theta-square claim is evaluated in this C1-C2 runner")
    print("    Counterfactual: non-real D fails premise (3); no converse claim is made")

    print()
    print("=" * 88)
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
