#!/usr/bin/env python3
"""First remaining-bit refuse of F_cut (1,0,1,0,0) from S={(0,0,0),(2,0,0)}.

F_cut is the cube-covariant class with f(empty)=f(full)=0 and f(c)=f(1-c).
Dynamics are occupancy-to-lock on the twelve-vertex two-cube with off-patch
occupancy 0. Q_* is the remaining-bit cut wt1=1 and adj2=1. The scored map
is f_lo=(1,0,1,0,0). The seed is the lex-first 2-site split of
cov2=32 versus 36. The runner names the first remaining-bit refuse of
f_lo from that seed and N_refuse on that tick. Displayed, not adopted.
The runner does not adopt a bit. f_L1 is the unbalanced-axis predicate
(some n_mu != 0), never Hamming |c|_1 mod 2.
"""

from __future__ import annotations

from itertools import combinations, permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/F_CUT_QSTAR_NONTOT_COV2_SPLIT_REFUSE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/F_CUT_QSTAR_NONTOT_COV2_SPLIT_REFUSE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
    sorted((x, y, z) for x in range(3) for y in range(2) for z in range(2))
)
TWO_SITE_SEEDS: tuple[tuple[Site, Site], ...] = tuple(combinations(TWO_CUBE, 2))
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
F_LO: Remaining = (1, 0, 1, 0, 0)
F_HI: Remaining = (1, 1, 1, 0, 0)
SEED: tuple[Site, Site] = ((0, 0, 0), (2, 0, 0))
OPP2_REP: Config = (1, 1, 0, 0, 0, 0)
MIDDLE: Site = (1, 0, 0)


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


def remaining_label(kind: OrbitType) -> str | None:
    if kind in REMAINING_ORDER:
        return REMAINING_LABELS[REMAINING_ORDER.index(kind)]
    partner = complement_type(kind)
    if partner in REMAINING_ORDER:
        return REMAINING_LABELS[REMAINING_ORDER.index(partner)]
    return None


def remaining_value(config: Config, remaining: Remaining) -> int:
    kind = axis_type(config)
    if kind in (EMPTY_TYPE, FULL_TYPE):
        return 0
    assignment = dict(zip(REMAINING_ORDER, remaining, strict=True))
    if kind in assignment:
        return assignment[kind]
    return assignment[complement_type(kind)]


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


def seed_mask(seed: tuple[Site, ...]) -> int:
    index_of = site_index_map()
    return sum(1 << index_of[site] for site in seed)


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


def run_from_mask(
    seed_mask_value: int,
    table: tuple[int, ...],
    neighbors: tuple[tuple[int, ...], ...],
) -> tuple[bool, tuple[int, ...]]:
    locked = seed_mask_value
    full_mask = (1 << 12) - 1
    history = [bin(locked).count("1")]
    for _tick in range(13):
        nxt = evolve_mask(locked, table, neighbors)
        if nxt == locked:
            return locked == full_mask, tuple(history)
        locked = nxt
        history.append(bin(locked).count("1"))
    return False, tuple(history)


def fills_from_mask(
    seed_mask_value: int,
    table: tuple[int, ...],
    neighbors: tuple[tuple[int, ...], ...],
) -> bool:
    return run_from_mask(seed_mask_value, table, neighbors)[0]


def coverage_from_masks(
    table: tuple[int, ...],
    seeds: tuple[int, ...],
    neighbors: tuple[tuple[int, ...], ...],
) -> int:
    return sum(1 for seed in seeds if fills_from_mask(seed, table, neighbors))


def in_qstar(remaining: Remaining) -> bool:
    return remaining[0] == 1 and remaining[2] == 1


def bits_from_predicate(
    predicate,
    orbit_types: tuple[OrbitType, ...],
    orbits: dict[OrbitType, frozenset[Config]],
) -> tuple[int, ...]:
    bits = []
    for orbit_type in orbit_types:
        sample = next(iter(orbits[orbit_type]))
        value = int(predicate(sample))
        if any(int(predicate(member)) != value for member in orbits[orbit_type]):
            raise RuntimeError("predicate is not cube-covariant")
        bits.append(value)
    return tuple(bits)


def remaining_from_full(bits: tuple[int, ...], orbit_types: tuple[OrbitType, ...]) -> Remaining:
    assignment = dict(zip(orbit_types, bits, strict=True))
    return remaining_bits_from_assignment(assignment)


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


def first_remaining_bit_refuse(
    remaining: Remaining, seed: set[Site]
) -> tuple[int, Site, Config, OrbitType, str, int] | None:
    locked = set(seed)
    for tick in range(1, 14):
        events: list[tuple[Site, Config, OrbitType, str | None, int]] = []
        nxt = set(locked)
        for site in TWO_CUBE:
            if site in locked:
                continue
            config = neighborhood(site, locked)
            kind = axis_type(config)
            label = remaining_label(kind)
            value = remaining_value(config, remaining)
            events.append((site, config, kind, label, value))
            if value:
                nxt.add(site)
        remaining_refuses = [
            (site, config, kind, label)
            for site, config, kind, label, value in events
            if value == 0 and label is not None
        ]
        if remaining_refuses:
            site, config, kind, label = remaining_refuses[0]
            return (tick, site, config, kind, label, len(remaining_refuses))
        if nxt == locked:
            return None
        locked = nxt
    return None


def halt_set(remaining: Remaining, seed: set[Site]) -> frozenset[Site]:
    locked = set(seed)
    for _tick in range(13):
        nxt = set(locked)
        for site in TWO_CUBE:
            if site in locked:
                continue
            if remaining_value(neighborhood(site, locked), remaining):
                nxt.add(site)
        if nxt == locked:
            return frozenset(locked)
        locked = nxt
    return frozenset(locked)


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
        "negative_scope: displayed first remaining-bit refuse of non-tot Q_* "
        "f_lo from S; does not adopt a bit"
    )

    orbits = build_orbits()
    orbit_types = tuple(sorted(orbits))
    type_of = {config: orbit_type for orbit_type, group in orbits.items() for config in group}
    members = enumerate_f_cut(orbit_types, EMPTY_TYPE, FULL_TYPE)
    neighbors = neighbor_indices()
    seed_masks = tuple(seed_mask(seed) for seed in TWO_SITE_SEEDS)
    n_two_site = len(seed_masks)
    by_remaining = {remaining: bits for bits, remaining in members}

    table_lo = predicate_table(by_remaining[F_LO], orbit_types, type_of)
    table_hi = predicate_table(by_remaining[F_HI], orbit_types, type_of)
    cov_lo = coverage_from_masks(table_lo, seed_masks, neighbors)
    cov_hi = coverage_from_masks(table_hi, seed_masks, neighbors)
    hi_fill, hist_hi = run_from_mask(seed_mask(SEED), table_hi, neighbors)
    lo_fill, hist_lo = run_from_mask(seed_mask(SEED), table_lo, neighbors)

    seed_set = set(SEED)
    refuse = first_remaining_bit_refuse(F_LO, seed_set)
    halt_lo = halt_set(F_LO, seed_set)
    middle_cfg = neighborhood(MIDDLE, seed_set)

    l1_bits = bits_from_predicate(f_L1, orbit_types, orbits)
    l1_remaining = remaining_from_full(l1_bits, orbit_types)
    qstar = [remaining for _bits, remaining in members if in_qstar(remaining)]
    nontot = [remaining for remaining in qstar if remaining[3] == 0]

    print(f"n_rotations={len(ROTATIONS)}")
    print(f"n_orbits={len(orbit_types)}")
    print(f"remaining_labels={REMAINING_LABELS}")
    print(f"|F_cut|={len(members)}")
    print(f"n_two_site_seeds={n_two_site}")
    print(f"|Q_*|={len(qstar)}")
    print(f"|non-tot Q_*|={len(nontot)}")
    print(f"f_lo={F_LO} cov2={cov_lo} vertex3={F_LO[3]} qstar={int(in_qstar(F_LO))}")
    print(f"f_hi={F_HI} cov2={cov_hi} vertex3={F_HI[3]} qstar={int(in_qstar(F_HI))}")
    print(f"f_L1_remaining={l1_remaining}")
    print(f"hist_hi={hist_hi} fill_hi={int(hi_fill)}")
    print(f"hist_lo={hist_lo} fill_lo={int(lo_fill)}")
    print(f"halt_lo={sorted(halt_lo)} halt_size={len(halt_lo)}")
    print(f"first_refuse={refuse}")
    print(f"middle_from_S={middle_cfg} axis={axis_type(middle_cfg)}")

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required note-plus-axiom string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/F_CUT_QSTAR_NONTOT_COV2_SPLIT_REFUSE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and AUDIT_TIMEOUT_SEC == 120
        and 'AUDIT_INPUT_PATHS = (\n'
        '    "docs/F_CUT_QSTAR_NONTOT_COV2_SPLIT_REFUSE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ')' in self_source,
    )
    checks.check(
        "thm1-host",
        "24 rotations, 10 orbits, 32 F_cut maps, 66 two-site seeds, 8 Q_* maps",
        len(ROTATIONS) == 24
        and len(set(ROTATIONS)) == 24
        and len(orbit_types) == 10
        and sum(len(orbits[orbit_type]) for orbit_type in orbit_types) == 64
        and len(members) == 32
        and n_two_site == 66
        and len(TWO_CUBE) == 12
        and TWO_CUBE == tuple(sorted(TWO_CUBE))
        and len(qstar) == 8
        and len(nontot) == 4
        and EMPTY_TYPE == axis_type(EMPTY)
        and FULL_TYPE == axis_type(FULL)
        and axis_type(OPP2_REP) == (0, 1, 2),
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
        and l1_remaining[3] == 1,
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
        "thm1-f-lo-nontot-qstar",
        "f_lo is Q_* with vertex3=0; cov2 is 32 versus 36",
        in_qstar(F_LO)
        and in_qstar(F_HI)
        and F_LO[3] == 0
        and F_HI[3] == 0
        and F_LO in nontot
        and F_HI in nontot
        and F_LO in by_remaining
        and F_HI in by_remaining
        and cov_lo == 32
        and cov_hi == 36
        and "cov2=32" in note
        and "cov2=36" in note,
    )
    assert refuse is not None
    refuse_tick, refuse_site, refuse_config, refuse_kind, refuse_label, n_refuse = refuse
    checks.check(
        "thm1-first-refuse-tick-site-type",
        "first remaining-bit refuse of f_lo from S is tick 1, site (1,0,0), type opp2",
        refuse_tick == 1
        and refuse_site == MIDDLE
        and refuse_label == "opp2"
        and refuse_kind == (0, 1, 2)
        and remaining_value(refuse_config, F_LO) == 0
        and remaining_value(refuse_config, F_HI) == 1
        and not lo_fill
        and hi_fill
        and hist_lo == (2, 6, 8)
        and hist_hi == (2, 7, 9, 10, 12)
        and len(halt_lo) == 8
        and MIDDLE not in halt_lo,
    )
    checks.check(
        "thm1-first-refused-neighborhood",
        "lex-first refused remaining-bit neighborhood is (1,1,0,0,0,0) at (1,0,0)",
        refuse_config == OPP2_REP
        and axis_type(refuse_config) == (0, 1, 2)
        and middle_cfg == OPP2_REP
        and "(1, 1, 0, 0, 0, 0)" in note
        and "`(1,0,0)`" in note
        and "type `opp2`" in note,
    )
    checks.check(
        "thm2-n-refuse-first-tick",
        "N_refuse on the first refuse tick is 1",
        n_refuse == 1
        and "N_refuse = 1" in note
        and refuse_tick == 1,
    )
    checks.check(
        "thm2-opp2-is-32-vs-36-mechanism",
        "from S the middle site (1,0,0) is opp2, so only f_hi locks it at tick 1",
        axis_type(middle_cfg) == (0, 1, 2)
        and middle_cfg == OPP2_REP
        and table_hi[sum(bit << index for index, bit in enumerate(middle_cfg))] == 1
        and table_lo[sum(bit << index for index, bit in enumerate(middle_cfg))] == 0
        and F_HI[1] == 1
        and F_LO[1] == 0
        and "mechanism of the 32-versus-36" in note,
    )
    checks.check(
        "thm3-display-not-adopted",
        "the refuse is displayed and no bit is adopted",
        "Displayed, not adopted" in note
        and "Do not adopt a bit" in note
        and "Do not write `opp2`" in note
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
        "On the two-cube with off-patch o=0, the "
        "first remaining-bit refuse of F_cut (1,0,1,0,0) from "
        "S={(0,0,0),(2,0,0)} is reported. Displayed, not adopted."
    )
    checks.check(
        "claim-scope",
        "claim_scope reports the first remaining-bit refuse of f_lo from S and does not adopt a bit",
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
    print("per_mode: checked exactly — f_lo is evolved from S; f_hi is displayed contrast only")
    print("per_block: checked exactly — first remaining-bit refuse and N_refuse are named and not adopted")
    print("lattice_wide: checked and not executed — no Z^3-wide formation law or physical Admissibility selector is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
