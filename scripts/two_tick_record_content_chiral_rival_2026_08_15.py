#!/usr/bin/env python3
"""Displayed two-tick Record-content chiral rival: tick-2 can be P-odd.

Tick 1 is occupancy-only with f_L1 given by n≠0. Tick 2 uses the readable
Record alphabet {0,+,−}. The July-3 unique k=3 pair is re-earned as a
formation predicate and left displayed, not adopted.
"""

from __future__ import annotations

import ast
import itertools
import sys
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/TWO_TICK_RECORD_CONTENT_CHIRAL_RIVAL_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/TWO_TICK_RECORD_CONTENT_CHIRAL_RIVAL_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

DIRS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
DIR_INDEX = {direction: index for index, direction in enumerate(DIRS)}
LETTERS = ("0", "+", "−")
LETTER_INDEX = {letter: index for index, letter in enumerate(LETTERS)}
REPRESENTATIVE = ("0", "+", "0", "−", "+", "−")
CLAIM_SCOPE = (
    "Whether a two-tick rival whose tick-2 neighbor alphabet is Record "
    "content {0,+,−} admits a P-odd formation predicate (the July-3 k=3 "
    "pair), while occupancy-only tick-1 cannot, is reported. Displayed, "
    "not adopted."
)
FORBIDDEN_PHRASES = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")


def normalize(text: str) -> str:
    return " ".join(text.split())


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
FULL_PERMS = tuple(perm for _matrix, _determinant, perm in RECORDS)
P_MATRIX = ((-1, 0, 0), (0, -1, 0), (0, 0, -1))
P_PERM = next(perm for matrix, _determinant, perm in RECORDS if matrix == P_MATRIX)


def act(perm: tuple[int, ...], coloring: tuple[str, ...]) -> tuple[str, ...]:
    out = [""] * 6
    for source, image in enumerate(perm):
        out[image] = coloring[source]
    return tuple(out)


def all_colorings(alphabet: tuple[str, ...]) -> tuple[tuple[str, ...], ...]:
    return tuple(itertools.product(alphabet, repeat=6))


def cycle_count(perm: tuple[int, ...]) -> int:
    seen = [False] * 6
    cycles = 0
    for start in range(6):
        if seen[start]:
            continue
        cycles += 1
        here = start
        while not seen[here]:
            seen[here] = True
            here = perm[here]
    return cycles


def burnside_orbits(perms: tuple[tuple[int, ...], ...], alphabet_size: int) -> int:
    total = sum(alphabet_size ** cycle_count(perm) for perm in perms)
    if total % len(perms) != 0:
        raise ValueError("Burnside count is not integral")
    return total // len(perms)


def orbit_of(seed: tuple[str, ...], perms: tuple[tuple[int, ...], ...]) -> frozenset[tuple[str, ...]]:
    return frozenset(act(perm, seed) for perm in perms)


def proper_equiv_to_p_image(coloring: tuple[str, ...]) -> bool:
    image = act(P_PERM, coloring)
    return any(act(perm, coloring) == image for perm in PROPER_PERMS)


def is_fully_mixed(coloring: tuple[str, ...]) -> bool:
    axis_mixed = all(coloring[2 * axis] != coloring[2 * axis + 1] for axis in range(3))
    counts = sorted(coloring.count(letter) for letter in LETTERS)
    return axis_mixed and counts == [2, 2, 2]


def occupancy(coloring: tuple[str, ...]) -> tuple[int, ...]:
    return tuple(0 if letter == "0" else 1 for letter in coloring)


def letter_map_image(
    coloring: tuple[str, ...], mapping: tuple[int, int, int]
) -> tuple[int, ...]:
    return tuple(mapping[LETTER_INDEX[letter]] for letter in coloring)


def n_of_occupancy(bits: tuple[int, ...]) -> float:
    return sum(bits) / 3


def f_l1(bits: tuple[int, ...]) -> bool:
    return n_of_occupancy(bits) != 0


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

    print("two-tick Record-content chiral rival (displayed, not adopted)")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print("construction: exact six-direction colorings; no 20-site spatial patch")

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
    record_content = "A readout value is determined by record content alone."
    record_absence = "A site with no record cannot be read."

    checks.check(
        "source-admissibility-rule",
        admissibility_rule in normalized_axiom and admissibility_rule in normalized_note,
    )
    checks.check(
        "source-distribution-sentence",
        distribution_sentence in normalized_axiom and distribution_sentence in normalized_note,
    )
    checks.check(
        "source-formation-boundary",
        formation_boundary in normalized_axiom and formation_boundary in normalized_note,
    )
    checks.check(
        "source-record-readable-content",
        "Records form." in axiom
        and record_lock in normalized_axiom
        and record_content in normalized_axiom
        and record_absence in normalized_axiom
        and record_lock in normalized_note
        and record_content in normalized_note
        and record_absence in normalized_note,
    )

    checks.check(
        "note-f-L1-is-n-nonzero-not-hamming",
        "f_L1" in note
        and "n≠0" in note
        and "not Hamming" in note
        and "Hamming-grade" in note,
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
        "Do not write the pair or V−A into Admissibility" in note
        and "hypothetical_axiom_status: no edit" in note,
    )
    checks.check(
        "note-does-not-reopen-born-compiler-or-color-unital-m3",
        "does not reopen born-compiler / color-unital-m3" in note,
    )
    checks.check(
        "note-no-forbidden-phrases",
        all(phrase not in note for phrase in FORBIDDEN_PHRASES),
    )
    checks.check(
        "note-no-spatial-patch",
        "20→" in note and "not executed" in note,
    )

    three_letter = all_colorings(LETTERS)
    two_letter = all_colorings(("0", "1"))
    checks.check(
        "alphabets-exact",
        len(three_letter) == 729 and len(two_letter) == 64 and len(RECORDS) == 48 and len(PROPER_PERMS) == 24,
        f"3^{6}={len(three_letter)}; 2^{6}={len(two_letter)}; |G|={len(RECORDS)}",
    )
    checks.check(
        "p-central-swap",
        P_PERM == (1, 0, 3, 2, 5, 4) and det3(P_MATRIX) == -1,
    )

    proper_k3 = burnside_orbits(PROPER_PERMS, 3)
    full_k3 = burnside_orbits(FULL_PERMS, 3)
    forming = orbit_of(REPRESENTATIVE, PROPER_PERMS)
    p_forming = orbit_of(act(P_PERM, REPRESENTATIVE), PROPER_PERMS)
    fully_mixed = tuple(coloring for coloring in three_letter if is_fully_mixed(coloring))
    checks.check(
        "july3-unique-k3-pair",
        proper_k3 == 57
        and full_k3 == 56
        and proper_k3 - full_k3 == 1
        and len(forming) == 24
        and len(p_forming) == 24
        and forming.isdisjoint(p_forming)
        and forming | p_forming == frozenset(fully_mixed)
        and len(fully_mixed) == 48,
        f"Burnside {proper_k3}/{full_k3}; orbit sizes {len(forming)}/{len(p_forming)}",
    )
    checks.check(
        "representative-fully-mixed",
        REPRESENTATIVE in forming
        and is_fully_mixed(REPRESENTATIVE)
        and all(is_fully_mixed(coloring) for coloring in forming)
        and all(act(P_PERM, coloring) in p_forming for coloring in forming),
        f"rep={REPRESENTATIVE}",
    )

    def f(coloring: tuple[str, ...]) -> bool:
        return coloring in forming

    n_form = sum(1 for coloring in three_letter if f(coloring))
    n_p_form = sum(1 for coloring in three_letter if f(act(P_PERM, coloring)))
    n_both = sum(
        1 for coloring in three_letter if f(coloring) and f(act(P_PERM, coloring))
    )
    checks.check(
        "theorem1-N-form-N-P-form-N-both",
        n_form == 24 and n_p_form == 24 and n_both == 0 and n_both < n_form,
        f"N_form={n_form}, N_P_form={n_p_form}, N_both={n_both}",
    )
    checks.check(
        "theorem1-f-not-P-invariant",
        any(f(coloring) != f(act(P_PERM, coloring)) for coloring in three_letter)
        and all(not f(act(P_PERM, coloring)) for coloring in forming),
    )
    checks.check(
        "note-reports-N-counts",
        "N_form" in note and "N_P_form" in note and "N_both" in note and "N_both < N_form" in note,
    )

    occ_image = {occupancy(coloring) for coloring in forming}
    p_occ_image = {act(P_PERM, bits) for bits in occ_image}
    checks.check(
        "theorem2-occupancy-projection-P-invariant",
        occ_image == p_occ_image and len(occ_image) == 12,
        f"|S_π|={len(occ_image)}",
    )

    all_maps_p_even = True
    for mapping in itertools.product((0, 1), repeat=3):
        image = {letter_map_image(coloring, mapping) for coloring in forming}
        if {act(P_PERM, bits) for bits in image} != image:
            all_maps_p_even = False
            break
    checks.check(
        "theorem2-every-two-letter-projection-P-invariant",
        all_maps_p_even,
    )

    occupancy_bits = tuple(tuple(int(bit) for bit in coloring) for coloring in two_letter)
    tick1_form = tuple(bits for bits in occupancy_bits if f_l1(bits))
    tick1_p_even = all(f_l1(bits) == f_l1(act(P_PERM, bits)) for bits in occupancy_bits)
    all_occupancy_p_related = all(
        proper_equiv_to_p_image(tuple("1" if bit else "0" for bit in bits))
        for bits in occupancy_bits
    )
    checks.check(
        "tick1-f-L1-n-nonzero",
        len(tick1_form) == 63
        and not f_l1((0, 0, 0, 0, 0, 0))
        and f_l1((1, 0, 0, 0, 0, 0))
        and n_of_occupancy((1, 1, 1, 1, 1, 1)) == 2.0,
    )
    checks.check(
        "tick1-cannot-carry-P-odd-grade",
        tick1_p_even and all_occupancy_p_related,
    )
    checks.check(
        "rival-not-identified-with-L1",
        forming != {coloring for coloring in three_letter if occupancy(coloring) != (0, 0, 0, 0, 0, 0)}
        and REPRESENTATIVE not in {("0",) * 6},
    )
    return checks.finish()


if __name__ == "__main__":
    sys.exit(main())
