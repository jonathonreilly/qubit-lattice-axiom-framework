#!/usr/bin/env python3
"""Exact verifier for the scalar-generator tensor-action localization no-go.

The runner proves two independent statements:

1. a fixed scalar log-determinant generator admits inequivalent metric
   Hessians when the metric-to-source map is not fixed, including an arbitrary
   prescribed symmetric Hessian;
2. the live direct-source log-determinant Hessian is definite and therefore
   cannot become the mixed-inertia, gauge-degenerate linearized Einstein
   operator through any real linear field pullback.

All load-bearing checks are exact SymPy calculations.  No phenomenological
target, fitted value, random sample, or imported dataset is used.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "UNIVERSAL_GR_TENSOR_ACTION_BLOCKER_NOTE.md"
SUPERMETRIC_NOTE = ROOT / "docs" / "UNIVERSAL_GR_SUPERMETRIC_NORMAL_FORM_NOTE.md"
S3_HESSIAN_NOTE = ROOT / "docs" / "S3_TIME_OBSERVABLE_HESSIAN_ROUTE_NOTE.md"
S3_SPACETIME_NOTE = ROOT / "docs" / "S3_TIME_SPACETIME_OBSERVABLE_ROUTE_NOTE.md"


@dataclass(frozen=True)
class Check:
    name: str
    ok: bool
    detail: str
    rubric: str = "class A exact algebra"


def symmetric_basis(n: int = 4) -> list[sp.Matrix]:
    """Frobenius-orthonormal basis of Sym^2(R^n)."""

    out: list[sp.Matrix] = []
    for i in range(n):
        for j in range(i, n):
            matrix = sp.zeros(n)
            if i == j:
                matrix[i, j] = 1
            else:
                matrix[i, j] = 1 / sp.sqrt(2)
                matrix[j, i] = 1 / sp.sqrt(2)
            out.append(matrix)
    return out


def gram(operator, basis: list[sp.Matrix]) -> sp.Matrix:
    return sp.Matrix(
        [[sp.trace(left.T * operator(right)) for right in basis] for left in basis]
    )


def linearized_einstein(momentum: sp.Matrix, h: sp.Matrix) -> sp.Matrix:
    """Euclidean Fourier-space linearized Einstein operator."""

    n = momentum.rows
    p2 = (momentum.T * momentum)[0]
    trace_h = sp.trace(h)
    php = (momentum.T * h * momentum)[0]
    result = sp.zeros(n)
    for mu in range(n):
        for nu in range(n):
            p_h_nu = sum(momentum[rho] * h[rho, nu] for rho in range(n))
            p_h_mu = sum(momentum[rho] * h[rho, mu] for rho in range(n))
            result[mu, nu] = sp.Rational(1, 2) * (
                p2 * h[mu, nu]
                - momentum[mu] * p_h_nu
                - momentum[nu] * p_h_mu
                + momentum[mu] * momentum[nu] * trace_h
                + (1 if mu == nu else 0) * (php - p2 * trace_h)
            )
    return sp.simplify(result)


def gauge_map(momentum: sp.Matrix) -> sp.Matrix:
    """Columns are h_mu_nu=p_mu xi_nu+p_nu xi_mu in the symmetric basis."""

    basis = symmetric_basis(momentum.rows)
    columns = []
    for index in range(momentum.rows):
        xi = sp.eye(momentum.rows)[:, index]
        h = momentum * xi.T + xi * momentum.T
        columns.append(sp.Matrix([sp.trace(element.T * h) for element in basis]))
    return sp.Matrix.hstack(*columns)


def fierz_pauli_hessian(momentum: sp.Matrix, basis: list[sp.Matrix]) -> sp.Matrix:
    """Independent action route to the Euclidean Einstein quadratic kernel."""

    coefficients = sp.symbols(f"x0:{len(basis)}", real=True)
    h = sp.zeros(momentum.rows)
    for coefficient, element in zip(coefficients, basis):
        h += coefficient * element
    p2 = (momentum.T * momentum)[0]
    trace_h = sp.trace(h)
    hp = h * momentum
    php = (momentum.T * h * momentum)[0]
    q_fp = sp.Rational(1, 4) * (
        p2 * sp.trace(h.T * h)
        - 2 * (hp.T * hp)[0]
        + 2 * trace_h * php
        - p2 * trace_h**2
    )
    return sp.hessian(q_fp, coefficients)


def source_map_checks() -> tuple[bool, bool, bool]:
    """Exact same-W countermodels and arbitrary-Hessian realization."""

    j, m, alpha = sp.symbols("j m alpha", positive=True, nonzero=True)
    d = sp.Matrix([[0, m], [-m, 0]])
    source_det = (d + j * sp.eye(2)).det()
    w = sp.log(source_det / d.det())
    determinant_ok = sp.simplify(w - sp.log(1 + j**2 / m**2)) == 0
    derivatives_ok = (
        sp.simplify(sp.diff(w, j).subs(j, 0)) == 0
        and sp.simplify(sp.diff(w, j, 2).subs(j, 0) - 2 / m**2) == 0
    )

    # Two-dimensional toy metric-coordinate space.  Linear trace/shear maps
    # produce distinct rank-one Hessians from the same scalar W.
    x, y = sp.symbols("x y", real=True)
    trace_map = alpha * (x + y)
    shear_map = alpha * (x - y)
    h_trace = sp.hessian(w.subs(j, trace_map), (x, y)).subs({x: 0, y: 0})
    h_shear = sp.hessian(w.subs(j, shear_map), (x, y)).subs({x: 0, y: 0})
    expected_trace = (2 * alpha**2 / m**2) * sp.Matrix([[1, 1], [1, 1]])
    expected_shear = (2 * alpha**2 / m**2) * sp.Matrix([[1, -1], [-1, 1]])
    rank_one_ok = (
        sp.simplify(h_trace - expected_trace) == sp.zeros(2)
        and sp.simplify(h_shear - expected_shear) == sp.zeros(2)
        and h_trace.rank() == 1
        and h_shear.rank() == 1
        and h_trace != h_shear
    )

    # At a nonzero source background, a nonlinear source map realizes an
    # arbitrary symmetric Hessian K exactly through the chain-rule second term.
    s = sp.symbols("s", positive=True, nonzero=True)
    k11, k12, k22 = sp.symbols("k11 k12 k22", real=True)
    k_target = sp.Matrix([[k11, k12], [k12, k22]])
    wp = sp.diff(w, j).subs(j, s)
    vector = sp.Matrix([x, y])
    phi_k = s + (vector.T * k_target * vector)[0] / (2 * wp)
    realized = sp.hessian(w.subs(j, phi_k), (x, y)).subs({x: 0, y: 0})
    arbitrary_ok = sp.simplify(realized - k_target) == sp.zeros(2)
    return bool(determinant_ok and derivatives_ok), bool(rank_one_ok), bool(arbitrary_ok)


def direct_hessian_checks(basis: list[sp.Matrix]) -> tuple[bool, bool, sp.Matrix]:
    """Differentiate log det and verify the exact definite Gram matrix."""

    source_s, source_t = sp.symbols("source_s source_t", real=True)
    d_numeric = sp.diag(2, 3, 3, 3)
    d_numeric_inv = d_numeric.inv()
    hessian = sp.Matrix(
        [
            [
                sp.diff(
                    sp.log((d_numeric + source_s * left + source_t * right).det()),
                    source_s,
                    source_t,
                )
                .subs({source_s: 0, source_t: 0})
                for right in basis
            ]
            for left in basis
        ]
    )
    trace_numeric = sp.Matrix(
        [
            [-sp.trace(d_numeric_inv * left * d_numeric_inv * right) for right in basis]
            for left in basis
        ]
    )
    a, b = sp.symbols("a b", positive=True, nonzero=True)
    d_symbolic_inv = sp.diag(1 / a, 1 / b, 1 / b, 1 / b)
    trace_formula = sp.Matrix(
        [
            [-sp.trace(d_symbolic_inv * left * d_symbolic_inv * right) for right in basis]
            for left in basis
        ]
    )
    expected = sp.diag(
        -1 / a**2,
        -1 / (a * b),
        -1 / (a * b),
        -1 / (a * b),
        -1 / b**2,
        -1 / b**2,
        -1 / b**2,
        -1 / b**2,
        -1 / b**2,
        -1 / b**2,
    )
    formula_ok = sp.simplify(hessian - trace_numeric) == sp.zeros(10)
    definite_ok = (
        sp.simplify(trace_formula - expected) == sp.zeros(10)
        and trace_formula.rank() == 10
        and all(value.is_negative for value in trace_formula.diagonal())
    )
    return bool(formula_ok), bool(definite_ok), trace_formula


def main() -> int:
    basis = symmetric_basis()
    checks: list[Check] = []

    determinant_ok, rank_one_ok, arbitrary_ok = source_map_checks()
    checks.append(
        Check(
            "finite antisymmetric block gives W(j)=log(1+j^2/m^2) exactly",
            determinant_ok,
            "det(D_m+jI)=m^2+j^2, W'(0)=0, W''(0)=2/m^2",
        )
    )
    checks.append(
        Check(
            "one scalar W gives inequivalent trace and shear metric Hessians",
            rank_one_ok,
            "both are exact rank-one forms with different image lines",
        )
    )
    checks.append(
        Check(
            "a nonlinear metric-to-source map can encode an arbitrary Hessian",
            arbitrary_ok,
            "exact chain-rule witness realizes symbolic K=[[k11,k12],[k12,k22]]",
        )
    )

    formula_ok, definite_ok, direct_gram = direct_hessian_checks(basis)
    checks.append(
        Check(
            "direct-source log-det Hessian equals -Tr(D^-1 h D^-1 k)",
            formula_ok,
            "all 100 canonical basis pairs agree by exact differentiation",
        )
    )
    checks.append(
        Check(
            "direct-source Hessian is rank ten and negative definite",
            definite_ok,
            f"symbolic rank={direct_gram.rank()}, diagonal={list(direct_gram.diagonal())}",
        )
    )

    supermetric = SUPERMETRIC_NOTE.read_text(encoding="utf-8")
    route_binding_ok = (
        "B_D(h,k) = D^2 W[0](h,k) = -Tr(D^-1 h D^-1 k)" in supermetric
        and "exact local supermetric normal form" in supermetric
        and "UNIVERSAL_GR_SUPERMETRIC_NORMAL_FORM_NOTE.md" in NOTE.read_text(encoding="utf-8")
    )
    checks.append(
        Check(
            "retained route source carries the same direct-source Hessian",
            route_binding_ok,
            "supermetric source formula and load-bearing markdown dependency are present",
            rubric="class B route-binding check",
        )
    )

    p0 = sp.zeros(4, 1)
    p_time = sp.Matrix([1, 0, 0, 0])
    p_space = sp.Matrix([0, 1, 0, 0])
    einstein_time = gram(lambda h: linearized_einstein(p_time, h), basis)
    einstein_zero = gram(lambda h: linearized_einstein(p0, h), basis)
    eigenvalues = einstein_time.eigenvals()
    expected_eigenvalues = {sp.Rational(1, 2): 5, sp.Integer(-1): 1, sp.Integer(0): 4}
    checks.append(
        Check(
            "linearized Einstein symbol has the exact mixed/gauge spectrum",
            einstein_time == einstein_time.T
            and einstein_time.rank() == 6
            and eigenvalues == expected_eigenvalues,
            f"rank={einstein_time.rank()}, spectrum={eigenvalues}",
        )
    )

    fp_hessian = fierz_pauli_hessian(p_time, basis)
    checks.append(
        Check(
            "geometry-derived Einstein symbol equals the Fierz-Pauli action Hessian",
            sp.simplify(fp_hessian - einstein_time) == sp.zeros(10),
            "all 100 symmetric-basis pairs agree exactly by an independent action path",
        )
    )

    gauge_time = gauge_map(p_time)
    gauge_space = gauge_map(p_space)
    gauge_kernel_ok = (
        gauge_time.rank() == 4
        and einstein_time * gauge_time == sp.zeros(10, 4)
        and sp.Matrix.hstack(gauge_time, gauge_space).rank() == 7
    )
    checks.append(
        Check(
            "Einstein gauge kernel is four-dimensional and momentum-dependent",
            gauge_kernel_ok,
            "rank(G_p)=4 and dim(ker E_e0 intersection ker E_e1)=1",
        )
    )

    s3_hessian = S3_HESSIAN_NOTE.read_text(encoding="utf-8")
    s3_spacetime = S3_SPACETIME_NOTE.read_text(encoding="utf-8")
    primary_runner_name = "scripts/frontier_universal_gr_tensor_action_blocker.py"
    s3_pin_ok = (
        primary_runner_name in s3_hessian
        and "**Claim type:** open_gate" in s3_hessian
        and "scalar-only on this route" in s3_hessian
        and "tensor/time-coupling law" in s3_hessian
        and primary_runner_name in s3_spacetime
        and "**Claim type:** open_gate" in s3_spacetime
        and "O_lift = 1" in s3_spacetime
        and "no exact dynamics bridge" in s3_spacetime.lower()
    )
    checks.append(
        Check(
            "legacy S3 primary-runner pins retain substantive open-gate checks",
            s3_pin_ok,
            "both pinned notes preserve scalar/kinematic-only scope and missing dynamics",
            rubric="class B sibling-pin check",
        )
    )

    scaling = gram(lambda h: linearized_einstein(2 * p_time, h), basis)
    checks.append(
        Check(
            "Einstein symbol is two-derivative while the direct Hessian is order zero",
            einstein_zero == sp.zeros(10) and scaling == 4 * einstein_time,
            "E_0=0 and E_(2p)=4 E_p exactly",
        )
    )

    # A pullback of a definite real quadratic form is semidefinite.  The exact
    # mixed spectrum above supplies both signs, so no real A and global scalar
    # c can satisfy c A^T B A = E_p.  The executable witnesses below ensure the
    # two required Einstein signs and the definiteness premise are not prose-only.
    has_positive = any(value > 0 for value in eigenvalues)
    has_negative = any(value < 0 for value in eigenvalues)
    pullback_no_go = definite_ok and has_positive and has_negative
    checks.append(
        Check(
            "real pullbacks of the direct Hessian cannot equal Einstein",
            pullback_no_go,
            "A^T B A is semidefinite for definite B; E_p has both +1/2 and -1",
        )
    )

    note = NOTE.read_text(encoding="utf-8")
    note_scope_ok = (
        "**Type:** no_go" in note
        and all(f"### N{index}" in note for index in range(1, 9))
        and "does not exclude" in note
        and "real pullback" in note
        and "Source-map underdetermination" in note
        and "independent audit is required" in note
    )
    checks.append(
        Check(
            "source note carries the N1-N8 and claim-state firewalls",
            note_scope_ok,
            "no-go type, exact class, escapes, and independent-audit boundary are explicit",
            rubric="class D source-boundary check",
        )
    )

    print("SCALAR-GENERATOR TENSOR-ACTION LOCALIZATION NO-GO")
    print("=" * 78)
    for check in checks:
        tag = "PASS" if check.ok else "FAIL"
        print(f"[{tag}] [{check.rubric}] {check.name}")
        print(f"    {check.detail}")

    n_pass = sum(check.ok for check in checks)
    n_fail = len(checks) - n_pass
    print("\n" + "=" * 78)
    print(f"SUMMARY: PASS={n_pass} FAIL={n_fail} TOTAL={len(checks)}")
    if n_fail == 0:
        print(
            "Exact boundary: W alone does not select a metric Hessian, and the "
            "direct-source definite Hessian cannot become the mixed-inertia, "
            "gauge-degenerate Einstein operator by a real linear pullback."
        )
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
