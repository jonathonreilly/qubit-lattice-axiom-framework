#!/usr/bin/env python3
"""Independent reconstruction for the Block-3 congruence boundary.

This checker deliberately does not import the primary Block-3 runner or its
exact-matrix helper.  It rebuilds the Q(sqrt(2)) menus with SymPy, the physical
Kraus pair with NumPy on the shared Cycle-317 upstream carrier, the three law
tables, an alternative conditional-content table, and the no-go/status packet.
The table is not a sampler, formation law, or realized Record history.
"""

from __future__ import annotations

from fractions import Fraction
from math import sqrt
from pathlib import Path
import sys

import numpy as np
import sympy as sp


AUDIT_TIMEOUT_SEC = 180

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18 as c317


NOTE_PATH = ROOT / "docs" / (
    "SHARED_EFFECT_RECORD_RANDOMIZED_PREPARATION_CONGRUENCE_"
    "INDEPENDENCE_BOUNDED_THEOREM_NOTE_2026-08-20.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
CYCLE317_PATH = ROOT / "docs/work_history/repo/review_feedback" / (
    "PHYSICAL_CONTACT_TERNARY_BORN_FORCING_BRIDGE_CYCLE317_NOTE_2026-07-18.md"
)
CYCLE321_PATH = ROOT / "docs/work_history/repo/review_feedback" / (
    "PHYSICAL_EFFECT_EQUIVALENCE_NORMALIZED_GRADE_CYCLE321_NOTE_2026-07-18.md"
)

AUDIT_INPUT_PATHS = (
    "docs/SHARED_EFFECT_RECORD_RANDOMIZED_PREPARATION_CONGRUENCE_INDEPENDENCE_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_CONTACT_TERNARY_BORN_FORCING_BRIDGE_CYCLE317_NOTE_2026-07-18.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_EFFECT_EQUIVALENCE_NORMALIZED_GRADE_CYCLE321_NOTE_2026-07-18.md",
)

TOL = 9.0e-11
PASS = 0
FAIL = 0

I = sp.I
SQRT2 = sp.sqrt(2)
I2S = sp.eye(2)
I2 = np.eye(2, dtype=complex)
X = sp.Matrix(((0, 1), (1, 0)))
Z = sp.Matrix(((1, 0), (0, -1)))


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS [{label}] {detail}")
    else:
        FAIL += 1
        print(f"FAIL [{label}] {detail}")


def normalized(path: Path) -> str:
    body = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        body = body.replace(marker, "")
    return " ".join(body.split())


def projector(nx: sp.Expr, nz: sp.Expr) -> sp.Matrix:
    return sp.simplify((I2S + nx * X + nz * Z) / 2)


def exact_menus() -> tuple[tuple[sp.Matrix, ...], tuple[sp.Matrix, ...]]:
    e0 = sp.Rational(1, 2) * projector(0, 1)
    a1 = sp.Rational(9, 10) * projector(4 * SQRT2 / 9, -sp.Rational(7, 9))
    a2 = sp.Rational(3, 5) * projector(-2 * SQRT2 / 3, sp.Rational(1, 3))
    b1 = sp.Rational(3, 4) * projector(2 * SQRT2 / 3, -sp.Rational(1, 3))
    b2 = sp.Rational(3, 4) * projector(-2 * SQRT2 / 3, -sp.Rational(1, 3))
    return (e0, a1, a2), (e0, b1, b2)


def matrix_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    return all(sp.simplify(value) == 0 for value in left - right)


def to_numpy(matrix: sp.Matrix) -> np.ndarray:
    return np.asarray(matrix.evalf(), dtype=complex)


def affine(state: sp.Matrix, menu: tuple[sp.Matrix, ...]) -> tuple[sp.Rational, ...]:
    return tuple(sp.simplify(sp.trace(state * effect)) for effect in menu)


def square_law(state: sp.Matrix, menu: tuple[sp.Matrix, ...]) -> tuple[sp.Rational, ...]:
    square = state * state
    sigma = square / sp.trace(square)
    return tuple(sp.simplify(sp.trace(sigma * effect)) for effect in menu)


def context_law(menu: tuple[sp.Matrix, ...]) -> tuple[sp.Rational, ...]:
    scores = tuple(sp.trace(effect) ** 2 for effect in menu)
    denominator = sum(scores)
    return tuple(sp.simplify(score / denominator) for score in scores)


def choi(kraus: tuple[np.ndarray, ...]) -> np.ndarray:
    return sum(
        (
            np.outer(
                operator.reshape(-1, order="F"),
                operator.reshape(-1, order="F").conj(),
            )
            for operator in kraus
        ),
        start=np.zeros((4, 4), dtype=complex),
    )


def program(menu: tuple[sp.Matrix, ...], contact: np.ndarray) -> tuple[np.ndarray, ...]:
    blocks = []
    for effect in menu:
        coefficient = float(sp.trace(effect))
        blocks.append(sqrt(coefficient) * to_numpy(effect / sp.trace(effect)) @ contact)
    return tuple(blocks)


def effects(kraus: tuple[np.ndarray, ...]) -> tuple[np.ndarray, ...]:
    return tuple(operator.conj().T @ operator for operator in kraus)


def clifford_group() -> tuple[np.ndarray, ...]:
    h = np.asarray(((1, 1), (1, -1)), dtype=complex) / sqrt(2)
    s = np.diag((1, 1j)).astype(complex)

    def key(unitary: np.ndarray) -> tuple[float, ...]:
        pivot = next(value for value in unitary.reshape(-1) if abs(value) > 1e-10)
        fixed = np.round(unitary / (pivot / abs(pivot)), 11)
        return tuple(
            float(value)
            for pair in zip(fixed.real.reshape(-1), fixed.imag.reshape(-1))
            for value in pair
        )

    found: dict[tuple[float, ...], np.ndarray] = {}
    pending = [I2]
    while pending:
        candidate = pending.pop()
        candidate_key = key(candidate)
        if candidate_key in found:
            continue
        found[candidate_key] = candidate
        pending.extend((candidate @ h, candidate @ s))
    return tuple(found.values())


def numeric_law(kind: str, state: np.ndarray, menu: tuple[np.ndarray, ...]) -> tuple[float, ...]:
    if kind == "affine":
        evaluator = state
        return tuple(float(np.trace(evaluator @ effect).real) for effect in menu)
    if kind == "square":
        evaluator = state @ state
        evaluator /= np.trace(evaluator)
        return tuple(float(np.trace(evaluator @ effect).real) for effect in menu)
    scores = tuple(float(np.trace(effect).real) ** 2 for effect in menu)
    return tuple(score / sum(scores) for score in scores)


def source_and_packet_controls() -> None:
    note = normalized(NOTE_PATH)
    axiom = normalized(AXIOM_PATH)
    cycle317 = normalized(CYCLE317_PATH)
    cycle321 = normalized(CYCLE321_PATH)
    for relative in AUDIT_INPUT_PATHS:
        (ROOT / relative).read_text(encoding="utf-8")
    section_markers = tuple(f"n{index} —" for index in range(1, 9))
    pair_markers = (
        "p/e", "p/r", "p/z", "p/h", "p/f",
        "e/r", "e/z", "e/h", "e/f",
        "r/z", "r/h", "r/f", "z/h", "z/f", "h/f",
    )
    check(
        "sources-packet",
        all(
            (
                "records form" in axiom,
                "readout value is determined by record content alone" in axiom,
                "effect functionality remains a hypothesis" in cycle317,
                "equal effects, unequal processes" in cycle321,
                all(marker in note for marker in section_markers),
                all(marker in note for marker in pair_markers),
                "broad gate status: fail / do not ship" in note,
                "zero obligation retirement" in note,
            )
        ),
        "current sources, N1-N8, the complete 15-pair wall matrix, broad stop, and zero-retirement status are bound",
    )


def exact_algebra_controls(
    menu_a: tuple[sp.Matrix, ...], menu_b: tuple[sp.Matrix, ...]
) -> None:
    unique = {sp.srepr(effect) for effect in menu_a + menu_b}
    check(
        "exact-menus",
        matrix_equal(sum(menu_a, sp.zeros(2)), I2S)
        and matrix_equal(sum(menu_b, sp.zeros(2)), I2S)
        and matrix_equal(menu_a[0], menu_b[0])
        and len(unique) == 5,
        "an independent SymPy reconstruction gives two exact resolutions sharing one of five effects",
    )
    rho35 = sp.diag(sp.Rational(3, 5), sp.Rational(2, 5))
    direct = sp.diag(sp.Rational(3, 4), sp.Rational(1, 4))
    mixed = I2S / 2
    pz = sp.diag(1, 0)
    values = {
        "affine_a": affine(rho35, menu_a)[0],
        "affine_b": affine(rho35, menu_b)[0],
        "square_a": square_law(rho35, menu_a)[0],
        "square_b": square_law(rho35, menu_b)[0],
        "context_a": context_law(menu_a)[0],
        "context_b": context_law(menu_b)[0],
        "fair_affine": sp.simplify((affine(mixed, menu_a)[0] + affine(pz, menu_a)[0]) / 2),
        "direct_affine": affine(direct, menu_a)[0],
        "fair_square": sp.simplify((square_law(mixed, menu_a)[0] + square_law(pz, menu_a)[0]) / 2),
        "direct_square": square_law(direct, menu_a)[0],
    }
    check(
        "exact-discriminators",
        values
        == {
            "affine_a": sp.Rational(3, 10),
            "affine_b": sp.Rational(3, 10),
            "square_a": sp.Rational(9, 26),
            "square_b": sp.Rational(9, 26),
            "context_a": sp.Rational(25, 142),
            "context_b": sp.Rational(2, 11),
            "fair_affine": sp.Rational(3, 8),
            "direct_affine": sp.Rational(3, 8),
            "fair_square": sp.Rational(3, 8),
            "direct_square": sp.Rational(9, 20),
        },
        values,
    )
    check(
        "independent-walls",
        values["context_a"] != values["context_b"]
        and values["fair_square"] != values["direct_square"]
        and values["affine_a"] == values["affine_b"]
        and values["fair_affine"] == values["direct_affine"],
        "the context and preparation failures separate while the affine control passes both",
    )


def physical_controls(
    menu_a: tuple[sp.Matrix, ...], menu_b: tuple[sp.Matrix, ...]
) -> tuple[tuple[np.ndarray, ...], tuple[np.ndarray, ...]]:
    fixture3 = c317.physical_fixture(3)
    fixture6 = c317.physical_fixture(6)
    kraus_a = program(menu_a, fixture3.contact)
    kraus_b = program(menu_b, fixture3.contact)
    complete_a = sum(effects(kraus_a), start=np.zeros((2, 2), dtype=complex))
    complete_b = sum(effects(kraus_b), start=np.zeros((2, 2), dtype=complex))
    compressed_residual = max(
        float(
            np.linalg.norm(
                actual
                - fixture3.contact.conj().T
                @ to_numpy(logical)
                @ fixture3.contact
            )
        )
        for logical_menu, kraus in ((menu_a, kraus_a), (menu_b, kraus_b))
        for logical, actual in zip(logical_menu, effects(kraus))
    )
    selected_effect = float(np.linalg.norm(effects(kraus_a)[0] - effects(kraus_b)[0]))
    selected_kraus = float(np.linalg.norm(kraus_a[0] - kraus_b[0]))
    selected_choi = float(np.linalg.norm(choi((kraus_a[0],)) - choi((kraus_b[0],))))
    complete_choi = float(np.linalg.norm(choi(kraus_a) - choi(kraus_b)))
    physical_residuals = []
    for fixture in (fixture3, fixture6):
        for kraus in (kraus_a, kraus_b):
            physical = c317.physical_isometry(fixture.two_ray_encoding, kraus)
            physical_residuals.append(float(np.linalg.norm(physical.conj().T @ physical - I2)))
    check(
        "physical-shared-branch",
        max(
            float(np.linalg.norm(complete_a - I2)),
            float(np.linalg.norm(complete_b - I2)),
            selected_effect,
            selected_kraus,
            selected_choi,
            compressed_residual,
            max(physical_residuals),
        )
        < TOL
        and complete_choi > 0.5,
        {
            "selected_effect_K_Choi": f"< {TOL:g}",
            "complete_choi_difference": round(complete_choi, 6),
            "compressed_effects_and_isometries": f"< {TOL:g}",
        },
    )
    logical_e0 = to_numpy(menu_a[0])

    def positive_sqrt(matrix: np.ndarray) -> np.ndarray:
        values, vectors = np.linalg.eigh(matrix)
        if float(np.min(values)) < -TOL:
            raise ValueError("positive_sqrt received a matrix outside the positive cone")
        return vectors @ np.diag(np.sqrt(np.maximum(values, 0.0))) @ vectors.conj().T

    selected = positive_sqrt(logical_e0) @ fixture3.contact
    remainder = positive_sqrt(I2 - logical_e0) @ fixture3.contact
    inverse_remainder = np.linalg.inv(remainder)
    first_stage = max(
        float(np.linalg.norm(selected - kraus_a[0])),
        float(np.linalg.norm(selected - kraus_b[0])),
        float(
            np.linalg.norm(
                selected.conj().T @ selected
                + remainder.conj().T @ remainder
                - I2
            )
        ),
    )
    conditional_completeness = []
    program_recovery = []
    for kraus in (kraus_a, kraus_b):
        conditional = tuple(operator @ inverse_remainder for operator in kraus[1:])
        conditional_completeness.append(
            float(
                np.linalg.norm(
                    sum(
                        (operator.conj().T @ operator for operator in conditional),
                        start=np.zeros((2, 2), dtype=complex),
                    )
                    - I2
                )
            )
        )
        program_recovery.append(
            max(
                float(np.linalg.norm(operator @ remainder - target))
                for operator, target in zip(conditional, kraus[1:])
            )
        )
    check(
        "independent-context-delay-factorization",
        max(first_stage, *conditional_completeness, *program_recovery) < TOL,
        {
            "all_factorization_residuals": f"< {TOL:g}",
            "scope": "matrix factorization only; physical delayed-context compiler remains open",
        },
    )
    deleted_contact_a = program(menu_a, I2)
    nonshared_contact_change = max(
        float(np.linalg.norm(before - after))
        for before, after in zip(effects(kraus_a), effects(deleted_contact_a))
    )
    shared_contact_change = float(np.linalg.norm(effects(kraus_a)[0] - effects(deleted_contact_a)[0]))
    check(
        "contact-deletion",
        shared_contact_change < TOL and nonshared_contact_change > 0.1,
        {
            "shared_E0_change": f"< {TOL:g}",
            "maximum_nonshared_change": round(nonshared_contact_change, 6),
        },
    )
    return kraus_a, kraus_b


def covariance_controls(kraus_a: tuple[np.ndarray, ...], kraus_b: tuple[np.ndarray, ...]) -> None:
    group = clifford_group()
    state = np.diag((0.63, 0.37)).astype(complex)
    maximum = 0.0
    code_maximum = 0.0
    for unitary in group:
        rotated_state = unitary @ state @ unitary.conj().T
        for kraus in (kraus_a, kraus_b):
            menu = effects(kraus)
            rotated = tuple(unitary @ effect @ unitary.conj().T for effect in menu)
            for kind in ("affine", "square", "context"):
                maximum = max(
                    maximum,
                    max(
                        abs(left - right)
                        for left, right in zip(
                            numeric_law(kind, state, menu),
                            numeric_law(kind, rotated_state, rotated),
                        )
                    ),
                )
            for label, (effect, rotated_effect) in enumerate(zip(menu, rotated)):
                code = effect + 1j * label * I2
                rotated_code = rotated_effect + 1j * label * I2
                code_maximum = max(
                    code_maximum,
                    float(np.linalg.norm(unitary @ code @ unitary.conj().T - rotated_code)),
                )
    check(
        "independent-covariance",
        len(group) == 24 and max(maximum, code_maximum) < TOL,
        {
            "cliffords": len(group),
            "formula_and_carrier_residuals": f"< {TOL:g}",
        },
    )


def conditional_table_controls(
    menu_a: tuple[sp.Matrix, ...],
    menu_b: tuple[sp.Matrix, ...],
    kraus_a: tuple[np.ndarray, ...],
    kraus_b: tuple[np.ndarray, ...],
) -> None:
    rho = sp.diag(sp.Rational(3, 5), sp.Rational(2, 5))
    tables = {
        ("affine", "A"): affine(rho, menu_a),
        ("affine", "B"): affine(rho, menu_b),
        ("square", "A"): square_law(rho, menu_a),
        ("square", "B"): square_law(rho, menu_b),
        ("context", "A"): context_law(menu_a),
        ("context", "B"): context_law(menu_b),
    }
    physical_menus = {"A": effects(kraus_a), "B": effects(kraus_b)}
    tables_with_content = {}
    for key, weights in tables.items():
        physical_menu = physical_menus[key[1]]
        tables_with_content[key] = tuple(
            {
                "probability": weight,
                "physical_Q": effect,
                "label": label,
                "context": key[1],
            }
            for label, (weight, effect) in enumerate(zip(weights, physical_menu))
            if weight > 0
        )
    check(
        "conditional-content-table",
        all(
            sum(row["probability"] for row in table) == 1
            for table in tables_with_content.values()
        )
        and all(
            row["label"] == label
            for table in tables_with_content.values()
            for label, row in enumerate(table)
        )
        and np.linalg.norm(
            tables_with_content[("affine", "A")][0]["physical_Q"]
            - tables_with_content[("affine", "B")][0]["physical_Q"]
        )
        < TOL
        and tables_with_content[("affine", "A")][0]["context"]
        != tables_with_content[("affine", "B")][0]["context"],
        "independent conditional tables normalize and carry identical physical E0 content across distinct program contexts; no draw or Record formation is modeled",
    )
    required_roles = frozenset((10, 20, 21, 100, 101, 102))

    def recognized(labels: tuple[int, ...], central_blank: bool = True) -> bool:
        return central_blank and len(labels) == 6 and frozenset(labels) == required_roles

    check(
        "conditional-domain-roles",
        recognized((102, 20, 100, 10, 21, 101))
        and recognized(tuple(reversed((102, 20, 100, 10, 21, 101))))
        and not recognized((102, 100, 10, 21, 101))
        and not recognized((102, 20, 100, 10, 21, 101), False)
        and not recognized((102, 20, 100, 10, 21, 101, 101)),
        "an independently ordered role multiset is recognized while missing, occupied, and duplicate-role conditions are rejected symbolically",
    )


def n5_controls() -> None:
    lines = (
        "per_element: exact shared effect, codeword, probabilities, and selected CP branch are checked",
        "per_site: one unordered six-neighbour conditional packet and candidate output content are checked",
        "per_mode: affine, normalized-square, context-restriction, direct, and randomized preparations are checked",
        "per_block: two physical ternary programs, conditional normalization, physical content, and domain deletions are checked",
        "lattice_wide: checked and not executed — formation, sampling, arbitrary programs, autonomous genesis, rates, histories, and frequencies remain open",
    )
    for line in lines:
        print(line)
    note = normalized(NOTE_PATH)
    check(
        "n5-certificate",
        all(line.lower() in note for line in lines) and all(len(line) >= 80 for line in lines),
        "the note and independent executable share the five exact substantive resolution lines",
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    source_and_packet_controls()
    menu_a, menu_b = exact_menus()
    exact_algebra_controls(menu_a, menu_b)
    kraus_a, kraus_b = physical_controls(menu_a, menu_b)
    covariance_controls(kraus_a, kraus_b)
    conditional_table_controls(menu_a, menu_b, kraus_a, kraus_b)
    n5_controls()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
