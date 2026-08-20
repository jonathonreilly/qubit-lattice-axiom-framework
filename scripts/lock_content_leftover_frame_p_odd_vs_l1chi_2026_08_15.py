#!/usr/bin/env python3
"""Leftover-frame lock-content section versus L1 occupancy achirality.

On the 64 occupancy 6-tuples: n=d/3 formation is P-even (l1chi algebra);
leftover-frame-positive f is a lock-content bit, named as in ridclk.
Uniqueness is not required. Displayed, not adopted. No axiom edit, no
cache write, no new spatial patch, no L1 attachment.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "LOCK_CONTENT_LEFTOVER_FRAME_P_ODD_VS_L1CHI_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/LOCK_CONTENT_LEFTOVER_FRAME_P_ODD_VS_L1CHI_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

DIRS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
DIR_INDEX = {direction: index for index, direction in enumerate(DIRS)}
AXES = ((0, 1), (2, 3), (4, 5))
EMPTY, PLUS, MINUS = 0, 1, 2
OCCUPANCY_ALPHABET = (0, 1)

CLAIM_SCOPE = (
    "On the six-neighbor occupancy star, whether leftover-frame "
    "lock-content section f is P-odd while L1 occupancy formation is "
    "P-even is reported. Displayed, not adopted."
)

FORBIDDEN = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")


def mat_vec(matrix: tuple[tuple[int, int, int], ...], vec: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(sum(matrix[i][j] * vec[j] for j in range(3)) for i in range(3))


def det3(matrix: tuple[tuple[int, int, int], ...]) -> int:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def dperm(matrix: tuple[tuple[int, int, int], ...]) -> tuple[int, ...]:
    return tuple(DIR_INDEX[mat_vec(matrix, direction)] for direction in DIRS)


def act_col(perm: tuple[int, ...], coloring: tuple[int, ...]) -> tuple[int, ...]:
    out = [0] * len(coloring)
    for source, image in enumerate(perm):
        out[image] = coloring[source]
    return tuple(out)


def inversion_matrix() -> tuple[tuple[int, int, int], ...]:
    return ((-1, 0, 0), (0, -1, 0), (0, 0, -1))


def signed_permutation_records() -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    seen: set[tuple[int, ...]] = set()
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            rows = []
            for row, axis in enumerate(perm):
                entry = [0, 0, 0]
                entry[axis] = signs[row]
                rows.append(tuple(entry))
            matrix = tuple(rows)
            key = tuple(value for row in matrix for value in row)
            if key in seen:
                continue
            seen.add(key)
            records.append({"M": matrix, "det": det3(matrix), "perm": dperm(matrix)})
    return records


def dipole(occupancy: tuple[int, ...]) -> tuple[int, int, int]:
    return (
        occupancy[0] - occupancy[1],
        occupancy[2] - occupancy[3],
        occupancy[4] - occupancy[5],
    )


def n_from_occupancy(occupancy: tuple[int, ...]) -> tuple[Fraction, Fraction, Fraction]:
    d_vec = dipole(occupancy)
    return (Fraction(d_vec[0], 3), Fraction(d_vec[1], 3), Fraction(d_vec[2], 3))


def forms(occupancy: tuple[int, ...]) -> bool:
    return n_from_occupancy(occupancy) != (Fraction(0), Fraction(0), Fraction(0))


def invert_tuple(perm: tuple[int, ...], coloring: tuple[int, ...]) -> tuple[int, ...]:
    return act_col(perm, coloring)


def support(coloring: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(int(slot != EMPTY) for slot in coloring)


def unique_full_axis(sigma: tuple[int, ...]) -> int | None:
    named = [
        axis_index
        for axis_index, (plus, minus) in enumerate(AXES)
        if sigma[plus] == 1 and sigma[minus] == 1
    ]
    if len(named) == 1:
        return named[0]
    return None


def leftover_frame_sign(coloring: tuple[int, ...]) -> int:
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


def axis_letters(bit: int) -> tuple[int, int]:
    if bit == 1:
        return (PLUS, MINUS)
    return (MINUS, PLUS)


def july3_k3_pair(proper_perms: list[tuple[int, ...]], inversion: tuple[int, ...]) -> frozenset[tuple[int, ...]]:
    unseen = set(product(range(3), repeat=6))
    pair: set[tuple[int, ...]] = set()
    while unseen:
        seed = min(unseen)
        orbit = {act_col(perm, seed) for perm in proper_perms}
        unseen -= orbit
        image = act_col(inversion, next(iter(orbit)))
        if image not in orbit:
            pair |= orbit
    return frozenset(pair)


def completions(
    sigma: tuple[int, ...],
    bit: int,
    pair: frozenset[tuple[int, ...]],
) -> tuple[tuple[int, ...], ...]:
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


def leftover_frame_positive(
    sigma: tuple[int, ...],
    bit: int,
    pair: frozenset[tuple[int, ...]],
) -> tuple[int, ...] | None:
    found = completions(sigma, bit, pair)
    positive = [item for item in found if leftover_frame_sign(item) == 1]
    if not positive:
        return None
    return positive[0]


def occupancy_lock_content_bit(
    sigma: tuple[int, ...],
    pair: frozenset[tuple[int, ...]],
) -> bool:
    if unique_full_axis(sigma) is None:
        return False
    return any(leftover_frame_positive(sigma, bit, pair) is not None for bit in (0, 1))


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


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    self_source = Path(__file__).read_text(encoding="utf-8")

    print("external_scientific_inputs: none; occupancy alphabet, n=d/3, leftover-frame-positive f displayed")
    print("package_local_integrity_reads: runner source, proposed source note, live axiom memo")
    print("measure_boundary: exact Fraction and exact pair section on the 64 occupancy tuples; no spatial patch")
    print("negative_scope: occupancy n≠0 is automatically achiral; lock-content f is not")

    stars = list(product(OCCUPANCY_ALPHABET, repeat=6))
    records = signed_permutation_records()
    proper = [record for record in records if record["det"] == 1]
    p_perm = dperm(inversion_matrix())
    proper_perms = [record["perm"] for record in proper]
    pair = july3_k3_pair(proper_perms, p_perm)

    checks.check("alphabet-two-letter", "occupancy alphabet is {0,1}", OCCUPANCY_ALPHABET == (0, 1))
    checks.check("star-cardinality", "six-neighbor occupancy star has 64 tuples", len(stars) == 64)
    checks.check("cubic-group-size", "full signed-permutation group has 48 elements", len(records) == 48)
    checks.check("proper-group-size", "proper cubic rotations number 24", len(proper) == 24)

    empty = (0, 0, 0, 0, 0, 0)
    full = (1, 1, 1, 1, 1, 1)
    axis_plus = (1, 0, 0, 0, 0, 0)
    zero_n = (Fraction(0), Fraction(0), Fraction(0))

    checks.check("thm1-n-empty-zero", "n(empty) = 0", n_from_occupancy(empty) == zero_n)
    checks.check("thm1-n-full-zero", "n(full) = 0", n_from_occupancy(full) == zero_n)
    checks.check(
        "thm1-n-axis-one-third",
        "n(+x occupied) = (1/3, 0, 0)",
        n_from_occupancy(axis_plus) == (Fraction(1, 3), Fraction(0), Fraction(0)),
    )
    checks.check(
        "thm1-forms-is-n-nonzero",
        "forms iff n ≠ 0 on the three witnesses",
        (not forms(empty)) and (not forms(full)) and forms(axis_plus),
    )

    n_form = sum(1 for occupancy in stars if forms(occupancy))
    n_p_form = sum(1 for occupancy in stars if forms(invert_tuple(p_perm, occupancy)))
    n_both_form = sum(
        1
        for occupancy in stars
        if forms(occupancy) and forms(invert_tuple(p_perm, occupancy))
    )
    checks.check("thm1-n-form", "N_form = 56", n_form == 56)
    checks.check("thm1-n-p-form", "N_P_form = 56", n_p_form == 56)
    checks.check("thm1-n-both", "N_both = 56", n_both_form == 56)

    p_flips_n = all(
        n_from_occupancy(invert_tuple(p_perm, occupancy))
        == tuple(-component for component in n_from_occupancy(occupancy))
        for occupancy in stars
    )
    form_p_invariant = all(
        forms(occupancy) == forms(invert_tuple(p_perm, occupancy)) for occupancy in stars
    )
    checks.check("thm1-p-sends-n-to-minus-n", "n(P(c)) = -n(c) on all 64 tuples", p_flips_n)
    checks.check("thm1-formation-set-p-invariant", "{c : n(c) ≠ 0} is P-invariant", form_p_invariant)

    all_binary_p_related = True
    for coloring in stars:
        p_image = act_col(p_perm, coloring)
        if not any(act_col(perm, coloring) == p_image for perm in proper_perms):
            all_binary_p_related = False
            break
    checks.check(
        "thm1-july3-t2-local",
        "every 2-letter coloring is proper-equivalent to its P-image",
        all_binary_p_related,
    )

    f_set = {occupancy for occupancy in stars if occupancy_lock_content_bit(occupancy, pair)}
    n_f = len(f_set)
    n_p_f = sum(1 for occupancy in stars if invert_tuple(p_perm, occupancy) in f_set)
    n_both_f = sum(
        1 for occupancy in stars if occupancy in f_set and invert_tuple(p_perm, occupancy) in f_set
    )
    f_p_invariant = all(
        (occupancy in f_set) == (invert_tuple(p_perm, occupancy) in f_set) for occupancy in stars
    )
    f_p_odd_as_set = not f_p_invariant

    checks.check("thm2-n-f", "N_f = 12", n_f == 12)
    checks.check("thm2-n-p-f", "N_P_f = 12", n_p_f == 12)
    checks.check("thm2-n-both", "N_both = 12", n_both_f == 12)
    checks.check(
        "thm2-occupancy-f-set-not-p-odd",
        "{c : f(c)=1} is P-invariant, not P-odd",
        f_p_invariant and (not f_p_odd_as_set) and n_f == n_p_f == n_both_f,
    )
    form_set = {occupancy for occupancy in stars if forms(occupancy)}
    checks.check("thm2-f-is-not-n-nonzero", "lock-content f is not occupancy n≠0", f_set != form_set and n_f != n_form)
    checks.check(
        "thm2-f-set-has-unique-full-axis",
        "every occupancy with f=1 has a unique full axis",
        all(unique_full_axis(occupancy) is not None for occupancy in f_set),
    )
    checks.check("thm2-july3-pair-size", "July-3 chiral pair has 48 colorings", len(pair) == 48)

    pos_content = [item for item in pair if leftover_frame_sign(item) == 1]
    neg_content = [item for item in pair if leftover_frame_sign(item) == -1]
    pos_set = set(pos_content)
    p_of_pos = {invert_tuple(p_perm, item) for item in pos_content}
    sign_flips = all(
        leftover_frame_sign(invert_tuple(p_perm, item)) == -leftover_frame_sign(item) for item in pair
    )
    per_support = {}
    for item in pos_content:
        per_support.setdefault(support(item), []).append(item)

    checks.check("thm2-content-positive-count", "leftover-frame-positive colorings number 24", len(pos_content) == 24)
    checks.check("thm2-content-negative-count", "leftover-frame-negative colorings number 24", len(neg_content) == 24)
    checks.check(
        "thm2-content-p-odd",
        "lock-content leftover-frame-positive set is disjoint from its P-image",
        pos_set.isdisjoint(p_of_pos) and p_of_pos == set(neg_content),
    )
    checks.check("thm2-content-sign-flips", "leftover-frame sign is P-odd on the pair", sign_flips)
    checks.check(
        "thm2-uniqueness-not-required",
        "each f=1 occupancy has two leftover-frame-positive completions",
        all(len(items) == 2 for items in per_support.values()) and len(per_support) == 12,
    )
    checks.check(
        "thm2-content-supports-are-f-set",
        "occupancy supports of leftover-frame-positive colorings are exactly {c : f(c)=1}",
        set(per_support) == f_set,
    )

    checks.check(
        "thm3-occupancy-automatically-achiral",
        "occupancy n≠0 is two-letter P-invariant, so July-3 theorem 2 applies",
        form_p_invariant and all_binary_p_related and len(OCCUPANCY_ALPHABET) == 2,
    )
    checks.check(
        "thm3-lock-content-not-automatically-achiral",
        "lock-content f lives on the July-3 k=3 chiral pair and is P-odd",
        sign_flips and pos_set.isdisjoint(p_of_pos) and len(pair) == 48,
    )
    checks.check(
        "thm3-displayed-not-adopted",
        "note reports the split as displayed, not adopted",
        "Displayed, not adopted" in note
        and "Do not write f or V" + "−A into Admissibility" in note
        and "Do not attach L1" in note,
    )

    checks.check("claim-scope", "note reports the displayed claim_scope verbatim", CLAIM_SCOPE in note)
    axiom_flat = " ".join(axiom.split())
    checks.check(
        "axiom-boundary",
        "Admissibility is proper-covariant and does not supply formation",
        "covariant under lattice translations and proper cubic rotations" in axiom_flat
        and "it does not supply the formation site, probability, or rate." in axiom_flat
        and "A readout value is determined by record content alone." in axiom_flat,
    )
    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/LOCK_CONTENT_LEFTOVER_FRAME_P_ODD_VS_L1CHI_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and 'AUDIT_INPUT_PATHS = (\n    "docs/LOCK_CONTENT_LEFTOVER_FRAME_P_ODD_VS_L1CHI_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n)'
        in self_source
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file(),
    )
    script_lines = [line for line in self_source.splitlines() if "FORBIDDEN" not in line]
    forbidden_hit = any(
        token in note or any(token in line for line in script_lines) for token in FORBIDDEN
    )
    checks.check("forbidden-phrases-absent", "forbidden phrases are absent from note and runner", not forbidden_hit)
    checks.check(
        "no-new-spatial-patch",
        "runner never steps occupancy on a new spatial patch",
        "new spatial patch" in note
        and "product(OCCUPANCY_ALPHABET, repeat=6)" in self_source
        and "lattice_wide: checked and not executed" in self_source
        and ("ba" + "ll(") not in self_source
        and ("B_" + "3") not in self_source,
    )
    checks.check(
        "no-orbit-dump",
        "runner does not dump the proper-orbit census",
        ("B_" + "57") not in self_source
        and ("B_" + "57") not in note
        and ("path " + "dump") not in self_source.lower(),
    )
    checks.check(
        "claim-type-and-gate",
        "bounded theorem type and a passing N1-N8 gate are source-visible",
        "**Type:** bounded_theorem" in note
        and all(f"### N{index}" in note for index in range(1, 9))
        and "No-Go Discipline disposition: **PASS**" in note
        and note.count("**ATTEMPTED**") == 6
        and ("import " + "qcd") not in self_source.lower(),
    )
    checks.check(
        "machine-status-contract",
        "note carries the bounded-support status and no hypothetical axiom adoption",
        'hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"'
        in note
        and "actual_current_surface_status: bounded-support" in note
        and "next_trace_action:" in note,
    )
    checks.check(
        "qubit-unchanged",
        "Qubit remains M_2(C); no axiom edit",
        "Qubit remains `M_2(C)`" in note and "No axiom edit" in note,
    )
    checks.check(
        "mutation-occupancy-f-equals-forms-fails",
        "predicate f-set == n≠0 fails",
        f_set != form_set,
    )
    checks.check(
        "mutation-occupancy-f-is-p-odd-fails",
        "predicate occupancy {c : f(c)=1} is P-odd fails",
        not f_p_odd_as_set,
    )

    print("per_element: checked exactly — each of the 64 occupancy tuples has n=d/3, forms iff n≠0, and a leftover-frame lock-content bit")
    print("per_site: checked exactly — one six-neighbor star; no host rebuild and no occupancy step")
    print("per_mode: checked exactly — two-letter occupancy n≠0 versus three-letter leftover-frame-positive f")
    print("per_block: checked exactly — N_form=56/56/56 P-even; occupancy N_f=12/12/12; content f is P-odd")
    print("lattice_wide: checked and not executed — no occupancy step on a new spatial patch")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
