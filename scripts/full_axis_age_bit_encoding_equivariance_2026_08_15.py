#!/usr/bin/env python3
"""Age-bit encoding on the occupancy-named full axis under G+.

Score the 12 perpendicular weight-4 occupancy masks. For each mask and
each older-end bit, write opposite letters on the unique full axis
(older −, younger +) and take the unique or lex-first July-3 pair
completion of the other two occupied slots. N_complete counts (σ,b)
with a completion. N_commute counts the (σ,b,g) triples that satisfy
f(g·σ, b_g)=g·f(σ,b). Displayed, not adopted. No cache is written.
"""

from __future__ import annotations

import ast
import itertools
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/FULL_AXIS_AGE_BIT_ENCODING_EQUIVARIANCE_"
    "BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/FULL_AXIS_AGE_BIT_ENCODING_EQUIVARIANCE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Coloring = tuple[int, ...]
Tick = tuple[int | None, ...]
Matrix = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]

DIRS: tuple[tuple[int, int, int], ...] = (
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
LETTER_SHOW = {EMPTY: "0", PLUS: "+", MINUS: "−"}
FORBIDDEN = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")
CLAIM_SCOPE = (
    'claim_scope: "On the 12 perpendicular weight-4 masks, whether encoding '
    "the age bit as opposite letters on the full axis yields a G+-equivariant "
    'pair labeling is reported. Displayed, not adopted."'
)
SWAPPER: Matrix = ((0, 1, 0), (1, 0, 0), (0, 0, -1))
FAIL_SIGMA: Coloring = (0, 1, 0, 1, 1, 1)
FAIL_G: Matrix = ((0, -1, 0), (1, 0, 0), (0, 0, 1))
OK_G: Matrix = ((-1, 0, 0), (0, -1, 0), (0, 0, 1))
EXPECTED_F: dict[tuple[Coloring, int], Coloring] = {
    ((0, 1, 0, 1, 1, 1), 0): (0, PLUS, 0, MINUS, MINUS, PLUS),
    ((0, 1, 0, 1, 1, 1), 1): (0, PLUS, 0, MINUS, PLUS, MINUS),
    ((0, 1, 1, 0, 1, 1), 0): (0, PLUS, MINUS, 0, MINUS, PLUS),
    ((0, 1, 1, 0, 1, 1), 1): (0, PLUS, MINUS, 0, PLUS, MINUS),
    ((0, 1, 1, 1, 0, 1), 0): (0, PLUS, MINUS, PLUS, 0, MINUS),
    ((0, 1, 1, 1, 0, 1), 1): (0, PLUS, PLUS, MINUS, 0, MINUS),
    ((0, 1, 1, 1, 1, 0), 0): (0, PLUS, MINUS, PLUS, MINUS, 0),
    ((0, 1, 1, 1, 1, 0), 1): (0, PLUS, PLUS, MINUS, MINUS, 0),
    ((1, 0, 0, 1, 1, 1), 0): (PLUS, 0, 0, MINUS, MINUS, PLUS),
    ((1, 0, 0, 1, 1, 1), 1): (PLUS, 0, 0, MINUS, PLUS, MINUS),
    ((1, 0, 1, 0, 1, 1), 0): (PLUS, 0, MINUS, 0, MINUS, PLUS),
    ((1, 0, 1, 0, 1, 1), 1): (PLUS, 0, MINUS, 0, PLUS, MINUS),
    ((1, 0, 1, 1, 0, 1), 0): (PLUS, 0, MINUS, PLUS, 0, MINUS),
    ((1, 0, 1, 1, 0, 1), 1): (PLUS, 0, PLUS, MINUS, 0, MINUS),
    ((1, 0, 1, 1, 1, 0), 0): (PLUS, 0, MINUS, PLUS, MINUS, 0),
    ((1, 0, 1, 1, 1, 0), 1): (PLUS, 0, PLUS, MINUS, MINUS, 0),
    ((1, 1, 0, 1, 0, 1), 0): (MINUS, PLUS, 0, PLUS, 0, MINUS),
    ((1, 1, 0, 1, 0, 1), 1): (PLUS, MINUS, 0, PLUS, 0, MINUS),
    ((1, 1, 0, 1, 1, 0), 0): (MINUS, PLUS, 0, PLUS, MINUS, 0),
    ((1, 1, 0, 1, 1, 0), 1): (PLUS, MINUS, 0, PLUS, MINUS, 0),
    ((1, 1, 1, 0, 0, 1), 0): (MINUS, PLUS, PLUS, 0, 0, MINUS),
    ((1, 1, 1, 0, 0, 1), 1): (PLUS, MINUS, PLUS, 0, 0, MINUS),
    ((1, 1, 1, 0, 1, 0), 0): (MINUS, PLUS, PLUS, 0, MINUS, 0),
    ((1, 1, 1, 0, 1, 0), 1): (PLUS, MINUS, PLUS, 0, MINUS, 0),
}


def normalize(text: str) -> str:
    return " ".join(text.split())


def show_col(coloring: Coloring) -> str:
    return "(" + ", ".join(LETTER_SHOW[letter] for letter in coloring) + ")"


def det3(matrix: Matrix) -> int:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def mat_vec(matrix: Matrix, vector: tuple[int, int, int]) -> tuple[int, int, int]:
    return (
        matrix[0][0] * vector[0] + matrix[0][1] * vector[1] + matrix[0][2] * vector[2],
        matrix[1][0] * vector[0] + matrix[1][1] * vector[1] + matrix[1][2] * vector[2],
        matrix[2][0] * vector[0] + matrix[2][1] * vector[1] + matrix[2][2] * vector[2],
    )


def direction_perm(matrix: Matrix) -> tuple[int, ...]:
    return tuple(DIR_INDEX[mat_vec(matrix, direction)] for direction in DIRS)


def act_col(perm: tuple[int, ...], coloring: Coloring | Tick) -> tuple:
    out = [None] * len(coloring)
    for source, image in enumerate(perm):
        out[image] = coloring[source]
    return tuple(out)


def proper_rotations() -> tuple[Matrix, ...]:
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


def support(coloring: Coloring) -> Coloring:
    return tuple(int(letter != EMPTY) for letter in coloring)


def empty_slots(sigma: Coloring) -> tuple[int, int]:
    emptied = tuple(index for index, bit in enumerate(sigma) if bit == 0)
    if len(emptied) != 2:
        raise AssertionError(f"expected two empty slots, got {emptied}")
    return (emptied[0], emptied[1])


def same_axis(left: int, right: int) -> bool:
    return any({left, right} == set(axis) for axis in AXES)


def unique_full_axis(sigma: Coloring) -> int | None:
    named = tuple(
        axis_index
        for axis_index, (plus, minus) in enumerate(AXES)
        if sigma[plus] == 1 and sigma[minus] == 1
    )
    if len(named) == 1:
        return named[0]
    return None


def weight4_masks() -> tuple[Coloring, ...]:
    return tuple(bits for bits in itertools.product((0, 1), repeat=6) if sum(bits) == 4)


def perp_masks() -> tuple[Coloring, ...]:
    return tuple(
        sigma
        for sigma in weight4_masks()
        if not same_axis(*empty_slots(sigma))
    )


def display_ticks(sigma: Coloring, axis_index: int, bit: int) -> Tick:
    plus, minus = AXES[axis_index]
    ticks: list[int | None] = [None] * 6
    for slot, occupied in enumerate(sigma):
        if occupied == 0:
            continue
        if slot == minus:
            ticks[slot] = 1 if bit == 1 else 2
        elif slot == plus:
            ticks[slot] = 2 if bit == 1 else 1
        else:
            ticks[slot] = 0
    return tuple(ticks)


def bit_on_axis(ticks: Tick, axis_index: int) -> int:
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


def july3_pair(perms: list[tuple[int, ...]]) -> frozenset[Coloring]:
    unseen = set(itertools.product((EMPTY, PLUS, MINUS), repeat=6))
    inversion = direction_perm(((-1, 0, 0), (0, -1, 0), (0, 0, -1)))
    pair: set[Coloring] = set()
    while unseen:
        seed = min(unseen)
        orbit = {act_col(perm, seed) for perm in perms}
        unseen -= orbit
        image = act_col(inversion, next(iter(orbit)))
        if image not in orbit:
            pair |= orbit
    return frozenset(pair)


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
    note_flat = normalize(note)
    axiom_flat = normalize(axiom)
    self_source = Path(__file__).read_text(encoding="utf-8")
    literal_paths = parse_audit_input_paths(self_source)
    rotations = proper_rotations()
    perms = [direction_perm(matrix) for matrix in rotations]
    pair = july3_pair(perms)
    masks = perp_masks()
    complete_denom = len(masks) * 2
    commute_denom = len(masks) * 2 * len(rotations)

    rule: dict[tuple[Coloring, int], Coloring] = {}
    n_comp: dict[tuple[Coloring, int], int] = {}
    both_ok = True
    unique_any = False
    f_indep = False
    for sigma in masks:
        named = unique_full_axis(sigma)
        if named is None:
            both_ok = False
            continue
        for bit in (0, 1):
            comps = completions(sigma, bit, pair)
            n_comp[(sigma, bit)] = len(comps)
            if len(comps) == 1:
                unique_any = True
            if not comps:
                both_ok = False
                continue
            rule[(sigma, bit)] = comps[0]
        if (sigma, 0) in rule and (sigma, 1) in rule:
            if rule[(sigma, 0)] == rule[(sigma, 1)]:
                f_indep = True

    n_complete = sum(1 for sigma in masks for bit in (0, 1) if (sigma, bit) in rule)
    n_commute = 0
    per_mask: list[int] = []
    for sigma in masks:
        named = unique_full_axis(sigma)
        if named is None:
            per_mask.append(0)
            continue
        mask_commute = 0
        for bit in (0, 1):
            if (sigma, bit) not in rule:
                continue
            ticks = display_ticks(sigma, named, bit)
            coloring = rule[(sigma, bit)]
            for perm in perms:
                sigma_g = act_col(perm, sigma)
                named_g = unique_full_axis(sigma_g)
                if named_g is None:
                    continue
                bit_g = bit_on_axis(act_col(perm, ticks), named_g)
                image = rule.get((sigma_g, bit_g))
                if image is not None and image == act_col(perm, coloring):
                    n_commute += 1
                    mask_commute += 1
        per_mask.append(mask_commute)

    fail_perm = direction_perm(FAIL_G)
    fail_named = unique_full_axis(FAIL_SIGMA)
    fail_ticks = display_ticks(FAIL_SIGMA, fail_named, 0) if fail_named is not None else None
    fail_sigma_g = act_col(fail_perm, FAIL_SIGMA)
    fail_named_g = unique_full_axis(fail_sigma_g)
    fail_bit_g = (
        bit_on_axis(act_col(fail_perm, fail_ticks), fail_named_g)
        if fail_ticks is not None and fail_named_g is not None
        else None
    )
    fail_lhs = rule.get((fail_sigma_g, fail_bit_g)) if fail_bit_g is not None else None
    fail_rhs = act_col(fail_perm, rule[(FAIL_SIGMA, 0)]) if (FAIL_SIGMA, 0) in rule else None

    ok_perm = direction_perm(OK_G)
    ok_ticks = display_ticks(FAIL_SIGMA, fail_named, 0) if fail_named is not None else None
    ok_sigma_g = act_col(ok_perm, FAIL_SIGMA)
    ok_named_g = unique_full_axis(ok_sigma_g)
    ok_bit_g = (
        bit_on_axis(act_col(ok_perm, ok_ticks), ok_named_g)
        if ok_ticks is not None and ok_named_g is not None
        else None
    )
    ok_lhs = rule.get((ok_sigma_g, ok_bit_g)) if ok_bit_g is not None else None
    ok_rhs = act_col(ok_perm, rule[(FAIL_SIGMA, 0)]) if (FAIL_SIGMA, 0) in rule else None

    print("full-axis age-bit encoding G+ equivariance")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print(f"G_plus={len(rotations)}")
    print(f"N_perp={len(masks)}")
    print(f"N_pair={len(pair)}")
    print(f"N_complete={n_complete}")
    print(f"N_complete_over_24={n_complete}/{complete_denom}")
    print(f"N_denom={commute_denom}")
    print(f"N_commute={n_commute}")
    print(f"N_commute_over_denom={n_commute}/{commute_denom}")
    print(f"N_commute_eq_576={n_commute == 576}")
    print(f"f_independent_of_b={f_indep}")
    print("perp_rows:")
    for sigma, count in zip(masks, per_mask):
        named = unique_full_axis(sigma)
        axis = AXIS_NAME[named] if named is not None else None
        f0 = rule.get((sigma, 0))
        f1 = rule.get((sigma, 1))
        n0 = n_comp.get((sigma, 0), 0)
        n1 = n_comp.get((sigma, 1), 0)
        both = n0 > 0 and n1 > 0
        print(
            f"  {sigma} full={axis} both={both} n_comp={n0},{n1} "
            f"f0={show_col(f0) if f0 is not None else None} "
            f"f1={show_col(f1) if f1 is not None else None} "
            f"commute={count}/48"
        )

    expected_paths = (
        "docs/FULL_AXIS_AGE_BIT_ENCODING_EQUIVARIANCE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
        len(rotations) == 24
        and len(set(rotations)) == 24
        and det3(SWAPPER) == 1
        and SWAPPER in rotations,
        f"proper={len(rotations)}",
    )
    checks.check(
        "twelve-perp-masks",
        len(masks) == 12
        and all(unique_full_axis(sigma) is not None for sigma in masks)
        and all((sigma, 0) in rule and (sigma, 1) in rule for sigma in masks)
        and all(rule[(sigma, bit)] == EXPECTED_F[(sigma, bit)] for sigma in masks for bit in (0, 1))
        and "12 perpendicular" in note
        and "`12 × 2 × 24 = 576`" in note,
        f"N_perp={len(masks)}",
    )
    checks.check(
        "theorem-1-n-complete",
        both_ok
        and n_complete == 24
        and complete_denom == 24
        and not unique_any
        and all(n_comp[(sigma, bit)] == 2 for sigma in masks for bit in (0, 1))
        and all(rule[(sigma, 0)] != rule[(sigma, 1)] for sigma in masks)
        and not f_indep
        and "N_complete / 24 = 24/24" in note
        and "N_complete = 24" in note
        and "both bits" in note,
        f"N_complete={n_complete}/{complete_denom}",
    )
    checks.check(
        "theorem-2-n-commute",
        n_commute == 288
        and commute_denom == 576
        and n_commute != 576
        and per_mask == [24] * 12
        and "N_commute / 576 = 288/576" in note
        and "N_commute = 288" in note
        and "Whether `N_commute=576`" in note
        and "not the full 576" in note
        and "not a `G+`-equivariant pair labeling" in note,
        f"N_commute={n_commute}/{commute_denom}",
    )
    checks.check(
        "fail-witness",
        fail_lhs == (PLUS, 0, 0, MINUS, MINUS, PLUS)
        and fail_rhs == (MINUS, 0, 0, PLUS, MINUS, PLUS)
        and fail_lhs != fail_rhs
        and fail_bit_g == 0
        and fail_sigma_g == (1, 0, 0, 1, 1, 1)
        and ok_lhs == ok_rhs == (PLUS, 0, MINUS, 0, MINUS, PLUS)
        and "`g : (x, y, z) ↦ (−y, x, z)`" in note
        and "`f(σ_g, b_g) = (+, 0, 0, −, −, +)`" in note
        and "`g · f(σ,b) = (−, 0, 0, +, −, +)`" in note,
        f"lhs={fail_lhs} rhs={fail_rhs}",
    )
    checks.check("claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "displayed-not-adopted",
        "Displayed, not adopted" in note
        and "Do not write `f` into Admissibility" in note
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
        "not-leftover-bitlaw",
        "not leftover of bitlaw" in note_flat
        and "lex-first ignored" in note
        and "N_commute=144/576" in note
        and "f(σ,0)=f(σ,1)" in note,
    )
    checks.check(
        "admissibility-unedited",
        covariance_clause in axiom_flat
        and "N_commute" not in axiom
        and "N_complete" not in axiom
        and "bitlaw" not in axiom,
    )
    checks.check(
        "forbidden-phrases",
        all(phrase not in note for phrase in FORBIDDEN)
        and all(
            phrase not in self_source.split("FORBIDDEN = ", 1)[0]
            for phrase in FORBIDDEN
        ),
    )
    checks.check(
        "no-axiom-edit",
        "[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)" in note
        and "cache_write: false" in self_source
        and AXIOM_REL in AUDIT_INPUT_PATHS
        and "no axiom" in note_flat.lower(),
    )

    print("per_element: N_complete, N_commute, and f(σ,b) are exact")
    print("per_site: 12 perpendicular weight-4 occupancy masks scored")
    print("per_mode: no spectral calculation")
    print("per_block: 6-NN star masks and G+ only")
    print("lattice_wide: checked and not executed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
