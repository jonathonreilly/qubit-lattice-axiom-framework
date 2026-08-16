#!/usr/bin/env python3
"""Cube equivariance of the firing local-in-n map on one three-seed star.

U = B_2(0) ∪ B_2((2,0,0)) ∪ B_2((1,2,1)). Score only the unread star at
v = (−1, 1, 1). The displayed local-in-n map of the firing 6-tuple
c = (−, 0, +, −, 0, +) is unique-axis sign on |supp n| = 1, shared kernel
→ −, and n = (1/3, −1/3, 0) → +. Empty stays 0. Count how many of the
24 proper cube rotations commute when n and slots rotate together.
Displayed, not adopted. No cache is written.
"""

from __future__ import annotations

import ast
import itertools
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/SKEW_THREE_SEED_LOCAL_N_EQUIVARIANCE_"
    "BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/SKEW_THREE_SEED_LOCAL_N_EQUIVARIANCE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Point = tuple[int, int, int]
Coloring = tuple[int, ...]
Kernel = tuple[Fraction, Fraction, Fraction]
Matrix = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]

DIRS: tuple[Point, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
DIR_INDEX = {direction: index for index, direction in enumerate(DIRS)}
EMPTY, PLUS, MINUS, UNDEF = 0, 1, 2, 99
LETTER = {EMPTY: "0", PLUS: "+", MINUS: "−", UNDEF: "?"}
V: Point = (-1, 1, 1)
SEEDS: tuple[Point, ...] = ((0, 0, 0), (2, 0, 0), (1, 2, 1))
SHARED: Kernel = (Fraction(1, 3), Fraction(0), Fraction(-1, 3))
OTHER: Kernel = (Fraction(1, 3), Fraction(-1, 3), Fraction(0))
TABLE: dict[Kernel, int] = {SHARED: MINUS, OTHER: PLUS}
C: Coloring = (MINUS, EMPTY, PLUS, MINUS, EMPTY, PLUS)
FORBIDDEN = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")


def normalize(text: str) -> str:
    return " ".join(text.split())


def add(left: Point, right: Point) -> Point:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def sub(left: Point, right: Point) -> Point:
    return (left[0] - right[0], left[1] - right[1], left[2] - right[2])


def l1(point: Point) -> int:
    return abs(point[0]) + abs(point[1]) + abs(point[2])


def ball(center: Point, radius: int = 2) -> frozenset[Point]:
    sites: set[Point] = set()
    span = range(-radius, radius + 1)
    for offset in itertools.product(span, repeat=3):
        site = add(center, offset)
        if l1(sub(site, center)) <= radius:
            sites.add(site)
    return frozenset(sites)


def locked_union() -> frozenset[Point]:
    occupied = frozenset()
    for seed in SEEDS:
        occupied = occupied | ball(seed)
    return occupied


def occupancy_tuple(site: Point, occupied: frozenset[Point]) -> Coloring:
    return tuple(int(add(site, direction) in occupied) for direction in DIRS)


def dipole(occ: Coloring) -> Kernel:
    return (
        Fraction(occ[0] - occ[1], 3),
        Fraction(occ[2] - occ[3], 3),
        Fraction(occ[4] - occ[5], 3),
    )


def unique_axis_label(n: Kernel) -> int | None:
    support = [index for index, value in enumerate(n) if value != 0]
    if len(support) != 1:
        return None
    return PLUS if n[support[0]] > 0 else MINUS


def star_kernels(center: Point, occupied: frozenset[Point]) -> tuple[Kernel | None, ...]:
    kernels: list[Kernel | None] = []
    for direction in DIRS:
        neighbor = add(center, direction)
        if neighbor not in occupied:
            kernels.append(None)
            continue
        kernels.append(dipole(occupancy_tuple(neighbor, occupied)))
    return tuple(kernels)


def label_from_n(n: Kernel | None) -> int:
    if n is None:
        return EMPTY
    unique = unique_axis_label(n)
    if unique is not None:
        return unique
    return TABLE.get(n, UNDEF)


def label_star(kernels: tuple[Kernel | None, ...]) -> Coloring:
    return tuple(label_from_n(kernel) for kernel in kernels)


def det3(matrix: Matrix) -> int:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def mat_vec(matrix: Matrix, vector: tuple[Fraction, ...] | Point) -> tuple:
    return (
        matrix[0][0] * vector[0] + matrix[0][1] * vector[1] + matrix[0][2] * vector[2],
        matrix[1][0] * vector[0] + matrix[1][1] * vector[1] + matrix[1][2] * vector[2],
        matrix[2][0] * vector[0] + matrix[2][1] * vector[1] + matrix[2][2] * vector[2],
    )


def proper_rotations() -> tuple[Matrix, ...]:
    records: list[Matrix] = []
    seen: set[Matrix] = set()
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            rows = []
            for row, col in enumerate(perm):
                entry = [0, 0, 0]
                entry[col] = signs[row]
                rows.append(tuple(entry))
            matrix = (rows[0], rows[1], rows[2])
            if matrix not in seen and det3(matrix) == 1:
                seen.add(matrix)
                records.append(matrix)
    return tuple(records)


def rotate_kernels(
    matrix: Matrix, kernels: tuple[Kernel | None, ...]
) -> tuple[Kernel | None, ...]:
    out: list[Kernel | None] = [None] * 6
    for source, direction in enumerate(DIRS):
        image = DIR_INDEX[mat_vec(matrix, direction)]
        kernel = kernels[source]
        if kernel is None:
            out[image] = None
        else:
            rotated = mat_vec(matrix, kernel)
            out[image] = (rotated[0], rotated[1], rotated[2])
    return tuple(out)


def rotate_labels(matrix: Matrix, labels: Coloring) -> Coloring:
    out = [EMPTY] * 6
    for source, direction in enumerate(DIRS):
        image = DIR_INDEX[mat_vec(matrix, direction)]
        out[image] = labels[source]
    return tuple(out)


def commute_count(
    kernels: tuple[Kernel | None, ...], rotations: tuple[Matrix, ...]
) -> tuple[int, int]:
    base = label_star(kernels)
    n_commute = 0
    n_defined = 0
    for matrix in rotations:
        rebuilt = label_star(rotate_kernels(matrix, kernels))
        if UNDEF not in rebuilt:
            n_defined += 1
        n_commute += int(rebuilt == rotate_labels(matrix, base))
    return n_commute, n_defined


def same_orbit(left: Kernel, right: Kernel, rotations: tuple[Matrix, ...]) -> bool:
    return any(mat_vec(matrix, left) == right for matrix in rotations)


def format_tuple(coloring: Coloring) -> str:
    return "(" + ",".join(LETTER[slot] for slot in coloring) + ")"


def format_n(n: Kernel | None) -> str:
    if n is None:
        return "empty"
    return "(" + ",".join(str(component) for component in n) + ")"


def parse_audit_input_paths(source: str) -> object:
    tree = ast.parse(source)
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id == "AUDIT_INPUT_PATHS":
                return ast.literal_eval(node.value)
    raise AssertionError("AUDIT_INPUT_PATHS assignment is missing")


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(
        self,
        label: str,
        statement: str,
        condition: bool,
        residual: object | None = None,
    ) -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        print(f"{'PASS' if ok else 'FAIL'}: {label} {statement}")
        if not ok and residual is not None:
            print(f"  residual: {residual}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note_path = ROOT / NOTE_REL
    axiom_path = ROOT / AXIOM_REL
    note = note_path.read_text(encoding="utf-8")
    axiom = axiom_path.read_text(encoding="utf-8")
    note_flat = normalize(note)
    axiom_flat = normalize(axiom)
    self_source = Path(__file__).read_text(encoding="utf-8")
    literal_paths = parse_audit_input_paths(self_source)

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print(
        "external_scientific_inputs: current Lattice, Qubit, Admissibility, "
        "and Record sentences; G+ rebuilt as the 24 proper cube rotations"
    )
    print("construction: U=B_2(0)∪B_2((2,0,0))∪B_2((1,2,1)), unread v=(-1,1,1)")
    print("negative_scope: displayed local-in-n map only; not adopted; L1 not attached")

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required static two-string literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/SKEW_THREE_SEED_LOCAL_N_EQUIVARIANCE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and literal_paths == AUDIT_INPUT_PATHS
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and AUDIT_TIMEOUT_SEC == 120,
    )

    lattice_sentence = (
        "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
    )
    admissibility_sentence = (
        "For each site, the probability distribution over the possibilities is "
        "determined by, and varies with, the nearest-neighbor conditions."
    )
    covariance_clause = (
        "one fixed nearest-neighbor admissibility rule, covariant under "
        "lattice translations and proper cubic rotations"
    )
    formation_boundary = "it does not supply the formation site, probability,"
    qubit_sentence = "The full one-site possibility domain has algebraic presentation `M_2(C)`."
    record_lock = "When present, a record locks exactly one admissible local possibility."
    record_perm = "A site never carries more than one record; records are permanent."
    record_content = "A readout value is determined by record content alone."
    record_absence = "A site with no record cannot be read."

    checks.check(
        "source-lattice",
        "current cubic nearest-neighbor wording is pinned",
        lattice_sentence in axiom and lattice_sentence in note,
    )
    checks.check(
        "source-admissibility",
        "current local-distribution wording is pinned",
        admissibility_sentence in axiom_flat and admissibility_sentence in note_flat,
    )
    checks.check(
        "source-covariance",
        "Admissibility still requires one proper-cubic covariant rule",
        covariance_clause in axiom_flat and covariance_clause in note_flat,
    )
    checks.check(
        "source-formation-boundary",
        "formation site/probability/rate remains outside Admissibility",
        formation_boundary in axiom and formation_boundary in note,
    )
    checks.check(
        "source-qubit",
        "Qubit remains M_2(C)",
        qubit_sentence in axiom and qubit_sentence in note and "Qubit remains `M_2(C)`" in note,
    )
    checks.check(
        "source-record",
        "lock, permanence, content-only readout, and unreadability at absence are pinned",
        all(
            phrase in axiom_flat
            for phrase in (record_lock, record_perm, record_content, record_absence)
        )
        and all(
            phrase in note
            for phrase in (record_lock, record_perm, record_content, record_absence)
        ),
    )

    occupied = locked_union()
    mask = occupancy_tuple(V, occupied)
    kernels = star_kernels(V, occupied)
    displayed = label_star(kernels)
    rotations = proper_rotations()
    n_commute, n_defined = commute_count(kernels, rotations)
    orbit_same = same_orbit(SHARED, OTHER, rotations)
    identity = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    identity_commutes = label_star(rotate_kernels(identity, kernels)) == rotate_labels(
        identity, displayed
    )
    neighbor_rows: list[tuple[Point, Point, Kernel | None, int]] = []
    for direction, kernel in zip(DIRS, kernels, strict=True):
        neighbor_rows.append((direction, add(V, direction), kernel, label_from_n(kernel)))

    print(f"U_card={len(occupied)}")
    print(f"v_in_U={V in occupied}")
    print(f"occupancy_mask={mask}")
    print(f"displayed_c={format_tuple(displayed)}")
    for direction, neighbor, kernel, letter in neighbor_rows:
        print(
            f"slot dir={direction} w={neighbor} n={format_n(kernel)} "
            f"label={LETTER[letter]}"
        )
    print(f"G_plus={len(rotations)}")
    print(f"N_commute={n_commute}")
    print(f"N_defined={n_defined}")
    print(f"N_commute_over_24={n_commute}/24")
    print(f"shared_other_same_orbit={orbit_same}")
    print(f"identity_commutes={identity_commutes}")

    balls = tuple(ball(seed) for seed in SEEDS)
    pairwise = (
        len(balls[0] & balls[1]),
        len(balls[0] & balls[2]),
        len(balls[1] & balls[2]),
    )
    triple = len(balls[0] & balls[1] & balls[2])

    checks.check(
        "g-plus-order",
        "finite G+ is exactly the 24 proper cube rotations",
        len(rotations) == 24 and len(set(rotations)) == 24,
    )
    checks.check(
        "center-unread",
        "the star center v is not already in U",
        V not in occupied
        and l1(V) == 3
        and l1(sub(V, (2, 0, 0))) == 5
        and l1(sub(V, (1, 2, 1))) == 3,
        residual=V in occupied,
    )
    checks.check(
        "u-geometry",
        "U is the union of three radius-2 ℓ¹ balls and has 62 sites",
        all(len(item) == 25 for item in balls)
        and pairwise == (7, 4, 4)
        and triple == 2
        and len(occupied) == 62,
    )
    checks.check(
        "occupancy-mask",
        "occupied nearest neighbors of v are exactly +x,+y,−y,−z",
        mask == (1, 0, 1, 1, 0, 1) and "(1, 0, 1, 1, 0, 1)" in note,
    )
    checks.check(
        "theorem-1-map",
        "the displayed local-in-n map reproduces c=(−,0,+,−,0,+)",
        displayed == C
        and kernels[0] == SHARED
        and kernels[2] == (Fraction(1, 3), Fraction(0), Fraction(0))
        and kernels[3] == SHARED
        and kernels[5] == OTHER
        and unique_axis_label(kernels[2]) == PLUS
        and "(−,0,+,−,0,+)" in note,
    )
    checks.check(
        "theorem-1-commute",
        "N_commute among the 24 proper rotations is computed and reported",
        n_commute == n_defined
        and identity_commutes
        and f"N_commute = {n_commute}" in note
        and f"{n_commute}/24" in note,
        residual=n_commute,
    )
    checks.check(
        "theorem-2-not-equivariant",
        "N_commute is not 24, so the map is not cube-covariant",
        n_commute != 24
        and n_commute < 24
        and orbit_same
        and TABLE[SHARED] != TABLE[OTHER]
        and "not a cube-covariant Admissibility rule" in note,
        residual=n_commute,
    )

    claim_scope = (
        'claim_scope: "On the off-axis three-ball star at v=(-1,1,1), '
        "whether the firing local-in-n labeling is equivariant under the "
        '24 proper cube rotations is reported. Displayed, not adopted."'
    )
    checks.check(
        "claim-scope",
        "the note reports the declared displayed claim_scope",
        claim_scope in note,
    )
    checks.check(
        "displayed-not-adopted",
        "the map is displayed and is not written into Admissibility",
        "Displayed, not adopted" in note
        and "Do not write the map into Admissibility" in note
        and "hypothetical_axiom_status:" in note
        and "This note authors no audit verdict" in note,
    )
    checks.check(
        "l1-not-attached",
        "the note does not attach L1 and does not add a fourth ball",
        "Do not attach L1" in note
        and "Do not add a 4th ball" in note
        and "we attach L1" not in note_flat
        and "we add a 4th ball" not in note_flat,
    )
    checks.check(
        "not-leftover-prior",
        "the note is not leftover-char of skewrun execution or slotn",
        "not leftover-char of skewrun" in note_flat
        and "execution" in note_flat
        and "not leftover-char of slotn" in note_flat
        and "different rule" in note_flat,
    )
    checks.check(
        "admissibility-unedited",
        "the firing local-in-n map is not written into Admissibility",
        covariance_clause in axiom_flat
        and "(−,0,+,−,0,+)" not in axiom
        and "local-in-n" not in axiom
        and "B_2((1,2,1))" not in axiom,
    )
    checks.check(
        "forbidden-phrases",
        "the forbidden rhetoric strings are absent from the note and runner",
        all(phrase not in note for phrase in FORBIDDEN)
        and all(phrase not in self_source.split("FORBIDDEN = ", 1)[0] for phrase in FORBIDDEN),
    )
    checks.check(
        "no-axiom-edit",
        "the only axiom authority is the current memo; no cache or axiom rewrite",
        "[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)" in note
        and "cache_write: false" in self_source
        and AXIOM_REL in AUDIT_INPUT_PATHS
        and "no axiom" in note_flat.lower(),
    )

    print("per_element: local-in-n letters and N_commute are exact integers")
    print("per_site: only the unread star center v is scored")
    print("per_mode: no spectral calculation")
    print("per_block: the six-neighbor star at v only")
    print("lattice_wide: checked and not executed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
