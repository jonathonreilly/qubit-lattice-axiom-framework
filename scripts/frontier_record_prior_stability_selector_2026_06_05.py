"""Record-prior stability selector verifier.

This runner checks the finite selector theorem used by
docs/RECORD_PRIOR_STABILITY_SELECTOR_2026-06-05.md.

The theorem is deliberately narrow:

* Record supplies the finite atom alphabet after a readout context is supplied.
* Record does not supply a probability, weighting, dynamics, or occupancy rule.
* On a finite alphabet with atom dimensions d_i, the prior dial

      pi_s(i) = d_i**s / sum_j d_j**s

  has two generation-sector endpoints for dimensions (1, 2):

      s = 0: equal record-letter / block prior = (1/2, 1/2)
      s = 1: dimension / microstate prior      = (1/3, 2/3)

* For each fixed s, the finite reset/thermalizing Markov update

      p_{t+1} = (1 - alpha) p_t + alpha pi_s

  has pi_s as its unique attracting fixed point. Hence "stable" does not by
  itself choose s.
* The selector is the invariance granularity: post-record atom permutation
  symmetry selects s=0; pre-record microstate/Born symmetry selects s=1.

Run:
    python3 scripts/frontier_record_prior_stability_selector_2026_06_05.py
"""

from __future__ import annotations

import sympy as sp


PASS = 0
FAIL = 0


def check(name: str, cond: bool, detail: str = "") -> bool:
    """Record a boolean check."""
    global PASS, FAIL
    ok = bool(cond)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return ok


def row_sums_one(P: sp.Matrix) -> bool:
    return all(sp.simplify(sum(P[i, j] for j in range(P.cols)) - 1) == 0 for i in range(P.rows))


def stationary(pi: list[sp.Expr], P: sp.Matrix) -> bool:
    pi_row = sp.Matrix([pi])
    return all(sp.simplify(x) == 0 for x in list(pi_row * P - pi_row))


def detailed_balance(pi: list[sp.Expr], P: sp.Matrix) -> bool:
    n = len(pi)
    return all(
        sp.simplify(pi[i] * P[i, j] - pi[j] * P[j, i]) == 0
        for i in range(n)
        for j in range(n)
    )


def reset_chain(pi: list[sp.Expr], alpha: sp.Expr) -> sp.Matrix:
    n = len(pi)
    P = sp.zeros(n, n)
    for i in range(n):
        for j in range(n):
            P[i, j] = (1 - alpha if i == j else 0) + alpha * pi[j]
    return sp.simplify(P)


def eigen_multiset(P: sp.Matrix) -> dict[sp.Expr, int]:
    return {sp.simplify(k): v for k, v in P.eigenvals().items()}


def main() -> int:
    s = sp.symbols("s", real=True)
    alpha_sym = sp.symbols("alpha", real=True)
    alpha = sp.Rational(1, 3)
    u = sp.symbols("u", real=True)

    dim_singlet = sp.Integer(1)
    dim_doublet = sp.Integer(2)

    # -------------------------------------------------------------------------
    # 1. The record-prior dial on the two supplied generation-sector atoms.
    # -------------------------------------------------------------------------
    pi_singlet = sp.simplify(dim_singlet**s / (dim_singlet**s + dim_doublet**s))
    pi_doublet = sp.simplify(dim_doublet**s / (dim_singlet**s + dim_doublet**s))
    pi_s = [pi_singlet, pi_doublet]

    check(
        "D1.1 pi_s is normalized on the finite two-atom record alphabet",
        sp.simplify(pi_singlet + pi_doublet - 1) == 0,
        f"pi_s = ({pi_singlet}, {pi_doublet})",
    )

    odds_s = sp.simplify(pi_doublet / pi_singlet)
    check(
        "D1.2 doublet/singlet prior odds are 2^s",
        sp.simplify(odds_s - 2**s) == 0,
        "The dial exponent is the dimension exponent.",
    )

    r_s = sp.simplify(odds_s / 2)
    check(
        "D1.3 generation amplitude ratio is r(s)=2^(s-1)",
        sp.simplify(r_s - 2 ** (s - 1)) == 0,
        "The extra factor 2 is the doublet power 2|b|^2 in the generation dial.",
    )

    pi0 = [sp.simplify(x.subs(s, 0)) for x in pi_s]
    pi1 = [sp.simplify(x.subs(s, 1)) for x in pi_s]
    pi_half = [sp.simplify(x.subs(s, sp.Rational(1, 2))) for x in pi_s]

    check("D1.4 endpoint s=0 is equal-letter/block prior (1/2, 1/2)", pi0 == [sp.Rational(1, 2), sp.Rational(1, 2)])
    check("D1.5 endpoint s=1 is dimension/microstate prior (1/3, 2/3)", pi1 == [sp.Rational(1, 3), sp.Rational(2, 3)])
    check(
        "D1.6 interior point s=1/2 is neither endpoint",
        pi_half != pi0 and pi_half != pi1 and sp.simplify(pi_half[0] + pi_half[1] - 1) == 0,
        f"pi_1/2 = ({pi_half[0]}, {pi_half[1]})",
    )

    r0 = sp.simplify(r_s.subs(s, 0))
    r1 = sp.simplify(r_s.subs(s, 1))
    check("D1.7 endpoint s=0 gives r=1/2", r0 == sp.Rational(1, 2))
    check("D1.8 endpoint s=1 gives r=1", r1 == 1)

    # -------------------------------------------------------------------------
    # 2. Selector by invariance granularity.
    # -------------------------------------------------------------------------
    x, y = sp.symbols("x y", real=True)
    atom_solution = sp.solve([sp.Eq(x + y, 1), sp.Eq(x, y)], [x, y], dict=True)
    check(
        "S2.1 invariance under record-atom swap plus normalization selects uniform atoms",
        atom_solution == [{x: sp.Rational(1, 2), y: sp.Rational(1, 2)}],
        "This is the post-record equal-letter selector.",
    )

    micro = sp.Matrix([[sp.Rational(1, 3), sp.Rational(1, 3), sp.Rational(1, 3)]])
    coarse = sp.Matrix([[1, 0], [0, 1], [0, 1]])
    coarse_prior = list(micro * coarse)
    check(
        "S2.2 uniformity over one singlet microstate and two doublet microstates coarse-grains to (1/3, 2/3)",
        coarse_prior == pi1,
        "This is the pre-record/microstate dimension selector.",
    )

    z0, z1, z2 = sp.symbols("z0 z1 z2", real=True)
    micro_solution = sp.solve(
        [sp.Eq(z0 + z1 + z2, 1), sp.Eq(z0, z1), sp.Eq(z1, z2)],
        [z0, z1, z2],
        dict=True,
    )
    check(
        "S2.3 full microstate permutation symmetry has a unique uniform three-state prior",
        micro_solution == [{z0: sp.Rational(1, 3), z1: sp.Rational(1, 3), z2: sp.Rational(1, 3)}],
    )

    check(
        "S2.4 atom symmetry and microstate symmetry select different endpoints",
        pi0 != pi1,
        f"pi_atom={pi0}, pi_micro={pi1}",
    )

    # -------------------------------------------------------------------------
    # 3. Stable Markov dynamics for fixed target priors.
    # -------------------------------------------------------------------------
    Ps_sym = reset_chain(pi_s, alpha_sym)
    p = [u, 1 - u]
    p_row = sp.Matrix([p])
    pi_s_row = sp.Matrix([pi_s])
    check("M3.0a symbolic pi_s reset chain is row-stochastic for arbitrary alpha", row_sums_one(Ps_sym))
    check("M3.0b symbolic pi_s reset chain has pi_s stationary", stationary(pi_s, Ps_sym))
    check("M3.0c symbolic pi_s reset chain satisfies detailed balance", detailed_balance(pi_s, Ps_sym))
    check(
        "M3.0d symbolic pi_s deviations contract by 1-alpha",
        all(
            sp.simplify(x) == 0
            for x in list(p_row * Ps_sym - pi_s_row - (1 - alpha_sym) * (p_row - pi_s_row))
        ),
    )

    P0 = reset_chain(pi0, alpha)
    P1 = reset_chain(pi1, alpha)
    Ph = reset_chain(pi_half, alpha)
    P0_sym = reset_chain(pi0, alpha_sym)
    P1_sym = reset_chain(pi1, alpha_sym)

    check("M3.1 s=0 reset chain is row-stochastic", row_sums_one(P0), str(P0))
    check("M3.2 s=1 reset chain is row-stochastic", row_sums_one(P1), str(P1))
    check("M3.3 s=1/2 reset chain is row-stochastic", row_sums_one(Ph), str(Ph))

    check("M3.4 s=0 prior is stationary", stationary(pi0, P0))
    check("M3.5 s=1 prior is stationary", stationary(pi1, P1))
    check("M3.6 s=1/2 prior is stationary", stationary(pi_half, Ph))

    check("M3.7 s=0 reset chain satisfies detailed balance", detailed_balance(pi0, P0))
    check("M3.8 s=1 reset chain satisfies detailed balance", detailed_balance(pi1, P1))
    check("M3.9 s=1/2 reset chain satisfies detailed balance", detailed_balance(pi_half, Ph))

    eig0 = eigen_multiset(P0)
    eig1 = eigen_multiset(P1)
    eih = eigen_multiset(Ph)
    expected_eigs = {sp.Integer(1): 1, sp.Rational(2, 3): 1}
    expected_symbolic_eigs = {sp.Integer(1): 1, 1 - alpha_sym: 1}
    check("M3.9a s=0 symbolic chain has eigenvalues {1, 1-alpha}", eigen_multiset(P0_sym) == expected_symbolic_eigs)
    check("M3.9b s=1 symbolic chain has eigenvalues {1, 1-alpha}", eigen_multiset(P1_sym) == expected_symbolic_eigs)
    check("M3.10 s=0 chain has eigenvalues {1, 1-alpha}", eig0 == expected_eigs, str(eig0))
    check("M3.11 s=1 chain has eigenvalues {1, 1-alpha}", eig1 == expected_eigs, str(eig1))
    check("M3.12 s=1/2 chain has eigenvalues {1, 1-alpha}", eih == expected_eigs, str(eih))

    pi0_row = sp.Matrix([pi0])
    pi1_row = sp.Matrix([pi1])
    check(
        "M3.13 s=0 deviations contract exactly by 1-alpha",
        all(sp.simplify(x) == 0 for x in list(p_row * P0 - pi0_row - (1 - alpha) * (p_row - pi0_row))),
    )
    check(
        "M3.14 s=1 deviations contract exactly by 1-alpha",
        all(sp.simplify(x) == 0 for x in list(p_row * P1 - pi1_row - (1 - alpha) * (p_row - pi1_row))),
    )

    # -------------------------------------------------------------------------
    # 4. Stability alone does not choose the dial position.
    # -------------------------------------------------------------------------
    same_form = row_sums_one(P0) and row_sums_one(P1) and detailed_balance(pi0, P0) and detailed_balance(pi1, P1)
    different_fixed_points = pi0 != pi1
    same_contraction = eigen_multiset(P0) == eigen_multiset(P1) == expected_eigs
    check(
        "U4.1 two chains with the same stability form select different fixed priors",
        same_form and different_fixed_points and same_contraction,
        "Therefore stability must be paired with an invariance granularity or target prior.",
    )

    check(
        "U4.2 Record supplies the alphabet type, not pi_s",
        dim_singlet == 1 and dim_doublet == 2 and pi0 != pi1,
        "The same two record atoms admit both endpoint priors.",
    )

    # -------------------------------------------------------------------------
    # 5. Interface to Koide/generation claims: stable dial, not forced value.
    # -------------------------------------------------------------------------
    Q = sp.Rational(1, 3) + sp.Rational(2, 3) * r_s
    check("K5.1 Q(s) endpoint at s=0 is 2/3", sp.simplify(Q.subs(s, 0) - sp.Rational(2, 3)) == 0)
    check("K5.2 Q(s) endpoint at s=1 is 1", sp.simplify(Q.subs(s, 1) - 1) == 0)
    check(
        "K5.3 Q(s) is not constant across the stable dial",
        sp.simplify(Q.subs(s, 0) - Q.subs(s, 1)) != 0,
        "The theorem does not force the Koide endpoint.",
    )

    print(f"SCORECARD PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
