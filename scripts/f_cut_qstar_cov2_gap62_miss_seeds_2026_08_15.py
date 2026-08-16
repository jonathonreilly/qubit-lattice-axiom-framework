#!/usr/bin/env python3
"""Four two-site seeds the Q_* cov2=62 map f_g misses, and N_orb.

F_cut is the cube-covariant class with f(empty)=f(full)=0 and f(c)=f(1-c).
Q_* is the eight-member subclass with remaining bits wt1=1 and adj2=1.
Dynamics are occupancy-to-lock on the twelve-vertex two-cube with off-patch
occupancy 0. f_L1 is the unbalanced-axis predicate (some n_mu != 0), never
Hamming |c|_1 mod 2. f_g is the remaining-bit tuple (1, 0, 1, 1, 0). The
new object is the four 2-site seeds f_g misses, in lex order, and N_orb of
that four-set under two-cube-preserving rotations. One map only. Not a
two-map share-test. Displayed, not adopted. Does not adopt a seed.
"""

from __future__ import annotations

from itertools import combinations, permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/F_CUT_QSTAR_COV2_GAP62_MISS_SEEDS_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/F_CUT_QSTAR_COV2_GAP62_MISS_SEEDS_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Direction = tuple[int, int, int]
Config = tuple[int, int, int, int, int, int]
Rotation = tuple[tuple[int, int, int], tuple[int, int, int]]
Matrix = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]
OrbitType = tuple[int, int, int]
Site = tuple[int, int, int]
Remaining = tuple[int, int, int, int, int]

DIRECTIONS: tuple[Direction, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
EMPTY: Config = (0, 0, 0, 0, 0, 0)
FULL: Config = (1, 1, 1, 1, 1, 1)
TWO_CUBE: tuple[Site, ...] = tuple(
    (x, y, z) for x in range(3) for y in range(2) for z in range(2)
)
TWO_CUBE_SET = frozenset(TWO_CUBE)
REMAINING_ORDER: tuple[OrbitType, ...] = (
    (1, 0, 2),
    (0, 1, 2),
    (2, 0, 1),
    (3, 0, 0),
    (1, 1, 1),
)
REMAINING_LABELS: tuple[str, ...] = ("wt1", "opp2", "adj2", "vertex3", "mixed3")
L1_REMAINING: Remaining = (1, 0, 1, 1, 1)
G_REMAINING: Remaining = (1, 0, 1, 1, 0)
EXPECTED_MISS_SEEDS: tuple[frozenset[Site], ...] = (
    frozenset([(0, 0, 0), (2, 0, 0)]),
    frozenset([(0, 0, 1), (2, 0, 1)]),
    frozenset([(0, 1, 0), (2, 1, 0)]),
    frozenset([(0, 1, 1), (2, 1, 1)]),
)
EXPECTED_HISTORIES: tuple[tuple[int, ...], ...] = (
    (2, 6, 8),
    (2, 6, 8),
    (2, 6, 8),
    (2, 6, 8),
)
N_ORB = 1
ORBIT_SIZE = 4


def permutation_sign(permutation: tuple[int, int, int]) -> int:
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(3)
        for j in range(i + 1, 3)
    )
    return -1 if inversions % 2 else 1


ROTATIONS: tuple[Rotation, ...] = tuple(
    (permutation, signs)
    for permutation in permutations((0, 1, 2))
    for signs in product((-1, 1), repeat=3)
    if permutation_sign(permutation) * signs[0] * signs[1] * signs[2] == 1
)


def rotate_vector(rotation: Rotation, vector: Direction) -> Direction:
    permutation, signs = rotation
    result = [0, 0, 0]
    for source_axis in range(3):
        result[permutation[source_axis]] = signs[source_axis] * vector[source_axis]
    return (result[0], result[1], result[2])


def rotate_config(config: Config, rotation: Rotation) -> Config:
    occupancy = {direction: config[index] for index, direction in enumerate(DIRECTIONS)}
    forward = {direction: rotate_vector(rotation, direction) for direction in DIRECTIONS}
    inverse = {image: source for source, image in forward.items()}
    return tuple(occupancy[inverse[direction]] for direction in DIRECTIONS)  # type: ignore[return-value]


def axis_type(config: Config) -> OrbitType:
    n_unbalanced = 0
    n_both = 0
    n_empty = 0
    for axis in range(3):
        plus = config[2 * axis]
        minus = config[2 * axis + 1]
        if plus != minus:
            n_unbalanced += 1
        elif plus == 1:
            n_both += 1
        else:
            n_empty += 1
    return (n_unbalanced, n_both, n_empty)


def complement_type(orbit_type: OrbitType) -> OrbitType:
    unbalanced, both, empty = orbit_type
    return (unbalanced, empty, both)


def f_L1(config: Config) -> int:
    """1 iff some axis is unbalanced: n_mu != 0.  Not Hamming parity."""
    return int(any(config[2 * axis] != config[2 * axis + 1] for axis in range(3)))


def f_hamming(config: Config) -> int:
    return sum(config) % 2


def remaining_value(config: Config, remaining: tuple[int, ...]) -> int:
    kind = axis_type(config)
    if kind in (axis_type(EMPTY), axis_type(FULL)):
        return 0
    assignment = dict(zip(REMAINING_ORDER, remaining, strict=True))
    if kind in assignment:
        return assignment[kind]
    return assignment[complement_type(kind)]


def f_g(config: Config) -> int:
    return remaining_value(config, G_REMAINING)


def in_qstar(remaining: tuple[int, ...]) -> bool:
    """Q_* is the F_cut subclass with wt1=1 and adj2=1."""
    return remaining[0] == 1 and remaining[2] == 1


def build_orbits() -> dict[OrbitType, frozenset[Config]]:
    orbits: dict[OrbitType, frozenset[Config]] = {}
    seen: set[Config] = set()
    for raw in product((0, 1), repeat=6):
        config: Config = (raw[0], raw[1], raw[2], raw[3], raw[4], raw[5])
        if config in seen:
            continue
        orbit: set[Config] = set()
        stack = [config]
        while stack:
            current = stack.pop()
            if current in orbit:
                continue
            orbit.add(current)
            for rotation in ROTATIONS:
                stack.append(rotate_config(current, rotation))
        orbit_type = axis_type(config)
        if any(axis_type(member) != orbit_type for member in orbit):
            raise RuntimeError("orbit mixed axis types")
        orbits[orbit_type] = frozenset(orbit)
        seen.update(orbit)
    return orbits


def neighborhood(site: Site, locked: set[Site]) -> Config:
    values = []
    for direction in DIRECTIONS:
        neighbor = (
            site[0] + direction[0],
            site[1] + direction[1],
            site[2] + direction[2],
        )
        values.append(1 if neighbor in locked else 0)
    return (values[0], values[1], values[2], values[3], values[4], values[5])


def evolve(locked: set[Site], predicate) -> set[Site]:
    nxt = set(locked)
    for site in TWO_CUBE:
        if site in locked:
            continue
        if predicate(neighborhood(site, locked)):
            nxt.add(site)
    return nxt


def fills_from_seed(predicate, seed: frozenset[Site]) -> bool:
    locked = set(seed)
    for _tick in range(13):
        nxt = evolve(locked, predicate)
        if nxt == locked:
            return len(locked) == 12
        locked = nxt
    return False


def lock_count_history(predicate, seed: frozenset[Site]) -> tuple[int, ...]:
    locked = set(seed)
    history = [len(locked)]
    for _tick in range(13):
        nxt = evolve(locked, predicate)
        if nxt == locked:
            return tuple(history)
        locked = nxt
        history.append(len(locked))
    return tuple(history)


def two_site_seeds() -> tuple[frozenset[Site], ...]:
    return tuple(frozenset(pair) for pair in combinations(TWO_CUBE, 2))


def miss_seeds(predicate) -> tuple[frozenset[Site], ...]:
    misses: list[frozenset[Site]] = []
    for seed in two_site_seeds():
        if not fills_from_seed(predicate, seed):
            misses.append(seed)
    return tuple(misses)


def bits_from_predicate(
    predicate, orbit_types: tuple[OrbitType, ...], orbits: dict[OrbitType, frozenset[Config]]
) -> tuple[int, ...]:
    bits = []
    for orbit_type in orbit_types:
        sample = next(iter(orbits[orbit_type]))
        value = int(predicate(sample))
        if any(int(predicate(member)) != value for member in orbits[orbit_type]):
            raise RuntimeError("predicate is not cube-covariant")
        bits.append(value)
    return tuple(bits)


def remaining_bits_from_assignment(
    assignment: dict[OrbitType, int], orbit_types: tuple[OrbitType, ...]
) -> tuple[int, ...]:
    return tuple(assignment[orbit_type] for orbit_type in REMAINING_ORDER)


def in_f_cut(
    bits: tuple[int, ...],
    orbit_types: tuple[OrbitType, ...],
    empty_type: OrbitType,
    full_type: OrbitType,
) -> bool:
    assignment = dict(zip(orbit_types, bits, strict=True))
    if assignment[empty_type] != 0 or assignment[full_type] != 0:
        return False
    for orbit_type in orbit_types:
        partner = complement_type(orbit_type)
        if assignment[orbit_type] != assignment[partner]:
            return False
    return True


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


def apply_about_center(matrix: Matrix, point: Site) -> Site | None:
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
        images = [apply_about_center(matrix, site) for site in TWO_CUBE]
        if all(image in TWO_CUBE_SET for image in images) and set(images) == TWO_CUBE_SET:
            kept.append(matrix)
    return tuple(kept)


def act_on_seed(matrix: Matrix, seed: frozenset[Site]) -> frozenset[Site] | None:
    images = [apply_about_center(matrix, site) for site in seed]
    if any(image is None or image not in TWO_CUBE_SET for image in images):
        return None
    return frozenset(images)  # type: ignore[arg-type]


def orbit_partition(
    seeds: tuple[frozenset[Site], ...], group: tuple[Matrix, ...]
) -> tuple[tuple[frozenset[Site], ...], ...]:
    unused = set(range(len(seeds)))
    orbits: list[tuple[frozenset[Site], ...]] = []
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


def lex_key(seed: frozenset[Site]) -> tuple[Site, ...]:
    return tuple(sorted(seed))


def seed_as_set_text(seed: frozenset[Site] | tuple[Site, ...]) -> str:
    ordered = tuple(sorted(seed))
    inner = ", ".join(f"({p[0]},{p[1]},{p[2]})" for p in ordered)
    return "{" + inner + "}"


def compact(text: str) -> str:
    return text.replace(" ", "")


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
    note_flat = " ".join(note.split())
    axiom_flat = " ".join(axiom.split())
    compact_note = compact(note)
    for relative in AUDIT_INPUT_PATHS:
        (ROOT / relative).read_text(encoding="utf-8")

    print("external_scientific_inputs: current Lattice, Admissibility, and Record boundaries; no observations or fits")
    print("integrity_reads: this runner, its note, and the live axiom memo; no other scientific inputs")
    print("construction: displayed F_cut occupancy-to-lock map; miss set of f_g and its G-orbits on the twelve-vertex two-cube")
    print("negative_scope: neither the map nor a miss seed is adopted or written into Admissibility")
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
            "docs/F_CUT_QSTAR_COV2_GAP62_MISS_SEEDS_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and AUDIT_TIMEOUT_SEC == 120
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and 'AUDIT_INPUT_PATHS = (\n    "docs/F_CUT_QSTAR_COV2_GAP62_MISS_SEEDS_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n)'
        in self_source,
    )

    orbits = build_orbits()
    orbit_types = tuple(sorted(orbits, key=lambda kind: (kind[0], kind[1], kind[2])))
    empty_type = axis_type(EMPTY)
    full_type = axis_type(FULL)
    g_bits = bits_from_predicate(f_g, orbit_types, orbits)
    l1_bits = bits_from_predicate(f_L1, orbit_types, orbits)
    ham_bits = bits_from_predicate(f_hamming, orbit_types, orbits)
    g_remaining = remaining_bits_from_assignment(
        dict(zip(orbit_types, g_bits, strict=True)), orbit_types
    )
    l1_remaining = remaining_bits_from_assignment(
        dict(zip(orbit_types, l1_bits, strict=True)), orbit_types
    )

    checks.check(
        "thm1-f-L1-n-unbalanced",
        "f_L1 fires iff some axis is unbalanced: n_mu != 0, c_+ != c_-",
        all(
            f_L1(config) == int(axis_type(config)[0] >= 1)
            for config in product((0, 1), repeat=6)
        )
        and l1_remaining == L1_REMAINING
        and in_f_cut(l1_bits, orbit_types, empty_type, full_type),
    )
    checks.check(
        "thm1-f-L1-not-hamming",
        "f_L1 is n!=0, not Hamming |c|_1 mod 2",
        l1_bits != ham_bits
        and any(f_L1(config) != f_hamming(config) for config in product((0, 1), repeat=6))
        and "sum(config) % 2"
        not in self_source.split("def f_L1", 1)[1].split("def f_hamming", 1)[0]
        and "n ≠ 0" in note
        and "This is **not** Hamming parity" in note,
    )
    checks.check(
        "thm1-f-g-in-qstar",
        "f_g is (1,0,1,1,0) in Q_* with vertex3=1 and opp2=0",
        g_remaining == G_REMAINING
        and g_remaining == (1, 0, 1, 1, 0)
        and g_remaining[3] == 1
        and g_remaining[1] == 0
        and in_qstar(g_remaining)
        and in_f_cut(g_bits, orbit_types, empty_type, full_type)
        and "`f_g`" in note
        and "(1, 0, 1, 1, 0)" in note,
    )

    seeds = two_site_seeds()
    miss = miss_seeds(f_g)
    cov_g = len(seeds) - len(miss)
    histories = tuple(lock_count_history(f_g, seed) for seed in miss)
    print(f"cov2(f_g)={cov_g} n_miss={len(miss)} histories={histories}")

    checks.check(
        "two-cube-and-lex-order",
        "the two-cube has twelve lexicographically ordered vertices and 66 two-site seeds",
        len(TWO_CUBE) == 12
        and TWO_CUBE == tuple(sorted(TWO_CUBE))
        and TWO_CUBE[0] == (0, 0, 0)
        and TWO_CUBE[-1] == (2, 1, 1)
        and len(seeds) == 66
        and seeds == tuple(sorted(seeds, key=lex_key)),
    )
    checks.check(
        "off-patch-zero",
        "off-patch occupancy is the explicit 0 default, not a blank-block",
        neighborhood((0, 0, 0), {(0, 0, 0)})[1] == 0
        and neighborhood((2, 0, 0), {(2, 0, 0)})[0] == 0
        and "off-patch occupancy `0`" in note
        and "off-patch o=0" in note
        and "blank-block is a different rule" in note,
    )
    checks.check(
        "thm1-four-miss-seeds-lex",
        "the four 2-site seeds f_g misses, in lex order, are the long-axis pairs",
        cov_g == 62
        and len(miss) == 4
        and miss == EXPECTED_MISS_SEEDS
        and all(not fills_from_seed(f_g, seed) for seed in miss)
        and all(fills_from_seed(f_g, seed) for seed in seeds if seed not in set(miss))
        and all(compact(seed_as_set_text(seed)) in compact_note for seed in EXPECTED_MISS_SEEDS)
        and "cov2(f_g)=62" in compact(note).replace("`", ""),
        residual=(cov_g, [lex_key(seed) for seed in miss]),
    )
    checks.check(
        "thm1-halt-histories",
        "each miss has halt lock-count 8 and history (2, 6, 8)",
        histories == EXPECTED_HISTORIES
        and all(history[-1] == 8 for history in histories)
        and "(2, 6, 8)" in note,
        residual=histories,
    )

    ambient = proper_cube_rotations()
    group = two_cube_preserving_rotations()
    orbits_m = orbit_partition(miss, group)
    n_orb = len(orbits_m)
    orbit_sizes = tuple(len(orbit) for orbit in orbits_m)
    lex_rep = min(lex_key(seed) for seed in miss)
    print(
        "orbit: "
        f"N_ambient={len(ambient)} |G|={len(group)} N_orb={n_orb} "
        f"sizes={orbit_sizes} lex={lex_rep}"
    )

    checks.check(
        "group-preserves-twelve",
        "only site-permutations of the two-cube induced by proper cube rotations are used",
        len(ambient) == 24
        and len(group) == 8
        and all(det3(matrix) == 1 for matrix in group)
        and all(
            {apply_about_center(matrix, site) for site in TWO_CUBE} == TWO_CUBE_SET
            for matrix in group
        ),
        residual=len(group),
    )
    checks.check(
        "thm2-n-orb",
        "N_orb of the four-set under two-cube-preserving rotations is 1",
        n_orb == N_ORB
        and orbit_sizes == (ORBIT_SIZE,)
        and lex_rep == ((0, 0, 0), (2, 0, 0))
        and "N_orb = 1" in note
        and "single orbit" in note,
        residual=(n_orb, orbit_sizes, lex_rep),
    )
    checks.check(
        "thm3-displayed-not-adopted",
        "the four seeds are displayed and no seed is adopted",
        "Do not adopt a seed" in note
        and "Displayed, not adopted" in note
        and "does not adopt a seed" in self_source
        and "Do not write the four-set into" in note,
    )

    lattice_sites = (
        "Physical sites are the points of the cubic lattice `Z^3`, with "
        "nearest-neighbor adjacency, standard translations, and proper cubic "
        "rotations about each site."
    )
    admissibility = (
        "There is one fixed nearest-neighbor admissibility rule, covariant "
        "under lattice translations and proper cubic rotations."
    )
    formation_residual = "it does not supply the formation site, probability, or rate."
    record_lock = "When present, a record locks exactly one admissible local possibility."
    record_content = "A readout value is determined by record content alone."
    record_absence = "A site with no record cannot be read."
    records_form = "Records form."

    checks.check(
        "source-lattice-admissibility",
        "Lattice rotations and Admissibility covariance are pinned",
        lattice_sites in axiom_flat
        and admissibility in axiom_flat
        and lattice_sites in note_flat
        and admissibility in note_flat,
    )
    checks.check(
        "source-record-boundary",
        "Record lock, content-only readout, unreadable absence, and formation residual are pinned",
        all(
            phrase in axiom_flat
            for phrase in (
                records_form,
                record_lock,
                record_content,
                record_absence,
                formation_residual,
            )
        )
        and all(
            phrase in note_flat
            for phrase in (
                records_form,
                record_lock,
                record_content,
                record_absence,
                formation_residual,
            )
        ),
    )

    claim_scope = (
        "On the two-cube with off-patch o=0, the four two-site seeds that "
        "F_cut (1,0,1,1,0) misses, and the orbit count of that set, are "
        "reported. Displayed, not adopted."
    )
    checks.check(
        "claim-scope",
        "claim_scope reports the four miss seeds and N_orb and does not adopt a seed",
        claim_scope in note and "Displayed, not adopted" in note,
    )

    allowed_retained = (
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
    )
    other_retained = note
    for line in allowed_retained:
        other_retained = other_retained.replace(line, "")
    required = (
        "actual_current_surface_status: bounded-support",
        "target_claim_type: bounded_theorem",
        "trace_class: frontier_discovery",
        "reachability_to_target: advances",
        'hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"',
        "authors no audit verdict",
        "FAIL / DO NOT SHIP",
        "Theorem 1",
        "Theorem 2",
        "Theorem 3",
        "|F_cut| = 32",
        "No-Go Discipline disposition: **PASS**",
        "N_orb = 1",
    )
    forbidden = ("G_" + "N", "1/" + "r", "1/" + "r^2", "Lattice-" + "named", "not a " + "TOE")
    checks.check(
        "note-contract",
        "machine fields, three theorems, and forbidden-phrase hygiene hold",
        all(phrase in note for phrase in required)
        and all(line in note for line in allowed_retained)
        and all(f"### N{index}" in note for index in range(1, 9))
        and note.count("**ATTEMPTED**") == 6
        and not any(phrase in note or phrase in self_source for phrase in forbidden)
        and "retained" not in other_retained
        and "promoted" not in note.lower()
        and "toe-lphys" not in note
        and "runner-cache" not in note
        and "citation" not in note.lower(),
    )
    checks.check(
        "no-axiom-edit",
        "the axiom memo is unedited and the theorem proposes no axiom change",
        "### Lattice / Physical Locality" in axiom
        and "### Qubit / Site Possibility" in axiom
        and "### Admissibility / Local Constraint" in axiom
        and "### Record / Fixed Reality" in axiom
        and "F_cut" not in axiom
        and "f_L1" not in axiom
        and "no axiom or approved primitive is added" in note
        and "Do not write `Q_*` or `f_g` into Admissibility" in note,
    )
    checks.check(
        "l1-definition-in-note",
        "the note defines f_L1 as unbalanced-axis / n != 0 and rejects Hamming",
        "`f_L1(c)=1` if and only if some axis is unbalanced" in note_flat
        and "`n_μ = c_{+μ} − c_{-μ}` is nonzero" in note
        and "This is **not** Hamming parity" in note,
    )
    checks.check(
        "not-share-test",
        "the residual is the one-map miss list and N_orb, not a two-map share-test",
        "Not leftover-character of a two-map share-test" in note
        and "One map. Not a two-map share-test" in note
        and "`f_g` only" in note
        and "Not leftover-character of tot2why" in note
        and "Not leftover-character of tot2q" in note
        and "Not leftover-character of the `f_L1` two-site miss list" in note,
    )

    print("per_element: checked exactly — each of the 64 neighbor 6-tuples is assigned its axis-type orbit")
    print("per_site: checked exactly — each of the twelve two-cube vertices uses the same six-direction stencil")
    print("per_mode: checked exactly — f_g is scored on all sixty-six two-site seeds")
    print("per_block: checked exactly — the four-set and N_orb are exact on this patch")
    print("lattice_wide: checked and not executed — no Z^3-wide formation law or physical Admissibility selector is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
