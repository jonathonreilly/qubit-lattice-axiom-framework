#!/usr/bin/env python3
"""Exact checks: lex-first |S|<=3 fill split of F_cut (1,0,0,0,0) vs (1,1,0,0,0).

Two-cube, off-patch occupancy 0. Independent lock histories. No axiom edit,
no cache write, no network, no citation manifest. f_L1 is n!=0, not Hamming.
"""

from __future__ import annotations

import ast
from dataclasses import dataclass
from itertools import combinations, permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/F_CUT_C00_C10_FIRST_SPLIT_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/F_CUT_C00_C10_FIRST_SPLIT_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Site = tuple[int, int, int]
Bits = tuple[int, int, int, int, int]

AXES = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
SITES: tuple[Site, ...] = tuple(
    (x, y, z) for x in range(3) for y in range(2) for z in range(2)
)
SITE_SET = frozenset(SITES)

# Remaining F_cut bits in the order (wt1, opp2, adj2, vertex3, mixed3).
F00: Bits = (1, 0, 0, 0, 0)
F10: Bits = (1, 1, 0, 0, 0)
F_L1: Bits = (1, 0, 1, 1, 1)

FORBIDDEN = (
    "G_" + "N",
    "1/" + "r",
    "1/" + "r^2",
    "Lattice-" + "named",
    "not a " + "TOE",
)

CLAIM_SCOPE = (
    "On the two-cube with off-patch o=0, the lex-first seed of size at most "
    "3 at which F_cut (1,0,0,0,0) and (1,1,0,0,0) disagree on fill is "
    "reported, or they agree on every such seed. Displayed, not adopted."
)

DISPLAY_MIDPOINT: Site = (1, 0, 0)
OPP2_CELL = (1, 1, 0, 0, 0, 0)


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


def remaining_bits_from_rule(rule) -> Bits:
    assignment: dict[str, int] = {}
    for cell in all_cells():
        name = orbit_name(cell)
        value = int(rule(cell))
        if name in assignment and assignment[name] != value:
            raise RuntimeError("rule is not cube-covariant")
        assignment[name] = value
    if assignment["empty"] != 0 or assignment["full"] != 0:
        raise RuntimeError("rule is not in F_cut")
    bits = (
        assignment["wt1"],
        assignment["opp2"],
        assignment["adj2"],
        assignment["vertex3"],
        assignment["mixed3"],
    )
    if (
        assignment["wt5"] != bits[0]
        or assignment["opp4"] != bits[1]
        or assignment["adj4"] != bits[2]
    ):
        raise RuntimeError("rule is not complement-even")
    return bits


def run_map(
    bits: Bits, seed: tuple[Site, ...]
) -> tuple[tuple[int, ...], tuple[frozenset[Site], ...]]:
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


def k_site_seeds(size: int) -> tuple[tuple[Site, ...], ...]:
    return tuple(combinations(SITES, size))


def seeds_upto(max_size: int) -> tuple[tuple[Site, ...], ...]:
    out: list[tuple[Site, ...]] = []
    for size in range(1, max_size + 1):
        out.extend(k_site_seeds(size))
    return tuple(out)


def coverage(bits: Bits, size: int) -> int:
    return sum(1 for seed in k_site_seeds(size) if fills(bits, seed))


def first_fill_split(
    left: Bits, right: Bits, max_size: int
) -> tuple[Site, ...] | None:
    for seed in seeds_upto(max_size):
        if fills(left, seed) != fills(right, seed):
            return seed
    return None


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
    compact_note = note.replace(" ", "")

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print("external_scientific_inputs: none; two-cube occupancy ticks only")
    print("explicit_bounded_inputs: the twelve-vertex two-cube, off-patch occupancy 0")
    print(
        "framework_context: Lattice supplies Z^3 nearest-neighbor adjacency; "
        "Record supplies permanence of a formed lock; no map is written into "
        "Admissibility"
    )
    print("package_local_integrity_reads: proposed source note and live axiom memo only")
    print("measure_boundary: exact integer occupancy, lock counts, and coverage")
    print("claim_boundary: displayed first fill split; opp2 is not adopted")
    print("negative_scope: the first split seed is displayed and is not adopted")

    literal = audit_paths_literal(source)
    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        literal == AUDIT_INPUT_PATHS
        and AUDIT_INPUT_PATHS
        == (
            "docs/F_CUT_C00_C10_FIRST_SPLIT_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and AUDIT_TIMEOUT_SEC == 120
        and 'AUDIT_INPUT_PATHS = (\n'
        '    "docs/F_CUT_C00_C10_FIRST_SPLIT_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in source,
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
        len(rots) == 24
        and len(orbits) == 10
        and len(named) == 10
        and len(SITES) == 12
        and SITES[0] == (0, 0, 0)
        and SITES[-1] == (2, 1, 1)
        and SITES == tuple(sorted(SITES)),
    )

    l1_from_n = remaining_bits_from_rule(n_neq_0)
    ham_bits = remaining_bits_from_rule(hamming_parity)
    checks.check(
        "l1-is-n-neq-0",
        "f_L1 equals some-axis-unbalanced and is not Hamming parity",
        l1_from_n == F_L1
        and ham_bits != F_L1
        and ham_bits == (1, 0, 0, 1, 1)
        and F_L1 == (1, 0, 1, 1, 1)
        and eval_bits(F_L1, (1, 0, 0, 0, 0, 0)) == 1
        and eval_bits(F_L1, OPP2_CELL) == 0
        and "sum(cell) % 2"
        not in source.split("def n_neq_0", 1)[1].split("def hamming_parity", 1)[0],
    )
    checks.check(
        "pair-in-fcut",
        "both remaining-bit tuples are F_cut maps and differ only on opp2",
        F00 == (1, 0, 0, 0, 0)
        and F10 == (1, 1, 0, 0, 0)
        and F00[0] == 1
        and F10[0] == 1
        and F00[1] == 0
        and F10[1] == 1
        and F00[2:] == (0, 0, 0)
        and F10[2:] == (0, 0, 0)
        and 2**5 == 32,
    )

    cov2_00 = coverage(F00, 2)
    cov2_10 = coverage(F10, 2)
    cov2_l1 = coverage(F_L1, 2)
    cov1_00 = coverage(F00, 1)
    cov1_10 = coverage(F10, 1)
    cov3_00 = coverage(F00, 3)
    cov3_10 = coverage(F10, 3)
    checks.check(
        "thm1-both-cov2-zero",
        "both maps have two-site coverage 0",
        cov2_00 == 0
        and cov2_10 == 0
        and cov1_00 == 0
        and cov1_10 == 0
        and cov2_l1 == 62
        and len(k_site_seeds(2)) == 66
        and "cov2(f00) = 0" in note
        and "cov2(f10) = 0" in note,
    )

    split = first_fill_split(F00, F10, 3)
    small_agree = all(
        fills(F00, seed) == fills(F10, seed) for seed in seeds_upto(2)
    )
    earlier_three = tuple(
        seed
        for seed in k_site_seeds(3)
        if split is not None and seed < split and fills(F00, seed) != fills(F10, seed)
    )
    checks.check(
        "thm2-lex-first-split",
        "the lex-first |S|<=3 fill disagreement is {(0,0,0),(1,1,1),(2,0,0)}",
        split == ((0, 0, 0), (1, 1, 1), (2, 0, 0))
        and small_agree
        and earlier_three == ()
        and "{(0,0,0),(1,1,1),(2,0,0)}" in compact_note
        and cov3_00 == 0
        and cov3_10 == 4
        and len(k_site_seeds(3)) == 220,
    )

    hist00, layers00 = run_map(F00, split) if split is not None else ((), ())
    hist10, layers10 = run_map(F10, split) if split is not None else ((), ())
    fill00 = hist00[-1] == 12 if hist00 else False
    fill10 = hist10[-1] == 12 if hist10 else False
    seed_locked = frozenset(split) if split is not None else frozenset()
    mid_cell = occupancy_tuple(DISPLAY_MIDPOINT, seed_locked)
    checks.check(
        "thm3-who-fills",
        "f10 fills the displayed seed and f00 does not",
        fill10 is True
        and fill00 is False
        and hist00 == (3, 11)
        and hist10 == (3, 12)
        and layers00[-1] == SITE_SET - {DISPLAY_MIDPOINT}
        and layers10[-1] == SITE_SET
        and "(3, 11)" in note
        and "(3, 12)" in note,
    )
    checks.check(
        "thm3-opp2-midpoint",
        "the leftover site (1,0,0) sees the opp2 cell; f00=0 and f10=1",
        mid_cell == OPP2_CELL
        and orbit_name(mid_cell) == "opp2"
        and eval_bits(F00, mid_cell) == 0
        and eval_bits(F10, mid_cell) == 1
        and DISPLAY_MIDPOINT not in layers00[-1]
        and DISPLAY_MIDPOINT in layers10[-1]
        and "opp2" in note,
    )

    same_map_split = first_fill_split(F00, F00, 3)
    checks.check(
        "mutation-same-map-has-no-split",
        "a map does not disagree with itself on any |S|<=3 seed",
        same_map_split is None,
    )
    checks.check(
        "mutation-hamming-is-not-l1",
        "Hamming parity is a different remaining-bit tuple from n!=0",
        ham_bits != F_L1
        and ham_bits != F00
        and ham_bits != F10
        and fills(ham_bits, ((0, 0, 0),)) is False
        and fills(F_L1, ((0, 0, 0),)) is True,
    )
    checks.check(
        "mutation-swap-who-fills-fails",
        "the swapped fill-bit claim is rejected by the recomputed histories",
        not (fill00 and not fill10),
    )
    checks.check(
        "claim-scope",
        "the note reports the lex-first |S|<=3 split and does not adopt it",
        CLAIM_SCOPE in note
        and "Displayed, not adopted." in note
        and "Do not adopt opp2." in note,
    )
    checks.check(
        "machine-status-contract",
        "bounded status, frontier trace, and next action are source-visible",
        "actual_current_surface_status: bounded-support" in note
        and "trace_class: frontier_discovery" in note
        and 'hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"'
        in note
        and 'next_trace_action: "independent audit of the bounded algebraic claim"'
        in note,
    )
    checks.check(
        "import-boundary-contract",
        "the supplied patch and absent physical bridge are disclosed",
        "## Inputs And Import Boundary" in note
        and "Explicit theorem-domain condition" in note
        and "External empirical or literature inputs:** none" in note
        and "Open physical bridge" in note,
    )
    checks.check(
        "live-parent-quotes",
        "the live Lattice and Record unread sentences are quoted without rewrite",
        "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
        in axiom
        and "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
        in note
        and "A site with no record cannot be read." in axiom
        and "A site with no record cannot be read." in note
        and "When present, a record locks exactly one admissible local possibility."
        in note,
    )
    checks.check(
        "l1-definition-in-note",
        "the note defines f_L1 as unbalanced-axis / n != 0 and rejects Hamming",
        "`n_μ = c_{+μ} − c_{-μ}`" in note
        and "This is **not** Hamming parity" in note
        and "`f_L1(c)=1` if and only if some axis is unbalanced" in note,
    )
    checks.check(
        "claim-type-and-forbidden",
        "the bounded type is declared and forbidden phrases are absent",
        "**Type:** bounded_theorem" in note
        and "### N8" not in note
        and "FAIL / DO NOT SHIP" not in note
        and all(token not in note and token not in source for token in FORBIDDEN)
        and ("import " + "qcd") not in source.lower()
        and ("from " + "qcd") not in source.lower(),
    )
    checks.check(
        "no-axiom-edit",
        "the theorem proposes no axiom change",
        "no axiom or approved primitive is added" in note
        and "hypothetical_axiom_status" in note
        and "Do not adopt opp2" in note
        and "no Admissibility sentence is rewritten" in note,
    )
    checks.check(
        "off-patch-zero",
        "off-patch occupancy is the explicit 0 default",
        "off-patch occupancy 0" in note or "off-patch occupancy `0`" in note,
    )

    print(f"n_rotations={len(rots)}")
    print(f"n_orbits={len(orbits)}")
    print(f"n_two_site_seeds={len(k_site_seeds(2))}")
    print(f"n_three_site_seeds={len(k_site_seeds(3))}")
    print(f"f00_remaining={F00}")
    print(f"f10_remaining={F10}")
    print(f"f_L1_remaining={F_L1}")
    print(f"cov2_f00={cov2_00}")
    print(f"cov2_f10={cov2_10}")
    print(f"cov2_f_L1={cov2_l1}")
    print(f"cov3_f00={cov3_00}")
    print(f"cov3_f10={cov3_10}")
    print(f"first_split={split}")
    print(f"f00_history={hist00} fill={fill00}")
    print(f"f10_history={hist10} fill={fill10}")
    print(f"midpoint_cell={mid_cell} kind={orbit_name(mid_cell)}")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
