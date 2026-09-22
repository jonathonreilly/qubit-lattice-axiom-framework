#!/usr/bin/env python3
"""Exact positive path/star identities and finite scope witnesses in supplied models."""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
AUDIT_INPUT_PATHS = (
    "docs/SEQUENTIAL_FORMATION_PATH_AND_STAR_IDENTITIES_BOUNDED_THEOREM_NOTE_2026-09-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
)
NOTE_PATH = ROOT / AUDIT_INPUT_PATHS[0]
AXIOM_PATH = ROOT / AUDIT_INPUT_PATHS[1]
REALIZED_PATH = ROOT / AUDIT_INPUT_PATHS[2]

Vector = tuple[int, int, int]
Rotation = tuple[tuple[int, int, int], tuple[int, int, int]]


def permutation_sign(permutation: tuple[int, int, int]) -> int:
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(3)
        for j in range(i + 1, 3)
    )
    return -1 if inversions % 2 else 1


ROTATIONS: tuple[Rotation, ...] = tuple(
    (permutation, signs)
    for permutation in permutations((0, 1, 2))
    for signs in product((-1, 1), repeat=3)
    if permutation_sign(permutation) * signs[0] * signs[1] * signs[2] == 1
)


def rotate_vector(rotation: Rotation, vector: Vector) -> Vector:
    permutation, signs = rotation
    result = [0, 0, 0]
    for source_axis in range(3):
        result[permutation[source_axis]] = signs[source_axis] * vector[source_axis]
    return tuple(result)  # type: ignore[return-value]


def normalize(text: str) -> str:
    return " ".join(text.split())


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, condition: bool, detail: str) -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        print(f"{'PASS' if ok else 'FAIL'}: {label} {detail}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


AXES: tuple[Vector, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)


def pair_orbit(left: Vector, right: Vector) -> str:
    dot = sum(a * b for a, b in zip(left, right, strict=True))
    if dot == 1:
        return "same"
    if dot == -1:
        return "opp"
    if dot == 0:
        return "orth"
    raise ValueError(dot)


def cubic_kernel_row(source: Vector, same: Fraction, opp: Fraction, orth: Fraction) -> dict[Vector, Fraction]:
    return {target: {"same": same, "opp": opp, "orth": orth}[pair_orbit(source, target)] for target in AXES}


def kernel_square_entry(
    source: Vector,
    target: Vector,
    same: Fraction,
    opp: Fraction,
    orth: Fraction,
) -> Fraction:
    total = Fraction(0)
    for mid in AXES:
        total += cubic_kernel_row(source, same, opp, orth)[mid] * cubic_kernel_row(mid, same, opp, orth)[target]
    return total


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    realized = REALIZED_PATH.read_text(encoding="utf-8")
    note_flat = normalize(note)
    axiom_flat = normalize(axiom)
    realized_flat = normalize(realized)

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print("scientific_dependency: current minimal_axioms Qubit/Admissibility/Record clauses and realized_state_primitive")
    print("declared_math: proper cubic rotations, finite Markov kernels, zonal moments on S^2")

    checks.check(
        "audit-input-paths",
        all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and len(AUDIT_INPUT_PATHS) == len(set(AUDIT_INPUT_PATHS)),
        "the note, axiom memo, and realized-state primitive are the declared source packet",
    )
    checks.check(
        "qubit-no-privilege",
        "No possibility is privileged. Possibilities are distinguished by the supplied algebraic structure alone."
        in axiom_flat,
        "Qubit forbids privileging possibilities beyond the one-site algebra",
    )
    checks.check(
        "qubit-cl3-no-extra",
        "A `Cl(3,0)`-compatible real-algebra presentation may be used equivalently and adds no further primitive structure."
        in axiom_flat,
        "the Cl(3,0) presentation adds no further primitive structure",
    )
    checks.check(
        "admissibility-clauses",
        "one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations"
        in axiom_flat
        and "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions."
        in axiom_flat,
        "Admissibility supplies one covariant rule that varies with neighbour conditions",
    )
    record_section = axiom.split("### Record / Fixed Reality", 1)[1].split(
        "## Qualification", 1
    )[0]
    checks.check(
        "record-form",
        "Records form." in record_section
        and "Only records are readable." in record_section,
        "Record supplies formation and readability of records only",
    )
    checks.check(
        "realized-state-no-average",
        "no averaging over alternatives" in realized_flat
        and "A value that would change under a different law-admissible realized state is registered data, not derivation output."
        in realized_flat,
        "the primitive supplies no averaging or process-law distribution",
    )
    checks.check(
        "note-contract",
        "**Type:** bounded_theorem" in note
        and "actual_current_surface_status: bounded-support" in note
        and "ends are independent" in note_flat
        and "K^2(.|L)=mu_0" in note_flat
        and "supplied mathematical hypotheses" in note_flat,
        "the note states conditional identities under supplied hypotheses",
    )
    checks.check(
        "note-dependency",
        "(MINIMAL_AXIOMS_2026-06-29.md)" in note
        and "(REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md)" in note,
        "current authorities delimit grants rather than supplying the process",
    )

    checks.check(
        "proper-cubic-group",
        len(ROTATIONS) == 24 and len(set(ROTATIONS)) == 24,
        "the determinant-positive signed-permutation group has 24 elements",
    )
    orbit = {rotate_vector(rotation, (1, 0, 0)) for rotation in ROTATIONS}
    checks.check(
        "six-axis-orbit",
        orbit == set(AXES) and len(AXES) == 6,
        "the proper cubic group is transitive on the six axis points",
    )
    averaged = {axis: Fraction(0) for axis in AXES}
    for rotation in ROTATIONS:
        averaged[rotate_vector(rotation, (1, 0, 0))] += Fraction(1, 24)
    checks.check(
        "unique-invariant-six-axis",
        all(weight == Fraction(1, 6) for weight in averaged.values())
        and sum(averaged.values()) == 1,
        "the cubic orbit average of any axis point mass is the uniform law 1/6",
    )

    # Two-state: K^2 independent of the start iff pplus = pminus.
    samples = (
        (Fraction(1, 2), Fraction(1, 2)),
        (Fraction(4, 5), Fraction(1, 5)),
        (Fraction(2, 3), Fraction(1, 4)),
        (Fraction(0), Fraction(1)),
        (Fraction(1), Fraction(0)),
        (Fraction(3, 10), Fraction(3, 10)),
    )

    def k2_plus_from_plus(pplus: Fraction, pminus: Fraction) -> Fraction:
        return pplus * pplus + (1 - pplus) * pminus

    def k2_plus_from_minus(pplus: Fraction, pminus: Fraction) -> Fraction:
        return pminus * pplus + (1 - pminus) * pminus

    identity_ok = all(
        k2_plus_from_plus(pplus, pminus) - k2_plus_from_minus(pplus, pminus)
        == (pplus - pminus) ** 2
        for pplus, pminus in samples
    )
    checks.check(
        "two-state-k2-residual",
        identity_ok,
        "K^2(+|+) - K^2(+|-) = (pplus - pminus)^2 on every sampled two-state kernel",
    )
    checks.check(
        "two-state-k2-constant-iff-independent",
        all(
            (k2_plus_from_plus(pplus, pminus) == k2_plus_from_minus(pplus, pminus))
            == (pplus == pminus)
            for pplus, pminus in samples
        ),
        "sampled two-state residual vanishes exactly for equal rows",
    )
    pplus, pminus = Fraction(4, 5), Fraction(1, 5)
    checks.check(
        "two-state-ising-k2-not-haar",
        k2_plus_from_plus(pplus, pminus) == Fraction(17, 25)
        and k2_plus_from_minus(pplus, pminus) == Fraction(8, 25)
        and k2_plus_from_plus(pplus, pminus) != k2_plus_from_minus(pplus, pminus),
        "the declared Ising one-neighbour kernel has K^2(+|+) = 17/25 against K^2(+|-) = 8/25",
    )

    # Path3 ends-first versus chain: (L,R) marginals.
    # Ends-first: L,R i.i.d. Bernoulli(1/2). Chain with Ising: not independent.
    def chain_lr_joint(pplus: Fraction, pminus: Fraction, p0: Fraction) -> dict[tuple[int, int], Fraction]:
        # L ~ p0, M | L, R | M. Return joint of (L,R).
        joint = {}
        for left, right in product((0, 1), repeat=2):
            total = Fraction(0)
            for mid in (0, 1):
                p_l = p0 if left == 1 else (1 - p0)
                if left == 1:
                    p_m = pplus if mid == 1 else (1 - pplus)
                else:
                    p_m = pminus if mid == 1 else (1 - pminus)
                if mid == 1:
                    p_r = pplus if right == 1 else (1 - pplus)
                else:
                    p_r = pminus if right == 1 else (1 - pminus)
                total += p_l * p_m * p_r
            joint[(left, right)] = total
        return joint

    def ends_lr_joint(p0: Fraction) -> dict[tuple[int, int], Fraction]:
        joint = {}
        for left, right in product((0, 1), repeat=2):
            p_l = p0 if left == 1 else (1 - p0)
            p_r = p0 if right == 1 else (1 - p0)
            joint[(left, right)] = p_l * p_r
        return joint

    p0 = Fraction(1, 2)
    chain_j = chain_lr_joint(Fraction(4, 5), Fraction(1, 5), p0)
    ends_j = ends_lr_joint(p0)
    checks.check(
        "path3-ends-independent",
        ends_j[(1, 1)] == Fraction(1, 4) and ends_j[(1, 0)] == Fraction(1, 4),
        "ends-first on path3 gives independent empty laws on the two ends",
    )
    checks.check(
        "path3-chain-ising-correlated",
        chain_j[(1, 1)] == Fraction(17, 50)
        and chain_j[(1, 1)] != ends_j[(1, 1)]
        and sum(chain_j.values()) == 1,
        "the Ising chain's (L,R) marginal is 17/50 on (++), not the independent 1/4",
    )
    indep_chain = chain_lr_joint(Fraction(1, 2), Fraction(1, 2), p0)
    checks.check(
        "path3-independent-kernel-matches",
        indep_chain == ends_j,
        "the independent kernel makes the chain (L,R) marginal equal the ends-first law",
    )

    # Six-axis: K^2_same - K^2_opp = (a-b)^2.
    def k2_same(a: Fraction, b: Fraction, c: Fraction) -> Fraction:
        return a * a + b * b + 4 * c * c

    def k2_opp(a: Fraction, b: Fraction, c: Fraction) -> Fraction:
        return 2 * a * b + 4 * c * c

    def k2_orth(a: Fraction, b: Fraction, c: Fraction) -> Fraction:
        return 2 * a * c + 2 * b * c + 2 * c * c

    cubic_samples = (
        (Fraction(1, 6), Fraction(1, 6), Fraction(1, 6)),
        (Fraction(1, 2), Fraction(1, 2), Fraction(0)),
        (Fraction(1, 3), Fraction(0), Fraction(1, 6)),
        (Fraction(3, 7), Fraction(1, 7), Fraction(3, 28)),
        (Fraction(1), Fraction(0), Fraction(0)),
    )
    cubic_identity = all(
        k2_same(a, b, c) - k2_opp(a, b, c) == (a - b) ** 2
        for a, b, c in cubic_samples
    )
    checks.check(
        "six-axis-k2-same-minus-opp",
        cubic_identity,
        "K^2(same) - K^2(opp) = (a-b)^2 on every sampled cubic kernel",
    )

    # Direct evaluation of the squared kernel against the closed form.
    a, b, c = Fraction(3, 7), Fraction(1, 7), Fraction(3, 28)
    source = (1, 0, 0)
    same_pt = (1, 0, 0)
    opp_pt = (-1, 0, 0)
    orth_pt = (0, 1, 0)
    checks.check(
        "six-axis-k2-closed-form",
        kernel_square_entry(source, same_pt, a, b, c) == k2_same(a, b, c)
        and kernel_square_entry(source, opp_pt, a, b, c) == k2_opp(a, b, c)
        and kernel_square_entry(source, orth_pt, a, b, c) == k2_orth(a, b, c)
        and a + b + 4 * c == 1,
        "the closed forms equal the explicit six-by-six product for a non-uniform cubic kernel",
    )

    uniform = Fraction(1, 6)
    haar_rows = k2_same(uniform, uniform, uniform) == uniform and k2_opp(
        uniform, uniform, uniform
    ) == uniform and k2_orth(uniform, uniform, uniform) == uniform
    checks.check(
        "six-axis-uniform-is-haar-square",
        haar_rows,
        "the uniform kernel squares to itself, the unique invariant law",
    )

    # Uniqueness: a=b from (a-b)^2=0, then a+2c=1/2, then 36c^2-12c+1=0.
    # If K^2 is constant on the three orbits, same=opp so a=b.
    # Then 2a+4c=1. Substitute into same=1/6: 2a^2+4c^2=1/6 with a=1/2-2c.
    def quadratic_at(cval: Fraction) -> Fraction:
        aval = Fraction(1, 2) - 2 * cval
        return 2 * aval * aval + 4 * cval * cval - Fraction(1, 6)

    checks.check(
        "six-axis-quadratic-is-a-square",
        quadratic_at(Fraction(1, 6)) == 0
        and quadratic_at(Fraction(0)) == Fraction(1, 3)
        and quadratic_at(Fraction(1, 4)) == Fraction(1, 12)
        and all(
            quadratic_at(cval) == (6 * cval - 1) ** 2 / 3
            for cval in (Fraction(0), Fraction(1, 12), Fraction(1, 6), Fraction(1, 4), Fraction(1, 5))
        ),
        "after a=b the Haar-square condition is (6c-1)^2/3 = 0, hence only c=a=b=1/6",
    )

    # Scan small-denominator cubic kernels for any other Haar-square solution.
    extras = []
    for den in range(1, 9):
        for na in range(den + 1):
            for nb in range(den - na + 1):
                a = Fraction(na, den)
                b = Fraction(nb, den)
                c = (1 - a - b) / 4
                if c < 0:
                    continue
                if k2_same(a, b, c) == k2_opp(a, b, c) == k2_orth(a, b, c) == uniform:
                    extras.append((a, b, c))
    checks.check(
        "six-axis-no-other-small-denominator-solution",
        set(extras) == {(uniform, uniform, uniform)},
        "the only cubic kernel with denominator at most 8 whose square is uniform is the uniform kernel",
    )

    # S^2 zonal moments. Haar on [-1,1] is dt/2.
    # g(t) = 1 + beta t + gamma (3t^2-1)/2, already Haar-normalized at degree 0.
    def polynomial_product(left, right):
        result = [Fraction(0)] * (len(left) + len(right) - 1)
        for i, x in enumerate(left):
            for j, y in enumerate(right):
                result[i + j] += x * y
        return result

    def haar_integral(coefficients):
        return sum((x / (i + 1) for i, x in enumerate(coefficients) if i % 2 == 0), Fraction(0))

    def density(beta, gamma):
        return [1 - gamma / 2, beta, 3 * gamma / 2]

    def lambda1(beta: Fraction, gamma: Fraction) -> Fraction:
        return haar_integral(polynomial_product([Fraction(0), Fraction(1)], density(beta, gamma)))

    def lambda2(beta: Fraction, gamma: Fraction) -> Fraction:
        return haar_integral(polynomial_product([Fraction(-1, 2), Fraction(0), Fraction(3, 2)], density(beta, gamma)))

    checks.check(
        "sphere-dipole-moment",
        lambda1(Fraction(1), Fraction(0)) == Fraction(1, 3)
        and lambda1(Fraction(0), Fraction(1)) == 0
        and lambda1(Fraction(3, 5), Fraction(2, 7)) == Fraction(1, 5),
        "the zonal dipole of 1 + beta t is beta/3, vanishing iff beta=0",
    )
    checks.check(
        "sphere-quadrupole-moment",
        lambda2(Fraction(0), Fraction(1)) == Fraction(1, 5)
        and lambda2(Fraction(1), Fraction(0)) == 0
        and lambda2(Fraction(3, 5), Fraction(1)) == Fraction(1, 5),
        "the zonal quadrupole of gamma P2 is gamma/5, vanishing iff gamma=0",
    )
    checks.check(
        "sphere-k2-haar-kills-moments",
        all(
            (lambda1(beta, gamma) == 0 and lambda2(beta, gamma) == 0) == (beta == 0 and gamma == 0)
            for beta, gamma in (
                (Fraction(0), Fraction(0)),
                (Fraction(1), Fraction(0)),
                (Fraction(0), Fraction(1)),
                (Fraction(1, 2), Fraction(-1, 3)),
                (Fraction(3, 4), Fraction(1, 8)),
            )
        ),
        "the exact first two moments distinguish the sampled degree-two coefficients; no infinite harmonic classification executed",
    )
    # Integrate cos(phi)^2 by its Laurent constant coefficient.
    cosine = {-1: Fraction(1, 2), 1: Fraction(1, 2)}
    square = {}
    for i, x in cosine.items():
        for j, y in cosine.items():
            square[i + j] = square.get(i + j, Fraction(0)) + x * y
    haar_t2 = haar_integral([Fraction(0), Fraction(0), Fraction(1)])
    circle_t2 = square[0]
    checks.check("equator-two-step-moment", circle_t2 == Fraction(1, 2)
                 and haar_t2 == Fraction(1, 3) and circle_t2 != haar_t2,
                 "Laurent-angle integral versus polynomial-area integral")

    def atomic_square(a):
        result = {1: Fraction(0), -1: Fraction(0)}
        kernel = {1: a, -1: 1-a}
        for x, px in kernel.items():
            for y, py in kernel.items():
                result[x*y] += px*py
        return result
    checks.check("atomic-composition", all(
        atomic_square(a) == {1: a*a+(1-a)**2, -1: 2*a*(1-a)}
        for a in (Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(1))),
        "all sign products accumulated for four atomic kernels")

    def sequential_joint(vertices, edges, order, majority_at_three):
        joint = {}
        for values in product((0, 1), repeat=len(vertices)):
            assignment = dict(zip(vertices, values))
            seen = set()
            weight = Fraction(1)
            for vertex in order:
                neighbours = [x for x in seen if (vertex, x) in edges or (x, vertex) in edges]
                plus = Fraction(1, 2)
                if majority_at_three and len(neighbours) == 3:
                    plus = Fraction(int(sum(assignment[x] for x in neighbours) >= 2))
                weight *= plus if assignment[vertex] else 1-plus
                seen.add(vertex)
            joint[values] = weight
        return joint

    path_vertices = (0, 1, 2)
    path_edges = {(0, 1), (1, 2)}
    path_laws = [sequential_joint(path_vertices, path_edges, order, True)
                 for order in permutations(path_vertices)]
    checks.check("delayed-variation-path", all(
        law == {v: Fraction(1, 8) for v in product((0, 1), repeat=3)}
        for law in path_laws), "all six path orders iid when variation begins at three neighbours")
    star_vertices = (0, 1, 2, 3)
    star_edges = {(0, x) for x in (1, 2, 3)}
    center_first = sequential_joint(star_vertices, star_edges, star_vertices, True)
    leaves_first = sequential_joint(star_vertices, star_edges, (1, 2, 3, 0), True)
    checks.check("delayed-variation-star", sum(center_first.values()) == sum(leaves_first.values()) == 1
                 and center_first[(0, 1, 1, 1)] == Fraction(1, 16)
                 and leaves_first[(0, 1, 1, 1)] == 0,
                 "complete four-site joint laws differ at a majority-incompatible center")
    checks.check("independent-star-matching", all(
        sequential_joint(star_vertices, star_edges, order, False)
        == {v: Fraction(1, 16) for v in product((0, 1), repeat=4)}
        for order in permutations(star_vertices)), "all 24 independent-star orders give the product law")

    u, v = (1, -1, 0), (1, 1, -2)
    radial = [[Fraction(1, 3)+Fraction(u[i]*v[j], 12) for j in range(3)] for i in range(3)]
    radial_square = [[sum((radial[i][k]*radial[k][j] for k in range(3)), Fraction(0))
                     for j in range(3)] for i in range(3)]
    checks.check("radial-square-witness", all(sum(row) == 1 for row in radial)
                 and all(x > 0 for row in radial for x in row)
                 and radial[0] != radial[1]
                 and all(x == Fraction(1, 3) for row in radial_square for x in row)
                 and radial[0][1] != radial[1][0],
                 "positive nonconstant radial kernel squares to uniform but is not reversible")

    checks.check(
        "note-quotes-identities",
        "(pplus - pminus)^2" in note_flat
        and "(a-b)^2" in note_flat
        and "17/25" in note
        and "17/50" in note
        and "(6c-1)^2" in note_flat
        and "beta/3" in note_flat,
        "the note quotes the two-state, six-axis, path3, and zonal identities",
    )
    checks.check("note-scope", "supplied mathematical hypotheses" in note_flat
                 and "almost every" in note_flat
                 and "negative packet lacks five" in note_flat,
                 "positive scope, a.e. qualification and deferred negative certification are explicit")
    print("per_element: exact rational entries, polynomial coefficients and finite joint assignments checked")
    print("per_site: complete three-site path and four-site star assignments checked")
    print("per_mode: degree-one and degree-two sphere moments checked; infinite harmonic family not executed")
    print("per_block: binary, six-axis and three-state radial matrices plus path/star joints checked")
    print("lattice_wide: checked and not executed — finite isolated windows only; no infinite dynamics claim")

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
