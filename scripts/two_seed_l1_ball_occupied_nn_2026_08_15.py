#!/usr/bin/env python3
"""Exact occupied 6-NN census for the union of two small ℓ¹ balls.

Occupied set U = B_r(0) ∪ B_s(p) with r,s in {0,1,2} and p one of
(1,0,0), (1,1,0), (1,1,1), (2,0,0). Unread sites are Z^3 points outside
U inside the box |x|,|y|,|z| ≤ 6. Occupied-NN count is how many of the
six axial neighbors lie in U. Finite integer geometry only. No axiom
edit, no cache write, no network, no citation manifest.
"""

from __future__ import annotations

from itertools import product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "TWO_SEED_L1_BALL_OCCUPIED_NN_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/TWO_SEED_L1_BALL_OCCUPIED_NN_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Point = tuple[int, int, int]
ORIGIN: Point = (0, 0, 0)
SHIFTS: tuple[Point, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
SEPARATIONS: tuple[Point, ...] = (
    (1, 0, 0),
    (1, 1, 0),
    (1, 1, 1),
    (2, 0, 0),
)
RADII: tuple[int, ...] = (0, 1, 2)
BOX = 6


def normalize(text: str) -> str:
    return " ".join(text.split())


def add(left: Point, right: Point) -> Point:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def l1(left: Point, right: Point = ORIGIN) -> int:
    return abs(left[0] - right[0]) + abs(left[1] - right[1]) + abs(left[2] - right[2])


def ball(center: Point, radius: int) -> frozenset[Point]:
    sites: list[Point] = []
    for offset in product(range(-radius, radius + 1), repeat=3):
        if l1(offset) <= radius:
            sites.append(add(center, offset))
    return frozenset(sites)


def occupied_neighbors(site: Point, occupied: frozenset[Point]) -> tuple[Point, ...]:
    return tuple(add(site, shift) for shift in SHIFTS if add(site, shift) in occupied)


def box_sites() -> tuple[Point, ...]:
    return tuple(product(range(-BOX, BOX + 1), repeat=3))


def score_union(center_p: Point, radius_r: int, radius_s: int) -> dict[str, object]:
    occupied = ball(ORIGIN, radius_r) | ball(center_p, radius_s)
    max_count = -1
    ge4: list[tuple[Point, tuple[Point, ...]]] = []
    max_sites: list[tuple[Point, tuple[Point, ...]]] = []
    for site in box_sites():
        if site in occupied:
            continue
        neighbors = occupied_neighbors(site, occupied)
        count = len(neighbors)
        if count > max_count:
            max_count = count
            max_sites = [(site, neighbors)]
        elif count == max_count:
            max_sites.append((site, neighbors))
        if count >= 4:
            ge4.append((site, neighbors))
    lex_max = min(max_sites, key=lambda item: item[0]) if max_sites else None
    lex_ge4 = min(ge4, key=lambda item: item[0]) if ge4 else None
    return {
        "p": center_p,
        "r": radius_r,
        "s": radius_s,
        "size": len(occupied),
        "max_count": max_count,
        "reaches_four": max_count >= 4,
        "lex_max": lex_max,
        "lex_ge4": lex_ge4,
        "ge4_sites": tuple(sorted(site for site, _ in ge4)),
    }


def one_ball_max(radius: int) -> int:
    occupied = ball(ORIGIN, radius)
    return max(
        (
            len(occupied_neighbors(site, occupied))
            for site in box_sites()
            if site not in occupied
        ),
        default=0,
    )


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
        result = bool(condition)
        self.passed += int(result)
        self.failed += int(not result)
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")
        if not result and residual is not None:
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
        "external_scientific_inputs: current Lattice nearest-neighbor wording "
        "is source-bound; the two-ball sets are constructed here; no observation "
        "or fit is used"
    )
    print(
        "package_local_integrity_reads: the note and current minimal axiom memo "
        "are read; no cache, citation manifest, or governance surface is written"
    )
    print(
        "negative_scope: two-seed geometry is scored and displayed, not written "
        "into Admissibility and not attached to L1"
    )

    rows = [
        score_union(center_p, radius_r, radius_s)
        for center_p in SEPARATIONS
        for radius_r in RADII
        for radius_s in RADII
    ]
    reaching = [row for row in rows if row["reaches_four"]]
    one_ball = {radius: one_ball_max(radius) for radius in RADII}

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/TWO_SEED_L1_BALL_OCCUPIED_NN_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and AUDIT_TIMEOUT_SEC == 120,
    )
    lattice_sentence = (
        "Physical sites are the points of the cubic lattice `Z^3`, with "
        "nearest-neighbor adjacency, standard translations, and proper cubic "
        "rotations about each site."
    )
    checks.check(
        "source-lattice",
        "current cubic nearest-neighbor wording is pinned",
        lattice_sentence in normalized_axiom and lattice_sentence in normalized_note,
    )
    checks.check(
        "census-cardinality",
        "the declared (p,r,s) family has exactly 36 unions",
        len(rows) == 4 * 3 * 3 == 36,
        len(rows),
    )
    checks.check(
        "one-ball-control",
        "a single ℓ¹ ball of radius 0, 1, or 2 has unread occupied-NN max 1, 2, 3",
        one_ball == {0: 1, 1: 2, 2: 3},
        one_ball,
    )
    checks.check(
        "unique-four",
        "exactly one declared union reaches occupied-NN count 4",
        len(reaching) == 1
        and reaching[0]["p"] == (2, 0, 0)
        and reaching[0]["r"] == 2
        and reaching[0]["s"] == 2
        and reaching[0]["max_count"] == 4,
        [(row["p"], row["r"], row["s"], row["max_count"]) for row in reaching],
    )

    witness_row = reaching[0]
    lex_site, lex_neighbors = witness_row["lex_ge4"]
    checks.check(
        "lex-first-witness",
        "the lex-first unread site with occupied-NN ≥ 4 is (1,-1,-1)",
        lex_site == (1, -1, -1),
        lex_site,
    )
    checks.check(
        "occupied-nn-list",
        "that witness has occupied neighbors (2,-1,-1), (0,-1,-1), (1,0,-1), (1,-1,0)",
        lex_neighbors
        == (
            (2, -1, -1),
            (0, -1, -1),
            (1, 0, -1),
            (1, -1, 0),
        ),
        lex_neighbors,
    )
    checks.check(
        "four-site-orbit",
        "exactly the four unread sites (1,±1,±1) reach count 4 on that union",
        witness_row["ge4_sites"]
        == ((1, -1, -1), (1, -1, 1), (1, 1, -1), (1, 1, 1)),
        witness_row["ge4_sites"],
    )
    checks.check(
        "witness-unread",
        "the lex-first witness lies outside both radius-2 balls and inside the box",
        l1(lex_site) == 3
        and l1(lex_site, (2, 0, 0)) == 3
        and max(abs(coord) for coord in lex_site) <= BOX,
    )
    checks.check(
        "other-separations-stay-below-four",
        "the other 35 declared unions have unread occupied-NN max ≤ 3",
        all(row["max_count"] <= 3 for row in rows if row is not witness_row),
        max(row["max_count"] for row in rows if row is not witness_row),
    )

    reported_max_lines = (
        "`p=(1,0,0)`: max occupied-NN by `(r,s)` is "
        "`[[1,2,3],[2,2,3],[3,3,3]]`",
        "`p=(1,1,0)`: max occupied-NN by `(r,s)` is "
        "`[[2,2,3],[2,3,3],[3,3,3]]`",
        "`p=(1,1,1)`: max occupied-NN by `(r,s)` is "
        "`[[1,3,3],[3,2,3],[3,3,3]]`",
        "`p=(2,0,0)`: max occupied-NN by `(r,s)` is "
        "`[[2,2,3],[2,3,3],[3,3,4]]`",
    )

    def matrix_for(center_p: Point) -> list[list[int]]:
        return [
            [
                next(
                    row["max_count"]
                    for row in rows
                    if row["p"] == center_p and row["r"] == radius_r and row["s"] == radius_s
                )
                for radius_s in RADII
            ]
            for radius_r in RADII
        ]

    computed_matrices = {
        (1, 0, 0): [[1, 2, 3], [2, 2, 3], [3, 3, 3]],
        (1, 1, 0): [[2, 2, 3], [2, 3, 3], [3, 3, 3]],
        (1, 1, 1): [[1, 3, 3], [3, 2, 3], [3, 3, 3]],
        (2, 0, 0): [[2, 2, 3], [2, 3, 3], [3, 3, 4]],
    }
    checks.check(
        "theorem1-matrices",
        "computed per-separation max matrices match the note display",
        all(matrix_for(center_p) == expected for center_p, expected in computed_matrices.items())
        and all(line in note for line in reported_max_lines),
        {center_p: matrix_for(center_p) for center_p in SEPARATIONS},
    )
    checks.check(
        "theorem2-note-witness",
        "the note reports the lex-first unread witness and its occupied-NN list",
        all(
            phrase in normalized_note
            for phrase in (
                "p = (2,0,0)",
                "r = 2",
                "s = 2",
                "(1,-1,-1)",
                "(2,-1,-1)",
                "(0,-1,-1)",
                "(1,0,-1)",
                "(1,-1,0)",
            )
        ),
    )
    claim_scope = (
        "Whether the union of two ℓ¹ balls of radii 0..2 at the listed "
        "separations ever gives an unread site 4 or more occupied 6-NN is "
        "reported. Displayed, not adopted."
    )
    checks.check(
        "claim-scope",
        "frontmatter reports the two-ball 4-NN question as displayed, not adopted",
        claim_scope in note,
    )
    checks.check(
        "displayed-not-adopted",
        "Theorem 3 keeps the census displayed and refuses an Admissibility or L1 write",
        all(
            phrase in normalized_note
            for phrase in (
                "Displayed, not adopted",
                "Do not write two-seed geometry into Admissibility",
                "Do not attach L1",
            )
        ),
    )
    checks.check(
        "axiom-unedited",
        "the current axiom memo does not contain two-seed ball geometry",
        all(
            phrase not in axiom
            for phrase in (
                "two-seed",
                "B_r(0)",
                "occupied-NN",
                "ℓ¹ ball",
            )
        ),
    )

    machine_fields = (
        "actual_current_surface_status: bounded-support",
        "target_claim_type: bounded_theorem",
        'hypothetical_axiom_status: "no edit"',
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
    )
    checks.check(
        "machine-status-contract",
        "the note uses controlled bounded-support fields and no-edit status",
        all(field in note for field in machine_fields)
        and all(f"### N{index}" in note for index in range(1, 9)),
    )
    forbidden = (
        "G_N",
        "1/r",
        "1/r^2",
        "Lattice-named",
        "not a TOE",
        "Therefore gravity is impossible",
    )
    checks.check(
        "forbidden-phrases",
        "the note avoids the dispatch-forbidden phrases",
        all(phrase not in note for phrase in forbidden),
        [phrase for phrase in forbidden if phrase in note],
    )
    checks.check(
        "not-need6-or-pairsupp",
        "the note scores two-ball unread 6-NN and refuses leftover-character of one-center or pair-census work",
        all(
            phrase in normalized_note
            for phrase in (
                "not leftover-character of a one-center next-shell bound",
                "not a pair-member slot census",
                "score geometry of two ℓ¹ balls only",
            )
        ),
    )

    print(
        "per_element: each unread site in the box is scored by an exact six-neighbor count"
    )
    print(
        "per_site: the lex-first unread witness and its four occupied neighbors are listed"
    )
    print(
        "per_mode: checked and not executed — no spectral or harmonic claim is used"
    )
    print(
        "per_block: each of the 36 declared two-ball unions is scored independently"
    )
    print(
        "lattice_wide: checked and not executed — no lattice-wide occupancy member or axiom write is claimed"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
