#!/usr/bin/env python3
"""Whether maximal cov9 among Q_* equals vertex3 and mixed3.

Q_* is the F_cut subclass with wt1=1 and adj2=1 (eight remaining-bit
tuples). F_cut is the cube-covariant class with f(empty)=f(full)=0 and
f(c)=f(1-c). Dynamics are occupancy-to-lock on the twelve-vertex
two-cube with off-patch occupancy 0. Coverage cov9(f) is the number of
unordered 9-site seeds from which f fills. Q is the displayed cut
vertex3=1 and mixed3=1. The runner reports whether maximal cov9 among
the eight equals Q, the census integers N_max, N_Q, N_both, and the
lex-first miss if the identity fails. Displayed, not adopted. f_L1 is
the unbalanced-axis predicate (some n_mu != 0), never Hamming
|c|_1 mod 2. Duality is not assumed. The runner does not adopt a bit.
"""

from __future__ import annotations

from itertools import combinations, permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/F_CUT_QSTAR_COV9_MAX_SELECTOR_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/F_CUT_QSTAR_COV9_MAX_SELECTOR_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Direction = tuple[int, int, int]
Config = tuple[int, int, int, int, int, int]
Rotation = tuple[tuple[int, int, int], tuple[int, int, int]]
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
NINE_SITE_SEEDS: tuple[frozenset[Site], ...] = tuple(
    frozenset(combo) for combo in combinations(TWO_CUBE, 9)
)
REMAINING_ORDER: tuple[OrbitType, ...] = (
    (1, 0, 2),
    (0, 1, 2),
    (2, 0, 1),
    (3, 0, 0),
    (1, 1, 1),
)
REMAINING_LABELS: tuple[str, ...] = ("wt1", "opp2", "adj2", "vertex3", "mixed3")
L1_REMAINING: Remaining = (1, 0, 1, 1, 1)
F1_REMAINING: Remaining = (1, 1, 1, 1, 1)
M9 = 220
N_MAX = 2
N_Q = 2
N_BOTH = 2
CENSUS: dict[Remaining, int] = {
    (1, 0, 1, 0, 0): 68,
    (1, 0, 1, 0, 1): 72,
    (1, 0, 1, 1, 0): 200,
    (1, 0, 1, 1, 1): 220,
    (1, 1, 1, 0, 0): 72,
    (1, 1, 1, 0, 1): 72,
    (1, 1, 1, 1, 0): 204,
    (1, 1, 1, 1, 1): 220,
}


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


def remaining_value(config: Config, remaining: Remaining) -> int:
    kind = axis_type(config)
    if kind in (axis_type(EMPTY), axis_type(FULL)):
        return 0
    assignment = dict(zip(REMAINING_ORDER, remaining, strict=True))
    if kind in assignment:
        return assignment[kind]
    return assignment[complement_type(kind)]


def in_qstar(remaining: Remaining) -> bool:
    wt1, _opp2, adj2, _vertex3, _mixed3 = remaining
    return wt1 == 1 and adj2 == 1


def selector_q(remaining: Remaining) -> bool:
    """Displayed Q: vertex3=1 and mixed3=1."""
    _wt1, _opp2, _adj2, vertex3, mixed3 = remaining
    return vertex3 == 1 and mixed3 == 1


def enumerate_qstar() -> list[Remaining]:
    members: list[Remaining] = []
    for bits in product((0, 1), repeat=5):
        remaining: Remaining = (bits[0], bits[1], bits[2], bits[3], bits[4])
        if in_qstar(remaining):
            members.append(remaining)
    return members


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


SITE_INDEX: dict[Site, int] = {site: index for index, site in enumerate(TWO_CUBE)}
NEIGHBOR_INDEX: tuple[tuple[int | None, ...], ...] = tuple(
    tuple(
        SITE_INDEX.get(
            (site[0] + direction[0], site[1] + direction[1], site[2] + direction[2])
        )
        for direction in DIRECTIONS
    )
    for site in TWO_CUBE
)


def fills_from_mask(fire: tuple[int, ...], seed_mask: int) -> bool:
    locked = seed_mask
    for _tick in range(13):
        nxt = locked
        for site_index in range(12):
            if (locked >> site_index) & 1:
                continue
            bits = 0
            for axis, neighbor in enumerate(NEIGHBOR_INDEX[site_index]):
                occupied = neighbor is not None and ((locked >> neighbor) & 1)
                if occupied:
                    bits |= 1 << axis
            if fire[bits]:
                nxt |= 1 << site_index
        if nxt == locked:
            return locked == (1 << 12) - 1
        locked = nxt
    return False


def seed_mask(seed: frozenset[Site]) -> int:
    mask = 0
    for site in seed:
        mask |= 1 << SITE_INDEX[site]
    return mask


SEED_MASKS: tuple[int, ...] = tuple(seed_mask(seed) for seed in NINE_SITE_SEEDS)


def fire_table(remaining: Remaining) -> tuple[int, ...]:
    table = [0] * 64
    for raw in product((0, 1), repeat=6):
        config: Config = (raw[0], raw[1], raw[2], raw[3], raw[4], raw[5])
        index = (
            raw[0]
            | (raw[1] << 1)
            | (raw[2] << 2)
            | (raw[3] << 3)
            | (raw[4] << 4)
            | (raw[5] << 5)
        )
        table[index] = remaining_value(config, remaining)
    return tuple(table)


def coverage9(remaining: Remaining) -> int:
    fire = fire_table(remaining)
    return sum(1 for mask in SEED_MASKS if fills_from_mask(fire, mask))


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


def remaining_bits_from_assignment(assignment: dict[OrbitType, int]) -> Remaining:
    return tuple(assignment[orbit_type] for orbit_type in REMAINING_ORDER)  # type: ignore[return-value]


def remaining_bits_from_full(
    bits: tuple[int, ...], orbit_types: tuple[OrbitType, ...]
) -> Remaining:
    assignment = dict(zip(orbit_types, bits, strict=True))
    return remaining_bits_from_assignment(assignment)


def in_f_cut(
    bits: tuple[int, ...],
    orbit_types: tuple[OrbitType, ...],
    empty_type: OrbitType,
    full_type: OrbitType,
) -> bool:
    assignment = dict(zip(orbit_types, bits, strict=True))
    if assignment[empty_type] != 0 or assignment[full_type] != 0:
        return False
    return all(
        assignment[orbit_type] == assignment[complement_type(orbit_type)]
        for orbit_type in orbit_types
    )


def f_cut_free_data(
    orbit_types: tuple[OrbitType, ...],
    empty_type: OrbitType,
    full_type: OrbitType,
) -> tuple[list[tuple[OrbitType, OrbitType]], list[OrbitType]]:
    used: set[OrbitType] = set()
    pairs: list[tuple[OrbitType, OrbitType]] = []
    fixed: list[OrbitType] = []
    for orbit_type in orbit_types:
        if orbit_type in used:
            continue
        image = complement_type(orbit_type)
        if image == orbit_type:
            fixed.append(orbit_type)
        else:
            pair = tuple(sorted((orbit_type, image)))
            pairs.append((pair[0], pair[1]))
            used.add(orbit_type)
            used.add(image)
    free_pairs = [pair for pair in pairs if empty_type not in pair and full_type not in pair]
    free_fixed = [orbit_type for orbit_type in fixed if orbit_type not in (empty_type, full_type)]
    return free_pairs, free_fixed


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        if condition:
            self.passed += 1
        else:
            self.failed += 1
        print(f"{'PASS' if condition else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def normalize(text: str) -> str:
    return " ".join(text.split())


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    self_source = Path(__file__).read_text(encoding="utf-8")
    note_flat = normalize(note)
    axiom_flat = normalize(axiom)

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
        (ROOT / path).read_text(encoding="utf-8")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print(
        "external_scientific_inputs: current Lattice/Admissibility/Record "
        "boundary only; no observation or fit"
    )
    print(
        "negative_scope: displayed Max(9) versus Q among the eight Q_* maps; "
        "does not adopt a bit"
    )

    orbits = build_orbits()
    orbit_types = tuple(sorted(orbits))
    orbit_sizes = {orbit_type: len(orbits[orbit_type]) for orbit_type in orbit_types}
    empty_type = axis_type(EMPTY)
    full_type = axis_type(FULL)
    free_pairs, free_fixed = f_cut_free_data(orbit_types, empty_type, full_type)
    n_free = len(free_pairs) + len(free_fixed)
    n_cut = 1 << n_free
    qstar = enumerate_qstar()
    ranked = [(remaining, coverage9(remaining)) for remaining in qstar]
    m9 = max(cov for _remaining, cov in ranked)
    n_max = sum(1 for _remaining, cov in ranked if cov == m9)
    n_q = sum(1 for remaining, _cov in ranked if selector_q(remaining))
    n_both = sum(1 for remaining, cov in ranked if cov == m9 and selector_q(remaining))
    equivalent = all((cov == m9) == selector_q(remaining) for remaining, cov in ranked)
    max_maps = [remaining for remaining, cov in ranked if cov == m9]
    q_maps = [remaining for remaining, _cov in ranked if selector_q(remaining)]
    misses = [
        remaining
        for remaining, cov in ranked
        if (cov == m9) != selector_q(remaining)
    ]
    lex_miss = misses[0] if misses else None

    l1_bits = bits_from_predicate(f_L1, orbit_types, orbits)
    ham_bits = bits_from_predicate(f_hamming, orbit_types, orbits)
    l1_remaining = remaining_bits_from_full(l1_bits, orbit_types)
    cov_l1 = next(cov for remaining, cov in ranked if remaining == l1_remaining)
    cov_f1 = next(cov for remaining, cov in ranked if remaining == F1_REMAINING)

    print(f"n_rotations={len(ROTATIONS)}")
    print(f"n_orbits={len(orbit_types)}")
    print(f"remaining_labels={REMAINING_LABELS}")
    print(f"N_free={n_free}")
    print(f"|F_cut|={n_cut}")
    print(f"|Q_*|={len(qstar)}")
    print(f"n_nine_site_seeds={len(NINE_SITE_SEEDS)}")
    print(f"m9={m9}")
    for remaining, cov in ranked:
        print(
            f"remaining={remaining} cov9={cov} max={int(cov == m9)} "
            f"Q={int(selector_q(remaining))}"
        )
    print(f"N_max={n_max}")
    print(f"N_Q={n_q}")
    print(f"N_both={n_both}")
    print(f"max_cov9_iff_Q={int(equivalent)}")
    print(f"max_maps={max_maps}")
    print(f"Q_maps={q_maps}")
    print(f"lex_first_miss={lex_miss}")
    print(f"f_L1_remaining={l1_remaining}")
    print(f"cov9_f_L1={cov_l1}")
    print(f"cov9_f1={cov_f1}")

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required note-plus-axiom string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/F_CUT_QSTAR_COV9_MAX_SELECTOR_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and AUDIT_TIMEOUT_SEC == 120
        and 'AUDIT_INPUT_PATHS = (\n'
        '    "docs/F_CUT_QSTAR_COV9_MAX_SELECTOR_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ')' in self_source,
    )
    checks.check(
        "thm1-twenty-four-rotations",
        "exactly 24 proper cube rotations",
        len(ROTATIONS) == 24 and len(set(ROTATIONS)) == 24,
    )
    checks.check(
        "thm1-ten-orbits",
        "exactly 10 orbits partition the 64 cells of {0,1}^6",
        len(orbit_types) == 10 and sum(orbit_sizes.values()) == 64,
    )
    expected_sizes = {
        (0, 0, 3): 1,
        (0, 1, 2): 3,
        (0, 2, 1): 3,
        (0, 3, 0): 1,
        (1, 0, 2): 6,
        (1, 1, 1): 12,
        (1, 2, 0): 6,
        (2, 0, 1): 12,
        (2, 1, 0): 12,
        (3, 0, 0): 8,
    }
    checks.check(
        "thm1-orbit-sizes",
        "orbit sizes are the axis-type class sizes",
        orbit_sizes == expected_sizes,
    )
    checks.check(
        "thm1-f-cut-cardinality",
        "F_cut has five free bits and size 32",
        n_free == 5
        and n_cut == 32
        and len(free_pairs) == 3
        and len(free_fixed) == 2
        and empty_type == (0, 0, 3)
        and full_type == (0, 3, 0)
        and REMAINING_ORDER == ((1, 0, 2), (0, 1, 2), (2, 0, 1), (3, 0, 0), (1, 1, 1)),
    )
    checks.check(
        "thm1-qstar-eight-lex",
        "Q_* is the eight remaining-bit tuples with wt1=1 and adj2=1 in lex order",
        len(qstar) == 8
        and qstar
        == [
            (1, 0, 1, 0, 0),
            (1, 0, 1, 0, 1),
            (1, 0, 1, 1, 0),
            (1, 0, 1, 1, 1),
            (1, 1, 1, 0, 0),
            (1, 1, 1, 0, 1),
            (1, 1, 1, 1, 0),
            (1, 1, 1, 1, 1),
        ]
        and all(in_qstar(remaining) for remaining in qstar)
        and qstar == sorted(qstar),
    )
    checks.check(
        "thm1-f-L1-is-unbalanced-axis",
        "f_L1 is 1 iff some axis has c_+ != c_-",
        all(
            f_L1(config) == int(axis_type(config)[0] >= 1)
            for config in product((0, 1), repeat=6)
        )
        and l1_remaining == L1_REMAINING
        and in_qstar(l1_remaining)
        and selector_q(l1_remaining)
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
        "thm1-two-cube-and-nine-site-seeds",
        "the two-cube has twelve vertices and C(12,9)=220 nine-site seeds",
        len(TWO_CUBE) == 12
        and len(set(TWO_CUBE)) == 12
        and len(NINE_SITE_SEEDS) == 220
        and len(set(NINE_SITE_SEEDS)) == 220
        and all(seed <= set(TWO_CUBE) and len(seed) == 9 for seed in NINE_SITE_SEEDS),
    )
    census_ok = True
    for remaining, cov in ranked:
        spaced = f"cov9({remaining}) = {cov}"
        if spaced not in note:
            census_ok = False
        if CENSUS[remaining] != cov:
            census_ok = False
    checks.check(
        "thm1-max-cov9-iff-Q",
        "among the eight Q_* maps, maximal cov9 equals vertex3=mixed3=1",
        equivalent
        and m9 == M9
        and ranked == [(remaining, CENSUS[remaining]) for remaining in qstar]
        and census_ok
        and all(0 <= cov <= M9 for _remaining, cov in ranked)
        and "remaining-bit lex order" in note
        and "maximal cov9" in note
        and "equivalent" in note,
    )
    checks.check(
        "thm2-census",
        "N_max = 2, N_Q = 2, N_both = 2 and there is no miss",
        n_max == N_MAX
        and n_q == N_Q
        and n_both == N_BOTH
        and n_max == n_q == n_both
        and max_maps == [L1_REMAINING, F1_REMAINING]
        and q_maps == [L1_REMAINING, F1_REMAINING]
        and misses == []
        and lex_miss is None
        and cov_l1 == M9
        and cov_f1 == M9
        and "N_max = 2" in note
        and "N_Q = 2" in note
        and "N_both = 2" in note
        and "no lex-first miss" in note,
    )
    checks.check(
        "thm3-display-not-adopted",
        "the identity is displayed and no remaining bit is adopted",
        "Displayed, not adopted" in note
        and "Do not adopt a bit" in note
        and "Do not write Q into Admissibility" in note
        and "does not adopt a bit" in self_source,
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
        "Among the 8 F_cut maps with wt1=1 and adj2=1 on the two-cube with "
        "off-patch o=0, whether maximal cov9 equals vertex3=mixed3=1 is "
        "reported. Displayed, not adopted."
    )
    checks.check(
        "claim-scope",
        "claim_scope reports the Max(9) versus Q identity and does not adopt a bit",
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
        and "Do not write Q into Admissibility" in note,
    )
    checks.check(
        "off-patch-zero",
        "off-patch occupancy is the explicit 0 default, not a blank-block",
        "off-patch occupancy `0`" in note
        and "off-patch o=0" in note
        and "blank-block is a different rule" in note,
    )
    checks.check(
        "l1-definition-in-note",
        "the note defines f_L1 as unbalanced-axis / n != 0 and rejects Hamming",
        "`f_L1(c)=1` if and only if some axis is unbalanced" in note_flat
        and "`n_μ = c_{+μ} − c_{-μ}` is nonzero" in note
        and "This is **not** Hamming parity" in note,
    )
    checks.check(
        "not-leftover-prior-k",
        "the residual is a new odd k inside Q_*, not leftover of tot3/5/7/10 or Max(4/6/8)",
        "New odd k" in note
        and "Not leftover-character of tot3" in note
        and "Not leftover-character of Max(4/6/8)" in note
        and "does not adopt a bit" in self_source
        and "Duality is not assumed" in note,
    )

    print("per_element: checked exactly — each of the 64 neighbor 6-tuples is assigned its axis-type orbit")
    print("per_site: checked exactly — each of the twelve two-cube vertices uses the same six-direction stencil")
    print("per_mode: checked exactly — each of the eight Q_* maps is scored on 220 nine-site seeds against Q")
    print("per_block: checked exactly — N_max, N_Q, N_both are the Q_* Max(9)-versus-Q counts on this patch")
    print("lattice_wide: checked and not executed — no Z^3-wide formation law or physical Admissibility selector is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
