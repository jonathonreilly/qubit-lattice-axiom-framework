#!/usr/bin/env python3
"""Exact checks: lex-first |S|<=3 seed splitting f_L1 from F_cut (0,0,1,1,1).

Two-cube, off-patch occupancy 0. Independent lock histories. No axiom edit,
no cache write, no network, no citation manifest.
"""

from __future__ import annotations

import ast
from dataclasses import dataclass
from itertools import combinations, permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / (
    "docs/F_CUT_WT1_ZERO_L1_FIRST_SPLIT_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_PATH = ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/F_CUT_WT1_ZERO_L1_FIRST_SPLIT_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Site = tuple[int, int, int]
Bits = tuple[int, int, int, int, int]

AXES = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
SITES: tuple[Site, ...] = tuple(
    (x, y, z) for x in range(3) for y in range(2) for z in range(2)
)
SITE_SET = frozenset(SITES)

# Remaining F_cut bits in the order (wt1, opp2, adj2, vertex3, mixed3).
F_L1: Bits = (1, 0, 1, 1, 1)
F0WT: Bits = (0, 0, 1, 1, 1)
F1: Bits = (1, 1, 1, 1, 1)

FORBIDDEN = (
    "G_" + "N",
    "1/" + "r",
    "1/" + "r^2",
    "Lattice-" + "named",
    "not a " + "TOE",
)

CLAIM_SCOPE = (
    "On the two-cube with off-patch o=0, the lex-first seed of size at most "
    "3 at which f_L1 fills and F_cut (0,0,1,1,1) does not is reported. "
    "Displayed, not adopted."
)


def add(left: Site, right: Site) -> Site:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def occupancy_tuple(site: Site, locked: frozenset[Site]) -> tuple[int, ...]:
    bits: list[int] = []
    for axis in AXES:
        plus = add(site, axis)
        minus = add(site, (-axis[0], -axis[1], -axis[2]))
        bits.append(int(plus in locked))
        bits.append(int(minus in locked))
    return tuple(bits)


def axis_pairs(cell: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    return ((cell[0], cell[1]), (cell[2], cell[3]), (cell[4], cell[5]))


def orbit_name(cell: tuple[int, ...]) -> str:
    pairs = axis_pairs(cell)
    weight = sum(cell)
    both = sum(1 for a, b in pairs if a == 1 and b == 1)
    unbalanced = sum(1 for a, b in pairs if a != b)
    if weight == 0:
        return "empty"
    if weight == 6:
        return "full"
    if weight == 1:
        return "wt1"
    if weight == 5:
        return "wt5"
    if weight == 2 and both == 1:
        return "opp2"
    if weight == 2 and unbalanced == 2:
        return "adj2"
    if weight == 4 and both == 2:
        return "opp4"
    if weight == 4:
        return "adj4"
    if weight == 3 and both == 1:
        return "vertex3"
    if weight == 3 and unbalanced == 3:
        return "mixed3"
    raise ValueError(f"unclassified cell {cell}")


def n_neq_0(cell: tuple[int, ...]) -> int:
    return int(any(a != b for a, b in axis_pairs(cell)))


def hamming_parity(cell: tuple[int, ...]) -> int:
    return sum(cell) % 2


def eval_bits(bits: Bits, cell: tuple[int, ...]) -> int:
    name = orbit_name(cell)
    if name in ("empty", "full"):
        return 0
    if name in ("wt1", "wt5"):
        return bits[0]
    if name in ("opp2", "opp4"):
        return bits[1]
    if name in ("adj2", "adj4"):
        return bits[2]
    if name == "vertex3":
        return bits[3]
    if name == "mixed3":
        return bits[4]
    raise ValueError(name)


def all_cells() -> tuple[tuple[int, ...], ...]:
    return tuple(tuple((n >> k) & 1 for k in range(6)) for n in range(64))


def proper_cube_rotations() -> tuple[tuple[int, ...], ...]:
    """24 proper rotations as permutations of the six signed-axis slots."""
    images: list[tuple[int, ...]] = []
    for perm in permutations(range(3)):
        parity = 0
        seen = list(perm)
        for i in range(3):
            while seen[i] != i:
                j = seen[i]
                seen[i], seen[j] = seen[j], seen[i]
                parity += 1
        for signs in product((-1, 1), repeat=3):
            if (parity + sum(1 for s in signs if s < 0)) % 2 != 0:
                continue
            image = [0] * 6
            for axis in range(3):
                for sign_bit, sign in ((0, 1), (1, -1)):
                    src = 2 * axis + sign_bit
                    new_axis = perm[axis]
                    new_sign = sign * signs[axis]
                    image[src] = 2 * new_axis + (0 if new_sign == 1 else 1)
            images.append(tuple(image))
    return tuple(images)


def apply_perm(cell: tuple[int, ...], perm: tuple[int, ...]) -> tuple[int, ...]:
    out = [0] * 6
    for src, dst in enumerate(perm):
        out[dst] = cell[src]
    return tuple(out)


def rotation_orbits() -> dict[tuple[int, ...], frozenset[tuple[int, ...]]]:
    rots = proper_cube_rotations()
    seen: set[tuple[int, ...]] = set()
    orbits: dict[tuple[int, ...], frozenset[tuple[int, ...]]] = {}
    for cell in all_cells():
        if cell in seen:
            continue
        orbit = frozenset(apply_perm(cell, rot) for rot in rots)
        seen.update(orbit)
        orbits[min(orbit)] = orbit
    return orbits


def run_map(bits: Bits, seed: tuple[Site, ...]) -> tuple[tuple[int, ...], tuple[frozenset[Site], ...]]:
    locked = frozenset(seed)
    counts = [len(locked)]
    layers = [locked]
    for _ in range(12):
        nxt = set(locked)
        for site in SITES:
            if site in locked:
                continue
            if eval_bits(bits, occupancy_tuple(site, locked)) == 1:
                nxt.add(site)
        nxt_f = frozenset(nxt)
        if nxt_f == locked:
            return tuple(counts), tuple(layers)
        locked = nxt_f
        counts.append(len(locked))
        layers.append(locked)
    return tuple(counts), tuple(layers)


def fills(bits: Bits, seed: tuple[Site, ...]) -> bool:
    return run_map(bits, seed)[0][-1] == 12


def seeds_upto(max_size: int) -> tuple[tuple[Site, ...], ...]:
    out: list[tuple[Site, ...]] = []
    for size in range(1, max_size + 1):
        out.extend(combinations(SITES, size))
    return tuple(out)


def audit_paths_literal(source: str) -> tuple[str, ...] | None:
    tree = ast.parse(source)
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        if not any(isinstance(t, ast.Name) and t.id == "AUDIT_INPUT_PATHS" for t in node.targets):
            continue
        value = ast.literal_eval(node.value)
        if isinstance(value, tuple) and all(isinstance(item, str) for item in value):
            return value
    return None


@dataclass
class Checks:
    passed: int = 0
    failed: int = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        result = bool(condition)
        if result:
            self.passed += 1
        else:
            self.failed += 1
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    source = Path(__file__).read_text(encoding="utf-8")

    print(
        "external_scientific_inputs: none; no observational, fitted, literature, "
        "scale, or normalization value is used"
    )
    print(
        "explicit_bounded_inputs: the twelve-vertex two-cube, off-patch occupancy "
        "0, and the 32 complement-even F_cut maps are supplied finite data"
    )
    print(
        "framework_context: Lattice supplies Z^3 nearest-neighbor adjacency; "
        "Record supplies permanence of a formed lock; no map is written into "
        "Admissibility"
    )
    print(
        "package_local_integrity_reads: the proposed source note and current "
        "axiom memo are read; no cache or governance surface is written"
    )
    print(
        "measure_boundary: exact finite occupancy dynamics on 12 sites and 64 "
        "neighborhood cells"
    )
    print(
        "negative_scope: the first split seed is displayed and is not adopted; "
        "wt1 is not proposed as axiom content"
    )

    literal = audit_paths_literal(source)
    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the static pair (note, current axiom memo)",
        literal == AUDIT_INPUT_PATHS
        and AUDIT_INPUT_PATHS
        == (
            "docs/F_CUT_WT1_ZERO_L1_FIRST_SPLIT_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )

    checks.check(
        "source-lattice",
        "the axiom memo names Z^3 sites with nearest-neighbor adjacency",
        "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
        in axiom,
    )
    checks.check(
        "source-record",
        "the axiom memo states that a formed record locks one admissible possibility",
        "When present, a record locks exactly one admissible local possibility."
        in axiom,
    )

    rots = proper_cube_rotations()
    orbits = rotation_orbits()
    named = {orbit_name(cell) for cell in all_cells()}
    checks.check(
        "ten-orbits",
        "the 24 proper cube rotations partition the 64 cells into 10 orbits",
        len(rots) == 24 and len(orbits) == 10 and len(named) == 10,
    )

    n_cut = 2**5
    checks.check(
        "f-cut-count",
        "complement-even maps vanishing on empty and full number 32",
        n_cut == 32,
    )

    l1_match = all(eval_bits(F_L1, cell) == n_neq_0(cell) for cell in all_cells())
    ham_diff = sum(
        1 for cell in all_cells() if eval_bits(F_L1, cell) != hamming_parity(cell)
    )
    checks.check(
        "l1-is-n-neq-0",
        "f_L1 equals some-axis-unbalanced and is not Hamming parity",
        F_L1 == (1, 0, 1, 1, 1) and l1_match and ham_diff == 24,
    )
    checks.check(
        "f0wt-bits",
        "the displayed sibling is L1 with remaining bit wt1 flipped to 0",
        F0WT == (0, 0, 1, 1, 1) and F0WT[0] == 0 and F0WT[1:] == F_L1[1:],
    )

    seed0 = ((0, 0, 0),)
    hist_l1_0, layers_l1_0 = run_map(F_L1, seed0)
    hist_f0_0, layers_f0_0 = run_map(F0WT, seed0)
    checks.check(
        "l1-one-site-history",
        "L1 from (0,0,0) has lock counts (1, 4, 8, 11, 12)",
        hist_l1_0 == (1, 4, 8, 11, 12) and layers_l1_0[-1] == SITE_SET,
    )
    checks.check(
        "f0wt-one-site-halt",
        "F_cut (0,0,1,1,1) from (0,0,0) halts at the seed",
        hist_f0_0 == (1,) and layers_f0_0[-1] == frozenset(seed0),
    )

    seeds3 = tuple(combinations(SITES, 3))
    n_fill_l1_3 = sum(1 for seed in seeds3 if fills(F_L1, seed))
    n_fill_f0_3 = sum(1 for seed in seeds3 if fills(F0WT, seed))
    n_fill_f1_3 = sum(1 for seed in seeds3 if fills(F1, seed))
    checks.check(
        "theorem-1-l1-covers-220",
        "L1 fills all 220 three-site seeds",
        len(SITES) == 12 and len(seeds3) == 220 and n_fill_l1_3 == 220,
    )
    checks.check(
        "theorem-1-f0wt-not-max3",
        "F_cut (0,0,1,1,1) is not a 3-site maximizer",
        n_fill_f0_3 == 24
        and n_fill_f1_3 == 220
        and n_fill_f0_3 < n_fill_l1_3
        and F0WT != F_L1
        and F0WT != F1,
    )

    first: tuple[Site, ...] | None = None
    first_l1: tuple[int, ...] | None = None
    first_f0: tuple[int, ...] | None = None
    first_layers_l1: tuple[frozenset[Site], ...] | None = None
    first_layers_f0: tuple[frozenset[Site], ...] | None = None
    for seed in seeds_upto(3):
        hist_l1, layers_l1 = run_map(F_L1, seed)
        hist_f0, layers_f0 = run_map(F0WT, seed)
        if hist_l1[-1] == 12 and hist_f0[-1] != 12:
            first = seed
            first_l1 = hist_l1
            first_f0 = hist_f0
            first_layers_l1 = layers_l1
            first_layers_f0 = layers_f0
            break

    checks.check(
        "theorem-2-first-seed",
        "the lex-first |S|<=3 split seed is the one-site seed {(0,0,0)}",
        first == seed0 and first is not None and len(first) == 1,
    )

    split_tick = 0
    if first_layers_l1 is not None and first_layers_f0 is not None:
        limit = min(len(first_layers_l1), len(first_layers_f0))
        split_tick = next(
            (
                tick
                for tick in range(limit)
                if first_layers_l1[tick] != first_layers_f0[tick]
            ),
            limit,
        )
    new_l1 = (
        frozenset()
        if first_layers_l1 is None or split_tick == 0
        else first_layers_l1[split_tick] - first_layers_l1[split_tick - 1]
    )
    checks.check(
        "theorem-3-histories",
        "independent histories from that seed are (1,4,8,11,12) and (1)",
        first_l1 == (1, 4, 8, 11, 12)
        and first_f0 == (1,)
        and split_tick == 1
        and new_l1 == frozenset({(1, 0, 0), (0, 1, 0), (0, 0, 1)}),
    )

    compact_note = note.replace(" ", "")
    checks.check(
        "claim-scope",
        "the note reports the lex-first |S|<=3 split and does not adopt it",
        CLAIM_SCOPE in note
        and "Displayed, not adopted." in note
        and "(0,0,0)" in note,
    )
    checks.check(
        "note-reports-split",
        "the note records both lock histories and the tick-1 split",
        "(1, 4, 8, 11, 12)" in note
        and "halting lock history `(1)`" in note
        and "{(1,0,0),(0,1,0),(0,0,1)}" in compact_note,
    )
    checks.check(
        "not-adopted",
        "the note does not write wt1 or the sibling map into Admissibility",
        "Do not adopt wt1." in note
        and "not proposed as axiom content" in note.lower()
        and "Displayed, not adopted." in note,
    )

    forbidden_hits = [token for token in FORBIDDEN if token in note or token in source]
    checks.check(
        "forbidden-tokens",
        "note and runner omit the forbidden phrases",
        forbidden_hits == [],
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
