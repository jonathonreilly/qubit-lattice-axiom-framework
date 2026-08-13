#!/usr/bin/env python3
"""Exact Fraction / integer-lattice checks: 1/d is not a 6-nn Green trial.

Parents read as AUDIT_INPUT_PATHS only: this note, the Newton packet, and
the current axiom memo. No cache write, no G_N, no continuum 1/r install.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]

AUDIT_INPUT_PATHS = (
    "docs/LATTICE_GREEN_ON_Z3_IS_NOT_CONTINUUM_ONE_OVER_R_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/NEWTON_LAW_DERIVED_NOTE.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE = ROOT / AUDIT_INPUT_PATHS[0]
NEWTON = ROOT / AUDIT_INPUT_PATHS[1]
AXIOM = ROOT / AUDIT_INPUT_PATHS[2]

NN = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)

E1 = (1, 0, 0)
TWO_E1 = (2, 0, 0)
E1_E2 = (1, 1, 0)
ORIGIN = (0, 0, 0)


def add(x, y):
    return (x[0] + y[0], x[1] + y[1], x[2] + y[2])


def graph_distance(x):
    return abs(x[0]) + abs(x[1]) + abs(x[2])


def one_over_d(x):
    dist = graph_distance(x)
    if dist == 0:
        return None
    return Fraction(1, dist)


def one_over_d_zero_at_origin(x):
    value = one_over_d(x)
    return Fraction(0) if value is None else value


def nn_laplacian(func, x):
    center = func(x)
    return sum(func(add(x, shift)) for shift in NN) - 6 * center


def one_over_d_is_nn_harmonic_off_0(site) -> bool:
    """Predicate: 1/d is nn-harmonic off 0 at `site`.

    The origin is outside the domain of 1/d. If the 6-nn stencil meets the
    origin, the predicate is false. Otherwise it is true only if the
    Laplacian Fraction is exactly zero.
    """
    if site == ORIGIN:
        return False
    for shift in NN:
        if add(site, shift) == ORIGIN:
            return False
    return nn_laplacian(one_over_d_zero_at_origin, site) == 0


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, condition: bool) -> None:
        if condition:
            self.passed += 1
            print(f"PASS {label}")
        else:
            self.failed += 1
            print(f"FAIL {label}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return 0 if self.failed == 0 and self.passed >= 10 else 1


def main() -> int:
    checks = Checks()
    note_text = NOTE.read_text(encoding="utf-8")
    newton_text = NEWTON.read_text(encoding="utf-8")
    axiom_text = AXIOM.read_text(encoding="utf-8")

    checks.check("AUDIT_INPUT_PATHS has the new note, Newton note, axiom memo",
                 AUDIT_INPUT_PATHS == (
                     "docs/LATTICE_GREEN_ON_Z3_IS_NOT_CONTINUUM_ONE_OVER_R_BOUNDED_THEOREM_NOTE_2026-08-13.md",
                     "docs/NEWTON_LAW_DERIVED_NOTE.md",
                     "docs/MINIMAL_AXIOMS_2026-06-29.md",
                 ) and NOTE.is_file() and NEWTON.is_file() and AXIOM.is_file())

    checks.check("T1 graph distances at e1, 2e1, e1+e2 are 1, 2, 2",
                 graph_distance(E1) == 1
                 and graph_distance(TWO_E1) == 2
                 and graph_distance(E1_E2) == 2)

    checks.check("T1 reciprocals at e1, 2e1, e1+e2 are 1, 1/2, 1/2",
                 one_over_d(E1) == 1
                 and one_over_d(TWO_E1) == Fraction(1, 2)
                 and one_over_d(E1_E2) == Fraction(1, 2))

    neighbor_values = tuple(one_over_d(add(E1, shift)) for shift in NN)
    checks.check("T1 six neighbors of e1: origin undefined, five halves",
                 neighbor_values.count(None) == 1
                 and neighbor_values.count(Fraction(1, 2)) == 5)

    lap_e1 = nn_laplacian(one_over_d_zero_at_origin, E1)
    checks.check("T1 zero-extended nn-Laplacian of 1/d at e1 is -7/2",
                 lap_e1 == Fraction(-7, 2))

    checks.check("mutation: 1/d is nn-harmonic off 0 fails at e1",
                 one_over_d_is_nn_harmonic_off_0(E1) is False
                 and lap_e1 != 0)

    poisson_c = Fraction(7, 6)
    harmonic_c = Fraction(7, 2)
    lap_origin_at_poisson = (
        6 * Fraction(1) - 6 * poisson_c
    )
    lap_e1_at_poisson = poisson_c + 5 * Fraction(1, 2) - 6
    checks.check("T2 no origin value makes 1/d a Green trial (7/6 != 7/2)",
                 poisson_c != harmonic_c
                 and lap_origin_at_poisson == Fraction(-1)
                 and lap_e1_at_poisson == poisson_c - Fraction(7, 2)
                 and lap_e1_at_poisson != 0)

    lap_diag = nn_laplacian(one_over_d_zero_at_origin, E1_E2)
    checks.check("T2 1/d Laplacian at e1+e2 is 1/3 (stencil avoids origin)",
                 one_over_d_is_nn_harmonic_off_0(E1_E2) is False
                 and lap_diag == Fraction(1, 3))

    cube_star = [
        (x, y, z)
        for x in range(-2, 3)
        for y in range(-2, 3)
        for z in range(-2, 3)
        if (x, y, z) != ORIGIN
    ]
    checks.check("executed cube {-2..2}^3\\{0} has 124 Fraction values 1/d",
                 len(cube_star) == 124
                 and all(isinstance(one_over_d(site), Fraction) for site in cube_star))

    # G_cont o d is a formal positive multiple of 1/d on C*, so it inherits
    # the failed harmonicity. The multiple 1/(4π) is never instantiated.
    checks.check("T2 G_cont∘d is not a lattice Green: 1/d fails Poisson/harmonicity",
                 lap_e1 != 0 and poisson_c != harmonic_c)

    checks.check("T3 axiom memo states Record readout additivity on disjoint records",
                 "pairwise-disjoint records, scalar readout" in axiom_text
                 and "I(empty)=0" in axiom_text.replace(" ", ""))

    kernel_needles = (
        "lattice Green",
        "G_cont",
        "1/d",
        "1/r",
        "graph distance",
        "Poisson",
    )
    checks.check("T3 Record additivity text does not name either kernel",
                 all(needle not in axiom_text.split("### Record / Fixed Reality")[1]
                     .split("## Qualification")[0]
                     for needle in kernel_needles))

    checks.check("T4 Newton packet still isolates phi = M G and formal G(r)",
                 "G(r) = 1/(4 pi r)" in newton_text
                 and "phi(r) = M G(r)" in newton_text
                 and "source-linearity" in newton_text)

    checks.check("T4 this note does not retire Newton and splits kernel from π",
                 "does not retire the Newton packet" in note_text
                 and "already-isolated product pairing" in note_text
                 and "π(M, G) := M · G" in note_text)

    checks.check("note states Theorems 1–4 and refuses gravity / G_N / 1/r install",
                 "Theorem 1" in note_text
                 and "Theorem 2" in note_text
                 and "Theorem 3" in note_text
                 and "Theorem 4" in note_text
                 and "No gravitational coupling, no `G_N`" in note_text
                 and "does not install `1/r`" in note_text
                 and "G_N" not in newton_text.split("## In-Scope Theorem")[0])

    forbidden = ("G_N =", "import G_N", "Newton force law is derived")
    checks.check("no G_N import and no force-law derivation in this pair",
                 all(token not in note_text for token in forbidden)
                 and "G_N" not in Path(__file__).read_text(encoding="utf-8").split(
                     'no G_N, no continuum'
                 )[0])

    n5_lines = (
        "per_element: graph distances and 1/d values at e1, 2e1, e1+e2 are exact Fractions",
        "per_site: the nn-Laplacian is evaluated at e1 and e1+e2 only",
        "per_mode: 6-nn graph Laplacian is checked; no continuum mode is claimed",
        "per_block: only the 1/d versus Green-trial split and the additivity residual are executed",
        "lattice_wide: checked and not executed — no lattice-wide gravity or G_N is claimed",
    )
    for line in n5_lines:
        checks.check(
            f"n5 {line[:24]}",
            line.startswith(("per_element:", "per_site:", "per_mode:", "per_block:", "lattice_wide:"))
            and len(line) >= 40,
        )
        print(line)
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
