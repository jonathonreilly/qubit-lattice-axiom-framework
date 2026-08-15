#!/usr/bin/env python3
"""Blank-block empties the 1-site first wave for every f(wt1)=1 member.

The paired note is
docs/BLANK_BLOCK_EMPTIES_ONESITE_SUBCLASS_BOUNDED_THEOREM_NOTE_2026-08-15.md.

Displayed finite objects only: the twelve-vertex two-cube, cube-covariant
boolean predicates on {0,1}^6, and the blank-block readiness rule. No law is
adopted. No runner cache is written.
"""

from __future__ import annotations

from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
AUDIT_INPUT_PATHS = (
    "docs/BLANK_BLOCK_EMPTIES_ONESITE_SUBCLASS_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
NOTE_PATH = ROOT / AUDIT_INPUT_PATHS[0]
AXIOM_PATH = ROOT / AUDIT_INPUT_PATHS[1]

# Six directed nearest-neighbor slots, in this fixed order.
DIRS: tuple[tuple[int, int, int], ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
DIR_INDEX = {direction: index for index, direction in enumerate(DIRS)}

A_CUBE = frozenset(product((0, 1), (0, 1), (0, 1)))
B_CUBE = frozenset(product((1, 2), (0, 1), (0, 1)))
PATCH = frozenset(set(A_CUBE) | set(B_CUBE))
SEED = (0, 0, 0)
AXIS_SITES = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def normalize(text: str) -> str:
    return " ".join(text.split())


def add(
    site: tuple[int, int, int], direction: tuple[int, int, int]
) -> tuple[int, int, int]:
    return (site[0] + direction[0], site[1] + direction[1], site[2] + direction[2])


def neighbors(site: tuple[int, int, int]) -> tuple[tuple[int, int, int], ...]:
    return tuple(add(site, direction) for direction in DIRS)


def off_patch_neighbor_count(site: tuple[int, int, int]) -> int:
    return sum(1 for neigh in neighbors(site) if neigh not in PATCH)


def blank_blocked(site: tuple[int, int, int]) -> bool:
    return off_patch_neighbor_count(site) > 0


def occupancy_o0(
    site: tuple[int, int, int], locks: frozenset[tuple[int, int, int]]
) -> tuple[int, ...]:
    """Off-patch neighbors default to occupancy 0. On-patch unread is 0."""
    cell = []
    for neigh in neighbors(site):
        cell.append(1 if neigh in locks else 0)
    return tuple(cell)


def permutation_sign(perm: tuple[int, ...]) -> int:
    sign = 1
    values = list(perm)
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            if values[i] > values[j]:
                sign *= -1
    return sign


def proper_cube_rotations() -> tuple[tuple[tuple[int, ...], tuple[int, ...]], ...]:
    """24 proper cube rotations as (axis permutation, axis signs).

    R maps e_j to signs[j] * e_{perm[j]}. Det = sign(perm) * product(signs).
    """
    rotations: list[tuple[tuple[int, ...], tuple[int, ...]]] = []
    for perm in permutations(range(3)):
        perm_t = tuple(perm)
        sign_perm = permutation_sign(perm_t)
        for signs in product((-1, 1), repeat=3):
            if sign_perm * signs[0] * signs[1] * signs[2] != 1:
                continue
            rotations.append((perm_t, signs))
    return tuple(rotations)


def rotate_direction(
    direction: tuple[int, int, int],
    perm: tuple[int, ...],
    signs: tuple[int, ...],
) -> tuple[int, int, int]:
    image = [0, 0, 0]
    for axis in range(3):
        image[perm[axis]] = signs[axis] * direction[axis]
    return (image[0], image[1], image[2])


def rotate_cell(
    cell: tuple[int, ...],
    perm: tuple[int, ...],
    signs: tuple[int, ...],
) -> tuple[int, ...]:
    image = [0] * 6
    for slot, direction in enumerate(DIRS):
        image[DIR_INDEX[rotate_direction(direction, perm, signs)]] = cell[slot]
    return tuple(image)


def all_cells() -> tuple[tuple[int, ...], ...]:
    return tuple(product((0, 1), repeat=6))


def orbit_reps() -> tuple[tuple[int, ...], ...]:
    rotations = proper_cube_rotations()
    seen: set[tuple[int, ...]] = set()
    reps: list[tuple[int, ...]] = []
    for cell in all_cells():
        if cell in seen:
            continue
        reps.append(cell)
        stack = [cell]
        seen.add(cell)
        while stack:
            current = stack.pop()
            for perm, signs in rotations:
                image = rotate_cell(current, perm, signs)
                if image not in seen:
                    seen.add(image)
                    stack.append(image)
    return tuple(reps)


def cell_to_rep(
    reps: tuple[tuple[int, ...], ...],
) -> dict[tuple[int, ...], tuple[int, ...]]:
    rotations = proper_cube_rotations()
    mapping: dict[tuple[int, ...], tuple[int, ...]] = {}
    for rep in reps:
        stack = [rep]
        mapping[rep] = rep
        while stack:
            current = stack.pop()
            for perm, signs in rotations:
                image = rotate_cell(current, perm, signs)
                if image not in mapping:
                    mapping[image] = rep
                    stack.append(image)
    return mapping


def f_L1(cell: tuple[int, ...]) -> int:
    """Form iff at least one axis is unbalanced. Not Hamming |c|_1 mod 2."""
    return int(cell[0] != cell[1] or cell[2] != cell[3] or cell[4] != cell[5])


def f_hamming_parity(cell: tuple[int, ...]) -> int:
    return int(sum(cell) % 2)


def is_wt1(cell: tuple[int, ...]) -> bool:
    return sum(cell) == 1


def first_wave_blank_block(
    form: object,
    locks: frozenset[tuple[int, int, int]],
) -> tuple[tuple[int, int, int], ...]:
    """Ready sites under blank-block. `form` is unused if any neighbor is off-patch."""
    ready: list[tuple[int, int, int]] = []
    for site in sorted(PATCH):
        if site in locks:
            continue
        if blank_blocked(site):
            continue
        cell = occupancy_o0(site, locks)
        if int(form(cell)) == 1:
            ready.append(site)
    return tuple(ready)


def first_wave_o0(
    form: object,
    locks: frozenset[tuple[int, int, int]],
) -> tuple[tuple[int, int, int], ...]:
    ready: list[tuple[int, int, int]] = []
    for site in sorted(PATCH):
        if site in locks:
            continue
        cell = occupancy_o0(site, locks)
        if int(form(cell)) == 1:
            ready.append(site)
    return tuple(ready)


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
    self_source = Path(__file__).read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)

    print("Blank-block empties the 1-site first wave on the two-cube")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print(
        "scope: twelve-vertex two-cube; cube-covariant f; blank-block vs o=0; "
        "displayed, not adopted"
    )

    checks.check(
        "audit-input-paths-exist",
        all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )
    checks.check(
        "audit-input-paths-static-literals",
        AUDIT_INPUT_PATHS
        == (
            "docs/BLANK_BLOCK_EMPTIES_ONESITE_SUBCLASS_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and 'AUDIT_INPUT_PATHS = (\n    "docs/BLANK_BLOCK_EMPTIES_ONESITE_SUBCLASS_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n)'
        in self_source,
    )
    checks.check("audit-timeout-declared", AUDIT_TIMEOUT_SEC == 120)
    checks.check(
        "no-cache-write",
        "cache_write: false" in self_source
        and "logs/" + "runner-cache" not in note,
    )

    checks.check("two-cube-has-twelve-vertices", len(PATCH) == 12)
    checks.check(
        "two-cube-is-union-of-adjacent-cubes",
        len(A_CUBE) == 8
        and len(B_CUBE) == 8
        and len(A_CUBE & B_CUBE) == 4
        and PATCH == A_CUBE | B_CUBE,
    )
    checks.check("seed-on-patch", SEED in PATCH and SEED in A_CUBE)
    checks.check(
        "axis-sites-on-patch",
        all(site in PATCH for site in AXIS_SITES),
    )

    rotations = proper_cube_rotations()
    checks.check("proper-cube-rotation-count-is-24", len(rotations) == 24)
    reps = orbit_reps()
    mapping = cell_to_rep(reps)
    checks.check("occupancy-cells-are-64", len(all_cells()) == 64)
    checks.check("orbit-cover-is-complete", len(mapping) == 64)
    wt1_cells = tuple(cell for cell in all_cells() if is_wt1(cell))
    wt1_reps = {mapping[cell] for cell in wt1_cells}
    checks.check(
        "wt1-is-one-orbit-of-six",
        len(wt1_cells) == 6 and len(wt1_reps) == 1,
        f"n_wt1={len(wt1_cells)} n_reps={len(wt1_reps)}",
    )
    wt1_rep = next(iter(wt1_reps))

    checks.check(
        "f-L1-is-unbalanced-axis-not-hamming",
        all(f_L1(cell) == int(any(cell[2 * ax] != cell[2 * ax + 1] for ax in range(3))) for cell in all_cells())
        and any(f_L1(cell) != f_hamming_parity(cell) for cell in all_cells()),
    )
    disagree = [cell for cell in all_cells() if f_L1(cell) != f_hamming_parity(cell)]
    two_axis_wt2 = (1, 0, 1, 0, 0, 0)
    checks.check(
        "hamming-disagrees-on-two-axis-weight-two",
        two_axis_wt2 in disagree
        and f_L1(two_axis_wt2) == 1
        and f_hamming_parity(two_axis_wt2) == 0
        and sum(two_axis_wt2) == 2,
        f"n_disagree={len(disagree)}",
    )
    checks.check(
        "f-L1-on-wt1-is-one",
        all(f_L1(cell) == 1 for cell in wt1_cells),
    )
    checks.check(
        "f-L1-is-cube-covariant",
        all(
            f_L1(rotate_cell(cell, perm, signs)) == f_L1(cell)
            for cell in all_cells()
            for perm, signs in rotations
        ),
    )

    locks = frozenset({SEED})
    axis_cells = {site: occupancy_o0(site, locks) for site in AXIS_SITES}
    checks.check(
        "theorem1-axis-sites-are-wt1-under-o0",
        all(is_wt1(cell) for cell in axis_cells.values())
        and all(mapping[cell] == wt1_rep for cell in axis_cells.values()),
        ",".join(f"{site}:{cell}" for site, cell in axis_cells.items()),
    )
    checks.check(
        "theorem1-axis-sites-are-blank-blocked",
        all(blank_blocked(site) for site in AXIS_SITES)
        and all(off_patch_neighbor_count(site) >= 1 for site in AXIS_SITES),
        ",".join(f"{site}:{off_patch_neighbor_count(site)}" for site in AXIS_SITES),
    )

    unlocked = tuple(sorted(site for site in PATCH if site != SEED))
    checks.check(
        "theorem2-no-unlocked-site-has-six-on-patch-neighbors",
        all(blank_blocked(site) for site in unlocked)
        and all(off_patch_neighbor_count(site) >= 1 for site in PATCH),
    )
    record_neighbor_counts = {
        site: sum(1 for neigh in neighbors(site) if neigh in locks) for site in unlocked
    }
    checks.check(
        "theorem2-no-unlocked-site-has-six-record-neighbors",
        all(count < 6 for count in record_neighbor_counts.values())
        and max(record_neighbor_counts.values()) == 1,
        f"max_record_nn={max(record_neighbor_counts.values())}",
    )

    empty_wave = first_wave_blank_block(f_L1, locks)
    checks.check(
        "theorem2-blank-block-first-wave-empty-for-L1",
        empty_wave == (),
    )

    empty_cell = (0, 0, 0, 0, 0, 0)
    empty_rep = mapping[empty_cell]
    subclass_empty = True
    subclass_size = 0
    o0_contains_axis = True
    o0_exact_when_empty_zero = True
    empty_zero_size = 0
    n_orb = len(reps)
    # Assign bits to orbits; wt1 orbit bit forced to 1.
    wt1_index = reps.index(wt1_rep)
    other_bits = n_orb - 1
    for mask in range(1 << other_bits):
        values = {}
        bit_pos = 0
        for index, rep in enumerate(reps):
            if index == wt1_index:
                values[rep] = 1
            else:
                values[rep] = (mask >> bit_pos) & 1
                bit_pos += 1

        def form(cell: tuple[int, ...], _values: dict = values) -> int:
            return _values[mapping[cell]]

        subclass_size += 1
        if first_wave_blank_block(form, locks) != ():
            subclass_empty = False
        wave_o0 = first_wave_o0(form, locks)
        if not set(AXIS_SITES) <= set(wave_o0):
            o0_contains_axis = False
        if values[empty_rep] == 0:
            empty_zero_size += 1
            if wave_o0 != tuple(sorted(AXIS_SITES)):
                o0_exact_when_empty_zero = False

    checks.check(
        "theorem2-blank-block-first-wave-empty-for-wt1-subclass",
        subclass_empty and subclass_size == (1 << other_bits) and subclass_size >= 1,
        f"|F_wt1|={subclass_size} n_orb={n_orb}",
    )

    # Independence of f: blank-block never evaluates f on this patch after the seed.
    any_f_empty = True
    for mask in range(1 << n_orb):
        values = {rep: (mask >> index) & 1 for index, rep in enumerate(reps)}

        def form_any(cell: tuple[int, ...], _values: dict = values) -> int:
            return _values[mapping[cell]]

        if first_wave_blank_block(form_any, locks) != ():
            any_f_empty = False
            break
    checks.check(
        "theorem2-blank-block-first-wave-empty-for-every-covariant-f",
        any_f_empty,
        f"|F_G|={1 << n_orb}",
    )

    checks.check(
        "theorem3-o0-first-wave-contains-axis-sites-for-wt1-subclass",
        o0_contains_axis
        and set(AXIS_SITES) <= set(first_wave_o0(f_L1, locks)),
    )
    checks.check(
        "theorem3-o0-first-wave-is-exactly-axis-sites-when-empty-is-zero",
        o0_exact_when_empty_zero
        and empty_zero_size == (1 << (other_bits - 1))
        and f_L1(empty_cell) == 0
        and first_wave_o0(f_L1, locks) == tuple(sorted(AXIS_SITES)),
        f"|F_wt1_empty0|={empty_zero_size}",
    )
    checks.check(
        "theorem3-L1-is-in-the-wt1-ready-subclass",
        f_L1(wt1_rep) == 1 and mapping[wt1_cells[0]] == wt1_rep,
    )

    # Mutations: Hamming parity is not L1; o=0 is not blank-block.
    checks.check(
        "mutation-hamming-parity-is-not-f-L1",
        f_hamming_parity(two_axis_wt2) != f_L1(two_axis_wt2)
        and all(f_hamming_parity(cell) == f_L1(cell) for cell in wt1_cells),
    )
    checks.check(
        "mutation-o0-is-not-blank-block-on-axis-sites",
        first_wave_o0(f_L1, locks) != first_wave_blank_block(f_L1, locks)
        and first_wave_o0(f_L1, locks) == tuple(sorted(AXIS_SITES)),
    )

    unread = "A site with no record cannot be read."
    nn_sentence = (
        "For each site, the probability distribution over the possibilities is "
        "determined by, and varies with, the nearest-neighbor conditions."
    )
    checks.check(
        "axiom-unread-and-nn-sentences-current",
        unread in axiom and nn_sentence in normalized_axiom,
    )
    checks.check(
        "axiom-no-formation-site-or-rate",
        "it does not supply the formation site, probability, or rate" in normalized_axiom,
    )

    claim_scope = (
        "On the twelve-vertex two-cube, replacing off-patch o=0 by blank-block "
        "empties the 1-site first wave for every cube-covariant f, including "
        "every f with f(wt1)=1. Displayed, not adopted."
    )
    checks.check("note-claim-scope-matches-spec", claim_scope in note)
    machine_markers = (
        "actual_current_surface_status: bounded-support",
        "target_claim_type: bounded_theorem",
        "claim_type_reason:",
        "hypothetical_axiom_status: no edit",
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
    )
    checks.check(
        "note-machine-status-complete",
        all(marker in note for marker in machine_markers),
    )
    checks.check(
        "note-one-hop-dependency-axioms-only",
        "upstream_dependencies:\n  - minimal_axioms" in note
        and "MINIMAL_AXIOMS_2026-06-29.md" in note,
    )
    checks.check(
        "note-displayed-not-adopted-and-not-l1-only",
        "Displayed, not adopted" in note
        and "not only for L1" in normalized_note
        and "not a second vacalt" in normalized_note,
    )
    forbidden = (
        "G_" + "N",
        "1/" + "r",
        "1/" + "r^2",
        "Lattice-" + "named",
        "not a " + "TOE",
    )
    checks.check(
        "note-avoids-forbidden-phrases",
        all(token not in note for token in forbidden),
    )
    checks.check(
        "note-states-f-L1-is-unbalanced-axis",
        "unbalanced" in normalized_note
        and "Hamming" in note
        and "n≠0" in note,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
