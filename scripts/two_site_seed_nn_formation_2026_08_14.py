#!/usr/bin/env python3
"""Exact two-point unread-site n evaluation for two-site seeds.

Mutual formation-readiness is computed from occupancy. The 6-NN
classification is a derived identity, not an embedded lookup table.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "TWO_SITE_SEED_NN_FORMATION_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/TWO_SITE_SEED_NN_FORMATION_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Site = tuple[int, int, int]
Triple = tuple[Fraction, Fraction, Fraction]

ORIGIN: Site = (0, 0, 0)
AXES: tuple[Site, ...] = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
ZERO_N: Triple = (Fraction(0), Fraction(0), Fraction(0))


def add(left: Site, right: Site) -> Site:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def sub(left: Site, right: Site) -> Site:
    return (left[0] - right[0], left[1] - right[1], left[2] - right[2])


def neg(site: Site) -> Site:
    return (-site[0], -site[1], -site[2])


def apply_matrix(matrix: tuple[Site, ...], site: Site) -> Site:
    return tuple(sum(matrix[row][col] * site[col] for col in range(3)) for row in range(3))  # type: ignore[return-value]


def det3(matrix: tuple[Site, ...]) -> int:
    a, b, c = matrix
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def occupancy_bit(support: frozenset[Site], site: Site) -> int:
    return 1 if site in support else 0


def unread_n(support: frozenset[Site], site: Site) -> Triple:
    """n_μ = (o_{+μ} − o_{-μ}) / 3 at an unread site."""
    return tuple(
        Fraction(
            occupancy_bit(support, add(site, axis))
            - occupancy_bit(support, add(site, neg(axis))),
            3,
        )
        for axis in AXES
    )  # type: ignore[return-value]


def is_nonzero(triple: Triple) -> bool:
    return any(component != 0 for component in triple)


def mutually_ready(first: Site, second: Site) -> bool:
    n_first = unread_n(frozenset({second}), first)
    n_second = unread_n(frozenset({first}), second)
    return is_nonzero(n_first) and is_nonzero(n_second)


def six_nn_of(site: Site) -> frozenset[Site]:
    neighbors = set()
    for axis in AXES:
        neighbors.add(add(site, axis))
        neighbors.add(add(site, neg(axis)))
    return frozenset(neighbors)


def closed_n_at_origin(seed: Site) -> Triple:
    return tuple(
        Fraction(int(seed == axis) - int(seed == neg(axis)), 3) for axis in AXES
    )  # type: ignore[return-value]


def closed_n_at_seed(seed: Site) -> Triple:
    return tuple(
        Fraction(int(seed == neg(axis)) - int(seed == axis), 3) for axis in AXES
    )  # type: ignore[return-value]


def proper_rotations() -> tuple[tuple[Site, ...], ...]:
    rotations: list[tuple[Site, ...]] = []
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = tuple(
                tuple((signs[row] if col == perm[row] else 0) for col in range(3))
                for row in range(3)
            )
            if det3(matrix) == 1:  # type: ignore[arg-type]
                rotations.append(matrix)  # type: ignore[arg-type]
    return tuple(rotations)


def orbit_of(seed: Site) -> frozenset[Site]:
    return frozenset(apply_matrix(matrix, seed) for matrix in proper_rotations())


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

    print("external_scientific_inputs: none; exact unread-site occupancy arithmetic only")
    print("package_local_integrity_reads: proposed source note and live axiom memo only")
    print("measure_boundary: exact Fraction coefficients; no floating-point inputs")
    print("claim_boundary: bounded two-point n evaluation; no lock rule or rate is asserted")

    nn_origin = six_nn_of(ORIGIN)
    rotations = proper_rotations()
    checks.check(
        "rotation-group-order",
        "there are 24 proper cubic rotations",
        len(rotations) == 24 and len(set(rotations)) == 24,
    )
    checks.check(
        "six-nn-count",
        "the origin has exactly six axis neighbors",
        nn_origin
        == frozenset(
            (
                (1, 0, 0),
                (-1, 0, 0),
                (0, 1, 0),
                (0, -1, 0),
                (0, 0, 1),
                (0, 0, -1),
            )
        ),
    )

    box = [
        (x, y, z)
        for x in range(-3, 4)
        for y in range(-3, 4)
        for z in range(-3, 4)
        if (x, y, z) != ORIGIN
    ]

    identity_at_origin = all(
        unread_n(frozenset({seed}), ORIGIN) == closed_n_at_origin(seed) for seed in box
    )
    identity_at_seed = all(
        unread_n(frozenset({ORIGIN}), seed) == closed_n_at_seed(seed) for seed in box
    )
    checks.check(
        "thm1-closed-form",
        "n(0;{v}) equals the indicator difference on ±e_μ",
        identity_at_origin,
    )
    checks.check(
        "thm2-closed-form",
        "n(v;{0}) equals the opposite indicator difference",
        identity_at_seed,
    )

    ready_box = [seed for seed in box if mutually_ready(ORIGIN, seed)]
    checks.check(
        "thm3-box-classification",
        "on the radius-3 box, mutual readiness holds exactly on the 6-NN",
        set(ready_box) == set(nn_origin),
    )
    checks.check(
        "thm3-both-sides-equivalent",
        "n(0) nonzero and n(v) nonzero are the same 6-NN predicate",
        all(
            (
                is_nonzero(unread_n(frozenset({seed}), ORIGIN))
                == is_nonzero(unread_n(frozenset({ORIGIN}), seed))
                == (seed in nn_origin)
            )
            for seed in box
        ),
    )

    e_x = (1, 0, 0)
    n0_ex = unread_n(frozenset({e_x}), ORIGIN)
    nv_ex = unread_n(frozenset({ORIGIN}), e_x)
    checks.check(
        "rep-6nn-n0",
        "n(0) from {e_x} is (1/3,0,0)",
        n0_ex == (Fraction(1, 3), Fraction(0), Fraction(0)),
    )
    checks.check(
        "rep-6nn-nv",
        "n(e_x) from {0} is (-1/3,0,0)",
        nv_ex == (Fraction(-1, 3), Fraction(0), Fraction(0)),
    )
    checks.check(
        "rep-6nn-ready",
        "the 6-NN representative is mutually formation-ready",
        mutually_ready(ORIGIN, e_x),
    )

    representatives: tuple[tuple[Site, str, Triple, bool], ...] = (
        ((1, 0, 0), "6-NN", (Fraction(1, 3), Fraction(0), Fraction(0)), True),
        ((2, 0, 0), "axis-2", ZERO_N, False),
        ((1, 1, 0), "face diagonal", ZERO_N, False),
        ((1, 1, 1), "space diagonal", ZERO_N, False),
        ((2, 1, 0), "knight", ZERO_N, False),
    )
    representative_table = all(
        unread_n(frozenset({seed}), ORIGIN) == expected
        and mutually_ready(ORIGIN, seed) is ready
        for seed, _name, expected, ready in representatives
    )
    checks.check(
        "thm4-representative-table",
        "the five orbit representatives match the stated n(0) and readiness",
        representative_table,
    )

    orbit_sizes = {
        (1, 0, 0): 6,
        (2, 0, 0): 6,
        (1, 1, 0): 12,
        (1, 1, 1): 8,
        (2, 1, 0): 24,
    }
    orbit_ready_constant = True
    orbit_size_ok = True
    for seed, _name, _expected, ready in representatives:
        orbit = orbit_of(seed)
        orbit_size_ok = orbit_size_ok and len(orbit) == orbit_sizes[seed]
        orbit_ready_constant = orbit_ready_constant and all(
            mutually_ready(ORIGIN, image) is ready for image in orbit
        )
    checks.check(
        "thm4-orbit-sizes",
        "proper-rotation orbit sizes are 6, 6, 12, 8, 24",
        orbit_size_ok,
    )
    checks.check(
        "thm4-orbit-readiness",
        "readiness is constant on each proper-rotation orbit",
        orbit_ready_constant,
    )
    checks.check(
        "thm4-only-nn-orbit-ready",
        "among the five orbits, only the 6-NN orbit is ready",
        all(mutually_ready(ORIGIN, seed) for seed in orbit_of(e_x))
        and not any(
            mutually_ready(ORIGIN, seed)
            for representative in ((2, 0, 0), (1, 1, 0), (1, 1, 1), (2, 1, 0))
            for seed in orbit_of(representative)
        ),
    )

    translated = all(
        mutually_ready(shift, add(shift, seed)) == mutually_ready(ORIGIN, seed)
        for shift in ((0, 0, 0), (1, 0, 0), (0, 2, -1), (4, -3, 5))
        for seed, _name, _expected, _ready in representatives
    )
    checks.check(
        "thm3-translation-coordinate",
        "mutual readiness of {a,a+v} equals that of {0,v}",
        translated,
    )

    checks.check(
        "mutation-axis-2-not-ready",
        "predicate v=(2,0,0) is ready fails",
        not mutually_ready(ORIGIN, (2, 0, 0)),
    )
    checks.check(
        "mutation-face-diagonal-not-ready",
        "predicate v=(1,1,0) is ready fails",
        not mutually_ready(ORIGIN, (1, 1, 0)),
    )
    checks.check(
        "mutation-n0-ex-zero-fails",
        "predicate n(0;{e_x})=(0,0,0) fails",
        n0_ex != ZERO_N,
    )
    checks.check(
        "mutation-face-diagonal-is-nn-fails",
        "predicate (1,1,0) is a 6-NN of the origin fails",
        (1, 1, 0) not in nn_origin,
    )

    lattice_quote = (
        "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
    )
    privilege_quote = "No site is privileged. Sites are distinguished by the supplied lattice"
    admissibility_quote = (
        "There is one fixed nearest-neighbor admissibility rule, covariant under lattice"
    )
    distribution_quote = (
        "For each site, the probability distribution over the possibilities is"
    )
    unread_quote = "A site with no record cannot be read."
    checks.check(
        "live-parent-quotes",
        "Lattice, Admissibility, and Record sentences are quoted without rewrite",
        lattice_quote in axiom
        and lattice_quote in note
        and privilege_quote in axiom
        and privilege_quote in note
        and admissibility_quote in axiom
        and admissibility_quote in note
        and distribution_quote in axiom
        and distribution_quote in note
        and "Records form." in axiom
        and "Records form." in note
        and unread_quote in axiom
        and unread_quote in note,
    )
    checks.check(
        "seed-is-initial-condition",
        "the seed is initial-condition content and not a privileged site",
        "The seed is initial-condition content." in note
        and "not a privileged Lattice site" in note
        and "No site is privileged." in note,
    )
    checks.check(
        "scope-boundary",
        "the theorem disclaims a lock rule, axiom edit, and twelve-seed clone",
        "no additional\naxiom is proposed" in note
        and "not a multi-step occupancy evolution" in note
        and "not a twelve-seed occupancy clone" in note
        and "These are scope boundaries, not impossibility" in note
        and "The Qubit sentence is not rewritten." in note,
    )
    checks.check(
        "machine-status-contract",
        "bounded status, frontier trace, and next action are source-visible",
        "actual_current_surface_status: bounded-support" in note
        and "trace_class: frontier_discovery" in note
        and 'next_trace_action: "independent audit of the bounded algebraic claim"'
        in note,
    )
    checks.check(
        "import-boundary-contract",
        "the supplied combination and absent physical bridge are disclosed",
        "## Inputs And Import Boundary" in note
        and "Explicit theorem-domain condition" in note
        and "External empirical or literature inputs:** none" in note
        and "Open physical bridge" in note,
    )
    forbidden = (
        "G" + "_N",
        "1/" + "r",
        "1/" + "r^2",
        "Lattice" + "-named",
        "not a " + "TOE",
        "L_" + "phys",
        "we " + "adopt",
        "Cod" + "ex",
    )
    checks.check(
        "forbidden-hygiene",
        "note omits the barred substrings",
        all(token not in note for token in forbidden),
    )
    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/TWO_SITE_SEED_NN_FORMATION_BOUNDED_THEOREM_NOTE_2026-08-14.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file(),
    )
    checks.check(
        "claim-type-and-proof-contract",
        "the bounded type and two-point evaluation are source-visible",
        "**Type:** bounded_theorem" in note
        and "two-point `n` evaluation" in note
        and "### N8" not in note
        and "FAIL / DO NOT SHIP" not in note
        and ("import " + "qcd") not in self_source.lower()
        and ("from " + "qcd") not in self_source.lower()
        and "unread_n(" in self_source
        and "mutually_ready(" in self_source,
    )

    print(
        "per_element: n is evaluated from singleton occupancy at each unread seed site."
    )
    print(
        "per_site: mutual readiness is a two-site predicate; origin placement is a coordinate choice."
    )
    print(
        "per_mode: both unread triples are resolved; readiness is their joint nonvanishing."
    )
    print(
        "per_block: five translation-fixed orbits are classified; only the 6-NN orbit is ready."
    )
    print(
        "lattice_wide: checked on a radius-3 box and by closed form; no multi-step evolution is run."
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
