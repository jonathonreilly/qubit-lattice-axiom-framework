"""Audit companion runner for the substep-4 AC_lambda simultaneous-
diagonalization bridge narrow theorem (2026-05-17).

Verifies with exact SymPy arithmetic that, for the explicit triple of
commuting diagonal unitary 3x3 matrices T_1, T_2, T_3 with joint
eigenvalue signatures

  tau^(1) = (-1, +1, +1),
  tau^(2) = (+1, -1, +1),
  tau^(3) = (+1, +1, -1),

the following statements are equivalent for a fully generic complex
operator K on V_3 = C^3:

  (i)  [K, T_mu] = 0 for mu = 1, 2, 3;
  (ii) all six ordered off-diagonal entries of K vanish.

The generic K has 18 independent real coordinates: independent real and
imaginary parts for all nine matrix entries.  No reality, Hermiticity,
normality, diagonality, sparsity, or relation between K_ab and K_ba is
assumed.

The equivalence is checked in two independent exact ways:

  1. solve the real and imaginary parts of all three commutator systems;
  2. build the 27x9 complex-linear commutator map
         K -> ([K,T_1], [K,T_2], [K,T_3])
     and verify rank 6 with kernel exactly span(E_11,E_22,E_33).

Under the theorem's pairwise-distinct joint-signature hypothesis, every
alpha != beta has exact separation weight

  sum_mu (tau_mu^(beta) - tau_mu^(alpha))^2

equal to 8, giving an entrywise reconstruction identity for K_ab from the
three commutators.  Directed, dense, and one-unitary-blind non-Hermitian
complex controls exercise the positive certificate across the quantified
operator space.  The original generic Hermitian specialization is retained
as a secondary continuity check.

Expected output: PASS=N FAIL=0 with N >= 50.
"""

from __future__ import annotations

import sympy as sp


INDICES = range(3)
MUS = (1, 2, 3)


def is_zero_matrix(matrix: sp.MatrixBase) -> bool:
    return all(sp.simplify(entry) == 0 for entry in matrix)


def dagger(matrix: sp.MatrixBase) -> sp.Matrix:
    return sp.Matrix(matrix).conjugate().T


def main() -> int:
    fails: list[str] = []
    passes: list[str] = []

    def check(label: str, ok: bool, detail: str = "") -> None:
        if bool(ok):
            passes.append(label)
            print(f"  PASS  {label}" + (f" :: {detail}" if detail else ""))
        else:
            fails.append(label)
            print(f"  FAIL  {label}" + (f" :: {detail}" if detail else ""))

    # tau^(alpha) is the joint eigenvalue signature on basis vector e_alpha.
    tau = {
        1: {1: -1, 2: +1, 3: +1},
        2: {1: +1, 2: -1, 3: +1},
        3: {1: +1, 2: +1, 3: -1},
    }
    signatures = {
        alpha: tuple(tau[alpha][mu] for mu in MUS)
        for alpha in (1, 2, 3)
    }
    T = {
        mu: sp.diag(*(tau[alpha][mu] for alpha in (1, 2, 3)))
        for mu in MUS
    }
    I3 = sp.eye(3)

    print("=== Substep-4 AC_lambda simultaneous-diagonalization bridge ===")

    # ----- Setup: explicit commuting-unitary triple -----
    print("\n[setup] explicit commuting unitary triple")
    for mu in MUS:
        check(
            f"T_{mu} unitary: T_{mu}^dagger T_{mu} = I",
            is_zero_matrix(dagger(T[mu]) * T[mu] - I3),
        )
    for mu in MUS:
        for nu in MUS:
            check(
                f"[T_{mu}, T_{nu}] = 0",
                is_zero_matrix(T[mu] * T[nu] - T[nu] * T[mu]),
            )

    # ----- (L1) pairwise-distinct signatures and exact separation -----
    print("\n[L1] theorem hypothesis: pairwise-distinct joint signatures")
    check(
        "the three joint eigenvalue signatures are pairwise distinct",
        len(set(signatures.values())) == 3,
        detail=f"signatures = {signatures}",
    )
    separation_weights: dict[tuple[int, int], int] = {}
    for alpha in (1, 2, 3):
        for beta in (1, 2, 3):
            if alpha == beta:
                continue
            deltas = tuple(tau[beta][mu] - tau[alpha][mu] for mu in MUS)
            distinguishing_mus = [
                mu for mu, delta in zip(MUS, deltas, strict=True) if delta != 0
            ]
            weight = sum(delta * delta for delta in deltas)
            separation_weights[(alpha, beta)] = weight
            check(
                f"ordered pair ({alpha},{beta}) has nonzero exact separation",
                bool(distinguishing_mus) and weight == 8,
                detail=(
                    f"deltas = {deltas}; distinguishing mus = "
                    f"{distinguishing_mus}; weight = {weight}"
                ),
            )

    # ----- Fully generic complex K: 18 independent real coordinates -----
    print("\n[generic complex K] no Hermiticity or other specialization")
    real_names = " ".join(
        f"a{i + 1}{j + 1}" for i in INDICES for j in INDICES
    )
    imag_names = " ".join(
        f"b{i + 1}{j + 1}" for i in INDICES for j in INDICES
    )
    real_coordinates = sp.symbols(real_names, real=True)
    imag_coordinates = sp.symbols(imag_names, real=True)
    K = sp.Matrix(
        3,
        3,
        lambda i, j: (
            real_coordinates[3 * i + j] + sp.I * imag_coordinates[3 * i + j]
        ),
    )
    all_coordinates = set(real_coordinates) | set(imag_coordinates)
    check(
        "K contains 18 independent real coordinates for nine complex entries",
        len(all_coordinates) == 18 and K.free_symbols == all_coordinates,
        detail=f"coordinate count = {len(K.free_symbols)}",
    )
    check(
        "opposite off-diagonal entries have disjoint coordinate sets",
        all(
            K[i, j].free_symbols.isdisjoint(K[j, i].free_symbols)
            for i in INDICES
            for j in INDICES
            if i < j
        ),
        detail="no K_ba = conjugate(K_ab) or K_ba = K_ab constraint",
    )
    check(
        "generic K is not identically Hermitian",
        not is_zero_matrix(K - dagger(K)),
    )

    commutators = {
        mu: sp.simplify(K * T[mu] - T[mu] * K)
        for mu in MUS
    }

    # ----- (L3) exact entry identities and signature-weight reconstruction -----
    print("\n[L3] exact commutator-entry and reconstruction identities")
    for mu in MUS:
        expected = sp.Matrix(
            3,
            3,
            lambda i, j: (
                (tau[j + 1][mu] - tau[i + 1][mu]) * K[i, j]
            ),
        )
        check(
            f"full entry identity for [K,T_{mu}]",
            is_zero_matrix(commutators[mu] - expected),
        )

    for alpha in (1, 2, 3):
        for beta in (1, 2, 3):
            if alpha == beta:
                continue
            i = alpha - 1
            j = beta - 1
            weighted_commutator_entry = sp.expand(
                sum(
                    (tau[beta][mu] - tau[alpha][mu])
                    * commutators[mu][i, j]
                    for mu in MUS
                )
            )
            weight = separation_weights[(alpha, beta)]
            check(
                f"reconstruct K_{alpha}{beta} from all three commutators",
                sp.simplify(weighted_commutator_entry - weight * K[i, j]) == 0
                and weight != 0,
                detail=f"sum_mu Delta_mu [K,T_mu]_{alpha}{beta} = {weight} K_{alpha}{beta}",
            )

    # ----- (L2) solve all three systems over independent real/imag parts -----
    print("\n[L2] generic complex commutator solve")
    off_diagonal_coordinates: list[sp.Symbol] = []
    diagonal_coordinates: set[sp.Symbol] = set()
    for i in INDICES:
        for j in INDICES:
            coords = (
                real_coordinates[3 * i + j],
                imag_coordinates[3 * i + j],
            )
            if i == j:
                diagonal_coordinates.update(coords)
            else:
                off_diagonal_coordinates.extend(coords)

    real_equations: list[sp.Expr] = []
    for mu in MUS:
        for entry in commutators[mu]:
            real_part, imag_part = sp.expand_complex(entry).as_real_imag()
            real_equations.extend((sp.expand(real_part), sp.expand(imag_part)))
    nonzero_real_equations = [
        equation for equation in real_equations if equation != 0
    ]
    equation_symbols = set().union(
        *(equation.free_symbols for equation in nonzero_real_equations)
    )

    check(
        "three commutator systems expose all 12 off-diagonal real coordinates",
        set(off_diagonal_coordinates) == equation_symbols
        and len(off_diagonal_coordinates) == 12,
        detail=(
            f"equations = {len(nonzero_real_equations)}; "
            f"off-diagonal coordinates = {len(off_diagonal_coordinates)}"
        ),
    )
    check(
        "all six diagonal real coordinates remain absent and free",
        diagonal_coordinates.isdisjoint(equation_symbols)
        and len(diagonal_coordinates) == 6,
    )

    solution = sp.solve(
        nonzero_real_equations,
        off_diagonal_coordinates,
        dict=True,
    )
    check(
        "generic complex system has one off-diagonal solution",
        isinstance(solution, list) and len(solution) == 1,
        detail=f"#solutions = {len(solution) if isinstance(solution, list) else 'non-list'}",
    )
    generic_solution = solution[0] if len(solution) == 1 else {}
    for coordinate in off_diagonal_coordinates:
        check(
            f"generic solve forces {coordinate} = 0",
            sp.simplify(generic_solution.get(coordinate, coordinate)) == 0,
            detail=f"{coordinate} -> {generic_solution.get(coordinate)}",
        )

    solved_commutators = {
        mu: commutators[mu].subs(generic_solution)
        for mu in MUS
    }
    off_diagonal_zero_substitution = {
        coordinate: 0 for coordinate in off_diagonal_coordinates
    }
    check(
        "commuting with the triple implies every off-diagonal complex entry vanishes",
        len(generic_solution) == 12
        and all(is_zero_matrix(matrix) for matrix in solved_commutators.values()),
    )
    check(
        "vanishing off-diagonal entries implies commuting with the triple",
        all(
            is_zero_matrix(commutators[mu].subs(off_diagonal_zero_substitution))
            for mu in MUS
        ),
    )

    # ----- Independent exact linear-map rank/kernel certificate -----
    print("\n[independent certificate] rank and kernel of the commutator map")
    basis_labels: list[tuple[int, int]] = []
    image_columns: list[sp.Matrix] = []
    for i in INDICES:
        for j in INDICES:
            basis_labels.append((i + 1, j + 1))
            E_ij = sp.zeros(3, 3)
            E_ij[i, j] = 1
            image_entries: list[sp.Expr] = []
            for mu in MUS:
                image_entries.extend(list(E_ij * T[mu] - T[mu] * E_ij))
            image_columns.append(sp.Matrix(image_entries))
    commutator_map = sp.Matrix.hstack(*image_columns)
    rank = commutator_map.rank()
    nullspace = commutator_map.nullspace()
    pivot_columns = commutator_map.rref()[1]
    pivot_labels = {basis_labels[index] for index in pivot_columns}
    expected_off_diagonal_labels = {
        (i + 1, j + 1)
        for i in INDICES
        for j in INDICES
        if i != j
    }
    diagonal_coordinate_vectors = []
    for index in (0, 4, 8):
        vector = sp.zeros(9, 1)
        vector[index, 0] = 1
        diagonal_coordinate_vectors.append(vector)
    diagonal_kernel_basis = sp.Matrix.hstack(*diagonal_coordinate_vectors)
    computed_kernel_basis = sp.Matrix.hstack(*nullspace)

    check(
        "commutator map has exact shape 27x9",
        commutator_map.shape == (27, 9),
    )
    check(
        "commutator map has exact complex rank 6",
        rank == 6,
        detail=f"rank = {rank}",
    )
    check(
        "the six pivot directions are exactly the off-diagonal E_ab",
        pivot_labels == expected_off_diagonal_labels,
        detail=f"pivot labels = {sorted(pivot_labels)}",
    )
    check(
        "commutator-map nullity is exactly 3",
        len(nullspace) == 3,
        detail=f"nullity = {len(nullspace)}",
    )
    check(
        "each diagonal matrix unit lies in the kernel",
        all(
            is_zero_matrix(commutator_map * vector)
            for vector in diagonal_coordinate_vectors
        ),
    )
    check(
        "the computed kernel equals span(E_11,E_22,E_33)",
        computed_kernel_basis.rank() == 3
        and diagonal_kernel_basis.rank() == 3
        and sp.Matrix.hstack(
            computed_kernel_basis,
            diagonal_kernel_basis,
        ).rank() == 3,
    )

    # ----- Original Hermitian specialization retained as a continuity check -----
    print("\n[continuity check] original generic Hermitian specialization")
    d1, d2, d3 = sp.symbols("d1 d2 d3", real=True)
    u12, v12, u13, v13, u23, v23 = sp.symbols(
        "u12 v12 u13 v13 u23 v23",
        real=True,
    )
    K_hermitian = sp.Matrix(
        [
            [d1, u12 + sp.I * v12, u13 + sp.I * v13],
            [u12 - sp.I * v12, d2, u23 + sp.I * v23],
            [u13 - sp.I * v13, u23 - sp.I * v23, d3],
        ]
    )
    check(
        "generic Hermitian specialization is Hermitian",
        is_zero_matrix(K_hermitian - dagger(K_hermitian)),
    )
    hermitian_off_diagonal = [u12, v12, u13, v13, u23, v23]
    hermitian_equations: list[sp.Expr] = []
    for mu in MUS:
        commutator = K_hermitian * T[mu] - T[mu] * K_hermitian
        for entry in commutator:
            real_part, imag_part = sp.expand_complex(entry).as_real_imag()
            hermitian_equations.extend((sp.expand(real_part), sp.expand(imag_part)))
    hermitian_solution = sp.solve(
        [equation for equation in hermitian_equations if equation != 0],
        hermitian_off_diagonal,
        dict=True,
    )
    check(
        "Hermitian specialization has one off-diagonal solution",
        len(hermitian_solution) == 1,
        detail=f"#solutions = {len(hermitian_solution)}",
    )
    check(
        "Hermitian specialization forces all six off-diagonal real components to zero",
        len(hermitian_solution) == 1
        and all(
            sp.simplify(hermitian_solution[0].get(variable, variable)) == 0
            for variable in hermitian_off_diagonal
        ),
    )

    # ----- (L4) diagonal class and complex positive controls -----
    print("\n[L4] exact diagonal commutant")
    k1, k2, k3 = sp.symbols("k1 k2 k3", complex=True)
    K_diagonal = sp.diag(k1, k2, k3)
    for mu in MUS:
        check(
            f"diag(k1,k2,k3) commutes with T_{mu}",
            is_zero_matrix(K_diagonal * T[mu] - T[mu] * K_diagonal),
        )
    check(
        "commuting algebra has complex dimension 3",
        rank == 6 and len(nullspace) == 3,
    )

    K_complex_diagonal = sp.diag(
        1 + 2 * sp.I,
        -3 + sp.I,
        4 - 5 * sp.I,
    )
    check(
        "commuting complex diagonal control is non-Hermitian",
        not is_zero_matrix(K_complex_diagonal - dagger(K_complex_diagonal)),
    )
    check(
        "complex diagonal non-Hermitian control commutes with the full triple",
        all(
            is_zero_matrix(K_complex_diagonal * T[mu] - T[mu] * K_complex_diagonal)
            for mu in MUS
        ),
    )

    K_worked = sp.diag(1, 2, 5)
    for mu in MUS:
        check(
            f"[diag(1,2,5), T_{mu}] = 0",
            is_zero_matrix(K_worked * T[mu] - T[mu] * K_worked),
        )

    # ----- Hostile deterministic complex controls -----
    print("\n[hostile complex controls]")
    K_directed = sp.zeros(3, 3)
    K_directed[0, 1] = 1 + 2 * sp.I
    directed_commutators = {
        mu: K_directed * T[mu] - T[mu] * K_directed
        for mu in MUS
    }
    check(
        "directed E_12 control lies outside the previous Hermitian ansatz",
        K_directed[0, 1] != 0
        and K_directed[1, 0] == 0
        and not is_zero_matrix(K_directed - dagger(K_directed)),
        detail="K_12 is nonzero while K_21 = 0",
    )
    check(
        "the full commutator mechanism rejects that non-Hermitian direction",
        not is_zero_matrix(directed_commutators[1])
        and not is_zero_matrix(directed_commutators[2])
        and is_zero_matrix(directed_commutators[3]),
        detail="coverage outside the old ansatz with the expected nonzero commutators",
    )

    K_dense_hostile = sp.Matrix(
        [
            [1 + 2 * sp.I, 2 - sp.I, -3 + 4 * sp.I],
            [5 + 7 * sp.I, -2 + sp.I, 6 - 5 * sp.I],
            [4 - 3 * sp.I, -8 + 2 * sp.I, 9 - sp.I],
        ]
    )
    dense_commutators = {
        mu: K_dense_hostile * T[mu] - T[mu] * K_dense_hostile
        for mu in MUS
    }
    check(
        "dense hostile K is complex, non-Hermitian, and has all six off-diagonal entries nonzero",
        not is_zero_matrix(K_dense_hostile - dagger(K_dense_hostile))
        and all(
            K_dense_hostile[i, j] != 0
            for i in INDICES
            for j in INDICES
            if i != j
        ),
    )
    check(
        "every dense hostile off-diagonal entry is detected by the triple",
        all(
            any(dense_commutators[mu][i, j] != 0 for mu in MUS)
            for i in INDICES
            for j in INDICES
            if i != j
        ),
    )
    check(
        "dense hostile K is detected by all three commutator systems",
        all(not is_zero_matrix(dense_commutators[mu]) for mu in MUS),
        detail=(
            f"nonzero counts = "
            f"{ {mu: sum(entry != 0 for entry in dense_commutators[mu]) for mu in MUS} }"
        ),
    )

    # T_1 has a +1 eigenspace span(e_2,e_3), so it cannot alone detect
    # mixing inside that block.  T_2 and T_3 do detect it.
    K_T1_blind = sp.diag(1 + sp.I, 2 - sp.I, 3 + 2 * sp.I)
    K_T1_blind[1, 2] = 2 + 3 * sp.I
    K_T1_blind[2, 1] = -4 + sp.I
    blind_commutators = {
        mu: K_T1_blind * T[mu] - T[mu] * K_T1_blind
        for mu in MUS
    }
    check(
        "one-unitary-blind control is non-Hermitian",
        not is_zero_matrix(K_T1_blind - dagger(K_T1_blind)),
    )
    check(
        "mixing inside the degenerate +1 eigenspace commutes with T_1",
        is_zero_matrix(blind_commutators[1]),
    )
    check(
        "the same mixing is detected by T_2 and T_3",
        not is_zero_matrix(blind_commutators[2])
        and not is_zero_matrix(blind_commutators[3]),
    )

    # ----- Summary -----
    print("\n=== Summary ===")
    print(f"PASS={len(passes)} FAIL={len(fails)}")
    if fails:
        print("Failures:")
        for failure in fails:
            print(f"  - {failure}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
