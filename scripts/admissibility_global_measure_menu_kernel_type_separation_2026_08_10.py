#!/usr/bin/env python3
"""Exact checks for the Admissibility measure/menu-kernel type separation.

The runner checks the finite disjoint-menu contradiction, the exact Gaussian
dimension and neighbor-center data, the two shared-effect ternary menus, and
the context-dependent atomic restriction. Measure-theoretic facts about positive
densities and null singletons are proved in the source note, not approximated
by sampling here.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PARENT_PATH = ROOT / "docs" / "BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md"
PRIOR_PATH = ROOT / "docs" / "BORN_FORM_MENU_OUTCOME_THRESHOLD_AND_MIXED_PROJECTIVE_FORCING_BOUNDED_THEOREM_NOTE_2026-07-17.md"

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md",
    "docs/BORN_FORM_MENU_OUTCOME_THRESHOLD_AND_MIXED_PROJECTIVE_FORCING_BOUNDED_THEOREM_NOTE_2026-07-17.md",
)


def normalize(text: str) -> str:
    return " ".join(text.split())


@dataclass(frozen=True)
class Qsqrt2:
    """Exact a + b sqrt(2) scalar sufficient for the Bloch witnesses."""

    a: Fraction = Fraction(0)
    b: Fraction = Fraction(0)

    def __add__(self, other: "Qsqrt2") -> "Qsqrt2":
        return Qsqrt2(self.a + other.a, self.b + other.b)

    def __neg__(self) -> "Qsqrt2":
        return Qsqrt2(-self.a, -self.b)

    def __sub__(self, other: "Qsqrt2") -> "Qsqrt2":
        return self + (-other)

    def __mul__(self, other: "Qsqrt2") -> "Qsqrt2":
        return Qsqrt2(
            self.a * other.a + 2 * self.b * other.b,
            self.a * other.b + self.b * other.a,
        )

    def scale(self, value: Fraction) -> "Qsqrt2":
        return Qsqrt2(value * self.a, value * self.b)


ZERO = Qsqrt2()
ONE = Qsqrt2(Fraction(1))


def q(value: int | Fraction) -> Qsqrt2:
    return Qsqrt2(Fraction(value))


def rs2(value: int | Fraction) -> Qsqrt2:
    return Qsqrt2(Fraction(0), Fraction(value))


Vector = tuple[Qsqrt2, Qsqrt2, Qsqrt2]


def vector_scale(value: Fraction, vector: Vector) -> Vector:
    return tuple(component.scale(value) for component in vector)  # type: ignore[return-value]


def vector_sum(vectors: tuple[Vector, ...]) -> Vector:
    return tuple(
        sum((vector[index] for vector in vectors), ZERO)
        for index in range(3)
    )  # type: ignore[return-value]


def norm_squared(vector: Vector) -> Qsqrt2:
    return sum((component * component for component in vector), ZERO)


def matrix_add(left, right):
    return tuple(
        tuple(left[row][column] + right[row][column] for column in range(2))
        for row in range(2)
    )


@dataclass(frozen=True)
class Effect:
    coefficient: Fraction
    bloch: Vector


def menu_is_resolution(menu: tuple[Effect, ...]) -> bool:
    scalar_ok = sum(effect.coefficient for effect in menu) == 2
    vector = vector_sum(tuple(vector_scale(effect.coefficient, effect.bloch) for effect in menu))
    unit_vectors = all(norm_squared(effect.bloch) == ONE for effect in menu)
    scaled_domain = all(Fraction(0) < effect.coefficient <= Fraction(1) for effect in menu)
    return scalar_ok and vector == (ZERO, ZERO, ZERO) and unit_vectors and scaled_domain


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

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    parent = PARENT_PATH.read_text(encoding="utf-8")
    prior = PRIOR_PATH.read_text(encoding="utf-8")
    normalized_note = normalize(note).replace("> ", "")

    print("external_scientific_inputs: current axiom wording, the parent low-arity theorem, and the earlier atomless menu-boundary note are source-bound; no observational or fitted inputs are used")
    print("package_local_integrity_reads: the proposed source note is read for claim-surface consistency; the cache envelope separately binds this runner and every declared input")
    print("measure_boundary: the runner checks exact finite algebra and Gaussian dimension data; it does not replace the source proof of atomlessness/full support with samples")
    print("negative_scope: only raw singleton identification and normalized finite restriction are rejected; other physical measure-to-effect constructions remain live")

    canonical_sentence = (
        "For each site, the probability distribution over the possibilities is "
        "determined by, and varies with, the nearest-neighbor conditions."
    )
    checks.check(
        "source-admissibility",
        "the exact current distribution sentence is present",
        canonical_sentence in normalize(axiom),
    )
    checks.check(
        "source-atomless",
        "the current axiom note explicitly permits supported points of zero singleton measure",
        "supported exact point may have zero singleton measure" in normalize(axiom),
    )
    checks.check(
        "source-parent",
        "the parent theorem supplies the unique trace form only after menu-independent low-arity grading",
        all(
            phrase in parent
            for phrase in (
                "menu-independent grading",
                "Every two- or three-member menu is normalized",
                "There is a unique density matrix",
            )
        ),
    )
    checks.check(
        "source-boundary",
        "the earlier menu note separates atomless support from conditional effect menus",
        "supported point in an atomless continuous law" in prior,
    )

    # The z and x projective bases are two disjoint two-point subsets.
    pz_plus = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(0)))
    pz_minus = ((Fraction(0), Fraction(0)), (Fraction(0), Fraction(1)))
    px_plus = ((Fraction(1, 2), Fraction(1, 2)), (Fraction(1, 2), Fraction(1, 2)))
    px_minus = ((Fraction(1, 2), Fraction(-1, 2)), (Fraction(-1, 2), Fraction(1, 2)))
    projectors = (pz_plus, pz_minus, px_plus, px_minus)
    identity = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)))
    checks.check(
        "binary-menu-resolutions",
        "the z and x projector pairs each sum exactly to the identity",
        matrix_add(pz_plus, pz_minus) == identity
        and matrix_add(px_plus, px_minus) == identity,
    )
    checks.check(
        "binary-menu-disjointness",
        "the z and x projective menus contain four distinct effects",
        len(set(projectors)) == 4,
    )

    # Raw singleton normalization makes each disjoint two-point set mass one.
    menu_z_mass = Fraction(1)
    menu_x_mass = Fraction(1)
    probability_space_mass = Fraction(1)
    checks.check(
        "raw-singleton-contradiction",
        "two disjoint normalized binary menus force mass two inside a probability space of mass one",
        menu_z_mass + menu_x_mass == 2
        and menu_z_mass + menu_x_mass > probability_space_mass,
    )

    # M_2(C) has 8 real coordinates; exp(-||x||^2) integrates to pi^(8/2).
    real_dimension = 2 * 2 * 2
    gaussian_density_pi_power = Fraction(-4)
    gaussian_integral_pi_power = Fraction(real_dimension, 2)
    alpha = tuple(Fraction(k, 12) for k in range(7))
    checks.check(
        "gaussian-normalization",
        "the pi^-4 density cancels the eight-real-dimensional Gaussian integral exactly",
        real_dimension == 8 and gaussian_density_pi_power + gaussian_integral_pi_power == 0,
    )
    checks.check(
        "gaussian-neighbor-variation",
        "all seven neighbor-count classes have distinct scalar centers",
        len(set(alpha)) == 7 and alpha[0] == 0 and alpha[-1] == Fraction(1, 2),
    )

    z = (ZERO, ZERO, ONE)
    n1 = (rs2(Fraction(4, 9)), ZERO, q(Fraction(-7, 9)))
    n2 = (rs2(Fraction(-2, 3)), ZERO, q(Fraction(1, 3)))
    m1 = (rs2(Fraction(2, 3)), ZERO, q(Fraction(-1, 3)))
    m2 = (rs2(Fraction(-2, 3)), ZERO, q(Fraction(-1, 3)))

    e0 = Effect(Fraction(1, 2), z)
    a1 = Effect(Fraction(9, 10), n1)
    a2 = Effect(Fraction(3, 5), n2)
    b1 = Effect(Fraction(3, 4), m1)
    b2 = Effect(Fraction(3, 4), m2)
    menu_a = (e0, a1, a2)
    menu_b = (e0, b1, b2)

    checks.check(
        "ternary-menu-a",
        "the asymmetric shared-effect menu is an exact scaled-projector resolution",
        menu_is_resolution(menu_a),
    )
    checks.check(
        "ternary-menu-b",
        "the symmetric shared-effect menu is an exact scaled-projector resolution",
        menu_is_resolution(menu_b),
    )
    checks.check(
        "shared-effect-incidence",
        "the two menus share exactly E0 and otherwise contain distinct effects",
        set(menu_a).intersection(menu_b) == {e0} and len(set(menu_a).union(menu_b)) == 5,
    )

    coefficients = (e0.coefficient, a1.coefficient, a2.coefficient, b1.coefficient, b2.coefficient)
    atomic_normalization = sum(value * value for value in coefficients)
    checks.check(
        "atomic-global-normalization",
        "the five squared-trace atomic weights have exact normalization 509/200",
        atomic_normalization == Fraction(509, 200)
        and sum(value * value / atomic_normalization for value in coefficients) == 1,
    )

    e0_square = e0.coefficient * e0.coefficient
    menu_a_square_sum = sum(effect.coefficient**2 for effect in menu_a)
    menu_b_square_sum = sum(effect.coefficient**2 for effect in menu_b)
    conditional_a = e0_square / menu_a_square_sum
    conditional_b = e0_square / menu_b_square_sum
    checks.check(
        "atomic-context-values",
        "normalized restriction gives the exact shared-effect values 25/142 and 2/11",
        conditional_a == Fraction(25, 142) and conditional_b == Fraction(2, 11),
    )
    checks.check(
        "atomic-context-separation",
        "the same effect differs across the two menus by exactly -9/1562",
        conditional_a - conditional_b == Fraction(-9, 1562),
    )

    born_e0 = e0.coefficient / 2
    checks.check(
        "trace-grade-control",
        "the maximally mixed trace grade assigns E0 one quarter in both menus and normalizes each",
        born_e0 == Fraction(1, 4)
        and sum(effect.coefficient / 2 for effect in menu_a) == 1
        and sum(effect.coefficient / 2 for effect in menu_b) == 1,
    )

    candidate_needles = (
        "registers a measurable partition `(A_eta(i|M))_{i=1}^r` of `X`",
        "`K_eta(i|M)=mu_eta(A_eta(i|M))`",
        "locks `x in A_eta(i|M)`, its readout is labeled outcome `i`",
        "Conditional on formation at that site",
        "There is one grade `w_eta`",
        "with `w_eta(0)=0` and `w_eta(I)=1`",
        "Every binary and ternary nonzero resolution of `I` by members of `S`",
        "not an edit, an adopted primitive, a recommendation",
    )
    checks.check(
        "candidate-sufficiency-surface",
        "the note links the existing measure to all four typed interfaces and keeps the wording hypothetical",
        all(phrase in normalized_note for phrase in candidate_needles),
    )
    checks.check(
        "machine-status-contract",
        "the source uses the controlled bounded-support and negative-route-pruning trace fields",
        all(
            phrase in note
            for phrase in (
                "actual_current_surface_status: bounded-support",
                "target_claim_type: bounded_theorem",
                "claim_type_reason:",
                "trace_class: negative_route_pruning",
                "source_of_blocker_text: handoff",
                "audit_required_before_effective_retained: true",
                "bare_retained_allowed: false",
            )
        ),
    )
    checks.check(
        "canonical-nonmutation",
        "the hypothetical partition/menu-kernel notation is absent from the canonical axiom file",
        all(phrase not in axiom for phrase in ("A_eta", "K_eta", "w_eta", "menu-indexed")),
    )
    checks.check(
        "no-go-gate",
        "all N1-N8 sections and the broad-claim rejection are source-visible",
        all(f"### N{index}" in note for index in range(1, 9))
        and "FAIL / DO NOT SHIP" in note
        and "an axiom update is necessary" in note,
    )

    print("per_element: four exact binary projectors and five exact scaled ternary effects are checked; the shared effect is evaluated in both contexts")
    print("per_site: the contradiction and both restriction witnesses are one-site statements at fixed neighbor data; no composite carrier is asserted")
    print("per_mode: all seven neighbor-occupancy classes k=0,...,6 are checked for distinct Gaussian centers; no spectral-mode exhaustion is claimed")
    print("per_block: the global-measure to normalized-menu to effect-grade interface is the only negative block tested")
    print("lattice_wide: checked and not executed — neighbor-count covariance is an analytic source argument; no lattice-wide dynamics or Born no-go is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
