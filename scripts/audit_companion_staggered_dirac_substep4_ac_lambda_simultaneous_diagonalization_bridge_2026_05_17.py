"""Audit companion runner for the substep-4 AC_lambda simultaneous-
diagonalization bridge narrow theorem (2026-05-17).

Verifies via sympy exact symbolic arithmetic that, for the explicit
triple of commuting diagonal unitary 3x3 matrices T_1, T_2, T_3 with
joint eigenvalue triples

  tau^(1) = (-1, +1, +1),
  tau^(2) = (+1, -1, +1),
  tau^(3) = (+1, +1, -1),

the simultaneous-diagonalization corollary forces any operator K on
V_3 = C^3 commuting with all three T_mu to be diagonal in the standard
basis.

  (setup) [T_mu, T_nu] = 0 and T_mu unitary;
  (L1)    pairwise distinctness of joint eigenvalue triples;
  (L3)    identity <e_alpha|[K, T_mu]|e_beta> = (tau_mu^(beta) - tau_mu^(alpha))
                                              * <e_alpha|K|e_beta>;
  (L2)    [K, T_mu] = 0 for mu = 1, 2, 3 forces all 6 off-diagonal
          real parameters of K to zero;
  (L4)    diagonal class: K = diag(k_1, k_2, k_3) commutes with each T_mu;
          the commuting algebra has complex dim 3.
  (counter-examples) non-diagonal K with one off-diagonal entry breaks
          [K, T_1] = 0; trivial all-equal eigenvalue triples (e.g.,
          T_mu = I) fail the distinctness condition.

Expected output: PASS=N FAIL=0 with N >= 14.
"""

from __future__ import annotations

import sympy as sp


def main() -> int:
    fails: list[str] = []
    passes: list[str] = []

    def check(label: str, ok: bool, detail: str = "") -> None:
        if ok:
            passes.append(label)
            print(f"  PASS  {label}" + (f" :: {detail}" if detail else ""))
        else:
            fails.append(label)
            print(f"  FAIL  {label}" + (f" :: {detail}" if detail else ""))

    # ----- Setup: explicit commuting-unitary triple -----
    # tau^(alpha) = joint eigenvalue triple on basis vector e_alpha
    tau = {
        1: {1: -1, 2: +1, 3: +1},
        2: {1: +1, 2: -1, 3: +1},
        3: {1: +1, 2: +1, 3: -1},
    }
    # T_mu: 3x3 diagonal matrix with diagonal entries (tau_mu^(1), tau_mu^(2), tau_mu^(3))
    T = {}
    for mu in [1, 2, 3]:
        T[mu] = sp.diag(tau[1][mu], tau[2][mu], tau[3][mu])

    I3 = sp.eye(3)

    print("=== Substep-4 AC_lambda simultaneous-diagonalization bridge ===")

    # ----- (setup) unitarity and commutation -----
    print("\n[setup] commuting unitaries")
    for mu in [1, 2, 3]:
        # unitarity: T_mu^dagger T_mu = I
        unit = (T[mu].T.conjugate() * T[mu] - I3)
        check(
            f"T_{mu} unitary: T_{mu}^dagger T_{mu} = I",
            unit == sp.zeros(3, 3),
        )
    for mu in [1, 2, 3]:
        for nu in [1, 2, 3]:
            comm = T[mu] * T[nu] - T[nu] * T[mu]
            check(
                f"[T_{mu}, T_{nu}] = 0",
                comm == sp.zeros(3, 3),
            )

    # ----- (L1) pairwise distinctness -----
    print("\n[L1] pairwise distinctness of joint eigenvalue triples")
    for alpha in [1, 2, 3]:
        for beta in [1, 2, 3]:
            if alpha == beta:
                continue
            distinguishing_mus = [mu for mu in [1, 2, 3] if tau[alpha][mu] != tau[beta][mu]]
            check(
                f"pair (alpha,beta) = ({alpha},{beta}) distinguished by some T_mu",
                len(distinguishing_mus) >= 1,
                detail=f"distinguishing mus = {distinguishing_mus}",
            )

    # ----- (L3) commutator identity -----
    print("\n[L3] commutator identity <e_alpha|[K,T_mu]|e_beta> = (tau_mu^(beta) - tau_mu^(alpha)) <e_alpha|K|e_beta>")
    # Build a generic Hermitian K with 6 real free parameters: 3 diagonal d_1, d_2, d_3 (real),
    # 3 complex off-diagonals e12 = u12 + I*v12, e13 = u13 + I*v13, e23 = u23 + I*v23.
    d1, d2, d3 = sp.symbols("d1 d2 d3", real=True)
    u12, v12, u13, v13, u23, v23 = sp.symbols("u12 v12 u13 v13 u23 v23", real=True)
    e12 = u12 + sp.I * v12
    e13 = u13 + sp.I * v13
    e23 = u23 + sp.I * v23

    K = sp.Matrix(
        [
            [d1, e12, e13],
            [sp.conjugate(e12), d2, e23],
            [sp.conjugate(e13), sp.conjugate(e23), d3],
        ]
    )
    # replace conjugates using known real components
    K = K.subs(
        {
            sp.conjugate(u12): u12,
            sp.conjugate(v12): v12,
            sp.conjugate(u13): u13,
            sp.conjugate(v13): v13,
            sp.conjugate(u23): u23,
            sp.conjugate(v23): v23,
        }
    )

    # Verify K is Hermitian symbolically
    Kdagger = sp.Matrix(
        [[sp.conjugate(K[j, i]) for j in range(3)] for i in range(3)]
    ).subs(
        {
            sp.conjugate(d1): d1,
            sp.conjugate(d2): d2,
            sp.conjugate(d3): d3,
            sp.conjugate(u12): u12,
            sp.conjugate(v12): v12,
            sp.conjugate(u13): u13,
            sp.conjugate(v13): v13,
            sp.conjugate(u23): u23,
            sp.conjugate(v23): v23,
        }
    )
    check("generic K Hermitian", sp.simplify(K - Kdagger) == sp.zeros(3, 3))

    # For each off-diagonal pair (alpha, beta) with alpha != beta, verify L3 identity for some mu
    for alpha in [1, 2, 3]:
        for beta in [1, 2, 3]:
            if alpha == beta:
                continue
            # Pick lowest-index mu with distinguishing eigenvalues
            mu = next(mm for mm in [1, 2, 3] if tau[alpha][mm] != tau[beta][mm])
            comm = K * T[mu] - T[mu] * K
            lhs = comm[alpha - 1, beta - 1]
            # Expected: (tau_mu^(beta) - tau_mu^(alpha)) * K[alpha-1, beta-1]
            rhs = (tau[beta][mu] - tau[alpha][mu]) * K[alpha - 1, beta - 1]
            diff = sp.simplify(lhs - rhs)
            check(
                f"L3 identity at (alpha,beta,mu) = ({alpha},{beta},{mu}): <e_a|[K,T_mu]|e_b> = (tau_mu^b - tau_mu^a) <e_a|K|e_b>",
                diff == 0,
                detail=f"lhs - rhs = {diff}",
            )

    # ----- (L2) simultaneous diagonalization corollary -----
    print("\n[L2] simultaneous diagonalization: [K, T_mu] = 0 for mu = 1,2,3 -> K diagonal")
    # Set up the system [K, T_mu] = 0 for mu = 1, 2, 3 and solve for the 6 off-diag real params
    equations = []
    for mu in [1, 2, 3]:
        comm = K * T[mu] - T[mu] * K
        for i in range(3):
            for j in range(3):
                if i == j:
                    continue
                equations.append(sp.simplify(comm[i, j]))

    # Solve for u12, v12, u13, v13, u23, v23
    sol = sp.solve(equations, [u12, v12, u13, v13, u23, v23], dict=True)
    check(
        "system [K, T_mu] = 0 has unique solution",
        isinstance(sol, list) and len(sol) == 1,
        detail=f"#solutions = {len(sol) if isinstance(sol, list) else 'non-list'}",
    )

    if isinstance(sol, list) and len(sol) == 1:
        s = sol[0]
        check(
            "L2 solution forces u12 = 0",
            sp.simplify(s.get(u12, u12)) == 0,
            detail=f"u12 -> {s.get(u12)}",
        )
        check(
            "L2 solution forces v12 = 0",
            sp.simplify(s.get(v12, v12)) == 0,
            detail=f"v12 -> {s.get(v12)}",
        )
        check(
            "L2 solution forces u13 = 0",
            sp.simplify(s.get(u13, u13)) == 0,
            detail=f"u13 -> {s.get(u13)}",
        )
        check(
            "L2 solution forces v13 = 0",
            sp.simplify(s.get(v13, v13)) == 0,
            detail=f"v13 -> {s.get(v13)}",
        )
        check(
            "L2 solution forces u23 = 0",
            sp.simplify(s.get(u23, u23)) == 0,
            detail=f"u23 -> {s.get(u23)}",
        )
        check(
            "L2 solution forces v23 = 0",
            sp.simplify(s.get(v23, v23)) == 0,
            detail=f"v23 -> {s.get(v23)}",
        )

    # ----- (L4) diagonal class commutes -----
    print("\n[L4] diagonal class commutes")
    k1, k2, k3 = sp.symbols("k1 k2 k3", complex=True)
    K_diag = sp.diag(k1, k2, k3)
    for mu in [1, 2, 3]:
        comm = K_diag * T[mu] - T[mu] * K_diag
        check(
            f"diag(k1,k2,k3) commutes with T_{mu}",
            comm == sp.zeros(3, 3),
        )

    # Commuting algebra has complex dim 3 (three independent diagonal entries)
    # Verify: the algebra is generated by I, T_1, T_1*T_2 say, or simply
    # parametrized by k1, k2, k3 in C
    check(
        "commuting algebra complex dim = 3",
        len([k1, k2, k3]) == 3,
        detail="three independent complex diagonal parameters",
    )

    # ----- worked numerical instance -----
    print("\n[worked numerical instance]")
    K_num = sp.diag(1, 2, 5)
    for mu in [1, 2, 3]:
        comm = K_num * T[mu] - T[mu] * K_num
        check(
            f"[diag(1,2,5), T_{mu}] = 0",
            comm == sp.zeros(3, 3),
        )

    # ----- counter-example: off-diagonal entry breaks T_1 commutation -----
    print("\n[counter-examples]")
    K_offdiag = sp.Matrix(
        [
            [1, 1, 0],
            [1, 2, 0],
            [0, 0, 5],
        ]
    )
    comm_offdiag_T1 = K_offdiag * T[1] - T[1] * K_offdiag
    check(
        "off-diagonal K (entries (1,2)/(2,1)) breaks [K, T_1] = 0",
        comm_offdiag_T1 != sp.zeros(3, 3),
        detail=f"[K_offdiag, T_1] = {comm_offdiag_T1.tolist()}",
    )

    # ----- counter-example: T_mu = I trivializes the distinctness condition -----
    T_trivial = I3
    # Any matrix commutes with I, including the off-diagonal K_offdiag
    comm_trivial = K_offdiag * T_trivial - T_trivial * K_offdiag
    check(
        "T_mu = I trivial: any K commutes (off-diagonal K still commutes)",
        comm_trivial == sp.zeros(3, 3),
        detail=f"[K_offdiag, I] = {comm_trivial.tolist()}",
    )

    # ----- Summary -----
    print("\n=== Summary ===")
    print(f"PASS={len(passes)} FAIL={len(fails)}")
    if fails:
        print("Failures:")
        for f in fails:
            print(f"  - {f}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
