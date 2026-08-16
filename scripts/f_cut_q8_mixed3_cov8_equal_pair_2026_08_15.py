#!/usr/bin/env python3
"""Name the unique Q8-true mixed3-pair with equal cov8.

F_cut is the cube-covariant class with f(empty)=f(full)=0 and f(c)=f(1-c).
Dynamics are occupancy-to-lock on the twelve-vertex two-cube with off-patch
occupancy 0. Coverage cov8(f) is the number of unordered 8-site seeds from
which f fills. Q8 is wt1 OR opp2 OR adj2 OR vertex3; it ignores mixed3.
Among the 15 Q8-true mixed3-pairs, Equal means the two maps that differ
only by mixed3 have the same cov8. The runner names the unique equal pair
(both remaining-bit tuples and both cov8 values), confirms N_eq=1, and
does not adopt the pair. f_L1 is the unbalanced-axis predicate (some
n_mu != 0), never Hamming |c|_1 mod 2.
"""

from __future__ import annotations

from itertools import combinations, permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/F_CUT_Q8_MIXED3_COV8_EQUAL_PAIR_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/F_CUT_Q8_MIXED3_COV8_EQUAL_PAIR_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Direction = tuple[int, int, int]
Config = tuple[int, int, int, int, int, int]
Rotation = tuple[tuple[int, int, int], tuple[int, int, int]]
OrbitType = tuple[int, int, int]
Site = tuple[int, int, int]
Bits = tuple[int, ...]
Prefix = tuple[int, int, int, int]

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
SITE_INDEX: dict[Site, int] = {site: index for index, site in enumerate(TWO_CUBE)}
EIGHT_SITE_SEEDS: tuple[frozenset[Site], ...] = tuple(
    frozenset(combo) for combo in combinations(TWO_CUBE, 8)
)
NEIGHBOR_INDICES: tuple[tuple[int | None, ...], ...] = tuple(
    tuple(
        SITE_INDEX.get(
            (site[0] + direction[0], site[1] + direction[1], site[2] + direction[2])
        )
        for direction in DIRECTIONS
    )
    for site in TWO_CUBE
)
REMAINING_ORDER: tuple[OrbitType, ...] = (
    (1, 0, 2),
    (0, 1, 2),
    (2, 0, 1),
    (3, 0, 0),
    (1, 1, 1),
)
REMAINING_LABELS: tuple[str, ...] = ("wt1", "opp2", "adj2", "vertex3", "mixed3")
L1_REMAINING: Bits = (1, 0, 1, 1, 1)
Q8_FALSE_PREFIX: Prefix = (0, 0, 0, 0)
EQUAL_PAIR_PREFIX: Prefix = (0, 1, 0, 0)
LEX_FIRST_DIFF_PREFIX: Prefix = (0, 0, 0, 1)
EQUAL_F0: Bits = (0, 1, 0, 0, 0)
EQUAL_F1: Bits = (0, 1, 0, 0, 1)
EQUAL_COV8 = 1


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


def remaining_value(config: Config, remaining: Bits) -> int:
    kind = axis_type(config)
    if kind in (axis_type(EMPTY), axis_type(FULL)):
        return 0
    assignment = dict(zip(REMAINING_ORDER, remaining, strict=True))
    if kind in assignment:
        return assignment[kind]
    return assignment[complement_type(kind)]


def q8(remaining: Bits) -> bool:
    """wt1 OR opp2 OR adj2 OR vertex3. Ignores mixed3."""
    return remaining[0] == 1 or remaining[1] == 1 or remaining[2] == 1 or remaining[3] == 1


def fire_table(remaining: Bits) -> dict[Config, int]:
    return {
        config: remaining_value(config, remaining)  # type: ignore[misc]
        for config in product((0, 1), repeat=6)
    }


def fills_from_mask(seed_mask: int, table: dict[Config, int]) -> bool:
    locked = seed_mask
    for _tick in range(13):
        nxt = locked
        for site_index in range(12):
            if (locked >> site_index) & 1:
                continue
            config = tuple(
                1 if neighbor is not None and (locked >> neighbor) & 1 else 0
                for neighbor in NEIGHBOR_INDICES[site_index]
            )
            if table[config]:  # type: ignore[index]
                nxt |= 1 << site_index
        if nxt == locked:
            return locked == (1 << 12) - 1
        locked = nxt
    return False


def coverage(remaining: Bits) -> int:
    table = fire_table(remaining)
    total = 0
    for combo in combinations(range(12), 8):
        seed_mask = 0
        for index in combo:
            seed_mask |= 1 << index
        if fills_from_mask(seed_mask, table):
            total += 1
    return total


def bits_from_predicate(
    predicate, orbit_types: tuple[OrbitType, ...], orbits: dict[OrbitType, frozenset[Config]]
) -> Bits:
    bits = []
    for orbit_type in orbit_types:
        sample = next(iter(orbits[orbit_type]))
        value = int(predicate(sample))
        if any(int(predicate(member)) != value for member in orbits[orbit_type]):
            raise RuntimeError("predicate is not cube-covariant")
        bits.append(value)
    return tuple(bits)


def remaining_bits_from_assignment(assignment: dict[OrbitType, int]) -> Bits:
    return tuple(assignment[orbit_type] for orbit_type in REMAINING_ORDER)


def remaining_bits_from_full(
    bits: Bits, orbit_types: tuple[OrbitType, ...]
) -> Bits:
    assignment = dict(zip(orbit_types, bits, strict=True))
    return remaining_bits_from_assignment(assignment)


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


def enumerate_f_cut(
    orbit_types: tuple[OrbitType, ...],
    empty_type: OrbitType,
    full_type: OrbitType,
) -> list[Bits]:
    free_pairs, free_fixed = f_cut_free_data(orbit_types, empty_type, full_type)
    n_free = len(free_pairs) + len(free_fixed)
    members: list[Bits] = []
    for mask in range(1 << n_free):
        assignment = {empty_type: 0, full_type: 0}
        for rank, pair in enumerate(free_pairs):
            value = (mask >> rank) & 1
            assignment[pair[0]] = value
            assignment[pair[1]] = value
        for rank, orbit_type in enumerate(free_fixed):
            assignment[orbit_type] = (mask >> (len(free_pairs) + rank)) & 1
        members.append(remaining_bits_from_assignment(assignment))
    return members


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
        "negative_scope: unique Q8-true mixed3-pair with equal cov8; "
        "does not adopt the pair"
    )

    orbits = build_orbits()
    orbit_types = tuple(sorted(orbits))
    orbit_sizes = {orbit_type: len(orbits[orbit_type]) for orbit_type in orbit_types}
    empty_type = axis_type(EMPTY)
    full_type = axis_type(FULL)
    free_pairs, free_fixed = f_cut_free_data(orbit_types, empty_type, full_type)
    n_free = len(free_pairs) + len(free_fixed)
    n_cut = 1 << n_free

    members = enumerate_f_cut(orbit_types, empty_type, full_type)
    cov_by_remaining = {remaining: coverage(remaining) for remaining in members}
    q8_true = sorted(remaining for remaining in members if q8(remaining))
    q8_false = sorted(remaining for remaining in members if not q8(remaining))
    prefixes = sorted({remaining[:4] for remaining in q8_true})
    pair_rows = []
    for prefix in prefixes:
        f0 = prefix + (0,)
        f1 = prefix + (1,)
        pair_rows.append((prefix, f0, f1, cov_by_remaining[f0], cov_by_remaining[f1]))
    equal_rows = [row for row in pair_rows if row[3] == row[4]]
    diff_rows = [row for row in pair_rows if row[3] != row[4]]
    n_eq = len(equal_rows)
    n_diff = len(diff_rows)
    lex_first_diff = diff_rows[0]
    equal_pair = equal_rows[0] if equal_rows else None

    l1_bits = bits_from_predicate(f_L1, orbit_types, orbits)
    ham_bits = bits_from_predicate(f_hamming, orbit_types, orbits)
    l1_remaining = remaining_bits_from_full(l1_bits, orbit_types)
    l1_prefix = l1_remaining[:4]
    cov_l1 = cov_by_remaining[l1_remaining]
    cov_l1_partner = cov_by_remaining[l1_prefix + (1 - l1_remaining[4],)]

    print(f"n_rotations={len(ROTATIONS)}")
    print(f"n_orbits={len(orbit_types)}")
    print(f"remaining_labels={REMAINING_LABELS}")
    print(f"N_free={n_free}")
    print(f"|F_cut|={n_cut}")
    print(f"n_eight_site_seeds={len(EIGHT_SITE_SEEDS)}")
    print(f"N_Q8={len(q8_true)}")
    print(f"N_Q8_false={len(q8_false)}")
    print(f"N_pairs={len(pair_rows)}")
    print(f"N_eq={n_eq}")
    print(f"N_diff={n_diff}")
    print(f"equal_pairs={[(row[1], row[2], row[3], row[4]) for row in equal_rows]}")
    print(
        "lex_first_diff="
        f"{lex_first_diff[1]} cov8={lex_first_diff[3]}; "
        f"{lex_first_diff[2]} cov8={lex_first_diff[4]}"
    )
    print(f"f_L1_remaining={l1_remaining}")
    print(f"f_L1_prefix={l1_prefix} cov8={cov_l1} partner_cov8={cov_l1_partner}")
    print(f"f_hamming_bits={ham_bits}")

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required note-plus-axiom string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/F_CUT_Q8_MIXED3_COV8_EQUAL_PAIR_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and AUDIT_TIMEOUT_SEC == 120
        and 'AUDIT_INPUT_PATHS = (\n'
        '    "docs/F_CUT_Q8_MIXED3_COV8_EQUAL_PAIR_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ')' in self_source,
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
        "thm1-host",
        "24 rotations, 10 orbits, 32 F_cut maps, 495 eight-site seeds",
        len(ROTATIONS) == 24
        and len(set(ROTATIONS)) == 24
        and len(orbit_types) == 10
        and sum(orbit_sizes.values()) == 64
        and orbit_sizes == expected_sizes
        and n_free == 5
        and n_cut == 32
        and len(members) == 32
        and len(set(members)) == 32
        and len(free_pairs) == 3
        and len(free_fixed) == 2
        and empty_type == (0, 0, 3)
        and full_type == (0, 3, 0)
        and len(TWO_CUBE) == 12
        and len(EIGHT_SITE_SEEDS) == 495
        and REMAINING_ORDER == ((1, 0, 2), (0, 1, 2), (2, 0, 1), (3, 0, 0), (1, 1, 1)),
    )
    checks.check(
        "thm1-f-L1-is-unbalanced-axis",
        "f_L1 is 1 iff some axis has c_+ != c_-",
        all(
            f_L1(config) == int(axis_type(config)[0] >= 1)
            for config in product((0, 1), repeat=6)
        )
        and l1_remaining == L1_REMAINING
        and q8(l1_remaining),
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
        "thm1-fifteen-q8-true-pairs",
        "Q8 is true on exactly 30 maps, grouped as 15 mixed3-pairs",
        len(q8_true) == 30
        and len(q8_false) == 2
        and q8_false == [(0, 0, 0, 0, 0), (0, 0, 0, 0, 1)]
        and all(cov_by_remaining[remaining] == 0 for remaining in q8_false)
        and all(cov_by_remaining[remaining] > 0 for remaining in q8_true)
        and len(prefixes) == 15
        and Q8_FALSE_PREFIX not in prefixes
        and all(q8(prefix + (0,)) and q8(prefix + (1,)) for prefix in prefixes),
    )
    checks.check(
        "thm1-unique-equal-pair",
        "unique equal pair is (0,1,0,0,0) cov8=1 and (0,1,0,0,1) cov8=1",
        equal_pair is not None
        and equal_pair[0] == EQUAL_PAIR_PREFIX
        and equal_pair[1] == EQUAL_F0
        and equal_pair[2] == EQUAL_F1
        and equal_pair[3] == EQUAL_COV8
        and equal_pair[4] == EQUAL_COV8
        and cov_by_remaining[EQUAL_F0] == 1
        and cov_by_remaining[EQUAL_F1] == 1
        and "(0, 1, 0, 0, 0)" in note
        and "(0, 1, 0, 0, 1)" in note
        and "cov8 = 1" in note,
    )
    checks.check(
        "thm2-n-eq-one-no-other",
        "N_eq=1 and no other of the 15 pairs has equal cov8",
        n_eq == 1
        and n_diff == 14
        and n_eq + n_diff == 15
        and all(row[3] != row[4] for row in pair_rows if row[0] != EQUAL_PAIR_PREFIX)
        and f"N_eq = {n_eq}" in note
        and "N_diff = 14" in note
        and "No other" in note
        and lex_first_diff[0] == LEX_FIRST_DIFF_PREFIX
        and lex_first_diff[3] == 44
        and lex_first_diff[4] == 132
        and cov_l1 != cov_l1_partner
        and l1_prefix != EQUAL_PAIR_PREFIX,
    )
    checks.check(
        "thm3-display-not-adopt",
        "the unique pair is displayed and is not adopted",
        "Displayed, not adopted" in note
        and "Do not adopt the pair" in note
        and "does not adopt the pair" in self_source
        and "Do not write the pair into Admissibility" in note,
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
        "Among the 15 Q8-true mixed3-pairs of F_cut on the two-cube with "
        "off-patch o=0, the unique pair with equal cov8 is reported. "
        "Displayed, not adopted."
    )
    checks.check(
        "claim-scope",
        "claim_scope reports the unique equal-cov8 pair among the 15 pairs",
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
        and "citation" not in note.lower()
        and ("import " + "qcd") not in self_source.lower(),
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
        and "Do not adopt the pair" in note,
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
        "not-leftover-mix3c8-mix3sel",
        "the residual is the newly named N_eq=1 pair, not leftover mix3c8 or mix3sel",
        "Not leftover-character of mix3c8" in note
        and "Not leftover-character of mix3sel" in note
        and "Newly named residual of `N_eq = 1`" in note
        and "does not adopt the pair" in self_source,
    )
    checks.check(
        "claim-type-and-gate",
        "N1-N8 and a passing no-go disposition are source-visible",
        all(f"### N{index}" in note for index in range(1, 9))
        and "No-Go Discipline disposition: **PASS**" in note
        and note.count("**ATTEMPTED**") == 6,
    )

    print(
        "per_element: checked exactly — each of the 64 neighbor 6-tuples "
        "is assigned its axis-type orbit"
    )
    print(
        "per_site: checked exactly — each of the twelve two-cube vertices "
        "uses the same six-direction stencil"
    )
    print(
        "per_mode: checked exactly — every Q8-true F_cut map is scored by "
        "how many of the 495 eight-site seeds it fills"
    )
    print(
        "per_block: checked exactly — the unique equal-cov8 mixed3-pair "
        "is named among the 15 Q8-true pairs"
    )
    print(
        "lattice_wide: checked and not executed — no Z^3-wide formation law "
        "or physical Admissibility selector is claimed"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
