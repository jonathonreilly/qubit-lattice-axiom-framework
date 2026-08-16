#!/usr/bin/env python3
"""Census whether a third radius-2 ℓ¹ seed breaks tied-n swap symmetry.

U3 = B_2(0) ∪ B_2((2,0,0)) ∪ B_2((0,2,0)). Unread 4-occupied-NN sites
in the box |x|,|y|,|z|≤6 are scored by n = d/3 from U3 occupancy only.
The theorem reports N_4, N_uneq, and N_noswap. Displayed, not adopted.
"""

from __future__ import annotations

import ast
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/THREE_SEED_L1_BALL_TIED_N_BREAK_"
    "BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/THREE_SEED_L1_BALL_TIED_N_BREAK_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

BOX = 6
RADIUS = 2
SEEDS: tuple[tuple[int, int, int], ...] = ((0, 0, 0), (2, 0, 0), (0, 2, 0))
NEIGHBORS: tuple[tuple[int, int, int], ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
SLOT_NAME = {
    (1, 0, 0): "+x",
    (-1, 0, 0): "-x",
    (0, 1, 0): "+y",
    (0, -1, 0): "-y",
    (0, 0, 1): "+z",
    (0, 0, -1): "-z",
}
TIED_AXES: tuple[tuple[tuple[int, int, int], tuple[int, int, int]], ...] = (
    ((1, 0, 0), (-1, 0, 0)),
    ((0, 1, 0), (0, -1, 0)),
    ((0, 0, 1), (0, 0, -1)),
)

Vector = tuple[Fraction, Fraction, Fraction]
Rotation = tuple[tuple[int, int, int], tuple[int, int, int]]
Site = tuple[int, int, int]


def add(left: Site, right: Site) -> Site:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def l1(left: Site, right: Site) -> int:
    return abs(left[0] - right[0]) + abs(left[1] - right[1]) + abs(left[2] - right[2])


def ball(center: Site, radius: int = RADIUS) -> frozenset[Site]:
    lo = [axis - radius for axis in center]
    hi = [axis + radius for axis in center]
    return frozenset(
        (x, y, z)
        for x, y, z in product(
            range(lo[0], hi[0] + 1),
            range(lo[1], hi[1] + 1),
            range(lo[2], hi[2] + 1),
        )
        if l1((x, y, z), center) <= radius
    )


def permutation_sign(permutation: tuple[int, int, int]) -> int:
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(3)
        for j in range(i + 1, len(permutation))
    )
    return -1 if inversions % 2 else 1


G_PLUS: tuple[Rotation, ...] = tuple(
    (permutation, signs)
    for permutation in permutations((0, 1, 2))
    for signs in product((-1, 1), repeat=3)
    if permutation_sign(permutation) * signs[0] * signs[1] * signs[2] == 1
)


def rotate_vector(rotation: Rotation, vector: Vector) -> Vector:
    permutation, signs = rotation
    result = [Fraction(0), Fraction(0), Fraction(0)]
    for source_axis in range(3):
        result[permutation[source_axis]] = signs[source_axis] * vector[source_axis]
    return (result[0], result[1], result[2])


def slot_vector(slot: Site) -> Vector:
    return (Fraction(slot[0]), Fraction(slot[1]), Fraction(slot[2]))


def occupancy_kernel(site: Site, occupied: frozenset[Site]) -> Vector:
    components: list[Fraction] = []
    for axis in range(3):
        step = [0, 0, 0]
        step[axis] = 1
        plus = add(site, (step[0], step[1], step[2]))
        minus = add(site, (-step[0], -step[1], -step[2]))
        dipole = int(plus in occupied) - int(minus in occupied)
        components.append(Fraction(dipole, 3))
    return (components[0], components[1], components[2])


def support_size(kernel: Vector) -> int:
    return sum(component != 0 for component in kernel)


def stabilizer(kernel: Vector) -> tuple[Rotation, ...]:
    return tuple(
        rotation
        for rotation in G_PLUS
        if rotate_vector(rotation, kernel) == kernel
    )


def swaps_slots(rotation: Rotation, plus: Site, minus: Site) -> bool:
    return rotate_vector(rotation, slot_vector(plus)) == slot_vector(minus)


def format_kernel(kernel: Vector) -> str:
    return "(" + ", ".join(str(component) for component in kernel) + ")"


def parse_audit_input_paths(source: str) -> object:
    tree = ast.parse(source)
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id == "AUDIT_INPUT_PATHS":
                return ast.literal_eval(node.value)
    raise AssertionError("AUDIT_INPUT_PATHS assignment is missing")


def normalize(text: str) -> str:
    return " ".join(text.split())


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, condition: bool, detail: str) -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        print(f"{'PASS' if ok else 'FAIL'}: {label} {detail}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def census(occupied: frozenset[Site]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for site in product(range(-BOX, BOX + 1), repeat=3):
        if site in occupied:
            continue
        occupied_slots = tuple(slot for slot in NEIGHBORS if add(site, slot) in occupied)
        if len(occupied_slots) != 4:
            continue
        kernels = {
            slot: occupancy_kernel(add(site, slot), occupied) for slot in occupied_slots
        }
        ambiguous = tuple(
            (slot, kernels[slot])
            for slot in occupied_slots
            if support_size(kernels[slot]) != 1
        )
        ambiguous_kernels = [kernel for _, kernel in ambiguous]
        unequal = any(
            left != right for left in ambiguous_kernels for right in ambiguous_kernels
        )
        tied: list[tuple[Site, Site, Vector, int, bool]] = []
        no_swap = False
        for plus, minus in TIED_AXES:
            if plus not in kernels or minus not in kernels:
                continue
            kernel = kernels[plus]
            if kernel != kernels[minus]:
                continue
            if support_size(kernel) == 1 or support_size(kernels[minus]) == 1:
                continue
            stab = stabilizer(kernel)
            swap = any(swaps_slots(rotation, plus, minus) for rotation in stab)
            tied.append((plus, minus, kernel, len(stab), swap))
            if not swap:
                no_swap = True
        rows.append(
            {
                "site": site,
                "occupied_slots": occupied_slots,
                "kernels": kernels,
                "ambiguous": ambiguous,
                "unequal": unequal,
                "tied": tuple(tied),
                "no_swap": no_swap,
            }
        )
    rows.sort(key=lambda row: row["site"])
    return rows


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

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print("scientific_dependency: current minimal_axioms Lattice covariance clause")
    print("declared_math: U3 occupancy; n = d/3; finite G+ in the 3-vector representation")

    checks.check(
        "audit-input-paths",
        AUDIT_INPUT_PATHS
        == (
            "docs/THREE_SEED_L1_BALL_TIED_N_BREAK_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and literal_paths == AUDIT_INPUT_PATHS
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and AUDIT_TIMEOUT_SEC == 120,
        "AUDIT_INPUT_PATHS is the required static two-string literal tuple",
    )
    checks.check(
        "g-plus-order",
        len(G_PLUS) == 24 and len(set(G_PLUS)) == 24,
        "finite G+ is exactly the 24 proper cube rotations",
    )

    balls = tuple(ball(seed) for seed in SEEDS)
    occupied = frozenset().union(*balls)
    pairwise = (
        len(balls[0] & balls[1]),
        len(balls[0] & balls[2]),
        len(balls[1] & balls[2]),
    )
    triple = len(balls[0] & balls[1] & balls[2])
    print(f"U3_size: {len(occupied)}")
    print(f"ball_sizes: {[len(item) for item in balls]}")
    print(f"pairwise_overlaps: {list(pairwise)}")
    print(f"triple_overlap: {triple}")
    checks.check(
        "u3-geometry",
        all(len(item) == 25 for item in balls)
        and pairwise == (7, 7, 3)
        and triple == 2
        and len(occupied) == 60
        and all(max(abs(axis) for axis in site) <= BOX for site in occupied),
        "U3 is the union of three radius-2 ℓ¹ balls and lies inside the box",
    )

    rows = census(occupied)
    n4 = len(rows)
    n_uneq = sum(1 for row in rows if row["unequal"])
    n_noswap = sum(1 for row in rows if row["no_swap"])
    print(f"N_4: {n4}")
    print(f"N_uneq: {n_uneq}")
    print(f"N_noswap: {n_noswap}")
    for row in rows:
        site = row["site"]
        amb = ", ".join(
            f"{SLOT_NAME[slot]}:{format_kernel(kernel)}"
            for slot, kernel in row["ambiguous"]
        )
        tied = ", ".join(
            f"{SLOT_NAME[plus]}/{SLOT_NAME[minus]} n={format_kernel(kernel)} "
            f"|Stab|={order} swap={swap}"
            for plus, minus, kernel, order, swap in row["tied"]
        )
        print(f"site {site} amb=[{amb}] tied=[{tied}]")

    checks.check(
        "theorem-1-n4",
        n4 == 4 and f"N_4 = {n4}" in note,
        f"unread 4-occupied-NN count is N_4 = {n4}",
    )
    checks.check(
        "theorem-1-n-uneq",
        n_uneq == 0
        and all(len(row["ambiguous"]) == 2 for row in rows)
        and all(
            row["ambiguous"][0][1] == row["ambiguous"][1][1]
            for row in rows
        )
        and f"N_uneq = {n_uneq}" in note,
        f"no census site has unequal ambiguous n; N_uneq = {n_uneq}",
    )
    checks.check(
        "theorem-1-n-noswap",
        n_noswap == 0
        and all(len(row["tied"]) == 1 for row in rows)
        and all(row["tied"][0][4] for row in rows)
        and all(row["tied"][0][3] == 2 for row in rows)
        and f"N_noswap = {n_noswap}" in note,
        f"every tied pair has a slot-swap in Stab(n); N_noswap = {n_noswap}",
    )

    breakers = [row for row in rows if row["unequal"] or row["no_swap"]]
    no_break = n_uneq + n_noswap == 0 and breakers == []
    checks.check(
        "theorem-2-no-break",
        no_break
        and "the third seed does not break the obstruction on this `U3`" in note_flat,
        "N_uneq + N_noswap = 0, so the third seed does not break the obstruction",
    )

    expected_sites = ((-1, 1, -1), (-1, 1, 1), (1, -1, -1), (1, -1, 1))
    site_set = tuple(row["site"] for row in rows)
    opposite_allowed = any(
        not row["tied"][0][4] or row["unequal"] for row in rows if row["tied"]
    )
    checks.check(
        "theorem-2-sites-and-labels",
        site_set == expected_sites
        and not opposite_allowed
        and "Opposite labels are not equivariance-allowed" in note
        and "(1, −1, 1)" in note
        and "(1, −1, −1)" in note
        and "(−1, 1, 1)" in note
        and "(−1, 1, −1)" in note,
        "the four census sites match and opposite labels are not equivariance-allowed",
    )

    n_v1 = occupancy_kernel((2, -1, 1), occupied)
    n_v2 = occupancy_kernel((2, -1, -1), occupied)
    n_v3 = occupancy_kernel((-1, 2, 1), occupied)
    n_v4 = occupancy_kernel((-1, 2, -1), occupied)
    checks.check(
        "occupancy-kernels",
        n_v1 == (Fraction(0), Fraction(1, 3), Fraction(-1, 3))
        and n_v2 == (Fraction(0), Fraction(1, 3), Fraction(1, 3))
        and n_v3 == (Fraction(1, 3), Fraction(0), Fraction(-1, 3))
        and n_v4 == (Fraction(1, 3), Fraction(0), Fraction(1, 3))
        and "n = d/3" in note
        and "(0, 1/3, −1/3)" in note
        and "(0, 1/3, 1/3)" in note
        and "(1/3, 0, −1/3)" in note
        and "(1/3, 0, 1/3)" in note,
        "tied kernels are n = d/3 from U3 occupancy at the four sites",
    )

    swap_v1 = next(
        rotation
        for rotation in stabilizer(n_v1)
        if swaps_slots(rotation, (1, 0, 0), (-1, 0, 0))
    )
    swap_v2 = next(
        rotation
        for rotation in stabilizer(n_v2)
        if swaps_slots(rotation, (1, 0, 0), (-1, 0, 0))
    )
    swap_v3 = next(
        rotation
        for rotation in stabilizer(n_v3)
        if swaps_slots(rotation, (0, 1, 0), (0, -1, 0))
    )
    swap_v4 = next(
        rotation
        for rotation in stabilizer(n_v4)
        if swaps_slots(rotation, (0, 1, 0), (0, -1, 0))
    )
    plus_x = slot_vector((1, 0, 0))
    plus_y = slot_vector((0, 1, 0))
    plus_z = slot_vector((0, 0, 1))
    checks.check(
        "swapper-actions",
        rotate_vector(swap_v1, plus_x) == slot_vector((-1, 0, 0))
        and rotate_vector(swap_v1, plus_y) == slot_vector((0, 0, -1))
        and rotate_vector(swap_v2, plus_x) == slot_vector((-1, 0, 0))
        and rotate_vector(swap_v2, plus_y) == plus_z
        and rotate_vector(swap_v3, plus_y) == slot_vector((0, -1, 0))
        and rotate_vector(swap_v4, plus_y) == slot_vector((0, -1, 0))
        and "x, y, z) ↦ (−x, −z, −y)" in note
        and "x, y, z) ↦ (−x, z, y)" in note
        and "x, y, z) ↦ (−z, −y, −x)" in note
        and "x, y, z) ↦ (z, −y, x)" in note,
        "each tied kernel has an explicit G+ swapper of the tied slots",
    )
    checks.check(
        "lattice-clause",
        "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
        in axiom
        and "proper cubic rotations about each site" in axiom_flat
        and "proper cubic rotations about each site" in note_flat,
        "the current Lattice wording supplies finite proper cubic rotations",
    )
    checks.check(
        "admissibility-unedited",
        "one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations"
        in axiom_flat
        and "Do not write three-seed geometry into Admissibility" in note_flat
        and "B_2((0,2,0))" not in axiom
        and "three-seed" not in axiom.lower(),
        "three-seed geometry is displayed and is not written into Admissibility",
    )
    checks.check(
        "displayed-not-adopted",
        "Displayed, not adopted" in note
        and "Do not attach L1" in note
        and "not leftover-char of nstab" in note_flat
        and "leftover-char 10 of nstab" in note_flat
        and "finite G+ = 24 only" in note_flat.replace("`", "")
        and "Score geometry and `n` only" in note
        and "No new patch family" in note,
        "the note reports the U3 census without adopting it, attaching L1, or reusing nstab",
    )
    forbidden = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")
    script_body = self_source.split("forbidden = ", 1)[0]
    checks.check(
        "forbidden-phrases",
        all(phrase not in note for phrase in forbidden)
        and all(phrase not in script_body for phrase in forbidden),
        "the forbidden rhetoric strings are absent from the note and runner",
    )
    checks.check(
        "claim-scope",
        'claim_scope: "On the union of three radius-2 ℓ¹ balls at 0, (2,0,0), and (0,2,0), whether any unread 4-occupied-NN site has unequal ambiguous n or a non-swapping stabilizer, is reported. Displayed, not adopted."'
        in note
        and "**Type:** bounded_theorem" in note
        and "actual_current_surface_status: bounded-support" in note
        and "hypothetical_axiom_status: no edit" in note,
        "claim_scope and machine status match the displayed-not-adopted residual",
    )
    checks.check(
        "no-axiom-edit",
        "[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)" in note
        and "no axiom edit" in note_flat.lower()
        and "cache_write: false" in self_source
        and AXIOM_REL in AUDIT_INPUT_PATHS,
        "the only axiom authority is the current memo; no cache or axiom rewrite",
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
