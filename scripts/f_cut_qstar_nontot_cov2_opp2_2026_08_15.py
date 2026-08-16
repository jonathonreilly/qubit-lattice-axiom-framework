#!/usr/bin/env python3
"""Two-site coverage 36 versus opp2 among the four non-tot Q_* F_cut maps.

F_cut is the cube-covariant class with f(empty)=f(full)=0 and f(c)=f(1-c).
Dynamics are occupancy-to-lock on the twelve-vertex two-cube with off-patch
occupancy 0. Non-tot Q_* is the remaining-bit cut wt1=1, adj2=1 and
vertex3=0. Coverage cov2(f) is the number of two-site seeds from which f
fills. The runner reports whether cov2=36 iff opp2=1 on those four maps,
and the census integers N_opp, N_36, N_both. The identity is displayed;
the runner does not adopt a bit. f_L1 is the unbalanced-axis predicate
(some n_mu != 0), never Hamming |c|_1 mod 2.
"""

from __future__ import annotations

from itertools import combinations, permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/F_CUT_QSTAR_NONTOT_COV2_OPP2_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/F_CUT_QSTAR_NONTOT_COV2_OPP2_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
MAX36_REMAINING: frozenset[Remaining] = frozenset(
    (
        (1, 1, 1, 0, 0),
        (1, 1, 1, 0, 1),
    )
)
COV36 = 36
COV32 = 32


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


def in_qstar(remaining: Remaining) -> bool:
    return remaining[0] == 1 and remaining[2] == 1


def in_nontot_qstar(remaining: Remaining) -> bool:
    return in_qstar(remaining) and remaining[3] == 0


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
        "negative_scope: displayed cov2=36 versus opp2=1 inside non-tot Q_*; "
        "does not adopt a bit"
    )

    orbits = build_orbits()
    orbit_types = tuple(sorted(orbits))
    type_of = {config: orbit_type for orbit_type, group in orbits.items() for config in group}
    members = enumerate_f_cut(orbit_types, EMPTY_TYPE, FULL_TYPE)
    neighbors = neighbor_indices()
    seeds = seed_masks_for(2)
    n_two_site = len(seeds)
    rows: list[tuple[Remaining, int]] = []
    for bits, remaining in members:
        table = predicate_table(bits, orbit_types, type_of)
        cov = coverage_from_masks(table, seeds, neighbors)
        rows.append((remaining, cov))

    qstar = [(remaining, cov) for remaining, cov in rows if in_qstar(remaining)]
    nontot = [(remaining, cov) for remaining, cov in rows if in_nontot_qstar(remaining)]
    n_opp = sum(1 for remaining, _cov in nontot if remaining[1] == 1)
    n_36 = sum(1 for _remaining, cov in nontot if cov == COV36)
    n_both = sum(
        1 for remaining, cov in nontot if remaining[1] == 1 and cov == COV36
    )
    equivalent = all((cov == COV36) == (remaining[1] == 1) for remaining, cov in nontot)
    cov36 = frozenset(remaining for remaining, cov in nontot if cov == COV36)
    nontot_set = frozenset(remaining for remaining, _cov in nontot)
    opp_set = frozenset(remaining for remaining, _cov in nontot if remaining[1] == 1)
    cov_l1 = next(cov for remaining, cov in rows if remaining == L1_REMAINING)
    scored_table = {remaining: cov for remaining, cov in nontot}

    print(f"n_rotations={len(ROTATIONS)}")
    print(f"n_orbits={len(orbit_types)}")
    print(f"remaining_labels={REMAINING_LABELS}")
    print(f"|F_cut|={len(members)}")
    print(f"n_two_site_seeds={n_two_site}")
    print(f"|Q_*|={len(qstar)}")
    print(f"|non-tot Q_*|={len(nontot)}")
    print(f"N_opp={n_opp}")
    print(f"N_36={n_36}")
    print(f"N_both={n_both}")
    print(f"cov2=36_iff_opp2=1={int(equivalent)}")
    print(f"cov2(f_L1)={cov_l1}")
    for remaining, cov in sorted(nontot):
        print(
            f"non-tot Q_* {remaining} cov2={cov} opp2={remaining[1]} "
            f"is36={int(cov == COV36)}"
        )

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required note-plus-axiom string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/F_CUT_QSTAR_NONTOT_COV2_OPP2_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and AUDIT_TIMEOUT_SEC == 120
        and 'AUDIT_INPUT_PATHS = (\n'
        '    "docs/F_CUT_QSTAR_NONTOT_COV2_OPP2_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ')' in self_source,
    )
    checks.check(
        "thm1-host",
        "24 rotations, 10 orbits, 32 F_cut maps, 66 two-site seeds, 4 non-tot Q_* maps",
        len(ROTATIONS) == 24
        and len(set(ROTATIONS)) == 24
        and len(orbit_types) == 10
        and sum(len(orbits[orbit_type]) for orbit_type in orbit_types) == 64
        and len(members) == 32
        and n_two_site == 66
        and len(TWO_CUBE) == 12
        and len(qstar) == 8
        and len(nontot) == 4
        and EMPTY_TYPE == axis_type(EMPTY)
        and FULL_TYPE == axis_type(FULL),
    )
    checks.check(
        "thm1-f-L1-is-unbalanced-axis",
        "f_L1 is 1 iff some axis has c_+ != c_-",
        all(
            f_L1(config) == int(axis_type(config)[0] >= 1)
            for config in product((0, 1), repeat=6)
        )
        and L1_REMAINING not in nontot_set
        and in_qstar(L1_REMAINING)
        and L1_REMAINING[1] == 0
        and L1_REMAINING[3] == 1
        and cov_l1 == 62
        and cov_l1 != COV36
        and cov_l1 != COV32,
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
        "thm1-cov36-is-opp2-slice",
        "the two cov2=36 maps are exactly the non-tot Q_* maps with opp2=1",
        cov36 == MAX36_REMAINING
        and cov36 == opp_set
        and cov36 < nontot_set
        and len(cov36) == 2
        and all(in_nontot_qstar(remaining) for remaining in cov36)
        and all(remaining[1] == 1 for remaining in cov36),
    )
    checks.check(
        "thm1-equivalence",
        "among the four non-tot Q_* maps, cov2=36 is equivalent to opp2=1",
        equivalent
        and cov36 == opp_set
        and scored_table[(1, 0, 1, 0, 0)] == COV32
        and scored_table[(1, 0, 1, 0, 1)] == COV32
        and scored_table[(1, 1, 1, 0, 0)] == COV36
        and scored_table[(1, 1, 1, 0, 1)] == COV36
        and all(cov == COV36 for remaining, cov in nontot if remaining[1] == 1)
        and all(cov == COV32 for remaining, cov in nontot if remaining[1] == 0)
        and "cov2=36 is equivalent to" in note_flat
        and "holds" in note,
    )
    checks.check(
        "thm2-census",
        "N_opp = 2, N_36 = 2, N_both = 2",
        n_opp == 2
        and n_36 == 2
        and n_both == 2
        and n_opp == n_36 == n_both
        and "N_opp = 2" in note
        and "N_36 = 2" in note
        and "N_both = 2" in note,
    )
    checks.check(
        "thm3-display-not-adopted",
        "the identity is displayed and no bit is adopted",
        "Displayed, not adopted" in note
        and "Do not adopt a bit" in note
        and "Do not write `opp2` into Admissibility" in note
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
        "Among the 4 F_cut maps with wt1=1, adj2=1 and vertex3=0 on the two-cube "
        "with off-patch o=0, whether cov2=36 is equivalent to opp2=1 "
        "is reported. Displayed, not adopted."
    )
    checks.check(
        "claim-scope",
        "claim_scope reports the non-tot Q_* cov2=36 identity and does not adopt a bit",
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
        and "no axiom or approved primitive is added" in note,
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

    print("per_element: checked exactly — each of the 64 neighbor 6-tuples is assigned its axis-type orbit")
    print("per_site: checked exactly — each of the twelve two-cube vertices uses the same six-direction stencil")
    print("per_mode: checked exactly — every non-tot Q_* map is scored on sixty-six two-site seeds")
    print("per_block: checked exactly — cov2=36 iff opp2=1 is named, holds, and is not adopted")
    print("lattice_wide: checked and not executed — no Z^3-wide formation law or physical Admissibility selector is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
