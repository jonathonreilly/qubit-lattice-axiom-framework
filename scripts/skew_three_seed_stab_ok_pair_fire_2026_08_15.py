#!/usr/bin/env python3
"""Stab-ok July-3 pair fire census on one unread three-seed star.

Same U, v, σ as staborb / delloc. Rebuild S = July-3 k=3 pair members
whose support equals the occupancy mask σ and that are pointwise fixed
by Stab(σ). N_fire is how many of those members form exactly v
(N_new=1) with U persisting. Score U and the star at v only.
Displayed, not adopted. No cache is written.
"""

from __future__ import annotations

import ast
import itertools
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/SKEW_THREE_SEED_STAB_OK_PAIR_FIRE_"
    "BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/SKEW_THREE_SEED_STAB_OK_PAIR_FIRE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Point = tuple[int, int, int]
Coloring = tuple[int, ...]
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
FORBIDDEN = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")
CLAIM_SCOPE = (
    'claim_scope: "On the off-axis three-ball union at unread v=(-1,1,1), '
    "how many Stab-invariant July-3 pair members with this occupancy support "
    'fire is reported. Displayed, not adopted."'
)


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


def support(coloring: Coloring) -> Coloring:
    return tuple(int(slot != EMPTY) for slot in coloring)


def det3(matrix: Matrix) -> int:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def mat_vec(matrix: Matrix, vector: Point) -> Point:
    return (
        matrix[0][0] * vector[0] + matrix[0][1] * vector[1] + matrix[0][2] * vector[2],
        matrix[1][0] * vector[0] + matrix[1][1] * vector[1] + matrix[1][2] * vector[2],
        matrix[2][0] * vector[0] + matrix[2][1] * vector[1] + matrix[2][2] * vector[2],
    )


def direction_perm(matrix: Matrix) -> tuple[int, ...]:
    return tuple(DIR_INDEX[mat_vec(matrix, direction)] for direction in DIRS)


def act_col(perm: tuple[int, ...], coloring: Coloring) -> Coloring:
    out = [0] * len(coloring)
    for source, image in enumerate(perm):
        out[image] = coloring[source]
    return tuple(out)


def proper_rotations() -> tuple[tuple[Matrix, tuple[int, ...]], ...]:
    records: list[tuple[Matrix, tuple[int, ...]]] = []
    seen: set[tuple[int, ...]] = set()
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            rows = []
            for row, col in enumerate(perm):
                entry = [0, 0, 0]
                entry[col] = signs[row]
                rows.append(tuple(entry))
            matrix = (rows[0], rows[1], rows[2])
            if det3(matrix) != 1:
                continue
            slots = direction_perm(matrix)
            if slots not in seen:
                seen.add(slots)
                records.append((matrix, slots))
    return tuple(records)


def inversion_perm() -> tuple[int, ...]:
    return direction_perm(((-1, 0, 0), (0, -1, 0), (0, 0, -1)))


def july3_k3_pair() -> frozenset[Coloring]:
    proper = [slots for _matrix, slots in proper_rotations()]
    inversion = inversion_perm()
    unseen = set(itertools.product(range(3), repeat=6))
    pair: set[Coloring] = set()
    while unseen:
        seed = min(unseen)
        orbit = {act_col(perm, seed) for perm in proper}
        unseen -= orbit
        image = act_col(inversion, next(iter(orbit)))
        if image not in orbit:
            pair |= orbit
    return frozenset(pair)


def stab_of(mask: Coloring, rotations: tuple[tuple[Matrix, tuple[int, ...]], ...]) -> tuple[tuple[Matrix, tuple[int, ...]], ...]:
    return tuple(
        (matrix, slots) for matrix, slots in rotations if act_col(slots, mask) == mask
    )


def rebuild_s(
    pair: frozenset[Coloring],
    mask: Coloring,
    stab: tuple[tuple[Matrix, tuple[int, ...]], ...],
) -> tuple[Coloring, ...]:
    members = [coloring for coloring in pair if support(coloring) == mask]
    invariant = [
        coloring
        for coloring in members
        if all(act_col(slots, coloring) == coloring for _matrix, slots in stab)
    ]
    return tuple(sorted(invariant))


def format_tuple(coloring: Coloring) -> str:
    return "(" + ",".join(LETTER[slot] for slot in coloring) + ")"


def execute_at_v(
    occupied: frozenset[Point],
    coloring: Coloring,
    pair: frozenset[Coloring],
) -> tuple[frozenset[Point], int]:
    if V in occupied:
        return occupied, 0
    if coloring not in pair:
        return occupied, 0
    return occupied | {V}, 1


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
        "and Record sentences; July-3 k=3 pair rebuilt from the proper-cube "
        "action on 3-letter 6-tuples"
    )
    print("construction: U=B_2(0)∪B_2((2,0,0))∪B_2((1,2,1)), unread v=(-1,1,1)")
    print(
        "negative_scope: Stab-ok fire census only; displayed, not adopted; "
        "L1 not attached; no 4th equal-radius ball"
    )

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required static two-string literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/SKEW_THREE_SEED_STAB_OK_PAIR_FIRE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
    pair = july3_k3_pair()
    stab = stab_of(mask, rotations)
    support_members = tuple(sorted(c for c in pair if support(c) == mask))
    s_members = rebuild_s(pair, mask, stab)
    fires: list[Coloring] = []
    for coloring in s_members:
        after, n_new = execute_at_v(occupied, coloring, pair)
        if n_new == 1 and V in after and occupied <= after and V not in occupied:
            fires.append(coloring)
    n_fire = len(fires)
    identity = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    flip = ((0, 0, -1), (0, -1, 0), (-1, 0, 0))
    stab_matrices = {matrix for matrix, _slots in stab}

    print(f"U_card={len(occupied)}")
    print(f"v_in_U={V in occupied}")
    print(f"occupancy_mask={mask}")
    print(f"N_pair={len(pair)}")
    print(f"N_pair_support={len(support_members)}")
    print("support_members=" + ",".join(format_tuple(c) for c in support_members))
    print(f"Stab_order={len(stab)}")
    print("Stab_matrices=" + ",".join(str(matrix) for matrix, _slots in stab))
    print(f"S_card={len(s_members)}")
    if s_members:
        print(f"lex_first={format_tuple(s_members[0])}")
    else:
        print("lex_first=none")
    print(f"N_fire={n_fire}")

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
        len(rotations) == 24 and len({slots for _matrix, slots in rotations}) == 24,
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
        mask == (1, 0, 1, 1, 0, 1)
        and "(1, 0, 1, 1, 0, 1)" in note
        and len(pair) == 48,
    )
    checks.check(
        "theorem-1-rebuild-s",
        "S is rebuilt; |S| and the lex-first member (or its absence) are reported",
        f"|S| = {len(s_members)}" in note
        and (
            (
                len(s_members) == 0
                and "no lex-first" in note_flat
            )
            or (
                len(s_members) > 0
                and format_tuple(s_members[0]) in note
            )
        )
        and identity in stab_matrices
        and (flip in stab_matrices if len(stab) == 2 else True)
        and all(support(c) == mask for c in s_members)
        and all(
            act_col(slots, coloring) == coloring
            for coloring in s_members
            for _matrix, slots in stab
        ),
        residual=(len(s_members), [format_tuple(c) for c in s_members]),
    )
    if len(s_members) == 0:
        theorem_2_ok = (
            n_fire == 0
            and "N_fire = 0" in note
            and "no NN-determined G+-extendable pair member exists on this occupancy"
            in note_flat
        )
    else:
        theorem_2_ok = (
            n_fire == len(fires)
            and f"N_fire = {n_fire}" in note
            and n_fire == len(s_members)
        )
    checks.check(
        "theorem-2-n-fire",
        "N_fire counts Stab-ok pair members that form exactly v with U persisting",
        theorem_2_ok and 0 <= n_fire <= len(s_members),
        residual=n_fire,
    )
    checks.check(
        "claim-scope",
        "the note reports the declared displayed claim_scope",
        CLAIM_SCOPE in note,
    )
    checks.check(
        "displayed-not-adopted",
        "the fire census is displayed and is not written into Admissibility",
        "Displayed, not adopted" in note
        and "Do not write a firing c into Admissibility" in note
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
        "the note is not leftover of delrun execution or staborb census",
        "not leftover of delrun" in note_flat
        and "one named product tuple" in note_flat
        and "not leftover of staborb" in note_flat
        and "census, not execution" in note_flat,
    )
    checks.check(
        "admissibility-unedited",
        "no firing 6-tuple is written into Admissibility",
        covariance_clause in axiom_flat
        and "(+,0,+,−,0,−)" not in axiom
        and "Stab-ok" not in axiom
        and "B_2((1,2,1))" not in axiom
        and "N_fire" not in axiom,
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

    print("per_element: |S| and N_fire are exact integers")
    print("per_site: only the unread star center v is scored")
    print("per_mode: no spectral calculation")
    print("per_block: the six-neighbor star at v only")
    print("lattice_wide: checked and not executed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
