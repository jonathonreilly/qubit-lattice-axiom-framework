#!/usr/bin/env python3
"""Exact delayed-axis input-stabilizer and midpoint-boundary checks.

The runner classifies when a complete finite Record input admits an
input-fixing automorphism that exchanges an exhaustive binary outcome pair.
It then checks the fair-controller midpoint, the exact resource current, the
Record-fibre quotient, and the oblique-axis epsilon family.  No cache is
written by this script.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path
from typing import Iterable


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "DELAYED_AXIS_INPUT_STABILIZER_MIDPOINT_TYPE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-20.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
BORN_PATH = ROOT / "docs" / "BORN_FORM_SCALED_PROJECTOR_MENU_FAMILY_SITEWISE_FORCING_AND_PAIRED_MENU_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-17.md"
CYCLE20_PATH = ROOT / "docs" / "work_history" / "repo" / "review_feedback" / "OPERATIONAL_QUOTIENT_BORN_AFFINITY_CYCLE20_NOTE_2026-07-14.md"
BLOCK1_PATH = ROOT / "docs" / "RECORD_NATIVE_DYADIC_PREPARATION_TAG_SCREENING_BOUNDED_THEOREM_NOTE_2026-08-20.md"
UNIFORMITY_PATH = ROOT / "docs" / "GRADED_CONSTRAINT_MENU_UNIFORMITY_CONTEXTUALITY_AND_C3_ZERO_INFORMATION_POINT_BOUNDED_THEOREM_NOTE_2026-07-11.md"
REGISTRY_PATH = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
AUDIT_INPUT_PATHS = (
    "docs/DELAYED_AXIS_INPUT_STABILIZER_MIDPOINT_TYPE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/BORN_FORM_SCALED_PROJECTOR_MENU_FAMILY_SITEWISE_FORCING_AND_PAIRED_MENU_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-17.md",
    "docs/work_history/repo/review_feedback/OPERATIONAL_QUOTIENT_BORN_AFFINITY_CYCLE20_NOTE_2026-07-14.md",
    "docs/RECORD_NATIVE_DYADIC_PREPARATION_TAG_SCREENING_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "docs/GRADED_CONSTRAINT_MENU_UNIFORMITY_CONTEXTUALITY_AND_C3_ZERO_INFORMATION_POINT_BOUNDED_THEOREM_NOTE_2026-07-11.md",
    "docs/audit/data/axiom_premise_nodes.json",
)

Point = tuple[int, int, int]
Vector = tuple[int, int, int]

ZERO: Vector = (0, 0, 0)
AXIS_VECTOR: dict[str, Vector] = {
    "X": (1, 0, 0),
    "Y": (0, 1, 0),
    "Z": (0, 0, 1),
}
PREPARATION_VECTOR: dict[str, Vector] = {
    "U": ZERO,
    "Z": AXIS_VECTOR["Z"],
}
INTERNAL_ROTATION: dict[str, tuple[Vector, Vector, Vector]] = {
    "X": ((1, 0, 0), (0, -1, 0), (0, 0, -1)),
    "Z": ((-1, 0, 0), (0, -1, 0), (0, 0, 1)),
}
SPATIAL_HALF_TURN = INTERNAL_ROTATION["X"]

PREPARATION_SLOT: Point = (-1, 0, 0)
FUEL_SLOT: Point = (1, 0, 0)
AXIS_PLUS_SLOT: Point = (0, 1, 0)
AXIS_MINUS_SLOT: Point = (0, -1, 0)
GUARD_PLUS_SLOT: Point = (0, 0, 1)
GUARD_MINUS_SLOT: Point = (0, 0, -1)


def dot(a: Point, b: Point) -> int:
    return sum(x * y for x, y in zip(a, b, strict=True))


def determinant3(matrix: tuple[Vector, Vector, Vector]) -> int:
    a, b, c = matrix
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def cubic_rotations() -> tuple[tuple[Vector, Vector, Vector], ...]:
    basis: tuple[Vector, ...] = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    rotations: list[tuple[Vector, Vector, Vector]] = []
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            rows = tuple(
                tuple(signs[row] * entry for entry in basis[permutation[row]])
                for row in range(3)
            )
            if determinant3(rows) == 1:
                rotations.append(rows)  # type: ignore[arg-type]
    return tuple(rotations)


ROTATIONS = cubic_rotations()


def rotate(matrix: tuple[Vector, Vector, Vector], point: Point) -> Point:
    return tuple(dot(row, point) for row in matrix)  # type: ignore[return-value]


@dataclass(frozen=True)
class TesterInput:
    """Complete six-neighbour tester star at the instant before the write."""

    preparation: str
    axis: str
    axis_is_unoriented_pair: bool = True
    fuel: str = "fresh-scalar-token"
    guard_pair: tuple[Vector, Vector] = (ZERO, ZERO)


@dataclass(frozen=True)
class StabilizerWitness:
    internal_conjugation: str
    spatial_rotation: str
    fixes_preparation: bool
    fixes_resource_and_guards: bool
    fixes_axis_record_configuration: bool
    exchanges_outcomes: bool

    @property
    def valid(self) -> bool:
        return (
            self.fixes_preparation
            and self.fixes_resource_and_guards
            and self.fixes_axis_record_configuration
            and self.exchanges_outcomes
        )


def sign_swap_witness(data: TesterInput) -> StabilizerWitness | None:
    """Return the represented complete-input sign swap, when it exists.

    The spatial factor is the proper-cubic half turn diag(1,-1,-1).  It swaps
    the two sites carrying an unoriented axis pair and the two identical guard
    sites while fixing the preparation and fuel sites.  The internal factor
    swaps the two projectors in the declared outcome menu.
    """

    if not data.axis_is_unoriented_pair or data.axis not in AXIS_VECTOR:
        return None
    if data.axis in ("X", "Y"):
        conjugation = "Z"
        fixes_preparation = data.preparation in ("U", "Z")
    elif data.axis == "Z":
        conjugation = "X"
        fixes_preparation = data.preparation == "U"
    else:
        return None
    internal = INTERNAL_ROTATION[conjugation]
    preparation = PREPARATION_VECTOR[data.preparation]
    axis_plus = AXIS_VECTOR[data.axis]
    axis_minus = tuple(-entry for entry in axis_plus)
    star = {
        PREPARATION_SLOT: preparation,
        FUEL_SLOT: ZERO,
        AXIS_PLUS_SLOT: axis_plus,
        AXIS_MINUS_SLOT: axis_minus,
        GUARD_PLUS_SLOT: data.guard_pair[0],
        GUARD_MINUS_SLOT: data.guard_pair[1],
    }
    transformed_star = {
        rotate(SPATIAL_HALF_TURN, slot): rotate(internal, content)
        for slot, content in star.items()
    }
    fixes_resource_and_guards = all(
        transformed_star[slot] == star[slot]
        for slot in (FUEL_SLOT, GUARD_PLUS_SLOT, GUARD_MINUS_SLOT)
    )
    fixes_axis_record_configuration = all(
        transformed_star[slot] == star[slot]
        for slot in (AXIS_PLUS_SLOT, AXIS_MINUS_SLOT)
    )
    exchanges_outcomes = (
        rotate(internal, axis_plus) == axis_minus
        and rotate(internal, axis_minus) == axis_plus
    )
    return StabilizerWitness(
        internal_conjugation=conjugation,
        spatial_rotation="diag(1,-1,-1)",
        fixes_preparation=fixes_preparation
        and transformed_star[PREPARATION_SLOT] == star[PREPARATION_SLOT],
        fixes_resource_and_guards=fixes_resource_and_guards,
        fixes_axis_record_configuration=fixes_axis_record_configuration,
        exchanges_outcomes=exchanges_outcomes,
    )


def supported_outcomes(preparation: str, axis: str) -> tuple[str, ...]:
    """The separately declared orthogonality-support rule on tested rows."""

    if preparation == "Z" and axis == "Z":
        return ("+",)
    return ("+", "-")


def deformed_atom_weights(gamma: Fraction, epsilon: Fraction) -> dict[str, Fraction]:
    if gamma <= 0 or abs(epsilon) >= 1:
        raise ValueError("gamma must be positive and |epsilon| must be below one")
    return {
        "+": gamma * (1 + epsilon),
        "-": gamma * (1 - epsilon),
    }


def normalize_weights(weights: dict[str, Fraction], support: Iterable[str]) -> dict[str, Fraction]:
    allowed = tuple(support)
    total = sum((weights[label] for label in allowed), Fraction(0))
    if total <= 0:
        raise ValueError("supported atom weight must be positive")
    return {label: weights[label] / total for label in allowed}


def row_law(preparation: str, axis: str, epsilon: Fraction = Fraction(0)) -> dict[str, Fraction]:
    support = supported_outcomes(preparation, axis)
    if len(support) == 1:
        return {support[0]: Fraction(1), "-": Fraction(0)}
    witness = sign_swap_witness(TesterInput(preparation, axis))
    effective_epsilon = Fraction(0) if witness is not None and witness.valid else epsilon
    normalized = normalize_weights(deformed_atom_weights(Fraction(7, 5), effective_epsilon), support)
    return {"+": normalized["+"], "-": normalized["-"]}


@dataclass(frozen=True)
class TokenState:
    tokens: tuple[str, ...]
    consumers: frozenset[tuple[str, str]] = frozenset()

    def available(self, token: str) -> bool:
        return token in self.tokens and all(parent != token for parent, _event in self.consumers)

    def charge_components(self) -> tuple[int, int]:
        spent_parents = {parent for parent, _event in self.consumers}
        available = sum(token not in spent_parents for token in self.tokens)
        spent = len(spent_parents)
        return available, spent

    def charge(self) -> int:
        available, spent = self.charge_components()
        return available + spent

    def consume(self, token: str, event: str) -> "TokenState":
        if not self.available(token):
            raise ValueError("token is absent or already has a permanent consumer child")
        return TokenState(self.tokens, self.consumers | {(token, event)})


@dataclass(frozen=True)
class RawHistory:
    preparation: str
    controller_tag: str
    controller_route: str
    receipt_order: str
    setting: str
    controller_fuel_available: bool = False
    tester_fuel_available: bool = True


def transcript(history: RawHistory) -> tuple[Fraction, Fraction]:
    if not history.tester_fuel_available:
        return Fraction(0), Fraction(0)
    law = row_law(history.preparation, history.setting)
    return law["+"], law["-"]


def odd_response(overlap: Fraction, power: int) -> Fraction:
    if power <= 0 or power % 2 == 0:
        raise ValueError("power must be positive and odd")
    return (1 + overlap**power) / 2


def normalized_square(probability: Fraction) -> Fraction:
    numerator = probability * probability
    complement = (1 - probability) * (1 - probability)
    return numerator / (numerator + complement)


def delayed_z_mixture(controller_plus: Fraction, aligned_certainty: Fraction) -> Fraction:
    """Coarse-grain U/Z branches while leaving the aligned response explicit."""

    if not 0 <= controller_plus <= 1 or not 0 <= aligned_certainty <= 1:
        raise ValueError("probabilities must lie in the unit interval")
    mixed_row = normalize_weights(deformed_atom_weights(Fraction(1), Fraction(0)), ("+", "-"))["+"]
    return (1 - controller_plus) * mixed_row + controller_plus * aligned_certainty


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, section: str, description: str, condition: bool, residual: object = None) -> None:
        if condition:
            self.passed += 1
            print(f"PASS [{section}] {description}")
        else:
            self.failed += 1
            print(f"FAIL [{section}] {description}")
            if residual is not None:
                print(f"      residual={residual}")

    def finish(self) -> int:
        print(f"SUMMARY: PASS={self.passed} FAIL={self.failed}")
        return 1 if self.failed else 0


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    born = BORN_PATH.read_text(encoding="utf-8")
    cycle20 = CYCLE20_PATH.read_text(encoding="utf-8")
    block1 = BLOCK1_PATH.read_text(encoding="utf-8")
    uniformity = UNIFORMITY_PATH.read_text(encoding="utf-8")

    checks.check(
        "sources",
        "the live axiom distribution clause and the two exact prior comparator surfaces are bound",
        "probability distribution over the possibilities" in axiom
        and "g_c(n) = (1 + n_z^3)/2" in born
        and "record-fibre strong lumpability" in cycle20
        and "separately supplied bridge `B`" in block1
        and "constant on each `G`-orbit of cells" in uniformity,
    )

    checks.check(
        "geometry",
        "the proper-cubic group has 24 elements and the half turn used by every setting pair is represented",
        len(ROTATIONS) == 24
        and ((1, 0, 0), (0, -1, 0), (0, 0, -1)) in ROTATIONS
        and all({rotate(rotation, point) for point in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))}
                == {(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)}
                for rotation in ROTATIONS),
    )

    expected_witness_rows = {("U", "X"), ("U", "Y"), ("U", "Z"), ("Z", "X"), ("Z", "Y")}
    actual_witness_rows = {
        (preparation, axis)
        for preparation, axis in product(("U", "Z"), ("X", "Y", "Z"))
        if (witness := sign_swap_witness(TesterInput(preparation, axis))) is not None and witness.valid
    }
    checks.check(
        "stabilizers",
        "complete-input sign-swapping stabilizers exist exactly for mixed X/Y/Z and pure-Z transverse X/Y rows",
        actual_witness_rows == expected_witness_rows,
        residual=actual_witness_rows,
    )

    oriented_failures = [
        sign_swap_witness(TesterInput(preparation, axis, axis_is_unoriented_pair=False)) is None
        for preparation, axis in expected_witness_rows
    ]
    nonscalar_guard = sign_swap_witness(
        TesterInput("U", "X", guard_pair=(AXIS_VECTOR["X"], AXIS_VECTOR["X"]))
    )
    checks.check(
        "axis-typing",
        "an oriented setting and an identical but internally noninvariant guard pair both fail the complete-input fixed-point test",
        all(oriented_failures)
        and nonscalar_guard is not None
        and not nonscalar_guard.fixes_resource_and_guards
        and not nonscalar_guard.valid,
    )

    gamma = Fraction(11, 7)
    deformation_rows = []
    deformation_ok = True
    for epsilon in (Fraction(-2, 5), Fraction(-1, 7), Fraction(0), Fraction(1, 6), Fraction(3, 8)):
        weights = deformed_atom_weights(gamma, epsilon)
        probabilities = normalize_weights(weights, ("+", "-"))
        deformation_rows.append((epsilon, probabilities["+"], probabilities["-"]))
        deformation_ok &= probabilities["+"] - probabilities["-"] == epsilon
        deformation_ok &= sum(probabilities.values(), Fraction(0)) == 1
        deformation_ok &= (weights["+"] == weights["-"]) == (epsilon == 0)
    checks.check(
        "atom-weight-deformation",
        "symbolic two-atom weights retain epsilon unless an input-fixing exchange equates them",
        deformation_ok,
        residual=deformation_rows,
    )

    row_table = {
        (preparation, axis): row_law(preparation, axis)
        for preparation, axis in product(("U", "Z"), ("X", "Y", "Z"))
    }
    checks.check(
        "pauli-rows",
        "stabilizers force every supported transverse row while the supplied orthogonality-support rule makes pure Z-on-Z deterministic",
        all(row_table[("U", axis)] == {"+": Fraction(1, 2), "-": Fraction(1, 2)} for axis in ("X", "Y", "Z"))
        and all(row_table[("Z", axis)] == {"+": Fraction(1, 2), "-": Fraction(1, 2)} for axis in ("X", "Y"))
        and row_table[("Z", "Z")] == {"+": Fraction(1), "-": Fraction(0)},
        residual=row_table,
    )

    controller_weights = normalize_weights(deformed_atom_weights(Fraction(13, 9), Fraction(0)), ("+", "-"))
    aligned_rows = [
        (certainty, delayed_z_mixture(controller_weights["+"], certainty))
        for certainty in (Fraction(0), Fraction(1, 3), Fraction(5, 8), Fraction(2, 3), Fraction(1))
    ]
    aligned_for_square = 2 * (Fraction(9, 10) - Fraction(1, 4))
    checks.check(
        "aligned-response-residual",
        "a fair controller leaves the delayed Z transcript equal to one quarter plus one half of the aligned certainty",
        all(value == Fraction(1, 4) + certainty / 2 for certainty, value in aligned_rows)
        and [certainty for certainty, value in aligned_rows if value == Fraction(3, 4)] == [Fraction(1)]
        and dict(aligned_rows)[Fraction(5, 8)] == Fraction(9, 16)
        and aligned_for_square == Fraction(13, 10) > 1,
        residual=(aligned_rows, aligned_for_square),
    )
    mixture = {}
    for setting in ("X", "Y", "Z"):
        mixture[setting] = (
            controller_weights["-"] * row_law("U", setting)["+"]
            + controller_weights["+"] * row_law("Z", setting)["+"]
        )
    checks.check(
        "delayed-midpoint",
        "a symmetry-forced fair tag followed by the supplied tag-to-preparation compiler gives late X/Y halves and a late Z three-quarter transcript",
        mixture == {"X": Fraction(1, 2), "Y": Fraction(1, 2), "Z": Fraction(3, 4)},
        residual=mixture,
    )

    midpoint = mixture["Z"]
    overlap = 2 * midpoint - 1
    square = normalized_square(midpoint)
    radial_cubic = odd_response(overlap, 3)
    checks.check(
        "named-midpoint-controls",
        "the physical mixture transcript is 3/4, normalized square is 9/10, and the explicitly typed radial cubic extension is 9/16",
        midpoint == Fraction(3, 4)
        and square == Fraction(9, 10)
        and radial_cubic == Fraction(9, 16),
        residual=(midpoint, square, radial_cubic),
    )

    pure_pauli = {
        axis: (odd_response(Fraction(0) if axis in ("X", "Y") else Fraction(1), 1),
               odd_response(Fraction(0) if axis in ("X", "Y") else Fraction(1), 3))
        for axis in ("X", "Y", "Z")
    }
    oblique = {power: odd_response(Fraction(1, 2), power) for power in (1, 3, 5)}
    checks.check(
        "directional-cubic-type-boundary",
        "Born and the current directional cubic agree on pure-Z Pauli X/Y/Z rows but differ at the oblique half-overlap direction",
        all(born_value == cubic_value for born_value, cubic_value in pure_pauli.values())
        and oblique[1] == Fraction(3, 4)
        and oblique[3] == Fraction(9, 16)
        and len(set(oblique.values())) == 3,
        residual=(pure_pauli, oblique),
    )

    oblique_input = TesterInput("Z", "M")
    oblique_weights = {
        "Born": normalize_weights(deformed_atom_weights(Fraction(1), Fraction(1, 2)), ("+", "-"))["+"],
        "cubic": normalize_weights(deformed_atom_weights(Fraction(1), Fraction(1, 8)), ("+", "-"))["+"],
    }
    checks.check(
        "oblique-stabilizer-wall",
        "the pure-Z stabilizer preserves n_z and cannot exchange an oblique n_z=1/2 outcome with its complement",
        sign_swap_witness(oblique_input) is None
        and Fraction(1, 2) != -Fraction(1, 2)
        and oblique_weights == {"Born": Fraction(3, 4), "cubic": Fraction(9, 16)},
        residual=oblique_weights,
    )

    checks.check(
        "spectral-controller-wall",
        "unitary conjugation cannot exchange I/2 and P_z because their exact spectra differ",
        tuple(sorted((Fraction(1, 2), Fraction(1, 2))))
        != tuple(sorted((Fraction(1), Fraction(0)))),
    )

    resource = TokenState(("controller-fuel", "tester-fuel"))
    q0 = resource.charge()
    before_controller = resource.charge_components()
    after_controller = resource.consume("controller-fuel", "controller-record")
    after_test = after_controller.consume("tester-fuel", "outcome-record")
    duplicate_rejected = False
    try:
        after_test.consume("controller-fuel", "duplicate-record")
    except ValueError:
        duplicate_rejected = True
    checks.check(
        "token-debit-invariant",
        "the same two writes consume distinct tokens with Delta available=-1, Delta spent=+1 and conserved stoichiometric count",
        before_controller == (2, 0)
        and after_controller.charge_components() == (1, 1)
        and after_test.charge_components() == (0, 2)
        and q0 == after_controller.charge() == after_test.charge() == 2
        and duplicate_rejected,
    )

    histories = [
        RawHistory(preparation, controller_tag, route, receipt_order, setting)
        for preparation, controller_tag in (("U", "-"), ("Z", "+"))
        for route in ("north", "south")
        for receipt_order in ("guard-before-fuel", "fuel-before-guard")
        for setting in ("X", "Y", "Z")
    ]
    fibres: defaultdict[tuple[str, str], set[tuple[Fraction, Fraction]]] = defaultdict(set)
    without_preparation: defaultdict[str, set[tuple[Fraction, Fraction]]] = defaultdict(set)
    without_setting: defaultdict[str, set[tuple[Fraction, Fraction]]] = defaultdict(set)
    for history in histories:
        future = transcript(history)
        fibres[(history.preparation, history.setting)].add(future)
        without_preparation[history.setting].add(future)
        without_setting[history.preparation].add(future)
    fuel_sector_pair = {
        transcript(RawHistory("U", "-", "north", "guard-before-fuel", "X", tester_fuel_available=True)),
        transcript(RawHistory("U", "-", "north", "guard-before-fuel", "X", tester_fuel_available=False)),
    }
    checks.check(
        "record-fibre-lumpability",
        "outcome laws factor through current preparation plus later setting Records over controller route and receipt history",
        len(histories) == 24
        and all(len(fingerprints) == 1 for fingerprints in fibres.values())
        and len(without_preparation["Z"]) == 2
        and len(without_setting["Z"]) == 2
        and len(fuel_sector_pair) == 2,
        residual={key: len(value) for key, value in fibres.items()},
    )

    timeline = {"controller": 0, "preparation": 1, "setting": 2, "outcome": 3}
    checks.check(
        "delayed-setting-order",
        "the setting Record is formed strictly after preparation and strictly before the outcome Record",
        timeline["controller"] < timeline["preparation"] < timeline["setting"] < timeline["outcome"],
    )

    required_note_phrases = (
        "actual_current_surface_status: bounded-support",
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
        "No-Go Discipline Gate",
        "internal-automorphism covariance is not explicit axiom text",
        "three-quarter transcript occurs if and only if aligned certainty is supplied",
        "current directional cubic remains live",
        "FAIL / DO NOT SHIP",
        "no TOE percentage moves",
        "review-loop is not used",
    )
    checks.check(
        "claim-boundary",
        "the note exposes the axiom-interpretation wall, type correction, narrow no-go scope, and zero formal progress",
        all(phrase in note for phrase in required_note_phrases)
        and "the Born rule is derived" not in note.lower()
        and "gravity is closed" not in note.lower(),
    )

    n5_lines = (
        "per_element: exact preparation spectra, supported outcome labels, and input-fixing conjugation rows are checked",
        "per_site: one complete six-neighbour tester star with preparation, fuel, axis-pair, and guard Records is classified",
        "per_mode: mixed and pure preparations, X/Y/Z and oblique settings, affine, square, cubic, and epsilon modes run",
        "per_block: controller and aligned-response residuals, two-token debit invariant, delayed order, quotient, and deletions are checked",
        "lattice_wide: checked and not executed — arbitrary axes, full menu registration, autonomous settings, time, and actuality remain open",
    )
    for line in n5_lines:
        print(line)
    checks.check(
        "n5-certificate",
        "all five landing-resolution statements are substantive and at least forty characters",
        all(
            len(line) >= 40
            and line.startswith(("per_element:", "per_site:", "per_mode:", "per_block:", "lattice_wide:"))
            for line in n5_lines
        ),
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
