#!/usr/bin/env python3
"""Whether cov6>0 equals Q6, and whether any 1-bit or wt1-AND-bit does.

F_cut is the cube-covariant class with f(empty)=f(full)=0 and f(c)=f(1-c).
Dynamics are occupancy-to-lock on the twelve-vertex two-cube with off-patch
occupancy 0. Coverage cov6(f) is the number of six-site seeds from which f
fills. Q6 is the displayed remaining-bit predicate
(wt1=1) or (adj2=1) or (vertex3=1). The runner reports whether positivity
equals Q6, one lex-first counterexample if not, whether any 1-bit or
wt1-AND-bit equals cov6>0, and the counts N_Q6, N_pos, N_both. It does
not adopt a bit. f_L1 is the unbalanced-axis predicate (some n_mu != 0),
never Hamming |c|_1 mod 2.
"""

from __future__ import annotations

from itertools import combinations, permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/F_CUT_COV6_POSITIVE_SELECTOR_SEARCH_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/F_CUT_COV6_POSITIVE_SELECTOR_SEARCH_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
ZEROS: tuple[Remaining, ...] = (
    (0, 0, 0, 0, 0),
    (0, 0, 0, 0, 1),
    (0, 1, 0, 0, 0),
    (0, 1, 0, 0, 1),
)
EXTRAS_Q4: tuple[Remaining, ...] = (
    (0, 0, 0, 1, 0),
    (0, 0, 0, 1, 1),
    (0, 1, 0, 1, 0),
    (0, 1, 0, 1, 1),
)
EXTRA_COV6: dict[Remaining, int] = {
    (0, 0, 0, 1, 0): 4,
    (0, 0, 0, 1, 1): 12,
    (0, 1, 0, 1, 0): 20,
    (0, 1, 0, 1, 1): 28,
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


def selector_Q6(remaining: Remaining) -> bool:
    return remaining[0] == 1 or remaining[2] == 1 or remaining[3] == 1


def selector_Q4(remaining: Remaining) -> bool:
    return remaining[0] == 1 or remaining[2] == 1


def candidate_menu() -> list[tuple[str, object]]:
    bits = [
        (label, (lambda rem, index=index: rem[index] == 1))
        for index, label in enumerate(REMAINING_LABELS)
    ]
    ands = [
        (f"wt1 AND {label}", (lambda rem, index=index: rem[0] == 1 and rem[index] == 1))
        for index, label in enumerate(REMAINING_LABELS)
        if index != 0
    ]
    return bits + ands + [("Q6", selector_Q6)]


def score_candidate(rows: list[tuple[Remaining, int]], predicate) -> dict[str, int]:
    tp = tn = fp = fn = 0
    for remaining, cov in rows:
        q = bool(predicate(remaining))
        pos = cov > 0
        if pos and q:
            tp += 1
        elif (not pos) and (not q):
            tn += 1
        elif (not pos) and q:
            fp += 1
        else:
            fn += 1
    return {"tp": tp, "tn": tn, "fp": fp, "fn": fn, "equiv": int(fp == 0 and fn == 0)}


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
        "negative_scope: displayed Q6 and 1-bit / wt1-AND menu versus cov6>0; "
        "does not adopt a bit"
    )

    orbits = build_orbits()
    orbit_types = tuple(sorted(orbits))
    type_of = {config: orbit_type for orbit_type, group in orbits.items() for config in group}
    free_pairs, free_fixed = f_cut_free_data(orbit_types, EMPTY_TYPE, FULL_TYPE)
    members = enumerate_f_cut(orbit_types, EMPTY_TYPE, FULL_TYPE)
    neighbors = neighbor_indices()
    seeds = seed_masks_for(6)
    rows: list[tuple[Remaining, int]] = []
    for bits, remaining in members:
        table = predicate_table(bits, orbit_types, type_of)
        cov = coverage_from_masks(table, seeds, neighbors)
        rows.append((remaining, cov))

    scores = {name: score_candidate(rows, pred) for name, pred in candidate_menu()}
    n_q6 = sum(1 for remaining, _cov in rows if selector_Q6(remaining))
    n_pos = sum(1 for _remaining, cov in rows if cov > 0)
    n_both = sum(1 for remaining, cov in rows if cov > 0 and selector_Q6(remaining))
    mismatches = [
        (remaining, cov)
        for remaining, cov in rows
        if selector_Q6(remaining) != (cov > 0)
    ]
    q4_extras = frozenset(
        remaining
        for remaining, cov in rows
        if cov > 0 and not selector_Q4(remaining)
    )
    zero_set = frozenset(remaining for remaining, cov in rows if cov == 0)
    lex_first = min(mismatches, key=lambda row: row[0]) if mismatches else None
    cov_by_remaining = {remaining: cov for remaining, cov in rows}
    cov_l1 = cov_by_remaining[L1_REMAINING]
    extra_cov = {remaining: cov_by_remaining[remaining] for remaining in EXTRAS_Q4}
    matching = [name for name, score in scores.items() if score["equiv"] == 1]
    and_names = [f"wt1 AND {label}" for label in REMAINING_LABELS if label != "wt1"]

    print(f"n_rotations={len(ROTATIONS)}")
    print(f"n_orbits={len(orbit_types)}")
    print(f"remaining_labels={REMAINING_LABELS}")
    print(f"|F_cut|={len(members)}")
    print(f"n_six_site_seeds={len(seeds)}")
    print(f"N_Q6={n_q6}")
    print(f"N_pos={n_pos}")
    print(f"N_both={n_both}")
    print(f"N_mismatch={len(mismatches)}")
    print(f"cov6(f_L1)={cov_l1}")
    print(f"lex_first_counterexample={None if lex_first is None else lex_first[0]}")
    print(f"equiv={int(len(mismatches) == 0)}")
    print(f"matching_candidates={matching}")
    for name, score in scores.items():
        print(
            f"candidate {name}: equiv={score['equiv']} "
            f"tp={score['tp']} tn={score['tn']} fp={score['fp']} fn={score['fn']}"
        )

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required note-plus-axiom string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/F_CUT_COV6_POSITIVE_SELECTOR_SEARCH_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and AUDIT_TIMEOUT_SEC == 120
        and 'AUDIT_INPUT_PATHS = (\n'
        '    "docs/F_CUT_COV6_POSITIVE_SELECTOR_SEARCH_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
        and REMAINING_ORDER == ((1, 0, 2), (0, 1, 2), (2, 0, 1), (3, 0, 0), (1, 1, 1)),
    )
    checks.check(
        "thm1-f-L1-is-unbalanced-axis",
        "f_L1 is 1 iff some axis has c_+ != c_-",
        all(
            f_L1(config) == int(axis_type(config)[0] >= 1)
            for config in product((0, 1), repeat=6)
        )
        and selector_Q6(L1_REMAINING)
        and cov_l1 == 920,
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
        "thm1-q6-equivalent",
        "cov6>0 is equivalent to Q6 among the 32 F_cut maps",
        len(mismatches) == 0
        and lex_first is None
        and scores["Q6"] == {"tp": 28, "tn": 4, "fp": 0, "fn": 0, "equiv": 1}
        and all(selector_Q6(remaining) == (cov > 0) for remaining, cov in rows)
        and zero_set == frozenset(ZEROS)
        and q4_extras == frozenset(EXTRAS_Q4)
        and extra_cov == EXTRA_COV6
        and all(not selector_Q4(remaining) and remaining[3] == 1 for remaining in EXTRAS_Q4)
        and "if and only if `Q6(f)`" in note_flat
        and "There is no counterexample" in note,
    )
    checks.check(
        "thm1-no-1-bit",
        "no standalone remaining bit equals cov6>0",
        all(scores[label]["equiv"] == 0 for label in REMAINING_LABELS)
        and scores["wt1"]["fn"] == 12
        and scores["adj2"]["fn"] == 12
        and scores["vertex3"]["fn"] == 12
        and scores["opp2"]["fp"] == 2
        and scores["mixed3"]["fp"] == 2
        and "No standalone remaining bit equals" in note,
    )
    checks.check(
        "thm1-no-wt1-and-bit",
        "no wt1 AND other remaining bit equals cov6>0",
        all(scores[name]["equiv"] == 0 for name in and_names)
        and all(scores[name]["fn"] == 20 for name in and_names)
        and matching == ["Q6"]
        and "No `wt1` AND other remaining bit equals" in note,
    )
    checks.check(
        "thm2-counts",
        f"N_Q6={n_q6}, N_pos={n_pos}, N_both={n_both}",
        n_q6 == 28
        and n_pos == 28
        and n_both == 28
        and n_q6 == n_pos == n_both
        and f"N_Q6 = {n_q6}" in note
        and f"N_pos = {n_pos}" in note
        and f"N_both = {n_both}" in note,
    )
    checks.check(
        "thm3-display-not-adopt",
        "Q6 is displayed and no bit is adopted as an Admissibility selector",
        (
            "Q6(f) := (wt1 = 1) or (adj2 = 1) or (vertex3 = 1)" in note
            or "Q6(f) := (wt1=1) or (adj2=1) or (vertex3=1)" in note
        )
        and "Displayed, not adopted" in note
        and "Do not adopt a bit" in note
        and "Do not adopt `Q6`" in note
        and "Do not write `Q6` into Admissibility" in note
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
        "Among the 32 F_cut maps on the two-cube with off-patch o=0, whether "
        "positive 6-site coverage is equivalent to (wt1=1) or (adj2=1) or "
        "(vertex3=1) is reported. Displayed, not adopted."
    )
    checks.check(
        "claim-scope",
        "claim_scope reports the 6-site positivity-versus-Q6 comparison and does not adopt a bit",
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
        and "Do not write `Q6` into Admissibility" in note,
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
        "the residual is 6-site positivity versus Q6, not leftover-character of #6526",
        "Not leftover-character of #6526" in note
        and "New k-selector after `Q4` failed at `k=6`" in note
        and "N_Q4 = 24" in note
        and "N_pos = 28" in note,
    )
    checks.check(
        "q6-definition-and-l1-in-class",
        "Q6 is (wt1=1) or (adj2=1) or (vertex3=1) and f_L1 satisfies Q6",
        selector_Q6((1, 0, 1, 1, 1))
        and selector_Q6((1, 0, 0, 0, 0))
        and selector_Q6((0, 0, 1, 0, 0))
        and selector_Q6((0, 0, 0, 1, 0))
        and not selector_Q6((0, 0, 0, 0, 0))
        and not selector_Q6((0, 1, 0, 0, 1))
        and cov_l1 == cov_by_remaining[(1, 0, 1, 1, 1)],
    )

    print("per_element: checked exactly — each of the 64 neighbor 6-tuples is assigned its axis-type orbit")
    print("per_site: checked exactly — each of the twelve two-cube vertices uses the same six-direction stencil")
    print("per_mode: checked exactly — every F_cut map is scored on 924 six-site seeds against displayed Q6 and the 1-bit / wt1-AND menu")
    print("per_block: checked exactly — N_Q6, N_pos, and N_both are the F_cut positivity-versus-Q6 counts on this patch")
    print("lattice_wide: checked and not executed — no Z^3-wide formation law or physical Admissibility selector is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
