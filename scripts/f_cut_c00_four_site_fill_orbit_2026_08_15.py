#!/usr/bin/env python3
"""Orbit type of the seven four-site seeds F_cut (1,0,0,0,0) fills.

Reconfirm |M|=7 on the twelve-vertex two-cube with off-patch occupancy 0,
and that the #6493 face is in M.  Count G-orbits of M under the proper
cube rotations about the box center that permute those twelve sites.
Display N_orb and one lex representative per orbit.  Do not list the
seven.  f_L1 is the some-axis-unbalanced (n!=0) map, not Hamming parity.
The orbit type is displayed, not adopted.
"""

from __future__ import annotations

from itertools import combinations, permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "F_CUT_C00_FOUR_SITE_FILL_ORBIT_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/F_CUT_C00_FOUR_SITE_FILL_ORBIT_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Point = tuple[int, int, int]
Config = tuple[int, int, int, int, int, int]
Matrix = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]

SITES: tuple[Point, ...] = tuple(
    sorted((x, y, z) for x in (0, 1, 2) for y in (0, 1) for z in (0, 1))
)
TWO_CUBE_SET = frozenset(SITES)
AXIS_SHIFTS: tuple[tuple[Point, Point], ...] = (
    ((1, 0, 0), (-1, 0, 0)),
    ((0, 1, 0), (0, -1, 0)),
    ((0, 0, 1), (0, 0, -1)),
)
F00_TUPLE: tuple[int, ...] = (1, 0, 0, 0, 0)
L1_TUPLE: tuple[int, ...] = (1, 0, 1, 1, 1)
FACE_6493: tuple[Point, ...] = ((0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1))
N_FOUR = 495
N_FILL = 7
N_ORB = 3
ORBIT_SIZES: tuple[int, ...] = (2, 4, 1)
LEX_REPS: tuple[tuple[Point, ...], ...] = (
    ((0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1)),
    ((0, 0, 0), (0, 0, 1), (2, 1, 0), (2, 1, 1)),
    ((1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)),
)

ORBIT_REPS: dict[str, Config] = {
    "empty": (0, 0, 0, 0, 0, 0),
    "wt1": (1, 0, 0, 0, 0, 0),
    "opp2": (1, 1, 0, 0, 0, 0),
    "adj2": (1, 0, 1, 0, 0, 0),
    "vertex3": (1, 0, 1, 0, 1, 0),
    "mixed3": (1, 0, 1, 1, 0, 0),
    "type210": (1, 1, 1, 0, 0, 1),
    "wt5": (1, 1, 1, 1, 1, 0),
    "full": (1, 1, 1, 1, 1, 1),
}
BIT_NAMES: tuple[str, ...] = ("wt1", "opp2", "adj2", "vertex3", "mixed3")


def normalize(text: str) -> str:
    return " ".join(text.split())


def compact(text: str) -> str:
    return text.replace(" ", "")


def add(left: Point, right: Point) -> Point:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def occupancy(site: Point, locks: frozenset[Point]) -> int:
    if site not in TWO_CUBE_SET:
        return 0
    return 1 if site in locks else 0


def neighbor_config(site: Point, locks: frozenset[Point]) -> Config:
    bits: list[int] = []
    for plus, minus in AXIS_SHIFTS:
        bits.append(occupancy(add(site, plus), locks))
        bits.append(occupancy(add(site, minus), locks))
    return (bits[0], bits[1], bits[2], bits[3], bits[4], bits[5])


def axis_type(config: Config) -> tuple[int, int, int]:
    n_unbalanced = 0
    n_both = 0
    n_empty = 0
    for index in (0, 2, 4):
        plus, minus = config[index], config[index + 1]
        if plus == 1 and minus == 1:
            n_both += 1
        elif plus == 0 and minus == 0:
            n_empty += 1
        else:
            n_unbalanced += 1
    return (n_unbalanced, n_both, n_empty)


def f_L1(config: Config) -> int:
    """1 iff some axis is unbalanced: n_mu != 0.  Not Hamming parity."""
    n_unbalanced, _n_both, _n_empty = axis_type(config)
    return 1 if n_unbalanced >= 1 else 0


def f00(config: Config) -> int:
    """F_cut remaining bits (1,0,0,0,0): fire only on wt1 and wt5."""
    kind = axis_type(config)
    return 1 if kind in ((1, 0, 2), (1, 2, 0)) else 0


def f_hamming(config: Config) -> int:
    return sum(config) % 2


def remaining_tuple(predicate) -> tuple[int, ...]:
    return tuple(int(predicate(ORBIT_REPS[name]) == 1) for name in BIT_NAMES)


def step(locks: frozenset[Point], predicate) -> frozenset[Point]:
    newcomers = {
        site
        for site in SITES
        if site not in locks and predicate(neighbor_config(site, locks)) == 1
    }
    return locks | newcomers


def run_from_seed(seed: frozenset[Point], predicate, halt_bound: int = 12):
    locks = frozenset(seed)
    history = [len(locks)]
    tick = 0
    while tick < halt_bound:
        nxt = step(locks, predicate)
        if nxt == locks:
            break
        locks = nxt
        tick += 1
        history.append(len(locks))
    return tick, frozenset(locks), tuple(history)


def fills(seed: tuple[Point, ...] | frozenset[Point], predicate=f00) -> bool:
    _tick, locks, _history = run_from_seed(frozenset(seed), predicate)
    return len(locks) == 12


def fill_set(size: int = 4, predicate=f00) -> tuple[tuple[Point, ...], ...]:
    return tuple(combo for combo in combinations(SITES, size) if fills(combo, predicate))


def det3(matrix: Matrix) -> int:
    a, b, c = matrix
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def proper_cube_rotations() -> tuple[Matrix, ...]:
    """The 24 proper cubic matrices: signed permutations with det +1."""
    mats: list[Matrix] = []
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            rows = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            for i in range(3):
                rows[i][perm[i]] = signs[i]
            matrix = (tuple(rows[0]), tuple(rows[1]), tuple(rows[2]))
            if det3(matrix) == 1:
                mats.append(matrix)
    return tuple(mats)


def apply_about_center(matrix: Matrix, point: Point) -> Point | None:
    """Apply R about the box center (1, 1/2, 1/2) in doubled integer coordinates."""
    delta = (2 * point[0] - 2, 2 * point[1] - 1, 2 * point[2] - 1)
    image = tuple(sum(matrix[i][j] * delta[j] for j in range(3)) for i in range(3))
    if (image[0] + 2) % 2 != 0 or (image[1] + 1) % 2 != 0 or (image[2] + 1) % 2 != 0:
        return None
    return ((image[0] + 2) // 2, (image[1] + 1) // 2, (image[2] + 1) // 2)


def two_cube_preserving_rotations() -> tuple[Matrix, ...]:
    """Keep only proper cube rotations that permute the twelve sites."""
    kept: list[Matrix] = []
    for matrix in proper_cube_rotations():
        images = [apply_about_center(matrix, site) for site in SITES]
        if all(image in TWO_CUBE_SET for image in images) and set(images) == TWO_CUBE_SET:
            kept.append(matrix)
    return tuple(kept)


def act_on_seed(matrix: Matrix, seed: frozenset[Point]) -> frozenset[Point] | None:
    images = [apply_about_center(matrix, site) for site in seed]
    if any(image is None or image not in TWO_CUBE_SET for image in images):
        return None
    return frozenset(images)  # type: ignore[arg-type]


def orbit_partition(
    seeds: tuple[frozenset[Point], ...], group: tuple[Matrix, ...]
) -> tuple[tuple[frozenset[Point], ...], ...]:
    unused = set(range(len(seeds)))
    orbits: list[tuple[frozenset[Point], ...]] = []
    while unused:
        start = min(unused)
        unused.remove(start)
        stack = [start]
        members = {start}
        while stack:
            index = stack.pop()
            for matrix in group:
                image = act_on_seed(matrix, seeds[index])
                if image is None:
                    continue
                for other, seed in enumerate(seeds):
                    if seed == image and other in unused:
                        unused.remove(other)
                        stack.append(other)
                        members.add(other)
        orbits.append(tuple(seeds[i] for i in sorted(members)))
    return tuple(orbits)


def lex_key(seed: frozenset[Point]) -> tuple[Point, ...]:
    return tuple(sorted(seed))


def seed_as_set_text(seed: tuple[Point, ...]) -> str:
    inner = ",".join(f"({p[0]},{p[1]},{p[2]})" for p in seed)
    return "{" + inner + "}"


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
    compact_note = compact(note)
    for relative in AUDIT_INPUT_PATHS:
        (ROOT / relative).read_text(encoding="utf-8")

    print("external_scientific_inputs: current Lattice, Admissibility, and Record boundaries; no observations or fits")
    print("integrity_reads: this runner, its note, and the live axiom memo; no other scientific inputs")
    print("construction: displayed F_cut occupancy-to-lock map; G-orbits of the four-site fill set on the twelve-vertex two-cube")
    print("negative_scope: neither the map nor the fill-set orbit type is adopted or written into Admissibility")
    print("cache_write: false")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")

    checks.check(
        "audit-inputs",
        "declared source-bound inputs exist as static literals",
        AUDIT_INPUT_PATHS
        == (
            "docs/F_CUT_C00_FOUR_SITE_FILL_ORBIT_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and AUDIT_TIMEOUT_SEC == 120
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and 'AUDIT_INPUT_PATHS = (\n'
        '    "docs/F_CUT_C00_FOUR_SITE_FILL_ORBIT_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ')' in self_source,
    )

    lattice_sentence = "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
    admissibility_sentence = (
        "For each site, the probability distribution over the possibilities is "
        "determined by, and varies with, the nearest-neighbor conditions."
    )
    formation_boundary = "does not supply the formation site, probability, or rate"
    record_lock = "When present, a record locks exactly one admissible local possibility."
    not_dynamics = "Admissibility is not a dynamics axiom."

    checks.check(
        "source-lattice",
        "current cubic nearest-neighbor wording is pinned",
        lattice_sentence in normalize(axiom) and lattice_sentence in note,
    )
    checks.check(
        "source-admissibility",
        "current local-distribution wording is pinned",
        admissibility_sentence in normalize(axiom) and admissibility_sentence in note,
    )
    checks.check(
        "source-formation-boundary",
        "formation site, probability, and rate remain outside Admissibility",
        formation_boundary in normalize(axiom) and formation_boundary in normalize(note),
    )
    checks.check(
        "source-record-and-non-dynamics",
        "Record lock wording and the non-dynamics Admissibility boundary are pinned",
        record_lock in normalize(axiom)
        and record_lock in note
        and not_dynamics in axiom
        and not_dynamics in note,
    )

    checks.check(
        "two-cube-and-lex-order",
        "the two-cube has twelve lexicographically ordered vertices",
        len(SITES) == 12
        and SITES == tuple(sorted(SITES))
        and SITES[0] == (0, 0, 0)
        and SITES[-1] == (2, 1, 1)
        and TWO_CUBE_SET == frozenset(SITES),
    )
    checks.check(
        "census-cardinality",
        "four-site seed count is C(12,4)=495",
        len(list(combinations(SITES, 4))) == N_FOUR,
    )
    checks.check(
        "off-patch-zero",
        "every off-patch neighbor contributes occupancy 0",
        occupancy((-1, 0, 0), frozenset({(0, 0, 0)})) == 0
        and occupancy((0, -1, 0), frozenset({(0, 0, 0)})) == 0
        and occupancy((3, 0, 0), frozenset({(2, 0, 0)})) == 0,
    )
    checks.check(
        "axis-type-reps",
        "declared orbit representatives have the stated axis types",
        axis_type(ORBIT_REPS["wt1"]) == (1, 0, 2)
        and axis_type(ORBIT_REPS["opp2"]) == (0, 1, 2)
        and axis_type(ORBIT_REPS["adj2"]) == (2, 0, 1)
        and axis_type(ORBIT_REPS["vertex3"]) == (3, 0, 0)
        and axis_type(ORBIT_REPS["mixed3"]) == (1, 1, 1)
        and axis_type(ORBIT_REPS["type210"]) == (2, 1, 0)
        and axis_type(ORBIT_REPS["empty"]) == (0, 0, 3)
        and axis_type(ORBIT_REPS["wt5"]) == (1, 2, 0)
        and axis_type(ORBIT_REPS["full"]) == (0, 3, 0),
    )

    f00_bits = remaining_tuple(f00)
    l1_bits = remaining_tuple(f_L1)
    checks.check(
        "f00-remaining-bits",
        "f00 is the F_cut remaining-bit tuple (1,0,0,0,0)",
        f00_bits == F00_TUPLE
        and l1_bits == L1_TUPLE
        and f00(ORBIT_REPS["wt1"]) == 1
        and f00(ORBIT_REPS["wt5"]) == 1
        and f00(ORBIT_REPS["opp2"]) == 0
        and f00(ORBIT_REPS["adj2"]) == 0
        and f00(ORBIT_REPS["vertex3"]) == 0
        and f00(ORBIT_REPS["mixed3"]) == 0
        and f00(ORBIT_REPS["type210"]) == 0
        and f00(ORBIT_REPS["empty"]) == 0
        and f00(ORBIT_REPS["full"]) == 0,
    )
    checks.check(
        "f-l1-is-n-unbalanced",
        "f_L1 is the n!=0 (some-axis-unbalanced) map, not Hamming parity",
        f_L1(ORBIT_REPS["wt1"]) == 1
        and f_L1(ORBIT_REPS["mixed3"]) == 1
        and f_L1(ORBIT_REPS["type210"]) == 1
        and f_L1(ORBIT_REPS["opp2"]) == 0
        and f_L1(ORBIT_REPS["empty"]) == 0
        and f_L1(ORBIT_REPS["adj2"]) != f_hamming(ORBIT_REPS["adj2"])
        and sum(ORBIT_REPS["opp2"]) % 2 == 0
        and "sum(config) % 2"
        not in self_source.split("def f_L1", 1)[1].split("def f00", 1)[0],
    )

    members = fill_set()
    fill_frozens = tuple(frozenset(seed) for seed in members)
    ambient = proper_cube_rotations()
    group = two_cube_preserving_rotations()
    orbits = orbit_partition(fill_frozens, group)
    n_orb = len(orbits)
    lex_reps = tuple(min(lex_key(seed) for seed in orbit) for orbit in orbits)
    orbit_sizes = tuple(len(orbit) for orbit in orbits)
    face_tick, face_locks, face_history = run_from_seed(frozenset(FACE_6493), f00)
    print(f"|M|={len(members)} n_four={N_FOUR}")
    print(f"face_in_M={FACE_6493 in members} history={face_history} T={face_tick}")
    print(
        "orbit: "
        f"N_ambient={len(ambient)} |G|={len(group)} N_orb={n_orb} "
        f"sizes={orbit_sizes} lex={lex_reps}"
    )

    checks.check(
        "theorem-1-fill-set",
        "|M|=7 among the 495 four-site seeds and the #6493 face is in M",
        len(members) == N_FILL
        and FACE_6493 in members
        and fills(FACE_6493)
        and face_history == (4, 8, 12)
        and face_locks == TWO_CUBE_SET
        and "#6493" in note
        and "|M|=7" in compact_note
        and seed_as_set_text(FACE_6493) in compact_note,
        residual=(len(members), FACE_6493 in members, face_history),
    )
    checks.check(
        "group-preserves-twelve",
        "only site-permutations of the two-cube induced by proper cube rotations are used",
        len(ambient) == 24
        and len(group) == 8
        and all(det3(matrix) == 1 for matrix in group)
        and all(
            {apply_about_center(matrix, site) for site in SITES} == TWO_CUBE_SET
            for matrix in group
        ),
        residual=len(group),
    )
    checks.check(
        "theorem-2-n-orb",
        "N_orb=3 with one lex representative per orbit",
        n_orb == N_ORB
        and orbit_sizes == ORBIT_SIZES
        and lex_reps == LEX_REPS
        and "N_orb = 3" in note
        and all(seed_as_set_text(rep) in compact_note for rep in LEX_REPS)
        and "one lex representative per orbit" in note.lower(),
        residual=(n_orb, orbit_sizes, lex_reps),
    )

    non_reps = [seed for seed in members if seed not in LEX_REPS]
    listed_non_reps = [seed for seed in non_reps if seed_as_set_text(seed) in compact_note]
    checks.check(
        "theorem-3-display-not-list",
        "the note displays N_orb and does not list all seven",
        "N_orb = 3" in note
        and "Do not list all seven" in note
        and len(non_reps) == 4
        and listed_non_reps == []
        and "Displayed, not adopted" in note
        and "not written into Admissibility" in normalize(note)
        and "Do not adopt" in note
        and "Do not write" in note,
        residual=listed_non_reps,
    )

    claim_scope = (
        "On the two-cube with off-patch o=0, the "
        "seven 4-site seeds that F_cut (1,0,0,0,0) fills form "
        "N_orb orbits under two-cube-preserving rotations. "
        "Displayed, not adopted."
    )
    forbidden = (
        "G_" + "N",
        "1/" + "r",
        "1/" + "r^2",
        "Lattice-" + "named",
        "not a " + "TOE",
    )
    required = (
        "actual_current_surface_status: bounded-support",
        "target_claim_type: bounded_theorem",
        'hypothetical_axiom_status: "no edit"',
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
        "authors no audit verdict",
        "FAIL / DO NOT SHIP",
        "N_orb = 3",
        "(1, 0, 0, 0, 0)",
        "#6493",
    )
    allowed_retained = (
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
    )
    other_retained = note
    for line in allowed_retained:
        other_retained = other_retained.replace(line, "")

    checks.check(
        "claim-scope",
        "claim_scope reports the fill-set orbit type and does not adopt it",
        claim_scope in note
        and "Displayed, not adopted" in note
        and "do not adopt" in note.lower(),
    )
    checks.check(
        "note-contract",
        "machine fields, orbit statement, and forbidden-phrase hygiene hold",
        all(phrase in note for phrase in required)
        and all(f"### N{index}" in note for index in range(1, 9))
        and all(phrase not in note and phrase not in self_source for phrase in forbidden)
        and "promoted" not in note.lower()
        and "new axiom" not in note
        and "Block 12" not in note
        and "toe-lphys" not in note
        and "citation" not in note.lower()
        and "runner-cache" not in note
        and "retained" not in other_retained,
    )
    checks.check(
        "not-leftover-6493",
        "the residual is the fill-set orbit type, not leftover #6493 scoring or a miss-set N_orb",
        "Not leftover-character of #6493" in note
        or "not leftover-character of `#6493`" in note.lower()
        or "It is not leftover-character of `#6493`" in note
        or "not leftover-character of `#6493`" in normalize(note).lower(),
    )
    leftover_ok = (
        "not leftover-character of `#6493`" in normalize(note).lower()
        or "It is not leftover-character of `#6493`" in note
        or "not leftover-character of #6493" in note
    )
    miss_ok = "not `N_orb` of a miss set" in note or "not N_orb of a miss set" in note
    new_ok = "new finite object" in note.lower() or "new geometry" in note.lower()
    checks.check(
        "not-miss-set-orbit",
        "the residual is new fill-set geometry, not N_orb of a miss set",
        leftover_ok and miss_ok and new_ok,
        residual=(leftover_ok, miss_ok, new_ok),
    )
    checks.check(
        "l1-definition-in-note",
        "the note defines f_L1 as unbalanced-axis / n != 0 and rejects Hamming",
        "`f_L1(c)=1` if and only if some axis is unbalanced" in normalize(note)
        and "not Hamming" in note
        and "`n_μ = c_{+μ} − c_{-μ}` is nonzero" in note
        and "This is **not** Hamming parity" in note,
    )
    checks.check(
        "off-patch-declared",
        "off-patch occupancy is the explicit 0 default, not a blank-block",
        "off-patch occupancy `0`" in note and "blank-block is a different rule" in note,
    )
    checks.check(
        "axiom-unedited",
        "the axiom memo still carries the four named premises and no F_cut map",
        "### Lattice / Physical Locality" in axiom
        and "### Qubit / Site Possibility" in axiom
        and "### Admissibility / Local Constraint" in axiom
        and "### Record / Fixed Reality" in axiom
        and "F_cut" not in axiom
        and "f_L1" not in axiom
        and "f00" not in axiom,
    )

    print("per_element: axis-type representatives and off-patch occupancy 0 are enumerated")
    print("per_site: each two-cube vertex is tested against the displayed lock predicate")
    print("per_mode: checked and not executed — no spectral claim occurs")
    print("per_block: all 495 four-site seeds and the G-action on M are executed")
    print("lattice_wide: checked and not executed — neither the map nor the orbit is adopted")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
