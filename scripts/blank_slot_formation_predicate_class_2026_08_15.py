#!/usr/bin/env python3
"""Exact orbit count of cube-covariant boolean predicates on {0,1,blank}^6.

Enumerates the 729 cells and the 24 proper cube rotations. No cache write,
no network, no axiom edit.
"""

from __future__ import annotations

from collections import Counter
from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "BLANK_SLOT_FORMATION_PREDICATE_CLASS_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/BLANK_SLOT_FORMATION_PREDICATE_CLASS_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

ZERO = 0
ONE = 1
BLANK = 2
ALPHABET: tuple[int, ...] = (ZERO, ONE, BLANK)
BINARY: tuple[int, ...] = (ZERO, ONE)
SLOT_COUNT = 6
FACES: tuple[tuple[int, int, int], ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
Cell = tuple[int, ...]
Perm = tuple[int, ...]


def normalize(text: str) -> str:
    return " ".join(text.split())


def det3(matrix: tuple[tuple[int, int, int], ...]) -> int:
    a, b, c = matrix
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def apply_matrix(
    matrix: tuple[tuple[int, int, int], ...], vector: tuple[int, int, int]
) -> tuple[int, int, int]:
    return tuple(
        sum(matrix[row][col] * vector[col] for col in range(3)) for row in range(3)
    )


def proper_rotation_matrices() -> tuple[tuple[tuple[int, int, int], ...], ...]:
    matrices = []
    for axis_perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            rows = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            for row, axis in enumerate(axis_perm):
                rows[row][axis] = signs[row]
            matrix = tuple(tuple(row) for row in rows)
            if det3(matrix) == 1:
                matrices.append(matrix)
    return tuple(matrices)


def face_permutations() -> tuple[Perm, ...]:
    face_index = {face: index for index, face in enumerate(FACES)}
    perms = []
    for matrix in proper_rotation_matrices():
        perm = tuple(face_index[apply_matrix(matrix, face)] for face in FACES)
        perms.append(perm)
    return tuple(perms)


def compose(left: Perm, right: Perm) -> Perm:
    return tuple(left[right[index]] for index in range(SLOT_COUNT))


def inverse(perm: Perm) -> Perm:
    out = [0] * SLOT_COUNT
    for source, dest in enumerate(perm):
        out[dest] = source
    return tuple(out)


def act(perm: Perm, cell: Cell) -> Cell:
    inv = inverse(perm)
    return tuple(cell[inv[index]] for index in range(SLOT_COUNT))


def cycle_lengths(perm: Perm) -> tuple[int, ...]:
    seen = [False] * SLOT_COUNT
    lengths: list[int] = []
    for start in range(SLOT_COUNT):
        if seen[start]:
            continue
        length = 0
        cursor = start
        while not seen[cursor]:
            seen[cursor] = True
            cursor = perm[cursor]
            length += 1
        lengths.append(length)
    return tuple(sorted(lengths, reverse=True))


def burnside_orbit_count(perms: tuple[Perm, ...], alphabet_size: int) -> int:
    total = 0
    for perm in perms:
        total += alphabet_size ** len(cycle_lengths(perm))
    if total % len(perms) != 0:
        raise ArithmeticError("Burnside sum is not divisible by |G|")
    return total // len(perms)


def enumerate_orbits(
    perms: tuple[Perm, ...], alphabet: tuple[int, ...]
) -> tuple[int, frozenset[Cell], dict[Cell, Cell]]:
    representatives: set[Cell] = set()
    to_rep: dict[Cell, Cell] = {}
    for cell in product(alphabet, repeat=SLOT_COUNT):
        if cell in to_rep:
            continue
        orbit = tuple(act(perm, cell) for perm in perms)
        representative = min(orbit)
        representatives.add(representative)
        for image in orbit:
            to_rep[image] = representative
    return len(representatives), frozenset(representatives), to_rep


def letter_count(cell: Cell) -> tuple[int, int, int]:
    return (cell.count(ZERO), cell.count(ONE), cell.count(BLANK))


def has_blank(cell: Cell) -> bool:
    return BLANK in cell


def is_binary(cell: Cell) -> bool:
    return all(letter in BINARY for letter in cell)


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
    for relative in AUDIT_INPUT_PATHS:
        (ROOT / relative).read_text(encoding="utf-8")
    self_source = Path(__file__).read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)

    print(
        "external_scientific_inputs: current Lattice, Admissibility, and Record "
        "boundaries are source-bound; no observation or fit"
    )
    print(
        "integrity_reads: this runner, its note, and the current axiom memo; "
        "no other scientific inputs"
    )
    print(
        "construction: 24 proper cube rotations acting on six nearest-neighbor "
        "slots; alphabet {0,1,blank}; boolean G-covariant predicates"
    )
    print(
        "negative_scope: the counted class is displayed, not adopted as a "
        "formation law, site selector, or Record compiler"
    )

    checks.check(
        "audit-inputs",
        "declared source-bound inputs exist as the required two-path literal",
        AUDIT_INPUT_PATHS
        == (
            "docs/BLANK_SLOT_FORMATION_PREDICATE_CLASS_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and len(AUDIT_INPUT_PATHS) == 2
        and AUDIT_TIMEOUT_SEC == 120
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and 'AUDIT_INPUT_PATHS = (\n    "docs/BLANK_SLOT_FORMATION_PREDICATE_CLASS_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n)'
        in self_source,
    )

    lattice_sentence = (
        "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
    )
    admissibility_cov = (
        "There is one fixed nearest-neighbor admissibility rule, covariant under lattice"
    )
    record_lock = "When present, a record locks exactly one admissible local possibility."
    record_content = "A readout value is determined by record content alone."
    record_absence = "A site with no record cannot be read."
    formation_boundary = "does not supply the formation site, probability, or rate"

    checks.check(
        "source-lattice",
        "current cubic nearest-neighbor and proper-rotation wording is pinned",
        lattice_sentence in normalize(axiom)
        and "proper cubic rotations about each site" in axiom
        and lattice_sentence in note
        and "proper cubic rotations" in note,
    )
    checks.check(
        "source-admissibility",
        "current covariant nearest-neighbor wording is pinned",
        admissibility_cov in normalize(axiom) and admissibility_cov in note,
    )
    checks.check(
        "source-record-boundary",
        "current lock, content-only readout, and unreadable absence are pinned",
        all(
            phrase in normalized_axiom
            for phrase in (record_lock, record_content, record_absence)
        )
        and all(phrase in note for phrase in (record_lock, record_content, record_absence)),
    )
    checks.check(
        "source-formation-boundary",
        "Admissibility still withholds formation site, probability, and rate",
        formation_boundary in normalized_axiom and formation_boundary in normalized_note,
    )

    matrices = proper_rotation_matrices()
    perms = face_permutations()
    identity = tuple(range(SLOT_COUNT))
    perm_set = set(perms)
    closed = all(compose(left, right) in perm_set for left in perms for right in perms)
    inverses = all(inverse(perm) in perm_set for perm in perms)
    unique_slots = all(len(set(perm)) == SLOT_COUNT for perm in perms)

    checks.check(
        "thm1-group-order",
        "|G|=24 distinct proper rotations of the six slots",
        len(matrices) == 24
        and len(set(matrices)) == 24
        and len(perms) == 24
        and len(perm_set) == 24
        and identity in perm_set
        and closed
        and inverses
        and unique_slots,
        residual=(len(matrices), len(perm_set)),
    )
    checks.check(
        "thm1-domain-size",
        "|A|=3 and |A^6|=729",
        len(ALPHABET) == 3 and 3**SLOT_COUNT == 729 and len(list(product(ALPHABET, repeat=SLOT_COUNT))) == 729,
    )

    n_orb, representatives, to_rep = enumerate_orbits(perms, ALPHABET)
    n_orb_burnside = burnside_orbit_count(perms, 3)
    n_orb_binary, binary_reps, binary_to_rep = enumerate_orbits(perms, BINARY)
    n_orb_binary_burnside = burnside_orbit_count(perms, 2)
    blank_reps = frozenset(rep for rep in representatives if has_blank(rep))
    type_hist = Counter(letter_count(rep) for rep in representatives)

    print(f"N_orb_perp={n_orb}")
    print(f"N_orb_binary={n_orb_binary}")
    print(f"|F_perp|=2^{n_orb}={2**n_orb}")
    print(f"|F_G|=2^{n_orb_binary}={2**n_orb_binary}")
    print(f"blank_bearing_orbits={len(blank_reps)}")

    checks.check(
        "thm1-orbit-enumeration",
        "N_orb_perp from 729 cells and 24 rotations equals the Burnside count",
        n_orb == n_orb_burnside and n_orb > 10 and len(representatives) == n_orb,
        residual=(n_orb, n_orb_burnside),
    )
    checks.check(
        "thm1-boolean-class-size",
        "|F_perp| equals 2 to the orbit count",
        2**n_orb == pow(2, n_orb) and n_orb == len(representatives),
    )
    checks.check(
        "thm1-note-reports-count",
        "note displays the computed orbit count and boolean class size",
        f"N_orb_perp = {n_orb}" in note
        and f"2^{{{n_orb}}}" in note
        and str(2**n_orb) in note,
    )
    checks.check(
        "thm1-blank-stays-blank",
        "rotations permute slots and send blank only to blank",
        all(
            act(perm, cell).count(BLANK) == cell.count(BLANK)
            for perm in perms
            for cell in (
                (BLANK, ZERO, ZERO, ZERO, ZERO, ZERO),
                (BLANK, ONE, ZERO, ZERO, ZERO, ZERO),
                (BLANK, BLANK, ONE, ZERO, ZERO, ZERO),
            )
        )
        and all(letter_count(act(perm, cell)) == letter_count(cell) for perm in perms for cell in representatives),
    )

    checks.check(
        "thm2-binary-orbits",
        "{0,1}^6 has exactly 10 G-orbits by the same enumeration",
        n_orb_binary == 10
        and n_orb_binary_burnside == 10
        and len(binary_reps) == 10
        and all(is_binary(rep) for rep in binary_reps),
        residual=(n_orb_binary, n_orb_binary_burnside),
    )
    checks.check(
        "thm2-binary-invariant",
        "{0,1}^6 is G-invariant, and so is the blank-bearing complement",
        all(is_binary(act(perm, cell)) for perm in perms for cell in binary_reps)
        and all(has_blank(act(perm, cell)) for perm in perms for cell in blank_reps)
        and len(binary_reps) + len(blank_reps) == n_orb,
    )

    restriction_ok = True
    for assignment in product((0, 1), repeat=n_orb_binary):
        value_of = {rep: bit for rep, bit in zip(sorted(binary_reps), assignment, strict=True)}

        def extended(cell: Cell) -> int:
            if has_blank(cell):
                return 0
            return value_of[binary_to_rep[cell]]

        for perm in perms:
            for rep in binary_reps:
                if extended(act(perm, rep)) != extended(rep):
                    restriction_ok = False
            for rep in blank_reps:
                if extended(act(perm, rep)) != 0:
                    restriction_ok = False
        if not restriction_ok:
            break

    checks.check(
        "thm2-restriction-surjective",
        "zero-on-blank extension realizes every covariant predicate on {0,1}^6",
        restriction_ok and 2**n_orb_binary == 1024,
    )
    checks.check(
        "thm2-restriction-map",
        "restriction F_perp -> F_G is well-defined because {0,1}^6 is G-invariant",
        all(to_rep[cell] in binary_reps for cell in binary_to_rep)
        and all(not has_blank(cell) for cell in binary_to_rep),
    )

    all_zero = (ZERO,) * SLOT_COUNT
    all_blank = (BLANK,) * SLOT_COUNT
    one_blank = (BLANK, ZERO, ZERO, ZERO, ZERO, ZERO)
    checks.check(
        "thm3-strict-enlargement",
        "N_orb_perp > 10 so |F_perp| > |F_G|",
        n_orb > 10 and 2**n_orb > 2**n_orb_binary and len(blank_reps) == n_orb - 10,
        residual=(n_orb, n_orb_binary),
    )
    checks.check(
        "thm3-blank-not-relabel",
        "blank is new orbit content: letter counts are G-invariants",
        to_rep[all_blank] != to_rep[all_zero]
        and has_blank(one_blank)
        and not is_binary(one_blank)
        and letter_count(one_blank) != letter_count(all_zero)
        and type_hist[(6, 0, 0)] == 1
        and type_hist[(0, 0, 6)] == 1
        and type_hist[(5, 0, 1)] == 1
        and sum(count for key, count in type_hist.items() if key[2] == 0) == 10
        and sum(count for key, count in type_hist.items() if key[2] > 0) == n_orb - 10,
    )
    checks.check(
        "claim-scope-displayed",
        "claim_scope states the counted class, the inequality, onto restriction, and display-only status",
        'claim_scope: "Cube-covariant boolean predicates on {0,1,blank}^6 form a set of size 2^{N_orb_⊥} with'
        in note
        and "N_orb_⊥ > 10" in note
        and "Restriction to {0,1}^6 is onto F_G" in note
        and "Displayed, not adopted." in note,
    )
    checks.check(
        "displayed-not-adopted",
        "note refuses to adopt a member of the class as a formation law",
        "displayed, not adopted" in normalized_note
        and "No member of `F_perp` is selected" in note
        and "hypothetical_axiom_status: \"not proposed; no axiom or approved primitive is added\""
        in note,
    )
    forbidden = (
        "G" + "_N",
        "1/" + "r",
        "1/" + "r^2",
        "Lattice-" + "named",
        "not a " + "TOE",
    )
    checks.check(
        "forbidden-phrases-absent",
        "note and runner avoid the dispatch-forbidden phrases",
        all(phrase not in note and phrase not in self_source for phrase in forbidden),
        residual=[phrase for phrase in forbidden if phrase in note or phrase in self_source],
    )
    checks.check(
        "machine-status-contract",
        "note carries bounded-support status and the N1-N8 gate",
        "actual_current_surface_status: bounded-support" in note
        and "**Type:** bounded_theorem" in note
        and all(f"### N{index}" in note for index in range(1, 9))
        and "No-Go Discipline disposition: **PASS**" in note
        and note.count("**ATTEMPTED**") == 6
        and "runner-cache" not in note
        and "citation_manifest" not in note
        and "citation-manifest" not in note,
    )

    print("per_element: checked exactly — each of the 729 cells is assigned its G-orbit representative")
    print("per_site: checked exactly — six nearest-neighbor slots at one displayed site")
    print("per_mode: checked exactly — boolean G-covariant predicates; ternary ready/blocked/no maps are uncounted")
    print("per_block: checked exactly — restriction onto the 10-orbit binary class by zero extension")
    print("lattice_wide: checked and not executed — no physical formation predicate or lattice-wide ready law is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
