#!/usr/bin/env python3
"""Name the 4 of 12 hosts that survive the cost-1 leftover-frame filter.

The 12 (mask, centers, radii, v) rows are the bitall / bitreal Theorem 2
lex-first realizing 3-ball hosts of the perpendicular weight-4 masks.
f is leftover-frame-positive. rho is cost 3 iff equal inward weight or
seed-exit, else 1. Restrict fire to cost-1 incoming edges. Name the 4
lex-first hosts with N_new=1 and the 8 with N_new=0. Displayed, not
adopted. No cache.
"""

from __future__ import annotations

import ast
import itertools
from array import array
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/COST1_FILTER_FOUR_HOSTS_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/COST1_FILTER_FOUR_HOSTS_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Point = tuple[int, int, int]
Coloring = tuple[int, ...]
Tick = tuple[int | None, ...]
Host = tuple[tuple[Point, Point, Point], tuple[int, int, int], Point]
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
AXES: tuple[tuple[int, int], ...] = ((0, 1), (2, 3), (4, 5))
AXIS_NAME = ("x", "y", "z")
EMPTY, PLUS, MINUS = 0, 1, 2
LETTER = {EMPTY: "0", PLUS: "+", MINUS: "−"}
SHIFT = 5
STRIDE = 11
GRID = STRIDE * STRIDE * STRIDE
CLAIM_SCOPE = (
    'claim_scope: "The 4 of 12 perp-mask hosts on which leftover-frame '
    "fire survives a cost-1 hop-cost filter are named. "
    'Displayed, not adopted."'
)
BITREAL_HOSTS: dict[Coloring, Host] = {
    (0, 1, 0, 1, 1, 1): (
        ((-2, -2, -2), (-2, -2, -1), (-2, -2, 0)),
        (2, 1, 2),
        (-1, -1, -1),
    ),
    (0, 1, 1, 0, 1, 1): (
        ((-2, -2, -2), (-2, -2, -1), (-2, -2, 0)),
        (2, 1, 2),
        (-1, -3, -1),
    ),
    (0, 1, 1, 1, 0, 1): (
        ((-2, -2, -2), (-2, -2, -1), (-2, 0, -2)),
        (1, 1, 2),
        (-1, -1, -1),
    ),
    (0, 1, 1, 1, 1, 0): (
        ((-2, -2, -2), (-2, -2, -1), (-2, 0, -2)),
        (1, 2, 1),
        (-1, -1, -2),
    ),
    (1, 0, 0, 1, 1, 1): (
        ((-2, -2, -2), (-2, -2, -1), (-2, -2, 0)),
        (2, 1, 2),
        (-3, -1, -1),
    ),
    (1, 0, 1, 0, 1, 1): (
        ((-2, -2, -2), (-2, -2, -1), (-2, -2, 0)),
        (2, 1, 2),
        (-3, -3, -1),
    ),
    (1, 0, 1, 1, 0, 1): (
        ((-2, -2, -2), (-2, -2, -1), (-2, 0, -2)),
        (1, 1, 2),
        (-3, -1, -1),
    ),
    (1, 0, 1, 1, 1, 0): (
        ((-2, -2, -2), (-2, -2, -1), (-2, 0, -2)),
        (1, 2, 1),
        (-3, -1, -2),
    ),
    (1, 1, 0, 1, 0, 1): (
        ((-2, -2, -2), (-2, -2, -1), (0, -2, -2)),
        (1, 1, 2),
        (-1, -1, -1),
    ),
    (1, 1, 0, 1, 1, 0): (
        ((-2, -2, -2), (-2, -2, -1), (0, -2, -2)),
        (1, 2, 1),
        (-1, -1, -2),
    ),
    (1, 1, 1, 0, 0, 1): (
        ((-2, -2, -2), (-2, -2, -1), (0, -2, -2)),
        (1, 1, 2),
        (-1, -3, -1),
    ),
    (1, 1, 1, 0, 1, 0): (
        ((-2, -2, -2), (-2, -2, -1), (0, -2, -2)),
        (1, 2, 1),
        (-1, -3, -2),
    ),
}
EXPECTED_SURVIVORS: tuple[Coloring, ...] = (
    (0, 1, 1, 1, 1, 0),
    (1, 0, 1, 1, 1, 0),
    (1, 1, 0, 1, 1, 0),
    (1, 1, 1, 0, 1, 0),
)
EXPECTED_DEATHS: tuple[Coloring, ...] = (
    (0, 1, 0, 1, 1, 1),
    (0, 1, 1, 0, 1, 1),
    (0, 1, 1, 1, 0, 1),
    (1, 0, 0, 1, 1, 1),
    (1, 0, 1, 0, 1, 1),
    (1, 0, 1, 1, 0, 1),
    (1, 1, 0, 1, 0, 1),
    (1, 1, 1, 0, 0, 1),
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


def ball(center: Point, radius: int) -> tuple[Point, ...]:
    sites: list[Point] = []
    span = range(-radius, radius + 1)
    for offset in itertools.product(span, repeat=3):
        if abs(offset[0]) + abs(offset[1]) + abs(offset[2]) <= radius:
            sites.append(add(center, offset))
    return tuple(sites)


def enc(point: Point) -> int:
    return (point[0] + SHIFT) + STRIDE * (
        (point[1] + SHIFT) + STRIDE * (point[2] + SHIFT)
    )


def perp_masks() -> tuple[Coloring, ...]:
    records: list[Coloring] = []
    for mask in itertools.product((0, 1), repeat=len(DIRS)):
        if sum(mask) != 4:
            continue
        empty = [index for index, bit in enumerate(mask) if bit == 0]
        axes = {index // 2 for index in empty}
        if len(axes) == 2:
            records.append(mask)
    return tuple(records)


def locked_union(seeds: tuple[Point, ...], radii: tuple[int, ...]) -> frozenset[Point]:
    occupied: set[Point] = set()
    for seed, radius in zip(seeds, radii):
        occupied.update(ball(seed, radius))
    return frozenset(occupied)


def occupancy_tuple(site: Point, occupied: frozenset[Point]) -> Coloring:
    return tuple(int(add(site, direction) in occupied) for direction in DIRS)


def lock_tick(site: Point, seeds: tuple[Point, ...]) -> int:
    return min(l1(site, seed) for seed in seeds)


def tick_on_occupied(
    site: Point,
    occupied: frozenset[Point],
    seeds: tuple[Point, ...],
) -> Tick:
    ticks: list[int | None] = []
    for direction in DIRS:
        neighbor = add(site, direction)
        if neighbor in occupied:
            ticks.append(lock_tick(neighbor, seeds))
        else:
            ticks.append(None)
    return tuple(ticks)


def inward_occupancy(site: Point, seeds: tuple[Point, ...]) -> Coloring:
    here = lock_tick(site, seeds)
    return tuple(
        int(lock_tick(add(site, direction), seeds) < here) for direction in DIRS
    )


def inward_weight(site: Point, seeds: tuple[Point, ...]) -> int:
    return int(sum(inward_occupancy(site, seeds)))


def named_rho(source: Point, target: Point, seeds: tuple[Point, ...]) -> int:
    source_weight = inward_weight(source, seeds)
    target_weight = inward_weight(target, seeds)
    if source_weight == target_weight or source_weight == 0:
        return 3
    return 1


def support(coloring: Coloring) -> Coloring:
    return tuple(int(slot != EMPTY) for slot in coloring)


def det3(matrix: Matrix) -> int:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def mat_vec(matrix: Matrix, vector: Point) -> Point:
    return (
        matrix[0][0] * vector[0] + matrix[0][1] * vector[1] + matrix[0][2] * vector[2],
        matrix[1][0] * vector[0] + matrix[1][1] * vector[1] + matrix[1][2] * vector[2],
        matrix[2][0] * vector[0] + matrix[2][1] * vector[1] + matrix[2][2] * vector[2],
    )


def direction_perm(matrix: Matrix) -> tuple[int, ...]:
    return tuple(DIR_INDEX[mat_vec(matrix, direction)] for direction in DIRS)


def act_col(perm: tuple[int, ...], coloring: Coloring | tuple) -> tuple:
    out = [None] * len(coloring)
    for source, image in enumerate(perm):
        out[image] = coloring[source]
    return tuple(out)


def proper_rotations() -> tuple[tuple[Matrix, tuple[int, ...]], ...]:
    records: list[tuple[Matrix, tuple[int, ...]]] = []
    seen: set[tuple[int, ...]] = set()
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            rows = []
            for row, col in enumerate(perm):
                entry = [0, 0, 0]
                entry[col] = signs[row]
                rows.append(tuple(entry))
            matrix = (rows[0], rows[1], rows[2])
            if det3(matrix) != 1:
                continue
            slots = direction_perm(matrix)
            if slots not in seen:
                seen.add(slots)
                records.append((matrix, slots))
    return tuple(records)


def inversion_perm() -> tuple[int, ...]:
    return direction_perm(((-1, 0, 0), (0, -1, 0), (0, 0, -1)))


def july3_k3_pair() -> frozenset[Coloring]:
    proper = [slots for _matrix, slots in proper_rotations()]
    inversion = inversion_perm()
    unseen = set(itertools.product(range(3), repeat=6))
    pair: set[Coloring] = set()
    while unseen:
        seed = min(unseen)
        orbit = {act_col(perm, seed) for perm in proper}
        unseen -= orbit
        image = act_col(inversion, next(iter(orbit)))
        if image not in orbit:
            pair |= orbit
    return frozenset(pair)


def unique_full_axis(sigma: Coloring) -> int | None:
    named = tuple(
        axis_index
        for axis_index, (plus, minus) in enumerate(AXES)
        if sigma[plus] == 1 and sigma[minus] == 1
    )
    if len(named) == 1:
        return named[0]
    return None


def age_bit(ticks: Tick, axis_index: int) -> int:
    plus, minus = AXES[axis_index]
    minus_tick = ticks[minus]
    plus_tick = ticks[plus]
    if minus_tick is not None and plus_tick is not None and minus_tick < plus_tick:
        return 1
    return 0


def axis_letters(bit: int) -> tuple[int, int]:
    if bit == 1:
        return (PLUS, MINUS)
    return (MINUS, PLUS)


def completions(
    sigma: Coloring,
    bit: int,
    pair: frozenset[Coloring],
) -> tuple[Coloring, ...]:
    named = unique_full_axis(sigma)
    if named is None:
        return ()
    plus, minus = AXES[named]
    plus_letter, minus_letter = axis_letters(bit)
    matches = [
        item
        for item in pair
        if support(item) == sigma
        and item[plus] == plus_letter
        and item[minus] == minus_letter
    ]
    return tuple(sorted(matches))


def leftover_frame_sign(coloring: Coloring) -> int:
    named = unique_full_axis(support(coloring))
    if named is None:
        raise AssertionError("completion has no unique full axis")
    leftover = [
        index
        for index in range(6)
        if support(coloring)[index] == 1 and index not in AXES[named]
    ]
    plus_left = next(index for index in leftover if coloring[index] == PLUS)
    minus_left = next(index for index in leftover if coloring[index] == MINUS)
    plus_full = next(index for index in AXES[named] if coloring[index] == PLUS)
    return det3((DIRS[plus_left], DIRS[minus_left], DIRS[plus_full]))


def leftover_frame_positive(
    sigma: Coloring,
    bit: int,
    pair: frozenset[Coloring],
) -> Coloring | None:
    found = completions(sigma, bit, pair)
    positive = [item for item in found if leftover_frame_sign(item) == 1]
    if len(positive) != 1:
        return None
    return positive[0]


def format_tuple(coloring: Coloring) -> str:
    return "(" + ", ".join(LETTER[slot] for slot in coloring) + ")"


def format_mask(mask: Coloring) -> str:
    return "(" + ", ".join(str(slot) for slot in mask) + ")"


def format_ticks(ticks: Tick) -> str:
    parts = ["·" if tick is None else str(tick) for tick in ticks]
    return "(" + ", ".join(parts) + ")"


def execute_at_v(
    occupied: frozenset[Point],
    site: Point,
    coloring: Coloring | None,
    pair: frozenset[Coloring],
) -> tuple[frozenset[Point], int]:
    if coloring is None or site in occupied or coloring not in pair:
        return occupied, 0
    return occupied | {site}, 1


def realize_hosts() -> dict[Coloring, Host]:
    masks = perp_masks()
    remaining = set(masks)
    hosts: dict[Coloring, Host] = {}
    seed_box = tuple(itertools.product(range(-2, 3), repeat=3))
    v_box = tuple(itertools.product(range(-4, 5), repeat=3))
    radii_opts = tuple(
        radii
        for radii in itertools.product((1, 2, 3), repeat=3)
        if not (radii[0] == radii[1] == radii[2])
    )
    ball_enc = {
        (seed, radius): tuple(enc(site) for site in ball(seed, radius))
        for seed in seed_box
        for radius in (1, 2, 3)
    }
    v_enc = tuple(enc(site) for site in v_box)
    neighbor_enc = tuple(
        tuple(enc(add(site, direction)) for direction in DIRS) for site in v_box
    )
    mark = array("I", [0]) * GRID
    generation = 0
    for s1, s2, s3 in itertools.combinations(seed_box, 3):
        seeds = (s1, s2, s3)
        for radii in radii_opts:
            generation += 1
            for seed, radius in zip(seeds, radii):
                for index in ball_enc[(seed, radius)]:
                    mark[index] = generation
            for v_index, site in enumerate(v_box):
                if mark[v_enc[v_index]] == generation:
                    continue
                sigma = tuple(
                    1 if mark[w_enc] == generation else 0
                    for w_enc in neighbor_enc[v_index]
                )
                if sum(sigma) != 4:
                    continue
                if sigma in remaining:
                    remaining.remove(sigma)
                    hosts[sigma] = (seeds, radii, site)
            if not remaining:
                return hosts
    return hosts


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


def score_host(
    sigma: Coloring,
    host: Host,
    pair: frozenset[Coloring],
) -> dict:
    seeds, radii, site = host
    occupied = locked_union(seeds, radii)
    mask = occupancy_tuple(site, occupied)
    ticks = tick_on_occupied(site, occupied, seeds)
    named = unique_full_axis(mask)
    bit = age_bit(ticks, named) if named is not None else None
    chosen = leftover_frame_positive(mask, bit, pair) if bit is not None else None
    incoming_rho = tuple(
        named_rho(add(site, direction), site, seeds)
        for direction in DIRS
        if add(site, direction) in occupied
    )
    ready_mask = tuple(
        int(
            add(site, direction) in occupied
            and named_rho(add(site, direction), site, seeds) == 1
        )
        for direction in DIRS
    )
    ready_axis = unique_full_axis(ready_mask)
    ready_chosen = (
        leftover_frame_positive(ready_mask, bit, pair)
        if ready_axis is not None and bit is not None
        else None
    )
    after_ready, n_new_ready = execute_at_v(occupied, site, ready_chosen, pair)
    rebuild = mask == sigma and site not in occupied and host == BITREAL_HOSTS[sigma]
    fires_filt = (
        ready_chosen is not None
        and n_new_ready == 1
        and ready_chosen in pair
        and leftover_frame_sign(ready_chosen) == 1
        and site in after_ready
    )
    return {
        "sigma": sigma,
        "host": host,
        "rebuild": rebuild,
        "ticks": ticks,
        "named": named,
        "bit": bit,
        "chosen": chosen,
        "incoming_rho": incoming_rho,
        "ready_mask": ready_mask,
        "ready_axis": ready_axis,
        "ready_chosen": ready_chosen,
        "n_new_filt": n_new_ready,
        "fires_filt": fires_filt,
    }


def main() -> int:
    checks = Checks()
    note_path = ROOT / NOTE_REL
    axiom_path = ROOT / AXIOM_REL
    note = note_path.read_text(encoding="utf-8")
    axiom = axiom_path.read_text(encoding="utf-8")
    note_flat = normalize(note)
    axiom_flat = normalize(axiom)
    self_source = Path(__file__).read_text(encoding="utf-8")
    literal_paths = parse_audit_input_paths(self_source)
    masks = perp_masks()
    hosts = realize_hosts()
    pair = july3_k3_pair()
    rotations = proper_rotations()

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print(
        "external_scientific_inputs: current Lattice, Qubit, Admissibility, "
        "and Record sentences; leftover-frame-positive section rebuilt from "
        "the July-3 pair; named hop-cost rho; bitall lex-first hosts"
    )
    print(
        "construction: 12 lex-first perp-mask hosts; "
        "f leftover-frame-positive; "
        "rho=3 iff equal inward weight or seed-exit else 1; "
        "cost-1 readiness filter; name the 4 survivors and 8 deaths"
    )
    print(
        "negative_scope: 12 lex-first perp-mask hosts only; displayed, not "
        "adopted; L1 not attached; f and rho not written into Admissibility; "
        "not leftover of the 12/4 counts"
    )

    rows = [score_host(sigma, hosts[sigma], pair) for sigma in masks]
    survivors = tuple(row["sigma"] for row in rows if row["fires_filt"])
    deaths = tuple(row["sigma"] for row in rows if not row["fires_filt"])
    for row in rows:
        sigma = row["sigma"]
        ready_axis = row["ready_axis"]
        print(
            f"host {sigma} incoming_rho={row['incoming_rho']} "
            f"sigma_ready={row['ready_mask']} "
            f"ready_axis={AXIS_NAME[ready_axis] if ready_axis is not None else None} "
            f"N_new_filt={row['n_new_filt']} fires_filt={row['fires_filt']}"
        )
    print(f"survivors_bitall={survivors}")
    print(f"deaths_bitall={deaths}")
    print("score: 12 lex-first perp-mask hosts only")

    expected_paths = (
        "docs/COST1_FILTER_FOUR_HOSTS_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
        "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
    )
    admissibility_sentence = (
        "For each site, the probability distribution over the possibilities is "
        "determined by, and varies with, the nearest-neighbor conditions."
    )
    covariance_clause = (
        "one fixed nearest-neighbor admissibility rule, covariant under "
        "lattice translations and proper cubic rotations"
    )
    formation_boundary = "it does not supply the formation site, probability,"
    qubit_sentence = (
        "The full one-site possibility domain has algebraic presentation `M_2(C)`."
    )
    record_lock = "When present, a record locks exactly one admissible local possibility."
    record_perm = "A site never carries more than one record; records are permanent."
    record_content = "A readout value is determined by record content alone."
    record_absence = "A site with no record cannot be read."

    checks.check(
        "source-lattice",
        lattice_sentence in axiom and lattice_sentence in note,
    )
    checks.check(
        "source-admissibility",
        admissibility_sentence in axiom_flat and admissibility_sentence in note_flat,
    )
    checks.check(
        "source-covariance",
        covariance_clause in axiom_flat and covariance_clause in note_flat,
    )
    checks.check(
        "source-formation-boundary",
        formation_boundary in axiom and formation_boundary in note,
    )
    checks.check(
        "source-qubit",
        qubit_sentence in axiom
        and qubit_sentence in note
        and "Qubit remains `M_2(C)`" in note,
    )
    checks.check(
        "source-record",
        all(
            phrase in axiom_flat
            for phrase in (record_lock, record_perm, record_content, record_absence)
        )
        and all(
            phrase in note
            for phrase in (record_lock, record_perm, record_content, record_absence)
        ),
    )
    checks.check(
        "g-plus-order",
        len(rotations) == 24
        and len({slots for _matrix, slots in rotations}) == 24
        and len(pair) == 48,
        f"N_G+={len(rotations)} N_pair={len(pair)}",
    )
    checks.check(
        "theorem-1-four-survivors",
        survivors == EXPECTED_SURVIVORS
        and len(survivors) == 4
        and all(row["n_new_filt"] == 1 and row["fires_filt"] for row in rows if row["sigma"] in EXPECTED_SURVIVORS)
        and all(format_mask(mask) in note for mask in EXPECTED_SURVIVORS)
        and "bitall order" in note
        and note.find(format_mask(EXPECTED_SURVIVORS[0]))
        < note.find(format_mask(EXPECTED_SURVIVORS[1]))
        < note.find(format_mask(EXPECTED_SURVIVORS[2]))
        < note.find(format_mask(EXPECTED_SURVIVORS[3])),
        f"survivors={survivors}",
    )
    checks.check(
        "theorem-2-eight-deaths",
        deaths == EXPECTED_DEATHS
        and len(deaths) == 8
        and all(row["n_new_filt"] == 0 and not row["fires_filt"] for row in rows if row["sigma"] in EXPECTED_DEATHS)
        and all(format_mask(mask) in note for mask in EXPECTED_DEATHS)
        and "Displayed, not adopted" in note,
        f"deaths={deaths}",
    )
    for row in rows:
        sigma = row["sigma"]
        host = row["host"]
        ready = row["ready_mask"]
        incoming = row["incoming_rho"]
        ready_axis = row["ready_axis"]
        chosen = row["chosen"]
        checks.check(
            f"host-{sigma}",
            row["rebuild"]
            and host is not None
            and host == BITREAL_HOSTS[sigma]
            and hosts[sigma] == BITREAL_HOSTS[sigma]
            and str(host) in note
            and format_mask(sigma) in note
            and format_mask(ready) in note
            and str(incoming) in note
            and (
                (row["fires_filt"] and ready_axis is not None and f"`{AXIS_NAME[ready_axis]}`" in note and chosen is not None and format_tuple(chosen) in note)
                or (not row["fires_filt"] and ready_axis is None and "none" in note)
            )
            and row["n_new_filt"] == int(row["fires_filt"]),
            (
                f"N_new_filt={row['n_new_filt']} incoming_rho={incoming} "
                f"sigma_ready={ready}"
            ),
        )
    checks.check("claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "displayed-not-adopted",
        "Displayed, not adopted" in note
        and "Do not write f or ρ into Admissibility" in note
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
        "uniqueness-not-required",
        "Uniqueness not required" in note
        and "uniqueness not required" in note_flat.lower()
        and "unique leftover" not in note_flat.lower(),
    )
    checks.check(
        "not-leftover-of-12-4-counts",
        "not leftover of the 12/4 counts" in note_flat.replace("`", "").lower(),
    )
    checks.check(
        "score-lex-first-hosts-only",
        "The 12 lex-first perp-mask hosts only" in note
        and "12 lex-first" in note,
    )
    checks.check(
        "admissibility-unedited",
        covariance_clause in axiom_flat
        and "leftover-frame-positive" not in axiom
        and "N_filt_fire" not in axiom
        and "hop-cost" not in axiom
        and "cost-1" not in axiom,
    )
    checks.check(
        "forbidden-phrases",
        all(phrase not in note for phrase in forbidden_tokens())
        and all(phrase not in self_source for phrase in forbidden_tokens()),
    )
    checks.check(
        "no-axiom-edit",
        "[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)" in note
        and "cache_write: false" in self_source
        and AXIOM_REL in AUDIT_INPUT_PATHS
        and "no axiom" in note_flat.lower(),
    )
    checks.check(
        "plus-z-occupied-minus-z-empty",
        all(mask[4] == 1 and mask[5] == 0 for mask in survivors)
        and all(not (mask[4] == 1 and mask[5] == 0) for mask in deaths)
        and "`+z` occupied and `−z` empty" in note,
    )

    print("per_element: the 4 surviving masks and 8 dying masks are exact")
    print("per_site: the 12 lex-first unread realizing hosts only")
    print("per_mode: no spectral calculation")
    print("per_block: 12 perp-mask hosts")
    print("lattice_wide: checked and not executed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
