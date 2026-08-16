#!/usr/bin/env python3
"""Census all eight tick-1 {+,−} labelings of the two-cube axis sites.

Tick 1 forms by occupancy n≠0. Tick-1 lock labels are then assigned freely
in {+,−} at (1,0,0), (0,1,0), (0,0,1). Tick 2 forms by the July-3 unique
k=3 chiral pair on neighbor Record content {0,+,−}. Existing locks are not
overwritten. The census is displayed, not adopted.
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
    "docs/TWO_CUBE_TICK1_LABELING_CHIRAL_FIRE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/TWO_CUBE_TICK1_LABELING_CHIRAL_FIRE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Site = tuple[int, int, int]
Coloring = tuple[str, ...]
AXES: tuple[Site, Site, Site] = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
TICK1_SITES: tuple[Site, Site, Site] = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
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
LABELS = ("+", "−")
SEED: Site = (0, 0, 0)
SEED_CONTENT = "+"
REPRESENTATIVE: Coloring = ("0", "+", "0", "−", "+", "−")
ZERO_N = (Fraction(0), Fraction(0), Fraction(0))
CLAIM_SCOPE = (
    "On the two-cube with off-patch o=0 and seed +, whether any of the 8 "
    "tick-1 {+,−} labelings of the three axis sites makes the July-3 k=3 "
    "pair fire at tick 2 is reported. Displayed, not adopted."
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


def f_l1_bits(bits: tuple[int, ...]) -> bool:
    n = tuple(Fraction(bits[2 * axis] - bits[2 * axis + 1], 3) for axis in range(3))
    return n != ZERO_N


def neighbor_coloring(site: Site, labels: dict[Site, str]) -> Coloring:
    return tuple(labels.get(add_site(site, step), "0") for step in DIRS)


def locked_neighbor_count(site: Site, locks: frozenset[Site]) -> int:
    return sum(occupancy_bit(add_site(site, step), locks) for step in DIRS)


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


def all_labelings() -> tuple[tuple[str, str, str], ...]:
    return tuple(itertools.product(LABELS, repeat=3))


def labels_for(assignment: tuple[str, str, str]) -> dict[Site, str]:
    labels = {SEED: SEED_CONTENT}
    for site, letter in zip(TICK1_SITES, assignment):
        labels[site] = letter
    return labels


def tick2_new_sites(
    unread: tuple[Site, ...], labels: dict[Site, str]
) -> frozenset[Site]:
    return frozenset(site for site in unread if chiral_forms(neighbor_coloring(site, labels)))


def is_p_odd_set(sites: frozenset[Site]) -> bool:
    return sites != frozenset(invert_site(site) for site in sites)


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

    print("two-cube tick-1 labeling chiral-fire census (displayed, not adopted)")
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
        "note-does-not-write-labeling-rule-into-admissibility",
        "Do not write a labeling rule into Admissibility" in note
        and "hypothetical_axiom_status: no edit" in note,
    )
    checks.check(
        "note-same-two-cube-no-new-patch",
        "twelve-vertex" in note
        and "4×4×4" in note
        and "not a new patch" in note,
    )
    checks.check(
        "note-not-leftover-wav2run",
        "leftover-char of wav2run" in note and "one labeling" in note,
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

    seed_locks = frozenset({SEED})
    tick1_new = frozenset(site for site in patch if occupancy_forms(site, seed_locks))
    expected_tick1 = frozenset(TICK1_SITES)
    checks.check(
        "tick1-new-locks",
        tick1_new == expected_tick1,
        f"new={sorted(tick1_new)}",
    )
    checks.check(
        "tick1-not-hamming",
        occupancy_forms((2, 0, 0), seed_locks) is False
        and hamming_would_form((2, 0, 0), seed_locks) is False
        and f_l1_bits((1, 1, 0, 0, 0, 0)) is False
        and sum((1, 1, 0, 0, 0, 0)) != 0,
    )

    tick1_locks = seed_locks | tick1_new
    unread = tuple(sorted(site for site in patch if site not in tick1_locks))
    assignments = all_labelings()
    rows = []
    for assignment in assignments:
        labels = labels_for(assignment)
        new_sites = tick2_new_sites(unread, labels)
        colorings = tuple(neighbor_coloring(site, labels) for site in unread)
        rows.append(
            {
                "assignment": assignment,
                "new_sites": new_sites,
                "n_new": len(new_sites),
                "colorings": colorings,
                "labels": labels,
            }
        )

    print("tick1_axis_order=(1,0,0),(0,1,0),(0,0,1)")
    for row in rows:
        assignment = "".join(row["assignment"])
        new_txt = tuple(sorted(row["new_sites"]))
        print(f"labeling {assignment} N_new={row['n_new']} new={new_txt}")

    n_values = tuple(row["n_new"] for row in rows)
    firing = [row for row in rows if row["n_new"] > 0]
    n_fire = len(firing)
    any_fire = n_fire > 0
    lex_first = firing[0] if firing else None
    firer_new_sets_p_odd = tuple(is_p_odd_set(row["new_sites"]) for row in firing)

    print(f"any_fire={any_fire}")
    print(f"N_fire={n_fire}")
    if lex_first is None:
        print("lex_first_firing=none")
        print("theorem1: none of the 8 labelings has N_new>0")
    else:
        print(f"lex_first_firing={''.join(lex_first['assignment'])}")
        print(f"lex_first_new={tuple(sorted(lex_first['new_sites']))}")
        print(f"firer_new_sets_P_odd={firer_new_sets_p_odd}")

    checks.check(
        "july3-unique-k3-pair",
        len(FORMING_ORBIT) == 24
        and len(P_FORMING_ORBIT) == 24
        and FORMING_ORBIT.isdisjoint(P_FORMING_ORBIT)
        and REPRESENTATIVE in FORMING_ORBIT
        and is_fully_mixed(REPRESENTATIVE)
        and all(is_fully_mixed(coloring) for coloring in FORMING_ORBIT)
        and P_PERM == (1, 0, 3, 2, 5, 4),
    )
    checks.check(
        "theorem1-eight-labelings",
        assignments == tuple(itertools.product(LABELS, repeat=3))
        and len(assignments) == 8
        and len(rows) == 8,
        f"count={len(assignments)}",
    )
    checks.check(
        "theorem1-N-new-all-zero",
        n_values == (0,) * 8 and not any_fire,
        f"N_new={n_values}",
    )
    checks.check(
        "theorem1-none-report",
        lex_first is None
        and "none of the 8 labelings" in note
        and "N_new>0" in note,
    )
    checks.check(
        "theorem2-N-fire",
        n_fire == 0 and "N_fire = 0" in note,
        f"N_fire={n_fire}",
    )
    checks.check(
        "theorem2-among-firers-P-odd-empty-domain",
        n_fire == 0
        and firer_new_sets_p_odd == ()
        and all(is_p_odd_set(row["new_sites"]) for row in firing),
    )
    max_locked = max(locked_neighbor_count(site, tick1_locks) for site in unread)
    checks.check(
        "unread-at-most-two-locked-neighbors",
        max_locked <= 2
        and all(not is_fully_mixed(coloring) for row in rows for coloring in row["colorings"])
        and all(not chiral_forms(coloring) for row in rows for coloring in row["colorings"]),
        f"max_locked={max_locked}",
    )
    checks.check(
        "tick2-does-not-overwrite",
        all(SEED in row["labels"] and row["labels"][SEED] == SEED_CONTENT for row in rows)
        and all(tick1_new.isdisjoint(row["new_sites"]) for row in rows)
        and all(site not in tick1_locks for row in rows for site in row["new_sites"]),
    )
    sign_n_mu = ("−", "−", "−")
    checks.check(
        "wav2run-sign-n-mu-is-one-of-eight",
        sign_n_mu in assignments
        and n_vector((1, 0, 0), seed_locks) == (Fraction(-1, 3), Fraction(0), Fraction(0))
        and next(row["n_new"] for row in rows if row["assignment"] == sign_n_mu) == 0,
    )
    checks.check(
        "mutation-hamming-is-not-f-L1",
        f_l1_bits((1, 1, 0, 0, 0, 0)) is False
        and sum((1, 1, 0, 0, 0, 0)) == 2,
    )
    checks.check(
        "mutation-occupancy-tick2-is-not-this-census",
        occupancy_forms((1, 1, 0), tick1_locks)
        and occupancy_forms((2, 0, 0), tick1_locks)
        and all((1, 1, 0) not in row["new_sites"] for row in rows)
        and all((2, 0, 0) not in row["new_sites"] for row in rows),
    )
    checks.check(
        "note-reports-census",
        "N_new = 0" in note
        and "N_fire = 0" in note
        and "lex-first" in note,
    )
    checks.check(
        "theorem3-displayed-not-adopted",
        "Displayed, not adopted" in note
        and "Do not write a labeling rule into Admissibility" in note
        and "Do not attach L1" in note
        and "we adopt" not in note.lower()
        and "Codex" not in note,
    )
    return checks.finish()


if __name__ == "__main__":
    sys.exit(main())
