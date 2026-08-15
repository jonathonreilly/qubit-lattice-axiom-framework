#!/usr/bin/env python3
"""Exact three-cut survivor count on the cube-covariant formation class.

The host is the 64 occupation cells of the six-ray cubic star and the 24
proper cube rotations. The raw class has size 2^10. This runner counts the
subclass that vanishes on empty and full and is complement-even. It does
not adopt a member.
"""

from __future__ import annotations

from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "FORMATION_CLASS_THREE_CUT_SURVIVORS_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/FORMATION_CLASS_THREE_CUT_SURVIVORS_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

RAYS: tuple[tuple[int, int, int], ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
N_CELLS = 64
N_ORB_DECLARED = 10


def normalize(text: str) -> str:
    return " ".join(text.split())


def permutation_sign(values: tuple[int, ...]) -> int:
    inversions = sum(
        values[i] > values[j]
        for i in range(len(values))
        for j in range(i + 1, len(values))
    )
    return -1 if inversions % 2 else 1


def apply_signed_permutation(
    ray: tuple[int, int, int],
    perm: tuple[int, ...],
    signs: tuple[int, ...],
) -> tuple[int, int, int]:
    moved = [0, 0, 0]
    for row in range(3):
        moved[row] = signs[row] * ray[perm[row]]
    return (moved[0], moved[1], moved[2])


def proper_cube_ray_permutations() -> tuple[tuple[int, ...], ...]:
    index = {ray: i for i, ray in enumerate(RAYS)}
    rotations: list[tuple[int, ...]] = []
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            if permutation_sign(perm) * signs[0] * signs[1] * signs[2] != 1:
                continue
            image = tuple(
                index[apply_signed_permutation(ray, perm, signs)] for ray in RAYS
            )
            rotations.append(image)
    return tuple(rotations)


def compose(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(left[i] for i in right)


def apply_perm(mask: int, perm: tuple[int, ...]) -> int:
    image = 0
    for src, dest in enumerate(perm):
        if mask >> src & 1:
            image |= 1 << dest
    return image


def complement(mask: int) -> int:
    return mask ^ (N_CELLS - 1)


def l1_weight(mask: int) -> int:
    return mask.bit_count()


def f_l1(mask: int) -> int:
    return l1_weight(mask) % 2


def orbit_of(mask: int, rotations: tuple[tuple[int, ...], ...]) -> frozenset[int]:
    return frozenset(apply_perm(mask, rot) for rot in rotations)


def all_orbits(rotations: tuple[tuple[int, ...], ...]) -> tuple[frozenset[int], ...]:
    seen: set[int] = set()
    orbits: list[frozenset[int]] = []
    for mask in range(N_CELLS):
        if mask in seen:
            continue
        orbit = orbit_of(mask, rotations)
        seen.update(orbit)
        orbits.append(orbit)
    return tuple(sorted(orbits, key=lambda orb: (min(orb), len(orb))))


def orbit_index(orbits: tuple[frozenset[int], ...], mask: int) -> int:
    for i, orbit in enumerate(orbits):
        if mask in orbit:
            return i
    raise KeyError(mask)


def opposite_pair_bits() -> tuple[frozenset[int], ...]:
    return (frozenset({0, 1}), frozenset({2, 3}), frozenset({4, 5}))


def occupied_axes(mask: int) -> int:
    return sum(1 for pair in opposite_pair_bits() if mask & sum(1 << b for b in pair))


def geometric_type(mask: int) -> str:
    weight = l1_weight(mask)
    if weight == 0:
        return "empty"
    if weight == 6:
        return "full"
    if weight == 1:
        return "wt1"
    if weight == 5:
        return "wt5"
    pairs = opposite_pair_bits()
    full_pairs = sum(
        1 for pair in pairs if all(mask >> bit & 1 for bit in pair)
    )
    if weight == 2:
        return "opp2" if full_pairs == 1 else "adj2"
    if weight == 4:
        return "opp4" if full_pairs == 2 else "adj4"
    if weight == 3:
        return "vertex3" if occupied_axes(mask) == 3 else "mixed3"
    raise ValueError(mask)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(
        self,
        label: str,
        statement: str,
        condition: bool,
        residual: object | None = None,
    ) -> None:
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
    source = Path(__file__).read_text(encoding="utf-8")
    for relative in AUDIT_INPUT_PATHS:
        (ROOT / relative).read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)

    print(
        "external_scientific_inputs: current Lattice/Admissibility/Record "
        "boundary only; no observation or fit"
    )
    print(
        "integrity_reads: this runner, its note, and the current axiom memo; "
        "no other scientific inputs"
    )
    print(
        "construction: 24 proper cube rotations on 64 six-ray cells; "
        "orbit partition under complement; free-bit count for three cuts"
    )
    print(
        "negative_scope: the three displayed cuts do not uniquely select "
        "f_L1; another extra remains; no member is adopted"
    )

    expected_tuple = (
        'AUDIT_INPUT_PATHS = (\n'
        '    "docs/FORMATION_CLASS_THREE_CUT_SURVIVORS_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ')'
    )
    checks.check(
        "audit-inputs",
        "declared inputs are the required two static string literals and exist",
        AUDIT_INPUT_PATHS
        == (
            "docs/FORMATION_CLASS_THREE_CUT_SURVIVORS_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and expected_tuple in source
        and AUDIT_TIMEOUT_SEC == 120
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file(),
    )

    lattice_sites = (
        "Physical sites are the points of the cubic lattice `Z^3`, with "
        "nearest-neighbor adjacency, standard translations, and proper cubic "
        "rotations about each site."
    )
    admissibility = (
        "There is one fixed nearest-neighbor admissibility rule, covariant "
        "under lattice translations and proper cubic rotations."
    )
    formation_residual = (
        "it does not supply the formation site, probability, or rate."
    )
    record_lock = "When present, a record locks exactly one admissible local possibility."
    record_content = "A readout value is determined by record content alone."
    record_absence = "A site with no record cannot be read."
    records_form = "Records form."

    checks.check(
        "source-lattice-admissibility",
        "Lattice rotations and Admissibility covariance are pinned",
        lattice_sites in normalized_axiom
        and admissibility in normalized_axiom
        and lattice_sites in normalized_note
        and admissibility in normalized_note,
    )
    checks.check(
        "source-record-boundary",
        "Record lock, content-only readout, unreadable absence, and formation residual are pinned",
        all(
            phrase in normalized_axiom
            for phrase in (
                records_form,
                record_lock,
                record_content,
                record_absence,
                formation_residual,
            )
        )
        and all(
            phrase in normalized_note
            for phrase in (
                records_form,
                record_lock,
                record_content,
                record_absence,
                formation_residual,
            )
        ),
    )

    rotations = proper_cube_ray_permutations()
    identity = tuple(range(6))
    checks.check(
        "rotation-group-order",
        "exactly 24 distinct proper cube rotations of the six rays",
        len(rotations) == 24 and len(set(rotations)) == 24 and identity in rotations,
    )
    closed = all(compose(left, right) in set(rotations) for left in rotations for right in rotations)
    inverses = all(
        any(compose(left, right) == identity for right in rotations) for left in rotations
    )
    checks.check(
        "rotation-group-laws",
        "the 24 maps are a group under composition",
        closed and inverses,
    )

    cells = tuple(range(N_CELLS))
    checks.check("cell-count", "the host has exactly 64 cells", len(cells) == 64)

    orbits = all_orbits(rotations)
    n_orb = len(orbits)
    checks.check(
        "orbit-count",
        "N_orb equals 10 and the orbits partition the 64 cells",
        n_orb == N_ORB_DECLARED
        and sum(len(orbit) for orbit in orbits) == 64
        and set().union(*orbits) == set(cells),
        residual=(n_orb, [len(orbit) for orbit in orbits]),
    )

    covariant_ok = all(
        apply_perm(mask, rot) in orbit_of(mask, rotations)
        for mask in cells
        for rot in rotations
    )
    checks.check(
        "orbit-covariance",
        "every rotation sends each cell into its own orbit",
        covariant_ok,
    )

    complement_cells = {complement(mask) for mask in cells}
    checks.check(
        "complement-permutes-cells",
        "c maps to 1-c is an involution of the 64 cells",
        complement_cells == set(cells)
        and all(complement(complement(mask)) == mask for mask in cells)
        and complement(0) == 63
        and complement(63) == 0,
    )

    image_orbits = []
    complement_fixed = []
    complement_pairs = []
    paired: set[int] = set()
    for i, orbit in enumerate(orbits):
        image = frozenset(complement(mask) for mask in orbit)
        image_orbits.append(image)
        j = orbit_index(orbits, min(image))
        if image != orbit:
            pair = tuple(sorted((i, j)))
            if pair not in paired:
                paired.add(pair)
                complement_pairs.append(pair)
        else:
            complement_fixed.append(i)
    checks.check(
        "complement-permutes-orbits",
        "complement sends orbits to orbits",
        set(image_orbits) == set(orbits),
    )

    empty_orbit = orbit_of(0, rotations)
    full_orbit = orbit_of(N_CELLS - 1, rotations)
    empty_idx = orbit_index(orbits, 0)
    full_idx = orbit_index(orbits, N_CELLS - 1)
    remaining_fixed = [
        i for i in complement_fixed if i not in (empty_idx, full_idx)
    ]
    pair_without_empty_full = [
        pair
        for pair in complement_pairs
        if set(pair) != {empty_idx, full_idx}
    ]

    checks.check(
        "theorem-1-empty-full",
        "empty and full are distinct singleton orbits exchanged by complement",
        empty_orbit == frozenset({0})
        and full_orbit == frozenset({N_CELLS - 1})
        and empty_idx != full_idx
        and complement(0) in full_orbit
        and {empty_idx, full_idx} in {frozenset(pair) for pair in complement_pairs},
    )
    checks.check(
        "theorem-1-partition",
        "the 10 orbits split as 1 empty + 1 full + 2 complement-fixed + 3 complement-pairs",
        len(orbits) == 10
        and len(complement_fixed) == 2
        and len(remaining_fixed) == 2
        and len(complement_pairs) == 4
        and len(pair_without_empty_full) == 3
        and 1 + 1 + len(remaining_fixed) + 2 * len(pair_without_empty_full) == 10,
        residual=(len(complement_fixed), len(complement_pairs), remaining_fixed),
    )

    type_of_orbit = {
        geometric_type(min(orbit)): frozenset(orbit) for orbit in orbits
    }
    expected_sizes = {
        "empty": 1,
        "full": 1,
        "wt1": 6,
        "wt5": 6,
        "opp2": 3,
        "opp4": 3,
        "adj2": 12,
        "adj4": 12,
        "vertex3": 8,
        "mixed3": 12,
    }
    type_sizes_ok = all(
        geometric_type(mask) in expected_sizes for mask in cells
    ) and all(
        sum(1 for mask in cells if geometric_type(mask) == name) == size
        for name, size in expected_sizes.items()
    )
    checks.check(
        "geometric-orbit-types",
        "geometric types recover the ten orbits and their sizes",
        type_sizes_ok
        and set(type_of_orbit) == set(expected_sizes)
        and all(len(type_of_orbit[name]) == size for name, size in expected_sizes.items()),
    )
    checks.check(
        "geometric-complement-pairs",
        "complement pairs are wt1/wt5, adj2/adj4, and opp2/opp4; vertex3 and mixed3 are fixed",
        type_of_orbit["wt1"] == frozenset(complement(m) for m in type_of_orbit["wt5"])
        and type_of_orbit["adj2"] == frozenset(complement(m) for m in type_of_orbit["adj4"])
        and type_of_orbit["opp2"] == frozenset(complement(m) for m in type_of_orbit["opp4"])
        and frozenset(complement(m) for m in type_of_orbit["vertex3"]) == type_of_orbit["vertex3"]
        and frozenset(complement(m) for m in type_of_orbit["mixed3"]) == type_of_orbit["mixed3"]
        and type_of_orbit["empty"] == frozenset(complement(m) for m in type_of_orbit["full"]),
    )

    n_free = len(pair_without_empty_full) + len(remaining_fixed)
    f_cut = 2 ** n_free
    f_raw = 2 ** n_orb
    checks.check(
        "theorem-2-free-bits",
        "N_free is 5 and |F_cut| is 32",
        n_free == 5 and f_cut == 32,
        residual=(n_free, f_cut),
    )
    checks.check(
        "raw-class-size",
        "the raw cube-covariant class has size 1024 and is not the three-cut residual",
        f_raw == 1024 and "|F_G| = 1024" in note and "not leftover-char" in note,
    )

    def orbit_value(predicate, orbit: frozenset[int]) -> int:
        values = {predicate(mask) for mask in orbit}
        if len(values) != 1:
            raise ValueError(values)
        return next(iter(values))

    l1_values = [orbit_value(f_l1, orbit) for orbit in orbits]
    l1_empty = f_l1(0)
    l1_full = f_l1(N_CELLS - 1)
    l1_even = all(f_l1(mask) == f_l1(complement(mask)) for mask in cells)
    l1_covariant = all(
        f_l1(mask) == f_l1(apply_perm(mask, rot))
        for mask in cells
        for rot in rotations
    )
    checks.check(
        "theorem-3-l1-in-fcut",
        "f_L1 is cube-covariant, vanishes on empty and full, and is complement-even",
        l1_covariant
        and l1_empty == 0
        and l1_full == 0
        and l1_even
        and l1_values[empty_idx] == 0
        and l1_values[full_idx] == 0,
    )

    other = [0] * n_orb
    vertex_idx = orbit_index(orbits, min(type_of_orbit["vertex3"]))
    other[vertex_idx] = 1
    other_fn = {
        mask: other[orbit_index(orbits, mask)] for mask in cells
    }
    other_in_cut = (
        other[empty_idx] == 0
        and other[full_idx] == 0
        and all(other_fn[mask] == other_fn[complement(mask)] for mask in cells)
        and other != l1_values
    )
    checks.check(
        "theorem-3-not-unique",
        "|F_cut| > 1 so f_L1 is not the unique survivor; another extra remains",
        f_cut > 1 and other_in_cut and "not unique" in note and "another extra" in note,
    )

    claim_scope = (
        "Among cube-covariant boolean formation predicates, the subclass that "
        "vanishes on empty and full and is complement-even has size 2^{N_free}. "
        "L1 is one element. Displayed, not adopted."
    )
    checks.check(
        "claim-scope",
        "claim_scope displays the 2^{N_free} subclass and does not adopt L1",
        claim_scope in note
        and "Displayed, not adopted" in note
        and "do not adopt" in note.lower(),
    )

    allowed_retained = (
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
    )
    other_retained = note
    for line in allowed_retained:
        other_retained = other_retained.replace(line, "")
    required = (
        "actual_current_surface_status: bounded-support",
        "target_claim_type: bounded_theorem",
        "trace_class: negative_route_pruning",
        "reachability_to_target: prunes",
        'hypothetical_axiom_status: "no edit"',
        "authors no audit verdict",
        "FAIL / DO NOT SHIP",
        "Theorem 1",
        "Theorem 2",
        "Theorem 3",
        "N_free = 5",
        "|F_cut| = 32",
    )
    forbidden = (
        "G_N",
        "1/r",
        "1/r^2",
        "Lattice-named",
        "not a TOE",
        "new axiom",
        "adopt f_L1 as the formation law",
        "unique survivor of the three cuts is f_L1",
    )
    checks.check(
        "note-contract",
        "machine fields, three theorems, and forbidden-phrase hygiene hold",
        all(phrase in note for phrase in required)
        and all(line in note for line in allowed_retained)
        and all(f"### N{i}" in note for i in range(1, 9))
        and not any(phrase in note for phrase in forbidden)
        and "retained" not in other_retained
        and "promoted" not in note.lower()
        and "toe-lphys" not in note
        and "runner-cache" not in note
        and "citation" not in note.lower(),
    )
    checks.check(
        "script-hygiene",
        "the runner states that it does not adopt a member",
        "does not adopt a member" in source
        and "Displayed, not adopted" in note,
    )
    checks.check(
        "axiom-unedited",
        "the axiom memo still carries the four named premises and no three-cut class",
        "### Lattice / Physical Locality" in axiom
        and "### Qubit / Site Possibility" in axiom
        and "### Admissibility / Local Constraint" in axiom
        and "### Record / Fixed Reality" in axiom
        and "F_cut" not in axiom
        and "f_L1" not in axiom,
    )

    print("per_element: each of the 64 cells is classified by orbit and complement")
    print("per_site: the six-ray star at one origin is the declared finite host")
    print("per_mode: checked and not executed — no spectral claim occurs")
    print("per_block: the ten-orbit partition and the 2^5 survivor count are executed")
    print(
        "lattice_wide: checked and not executed — no physical formation law "
        "or member adoption is claimed"
    )
    print(
        f"counts: N_orb={n_orb} n_empty=1 n_full=1 n_fixed={len(remaining_fixed)} "
        f"n_pairs={len(pair_without_empty_full)} N_free={n_free} |F_cut|={f_cut}"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
