#!/usr/bin/env python3
"""Execute occupancy tick-1 then the July-3 k=3 pair at tick-2 on the two-cube.

The same twelve-vertex patch that L1 uses is reused. Tick 1 forms by
occupancy n≠0 and writes lock labels from sign(n_μ). Tick 2 reads neighbor
Record content in {0,+,−} and forms by the July-3 unique k=3 chiral pair.
Existing locks are not overwritten. The rival is displayed, not adopted.
"""

from __future__ import annotations

import ast
import itertools
import sys
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/TWO_CUBE_TWO_TICK_CHIRAL_RIVAL_EXECUTION_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/TWO_CUBE_TWO_TICK_CHIRAL_RIVAL_EXECUTION_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Site = tuple[int, int, int]
Coloring = tuple[str, ...]
AXES: tuple[Site, Site, Site] = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
DIRS: tuple[Site, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
DIR_INDEX = {direction: index for index, direction in enumerate(DIRS)}
LETTERS = ("0", "+", "−")
SEED: Site = (0, 0, 0)
SEED_CONTENT = "+"
DEFAULT_MULTI_AXIS_LABEL = "+"
REPRESENTATIVE: Coloring = ("0", "+", "0", "−", "+", "−")
ZERO_N = (Fraction(0), Fraction(0), Fraction(0))
CLAIM_SCOPE = (
    "On the two-cube with off-patch o=0, whether executing occupancy "
    "tick-1 then the July-3 k=3 pair at tick-2 yields a P-odd lock set "
    "while preserving tick-1 locks is reported. Displayed, not adopted."
)
FORBIDDEN_PHRASES = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")


def normalize(text: str) -> str:
    return " ".join(text.split())


def add_site(site: Site, step: Site) -> Site:
    return (site[0] + step[0], site[1] + step[1], site[2] + step[2])


def invert_site(site: Site) -> Site:
    return (-site[0], -site[1], -site[2])


def cube_a_vertices() -> frozenset[Site]:
    return frozenset((x, y, z) for x in (0, 1) for y in (0, 1) for z in (0, 1))


def cube_b_vertices() -> frozenset[Site]:
    return frozenset((x, y, z) for x in (1, 2) for y in (0, 1) for z in (0, 1))


def patch_vertices() -> frozenset[Site]:
    return cube_a_vertices() | cube_b_vertices()


def occupancy_bit(site: Site, locks: frozenset[Site]) -> int:
    if site not in patch_vertices():
        return 0
    return 1 if site in locks else 0


def n_vector(site: Site, locks: frozenset[Site]) -> tuple[Fraction, Fraction, Fraction]:
    components = []
    for axis in AXES:
        plus = occupancy_bit(add_site(site, axis), locks)
        minus = occupancy_bit(add_site(site, invert_site(axis)), locks)
        components.append(Fraction(plus - minus, 3))
    return (components[0], components[1], components[2])


def occupancy_forms(site: Site, locks: frozenset[Site]) -> bool:
    if site in locks or site not in patch_vertices():
        return False
    return n_vector(site, locks) != ZERO_N


def hamming_would_form(site: Site, locks: frozenset[Site]) -> bool:
    if site in locks or site not in patch_vertices():
        return False
    return sum(occupancy_bit(add_site(site, step), locks) for step in DIRS) != 0


def occupancy_tuple(site: Site, locks: frozenset[Site]) -> tuple[int, ...]:
    return tuple(occupancy_bit(add_site(site, step), locks) for step in DIRS)


def act_bits(perm: tuple[int, ...], bits: tuple[int, ...]) -> tuple[int, ...]:
    out = [0] * 6
    for source, image in enumerate(perm):
        out[image] = bits[source]
    return tuple(out)


def f_l1_bits(bits: tuple[int, ...]) -> bool:
    n = tuple(Fraction(bits[2 * axis] - bits[2 * axis + 1], 3) for axis in range(3))
    return n != ZERO_N


def lock_label(site: Site, locks: frozenset[Site]) -> str:
    n = n_vector(site, locks)
    nonzero = [(axis, component) for axis, component in zip(AXES, n) if component != 0]
    if len(nonzero) == 1:
        component = nonzero[0][1]
        if component > 0:
            return "+"
        if component < 0:
            return "−"
    return DEFAULT_MULTI_AXIS_LABEL


def neighbor_coloring(site: Site, labels: dict[Site, str]) -> Coloring:
    colors = []
    for step in DIRS:
        neighbor = add_site(site, step)
        colors.append(labels.get(neighbor, "0"))
    return tuple(colors)


def det3(matrix: tuple[tuple[int, int, int], ...]) -> int:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def matvec(
    matrix: tuple[tuple[int, int, int], ...], vector: tuple[int, int, int]
) -> tuple[int, int, int]:
    return tuple(sum(matrix[row][col] * vector[col] for col in range(3)) for row in range(3))


def cubic_records() -> tuple[tuple[tuple[tuple[int, int, int], ...], int, tuple[int, ...]], ...]:
    records = []
    seen: set[tuple[tuple[int, int, int], ...]] = set()
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            for row, col in enumerate(perm):
                matrix[row][col] = signs[row]
            key = tuple(tuple(row) for row in matrix)
            if key in seen:
                continue
            seen.add(key)
            direction_perm = tuple(DIR_INDEX[matvec(key, direction)] for direction in DIRS)
            records.append((key, det3(key), direction_perm))
    return tuple(records)


RECORDS = cubic_records()
PROPER_PERMS = tuple(perm for _matrix, determinant, perm in RECORDS if determinant == 1)
P_MATRIX = ((-1, 0, 0), (0, -1, 0), (0, 0, -1))
P_PERM = next(perm for matrix, _determinant, perm in RECORDS if matrix == P_MATRIX)


def act_color(perm: tuple[int, ...], coloring: Coloring) -> Coloring:
    out = [""] * 6
    for source, image in enumerate(perm):
        out[image] = coloring[source]
    return tuple(out)


def orbit_of(seed: Coloring, perms: tuple[tuple[int, ...], ...]) -> frozenset[Coloring]:
    return frozenset(act_color(perm, seed) for perm in perms)


FORMING_ORBIT = orbit_of(REPRESENTATIVE, PROPER_PERMS)
P_FORMING_ORBIT = orbit_of(act_color(P_PERM, REPRESENTATIVE), PROPER_PERMS)


def is_fully_mixed(coloring: Coloring) -> bool:
    axis_mixed = all(coloring[2 * axis] != coloring[2 * axis + 1] for axis in range(3))
    counts = sorted(coloring.count(letter) for letter in LETTERS)
    return axis_mixed and counts == [2, 2, 2]


def chiral_forms(coloring: Coloring) -> bool:
    return coloring in FORMING_ORBIT


def audit_input_literal() -> tuple[str, ...]:
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id == "AUDIT_INPUT_PATHS":
                value = ast.literal_eval(node.value)
                if not isinstance(value, tuple) or not all(isinstance(item, str) for item in value):
                    raise TypeError("AUDIT_INPUT_PATHS must be a tuple of strings")
                return value
    raise RuntimeError("AUDIT_INPUT_PATHS assignment not found")


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, condition: bool, detail: str = "") -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        suffix = f"  ({detail})" if detail else ""
        print(f"{'PASS' if ok else 'FAIL'}: {label}{suffix}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)
    patch = patch_vertices()

    print("two-cube two-tick chiral rival execution (displayed, not adopted)")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print("construction: same twelve-vertex two-cube; no 4x4x4 or other new patch")

    declared = audit_input_literal()
    checks.check(
        "audit-input-paths-exact-literals",
        declared == AUDIT_INPUT_PATHS == (NOTE_REL, AXIOM_REL),
        f"declared={declared}",
    )
    checks.check(
        "audit-input-paths-exist",
        all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )
    checks.check("audit-timeout-declared", AUDIT_TIMEOUT_SEC == 120)
    checks.check("note-claim-scope", CLAIM_SCOPE in normalize(note.replace("`", "")))

    admissibility_rule = (
        "There is one fixed nearest-neighbor admissibility rule, covariant under lattice "
        "translations and proper cubic rotations."
    )
    distribution_sentence = (
        "For each site, the probability distribution over the possibilities is "
        "determined by, and varies with, the nearest-neighbor conditions."
    )
    formation_boundary = "it does not supply the formation site, probability, or rate."
    record_lock = "When present, a record locks exactly one admissible local possibility."
    record_permanence = "A site never carries more than one record; records are permanent."
    record_content = "A readout value is determined by record content alone."
    record_absence = "A site with no record cannot be read."

    checks.check(
        "source-admissibility",
        admissibility_rule in normalized_axiom
        and distribution_sentence in normalized_axiom
        and admissibility_rule in normalized_note
        and distribution_sentence in normalized_note,
    )
    checks.check(
        "source-formation-boundary",
        formation_boundary in normalized_axiom and formation_boundary in normalized_note,
    )
    checks.check(
        "source-record",
        "Records form." in axiom
        and record_lock in normalized_axiom
        and record_permanence in normalized_axiom
        and record_content in normalized_axiom
        and record_absence in normalized_axiom
        and record_lock in normalized_note
        and record_permanence in normalized_note
        and record_content in normalized_note
        and record_absence in normalized_note,
    )
    checks.check(
        "note-f-L1-is-n-nonzero-not-hamming",
        "f_L1" in note and "n≠0" in note and "not Hamming" in note,
    )
    checks.check(
        "note-displayed-not-adopted",
        "Displayed, not adopted" in note and "displayed, not adopted" in note,
    )
    checks.check(
        "note-does-not-attach-L1",
        "does not attach L1" in note and "Do not attach L1" in note,
    )
    checks.check(
        "note-does-not-write-pair-into-admissibility",
        "Do not write the pair into Admissibility" in note
        and "hypothetical_axiom_status: no edit" in note,
    )
    checks.check(
        "note-same-two-cube-no-new-patch",
        "twelve-vertex" in note
        and "4×4×4" in note
        and "not a new patch" in note,
    )
    checks.check(
        "note-no-forbidden-phrases",
        all(phrase not in note for phrase in FORBIDDEN_PHRASES),
    )

    checks.check("patch-twelve-vertices", len(patch) == 12)
    checks.check(
        "off-patch-occupancy-zero",
        occupancy_bit((-1, 0, 0), frozenset({SEED})) == 0
        and occupancy_bit((0, -1, 0), frozenset({SEED})) == 0
        and occupancy_bit((3, 0, 0), frozenset({SEED})) == 0,
    )
    checks.check(
        "empty-occupancy-fixed-point",
        not any(occupancy_forms(site, frozenset()) for site in patch),
    )

    seed_locks = frozenset({SEED})
    tick1_new = frozenset(site for site in patch if occupancy_forms(site, seed_locks))
    expected_tick1 = frozenset({(1, 0, 0), (0, 1, 0), (0, 0, 1)})
    checks.check(
        "tick1-new-locks",
        tick1_new == expected_tick1,
        f"new={sorted(tick1_new)}",
    )

    tick1_labels = {SEED: SEED_CONTENT}
    for site in tick1_new:
        tick1_labels[site] = lock_label(site, seed_locks)
    checks.check(
        "tick1-labels-from-sign-n-mu",
        tick1_labels[(1, 0, 0)] == "−"
        and tick1_labels[(0, 1, 0)] == "−"
        and tick1_labels[(0, 0, 1)] == "−"
        and n_vector((1, 0, 0), seed_locks) == (Fraction(-1, 3), Fraction(0), Fraction(0)),
        f"labels={tick1_labels}",
    )
    checks.check(
        "tick1-not-hamming",
        occupancy_forms((2, 0, 0), seed_locks) is False
        and hamming_would_form((2, 0, 0), seed_locks) is False
        and f_l1_bits((1, 1, 0, 0, 0, 0)) is False
        and sum((1, 1, 0, 0, 0, 0)) != 0,
    )

    tick1_locks = seed_locks | tick1_new
    tick1_predicate_p_even = all(
        f_l1_bits(occupancy_tuple(site, seed_locks))
        == f_l1_bits(act_bits(P_PERM, occupancy_tuple(site, seed_locks)))
        for site in patch
    )
    checks.check(
        "theorem1-tick1-lock-set-P-even",
        tick1_predicate_p_even
        and tick1_new == frozenset(site for site in patch if occupancy_forms(site, seed_locks)),
    )

    unread_after_tick1 = sorted(site for site in patch if site not in tick1_locks)
    colorings = {site: neighbor_coloring(site, tick1_labels) for site in unread_after_tick1}
    tick2_new = frozenset(site for site, coloring in colorings.items() if chiral_forms(coloring))
    n_new = len(tick2_new)
    tick2_locks = tick1_locks | tick2_new
    tick2_labels = dict(tick1_labels)
    for site in tick2_new:
        tick2_labels[site] = DEFAULT_MULTI_AXIS_LABEL
    p_tick2 = frozenset(invert_site(site) for site in tick2_locks)
    tick2_p_odd = tick2_locks != p_tick2

    print(f"N_new={n_new}")
    print(f"tick2_lock_set={tuple(sorted(tick2_locks))}")
    print(f"P_of_tick2_lock_set={tuple(sorted(p_tick2))}")
    print(f"tick2_lock_set_P_odd={tick2_p_odd}")

    checks.check(
        "july3-unique-k3-pair",
        len(FORMING_ORBIT) == 24
        and len(P_FORMING_ORBIT) == 24
        and FORMING_ORBIT.isdisjoint(P_FORMING_ORBIT)
        and REPRESENTATIVE in FORMING_ORBIT
        and is_fully_mixed(REPRESENTATIVE)
        and P_PERM == (1, 0, 3, 2, 5, 4),
    )
    checks.check("theorem2-N-new", n_new == 0, f"N_new={n_new}")
    checks.check(
        "theorem2-lock-set-and-P-of-set",
        tick2_locks == tick1_locks
        and p_tick2 == frozenset({(0, 0, 0), (-1, 0, 0), (0, -1, 0), (0, 0, -1)})
        and tick2_p_odd,
        f"P_odd={tick2_p_odd}",
    )
    checks.check(
        "theorem2-pair-does-not-fire",
        all(not chiral_forms(coloring) for coloring in colorings.values())
        and all(not chiral_forms(act_color(P_PERM, coloring)) for coloring in colorings.values())
        and all(not is_fully_mixed(coloring) for coloring in colorings.values()),
    )
    checks.check(
        "theorem1-permanence",
        tick1_locks.issubset(tick2_locks)
        and all(tick2_labels[site] == tick1_labels[site] for site in tick1_locks)
        and tick1_new.isdisjoint(tick2_new),
    )
    checks.check(
        "tick2-does-not-overwrite",
        all(site not in tick1_locks for site in tick2_new)
        and SEED in tick2_locks
        and tick2_labels[SEED] == SEED_CONTENT,
    )
    checks.check(
        "note-reports-N-new-and-P-odd-pair",
        "N_new" in note
        and "N_new = 0" in note
        and "tick-2 lock set" in note
        and "P of that set" in note,
    )
    checks.check(
        "theorem3-displayed-rival",
        "Displayed rival execution" in note
        and "not adopted" in note
        and "we adopt" not in note.lower()
        and "Codex" not in note,
    )
    checks.check(
        "mutation-hamming-is-not-f-L1",
        f_l1_bits((1, 1, 0, 0, 0, 0)) is False
        and sum((1, 1, 0, 0, 0, 0)) == 2,
    )
    checks.check(
        "mutation-L1-occupancy-tick2-is-not-this-execution",
        occupancy_forms((1, 1, 0), tick1_locks)
        and occupancy_forms((2, 0, 0), tick1_locks)
        and (1, 1, 0) not in tick2_new
        and (2, 0, 0) not in tick2_new,
    )
    return checks.finish()


if __name__ == "__main__":
    sys.exit(main())
