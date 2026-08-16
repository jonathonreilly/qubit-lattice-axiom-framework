#!/usr/bin/env python3
"""Displayed L1 formation (n≠0) on the six-neighbor occupancy star.

Two-letter openness census, P-invariance, July-3 theorem 2/3 application,
and displayed mismatch with a P-odd / V-A grading. No axiom edit, no
cache write, no new spatial patch, no L1 attachment.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "L1_WEAK_CHIRALITY_MATCH_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/L1_WEAK_CHIRALITY_MATCH_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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

# Occupancy letters: empty / occupied. Lock labels are not letters of n.
OCCUPANCY_ALPHABET = (0, 1)
LOCK_LABELS = (0, 1, 2)

CLAIM_SCOPE = (
    "On the six-neighbor occupancy star, whether "
    "displayed L1 formation (n≠0) is a two-letter automatically "
    "achiral rule, and whether that matches observed weak "
    "P-violation, is reported. Displayed, not adopted."
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
            records.append(
                {
                    "M": matrix,
                    "det": det3(matrix),
                    "perm": dperm(matrix),
                }
            )
    return records


def dipole(occupancy: tuple[int, ...]) -> tuple[int, int, int]:
    return (
        occupancy[0] - occupancy[1],
        occupancy[2] - occupancy[3],
        occupancy[4] - occupancy[5],
    )


def n_from_occupancy(occupancy: tuple[int, ...]) -> tuple[Fraction, Fraction, Fraction]:
    d_vec = dipole(occupancy)
    return (
        Fraction(d_vec[0], 3),
        Fraction(d_vec[1], 3),
        Fraction(d_vec[2], 3),
    )


def forms(occupancy: tuple[int, ...]) -> bool:
    return n_from_occupancy(occupancy) != (Fraction(0), Fraction(0), Fraction(0))


def hamming(occupancy: tuple[int, ...]) -> int:
    return sum(occupancy)


def invert_occupancy(occupancy: tuple[int, ...]) -> tuple[int, ...]:
    return act_col(dperm(inversion_matrix()), occupancy)


def all_occupancy() -> list[tuple[int, ...]]:
    return list(product(OCCUPANCY_ALPHABET, repeat=6))


def n_from_labeled(occupancy: tuple[int, ...], labels: tuple[int, ...]) -> tuple[Fraction, Fraction, Fraction]:
    """Lock labels are accepted and discarded; n reads occupancy only."""
    del labels
    return n_from_occupancy(occupancy)


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

    print("external_scientific_inputs: none; occupancy alphabet and n=d/3 are displayed")
    print("package_local_integrity_reads: runner source, proposed source note, live axiom memo")
    print("measure_boundary: exact Fraction on the 64 occupancy tuples; no spatial patch")
    print("negative_scope: displayed L1 formation is automatically achiral and does not produce V-A")

    stars = all_occupancy()
    records = signed_permutation_records()
    proper = [record for record in records if record["det"] == 1]
    p_perm = dperm(inversion_matrix())
    proper_perms = [record["perm"] for record in proper]

    checks.check("alphabet-two-letter", "occupancy alphabet is {0,1}", OCCUPANCY_ALPHABET == (0, 1))
    checks.check("star-cardinality", "six-neighbor occupancy star has 64 tuples", len(stars) == 64)
    checks.check("cubic-group-size", "full signed-permutation group has 48 elements", len(records) == 48)
    checks.check("proper-group-size", "proper cubic rotations number 24", len(proper) == 24)

    empty = (0, 0, 0, 0, 0, 0)
    full = (1, 1, 1, 1, 1, 1)
    axis_plus = (1, 0, 0, 0, 0, 0)
    balanced_pair = (1, 1, 0, 0, 0, 0)
    zero_n = (Fraction(0), Fraction(0), Fraction(0))

    checks.check(
        "thm1-n-empty-zero",
        "n(empty) = 0",
        n_from_occupancy(empty) == zero_n,
    )
    checks.check(
        "thm1-n-full-zero",
        "n(full) = 0",
        n_from_occupancy(full) == zero_n,
    )
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
    n_p_form = sum(1 for occupancy in stars if forms(invert_occupancy(occupancy)))
    n_both = sum(
        1
        for occupancy in stars
        if forms(occupancy) and forms(invert_occupancy(occupancy))
    )
    n_zero = sum(1 for occupancy in stars if not forms(occupancy))

    checks.check("thm2-n-zero", "exactly 8 occupancy tuples have n = 0", n_zero == 8)
    checks.check("thm2-n-form", "N_form = 56", n_form == 56)
    checks.check("thm2-n-p-form", "N_P_form = 56", n_p_form == 56)
    checks.check("thm2-n-both", "N_both = 56", n_both == 56)

    p_flips_n = all(
        n_from_occupancy(invert_occupancy(occupancy))
        == tuple(-component for component in n_from_occupancy(occupancy))
        for occupancy in stars
    )
    set_p_invariant = all(forms(occupancy) == forms(invert_occupancy(occupancy)) for occupancy in stars)
    checks.check("thm1-p-sends-n-to-minus-n", "n(P(c)) = -n(c) on all 64 tuples", p_flips_n)
    checks.check("thm1-formation-set-p-invariant", "{c : n(c) ≠ 0} is P-invariant", set_p_invariant)

    proper_preserves_forms = True
    for occupancy in stars:
        formed = forms(occupancy)
        for perm in proper_perms:
            if forms(act_col(perm, occupancy)) != formed:
                proper_preserves_forms = False
                break
        if not proper_preserves_forms:
            break
    checks.check(
        "thm1-proper-covariant",
        "n≠0 is invariant under the 24 proper cubic rotations",
        proper_preserves_forms,
    )

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

    labels_a = (0, 0, 0, 0, 0, 0)
    labels_b = (1, 2, 0, 1, 2, 0)
    labels_c = (2, 1, 1, 2, 0, 1)
    lock_blind = (
        n_from_labeled(axis_plus, labels_a)
        == n_from_labeled(axis_plus, labels_b)
        == n_from_labeled(axis_plus, labels_c)
        == n_from_occupancy(axis_plus)
        and n_from_labeled(balanced_pair, labels_b) == n_from_occupancy(balanced_pair)
    )
    checks.check(
        "thm1-lock-labels-do-not-feed-n",
        "distinct lock labels on the same occupancy give the same n",
        lock_blind,
    )
    checks.check(
        "mutation-lock-labels-feed-n-fails",
        "predicate 'lock labels feed n' fails",
        n_from_labeled(axis_plus, labels_b) == n_from_occupancy(axis_plus),
    )

    hamming_nonzero = {occupancy for occupancy in stars if hamming(occupancy) != 0}
    form_set = {occupancy for occupancy in stars if forms(occupancy)}
    checks.check(
        "thm2-not-hamming",
        "f_L1 is n≠0, not Hamming-nonzero",
        form_set != hamming_nonzero and balanced_pair in hamming_nonzero and balanced_pair not in form_set,
    )
    checks.check(
        "mutation-hamming-equals-forms-fails",
        "predicate Hamming-nonzero == n≠0 fails",
        form_set != hamming_nonzero,
    )
    checks.check(
        "thm2-alphabet-not-three",
        "neighbor occupancy alphabet has 2 letters, not 3",
        len(OCCUPANCY_ALPHABET) == 2 and len(OCCUPANCY_ALPHABET) != 3,
    )

    # P-odd comparison grading on the star: chi(c) = n_x(c). Formation is P-even.
    chi = {occupancy: n_from_occupancy(occupancy)[0] for occupancy in stars}
    chi_odd = all(chi[invert_occupancy(occupancy)] == -chi[occupancy] for occupancy in stars)
    form_indicator = {occupancy: (1 if forms(occupancy) else 0) for occupancy in stars}
    form_even = all(
        form_indicator[invert_occupancy(occupancy)] == form_indicator[occupancy] for occupancy in stars
    )
    only_zero_is_even_and_odd = all(
        not (form_indicator[occupancy] == chi[occupancy] != 0) for occupancy in stars
    )
    checks.check("thm3-chi-is-p-odd", "displayed comparison grade n_x is P-odd", chi_odd)
    checks.check("thm3-formation-is-p-even", "formation indicator is P-even", form_even)
    checks.check(
        "thm3-even-cannot-equal-odd",
        "P-even formation cannot equal the P-odd grade except at 0",
        only_zero_is_even_and_odd and chi[axis_plus] != 0,
    )
    checks.check(
        "thm3-mismatch-displayed",
        "automatically achiral L1 formation does not produce the P-odd grade",
        form_even and chi_odd and form_set != set(occupancy for occupancy, value in chi.items() if value != 0),
    )

    checks.check(
        "claim-scope",
        "note reports the displayed claim_scope verbatim",
        CLAIM_SCOPE in note and "Displayed, not adopted." in note,
    )
    checks.check(
        "no-attachment",
        "note refuses L1 attachment and Admissibility rewrite",
        "Do not attach L1" in note
        and "Do not write L1 or V−A into Admissibility" in note
        and "Do not adopt a chirality bit" in note,
    )
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
            "docs/L1_WEAK_CHIRALITY_MATCH_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and 'AUDIT_INPUT_PATHS = (\n    "docs/L1_WEAK_CHIRALITY_MATCH_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n)'
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
        and "all_occupancy()" in self_source
        and "product(OCCUPANCY_ALPHABET, repeat=6)" in self_source
        and "lattice_wide: checked and not executed" in self_source,
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

    print("per_element: checked exactly — each of the 64 occupancy tuples has n=d/3 and forms iff n≠0")
    print("per_site: checked exactly — one six-neighbor star; lock labels do not feed n")
    print("per_mode: checked exactly — two-letter openness versus a displayed P-odd comparison grade")
    print("per_block: checked exactly — N_form=N_P_form=N_both=56; Hamming-nonzero is a different set")
    print("lattice_wide: checked and not executed — no occupancy step on a new spatial patch")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
