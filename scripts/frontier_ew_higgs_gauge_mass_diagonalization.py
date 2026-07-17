#!/usr/bin/env python3
"""Exact evidence for the defined C2 quadratic-form theorem.

The stable filename is historical.  This runner constructs the theorem's
finite-dimensional objects directly and does not read audit state, source-note
prose, network resources, external data, or physical inputs.
"""

from __future__ import annotations

import argparse
import ast
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

import sympy as sp


SOURCE = Path(__file__).resolve()


@dataclass
class Audit:
    passed: int = 0
    failed: int = 0

    def check(self, label: str, condition: object, detail: str = "") -> None:
        if bool(condition):
            self.passed += 1
            print(f"PASS: {label}" + (f" :: {detail}" if detail else ""))
        else:
            self.failed += 1
            print(f"FAIL: {label}" + (f" :: {detail}" if detail else ""))


@dataclass(frozen=True)
class Algebra:
    g: sp.Symbol
    gy: sp.Symbol
    v: sp.Symbol
    w1: sp.Symbol
    w2: sp.Symbol
    w3: sp.Symbol
    b: sp.Symbol
    t1: sp.Matrix
    t2: sp.Matrix
    t3: sp.Matrix
    y: sp.Matrix
    h0: sp.Matrix
    lvec: sp.Matrix
    q: sp.Expr
    full_matrix: sp.Matrix
    neutral_matrix: sp.Matrix


Residual = sp.Expr | sp.Matrix


def banner(title: str) -> None:
    print()
    print(f"=== {title} ===")


def is_zero(expr: sp.Expr) -> bool:
    return sp.simplify(sp.expand(expr)) == 0


def matrix_is_zero(matrix: sp.Matrix) -> bool:
    return all(is_zero(entry) for entry in matrix)


def residual_is_zero(residual: Residual) -> bool:
    if isinstance(residual, sp.MatrixBase):
        return matrix_is_zero(sp.Matrix(residual))
    return is_zero(residual)


def render_residual(residual: Residual) -> str:
    if isinstance(residual, sp.MatrixBase):
        return str(sp.simplify(residual))
    return str(sp.factor(residual))


def hermitian_norm_squared(vector: sp.Matrix) -> sp.Expr:
    return sp.simplify((sp.conjugate(vector).T * vector)[0])


def construct() -> Algebra:
    g, gy, v = sp.symbols("g gY v", positive=True, real=True)
    w1, w2, w3, b = sp.symbols("W1 W2 W3 B", real=True)

    sigma1 = sp.Matrix([[0, 1], [1, 0]])
    sigma2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    sigma3 = sp.Matrix([[1, 0], [0, -1]])
    t1, t2, t3 = sigma1 / 2, sigma2 / 2, sigma3 / 2
    y = sp.eye(2) / 2
    h0 = sp.Matrix([0, v / sp.sqrt(2)])

    operator = g * (w1 * t1 + w2 * t2 + w3 * t3) + gy * b * y
    lvec = sp.simplify(-sp.I * operator * h0)
    q = hermitian_norm_squared(lvec)
    variables = sp.Matrix([w1, w2, w3, b])
    full_matrix = sp.hessian(q, tuple(variables))
    neutral_matrix = full_matrix.extract([2, 3], [2, 3])

    return Algebra(
        g=g,
        gy=gy,
        v=v,
        w1=w1,
        w2=w2,
        w3=w3,
        b=b,
        t1=t1,
        t2=t2,
        t3=t3,
        y=y,
        h0=h0,
        lvec=lvec,
        q=q,
        full_matrix=full_matrix,
        neutral_matrix=neutral_matrix,
    )


def expected_full_matrix(a: Algebra) -> sp.Matrix:
    g, gy, v = a.g, a.gy, a.v
    return v**2 / 4 * sp.Matrix(
        [
            [g**2, 0, 0, 0],
            [0, g**2, 0, 0],
            [0, 0, g**2, -g * gy],
            [0, 0, -g * gy, gy**2],
        ]
    )


def audit_source_firewall(audit: Audit) -> None:
    """Check only hazards that could substitute metadata for mathematics."""

    banner("Executable-evidence firewall")
    tree = ast.parse(SOURCE.read_text(encoding="utf-8"), filename=str(SOURCE))
    imports = {
        alias.name.split(".")[0]
        for node in ast.walk(tree)
        if isinstance(node, (ast.Import, ast.ImportFrom))
        for alias in node.names
    }
    literal_true_checks = []
    forbidden_calls = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = ""
            if isinstance(node.func, ast.Name):
                name = node.func.id
            elif isinstance(node.func, ast.Attribute):
                name = node.func.attr
            if name == "check" and len(node.args) >= 2:
                condition = node.args[1]
                if isinstance(condition, ast.Constant) and condition.value is True:
                    literal_true_checks.append(node.lineno)
            if name in {"eval", "exec"}:
                forbidden_calls.append((name, node.lineno))

    audit.check(
        "no network or external-data imports",
        imports.isdisjoint({"requests", "urllib", "http", "socket", "pandas"}),
        f"imports={sorted(imports)}",
    )
    audit.check(
        "no literal-True evidence checks",
        len(literal_true_checks) == 0,
        f"lines={literal_true_checks}",
    )
    audit.check(
        "no dynamic eval or exec",
        len(forbidden_calls) == 0,
        f"calls={forbidden_calls}",
    )


def audit_normal(audit: Audit, a: Algebra) -> None:
    g, gy, v = a.g, a.gy, a.v
    w1, w2, w3, b = a.w1, a.w2, a.w3, a.b
    root2 = sp.sqrt(2)

    banner("Defined matrix actions and linear map")
    action_targets = (
        ("T1 h0", a.t1 * a.h0, sp.Matrix([v / (2 * root2), 0])),
        ("T2 h0", a.t2 * a.h0, sp.Matrix([-sp.I * v / (2 * root2), 0])),
        ("T3 h0", a.t3 * a.h0, sp.Matrix([0, -v / (2 * root2)])),
        ("Y h0", a.y * a.h0, sp.Matrix([0, v / (2 * root2)])),
    )
    for label, actual, expected in action_targets:
        audit.check(label, matrix_is_zero(actual - expected), str(actual))

    expected_l = -sp.I * v / (2 * root2) * sp.Matrix(
        [g * (w1 - sp.I * w2), -g * w3 + gy * b]
    )
    audit.check("full L coordinate vector", matrix_is_zero(a.lvec - expected_l), str(a.lvec))
    audit.check("L is real-linear in four coefficients", all(sp.diff(a.lvec, x, 2) == sp.zeros(2, 1) for x in (w1, w2, w3, b)))

    expected_q = v**2 / 8 * (g**2 * (w1**2 + w2**2) + (g * w3 - gy * b) ** 2)
    audit.check("full Hermitian-norm quadratic form", is_zero(a.q - expected_q), str(sp.factor(a.q)))

    banner("Full Gram matrix and charged block")
    expected_m = expected_full_matrix(a)
    audit.check("Hessian constructs the unique symmetric matrix M", matrix_is_zero(a.full_matrix - expected_m), str(a.full_matrix))
    audit.check("M is symmetric", matrix_is_zero(a.full_matrix - a.full_matrix.T))
    x = sp.Matrix([w1, w2, w3, b])
    audit.check("Q reconstructs as one-half x^T M x", is_zero(a.q - (x.T * a.full_matrix * x)[0] / 2))
    charged = a.full_matrix.extract([0, 1], [0, 1])
    mw2 = g**2 * v**2 / 4
    audit.check("charged block has two equal directions", matrix_is_zero(charged - mw2 * sp.eye(2)), str(charged))
    wplus = (w1 - sp.I * w2) / root2
    wminus = (w1 + sp.I * w2) / root2
    audit.check("charged basis product identity", is_zero(wplus * wminus - (w1**2 + w2**2) / 2))
    q_charged = g**2 * v**2 * (w1**2 + w2**2) / 8
    audit.check("charged Q coefficient after basis rotation", is_zero(q_charged - mw2 * wplus * wminus))

    banner("Neutral rank-one matrix")
    m0 = a.neutral_matrix
    expected_m0 = v**2 / 4 * sp.Matrix([[g**2, -g * gy], [-g * gy, gy**2]])
    for row in range(2):
        for col in range(2):
            audit.check(
                f"neutral entry ({row},{col})",
                is_zero(m0[row, col] - expected_m0[row, col]),
                str(m0[row, col]),
            )
    mz2 = (g**2 + gy**2) * v**2 / 4
    lam = sp.symbols("lambda")
    audit.check("neutral determinant", is_zero(m0.det()), str(sp.factor(m0.det())))
    audit.check("neutral rank", m0.rank() == 1, str(m0.rank()))
    audit.check("neutral trace", is_zero(sp.trace(m0) - mz2), str(sp.trace(m0)))
    audit.check(
        "neutral characteristic polynomial",
        is_zero(m0.charpoly(lam).as_expr() - lam * (lam - mz2)),
        str(sp.factor(m0.charpoly(lam).as_expr())),
    )
    kernel = sp.Matrix([gy, g])
    eigen = sp.Matrix([g, -gy])
    audit.check("neutral kernel vector", matrix_is_zero(m0 * kernel))
    audit.check("neutral nonzero eigenvector", matrix_is_zero(m0 * eigen - mz2 * eigen))
    audit.check("neutral kernel is one-dimensional", len(m0.nullspace()) == 1)
    audit.check("neutral range is one-dimensional", len(m0.columnspace()) == 1)
    audit.check("neutral eigenvectors are orthogonal", is_zero((kernel.T * eigen)[0]))

    banner("Normalized orthogonal rotation and scalar readouts")
    total = sp.sqrt(g**2 + gy**2)
    c, s = g / total, gy / total
    rotation = sp.Matrix([[c, -s], [s, c]])
    audit.check("rotation is orthogonal", matrix_is_zero(rotation * rotation.T - sp.eye(2)))
    audit.check("rotation determinant is one", is_zero(rotation.det() - 1))
    audit.check("rotation diagonalizes M0", matrix_is_zero(rotation * m0 * rotation.T - sp.diag(mz2, 0)))
    z, photon_label = sp.symbols("Z A", real=True)
    neutral_old = rotation.T * sp.Matrix([z, photon_label])
    q_neutral = (sp.Matrix([w3, b]).T * m0 * sp.Matrix([w3, b]))[0] / 2
    q_rotated = sp.expand(q_neutral.subs({w3: neutral_old[0], b: neutral_old[1]}, simultaneous=True))
    audit.check("rotation reconstructs neutral Q", is_zero(q_rotated - mz2 * z**2 / 2), str(sp.factor(q_rotated)))

    ma2 = sp.Integer(0)
    e = g * gy / total
    rho = sp.simplify(mw2 / (mz2 * c**2))
    audit.check("c squared plus s squared", is_zero(c**2 + s**2 - 1))
    audit.check("formal MA2 label", is_zero(ma2))
    audit.check("formal e equals g times s", is_zero(e - g * s))
    audit.check("formal e equals gY times c", is_zero(e - gy * c))
    audit.check("inverse-e identity", is_zero(1 / e**2 - 1 / g**2 - 1 / gy**2))
    audit.check("formal rho identity", is_zero(rho - 1), str(rho))

    banner("Full annihilator classification")
    alpha, beta = sp.symbols("alpha beta")
    annihilator_action = sp.simplify((alpha * a.t3 + beta * a.y) * a.h0)
    target_action = v / (2 * root2) * sp.Matrix([0, beta - alpha])
    audit.check("generic annihilator action", matrix_is_zero(annihilator_action - target_action), str(annihilator_action))
    coefficient = sp.Matrix.hstack(a.t3 * a.h0, a.y * a.h0)
    nullspace = coefficient.nullspace()
    audit.check("annihilator coefficient rank", coefficient.rank() == 1, str(coefficient.rank()))
    audit.check("annihilator is one-dimensional", len(nullspace) == 1, str(nullspace))
    audit.check("T3 plus Y kills h0", matrix_is_zero((a.t3 + a.y) * a.h0))
    audit.check(
        "annihilator basis has equal coefficients",
        len(nullspace) == 1 and is_zero(nullspace[0][0] - nullspace[0][1]),
        str(nullspace),
    )


def audit_independent(audit: Audit, a: Algebra) -> None:
    """Rebuild the result from coordinate columns and solved subspaces."""

    banner("Independent coordinate-Gram construction")
    variables = sp.Matrix([a.w1, a.w2, a.w3, a.b])
    coordinate_columns = a.lvec.jacobian(variables)
    complex_gram = sp.conjugate(coordinate_columns).T * coordinate_columns
    coordinate_matrix = 2 * complex_gram.applyfunc(lambda entry: sp.simplify(sp.re(entry)))
    coordinate_matrix = coordinate_matrix.applyfunc(sp.simplify)
    audit.check("coordinate columns are constant", all(not entry.has(*variables) for entry in coordinate_columns))
    audit.check("coordinate Gram is real", all(sp.im(entry).simplify() == 0 for entry in coordinate_matrix))
    audit.check("coordinate Gram independently reproduces M", matrix_is_zero(coordinate_matrix - a.full_matrix), str(coordinate_matrix))
    reconstructed = (variables.T * coordinate_matrix * variables)[0] / 2
    audit.check("coordinate Gram independently reconstructs Q", is_zero(reconstructed - a.q), str(sp.factor(reconstructed)))

    banner("Independent solved neutral subspaces")
    solved_m0 = coordinate_matrix.extract([2, 3], [2, 3])
    nullspace = solved_m0.nullspace()
    columnspace = solved_m0.columnspace()
    audit.check("solver finds one null direction", len(nullspace) == 1, str(nullspace))
    audit.check("solver finds one range direction", len(columnspace) == 1, str(columnspace))
    null = nullspace[0]
    image = columnspace[0]
    audit.check("solved directions are orthogonal", is_zero((null.T * image)[0]))
    null_unit = sp.simplify(null / sp.sqrt((null.T * null)[0]))
    image_unit = sp.simplify(image / sp.sqrt((image.T * image)[0]))
    solved_rotation = sp.Matrix.vstack(image_unit.T, null_unit.T)
    audit.check("solver-derived rows are normalized", matrix_is_zero(solved_rotation * solved_rotation.T - sp.eye(2)), str(solved_rotation))
    solved_diagonal = sp.simplify(solved_rotation * solved_m0 * solved_rotation.T)
    audit.check("solver-derived rotation is diagonal", is_zero(solved_diagonal[0, 1]) and is_zero(solved_diagonal[1, 0]), str(solved_diagonal))
    audit.check("solver-derived null eigenvalue", is_zero(solved_diagonal[1, 1]))
    audit.check("solver-derived nonzero eigenvalue equals trace", is_zero(solved_diagonal[0, 0] - sp.trace(solved_m0)))
    neutral_variables = sp.Matrix([a.w3, a.b])
    solved_coordinates = solved_rotation * neutral_variables
    reconstruction = solved_coordinates[0] ** 2 * solved_diagonal[0, 0] / 2
    original_neutral_q = (neutral_variables.T * solved_m0 * neutral_variables)[0] / 2
    audit.check("solved eigenspaces independently reconstruct neutral Q", is_zero(reconstruction - original_neutral_q))

    banner("Independent annihilator solve")
    action_columns = sp.Matrix.hstack(a.t3 * a.h0, a.y * a.h0)
    solved_annihilator = action_columns.nullspace()
    audit.check("generic coefficient solve has nullity one", len(solved_annihilator) == 1, str(solved_annihilator))
    basis = solved_annihilator[0]
    audit.check("solved annihilator acts as zero", matrix_is_zero(action_columns * basis))
    audit.check("no second annihilator direction", action_columns.rank() == 1)


def hostile_residuals(a: Algebra) -> list[tuple[str, Residual]]:
    """Return propagated residuals for concrete installed mutations."""

    g, gy, v = a.g, a.gy, a.v
    w1, w2, w3, b = a.w1, a.w2, a.w3, a.b
    operator_base = g * (w1 * a.t1 + w2 * a.t2 + w3 * a.t3)

    wrong_y = -sp.eye(2) / 2
    wrong_y_l = -sp.I * (operator_base + gy * b * wrong_y) * a.h0
    wrong_y_q = hermitian_norm_squared(wrong_y_l)

    wrong_h0 = sp.Matrix([v / sp.sqrt(2), 0])
    wrong_carrier_l = -sp.I * (operator_base + gy * b * a.y) * wrong_h0
    wrong_carrier_q = hermitian_norm_squared(wrong_carrier_l)

    missing_cross_q = v**2 / 8 * (
        g**2 * (w1**2 + w2**2 + w3**2) + gy**2 * b**2
    )
    wrong_charged_q = a.q + g**2 * v**2 * (w1**2 + w2**2) / 8

    total = sp.sqrt(g**2 + gy**2)
    c, s = g / total, gy / total
    mz2 = (g**2 + gy**2) * v**2 / 4
    wrong_rotation = sp.Matrix([[c, s], [-s, c]])
    swapped_rotation = sp.Matrix([[s, c], [c, -s]])
    expected_diagonal = sp.diag(mz2, 0)

    rank_two_matrix = a.neutral_matrix + v**2 / 4 * sp.Matrix([[0, 0], [0, 1]])
    wrong_annihilator = (a.t3 - a.y) * a.h0

    return [
        ("wrong Y sign changes the full quadratic form", sp.expand(wrong_y_q - a.q)),
        ("upper carrier vector changes the full quadratic form", sp.expand(wrong_carrier_q - a.q)),
        ("missing neutral cross term changes Q", sp.expand(missing_cross_q - a.q)),
        ("wrong charged normalization changes Q", sp.expand(wrong_charged_q - a.q)),
        ("incorrect-sign rotation fails diagonalization", sp.simplify(wrong_rotation * a.neutral_matrix * wrong_rotation.T - expected_diagonal)),
        ("swapped rotation fails the claimed eigenvalue order", sp.simplify(swapped_rotation * a.neutral_matrix * swapped_rotation.T - expected_diagonal)),
        ("rank-two perturbation destroys zero determinant", sp.factor(rank_two_matrix.det())),
        ("T3 minus Y fails to annihilate h0", sp.simplify(wrong_annihilator)),
    ]


def audit_hostile(audit: Audit, a: Algebra) -> None:
    banner("Hostile mutation rejection")
    for label, residual in hostile_residuals(a):
        audit.check(label, not residual_is_zero(residual), render_residual(residual))


def audit_intentional_failure(audit: Audit, a: Algebra) -> None:
    banner("Promoted hostile claims (expected failures)")
    for label, residual in hostile_residuals(a):
        audit.check(
            f"promoted claim: {label}",
            residual_is_zero(residual),
            f"nonzero residual={render_residual(residual)}",
        )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Exact verifier for the defined C2 quadratic-form theorem."
    )
    parser.add_argument(
        "--mode",
        choices=("normal", "independent", "hostile", "intentional-failure"),
        default="normal",
        help="evidence route (default: normal)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    audit = Audit()
    algebra = construct()
    routes: dict[str, Callable[[Audit, Algebra], None]] = {
        "normal": audit_normal,
        "independent": audit_independent,
        "hostile": audit_hostile,
        "intentional-failure": audit_intentional_failure,
    }

    print("=== Defined C2 quadratic-form diagonalization verifier ===")
    print(f"MODE: {args.mode}")
    if args.mode != "intentional-failure":
        audit_source_firewall(audit)
    routes[args.mode](audit, algebra)

    print()
    print(f"TOTAL: PASS={audit.passed}, FAIL={audit.failed}")
    if audit.failed:
        print("VERDICT: FAIL")
        return 1
    print("VERDICT: FORMAL_THEOREM_VERIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
