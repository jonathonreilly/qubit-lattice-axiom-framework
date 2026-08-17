#!/usr/bin/env python3
"""Age bit and hop-cost 8-tuple are independent displayed extras.

On the uneqrad lex-first breaker the age bit b names which end of the
unique full axis is older. The hop cost c is a G+-equivariant map from
the eight inward-occupancy-pair orbits on B_3(0) to {1,2,3}. Same
occupancy admits both b values; flipping b leaves inward occupancy
pairs unchanged; among the 405 reversals more than one 8-tuple exists.
Displayed, not adopted. No cache is written.
"""

from __future__ import annotations

import ast
import heapq
import itertools
from collections import defaultdict
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/AGEBIT_HOPCOST_INDEPENDENT_EXTRAS_"
    "BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/AGEBIT_HOPCOST_INDEPENDENT_EXTRAS_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Point = tuple[int, int, int]
Coloring = tuple[int, ...]
Tick = tuple[int | None, ...]
Matrix = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]

DIRS: tuple[Point, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
DIR_INDEX = {direction: index for index, direction in enumerate(DIRS)}
SLOT_PLUS_Z = 4
SLOT_MINUS_Z = 5
UNEQ_SEEDS: tuple[Point, Point, Point] = (
    (-2, -2, -2),
    (-2, -2, -1),
    (-2, -2, 1),
)
UNEQ_RADII = (2, 1, 3)
UNEQ_V: Point = (-3, -3, -1)
FIRST_SEEDS: tuple[Point, Point, Point] = (
    (-2, -2, -2),
    (-2, -2, -1),
    (-2, -2, 0),
)
FIRST_RADII = (2, 1, 2)
ORIGIN: Point = (0, 0, 0)
AXIS: Point = (3, 0, 0)
DIAG: Point = (1, 1, 1)
MINKBEST: tuple[int, ...] = (3, 1, 3, 1, 1, 3, 1, 1)
LEX_FIRST_REVERSAL: tuple[int, ...] = (1, 1, 3, 1, 1, 1, 1, 1)
CLAIM_SCOPE = (
    'claim_scope: "The age bit and the two-end hop-cost 8-tuple are '
    "independent displayed extras. Neither names the other. "
    'Displayed, not adopted."'
)


def forbidden_tokens() -> tuple[str, ...]:
    return (
        "G" + "_N",
        "1/" + "r",
        "1/" + "r^2",
        "Lattice-" + "named",
        "not a " + "TOE",
    )


def normalize(text: str) -> str:
    return " ".join(text.split())


def add(left: Point, right: Point) -> Point:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def l1(left: Point, right: Point) -> int:
    return abs(left[0] - right[0]) + abs(left[1] - right[1]) + abs(left[2] - right[2])


def ball_around(center: Point, radius: int) -> tuple[Point, ...]:
    sites: list[Point] = []
    span = range(-radius, radius + 1)
    for offset in itertools.product(span, repeat=3):
        if abs(offset[0]) + abs(offset[1]) + abs(offset[2]) <= radius:
            sites.append(add(center, offset))
    return tuple(sites)


def occupied_set(seeds: tuple[Point, ...], radii: tuple[int, ...]) -> set[Point]:
    sites: set[Point] = set()
    for seed, radius in zip(seeds, radii):
        sites.update(ball_around(seed, radius))
    return sites


def sigma_ticks(
    site: Point, seeds: tuple[Point, ...], radii: tuple[int, ...]
) -> tuple[Coloring, Tick]:
    occupied = occupied_set(seeds, radii)
    sigma_bits: list[int] = []
    ticks_bits: list[int | None] = []
    for direction in DIRS:
        neighbor = add(site, direction)
        if neighbor in occupied:
            sigma_bits.append(1)
            ticks_bits.append(min(l1(neighbor, seed) for seed in seeds))
        else:
            sigma_bits.append(0)
            ticks_bits.append(None)
    return tuple(sigma_bits), tuple(ticks_bits)


def age_bit(ticks: Tick) -> int:
    minus_z = ticks[SLOT_MINUS_Z]
    plus_z = ticks[SLOT_PLUS_Z]
    if minus_z is None or plus_z is None:
        raise AssertionError("age bit requires both ends of the z axis occupied")
    return int(minus_z < plus_z)


def unique_full_axis(sigma: Coloring) -> str | None:
    axes = (
        ("x", sigma[0], sigma[1]),
        ("y", sigma[2], sigma[3]),
        ("z", sigma[4], sigma[5]),
    )
    full = [name for name, plus, minus in axes if plus == 1 and minus == 1]
    if len(full) != 1:
        return None
    return full[0]


def det3(matrix: Matrix) -> int:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def apply_matrix(matrix: Matrix, point: Point) -> Point:
    return (
        matrix[0][0] * point[0] + matrix[0][1] * point[1] + matrix[0][2] * point[2],
        matrix[1][0] * point[0] + matrix[1][1] * point[1] + matrix[1][2] * point[2],
        matrix[2][0] * point[0] + matrix[2][1] * point[1] + matrix[2][2] * point[2],
    )


def proper_cubic_rotations() -> tuple[Matrix, ...]:
    records: list[Matrix] = []
    seen: set[Matrix] = set()
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            rows = []
            for row, col in enumerate(perm):
                entry = [0, 0, 0]
                entry[col] = signs[row]
                rows.append(tuple(entry))
            matrix = (rows[0], rows[1], rows[2])
            if matrix not in seen and det3(matrix) == 1:
                seen.add(matrix)
                records.append(matrix)
    return tuple(records)


def graph_radius(point: Point) -> int:
    return abs(point[0]) + abs(point[1]) + abs(point[2])


def ball(radius: int) -> tuple[Point, ...]:
    sites: list[Point] = []
    span = range(-radius, radius + 1)
    for coords in itertools.product(span, repeat=3):
        if graph_radius(coords) <= radius:
            sites.append(coords)
    return tuple(sites)


def occupancy(point: Point) -> int:
    bits = 0
    for index, shift in enumerate(DIRS):
        neighbor = add(point, shift)
        if graph_radius(neighbor) < graph_radius(point):
            bits |= 1 << index
    return bits


def occupancy_with_ignored_bit(point: Point, ignored_age_bit: int) -> int:
    del ignored_age_bit
    return occupancy(point)


def bit_permutation(matrix: Matrix) -> tuple[int, ...]:
    return tuple(DIR_INDEX[apply_matrix(matrix, shift)] for shift in DIRS)


def apply_bits(perm: tuple[int, ...], bits: int) -> int:
    out = 0
    for index in range(6):
        if bits >> index & 1:
            out |= 1 << perm[index]
    return out


def apply_pair(perm: tuple[int, ...], pair: tuple[int, int]) -> tuple[int, int]:
    return (apply_bits(perm, pair[0]), apply_bits(perm, pair[1]))


def orbit_rep(
    pair: tuple[int, int], perms: tuple[tuple[int, ...], ...]
) -> tuple[int, int]:
    return min(apply_pair(perm, pair) for perm in perms)


def directed_edges(sites: tuple[Point, ...]) -> tuple[tuple[Point, Point], ...]:
    present = set(sites)
    edges: list[tuple[Point, Point]] = []
    for site in sites:
        for shift in DIRS:
            neighbor = add(site, shift)
            if neighbor in present:
                edges.append((site, neighbor))
    return tuple(edges)


def pair_orbits(
    sites: tuple[Point, ...],
    edges: tuple[tuple[Point, Point], ...],
    perms: tuple[tuple[int, ...], ...],
    age_label: int,
) -> tuple[tuple[int, int], ...]:
    pairs = tuple(
        (
            occupancy_with_ignored_bit(src, age_label),
            occupancy_with_ignored_bit(dst, age_label),
        )
        for src, dst in edges
    )
    return tuple(sorted({orbit_rep(pair, perms) for pair in pairs}))


def shortest(
    start: Point,
    goals: tuple[Point, ...],
    adj: dict[Point, list[tuple[Point, int]]],
    costs: tuple[int, ...],
) -> dict[Point, int]:
    dist = {start: 0}
    heap: list[tuple[int, Point]] = [(0, start)]
    remaining = set(goals)
    while heap and remaining:
        current, node = heapq.heappop(heap)
        if current != dist[node]:
            continue
        remaining.discard(node)
        for neighbor, orbit in adj[node]:
            trial = current + costs[orbit]
            prior = dist.get(neighbor)
            if prior is None or trial < prior:
                dist[neighbor] = trial
                heapq.heappush(heap, (trial, neighbor))
    return dist


def reverses(t_axis: int, t_diag: int) -> bool:
    return 3 * t_axis * t_axis > 9 * t_diag * t_diag


def parse_audit_input_paths(source: str) -> object:
    tree = ast.parse(source)
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id == "AUDIT_INPUT_PATHS":
                return ast.literal_eval(node.value)
    raise AssertionError("AUDIT_INPUT_PATHS assignment is missing")


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, condition: bool, detail: str = "") -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        suffix = f" | {detail}" if detail else ""
        print(f"{'PASS' if ok else 'FAIL'}: {label}{suffix}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note_path = ROOT / NOTE_REL
    axiom_path = ROOT / AXIOM_REL
    note = note_path.read_text(encoding="utf-8")
    axiom = axiom_path.read_text(encoding="utf-8")
    self_source = Path(__file__).read_text(encoding="utf-8")
    note_flat = normalize(note)
    axiom_flat = normalize(axiom)
    literal_paths = parse_audit_input_paths(self_source)

    print("age-bit / hop-cost independent extras")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")

    rotations = proper_cubic_rotations()
    perms = tuple(bit_permutation(matrix) for matrix in rotations)
    uneq_unread = UNEQ_V not in occupied_set(UNEQ_SEEDS, UNEQ_RADII)
    first_unread = UNEQ_V not in occupied_set(FIRST_SEEDS, FIRST_RADII)
    uneq_sigma, uneq_ticks = sigma_ticks(UNEQ_V, UNEQ_SEEDS, UNEQ_RADII)
    first_sigma, first_ticks = sigma_ticks(UNEQ_V, FIRST_SEEDS, FIRST_RADII)
    uneq_b = age_bit(uneq_ticks)
    first_b = age_bit(first_ticks)
    axis_name = unique_full_axis(uneq_sigma)

    sites = ball(3)
    edges = directed_edges(sites)
    orbits_b0 = pair_orbits(sites, edges, perms, 0)
    orbits_b1 = pair_orbits(sites, edges, perms, 1)
    weights = tuple(
        (bin(rep[0]).count("1"), bin(rep[1]).count("1")) for rep in orbits_b1
    )
    expected_weights = (
        (0, 1),
        (1, 0),
        (1, 1),
        (1, 2),
        (2, 1),
        (2, 2),
        (2, 3),
        (3, 2),
    )
    rep_index = {rep: index for index, rep in enumerate(orbits_b1)}
    adj: dict[Point, list[tuple[Point, int]]] = defaultdict(list)
    for src, dst in edges:
        pair = (occupancy(src), occupancy(dst))
        adj[src].append((dst, rep_index[orbit_rep(pair, perms)]))

    reverse = 0
    lex_first: tuple[int, ...] | None = None
    lex_times: tuple[int, int] | None = None
    minkbest_times: tuple[int, int] | None = None
    n_orbit = len(orbits_b1)
    for filling in itertools.product((1, 2, 3), repeat=n_orbit):
        reached = shortest(ORIGIN, (AXIS, DIAG), adj, filling)
        t_axis = reached[AXIS]
        t_diag = reached[DIAG]
        if filling == MINKBEST:
            minkbest_times = (t_axis, t_diag)
        if reverses(t_axis, t_diag):
            reverse += 1
            if lex_first is None:
                lex_first = filling
                lex_times = (t_axis, t_diag)

    print(f"G_plus={len(rotations)}")
    print(f"uneq_unread={uneq_unread} first_unread={first_unread}")
    print(f"uneq_sigma={uneq_sigma} uneq_ticks={uneq_ticks} uneq_b={uneq_b}")
    print(f"first_sigma={first_sigma} first_ticks={first_ticks} first_b={first_b}")
    print(f"unique_full_axis={axis_name}")
    print(f"orbit_weights={weights}")
    print(f"n_maps={3 ** n_orbit}")
    print(f"reverse_count={reverse}")
    print(f"lex_first_c={lex_first} lex_first_times={lex_times}")
    print(f"minkbest_times={minkbest_times}")

    expected_paths = (
        "docs/AGEBIT_HOPCOST_INDEPENDENT_EXTRAS_BOUNDED_THEOREM_NOTE_2026-08-15.md",
        "docs/MINIMAL_AXIOMS_2026-06-29.md",
    )
    checks.check(
        "audit-input-paths",
        AUDIT_INPUT_PATHS == expected_paths
        and literal_paths == AUDIT_INPUT_PATHS
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and AUDIT_TIMEOUT_SEC == 120,
        "AUDIT_INPUT_PATHS is the required static two-string literal tuple",
    )

    lattice_sentence = (
        "Physical sites are the points of the cubic lattice `Z^3`, with "
        "nearest-neighbor adjacency, standard translations, and proper cubic "
        "rotations about each site."
    )
    covariance_clause = (
        "There is one fixed nearest-neighbor admissibility rule, covariant "
        "under lattice translations and proper cubic rotations."
    )
    admissibility_sentence = (
        "For each site, the probability distribution over the possibilities is "
        "determined by, and varies with, the nearest-neighbor conditions."
    )
    unread_sentence = "A site with no record cannot be read."
    qubit_sentence = (
        "The full one-site possibility domain has algebraic presentation `M_2(C)`."
    )
    checks.check(
        "source-lattice",
        lattice_sentence in axiom_flat and lattice_sentence in note_flat,
    )
    checks.check(
        "source-admissibility",
        covariance_clause in axiom_flat
        and admissibility_sentence in axiom_flat
        and covariance_clause in note_flat
        and admissibility_sentence in note_flat,
    )
    checks.check(
        "source-unread-qubit",
        unread_sentence in axiom
        and unread_sentence in note
        and qubit_sentence in axiom
        and qubit_sentence in note,
    )
    checks.check(
        "g-plus-order",
        len(rotations) == 24 and len(set(rotations)) == 24,
        f"proper={len(rotations)}",
    )
    checks.check(
        "theorem-1-same-sigma-both-bits",
        uneq_unread
        and first_unread
        and uneq_sigma == first_sigma
        and uneq_sigma == (1, 0, 1, 0, 1, 1)
        and uneq_ticks == (1, None, 1, None, 3, 2)
        and first_ticks == (1, None, 1, None, 2, 2)
        and uneq_b == 1
        and first_b == 0
        and axis_name == "z"
        and unique_full_axis(first_sigma) == "z"
        and {uneq_b, first_b} == {0, 1}
        and "`σ = (1, 0, 1, 0, 1, 1)`" in note
        and "`b = 1`" in note
        and "`b = 0`" in note
        and "same `σ` admits both" in note_flat,
        f"uneq_b={uneq_b} first_b={first_b} sigma={uneq_sigma}",
    )
    checks.check(
        "theorem-1-c-not-function-of-b",
        orbits_b0 == orbits_b1
        and weights == expected_weights
        and uneq_sigma == first_sigma
        and uneq_b != first_b
        and "flipping `b`" in note
        and "leaves inward occupancy pairs" in note
        and "not a function of `b`" in note,
        f"n_orbit={len(orbits_b1)}",
    )
    checks.check(
        "theorem-2-axiom-no-hop-cost",
        "two-end occupancy" not in axiom
        and "c(σ_v, σ_w)" not in axiom
        and "8-tuple" not in axiom
        and "numerical hop cost" in note
        and "does not supply a numerical hop cost" in note,
    )
    checks.check(
        "theorem-2-more-than-one-8tuple",
        n_orbit == 8
        and 3 ** n_orbit == 6561
        and reverse > 1
        and reverse == 405
        and lex_first == LEX_FIRST_REVERSAL
        and lex_times == (7, 3)
        and minkbest_times is not None
        and reverses(*minkbest_times)
        and MINKBEST != LEX_FIRST_REVERSAL
        and "405" in note
        and "more than one 8-tuple" in note,
        f"reverse={reverse} lex={lex_first} minkbest_times={minkbest_times}",
    )
    checks.check(
        "theorem-2-occupancy-does-not-select-minkbest",
        reverse > 1
        and MINKBEST != LEX_FIRST_REVERSAL
        and "(3, 1, 3, 1, 1, 3, 1, 1)" in note
        and "(1, 1, 3, 1, 1, 1, 1, 1)" in note
        and "does not select the minkbest 8-tuple" in note,
    )
    checks.check("claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "theorem-3-displayed",
        "Displayed, not adopted" in note
        and "Do not write b or" in note
        and "c into Admissibility" in note
        and "Uniqueness of either extra is not claimed" in note
        and "hypothetical_axiom_status:" in note
        and "This note authors no audit verdict" in note,
    )
    checks.check(
        "l1-not-attached",
        "Do not attach L1" in note
        and "we attach L1" not in note_flat
        and "we add a 4th ball" not in note_flat,
    )
    checks.check(
        "not-leftover-bitsec-minkbest",
        "not leftover of bitsec" in note_flat
        and "minkbest" in note_flat
        and "those score one extra" in note,
    )
    checks.check(
        "uniqueness-not-claimed",
        "Uniqueness of either extra is not claimed" in note
        and "Uniqueness not required" not in axiom
        and "matching member needs both" in note,
    )
    checks.check(
        "admissibility-unedited",
        covariance_clause in axiom_flat
        and "age bit" not in axiom
        and "hop cost" not in axiom
        and "minkbest" not in axiom
        and "lock-tick" not in axiom,
    )
    checks.check(
        "forbidden-phrases",
        all(phrase not in note for phrase in forbidden_tokens())
        and all(phrase not in self_source for phrase in forbidden_tokens())
        and all(phrase not in axiom for phrase in forbidden_tokens()),
    )
    checks.check(
        "no-axiom-edit",
        "[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)" in note
        and "cache_write: false" in self_source
        and AXIOM_REL in AUDIT_INPUT_PATHS
        and "no axiom" in note_flat.lower(),
    )

    print("per_element: b, σ, eight pair-orbits, and reversing 8-tuples are exact")
    print("per_site: uneqrad breaker, uneqext same-σ star, and B_3(0) one-seed front")
    print("per_mode: no spectral calculation")
    print("per_block: 3-ball star and radius-3 ball only")
    print("lattice_wide: checked and not executed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
