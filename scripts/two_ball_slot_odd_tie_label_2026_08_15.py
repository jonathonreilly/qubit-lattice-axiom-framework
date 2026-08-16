#!/usr/bin/env python3
"""Slot-odd equal-n tie-break on the two-ball union: fire and cube covariance.

On U = B_2(0) ∪ B_2((2,0,0)), complete the 6-NN stars at the two positive
unread sites by keeping unique-axis signs and assigning tied equal-n opposite
slots the slot's own ± sign. Report July-3 k=3 pair membership of those two
6-tuples and whether the displayed completion commutes with the 24 proper
cube rotations of the star. Displayed, not adopted. No cache write.
"""

from __future__ import annotations

import itertools
from collections import Counter
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "TWO_BALL_SLOT_ODD_TIE_LABEL_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/TWO_BALL_SLOT_ODD_TIE_LABEL_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

DIRS: tuple[tuple[int, int, int], ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
AXIS_PAIRS = ((0, 1), (2, 3), (4, 5))
PLUS, MINUS, EMPTY = "+", "-", "0"
LETTER_TO_COLOR = {EMPTY: 0, PLUS: 1, MINUS: 2}
CENTER = (0, 0, 0)
OTHER = (2, 0, 0)
V1 = (1, -1, 1)
V2 = (1, 1, -1)
Vec = tuple[int, int, int]
NVec = tuple[Fraction, Fraction, Fraction]
Lab = str


def normalize(text: str) -> str:
    return " ".join(text.split())


def add(left: Vec, right: Vec) -> Vec:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def l1(point: Vec, origin: Vec) -> int:
    return abs(point[0] - origin[0]) + abs(point[1] - origin[1]) + abs(point[2] - origin[2])


def in_ball(point: Vec, origin: Vec, radius: int) -> bool:
    return l1(point, origin) <= radius


def in_U(point: Vec) -> bool:
    return in_ball(point, CENTER, 2) or in_ball(point, OTHER, 2)


def occupancy_sites() -> frozenset[Vec]:
    sites: set[Vec] = set()
    for x in range(-2, 5):
        for y in range(-2, 3):
            for z in range(-2, 3):
                point = (x, y, z)
                if in_U(point):
                    sites.add(point)
    return frozenset(sites)


def n_at(site: Vec) -> NVec:
    components = []
    for plus_i, minus_i in AXIS_PAIRS:
        delta = int(in_U(add(site, DIRS[plus_i]))) - int(in_U(add(site, DIRS[minus_i])))
        components.append(Fraction(delta, 3))
    return (components[0], components[1], components[2])


def unique_axis_label(n_vec: NVec) -> Lab | None:
    support = [index for index, value in enumerate(n_vec) if value != 0]
    if len(support) != 1:
        return None
    return PLUS if n_vec[support[0]] > 0 else MINUS


def star(site: Vec) -> tuple[tuple[bool, ...], tuple[NVec | None, ...], tuple[Lab, ...]]:
    occupied: list[bool] = []
    kernels: list[NVec | None] = []
    labels: list[Lab] = []
    for direction in DIRS:
        neighbor = add(site, direction)
        present = in_U(neighbor)
        occupied.append(present)
        if present:
            kernel = n_at(neighbor)
            kernels.append(kernel)
            unique = unique_axis_label(kernel)
            labels.append(EMPTY if unique is None else unique)
        else:
            kernels.append(None)
            labels.append(EMPTY)
    return tuple(occupied), tuple(kernels), tuple(labels)


def slot_odd_complete(
    occupied: tuple[bool, ...],
    kernels: tuple[NVec | None, ...],
    unique_labels: tuple[Lab, ...],
) -> tuple[Lab, ...]:
    labels = list(unique_labels)
    for plus_i, minus_i in AXIS_PAIRS:
        if not (occupied[plus_i] and occupied[minus_i]):
            continue
        left = kernels[plus_i]
        right = kernels[minus_i]
        if left is None or right is None:
            continue
        if left == right and unique_axis_label(left) is None:
            labels[plus_i] = PLUS
            labels[minus_i] = MINUS
    return tuple(labels)


def letters_to_coloring(labels: tuple[Lab, ...]) -> tuple[int, ...]:
    return tuple(LETTER_TO_COLOR[label] for label in labels)


def det3(matrix: tuple[tuple[int, ...], ...]) -> int:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def apply_matrix(matrix: tuple[tuple[int, ...], ...], vector: tuple[int, ...] | NVec) -> tuple:
    return tuple(
        sum(matrix[row][col] * vector[col] for col in range(3)) for row in range(3)
    )


def proper_rotations() -> tuple[tuple[tuple[int, ...], ...], ...]:
    records: list[tuple[tuple[int, ...], ...]] = []
    seen: set[tuple[tuple[int, ...], ...]] = set()
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            rows = []
            for row, col in enumerate(perm):
                line = [0, 0, 0]
                line[col] = signs[row]
                rows.append(tuple(line))
            matrix = tuple(rows)
            if matrix not in seen and det3(matrix) == 1:
                seen.add(matrix)
                records.append(matrix)
    return tuple(records)


def direction_perm(matrix: tuple[tuple[int, ...], ...]) -> tuple[int, ...]:
    return tuple(DIRS.index(apply_matrix(matrix, direction)) for direction in DIRS)


def act_coloring(perm: tuple[int, ...], coloring: tuple[int, ...]) -> tuple[int, ...]:
    out = [0] * 6
    for source, image in enumerate(perm):
        out[image] = coloring[source]
    return tuple(out)


def july3_k3_pair(proper_perms: tuple[tuple[int, ...], ...]) -> frozenset[tuple[int, ...]]:
    unseen = set(itertools.product(range(3), repeat=6))
    orbits: list[set[tuple[int, ...]]] = []
    while unseen:
        seed = min(unseen)
        orbit = {act_coloring(perm, seed) for perm in proper_perms}
        orbits.append(orbit)
        unseen -= orbit
    inversion = ((-1, 0, 0), (0, -1, 0), (0, 0, -1))
    inversion_perm = direction_perm(inversion)
    ids = {coloring: index for index, orbit in enumerate(orbits) for coloring in orbit}
    pair_ids: set[tuple[int, int]] = set()
    for index, orbit in enumerate(orbits):
        image = ids[act_coloring(inversion_perm, next(iter(orbit)))]
        if image != index:
            pair_ids.add(tuple(sorted((index, image))))
    if len(pair_ids) != 1:
        raise RuntimeError(f"expected one k=3 chiral pair, found {pair_ids!r}")
    left, right = next(iter(pair_ids))
    return frozenset(orbits[left] | orbits[right])


def fully_mixed_bicolored(coloring: tuple[int, ...]) -> bool:
    if Counter(coloring) != {0: 2, 1: 2, 2: 2}:
        return False
    return all(coloring[plus_i] != coloring[minus_i] for plus_i, minus_i in AXIS_PAIRS)


def rotate_kernels(
    matrix: tuple[tuple[int, ...], ...],
    kernels: tuple[NVec | None, ...],
) -> tuple[NVec | None, ...]:
    out: list[NVec | None] = [None] * 6
    for source, direction in enumerate(DIRS):
        image = DIRS.index(apply_matrix(matrix, direction))
        kernel = kernels[source]
        if kernel is None:
            out[image] = None
        else:
            rotated = apply_matrix(matrix, kernel)
            out[image] = (rotated[0], rotated[1], rotated[2])
    return tuple(out)


def rotate_labels(
    matrix: tuple[tuple[int, ...], ...],
    labels: tuple[Lab, ...],
) -> tuple[Lab, ...]:
    out = [EMPTY] * 6
    for source, direction in enumerate(DIRS):
        image = DIRS.index(apply_matrix(matrix, direction))
        out[image] = labels[source]
    return tuple(out)


def complete_from_kernels(kernels: tuple[NVec | None, ...]) -> tuple[Lab, ...]:
    occupied = tuple(kernel is not None for kernel in kernels)
    unique_labels = []
    for kernel in kernels:
        if kernel is None:
            unique_labels.append(EMPTY)
        else:
            unique = unique_axis_label(kernel)
            unique_labels.append(EMPTY if unique is None else unique)
    return slot_odd_complete(occupied, kernels, tuple(unique_labels))


def commuting_count(
    kernels: tuple[NVec | None, ...],
    rotations: tuple[tuple[tuple[int, ...], ...], ...],
) -> int:
    base = complete_from_kernels(kernels)
    count = 0
    for matrix in rotations:
        moved = rotate_labels(matrix, base)
        rebuilt = complete_from_kernels(rotate_kernels(matrix, kernels))
        count += int(moved == rebuilt)
    return count


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


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    note_flat = normalize(note)
    axiom_flat = normalize(axiom)
    sites = occupancy_sites()
    rotations = proper_rotations()
    proper_perms = tuple(direction_perm(matrix) for matrix in rotations)
    pair = july3_k3_pair(proper_perms)
    mixed = frozenset(
        coloring
        for coloring in itertools.product(range(3), repeat=6)
        if fully_mixed_bicolored(coloring)
    )

    occ1, n1, uniq1 = star(V1)
    occ2, n2, uniq2 = star(V2)
    complete1 = slot_odd_complete(occ1, n1, uniq1)
    complete2 = slot_odd_complete(occ2, n2, uniq2)
    color1 = letters_to_coloring(complete1)
    color2 = letters_to_coloring(complete2)
    fire1 = color1 in pair
    fire2 = color2 in pair
    commute1 = commuting_count(n1, rotations)
    commute2 = commuting_count(n2, rotations)
    even_axis = tuple(
        matrix
        for matrix in rotations
        if all(matrix[row][col] >= 0 for row in range(3) for col in range(3))
    )

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print("U: B_2(0) ∪ B_2((2,0,0)); |U| computed by ℓ¹ membership only")
    print(f"v1={V1} mask={tuple(int(flag) for flag in occ1)} complete={complete1} fire={int(fire1)}")
    print(f"v2={V2} mask={tuple(int(flag) for flag in occ2)} complete={complete2} fire={int(fire2)}")
    print(f"N_pair={len(pair)} commute_v1={commute1}/24 commute_v2={commute2}/24")

    checks.check(
        "audit-input-paths",
        AUDIT_INPUT_PATHS
        == (
            "docs/TWO_BALL_SLOT_ODD_TIE_LABEL_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
        "declared inputs are exactly the note and the current axiom memo",
    )
    checks.check(
        "lattice-clause",
        "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard translations, and proper cubic rotations about each site."
        in axiom_flat,
        "Lattice supplies Z^3, six-neighbor adjacency, and proper cubic rotations",
    )
    checks.check(
        "admissibility-covariance-clause",
        "one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations"
        in axiom_flat,
        "Admissibility requires one covariant nearest-neighbor rule",
    )
    checks.check(
        "U-two-ball",
        len(sites) == 43
        and CENTER in sites
        and OTHER in sites
        and V1 not in sites
        and V2 not in sites
        and all(in_U(point) for point in sites),
        f"|U|={len(sites)}; both positive sites unread",
    )
    checks.check(
        "v1-mask-and-equal-n",
        occ1 == (True, True, True, False, False, True)
        and n1[0] == n1[1] == (Fraction(0), Fraction(1, 3), Fraction(-1, 3))
        and unique_axis_label(n1[0]) is None
        and uniq1 == (EMPTY, EMPTY, MINUS, EMPTY, EMPTY, PLUS),
        "v1 mask (1,1,1,0,0,1); tied n=(0,1/3,-1/3); unique-axis −,+ on +y,−z",
    )
    checks.check(
        "v2-mask-and-equal-n",
        occ2 == (True, True, False, True, True, False)
        and n2[0] == n2[1] == (Fraction(0), Fraction(-1, 3), Fraction(1, 3))
        and unique_axis_label(n2[0]) is None
        and uniq2 == (EMPTY, EMPTY, EMPTY, PLUS, MINUS, EMPTY),
        "v2 mask (1,1,0,1,1,0); tied n=(0,-1/3,1/3); unique-axis +,- on −y,+z",
    )
    checks.check(
        "theorem1-completed-tuples",
        complete1 == (PLUS, MINUS, MINUS, EMPTY, EMPTY, PLUS)
        and complete2 == (PLUS, MINUS, EMPTY, PLUS, MINUS, EMPTY)
        and complete1[0] == PLUS
        and complete1[1] == MINUS
        and complete2[0] == PLUS
        and complete2[1] == MINUS,
        "slot-odd completions (+,−,−,0,0,+) and (+,−,0,+,−,0)",
    )
    checks.check(
        "july3-pair-census",
        len(rotations) == 24
        and len(set(proper_perms)) == 24
        and len(pair) == 48
        and pair == mixed
        and color1 in pair
        and color2 in pair,
        "unique k=3 pair has 48 fully-mixed axis-bicolored 6-tuples and contains both completions",
    )
    checks.check(
        "theorem1-N-fire",
        fire1
        and fire2
        and int(fire1) + int(fire2) == 2,
        "N_fire=1 at each positive unread site",
    )
    checks.check(
        "theorem2-not-cube-equivariant",
        commute1 == 3
        and commute2 == 3
        and commute1 < 24
        and commute2 < 24
        and len(even_axis) == 3,
        f"full completion commutes for {commute1}/24 and {commute2}/24 proper rotations",
    )
    checks.check(
        "theorem3-displayed-not-adopted",
        "Displayed, not adopted" in note
        and "Do not write" in note
        and "slot-odd" in note
        and "Admissibility" in note
        and "hypothetical_axiom_status: \"no edit\"" in note,
        "the note displays the tie-break and refuses adoption into Admissibility",
    )
    checks.check(
        "claim-scope",
        'claim_scope: "On U at the two positive unread sites, whether the slot-odd tie-break of equal-n neighbors yields a July-3 pair member, and whether that tie-break is cube-equivariant on the star, is reported. Displayed, not adopted."'
        in note,
        "front matter carries the dispatch claim_scope verbatim",
    )
    checks.check(
        "forbidden-phrases",
        "G_N" not in note
        and "1/r" not in note
        and "Lattice-named" not in note
        and "not a TOE" not in note
        and "L1" not in note,
        "the note omits the dispatch-forbidden tokens",
    )
    checks.check(
        "no-axiom-edit",
        "### Lattice / Physical Locality" in axiom
        and "one fixed nearest-neighbor admissibility rule" in axiom
        and "slot-odd" not in axiom
        and "tie-break" not in axiom,
        "the axiom memo is unread for edit and does not contain the displayed rule",
    )
    checks.check(
        "note-contract",
        "**Type:** bounded_theorem" in note
        and "actual_current_surface_status: bounded-support" in note
        and "bare_retained_allowed: false" in note
        and "[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)" in note
        and "Theorem 1" in note
        and "Theorem 2" in note
        and "Theorem 3" in note,
        "bounded-support note states the three theorems and the current axiom memo",
    )
    print(
        "per_star: occupancy kernel n=d/3, unique-axis sign, and slot-odd completion "
        "are evaluated only at v1 and v2 on U"
    )
    print(
        "lattice_wide: checked and not executed — no further unread site or grown occupancy is scored"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
