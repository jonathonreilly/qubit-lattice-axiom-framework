#!/usr/bin/env python3
"""Exact checks for two-tick composition of the integrated member L1.

L1 is reconstructed locally on the supplied twelve-vertex two-cube patch.
Two successive ticks are one composition: occupancy kernel, formation-count
clock, k census, and rho/phi tree gauge. Tick-1 PVM traces stay in Q.
Tick-2 sites with k=2 are k-checked only; their traces are not forced into Q.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "TWO_CUBE_L1_TWO_TICK_COMPOSITION_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/TWO_CUBE_L1_TWO_TICK_COMPOSITION_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Site = tuple[int, int, int]
Locks = frozenset[Site]
Vec3 = tuple[Fraction, Fraction, Fraction]
KMap = dict[Site, int]
TraceMap = dict[Site, tuple[int, Fraction, Fraction]]

AXES: tuple[Site, Site, Site] = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
ZERO_N: Vec3 = (Fraction(0), Fraction(0), Fraction(0))
SEED: Site = (0, 0, 0)
TICK1_NEW: tuple[Site, Site, Site] = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
TICK2_NEW: tuple[Site, Site, Site, Site] = (
    (1, 1, 0),
    (1, 0, 1),
    (0, 1, 1),
    (2, 0, 0),
)
TICK2_K2: tuple[Site, Site, Site] = ((1, 1, 0), (1, 0, 1), (0, 1, 1))


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


def n_vector(site: Site, locks: Locks) -> Vec3:
    components = []
    for axis in AXES:
        plus = occupancy(add_site(site, axis), locks)
        minus = occupancy(add_site(site, (-axis[0], -axis[1], -axis[2])), locks)
        components.append(Fraction(plus - minus, 3))
    return (components[0], components[1], components[2])


def k_value(n: Vec3) -> int:
    squared = sum((3 * component) ** 2 for component in n)
    if squared.denominator != 1:
        raise ValueError(f"k left Q: {squared}")
    return int(squared)


def site_forms(site: Site, locks: Locks) -> bool:
    if site in locks or site not in patch_vertices():
        return False
    return n_vector(site, locks) != ZERO_N


def spectral_traces(k: int) -> tuple[Fraction, Fraction]:
    if k != 1:
        raise ValueError("PVM traces in Q are defined only at k=1")
    return Fraction(2, 3), Fraction(1, 3)


def clock_tick(new_locks: Locks) -> int:
    return len(new_locks)


def clock_after(clock: int, new_locks: Locks) -> int:
    return clock + clock_tick(new_locks)


def rho_cell(cell: frozenset[Site], locks: Locks) -> int:
    return sum(occupancy(site, locks) for site in cell)


def phi_star(rho_a: int) -> int:
    return rho_a


def phi_outer(rho_a: int, rho_b: int) -> int:
    return rho_a + rho_b


def forming_sites(locks: Locks) -> Locks:
    return frozenset(site for site in patch_vertices() if site_forms(site, locks))


def step_L1(
    locks: Locks, clock: int
) -> tuple[Locks, int, KMap, TraceMap, int, int, int, int]:
    new_locks = forming_sites(locks)
    ks: KMap = {}
    traces: TraceMap = {}
    for site in new_locks:
        k = k_value(n_vector(site, locks))
        ks[site] = k
        if k == 1:
            plus, minus = spectral_traces(k)
            traces[site] = (k, plus, minus)
    updated = locks | new_locks
    rho_a = rho_cell(cube_a_vertices(), updated)
    rho_b = rho_cell(cube_b_vertices(), updated)
    return (
        updated,
        clock_after(clock, new_locks),
        ks,
        traces,
        rho_a,
        rho_b,
        phi_star(rho_a),
        phi_outer(rho_a, rho_b),
    )


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

    print("external_scientific_inputs: none; exact two-tick occupancy arithmetic on a supplied 12-vertex patch")
    print("package_local_integrity_reads: proposed source note and live axiom memo only")
    print("measure_boundary: exact integers and Fraction; tick-2 k=2 sites are k-checked only")
    print("claim_boundary: two-tick composition of displayed L1, not adopted law")

    patch = patch_vertices()
    cube_a = cube_a_vertices()
    cube_b = cube_b_vertices()
    seed_locks: Locks = frozenset({SEED})
    empty: Locks = frozenset()

    checks.identity_gate("patch-count", len(patch), 12)
    checks.identity_gate("off-patch-occupancy", occupancy((-1, 0, 0), seed_locks), 0)
    checks.identity_gate("seed-occupancy", occupancy(SEED, seed_locks), 1)

    empty_locks, empty_clock, empty_ks, empty_traces, e_ra, e_rb, e_fs, e_fo = step_L1(
        empty, 0
    )
    checks.check(
        "thm-empty-fixed-point",
        "empty is a fixed point of step_L1",
        empty_locks == empty
        and empty_clock == 0
        and empty_ks == {}
        and empty_traces == {}
        and e_ra == 0
        and e_rb == 0
        and e_fs == 0
        and e_fo == 0,
    )
    empty_again, empty_clock_2, _, _, _, _, _, _ = step_L1(empty_locks, empty_clock)
    checks.identity_gate("empty-second-tick", (empty_again, empty_clock_2), (empty, 0))

    locks1, f1, ks1, traces1, rho_a1, rho_b1, flux_star1, flux_outer1 = step_L1(
        seed_locks, 0
    )
    checks.identity_gate("tick1-new-locks", frozenset(ks1), frozenset(TICK1_NEW))
    checks.identity_gate(
        "tick1-locks",
        locks1,
        frozenset({SEED, (1, 0, 0), (0, 1, 0), (0, 0, 1)}),
    )
    checks.identity_gate("tick1-clock", f1, 3)
    checks.identity_gate("tick1-rho-a", rho_a1, 4)
    checks.identity_gate("tick1-rho-b", rho_b1, 1)
    checks.identity_gate("tick1-phi-star", flux_star1, 4)
    checks.identity_gate("tick1-phi-outer", flux_outer1, 5)
    checks.check(
        "tick1-pvm-traces",
        "tick 1 is k=1 so traces are 2/3 and 1/3",
        all(ks1[site] == 1 for site in TICK1_NEW)
        and all(
            traces1[site] == (1, Fraction(2, 3), Fraction(1, 3)) for site in TICK1_NEW
        )
        and set(traces1) == set(TICK1_NEW),
    )

    new2 = forming_sites(locks1)
    checks.identity_gate("tick2-forming-set", new2, frozenset(TICK2_NEW))
    checks.identity_gate("tick2-new-count", clock_tick(new2), 4)

    for site in TICK2_K2:
        checks.identity_gate(
            f"tick2-k-at-{site[0]}{site[1]}{site[2]}",
            k_value(n_vector(site, locks1)),
            2,
        )
    checks.identity_gate("tick2-k-at-200", k_value(n_vector((2, 0, 0), locks1)), 1)

    locks2, f2, ks2, traces2, rho_a2, rho_b2, flux_star2, flux_outer2 = step_L1(
        locks1, f1
    )
    checks.identity_gate("tick2-clock", f2, 7)
    checks.identity_gate("tick2-lock-count", len(locks2), 8)
    checks.identity_gate("tick2-rho-a", rho_a2, 7)
    checks.identity_gate("tick2-rho-b", rho_b2, 4)
    checks.identity_gate("tick2-phi-star", flux_star2, 7)
    checks.identity_gate("tick2-phi-outer", flux_outer2, 11)
    checks.check(
        "tick2-k-only",
        "tick 2 records k and does not force k=2 traces into Q",
        ks2[(1, 1, 0)] == 2
        and ks2[(1, 0, 1)] == 2
        and ks2[(0, 1, 1)] == 2
        and ks2[(2, 0, 0)] == 1
        and (1, 1, 0) not in traces2
        and (1, 0, 1) not in traces2
        and (0, 1, 1) not in traces2
        and traces2.get((2, 0, 0)) == (1, Fraction(2, 3), Fraction(1, 3)),
    )

    checks.check(
        "thm-permanence",
        "every tick-1 lock is still locked after tick 2",
        frozenset(TICK1_NEW).issubset(locks2) and SEED in locks2 and locks1.issubset(locks2),
    )
    checks.check(
        "thm-clock-additivity",
        "F_2 = F_1 + |new_2|",
        f2 == f1 + clock_tick(new2) == 3 + 4,
    )
    checks.check(
        "thm-tree-gauge-both-ticks",
        "phi(F*)=rho(A) and phi(F_B)=rho(A)+rho(B) after both ticks",
        flux_star1 == rho_a1
        and flux_outer1 == rho_a1 + rho_b1
        and flux_star2 == rho_a2
        and flux_outer2 == rho_a2 + rho_b2
        and phi_star(rho_a2) == 7
        and phi_outer(rho_a2, rho_b2) == 11,
    )

    face_star_2 = sum(occupancy(site, locks2) for site in cube_a & cube_b)
    face_outer_2 = sum(occupancy(site, locks2) for site in cube_b - cube_a)
    checks.check(
        "mutation-face-occupancy-is-not-phi",
        "after two ticks, face occupancy sums are not the tree-gauge fluxes",
        face_star_2 == 3
        and face_outer_2 == 1
        and flux_star2 != face_star_2
        and flux_outer2 != face_outer_2,
    )
    checks.check(
        "mutation-clock-not-lock-count",
        "F_2 is 7, not the seed-inclusive lock count identity at tick 1",
        f2 == 7 and f1 != rho_a1 and clock_tick(new2) != len(locks2),
    )

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/TWO_CUBE_L1_TWO_TICK_COMPOSITION_BOUNDED_THEOREM_NOTE_2026-08-14.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and axiom.startswith("# Minimal Framework Axioms"),
    )
    checks.check(
        "machine-status-contract",
        "bounded-support status and no axiom edit",
        "actual_current_surface_status: bounded-support" in note
        and "hypothetical_axiom_status: no edit" in note,
    )
    forbidden = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")
    checks.check(
        "note-hygiene",
        "forbidden strings and radical symbol are absent; L1 is displayed",
        all(token not in note for token in forbidden)
        and "\u221a" not in note
        and "sqrt" not in note.lower()
        and "\u221a" not in self_source
        and "L1 is displayed, not adopted" in note
        and "we adopt" not in note.lower()
        and "Codex" not in note,
    )

    print("per_element: occupancy, n, and k are recomputed at each forming site")
    print("per_site: locked sites stay; unread sites form iff n is nonzero")
    print("per_mode: tick-1 traces stay in Q; tick-2 k=2 sites are k-checked only")
    print("per_block: rho/phi tree gauge is evaluated after each tick")
    print("lattice_wide: checked and not executed — the claim is the supplied 12-vertex patch")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
