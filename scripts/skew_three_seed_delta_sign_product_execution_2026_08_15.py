#!/usr/bin/env python3
"""Execute the already-labeled delta-sign-product 6-tuple on the three-ball union.

The July-3 k=3 pair is reconstructed as the unique pair of proper-cube orbits
of fully-mixed 3-letter 6-tuples. The 6-tuple is used as a displayed neighbor
label, not written into Admissibility. No cache or governance surface is written.
"""

from __future__ import annotations

import itertools
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "SKEW_THREE_SEED_DELTA_SIGN_PRODUCT_EXECUTION_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/SKEW_THREE_SEED_DELTA_SIGN_PRODUCT_EXECUTION_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Point = tuple[int, int, int]
Coloring = tuple[int, ...]

SEEDS: tuple[Point, ...] = ((0, 0, 0), (2, 0, 0), (1, 2, 1))
V: Point = (-1, 1, 1)
RADIUS = 2
SHIFTS: tuple[Point, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
DIR_INDEX = {shift: index for index, shift in enumerate(SHIFTS)}
C_LETTERS: tuple[str, ...] = ("+", "0", "+", "-", "0", "-")
LETTER_TO_COLOR = {"0": 0, "+": 1, "-": 2}
CLAIM_SCOPE = (
    "On the off-axis three-ball union at unread v=(-1,1,1), whether the "
    "delta-sign-product 6-tuple (+,0,+,−,0,−) fires the July-3 k=3 pair is "
    "reported. Displayed, not adopted."
)
FORBIDDEN = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")


def normalize(text: str) -> str:
    return " ".join(text.split())


def add(left: Point, right: Point) -> Point:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def l1(left: Point, right: Point) -> int:
    return abs(left[0] - right[0]) + abs(left[1] - right[1]) + abs(left[2] - right[2])


def ball(center: Point, radius: int = RADIUS) -> frozenset[Point]:
    sites: set[Point] = set()
    span = range(-radius, radius + 1)
    for x, y, z in itertools.product(span, repeat=3):
        point = add(center, (x, y, z))
        if l1(point, center) <= radius:
            sites.add(point)
    return frozenset(sites)


def locked_union(seeds: tuple[Point, ...] = SEEDS) -> frozenset[Point]:
    occupied: set[Point] = set()
    for seed in seeds:
        occupied |= ball(seed)
    return frozenset(occupied)


def star(site: Point) -> tuple[Point, ...]:
    return tuple(add(site, shift) for shift in SHIFTS)


def occupancy_mask(occupied: frozenset[Point], site: Point) -> tuple[int, ...]:
    return tuple(int(neighbor in occupied) for neighbor in star(site))


def encode(letters: tuple[str, ...]) -> Coloring:
    return tuple(LETTER_TO_COLOR[letter] for letter in letters)


def det3(matrix: tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]) -> int:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def apply_matrix(
    matrix: tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]],
    vector: Point,
) -> Point:
    return (
        matrix[0][0] * vector[0] + matrix[0][1] * vector[1] + matrix[0][2] * vector[2],
        matrix[1][0] * vector[0] + matrix[1][1] * vector[1] + matrix[1][2] * vector[2],
        matrix[2][0] * vector[0] + matrix[2][1] * vector[1] + matrix[2][2] * vector[2],
    )


def direction_perm(
    matrix: tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]
) -> tuple[int, ...]:
    return tuple(DIR_INDEX[apply_matrix(matrix, shift)] for shift in SHIFTS)


def act_col(perm: tuple[int, ...], coloring: Coloring) -> Coloring:
    out = [0] * len(coloring)
    for source, image in enumerate(perm):
        out[image] = coloring[source]
    return tuple(out)


def proper_direction_perms() -> tuple[tuple[int, ...], ...]:
    perms: list[tuple[int, ...]] = []
    seen: set[tuple[int, ...]] = set()
    for order in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            rows = []
            for row, axis in enumerate(order):
                entry = [0, 0, 0]
                entry[axis] = signs[row]
                rows.append(tuple(entry))
            matrix = (rows[0], rows[1], rows[2])
            if det3(matrix) != 1:
                continue
            perm = direction_perm(matrix)
            if perm not in seen:
                seen.add(perm)
                perms.append(perm)
    return tuple(perms)


def inversion_perm() -> tuple[int, ...]:
    return direction_perm(((-1, 0, 0), (0, -1, 0), (0, 0, -1)))


def july3_k3_pair() -> frozenset[Coloring]:
    proper = proper_direction_perms()
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


def pair_fires(letters: tuple[str, ...], members: frozenset[Coloring]) -> bool:
    return encode(letters) in members


def execute(
    occupied: frozenset[Point],
    site: Point,
    letters: tuple[str, ...],
    members: frozenset[Coloring],
) -> tuple[frozenset[Point], frozenset[Point]]:
    """One displayed pair step: form at an unread site iff the 6-tuple is a member."""
    if site in occupied:
        return occupied, frozenset()
    new = frozenset({site}) if pair_fires(letters, members) else frozenset()
    return occupied | new, new


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
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)

    print(
        "external_scientific_inputs: current Lattice, Admissibility, and Record "
        "boundaries are source-bound; the July-3 k=3 pair is reconstructed from "
        "the proper-cube action on 3-letter 6-tuples; no observation or fit is used"
    )
    print(
        "package_local_integrity_reads: the note and current minimal axiom are "
        "read; no cache or governance surface is written"
    )
    print(
        "negative_scope: only the locked three-ball union and the six-neighbor "
        "star at unread v are scored; the 6-tuple is displayed, not adopted"
    )

    checks.check(
        "audit-input-paths",
        "declared inputs are exactly the note and current axiom",
        AUDIT_INPUT_PATHS
        == (
            "docs/SKEW_THREE_SEED_DELTA_SIGN_PRODUCT_EXECUTION_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and AUDIT_TIMEOUT_SEC == 120
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )

    lattice_sentence = (
        "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
    )
    admissibility_sentence = (
        "For each site, the probability distribution over the possibilities is "
        "determined by, and varies with, the nearest-neighbor conditions."
    )
    record_lock = "When present, a record locks exactly one admissible local possibility."
    record_permanent = "A site never carries more than one record; records are permanent."
    record_absence = "A site with no record cannot be read."
    formation_boundary = "does not supply the formation site, probability, or rate"
    checks.check(
        "source-lattice",
        "current cubic nearest-neighbor wording is pinned",
        lattice_sentence in normalized_axiom and lattice_sentence in normalized_note,
    )
    checks.check(
        "source-admissibility",
        "current local-distribution wording is pinned",
        admissibility_sentence in normalized_axiom and admissibility_sentence in normalized_note,
    )
    checks.check(
        "source-record-boundary",
        "current lock, permanence, and unreadable-absence wording is pinned",
        all(
            phrase in normalized_axiom
            for phrase in (record_lock, record_permanent, record_absence)
        )
        and all(
            phrase in normalized_note
            for phrase in (record_lock, record_permanent, record_absence)
        ),
    )
    checks.check(
        "source-formation-boundary",
        "formation site remains outside Admissibility",
        formation_boundary in normalized_axiom and formation_boundary in normalized_note,
    )

    occupied = locked_union()
    neighbors = star(V)
    mask = occupancy_mask(occupied, V)
    letter_support = tuple(int(letter != "0") for letter in C_LETTERS)
    members = july3_k3_pair()
    encoded = encode(C_LETTERS)
    after, new_locks = execute(occupied, V, C_LETTERS, members)

    checks.check(
        "v-unread",
        "v is outside every radius-2 seed ball, so it is unread",
        V not in occupied and all(l1(V, seed) > RADIUS for seed in SEEDS),
        (V in occupied, [l1(V, seed) for seed in SEEDS]),
    )
    checks.check(
        "star-occupancy",
        "the six-neighbor occupancy of U at v is exactly the support of c",
        mask == letter_support == (1, 0, 1, 1, 0, 1),
        (mask, letter_support, neighbors),
    )
    checks.check(
        "pair-census",
        "the reconstructed July-3 k=3 pair has 48 members",
        len(members) == 48 and encoded in members,
        (len(members), encoded),
    )
    checks.check(
        "c-is-member",
        "the displayed 6-tuple (+,0,+,-,0,-) is a pair member",
        pair_fires(C_LETTERS, members) and encoded == (1, 0, 1, 2, 0, 2),
        encoded,
    )
    checks.check(
        "n-new",
        "the pair fires at unread v and yields N_new=1",
        pair_fires(C_LETTERS, members) and len(new_locks) == 1,
        new_locks,
    )
    checks.check(
        "new-lock-is-v",
        "the unique new lock is v",
        new_locks == frozenset({V}),
        new_locks,
    )
    checks.check(
        "u-permanence",
        "every previously locked site remains locked",
        occupied <= after and after == occupied | frozenset({V}),
        (len(occupied), len(after)),
    )

    silent = execute(occupied, V, ("0",) * 6, members)
    same_mask_miss = ("+", "0", "+", "+", "0", "-")
    miss = execute(occupied, V, same_mask_miss, members)
    checks.check(
        "empty-tuple-silent",
        "the all-empty 6-tuple does not form at v",
        silent == (occupied, frozenset()) and encode(("0",) * 6) not in members,
    )
    checks.check(
        "same-mask-nonmember-silent",
        "a same-support non-member 6-tuple does not fire",
        occupancy_mask(occupied, V) == tuple(int(letter != "0") for letter in same_mask_miss)
        and encode(same_mask_miss) not in members
        and miss == (occupied, frozenset()),
        encode(same_mask_miss),
    )

    already = execute(occupied | frozenset({V}), V, C_LETTERS, members)
    checks.check(
        "already-locked-silent",
        "a second step at the same site adds no lock",
        already == (occupied | frozenset({V}), frozenset()),
    )

    required = (
        "actual_current_surface_status: bounded-support",
        "target_claim_type: bounded_theorem",
        'hypothetical_axiom_status: "no edit"',
        "authors no audit verdict",
        "Displayed, not adopted",
        "does not attach L1",
        "N_new=1",
        CLAIM_SCOPE,
    )
    forbidden_note = FORBIDDEN + (
        "we adopt",
        "write c into Admissibility",
        "fourth ball",
        "4th ball",
        "L_phys",
    )
    checks.check(
        "claim-scope",
        "the note reports the displayed execution scope and does not adopt it",
        CLAIM_SCOPE in note and "Displayed, not adopted" in note,
    )
    checks.check(
        "note-contract",
        "machine fields, execution report, and display-only hygiene hold",
        all(phrase in note for phrase in required)
        and all(token not in note for token in forbidden_note)
        and "new axiom" not in note.lower(),
    )
    checks.check(
        "axiom-unedited",
        "the live axiom memo does not contain the displayed 6-tuple or product rule",
        all(
            phrase not in axiom
            for phrase in (
                "(+,0,+,−,0,−)",
                "(+,0,+,-,0,-)",
                "delta-sign-product",
                "July-3 k=3 pair",
            )
        )
        and all(token not in axiom for token in FORBIDDEN),
    )
    checks.check(
        "no-l1-attachment",
        "the note refuses L1 attachment and a fourth seed ball",
        "does not attach L1" in note
        and "fourth seed ball" in note.lower()
        and "do not attach l1" in note.lower(),
    )

    script_text = Path(__file__).read_text(encoding="utf-8")
    checks.check(
        "forbidden-tokens",
        "note and runner omit the forbidden gravity and slogan tokens",
        all(token not in note for token in FORBIDDEN)
        and all(token not in script_text.split("FORBIDDEN", 1)[0] for token in FORBIDDEN),
    )

    print("per_element: v and its six neighbors are scored against the three seed balls")
    print("per_site: one unread center is tested for pair membership and permanence")
    print("per_mode: checked and not executed — no spectral claim occurs")
    print("per_block: the displayed 6-tuple is executed once on this union")
    print("lattice_wide: checked and not executed — only U and the star at v are scored")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
