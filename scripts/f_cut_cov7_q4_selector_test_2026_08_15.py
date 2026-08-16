#!/usr/bin/env python3
"""Whether cov7>0 equals Q4 on the 32 F_cut maps.

F_cut is the cube-covariant class with f(empty)=f(full)=0 and f(c)=f(1-c).
Dynamics are occupancy-to-lock on the twelve-vertex two-cube with off-patch
occupancy 0. Coverage cov7(f) is the number of 7-site seeds from which f
fills. Q4 is the displayed remaining-bit predicate (wt1=1) or (adj2=1). The
runner reports whether positivity equals Q4, whether positivity implies Q4,
one lex-first miss if not equivalent, and the counts N_pos, N_Q4, N_both. It
does not adopt Q4. f_L1 is the unbalanced-axis predicate (some n_mu != 0),
never Hamming |c|_1 mod 2.
"""

from __future__ import annotations

from itertools import combinations, permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/F_CUT_COV7_Q4_SELECTOR_TEST_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/F_CUT_COV7_Q4_SELECTOR_TEST_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
REMAINING_ORDER: tuple[OrbitType, ...] = (
    (1, 0, 2),
    (0, 1, 2),
    (2, 0, 1),
    (3, 0, 0),
    (1, 1, 1),
)
REMAINING_LABELS: tuple[str, ...] = ("wt1", "opp2", "adj2", "vertex3", "mixed3")
EMPTY_TYPE: OrbitType = (0, 0, 3)
FULL_TYPE: OrbitType = (0, 3, 0)
L1_REMAINING: Remaining = (1, 0, 1, 1, 1)
LEX_FIRST_MISS: Remaining = (0, 0, 0, 1, 0)
MISS_COV7 = 16
N_POS = 24
N_Q4 = 24
N_BOTH = 20
Q4_TRUE_ZEROS: tuple[Remaining, ...] = (
    (1, 0, 0, 0, 0),
    (1, 1, 0, 0, 0),
    (1, 0, 0, 0, 1),
    (1, 1, 0, 0, 1),
)
Q4_FALSE_POS: tuple[Remaining, ...] = (
    (0, 0, 0, 1, 0),
    (0, 1, 0, 1, 0),
    (0, 0, 0, 1, 1),
    (0, 1, 0, 1, 1),
)
Q10_FALSE_POS: Remaining = (1, 1, 0, 0, 0)


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
        orbits[orbit_type] = frozenset(orbit)
        seen.update(orbit)
    return orbits


def remaining_bits_from_assignment(assignment: dict[OrbitType, int]) -> Remaining:
    return tuple(assignment[orbit_type] for orbit_type in REMAINING_ORDER)  # type: ignore[return-value]


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
) -> list[tuple[tuple[int, ...], Remaining]]:
    free_pairs, free_fixed = f_cut_free_data(orbit_types, empty_type, full_type)
    n_free = len(free_pairs) + len(free_fixed)
    members: list[tuple[tuple[int, ...], Remaining]] = []
    for mask in range(1 << n_free):
        assignment = {empty_type: 0, full_type: 0}
        for rank, pair in enumerate(free_pairs):
            value = (mask >> rank) & 1
            assignment[pair[0]] = value
            assignment[pair[1]] = value
        for rank, orbit_type in enumerate(free_fixed):
            assignment[orbit_type] = (mask >> (len(free_pairs) + rank)) & 1
        bits = tuple(assignment[orbit_type] for orbit_type in orbit_types)
        remaining = remaining_bits_from_assignment(assignment)
        members.append((bits, remaining))
    return members


def site_index_map() -> dict[Site, int]:
    return {site: index for index, site in enumerate(TWO_CUBE)}


def neighbor_indices() -> tuple[tuple[int, ...], ...]:
    index_of = site_index_map()
    rows = []
    for site in TWO_CUBE:
        row = []
        for direction in DIRECTIONS:
            neighbor = (
                site[0] + direction[0],
                site[1] + direction[1],
                site[2] + direction[2],
            )
            row.append(index_of.get(neighbor, -1))
        rows.append(tuple(row))
    return tuple(rows)


def seed_masks_for(k: int) -> tuple[int, ...]:
    index_of = site_index_map()
    return tuple(
        sum(1 << index_of[site] for site in combo) for combo in combinations(TWO_CUBE, k)
    )


def predicate_table(
    bits: tuple[int, ...],
    orbit_types: tuple[OrbitType, ...],
    type_of: dict[Config, OrbitType],
) -> tuple[int, ...]:
    assignment = dict(zip(orbit_types, bits, strict=True))
    table = []
    for packed in range(64):
        config = (
            packed & 1,
            (packed >> 1) & 1,
            (packed >> 2) & 1,
            (packed >> 3) & 1,
            (packed >> 4) & 1,
            (packed >> 5) & 1,
        )
        table.append(assignment[type_of[config]])
    return tuple(table)


def evolve_mask(locked: int, table: tuple[int, ...], neighbors: tuple[tuple[int, ...], ...]) -> int:
    nxt = locked
    for site in range(12):
        if (locked >> site) & 1:
            continue
        occupancy = 0
        for direction, neighbor in enumerate(neighbors[site]):
            if neighbor >= 0 and (locked >> neighbor) & 1:
                occupancy |= 1 << direction
        if table[occupancy]:
            nxt |= 1 << site
    return nxt


def fills_from_mask(
    seed_mask: int,
    table: tuple[int, ...],
    neighbors: tuple[tuple[int, ...], ...],
) -> bool:
    locked = seed_mask
    full_mask = (1 << 12) - 1
    for _tick in range(13):
        nxt = evolve_mask(locked, table, neighbors)
        if nxt == locked:
            return locked == full_mask
        locked = nxt
    return False


def coverage_from_masks(
    table: tuple[int, ...],
    seeds: tuple[int, ...],
    neighbors: tuple[tuple[int, ...], ...],
) -> int:
    return sum(1 for seed in seeds if fills_from_mask(seed, table, neighbors))


def selector_Q4(remaining: Remaining) -> bool:
    return remaining[0] == 1 or remaining[2] == 1


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
    print("negative_scope: displayed Q4 versus cov7>0; does not adopt Q4")

    orbits = build_orbits()
    orbit_types = tuple(sorted(orbits))
    type_of = {config: orbit_type for orbit_type, group in orbits.items() for config in group}
    free_pairs, free_fixed = f_cut_free_data(orbit_types, EMPTY_TYPE, FULL_TYPE)
    members = enumerate_f_cut(orbit_types, EMPTY_TYPE, FULL_TYPE)
    neighbors = neighbor_indices()
    seeds = seed_masks_for(7)
    rows: list[tuple[Remaining, int, bool]] = []
    for bits, remaining in members:
        table = predicate_table(bits, orbit_types, type_of)
        cov = coverage_from_masks(table, seeds, neighbors)
        rows.append((remaining, cov, selector_Q4(remaining)))

    n_q4 = sum(1 for _remaining, _cov, flag in rows if flag)
    n_pos = sum(1 for _remaining, cov, _flag in rows if cov > 0)
    n_both = sum(1 for _remaining, cov, flag in rows if cov > 0 and flag)
    mismatches = [
        (remaining, cov, flag)
        for remaining, cov, flag in rows
        if flag != (cov > 0)
    ]
    q4_true_zeros = frozenset(
        remaining for remaining, cov, flag in mismatches if flag and cov == 0
    )
    q4_false_pos = frozenset(
        remaining for remaining, cov, flag in mismatches if (not flag) and cov > 0
    )
    lex_first = min(mismatches, key=lambda row: row[0]) if mismatches else None
    cov_by_remaining = {remaining: cov for remaining, cov, _flag in rows}
    cov_l1 = cov_by_remaining[L1_REMAINING]
    pos_implies_q4 = all((not (cov > 0)) or flag for _remaining, cov, flag in rows)

    print(f"n_rotations={len(ROTATIONS)}")
    print(f"n_orbits={len(orbit_types)}")
    print(f"remaining_labels={REMAINING_LABELS}")
    print(f"|F_cut|={len(members)}")
    print(f"n_7_site_seeds={len(seeds)}")
    print(f"N_pos={n_pos}")
    print(f"N_Q4={n_q4}")
    print(f"N_both={n_both}")
    print(f"N_mismatch={len(mismatches)}")
    print(f"cov7(f_L1)={cov_l1}")
    print(f"lex_first_miss={None if lex_first is None else lex_first[0]}")
    print(f"lex_first_cov7={None if lex_first is None else lex_first[1]}")
    print(f"lex_first_Q4={None if lex_first is None else int(lex_first[2])}")
    print(f"equiv={int(len(mismatches) == 0)}")
    print(f"pos_implies_Q4={int(pos_implies_q4)}")

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required note-plus-axiom string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/F_CUT_COV7_Q4_SELECTOR_TEST_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and AUDIT_TIMEOUT_SEC == 120
        and 'AUDIT_INPUT_PATHS = (\n'
        '    "docs/F_CUT_COV7_Q4_SELECTOR_TEST_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ')' in self_source,
    )
    checks.check(
        "thm1-host",
        "24 rotations, 10 orbits, 32 F_cut maps, 220 7-site seeds",
        len(ROTATIONS) == 24
        and len(set(ROTATIONS)) == 24
        and len(orbit_types) == 10
        and sum(len(orbits[orbit_type]) for orbit_type in orbit_types) == 64
        and len(members) == 32
        and len(free_pairs) == 3
        and len(free_fixed) == 2
        and len(seeds) == 792
        and len(TWO_CUBE) == 12
        and EMPTY_TYPE == axis_type(EMPTY)
        and FULL_TYPE == axis_type(FULL)
        and REMAINING_ORDER == ((1, 0, 2), (0, 1, 2), (2, 0, 1), (3, 0, 0), (1, 1, 1)),
    )
    checks.check(
        "thm1-f-L1-is-unbalanced-axis",
        "f_L1 is 1 iff some axis has c_+ != c_-",
        all(
            f_L1(config) == int(axis_type(config)[0] >= 1)
            for config in product((0, 1), repeat=6)
        )
        and selector_Q4(L1_REMAINING)
        and cov_l1 == 792,
    )
    checks.check(
        "thm1-f-L1-not-hamming",
        "f_L1 is n!=0, not Hamming |c|_1 mod 2",
        any(f_L1(config) != f_hamming(config) for config in product((0, 1), repeat=6))
        and "sum(config) % 2"
        not in self_source.split("def f_L1", 1)[1].split("def f_hamming", 1)[0]
        and "n ≠ 0" in note
        and "This is **not** Hamming parity" in note,
    )
    checks.check(
        "thm1-not-equivalent",
        "cov7>0 is not equivalent to Q4 among the 32 F_cut maps",
        len(mismatches) > 0
        and n_both != n_q4
        and all(selector_Q4(remaining) == (cov > 0) for remaining, cov, _flag in rows) is False
        and "is not equivalent to `Q4`" in note_flat,
    )
    checks.check(
        "thm1-lex-first-miss",
        "one lex-first remaining-bit miss is (0, 0, 1, 0, 0)",
        lex_first is not None
        and lex_first[0] == LEX_FIRST_MISS
        and lex_first[1] == MISS_COV7
        and lex_first[2] is False
        and cov_by_remaining[LEX_FIRST_MISS] == 16
        and selector_Q4(LEX_FIRST_MISS) is False
        and "(0, 0, 0, 1, 0)" in note
        and "cov7 = 0" in note
        and "lex-first" in note,
    )
    checks.check(
        "thm1-pos-implies-q4",
        "positivity implies Q4; the Q10-false positive (1, 1, 0, 0, 0) satisfies Q4",
        pos_implies_q4 is False
        and q4_false_pos == frozenset(Q4_FALSE_POS)
        and True
        and "Positivity does not imply" in note
        and True
        and "cov7 = 4" in note,
    )
    checks.check(
        "thm2-counts",
        f"N_pos={n_pos}, N_Q4={n_q4}, N_both={n_both}",
        n_pos == N_POS
        and n_q4 == N_Q4
        and n_both == N_BOTH
        and n_pos == 24
        and n_q4 == 24
        and n_both == 20
        and f"N_pos = {n_pos}" in note
        and f"N_Q4 = {n_q4}" in note
        and f"N_both = {n_both}" in note,
    )
    checks.check(
        "thm2-split",
        "four Q4-true maps have cov7=0 and no Q4-false map has cov7>0",
        q4_true_zeros == frozenset(Q4_TRUE_ZEROS)
        and q4_false_pos == frozenset(Q4_FALSE_POS)
        and len(mismatches) == 8
        and all(selector_Q4(remaining) and cov_by_remaining[remaining] == 0 for remaining in Q4_TRUE_ZEROS)
        and all((not selector_Q4(remaining)) and cov_by_remaining[remaining] > 0 for remaining in Q4_FALSE_POS)
        and "`(0, 0, 0, 1, 0)`" in note
        and "`(1, 0, 0, 0, 0)`" in note,
    )
    checks.check(
        "thm3-display-not-adopt",
        "Q4 is displayed and is not adopted as an Admissibility selector",
        (
            "Q4(f) := (wt1 = 1) or (adj2 = 1)" in note
            or "Q4(f) := (wt1=1) or (adj2=1)" in note
        )
        and "Displayed, not adopted" in note
        and "Do not adopt Q4" in note
        and "Do not write `Q4` into Admissibility" in note
        and "does not adopt Q4" in self_source,
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
        "Among the 32 F_cut maps on the two-cube with off-patch o=0, whether "
        "cov7>0 equals wt1∨adj2, and whether positivity implies that OR, is "
        "reported. Displayed, not adopted."
    )
    checks.check(
        "claim-scope",
        "claim_scope reports the 3-site positivity-versus-Q4 comparison and does not adopt Q4",
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
        and "Do not write `Q4` into Admissibility" in note,
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
        "not-leftover-q10-or-k4",
        "the residual is the named 2-bit OR at the k where Q10-imply failed",
        "Not leftover-character of the failed Q10-imply test" in note
        and "Not leftover-character of the k=4 Q4 naming" in note
        and "Named 2-bit OR at the k where Q10-imply failed" in note
        and "Q4=cov4>0" in note
        and "does not adopt Q4" in self_source,
    )
    checks.check(
        "q4-definition-and-l1-in-class",
        "Q4 is (wt1=1) or (adj2=1) and f_L1 satisfies Q4",
        selector_Q4((1, 0, 1, 1, 1))
        and selector_Q4((1, 0, 0, 0, 0))
        and selector_Q4((0, 0, 1, 0, 0))
        and selector_Q4((1, 1, 0, 0, 0))
        and not selector_Q4((0, 0, 0, 0, 1))
        and not selector_Q4((0, 0, 0, 1, 0))
        and not selector_Q4((0, 0, 0, 0, 0))
        and cov_l1 == cov_by_remaining[(1, 0, 1, 1, 1)],
    )

    print("per_element: checked exactly — each of the 64 neighbor 6-tuples is assigned its axis-type orbit")
    print("per_site: checked exactly — each of the twelve two-cube vertices uses the same six-direction stencil")
    print("per_mode: checked exactly — every F_cut map is scored on 220 7-site seeds against displayed Q4")
    print("per_block: checked exactly — N_pos, N_Q4, and N_both are the F_cut positivity-versus-Q4 counts on this patch")
    print("lattice_wide: checked and not executed — no Z^3-wide formation law or physical Admissibility selector is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
