#!/usr/bin/env python3
"""No-go certificate for Frobenius isotype-weight uniqueness."""

from __future__ import annotations

from pathlib import Path

import sympy as sp

REPO_ROOT = Path(__file__).resolve().parents[1]
NOTE = REPO_ROOT / "docs/KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md"
AUDIT_INPUT_PATHS = (
    "docs/KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md",
)

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "", kind: str = "A") -> None:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    suffix = f" ({detail})" if detail else ""
    print(f"[{status}] [{kind}] {name}{suffix}")


def note_boundary_checks() -> None:
    text = " ".join(NOTE.read_text(encoding="utf-8").split())
    required = [
        "Claim type:** no_go",
        "Claim scope:** Within the family of symmetric bilinear forms",
        "Status:** bounded no-go",
        "do not force the Frobenius normalization",
        "B_{1,1}(A,A) = 22",
        "Why The AM-GM Step Does Not Remove The Freedom",
        "Conditional Corollary Kept Out Of Scope",
        "does not claim",
        "any new axiom or audit verdict",
    ]
    for phrase in required:
        check(f"note boundary contains: {phrase}", phrase in text)

    forbidden = [
        "conditional AM-GM result; not a uniqueness theorem",
        "29/29 PASS",
        "audited_conditional",
        "retained-grade derivation",
        "target_audit_status",
    ]
    for phrase in forbidden:
        check(f"note omits stale conditional phrase: {phrase}", phrase not in text)


def bilinear(alpha: sp.Expr, beta: sp.Expr, a_mat: sp.Matrix, b_mat: sp.Matrix) -> sp.Expr:
    return sp.simplify(alpha * sp.trace(a_mat * b_mat) + beta * sp.trace(a_mat) * sp.trace(b_mat))


def algebra_checks() -> None:
    print("\n=== Frobenius isotype-weight freedom ===")
    alpha, beta = sp.symbols("alpha beta", real=True)
    a_entries = sp.symbols("a0:9", real=True)
    b_entries = sp.symbols("b0:9", real=True)
    a_mat = sp.Matrix(3, 3, a_entries)
    b_mat = sp.Matrix(3, 3, b_entries)
    identity = sp.eye(3)
    a_scalar = sp.trace(a_mat) * identity / 3
    a_traceless = sp.simplify(a_mat - a_scalar)
    b_scalar = sp.trace(b_mat) * identity / 3
    b_traceless = sp.simplify(b_mat - b_scalar)

    check("traceless component has zero trace", sp.simplify(sp.trace(a_traceless)) == 0)
    check(
        "scalar and traceless blocks are B_{alpha,beta}-orthogonal",
        bilinear(alpha, beta, a_scalar, b_traceless) == 0
        and bilinear(alpha, beta, a_traceless, b_scalar) == 0,
    )

    b_full = bilinear(alpha, beta, a_mat, b_mat)
    decomposed = sp.simplify(
        (alpha + 3 * beta) * sp.trace(a_scalar * b_scalar)
        + alpha * sp.trace(a_traceless * b_traceless)
    )
    check(
        "full bilinear B_{alpha,beta} diagonalizes by isotype weights",
        sp.simplify(b_full - decomposed) == 0,
    )

    scalar_weight = alpha + 3 * beta
    traceless_weight = alpha
    check("Frobenius point has equal weights", sp.simplify((scalar_weight / traceless_weight).subs({alpha: 1, beta: 0}) - 1) == 0)
    check("beta changes the scale-invariant isotype ratio", sp.simplify((scalar_weight / traceless_weight).subs({alpha: 1, beta: 1}) - 4) == 0)

    m_trace = sp.diag(1, 1, 2)
    frob = bilinear(1, 0, m_trace, m_trace)
    counter = bilinear(1, 1, m_trace, m_trace)
    scalar_witness = sp.eye(3)
    traceless_witness = sp.diag(1, -1, 0)
    check("scalar witness isolates alpha+3 beta", sp.simplify(bilinear(alpha, beta, scalar_witness, scalar_witness) - 3 * (alpha + 3 * beta)) == 0)
    check("traceless witness isolates alpha", sp.simplify(bilinear(alpha, beta, traceless_witness, traceless_witness) - 2 * alpha) == 0)
    check("alpha=beta=1 is positive on both isotype blocks", (1 + 3 * 1) > 0 and 1 > 0, "weights (4,1)")
    check("B_{1,1} differs from Frobenius on trace-bearing matrix", counter == 22 and frob == 6, f"B_11={counter}, B_10={frob}")

    t = sp.symbols("t", real=True)
    denom = 1 + t**2
    u_mat = sp.Matrix(
        [
            [(1 - t**2) / denom, 2 * t / denom, 0],
            [-2 * t / denom, (1 - t**2) / denom, 0],
            [0, 0, 1],
        ]
    )
    a_test = sp.Matrix([[1, 2, 0], [2, 3, 1], [0, 1, 4]])
    b_test = sp.Matrix([[2, 0, 1], [0, 5, 0], [1, 0, 3]])
    a_conj = sp.simplify(u_mat * a_test * u_mat.T)
    b_conj = sp.simplify(u_mat * b_test * u_mat.T)
    check("symbolic one-parameter conjugator is orthogonal", sp.simplify(u_mat * u_mat.T - identity) == sp.zeros(3))
    check(
        "B_{1,1} is invariant along a continuous adjoint family",
        sp.simplify(bilinear(1, 1, a_test, b_test) - bilinear(1, 1, a_conj, b_conj)) == 0,
    )

    print("\n=== weighted AM-GM family and Frobenius specialization ===")
    a2, r2, n = sp.symbols("a2 r2 n", positive=True, real=True)
    lam = sp.symbols("lambda", real=True)
    e_plus = 3 * (1 + 3 * lam) * a2
    e_perp = 6 * r2
    kappa_family = sp.solve(sp.Eq(e_plus, e_perp), a2)[0] / r2
    check("equal weighted energies leave kappa(lambda)=2/(1+3 lambda)", sp.simplify(kappa_family - 2 / (1 + 3 * lam)) == 0)
    check("Frobenius lambda=0 gives kappa=2", sp.simplify(kappa_family.subs(lam, 0) - 2) == 0)
    check("non-Frobenius lambda=1/3 gives kappa=1", sp.simplify(kappa_family.subs(lam, sp.Rational(1, 3)) - 1) == 0)

    kappa_symbol = sp.Symbol("kappa", positive=True, real=True)
    q_expr = (1 + 2 / kappa_symbol) / 3
    check("kappa=2 gives Q=2/3", sp.simplify(q_expr.subs(kappa_symbol, 2) - sp.Rational(2, 3)) == 0)
    x = sp.symbols("x", positive=True, real=True)
    objective = sp.log(x) + sp.log(n - x)
    check("AM-GM log objective is stationary at N/2", sp.simplify(sp.diff(objective, x).subs(x, n / 2)) == 0)
    check("AM-GM log objective is strictly concave at N/2", sp.simplify(sp.diff(objective, x, 2).subs(x, n / 2) + 8 / n**2) == 0, "second derivative = -8/N^2")


def main() -> int:
    note_boundary_checks()
    algebra_checks()
    print("\nKoide Frobenius isotype-weight freedom no-go certificate:", "PASS" if FAIL_COUNT == 0 else "FAIL")
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
