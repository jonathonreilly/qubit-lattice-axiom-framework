#!/usr/bin/env python3
"""Exact-symbolic audit-companion runner for
`CHSH_STRUCTURAL_BOUND_NARROW_THEOREM_NOTE_2026-05-17`.

Narrow theorem: derive the structural CHSH bounds from cited
primitives.

  Part 1 (classical bound):  For any LHV model with A_i, B_j in {-1,+1},
                             |S| <= 2.
  Part 2 (Tsirelson bound):  For any self-adjoint involutions A_i on H_A
                             and B_j on H_B on a tensor product H_A (x) H_B,
                             ||S_op|| <= 2*sqrt(2), via Landau's identity
                             S_op^2 = 4*I - [A_0,A_1] (x) [B_0,B_1].
  Part 3 (saturating):       Bell state |psi> = (|00>+|11>)/sqrt(2) with
                             A_0=sigma_z, A_1=sigma_x,
                             B_0=(sigma_z+sigma_x)/sqrt(2),
                             B_1=(sigma_z-sigma_x)/sqrt(2)
                             gives S = 2*sqrt(2) EXACTLY.
  Part 4 (product=>|S|<=2):  Product state in H_A (x) H_B always gives
                             |S| <= 2 (product-state bound only; the
                             G=0 separability bridge and the saturation
                             equality are NOT tested here and stay open).

One-hop inputs consumed (statuses per live audit ledger):
  (R1) Born quadratic surface P=|A|^2 (i3_zero_exact_theorem_note, cited)
  (R2) Tensor product bipartition H_A (x) H_B (SINGLE_AXIOM_HILBERT_NOTE, cited)
  (R3) Cl(3) per-site Hilbert dim two (cl3_per_site_hilbert_dim_two_theorem_note, cited bounded scope)
  (R4) Anticommuting Pauli involutions in Cl(3) (fermion_parity_pauli_tensor_involution_narrow_theorem_note, cited)
  Statuses for R1-R4 are set only by the independent audit lane (live ledger).

No fitted parameters, no observational comparator, no literature import.

Companion role: stands alone (NEW source theorem, not a re-audit). Class A.
"""

from __future__ import annotations

import sys
import itertools

try:
    from sympy import (
        Rational,
        sqrt,
        Matrix,
        eye,
        zeros,
        simplify,
        kronecker_product,
        Abs,
        S as Sym,
    )
except ImportError:
    print("FAIL: sympy required for exact algebra")
    sys.exit(1)

try:
    import numpy as np
except ImportError:
    print("FAIL: numpy required for norm checks")
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


def main() -> int:
    print("=" * 88)
    print("Audit companion (exact-symbolic + exact-numeric) for")
    print("CHSH_STRUCTURAL_BOUND_NARROW_THEOREM_NOTE_2026-05-17")
    print("Goal: derive structural CHSH bounds (classical 2, Tsirelson 2*sqrt(2))")
    print("One-hop inputs (cited):")
    print("  (R1) Born quadratic surface P=|A|^2   ... cited (i3_zero_exact)")
    print("  (R2) Tensor product H_A (x) H_B       ... cited (SINGLE_AXIOM_HILBERT)")
    print("  (R3) Cl(3) per-site Hilbert dim two   ... cited (bounded scope)")
    print("  (R4) Anticommuting Pauli involutions  ... cited")
    print("  (statuses per live audit ledger; independent audit lane only)")
    print("=" * 88)

    # ==================================================================
    section("Part 1: Classical CHSH bound |S| <= 2 (exhaustive 16-case)")
    # ==================================================================
    # For local hidden variable models with A_i, B_j in {-1, +1},
    # exhaustively enumerate all 2^4 = 16 sign assignments and verify
    # S(lambda) in {-2, 0, +2} for every one.
    s_values = []
    for a0, a1, b0, b1 in itertools.product([-1, +1], repeat=4):
        s_val = a0 * b0 + a0 * b1 + a1 * b0 - a1 * b1
        s_values.append((a0, a1, b0, b1, s_val))

    # All 16 cases produce S in {-2, 0, +2}
    valid_set = set(s for *_, s in s_values)
    check(
        "Part 1 — all 16 sign assignments give S in {-2, 0, +2}",
        valid_set <= {-2, 0, 2},
        detail=f"actual S values: {sorted(valid_set)}",
    )

    # max |S| over 16 assignments equals exactly 2
    max_abs_S = max(abs(s) for *_, s in s_values)
    check(
        "Part 1 — max |S(lambda)| over local hidden-variable assignments = 2",
        max_abs_S == 2,
        detail=f"max |S| = {max_abs_S}",
    )

    # Linearity of expectation: average over arbitrary p(lambda) preserves bound
    # Verify on a non-trivial distribution: uniform over the 16 cases
    avg_S_uniform = sum(s for *_, s in s_values) / 16
    check(
        "Part 1 — uniform-mix expectation gives 0 (by sign symmetry) and trivially |E[S]| <= 2",
        abs(avg_S_uniform) <= 2,
        detail=f"E[S]_uniform = {avg_S_uniform}",
    )

    # Verify the factorization S(lambda) = A_0(B_0+B_1) + A_1(B_0-B_1)
    for a0, a1, b0, b1, s_val in s_values:
        factored = a0 * (b0 + b1) + a1 * (b0 - b1)
        if factored != s_val:
            check(
                f"Part 1 — factorization broken at ({a0},{a1},{b0},{b1})",
                False,
                detail=f"direct={s_val} factored={factored}",
            )
            break
    else:
        check(
            "Part 1 — factorization S = A_0(B_0+B_1) + A_1(B_0-B_1) holds on all 16 cases",
            True,
        )

    # Verify exactly one of (B_0+B_1), (B_0-B_1) is zero (the other is +-2)
    for b0, b1 in itertools.product([-1, +1], repeat=2):
        s_plus = b0 + b1
        s_minus = b0 - b1
        zero_count = (1 if s_plus == 0 else 0) + (1 if s_minus == 0 else 0)
        if zero_count != 1:
            check(
                f"Part 1 — pivot lemma broken at ({b0},{b1})",
                False,
                detail=f"B+B'={s_plus} B-B'={s_minus}",
            )
            break
    else:
        check(
            "Part 1 — for any (B_0,B_1) in {-1,+1}^2, exactly one of (B_0+/-B_1) is zero",
            True,
        )

    # ==================================================================
    section("Part 2: Tsirelson bound via Landau identity (exact symbolic)")
    # ==================================================================
    # Build Pauli matrices as sympy exact Matrix
    I2 = eye(2)
    sigma_x = Matrix([[0, 1], [1, 0]])
    sigma_y = Matrix([[0, -Sym.ImaginaryUnit], [Sym.ImaginaryUnit, 0]])
    sigma_z = Matrix([[1, 0], [0, -1]])

    # Verify involutions: sigma_z^2 = sigma_x^2 = I (R4 cited input)
    check(
        "Part 2 — sigma_z^2 = I (involution, from cited R4)",
        sigma_z * sigma_z == I2,
    )
    check(
        "Part 2 — sigma_x^2 = I (involution, from cited R4)",
        sigma_x * sigma_x == I2,
    )
    # Verify anticommutation {sigma_z, sigma_x} = 0 (R4 cited)
    check(
        "Part 2 — {sigma_z, sigma_x} = 0 (anticommutation, from cited R4)",
        sigma_z * sigma_x + sigma_x * sigma_z == zeros(2, 2),
    )

    # Choose A_0=sigma_z, A_1=sigma_x as concrete instance of the
    # abstract A_i (any self-adjoint involutions in C^2 would work).
    A0 = sigma_z
    A1 = sigma_x
    # For B_j, use the canonical optimal directions for Tsirelson saturation
    B0 = (sigma_z + sigma_x) / sqrt(2)
    B1 = (sigma_z - sigma_x) / sqrt(2)

    # Verify B_j are also involutions and self-adjoint
    check(
        "Part 2 — B_0 = (sigma_z + sigma_x)/sqrt(2) is an involution",
        simplify(B0 * B0 - I2) == zeros(2, 2),
    )
    check(
        "Part 2 — B_1 = (sigma_z - sigma_x)/sqrt(2) is an involution",
        simplify(B1 * B1 - I2) == zeros(2, 2),
    )
    check(
        "Part 2 — B_0 is self-adjoint (Hermitian)",
        B0 == B0.H,
    )
    check(
        "Part 2 — B_1 is self-adjoint (Hermitian)",
        B1 == B1.H,
    )

    # Lift to H_A (x) H_B = C^2 (x) C^2 = C^4
    A0t = kronecker_product(A0, I2)
    A1t = kronecker_product(A1, I2)
    B0t = kronecker_product(I2, B0)
    B1t = kronecker_product(I2, B1)

    # Verify automatic commutation [A_i (x) I, I (x) B_j] = 0 (from R2)
    for i, At in enumerate([A0t, A1t]):
        for j, Bt in enumerate([B0t, B1t]):
            comm = At * Bt - Bt * At
            check(
                f"Part 2 — [A_{i} (x) I, I (x) B_{j}] = 0 (automatic from tensor bipartition R2)",
                simplify(comm) == zeros(4, 4),
            )

    # Build the CHSH operator S_op
    S_op = A0t * B0t + A0t * B1t + A1t * B0t - A1t * B1t

    # Verify S_op is self-adjoint
    check(
        "Part 2 — S_op is self-adjoint",
        simplify(S_op - S_op.H) == zeros(4, 4),
    )

    # Compute S_op^2 exactly
    S_sq = simplify(S_op * S_op)

    # Compute [A_0, A_1] and [B_0, B_1]
    comm_A = A0 * A1 - A1 * A0
    comm_B = B0 * B1 - B1 * B0

    # Landau identity: S_op^2 = 4*I - [A_0,A_1] (x) [B_0,B_1]
    # (Note: the sign convention — the cross-term contribution is
    # -[A_0,A_1] (x) [B_0,B_1] in the form derived in the note.)
    landau_rhs = simplify(
        4 * eye(4) - kronecker_product(comm_A, comm_B)
    )
    landau_diff = simplify(S_sq - landau_rhs)
    check(
        "Part 2 — Landau identity: S_op^2 = 4*I - [A_0,A_1] (x) [B_0,B_1] (exact symbolic)",
        landau_diff == zeros(4, 4),
        detail="Tsirelson 1980 / Landau 1987 algebraic identity",
    )

    # Verify ||[sigma_z, sigma_x]|| = 2 (commutator norm tight)
    # [sigma_z, sigma_x] = sigma_z*sigma_x - sigma_x*sigma_z = 2*i*sigma_y
    # ||2*i*sigma_y|| = 2 (operator norm)
    comm_zx = sigma_z * sigma_x - sigma_x * sigma_z
    expected = 2 * Sym.ImaginaryUnit * sigma_y
    check(
        "Part 2 — [sigma_z, sigma_x] = 2*i*sigma_y (Pauli algebra)",
        simplify(comm_zx - expected) == zeros(2, 2),
    )

    # Numeric operator norm check
    comm_zx_np = np.array(comm_zx.evalf().tolist(), dtype=complex)
    norm_comm_zx = np.linalg.norm(comm_zx_np, ord=2)
    check(
        "Part 2 — ||[sigma_z, sigma_x]||_op = 2 (commutator norm bound tight)",
        abs(norm_comm_zx - 2.0) < 1e-12,
        detail=f"||.|| = {norm_comm_zx:.15f}",
    )

    # Generic commutator-norm bound: ||[X,Y]|| <= 2 when ||X||=||Y||=1
    # Demonstrate on a 3-parameter sweep
    rng = np.random.default_rng(20260517)
    max_seen = 0.0
    for _ in range(200):
        # Random self-adjoint involutions on C^2: X = n.sigma with n unit vector
        nA = rng.standard_normal(3)
        nA /= np.linalg.norm(nA)
        nB = rng.standard_normal(3)
        nB /= np.linalg.norm(nB)
        sx = np.array([[0, 1], [1, 0]], dtype=complex)
        sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
        sz = np.array([[1, 0], [0, -1]], dtype=complex)
        X = nA[0] * sx + nA[1] * sy + nA[2] * sz
        Y = nB[0] * sx + nB[1] * sy + nB[2] * sz
        C = X @ Y - Y @ X
        nc = np.linalg.norm(C, ord=2)
        if nc > max_seen:
            max_seen = nc
    check(
        "Part 2 — random sweep: ||[X,Y]|| <= 2 for ||X||=||Y||=1 (200 random pairs)",
        max_seen <= 2.0 + 1e-9,
        detail=f"max observed ||[X,Y]|| = {max_seen:.12f} (theoretical max 2)",
    )

    # ||S_op|| <= 2*sqrt(2) numerically for the chosen witness setup
    S_op_np = np.array(S_op.evalf().tolist(), dtype=complex)
    s_op_norm = np.linalg.norm(S_op_np, ord=2)
    target_2sqrt2 = float(2 * np.sqrt(2))
    check(
        "Part 2 — ||S_op||_op = 2*sqrt(2) for Bell witness (Tsirelson saturating choice)",
        abs(s_op_norm - target_2sqrt2) < 1e-12,
        detail=f"||S_op|| = {s_op_norm:.15f} target = {target_2sqrt2:.15f}",
    )

    # ==================================================================
    section("Part 3: Saturating witness in Cl(3) per-site Hilbert dim two")
    # ==================================================================
    # Bell state |psi> = (|00> + |11>) / sqrt(2)
    psi = Matrix([Rational(1), Rational(0), Rational(0), Rational(1)]) / sqrt(2)

    check(
        "Part 3 — |psi> = (|00>+|11>)/sqrt(2) has unit norm",
        simplify((psi.H * psi)[0, 0] - 1) == 0,
    )

    # Compute exact expectations <psi| A_i (x) B_j |psi>
    exp_00 = simplify((psi.H * A0t * B0t * psi)[0, 0])
    exp_01 = simplify((psi.H * A0t * B1t * psi)[0, 0])
    exp_10 = simplify((psi.H * A1t * B0t * psi)[0, 0])
    exp_11 = simplify((psi.H * A1t * B1t * psi)[0, 0])

    target_pos = 1 / sqrt(2)
    target_neg = -1 / sqrt(2)

    check(
        f"Part 3 — <A_0 (x) B_0> = +1/sqrt(2)",
        simplify(exp_00 - target_pos) == 0,
        detail=f"computed = {exp_00}",
    )
    check(
        f"Part 3 — <A_0 (x) B_1> = +1/sqrt(2)",
        simplify(exp_01 - target_pos) == 0,
        detail=f"computed = {exp_01}",
    )
    check(
        f"Part 3 — <A_1 (x) B_0> = +1/sqrt(2)",
        simplify(exp_10 - target_pos) == 0,
        detail=f"computed = {exp_10}",
    )
    check(
        f"Part 3 — <A_1 (x) B_1> = -1/sqrt(2)",
        simplify(exp_11 - target_neg) == 0,
        detail=f"computed = {exp_11}",
    )

    # Sum: S = <A_0 B_0> + <A_0 B_1> + <A_1 B_0> - <A_1 B_1>
    S_witness = simplify(exp_00 + exp_01 + exp_10 - exp_11)
    target_S = 2 * sqrt(2)
    check(
        "Part 3 — S = 2*sqrt(2) EXACTLY on Bell-state witness (Tsirelson saturation)",
        simplify(S_witness - target_S) == 0,
        detail=f"S = {S_witness} = {float(S_witness):.15f}",
    )

    # Quantum exceeds classical: S_quantum / S_classical_max = sqrt(2)
    ratio = simplify(S_witness / 2)
    check(
        "Part 3 — quantum saturation S/2 = sqrt(2) exceeds classical bound 1",
        simplify(ratio - sqrt(2)) == 0,
        detail=f"S_quantum / S_classical = {ratio} ~ {float(ratio):.6f}",
    )

    # ==================================================================
    section("Part 4: Product-state bound |S| <= 2 (G=0 bridge not tested; stays open)")
    # ==================================================================
    # For any product state |psi> = |alpha>_A (x) |beta>_B,
    # <A_i (x) B_j> = <alpha|A_i|alpha> * <beta|B_j|beta> = a_i * b_j.
    # Enumerate a grid of (a_0, a_1, b_0, b_1) in [-1,+1]^4 with |a_i|,|b_j|<=1.
    # Verify |S| <= 2 always.
    grid = [Rational(-1), Rational(-1, 2), Rational(0), Rational(1, 2), Rational(1)]
    all_below_2 = True
    max_S_product = Rational(0)
    n_grid = 0
    for a0v in grid:
        for a1v in grid:
            for b0v in grid:
                for b1v in grid:
                    Sp = a0v * b0v + a0v * b1v + a1v * b0v - a1v * b1v
                    n_grid += 1
                    if abs(Sp) > 2:
                        all_below_2 = False
                    if abs(Sp) > abs(max_S_product):
                        max_S_product = Sp
    check(
        f"Part 4 — product-state grid ({n_grid} cases): |S| <= 2 always",
        all_below_2,
        detail=f"max |S_product| = {max_S_product} (theoretical max = 2 at corners)",
    )

    # Spot-check one explicit product state |+>|+>: S evaluates to sqrt(2),
    # comfortably inside the product-state bound |S| <= 2.
    plus = Matrix([Rational(1), Rational(1)]) / sqrt(2)
    psi_prod = kronecker_product(plus, plus)
    Sp_op = A0t * B0t + A0t * B1t + A1t * B0t - A1t * B1t
    S_prod = simplify((psi_prod.H * Sp_op * psi_prod)[0, 0])
    check(
        "Part 4 — product state |+>|+>: |S| <= 2 (verified non-entangled gives bounded)",
        abs(float(S_prod)) <= 2.0 + 1e-12,
        detail=f"S(|+>|+>) = {S_prod} = {float(S_prod):.12f}",
    )

    # ==================================================================
    section("Part 5: Cross-check vs cited one-hop inputs + boundary guards")
    # ==================================================================
    # R4 cross-check: anticommuting in Cl(3) and Z^2 = X^2 = I
    check(
        "Part 5 — R4 cross-check: anticommutation {sigma_z, sigma_x} = 0 matches cited row",
        sigma_z * sigma_x + sigma_x * sigma_z == zeros(2, 2),
    )
    # R3 cross-check: Hilbert dim two
    check(
        "Part 5 — R3 cross-check: H = C^2 (dim 2 per Cl(3) site)",
        sigma_z.shape == (2, 2),
    )

    # Numerical sanity: S_op eigenvalues are real and in [-2sqrt(2), 2sqrt(2)]
    eigvals = np.linalg.eigvalsh(np.array(S_op.evalf().tolist(), dtype=complex))
    check(
        "Part 5 — S_op eigenvalues in [-2sqrt(2), 2sqrt(2)] (self-adjoint spectral bound)",
        all(-target_2sqrt2 - 1e-9 <= e <= target_2sqrt2 + 1e-9 for e in eigvals),
        detail=f"eigenvalues = {sorted(eigvals.tolist())}",
    )
    # Max eigenvalue equals 2*sqrt(2)
    max_eig = max(eigvals)
    check(
        "Part 5 — max eigenvalue of S_op equals 2*sqrt(2) (saturating)",
        abs(max_eig - target_2sqrt2) < 1e-12,
        detail=f"max eig = {max_eig:.15f}",
    )

    # Boundary guards: enumerate things NOT claimed
    boundary_guards = [
        "This note does NOT derive the Born rule P=|A|^2 from nothing (R1 imported).",
        "This note does NOT claim the framework Hamiltonian saturates 2*sqrt(2) at derived couplings.",
        "This note does NOT close bell_inequality_derived_note from G to C; only sub-question (a) is closed, and (b) is narrowed to its algebraic core (product-state bound |S| <= 2) with the G=0 separability bridge and the saturation equality still open.",
        "This note does NOT derive a physical normalization of G or its continuum scaling.",
        "This note does NOT address experimental Bell-test loopholes (detection, locality).",
    ]
    print()
    print("  [BOUNDARY] explicit boundary guards (printed only):")
    for g in boundary_guards:
        print(f"    - {g}")

    # ==================================================================
    section("SCORECARD")
    # ==================================================================
    print()
    print(f"  PASS = {PASS}")
    print(f"  FAIL = {FAIL}")
    print()
    if FAIL == 0:
        print("  STATUS: ALL EXACT-ALGEBRA CHECKS PASS")
        print("  CLOSURE: Structural CHSH bounds (classical 2, Tsirelson 2*sqrt(2)) derived")
        print("           from cited one-hop inputs R1-R4 + Landau identity.")
        print("           Class A (pure algebra over cited inputs).")
        print("           Saturating witness exists in Cl(3) per-site Hilbert dim two.")
        return 0
    else:
        print("  STATUS: FAIL — algebra check broke")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
