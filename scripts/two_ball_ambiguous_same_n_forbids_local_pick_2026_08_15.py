#!/usr/bin/env python3
"""Equal n on two ambiguous neighbors forbids every local-in-n pick.

U = B_2(0) ∪ B_2((2,0,0)) is treated as already locked. The unread center is
v = (1, −1, 1). The two occupied neighbors with |supp n| ≠ 1 carry the same
kernel. Every map f(n) → {+, −} therefore assigns them the same letter. Both
July-3 firing completions assign opposite letters on those slots, so
N_same_label_fire = 0. Displayed, not adopted. No cache is written.
"""

from __future__ import annotations

import itertools
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "TWO_BALL_AMBIGUOUS_SAME_N_FORBIDS_LOCAL_PICK_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/TWO_BALL_AMBIGUOUS_SAME_N_FORBIDS_LOCAL_PICK_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Point = tuple[int, int, int]
Coloring = tuple[int, ...]

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
V: Point = (1, -1, 1)
P_SHIFT: Point = (2, 0, 0)
FORBIDDEN = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")


def normalize(text: str) -> str:
    return " ".join(text.split())


def add(left: Point, right: Point) -> Point:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def sub(left: Point, right: Point) -> Point:
    return (left[0] - right[0], left[1] - right[1], left[2] - right[2])


def l1(point: Point) -> int:
    return abs(point[0]) + abs(point[1]) + abs(point[2])


def ball(center: Point, radius: int) -> frozenset[Point]:
    sites: set[Point] = set()
    span = range(-radius, radius + 1)
    for x, y, z in itertools.product(span, repeat=3):
        site = add(center, (x, y, z))
        if l1(sub(site, center)) <= radius:
            sites.add(site)
    return frozenset(sites)


def locked_union() -> frozenset[Point]:
    return ball((0, 0, 0), 2) | ball(P_SHIFT, 2)


def occupancy_tuple(site: Point, occupied: frozenset[Point]) -> Coloring:
    return tuple(int(add(site, direction) in occupied) for direction in DIRS)


def dipole(occ: Coloring) -> tuple[Fraction, Fraction, Fraction]:
    return (
        Fraction(occ[0] - occ[1], 3),
        Fraction(occ[2] - occ[3], 3),
        Fraction(occ[4] - occ[5], 3),
    )


def unique_axis_label(n: tuple[Fraction, Fraction, Fraction]) -> int | None:
    support = [index for index, value in enumerate(n) if value != 0]
    if len(support) != 1:
        return None
    return PLUS if n[support[0]] > 0 else MINUS


def unique_axis_fragment(center: Point, occupied: frozenset[Point]) -> tuple[int | None, ...]:
    labels: list[int | None] = []
    for direction in DIRS:
        neighbor = add(center, direction)
        if neighbor not in occupied:
            labels.append(EMPTY)
            continue
        label = unique_axis_label(dipole(occupancy_tuple(neighbor, occupied)))
        labels.append(label)
    return tuple(labels)


def completions_of(fragment: tuple[int | None, ...]) -> tuple[Coloring, ...]:
    free = [index for index, slot in enumerate(fragment) if slot is None]
    if len(free) != 2:
        raise RuntimeError(f"expected two ambiguous slots, found {len(free)}")
    out: list[Coloring] = []
    for left, right in itertools.product((PLUS, MINUS), repeat=2):
        coloring = [EMPTY if slot is None else slot for slot in fragment]
        coloring[free[0]] = left
        coloring[free[1]] = right
        out.append(tuple(coloring))
    return tuple(out)


def local_in_n_completions(
    fragment: tuple[int | None, ...],
    kernels: tuple[tuple[Fraction, Fraction, Fraction], ...],
) -> tuple[Coloring, ...]:
    free = [index for index, slot in enumerate(fragment) if slot is None]
    if len(free) != 2:
        raise RuntimeError(f"expected two ambiguous slots, found {len(free)}")
    domain = tuple(dict.fromkeys(kernels))
    out: list[Coloring] = []
    for values in itertools.product((PLUS, MINUS), repeat=len(domain)):
        assigned = dict(zip(domain, values, strict=True))
        coloring = [EMPTY if slot is None else slot for slot in fragment]
        for slot_index, kernel in zip(free, kernels, strict=True):
            coloring[slot_index] = assigned[kernel]
        out.append(tuple(coloring))
    return tuple(dict.fromkeys(out))


def det3(matrix: tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]) -> int:
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
    matrix: tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]
) -> tuple[int, ...]:
    return tuple(DIR_INDEX[mat_vec(matrix, direction)] for direction in DIRS)


def act_col(perm: tuple[int, ...], coloring: Coloring) -> Coloring:
    out = [0] * 6
    for source, image in enumerate(perm):
        out[image] = coloring[source]
    return tuple(out)


def cubic_signed_permutations() -> tuple[
    list[tuple[int, ...]],
    list[tuple[int, ...]],
    tuple[int, ...],
]:
    records: list[tuple[tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]], int]] = []
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
    full = [direction_perm(matrix) for matrix, _det in records]
    inversion = ((-1, 0, 0), (0, -1, 0), (0, 0, -1))
    return proper, full, direction_perm(inversion)


def july3_k3_pair() -> frozenset[Coloring]:
    proper, _full, inversion = cubic_signed_permutations()
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


def format_n(n: tuple[Fraction, Fraction, Fraction]) -> str:
    return "(" + ",".join(str(component) for component in n) + ")"


def format_fragment(fragment: tuple[int | None, ...]) -> str:
    parts = []
    for slot in fragment:
        if slot is None:
            parts.append("*")
        else:
            parts.append(LETTER[slot])
    return "(" + ",".join(parts) + ")"


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool, residual: object | None = None) -> None:
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
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)
    for relative in AUDIT_INPUT_PATHS:
        (ROOT / relative).read_text(encoding="utf-8")

    print(
        "external_scientific_inputs: current Lattice, Qubit, Admissibility, "
        "and Record sentences plus the July-3 pair construction reconstructed locally"
    )
    print("integrity_reads: this runner, its note, and the current axiom memo; no cache written")
    print("construction: U=B_2(0)∪B_2((2,0,0)), unread v=(1,−1,1), equal n on two ambiguous neighbors")
    print("negative_scope: displayed local-in-n obstruction only; not adopted; L1 not attached")

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/TWO_BALL_AMBIGUOUS_SAME_N_FORBIDS_LOCAL_PICK_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and AUDIT_TIMEOUT_SEC == 120
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file(),
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
        lattice_sentence in normalized_axiom and lattice_sentence in note,
    )
    checks.check(
        "source-admissibility",
        "current local-distribution wording is pinned",
        admissibility_sentence in normalized_axiom and admissibility_sentence in normalized_note,
    )
    checks.check(
        "source-formation-boundary",
        "formation site/probability/rate remains outside Admissibility",
        formation_boundary in normalized_axiom and formation_boundary in note,
    )
    checks.check(
        "source-qubit",
        "Qubit remains M_2(C)",
        qubit_sentence in normalized_axiom
        and qubit_sentence in note
        and "Qubit remains `M_2(C)`" in note,
    )
    checks.check(
        "source-record",
        "lock, permanence, content-only readout, and unreadability at absence are pinned",
        all(
            phrase in normalized_axiom
            for phrase in (record_lock, record_perm, record_content, record_absence)
        )
        and all(phrase in note for phrase in (record_lock, record_perm, record_content, record_absence)),
    )

    occupied = locked_union()
    mask = occupancy_tuple(V, occupied)
    fragment = unique_axis_fragment(V, occupied)
    pair = july3_k3_pair()
    four = completions_of(fragment)
    firing = tuple(coloring for coloring in four if coloring in pair)
    ambiguous: list[tuple[Point, Coloring, tuple[Fraction, Fraction, Fraction]]] = []
    for direction in DIRS:
        neighbor = add(V, direction)
        if neighbor not in occupied:
            continue
        occ = occupancy_tuple(neighbor, occupied)
        n_vec = dipole(occ)
        if unique_axis_label(n_vec) is None:
            ambiguous.append((neighbor, occ, n_vec))
    kernels = tuple(n_vec for _w, _occ, n_vec in ambiguous)
    local_completions = local_in_n_completions(fragment, kernels)
    same_label_fire = tuple(coloring for coloring in local_completions if coloring in firing)
    opposite_on_fire = all(coloring[0] != coloring[1] for coloring in firing)
    any_f_same_label = all(coloring[0] == coloring[1] for coloring in local_completions)

    print(f"U_card={len(occupied)}")
    print(f"v_in_U={V in occupied}")
    print(f"occupancy_mask={mask}")
    print(f"unique_axis_fragment={format_fragment(fragment)}")
    print("ambiguous_n=" + ";".join(
        f"w={neighbor} occ={occ} n={format_n(n_vec)}"
        for neighbor, occ, n_vec in ambiguous
    ))
    print("local_in_n=" + ",".join(format_tuple(coloring) for coloring in local_completions))
    print(f"N_pair={len(pair)}")
    print("firing=" + ",".join(format_tuple(coloring) for coloring in firing))
    print(f"N_same_label_fire={len(same_label_fire)}")

    checks.check(
        "center-unread",
        "the star center v is not already in U",
        V not in occupied and l1(V) == 3 and l1(sub(V, P_SHIFT)) == 3,
        residual=V in occupied,
    )
    checks.check(
        "u-cardinality",
        "the two radius-two balls union to 43 locked sites",
        len(occupied) == 43 and len(ball((0, 0, 0), 2)) == 25 and len(ball(P_SHIFT, 2)) == 25,
    )
    checks.check(
        "occupancy-mask",
        "occupied nearest neighbors of v are exactly +x,−x,+y,−z",
        mask == (1, 1, 1, 0, 0, 1),
    )
    checks.check(
        "unique-axis-fragment",
        "unique-axis labels are ambiguous, ambiguous, −, 0, 0, +",
        fragment == (None, None, MINUS, EMPTY, EMPTY, PLUS),
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
        "theorem-1-same-n",
        "the two ambiguous neighbors have equal n=(0,1/3,−1/3)",
        len(ambiguous) == 2
        and ambiguous[0][0] == add(V, (1, 0, 0))
        and ambiguous[1][0] == add(V, (-1, 0, 0))
        and ambiguous[0][2] == ambiguous[1][2]
        and all(
            n_vec == (Fraction(0, 1), Fraction(1, 3), Fraction(-1, 3))
            for _w, _occ, n_vec in ambiguous
        )
        and all(occ == (0, 0, 1, 0, 0, 1) for _w, occ, _n in ambiguous),
    )
    checks.check(
        "theorem-1-any-f-same-label",
        "any map f(n)→{+,−} assigns the two ambiguous neighbors the same letter",
        any_f_same_label
        and local_completions
        == (
            (PLUS, PLUS, MINUS, EMPTY, EMPTY, PLUS),
            (MINUS, MINUS, MINUS, EMPTY, EMPTY, PLUS),
        ),
    )
    checks.check(
        "theorem-2-opposite-on-fire",
        "both firing 6-tuples have opposite labels on +x and −x",
        opposite_on_fire
        and firing
        == (
            (PLUS, MINUS, MINUS, EMPTY, EMPTY, PLUS),
            (MINUS, PLUS, MINUS, EMPTY, EMPTY, PLUS),
        )
        and "(+,−,−,0,0,+)" in note
        and "(−,+,−,0,0,+)" in note,
    )
    checks.check(
        "theorem-2-n-same-label-fire",
        "no local-in-n completion is a firing completion",
        len(same_label_fire) == 0
        and "N_same_label_fire = 0" in note
        and set(local_completions).isdisjoint(firing),
        residual=len(same_label_fire),
    )

    claim_scope = (
        "On U at unread v=(1,−1,1), whether the two ambiguous neighbors have "
        "equal n, and whether that forbids every local-in-n labeling from being "
        "a July-3 pair member, is reported. Displayed, not adopted."
    )
    checks.check(
        "claim-scope",
        "the note reports the declared displayed claim_scope",
        claim_scope in note,
    )
    checks.check(
        "displayed-not-adopted",
        "the note keeps the obstruction displayed and does not write a non-local pick",
        "Displayed, not adopted" in note
        and "does not write a non-local pick into Admissibility" in normalized_note
        and 'hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"'
        in note
        and "This note authors no audit verdict" in note,
    )
    checks.check(
        "l1-not-attached",
        "the note does not attach L1",
        "Do not attach L1" in note
        and "not attached" in normalized_note
        and "we attach L1" not in normalized_note,
    )
    checks.check(
        "not-leftover-ambpick",
        "the note is the equal-n obstruction, not leftover-char of one displayed pick",
        "not leftover-char of ambpick (that scored one displayed pick)" in normalized_note,
    )
    checks.check(
        "forbidden-absent",
        "the note avoids the dispatch-forbidden phrases",
        all(phrase not in note for phrase in FORBIDDEN),
    )
    checks.check(
        "canonical-nonmutation",
        "the axiom memo does not contain the displayed local-in-n obstruction as axiom text",
        "local-in-n" not in axiom
        and "N_same_label_fire" not in axiom
        and "we adopt" not in normalized_note.lower(),
    )

    print("per_element: equal n, opposite firing labels, and N_same_label_fire are exact")
    print("per_site: only the unread star center v is scored")
    print("per_mode: no spectral calculation")
    print("per_block: U and the six-neighbor star at v only")
    print("lattice_wide: checked and not executed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
