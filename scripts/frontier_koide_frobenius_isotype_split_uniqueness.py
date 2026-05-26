#!/usr/bin/env python3
"""No-go certificate for Frobenius isotype-weight uniqueness."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

REPO_ROOT = Path(__file__).resolve().parents[1]
NOTE = REPO_ROOT / "docs/KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md"
LEDGER = REPO_ROOT / "docs/audit/data/audit_ledger.json"
QUEUE = REPO_ROOT / "docs/audit/data/audit_queue.json"

CLAIM_ID = "koide_frobenius_isotype_split_uniqueness_note_2026-04-21"
RUNNER_PATH = "scripts/frontier_koide_frobenius_isotype_split_uniqueness.py"

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
        "Status:** bounded no-go",
        "do not force the Frobenius normalization",
        "alpha = beta = 1",
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
    x1, x2, x3 = sp.symbols("x1 x2 x3", real=True)
    a_mat = sp.diag(x1, x2, x3)
    trace_a = sp.trace(a_mat)
    identity = sp.eye(3)
    a_scalar = sp.simplify(trace_a * identity / 3)
    a_traceless = sp.simplify(a_mat - a_scalar)

    check("traceless component has zero trace", sp.simplify(sp.trace(a_traceless)) == 0)
    check("scalar and traceless components are Frobenius-orthogonal", sp.simplify(sp.trace(a_scalar * a_traceless)) == 0)

    b_full = bilinear(alpha, beta, a_mat, a_mat)
    decomposed = sp.simplify((alpha + 3 * beta) * sp.trace(a_scalar * a_scalar) + alpha * sp.trace(a_traceless * a_traceless))
    check("B_{alpha,beta} diagonalizes by isotype weights", sp.simplify(b_full - decomposed) == 0, str(decomposed))

    scalar_weight = alpha + 3 * beta
    traceless_weight = alpha
    check("Frobenius point has equal weights", sp.simplify((scalar_weight / traceless_weight).subs({alpha: 1, beta: 0}) - 1) == 0)
    check("positive beta changes the isotype ratio", sp.simplify((scalar_weight / traceless_weight).subs({alpha: 1, beta: 1}) - 4) == 0, kind="B")

    m_trace = sp.diag(1, 1, 2)
    frob = bilinear(1, 0, m_trace, m_trace)
    counter = bilinear(1, 1, m_trace, m_trace)
    check("alpha=beta=1 is positive on scalar block", (1 + 3 * 1) > 0, "scalar weight 4", kind="B")
    check("alpha=beta=1 is positive on traceless block", 1 > 0, "traceless weight 1", kind="B")
    check("alpha=beta=1 differs from Frobenius on trace-bearing matrix", counter != frob, f"B_11={counter}, B_10={frob}", kind="B")

    c = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    a_test = sp.Matrix([[1, 2, 0], [2, 3, 1], [0, 1, 4]])
    b_test = sp.Matrix([[2, 0, 1], [0, 5, 0], [1, 0, 3]])
    a_conj = c.T * a_test * c
    b_conj = c.T * b_test * c
    check(
        "B_{1,1} is invariant under cyclic conjugation on test pair",
        sp.simplify(bilinear(1, 1, a_test, b_test) - bilinear(1, 1, a_conj, b_conj)) == 0,
        kind="B",
    )

    print("\n=== admitted beta=0 AM-GM corollary sanity check ===")
    a, r, n = sp.symbols("a r n", positive=True, real=True)
    e_plus = 3 * a**2
    e_perp = 6 * r**2
    kappa_symbol = sp.Symbol("kappa", positive=True, real=True)
    q_expr = (1 + 2 / kappa_symbol) / 3
    a2_solution = sp.solve(sp.Eq(e_plus, e_perp), a**2)[0]
    check("AM-GM equality gives kappa=2 if beta=0 is admitted", sp.simplify(a2_solution / r**2 - 2) == 0)
    check("kappa=2 gives Q=2/3", sp.simplify(q_expr.subs(kappa_symbol, 2) - sp.Rational(2, 3)) == 0)
    check("AM-GM stationary point is interior for N>0", sp.simplify((n / 2) * (n / 2) - n**2 / 4) == 0)


def audit_metadata_checks() -> None:
    if not LEDGER.exists() or not QUEUE.exists():
        print("\n=== audit metadata unavailable before pipeline ===")
        return
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    row = ledger["rows"][CLAIM_ID]
    queue = json.loads(QUEUE.read_text(encoding="utf-8"))["queue"]
    queue_entry = next(e for e in queue if e["claim_id"] == CLAIM_ID)

    print("\n=== regenerated audit metadata ===")
    check("ledger claim_type is no_go", row.get("claim_type") == "no_go")
    check("ledger audit_status reset to unaudited", row.get("audit_status") == "unaudited")
    check("ledger effective_status reset to unaudited", row.get("effective_status") == "unaudited")
    check("ledger runner_path registered", row.get("runner_path") == RUNNER_PATH, str(row.get("runner_path")))
    check("ledger has no direct deps", row.get("deps") == [], str(row.get("deps")))
    check("no open dependency paths remain", row.get("open_dependency_paths") == [], str(row.get("open_dependency_paths")))
    check("queue marks row ready", queue_entry.get("ready") is True, str(queue_entry.get("ready")))
    check("descendant chain remains material", int(row.get("transitive_descendants") or 0) >= 50, str(row.get("transitive_descendants")), kind="B")


def main() -> int:
    note_boundary_checks()
    algebra_checks()
    audit_metadata_checks()
    print("\nKoide Frobenius isotype-weight freedom no-go certificate:", "PASS" if FAIL_COUNT == 0 else "FAIL")
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
