#!/usr/bin/env python3
"""Search displayed 5-bit remaining-bit predicates Q with cov3>0 iff Q.

F_cut is the cube-covariant class with f(empty)=f(full)=0 and f(c)=f(1-c).
Dynamics are occupancy-to-lock on the twelve-vertex two-cube with off-patch
occupancy 0. Coverage cov3(f) is the number of unordered 3-site seeds from
which f fills. The search is the last remaining-bit width for cov3>0 after
p3bit4 (no 4-bit AND/OR): Q_and5 is the AND of all five remaining bits and
Q_or5 is the OR of all five remaining bits. f_L1 is the unbalanced-axis
predicate (some n_mu != 0), never Hamming |c|_1 mod 2. No candidate is
adopted.
"""

from __future__ import annotations

from itertools import combinations, permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/F_CUT_COV3_FIVE_BIT_SELECTOR_SEARCH_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/F_CUT_COV3_FIVE_BIT_SELECTOR_SEARCH_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
THREE_SITE_SEEDS: tuple[frozenset[Site], ...] = tuple(
    frozenset(triple) for triple in combinations(TWO_CUBE, 3)
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
EXPECTED_N_POS = 20
EXPECTED_P_N_BOTH = 13


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


SEED_MASKS: tuple[int, ...] = tuple(seed_mask(seed) for seed in THREE_SITE_SEEDS)


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


def coverage3(remaining: Remaining) -> int:
    fire = fire_table(remaining)
    return sum(1 for mask in SEED_MASKS if fills_from_mask(fire, mask))


def predicate_P(remaining: Remaining) -> bool:
    wt1, _opp2, adj2, vertex3, mixed3 = remaining
    return wt1 == 1 and (adj2, vertex3, mixed3) != (0, 0, 0)


def predicate_Q4(remaining: Remaining) -> bool:
    return remaining[0] == 1 or remaining[2] == 1


def predicate_Q1(remaining: Remaining) -> bool:
    return remaining[0] == 1 and remaining[2] == 1


def predicate_Q_and5(remaining: Remaining) -> bool:
    return all(bit == 1 for bit in remaining)


def predicate_Q_or5(remaining: Remaining) -> bool:
    return any(bit == 1 for bit in remaining)


def _and_bits(*indices: int):
    return lambda rem, indices=indices: all(rem[i] == 1 for i in indices)


def _or_bits(*indices: int):
    return lambda rem, indices=indices: any(rem[i] == 1 for i in indices)


QUAD_INDICES: tuple[tuple[int, ...], ...] = tuple(combinations(range(5), 4))

CANDIDATES: tuple[tuple[str, object], ...] = (
    ("Q_and5", predicate_Q_and5),
    ("Q_or5", predicate_Q_or5),
)

FOUR_BIT_LEFTOVER_CANDIDATES: tuple[tuple[str, object], ...] = tuple(
    [
        (
            " AND ".join(REMAINING_LABELS[i] for i in quad),
            _and_bits(*quad),
        )
        for quad in QUAD_INDICES
    ]
    + [
        (
            " OR ".join(REMAINING_LABELS[i] for i in quad),
            _or_bits(*quad),
        )
        for quad in QUAD_INDICES
    ]
)


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


def enumerate_f_cut_remaining() -> list[Remaining]:
    return [tuple(bits) for bits in product((0, 1), repeat=5)]  # type: ignore[misc]


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


def score_candidate(
    name: str,
    predicate,
    rows: list[tuple[Remaining, int, int]],
) -> dict[str, object]:
    flags = [int(bool(predicate(remaining))) for remaining, _cov, _pos in rows]
    n_q = sum(flags)
    n_pos = sum(pos for _remaining, _cov, pos in rows)
    n_both = sum(flag and pos for flag, (_remaining, _cov, pos) in zip(flags, rows))
    iff = all(flag == pos for flag, (_remaining, _cov, pos) in zip(flags, rows))
    return {
        "name": name,
        "N_Q": n_q,
        "N_pos": n_pos,
        "N_both": n_both,
        "iff": iff,
    }


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    self_source = Path(__file__).read_text(encoding="utf-8")
    note_flat = normalize(note)

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")

    orbits = build_orbits()
    orbit_types = tuple(sorted(orbits))
    orbit_sizes = {orbit_type: len(orbits[orbit_type]) for orbit_type in orbit_types}
    empty_type = axis_type(EMPTY)
    full_type = axis_type(FULL)
    free_pairs, free_fixed = f_cut_free_data(orbit_types, empty_type, full_type)
    n_free = len(free_pairs) + len(free_fixed)
    n_cut = 1 << n_free
    members = enumerate_f_cut_remaining()

    rows: list[tuple[Remaining, int, int]] = []
    for remaining in members:
        cov = coverage3(remaining)
        rows.append((remaining, cov, int(cov > 0)))
        print(f"remaining={remaining} cov3={cov} pos={int(cov > 0)}")

    n_pos = sum(pos for _remaining, _cov, pos in rows)
    n_p = sum(1 for remaining, _cov, _pos in rows if predicate_P(remaining))
    n_both_p = sum(
        1 for remaining, _cov, pos in rows if predicate_P(remaining) and pos
    )
    p_iff = all(int(predicate_P(remaining)) == pos for remaining, _cov, pos in rows)

    scored = [score_candidate(name, pred, rows) for name, pred in CANDIDATES]
    leftover = [
        score_candidate(name, pred, rows) for name, pred in FOUR_BIT_LEFTOVER_CANDIDATES
    ]
    matches = [item["name"] for item in scored if item["iff"]]
    leftover_matches = [item["name"] for item in leftover if item["iff"]]
    l1_bits = bits_from_predicate(f_L1, orbit_types, orbits)
    ham_bits = bits_from_predicate(f_hamming, orbit_types, orbits)
    l1_remaining = remaining_bits_from_full(l1_bits, orbit_types)
    cov_l1 = next(cov for remaining, cov, _pos in rows if remaining == l1_remaining)

    print(f"n_rotations={len(ROTATIONS)}")
    print(f"n_orbits={len(orbit_types)}")
    print(f"remaining_labels={REMAINING_LABELS}")
    print(f"N_free={n_free}")
    print(f"|F_cut|={n_cut}")
    print(f"n_three_site_seeds={len(THREE_SITE_SEEDS)}")
    print(f"N_pos={n_pos}")
    print(f"N_P={n_p}")
    print(f"N_both_P={n_both_p}")
    print(f"P_iff_pos={p_iff}")
    print(f"f_L1_remaining={l1_remaining}")
    print(f"cov3_f_L1={cov_l1}")
    print(f"n_candidates={len(scored)}")
    for item in scored:
        print(
            "Q={name} N_Q={N_Q} N_pos={N_pos} N_both={N_both} iff={iff}".format(
                **item
            )
        )
    print(f"matching_Q={matches}")
    print(f"leftover_p3bit4_matches={leftover_matches}")

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required note-plus-axiom string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/F_CUT_COV3_FIVE_BIT_SELECTOR_SEARCH_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and 'AUDIT_INPUT_PATHS = (\n'
        '    "docs/F_CUT_COV3_FIVE_BIT_SELECTOR_SEARCH_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
        and len(members) == 32
        and len(free_pairs) == 3
        and len(free_fixed) == 2
        and empty_type == (0, 0, 3)
        and full_type == (0, 3, 0)
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
        and in_f_cut(l1_bits, orbit_types, empty_type, full_type),
    )
    checks.check(
        "thm1-f-L1-not-hamming",
        "f_L1 is not Hamming |c|_1 mod 2",
        l1_bits != ham_bits
        and any(f_L1(config) != f_hamming(config) for config in product((0, 1), repeat=6))
        and "sum(config) % 2"
        not in self_source.split("def f_L1", 1)[1].split("def f_hamming", 1)[0],
    )
    checks.check(
        "thm1-two-cube-and-three-site-seeds",
        "the two-cube has twelve vertices and C(12,3)=220 three-site seeds",
        len(TWO_CUBE) == 12
        and len(set(TWO_CUBE)) == 12
        and len(THREE_SITE_SEEDS) == 220
        and len(set(THREE_SITE_SEEDS)) == 220
        and all(seed <= set(TWO_CUBE) and len(seed) == 3 for seed in THREE_SITE_SEEDS),
    )
    expected_scores = {
        "Q_and5": (1, 20, 1, False),
        "Q_or5": (31, 20, 20, False),
    }
    computed_scores = {
        item["name"]: (item["N_Q"], item["N_pos"], item["N_both"], item["iff"])
        for item in scored
    }
    checks.check(
        "thm1-each-candidate-iff",
        "for Q_and5 and Q_or5, cov3>0 iff Q is decided and both fail",
        list(item["name"] for item in scored) == list(expected_scores)
        and computed_scores == expected_scores
        and n_pos == EXPECTED_N_POS
        and all(item["N_pos"] == EXPECTED_N_POS for item in scored)
        and not any(item["iff"] for item in scored)
        and len(scored) == 2
        and matches == [],
    )
    leftover_expected = {
        "wt1 AND opp2 AND adj2 AND vertex3": (2, 20, 2, False),
        "wt1 AND opp2 AND adj2 AND mixed3": (2, 20, 2, False),
        "wt1 AND opp2 AND vertex3 AND mixed3": (2, 20, 2, False),
        "wt1 AND adj2 AND vertex3 AND mixed3": (2, 20, 2, False),
        "opp2 AND adj2 AND vertex3 AND mixed3": (2, 20, 2, False),
        "wt1 OR opp2 OR adj2 OR vertex3": (30, 20, 20, False),
        "wt1 OR opp2 OR adj2 OR mixed3": (30, 20, 20, False),
        "wt1 OR opp2 OR vertex3 OR mixed3": (30, 20, 20, False),
        "wt1 OR adj2 OR vertex3 OR mixed3": (30, 20, 20, False),
        "opp2 OR adj2 OR vertex3 OR mixed3": (30, 20, 20, False),
    }
    leftover_computed = {
        item["name"]: (item["N_Q"], item["N_pos"], item["N_both"], item["iff"])
        for item in leftover
    }
    checks.check(
        "thm1-reconfirm-p3bit4-four-bit-menu",
        "reconfirm p3bit4: no 4-bit remaining-bit AND or OR equals cov3>0",
        leftover_computed == leftover_expected
        and leftover_matches == []
        and n_pos == EXPECTED_N_POS
        and n_p == 14
        and n_both_p == EXPECTED_P_N_BOTH
        and not p_iff
        and "no 4-bit AND/OR" in note
        and "p3bit4" in note,
    )
    checks.check(
        "thm2-counts-and-none",
        "each displayed Q reports N_Q, N_pos, N_both, and none match",
        matches == []
        and all(
            item["N_Q"] != item["N_pos"] or item["N_both"] != item["N_pos"]
            for item in scored
        )
        and all(item["N_pos"] == EXPECTED_N_POS for item in scored)
        and all(f"N_Q = {item['N_Q']}" in note for item in scored)
        and all(f"N_both = {item['N_both']}" in note or str(item["N_both"]) in note for item in scored)
        and "none" in note_flat
        and "no displayed 5-bit remaining-bit AND or OR equals" in note_flat,
    )
    checks.check(
        "thm3-displayed-not-adopted",
        "the search is displayed and no remaining bit is adopted",
        "Displayed, not adopted" in note
        and "Do not adopt a bit" in note
        and "Do not write the search into Admissibility" in note
        and "not a Max(3) rename" in note,
    )
    checks.check(
        "lattice-and-admissibility-parents",
        "the live axiom memo supplies Z^3, proper cubic rotations, and a covariant nearest-neighbor rule",
        "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
        in axiom
        and "proper cubic rotations about each site." in axiom
        and "one fixed nearest-neighbor admissibility rule, covariant under lattice"
        in axiom
        and "A site with no record cannot be read." in axiom,
    )
    checks.check(
        "note-contract",
        "bounded theorem, displayed-not-adopted selector search, and machine status",
        "**Type:** bounded_theorem" in note
        and "actual_current_surface_status: bounded-support" in note
        and "Displayed, not adopted" in note
        and 'hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"'
        in note,
    )
    checks.check(
        "claim-type-and-gate",
        "N1-N8 and a passing no-go disposition are source-visible",
        all(f"### N{index}" in note for index in range(1, 9))
        and "No-Go Discipline disposition: **PASS**" in note
        and note.count("**ATTEMPTED**") == 6
        and ("import " + "qcd") not in self_source.lower(),
    )
    forbidden = ("G_" + "N", "1/" + "r", "1/" + "r^2", "Lattice-" + "named", "not a " + "TOE")
    checks.check(
        "forbidden-phrases-absent",
        "the note and runner omit the dispatch-forbidden phrases",
        all(phrase not in note and phrase not in self_source for phrase in forbidden),
    )
    checks.check(
        "l1-definition-in-note",
        "the note defines f_L1 as unbalanced-axis / n != 0 and rejects Hamming",
        "`f_L1(c)=1` if and only if some axis is unbalanced" in note_flat
        and "`n_μ = c_{+μ} − c_{-μ}` is nonzero" in note
        and "This is **not** Hamming parity" in note,
    )
    checks.check(
        "note-reports-search",
        "the note reports Q_and5, Q_or5, N_pos=20, and the none verdict",
        "(wt1, opp2, adj2, vertex3, mixed3)" in note
        and "Q_and5" in note
        and "Q_or5" in note
        and "wt1 AND opp2 AND adj2 AND vertex3 AND mixed3" in note
        and "wt1 OR opp2 OR adj2 OR vertex3 OR mixed3" in note
        and "N_pos = 20" in note
        and "none" in note
        and all(f"N_Q = {item['N_Q']}" in note for item in scored),
    )
    checks.check(
        "no-axiom-edit",
        "the theorem proposes no axiom change",
        "no axiom or approved primitive is added" in note
        and "hypothetical_axiom_status" in note
        and "Do not write the search into Admissibility" in note,
    )
    checks.check(
        "off-patch-zero",
        "off-patch occupancy is the explicit 0 default, not a blank-block",
        "off-patch occupancy `0`" in note and "blank-block is a different rule" in note,
    )
    checks.check(
        "last-remaining-bit-width-not-max3",
        "the residual is the last remaining-bit width for cov3>0, not a Max(3) rename",
        "Last remaining-bit width for cov3>0" in note
        and "not a Max(3) rename" in note
        and "no 4-bit AND/OR" in note
        and "p3bit4" in note,
    )
    checks.check(
        "claim-scope-search",
        "claim_scope reports whether the 5-bit remaining-bit AND or OR equals cov3>0",
        "Among the 32 F_cut maps on the two-cube" in note
        and "off-patch o=0" in note
        and "whether the 5-bit remaining-bit AND or the 5-bit OR equals cov3>0 is reported"
        in note
        and "Displayed, not adopted" in note,
    )

    print("per_element: checked exactly — each of the 64 neighbor 6-tuples is assigned its axis-type orbit")
    print("per_site: checked exactly — each of the twelve two-cube vertices uses the same six-direction stencil")
    print("per_mode: checked exactly — every F_cut map is scored by whether any of the 220 three-site seeds fills")
    print("per_block: checked exactly — Q_and5 and Q_or5 are each tested for cov3>0 iff Q")
    print("lattice_wide: checked and not executed — no Z^3-wide formation law or physical Admissibility selector is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
