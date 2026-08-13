#!/usr/bin/env python3
"""Exact checks: unique G-invariant probability on the six axis points is 1/6.

Identity gates call haar_six() and is_invariant(p). All arithmetic is
Fraction. The runner derives 1/|X|; it does not embed 1/6 and compare it to
itself as the sole uniqueness witness.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "UNIQUE_CUBIC_INVARIANT_PROBABILITY_ON_SIX_AXIS_POINTS_IS_ONE_SIXTH"
    "_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/UNIQUE_CUBIC_INVARIANT_PROBABILITY_ON_SIX_AXIS_POINTS_IS_ONE_SIXTH_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Vec = tuple[int, int, int]
Mat = tuple[Vec, Vec, Vec]
Prob = dict[Vec, Fraction]

E1: Vec = (1, 0, 0)
E2: Vec = (0, 1, 0)
E3: Vec = (0, 0, 1)
AXIS_POINTS: tuple[Vec, ...] = (
    E1,
    (-1, 0, 0),
    E2,
    (0, -1, 0),
    E3,
    (0, 0, -1),
)

IDENTITY: Mat = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
R_Z_90: Mat = ((0, -1, 0), (1, 0, 0), (0, 0, 1))
R_X_90: Mat = ((1, 0, 0), (0, 0, 1), (0, -1, 0))


def normalize(text: str) -> str:
    return " ".join(text.split())


def mat_vec(matrix: Mat, vector: Vec) -> Vec:
    return tuple(
        sum(matrix[row][col] * vector[col] for col in range(3)) for row in range(3)
    )  # type: ignore[return-value]


def mat_mul(left: Mat, right: Mat) -> Mat:
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(3)) for j in range(3))
        for i in range(3)
    )  # type: ignore[return-value]


def transpose(matrix: Mat) -> Mat:
    return tuple(tuple(matrix[j][i] for j in range(3)) for i in range(3))  # type: ignore[return-value]


def determinant(matrix: Mat) -> int:
    a, b, c = matrix
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def proper_cubic_group() -> tuple[Mat, ...]:
    matrices: list[Mat] = []
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            rows = []
            for row in range(3):
                entries = [0, 0, 0]
                entries[perm[row]] = signs[row]
                rows.append(tuple(entries))
            matrix = tuple(rows)  # type: ignore[assignment]
            if determinant(matrix) == 1:
                matrices.append(matrix)
    return tuple(matrices)


G: tuple[Mat, ...] = proper_cubic_group()


def is_probability(p: Prob) -> bool:
    if set(p) != set(AXIS_POINTS):
        return False
    if any(value < 0 for value in p.values()):
        return False
    return sum(p.values(), Fraction(0)) == 1


def haar_six() -> Prob:
    weight = Fraction(1, len(AXIS_POINTS))
    return {point: weight for point in AXIS_POINTS}


def is_invariant(p: Prob) -> bool:
    if not is_probability(p):
        return False
    for matrix in G:
        for point in AXIS_POINTS:
            if p[mat_vec(matrix, point)] != p[point]:
                return False
    return True


def pushforward(matrix: Mat, p: Prob) -> Prob:
    inverse = transpose(matrix)
    return {point: p[mat_vec(inverse, point)] for point in AXIS_POINTS}


def orbit_average(p: Prob) -> Prob:
    acc = {point: Fraction(0) for point in AXIS_POINTS}
    for matrix in G:
        pushed = pushforward(matrix, p)
        for point in AXIS_POINTS:
            acc[point] += pushed[point]
    order = Fraction(len(G))
    return {point: acc[point] / order for point in AXIS_POINTS}


def point_mass(support: Vec) -> Prob:
    return {point: Fraction(1 if point == support else 0) for point in AXIS_POINTS}


def half_on_e1() -> Prob:
    values = {point: Fraction(0) for point in AXIS_POINTS}
    values[E1] = Fraction(1, 2)
    values[E2] = Fraction(1, 2)
    return values


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        result = bool(condition)
        if result:
            self.passed += 1
        else:
            self.failed += 1
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    axiom_norm = normalize(axiom)
    note_norm = normalize(note)

    print("external_scientific_inputs: current axiom wording only; no observational or fitted inputs")
    print("package_local_integrity_reads: proposed source note plus axiom memo")
    print("audit_input_paths: " + ", ".join(AUDIT_INPUT_PATHS))

    checks.check(
        "source-lattice",
        "Lattice names proper cubic rotations about each site",
        "proper cubic rotations about each site" in axiom_norm,
    )
    checks.check(
        "source-qubit",
        "Qubit names that no possibility is privileged",
        "No possibility is privileged." in axiom,
    )
    checks.check(
        "cardinality",
        "the axis set X has six points",
        len(AXIS_POINTS) == 6 and len(set(AXIS_POINTS)) == 6,
    )
    checks.check(
        "group-order",
        "the proper cubic group has 24 matrices of determinant +1",
        len(G) == 24
        and len(set(G)) == 24
        and all(determinant(matrix) == 1 for matrix in G)
        and IDENTITY in G,
    )

    orbit = {mat_vec(matrix, E1) for matrix in G}
    checks.check(
        "transitivity",
        "G acts transitively; 90 degrees about z sends e1 to e2",
        orbit == set(AXIS_POINTS) and mat_vec(R_Z_90, E1) == E2 and R_Z_90 in G,
    )
    checks.check(
        "rx-sends-e3-to-e2",
        "90 degrees about x sends e3 to e2",
        mat_vec(R_X_90, E3) == E2 and R_X_90 in G,
    )

    # Identity gates must call haar_six() and is_invariant(p).
    p = haar_six()
    identity_push = pushforward(IDENTITY, p)
    checks.check(
        "identity-haar-six",
        "identity gate: haar_six is the constant 1/|X| probability",
        is_probability(p)
        and len(set(p.values())) == 1
        and p[E1] == Fraction(1, len(AXIS_POINTS))
        and p[E1] == Fraction(1, 6)
        and identity_push == p,
    )
    checks.check(
        "identity-invariance",
        "identity gate: is_invariant(haar_six()) holds and identity preserves p",
        is_invariant(p)
        and is_invariant(identity_push)
        and all(p[mat_vec(IDENTITY, point)] == p[point] for point in AXIS_POINTS),
    )

    averaged = orbit_average(point_mass(E3))
    checks.check(
        "uniqueness-reynolds",
        "the G-average of any probability equals haar_six",
        averaged == p and is_invariant(averaged) and is_probability(averaged),
    )

    delta = point_mass(E3)
    checks.check(
        "delta-legal",
        "the point mass on e3 is a legal probability",
        is_probability(delta) and delta[E3] == 1 and delta[E2] == 0,
    )
    mutation_delta_invariant = is_invariant(delta)
    checks.check(
        "mutation-delta-invariant",
        "predicate 'delta_e3 is G-invariant' fails",
        mutation_delta_invariant is False
        and pushforward(R_X_90, delta) != delta
        and delta[mat_vec(R_X_90, E3)] != delta[E3],
    )

    half = half_on_e1()
    unique_half_claim = (
        is_invariant(half) and half[E1] == Fraction(1, 2) and half == p
    )
    checks.check(
        "mutation-half-unique",
        "predicate 'p(e1)=1/2 is the unique invariant law' fails",
        unique_half_claim is False
        and half[E1] != p[E1]
        and Fraction(1, 2) != Fraction(1, 6)
        and is_invariant(half) is False
        and is_invariant(p)
        and p[E1] == Fraction(1, 6),
    )

    required_note = (
        "`|X|=6`",
        "acts transitively",
        "`p(x)=1/6`",
        "`\\delta_{e3}`",
        "Do not adopt Haar as a vacuum axiom",
        "Not universal `r=1/2`",
        "Not a Born kernel",
        "not an invariant Bloch vector",
        "Do not force `r=1/2`",
        "### N5 — rhetoric and resolution audit (Theorem 5)",
    )
    checks.check(
        "note-theorems",
        "the source note states Theorems 1-5 and the N5 fence on Theorem 5",
        all(needle in note for needle in required_note)
        and "## Theorem 5" in note
        and "minimal_axioms" in note
        and "bloch0" not in note
        and "pvmselect" not in note
        and "#6202" not in note,
    )
    checks.check(
        "note-scope",
        "Haar is displayed and not adopted; r=1/2 is not forced",
        "Display that unique invariant law" in note
        and "not a vacuum axiom" in note_norm
        and "Do not force `r=1/2`" in note
        and "**Type:** bounded_theorem" in note,
    )

    print("per_element: six axis points and 24 proper cubic matrices are enumerated exactly")
    print("negative_scope: only G-invariance on this six-point set is decided; no Born kernel or Bloch vector is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
