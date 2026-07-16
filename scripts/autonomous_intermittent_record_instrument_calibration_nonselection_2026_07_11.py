#!/usr/bin/env python3
"""Exact finite checks for the autonomous intermittent Record-instrument theorem."""

from pathlib import Path

import sympy as sp


PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str) -> None:
    global PASS, FAIL
    if bool(condition):
        PASS += 1
        print(f"PASS {name}: {detail}")
    else:
        FAIL += 1
        print(f"FAIL {name}: {detail}")


def ket(dimension: int, index: int) -> sp.Matrix:
    return sp.eye(dimension)[:, index]


def projector(vector: sp.Matrix) -> sp.Matrix:
    return sp.simplify(vector * vector.H)


def matrix_unit(dimension: int, row: int, column: int) -> sp.Matrix:
    return ket(dimension, row) * ket(dimension, column).H


def channel(kraus: list[sp.Matrix], rho: sp.Matrix) -> sp.Matrix:
    return sp.simplify(sum((item * rho * item.H for item in kraus), sp.zeros(rho.rows)))


def autonomous_kraus(
    dimension: int,
    mixing: sp.Expr,
    empty_weight: sp.Expr,
    frame: sp.Matrix | None = None,
) -> tuple[list[sp.Matrix], sp.Matrix, list[list[sp.Matrix]], list[list[sp.Matrix]]]:
    """Kraus family on system tensor (blank direct-sum locked labels)."""
    frame = sp.eye(dimension) if frame is None else frame
    register_dimension = dimension + 1
    blank = matrix_unit(register_dimension, 0, 0)

    no_record = sp.sqrt(empty_weight) * sp.kronecker_product(sp.eye(dimension), blank)
    formation: list[list[sp.Matrix]] = []
    locked: list[list[sp.Matrix]] = []

    for outcome in range(dimension):
        formation_row: list[sp.Matrix] = []
        locked_row: list[sp.Matrix] = []
        for source in range(dimension):
            weight = mixing * int(outcome == source) + (1 - mixing) / dimension
            system_write = frame * matrix_unit(dimension, outcome, source) * frame.H
            record_write = matrix_unit(register_dimension, outcome + 1, 0)
            formation_row.append(
                sp.sqrt((1 - empty_weight) * weight)
                * sp.kronecker_product(system_write, record_write)
            )
            locked_register = matrix_unit(register_dimension, outcome + 1, outcome + 1)
            locked_row.append(sp.kronecker_product(system_write, locked_register))
        formation.append(formation_row)
        locked.append(locked_row)

    all_kraus = [no_record]
    all_kraus.extend(item for row in formation for item in row)
    all_kraus.extend(item for row in locked for item in row)
    return all_kraus, no_record, formation, locked


def classification_checks() -> None:
    x, y, e0, e1 = sp.symbols("x y e0 e1", real=True)
    effect0 = sp.Matrix([[e0, x + sp.I * y], [x - sp.I * y, 0]])
    check("C01", sp.expand(effect0.det()) == -(x**2 + y**2), "PSD plus a zero cross-label diagonal kills the complex off-diagonal")
    check("C02", effect0.subs({x: 0, y: 0}) == e0 * projector(ket(2, 0)), "the first repeat-exclusive effect is e_0 P_0")

    p0, p1 = (projector(ket(2, i)) for i in range(2))
    effects = [e0 * p0, e1 * p1]
    empty = sp.simplify(sp.eye(2) - sum(effects, sp.zeros(2)))
    check("C03", empty == sp.diag(1 - e0, 1 - e1), "normalization fixes the diagonal no-record effect")
    check("C04", empty + sum(effects, sp.zeros(2)) == sp.eye(2), "the classified effects form a normalized intermittent menu")

    dimension = 3
    efficiencies = (sp.Rational(1, 2), sp.Rational(2, 3), sp.Rational(3, 4))
    menu = [projector(ket(dimension, i)) for i in range(dimension)]
    effects3 = [efficiencies[i] * menu[i] for i in range(dimension)]
    empty3 = sp.eye(dimension) - sum(effects3, sp.zeros(dimension))
    check("C05", empty3 == sp.diag(sp.Rational(1, 2), sp.Rational(1, 3), sp.Rational(1, 4)), "dimension-three efficiencies leave the complementary no-record effect")
    check("C06", all(sp.trace(effects3[i] * menu[j]) == 0 for i in range(dimension) for j in range(dimension) if i != j), "classified formation effects obey cross-label exclusion")

    rho = sp.diag(sp.Rational(1, 3), sp.Rational(2, 3))
    biased_effects = [sp.Rational(1, 2) * p0, sp.Rational(3, 4) * p1]
    biased_weights = [sp.trace(item * rho) for item in biased_effects]
    biased_conditional = sp.simplify(biased_weights[0] / sum(biased_weights))
    check("C07", biased_conditional == sp.Rational(1, 4), "unequal formation efficiencies bias the conditional nonempty distribution")
    check("C08", biased_conditional != sp.trace(p0 * rho), "normalization and repeat exclusivity alone do not recover Born-form conditional weights")

    efficiency = sp.Rational(2, 3)
    neutral_effects = [efficiency * p0, efficiency * p1]
    neutral_weights = [sp.trace(item * rho) for item in neutral_effects]
    check("C09", sp.simplify(neutral_weights[0] / sum(neutral_weights)) == sp.trace(p0 * rho), "permutation-neutral event efficiency restores Born-form conditional weights")
    check("C10", sp.eye(2) - sum(neutral_effects, sp.zeros(2)) == sp.Rational(1, 3) * sp.eye(2), "permutation neutrality makes the no-record effect scalar")


def autonomous_hostile_checks() -> None:
    dimension = 2
    mixing = sp.Rational(1, 3)
    empty_weight = sp.Rational(1, 4)
    kraus, no_record, formation, _ = autonomous_kraus(dimension, mixing, empty_weight)
    extended_dimension = dimension * (dimension + 1)
    completeness = sum((item.H * item for item in kraus), sp.zeros(extended_dimension))
    check("A01", sp.simplify(completeness) == sp.eye(extended_dimension), "the autonomous blank-plus-locked Kraus family is exactly CPTP")

    blank = projector(ket(dimension + 1, 0))
    locked_registers = [projector(ket(dimension + 1, i + 1)) for i in range(dimension)]
    menu = [projector(ket(dimension, i)) for i in range(dimension)]

    no_record_effect = sp.zeros(dimension)
    blank_projector = sp.kronecker_product(sp.eye(dimension), blank)
    no_record_effect_full = sp.simplify(blank_projector * no_record.H * no_record * blank_projector)
    for row in range(dimension):
        for column in range(dimension):
            no_record_effect[row, column] = no_record_effect_full[row * (dimension + 1), column * (dimension + 1)]
    check("A02", no_record_effect == empty_weight * sp.eye(dimension), "the blank-sector no-record effect is q I")

    for outcome in range(dimension):
        effect = sp.zeros(dimension)
        for item in formation[outcome]:
            full_effect = sp.simplify(blank_projector * item.H * item * blank_projector)
            for row in range(dimension):
                for column in range(dimension):
                    effect[row, column] += full_effect[row * (dimension + 1), column * (dimension + 1)]
        expected = (1 - empty_weight) * (
            mixing * menu[outcome] + (1 - mixing) * sp.eye(dimension) / dimension
        )
        check(f"A03i{outcome}", sp.simplify(effect - expected) == sp.zeros(dimension), "blank formation effect is the scaled depolarized hostile effect")

    cross_probability = sp.simplify(
        sum(sp.trace(item * sp.kronecker_product(menu[1], blank) * item.H) for item in formation[0])
    )
    check("A04", cross_probability == sp.Rational(1, 4), "the hostile blank sector has nonzero cross-label formation weight")

    for label in range(dimension):
        locked_state = sp.kronecker_product(menu[label], locked_registers[label])
        once = channel(kraus, locked_state)
        twice = channel(kraus, once)
        check(f"A05i{label}", once == locked_state, "the consistent locked-register state is fixed by one channel use")
        check(f"A06i{label}", twice == once, "same-map reuse preserves locked-register-sector absorption")

    calibrated, _, calibrated_formation, _ = autonomous_kraus(dimension, sp.Integer(1), empty_weight)
    calibrated_complete = sum((item.H * item for item in calibrated), sp.zeros(extended_dimension))
    check("A07", calibrated_complete == sp.eye(extended_dimension), "the calibrated a=1 positive control is also CPTP")
    calibrated_cross = sp.simplify(
        sum(sp.trace(item * sp.kronecker_product(menu[1], blank) * item.H) for item in calibrated_formation[0])
    )
    check("A08", calibrated_cross == 0, "a=1 removes cross-label formation")
    check("A09", mixing != 1 and cross_probability > 0, "auxiliary register absorption and same-map reuse do not imply blank-sector cross-label exclusion")


def covariance_and_dilation_checks() -> None:
    dimension = 2
    mixing = sp.Rational(1, 3)
    empty_weight = sp.Rational(1, 4)
    hadamard = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
    complex_unitary = sp.Matrix([[1, sp.I], [sp.I, 1]]) / sp.sqrt(2)
    base, _, _, _ = autonomous_kraus(dimension, mixing, empty_weight)
    register_identity = sp.eye(dimension + 1)
    rho_system = sp.Matrix([[sp.Rational(2, 3), sp.sqrt(2) / 3], [sp.sqrt(2) / 3, sp.Rational(1, 3)]])
    blank = projector(ket(dimension + 1, 0))
    locked_zero = projector(ket(dimension + 1, 1))
    fixtures = (
        ("hadamard_blank", hadamard, sp.kronecker_product(rho_system, blank)),
        ("hadamard_locked", hadamard, sp.kronecker_product(rho_system, locked_zero)),
        ("complex_blank", complex_unitary, sp.kronecker_product(rho_system, blank)),
        ("complex_locked", complex_unitary, sp.kronecker_product(rho_system, locked_zero)),
    )
    for index, (label, unitary, rho) in enumerate(fixtures, 1):
        rotated, _, _, _ = autonomous_kraus(dimension, mixing, empty_weight, unitary)
        intertwiner = sp.kronecker_product(unitary, register_identity)
        left = channel(rotated, intertwiner * rho * intertwiner.H)
        right = sp.simplify(intertwiner * channel(base, rho) * intertwiner.H)
        check(f"V{index:02d}", sp.simplify(left - right) == sp.zeros(left.rows), f"{label} corroborates supplied-menu family equivariance")

    q = sp.Rational(1, 3)
    p0, p1 = (projector(ket(2, i)) for i in range(2))
    x_gate = sp.sqrt(q) * sp.Matrix([[0, 1], [1, 0]])
    dephasing = [sp.sqrt(q) * p0, sp.sqrt(q) * p1]
    check("V05", x_gate.H * x_gate == q * sp.eye(2), "a one-Kraus no-record map has scalar effect q I")
    check("V06", sum((item.H * item for item in dephasing), sp.zeros(2)) == q * sp.eye(2), "a multi-Kraus no-record map can have the same scalar effect")
    plus = projector(sp.Matrix([1, 1]) / sp.sqrt(2))
    check("V07", channel([x_gate], plus) != channel(dephasing, plus), "the scalar no-record effect does not select the conditional no-record channel")
    unitary_part = sp.simplify(x_gate / sp.sqrt(q))
    check("V08", unitary_part.H * unitary_part == sp.eye(2), "the one-Kraus special case is sqrt(q) times a unitary")


def source_checks() -> None:
    path = Path("docs/AUTONOMOUS_INTERMITTENT_RECORD_INSTRUMENT_CALIBRATION_NONSELECTION_BOUNDED_THEOREM_NOTE_2026-07-11.md")
    check("S01", path.exists(), "source note exists")
    text = path.read_text() if path.exists() else ""
    markers = (
        "conditional repeat/exclusivity",
        "does not identify the external labels as framework Records",
        "does not derive probability semantics",
        "does not select event order, rate, or the no-record channel",
        "does not establish that the axioms require amendment",
    )
    for index, marker in enumerate(markers, 2):
        check(f"S{index:02d}", marker in text, f"source contains boundary marker: {marker}")


def main() -> int:
    classification_checks()
    autonomous_hostile_checks()
    covariance_and_dilation_checks()
    source_checks()
    print("BOUNDARY: finite Kraus representation is named mathematical authority; physical CP-instrument applicability, the supplied menu, probability semantics, cross-label exclusion, and event neutrality remain conditional/open and gain no chain-satisfying premise authority.")
    print("BOUNDARY: auxiliary locked-register absorption and same-map reuse do not imply blank-sector cross-label exclusion.")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
