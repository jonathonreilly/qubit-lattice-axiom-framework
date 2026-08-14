#!/usr/bin/env python3
"""Exact checks: L1 formation support at tick t is the ell^1 ball of radius t.

On the supplied twelve-vertex two-cube patch, two occupancy steps from the
seed are compared to the ell^1 ball computed from d(v)=|v_x|+|v_y|+|v_z|.
Every helper is identity-gated: replacing a helper formula fails the
corresponding check. No spectral traces are evaluated (tick-2 sites have
k=2).
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "TWO_CUBE_L1_L1_BALL_SUPPORT_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/TWO_CUBE_L1_L1_BALL_SUPPORT_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Site = tuple[int, int, int]
Locks = frozenset[Site]
Vec3 = tuple[Fraction, Fraction, Fraction]

AXES: tuple[Site, Site, Site] = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
ZERO_N: Vec3 = (Fraction(0), Fraction(0), Fraction(0))
SEED: Site = (0, 0, 0)


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


def n_vector(site: Site, locks: Locks) -> Vec3:
    components = []
    for axis in AXES:
        plus = occupancy(add_site(site, axis), locks)
        minus = occupancy(add_site(site, (-axis[0], -axis[1], -axis[2])), locks)
        components.append(Fraction(plus - minus, 3))
    return (components[0], components[1], components[2])


def site_forms(site: Site, locks: Locks) -> bool:
    if site in locks or site not in patch_vertices():
        return False
    return n_vector(site, locks) != ZERO_N


def forming_sites(locks: Locks) -> Locks:
    return frozenset(site for site in patch_vertices() if site_forms(site, locks))


def step_occupancy(locks: Locks) -> Locks:
    return locks | forming_sites(locks)


def l1_distance(site: Site) -> int:
    return abs(site[0]) + abs(site[1]) + abs(site[2])


def chebyshev_distance(site: Site) -> int:
    return max(abs(site[0]), abs(site[1]), abs(site[2]))


def l1_sphere(radius: int, patch: frozenset[Site]) -> Locks:
    return frozenset(site for site in patch if l1_distance(site) == radius)


def l1_ball(radius: int, patch: frozenset[Site]) -> Locks:
    return frozenset(site for site in patch if l1_distance(site) <= radius)


def chebyshev_ball(radius: int, patch: frozenset[Site]) -> Locks:
    return frozenset(site for site in patch if chebyshev_distance(site) <= radius)


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
    print("measure_boundary: exact integers and Fraction; formation support only, no PVM traces")
    print("claim_boundary: L1 is displayed executable data, not adopted law")

    patch = patch_vertices()
    seed_locks: Locks = frozenset({SEED})
    empty: Locks = frozenset()

    checks.identity_gate("patch-count", len(patch), 12)
    checks.identity_gate("d-seed", l1_distance(SEED), 0)
    checks.identity_gate("d-100", l1_distance((1, 0, 0)), 1)
    checks.identity_gate("d-110", l1_distance((1, 1, 0)), 2)
    checks.identity_gate("d-200", l1_distance((2, 0, 0)), 2)
    checks.identity_gate("d-111", l1_distance((1, 1, 1)), 3)
    checks.identity_gate("d-210", l1_distance((2, 1, 0)), 3)
    checks.identity_gate("d-201", l1_distance((2, 0, 1)), 3)
    checks.identity_gate("d-211", l1_distance((2, 1, 1)), 4)

    sphere0 = l1_sphere(0, patch)
    sphere1 = l1_sphere(1, patch)
    sphere2 = l1_sphere(2, patch)
    sphere3 = l1_sphere(3, patch)
    sphere4 = l1_sphere(4, patch)
    checks.identity_gate("sphere-0", sphere0, frozenset({SEED}))
    checks.identity_gate("sphere-1-count", len(sphere1), 3)
    checks.identity_gate("sphere-2-count", len(sphere2), 4)
    checks.identity_gate("sphere-3-count", len(sphere3), 3)
    checks.identity_gate("sphere-4-count", len(sphere4), 1)
    checks.identity_gate(
        "spheres-partition-patch",
        sphere0 | sphere1 | sphere2 | sphere3 | sphere4,
        patch,
    )
    checks.identity_gate(
        "sphere-1-sites",
        sphere1,
        frozenset({(1, 0, 0), (0, 1, 0), (0, 0, 1)}),
    )
    checks.identity_gate(
        "sphere-2-sites",
        sphere2,
        frozenset({(1, 1, 0), (1, 0, 1), (0, 1, 1), (2, 0, 0)}),
    )
    checks.identity_gate(
        "sphere-3-sites",
        sphere3,
        frozenset({(1, 1, 1), (2, 1, 0), (2, 0, 1)}),
    )
    checks.identity_gate("sphere-4-sites", sphere4, frozenset({(2, 1, 1)}))

    n_100 = n_vector((1, 0, 0), seed_locks)
    n_010 = n_vector((0, 1, 0), seed_locks)
    n_001 = n_vector((0, 0, 1), seed_locks)
    checks.identity_gate("n-100-seed", n_100, (Fraction(-1, 3), Fraction(0), Fraction(0)))
    checks.identity_gate("n-010-seed", n_010, (Fraction(0), Fraction(-1, 3), Fraction(0)))
    checks.identity_gate("n-001-seed", n_001, (Fraction(0), Fraction(0), Fraction(-1, 3)))
    checks.identity_gate("n-110-seed", n_vector((1, 1, 0), seed_locks), ZERO_N)
    checks.identity_gate("n-200-seed", n_vector((2, 0, 0), seed_locks), ZERO_N)
    checks.identity_gate("n-111-seed", n_vector((1, 1, 1), seed_locks), ZERO_N)
    checks.identity_gate("forming-from-seed", forming_sites(seed_locks), sphere1)

    after_t1 = step_occupancy(seed_locks)
    checks.identity_gate("thm1-locks-eq-ball-1", after_t1, l1_ball(1, patch))
    checks.identity_gate("thm1-lock-count", len(after_t1), 4)
    checks.identity_gate("thm1-seed-stays", SEED in after_t1, True)
    checks.identity_gate("thm1-sphere1-locked", sphere1 <= after_t1, True)
    checks.identity_gate(
        "thm1-sphere2-unread",
        all(site not in after_t1 for site in sphere2),
        True,
    )

    n_110_t1 = n_vector((1, 1, 0), after_t1)
    n_101_t1 = n_vector((1, 0, 1), after_t1)
    n_011_t1 = n_vector((0, 1, 1), after_t1)
    n_200_t1 = n_vector((2, 0, 0), after_t1)
    checks.identity_gate(
        "n-110-after-t1",
        n_110_t1,
        (Fraction(-1, 3), Fraction(-1, 3), Fraction(0)),
    )
    checks.identity_gate(
        "n-101-after-t1",
        n_101_t1,
        (Fraction(-1, 3), Fraction(0), Fraction(-1, 3)),
    )
    checks.identity_gate(
        "n-011-after-t1",
        n_011_t1,
        (Fraction(0), Fraction(-1, 3), Fraction(-1, 3)),
    )
    checks.identity_gate(
        "n-200-after-t1",
        n_200_t1,
        (Fraction(-1, 3), Fraction(0), Fraction(0)),
    )
    checks.identity_gate("n-111-after-t1", n_vector((1, 1, 1), after_t1), ZERO_N)
    checks.identity_gate("n-210-after-t1", n_vector((2, 1, 0), after_t1), ZERO_N)
    checks.identity_gate("n-201-after-t1", n_vector((2, 0, 1), after_t1), ZERO_N)
    checks.identity_gate("n-211-after-t1", n_vector((2, 1, 1), after_t1), ZERO_N)
    checks.identity_gate("forming-at-tick-2", forming_sites(after_t1), sphere2)

    after_t2 = step_occupancy(after_t1)
    checks.identity_gate("thm2-locks-eq-ball-2", after_t2, l1_ball(2, patch))
    checks.identity_gate("thm2-lock-count", len(after_t2), 8)
    checks.identity_gate("thm2-permanence", after_t1 <= after_t2, True)
    checks.identity_gate("thm2-sphere2-locked", sphere2 <= after_t2, True)

    unread_after_t2 = patch - after_t2
    checks.identity_gate("thm3-unread-eq-d-ge-3", unread_after_t2, sphere3 | sphere4)
    checks.identity_gate(
        "thm3-every-d3-unread",
        all(site not in after_t2 for site in sphere3),
        True,
    )
    checks.identity_gate(
        "thm3-every-d4-unread",
        all(site not in after_t2 for site in sphere4),
        True,
    )

    checks.check(
        "thm-empty-fixed",
        "the empty configuration forms no site",
        forming_sites(empty) == empty,
    )
    checks.check(
        "mutation-not-chebyshev-ball-1",
        "after tick 1 the locked set is not the Chebyshev ball of radius 1",
        after_t1 != chebyshev_ball(1, patch)
        and (1, 1, 0) in chebyshev_ball(1, patch)
        and (1, 1, 0) not in after_t1,
    )
    checks.check(
        "mutation-not-chebyshev-ball-2",
        "after tick 2 the locked set is not the Chebyshev ball of radius 2",
        after_t2 != chebyshev_ball(2, patch)
        and chebyshev_ball(2, patch) == patch
        and len(after_t2) == 8,
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
            "docs/TWO_CUBE_L1_L1_BALL_SUPPORT_BOUNDED_THEOREM_NOTE_2026-08-14.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file(),
    )
    forbidden = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE", "L_phys", "we adopt", "Codex")
    checks.check(
        "note-hygiene",
        "L1 is displayed; Qubit stays M_2(C); forbidden strings absent",
        "L1 is displayed, not adopted" in note
        and "Qubit remains `M_2(C)`" in note
        and all(token not in note for token in forbidden)
        and "we adopt" not in note.lower()
        and ("import " + "qcd") not in self_source.lower(),
    )

    print("per_element: n is recomputed at every unread patch site after each tick")
    print("per_site: formation is unread and n nonzero; locked sites stay")
    print("per_mode: support is compared to the computed ell^1 ball, not a Chebyshev ball")
    print("per_block: locked sets after ticks 1 and 2 are the radius-1 and radius-2 balls")
    print("lattice_wide: checked and not executed — the claim is the supplied 12-vertex patch")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
