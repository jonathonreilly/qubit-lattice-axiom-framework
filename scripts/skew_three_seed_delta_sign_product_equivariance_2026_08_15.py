#!/usr/bin/env python3
"""Cube equivariance of the claim-delta sign-product rule on one star.

U = B_2(0) ∪ B_2((2,0,0)) ∪ B_2((1,2,1)). Score only the unread star at
v = (−1, 1, 1). Same s* as delsgn: lex-first nearest seed. Rebuild c by
the product rule: unique-axis of n_hist when it exists, else the product
of the signs of the nonzero coordinates of δ = w − s*(w). G+ acts on
slots, seeds, and δ by rotating about v. Count how many of the 24 proper
cube rotations satisfy transported labels = the product rule after
rotating seeds and w. Displayed, not adopted. No cache is written.
"""

from __future__ import annotations

import ast
import itertools
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/SKEW_THREE_SEED_DELTA_SIGN_PRODUCT_EQUIVARIANCE_"
    "BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/SKEW_THREE_SEED_DELTA_SIGN_PRODUCT_EQUIVARIANCE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
EMPTY, PLUS, MINUS = 0, 1, 2
LETTER = {EMPTY: "0", PLUS: "+", MINUS: "−"}
V: Point = (-1, 1, 1)
SEEDS: tuple[Point, ...] = ((0, 0, 0), (2, 0, 0), (1, 2, 1))
C: Coloring = (PLUS, EMPTY, PLUS, MINUS, EMPTY, MINUS)
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


def locked_union(seeds: tuple[Point, ...] = SEEDS) -> frozenset[Point]:
    occupied = frozenset()
    for seed in seeds:
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


def unique_nonzero_sign(vec: tuple[object, ...]) -> int | None:
    support = [index for index, value in enumerate(vec) if value != 0]
    if len(support) != 1:
        return None
    return PLUS if vec[support[0]] > 0 else MINUS


def nonzero_sign_product(vec: tuple[object, ...]) -> int | None:
    product = 1
    support = 0
    for value in vec:
        if value == 0:
            continue
        support += 1
        product *= 1 if value > 0 else -1
    if support == 0:
        return None
    return PLUS if product > 0 else MINUS


def nearest_seed(site: Point, seeds: tuple[Point, ...]) -> Point:
    ranked = sorted((l1(sub(site, seed)), seed) for seed in seeds)
    return ranked[0][1]


def product_label(n_vec: Kernel, delta: Point) -> int | None:
    hist = unique_nonzero_sign(n_vec)
    if hist is not None:
        return hist
    return nonzero_sign_product(delta)


def det3(matrix: Matrix) -> int:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def mat_vec(matrix: Matrix, vector: tuple[object, ...] | Point) -> tuple:
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


def act_about(matrix: Matrix, point: Point, origin: Point = V) -> Point:
    return add(origin, mat_vec(matrix, sub(point, origin)))


def rotate_seeds(matrix: Matrix, seeds: tuple[Point, ...] = SEEDS) -> tuple[Point, ...]:
    return tuple(act_about(matrix, seed) for seed in seeds)


def rotate_labels(matrix: Matrix, labels: Coloring) -> Coloring:
    out = [EMPTY] * 6
    for source, direction in enumerate(DIRS):
        image = DIR_INDEX[mat_vec(matrix, direction)]
        out[image] = labels[source]
    return tuple(out)


NeighborRow = tuple[Point, Point, Point | None, Kernel | None, Point | None, int | None, int | None]


def star_from_seeds(seeds: tuple[Point, ...]) -> tuple[Coloring, tuple[NeighborRow, ...]]:
    occupied = locked_union(seeds)
    labels: list[int] = []
    rows: list[NeighborRow] = []
    for direction in DIRS:
        neighbor = add(V, direction)
        if neighbor not in occupied:
            labels.append(EMPTY)
            rows.append((direction, neighbor, None, None, None, None, EMPTY))
            continue
        seed_star = nearest_seed(neighbor, seeds)
        n_vec = dipole(occupancy_tuple(neighbor, ball(seed_star)))
        delta = sub(neighbor, seed_star)
        hist_only = unique_nonzero_sign(n_vec)
        label = product_label(n_vec, delta)
        if label is None:
            raise RuntimeError(f"empty product at occupied neighbor {neighbor}")
        labels.append(label)
        rows.append((direction, neighbor, seed_star, n_vec, delta, hist_only, label))
    return tuple(labels), tuple(rows)


def commute_count(
    rotations: tuple[Matrix, ...],
) -> tuple[int, Coloring, tuple[NeighborRow, ...], tuple[Matrix, ...]]:
    base, rows = star_from_seeds(SEEDS)
    commuting: list[Matrix] = []
    for matrix in rotations:
        rebuilt, _ = star_from_seeds(rotate_seeds(matrix))
        if rebuilt == rotate_labels(matrix, base):
            commuting.append(matrix)
    return len(commuting), base, rows, tuple(commuting)


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
    print(
        "negative_scope: displayed claim-delta sign-product rule only; "
        "not adopted; L1 not attached; no 4th equal-radius ball"
    )

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required static two-string literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/SKEW_THREE_SEED_DELTA_SIGN_PRODUCT_EQUIVARIANCE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
    rotations = proper_rotations()
    n_commute, displayed, neighbor_rows, commuting = commute_count(rotations)
    identity = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    cycle_plus = ((0, 1, 0), (0, 0, 1), (1, 0, 0))
    cycle_minus = ((0, 0, 1), (1, 0, 0), (0, 1, 0))
    identity_commutes = identity in commuting
    axis_cycles = {identity, cycle_plus, cycle_minus}

    print(f"U_card={len(occupied)}")
    print(f"v_in_U={V in occupied}")
    print(f"occupancy_mask={mask}")
    print(f"displayed_c={format_tuple(displayed)}")
    for direction, neighbor, seed_star, n_vec, delta, hist_only, label in neighbor_rows:
        hist_kind = "empty" if seed_star is None else (
            "unique-axis" if hist_only is not None else "hist-tied"
        )
        print(
            f"slot dir={direction} w={neighbor} s*={seed_star} "
            f"n_hist={format_n(n_vec)} {hist_kind} delta={delta} "
            f"label={LETTER[label] if label is not None else 'tied'}"
        )
    print(f"G_plus={len(rotations)}")
    print(f"N_commute={n_commute}")
    print(f"N_commute_over_24={n_commute}/24")
    print(f"identity_commutes={identity_commutes}")
    print("commuting_rotations=" + ",".join(str(matrix) for matrix in commuting))

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
        "theorem-1-product-tuple",
        "the product rule rebuilds c=(+,0,+,−,0,−) on this star",
        displayed == C
        and neighbor_rows[0][2] == (0, 0, 0)
        and neighbor_rows[0][4] == (0, 1, 1)
        and neighbor_rows[0][6] == PLUS
        and neighbor_rows[2][5] == PLUS
        and neighbor_rows[2][6] == PLUS
        and neighbor_rows[3][4] == (-1, 0, 1)
        and neighbor_rows[3][6] == MINUS
        and neighbor_rows[5][4] == (-1, 1, 0)
        and neighbor_rows[5][6] == MINUS
        and "(+,0,+,−,0,−)" in note,
        residual=format_tuple(displayed),
    )
    checks.check(
        "theorem-1-commute",
        "N_commute among the 24 proper rotations is computed and reported",
        identity_commutes
        and 0 <= n_commute <= 24
        and f"N_commute = {n_commute}" in note
        and f"{n_commute}/24" in note,
        residual=n_commute,
    )
    theorem_2_ok = (
        (
            n_commute == 24
            and "cube-covariant Admissibility rule" in note
            and "not a cube-covariant Admissibility rule" not in note
        )
        or (
            n_commute != 24
            and "not a cube-covariant Admissibility rule" in note
        )
    )
    checks.check(
        "theorem-2-covariance",
        "whether N_commute=24 is reported as cube-covariance of the history tag",
        theorem_2_ok and set(commuting) == axis_cycles if n_commute != 24 else theorem_2_ok,
        residual=n_commute,
    )

    claim_scope = (
        'claim_scope: "On the off-axis three-ball star at v=(-1,1,1), '
        "whether the claim-delta sign-product labeling is equivariant under "
        'the 24 proper cube rotations is reported. Displayed, not adopted."'
    )
    checks.check(
        "claim-scope",
        "the note reports the declared displayed claim_scope",
        claim_scope in note,
    )
    checks.check(
        "displayed-not-adopted",
        "the product is displayed and is not written into Admissibility",
        "Displayed, not adopted" in note
        and "Do not write the product into Admissibility" in note
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
        "the note is not leftover-char of delsgn membership or skeweq",
        "not leftover-char of delsgn" in note_flat
        and "membership" in note_flat
        and "not leftover-char of skeweq" in note_flat
        and "different map" in note_flat,
    )
    checks.check(
        "admissibility-unedited",
        "the product rule is not written into Admissibility",
        covariance_clause in axiom_flat
        and "(+,0,+,−,0,−)" not in axiom
        and "sign-product" not in axiom
        and "B_2((1,2,1))" not in axiom
        and "n_hist" not in axiom,
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

    print("per_element: product labels and N_commute are exact integers")
    print("per_site: only the unread star center v is scored")
    print("per_mode: no spectral calculation")
    print("per_block: the six-neighbor star at v only")
    print("lattice_wide: checked and not executed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
