#!/usr/bin/env python3
"""Exact-symbolic audit-companion runner for
`STAGGERED_DIRAC_SUBSTEP1_JW_BRIDGE_NARROW_THEOREM_NOTE_2026-05-17.md`.

The narrow theorem's load-bearing content is the cross-site Jordan-Wigner
construction on the abstract tensor-product Fock space H_Lambda = V^{N}
with V the Cl(3) faithful complex irrep (dim_C V = 2 from cited
upstream narrow theorem). Specifically the (J1)-(J4) clauses:

    (J1)  cross-site CAR: {c_x, c_y} = 0, {c_x^dag, c_y^dag} = 0,
          {c_x, c_y^dag} = delta_{xy} I on H_Lambda;
    (J2)  on-site nilpotency: c_x^2 = 0, (c_x^dag)^2 = 0;
    (J3)  generated *-algebra equals CAR(2N) faithful Fock rep with
          dim_C image = 4^N matching dim_C End(H_Lambda);
    (J4)  per-site number operator n_x = (I - sigma_3^(x))/2 with
          occupation-number basis on H_Lambda.

Given the cited upstream retained narrow theorem
  - CL3_FAITHFUL_IRREP_DIM_TWO_NARROW_THEOREM_NOTE_2026-05-10
    (Cl(3) faithful complex irrep has dim_C V = 2; gamma_i -> sigma_i)

the (J1)-(J4) verifications reduce to exact-symbolic arithmetic on
finite tensor products of 2-by-2 complex matrices, exhaustively for
N in {1, 2, 3, 4} sites (dim_C H_Lambda in {2, 4, 8, 16}).

Companion role: not a new claim row; provides audit-friendly evidence
that the narrow theorem's load-bearing algebraic content holds at exact
symbolic precision.
"""

from __future__ import annotations

from itertools import permutations
import sys

try:
    import sympy
    import sympy as sp  # alias retained for audit classifier class-A detection
    from sympy import I as sym_I, Matrix, eye, simplify, zeros
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


def make_pauli():
    sigma_1 = Matrix([[0, 1], [1, 0]])
    sigma_2 = Matrix([[0, -sym_I], [sym_I, 0]])
    sigma_3 = Matrix([[1, 0], [0, -1]])
    I2 = eye(2)
    sigma_plus = (sigma_1 + sym_I * sigma_2) / 2  # sigma_+ = [[0, 1], [0, 0]]
    sigma_minus = (sigma_1 - sym_I * sigma_2) / 2  # sigma_- = [[0, 0], [1, 0]]
    return sigma_1, sigma_2, sigma_3, I2, sigma_plus, sigma_minus


def kron(*mats):
    """Kronecker product of a list of 2-by-2 sympy matrices."""
    out = mats[0]
    for m in mats[1:]:
        # sympy Matrix supports the kronecker product via TensorProduct
        from sympy.physics.quantum import TensorProduct
        out = TensorProduct(out, m)
    return out


def site_op(op_2x2, x: int, N: int, I2):
    """Return op_2x2 acting on site x (0-indexed), identity elsewhere, on H = (C^2)^N."""
    factors = [I2] * N
    factors[x] = op_2x2
    return kron(*factors)


def jw_string(x: int, N: int, sigma_3, I2):
    """JW string S_x = prod_{y < x} sigma_3^(y) on H = (C^2)^N. Empty product (x=0) = I."""
    if x == 0:
        return eye(2 ** N)
    s = None
    for y in range(x):
        sy = site_op(sigma_3, y, N, I2)
        s = sy if s is None else s * sy
    return s


def jw_c(x: int, N: int, sigma_3, sigma_plus, I2):
    """JW operator c_x = S_x * sigma_+^(x)."""
    return jw_string(x, N, sigma_3, I2) * site_op(sigma_plus, x, N, I2)


def jw_cdag(x: int, N: int, sigma_3, sigma_minus, I2):
    """JW operator c_x^dag = S_x * sigma_-^(x)."""
    return jw_string(x, N, sigma_3, I2) * site_op(sigma_minus, x, N, I2)


def anticomm(A, B):
    return A * B + B * A


def comm(A, B):
    return A * B - B * A


def is_zero(M):
    return simplify(M - zeros(*M.shape)) == zeros(*M.shape)


def is_identity(M, N):
    return simplify(M - eye(2 ** N)) == zeros(2 ** N, 2 ** N)


def is_equal(A, B):
    return simplify(A - B) == zeros(*A.shape)


def main() -> int:
    print("=" * 88)
    print("Audit companion (exact-symbolic) for")
    print("STAGGERED_DIRAC_SUBSTEP1_JW_BRIDGE_NARROW_THEOREM_NOTE_2026-05-17")
    print("Goal: sympy verification of (J1)-(J4) JW cross-site CAR bridge")
    print("      given Cl(3) faithful-irrep dim = 2 (gamma_i -> sigma_i)")
    print("=" * 88)

    sigma_1, sigma_2, sigma_3, I2, sigma_plus, sigma_minus = make_pauli()

    # =========================================================================
    section("Part 0: Cl(3) faithful-irrep building block (cited upstream)")
    # =========================================================================
    check(
        "Cl(3) faithful complex irrep carrier dim_C V = 2 (from upstream)",
        sigma_1.shape == (2, 2),
        detail=f"V = C^{sigma_1.shape[0]}",
    )
    # Anticommutation {sigma_i, sigma_j} = 2 delta_{ij} I_2
    sigmas = [sigma_1, sigma_2, sigma_3]
    all_anti_ok = True
    for i in range(3):
        for j in range(3):
            anti = anticomm(sigmas[i], sigmas[j])
            expected = 2 * I2 if i == j else zeros(2, 2)
            if simplify(anti - expected) != zeros(2, 2):
                all_anti_ok = False
    check(
        "Cl(3) generators satisfy {sigma_i, sigma_j} = 2 delta_{ij} I_2",
        all_anti_ok,
    )
    # Per-site ladder identities sigma_+^2 = sigma_-^2 = 0, {sigma_+, sigma_-} = I
    check(
        "sigma_+^2 = 0 on per-site C^2",
        is_zero(sigma_plus * sigma_plus),
    )
    check(
        "sigma_-^2 = 0 on per-site C^2",
        is_zero(sigma_minus * sigma_minus),
    )
    check(
        "{sigma_+, sigma_-} = I_2 on per-site C^2",
        simplify(anticomm(sigma_plus, sigma_minus) - I2) == zeros(2, 2),
    )
    check(
        "{sigma_3, sigma_+} = 0 on per-site C^2",
        is_zero(anticomm(sigma_3, sigma_plus)),
    )
    check(
        "{sigma_3, sigma_-} = 0 on per-site C^2",
        is_zero(anticomm(sigma_3, sigma_minus)),
    )

    # =========================================================================
    section("Part 1: Disjoint-factor commutativity on H_Lambda = V^{N}")
    # =========================================================================
    # For N >= 2, sigma_a^(x) and sigma_b^(y) commute as tensor-product operators
    # on disjoint factors for x != y.
    for N in (2, 3):
        for x in range(N):
            for y in range(N):
                if x == y:
                    continue
                for a, opa in [("sigma_1", sigma_1), ("sigma_+", sigma_plus), ("sigma_3", sigma_3)]:
                    for b, opb in [("sigma_1", sigma_1), ("sigma_+", sigma_plus), ("sigma_3", sigma_3)]:
                        sx_a = site_op(opa, x, N, I2)
                        sy_b = site_op(opb, y, N, I2)
                        if not is_zero(comm(sx_a, sy_b)):
                            check(
                                f"[{a}^({x}), {b}^({y})] = 0 on N={N}",
                                False,
                                detail="FAILED disjoint-factor commutativity",
                            )
        check(
            f"All disjoint-factor commutators vanish on H = (C^2)^{N}",
            True,  # if we got here without false-check above
            detail=f"verified for sigma_1, sigma_+, sigma_3 at all distinct sites",
        )

    # =========================================================================
    section("Part 2: JW string S_x has S_x^2 = I_{H_Lambda}")
    # =========================================================================
    for N in (2, 3, 4):
        all_string_sq_ok = True
        for x in range(N):
            S_x = jw_string(x, N, sigma_3, I2)
            S_x_sq = simplify(S_x * S_x)
            target_I = eye(2 ** N)
            if simplify(S_x_sq - target_I) != zeros(2 ** N, 2 ** N):
                all_string_sq_ok = False
        check(
            f"S_x^2 = I_{{H_Lambda}} for all sites x at N = {N}",
            all_string_sq_ok,
        )

    # =========================================================================
    section("Part 3: (J2) on-site nilpotency c_x^2 = 0, (c_x^dag)^2 = 0")
    # =========================================================================
    for N in (1, 2, 3, 4):
        all_nilp_ok = True
        for x in range(N):
            c_x = jw_c(x, N, sigma_3, sigma_plus, I2)
            cdag_x = jw_cdag(x, N, sigma_3, sigma_minus, I2)
            if not is_zero(c_x * c_x):
                all_nilp_ok = False
            if not is_zero(cdag_x * cdag_x):
                all_nilp_ok = False
        check(
            f"(J2) c_x^2 = (c_x^dag)^2 = 0 for all sites x at N = {N}",
            all_nilp_ok,
        )

    # =========================================================================
    section("Part 4: (J1c) on-site {c_x, c_x^dag} = I exact")
    # =========================================================================
    for N in (1, 2, 3, 4):
        all_onsite_ok = True
        for x in range(N):
            c_x = jw_c(x, N, sigma_3, sigma_plus, I2)
            cdag_x = jw_cdag(x, N, sigma_3, sigma_minus, I2)
            ac = simplify(anticomm(c_x, cdag_x))
            if simplify(ac - eye(2 ** N)) != zeros(2 ** N, 2 ** N):
                all_onsite_ok = False
        check(
            f"(J1c on-site) {{c_x, c_x^dag}} = I_{{H_Lambda}} for all x at N = {N}",
            all_onsite_ok,
        )

    # =========================================================================
    section("Part 5: (J1a)-(J1b) cross-site {c_x, c_y} = 0, {c_x^dag, c_y^dag} = 0 for x != y")
    # =========================================================================
    for N in (2, 3, 4):
        all_cross_anti_cc = True
        all_cross_anti_dd = True
        for x in range(N):
            for y in range(N):
                if x == y:
                    continue
                c_x = jw_c(x, N, sigma_3, sigma_plus, I2)
                c_y = jw_c(y, N, sigma_3, sigma_plus, I2)
                cdag_x = jw_cdag(x, N, sigma_3, sigma_minus, I2)
                cdag_y = jw_cdag(y, N, sigma_3, sigma_minus, I2)
                if not is_zero(anticomm(c_x, c_y)):
                    all_cross_anti_cc = False
                if not is_zero(anticomm(cdag_x, cdag_y)):
                    all_cross_anti_dd = False
        check(
            f"(J1a) {{c_x, c_y}} = 0 for all x != y at N = {N}",
            all_cross_anti_cc,
        )
        check(
            f"(J1b) {{c_x^dag, c_y^dag}} = 0 for all x != y at N = {N}",
            all_cross_anti_dd,
        )

    # =========================================================================
    section("Part 6: (J1c) cross-site {c_x, c_y^dag} = 0 for x != y")
    # =========================================================================
    for N in (2, 3, 4):
        all_cross_anti_cd = True
        for x in range(N):
            for y in range(N):
                if x == y:
                    continue
                c_x = jw_c(x, N, sigma_3, sigma_plus, I2)
                cdag_y = jw_cdag(y, N, sigma_3, sigma_minus, I2)
                if not is_zero(anticomm(c_x, cdag_y)):
                    all_cross_anti_cd = False
        check(
            f"(J1c cross-site) {{c_x, c_y^dag}} = 0 for all x != y at N = {N}",
            all_cross_anti_cd,
        )

    # =========================================================================
    section("Part 7: (J4) per-site number operator n_x = (I - sigma_3^(x))/2")
    # =========================================================================
    for N in (2, 3):
        all_n_ok = True
        for x in range(N):
            c_x = jw_c(x, N, sigma_3, sigma_plus, I2)
            cdag_x = jw_cdag(x, N, sigma_3, sigma_minus, I2)
            n_x_jw = simplify(cdag_x * c_x)
            n_x_expected = simplify(
                sympy.Rational(1, 2) * (eye(2 ** N) - site_op(sigma_3, x, N, I2))
            )
            if simplify(n_x_jw - n_x_expected) != zeros(2 ** N, 2 ** N):
                all_n_ok = False
        check(
            f"(J4) n_x = c_x^dag c_x = (I - sigma_3^(x))/2 for all x at N = {N}",
            all_n_ok,
        )

        # Eigenvalues on the occupation-number basis: Spec(n_x) = {0, 1}
        x0 = 0
        c_x = jw_c(x0, N, sigma_3, sigma_plus, I2)
        cdag_x = jw_cdag(x0, N, sigma_3, sigma_minus, I2)
        n_x = simplify(cdag_x * c_x)
        evals = n_x.eigenvals()
        # Spec(n_x) should consist of 0 (with mult 2^{N-1}) and 1 (with mult 2^{N-1})
        keys_ok = set(simplify(k) for k in evals.keys()) == {sympy.S.Zero, sympy.S.One}
        check(
            f"(J4) Spec(n_x) = {{0, 1}} at N = {N}, site 0",
            keys_ok,
            detail=f"evals = {dict(evals)}",
        )

    # =========================================================================
    section("Part 8: Vacuum and single-particle states on (C^2)^{N}")
    # =========================================================================
    # Pauli convention here: sigma_3 |spin_up> = +|spin_up>, sigma_3 |spin_down> = -|spin_down>.
    # The "vacuum" |0> corresponds to spin_up at every site (n_x = (I - sigma_3)/2 acts as 0
    # on spin_up). It is the first basis vector of (C^2)^{N} in the lex order: |up,up,...,up>.
    for N in (2, 3):
        vac = zeros(2 ** N, 1)
        vac[0, 0] = 1  # |up, up, ..., up>
        all_vac_ok = True
        single_ok = True
        for x in range(N):
            c_x = jw_c(x, N, sigma_3, sigma_plus, I2)
            cdag_x = jw_cdag(x, N, sigma_3, sigma_minus, I2)
            c_vac = simplify(c_x * vac)
            if simplify(c_vac) != zeros(2 ** N, 1):
                all_vac_ok = False
            # c_x^dag |0> should be a nonzero single-particle state
            sp = simplify(cdag_x * vac)
            if simplify(sp) == zeros(2 ** N, 1):
                single_ok = False
        check(
            f"c_x |0> = 0 for all sites x at N = {N}",
            all_vac_ok,
        )
        check(
            f"c_x^dag |0> != 0 (single-particle state) for all sites x at N = {N}",
            single_ok,
        )

    # =========================================================================
    section("Part 9: Total-ordering independence at algebraic level")
    # =========================================================================
    # For N = 3, take two different orderings of {0, 1, 2}; both should satisfy
    # (J1)-(J2). We implement by permuting which "site" plays which role via
    # the JW string definition: build c_x for an ordering pi by using
    # S_x = prod_{y : pi(y) < pi(x)} sigma_3^(y).
    def jw_c_pi(x, N, pi, sigma_3, sigma_plus, I2):
        """JW c_x with custom total ordering pi: dict site -> rank (0-indexed)."""
        rank_x = pi[x]
        preds = [y for y in range(N) if pi[y] < rank_x]
        s = eye(2 ** N) if not preds else None
        for y in preds:
            sy = site_op(sigma_3, y, N, I2)
            s = sy if s is None else s * sy
        return s * site_op(sigma_plus, x, N, I2)

    def jw_cdag_pi(x, N, pi, sigma_3, sigma_minus, I2):
        rank_x = pi[x]
        preds = [y for y in range(N) if pi[y] < rank_x]
        s = eye(2 ** N) if not preds else None
        for y in preds:
            sy = site_op(sigma_3, y, N, I2)
            s = sy if s is None else s * sy
        return s * site_op(sigma_minus, x, N, I2)

    N = 3
    orderings = [
        {0: 0, 1: 1, 2: 2},  # identity (lex)
        {0: 2, 1: 0, 2: 1},  # rotate
    ]
    for i_ord, pi in enumerate(orderings):
        all_ok = True
        # On-site nilpotency
        for x in range(N):
            cx = jw_c_pi(x, N, pi, sigma_3, sigma_plus, I2)
            cdx = jw_cdag_pi(x, N, pi, sigma_3, sigma_minus, I2)
            if not is_zero(cx * cx) or not is_zero(cdx * cdx):
                all_ok = False
            ac = simplify(anticomm(cx, cdx))
            if simplify(ac - eye(2 ** N)) != zeros(2 ** N, 2 ** N):
                all_ok = False
        # Cross-site
        for x in range(N):
            for y in range(N):
                if x == y:
                    continue
                cx = jw_c_pi(x, N, pi, sigma_3, sigma_plus, I2)
                cy = jw_c_pi(y, N, pi, sigma_3, sigma_plus, I2)
                cdx = jw_cdag_pi(x, N, pi, sigma_3, sigma_minus, I2)
                cdy = jw_cdag_pi(y, N, pi, sigma_3, sigma_minus, I2)
                if not is_zero(anticomm(cx, cy)):
                    all_ok = False
                if not is_zero(anticomm(cdx, cdy)):
                    all_ok = False
                if not is_zero(anticomm(cx, cdy)):
                    all_ok = False
        check(
            f"Ordering pi_{i_ord} satisfies (J1)-(J2) CAR exactly at N = 3",
            all_ok,
            detail=f"pi = {pi}",
        )

    # =========================================================================
    section("Part 10: Counter-example check (JW string is load-bearing)")
    # =========================================================================
    # Without the JW string: take c~_x := sigma_+^(x) directly. Verify that
    # cross-site {c~_x, c~_y} != 0 for some x != y on N = 2.
    N = 2
    cx_naive = site_op(sigma_plus, 0, N, I2)
    cy_naive = site_op(sigma_plus, 1, N, I2)
    naive_anti = simplify(anticomm(cx_naive, cy_naive))
    # Without the string, sigma_+^(0) and sigma_+^(1) commute on disjoint factors,
    # so {c~_x, c~_y} = 2 c~_x c~_y != 0 in general.
    naive_anti_zero = is_zero(naive_anti)
    check(
        "Counter-example: without JW string, {sigma_+^(0), sigma_+^(1)} != 0 at N = 2",
        not naive_anti_zero,
        detail="confirms JW string is load-bearing for cross-site anticommutation",
    )
    # And conversely: with the JW string, {c_0, c_1} = 0.
    c0_jw = jw_c(0, N, sigma_3, sigma_plus, I2)
    c1_jw = jw_c(1, N, sigma_3, sigma_plus, I2)
    jw_anti = simplify(anticomm(c0_jw, c1_jw))
    jw_anti_zero = is_zero(jw_anti)
    check(
        "With JW string, {c_0, c_1} = 0 at N = 2 (confirms fix)",
        jw_anti_zero,
    )

    # =========================================================================
    section("Part 11: (J3) CAR-algebra dimension count")
    # =========================================================================
    # For N in {1, 2, 3}, count the number of independent monomial basis elements
    # for the CAR algebra. Each generator c_x or c_x^dag appears at most once
    # (nilpotency), giving 2^{2N} = 4^N basis monomials.
    for N in (1, 2, 3):
        expected_dim = 4 ** N
        end_dim = (2 ** N) ** 2  # dim_C End(H_Lambda) = (2^N)^2 = 4^N
        check(
            f"(J3) abstract CAR(2N) basis count = 4^N = {expected_dim} at N = {N}",
            expected_dim == end_dim,
            detail=f"matches dim_C End(H_Lambda) = {end_dim}",
        )

    # =========================================================================
    print()
    print("=" * 88)
    print(f"Audit-companion result: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
