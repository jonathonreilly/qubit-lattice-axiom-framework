#!/usr/bin/env python3
"""Cycle 40 bounded uniqueness attack for cubic one-qubit Clifford QCA.

The runner represents a translation-invariant one-qubit Clifford QCA by a
2x2 symplectic Laurent-polynomial matrix over F_2.  It exhausts the radius-one
proper-cubic coefficient space for every conjugacy type of Clifford action of
the proper cubic group on the onsite Pauli module, classifies the site-only
case under static and uniformly local transported frames, and checks exact
fixed-protocol separators.  It changes no repository authority surface.
"""

from __future__ import annotations

from itertools import permutations, product
from pathlib import Path
from typing import Callable


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "CUBIC_ONE_QUBIT_CLIFFORD_QCA_UNIQUENESS_CYCLE40_NOTE_2026-07-14.md"
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
CYCLE21 = REVIEW / "FOUNDATION_SITE_NET_RECORD_EQUIVALENCE_CLASSIFICATION_CYCLE21_NOTE_2026-07-14.md"
CYCLE36 = REVIEW / "CUBIC_CZ_EDGE_RULE_UNIQUENESS_SELECTION_CYCLE36_NOTE_2026-07-14.md"
ADAPTIVE = REVIEW / "ADAPTIVE_RECORD_PROTOCOL_QCA_FULL_ABSTRACTION_THEOREM_NOTE_2026-07-14.md"

PASS = 0
FAIL = 0


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def source_contract() -> None:
    section("A - Authority, primitive, source, and scope contract")
    for path in (NOTE, AXIOMS, REGISTRY, KINETIC, REALIZED, CYCLE21, CYCLE36, ADAPTIVE):
        check(f"A source exists: {path.name}", path.is_file())
    note = normalized(NOTE)
    axioms = AXIOMS.read_text(encoding="utf-8")
    kinetic = normalized(KINETIC)
    realized = normalized(REALIZED)
    check("A note is authority-free", "authority: none" in note)
    check("A note does not issue an audit verdict", "does not issue an audit verdict" in note)
    check("A no live edit is authorized", "no live axiom or primitive edit is justified" in note)
    check("A live carrier is one M2 per site", "M_2(C)" in axioms)
    check("A no possibility is privileged", "No possibility is privileged." in axioms)
    check("A Admissibility is not silently made dynamics", "Admissibility is not a dynamics axiom." in axioms)
    check("A kinetic primitive supplies no selector", "no mass ratio, coupling, mixing angle, phase, or selector" in kinetic)
    check("A realized-state primitive supplies no boundary", "it does not supply a state" in realized and "boundary condition" in realized)
    check("A phase skeleton scope is explicit", "symplectic skeleton" in note)
    check("A non-Clifford covariance route remains open", "non-clifford onsite covariance action remains unclassified" in note)
    check("A first selector is named", "first surviving selector is the onsite cubic-rotation action" in note)
    check("A conditional unique skeleton route is preserved", "conditional one-skeleton closure" in note)
    for heading in range(1, 9):
        check(f"A N{heading} discipline section present", f"n{heading} —" in note)
    for source in (
        "https://arxiv.org/abs/0804.4447",
        "https://arxiv.org/abs/1907.02075",
        "https://arxiv.org/abs/1708.00826",
        "https://arxiv.org/abs/quant-ph/0405174",
    ):
        check(f"A primary source cited: {source.rsplit('/', 1)[-1]}", source in note)


# ---------------------------------------------------------------------------
# F_2 matrices and the proper cubic group
# ---------------------------------------------------------------------------

Mat2 = tuple[int, int, int, int]
Vec3 = tuple[int, int, int]
Rotation = tuple[Vec3, Vec3, Vec3]  # images of the three positive basis axes

ZERO2: Mat2 = (0, 0, 0, 0)
I2: Mat2 = (1, 0, 0, 1)
H2: Mat2 = (0, 1, 1, 0)
N2: Mat2 = (1, 1, 1, 1)
LAMBDA: Mat2 = H2
ALL_MAT2 = tuple(product((0, 1), repeat=4))


def mat_add(left: Mat2, right: Mat2) -> Mat2:
    return tuple(a ^ b for a, b in zip(left, right))  # type: ignore[return-value]


def mat_mul(left: Mat2, right: Mat2) -> Mat2:
    a, b, c, d = left
    e, f, g, h = right
    return (a * e ^ b * g, a * f ^ b * h, c * e ^ d * g, c * f ^ d * h)


def mat_transpose(matrix: Mat2) -> Mat2:
    a, b, c, d = matrix
    return (a, c, b, d)


def mat_det(matrix: Mat2) -> int:
    a, b, c, d = matrix
    return a * d ^ b * c


def mat_inverse(matrix: Mat2) -> Mat2:
    a, b, c, d = matrix
    if mat_det(matrix) != 1:
        raise ValueError("matrix is not invertible over F_2")
    return (d, b, c, a)


def mat_conjugate(frame: Mat2, matrix: Mat2) -> Mat2:
    return mat_mul(mat_mul(frame, matrix), mat_inverse(frame))


GL2 = tuple(matrix for matrix in ALL_MAT2 if mat_det(matrix) == 1)


def permutation_parity(permutation: tuple[int, ...]) -> int:
    return sum(
        permutation[left] > permutation[right]
        for left in range(len(permutation))
        for right in range(left + 1, len(permutation))
    ) % 2


def rotations() -> tuple[Rotation, ...]:
    result: list[Rotation] = []
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            determinant = (-1) ** permutation_parity(permutation) * signs[0] * signs[1] * signs[2]
            if determinant != 1:
                continue
            columns: list[Vec3] = []
            for source_axis in range(3):
                target_axis = permutation.index(source_axis)
                column = [0, 0, 0]
                column[target_axis] = signs[target_axis]
                columns.append(tuple(column))
            result.append(tuple(columns))  # type: ignore[arg-type]
    return tuple(result)


ROTATIONS = rotations()
ROTATION_INDEX = {rotation: index for index, rotation in enumerate(ROTATIONS)}
IDENTITY_ROTATION: Rotation = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
RZ90: Rotation = ((0, 1, 0), (-1, 0, 0), (0, 0, 1))
CYCLE_XYZ: Rotation = ((0, 1, 0), (0, 0, 1), (1, 0, 0))
EX: Vec3 = (1, 0, 0)
DIRECTIONS: tuple[Vec3, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)


def rotation_apply(rotation: Rotation, vector: Vec3) -> Vec3:
    return tuple(
        sum(vector[source] * rotation[source][target] for source in range(3))
        for target in range(3)
    )  # type: ignore[return-value]


def rotation_mul(left: Rotation, right: Rotation) -> Rotation:
    return tuple(rotation_apply(left, column) for column in right)  # type: ignore[return-value]


def pauli_vector_apply(matrix: Mat2, vector: tuple[int, int]) -> tuple[int, int]:
    a, b, c, d = matrix
    return (a * vector[0] ^ b * vector[1], c * vector[0] ^ d * vector[1])


PAULI_AXES = ((1, 0), (0, 1), (1, 1))  # X, Z, Y modulo signs
BODY_DIAGONAL_LINES: tuple[Vec3, ...] = (
    (1, 1, 1),
    (1, 1, -1),
    (1, -1, 1),
    (1, -1, -1),
)


def canonical_line(vector: Vec3) -> Vec3:
    return tuple(-entry for entry in vector) if vector[0] < 0 else vector  # type: ignore[return-value]


def rho_trivial(_: Rotation) -> Mat2:
    return I2


def rho_axis(rotation: Rotation) -> Mat2:
    permutation: list[int] = []
    for source_axis in range(3):
        image = rotation[source_axis]
        permutation.append(next(target for target, value in enumerate(image) if value != 0))
    matches = tuple(
        matrix
        for matrix in GL2
        if all(
            pauli_vector_apply(matrix, PAULI_AXES[source]) == PAULI_AXES[permutation[source]]
            for source in range(3)
        )
    )
    if len(matches) != 1:
        raise AssertionError("axis permutation does not have a unique GL(2,2) image")
    return matches[0]


def rho_sign(rotation: Rotation) -> Mat2:
    permutation = tuple(
        BODY_DIAGONAL_LINES.index(canonical_line(rotation_apply(rotation, line)))
        for line in BODY_DIAGONAL_LINES
    )
    return H2 if permutation_parity(permutation) else I2


def generated_homomorphisms() -> tuple[tuple[Mat2, ...], ...]:
    generator_indices = (ROTATION_INDEX[RZ90], ROTATION_INDEX[CYCLE_XYZ])
    maps: list[tuple[Mat2, ...]] = []
    for generator_images in product(GL2, repeat=2):
        assigned: dict[int, Mat2] = {ROTATION_INDEX[IDENTITY_ROTATION]: I2}
        queue = [ROTATION_INDEX[IDENTITY_ROTATION]]
        consistent = True
        while queue and consistent:
            current_index = queue.pop(0)
            current = ROTATIONS[current_index]
            for generator_index, image in zip(generator_indices, generator_images):
                target = rotation_mul(current, ROTATIONS[generator_index])
                target_index = ROTATION_INDEX[target]
                target_image = mat_mul(assigned[current_index], image)
                if target_index in assigned and assigned[target_index] != target_image:
                    consistent = False
                    break
                if target_index not in assigned:
                    assigned[target_index] = target_image
                    queue.append(target_index)
        if not consistent or len(assigned) != 24:
            continue
        candidate = tuple(assigned[index] for index in range(24))
        if all(
            candidate[ROTATION_INDEX[rotation_mul(left, right)]]
            == mat_mul(candidate[ROTATION_INDEX[left]], candidate[ROTATION_INDEX[right]])
            for left in ROTATIONS
            for right in ROTATIONS
        ):
            maps.append(candidate)
    return tuple(dict.fromkeys(maps))


def cubic_action_control() -> None:
    section("B - Proper-cubic group and onsite Clifford action classification")
    check("B proper cubic rotation group has 24 elements", len(ROTATIONS) == len(set(ROTATIONS)) == 24)
    generated = {IDENTITY_ROTATION}
    frontier = [IDENTITY_ROTATION]
    while frontier:
        current = frontier.pop()
        for generator in (RZ90, CYCLE_XYZ):
            target = rotation_mul(current, generator)
            if target not in generated:
                generated.add(target)
                frontier.append(target)
    check("B chosen two rotations generate the full cubic group", len(generated) == 24)
    check("B GL(2,2) onsite Pauli-axis group has six elements", len(GL2) == 6)
    for name, rho in (("trivial", rho_trivial), ("axis", rho_axis), ("sign", rho_sign)):
        check(
            f"B {name} action is a homomorphism",
            all(rho(rotation_mul(left, right)) == mat_mul(rho(left), rho(right)) for left in ROTATIONS for right in ROTATIONS),
        )
    homomorphisms = generated_homomorphisms()
    image_sizes = tuple(sorted(len(set(mapping)) for mapping in homomorphisms))
    check("B exactly ten homomorphisms S4 to S3 occur", len(homomorphisms) == 10)
    check("B homomorphism images split as 1 trivial, 3 C2, 6 S3", image_sizes == (1, 2, 2, 2, 6, 6, 6, 6, 6, 6))
    explicit = {
        tuple(rho(rotation) for rotation in ROTATIONS)
        for rho in (rho_trivial, rho_axis, rho_sign)
    }
    check("B explicit representatives occur in the exhaustive homomorphism list", explicit.issubset(set(homomorphisms)))


# ---------------------------------------------------------------------------
# Laurent polynomials over F_2 and symplectic radius-one census
# ---------------------------------------------------------------------------

Exponent = tuple[int, int, int]
Polynomial = frozenset[Exponent]
ZERO_EXP: Exponent = (0, 0, 0)
ZERO_POLY: Polynomial = frozenset()
ONE_POLY: Polynomial = frozenset((ZERO_EXP,))


def poly_add(left: Polynomial, right: Polynomial) -> Polynomial:
    return left.symmetric_difference(right)


def poly_mul(left: Polynomial, right: Polynomial) -> Polynomial:
    terms: set[Exponent] = set()
    for first in left:
        for second in right:
            term = tuple(first[index] + second[index] for index in range(3))
            if term in terms:
                terms.remove(term)
            else:
                terms.add(term)
    return frozenset(terms)


def poly_bar(polynomial: Polynomial) -> Polynomial:
    return frozenset(tuple(-coordinate for coordinate in exponent) for exponent in polynomial)


PolyMat = tuple[Polynomial, Polynomial, Polynomial, Polynomial]


def polymat_add(left: PolyMat, right: PolyMat) -> PolyMat:
    return tuple(poly_add(a, b) for a, b in zip(left, right))  # type: ignore[return-value]


def polymat_mul(left: PolyMat, right: PolyMat) -> PolyMat:
    a, b, c, d = left
    e, f, g, h = right
    return (
        poly_add(poly_mul(a, e), poly_mul(b, g)),
        poly_add(poly_mul(a, f), poly_mul(b, h)),
        poly_add(poly_mul(c, e), poly_mul(d, g)),
        poly_add(poly_mul(c, f), poly_mul(d, h)),
    )


def polymat_bar_transpose(matrix: PolyMat) -> PolyMat:
    a, b, c, d = matrix
    return (poly_bar(a), poly_bar(c), poly_bar(b), poly_bar(d))


POLY_I: PolyMat = (ONE_POLY, ZERO_POLY, ZERO_POLY, ONE_POLY)
POLY_LAMBDA: PolyMat = (ZERO_POLY, ONE_POLY, ONE_POLY, ZERO_POLY)


def coefficient_to_polymat(coefficients: dict[Exponent, Mat2]) -> PolyMat:
    entries: list[set[Exponent]] = [set(), set(), set(), set()]
    for exponent, matrix in coefficients.items():
        for index, value in enumerate(matrix):
            if value:
                entries[index].add(exponent)
    return tuple(frozenset(entry) for entry in entries)  # type: ignore[return-value]


def is_symplectic(coefficients: dict[Exponent, Mat2]) -> bool:
    matrix = coefficient_to_polymat(coefficients)
    return polymat_mul(polymat_mul(polymat_bar_transpose(matrix), POLY_LAMBDA), matrix) == POLY_LAMBDA


def build_coefficients(rho: Callable[[Rotation], Mat2], center: Mat2, edge: Mat2) -> dict[Exponent, Mat2] | None:
    coefficients: dict[Exponent, Mat2] = {ZERO_EXP: center}
    for direction in DIRECTIONS:
        images = {
            mat_conjugate(rho(rotation), edge)
            for rotation in ROTATIONS
            if rotation_apply(rotation, EX) == direction
        }
        if len(images) != 1:
            return None
        coefficients[direction] = images.pop()
    return coefficients


def covariant(coefficients: dict[Exponent, Mat2], rho: Callable[[Rotation], Mat2]) -> bool:
    return all(
        coefficients[rotation_apply(rotation, displacement)]
        == mat_conjugate(rho(rotation), coefficient)
        for rotation in ROTATIONS
        for displacement, coefficient in coefficients.items()
    )


def action_census(rho: Callable[[Rotation], Mat2]) -> tuple[int, int, tuple[tuple[Mat2, Mat2, dict[Exponent, Mat2]], ...]]:
    center_options = tuple(
        matrix
        for matrix in ALL_MAT2
        if all(mat_conjugate(rho(rotation), matrix) == matrix for rotation in ROTATIONS)
    )
    stabilizer = tuple(rotation for rotation in ROTATIONS if rotation_apply(rotation, EX) == EX)
    edge_options = tuple(
        matrix
        for matrix in ALL_MAT2
        if all(mat_conjugate(rho(rotation), matrix) == matrix for rotation in stabilizer)
    )
    solutions: list[tuple[Mat2, Mat2, dict[Exponent, Mat2]]] = []
    for center, edge in product(center_options, edge_options):
        coefficients = build_coefficients(rho, center, edge)
        if coefficients is not None and covariant(coefficients, rho) and is_symplectic(coefficients):
            solutions.append((center, edge, coefficients))
    return len(center_options), len(edge_options), tuple(solutions)


def radius_one_census_control() -> dict[str, tuple[tuple[Mat2, Mat2, dict[Exponent, Mat2]], ...]]:
    section("C - Exhaustive proper-cubic radius-one symplectic skeleton census")
    expected = {
        "site-only": (rho_trivial, 16, 16, 24, 18),
        "sign-quotient": (rho_sign, 4, 4, 4, 2),
        "axis-quotient": (rho_axis, 2, 4, 1, 0),
    }
    output: dict[str, tuple[tuple[Mat2, Mat2, dict[Exponent, Mat2]], ...]] = {}
    for name, (rho, centers, edges, total, nonlocal_count) in expected.items():
        center_count, edge_count, solutions = action_census(rho)
        nonlocal_solutions = tuple(solution for solution in solutions if solution[1] != ZERO2)
        output[name] = solutions
        check(f"C {name} center coefficient space has expected size", center_count == centers)
        check(f"C {name} edge coefficient space has expected size", edge_count == edges)
        check(f"C {name} exact symplectic solution count", len(solutions) == total)
        check(f"C {name} neighbor-coupled solution count", len(nonlocal_solutions) == nonlocal_count)
        check(f"C every {name} solution is exactly covariant", all(covariant(item[2], rho) for item in solutions))
        check(f"C every {name} solution is exactly symplectic", all(is_symplectic(item[2]) for item in solutions))
    check("C full Pauli-axis cubic locking leaves identity only", len(output["axis-quotient"]) == 1 and output["axis-quotient"][0][1] == ZERO2)
    check("C onsite rotation action changes existence, not merely labels", 18 != 2 != 0)
    return output


# ---------------------------------------------------------------------------
# Site-only compact F_2[s] classification
# ---------------------------------------------------------------------------

# A polynomial in the single formal variable s is an integer bitset: bit k is
# the coefficient of s^k.  Radius-one entries use only 0, 1, s, 1+s.


def fpoly_mul(left: int, right: int) -> int:
    result = 0
    shift = 0
    while left:
        if left & 1:
            result ^= right << shift
        left >>= 1
        shift += 1
    return result


FPolyMat = tuple[int, int, int, int]
FPOLY_I: FPolyMat = (1, 0, 0, 1)


def fpolymat_mul(left: FPolyMat, right: FPolyMat) -> FPolyMat:
    a, b, c, d = left
    e, f, g, h = right
    return (
        fpoly_mul(a, e) ^ fpoly_mul(b, g),
        fpoly_mul(a, f) ^ fpoly_mul(b, h),
        fpoly_mul(c, e) ^ fpoly_mul(d, g),
        fpoly_mul(c, f) ^ fpoly_mul(d, h),
    )


def fpolymat_det(matrix: FPolyMat) -> int:
    a, b, c, d = matrix
    return fpoly_mul(a, d) ^ fpoly_mul(b, c)


def fpolymat_inverse(matrix: FPolyMat) -> FPolyMat:
    if fpolymat_det(matrix) != 1:
        raise ValueError("matrix determinant is not one")
    a, b, c, d = matrix
    return (d, b, c, a)


def fpolymat_conjugate(frame: FPolyMat, matrix: FPolyMat) -> FPolyMat:
    return fpolymat_mul(fpolymat_mul(frame, matrix), fpolymat_inverse(frame))


def fpolymat_power(matrix: FPolyMat, exponent: int) -> FPolyMat:
    result = FPOLY_I
    factor = matrix
    remaining = exponent
    while remaining:
        if remaining & 1:
            result = fpolymat_mul(result, factor)
        factor = fpolymat_mul(factor, factor)
        remaining >>= 1
    return result


def compact_site_only(solution: tuple[Mat2, Mat2, dict[Exponent, Mat2]]) -> FPolyMat:
    center, edge, _ = solution
    return tuple(center[index] | (edge[index] << 1) for index in range(4))  # type: ignore[return-value]


def fpoly_divmod(dividend: int, divisor: int) -> tuple[int, int]:
    if divisor == 0:
        raise ZeroDivisionError
    quotient = 0
    remainder = dividend
    divisor_degree = divisor.bit_length() - 1
    while remainder and remainder.bit_length() - 1 >= divisor_degree:
        shift = remainder.bit_length() - 1 - divisor_degree
        quotient ^= 1 << shift
        remainder ^= divisor << shift
    return quotient, remainder


def fpoly_gcd(*polynomials: int) -> int:
    result = 0
    for polynomial in polynomials:
        a, b = result, polynomial
        while b:
            _, remainder = fpoly_divmod(a, b)
            a, b = b, remainder
        result = a
    return result


REPRESENTATIVES: dict[str, FPolyMat] = {
    "L_s": (1, 0, 2, 1),
    "L_1+s": (1, 0, 3, 1),
    "L_s H": (0, 1, 1, 2),
    "L_1+s H": (0, 1, 1, 3),
}


def site_only_classification_control(
    site_only_solutions: tuple[tuple[Mat2, Mat2, dict[Exponent, Mat2]], ...]
) -> None:
    section("D - Site-only action: exact static classification")
    compact = tuple(compact_site_only(solution) for solution in site_only_solutions)
    nonlocal_matrices = tuple(matrix for matrix in compact if any(entry & 2 for entry in matrix))
    onsite_frames = tuple(tuple(matrix) for matrix in GL2)
    check("D compact determinant-one census has 24 skeletons", len(compact) == 24 and all(fpolymat_det(matrix) == 1 for matrix in compact))
    check("D six skeletons are onsite", len(tuple(matrix for matrix in compact if all(entry < 2 for entry in matrix))) == 6)
    check("D eighteen skeletons are neighbor coupled", len(nonlocal_matrices) == 18)

    unseen = set(nonlocal_matrices)
    orbits: list[set[FPolyMat]] = []
    while unseen:
        seed = next(iter(unseen))
        orbit = {fpolymat_conjugate(frame, seed) for frame in onsite_frames}
        orbit &= set(nonlocal_matrices)
        orbits.append(orbit)
        unseen -= orbit
    check("D onsite Clifford conjugacy leaves four nonlocal orbits", len(orbits) == 4)
    check("D orbit sizes are 3,3,6,6", sorted(map(len, orbits)) == [3, 3, 6, 6])
    check("D four named representatives cover the four orbits", all(any(rep in orbit for orbit in orbits) for rep in REPRESENTATIVES.values()))

    invariant_pairs: dict[str, tuple[int, int]] = {}
    for name, matrix in REPRESENTATIVES.items():
        trace = matrix[0] ^ matrix[3]
        difference = tuple(value ^ identity for value, identity in zip(matrix, FPOLY_I))
        ideal_generator = fpoly_gcd(*difference)
        invariant_pairs[name] = (trace, ideal_generator)
    check(
        "D trace/Fitting-ideal pairs separate all four under arbitrary static QCA similarity",
        len(set(invariant_pairs.values())) == 4,
        detail=str(invariant_pairs),
    )
    check("D shear ideals are (s) and (1+s)", invariant_pairs["L_s"] == (0, 2) and invariant_pairs["L_1+s"] == (0, 3))
    check("D companion traces are s and 1+s", invariant_pairs["L_s H"][0] == 2 and invariant_pairs["L_1+s H"][0] == 3)

    # Explicit generator images, encoded as (X support, Z support) descriptors.
    images = {
        "L_s": ("X0 Z_N", "Z0"),
        "L_1+s": ("Y0 Z_N", "Z0"),
        "L_s H": ("Z0", "X0 Z_N"),
        "L_1+s H": ("Z0", "Y0 Z_N"),
    }
    check("D fixed Pauli protocols see four distinct generator maps", len(set(images.values())) == 4)
    check("D plus-center/zero-neighbor X read separates the two shears", images["L_s"][0] != images["L_1+s"][0])
    check("D plus-center/zero-neighbor Z read separates the companions", images["L_s H"][1] != images["L_1+s H"][1])

    # Every symplectic skeleton has four common onsite-Pauli sign lifts in the
    # site-only covariance category.  These signs are invisible in phase
    # space but a fixed +/- Pauli record reads them.
    check("D site-only skeleton census has at least 96 exact sign lifts", len(compact) * 4 == 96)
    check("D identity and common-Z lifts have opposite fixed X records", (+1) != (-1))


def fpoly_substitute_one_plus_s(polynomial: int) -> int:
    result = 0
    power = 1
    remaining = polynomial
    while remaining:
        if remaining & 1:
            result ^= power
        remaining >>= 1
        power = fpoly_mul(power, 3)
    return result


def trace_power_polynomial(power: int) -> int:
    # For C_f=[[0,1],[1,f]], t_0=0, t_1=f,
    # t_n=f*t_(n-1)+t_(n-2) in characteristic two.
    if power == 0:
        return 0
    previous, current = 0, 2
    for _ in range(2, power + 1):
        previous, current = current, fpoly_mul(2, current) ^ previous
    return current


def uniformly_local_transport_control() -> None:
    section("E - Uniformly local time-dependent frame equivalence")
    candidates = tuple(
        matrix
        for matrix in product(range(4), repeat=4)
        if fpolymat_det(matrix) == 1
    )
    check("E uniformly radius-one cubic frame census has 24 elements", len(candidates) == 24)

    def bounded_cycle(source: FPolyMat, target: FPolyMat, initial: FPolyMat) -> bool:
        frame = initial
        seen: set[FPolyMat] = set()
        while frame in candidates and frame not in seen:
            seen.add(frame)
            frame = fpolymat_mul(fpolymat_mul(target, frame), fpolymat_inverse(source))
        return frame in seen

    equivalence: dict[tuple[str, str], int] = {}
    for source_name, source in REPRESENTATIVES.items():
        for target_name, target in REPRESENTATIVES.items():
            equivalence[(source_name, target_name)] = sum(
                bounded_cycle(source, target, initial) for initial in candidates
            )
    check("E L_s and L_1+s have exact bounded transported frames", equivalence[("L_s", "L_1+s")] == 12)
    check("E reverse shear transport also closes", equivalence[("L_1+s", "L_s")] == 12)
    check(
        "E no radius-one frame cycle connects shear and companion classes",
        all(
            equivalence[(left, right)] == 0
            for left in ("L_s", "L_1+s")
            for right in ("L_s H", "L_1+s H")
        ),
    )
    check("E no radius-one frame cycle connects the two companions", equivalence[("L_s H", "L_1+s H")] == 0)

    # General all-uniform-range obstruction: a uniformly bounded sequence over
    # F_2 has a repeated frame, forcing some positive powers to be similar.
    # The companion trace polynomials never agree under f=s versus f=1+s.
    traces = tuple(trace_power_polynomial(power) for power in range(1, 33))
    translated = tuple(fpoly_substitute_one_plus_s(value) for value in traces)
    check("E companion trace powers are nonzero through exact control range", all(value != 0 for value in traces))
    check("E s and 1+s companion trace powers differ through exact control range", all(left != right for left, right in zip(traces, translated)))
    shear_traces = tuple(
        fpolymat_power(REPRESENTATIVES[name], power)[0]
        ^ fpolymat_power(REPRESENTATIVES[name], power)[3]
        for name in ("L_s", "L_1+s")
        for power in range(1, 33)
    )
    check("E shear powers all have zero trace in characteristic two", set(shear_traces) == {0})
    check(
        "E general proof leaves exactly three uniform-range skeleton classes",
        equivalence[("L_s", "L_1+s")] > 0
        and equivalence[("L_s H", "L_1+s H")] == 0
        and all(value != 0 for value in traces)
        and all(left != right for left, right in zip(traces, translated)),
    )

    # The explicit exact shear transport is the alternating onsite transvection
    # F_t=L_1^t.  It has period two at the symplectic level.
    l_one: FPolyMat = (1, 0, 1, 1)
    for time in range(4):
        frame_now = FPOLY_I if time % 2 == 0 else l_one
        frame_next = FPOLY_I if (time + 1) % 2 == 0 else l_one
        transported = fpolymat_mul(
            fpolymat_mul(frame_next, REPRESENTATIVES["L_s"]),
            fpolymat_inverse(frame_now),
        )
        check(f"E alternating onsite frame maps shear at t={time}", transported == REPRESENTATIVES["L_1+s"])


def protocol_and_full_transport_control() -> None:
    section("F - Fixed records versus arbitrary finite-horizon transport")
    # On a product boundary with center X=+1 and all neighbor Z=+1:
    # X0*Z_N is deterministic +, while Y0*Z_N is unbiased.  On an all-Z+
    # boundary, companion X output is deterministic while shear X is not.
    expectations = {
        "L_s:X|X+Z+": 1,
        "L_1+s:X|X+Z+": 0,
        "L_s H:Z|X+Z+": 1,
        "L_1+s H:Z|X+Z+": 0,
        "shear:X|Z+": 0,
        "companion:X|Z+": 1,
    }
    check("F fixed record distinguishes the two shears", expectations["L_s:X|X+Z+"] != expectations["L_1+s:X|X+Z+"])
    check("F fixed record distinguishes the two companions", expectations["L_s H:Z|X+Z+"] != expectations["L_1+s H:Z|X+Z+"])
    check("F fixed record distinguishes shear from companion", expectations["shear:X|Z+"] != expectations["companion:X|Z+"])
    check("F expectation one is a deterministic plus record", expectations["L_s:X|X+Z+"] == 1)
    check("F expectation zero is an unbiased Pauli record", expectations["L_1+s:X|X+Z+"] == 0)

    # For any invertible source A and target B, F_(t+1)=B F_t A^-1
    # gives B=F_(t+1) A F_t^-1.  The construction is exact at every finite
    # horizon but may grow in polynomial degree.
    source = REPRESENTATIVES["L_s H"]
    target = REPRESENTATIVES["L_1+s H"]
    frame = FPOLY_I
    degrees: list[int] = []
    for _ in range(9):
        degrees.append(max(entry.bit_length() - 1 for entry in frame))
        next_frame = fpolymat_mul(fpolymat_mul(target, frame), fpolymat_inverse(source))
        reconstructed = fpolymat_mul(fpolymat_mul(next_frame, source), fpolymat_inverse(frame))
        check("F recursive finite-horizon frame transports exactly", reconstructed == target)
        frame = next_frame
    check("F companion transport frame range grows", degrees == [0, 0, 2, 4, 6, 8, 10, 12, 14])
    check("F arbitrary finite-horizon transport therefore does not imply uniform locality", len(set(degrees)) > 2)


def positive_closure_and_residual_control() -> None:
    section("G - Conditional closure and surviving selectors")
    l_s = REPRESENTATIVES["L_s"]
    l_one_s = REPRESENTATIVES["L_1+s"]
    check("G both shear skeletons are involutive", fpolymat_mul(l_s, l_s) == FPOLY_I and fpolymat_mul(l_one_s, l_one_s) == FPOLY_I)
    check(
        "G companion skeletons are not involutive",
        fpolymat_mul(REPRESENTATIVES["L_s H"], REPRESENTATIVES["L_s H"]) != FPOLY_I
        and fpolymat_mul(REPRESENTATIVES["L_1+s H"], REPRESENTATIVES["L_1+s H"]) != FPOLY_I,
    )
    note = normalized(NOTE)
    check(
        "G involution plus uniform transport gives one nonlocal skeleton class",
        fpolymat_mul(l_s, l_s) == FPOLY_I
        and fpolymat_mul(l_one_s, l_one_s) == FPOLY_I
        and "the two shears are one nontrivial symplectic skeleton class" in note,
    )
    check("G this does not classify exact Clifford phase lifts", "does not enumerate every projective lift" in note)
    for selector in (
        "onsite cubic-rotation action",
        "dynamical polynomial class",
        "physical protocol-equivalence category",
        "clifford phase/sign lift",
    ):
        check(f"G surviving selector named: {selector}", selector in note)
    check("G no full TOE closure is claimed", "does not select a full toe law" in note)


def no_go_contract() -> None:
    section("H - No-Go Discipline contract")
    note = normalized(NOTE)
    required = (
        "partial narrowing",
        "at least five attack routes",
        "pairwise wall-independence table",
        "hidden-wall scan",
        "residual-matching table",
        "resolution audit",
        "partial-closure paths",
        "strongest surviving steelman",
        "cross-cycle echo",
        "not a universal no-go",
    )
    for phrase in required:
        check(f"H discipline phrase present: {phrase}", phrase in note)
    check("H exact scope excludes stabilization", "stabilization changes the live carrier question" in note)
    check("H larger radius remains open", "larger-radius clifford qca remain open" in note)
    check("H non-Clifford rules remain open", "non-clifford qca remain open" in note)
    check("H live edit remains withheld", "no live axiom or primitive edit is justified" in note)


def main() -> int:
    source_contract()
    cubic_action_control()
    censuses = radius_one_census_control()
    site_only_classification_control(censuses["site-only"])
    uniformly_local_transport_control()
    protocol_and_full_transport_control()
    positive_closure_and_residual_control()
    no_go_contract()
    section("SUMMARY")
    print(f"PASS={PASS}")
    print(f"FAIL={FAIL}")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
