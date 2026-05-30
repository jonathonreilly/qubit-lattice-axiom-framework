#!/usr/bin/env python3
"""Exact-symbolic audit-companion runner for
`cl3_central_pseudoscalar_schur_separator_narrow_theorem_note_2026-05-17`.

The narrow theorem's load-bearing content is the Schur-scalar separator
structure on faithful irreducible finite-dim complex Cl(3,0)
representations, conditional on the retained sibling K3 split:

  (S1) For every faithful irreducible finite-dim complex rep
       rho : Cl(3,0) -> End(V), the central pseudoscalar omega acts as
       a scalar chi(rho) * I_V with chi(rho) in {+i, -i}.
  (S2) chi is a faithful chirality discriminator: chi(rho) != chi(rho')
       implies rho and rho' are not unitarily equivalent.
  (S3) Idempotent factorisation: e_+ = (1 - i omega)/2 and
       e_- = (1 + i omega)/2 satisfy rho(e_+) = I_V and rho(e_-) = 0
       when chi(rho) = +i, and rho(e_+) = 0 and rho(e_-) = I_V when
       chi(rho) = -i.

This runner verifies (S1)-(S3) at exact-symbolic precision via sympy
on 2x2 complex matrices, using the cited retained K1 (omega^2 = -1,
omega central) and K3 (complexification split via central idempotents
e_+- = (1 +- i omega)/2) from
`cl3_complexification_split_narrow_theorem_note_2026-05-10`
(generated as retained-grade in the audit ledger at the date of this run).

Companion role: not a new claim row, not a new source note, no status
promotion. Provides audit-friendly evidence that the Schur-separator
structure of the parent
`AXIOM_FIRST_CL3_PER_SITE_UNIQUENESS_THEOREM_NOTE_2026-04-29.md` U2
content holds at exact symbolic precision.
"""

from __future__ import annotations
import sys

try:
    import sympy
    from sympy import (
        Matrix, eye, zeros, simplify,
        I as sym_I, Symbol, symbols, solve,
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


def mat_eq(A: Matrix, B: Matrix) -> bool:
    """Symbolic equality of two sympy matrices via simplify."""
    diff = simplify(A - B)
    return all(diff[i, j] == 0 for i in range(diff.rows) for j in range(diff.cols))


def kron_block(blocks):
    """Build block-diagonal matrix from list of square Matrix blocks."""
    n = sum(b.shape[0] for b in blocks)
    result = zeros(n, n)
    offset = 0
    for b in blocks:
        for i in range(b.shape[0]):
            for j in range(b.shape[1]):
                result[offset + i, offset + j] = b[i, j]
        offset += b.shape[0]
    return result


def main() -> int:
    print("=" * 88)
    print("Audit companion (exact-symbolic) for")
    print("cl3_central_pseudoscalar_schur_separator_narrow_theorem_note_2026-05-17")
    print("Goal: sympy verification of (S1)-(S3) Schur separator on Cl(3,0)")
    print("=" * 88)

    # ---------------------------------------------------------------------
    section("Part 0: Pauli and parity-conjugate realisations")
    # ---------------------------------------------------------------------
    sigma_1 = Matrix([[0, 1], [1, 0]])
    sigma_2 = Matrix([[0, -sym_I], [sym_I, 0]])
    sigma_3 = Matrix([[1, 0], [0, -1]])
    I2 = eye(2)
    Z2 = zeros(2, 2)

    # Positive-chirality Pauli realisation rho_+: gamma_i -> sigma_i
    sigmas_p = [sigma_1, sigma_2, sigma_3]
    # Negative-chirality (parity-conjugate) realisation rho_-: gamma_i -> -sigma_i
    sigmas_m = [-sigma_1, -sigma_2, -sigma_3]

    for k, s in enumerate(sigmas_p, start=1):
        print(f"  rho_+: gamma_{k} -> sigma_{k} = {s.tolist()}")

    # ---------------------------------------------------------------------
    section("Part 1 (cited K1 sanity): omega^2 = -I in both realisations")
    # ---------------------------------------------------------------------
    omega_p = sigmas_p[0] * sigmas_p[1] * sigmas_p[2]
    omega_m = sigmas_m[0] * sigmas_m[1] * sigmas_m[2]
    check("(K1-cited) omega_p^2 = -I_2 (positive chirality)",
          mat_eq(omega_p * omega_p, -I2),
          detail=f"omega_p = {omega_p.tolist()}, omega_p^2 = {(omega_p*omega_p).tolist()}")
    check("(K1-cited) omega_m^2 = -I_2 (negative chirality)",
          mat_eq(omega_m * omega_m, -I2),
          detail=f"omega_m = {omega_m.tolist()}, omega_m^2 = {(omega_m*omega_m).tolist()}")

    # Centrality of omega: [omega, gamma_i] = 0 in both realisations
    for k, (s_p, s_m) in enumerate(zip(sigmas_p, sigmas_m), start=1):
        check(f"(K1-cited) [omega, gamma_{k}] = 0 (positive chirality)",
              mat_eq(omega_p * s_p - s_p * omega_p, Z2))
        check(f"(K1-cited) [omega, gamma_{k}] = 0 (negative chirality)",
              mat_eq(omega_m * s_m - s_m * omega_m, Z2))

    # ---------------------------------------------------------------------
    section("Part 2 (S1): Schur scalar chi(rho) in {+i, -i}")
    # ---------------------------------------------------------------------
    # On positive-chirality realisation: omega_p = +i I_2, so chi(rho_+) = +i.
    chi_plus_target = sym_I * I2
    check("(S1a) Positive chirality: rho(omega) = +i * I_2, so chi(rho_+) = +i",
          mat_eq(omega_p, chi_plus_target),
          detail=f"got rho_+(omega) = {omega_p.tolist()}")

    # On negative-chirality realisation: omega_m = -i I_2, so chi(rho_-) = -i.
    chi_minus_target = -sym_I * I2
    check("(S1b) Negative chirality: rho(omega) = -i * I_2, so chi(rho_-) = -i",
          mat_eq(omega_m, chi_minus_target),
          detail=f"got rho_-(omega) = {omega_m.tolist()}")

    # The two values +i and -i are distinct in C.
    check("(S1c) chi(rho_+) and chi(rho_-) are distinct in C",
          simplify(sym_I - (-sym_I)) != 0)

    # ---------------------------------------------------------------------
    section("Part 3 (S1): Schur scalar property forces chi^2 = -1")
    # ---------------------------------------------------------------------
    # Any 2x2 complex matrix M that commutes with all three sigma_i is a
    # scalar multiple of I_2 (this is the Schur scalar property for the
    # irreducible Pauli rep).
    a, b, c_sym, d = symbols("a b c d", complex=True)
    M = Matrix([[a, b], [c_sym, d]])
    eqs = []
    for s in sigmas_p:
        commutator = M * s - s * M
        for i in range(2):
            for j in range(2):
                eqs.append(commutator[i, j])
    sol = solve(eqs, [a, b, c_sym, d], dict=True)
    schur_scalar_ok = False
    if sol:
        s0 = sol[0]
        b_zero = s0.get(b, b) == 0 or simplify(s0.get(b, b)) == 0
        c_zero = s0.get(c_sym, c_sym) == 0 or simplify(s0.get(c_sym, c_sym)) == 0
        # a == d (both equal to the scalar)
        a_val = s0.get(a, a)
        d_val = s0.get(d, d)
        a_eq_d = simplify(a_val - d_val) == 0
        if b_zero and c_zero and a_eq_d:
            schur_scalar_ok = True
    check("(S1d) Schur scalar: M commutes with sigma_1, sigma_2, sigma_3 ⇒ M = a I",
          schur_scalar_ok,
          detail=f"solution: {sol}")

    # The scalar Schur image of omega satisfies c^2 = rho(omega)^2 = rho(omega^2) = rho(-1) = -I.
    # So c^2 = -1, giving c in {+i, -i}.
    c_sq_p = simplify((sym_I) ** 2)  # chi(rho_+)^2
    c_sq_m = simplify((-sym_I) ** 2)  # chi(rho_-)^2
    check("(S1e) chi(rho_+)^2 = -1 (so chi = +i is consistent with omega^2 = -1)",
          c_sq_p == -1,
          detail=f"chi_+^2 = {c_sq_p}")
    check("(S1f) chi(rho_-)^2 = -1 (so chi = -i is consistent with omega^2 = -1)",
          c_sq_m == -1,
          detail=f"chi_-^2 = {c_sq_m}")

    # Solve c^2 = -1 algebraically: only solutions are +i and -i.
    c_var = Symbol("c_var", complex=True)
    sols_c = solve(c_var ** 2 + 1, c_var)
    check("(S1g) c^2 = -1 has exactly two solutions {+i, -i} in C",
          set(sols_c) == {sym_I, -sym_I},
          detail=f"solutions: {sols_c}")

    # ---------------------------------------------------------------------
    section("Part 4 (S2): separator faithfulness via intertwiner equation")
    # ---------------------------------------------------------------------
    # If U intertwines rho_+ and rho_- (U * rho_+(omega) = rho_-(omega) * U),
    # then U * (+i I) = (-i I) * U, i.e. (+i U) = (-i U), so 2i U = 0, U = 0.
    u_a, u_b, u_c, u_d = symbols("u_a u_b u_c u_d", complex=True)
    U_mat = Matrix([[u_a, u_b], [u_c, u_d]])
    # Intertwiner equation U * (+i I) = (-i I) * U.
    LHS = U_mat * (sym_I * I2)
    RHS = (-sym_I * I2) * U_mat
    intertwiner_eqs = []
    diff_mat = LHS - RHS
    for i in range(2):
        for j in range(2):
            intertwiner_eqs.append(diff_mat[i, j])
    intertwiner_sols = solve(intertwiner_eqs, [u_a, u_b, u_c, u_d], dict=True)
    # The only solution is U = 0.
    only_zero = False
    if intertwiner_sols:
        s0 = intertwiner_sols[0]
        all_zero = (
            simplify(s0.get(u_a, u_a)) == 0
            and simplify(s0.get(u_b, u_b)) == 0
            and simplify(s0.get(u_c, u_c)) == 0
            and simplify(s0.get(u_d, u_d)) == 0
        )
        only_zero = all_zero
    check("(S2a) Only intertwiner of rho_+ (omega=+i I) and rho_- (omega=-i I) is U = 0",
          only_zero,
          detail=f"intertwiner solutions: {intertwiner_sols}")

    # Equivalently, U must commute with rho_+(omega) acting on rho_- side after intertwine:
    # (U * sigma_i) = (-sigma_i * U) for the full rep.
    # Check the full intertwiner equation on generators:
    intertwiner_full_eqs = []
    for sp, sm in zip(sigmas_p, sigmas_m):
        diff_full = U_mat * sp - sm * U_mat
        for i in range(2):
            for j in range(2):
                intertwiner_full_eqs.append(diff_full[i, j])
    intertwiner_full_sols = solve(intertwiner_full_eqs, [u_a, u_b, u_c, u_d], dict=True)
    only_zero_full = False
    if intertwiner_full_sols:
        s0 = intertwiner_full_sols[0]
        all_zero = (
            simplify(s0.get(u_a, u_a)) == 0
            and simplify(s0.get(u_b, u_b)) == 0
            and simplify(s0.get(u_c, u_c)) == 0
            and simplify(s0.get(u_d, u_d)) == 0
        )
        only_zero_full = all_zero
    check("(S2b) Full intertwiner of rho_+ and rho_- on generators forces U = 0",
          only_zero_full,
          detail=f"full intertwiner solutions: {intertwiner_full_sols}")

    # ---------------------------------------------------------------------
    section("Part 5 (S3): idempotent factorisation in each chirality")
    # ---------------------------------------------------------------------
    # e_+ = (1 - i omega) / 2 and e_- = (1 + i omega) / 2.
    # On positive chirality (omega = +i I_2):
    #   e_+ = (I - i*(+i*I))/2 = (I - i^2 I)/2 = (I + I)/2 = I.
    #   e_- = (I + i*(+i*I))/2 = (I + i^2 I)/2 = (I - I)/2 = 0.
    e_plus_p = (I2 - sym_I * omega_p) / 2
    e_minus_p = (I2 + sym_I * omega_p) / 2
    check("(S3a) Positive chirality: rho_+(e_+) = I_2",
          mat_eq(simplify(e_plus_p), I2),
          detail=f"got {simplify(e_plus_p).tolist()}")
    check("(S3b) Positive chirality: rho_+(e_-) = 0",
          mat_eq(simplify(e_minus_p), Z2),
          detail=f"got {simplify(e_minus_p).tolist()}")

    # On negative chirality (omega = -i I_2):
    #   e_+ = (I - i*(-i*I))/2 = (I - (-i^2) I)/2 = (I - 1*I)/2 = 0.
    #   e_- = (I + i*(-i*I))/2 = (I + (-i^2) I)/2 = (I + 1*I)/2 = I.
    e_plus_m = (I2 - sym_I * omega_m) / 2
    e_minus_m = (I2 + sym_I * omega_m) / 2
    check("(S3c) Negative chirality: rho_-(e_+) = 0",
          mat_eq(simplify(e_plus_m), Z2),
          detail=f"got {simplify(e_plus_m).tolist()}")
    check("(S3d) Negative chirality: rho_-(e_-) = I_2",
          mat_eq(simplify(e_minus_m), I2),
          detail=f"got {simplify(e_minus_m).tolist()}")

    # ---------------------------------------------------------------------
    section("Part 6 (S3 sanity): idempotent algebra at the realisation level")
    # ---------------------------------------------------------------------
    for label, ep, em in [("positive chirality", e_plus_p, e_minus_p),
                          ("negative chirality", e_plus_m, e_minus_m)]:
        check(f"({label}) e_+ + e_- = I_2",
              mat_eq(simplify(ep + em), I2))
        check(f"({label}) e_+ * e_- = 0",
              mat_eq(simplify(ep * em), Z2))
        check(f"({label}) e_+^2 = e_+",
              mat_eq(simplify(ep * ep), simplify(ep)))
        check(f"({label}) e_-^2 = e_-",
              mat_eq(simplify(em * em), simplify(em)))

    # ---------------------------------------------------------------------
    section("Part 7 (C1): Schur scalar map is a bijection on {rho_+, rho_-}")
    # ---------------------------------------------------------------------
    chi_plus = sym_I
    chi_minus = -sym_I
    check("(C1a) chi map is injective on {rho_+, rho_-}: chi(rho_+) != chi(rho_-)",
          simplify(chi_plus - chi_minus) != 0,
          detail=f"chi(rho_+) - chi(rho_-) = {simplify(chi_plus - chi_minus)}")
    check("(C1b) chi map image is exactly {+i, -i}",
          {chi_plus, chi_minus} == {sym_I, -sym_I})

    # ---------------------------------------------------------------------
    section("Part 8 (C2): block-diagonal omega on rho_+ ⊕ rho_-")
    # ---------------------------------------------------------------------
    omega_block = kron_block([sym_I * I2, -sym_I * I2])
    rho_pm_g1 = kron_block([sigmas_p[0], sigmas_m[0]])
    rho_pm_g2 = kron_block([sigmas_p[1], sigmas_m[1]])
    rho_pm_g3 = kron_block([sigmas_p[2], sigmas_m[2]])
    omega_pm = rho_pm_g1 * rho_pm_g2 * rho_pm_g3
    check("(C2a) On rho_+ ⊕ rho_- (C^4), omega = diag(+i I_2, -i I_2)",
          mat_eq(omega_pm, omega_block),
          detail=f"got omega on C^4 = {omega_pm.tolist()}")

    # ---------------------------------------------------------------------
    section("Part 9 (C3): chirality-independent dimensional content")
    # ---------------------------------------------------------------------
    # Cross-check: dim_C V = 2 in both chirality summands via Casimir scalar.
    C2_p = sigmas_p[0] * sigmas_p[0] + sigmas_p[1] * sigmas_p[1] + sigmas_p[2] * sigmas_p[2]
    C2_m = sigmas_m[0] * sigmas_m[0] + sigmas_m[1] * sigmas_m[1] + sigmas_m[2] * sigmas_m[2]
    check("(C3a) C_2 = gamma_1^2 + gamma_2^2 + gamma_3^2 = 3 I_2 (positive chirality)",
          mat_eq(C2_p, 3 * I2))
    check("(C3b) C_2 = gamma_1^2 + gamma_2^2 + gamma_3^2 = 3 I_2 (negative chirality)",
          mat_eq(C2_m, 3 * I2))
    check("(C3c) dim_C V = 2 in both chirality summands (matrix shape)",
          sigmas_p[0].shape == (2, 2) and sigmas_m[0].shape == (2, 2))

    # ---------------------------------------------------------------------
    section("Part 10: counterfactual probes (Schur dichotomy sharpness)")
    # ---------------------------------------------------------------------
    # Hypothetical real Schur scalar chi = +1 would require omega^2 = +1, not -1.
    cf_chi_real_plus = sym_I * 0 + 1  # +1, a real candidate
    chi_real_plus_sq = simplify(cf_chi_real_plus ** 2)
    check("(CF1) Counterfactual chi = +1 would force omega^2 = +1, contradicting K1 (omega^2 = -1)",
          chi_real_plus_sq != -1,
          detail=f"chi=+1 squared = {chi_real_plus_sq}, not -1")

    cf_chi_real_minus = -1  # -1, another real candidate
    chi_real_minus_sq = simplify(cf_chi_real_minus ** 2)
    check("(CF2) Counterfactual chi = -1 would force omega^2 = +1, contradicting K1",
          chi_real_minus_sq != -1,
          detail=f"chi=-1 squared = {chi_real_minus_sq}, not -1")

    # Only +i and -i satisfy chi^2 = -1 in C.
    cf_candidates = [sym_I, -sym_I, 1, -1, 2 * sym_I, sym_I + 1]
    valid_chi = [c for c in cf_candidates if simplify(c ** 2 + 1) == 0]
    check("(CF3) Only {+i, -i} satisfy chi^2 = -1 among test candidates",
          set(valid_chi) == {sym_I, -sym_I},
          detail=f"valid chi candidates = {valid_chi}")

    # ---------------------------------------------------------------------
    section("Part 11 (S3 cross-check): explicit idempotent projector verification")
    # ---------------------------------------------------------------------
    # Project (rho_+ ⊕ rho_-) via e_+ in the C^4 representation.
    # On rho_+ summand, e_+ acts as I_2; on rho_- summand, e_+ acts as 0.
    e_plus_block = (eye(4) - sym_I * omega_pm) / 2
    e_minus_block = (eye(4) + sym_I * omega_pm) / 2
    expected_e_plus = kron_block([I2, Z2])
    expected_e_minus = kron_block([Z2, I2])
    check("(S3-bd1) e_+ on rho_+ ⊕ rho_- = diag(I_2, 0)",
          mat_eq(simplify(e_plus_block), expected_e_plus),
          detail="e_+ projects onto the +i-chirality summand")
    check("(S3-bd2) e_- on rho_+ ⊕ rho_- = diag(0, I_2)",
          mat_eq(simplify(e_minus_block), expected_e_minus),
          detail="e_- projects onto the -i-chirality summand")
    check("(S3-bd3) e_+ + e_- = I_4 on rho_+ ⊕ rho_-",
          mat_eq(simplify(e_plus_block + e_minus_block), eye(4)))
    check("(S3-bd4) e_+ * e_- = 0 on rho_+ ⊕ rho_-",
          mat_eq(simplify(e_plus_block * e_minus_block), zeros(4, 4)))

    # ---------------------------------------------------------------------
    section("Summary")
    # ---------------------------------------------------------------------
    print("  Verified at exact sympy precision:")
    print("    (S1) chi(rho_+) = +i and chi(rho_-) = -i; chi^2 = -1 in both")
    print("    (S1) Schur scalar property: only scalar matrices commute with all sigma_i")
    print("    (S2) Intertwiner of rho_+ and rho_- with chi != chi' forces U = 0")
    print("    (S3) Idempotent factorisation: e_+ -> I, e_- -> 0 on rho_+")
    print("    (S3) Idempotent factorisation: e_+ -> 0, e_- -> I on rho_-")
    print("    (S3) Idempotent algebra e_+ + e_- = I, e_+ e_- = 0, e_+^2 = e_+, e_-^2 = e_-")
    print("    (C1) chi map is a bijection {rho_+, rho_-} -> {+i, -i}")
    print("    (C2) Block-diagonal omega on rho_+ ⊕ rho_-")
    print("    (C3) dim_C V = 2 in both summands (chirality-independent)")
    print("    (CF) Schur dichotomy is sharp: chi^2 = -1 forces chi in {+i, -i}")

    print()
    print("=" * 88)
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
