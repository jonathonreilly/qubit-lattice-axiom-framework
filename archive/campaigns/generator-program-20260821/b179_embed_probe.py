#!/usr/bin/env python3
"""Block 179 exact cross-lane embedding probe."""

from __future__ import annotations

import ast
import subprocess
import sys
import types
from fractions import Fraction
from pathlib import Path

import sympy as sp


SCRATCH = Path(__file__).resolve().parent
WORKTREE = Path(
    "/Users/jonBridger/Projects/Physics-baremetal-probes/"
    ".claude/worktrees/gravity-toe-lane-work-427b0b"
)
FORK_RUNNER = "scripts/berezin_detc_detr_fork_2026_06_04.py"
R = sp.Rational
I = sp.I
OMEGA = (-sp.Integer(1) + sp.sqrt(3) * I) / 2
ROTATION = sp.Matrix(
    [[-R(1, 2), -sp.sqrt(3) / 2], [sp.sqrt(3) / 2, -R(1, 2)]]
)
J_COMPLEX = sp.Matrix([[0, -1], [1, 0]])


def check(label: str, condition: bool) -> None:
    if not bool(condition):
        raise AssertionError(label)
    print(f"[PASS] {label}")


def exact_source_gate() -> None:
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    count = sum(
        1
        for node in ast.walk(tree)
        if isinstance(node, ast.Constant) and isinstance(node.value, float)
    )
    check("source has no floating-point literals", count == 0)


def matrix_zero(matrix: sp.MatrixBase) -> bool:
    return all(sp.simplify(entry) == 0 for entry in matrix)


def structural_form_gate() -> None:
    closure = (
        WORKTREE
        / "scripts"
        / "admissibility_dirac_kahler_closure_audit_two_2026_08_21.py"
    ).read_text(encoding="utf-8")
    bare = (
        WORKTREE
        / "scripts"
        / "admissibility_dirac_kahler_bare_character_2026_08_20.py"
    ).read_text(encoding="utf-8")
    check(
        "committed quotient measure is explicitly phi-dagger Q phi",
        "QUOTIENT GAUSSIAN WEIGHT exp(-phi^dagger Q phi)" in closure
        and "<phi_i phibar_j> = G_ij with G = Q^{-1}" in closure,
    )
    check(
        "committed operator assembly is Q=m Hq+Kq from the cover action",
        "self.Q = sp.expand(MASS * self.Hq + self.Kq)" in closure
        and "A = m H + i (H d + d^dagger H) on the cover" in bare,
    )
    phi_lines = [line.strip() for line in closure.splitlines() if "phi" in line]
    check(
        "all field-form declarations in the imported committed layer are sesquilinear",
        len(phi_lines) == 3
        and all("phi^dagger" in line or "phibar" in line for line in phi_lines),
    )


def load_fork_arbiter() -> dict[str, object]:
    source = subprocess.check_output(
        ["git", "-C", str(WORKTREE), "show", f"origin/main:{FORK_RUNNER}"],
        text=True,
    )
    name = "b179_origin_main_fork_arbiter"
    module = types.ModuleType(name)
    module.__file__ = str(WORKTREE / FORK_RUNNER)
    sys.modules[name] = module
    exec(compile(source, f"origin/main:{FORK_RUNNER}", "exec"), module.__dict__)
    return module.__dict__


def committed_fixture():
    import block174_gate_solve as gravity

    gravity.RULES["const"] = lambda t, x: R(7, 5)
    width = gravity.Width(6, "const")
    check("committed constant carrier is 12x6 with N=36", width.T == 6 and width.N == 36)
    check(
        "constant carrier rule is 7/5 at every physical cell",
        all(value[1] == R(7, 5) for value in width.field.values()),
    )
    check("committed Q is exact and symbol-free", not width.Q.free_symbols)
    check("herm(Q) has exact inertia (36,0,0)", width.inertia_S() == (36, 0, 0))
    return width


def chart_translation(t_count: int, width: int) -> sp.Matrix:
    size = t_count * width
    translation = sp.zeros(size)
    for t in range(t_count):
        for x in range(width):
            translation[width * t + (x + 2) % width, width * t + x] = 1
    return translation


def momentum_projectors(translation: sp.Matrix) -> tuple[sp.Matrix, ...]:
    identity = sp.eye(translation.rows)
    return tuple(
        sum(
            (OMEGA ** (-k * power) * translation**power for power in range(3)),
            sp.zeros(translation.rows),
        )
        / 3
        for k in range(3)
    )


def chart_character(t: int, parity: int, k: int) -> sp.Matrix:
    vector = sp.zeros(36, 1)
    for orbit_index in range(3):
        x = parity + 2 * orbit_index
        vector[6 * t + x] = OMEGA ** (-k * orbit_index) / sp.sqrt(3)
    return vector


def module_certificate(Q: sp.Matrix) -> tuple[sp.Matrix, sp.Matrix]:
    translation = chart_translation(6, 6)
    identity = sp.eye(36)
    check("U is unitary and U^3=I", translation.H * translation == identity and translation**3 == identity)
    check("[Q,U]=0 entry-for-entry", matrix_zero(Q * translation - translation * Q))

    projectors = momentum_projectors(translation)
    check(
        "P_0,P_1,P_2 are exact Hermitian orthogonal idempotents resolving I",
        all(matrix_zero(projector.H - projector) for projector in projectors)
        and all(
            matrix_zero(
                projectors[k] * projectors[j]
                - (projectors[k] if k == j else sp.zeros(36))
            )
            for k in range(3)
            for j in range(3)
        )
        and matrix_zero(sum(projectors, sp.zeros(36)) - identity),
    )
    check("each chart projector has exact rank/trace 12", all(sp.trace(p) == 12 for p in projectors))

    generator = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    p_single = (sp.eye(3) + generator + generator**2) / 3
    p_doublet = sp.eye(3) - p_single
    abstract_basis = sp.Matrix.hstack(
        sp.Matrix([2, -1, -1]) / sp.sqrt(6),
        sp.Matrix([0, 1, -1]) / sp.sqrt(2),
    )
    check(
        "abstract basis is an orthonormal basis of the C-summand",
        abstract_basis.H * abstract_basis == sp.eye(2)
        and matrix_zero(p_doublet * abstract_basis - abstract_basis)
        and sp.trace(p_doublet) == 2,
    )
    check(
        "abstract C-summand generator is ROTATION entry-for-entry",
        matrix_zero(generator * abstract_basis - abstract_basis * ROTATION),
    )

    f_one = chart_character(0, 0, 1)
    f_two = chart_character(0, 0, 2)
    check(
        "f_1 and f_2 are the exact conjugate chart-momentum pair",
        matrix_zero(translation * f_one - OMEGA * f_one)
        and matrix_zero(translation * f_two - OMEGA**2 * f_two)
        and matrix_zero(f_two - f_one.conjugate())
        and sp.simplify((f_one.H * f_one)[0]) == 1
        and sp.simplify((f_two.H * f_two)[0]) == 1
        and matrix_zero(projectors[1] * f_one - f_one)
        and matrix_zero(projectors[2] * f_two - f_two),
    )

    embed_one = sp.Matrix.hstack(f_one, I * f_one)
    embed_two = sp.Matrix.hstack(f_two, -I * f_two)
    check(
        "R[Z_3] intertwiner matches both conjugate character actions entry-for-entry",
        matrix_zero(translation * embed_one - embed_one * ROTATION)
        and matrix_zero(translation * embed_two - embed_two * ROTATION),
    )
    check(
        "ambient scalar i induces J on the holomorphic embedded doublet",
        matrix_zero(I * embed_one - embed_one * J_COMPLEX)
        and J_COMPLEX**2 == -sp.eye(2)
        and matrix_zero(J_COMPLEX * ROTATION - ROTATION * J_COMPLEX),
    )
    return f_one, f_two


def induced_metric_and_fork(Q: sp.Matrix, f_one: sp.Matrix, arbiter: dict[str, object]) -> None:
    beta = sp.simplify((f_one.H * Q * f_one)[0])
    check("induced one-complex-slot coefficient beta=3193/2240", beta == R(3193, 2240))

    x, y = sp.symbols("x y", real=True)
    phi = (x + I * y) * f_one
    restricted_form = sp.simplify((phi.H * Q * phi)[0])
    check(
        "restricted committed form is beta*(x^2+y^2) with no real-mixing term",
        sp.expand(restricted_form - beta * (x**2 + y**2)) == 0,
    )

    cpair = arbiter["CPair"]
    beta_fraction = Fraction(int(beta.p), int(beta.q))
    beta_complex = cpair(beta_fraction, Fraction(0))
    holo_block = ((beta_complex,),)
    holo_det = arbiter["det_cpair"](holo_block)
    real_metric = arbiter["complex_realification"](beta_complex)
    real_det = arbiter["det_fraction"](real_metric)
    check("fork arbiter reads induced holomorphic metric as one 1x1 complex block", holo_det == beta_complex)
    check(
        "fork arbiter realification is diag(beta,beta) with det_R=norm(det_C)^2",
        real_metric
        == ((beta_fraction, Fraction(0)), (Fraction(0), beta_fraction))
        and real_det == beta_fraction * beta_fraction
        and holo_det.norm2() == real_det,
    )

    real_slots = len(real_metric)
    holo_gaussian_slots = real_slots // 2
    holo_berezin_slots = len(holo_block)
    majorana = (
        (Fraction(0), beta_fraction),
        (-beta_fraction, Fraction(0)),
    )
    check(
        "arbiter Majorana control remains the two-real-slot cell",
        arbiter["pfaffian_2x2"](majorana) ** 2 == arbiter["det_fraction"](majorana)
        and len(majorana) == real_slots,
    )

    cells = {
        "real Gaussian": real_slots,
        "Majorana Berezin": len(majorana),
        "holomorphic Gaussian": holo_gaussian_slots,
        "holomorphic Berezin": holo_berezin_slots,
    }
    results = {
        name: (
            arbiter["r_from_slot_count"](slots),
            arbiter["q_from_r"](arbiter["r_from_slot_count"](slots)),
        )
        for name, slots in cells.items()
    }
    check(
        "four-cell arbiter gives real=(1,1), holomorphic=(1/2,2/3)",
        results["real Gaussian"] == (Fraction(1), Fraction(1))
        and results["Majorana Berezin"] == (Fraction(1), Fraction(1))
        and results["holomorphic Gaussian"] == (Fraction(1, 2), Fraction(2, 3))
        and results["holomorphic Berezin"] == (Fraction(1, 2), Fraction(2, 3)),
    )

    print(f"EXACT induced beta = {beta}")
    for name, slots in cells.items():
        r_value, q_value = results[name]
        print(f"CELL {name}: slots={slots} r={r_value} Q={q_value}")


def main() -> int:
    exact_source_gate()
    check("omega is an exact primitive cube root", sp.expand(OMEGA**2 + OMEGA + 1) == 0)
    structural_form_gate()
    arbiter = load_fork_arbiter()
    check("origin/main fork arbiter loaded", all(name in arbiter for name in (
        "CPair", "det_cpair", "complex_realification", "det_fraction",
        "r_from_slot_count", "q_from_r")))
    width = committed_fixture()
    f_one, _ = module_certificate(width.Q)
    induced_metric_and_fork(width.Q, f_one, arbiter)
    print("TOTAL: PASS (exact arithmetic only)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
