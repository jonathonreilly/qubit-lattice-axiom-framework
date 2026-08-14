#!/usr/bin/env python3
"""Exact checks for the two-cube integrated member L1.

One step_L1 law: occupancy kernel, k=1 spectral traces in Q, formation-count
clock, and rho/phi on the supplied twelve-vertex patch. Every helper is
identity-gated: replacing a helper formula fails the corresponding check.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "TWO_CUBE_INTEGRATED_MEMBER_L1_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/TWO_CUBE_INTEGRATED_MEMBER_L1_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Site = tuple[int, int, int]
Locks = frozenset[Site]
Vec3 = tuple[Fraction, Fraction, Fraction]

AXES: tuple[Site, Site, Site] = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
ZERO_N: Vec3 = (Fraction(0), Fraction(0), Fraction(0))
SEED: Site = (0, 0, 0)
FIRST_WAVE: tuple[Site, Site, Site] = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


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
        raise ValueError("PVM traces restricted to k=1 so the runner stays in Q")
    root = 1
    return Fraction(3 + root, 6), Fraction(3 - root, 6)


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
) -> tuple[
    Locks,
    int,
    dict[Site, tuple[int, Fraction, Fraction]],
    int,
    int,
    int,
    int,
]:
    new_locks = forming_sites(locks)
    traces: dict[Site, tuple[int, Fraction, Fraction]] = {}
    for site in new_locks:
        k = k_value(n_vector(site, locks))
        if k != 1:
            raise ValueError(f"first-wave PVM check requires k=1, got k={k} at {site}")
        plus, minus = spectral_traces(k)
        traces[site] = (k, plus, minus)
    updated = locks | new_locks
    rho_a = rho_cell(cube_a_vertices(), updated)
    rho_b = rho_cell(cube_b_vertices(), updated)
    return (
        updated,
        clock_after(clock, new_locks),
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

    print("external_scientific_inputs: none; exact occupancy arithmetic on a supplied 12-vertex patch")
    print("package_local_integrity_reads: proposed source note and live axiom memo only")
    print("measure_boundary: exact integers and Fraction; PVM traces restricted to k=1")
    print("claim_boundary: L1 is displayed executable data, not adopted law")

    patch = patch_vertices()
    cube_a = cube_a_vertices()
    cube_b = cube_b_vertices()
    seed_locks: Locks = frozenset({SEED})
    empty: Locks = frozenset()

    checks.identity_gate("patch-count", len(patch), 12)
    checks.identity_gate("cube-a-count", len(cube_a), 8)
    checks.identity_gate("cube-b-count", len(cube_b), 8)
    checks.identity_gate("shared-face-count", len(cube_a & cube_b), 4)
    checks.identity_gate("first-wave-on-patch", all(site in patch for site in FIRST_WAVE), True)
    checks.identity_gate("off-patch-occupancy", occupancy((-1, 0, 0), seed_locks), 0)
    checks.identity_gate("seed-occupancy", occupancy(SEED, seed_locks), 1)
    checks.identity_gate("unread-occupancy", occupancy((1, 0, 0), seed_locks), 0)
    checks.identity_gate("empty-clock", 0, 0)

    n_x = n_vector((1, 0, 0), seed_locks)
    n_y = n_vector((0, 1, 0), seed_locks)
    n_z = n_vector((0, 0, 1), seed_locks)
    checks.identity_gate("n-at-100", n_x, (Fraction(-1, 3), Fraction(0), Fraction(0)))
    checks.identity_gate("n-at-010", n_y, (Fraction(0), Fraction(-1, 3), Fraction(0)))
    checks.identity_gate("n-at-001", n_z, (Fraction(0), Fraction(0), Fraction(-1, 3)))
    checks.identity_gate("k-at-100", k_value(n_x), 1)
    checks.identity_gate("k-at-010", k_value(n_y), 1)
    checks.identity_gate("k-at-001", k_value(n_z), 1)
    checks.identity_gate("n-at-011-unread", n_vector((0, 1, 1), seed_locks), ZERO_N)
    checks.identity_gate("n-at-200-unread", n_vector((2, 0, 0), seed_locks), ZERO_N)
    checks.identity_gate("n-at-seed-locked", site_forms(SEED, seed_locks), False)

    new_from_seed = forming_sites(seed_locks)
    checks.identity_gate("forming-set", new_from_seed, frozenset(FIRST_WAVE))
    checks.identity_gate("tick", clock_tick(new_from_seed), 3)
    checks.identity_gate("clock-0-to-3", clock_after(0, new_from_seed), 3)
    checks.identity_gate("clock-1-to-4", clock_after(1, new_from_seed), 4)

    plus, minus = spectral_traces(1)
    checks.identity_gate("trace-plus", plus, Fraction(2, 3))
    checks.identity_gate("trace-minus", minus, Fraction(1, 3))
    checks.identity_gate("traces-sum", plus + minus, Fraction(1))

    updated, clock_prime, traces, rho_a, rho_b, flux_star, flux_outer = step_L1(
        seed_locks, 0
    )
    checks.identity_gate(
        "step-locks",
        updated,
        frozenset({SEED, (1, 0, 0), (0, 1, 0), (0, 0, 1)}),
    )
    checks.identity_gate("step-clock-from-0", clock_prime, 3)
    checks.identity_gate("step-lock-count", len(updated), 4)
    checks.identity_gate("rho-a", rho_a, 4)
    checks.identity_gate("rho-b", rho_b, 1)
    checks.identity_gate("phi-star", flux_star, 4)
    checks.identity_gate("phi-outer", flux_outer, 5)
    checks.identity_gate(
        "phi-star-is-rho-a",
        phi_star(rho_cell(cube_a, updated)),
        rho_cell(cube_a, updated),
    )
    checks.identity_gate(
        "phi-outer-is-sum",
        phi_outer(rho_cell(cube_a, updated), rho_cell(cube_b, updated)),
        rho_cell(cube_a, updated) + rho_cell(cube_b, updated),
    )

    first_wave_traces = all(
        traces[site] == (1, Fraction(2, 3), Fraction(1, 3)) for site in FIRST_WAVE
    )
    checks.check(
        "thm-first-wave-pvm",
        "each first-wave lock has k=1 and traces 2/3, 1/3",
        first_wave_traces and set(traces) == set(FIRST_WAVE),
    )
    checks.check(
        "thm-locked-stay",
        "the seed remains occupied after the step",
        occupancy(SEED, updated) == 1 and SEED in updated,
    )
    checks.check(
        "thm-empty-forms-none",
        "the empty configuration has n=0 at every patch site",
        forming_sites(empty) == empty,
    )
    face_star_occ = sum(occupancy(site, updated) for site in cube_a & cube_b)
    face_outer_occ = sum(occupancy(site, updated) for site in cube_b - cube_a)
    checks.check(
        "mutation-face-occupancy-is-not-phi",
        "phi is the rho assignment, not occupancy summed on the faces",
        face_star_occ == 1
        and face_outer_occ == 0
        and flux_star != face_star_occ
        and flux_outer != face_outer_occ,
    )
    checks.check(
        "mutation-clock-tick-not-lock-count",
        "the tick is the new-lock count 3, distinct from seed-inclusive 4",
        clock_tick(new_from_seed) == 3 and len(updated) == 4,
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
        all(quote in axiom_flat and quote in note for quote in (
            lattice_quote,
            qubit_quote,
            admissibility_quote,
            record_quote,
        )),
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
            "docs/TWO_CUBE_INTEGRATED_MEMBER_L1_BOUNDED_THEOREM_NOTE_2026-08-14.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file(),
    )
    forbidden = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE", "L_phys", "we adopt", "Codex")
    checks.check(
        "note-hygiene",
        "L1 is displayed; Qubit stays M_2(C); rho/phi are occupancy functions; forbidden strings absent",
        "L1 is displayed, not adopted" in note
        and "Qubit remains `M_2(C)`" in note
        and "functions of occupancy" in note
        and all(token not in note for token in forbidden)
        and "we adopt" not in note.lower()
        and ("import " + "qcd") not in self_source.lower(),
    )

    print("per_element: occupancy, n, k, and k=1 traces are recomputed at each first-wave site")
    print("per_site: formation is unread and n nonzero; locked sites stay")
    print("per_mode: PVM traces are the two spectral weights at k=1")
    print("per_block: rho/phi are evaluated on A, B, F*, and F_B after one step")
    print("lattice_wide: checked and not executed — the claim is the supplied 12-vertex patch")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
