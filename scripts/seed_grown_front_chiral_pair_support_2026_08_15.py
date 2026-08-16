#!/usr/bin/env python3
"""Exact six-neighbor occupancy census on seed-grown ℓ¹ balls.

For occupied B_t = {v in Z^3 : |v|_1 <= t} and next shell
S_{t+1} = {v : |v|_1 = t+1}, the runner counts how many of the six axial
neighbors of each unread shell site lie in B_t.  The July-3 unique k=3
chiral pair needs six occupied neighbors.  No cache is written.
"""

from __future__ import annotations

from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/SEED_GROWN_FRONT_CHIRAL_PAIR_SUPPORT_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/SEED_GROWN_FRONT_CHIRAL_PAIR_SUPPORT_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Point = tuple[int, int, int]
SHIFTS: tuple[Point, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
RADII = (0, 1, 2, 3, 4)


def normalize(text: str) -> str:
    return " ".join(text.split())


def add(left: Point, right: Point) -> Point:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def l1(point: Point) -> int:
    return abs(point[0]) + abs(point[1]) + abs(point[2])


def neighbors(site: Point) -> tuple[Point, ...]:
    return tuple(add(site, shift) for shift in SHIFTS)


def nonzero_count(site: Point) -> int:
    return sum(coordinate != 0 for coordinate in site)


def shell(radius: int) -> tuple[Point, ...]:
    if radius < 0:
        raise ValueError("shell radius must be nonnegative")
    if radius == 0:
        return ((0, 0, 0),)
    points: list[Point] = []
    for x in range(-radius, radius + 1):
        rest = radius - abs(x)
        for y in range(-rest, rest + 1):
            zabs = rest - abs(y)
            if zabs == 0:
                points.append((x, y, 0))
            else:
                points.append((x, y, zabs))
                points.append((x, y, -zabs))
    return tuple(points)


def occupied_neighbor_count(site: Point, occupied_radius: int) -> int:
    return sum(l1(neighbor) <= occupied_radius for neighbor in neighbors(site))


def score_radius(occupied_radius: int) -> dict[str, int]:
    next_shell = shell(occupied_radius + 1)
    counts = tuple(occupied_neighbor_count(site, occupied_radius) for site in next_shell)
    identities = tuple(count == nonzero_count(site) for site, count in zip(next_shell, counts, strict=True))
    if not all(identities):
        raise RuntimeError("occupied six-neighbor count must equal the nonzero-coordinate count")
    return {
        "t": occupied_radius,
        "N_shell": len(next_shell),
        "max_occ_nn": max(counts),
        "N_with_6": sum(count == 6 for count in counts),
        "min_occ_nn": min(counts),
    }


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
    source = Path(__file__).read_text(encoding="utf-8")
    note_flat = normalize(note)
    axiom_flat = normalize(axiom)

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print("scientific_dependency: current Lattice/Admissibility/Record sentences; July-3 pair used only as six-neighbor support")
    print("declared_math: seed-grown ℓ¹ balls B_t and six-neighbor occupancy of S_{t+1}")

    checks.check(
        "audit-input-paths",
        "declared inputs are exactly the source note and current axiom memo",
        AUDIT_INPUT_PATHS
        == (
            "docs/SEED_GROWN_FRONT_CHIRAL_PAIR_SUPPORT_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and AUDIT_TIMEOUT_SEC == 120
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and len(AUDIT_INPUT_PATHS) == len(set(AUDIT_INPUT_PATHS)),
    )
    checks.check(
        "audit-input-literals",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        'AUDIT_INPUT_PATHS = (\n    "docs/SEED_GROWN_FRONT_CHIRAL_PAIR_SUPPORT_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n)'
        in source,
    )

    lattice_sentence = "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
    admissibility_sentence = "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions."
    record_absence = "A site with no record cannot be read."
    record_lock = "When present, a record locks exactly one admissible local possibility."
    record_content = "A readout value is determined by record content alone."
    formation_boundary = "does not supply the formation site, probability, or rate"

    checks.check(
        "source-lattice",
        "current cubic nearest-neighbor wording is pinned",
        lattice_sentence in axiom_flat and lattice_sentence in note,
    )
    checks.check(
        "source-admissibility",
        "current local-distribution wording is pinned",
        admissibility_sentence in axiom_flat and admissibility_sentence in note,
    )
    checks.check(
        "source-record-unread",
        "current unread/lock/content boundary is pinned and formation stays outside",
        all(phrase in axiom_flat for phrase in (record_absence, record_lock, record_content, formation_boundary))
        and all(phrase in note for phrase in (record_absence, record_lock, record_content, formation_boundary)),
    )

    rows = tuple(score_radius(radius) for radius in RADII)
    for row in rows:
        print(
            f"t={row['t']} N_shell={row['N_shell']} "
            f"max_occ_nn={row['max_occ_nn']} N_with_6={row['N_with_6']}"
        )

    checks.check(
        "theorem-1-max-lt-6",
        "for each t in 0..4 the max occupied six-neighbor count on S_{t+1} is < 6",
        all(row["max_occ_nn"] < 6 for row in rows),
        [row["max_occ_nn"] for row in rows],
    )
    checks.check(
        "theorem-2-n-with-6",
        "N_with_6 = 0 on every scored next shell",
        all(row["N_with_6"] == 0 for row in rows),
        [row["N_with_6"] for row in rows],
    )
    checks.check(
        "identity-occ-equals-nnz",
        "occupied six-neighbor count equals the number of nonzero coordinates",
        all(row["max_occ_nn"] <= 3 and row["min_occ_nn"] >= 1 for row in rows),
        rows,
    )
    checks.check(
        "shell-cardinality",
        "enumerated |S_{t+1}| equals the ℓ¹ shell formula 4 r^2 + 2",
        all(row["N_shell"] == 4 * (row["t"] + 1) ** 2 + 2 for row in rows),
        [row["N_shell"] for row in rows],
    )

    origin_interior = occupied_neighbor_count((0, 0, 0), 1)
    axis_t0 = occupied_neighbor_count((1, 0, 0), 0)
    checks.check(
        "t0-axis-occupancy",
        "the t=0 next shell is the six axis sites, each with one occupied neighbor",
        rows[0]["N_shell"] == 6 and rows[0]["max_occ_nn"] == 1 and axis_t0 == 1,
        (rows[0], axis_t0),
    )
    checks.check(
        "interior-contrast",
        "the already-occupied origin at t>=1 has six occupied neighbors and is not a next-shell site",
        origin_interior == 6 and l1((0, 0, 0)) == 0,
        origin_interior,
    )

    table_phrases = tuple(
        f"| {row['t']} | {row['N_shell']} | {row['max_occ_nn']} | {row['N_with_6']} |"
        for row in rows
    )
    claim_scope = (
        "On Z^3 seed-grown ℓ¹ balls of radius 0..4, whether any next-shell "
        "site has 6 occupied neighbors — the support the July-3 k=3 chiral "
        "pair needs — is reported. Displayed, not adopted."
    )
    required = (
        claim_scope,
        "Displayed, not adopted",
        "does not attach L1",
        "hypothetical_axiom_status: \"no edit\"",
        "N_with_6",
        "max_occ_nn",
        "N_shell",
        "every axis is bi-colored",
        "cannot turn on the unique `k = 3` chiral channel",
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
        "authors no audit verdict",
        "FAIL / DO NOT SHIP",
        *table_phrases,
    )
    forbidden = (
        "G_N",
        "1/r^2",
        "1/r",
        "Lattice-named",
        "not a TOE",
        "Admissibility now says",
        "attach L1 ledger",
        "trace_class: direct_blocker_closure",
        "reachability_to_target: partially_closes",
    )
    other_retained = note
    for line in (
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
    ):
        other_retained = other_retained.replace(line, "")

    checks.check(
        "note-table",
        "the note reports the computed N_shell, max_occ_nn, and N_with_6 for each t",
        all(phrase in note for phrase in table_phrases),
        [phrase for phrase in table_phrases if phrase not in note],
    )
    checks.check(
        "note-claim-scope",
        "claim_scope is the dispatched displayed-not-adopted occupancy-support sentence",
        claim_scope in note,
    )
    checks.check(
        "displayed-not-adopted",
        "Theorem 3 is displayed, not adopted, and Admissibility is not edited",
        "displayed, not adopted" in note.lower()
        and "not written into Admissibility" in note
        and 'hypothetical_axiom_status: "no edit"' in note
        and "does not attach L1" in note,
    )
    checks.check(
        "note-contract",
        "machine fields, required phrases, and forbidden-rhetoric hygiene hold",
        all(phrase in note for phrase in required)
        and not any(phrase in note for phrase in forbidden)
        and "promoted" not in note.lower()
        and "toe-lphys" not in note
        and "retained" not in other_retained,
        {
            "missing": [phrase for phrase in required if phrase not in note],
            "forbidden_hits": [phrase for phrase in forbidden if phrase in note],
        },
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
