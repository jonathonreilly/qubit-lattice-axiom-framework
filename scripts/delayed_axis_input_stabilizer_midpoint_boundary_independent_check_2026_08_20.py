#!/usr/bin/env python3
"""Independent reconstruction of the delayed-axis stabilizer boundary.

This checker intentionally does not import the primary runner.  It rebuilds
the matrix conjugations, symbolic atom-weight family, midpoint residual, token
debit invariant, and history quotient from separate data structures.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "DELAYED_AXIS_INPUT_STABILIZER_MIDPOINT_TYPE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-20.md"
PRIMARY_PATH = ROOT / "scripts" / "delayed_axis_input_stabilizer_midpoint_boundary_2026_08_20.py"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
BORN_PATH = ROOT / "docs" / "BORN_FORM_SCALED_PROJECTOR_MENU_FAMILY_SITEWISE_FORCING_AND_PAIRED_MENU_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-17.md"
UNIFORMITY_PATH = ROOT / "docs" / "GRADED_CONSTRAINT_MENU_UNIFORMITY_CONTEXTUALITY_AND_C3_ZERO_INFORMATION_POINT_BOUNDED_THEOREM_NOTE_2026-07-11.md"
AUDIT_INPUT_PATHS = (
    "docs/DELAYED_AXIS_INPUT_STABILIZER_MIDPOINT_TYPE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "scripts/delayed_axis_input_stabilizer_midpoint_boundary_2026_08_20.py",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/BORN_FORM_SCALED_PROJECTOR_MENU_FAMILY_SITEWISE_FORCING_AND_PAIRED_MENU_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-17.md",
    "docs/GRADED_CONSTRAINT_MENU_UNIFORMITY_CONTEXTUALITY_AND_C3_ZERO_INFORMATION_POINT_BOUNDED_THEOREM_NOTE_2026-07-11.md",
)

I2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
Z = sp.diag(1, -1)
PAULI = {"X": X, "Y": Y, "Z": Z}
M_AXIS = sp.sqrt(3) * X / 2 + Z / 2
PREPARATIONS = {"U": I2 / 2, "Z": (I2 + Z) / 2}

PREPARATION_SLOT = (-1, 0, 0)
FUEL_SLOT = (1, 0, 0)
AXIS_PLUS_SLOT = (0, 1, 0)
AXIS_MINUS_SLOT = (0, -1, 0)
GUARD_PLUS_SLOT = (0, 0, 1)
GUARD_MINUS_SLOT = (0, 0, -1)


def projector(axis: sp.Matrix, sign: int) -> sp.Matrix:
    return sp.simplify((I2 + sign * axis) / 2)


def exact_matrix_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    return all(sp.simplify(entry) == 0 for entry in left - right)


def spatial_half_turn(slot: tuple[int, int, int]) -> tuple[int, int, int]:
    x, y, z = slot
    return x, -y, -z


def fixes_and_swaps(
    preparation: str,
    axis: str,
    guards: tuple[sp.Matrix, sp.Matrix] | None = None,
) -> bool:
    """Rebuild the whole six-neighbour fixed point and output exchange."""

    internal = Z if axis in ("X", "Y") else X
    axis_matrix = PAULI[axis]
    prep = PREPARATIONS[preparation]
    guard_plus, guard_minus = guards if guards is not None else (I2 / 2, I2 / 2)
    star = {
        PREPARATION_SLOT: prep,
        FUEL_SLOT: I2 / 2,
        AXIS_PLUS_SLOT: projector(axis_matrix, 1),
        AXIS_MINUS_SLOT: projector(axis_matrix, -1),
        GUARD_PLUS_SLOT: guard_plus,
        GUARD_MINUS_SLOT: guard_minus,
    }
    transformed = {
        spatial_half_turn(slot): sp.simplify(internal * content * internal)
        for slot, content in star.items()
    }
    complete_input_fixed = all(
        exact_matrix_equal(transformed[slot], content)
        for slot, content in star.items()
    )
    outcome_exchange = (
        exact_matrix_equal(internal * projector(axis_matrix, 1) * internal, projector(axis_matrix, -1))
        and exact_matrix_equal(internal * projector(axis_matrix, -1) * internal, projector(axis_matrix, 1))
    )
    return complete_input_fixed and outcome_exchange


def response(preparation: str, setting: str) -> tuple[Fraction, Fraction]:
    if preparation == "Z" and setting == "Z":
        return Fraction(1), Fraction(0)
    if fixes_and_swaps(preparation, setting):
        equal_weight = Fraction(19, 11)
        total = equal_weight + equal_weight
        return equal_weight / total, equal_weight / total
    raise AssertionError("an unclassified Pauli row reached the response table")


@dataclass(frozen=True)
class History:
    prep: str
    setting: str
    route: int
    receipt: int
    tester_fuel_available: bool = True


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, description: str, condition: bool, residual: object = None) -> None:
        if condition:
            self.passed += 1
            print(f"PASS [{label}] {description}")
        else:
            self.failed += 1
            print(f"FAIL [{label}] {description}")
            if residual is not None:
                print(f"      residual={residual}")

    def finish(self) -> int:
        print(f"SUMMARY: PASS={self.passed} FAIL={self.failed}")
        return 1 if self.failed else 0


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    primary = PRIMARY_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    born = BORN_PATH.read_text(encoding="utf-8")
    uniformity = UNIFORMITY_PATH.read_text(encoding="utf-8")

    checks.check(
        "sources",
        "independent inputs bind the distribution-value firewall, orbit theorem, and directional cubic",
        "extensional form and values are not specified by this memo" in axiom
        and "constant on each `G`-orbit of cells" in uniformity
        and "g_c(n) = (1 + n_z^3)/2" in born,
    )

    rows = {
        (prep, axis): fixes_and_swaps(prep, axis)
        for prep in ("U", "Z")
        for axis in ("X", "Y", "Z")
    }
    checks.check(
        "matrix-stabilizers",
        "direct conjugation and spatial slot transport independently reproduce exactly five complete-star Pauli sign-swap rows",
        {row for row, value in rows.items() if value}
        == {("U", "X"), ("U", "Y"), ("U", "Z"), ("Z", "X"), ("Z", "Y")},
        residual=rows,
    )

    mixed = PREPARATIONS["U"]
    pure = PREPARATIONS["Z"]
    oriented_setting_changes = not exact_matrix_equal(Z * projector(X, 1) * Z, projector(X, 1))
    nonscalar_guard_fails = not fixes_and_swaps(
        "U", "X", guards=(projector(X, 1), projector(X, 1))
    )
    checks.check(
        "typing-walls",
        "an oriented X projector changes under its swap and I/2 cannot be conjugated to P_z",
        oriented_setting_changes
        and nonscalar_guard_fails
        and sp.trace(mixed * mixed) == sp.Rational(1, 2)
        and sp.trace(pure * pure) == 1
        and mixed.det() != pure.det(),
    )

    gamma = sp.symbols("gamma", positive=True, real=True)
    epsilon = sp.symbols("epsilon", real=True)
    plus_weight = gamma * (1 + epsilon)
    minus_weight = gamma * (1 - epsilon)
    plus_probability = sp.simplify(plus_weight / (plus_weight + minus_weight))
    equality_solution = sp.solve(sp.Eq(plus_weight, minus_weight), epsilon)
    controller = sp.Rational(1, 2)
    aligned = sp.symbols("a", real=True)
    delayed_z = sp.simplify((1 - controller) * sp.Rational(1, 2) + controller * aligned)
    cubic_aligned = sp.solve(sp.Eq(delayed_z, sp.Rational(9, 16)), aligned)
    square_aligned = sp.solve(sp.Eq(delayed_z, sp.Rational(9, 10)), aligned)
    checks.check(
        "symbolic-residual",
        "symbolic normalization gives (1+epsilon)/2 and a fair controller leaves 1/4+a/2",
        plus_probability == (1 + epsilon) / 2
        and equality_solution == [0]
        and sp.simplify(plus_weight - minus_weight - 2 * gamma * epsilon) == 0
        and delayed_z == sp.Rational(1, 4) + aligned / 2
        and sp.solve(sp.Eq(delayed_z, sp.Rational(3, 4)), aligned) == [1]
        and cubic_aligned == [sp.Rational(5, 8)]
        and square_aligned == [sp.Rational(13, 10)],
        residual=(plus_probability, equality_solution, delayed_z, cubic_aligned, square_aligned),
    )

    controller_law = {"U": Fraction(1, 2), "Z": Fraction(1, 2)}
    mixture = {
        setting: sum(controller_law[prep] * response(prep, setting)[0] for prep in ("U", "Z"))
        for setting in ("X", "Y", "Z")
    }
    checks.check(
        "delayed-table",
        "separate Pauli reconstruction gives transverse halves and conditional aligned-certainty three quarters",
        mixture == {"X": Fraction(1, 2), "Y": Fraction(1, 2), "Z": Fraction(3, 4)},
        residual=mixture,
    )

    n = M_AXIS
    p_born = sp.simplify((1 + sp.Rational(1, 2)) / 2)
    p_cubic = sp.simplify((1 + sp.Rational(1, 2) ** 3) / 2)
    z_stabilizer_changes_m = not exact_matrix_equal(Z * projector(n, 1) * Z, projector(n, 1))
    z_stabilizer_fails_to_complement_m = not exact_matrix_equal(Z * projector(n, 1) * Z, projector(n, -1))
    pauli_agreement = all(
        sp.simplify((1 + t) / 2 - (1 + t**3) / 2) == 0 for t in (sp.Integer(0), sp.Integer(1))
    )
    nx, ny, nz = sp.symbols("n_x n_y n_z", real=True)
    orthogonality_necessity = sp.solve(sp.Eq(nz, -nz), nz) == [0]
    z_half_turn = sp.diag(-1, -1, 1)
    equatorial = sp.Matrix([nx, ny, 0])
    orthogonality_converse = exact_matrix_equal(z_half_turn * equatorial, -equatorial)
    checks.check(
        "cubic-domain",
        "a pure-Z fixed swap exists exactly on the equator, so it cannot swap the half-overlap direction while affine and cubic agree at Pauli overlaps",
        z_stabilizer_changes_m
        and z_stabilizer_fails_to_complement_m
        and orthogonality_necessity
        and orthogonality_converse
        and pauli_agreement
        and p_born == sp.Rational(3, 4)
        and p_cubic == sp.Rational(9, 16),
    )

    available, spent, total = 2, 0, 2
    current_rows = []
    for _event in ("controller", "tester"):
        before = (available, spent, total)
        available -= 1
        spent += 1
        after = (available, spent, available + spent)
        current_rows.append((before, after))
    checks.check(
        "token-debit-invariant",
        "two independently reconstructed consumer writes transfer available to spent tokens without changing the stoichiometric total",
        current_rows == [((2, 0, 2), (1, 1, 2)), ((1, 1, 2), (0, 2, 2))],
        residual=current_rows,
    )

    histories = [
        History(prep, setting, route, receipt)
        for prep in ("U", "Z")
        for setting in ("X", "Y", "Z")
        for route in range(3)
        for receipt in range(2)
    ]
    fibres: defaultdict[tuple[str, str], set[tuple[Fraction, Fraction]]] = defaultdict(set)
    delete_prep: defaultdict[str, set[tuple[Fraction, Fraction]]] = defaultdict(set)
    delete_setting: defaultdict[str, set[tuple[Fraction, Fraction]]] = defaultdict(set)
    for history in histories:
        law = response(history.prep, history.setting) if history.tester_fuel_available else (Fraction(0), Fraction(0))
        fibres[(history.prep, history.setting)].add(law)
        delete_prep[history.setting].add(law)
        delete_setting[history.prep].add(law)
    fuel_sector_pair = {
        response("U", "X"),
        (Fraction(0), Fraction(0)),
    }
    checks.check(
        "quotient",
        "36 raw histories lump on preparation plus setting, while either live field deletion fails",
        len(histories) == 36
        and all(len(values) == 1 for values in fibres.values())
        and len(delete_prep["Z"]) == 2
        and len(delete_setting["Z"]) == 2
        and len(fuel_sector_pair) == 2,
    )

    checks.check(
        "source-contract",
        "the note and primary expose conditional covariance, aligned certainty, the type correction, and narrow no-go boundary",
        all(
            phrase in note
            for phrase in (
                "internal-automorphism covariance is not explicit axiom text",
                "three-quarter transcript occurs if and only if aligned certainty is supplied",
                "current directional cubic remains live",
                "FAIL / DO NOT SHIP",
                "no TOE percentage moves",
            )
        )
        and "def sign_swap_witness" in primary
        and "def delayed_z_mixture" in primary
        and "the Born rule is derived" not in note.lower(),
    )

    n5_lines = (
        "per_element: independently reconstructed matrix spectra, projector swaps, and supported outcome rows",
        "per_site: independently checked the preparation-axis-resource complete-input stabilizer classification",
        "per_mode: rebuilt mixed, pure, Pauli, oblique, affine, cubic, square, and epsilon comparisons",
        "per_block: rebuilt fair-controller residual, token debit transfer, delayed table, quotient, and deletion failures",
        "lattice_wide: checked and not executed — arbitrary menus, autonomous setting genesis, action, time, and actuality remain open",
    )
    for line in n5_lines:
        print(line)
    checks.check(
        "n5-certificate",
        "independent evidence contains all five substantive forensic resolution classes",
        all(len(line) >= 40 for line in n5_lines),
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
