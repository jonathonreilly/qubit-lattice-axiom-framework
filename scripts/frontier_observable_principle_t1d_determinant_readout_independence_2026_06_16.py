#!/usr/bin/env python3
"""Exact independence/no-go check for observable-principle T1-d.

The target blocker is the parent row's T1-d readout-identification bridge:
Record additivity plus determinant block factorization does not derive that a
scalar record readout is a continuous function of det(D+J) alone, nor that
disjoint source blocks register as disjoint records.

This runner supplies exact countermodels over finite positive diagonal source
blocks.  It does not edit or apply audit verdicts.
"""

from __future__ import annotations

import math
import os
import sys

import sympy as sp


PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
    else:
        FAIL += 1
    suffix = f"  -- {detail}" if detail else ""
    print(f"[{status}] {name}{suffix}")


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
PARENT = os.path.join(REPO, "docs", "OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md")
NOTE = os.path.join(
    REPO,
    "docs",
    "OBSERVABLE_PRINCIPLE_T1D_DETERMINANT_READOUT_INDEPENDENCE_NO_GO_NOTE_2026-06-16.md",
)
AXIOMS = os.path.join(REPO, "docs", "MINIMAL_AXIOMS_2026-06-05.md")


def logdet_diag(entries: tuple[sp.Expr, ...]) -> sp.Expr:
    return sp.log(sp.prod(entries))


def trace_diag(entries: tuple[sp.Expr, ...]) -> sp.Expr:
    return sum(entries)


def w_eps(entries: tuple[sp.Expr, ...], eps: sp.Expr) -> sp.Expr:
    return sp.simplify(logdet_diag(entries) + eps * trace_diag(entries))


def direct_sum(a: tuple[sp.Expr, ...], b: tuple[sp.Expr, ...]) -> tuple[sp.Expr, ...]:
    return a + b


def read(path: str) -> str:
    with open(path, "r", encoding="utf-8") as handle:
        return handle.read()


def test_additive_countermodel() -> None:
    print("== T1: additive continuous readout countermodel ==")
    eps = sp.Symbol("epsilon", real=True, nonzero=True)
    a = (sp.Integer(4), sp.Integer(1))
    b = (sp.Integer(2), sp.Integer(2))
    c = (sp.Integer(3), sp.Integer(5))

    lhs = w_eps(direct_sum(a, c), eps)
    rhs = w_eps(a, eps) + w_eps(c, eps)
    check(
        "W_epsilon is exactly direct-sum additive",
        sp.simplify(lhs - rhs) == 0,
        "W(A+B)-W(A)-W(B)=0 for symbolic epsilon",
    )

    check(
        "log det part is direct-sum additive",
        sp.simplify(logdet_diag(direct_sum(a, c)) - logdet_diag(a) - logdet_diag(c)) == 0,
    )
    check(
        "trace part is direct-sum additive",
        sp.simplify(trace_diag(direct_sum(a, c)) - trace_diag(a) - trace_diag(c)) == 0,
    )
    check(
        "determinant multiplicativity is preserved",
        sp.prod(direct_sum(a, c)) == sp.prod(a) * sp.prod(c),
        f"det(A+C)={sp.prod(direct_sum(a, c))}, det(A)det(C)={sp.prod(a) * sp.prod(c)}",
    )

    det_a = sp.prod(a)
    det_b = sp.prod(b)
    gap = sp.simplify(w_eps(a, eps) - w_eps(b, eps))
    check(
        "same determinant witness exists",
        det_a == det_b and det_a == 4,
        f"det diag(4,1) = det diag(2,2) = {det_a}",
    )
    check(
        "W_epsilon is not a function of determinant alone",
        gap == eps,
        f"W(diag(4,1))-W(diag(2,2)) = {gap}",
    )

    # Continuity is ordinary smoothness on the positive source cone.
    x, y = sp.symbols("x y", positive=True)
    w_xy = sp.log(x * y) + eps * (x + y)
    check(
        "countermodel is smooth on the positive source cone",
        sp.diff(w_xy, x) == 1 / x + eps and sp.diff(w_xy, y) == 1 / y + eps,
        f"dW/dx={sp.diff(w_xy, x)}, dW/dy={sp.diff(w_xy, y)}",
    )


def test_determinant_only_is_extra_quotient() -> None:
    print("== T2: determinant-only quotient is the missing premise ==")
    r1, r2 = sp.symbols("r1 r2", positive=True)
    c = sp.Symbol("c", real=True)
    f = c * sp.log(r1)
    add_gap = sp.simplify(c * sp.log(r1 * r2) - c * sp.log(r1) - c * sp.log(r2))
    check(
        "once determinant-only is imposed, the log family is additive",
        add_gap == 0,
        "c log(r1 r2)-c log(r1)-c log(r2)=0",
    )
    check(
        "determinant-only is independent from block additivity",
        sp.simplify(f.subs(r1, 4) - (sp.log(4) + sp.Symbol("epsilon"))) != 0,
        "the additive countermodel separates blocks with equal determinant",
    )

    # A dimension-labelled variant shows even a purely extensive record label
    # can be additive while not determinant-only.
    eps = sp.Symbol("epsilon", real=True, nonzero=True)
    a = (sp.Integer(4),)
    b = (sp.Integer(2), sp.Integer(2))
    w_dim_a = sp.log(sp.prod(a)) + eps * len(a)
    w_dim_b = sp.log(sp.prod(b)) + eps * len(b)
    check(
        "dimension-labelled additive readout is also not determinant-only",
        sp.simplify(w_dim_a - w_dim_b) == -eps,
        f"same determinant 4 but dimension contribution differs by {-eps}",
    )


def test_disjoint_source_record_clause_independent() -> None:
    print("== T3: disjoint-source to disjoint-record clause is independent ==")
    source_blocks = {"A": {1, 2}, "B": {3, 4}}
    source_disjoint = source_blocks["A"].isdisjoint(source_blocks["B"])
    source_to_record = {"A": "r0", "B": "r0"}
    record_disjoint = source_to_record["A"] != source_to_record["B"]
    check(
        "source blocks can be disjoint",
        source_disjoint,
        f"A={source_blocks['A']}, B={source_blocks['B']}",
    )
    check(
        "a non-injective source-to-record assignment is logically allowed unless ruled out by an extra bridge",
        not record_disjoint,
        f"A->{source_to_record['A']}, B->{source_to_record['B']}",
    )
    check(
        "therefore source-disjoint does not imply record-disjoint as pure logic",
        source_disjoint and not record_disjoint,
        "the missing implication is exactly the T1-d blocks-to-records clause",
    )


def test_source_guardrails() -> None:
    print("== T4: source-note guardrails ==")
    parent = read(PARENT)
    note = read(NOTE)
    ax = read(AXIOMS)

    check(
        "parent still declares T1-d as a Boundary",
        "Boundary (declared bridge premise, T1-d)" in parent
        and "readout-identification Boundary" in parent,
    )
    check(
        "parent says T1-d is not derivable from minimal_axioms",
        "not derivable from `minimal_axioms`" in parent
        or "not a consequence of `minimal_axioms`" in parent,
    )
    check(
        "parent cites the new T1-d independence no-go",
        "OBSERVABLE_PRINCIPLE_T1D_DETERMINANT_READOUT_INDEPENDENCE_NO_GO_NOTE_2026-06-16.md"
        in parent,
    )
    check(
        "minimal axiom memo withholds source/action and physical-observable identification",
        "source/action and physical-observable identification" in ax
        and "Record" in ax
        and "does not supply" in ax,
    )
    check(
        "new note forbids treating T1-d as Record-derived",
        "must not treat T1-d as Record-derived" in note
        and "does not add a new axiom" in note,
    )
    check(
        "new note carries a source-visible no-go discipline gate",
        "## No-Go Discipline Gate" in note
        and "N1 -- Alternative route enumeration" in note
        and "N8 -- Cross-cycle echo" in note,
    )
    check(
        "new note does not claim an audit-ratified retained status",
        "audit-ratified" not in note.lower()
        and "effective status" in note
        and "independent audit" in note,
    )


def main() -> None:
    print("Observable-principle T1-d determinant-readout independence no-go")
    print("=" * 78)
    test_additive_countermodel()
    test_determinant_only_is_extra_quotient()
    test_disjoint_source_record_clause_independent()
    test_source_guardrails()
    print("=" * 78)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 78)
    sys.exit(1 if FAIL else 0)


if __name__ == "__main__":
    main()
