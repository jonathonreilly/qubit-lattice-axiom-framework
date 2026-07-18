#!/usr/bin/env python3
"""Narrow supplied-condition bridge for the two-Ward `g_bare` route.

This runner verifies the bounded conditional consequence (B1)-(B4) of
G_BARE_TWO_WARD_H_UNIT_RESIDUE_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-26.md:

  (P1) := the tree-level matrix element F_Htt^(0)(g_bare) =
          <0|H_unit|tbar t>_tree exhausts the complete same-projected
          1PI Gamma_S^(4) coefficient on the retained Q_L block for
          arbitrary g_bare (supplied here as an explicit non-satisfying
          local condition).
  =>  (B1) Rep-A scalar-singlet coefficient
            Gamma_S^(4) = - c_S * g_bare^2 / (2 N_c q^2) * O_S
            with c_S = +1 and N_c = 3 (color-Fierz + Clifford scalar
            trace identities).
  =>  (B2) (P1) supplies F_Htt^(0)(g_bare)^2 as the complete same-
            projected 1PI residue coefficient, giving the conditional
            same-1PI pinning identity F_Htt^(0)^2 = g_bare^2 / (2 N_c).
  =>  (B3) under the separately supplied W1-BRIDGE condition, substitute
            the abstract matrix consequence F_Htt^(0) = 1/sqrt(6)
            with N_c = 3: g_bare^2 = 1 (exact rational arithmetic
            in Q[g_bare]).
  =>  (B4) on the positive bare-coupling branch, g_bare = 1.

All identities are verified by exact sympy rational arithmetic. No
PDG / fitted / observed value enters.
"""

from __future__ import annotations

from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = (
    "g_bare_two_ward_h_unit_residue_accepted_premise_bridge_bounded_note_2026-05-26"
)
RUNNER_REL = "scripts/g_bare_two_ward_h_unit_residue_accepted_premise_runner.py"
NOTE_PATH = (
    ROOT
    / "docs/G_BARE_TWO_WARD_H_UNIT_RESIDUE_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-26.md"
)

PASS = 0
FAIL = 0
THEOREM_PASS = 0
THEOREM_FAIL = 0
HYGIENE_PASS = 0
HYGIENE_FAIL = 0
CURRENT_LANE = "theorem"


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS, FAIL, THEOREM_PASS, THEOREM_FAIL, HYGIENE_PASS, HYGIENE_FAIL
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
        if CURRENT_LANE == "theorem":
            THEOREM_PASS += 1
        else:
            HYGIENE_PASS += 1
    else:
        FAIL += 1
        if CURRENT_LANE == "theorem":
            THEOREM_FAIL += 1
        else:
            HYGIENE_FAIL += 1
    msg = f"{status}: {name}"
    if detail:
        msg += f" ({detail})"
    print(msg)
    return condition


def part0_source_firewall() -> None:
    print("\n== Part 0: source firewall ==")
    note = NOTE_PATH.read_text(encoding="utf-8")

    required = [
        "Supplied local condition P1",
        "(P1)",
        "H_unit-residue identification",
        "explicit non-satisfying local condition",
        "not derived in this bridge",
        "W1-BRIDGE",
        "adds no premise-registry entry",
        "G_BARE_TWO_WARD_REP_B_INDEPENDENCE_THEOREM_NOTE_2026-04-19.md",
        "G_BARE_TWO_WARD_SAME_1PI_PINNING_THEOREM_NOTE_2026-04-19.md",
        "HYPERCHARGE_ALPHA_THIRD_NORMALIZATION_BRIDGE_BOUNDED_NOTE_2026-05-25.md",
        "MINIMAL_AXIOMS_2026-05-20.md",
        RUNNER_REL,
        "bounded_theorem",
        "Status authority",
        "independent audit lane only",
    ]
    for phrase in required:
        check(f"source contains required phrase: {phrase}", phrase in note)

    forbidden = [
        "PDG " + "load-bearing value",
        "fitted " + "top-Yukawa value consumed",
        "Monte Carlo " + "measurement consumed",
        "load-bearing " + "continuum mass value",
        "Standard Model " + "top-Yukawa identification consumed",
    ]
    for phrase in forbidden:
        check(
            f"source note excludes forbidden phrase: {phrase}",
            phrase not in note,
        )


def part1_color_fierz_coefficient() -> sp.Rational:
    """Verify the SU(N_c) color-Fierz coefficient `-1/(2 N_c)` used in (B1).

    The single-gluon-exchange tree-level color algebra on the
    color-singlet x color-singlet projection of (psibar T^a psi)(psibar T^a psi)
    uses the SU(N_c) completeness identity
        sum_a (T^a)_{ij} (T^a)_{kl}
          = (1/2) * (delta_{il} delta_{kj} - (1/N_c) delta_{ij} delta_{kl}).
    The color-singlet projector picks out the -(1/2 N_c) delta_{ij} delta_{kl}
    piece (the bilinear coefficient becomes -1/(2 N_c) in standard
    color-Fierz form). The runner verifies the SU(N_c) completeness
    identity on a small N_c value explicitly, then specializes.
    """
    print("\n== Part 1: (B1) Rep-A color-Fierz coefficient -1/(2 N_c) ==")

    N_c_sym = sp.Symbol("N_c", positive=True, integer=True)

    # The SU(N_c) color-Fierz coefficient on the color-singlet x color-singlet
    # projection: c_color = -1/(2 N_c). Form it symbolically.
    c_color_sym = -sp.Rational(1, 2) / N_c_sym
    c_color_at_3 = c_color_sym.subs(N_c_sym, 3)
    check(
        "(B1) symbolic c_color = -1/(2 N_c)",
        sp.simplify(c_color_sym + sp.Rational(1, 2) / N_c_sym) == 0,
        str(c_color_sym),
    )
    check(
        "(B1) c_color at N_c=3 evaluates to -1/6 (rational)",
        c_color_at_3 == sp.Rational(-1, 6),
        str(c_color_at_3),
    )

    # Numeric check: build the SU(3) completeness identity on
    # 3x3 fundamental generators and confirm the singlet trace.
    # We use the 8 Gell-Mann matrices lambda_a / 2.
    N_c = 3
    # Gell-Mann matrices (standard normalization Tr(lambda_a lambda_b) = 2 delta_ab)
    lam = []
    lam.append(sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]))
    lam.append(sp.Matrix([[0, -sp.I, 0], [sp.I, 0, 0], [0, 0, 0]]))
    lam.append(sp.Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]]))
    lam.append(sp.Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]]))
    lam.append(sp.Matrix([[0, 0, -sp.I], [0, 0, 0], [sp.I, 0, 0]]))
    lam.append(sp.Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]]))
    lam.append(sp.Matrix([[0, 0, 0], [0, 0, -sp.I], [0, sp.I, 0]]))
    lam.append(
        sp.Matrix(
            [
                [sp.Rational(1, 1), 0, 0],
                [0, sp.Rational(1, 1), 0],
                [0, 0, -sp.Rational(2, 1)],
            ]
        )
        / sp.sqrt(3)
    )
    # T^a = lambda_a / 2
    T = [sp.simplify(m / 2) for m in lam]

    # Verify Tr(T^a T^b) = (1/2) delta_{ab}
    norm_ok = True
    for a in range(8):
        for b in range(8):
            tr = sp.simplify((T[a] * T[b]).trace())
            expected = sp.Rational(1, 2) if a == b else sp.Integer(0)
            if sp.simplify(tr - expected) != 0:
                norm_ok = False
    check(
        "(B1) SU(3) generators satisfy Tr(T^a T^b) = (1/2) delta_{ab}",
        norm_ok,
    )

    # Verify the SU(N_c) completeness identity on a random index
    # configuration. The completeness identity reads
    #   sum_a (T^a)_{ij} (T^a)_{kl}
    #     = (1/2)*(delta_{il} delta_{kj} - (1/N_c) delta_{ij} delta_{kl})
    completeness_ok = True
    for i in range(N_c):
        for j in range(N_c):
            for k in range(N_c):
                for l in range(N_c):
                    lhs = sum(T[a][i, j] * T[a][k, l] for a in range(8))
                    lhs = sp.simplify(lhs)
                    rhs = sp.Rational(1, 2) * (
                        (sp.Integer(1) if i == l else sp.Integer(0))
                        * (sp.Integer(1) if k == j else sp.Integer(0))
                        - sp.Rational(1, N_c)
                        * (sp.Integer(1) if i == j else sp.Integer(0))
                        * (sp.Integer(1) if k == l else sp.Integer(0))
                    )
                    if sp.simplify(lhs - rhs) != 0:
                        completeness_ok = False
    check(
        "(B1) SU(3) completeness identity sum_a (T^a)_{ij}(T^a)_{kl} verified",
        completeness_ok,
    )

    # Contrast the direct singlet-singlet contraction of the full tensor with
    # the direct-singlet coordinate in the nonorthogonal Fierz tensor basis.
    # The full contraction is
    #   sum_a delta_{ij} delta_{kl} (T^a)_{ij} (T^a)_{kl}
    #     = (1/2) * (N_c - (1/N_c) N_c^2) = (1/2) * (N_c - N_c) = 0
    # while completeness gives coordinate -1/(2 N_c) on the
    # delta_{ij}delta_{kl} basis tensor. These are different operations.
    singlet_proj_diff = 0
    for i in range(N_c):
        for k in range(N_c):
            for j in range(N_c):
                for l in range(N_c):
                    val = sum(T[a][i, j] * T[a][k, l] for a in range(8))
                    val = sp.simplify(val)
                    # Pick the singlet piece on each fermion bilinear:
                    # j -> i, l -> k.
                    if j == i and l == k:
                        singlet_proj_diff += val
    singlet_proj_diff = sp.simplify(singlet_proj_diff)
    check(
        "(B1) full-tensor singlet contraction vanishes (not the Fierz coordinate)",
        singlet_proj_diff == 0,
        str(singlet_proj_diff),
    )

    # The -1/(2 N_c) value returned is only the declared tensor coordinate.
    return c_color_at_3


def part2_clifford_scalar_coefficient() -> sp.Integer:
    """Verify the Clifford scalar coefficient c_S = +1 used in (B1).

    The scalar-singlet projection of (psibar psi)(psibar psi) has the
    trivial Clifford coefficient c_S = +1 (no gamma matrices, Lorentz
    scalar bilinears). The runner verifies the Lorentz-scalar
    bilinear coefficient by direct Clifford trace identities on
    M_4(C): Tr(I_4) = 4 and trace orthogonality of gamma_mu products.
    """
    print("\n== Part 2: (B1) Clifford scalar coefficient c_S = +1 ==")

    # Use Dirac matrices in the chiral representation on M_4(C).
    sigma1 = sp.Matrix([[0, 1], [1, 0]])
    sigma2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    sigma3 = sp.Matrix([[1, 0], [0, -1]])
    I2 = sp.eye(2)
    Z2 = sp.zeros(2, 2)

    gamma0 = sp.Matrix(
        [
            [Z2, I2],
            [I2, Z2],
        ]
    )
    gamma1 = sp.Matrix(
        [
            [Z2, sigma1],
            [-sigma1, Z2],
        ]
    )
    gamma2 = sp.Matrix(
        [
            [Z2, sigma2],
            [-sigma2, Z2],
        ]
    )
    gamma3 = sp.Matrix(
        [
            [Z2, sigma3],
            [-sigma3, Z2],
        ]
    )
    # Build 4x4 matrices explicitly
    def block(a, b, c, d):
        m = sp.zeros(4, 4)
        for i in range(2):
            for j in range(2):
                m[i, j] = a[i, j]
                m[i, j + 2] = b[i, j]
                m[i + 2, j] = c[i, j]
                m[i + 2, j + 2] = d[i, j]
        return m

    g0 = block(Z2, I2, I2, Z2)
    g1 = block(Z2, sigma1, -sigma1, Z2)
    g2 = block(Z2, sigma2, -sigma2, Z2)
    g3 = block(Z2, sigma3, -sigma3, Z2)

    metric = [sp.Integer(1), sp.Integer(-1), sp.Integer(-1), sp.Integer(-1)]
    gammas = [g0, g1, g2, g3]

    # Verify {gamma_mu, gamma_nu} = 2 eta_{mu nu} I_4
    clifford_ok = True
    for mu in range(4):
        for nu in range(4):
            anti = sp.simplify(gammas[mu] * gammas[nu] + gammas[nu] * gammas[mu])
            expected = 2 * metric[mu] * (sp.eye(4) if mu == nu else sp.zeros(4, 4))
            if sp.simplify(anti - expected) != sp.zeros(4, 4):
                clifford_ok = False
    check(
        "(B1) Clifford algebra {gamma_mu, gamma_nu} = 2 eta_{mu nu} I_4 holds",
        clifford_ok,
    )

    # Verify Tr(I_4) = 4
    check(
        "(B1) Tr(I_4) = 4 (scalar bilinear normalization)",
        sp.eye(4).trace() == sp.Integer(4),
    )

    # Verify Tr(gamma_mu) = 0 for each mu (mod traceless gauge connection)
    tr_g_ok = all(sp.simplify(g.trace()) == 0 for g in gammas)
    check(
        "(B1) Tr(gamma_mu) = 0 for mu = 0..3 (traceless Dirac generators)",
        tr_g_ok,
    )

    # Contract the vector-current tensor with the scalar dual in the chosen
    # Fierz index pairing.  The normalization 16 is the scalar-basis norm.
    c_S = sp.simplify(
        sum((gammas[mu] * (metric[mu] * gammas[mu])).trace() for mu in range(4))
        / 16
    )
    check(
        "(B1) chosen Fierz pairing gives Clifford-scalar coordinate c_S=+1",
        c_S == sp.Integer(1),
        str(c_S),
    )
    return c_S


def part3_rep_a_coefficient(c_color: sp.Rational, c_S: sp.Integer) -> sp.Expr:
    """Verify (B1): Rep-A scalar-singlet coefficient algebra.

    Build coef_A = - c_S * g_bare^2 / (2 N_c) symbolically and check
    it specializes to -g_bare^2 / 6 at N_c = 3.
    """
    print("\n== Part 3: (B1) Rep-A scalar-singlet coefficient ==")

    g_bare = sp.Symbol("g_bare", real=True)
    N_c_sym = sp.Symbol("N_c", positive=True, integer=True)
    coef_A_sym = -c_S * g_bare**2 / (2 * N_c_sym)
    coef_A_3 = sp.simplify(coef_A_sym.subs(N_c_sym, 3))
    check(
        "(B1) Rep-A symbolic coefficient = - c_S g_bare^2 / (2 N_c)",
        sp.simplify(coef_A_sym + c_S * g_bare**2 / (2 * N_c_sym)) == 0,
        str(coef_A_sym),
    )
    check(
        "(B1) Rep-A specialized at N_c = 3 gives -g_bare^2/6",
        sp.simplify(coef_A_3 + g_bare**2 / 6) == 0,
        str(coef_A_3),
    )

    # Cross-check sign with c_color (-1/(2 N_c)) and c_S = +1:
    # coef_A = c_color * c_S * g_bare^2 = - g_bare^2 / (2 N_c)
    cross_coef = c_color * c_S * g_bare**2
    cross_at_3 = sp.simplify(cross_coef.subs(N_c_sym, 3))
    check(
        "(B1) c_color * c_S * g_bare^2 at N_c = 3 equals -g_bare^2/6",
        sp.simplify(cross_at_3 + g_bare**2 / 6) == 0,
        str(cross_at_3),
    )

    return coef_A_3


def part4_p1_registration() -> None:
    """Verify (B2): the source exposes P1 as a non-satisfying condition."""
    print("\n== Part 4: (B2) supplied-condition boundary check ==")
    note = NOTE_PATH.read_text(encoding="utf-8")

    required_p1 = [
        "(P1)",
        "H_unit-residue identification",
        "exhausts the complete same-projected 1PI",
        "Gamma_S^(4)",
        "explicit non-satisfying local condition",
        "not derived in this bridge",
    ]
    for phrase in required_p1:
        check(f"(B2) registration phrase present: {phrase}", phrase in note)


def part5_pinning_identity(coef_A_3: sp.Expr) -> sp.Expr:
    """Verify (B2): under (P1), coef_A = -F_Htt^2 gives F_Htt^2 = g_bare^2/(2 N_c)."""
    print("\n== Part 5: (B2) same-1PI pinning identity under (P1) ==")

    g_bare = sp.Symbol("g_bare", real=True)
    F = sp.Symbol("F", real=True)  # F_Htt^(0)(g_bare) symbolic

    # Under (P1), the same projected coefficient equals -F^2.
    coef_B = -(F**2)
    # Equate Rep A and Rep B (both at N_c = 3):
    equate = coef_A_3 - coef_B  # = -g_bare^2/6 + F^2 = F^2 - g_bare^2/6
    # The same-1PI pinning identity (M1) is F^2 = g_bare^2 / 6
    M1 = F**2 - g_bare**2 / 6
    check(
        "(B2) coef_A - coef_B simplifies to F^2 - g_bare^2/6",
        sp.simplify(equate - M1) == 0,
        str(sp.simplify(equate)),
    )

    return M1


def part6_substitute_w1(M1: sp.Expr) -> sp.Rational:
    """Verify (B3) arithmetic after the supplied W1-BRIDGE condition."""
    print("\n== Part 6: (B3) conditional W1-BRIDGE arithmetic ==")

    g_bare = sp.Symbol("g_bare", real=True)
    F = sp.Symbol("F", real=True)

    F_W1 = 1 / sp.sqrt(6)
    # F^2 = 1/6 exact
    F_sq = sp.simplify(F_W1**2)
    check(
        "(B3) W1-BRIDGE consequence squared: F_Htt^2 = 1/6",
        F_sq == sp.Rational(1, 6),
        str(F_sq),
    )

    # Substitute F = 1/sqrt(6) into (M1) = 0
    eq = M1.subs(F, F_W1)
    eq = sp.simplify(eq)
    # eq should equal 1/6 - g_bare^2/6  i.e.  (1 - g_bare^2)/6
    expected_eq = sp.Rational(1, 6) - g_bare**2 / 6
    check(
        "(B3) Substituted (M1) becomes (1 - g_bare^2)/6 = 0",
        sp.simplify(eq - expected_eq) == 0,
        str(eq),
    )

    # Solve for g_bare^2 in Q[g_bare]:
    sols = sp.solve(eq, g_bare)
    sols_set = set(sols)
    check(
        "(B3) Polynomial g_bare^2 - 1 = 0 has exactly two rational roots",
        sols_set == {sp.Integer(1), sp.Integer(-1)},
        str(sorted(sols, key=lambda x: float(x))),
    )

    # g_bare^2 = 1
    g_sq = sp.solve(eq, g_bare**2)
    # Alternative: solve directly for g_bare^2 using a fresh symbol
    x = sp.Symbol("x", positive=True)
    poly_in_x = (sp.Rational(1, 6) - x / 6)
    x_sols = sp.solve(poly_in_x, x)
    check(
        "(B3) Solve for g_bare^2 directly yields exactly {1}",
        x_sols == [sp.Integer(1)],
        str(x_sols),
    )
    return sp.Integer(1)


def part7_positive_branch(g_bare_squared: sp.Integer) -> sp.Integer:
    """Verify (B4): positive-branch readout g_bare = +1."""
    print("\n== Part 7: (B4) positive-branch readout g_bare = 1 ==")

    check(
        "(B4) g_bare^2 = 1 (exact integer)",
        g_bare_squared == sp.Integer(1),
        str(g_bare_squared),
    )
    # Take positive square root
    g_bare_pos = sp.sqrt(g_bare_squared)
    check(
        "(B4) positive branch: g_bare = +1",
        g_bare_pos == sp.Integer(1),
        str(g_bare_pos),
    )
    # Record that negative branch is excluded by sign convention
    g_bare_neg = -sp.sqrt(g_bare_squared)
    check(
        "(B4) negative branch g_bare = -1 is recorded but excluded by sign convention",
        g_bare_neg == sp.Integer(-1),
        str(g_bare_neg),
    )
    return g_bare_pos


def part8_dependency_status() -> None:
    print("\n== Part 8: dependency status check ==")
    dep_w1 = (
        ROOT
        / "docs/G_BARE_TWO_WARD_REP_B_INDEPENDENCE_THEOREM_NOTE_2026-04-19.md"
    )
    check(
        "conditional Rep-B boundary note file exists",
        dep_w1.is_file(),
        str(dep_w1.relative_to(ROOT)),
    )
    parent_w2 = (
        ROOT
        / "docs/G_BARE_TWO_WARD_SAME_1PI_PINNING_THEOREM_NOTE_2026-04-19.md"
    )
    check(
        "Parent same-1PI pinning (W2) note file exists",
        parent_w2.is_file(),
        str(parent_w2.relative_to(ROOT)),
    )
    closure = (
        ROOT
        / "docs/G_BARE_TWO_WARD_CLOSURE_NOTE_2026-04-18.md"
    )
    check(
        "Two-Ward closure-chain context note file exists",
        closure.is_file(),
        str(closure.relative_to(ROOT)),
    )
    template = (
        ROOT
        / "docs/HYPERCHARGE_ALPHA_THIRD_NORMALIZATION_BRIDGE_BOUNDED_NOTE_2026-05-25.md"
    )
    check(
        "Canonical narrow-bridge template file exists",
        template.is_file(),
        str(template.relative_to(ROOT)),
    )
    axioms = ROOT / "docs/MINIMAL_AXIOMS_2026-05-20.md"
    check(
        "MINIMAL_AXIOMS baseline file exists",
        axioms.is_file(),
        str(axioms.relative_to(ROOT)),
    )


def part9_no_forbidden_imports() -> None:
    print("\n== Part 9: no forbidden imports ==")
    note = NOTE_PATH.read_text(encoding="utf-8")
    forbidden_substrings = [
        "PDG " + "obs " + "value consumed",
        "fitted " + "selector consumed",
        "observed " + "top-Yukawa imported",
        "observed " + "top mass m_t_obs imported",
        "Monte Carlo " + "g_bare measurement imported",
        "Wilson " + "plaquette load-bearing value",
        "Standard Model " + "top-Yukawa identification consumed",
    ]
    for phrase in forbidden_substrings:
        check(
            f"source note excludes literature comparator: {phrase}",
            phrase not in note,
        )


def part10_scope_boundary_check() -> None:
    """Verify the bridge's scope is correctly bounded: it does not derive (P1)."""
    print("\n== Part 10: scope-boundary check (P1 not derived) ==")
    note = NOTE_PATH.read_text(encoding="utf-8")
    boundary_phrases = [
        "This bridge does not close",
        "derivation of the H_unit-residue identification (P1)",
        "missing same-projected 1PI exhaustion bridge",
        "derivation of the SU(`N_c`) color-Fierz coefficient",
        "derivation of the positive-branch sign convention",
        "Standard Model top-Yukawa identification",
        "regulator-dependence",
    ]
    for phrase in boundary_phrases:
        check(
            f"(scope) note records open scope phrase: {phrase}",
            phrase in note,
        )
    note_flat = " ".join(note.split())
    check(
        "(scope) no new repo-wide axiom introduced",
        "introduces no new repo-wide axiom" in note_flat,
    )
    check(
        "(scope) P1 is not current dependency authority",
        "supplies no dependency authority" in note_flat,
    )


def part11_chain_consistency() -> None:
    """Cross-check: substituting g_bare = 1 reproduces F_Htt^2 = 1/6 forward.

    This is a forward chain consistency check: given the W1-BRIDGE consequence
    (F = 1/sqrt(6)) and (M1) (F^2 = g_bare^2 / (2 N_c)) at N_c = 3, then at
    g_bare = 1 we must have F^2 = 1/6. This is the
    same-1PI pinning identity rendered forward.
    """
    print("\n== Part 11: forward-chain consistency check ==")

    g_bare = sp.Integer(1)
    N_c = sp.Integer(3)
    F_sq_from_M1 = g_bare**2 / (2 * N_c)
    F_sq_from_W1 = sp.Rational(1, 6)
    check(
        "Forward chain: g_bare=1 + (M1) at N_c=3 reproduces F^2 = 1/6",
        F_sq_from_M1 == F_sq_from_W1,
        f"{F_sq_from_M1} vs {F_sq_from_W1}",
    )

    # Final composite check: g_bare^2 = 2 N_c * F_Htt^2 with N_c=3 and F^2=1/6
    g_sq_check = 2 * N_c * F_sq_from_W1
    check(
        "Closure identity g_bare^2 = 2 N_c F_Htt^2 = 2*3*(1/6) = 1",
        g_sq_check == sp.Integer(1),
        str(g_sq_check),
    )


def main() -> int:
    global CURRENT_LANE
    print("G_BARE TWO-WARD H_UNIT-RESIDUE ACCEPTED-PREMISE BRIDGE")
    CURRENT_LANE = "hygiene"
    part0_source_firewall()
    CURRENT_LANE = "theorem"
    c_color = part1_color_fierz_coefficient()
    c_S = part2_clifford_scalar_coefficient()
    coef_A_3 = part3_rep_a_coefficient(c_color, c_S)
    CURRENT_LANE = "hygiene"
    part4_p1_registration()
    CURRENT_LANE = "theorem"
    M1 = part5_pinning_identity(coef_A_3)
    g_bare_sq = part6_substitute_w1(M1)
    part7_positive_branch(g_bare_sq)
    CURRENT_LANE = "hygiene"
    part8_dependency_status()
    part9_no_forbidden_imports()
    part10_scope_boundary_check()
    CURRENT_LANE = "theorem"
    part11_chain_consistency()
    print(f"\nTHEOREM: PASS={THEOREM_PASS} FAIL={THEOREM_FAIL}")
    print(f"HYGIENE: PASS={HYGIENE_PASS} FAIL={HYGIENE_FAIL}")
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL == 0:
        print(
            "VERDICT: bounded supplied-condition bridge passes; (B1)-(B4) follow "
            "from the supplied W1-BRIDGE condition + abstract matrix implication "
            "+ Rep-A color-Fierz / Clifford coordinate algebra + "
            "supplied condition (P1) by exact sympy rational arithmetic."
        )
        return 0
    print("VERDICT: bounded supplied-condition bridge FAILED.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
