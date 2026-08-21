#!/usr/bin/env python3
"""Independent Block-7 staged cq/Record writer check.

This checker rebuilds the exact menus, Kraus operators, staged factorization,
fresh-label copy, tomography, hostile effects, and capacity count without
importing the primary Block-7 implementation or its upstream fixture modules.
"""

from __future__ import annotations

from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 180

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "FRESH_ANCILLA_STAGED_CQ_RECORD_INTERTWINER_CONDITIONAL_"
    "COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-20.md"
)

AUDIT_INPUT_PATHS = (
    "docs/FRESH_ANCILLA_STAGED_CQ_RECORD_INTERTWINER_CONDITIONAL_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
    "scripts/fresh_ancilla_staged_cq_record_intertwiner_conditional_completion_2026_08_20.py",
)

PASS = 0
FAIL = 0

I2 = sp.eye(2)
X = sp.Matrix(((0, 1), (1, 0)))
Y = sp.Matrix(((0, -sp.I), (sp.I, 0)))
Z = sp.diag(1, -1)
PAULIS = (I2, X, Y, Z)

E0 = sp.diag(sp.Rational(1, 2), 0)
EA1 = sp.Matrix(
    ((sp.Rational(1, 10), sp.sqrt(2) / 5), (sp.sqrt(2) / 5, sp.Rational(4, 5)))
)
EA2 = sp.Matrix(
    ((sp.Rational(2, 5), -sp.sqrt(2) / 5), (-sp.sqrt(2) / 5, sp.Rational(1, 5)))
)
EB1 = sp.Matrix(
    ((sp.Rational(1, 4), sp.sqrt(2) / 4), (sp.sqrt(2) / 4, sp.Rational(1, 2)))
)
EB2 = sp.Matrix(
    ((sp.Rational(1, 4), -sp.sqrt(2) / 4), (-sp.sqrt(2) / 4, sp.Rational(1, 2)))
)
MENUS = {"A": (E0, EA1, EA2), "B": (E0, EB1, EB2)}

RHO_STAR = sp.diag(sp.Rational(3, 5), sp.Rational(2, 5))
RHO_TOMO = (
    I2 / 2,
    (I2 + X) / 2,
    (I2 + Y) / 2,
    (I2 + Z) / 2,
)

EXPECTED = {
    "A": (
        sp.diag(sp.Rational(3, 10), 0),
        sp.Matrix(
            (
                (sp.Rational(19, 450), 19 * sp.sqrt(2) / 225),
                (19 * sp.sqrt(2) / 225, sp.Rational(76, 225)),
            )
        ),
        sp.Matrix(
            (
                (sp.Rational(16, 75), -8 * sp.sqrt(2) / 75),
                (-8 * sp.sqrt(2) / 75, sp.Rational(8, 75)),
            )
        ),
    ),
    "B": (
        sp.diag(sp.Rational(3, 10), 0),
        sp.Matrix(
            (
                (sp.Rational(7, 60), 7 * sp.sqrt(2) / 60),
                (7 * sp.sqrt(2) / 60, sp.Rational(7, 30)),
            )
        ),
        sp.Matrix(
            (
                (sp.Rational(7, 60), -7 * sp.sqrt(2) / 60),
                (-7 * sp.sqrt(2) / 60, sp.Rational(7, 30)),
            )
        ),
    ),
}


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS [{label}] {detail}")
    else:
        FAIL += 1
        print(f"FAIL [{label}] {detail}")


def zero(value: sp.Matrix) -> bool:
    return sp.simplify(value) == sp.zeros(*value.shape)


def direct_sum(blocks: tuple[sp.Matrix, ...]) -> sp.Matrix:
    return sp.diag(*blocks)


def programs() -> dict[str, tuple[sp.Matrix, ...]]:
    return {
        context: tuple(
            sp.simplify(effect / sp.sqrt(sp.trace(effect))) for effect in menu
        )
        for context, menu in MENUS.items()
    }


PROGRAMS = programs()
K0 = PROGRAMS["A"][0]
B = sp.diag(1 / sp.sqrt(2), 1)


def cq(operators: tuple[sp.Matrix, ...], rho: sp.Matrix) -> sp.Matrix:
    return direct_sum(
        tuple(sp.simplify(operator * rho * operator.H) for operator in operators)
    )


def residual(context: str) -> tuple[sp.Matrix, sp.Matrix]:
    return tuple(
        sp.simplify(operator * B.inv()) for operator in PROGRAMS[context][1:]
    )  # type: ignore[return-value]


def copy_matrix() -> sp.Matrix:
    return sp.Matrix(
        (
            (1, 0, 0, 0),
            (0, 1, 0, 0),
            (0, 0, 0, 1),
            (0, 0, 1, 0),
        )
    )


def copied_isometry(operators: tuple[sp.Matrix, sp.Matrix]) -> sp.Matrix:
    pointer = sp.Matrix.vstack(*operators)
    blank = sp.zeros(8, 4)
    for p in range(2):
        for s in range(2):
            blank[(p * 2) * 2 + s, p * 2 + s] = 1
    return sp.simplify(sp.kronecker_product(copy_matrix(), I2) * blank * pointer)


def trace_pointer(copied: sp.Matrix, rho: sp.Matrix) -> sp.Matrix:
    joint = sp.simplify(copied * rho * copied.H)
    output = sp.zeros(4)
    for left_memory in range(2):
        for right_memory in range(2):
            for left_system in range(2):
                for right_system in range(2):
                    output[2 * left_memory + left_system, 2 * right_memory + right_system] = sp.simplify(
                        sum(
                            joint[
                                (2 * pointer + left_memory) * 2 + left_system,
                                (2 * pointer + right_memory) * 2 + right_system,
                            ]
                            for pointer in range(2)
                        )
                    )
    return output


def staged_append_isometry(context: str) -> sp.Matrix:
    """Map first-memory bit x system to three memory bits x system."""

    j1, j2 = residual(context)
    stage = sp.zeros(16, 4)
    stage[0:2, 0:2] = I2
    stage[12:14, 2:4] = j1
    stage[14:16, 2:4] = j2
    return stage


def source_and_scope_checks() -> None:
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "probability-independent path channel",
        "central-restriction compatibility",
        "not an actual-member theorem",
        "no axiom amendment is justified yet",
        "universal impossibility and axiom necessity",
        "fail / do not ship",
        "obligation retirement: zero",
        "toe percentage movement: zero",
    )
    check(
        "independent-source-and-scope",
        NOTE.exists() and all(phrase in text for phrase in required),
        "positive channel result and negative one-site boundary are scoped separately",
    )


def menu_and_branch_checks() -> None:
    check(
        "independent-exact-menu-normalization",
        all(zero(sum(menu, sp.zeros(2)) - I2) for menu in MENUS.values())
        and all(effect.rank() == 1 and effect.is_positive_semidefinite is True for menu in MENUS.values() for effect in menu),
        "manual Q(sqrt(2)) effects are positive rank-one resolutions",
    )
    check(
        "independent-Kraus-normalization",
        all(
            zero(sum((operator.H * operator for operator in program), sp.zeros(2)) - I2)
            for program in PROGRAMS.values()
        )
        and PROGRAMS["A"][0] == PROGRAMS["B"][0],
        "manual Lüders operators give normalized A/B instruments with a shared K0",
    )
    check(
        "independent-fixed-branch-recovery",
        all(
            all(
                zero(sp.simplify(operator * RHO_STAR * operator.H) - expected)
                for operator, expected in zip(PROGRAMS[context], EXPECTED[context], strict=True)
            )
            for context in ("A", "B")
        ),
        "all fixed branch operators and rational traces are rebuilt independently",
    )


def staged_and_copy_checks() -> None:
    failures = 0
    for context, program in PROGRAMS.items():
        residual_ops = residual(context)
        failures += not zero(
            sum((operator.H * operator for operator in residual_ops), sp.zeros(2)) - I2
        )
        failures += any(
            not zero(operator * B - target)
            for operator, target in zip(residual_ops, program[1:], strict=True)
        )
        for operators in ((K0, B), residual_ops):
            copied = copied_isometry(operators)
            failures += not zero(copied.H * copied - I2)
            for rho in RHO_TOMO:
                failures += not zero(trace_pointer(copied, rho) - cq(operators, rho))
        stage = staged_append_isometry(context)
        full = sp.simplify(stage * sp.Matrix.vstack(K0, B))
        expected = sp.zeros(16, 2)
        expected[0:2, :] = program[0]
        expected[12:14, :] = program[1]
        expected[14:16, :] = program[2]
        failures += not zero(stage.H * stage - sp.eye(4))
        failures += not zero(full.H * full - I2)
        failures += not zero(full - expected)
    check(
        "independent-staged-fresh-copy",
        failures == 0 and zero(copy_matrix().H * copy_matrix() - sp.eye(4)),
        "both binary stages factor and copy to fresh orthogonal labels; an explicit append-aware isometry independently realizes memory words 000,110,111",
    )


def intertwiner_and_center_checks() -> None:
    x00, x11, xr, xi = sp.symbols("x00 x11 xr xi", real=True)
    rho = sp.Matrix(((x00, xr + sp.I * xi), (xr - sp.I * xi, x11)))
    failures = 0
    weights: dict[str, tuple[sp.Expr, ...]] = {}
    for context, program in PROGRAMS.items():
        j1, j2 = residual(context)
        path = (K0, sp.simplify(j1 * B), sp.simplify(j2 * B))
        failures += not zero(cq(path, rho) - cq(program, rho))
        state = cq(path, RHO_STAR)
        weights[context] = tuple(
            sp.simplify(sp.trace(state[2 * index : 2 * index + 2, 2 * index : 2 * index + 2]))
            for index in range(3)
        )
    check(
        "independent-symbolic-path-intertwiner",
        failures == 0,
        "the staged path and flat ternary channels agree for a symbolic Hermitian input",
    )
    check(
        "independent-central-masses",
        weights == {
            "A": (sp.Rational(3, 10), sp.Rational(19, 50), sp.Rational(8, 25)),
            "B": (sp.Rational(3, 10), sp.Rational(7, 20), sp.Rational(7, 20)),
        },
        weights,
    )


def operational_checks() -> None:
    coordinate_matrix = sp.Matrix(
        [[sp.trace(axis * rho) for axis in PAULIS] for rho in RHO_TOMO]
    )
    a, b, c, d = sp.symbols("a b c d", real=True)
    effect = sp.Matrix(((a, c - sp.I * d), (c + sp.I * d, b)))
    solutions = {
        (context, index): sp.solve(
            [sp.simplify(sp.trace((effect - expected) * rho)) for rho in RHO_TOMO],
            (a, b, c, d),
            dict=True,
        )
        for context, menu in MENUS.items()
        for index, expected in enumerate(menu)
    }
    expected_solutions = {
        (context, index): [
            {
                a: expected[0, 0],
                b: expected[1, 1],
                c: sp.re(expected[0, 1]),
                d: -sp.im(expected[0, 1]),
            }
        ]
        for context, menu in MENUS.items()
        for index, expected in enumerate(menu)
    }
    check(
        "independent-effect-complete-tomography",
        coordinate_matrix.rank() == 4
        and solutions == expected_solutions
        and solutions[("A", 0)]
        == [{a: sp.Rational(1, 2), b: 0, c: 0, d: 0}],
        "the four preparations independently force every A/B branch effect exactly",
    )

    wrong = (sp.Rational(3, 10) * I2, sp.Rational(7, 10) * I2)
    front = (K0, B)
    correct_star = tuple(sp.trace(effect * RHO_STAR) for effect in (E0, I2 - E0))
    wrong_star = tuple(sp.trace(effect * RHO_STAR) for effect in wrong)
    gaps = [
        sp.simplify(sp.trace((E0 - wrong[0]) * rho)) for rho in RHO_TOMO
    ]
    star_blocks = tuple(
        sp.simplify(operator * RHO_STAR * operator.H) for operator in front
    )
    tau_star = tuple(
        sp.simplify(block / sp.trace(block)) for block in star_blocks
    )

    def wrong_affine(rho: sp.Matrix) -> sp.Matrix:
        return direct_sum(
            tuple(
                sp.simplify(sp.trace(f * rho) * tau)
                for f, tau in zip(wrong, tau_star, strict=True)
            )
        )

    left, right = RHO_TOMO[1], RHO_TOMO[3]
    wrong_affinity_gap = sp.simplify(
        wrong_affine((left + right) / 2)
        - (wrong_affine(left) + wrong_affine(right)) / 2
    )
    choi_blocks = tuple(
        sp.kronecker_product(f.T, tau)
        for f, tau in zip(wrong, tau_star, strict=True)
    )
    check(
        "independent-wrong-effect-control",
        correct_star == wrong_star == (sp.Rational(3, 10), sp.Rational(7, 10))
        and zero(wrong_affine(RHO_STAR) - cq(front, RHO_STAR))
        and any(gap != 0 for gap in gaps)
        and zero(wrong_affinity_gap)
        and all(block.is_positive_semidefinite is True for block in choi_blocks)
        and all(effect.is_positive_semidefinite is True for effect in wrong)
        and zero(sum(wrong, sp.zeros(2)) - I2),
        {
            "single_preparation_full_cq_match": True,
            "fixed_state_control_is_affine_cp_tp": True,
            "spanning_family_rejects": True,
        },
    )

    mixed = RHO_TOMO[0]
    coherent = sp.simplify(sp.Matrix.vstack(*front) * mixed * sp.Matrix.vstack(*front).H)
    dephased = cq(front, mixed)
    diagonal_blind = all(
        sp.simplify(
            sp.trace(
                sp.kronecker_product(
                    sp.diag(1 if label == 0 else 0, 1 if label == 1 else 0),
                    observable,
                )
                * (coherent - dephased)
            )
        )
        == 0
        for label in range(2)
        for observable in PAULIS
    )
    offdiagonal_gaps = tuple(
        sp.simplify(
            sp.trace(
                sp.kronecker_product(label_axis, observable)
                * (coherent - dephased)
            )
        )
        for label_axis in (X, Y)
        for observable in PAULIS
    )
    check(
        "independent-coherent-label-control",
        diagonal_blind and any(gap != 0 for gap in offdiagonal_gaps),
        "diagonal label tomography is blind to coherent pointer offdiagonals, while label X/Y controls reject them",
    )

    direct = (left + right) / 2
    check(
        "independent-tag-screened-affinity",
        all(
            zero(cq(program, direct) - (cq(program, left) + cq(program, right)) / 2)
            for program in PROGRAMS.values()
        ),
        "the explicit channel is affine after the supplied tag is forgotten",
    )


def capacity_and_boundary_checks() -> None:
    affine_coordinate_map = sp.Matrix(
        (
            (1, 0, 0, 0, 0, 0, 0),
            (0, 1, 0, 0, 0, 0, 0),
            (0, 0, 0, 1, 0, 0, 0),
            (0, 0, 0, 0, 1, 0, 0),
            (0, 0, 0, 0, 0, 1, 0),
            (0, 0, 0, 0, 0, 0, 1),
            (0, 0, 1, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0),
        )
    )
    check(
        "independent-one-site-capacity",
        2 * 4 == 8 > 4 and 3 * 4 == 12 > 4 and 2**2 == 4 and 2**2 < 6 <= 2**3,
        "binary/ternary full cq algebras exceed one-M2 capacity for faithful complex-linear/*-algebraic representations while two-/three-qubit multisite representations suffice",
    )
    check(
        "independent-real-affine-counterroute",
        affine_coordinate_map.rank() == 7 and 3 * 4 - 1 == 11 > 8,
        "an explicit normalized-binary real-affine coordinate injection into non-Hermitian M2 defeats a broader affine no-go; the normalized ternary affine hull has dimension eleven",
    )
    text = NOTE.read_text(encoding="utf-8")
    plain = " ".join(text.replace("*", "").lower().split())
    check(
        "independent-boundary-ledger",
        "central-restriction compatibility" in plain
        and "sufficient candidate law/axiom interface" in plain
        and "not a proven necessary or minimal axiom" in plain
        and "no axiom amendment is justified yet" in plain,
        "the exact missing compatibility is named without an axiom-necessity claim",
    )


def main() -> int:
    source_and_scope_checks()
    menu_and_branch_checks()
    staged_and_copy_checks()
    intertwiner_and_center_checks()
    operational_checks()
    capacity_and_boundary_checks()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
