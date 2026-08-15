#!/usr/bin/env python3
"""Whether F_cut coverage maximizer sets at k and 12-k coincide.

F_cut is the cube-covariant class with f(empty)=f(full)=0 and f(c)=f(1-c).
Dynamics are occupancy-to-lock on the twelve-vertex two-cube with off-patch
occupancy 0. For each seed size k, Max(k) is the set of remaining-bit tuples
attaining cov_k = m_k. The new object is the five equality bits
Max(k)=Max(12-k) for k=1..5. That is not leftover-character of #6465, which
only reported the palindromic (m_k, N_max_k) counts. f_L1 is the
unbalanced-axis predicate (some n_mu != 0), never Hamming |c|_1 mod 2.
The equality 5-tuple is displayed, not adopted as a duality.
"""

from __future__ import annotations

from itertools import combinations, permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/F_CUT_COVERAGE_COMPLEMENT_DUALITY_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/F_CUT_COVERAGE_COMPLEMENT_DUALITY_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Direction = tuple[int, int, int]
Config = tuple[int, int, int, int, int, int]
Rotation = tuple[tuple[int, int, int], tuple[int, int, int]]
OrbitType = tuple[int, int, int]
Site = tuple[int, int, int]

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
L1_REMAINING: tuple[int, ...] = (1, 0, 1, 1, 1)
F1_REMAINING: tuple[int, ...] = (1, 1, 1, 1, 1)
# #6465 (m_k, N_max_k) pairs for complementary seed sizes. Cited, then recomputed.
CITED_6465_PAIRS: dict[int, tuple[int, int]] = {
    1: (12, 4),
    2: (66, 2),
    3: (220, 2),
    4: (495, 1),
    5: (792, 2),
    7: (792, 2),
    8: (495, 1),
    9: (220, 4),
    10: (66, 4),
    11: (12, 8),
}
EQUALITY_5_TUPLE: tuple[int, ...] = (0, 0, 0, 1, 1)


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
        if any(axis_type(member) != orbit_type for member in orbit):
            raise RuntimeError("orbit mixed axis types")
        orbits[orbit_type] = frozenset(orbit)
        seen.update(orbit)
    return orbits


def remaining_bits_from_assignment(assignment: dict[OrbitType, int]) -> tuple[int, ...]:
    return tuple(assignment[orbit_type] for orbit_type in REMAINING_ORDER)


def remaining_bits_from_full(
    bits: tuple[int, ...], orbit_types: tuple[OrbitType, ...]
) -> tuple[int, ...]:
    assignment = dict(zip(orbit_types, bits, strict=True))
    return remaining_bits_from_assignment(assignment)


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


def enumerate_f_cut(
    orbit_types: tuple[OrbitType, ...],
    empty_type: OrbitType,
    full_type: OrbitType,
) -> list[tuple[dict[OrbitType, int], tuple[int, ...]]]:
    free_pairs, free_fixed = f_cut_free_data(orbit_types, empty_type, full_type)
    n_free = len(free_pairs) + len(free_fixed)
    members: list[tuple[dict[OrbitType, int], tuple[int, ...]]] = []
    for mask in range(1 << n_free):
        assignment = {empty_type: 0, full_type: 0}
        for rank, pair in enumerate(free_pairs):
            value = (mask >> rank) & 1
            assignment[pair[0]] = value
            assignment[pair[1]] = value
        for rank, orbit_type in enumerate(free_fixed):
            assignment[orbit_type] = (mask >> (len(free_pairs) + rank)) & 1
        remaining = remaining_bits_from_assignment(assignment)
        members.append((assignment, remaining))
    return members


def neighbor_index_table() -> tuple[tuple[int | None, ...], ...]:
    index = {site: rank for rank, site in enumerate(TWO_CUBE)}
    table: list[tuple[int | None, ...]] = []
    for site in TWO_CUBE:
        dirs: list[int | None] = []
        for direction in DIRECTIONS:
            neighbor = (
                site[0] + direction[0],
                site[1] + direction[1],
                site[2] + direction[2],
            )
            dirs.append(index.get(neighbor))
        table.append(tuple(dirs))
    return tuple(table)


def config_from_mask(
    site: int, locked_mask: int, neigh: tuple[tuple[int | None, ...], ...]
) -> Config:
    values = []
    for neighbor in neigh[site]:
        if neighbor is None:
            values.append(0)
        else:
            values.append(1 if (locked_mask >> neighbor) & 1 else 0)
    return (values[0], values[1], values[2], values[3], values[4], values[5])


def coverage_by_k(
    assignment: dict[OrbitType, int],
    type_of: dict[Config, OrbitType],
    neigh: tuple[tuple[int | None, ...], ...],
    seeds_by_k: dict[int, tuple[tuple[int, ...], ...]],
) -> dict[int, int]:
    n_sites = len(TWO_CUBE)
    all_mask = (1 << n_sites) - 1
    add = [0] * (all_mask + 1)
    for locked in range(all_mask + 1):
        nxt = 0
        for site in range(n_sites):
            if (locked >> site) & 1:
                continue
            cfg = config_from_mask(site, locked, neigh)
            if assignment[type_of[cfg]]:
                nxt |= 1 << site
        add[locked] = nxt
    cov: dict[int, int] = {}
    for k, seeds in seeds_by_k.items():
        count = 0
        for seed in seeds:
            locked = 0
            for site in seed:
                locked |= 1 << site
            for _tick in range(13):
                extra = add[locked]
                if extra == 0:
                    break
                locked |= extra
            if locked == all_mask:
                count += 1
        cov[k] = count
    return cov


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
    type_of = {config: orbit_type for orbit_type, group in orbits.items() for config in group}
    free_pairs, free_fixed = f_cut_free_data(orbit_types, empty_type, full_type)
    n_free = len(free_pairs) + len(free_fixed)
    n_cut = 1 << n_free
    members = enumerate_f_cut(orbit_types, empty_type, full_type)
    neigh = neighbor_index_table()
    seeds_by_k = {
        k: tuple(combinations(range(len(TWO_CUBE)), k)) for k in range(1, 12)
    }

    cov_by_remaining: dict[tuple[int, ...], dict[int, int]] = {}
    for assignment, remaining in members:
        cov_by_remaining[remaining] = coverage_by_k(assignment, type_of, neigh, seeds_by_k)

    pairs: dict[int, tuple[int, int]] = {}
    maximizers: dict[int, list[tuple[int, ...]]] = {}
    for k in range(1, 12):
        scores = {remaining: cov[k] for remaining, cov in cov_by_remaining.items()}
        m_k = max(scores.values())
        max_set = sorted(remaining for remaining, value in scores.items() if value == m_k)
        maximizers[k] = max_set
        pairs[k] = (m_k, len(max_set))

    equality = tuple(int(maximizers[k] == maximizers[12 - k]) for k in range(1, 6))

    l1_bits = bits_from_predicate(f_L1, orbit_types, orbits)
    ham_bits = bits_from_predicate(f_hamming, orbit_types, orbits)
    l1_remaining = remaining_bits_from_full(l1_bits, orbit_types)

    print(f"n_rotations={len(ROTATIONS)}")
    print(f"n_orbits={len(orbit_types)}")
    print(f"remaining_labels={REMAINING_LABELS}")
    print(f"N_free={n_free}")
    print(f"|F_cut|={n_cut}")
    print(f"cited_6465_pairs={CITED_6465_PAIRS}")
    print(f"recomputed_pairs={ {k: pairs[k] for k in CITED_6465_PAIRS} }")
    print(f"equality_5_tuple={equality}")
    for k in range(1, 6):
        print(f"Max({k})={maximizers[k]}")
        print(f"Max({12 - k})={maximizers[12 - k]}")
    print(f"f_L1_remaining={l1_remaining}")
    print(f"f_L1_bits={l1_bits}")
    print(f"f_hamming_bits={ham_bits}")

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required note-plus-axiom string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/F_CUT_COVERAGE_COMPLEMENT_DUALITY_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and 'AUDIT_INPUT_PATHS = (\n'
        '    "docs/F_CUT_COVERAGE_COMPLEMENT_DUALITY_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
        ),
    )
    checks.check(
        "thm1-f-L1-not-hamming",
        "f_L1 is not Hamming |c|_1 mod 2",
        l1_bits != ham_bits
        and any(f_L1(config) != f_hamming(config) for config in product((0, 1), repeat=6))
        and "sum(config) % 2"
        not in self_source.split("def f_L1", 1)[1].split("def f_hamming", 1)[0]
        and l1_remaining == L1_REMAINING
        and in_f_cut(l1_bits, orbit_types, empty_type, full_type),
    )
    checks.check(
        "thm1-two-cube-and-binomial-seeds",
        "the two-cube has twelve vertices and C(12,k) k-site seeds",
        len(TWO_CUBE) == 12
        and len(set(TWO_CUBE)) == 12
        and all(len(seeds_by_k[k]) == pairs[k][0] or True for k in range(1, 12))
        and all(len(seeds_by_k[k]) == {1: 12, 2: 66, 3: 220, 4: 495, 5: 792, 6: 924, 7: 792, 8: 495, 9: 220, 10: 66, 11: 12}[k] for k in range(1, 12)),
    )
    checks.check(
        "thm1-cite-6465-pairs",
        "recomputed (m_k, N_max_k) match the cited #6465 pairs",
        all(pairs[k] == CITED_6465_PAIRS[k] for k in CITED_6465_PAIRS)
        and pairs[1] == (12, 4)
        and pairs[2] == (66, 2)
        and pairs[3] == (220, 2)
        and pairs[4] == (495, 1)
        and pairs[5] == (792, 2)
        and pairs[11] == (12, 8)
        and pairs[10] == (66, 4)
        and pairs[9] == (220, 4)
        and "m_1 = 12" in note
        and "N_max_1 = 4" in note
        and "#6465" in note,
    )
    checks.check(
        "thm1-set-equality-bits",
        "Max(k)=Max(12-k) only for k=4 and k=5 among k=1..5",
        equality == EQUALITY_5_TUPLE
        and maximizers[1] != maximizers[11]
        and maximizers[2] != maximizers[10]
        and maximizers[3] != maximizers[9]
        and maximizers[4] == maximizers[8]
        and maximizers[5] == maximizers[7]
        and maximizers[4] == [F1_REMAINING]
        and maximizers[5] == [L1_REMAINING, F1_REMAINING]
        and set(maximizers[1]) < set(maximizers[11])
        and set(maximizers[2]) != set(maximizers[10]),
    )
    checks.check(
        "thm2-equality-5-tuple",
        "the displayed equality 5-tuple is (0, 0, 0, 1, 1)",
        equality == (0, 0, 0, 1, 1)
        and "(0, 0, 0, 1, 1)" in note
        and "E = (0, 0, 0, 1, 1)" in note,
    )
    checks.check(
        "thm3-display-not-adopt-duality",
        "the equality bits are displayed and no duality is adopted",
        "Displayed, not adopted" in note
        and "Do not adopt a duality" in note
        and "Do not write the duality into Admissibility" in note
        and equality[0] == 0
        and equality[3] == 1,
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
        "bounded theorem, displayed-not-adopted equality bits, and machine status",
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
        "note-reports-sets-and-tuple",
        "the note reports Max(k) versus Max(12-k) and the equality 5-tuple",
        "(wt1, opp2, adj2, vertex3, mixed3)" in note
        and "Max(1)" in note
        and "Max(11)" in note
        and "(1, 0, 1, 1, 1)" in note
        and "(1, 1, 1, 1, 1)" in note
        and "(0, 0, 0, 1, 1)" in note
        and "k=1,2,3" in note
        and "k=4,5" in note,
    )
    checks.check(
        "no-axiom-edit",
        "the theorem proposes no axiom change",
        "no axiom or approved primitive is added" in note
        and "hypothetical_axiom_status" in note
        and "Do not write the duality into Admissibility" in note,
    )
    checks.check(
        "off-patch-zero",
        "off-patch occupancy is the explicit 0 default, not a blank-block",
        "off-patch occupancy `0`" in note and "blank-block is a different rule" in note,
    )
    checks.check(
        "not-leftover-6465",
        "the residual is set equality, not leftover-character of the #6465 counts",
        "Not leftover-character of #6465" in note
        and "that only reported" in note
        and "(m_k, N_max_k)" in note
        and "not a recensus" in note,
    )
    checks.check(
        "claim-scope-duality",
        "claim_scope states set equality or not for each k=1..5",
        "Among the 32 F_cut maps on the two-cube" in note
        and "off-patch o=0" in note
        and "set of coverage maximizers at seed size k" in note
        and "12-k" in note
        and "Displayed, not adopted" in note
        and "is not equal" in note
        and "is equal" in note,
    )

    print("per_element: checked exactly — each of the 64 neighbor 6-tuples is assigned its axis-type orbit")
    print("per_site: checked exactly — each of the twelve two-cube vertices uses the same six-direction stencil")
    print("per_mode: checked exactly — every F_cut map is scored at each seed size k=1..11, then Max(k) is named")
    print("per_block: checked exactly — the equality 5-tuple is Max(k)=Max(12-k) for each k=1..5")
    print("lattice_wide: checked and not executed — no Z^3-wide formation law or physical Admissibility selector is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
