#!/usr/bin/env python3
"""Exact checks that realized first-wave PVM labels do not feed n.

Same L1 occupancy kernel as the two-cube integrated member. After tick 1,
lock labels +/− at first-wave sites leave occupancy 1. The kernel n at every
unread site, and the tick-2 formation set, are identical for the all-+
assignment and the mixed assignment. Every helper is identity-gated.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "TWO_CUBE_L1_DRAW_DOES_NOT_FEED_N_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/TWO_CUBE_L1_DRAW_DOES_NOT_FEED_N_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Site = tuple[int, int, int]
Locks = frozenset[Site]
Vec3 = tuple[Fraction, Fraction, Fraction]
Assignment = dict[Site, str]

AXES: tuple[Site, Site, Site] = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
ZERO_N: Vec3 = (Fraction(0), Fraction(0), Fraction(0))
SEED: Site = (0, 0, 0)
FIRST_WAVE: tuple[Site, Site, Site] = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
TICK2_FORMATION: Locks = frozenset({(1, 1, 0), (1, 0, 1), (0, 1, 1), (2, 0, 0)})


def add_site(site: Site, step: Site) -> Site:
    return (site[0] + step[0], site[1] + step[1], site[2] + step[2])


def cube_a_vertices() -> frozenset[Site]:
    return frozenset((x, y, z) for x in (0, 1) for y in (0, 1) for z in (0, 1))


def cube_b_vertices() -> frozenset[Site]:
    return frozenset((x, y, z) for x in (1, 2) for y in (0, 1) for z in (0, 1))


def patch_vertices() -> frozenset[Site]:
    return cube_a_vertices() | cube_b_vertices()


def occupancy(site: Site, locks: Locks) -> int:
    if site not in patch_vertices():
        return 0
    return 1 if site in locks else 0


def occupancy_with_labels(site: Site, locks: Locks, assignment: Assignment) -> int:
    """Occupancy ignores realized PVM labels: a labeled lock still has o=1."""
    if site not in patch_vertices():
        return 0
    if site in locks:
        if site in assignment:
            label = assignment[site]
            if label not in ("+", "-"):
                raise ValueError(f"lock label must be + or -, got {label!r}")
        return 1
    return 0


def n_vector(site: Site, locks: Locks, assignment: Assignment | None = None) -> Vec3:
    occ = occupancy if assignment is None else (
        lambda neighbor, _locks=locks, _asg=assignment: occupancy_with_labels(
            neighbor, _locks, _asg
        )
    )
    components = []
    for axis in AXES:
        plus = occ(add_site(site, axis), locks)
        minus = occ(add_site(site, (-axis[0], -axis[1], -axis[2])), locks)
        components.append(Fraction(plus - minus, 3))
    return (components[0], components[1], components[2])


def k_value(n: Vec3) -> int:
    squared = sum((3 * component) ** 2 for component in n)
    if squared.denominator != 1:
        raise ValueError(f"k left Q: {squared}")
    return int(squared)


def site_forms(site: Site, locks: Locks, assignment: Assignment | None = None) -> bool:
    if site in locks or site not in patch_vertices():
        return False
    return n_vector(site, locks, assignment) != ZERO_N


def spectral_traces(k: int) -> tuple[Fraction, Fraction]:
    if k != 1:
        raise ValueError("PVM traces restricted to k=1 so the runner stays in Q")
    root = 1
    return Fraction(3 + root, 6), Fraction(3 - root, 6)


def forming_sites(locks: Locks, assignment: Assignment | None = None) -> Locks:
    return frozenset(
        site for site in patch_vertices() if site_forms(site, locks, assignment)
    )


def unread_sites(locks: Locks) -> Locks:
    return frozenset(site for site in patch_vertices() if site not in locks)


def all_plus() -> Assignment:
    return {site: "+" for site in FIRST_WAVE}


def mixed_assignment() -> Assignment:
    return {(1, 0, 0): "+", (0, 1, 0): "-", (0, 0, 1): "-"}


def signed_occupancy_mutation(site: Site, locks: Locks, assignment: Assignment) -> int:
    """Mutation: treat a minus label as vacant. Not the L1 occupancy rule."""
    if site not in patch_vertices():
        return 0
    if site not in locks:
        return 0
    if site in assignment and assignment[site] == "-":
        return 0
    return 1


def n_under_signed_mutation(site: Site, locks: Locks, assignment: Assignment) -> Vec3:
    components = []
    for axis in AXES:
        plus = signed_occupancy_mutation(add_site(site, axis), locks, assignment)
        minus = signed_occupancy_mutation(
            add_site(site, (-axis[0], -axis[1], -axis[2])), locks, assignment
        )
        components.append(Fraction(plus - minus, 3))
    return (components[0], components[1], components[2])


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        result = bool(condition)
        if result:
            self.passed += 1
        else:
            self.failed += 1
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")

    def identity_gate(self, name: str, computed: object, expected: object) -> None:
        self.check(f"id-{name}", f"{name} identity", computed == expected)

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    self_source = Path(__file__).read_text(encoding="utf-8")
    for relative in AUDIT_INPUT_PATHS:
        (ROOT / relative).read_text(encoding="utf-8")

    print("external_scientific_inputs: none; exact occupancy arithmetic on a supplied 12-vertex patch")
    print("package_local_integrity_reads: proposed source note and live axiom memo only")
    print("measure_boundary: exact integers and Fraction; PVM traces restricted to k=1")
    print("claim_boundary: realized first-wave labels do not feed n; L1 is displayed, not adopted")

    patch = patch_vertices()
    seed_locks: Locks = frozenset({SEED})
    empty: Locks = frozenset()
    plus_asg = all_plus()
    mixed_asg = mixed_assignment()

    checks.identity_gate("patch-count", len(patch), 12)
    checks.identity_gate("first-wave-on-patch", all(site in patch for site in FIRST_WAVE), True)
    checks.identity_gate("off-patch-occupancy", occupancy((-1, 0, 0), seed_locks), 0)
    checks.identity_gate("empty-forms-none", forming_sites(empty), empty)

    n_x = n_vector((1, 0, 0), seed_locks)
    n_y = n_vector((0, 1, 0), seed_locks)
    n_z = n_vector((0, 0, 1), seed_locks)
    checks.identity_gate("n-at-100", n_x, (Fraction(-1, 3), Fraction(0), Fraction(0)))
    checks.identity_gate("n-at-010", n_y, (Fraction(0), Fraction(-1, 3), Fraction(0)))
    checks.identity_gate("n-at-001", n_z, (Fraction(0), Fraction(0), Fraction(-1, 3)))
    checks.identity_gate("k-at-100", k_value(n_x), 1)
    checks.identity_gate("k-at-010", k_value(n_y), 1)
    checks.identity_gate("k-at-001", k_value(n_z), 1)
    checks.identity_gate("forming-set-tick1", forming_sites(seed_locks), frozenset(FIRST_WAVE))

    plus, minus = spectral_traces(1)
    checks.identity_gate("trace-plus", plus, Fraction(2, 3))
    checks.identity_gate("trace-minus", minus, Fraction(1, 3))
    checks.identity_gate("traces-sum", plus + minus, Fraction(1))

    after_tick1: Locks = seed_locks | frozenset(FIRST_WAVE)
    unread = unread_sites(after_tick1)
    checks.identity_gate("tick1-lock-count", len(after_tick1), 4)
    checks.identity_gate("unread-count", len(unread), 8)

    for site in FIRST_WAVE:
        checks.identity_gate(
            f"occ-plus-{site[0]}{site[1]}{site[2]}",
            occupancy_with_labels(site, after_tick1, plus_asg),
            1,
        )
        checks.identity_gate(
            f"occ-mixed-{site[0]}{site[1]}{site[2]}",
            occupancy_with_labels(site, after_tick1, mixed_asg),
            1,
        )
        checks.identity_gate(
            f"label-ignored-{site[0]}{site[1]}{site[2]}",
            occupancy_with_labels(site, after_tick1, plus_asg),
            occupancy_with_labels(site, after_tick1, mixed_asg),
        )

    expected_n: dict[Site, Vec3] = {
        (1, 1, 0): (Fraction(-1, 3), Fraction(-1, 3), Fraction(0)),
        (1, 0, 1): (Fraction(-1, 3), Fraction(0), Fraction(-1, 3)),
        (0, 1, 1): (Fraction(0), Fraction(-1, 3), Fraction(-1, 3)),
        (2, 0, 0): (Fraction(-1, 3), Fraction(0), Fraction(0)),
        (1, 1, 1): ZERO_N,
        (2, 1, 0): ZERO_N,
        (2, 0, 1): ZERO_N,
        (2, 1, 1): ZERO_N,
    }
    checks.identity_gate("expected-n-covers-unread", frozenset(expected_n), unread)

    n_plus = {site: n_vector(site, after_tick1, plus_asg) for site in unread}
    n_mixed = {site: n_vector(site, after_tick1, mixed_asg) for site in unread}
    n_bare = {site: n_vector(site, after_tick1) for site in unread}

    same_n = n_plus == n_mixed == n_bare == expected_n
    checks.check(
        "thm-n-assignment-independent",
        "n at every unread site before tick 2 is the same for both assignments",
        same_n,
    )
    for site in sorted(unread):
        tag = f"{site[0]}{site[1]}{site[2]}"
        checks.identity_gate(f"n-plus-{tag}", n_plus[site], expected_n[site])
        checks.identity_gate(f"n-mixed-{tag}", n_mixed[site], expected_n[site])

    form_plus = forming_sites(after_tick1, plus_asg)
    form_mixed = forming_sites(after_tick1, mixed_asg)
    form_bare = forming_sites(after_tick1)
    checks.identity_gate("form-plus", form_plus, TICK2_FORMATION)
    checks.identity_gate("form-mixed", form_mixed, TICK2_FORMATION)
    checks.identity_gate("form-bare", form_bare, TICK2_FORMATION)
    checks.check(
        "thm-formation-independent",
        "tick-2 formation set is independent of realized PVM content",
        form_plus == form_mixed == form_bare == TICK2_FORMATION,
    )
    checks.check(
        "thm-occupancy-one-both",
        "occupancy is 1 at every first-wave site in both assignments",
        all(
            occupancy_with_labels(site, after_tick1, plus_asg) == 1
            and occupancy_with_labels(site, after_tick1, mixed_asg) == 1
            for site in FIRST_WAVE
        ),
    )

    mutated_110 = n_under_signed_mutation((1, 1, 0), after_tick1, mixed_asg)
    mutated_011 = n_under_signed_mutation((0, 1, 1), after_tick1, mixed_asg)
    checks.check(
        "mutation-minus-is-not-vacant",
        "treating a minus label as vacant changes n at (1,1,0) and (0,1,1)",
        mutated_110 != n_mixed[(1, 1, 0)] and mutated_011 != n_mixed[(0, 1, 1)],
    )
    checks.check(
        "mutation-not-first-wave-set",
        "tick-2 formation set is not the first-wave set",
        form_plus != frozenset(FIRST_WAVE),
    )

    lattice_quote = (
        "Physical sites are the points of the cubic lattice `Z^3`, with "
        "nearest-neighbor adjacency, standard translations, and proper cubic "
        "rotations about each site."
    )
    qubit_quote = (
        "The full one-site possibility domain has algebraic presentation `M_2(C)`."
    )
    admissibility_quote = (
        "For each site, the probability distribution over the possibilities is "
        "determined by, and varies with, the nearest-neighbor conditions."
    )
    record_quote = "Records form."
    axiom_flat = " ".join(axiom.split())
    checks.check(
        "live-parent-quotes",
        "the note quotes all four live axiom sentences without rewrite",
        all(
            quote in axiom_flat and quote in note
            for quote in (
                lattice_quote,
                qubit_quote,
                admissibility_quote,
                record_quote,
            )
        ),
    )
    checks.check(
        "machine-status-contract",
        "bounded-support status and hypothetical_axiom_status: not proposed",
        "actual_current_surface_status: bounded-support" in note
        and "hypothetical_axiom_status: not proposed" in note,
    )
    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/TWO_CUBE_L1_DRAW_DOES_NOT_FEED_N_BOUNDED_THEOREM_NOTE_2026-08-14.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file(),
    )
    forbidden = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")
    checks.check(
        "note-hygiene",
        "L1 is displayed; Qubit stays M_2(C); forbidden strings absent",
        "L1 is displayed, not adopted" in note
        and "Qubit remains `M_2(C)`" in note
        and all(token not in note for token in forbidden)
        and "we adopt" not in note.lower()
        and ("import " + "qcd") not in self_source.lower(),
    )

    print("per_element: occupancy, n, and k=1 traces are recomputed at each first-wave site")
    print("per_site: n at every unread patch site is compared across the two assignments")
    print("per_mode: P+ and P- traces are the two spectral weights at k=1")
    print("per_block: tick-2 formation set is checked in both branches")
    print("lattice_wide: checked and not executed — the claim is the supplied 12-vertex patch")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
