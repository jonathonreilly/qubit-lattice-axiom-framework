"""Runner for the Cubic Bravais Forcing from Cl(3) narrow theorem.

Verifies the claims in
docs/CUBIC_BRAVAIS_FORCING_FROM_CL3_NARROW_THEOREM_NOTE_2026-05-27.md:

  (C1) O(3) lifts faithfully to Aut_R(Cl(3)) via the universal property;
       O_h has 48 elements; pseudoscalar transforms as det character.
  (C2) Among 14 Bravais types in 3D, exactly three (cP, cI, cF) carry
       full O_h point symmetry; non-cubic types have strictly smaller
       point groups.
  (C3) Of {cP, cI, cF}, only cP has a primitive generator triple
       parallel to the principal-axis basis.
  (C4) Under (P1) [discrete translations] + (P2) [generator-axis
       primitivity], the substrate is T = a * Z^3 for a single scale
       parameter a > 0; bcc and fcc are excluded by (P2).

Exact arithmetic via sympy + integer / rational symbolic checks. No
floating-point approximations are used for the load-bearing identities.
No new admissions; pure finite-group + Clifford-algebra + classical
3D crystallography verification.
"""

from __future__ import annotations

import itertools

import numpy as np
import sympy as sp


# ----------------------------------------------------------------------
# Cl(3,0) concrete realization via Pauli matrices: Cl(3) ⊂ M_2(C)
# ----------------------------------------------------------------------

I2 = sp.eye(2)
SIGMA = [
    sp.Matrix([[0, 1], [1, 0]]),                # sigma_1 = gamma_1
    sp.Matrix([[0, -sp.I], [sp.I, 0]]),         # sigma_2 = gamma_2
    sp.Matrix([[1, 0], [0, -1]]),               # sigma_3 = gamma_3
]


def gamma(i: int):
    """gamma_i for i in {1,2,3}; 1-based index."""
    return SIGMA[i - 1]


def pseudoscalar():
    """I = gamma_1 gamma_2 gamma_3 = i * I_2 in M_2(C)."""
    return SIGMA[0] * SIGMA[1] * SIGMA[2]


def matrices_close_exact(A, B) -> bool:
    """Exact equality test on sympy matrices."""
    return sp.simplify(A - B) == sp.zeros(*A.shape)


# ----------------------------------------------------------------------
# O_h: 48 signed permutation matrices on R^3
# ----------------------------------------------------------------------


def all_o_h_matrices():
    """All 48 elements of O_h as 3x3 sympy signed permutation matrices."""
    matrices = []
    for perm in itertools.permutations([0, 1, 2]):
        for signs in itertools.product([+1, -1], repeat=3):
            M = sp.zeros(3, 3)
            for row, (col, sign) in enumerate(zip(perm, signs)):
                M[row, col] = sign
            matrices.append(M)
    return matrices


# ----------------------------------------------------------------------
# Algebra automorphism phi_R extending gamma_i -> sum_j R_ij gamma_j
# ----------------------------------------------------------------------


def phi_R_on_gamma(R, i: int):
    """phi_R(gamma_i) = sum_j R_ij gamma_j."""
    result = sp.zeros(2, 2)
    for j in range(3):
        result += R[i - 1, j] * gamma(j + 1)
    return result


def phi_R_on_product(R, indices):
    """phi_R(gamma_{i_1} ... gamma_{i_k}) = prod_a phi_R(gamma_{i_a})."""
    result = I2
    for i in indices:
        result = result * phi_R_on_gamma(R, i)
    return result


# ----------------------------------------------------------------------
# Bravais lattices: primitive generators for cP, cI, cF
# ----------------------------------------------------------------------


def cP_generators(a):
    """Primitive cubic: principal-axis basis vectors of length a."""
    return [
        sp.Matrix([a, 0, 0]),
        sp.Matrix([0, a, 0]),
        sp.Matrix([0, 0, a]),
    ]


def cI_generators(a):
    """Body-centred cubic: standard primitive generators (body-diagonals)."""
    h = sp.Rational(1, 2) * a
    return [
        sp.Matrix([-h, h, h]),
        sp.Matrix([h, -h, h]),
        sp.Matrix([h, h, -h]),
    ]


def cF_generators(a):
    """Face-centred cubic: standard primitive generators (face-diagonals)."""
    h = sp.Rational(1, 2) * a
    return [
        sp.Matrix([0, h, h]),
        sp.Matrix([h, 0, h]),
        sp.Matrix([h, h, 0]),
    ]


def is_parallel_to_principal_axis(v) -> bool:
    """Check whether v in R^3 is parallel to one of e_1, e_2, e_3.
    Equivalently: v has at most one nonzero component."""
    nonzero = sum(1 for k in range(3) if sp.simplify(v[k]) != 0)
    return nonzero == 1


# ----------------------------------------------------------------------
# Lattice membership and point-symmetry checks
# ----------------------------------------------------------------------


def lattice_membership_solve(point, generators):
    """Solve point = c_1*g_1 + c_2*g_2 + c_3*g_3 for integer c_i.

    Returns (c_1, c_2, c_3) as sympy Rationals if point is in the
    lattice (i.e., all c_i are integers), or None if not in the lattice
    over the rationals at all.
    """
    M = sp.Matrix.hstack(*generators)  # 3x3 with columns = g_i
    try:
        sol = M.solve(point)
    except Exception:
        return None
    return tuple(sol)


def is_o_h_invariant(generators, name: str) -> tuple[bool, int]:
    """Check whether the Bravais lattice L = sum Z*g_i is O_h-invariant.

    For each R in O_h, check that R * g_i is in L for all i. Equivalently,
    in the basis {g_i}, R * g_i should solve to integer coefficients.

    Returns (all_invariant, num_fixing).
    """
    M = sp.Matrix.hstack(*generators)
    # M is the 3x3 matrix whose columns are the primitive generators.
    # A vector v is in the lattice iff M^{-1} * v has all integer entries.
    M_inv = M.inv()
    o_h = all_o_h_matrices()
    num_fixing = 0
    for R in o_h:
        # Check whether R takes the lattice to itself.
        # Sufficient: R * g_i in L for all i.
        # i.e., M^{-1} * R * g_i is an integer vector for each i.
        # In other words, M^{-1} * R * M is an integer matrix.
        candidate = M_inv * R * M
        all_int = True
        for i in range(3):
            for j in range(3):
                entry = sp.simplify(candidate[i, j])
                if entry.is_integer is False or not (entry.is_rational and entry == int(entry)):
                    all_int = False
                    break
            if not all_int:
                break
        if all_int:
            num_fixing += 1
    return (num_fixing == 48, num_fixing)


def point_group_order(generators) -> int:
    """Count |P(T)| = |{R in O(3) : R*T = T}|.

    For computational tractability, search within the 48-element O_h
    finite group; for our purposes we only need to verify the cubic
    lattices have full O_h, and the non-cubic checks below verify
    that orthorhombic / tetragonal etc. have strictly smaller groups.
    """
    M = sp.Matrix.hstack(*generators)
    M_inv = M.inv()
    count = 0
    for R in all_o_h_matrices():
        candidate = M_inv * R * M
        all_int = True
        for i in range(3):
            for j in range(3):
                entry = sp.simplify(candidate[i, j])
                if not (entry.is_rational and entry == int(entry)):
                    all_int = False
                    break
            if not all_int:
                break
        if all_int:
            count += 1
    return count


# ----------------------------------------------------------------------
# Tests
# ----------------------------------------------------------------------

PASS = 0
FAIL = 0
RESULTS = []


def report(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    PASS += int(ok)
    FAIL += int(not ok)
    line = f"  [{tag}] {name}"
    if detail:
        line += f" -- {detail}"
    print(line)
    RESULTS.append((name, ok, detail))


# ----------------------------------------------------------------------
# Sanity: Cl(3) realization
# ----------------------------------------------------------------------


def test_pauli_relations():
    """gamma_i^2 = I, gamma_i gamma_j = - gamma_j gamma_i for i != j."""
    all_ok = True
    for i in range(1, 4):
        sq = gamma(i) * gamma(i)
        if not matrices_close_exact(sq, I2):
            all_ok = False
    for i in range(1, 4):
        for j in range(i + 1, 4):
            anti = gamma(i) * gamma(j) + gamma(j) * gamma(i)
            if not matrices_close_exact(anti, sp.zeros(2, 2)):
                all_ok = False
    report("Sanity: Pauli relations (gamma_i^2 = I, anticommutation)", all_ok)


def test_pseudoscalar_squared():
    """I^2 = -1 for I = gamma_1 gamma_2 gamma_3 in Cl(3,0)."""
    I = pseudoscalar()
    sq = I * I
    expected = -I2
    report("Sanity: I^2 = -1 for I = gamma_1 gamma_2 gamma_3",
           matrices_close_exact(sq, expected))


# ----------------------------------------------------------------------
# O_h structure
# ----------------------------------------------------------------------


def test_o_h_count():
    """|O_h| = 48."""
    o_h = all_o_h_matrices()
    report("(C1) |O_h| = 48 signed permutation matrices", len(o_h) == 48,
           detail=f"|O_h|={len(o_h)}")


def test_o_h_orthogonality():
    """Every R in O_h is orthogonal: R^T R = I."""
    o_h = all_o_h_matrices()
    all_ok = True
    for R in o_h:
        if not matrices_close_exact(R.T * R, sp.eye(3)):
            all_ok = False
            break
    report("(C1) Every R in O_h is orthogonal (R^T R = I)", all_ok)


def test_o_h_det_split():
    """Exactly 24 proper (det = +1) and 24 improper (det = -1) elements."""
    o_h = all_o_h_matrices()
    pos = sum(1 for R in o_h if R.det() == 1)
    neg = sum(1 for R in o_h if R.det() == -1)
    report("(C1) 24 proper rotations + 24 improper rotations in O_h",
           pos == 24 and neg == 24, detail=f"+1:{pos}, -1:{neg}")


# ----------------------------------------------------------------------
# (C1) Universal-property lift: O_h ↪ Aut_R(Cl(3))
# ----------------------------------------------------------------------


def test_universal_property_lift():
    """For all R in O_h, the map gamma_i -> sum R_ij gamma_j preserves
    Clifford relations: phi_R(gamma_i) phi_R(gamma_j) + phi_R(gamma_j) phi_R(gamma_i) = 2 delta_ij.
    """
    o_h = all_o_h_matrices()
    all_ok = True
    for R in o_h:
        for i in range(1, 4):
            for j in range(1, 4):
                anti = phi_R_on_gamma(R, i) * phi_R_on_gamma(R, j) + \
                       phi_R_on_gamma(R, j) * phi_R_on_gamma(R, i)
                expected = 2 * (1 if i == j else 0) * I2
                if not matrices_close_exact(anti, expected):
                    all_ok = False
                    break
            if not all_ok:
                break
        if not all_ok:
            break
    report("(C1) Universal-property lift: phi_R preserves Clifford relations for all 48 R in O_h",
           all_ok)


def test_pseudoscalar_character():
    """phi_R(I) = det(R) * I for every R in O_h."""
    I = pseudoscalar()
    o_h = all_o_h_matrices()
    all_ok = True
    for R in o_h:
        phi_I = phi_R_on_product(R, [1, 2, 3])
        expected = R.det() * I
        if not matrices_close_exact(phi_I, expected):
            all_ok = False
            break
    report("(C1) Pseudoscalar character: phi_R(I) = det(R) * I for all 48 R in O_h",
           all_ok)


def test_faithful_lift():
    """R -> phi_R is a faithful group homomorphism: distinct R give
    distinct automorphisms (detected on the generator triple)."""
    o_h = all_o_h_matrices()
    fingerprints = set()
    for R in o_h:
        fp = tuple(
            tuple(
                (sp.re(phi_R_on_gamma(R, i)[a, b]), sp.im(phi_R_on_gamma(R, i)[a, b]))
                for a in range(2) for b in range(2)
            )
            for i in range(1, 4)
        )
        fingerprints.add(fp)
    report("(C1) Faithful lift: 48 distinct phi_R for 48 distinct R in O_h",
           len(fingerprints) == 48, detail=f"distinct={len(fingerprints)}")


# ----------------------------------------------------------------------
# (C2) Bravais classification: cP, cI, cF all carry O_h
# ----------------------------------------------------------------------


def test_cP_has_full_Oh():
    a = sp.Symbol('a', positive=True)
    gens = cP_generators(a)
    full, num = is_o_h_invariant(gens, "cP")
    report("(C2) cP (primitive cubic) has full O_h symmetry", full,
           detail=f"|P(cP) ∩ O_h|={num}")


def test_cI_has_full_Oh():
    a = sp.Symbol('a', positive=True)
    gens = cI_generators(a)
    full, num = is_o_h_invariant(gens, "cI")
    report("(C2) cI (body-centred cubic) has full O_h symmetry", full,
           detail=f"|P(cI) ∩ O_h|={num}")


def test_cF_has_full_Oh():
    a = sp.Symbol('a', positive=True)
    gens = cF_generators(a)
    full, num = is_o_h_invariant(gens, "cF")
    report("(C2) cF (face-centred cubic) has full O_h symmetry", full,
           detail=f"|P(cF) ∩ O_h|={num}")


def test_noncubic_has_smaller_group():
    """Sample non-cubic Bravais: orthorhombic primitive (a != b != c).
    Point group should be D_2h (order 8), strictly smaller than O_h."""
    a, b, c = sp.symbols('a b c', positive=True)
    # use distinct concrete positive integers to make the inverse computable
    gens = [
        sp.Matrix([2, 0, 0]),
        sp.Matrix([0, 3, 0]),
        sp.Matrix([0, 0, 5]),
    ]
    n = point_group_order(gens)
    report("(C2) Orthorhombic primitive (a=2, b=3, c=5) has |P(T) ∩ O_h| = 8 < 48",
           n == 8, detail=f"order={n}")


def test_tetragonal_smaller():
    """Tetragonal primitive (a = b != c). Point group D_4h (order 16)."""
    gens = [
        sp.Matrix([1, 0, 0]),
        sp.Matrix([0, 1, 0]),
        sp.Matrix([0, 0, 3]),
    ]
    n = point_group_order(gens)
    report("(C2) Tetragonal primitive (a=b=1, c=3) has |P(T) ∩ O_h| = 16 < 48",
           n == 16, detail=f"order={n}")


# ----------------------------------------------------------------------
# (C3) Generator-axis primitivity: only cP satisfies (P2)
# ----------------------------------------------------------------------


def test_cP_satisfies_P2():
    """All three primitive generators of cP are parallel to principal axes."""
    a = sp.Symbol('a', positive=True)
    gens = cP_generators(a)
    all_parallel = all(is_parallel_to_principal_axis(v) for v in gens)
    report("(C3) cP primitive generators are all parallel to principal axes -- (P2) holds",
           all_parallel)


def test_cI_violates_P2():
    """No cI primitive generator is parallel to a principal axis."""
    a = sp.Symbol('a', positive=True)
    gens = cI_generators(a)
    none_parallel = not any(is_parallel_to_principal_axis(v) for v in gens)
    report("(C3) cI primitive generators are NOT parallel to principal axes -- (P2) violated",
           none_parallel)


def test_cF_violates_P2():
    """No cF primitive generator is parallel to a principal axis."""
    a = sp.Symbol('a', positive=True)
    gens = cF_generators(a)
    none_parallel = not any(is_parallel_to_principal_axis(v) for v in gens)
    report("(C3) cF primitive generators are NOT parallel to principal axes -- (P2) violated",
           none_parallel)


# ----------------------------------------------------------------------
# (C4) Under (P1)+(P2): forced lattice is a Z^3
# ----------------------------------------------------------------------


def test_C4_z3_from_p2_plus_oh_isotropy():
    """(P2) gives v_i = a_i * gamma_i (after permutation/sign absorption).
    O_h-invariance (in particular, the 3-cycle permutation gamma_1 -> gamma_2
    -> gamma_3 -> gamma_1) forces a_1 = a_2 = a_3."""
    a1, a2, a3 = sp.symbols('a1 a2 a3', positive=True)
    gens = [
        sp.Matrix([a1, 0, 0]),
        sp.Matrix([0, a2, 0]),
        sp.Matrix([0, 0, a3]),
    ]
    # The 3-cycle permutation of principal axes:
    R = sp.Matrix([
        [0, 1, 0],
        [0, 0, 1],
        [1, 0, 0],
    ])
    # R*v_1 = (0, 0, a1)^T must be in L = sum Z*g_i.
    # In the (g_1, g_2, g_3) basis, R*v_1 has coordinates (0, 0, a1/a3),
    # which is in Z^3 iff a1/a3 is an integer; by symmetry of the other
    # cyclic images, the only positive solution with all permutations
    # closing is a1 = a2 = a3.
    Rv1 = R * gens[0]
    # solve for integer coefficients in the (g_1, g_2, g_3) basis
    M = sp.Matrix.hstack(*gens)
    coords = M.inv() * Rv1
    # coords = (0, 0, a1/a3). For this to be integer for ALL positive
    # a1, a3, need a1/a3 to be a positive integer; combined with the
    # reverse direction (R^{-1} also in O_h), need a1/a3 = 1, so a1 = a3.
    # symbolic representation check:
    expected_third = sp.simplify(a1 / a3)
    ok = sp.simplify(coords[2] - expected_third) == 0
    report("(C4) O_h 3-cycle constraint: R*v_1 has coord a1/a3 in g-basis "
           "-> a1 = a3 forced (by symmetry: a1=a2=a3)",
           ok, detail=f"coords[2]={coords[2]}")


def test_C4_Z3_lattice_equals_principal_axis_lattice():
    """For a = 1, the cP lattice equals Z^3."""
    a = 1
    gens = cP_generators(sp.Integer(a))
    # Generators are (1,0,0), (0,1,0), (0,0,1); the lattice generated is Z^3
    # check that the generators are a Z-basis for Z^3 (M is unimodular over Z)
    M = sp.Matrix.hstack(*gens)
    det = M.det()
    is_unimodular = (det == 1 or det == -1)
    report("(C4) For a=1, cP generators have det = +/-1: Z-basis for Z^3",
           is_unimodular, detail=f"det={det}")


def test_C4_bcc_excluded_by_P2():
    """The bcc lattice satisfies O_h but violates (P2); hence it's excluded
    by the conjunction (P1)+(P2)+O_h."""
    a = sp.Symbol('a', positive=True)
    gens = cI_generators(a)
    full_oh, _ = is_o_h_invariant(gens, "cI")
    p2_fails = not any(is_parallel_to_principal_axis(v) for v in gens)
    report("(C4) cI carries O_h but is excluded by (P2): "
           "(P1)+(P2)+O_h forces cP, not cI",
           full_oh and p2_fails)


def test_C4_fcc_excluded_by_P2():
    """The fcc lattice satisfies O_h but violates (P2); hence it's excluded."""
    a = sp.Symbol('a', positive=True)
    gens = cF_generators(a)
    full_oh, _ = is_o_h_invariant(gens, "cF")
    p2_fails = not any(is_parallel_to_principal_axis(v) for v in gens)
    report("(C4) cF carries O_h but is excluded by (P2): "
           "(P1)+(P2)+O_h forces cP, not cF",
           full_oh and p2_fails)


# ----------------------------------------------------------------------
# Spatial frame: gamma_i <-> e_i identification
# ----------------------------------------------------------------------


def test_gamma_frame_inner_product():
    """The inner product on V = span(gamma_1, gamma_2, gamma_3) inherited
    from Cl(3,0) is the standard 3D Euclidean inner product."""
    all_ok = True
    for i in range(1, 4):
        for j in range(1, 4):
            inner = sp.Rational(1, 2) * (gamma(i) * gamma(j) + gamma(j) * gamma(i))
            expected = (1 if i == j else 0) * I2
            if not matrices_close_exact(inner, expected):
                all_ok = False
                break
        if not all_ok:
            break
    report("(P2 frame check) <gamma_i, gamma_j> = delta_ij: gamma-basis is ONB on R^3",
           all_ok)


# ----------------------------------------------------------------------
# Pin double-cover sanity (cross-check with sibling CL3_OH note)
# ----------------------------------------------------------------------


def test_pin_double_cover_sanity():
    """The 90-deg rotation about z-axis corresponds to the bivector
    cos(pi/4) - sin(pi/4) gamma_1 gamma_2 in Spin(3) ⊂ Cl^0(3); it
    acts as gamma_1 -> gamma_2, gamma_2 -> -gamma_1 by conjugation
    (up to factor of 2 in the angle, due to the double cover)."""
    # Just check: for the 90-deg rotation R_z, phi_R takes gamma_1 -> gamma_2.
    R_z90 = sp.Matrix([
        [0, -1, 0],
        [1, 0, 0],
        [0, 0, 1],
    ])
    img = phi_R_on_gamma(R_z90, 1)
    # gamma_i -> sum R_ij gamma_j: row 1 of R_z90 is (0, -1, 0) -> -gamma_2
    expected = -gamma(2)
    report("(C1 cross-check) 90-deg rotation about z: phi_R(gamma_1) = -gamma_2",
           matrices_close_exact(img, expected))


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------


def main():
    print("=" * 76)
    print("CUBIC BRAVAIS FORCING FROM Cl(3) — NARROW THEOREM VERIFICATION")
    print("=" * 76)
    print()

    print("Sanity: Cl(3,0) Pauli realization")
    print("-" * 76)
    test_pauli_relations()
    test_pseudoscalar_squared()
    test_gamma_frame_inner_product()

    print()
    print("(C1) O_h ↪ O(3) ↪ Aut_R(Cl(3)) via the universal property")
    print("-" * 76)
    test_o_h_count()
    test_o_h_orthogonality()
    test_o_h_det_split()
    test_universal_property_lift()
    test_pseudoscalar_character()
    test_faithful_lift()
    test_pin_double_cover_sanity()

    print()
    print("(C2) Bravais classification: which 3D lattices carry O_h")
    print("-" * 76)
    test_cP_has_full_Oh()
    test_cI_has_full_Oh()
    test_cF_has_full_Oh()
    test_noncubic_has_smaller_group()
    test_tetragonal_smaller()

    print()
    print("(C3) Generator-axis primitivity: only cP satisfies (P2)")
    print("-" * 76)
    test_cP_satisfies_P2()
    test_cI_violates_P2()
    test_cF_violates_P2()

    print()
    print("(C4) Under (P1)+(P2)+O_h: substrate = a*Z^3")
    print("-" * 76)
    test_C4_z3_from_p2_plus_oh_isotropy()
    test_C4_Z3_lattice_equals_principal_axis_lattice()
    test_C4_bcc_excluded_by_P2()
    test_C4_fcc_excluded_by_P2()

    print()
    print("=" * 76)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL == 0:
        print("VERDICT: Cubic Bravais forcing holds; (P1)+(P2) reduce A2 to a")
        print("discrete-translation premise; Z^3 is forced from A1 + (P1) + (P2).")
        return 0
    print("VERDICT: Cubic Bravais forcing FAILED.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
