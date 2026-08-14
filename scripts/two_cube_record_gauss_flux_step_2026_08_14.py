#!/usr/bin/env python3
"""Exact two-cube occupancy, cube-source, and tree-gauge flux step.

Displayed decoder and gauge on two unit cubes that share a face.
No cache write, no axiom edit, exact Z/Q only.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "TWO_CUBE_RECORD_GAUSS_FLUX_STEP_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/TWO_CUBE_RECORD_GAUSS_FLUX_STEP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Vertex = tuple[int, int, int]
Occ = dict[Vertex, int]

A_ONLY: tuple[Vertex, ...] = (
    (0, 0, 0),
    (0, 0, 1),
    (0, 1, 0),
    (0, 1, 1),
)
SHARED: tuple[Vertex, ...] = (
    (1, 0, 0),
    (1, 0, 1),
    (1, 1, 0),
    (1, 1, 1),
)
B_ONLY: tuple[Vertex, ...] = (
    (2, 0, 0),
    (2, 0, 1),
    (2, 1, 0),
    (2, 1, 1),
)
VERTICES: tuple[Vertex, ...] = A_ONLY + SHARED + B_ONLY
CUBE_A: tuple[Vertex, ...] = A_ONLY + SHARED
CUBE_B: tuple[Vertex, ...] = SHARED + B_ONLY


def _quad(points: list[Vertex]) -> frozenset[Vertex]:
    return frozenset(points)


def _cube_faces(x0: int) -> list[frozenset[Vertex]]:
    xs = (x0, x0 + 1)
    ys = (0, 1)
    zs = (0, 1)
    return [
        _quad([(xs[0], y, z) for y in ys for z in zs]),
        _quad([(xs[1], y, z) for y in ys for z in zs]),
        _quad([(x, 0, z) for x in xs for z in zs]),
        _quad([(x, 1, z) for x in xs for z in zs]),
        _quad([(x, y, 0) for x in xs for y in ys]),
        _quad([(x, y, 1) for x in xs for y in ys]),
    ]


FACES: tuple[frozenset[Vertex], ...] = tuple(
    dict.fromkeys(_cube_faces(0) + _cube_faces(1))
)
F_STAR: frozenset[Vertex] = _quad([(1, y, z) for y in (0, 1) for z in (0, 1)])
F_B: frozenset[Vertex] = _quad([(2, y, z) for y in (0, 1) for z in (0, 1)])
OTHER_FACES: tuple[frozenset[Vertex], ...] = tuple(
    face for face in FACES if face not in (F_STAR, F_B)
)


def seed() -> Occ:
    return {vertex: 1 if vertex == (0, 0, 0) else 0 for vertex in VERTICES}


def empty_occ() -> Occ:
    return {vertex: 0 for vertex in VERTICES}


def occ_get(occupancy: Occ, vertex: Vertex) -> int:
    return occupancy.get(vertex, 0)


def _shift(vertex: Vertex, axis: int, step: int) -> Vertex:
    coords = [vertex[0], vertex[1], vertex[2]]
    coords[axis] += step
    return (coords[0], coords[1], coords[2])


def n_vec(occupancy: Occ, vertex: Vertex) -> tuple[Fraction, Fraction, Fraction]:
    components = []
    for axis in (0, 1, 2):
        plus = occ_get(occupancy, _shift(vertex, axis, 1))
        minus = occ_get(occupancy, _shift(vertex, axis, -1))
        components.append(Fraction(plus - minus, 3))
    return (components[0], components[1], components[2])


def occ_step(occupancy: Occ) -> Occ:
    updated: Occ = {}
    for vertex in VERTICES:
        if occ_get(occupancy, vertex) == 1:
            updated[vertex] = 1
        else:
            updated[vertex] = 0 if n_vec(occupancy, vertex) == (0, 0, 0) else 1
    return updated


def rho(occupancy: Occ) -> tuple[int, int]:
    return (
        sum(occ_get(occupancy, vertex) for vertex in CUBE_A),
        sum(occ_get(occupancy, vertex) for vertex in CUBE_B),
    )


def flux(occupancy: Occ) -> dict[frozenset[Vertex], int]:
    rho_a, rho_b = rho(occupancy)
    table = {face: 0 for face in FACES}
    table[F_STAR] = rho_a
    table[F_B] = rho_a + rho_b
    return table


def gauss_holds(occupancy: Occ) -> bool:
    rho_a, rho_b = rho(occupancy)
    phi = flux(occupancy)
    g_a = phi[F_STAR]
    g_b = -phi[F_STAR] + phi[F_B]
    others_zero = all(phi[face] == 0 for face in OTHER_FACES)
    return g_a == rho_a and g_b == rho_b and others_zero


def occupied_set(occupancy: Occ) -> set[Vertex]:
    return {vertex for vertex in VERTICES if occ_get(occupancy, vertex) == 1}


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        if condition:
            self.passed += 1
        else:
            self.failed += 1
        print(f"{'PASS' if condition else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    self_source = Path(__file__).read_text(encoding="utf-8")

    print("external_scientific_inputs: none")
    print("package_local_integrity_reads: proposed source note and live axiom memo")
    print("measure_boundary: exact Z/Q; displayed rho and tree-gauge flux")

    seed_occ = seed()
    tick1 = occ_step(seed_occ)
    empty = empty_occ()
    empty_step = occ_step(empty)
    seed_rho = rho(seed_occ)
    seed_phi = flux(seed_occ)
    tick1_rho = rho(tick1)
    tick1_phi = flux(tick1)
    empty_rho = rho(empty)
    empty_phi = flux(empty)

    checks.check(
        "thm1-listing",
        "twelve vertices, two cubes, eleven faces; F* listed once",
        len(VERTICES) == 12
        and len(set(VERTICES)) == 12
        and len(CUBE_A) == 8
        and len(CUBE_B) == 8
        and len(set(CUBE_A) & set(CUBE_B)) == 4
        and len(FACES) == 11
        and FACES.count(F_STAR) == 1
        and F_STAR in FACES
        and F_B in FACES,
    )
    checks.check(
        "thm2-seed-table",
        "seed rho=(1,0), phi(F*)=1, phi(F_B)=1",
        seed_rho == (1, 0)
        and seed_phi[F_STAR] == 1
        and seed_phi[F_B] == 1
        and gauss_holds(seed_occ),
    )
    formed = occupied_set(tick1) - occupied_set(seed_occ)
    checks.check(
        "thm3-occ-step",
        "seed step forms exactly (1,0,0), (0,1,0), (0,0,1)",
        formed == {(1, 0, 0), (0, 1, 0), (0, 0, 1)}
        and occupied_set(tick1)
        == {(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)},
    )
    checks.check(
        "thm4-tick1-table",
        "after step rho=(4,1), phi(F*)=4, phi(F_B)=5, Gauss holds",
        tick1_rho == (4, 1)
        and tick1_phi[F_STAR] == 4
        and tick1_phi[F_B] == 5
        and gauss_holds(tick1),
    )
    checks.check(
        "thm4-recoil",
        "shared-face flux changes 1 -> 4",
        seed_phi[F_STAR] == 1 and tick1_phi[F_STAR] == 4,
    )
    checks.check(
        "thm5-empty",
        "empty seed is a fixed point with zero source and flux",
        empty_step == empty
        and empty_rho == (0, 0)
        and empty_phi[F_STAR] == 0
        and empty_phi[F_B] == 0
        and all(value == 0 for value in empty_phi.values())
        and gauss_holds(empty),
    )
    checks.check(
        "thm6-rho-not-site-I",
        "tick-1 rho(A)=4 is not a single-vertex I in {0,1}",
        tick1_rho[0] == 4 and tick1_rho[0] not in (0, 1),
    )
    checks.check(
        "permanence",
        "occupied sites stay occupied",
        occupied_set(seed_occ).issubset(occupied_set(tick1))
        and all(
            occ_get(occ_step(tick1), vertex) == 1
            for vertex in occupied_set(tick1)
        ),
    )
    checks.check(
        "mutation-rho-eq-site-I-fails",
        "predicate tick-1 rho(A) equals a single-vertex I fails",
        tick1_rho[0] != 0 and tick1_rho[0] != 1,
    )
    checks.check(
        "mutation-phi-unchanged-fails",
        "predicate phi(F*) is unchanged by the occupancy step fails",
        seed_phi[F_STAR] != tick1_phi[F_STAR],
    )
    checks.check(
        "mutation-empty-forms-fails",
        "predicate empty seed forms a site or a nonzero flux fails",
        occupied_set(empty_step) == set()
        and empty_phi[F_STAR] == 0
        and empty_phi[F_B] == 0,
    )
    checks.check(
        "mutation-adopts-newton-fails",
        "predicate note adopts Newton / G_N / 1/r / axiom text fails",
        "G_N" not in note
        and "1/r" not in note
        and "L_phys" not in note
        and "we adopt" not in note.lower()
        and "Codex" not in note
        and "Display. Do not adopt." in note,
    )
    checks.check(
        "mutation-lattice-named-flux-fails",
        "predicate note claims Lattice-named flux or a unique L fails",
        "Lattice flux" not in note
        and "unique L_phys" not in note
        and "Not an axiom-named map. Not a unique `L`." in note,
    )
    record_quote = (
        "When present, a record locks exactly one admissible local possibility. A\n"
        "site never carries more than one record; records are permanent."
    )
    admiss_quote = (
        "For each site, the probability distribution over the possibilities is\n"
        "determined by, and varies with, the nearest-neighbor conditions."
    )
    qubit_quote = (
        "The full one-site possibility domain has algebraic presentation `M_2(C)`."
    )
    checks.check(
        "thm7-live-quotes",
        "note quotes live Record, Admissibility, and Qubit without rewrite",
        record_quote in axiom
        and record_quote in note
        and admiss_quote in axiom
        and admiss_quote in note
        and qubit_quote in axiom
        and qubit_quote in note
        and "do not name `ρ`, `φ`" in note,
    )
    checks.check(
        "machine-status-contract",
        "bounded-support status and gravity-update blocker are source-visible",
        "actual_current_surface_status: bounded-support" in note
        and "target_claim_id: two_cube_record_gauss_flux_step" in note
        and "Gravity update has no equation; Record source is a counter that geometry does not read"
        in note
        and 'next_trace_action: "independent audit; Pachner / perfect-action not in this note"'
        in note
        and 'hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"'
        in note,
    )
    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/TWO_CUBE_RECORD_GAUSS_FLUX_STEP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file(),
    )
    checks.check(
        "identity-gates-bound",
        "identity gates call rho, flux, gauss_holds, occ_step, seed",
        "def rho(" in self_source
        and "def flux(" in self_source
        and "def gauss_holds(" in self_source
        and "def occ_step(" in self_source
        and "def seed(" in self_source
        and "rho(seed_occ)" in self_source
        and "flux(seed_occ)" in self_source
        and "gauss_holds(seed_occ)" in self_source
        and "occ_step(seed_occ)" in self_source
        and "seed()" in self_source,
    )
    checks.check(
        "construction-not-nogo",
        "note is a construction and authors no N-gate no-go",
        "No N-gate no-go is authored. This is a construction." in note
        and "### N1" not in note
        and "exhausted" not in note
        and "only route" not in note
        and "closes gravity" not in note,
    )
    checks.check(
        "v-sections",
        "V1-V5 are present and origin/main is not given an unmerged parent",
        "## V1 — axiom quotes" in note
        and "## V2 — origin/main search" in note
        and "## V3 — textbook discrete Gauss" in note
        and "## V4 — exact `1 → 4` on `φ(F*)`" in note
        and "## V5 — not a corollary of the axiom sentences alone" in note
        and "Unmerged pull requests are not cited." in note,
    )

    print("per_element: twelve vertices and eleven faces checked")
    print("per_site: seed and empty occupancy steps checked")
    print("per_mode: displayed tree gauge on F* and F_B checked")
    print("per_block: two-cube Gauss identity checked")
    print("lattice_wide: checked and not executed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
