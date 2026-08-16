#!/usr/bin/env python3
"""Search 3-bit remaining-bit candidates for cov3=220 on the 32 F_cut maps.

F_cut is the cube-covariant class with f(empty)=f(full)=0 and f(c)=f(1-c).
Dynamics are occupancy-to-lock on the twelve-vertex two-cube with off-patch
occupancy 0. Coverage cov3(f) is the number of three-site seeds from which f
fills. Max(3) is the pair of maps with cov3=220. Candidates are every 3-bit
AND and every 3-bit OR of {wt1, opp2, adj2, vertex3, mixed3}. If none
matches, one lex-first miss of each is reported. The runner does not adopt
a bit. f_L1 is the unbalanced-axis predicate (some n_mu != 0), never
Hamming |c|_1 mod 2. q3v3m3 is a Q_* restriction, not a 32-wide 3-bit.
"""

from __future__ import annotations

from itertools import combinations, permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/F_CUT_COV3_MAX_THREE_BIT_SELECTOR_SEARCH_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/F_CUT_COV3_MAX_THREE_BIT_SELECTOR_SEARCH_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
EXPECTED_N_MAX = 2
COV3_MAX = 220
TRIPLE_INDICES: tuple[tuple[int, int, int], ...] = tuple(combinations(range(5), 3))


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
THREE_SITE_SEEDS: tuple[frozenset[Site], ...] = tuple(
    frozenset(triple) for triple in combinations(TWO_CUBE, 3)
)


def seed_mask(seed: frozenset[Site]) -> int:
    mask = 0
    for site in seed:
        mask |= 1 << SITE_INDEX[site]
    return mask


SEED_MASKS: tuple[int, ...] = tuple(seed_mask(seed) for seed in THREE_SITE_SEEDS)


def fire_table(remaining: Remaining) -> tuple[int, ...]:
    table = [0] * 64
    for raw in product((0, 1), repeat=6):
        index = (
            raw[0]
            | (raw[1] << 1)
            | (raw[2] << 2)
            | (raw[3] << 3)
            | (raw[4] << 4)
            | (raw[5] << 5)
        )
        table[index] = remaining_value(raw, remaining)
    return tuple(table)


def fills_from_mask(fire: tuple[int, ...], start: int) -> bool:
    locked = start
    full_mask = (1 << 12) - 1
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
            return locked == full_mask
        locked = nxt
    return False


def coverage3(remaining: Remaining) -> int:
    fire = fire_table(remaining)
    return sum(1 for mask in SEED_MASKS if fills_from_mask(fire, mask))


def candidate_menu() -> list[tuple[str, object]]:
    ands = [
        (
            " AND ".join(REMAINING_LABELS[i] for i in triple),
            (lambda rem, triple=triple: all(rem[i] == 1 for i in triple)),
        )
        for triple in TRIPLE_INDICES
    ]
    ors = [
        (
            " OR ".join(REMAINING_LABELS[i] for i in triple),
            (lambda rem, triple=triple: any(rem[i] == 1 for i in triple)),
        )
        for triple in TRIPLE_INDICES
    ]
    return ands + ors


def score_candidate(
    rows: list[tuple[Remaining, int]],
    predicate,
) -> dict:
    tp = tn = fp = fn = 0
    misses: list[tuple[Remaining, int, bool]] = []
    for remaining, cov in rows:
        q = bool(predicate(remaining))
        pos = cov == COV3_MAX
        if pos and q:
            tp += 1
        elif (not pos) and (not q):
            tn += 1
        elif (not pos) and q:
            fp += 1
            misses.append((remaining, cov, q))
        else:
            fn += 1
            misses.append((remaining, cov, q))
    lex = min(misses, key=lambda row: row[0]) if misses else None
    return {
        "tp": tp,
        "tn": tn,
        "fp": fp,
        "fn": fn,
        "equiv": int(fp == 0 and fn == 0),
        "N_Q": tp + fp,
        "N_both": tp,
        "lex": lex,
    }


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
        "negative_scope: displayed 3-bit remaining-bit candidates versus "
        "cov3=220; does not adopt a bit"
    )

    orbits = build_orbits()
    orbit_types = tuple(sorted(orbits))
    free_pairs, free_fixed = f_cut_free_data(orbit_types, EMPTY_TYPE, FULL_TYPE)
    members = [tuple(bits) for bits in product((0, 1), repeat=5)]
    rows: list[tuple[Remaining, int]] = []
    for remaining in members:
        remaining_bits: Remaining = remaining  # type: ignore[assignment]
        cov = coverage3(remaining_bits)
        rows.append((remaining_bits, cov))
        print(f"remaining={remaining_bits} cov3={cov} max={int(cov == COV3_MAX)}")

    scores = {name: score_candidate(rows, pred) for name, pred in candidate_menu()}
    matching = [name for name, score in scores.items() if score["equiv"] == 1]
    n_max = sum(1 for _remaining, cov in rows if cov == COV3_MAX)
    maximizers = [remaining for remaining, cov in rows if cov == COV3_MAX]
    cov_by_remaining = {remaining: cov for remaining, cov in rows}
    cov_l1 = cov_by_remaining[L1_REMAINING]
    cov_f1 = cov_by_remaining[F1_REMAINING]
    and_names = [" AND ".join(REMAINING_LABELS[i] for i in triple) for triple in TRIPLE_INDICES]
    or_names = [" OR ".join(REMAINING_LABELS[i] for i in triple) for triple in TRIPLE_INDICES]

    print(f"n_rotations={len(ROTATIONS)}")
    print(f"n_orbits={len(orbit_types)}")
    print(f"remaining_labels={REMAINING_LABELS}")
    print(f"|F_cut|={len(members)}")
    print(f"n_three_site_seeds={len(THREE_SITE_SEEDS)}")
    print(f"N_max={n_max}")
    print(f"maximizers={maximizers}")
    print(f"cov3(f_L1)={cov_l1}")
    print(f"cov3(f1)={cov_f1}")
    print(f"n_candidates={len(scores)}")
    print(f"matching_candidates={matching}")
    for name, score in scores.items():
        lex = score["lex"]
        print(
            f"candidate {name}: equiv={score['equiv']} N_Q={score['N_Q']} "
            f"N_both={score['N_both']} fp={score['fp']} fn={score['fn']} "
            f"lex={None if lex is None else lex[0]}"
        )

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required note-plus-axiom string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/F_CUT_COV3_MAX_THREE_BIT_SELECTOR_SEARCH_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and AUDIT_TIMEOUT_SEC == 120
        and 'AUDIT_INPUT_PATHS = (\n'
        '    "docs/F_CUT_COV3_MAX_THREE_BIT_SELECTOR_SEARCH_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ')' in self_source,
    )
    checks.check(
        "thm1-host",
        "24 rotations, 10 orbits, 32 F_cut maps, 220 three-site seeds",
        len(ROTATIONS) == 24
        and len(set(ROTATIONS)) == 24
        and len(orbit_types) == 10
        and sum(len(orbits[orbit_type]) for orbit_type in orbit_types) == 64
        and len(members) == 32
        and len(free_pairs) == 3
        and len(free_fixed) == 2
        and len(THREE_SITE_SEEDS) == 220
        and len(set(THREE_SITE_SEEDS)) == 220
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
        and cov_l1 == COV3_MAX
        and L1_REMAINING in cov_by_remaining,
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
    and_fail = all(scores[name]["equiv"] == 0 for name in and_names)
    or_fail = all(scores[name]["equiv"] == 0 for name in or_names)
    checks.check(
        "thm1-three-bit-and-or-fail",
        "no displayed 3-bit AND or 3-bit OR equals cov3=220",
        and_fail
        and or_fail
        and matching == []
        and len(and_names) == 10
        and len(or_names) == 10
        and all(scores[name]["N_Q"] == 4 for name in and_names)
        and all(scores[name]["N_Q"] == 28 for name in or_names)
        and scores["wt1 AND opp2 AND adj2"]["N_both"] == 1
        and scores["wt1 AND adj2 AND vertex3"]["N_both"] == 2,
    )
    expected_lex = {
        "wt1 AND opp2 AND adj2": ((1, 0, 1, 1, 1), 220, False),
        "wt1 AND opp2 AND vertex3": ((1, 0, 1, 1, 1), 220, False),
        "wt1 AND opp2 AND mixed3": ((1, 0, 1, 1, 1), 220, False),
        "wt1 AND adj2 AND vertex3": ((1, 0, 1, 1, 0), 188, True),
        "wt1 AND adj2 AND mixed3": ((1, 0, 1, 0, 1), 96, True),
        "wt1 AND vertex3 AND mixed3": ((1, 0, 0, 1, 1), 72, True),
        "opp2 AND adj2 AND vertex3": ((0, 1, 1, 1, 0), 44, True),
        "opp2 AND adj2 AND mixed3": ((0, 1, 1, 0, 1), 16, True),
        "opp2 AND vertex3 AND mixed3": ((0, 1, 0, 1, 1), 0, True),
        "adj2 AND vertex3 AND mixed3": ((0, 0, 1, 1, 1), 24, True),
        "wt1 OR opp2 OR adj2": ((0, 0, 1, 0, 0), 0, True),
        "wt1 OR opp2 OR vertex3": ((0, 0, 0, 1, 0), 0, True),
        "wt1 OR opp2 OR mixed3": ((0, 0, 0, 0, 1), 0, True),
        "wt1 OR adj2 OR vertex3": ((0, 0, 0, 1, 0), 0, True),
        "wt1 OR adj2 OR mixed3": ((0, 0, 0, 0, 1), 0, True),
        "wt1 OR vertex3 OR mixed3": ((0, 0, 0, 0, 1), 0, True),
        "opp2 OR adj2 OR vertex3": ((0, 0, 0, 1, 0), 0, True),
        "opp2 OR adj2 OR mixed3": ((0, 0, 0, 0, 1), 0, True),
        "opp2 OR vertex3 OR mixed3": ((0, 0, 0, 0, 1), 0, True),
        "adj2 OR vertex3 OR mixed3": ((0, 0, 0, 0, 1), 0, True),
    }
    computed_lex = {
        name: (score["lex"][0], score["lex"][1], score["lex"][2])
        for name, score in scores.items()
        if score["lex"] is not None
    }
    checks.check(
        "thm1-lex-first-miss-of-each",
        "one lex-first remaining-bit miss is reported for each displayed Q",
        computed_lex == expected_lex
        and all(f"`{name}`" in note for name in expected_lex)
        and "`(1, 0, 1, 1, 1)`" in note
        and "`(0, 0, 1, 1, 1)`" in note
        and "lex-first" in note,
    )
    expected_counts = {
        "wt1 AND opp2 AND adj2": (4, 1),
        "wt1 AND opp2 AND vertex3": (4, 1),
        "wt1 AND opp2 AND mixed3": (4, 1),
        "wt1 AND adj2 AND vertex3": (4, 2),
        "wt1 AND adj2 AND mixed3": (4, 2),
        "wt1 AND vertex3 AND mixed3": (4, 2),
        "opp2 AND adj2 AND vertex3": (4, 1),
        "opp2 AND adj2 AND mixed3": (4, 1),
        "opp2 AND vertex3 AND mixed3": (4, 1),
        "adj2 AND vertex3 AND mixed3": (4, 2),
        "wt1 OR opp2 OR adj2": (28, 2),
        "wt1 OR opp2 OR vertex3": (28, 2),
        "wt1 OR opp2 OR mixed3": (28, 2),
        "wt1 OR adj2 OR vertex3": (28, 2),
        "wt1 OR adj2 OR mixed3": (28, 2),
        "wt1 OR vertex3 OR mixed3": (28, 2),
        "opp2 OR adj2 OR vertex3": (28, 2),
        "opp2 OR adj2 OR mixed3": (28, 2),
        "opp2 OR vertex3 OR mixed3": (28, 2),
        "adj2 OR vertex3 OR mixed3": (28, 2),
    }
    computed_counts = {
        name: (score["N_Q"], score["N_both"]) for name, score in scores.items()
    }
    checks.check(
        "thm2-counts",
        f"N_max={n_max} and each displayed Q reports N_Q and N_both",
        n_max == EXPECTED_N_MAX
        and maximizers == [L1_REMAINING, F1_REMAINING]
        and cov_l1 == COV3_MAX
        and cov_f1 == COV3_MAX
        and computed_counts == expected_counts
        and "N_max = 2" in note
        and "N_Q = 4" in note
        and "N_Q = 28" in note
        and all(str(pair[0]) in note and str(pair[1]) in note for pair in expected_counts.values()),
    )
    checks.check(
        "thm3-display-not-adopt",
        "the menu is displayed and no bit is adopted as an Admissibility selector",
        "Displayed, not adopted" in note
        and "Do not adopt a bit" in note
        and "Do not adopt a 3-bit AND" in note
        and "Do not adopt a 3-bit OR" in note
        and "Do not write a remaining-bit formula into Admissibility" in note
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
        "a displayed 3-bit remaining-bit predicate equals cov3=220 is reported. "
        "Displayed, not adopted."
    )
    checks.check(
        "claim-scope",
        "claim_scope reports the 3-bit remaining-bit search and does not adopt a bit",
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
        and "Do not write a remaining-bit formula into Admissibility" in note,
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
        "not-leftover-first-max3-menu",
        "the residual is the next-width 3-bit menu after the first failed Max(3) menu",
        "Next width after the first failed Max(3) menu" in note
        and "Not leftover-character of the failed 1-bit / 2-bit AND/OR" in note
        and "no 1-bit or 2-bit AND/OR equals" in note
        and "q3v3m3 is the Q_* restriction, not a 32-wide 3-bit" in note,
    )

    print("per_element: checked exactly — each of the 64 neighbor 6-tuples is assigned its axis-type orbit")
    print("per_site: checked exactly — each of the twelve two-cube vertices uses the same six-direction stencil")
    print("per_mode: checked exactly — every F_cut map is scored on 220 three-site seeds against the displayed 3-bit menu")
    print("per_block: checked exactly — N_max and each (N_Q, N_both) are the F_cut Max(3)-versus-Q counts on this patch")
    print("lattice_wide: checked and not executed — no Z^3-wide formation law or physical Admissibility selector is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
