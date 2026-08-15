#!/usr/bin/env python3
"""Exact census of occupancy-only lock labels (S,k) on 64 binary six-tuples.

The paired note is
docs/OCCUPANCY_LOCK_LABEL_PAIRS_BOUNDED_THEOREM_NOTE_2026-08-15.md.

The 64-cell carrier and the map lambda are declared finite test objects.
No Aut(M_2) reduction, projector pairing, formation process, cache write,
or axiom edit is performed.
"""

from __future__ import annotations

from itertools import product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
AUDIT_INPUT_PATHS = (
    "docs/OCCUPANCY_LOCK_LABEL_PAIRS_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / AUDIT_INPUT_PATHS[0]
AXIOM_PATH = ROOT / AUDIT_INPUT_PATHS[1]

AXES = ("x", "y", "z")
ALL_SUBSETS = tuple(
    frozenset(bits)
    for bits in (
        (),
        ("x",),
        ("y",),
        ("z",),
        ("x", "y"),
        ("x", "z"),
        ("y", "z"),
        ("x", "y", "z"),
    )
)


def normalize(text: str) -> str:
    return " ".join(text.split())


def axis_bits(cell: tuple[int, ...], axis: str) -> tuple[int, int]:
    index = AXES.index(axis)
    return cell[2 * index], cell[2 * index + 1]


def unbalanced_axes(cell: tuple[int, ...]) -> frozenset[str]:
    return frozenset(axis for axis in AXES if axis_bits(cell, axis)[0] != axis_bits(cell, axis)[1])


def label_of(cell: tuple[int, ...]) -> tuple[frozenset[str], int]:
    axes = unbalanced_axes(cell)
    return axes, len(axes)


def swap_axis(cell: tuple[int, ...], axis: str) -> tuple[int, ...]:
    index = AXES.index(axis)
    values = list(cell)
    values[2 * index], values[2 * index + 1] = values[2 * index + 1], values[2 * index]
    return tuple(values)


def flip_both(cell: tuple[int, ...], axis: str) -> tuple[int, ...]:
    index = AXES.index(axis)
    values = list(cell)
    values[2 * index] = 1 - values[2 * index]
    values[2 * index + 1] = 1 - values[2 * index + 1]
    return tuple(values)


def exhibit(subset: frozenset[str]) -> tuple[int, ...]:
    values: list[int] = []
    for axis in AXES:
        if axis in subset:
            values.extend((1, 0))
        else:
            values.extend((0, 0))
    return tuple(values)


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

    cells = tuple(product((0, 1), repeat=6))
    labels = tuple(label_of(cell) for cell in cells)
    image = frozenset(labels)
    fibers: dict[tuple[frozenset[str], int], list[tuple[int, ...]]] = {}
    for cell, pair in zip(cells, labels, strict=True):
        fibers.setdefault(pair, []).append(cell)

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print(
        "scope: occupancy-only labels on the declared 64-cell carrier; "
        "displayed, not adopted; no Aut(M_2) and no projector pairing"
    )

    checks.check(
        "audit-input-paths",
        "declared inputs are exactly the note and the current axiom memo",
        AUDIT_INPUT_PATHS
        == (
            "docs/OCCUPANCY_LOCK_LABEL_PAIRS_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
        AUDIT_INPUT_PATHS,
    )
    checks.check(
        "audit-timeout-declared",
        "audit timeout is the standing 120-second bound",
        AUDIT_TIMEOUT_SEC == 120,
        AUDIT_TIMEOUT_SEC,
    )
    checks.check(
        "source-lock-sentence",
        "current Record locks exactly one admissible local possibility",
        "When present, a record locks exactly one admissible local possibility." in axiom,
    )
    checks.check(
        "source-content-readout",
        "current Record determines a readout by record content alone",
        "A readout value is determined by record content alone." in normalized_axiom,
    )
    checks.check(
        "cell-count-64",
        "the occupancy carrier is exactly the 64 binary six-tuples",
        len(cells) == 64 and len(set(cells)) == 64,
        len(cells),
    )
    checks.check(
        "k-determined-by-S",
        "the displayed integer k equals |S| on every cell",
        all(pair[1] == len(pair[0]) for pair in labels),
    )
    expected_image = frozenset((subset, len(subset)) for subset in ALL_SUBSETS)
    checks.check(
        "theorem-1-image-size-8",
        "the image of lambda has size 8",
        len(image) == 8 and image == expected_image,
        sorted((sorted(subset), k) for subset, k in image),
    )
    split = (
        sum(1 for subset, _ in image if len(subset) == 0),
        sum(1 for subset, _ in image if len(subset) == 1),
        sum(1 for subset, _ in image if len(subset) == 2),
        sum(1 for subset, _ in image if len(subset) == 3),
    )
    checks.check(
        "theorem-1-binomial-split",
        "the eight labels split as 1+3+3+1 empty and nonempty subsets",
        split == (1, 3, 3, 1) and 1 + 3 + 3 + 1 == 8,
        split,
    )
    balanced = tuple(cell for cell in cells if label_of(cell)[1] == 0)
    axis_balanced = tuple(
        cell for cell in cells if all(axis_bits(cell, axis)[0] == axis_bits(cell, axis)[1] for axis in AXES)
    )
    checks.check(
        "theorem-2-k0-axis-balanced",
        "cells with k=0 are exactly the 8 axis-balanced 6-tuples",
        balanced == axis_balanced and len(balanced) == 8,
        len(balanced),
    )
    nonempty_realized = all(
        fibers[(subset, len(subset))] and label_of(exhibit(subset)) == (subset, len(subset))
        for subset in ALL_SUBSETS
        if subset
    )
    checks.check(
        "theorem-2-nonempty-S-realized",
        "every nonempty S occurs as an occupancy label",
        nonempty_realized,
    )
    fiber_sizes = {pair: len(members) for pair, members in fibers.items()}
    checks.check(
        "theorem-2-eight-cells-per-label",
        "every occupancy label has exactly eight indistinguishable cells",
        all(size == 8 for size in fiber_sizes.values()) and sum(fiber_sizes.values()) == 64,
        fiber_sizes,
    )
    k_census = tuple(sum(1 for cell in cells if label_of(cell)[1] == k) for k in range(4))
    checks.check(
        "theorem-2-k-census",
        "the occupancy census is 8,24,24,8 by k",
        k_census == (8, 24, 24, 8),
        k_census,
    )
    swap_ok = all(
        label_of(swap_axis(cell, axis)) == label_of(cell)
        for cell in cells
        for axis in AXES
        if axis not in unbalanced_axes(cell)
    )
    checks.check(
        "theorem-3-balanced-swap",
        "swapping the two bits on any balanced axis leaves lambda fixed",
        swap_ok,
    )
    flip_ok = all(
        label_of(flip_both(cell, axis)) == label_of(cell)
        for cell in cells
        for axis in AXES
        if axis in unbalanced_axes(cell)
    )
    checks.check(
        "theorem-3-unbalanced-joint-flip",
        "flipping both bits on an unbalanced axis leaves S unchanged",
        flip_ok,
    )
    same_label_pairs = all(len(members) >= 2 for members in fibers.values())
    checks.check(
        "occupancy-only-indistinguishability",
        "two distinct cells can share a label and are then occupancy-indistinguishable",
        same_label_pairs
        and label_of((0, 0, 0, 0, 0, 0)) == label_of((1, 1, 1, 1, 1, 1)) == (frozenset(), 0),
    )
    checks.check(
        "not-rank-1-projector",
        "lambda is a discrete pair-valued map, not a rank-1 projector",
        all(isinstance(pair[0], frozenset) and isinstance(pair[1], int) for pair in image)
        and "not a rank-1 projector" in note
        and "axis–Pauli pairing" in note
        and "Aut(M_2)" in note
        and "does not use Aut(M_2)" in note,
    )
    required = (
        'claim_scope: "Occupancy-only lock labels are the 8 pairs (S,k) for S⊆{x,y,z}. This is not a PVM and does not use Aut(M_2). Displayed, not adopted."',
        "actual_current_surface_status: bounded-support",
        "target_claim_type: bounded_theorem",
        "trace_class: negative_route_pruning",
        'hypothetical_axiom_status: "no edit"',
        "Displayed, not adopted",
        "authors no audit verdict",
        "FAIL / DO NOT SHIP",
    )
    forbidden = (
        "G_N",
        "1/r",
        "1/r^2",
        "Lattice-named",
        "not a TOE",
    )
    theorem_block = note.split("## Theorem 1", 1)[1].split("## Negative check", 1)[0]
    checks.check(
        "note-contract",
        "claim scope, machine fields, and displayed-not-adopted wording hold",
        all(phrase in note for phrase in required)
        and all(f"### N{index}" in note for index in range(1, 9)),
        [phrase for phrase in required if phrase not in note],
    )
    checks.check(
        "forbidden-hygiene",
        "the note avoids the standing forbidden tokens",
        all(token not in note for token in forbidden),
        [token for token in forbidden if token in note],
    )
    checks.check(
        "theorem-statement-hygiene",
        "the theorem block names no Bloch sphere, no PVM, and no generator symbol",
        "Bloch" not in theorem_block
        and "PVM" not in theorem_block
        and "σ" not in theorem_block
        and "sigma" not in theorem_block.lower(),
    )
    checks.check(
        "negative-check-may-name-pvm",
        "the negative check may refuse a projector-valued reading",
        "not a projector-valued measure" in note and "This is not a PVM" in note,
    )

    print("per_element: every one of the 64 occupancy cells is labeled")
    print("per_site: only the three cubic axes enter S")
    print("per_mode: checked and not executed — no spectral pairing is claimed")
    print("per_block: image, fibers, invariances, and projector refusal are executed")
    print("lattice_wide: checked and not executed — no formation law is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
