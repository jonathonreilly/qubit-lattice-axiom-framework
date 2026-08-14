#!/usr/bin/env python3
"""Exact integer checks for L1 second-wave k on the two-cube patch.

After tick 1 locks the seed and three axis neighbors, recompute 3n in Z and
k = |3n|^2 at every unread patch site. Every helper is identity-gated:
replacing a helper formula fails the corresponding check.
"""

from __future__ import annotations

from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "TWO_CUBE_L1_SECOND_WAVE_K_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/TWO_CUBE_L1_SECOND_WAVE_K_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Site = tuple[int, int, int]
Locks = frozenset[Site]
Vec3 = tuple[int, int, int]

AXES: tuple[Site, Site, Site] = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
ZERO_3N: Vec3 = (0, 0, 0)
SEED: Site = (0, 0, 0)
FIRST_WAVE: tuple[Site, Site, Site] = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
TICK1_LOCKS: Locks = frozenset({SEED, (1, 0, 0), (0, 1, 0), (0, 0, 1)})
SECOND_WAVE: tuple[Site, Site, Site, Site] = (
    (1, 1, 0),
    (1, 0, 1),
    (0, 1, 1),
    (2, 0, 0),
)
SECOND_WAVE_TABLE: dict[Site, tuple[Vec3, int]] = {
    (1, 1, 0): ((-1, -1, 0), 2),
    (1, 0, 1): ((-1, 0, -1), 2),
    (0, 1, 1): ((0, -1, -1), 2),
    (2, 0, 0): ((-1, 0, 0), 1),
}


def add_site(site: Site, step: Site) -> Site:
    return (site[0] + step[0], site[1] + step[1], site[2] + step[2])


def cube_a_vertices() -> frozenset[Site]:
    return frozenset(
        (x, y, z) for x in (0, 1) for y in (0, 1) for z in (0, 1)
    )


def cube_b_vertices() -> frozenset[Site]:
    return frozenset(
        (x, y, z) for x in (1, 2) for y in (0, 1) for z in (0, 1)
    )


def patch_vertices() -> frozenset[Site]:
    return cube_a_vertices() | cube_b_vertices()


def occupancy(site: Site, locks: Locks) -> int:
    if site not in patch_vertices():
        return 0
    return 1 if site in locks else 0


def three_n(site: Site, locks: Locks) -> Vec3:
    components = []
    for axis in AXES:
        plus = occupancy(add_site(site, axis), locks)
        minus = occupancy(add_site(site, (-axis[0], -axis[1], -axis[2])), locks)
        components.append(plus - minus)
    return (components[0], components[1], components[2])


def k_value(vec: Vec3) -> int:
    return vec[0] * vec[0] + vec[1] * vec[1] + vec[2] * vec[2]


def site_forms(site: Site, locks: Locks) -> bool:
    if site in locks or site not in patch_vertices():
        return False
    return three_n(site, locks) != ZERO_3N


def forming_sites(locks: Locks) -> Locks:
    return frozenset(site for site in patch_vertices() if site_forms(site, locks))


def unread_patch_sites(locks: Locks) -> Locks:
    return frozenset(site for site in patch_vertices() if site not in locks)


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

    print("external_scientific_inputs: none; exact Z occupancy arithmetic on a supplied 12-vertex patch")
    print("package_local_integrity_reads: proposed source note and live axiom memo only")
    print("measure_boundary: exact integers; k = |3n|^2 stays in Z")
    print("claim_boundary: L1 is displayed executable data, not adopted law")

    patch = patch_vertices()
    seed_locks: Locks = frozenset({SEED})

    checks.identity_gate("patch-count", len(patch), 12)
    checks.identity_gate("cube-a-count", len(cube_a_vertices()), 8)
    checks.identity_gate("cube-b-count", len(cube_b_vertices()), 8)
    checks.identity_gate("off-patch-occupancy", occupancy((-1, 0, 0), TICK1_LOCKS), 0)
    checks.identity_gate("seed-occupancy", occupancy(SEED, TICK1_LOCKS), 1)

    tick1_from_seed = seed_locks | forming_sites(seed_locks)
    checks.identity_gate("tick1-locks-from-seed", tick1_from_seed, TICK1_LOCKS)
    checks.identity_gate("tick1-lock-count", len(TICK1_LOCKS), 4)

    for site, (expected_3n, expected_k) in SECOND_WAVE_TABLE.items():
        computed_3n = three_n(site, TICK1_LOCKS)
        computed_k = k_value(computed_3n)
        label = "".join(str(coord) for coord in site)
        checks.identity_gate(f"3n-at-{label}", computed_3n, expected_3n)
        checks.identity_gate(f"k-at-{label}", computed_k, expected_k)
        checks.check(
            f"3n-in-Z-{label}",
            f"3n at {site} is an integer triple",
            all(isinstance(component, int) for component in computed_3n),
        )

    new_at_tick2 = forming_sites(TICK1_LOCKS)
    checks.identity_gate("forming-set", new_at_tick2, frozenset(SECOND_WAVE))
    checks.identity_gate("forming-count", len(new_at_tick2), 4)

    other_unread = unread_patch_sites(TICK1_LOCKS) - frozenset(SECOND_WAVE)
    checks.identity_gate(
        "other-unread",
        other_unread,
        frozenset({(1, 1, 1), (2, 1, 0), (2, 0, 1), (2, 1, 1)}),
    )
    checks.check(
        "thm-no-other-unread-n",
        "every other unread patch site has 3n = 0",
        all(three_n(site, TICK1_LOCKS) == ZERO_3N for site in other_unread)
        and other_unread.isdisjoint(new_at_tick2),
    )
    checks.check(
        "thm-second-wave-table",
        "the four forming sites have the displayed 3n and k",
        all(
            (three_n(site, TICK1_LOCKS), k_value(three_n(site, TICK1_LOCKS)))
            == SECOND_WAVE_TABLE[site]
            for site in SECOND_WAVE
        )
        and new_at_tick2 == frozenset(SECOND_WAVE),
    )
    checks.check(
        "thm-k-in-1-2",
        "second-wave k values are exactly {1, 2}",
        {k_value(three_n(site, TICK1_LOCKS)) for site in SECOND_WAVE} == {1, 2},
    )
    checks.check(
        "thm-locked-stay",
        "tick-1 locks remain locked and do not re-form",
        all(not site_forms(site, TICK1_LOCKS) for site in TICK1_LOCKS)
        and TICK1_LOCKS.isdisjoint(new_at_tick2),
    )
    checks.check(
        "k-from-3n-squares",
        "k is the sum of squares of the integer components of 3n",
        k_value((-1, -1, 0)) == 2 and k_value((-1, 0, 0)) == 1,
    )
    checks.check(
        "mutation-k-not-uniform-1",
        "second-wave k is not uniformly 1",
        k_value(three_n((1, 1, 0), TICK1_LOCKS)) == 2
        and k_value(three_n((2, 0, 0), TICK1_LOCKS)) == 1,
    )
    checks.check(
        "mutation-k-is-not-a-trace",
        "k is |3n|^2 in Z, distinct from any one-site trace value",
        k_value(three_n((1, 1, 0), TICK1_LOCKS)) == 2
        and "k = |3n|^2" in note
        and "No one-site traces are evaluated at `k=2`" in note,
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
            "docs/TWO_CUBE_L1_SECOND_WAVE_K_BOUNDED_THEOREM_NOTE_2026-08-14.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file(),
    )
    forbidden = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE", "L_phys", "we adopt", "Codex")
    checks.check(
        "note-hygiene",
        "L1 is displayed; Qubit stays M_2(C); k stays in Z; forbidden strings absent",
        "L1 is displayed, not adopted" in note
        and "Qubit remains `M_2(C)`" in note
        and "k = |3n|^2 ∈ Z" in note
        and "√" not in note
        and all(token not in note for token in forbidden)
        and "we adopt" not in note.lower()
        and ("import " + "qcd") not in self_source.lower(),
    )

    print("per_element: 3n and k = |3n|^2 are recomputed at each unread patch site")
    print("per_site: formation is unread and n nonzero; locked sites stay")
    print("per_mode: k is the integer |3n|^2; no traces at k=2")
    print("per_block: tick-2 formation set is the four-site table")
    print("lattice_wide: checked and not executed — the claim is the supplied 12-vertex patch")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
