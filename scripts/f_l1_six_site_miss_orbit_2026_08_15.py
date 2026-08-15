#!/usr/bin/env python3
"""Orbit type of the four six-site seeds f_L1 does not fill.

Recomputes every unordered 6-subset of the twelve two-cube sites with
off-patch occupancy 0. Coverage is the number of those seeds from which
f_L1 fills. The miss set M has size 4 and splits into N_orb orbits under
two-cube-preserving rotations. One lex representative per orbit is
displayed, not adopted. The claim is the orbit type, not a 4-row leftover
table. f_L1 is the some-axis-unbalanced (n != 0) map, not Hamming weight.
"""

from __future__ import annotations

from itertools import combinations, permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "F_L1_SIX_SITE_MISS_ORBIT_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/F_L1_SIX_SITE_MISS_ORBIT_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Point = tuple[int, int, int]
Rotation = tuple[tuple[int, int, int], tuple[int, int, int]]
AXES: tuple[Point, ...] = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
SITES: tuple[Point, ...] = tuple(
    (x, y, z) for x in (0, 1, 2) for y in (0, 1) for z in (0, 1)
)
SITE_SET = frozenset(SITES)
N_SIX_SEEDS = 924
COV6_L1 = 920
N_MISS = 4
N_ORB = 1
LEX_TRI: tuple[Point, ...] = (
    (0, 0, 0),
    (0, 0, 1),
    (0, 1, 0),
    (2, 0, 0),
    (2, 0, 1),
    (2, 1, 0),
)
L1_MISS_HISTORY = (6, 8)
L1_MISS_HALT = 8
END_FACE_LOCKS = frozenset(
    (x, y, z) for x in (0, 2) for y in (0, 1) for z in (0, 1)
)


def permutation_sign(permutation: tuple[int, int, int]) -> int:
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(3)
        for j in range(i + 1, 3)
    )
    return -1 if inversions % 2 else 1


CUBE_ROTATIONS: tuple[Rotation, ...] = tuple(
    (permutation, signs)
    for permutation in permutations((0, 1, 2))
    for signs in product((-1, 1), repeat=3)
    if permutation_sign(permutation) * signs[0] * signs[1] * signs[2] == 1
)


def rotate_site(rotation: Rotation, site: Point) -> Point | None:
    """Proper cubic rotation about the two-cube barycenter (1, 1/2, 1/2)."""
    permutation, signs = rotation
    vector = (2 * site[0] - 2, 2 * site[1] - 1, 2 * site[2] - 1)
    image = [0, 0, 0]
    for source_axis in range(3):
        image[permutation[source_axis]] = signs[source_axis] * vector[source_axis]
    if (image[0] + 2) % 2 or (image[1] + 1) % 2 or (image[2] + 1) % 2:
        return None
    return ((image[0] + 2) // 2, (image[1] + 1) // 2, (image[2] + 1) // 2)


def is_two_cube_preserving(rotation: Rotation) -> bool:
    images = []
    for site in SITES:
        image = rotate_site(rotation, site)
        if image is None or image not in SITE_SET:
            return False
        images.append(image)
    return frozenset(images) == SITE_SET


PRESERVING_ROTATIONS: tuple[Rotation, ...] = tuple(
    rotation for rotation in CUBE_ROTATIONS if is_two_cube_preserving(rotation)
)


def normalize(text: str) -> str:
    return " ".join(text.split())


def add(left: Point, right: Point) -> Point:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def occupancy(site: Point, locked: frozenset[Point]) -> int:
    """On-patch occupancy is the lock bit; off-patch occupancy is 0."""
    if site not in SITE_SET:
        return 0
    return 1 if site in locked else 0


def axis_type(site: Point, locked: frozenset[Point]) -> tuple[int, int, int]:
    """Return (n_unbalanced, n_both, n_empty) for the three cubic axes."""
    n_unbalanced = n_both = n_empty = 0
    for axis in AXES:
        plus = occupancy(add(site, axis), locked)
        minus = occupancy(add(site, (-axis[0], -axis[1], -axis[2])), locked)
        if plus == minus == 0:
            n_empty += 1
        elif plus == minus == 1:
            n_both += 1
        else:
            n_unbalanced += 1
    return (n_unbalanced, n_both, n_empty)


def fire_l1(counts: tuple[int, int, int]) -> bool:
    """f_L1: some axis is unbalanced (n != 0). Not Hamming weight."""
    n_unbalanced, _n_both, _n_empty = counts
    return n_unbalanced != 0


def fire_hamming(site: Point, locked: frozenset[Point]) -> bool:
    weight = 0
    for axis in AXES:
        weight += occupancy(add(site, axis), locked)
        weight += occupancy(add(site, (-axis[0], -axis[1], -axis[2])), locked)
    return weight % 2 == 1


def run_l1(seed: frozenset[Point]) -> tuple[tuple[int, ...], bool, frozenset[Point]]:
    locked = frozenset(seed)
    history = [len(locked)]
    for _tick in range(len(SITES)):
        ready = [
            site
            for site in SITES
            if site not in locked and fire_l1(axis_type(site, locked))
        ]
        if not ready:
            break
        locked = locked.union(ready)
        history.append(len(locked))
    return (tuple(history), len(locked) == len(SITES), locked)


def seed_key(seed: frozenset[Point]) -> tuple[Point, ...]:
    return tuple(sorted(seed))


def seed_display(seed: frozenset[Point] | tuple[Point, ...]) -> str:
    points = seed_key(frozenset(seed))
    inner = ", ".join(f"({p[0]},{p[1]},{p[2]})" for p in points)
    return "{" + inner + "}"


def apply_rotation(rotation: Rotation, seed: frozenset[Point]) -> frozenset[Point]:
    images = []
    for site in seed:
        image = rotate_site(rotation, site)
        if image is None:
            raise RuntimeError("rotation left the integer lattice")
        images.append(image)
    return frozenset(images)


def census() -> dict[str, object]:
    n_fill = 0
    misses: list[frozenset[Point]] = []
    histories: dict[tuple[Point, ...], tuple[tuple[int, ...], int, bool, frozenset[Point]]] = {}
    seeds = tuple(frozenset(combo) for combo in combinations(SITES, 6))
    for seed in seeds:
        hist, fill, locked = run_l1(seed)
        if fill:
            n_fill += 1
        else:
            misses.append(seed)
            histories[seed_key(seed)] = (hist, hist[-1], fill, locked)
    misses_lex = tuple(sorted(misses, key=seed_key))
    return {
        "n_seeds": len(seeds),
        "n_fill": n_fill,
        "n_miss": len(misses),
        "misses_lex": misses_lex,
        "histories": histories,
    }


def orbit_of(seed: frozenset[Point]) -> tuple[frozenset[Point], ...]:
    images = {apply_rotation(rotation, seed) for rotation in PRESERVING_ROTATIONS}
    return tuple(sorted(images, key=seed_key))


def orbit_decomposition(
    misses: tuple[frozenset[Point], ...],
) -> tuple[tuple[frozenset[Point], ...], ...]:
    seen: set[frozenset[Point]] = set()
    orbits: list[tuple[frozenset[Point], ...]] = []
    for seed in misses:
        if seed in seen:
            continue
        orbit = orbit_of(seed)
        for member in orbit:
            seen.add(member)
        orbits.append(orbit)
    return tuple(orbits)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool, residual: object | None = None) -> None:
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
    self_source = Path(__file__).read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)
    for relative in AUDIT_INPUT_PATHS:
        (ROOT / relative).read_text(encoding="utf-8")

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("external_scientific_inputs: current Lattice, Admissibility, and Record boundaries; no observations or fits")
    print("integrity_reads: this runner, its note, and the axiom memo; no other scientific inputs")
    print("construction: exhaustive six-site lock-step census under f_L1; miss orbits under two-cube-preserving rotations")
    print("negative_scope: N_orb and the lex representative are displayed; no seed is adopted or written into Admissibility")
    print("cache_write: false")

    checks.check(
        "audit-inputs",
        "the two declared source-bound inputs exist as static literals",
        AUDIT_INPUT_PATHS
        == (
            "docs/F_L1_SIX_SITE_MISS_ORBIT_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and AUDIT_TIMEOUT_SEC == 120
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and 'AUDIT_INPUT_PATHS = (\n'
        '    "docs/F_L1_SIX_SITE_MISS_ORBIT_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ')' in self_source,
    )

    lattice_sentence = "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
    admissibility_sentence = "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions."
    record_lock = "When present, a record locks exactly one admissible local possibility."
    record_content = "A readout value is determined by record content alone."
    record_absence = "A site with no record cannot be read."
    formation_boundary = "does not supply the formation site, probability, or rate"

    checks.check("source-lattice", "current cubic nearest-neighbor wording is pinned", lattice_sentence in normalized_axiom and lattice_sentence in note)
    checks.check("source-admissibility", "current local-distribution wording is pinned", admissibility_sentence in normalized_axiom and admissibility_sentence in note)
    checks.check(
        "source-record-boundary",
        "current lock/content/unreadable-at-absence wording is pinned",
        all(phrase in normalized_axiom for phrase in (record_lock, record_content, record_absence))
        and all(phrase in note for phrase in (record_lock, record_content, record_absence)),
    )
    checks.check(
        "source-formation-boundary",
        "formation site/probability/rate remains outside Admissibility",
        formation_boundary in normalized_axiom and formation_boundary in normalized_note,
    )

    checks.check(
        "two-cube-cardinality",
        "the two-cube is exactly the twelve sites {0,1,2} x {0,1} x {0,1}",
        len(SITES) == 12 and len(SITE_SET) == 12 and SITES[0] == (0, 0, 0) and SITES[-1] == (2, 1, 1),
    )
    checks.check(
        "six-seed-count",
        "there are C(12,6)=924 unordered six-site seeds",
        len(tuple(combinations(SITES, 6))) == N_SIX_SEEDS,
    )

    counts = census()
    n_fill = int(counts["n_fill"])
    n_miss = int(counts["n_miss"])
    misses_lex = counts["misses_lex"]
    histories = counts["histories"]
    assert isinstance(misses_lex, tuple)
    assert isinstance(histories, dict)

    print(f"census: cov6(f_L1)={n_fill} n_miss={n_miss} n_seeds={counts['n_seeds']}")
    for seed in misses_lex:
        hist, halt, fill, locked = histories[seed_key(seed)]
        print(f"  miss {seed_display(seed)} hist_L1={hist} halt={halt} fill={fill}")

    checks.check(
        "theorem-1-abs-m",
        "|M|=4 and cov6(L1)=920 among the 924 six-site seeds",
        counts["n_seeds"] == N_SIX_SEEDS
        and n_fill == COV6_L1
        and n_miss == N_MISS
        and n_fill + n_miss == N_SIX_SEEDS
        and "|M| = 4" in note
        and "cov6(L1) = 920" in note,
        residual=(n_fill, n_miss),
    )

    history_ok = all(
        histories[seed_key(seed)][0] == L1_MISS_HISTORY
        and histories[seed_key(seed)][1] == L1_MISS_HALT
        and histories[seed_key(seed)][2] is False
        and histories[seed_key(seed)][3] == END_FACE_LOCKS
        for seed in misses_lex
    )
    checks.check(
        "theorem-1-common-halt",
        "each miss seed has history (6, 8) and locks only the eight end-face sites",
        history_ok and len(misses_lex) == N_MISS,
        residual=[(seed_display(seed), histories[seed_key(seed)][:3]) for seed in misses_lex],
    )

    checks.check(
        "preserving-rotation-count",
        "exactly eight proper cubic rotations preserve the two-cube",
        len(CUBE_ROTATIONS) == 24
        and len(PRESERVING_ROTATIONS) == 8
        and len(set(PRESERVING_ROTATIONS)) == 8,
    )

    miss_set = set(misses_lex)
    invariant = all(
        apply_rotation(rotation, seed) in miss_set
        for seed in misses_lex
        for rotation in PRESERVING_ROTATIONS
    )
    orbits = orbit_decomposition(misses_lex)
    orbit_sizes = tuple(len(orbit) for orbit in orbits)
    lex_reps = tuple(seed_key(orbit[0]) for orbit in orbits)
    print(f"N_orb={len(orbits)} orbit_sizes={orbit_sizes}")
    for orbit in orbits:
        print(f"  lexrep {seed_display(orbit[0])} size={len(orbit)}")

    checks.check(
        "theorem-2-n-orb",
        "N_orb=1 with orbit size 4",
        invariant
        and len(orbits) == N_ORB
        and orbit_sizes == (4,)
        and sum(orbit_sizes) == N_MISS
        and "N_orb = 1" in note,
        residual=(len(orbits), orbit_sizes),
    )

    checks.check(
        "theorem-2-lex-reps",
        "the lex representative is the three-of-four long-axis edge type",
        lex_reps == (LEX_TRI,)
        and seed_display(LEX_TRI).replace(" ", "") in note.replace(" ", "")
        and "R_tri" in note,
        residual=lex_reps,
    )

    identity_orbits = len(misses_lex)
    checks.check(
        "theorem-2-not-identity-action",
        "the identity-only action has four orbits and is not the claimed type",
        identity_orbits == 4
        and identity_orbits != N_ORB
        and "identity-only action" in normalized_note,
    )

    locked_opp = frozenset(((0, 0, 0), (2, 0, 0)))
    opp2 = axis_type((1, 0, 0), locked_opp)
    hamming_opp = sum(
        occupancy(add((1, 0, 0), shift), locked_opp)
        for shift in AXES + tuple((-a, -b, -c) for a, b, c in AXES)
    )
    checks.check(
        "identity-l1-not-hamming",
        "opp2 has Hamming weight 2 but n_unbalanced=0, so f_L1 does not fire",
        opp2 == (0, 1, 2)
        and hamming_opp == 2
        and not fire_l1(opp2)
        and fire_hamming((1, 0, 0), locked_opp) is False
        and "sum(config) % 2" not in self_source.split("def fire_l1", 1)[1].split("def fire_hamming", 1)[0],
    )

    checks.check(
        "theorem-3-display",
        "the note displays N_orb and the lex representative and does not adopt a seed",
        "displayed, not adopted" in normalized_note.lower()
        and "Do not adopt a seed" in note
        and "not written into Admissibility" in normalized_note,
    )
    checks.check(
        "not-four-row-leftover-table",
        "the claimed object is the orbit type, not a 4-row leftover table",
        "not a 4-row leftover table" in normalized_note
        and "Not leftover-character of `#6465`" in note
        and "three-long-axis-edge" in normalized_note
        and "first `N_orb` at `|S| = 6`" in note
        and "`#6463` was" in note
        and note.count("|M| = 4") >= 1,
    )

    forbidden = (
        "G_" + "N",
        "1/" + "r",
        "1/" + "r^2",
        "Lattice-" + "named",
        "not a " + "TOE",
    )
    checks.check(
        "forbidden-phrases",
        "the note and runner avoid the dispatch-forbidden phrases",
        all(phrase not in note and phrase not in self_source for phrase in forbidden),
    )
    checks.check(
        "claim-scope",
        "the YAML claim_scope states the N_orb display",
        "On the two-cube with off-patch o=0, the four 6-site seeds that f_L1 does not fill form N_orb orbits under two-cube-preserving rotations. Displayed, not adopted."
        in note,
    )
    checks.check(
        "off-patch-zero",
        "off-patch occupancy is the explicit 0 default, not a blank-block",
        "off-patch occupancy is the explicit default `0`" in note
        and "blank-block is a different rule" in note,
    )
    checks.check(
        "l1-definition-in-note",
        "the note defines f_L1 as unbalanced-axis / n != 0 and rejects Hamming",
        "n_unbalanced ≠ 0" in note
        and "not Hamming" in normalized_note
        and "some cubic axis" in normalized_note,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
