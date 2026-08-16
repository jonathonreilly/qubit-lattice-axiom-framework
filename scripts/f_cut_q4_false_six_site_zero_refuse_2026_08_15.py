#!/usr/bin/env python3
"""First remaining-bit refuse of F_cut (0,0,0,0,0) on the lex-first 6-site f1 fill.

F_cut is the cube-covariant class with f(empty)=f(full)=0 and f(c)=f(1-c).
Dynamics are occupancy-to-lock on the twelve-vertex two-cube with off-patch
occupancy 0. f_z is remaining bits (0,0,0,0,0). S is the lex-first six-site
seed that f1 fills. The runner names S and the first remaining-bit refuse
of f_z from S (tick, site, remaining-bit type) and reports N_refuse on that
tick. It does not adopt a bit. f_L1 is the unbalanced-axis predicate
(some n_mu != 0), never Hamming |c|_1 mod 2.
"""

from __future__ import annotations

from itertools import combinations, permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/F_CUT_Q4_FALSE_SIX_SITE_ZERO_REFUSE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/F_CUT_Q4_FALSE_SIX_SITE_ZERO_REFUSE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
F1_REMAINING: Remaining = (1, 1, 1, 1, 1)
FZ_REMAINING: Remaining = (0, 0, 0, 0, 0)


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


def remaining_label(orbit_type: OrbitType) -> str | None:
    if orbit_type in REMAINING_ORDER:
        return REMAINING_LABELS[REMAINING_ORDER.index(orbit_type)]
    image = complement_type(orbit_type)
    if image in REMAINING_ORDER:
        return REMAINING_LABELS[REMAINING_ORDER.index(image)]
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


def evolve(locked: set[Site], remaining: Remaining) -> set[Site]:
    nxt = set(locked)
    for site in TWO_CUBE:
        if site in locked:
            continue
        if remaining_value(neighborhood(site, locked), remaining):
            nxt.add(site)
    return nxt


def fills_from_seed(seed: frozenset[Site], remaining: Remaining) -> bool:
    locked = set(seed)
    for _tick in range(13):
        nxt = evolve(locked, remaining)
        if nxt == locked:
            return len(locked) == 12
        locked = nxt
    return False


def remaining_refuses(
    locked: set[Site], remaining: Remaining
) -> list[tuple[Site, str, OrbitType]]:
    rows: list[tuple[Site, str, OrbitType]] = []
    for site in TWO_CUBE:
        if site in locked:
            continue
        config = neighborhood(site, locked)
        kind = axis_type(config)
        label = remaining_label(kind)
        if label is not None and remaining_value(config, remaining) == 0:
            rows.append((site, label, kind))
    return rows


def first_remaining_refuse(
    seed: frozenset[Site], remaining: Remaining
) -> tuple[int, list[tuple[Site, str, OrbitType]]]:
    locked = set(seed)
    for tick in range(1, 14):
        refuses = remaining_refuses(locked, remaining)
        nxt = evolve(locked, remaining)
        if refuses:
            return tick, refuses
        if nxt == locked:
            return 0, []
        locked = nxt
    return 0, []


def six_site_seeds() -> tuple[frozenset[Site], ...]:
    return tuple(frozenset(combo) for combo in combinations(TWO_CUBE, 6))


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
    print("negative_scope: displayed first remaining-bit refuse; does not adopt a bit")

    orbits = build_orbits()
    orbit_types = tuple(sorted(orbits))
    free_pairs, free_fixed = f_cut_free_data(orbit_types, EMPTY_TYPE, FULL_TYPE)
    members = enumerate_f_cut(orbit_types, EMPTY_TYPE, FULL_TYPE)
    remaining_set = {remaining for _bits, remaining in members}
    seeds = six_site_seeds()
    lex_first_any = frozenset(next(combinations(TWO_CUBE, 6)))
    f1_fillers = [seed for seed in seeds if fills_from_seed(seed, F1_REMAINING)]
    seed_s = f1_fillers[0]
    f1_fills_s = fills_from_seed(seed_s, F1_REMAINING)
    fz_fills_s = fills_from_seed(seed_s, FZ_REMAINING)
    tick, refuses = first_remaining_refuse(seed_s, FZ_REMAINING)
    n_refuse = len(refuses)
    first_site, first_label, first_kind = min(refuses, key=lambda row: row[0])
    refuse_sites = tuple(sorted(row[0] for row in refuses))
    refuse_labels = {row[0]: row[1] for row in refuses}
    fz_identically_zero = all(
        remaining_value(config, FZ_REMAINING) == 0  # type: ignore[arg-type]
        for config in product((0, 1), repeat=6)
    )
    l1_remaining = tuple(
        remaining_value(next(iter(orbits[orbit_type])), L1_REMAINING)
        if orbit_type in REMAINING_ORDER
        else remaining_value(next(iter(orbits[orbit_type])), L1_REMAINING)
        for orbit_type in REMAINING_ORDER
    )
    computed_l1 = tuple(
        1 if orbit_type[0] >= 1 else 0 for orbit_type in REMAINING_ORDER
    )

    print(f"n_rotations={len(ROTATIONS)}")
    print(f"n_orbits={len(orbit_types)}")
    print(f"remaining_labels={REMAINING_LABELS}")
    print(f"|F_cut|={len(members)}")
    print(f"n_six_site_seeds={len(seeds)}")
    print(f"n_f1_fill={len(f1_fillers)}")
    print(f"S={tuple(sorted(seed_s))}")
    print(f"f1_fills_S={int(f1_fills_s)}")
    print(f"f_z_fills_S={int(fz_fills_s)}")
    print(f"first_tick={tick}")
    print(f"first_site={first_site}")
    print(f"first_type={first_label}")
    print(f"first_kind={first_kind}")
    print(f"N_refuse={n_refuse}")
    print(f"refuse_sites={refuse_sites}")
    print(f"f_z_identically_zero={int(fz_identically_zero)}")
    print(f"f_L1_remaining={computed_l1}")

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required note-plus-axiom string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/F_CUT_Q4_FALSE_SIX_SITE_ZERO_REFUSE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and AUDIT_TIMEOUT_SEC == 120
        and 'AUDIT_INPUT_PATHS = (\n'
        '    "docs/F_CUT_Q4_FALSE_SIX_SITE_ZERO_REFUSE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ')' in self_source,
    )
    checks.check(
        "thm1-host",
        "24 rotations, 10 orbits, 32 F_cut maps, 924 six-site seeds",
        len(ROTATIONS) == 24
        and len(set(ROTATIONS)) == 24
        and len(orbit_types) == 10
        and sum(len(orbits[orbit_type]) for orbit_type in orbit_types) == 64
        and len(members) == 32
        and len(free_pairs) == 3
        and len(free_fixed) == 2
        and len(seeds) == 924
        and len(TWO_CUBE) == 12
        and EMPTY_TYPE == axis_type(EMPTY)
        and FULL_TYPE == axis_type(FULL)
        and REMAINING_ORDER == ((1, 0, 2), (0, 1, 2), (2, 0, 1), (3, 0, 0), (1, 1, 1))
        and FZ_REMAINING in remaining_set
        and F1_REMAINING in remaining_set
        and L1_REMAINING in remaining_set,
    )
    checks.check(
        "thm1-name-S",
        "S is the lex-first 6-site seed that f1 fills",
        seed_s == lex_first_any
        and seed_s
        == frozenset(
            ((0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1))
        )
        and len(f1_fillers) == 924
        and "`S = {(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1)}`"
        in note,
    )
    checks.check(
        "thm1-f1-fills-S",
        "f1 fills S and f_z does not",
        f1_fills_s
        and not fz_fills_s
        and "The map `f1` fills `S`" in note_flat,
    )
    checks.check(
        "thm1-first-refuse",
        "first remaining-bit refuse is tick 1, site (1, 1, 0), type adj2",
        tick == 1
        and first_site == (1, 1, 0)
        and first_label == "adj2"
        and first_kind == (2, 0, 1)
        and "tick `1`, site `(1, 1, 0)`, remaining-bit type `adj2`" in note_flat,
    )
    checks.check(
        "thm1-f-L1-is-unbalanced-axis",
        "f_L1 is 1 iff some axis has c_+ != c_-",
        all(
            f_L1(config) == int(axis_type(config)[0] >= 1)
            for config in product((0, 1), repeat=6)
        )
        and computed_l1 == L1_REMAINING
        and l1_remaining == L1_REMAINING,
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
        "thm2-n-refuse",
        "N_refuse=4 on the first tick",
        n_refuse == 4
        and refuse_sites == ((1, 1, 0), (1, 1, 1), (2, 0, 0), (2, 0, 1))
        and refuse_labels[(1, 1, 0)] == "adj2"
        and refuse_labels[(1, 1, 1)] == "adj2"
        and refuse_labels[(2, 0, 0)] == "wt1"
        and refuse_labels[(2, 0, 1)] == "wt1"
        and "`N_refuse = 4`" in note,
    )
    checks.check(
        "thm2-zero-mechanism",
        "f_z is the zero map and locks no new site from S",
        fz_identically_zero
        and not fz_fills_s
        and "f_z` is the zero map" in note
        and "mechanism of this `cov6` zero" in note,
    )
    checks.check(
        "thm3-display-not-adopt",
        "the refuse is displayed and is not adopted as an Admissibility selector",
        "Displayed, not adopted" in note
        and "Do not adopt a bit" in note
        and "Do not write `adj2` or `f_z` into Admissibility" in note
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
        "On the two-cube with off-patch o=0, the first remaining-bit refuse "
        "of F_cut (0,0,0,0,0) on the lex-first 6-site seed f1 fills is "
        "reported. Displayed, not adopted."
    )
    checks.check(
        "claim-scope",
        "claim_scope reports the first remaining-bit refuse and does not adopt a bit",
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
        and "Do not write `adj2` or `f_z` into Admissibility" in note,
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
        "not-leftover-6526",
        "the residual is the first remaining-bit refuse, not leftover-character of #6526",
        "Not leftover-character of #6526" in note
        and "Mechanism of the `cov6` zeros" in note_flat,
    )

    print("per_element: checked exactly — each of the 64 neighbor 6-tuples is assigned its axis-type orbit")
    print("per_site: checked exactly — each of the twelve two-cube vertices uses the same six-direction stencil")
    print("per_mode: checked exactly — f_z is scored on the lex-first 6-site f1 fill")
    print("per_block: checked exactly — first refuse and N_refuse are the remaining-bit refuse facts on this patch")
    print("lattice_wide: checked and not executed — no Z^3-wide formation law or physical Admissibility selector is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
