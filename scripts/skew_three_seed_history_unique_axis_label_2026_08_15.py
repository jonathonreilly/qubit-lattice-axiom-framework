#!/usr/bin/env python3
"""Formation-history unique-axis labels at the off-axis three-seed breaker.

U = B_2(0) ∪ B_2((2,0,0)) ∪ B_2((1,2,1)). Score only the unread star at
v = (−1, 1, 1). For each occupied neighbor, n_hist is the occupancy
kernel from that neighbor's nearest-seed ball (lex-first if tied).
History 6-tuple, unique-axis versus tied, and N_hist_fire among
completions of the ties against the July-3 k=3 pair. Displayed, not
adopted. No cache.
"""

from __future__ import annotations

import ast
import itertools
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/SKEW_THREE_SEED_HISTORY_UNIQUE_AXIS_LABEL_"
    "BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/SKEW_THREE_SEED_HISTORY_UNIQUE_AXIS_LABEL_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Point = tuple[int, int, int]
Coloring = tuple[int, ...]
Kernel = tuple[Fraction, Fraction, Fraction]

DIRS: tuple[Point, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
DIR_INDEX = {direction: index for index, direction in enumerate(DIRS)}
EMPTY, PLUS, MINUS = 0, 1, 2
LETTER = {EMPTY: "0", PLUS: "+", MINUS: "−"}
V: Point = (-1, 1, 1)
SEEDS: tuple[Point, ...] = ((0, 0, 0), (2, 0, 0), (1, 2, 1))
FORBIDDEN = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")


def normalize(text: str) -> str:
    return " ".join(text.split())


def add(left: Point, right: Point) -> Point:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def sub(left: Point, right: Point) -> Point:
    return (left[0] - right[0], left[1] - right[1], left[2] - right[2])


def l1(point: Point) -> int:
    return abs(point[0]) + abs(point[1]) + abs(point[2])


def ball(center: Point, radius: int = 2) -> frozenset[Point]:
    sites: set[Point] = set()
    span = range(-radius, radius + 1)
    for offset in itertools.product(span, repeat=3):
        site = add(center, offset)
        if l1(sub(site, center)) <= radius:
            sites.add(site)
    return frozenset(sites)


def locked_union() -> frozenset[Point]:
    occupied = frozenset()
    for seed in SEEDS:
        occupied = occupied | ball(seed)
    return occupied


def occupancy_tuple(site: Point, occupied: frozenset[Point]) -> Coloring:
    return tuple(int(add(site, direction) in occupied) for direction in DIRS)


def dipole(occ: Coloring) -> Kernel:
    return (
        Fraction(occ[0] - occ[1], 3),
        Fraction(occ[2] - occ[3], 3),
        Fraction(occ[4] - occ[5], 3),
    )


def unique_axis_label(n: Kernel) -> int | None:
    support = [index for index, value in enumerate(n) if value != 0]
    if len(support) != 1:
        return None
    return PLUS if n[support[0]] > 0 else MINUS


def nearest_seed(site: Point) -> Point:
    ranked = sorted((l1(sub(site, seed)), seed) for seed in SEEDS)
    return ranked[0][1]


def completions_of(fragment: tuple[int | None, ...]) -> tuple[Coloring, ...]:
    free = [index for index, slot in enumerate(fragment) if slot is None]
    out: list[Coloring] = []
    for fill in itertools.product((PLUS, MINUS), repeat=len(free)):
        coloring = [EMPTY if slot is None else slot for slot in fragment]
        for index, letter in zip(free, fill):
            coloring[index] = letter
        out.append(tuple(coloring))
    return tuple(out)


def det3(
    matrix: tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]],
) -> int:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def mat_vec(
    matrix: tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]],
    vector: Point,
) -> Point:
    return (
        matrix[0][0] * vector[0] + matrix[0][1] * vector[1] + matrix[0][2] * vector[2],
        matrix[1][0] * vector[0] + matrix[1][1] * vector[1] + matrix[1][2] * vector[2],
        matrix[2][0] * vector[0] + matrix[2][1] * vector[1] + matrix[2][2] * vector[2],
    )


def direction_perm(
    matrix: tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]],
) -> tuple[int, ...]:
    return tuple(DIR_INDEX[mat_vec(matrix, direction)] for direction in DIRS)


def act_col(perm: tuple[int, ...], coloring: Coloring) -> Coloring:
    out = [0] * 6
    for source, image in enumerate(perm):
        out[image] = coloring[source]
    return tuple(out)


def cubic_signed_permutations() -> tuple[list[tuple[int, ...]], tuple[int, ...]]:
    records: list[
        tuple[tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]], int]
    ] = []
    seen: set[tuple[int, ...]] = set()
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            rows = []
            for row, col in enumerate(perm):
                entry = [0, 0, 0]
                entry[col] = signs[row]
                rows.append(tuple(entry))
            matrix = (rows[0], rows[1], rows[2])
            key = tuple(value for row in matrix for value in row)
            if key not in seen:
                seen.add(key)
                records.append((matrix, det3(matrix)))
    proper = [direction_perm(matrix) for matrix, det in records if det == 1]
    inversion = ((-1, 0, 0), (0, -1, 0), (0, 0, -1))
    return proper, direction_perm(inversion)


def july3_k3_pair() -> frozenset[Coloring]:
    proper, inversion = cubic_signed_permutations()
    unseen = set(itertools.product((EMPTY, PLUS, MINUS), repeat=6))
    orbits: list[set[Coloring]] = []
    ids: dict[Coloring, int] = {}
    while unseen:
        seed = min(unseen)
        orbit = {act_col(perm, seed) for perm in proper}
        index = len(orbits)
        orbits.append(orbit)
        unseen -= orbit
        for coloring in orbit:
            ids[coloring] = index
    pair: set[Coloring] = set()
    seen_pairs: set[tuple[int, int]] = set()
    for index, orbit in enumerate(orbits):
        sample = next(iter(orbit))
        image = ids[act_col(inversion, sample)]
        if image == index:
            continue
        key = tuple(sorted((index, image)))
        if key in seen_pairs:
            continue
        seen_pairs.add(key)
        pair |= orbits[index]
        pair |= orbits[image]
    if len(seen_pairs) != 1:
        raise RuntimeError(f"expected one chiral pair, found {len(seen_pairs)}")
    return frozenset(pair)


def format_tuple(coloring: Coloring) -> str:
    return "(" + ",".join(LETTER[slot] for slot in coloring) + ")"


def format_fragment(fragment: tuple[int | None, ...]) -> str:
    parts = []
    for slot in fragment:
        if slot is None:
            parts.append("tied")
        else:
            parts.append(LETTER[slot])
    return "(" + ",".join(parts) + ")"


def format_n(n: Kernel) -> str:
    return "(" + ",".join(str(component) for component in n) + ")"


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

    def check(
        self,
        label: str,
        statement: str,
        condition: bool,
        residual: object | None = None,
    ) -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        print(f"{'PASS' if ok else 'FAIL'}: {label} {statement}")
        if not ok and residual is not None:
            print(f"  residual: {residual}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


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

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print(
        "external_scientific_inputs: current Lattice, Qubit, Admissibility, "
        "and Record sentences plus the July-3 pair reconstructed locally"
    )
    print("construction: U=B_2(0)∪B_2((2,0,0))∪B_2((1,2,1)), unread v=(-1,1,1)")
    print(
        "negative_scope: displayed history unique-axis labels only; "
        "not adopted; L1 not attached; no 4th equal-radius ball"
    )

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required static two-string literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/SKEW_THREE_SEED_HISTORY_UNIQUE_AXIS_LABEL_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and literal_paths == AUDIT_INPUT_PATHS
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and AUDIT_TIMEOUT_SEC == 120,
    )

    lattice_sentence = (
        "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
    )
    admissibility_sentence = (
        "For each site, the probability distribution over the possibilities is "
        "determined by, and varies with, the nearest-neighbor conditions."
    )
    formation_boundary = "it does not supply the formation site, probability,"
    qubit_sentence = "The full one-site possibility domain has algebraic presentation `M_2(C)`."
    record_lock = "When present, a record locks exactly one admissible local possibility."
    record_perm = "A site never carries more than one record; records are permanent."
    record_content = "A readout value is determined by record content alone."
    record_absence = "A site with no record cannot be read."

    checks.check(
        "source-lattice",
        "current cubic nearest-neighbor wording is pinned",
        lattice_sentence in axiom and lattice_sentence in note,
    )
    checks.check(
        "source-admissibility",
        "current local-distribution wording is pinned",
        admissibility_sentence in axiom_flat and admissibility_sentence in note_flat,
    )
    checks.check(
        "source-formation-boundary",
        "formation site/probability/rate remains outside Admissibility",
        formation_boundary in axiom and formation_boundary in note,
    )
    checks.check(
        "source-qubit",
        "Qubit remains M_2(C)",
        qubit_sentence in axiom and qubit_sentence in note and "Qubit remains `M_2(C)`" in note,
    )
    checks.check(
        "source-record",
        "lock, permanence, content-only readout, and unreadability at absence are pinned",
        all(
            phrase in axiom_flat
            for phrase in (record_lock, record_perm, record_content, record_absence)
        )
        and all(
            phrase in note
            for phrase in (record_lock, record_perm, record_content, record_absence)
        ),
    )

    occupied = locked_union()
    balls = {seed: ball(seed) for seed in SEEDS}
    mask = occupancy_tuple(V, occupied)
    pair = july3_k3_pair()
    neighbor_rows: list[
        tuple[Point, Point, Point, Coloring, Kernel, int | None]
    ] = []
    fragment_slots: list[int | None] = []
    for direction in DIRS:
        neighbor = add(V, direction)
        if neighbor not in occupied:
            fragment_slots.append(EMPTY)
            continue
        seed_star = nearest_seed(neighbor)
        occ = occupancy_tuple(neighbor, balls[seed_star])
        n_vec = dipole(occ)
        label = unique_axis_label(n_vec)
        neighbor_rows.append((direction, neighbor, seed_star, occ, n_vec, label))
        fragment_slots.append(label)
    fragment = tuple(fragment_slots)
    completions = completions_of(fragment)
    firing = tuple(coloring for coloring in completions if coloring in pair)
    every_unique = all(label is not None for _d, _w, _s, _o, _n, label in neighbor_rows)
    tied_count = sum(1 for _d, _w, _s, _o, _n, label in neighbor_rows if label is None)

    print(f"U_card={len(occupied)}")
    print(f"v_in_U={V in occupied}")
    print(f"occupancy_mask={mask}")
    print(f"history_6tuple={format_fragment(fragment)}")
    print(f"every_occupied_unique_axis={every_unique}")
    for direction, neighbor, seed_star, occ, n_vec, label in neighbor_rows:
        kind = "unique-axis" if label is not None else "tied"
        letter = LETTER[label] if label is not None else "tied"
        print(
            f"neighbor dir={direction} w={neighbor} s*={seed_star} "
            f"occ_hist={occ} n_hist={format_n(n_vec)} {kind}={letter}"
        )
    print(f"N_tied={tied_count}")
    print(f"N_comp={len(completions)}")
    print("completions=" + ",".join(format_tuple(coloring) for coloring in completions))
    print(f"N_pair={len(pair)}")
    print(f"N_hist_fire={len(firing)}")
    print("hist_fire=" + ",".join(format_tuple(coloring) for coloring in firing))

    pairwise = (
        len(balls[(0, 0, 0)] & balls[(2, 0, 0)]),
        len(balls[(0, 0, 0)] & balls[(1, 2, 1)]),
        len(balls[(2, 0, 0)] & balls[(1, 2, 1)]),
    )
    triple = len(balls[(0, 0, 0)] & balls[(2, 0, 0)] & balls[(1, 2, 1)])
    proper, _inversion = cubic_signed_permutations()

    checks.check(
        "g-plus-order",
        "finite G+ is exactly the 24 proper cube rotations",
        len(proper) == 24 and len(set(proper)) == 24,
    )
    checks.check(
        "center-unread",
        "the star center v is not already in U",
        V not in occupied
        and l1(V) == 3
        and l1(sub(V, (2, 0, 0))) == 5
        and l1(sub(V, (1, 2, 1))) == 3,
        residual=V in occupied,
    )
    checks.check(
        "u-geometry",
        "U is the union of three radius-2 ℓ¹ balls and has 62 sites",
        all(len(balls[seed]) == 25 for seed in SEEDS)
        and pairwise == (7, 4, 4)
        and triple == 2
        and len(occupied) == 62,
    )
    checks.check(
        "theorem-1-mask",
        "occupancy mask at v is (1,0,1,1,0,1)",
        mask == (1, 0, 1, 1, 0, 1) and "(1, 0, 1, 1, 0, 1)" in note,
    )
    checks.check(
        "theorem-1-nearest-seeds",
        "nearest seeds are lex-first among least ℓ¹ distance",
        neighbor_rows[0][1] == (0, 1, 1)
        and neighbor_rows[0][2] == (0, 0, 0)
        and neighbor_rows[1][1] == (-1, 2, 1)
        and neighbor_rows[1][2] == (1, 2, 1)
        and neighbor_rows[2][1] == (-1, 0, 1)
        and neighbor_rows[2][2] == (0, 0, 0)
        and neighbor_rows[3][1] == (-1, 1, 0)
        and neighbor_rows[3][2] == (0, 0, 0)
        and l1(sub((0, 1, 1), (0, 0, 0))) == 2
        and l1(sub((0, 1, 1), (1, 2, 1))) == 2,
    )
    checks.check(
        "theorem-1-hist-kernels",
        "history kernels use only occupancy in each neighbor's nearest-seed ball",
        neighbor_rows[0][3] == (0, 0, 0, 1, 0, 1)
        and neighbor_rows[0][4] == (Fraction(0), Fraction(-1, 3), Fraction(-1, 3))
        and neighbor_rows[0][5] is None
        and neighbor_rows[1][3] == (1, 0, 0, 0, 0, 0)
        and neighbor_rows[1][4] == (Fraction(1, 3), Fraction(0), Fraction(0))
        and neighbor_rows[1][5] == PLUS
        and neighbor_rows[2][3] == (1, 0, 0, 0, 0, 1)
        and neighbor_rows[2][4] == (Fraction(1, 3), Fraction(0), Fraction(-1, 3))
        and neighbor_rows[2][5] is None
        and neighbor_rows[3][3] == (1, 0, 0, 1, 0, 0)
        and neighbor_rows[3][4] == (Fraction(1, 3), Fraction(-1, 3), Fraction(0))
        and neighbor_rows[3][5] is None,
    )
    checks.check(
        "theorem-1-history-tuple",
        "the history 6-tuple is (tied,0,+,tied,0,tied) and not fully unique-axis",
        fragment == (None, EMPTY, PLUS, None, EMPTY, None)
        and format_fragment(fragment) == "(tied,0,+,tied,0,tied)"
        and not every_unique
        and tied_count == 3
        and "(tied, 0, +, tied, 0, tied)" in note
        and "Not every occupied neighbor has a unique-axis history label" in note,
        residual=format_fragment(fragment),
    )
    checks.check(
        "pair-census",
        "the reconstructed July-3 k=3 pair has 48 members in one chiral pair",
        len(pair) == 48
        and all(coloring.count(EMPTY) == 2 for coloring in pair)
        and all(len({coloring[0], coloring[1]}) == 2 for coloring in pair)
        and all(len({coloring[2], coloring[3]}) == 2 for coloring in pair)
        and all(len({coloring[4], coloring[5]}) == 2 for coloring in pair),
    )
    checks.check(
        "theorem-2-n-hist-fire",
        "exactly two of the eight tied-slot completions are pair members",
        len(completions) == 8
        and len(firing) == 2
        and firing
        == (
            (PLUS, EMPTY, PLUS, MINUS, EMPTY, MINUS),
            (MINUS, EMPTY, PLUS, MINUS, EMPTY, PLUS),
        )
        and "N_hist_fire = 2" in note
        and "(+,0,+,−,0,−)" in note
        and "(−,0,+,−,0,+)" in note,
        residual=len(firing),
    )

    claim_scope = (
        'claim_scope: "On the off-axis three-ball union at unread v=(-1,1,1), '
        "whether unique-axis labels from each neighbor’s nearest-seed ball "
        'form a July-3 k=3 pair member is reported. Displayed, not adopted."'
    )
    checks.check(
        "claim-scope",
        "the note reports the declared displayed claim_scope",
        claim_scope in note,
    )
    checks.check(
        "displayed-not-adopted",
        "history labels are displayed and are not written into Admissibility",
        "Displayed, not adopted" in note
        and "Do not write history labels into Admissibility" in note
        and "hypothetical_axiom_status:" in note
        and "This note authors no audit verdict" in note,
    )
    checks.check(
        "l1-not-attached",
        "the note does not attach L1 and records the failed-bar against a fourth ball",
        "Do not attach L1" in note
        and "Failed-bar: no 4th equal-radius ball" in note
        and "we attach L1" not in note_flat
        and "we add a 4th ball" not in note_flat,
    )
    checks.check(
        "not-leftover-skeworb",
        "the note is not leftover-char of the skeworb final-n orbit census",
        "not leftover-char of skeworb" in note_flat
        and "final `n`" in note
        and "nearest-seed" in note_flat,
    )
    checks.check(
        "admissibility-unedited",
        "history labels and the off-axis triple are not written into Admissibility",
        "one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations"
        in axiom_flat
        and "B_2((1,2,1))" not in axiom
        and "n_hist" not in axiom
        and "history unique-axis" not in axiom,
    )
    checks.check(
        "forbidden-phrases",
        "the forbidden rhetoric strings are absent from the note and runner",
        all(phrase not in note for phrase in FORBIDDEN)
        and all(phrase not in self_source.split("FORBIDDEN = ", 1)[0] for phrase in FORBIDDEN),
    )
    checks.check(
        "no-axiom-edit",
        "the only axiom authority is the current memo; no cache or axiom rewrite",
        "[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)" in note
        and "cache_write: false" in self_source
        and AXIOM_REL in AUDIT_INPUT_PATHS
        and "no axiom" in note_flat.lower(),
    )

    print("per_element: history unique-axis signs, eight completions, and N_hist_fire are exact")
    print("per_site: only the unread star center v is scored")
    print("per_mode: no spectral calculation")
    print("per_block: U and the six-neighbor star at v only")
    print("lattice_wide: checked and not executed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
