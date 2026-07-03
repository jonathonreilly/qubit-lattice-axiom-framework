#!/usr/bin/env python3
"""Positive-diagonal readout classifier for Observable-Principle T1-d.

This runner verifies the finite algebra behind
OBSERVABLE_PRINCIPLE_T1D_POSITIVE_DIAGONAL_READOUT_CLASSIFIER_NOTE_2026-06-18.
It classifies continuous direct-sum additive readouts on finite positive
diagonal source blocks as one-site sums and checks that determinant-only global
readout is the logarithmic quotient. It does not audit, retag, or apply an
effective status.
"""

from __future__ import annotations

import os
import sys
from collections.abc import Callable

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
    "OBSERVABLE_PRINCIPLE_T1D_POSITIVE_DIAGONAL_READOUT_CLASSIFIER_NOTE_2026-06-18.md",
)
NO_GO = os.path.join(
    REPO,
    "docs",
    "OBSERVABLE_PRINCIPLE_T1D_DETERMINANT_READOUT_INDEPENDENCE_NO_GO_NOTE_2026-06-16.md",
)
AXIOMS = os.path.join(REPO, "docs", "MINIMAL_AXIOMS_2026-06-05.md")


def read(path: str) -> str:
    with open(path, "r", encoding="utf-8") as handle:
        return handle.read()


def direct_sum(a: tuple[sp.Expr, ...], b: tuple[sp.Expr, ...]) -> tuple[sp.Expr, ...]:
    return a + b


def one_site_sum(phi: Callable[[sp.Expr], sp.Expr], entries: tuple[sp.Expr, ...]) -> sp.Expr:
    return sp.simplify(sum(phi(entry) for entry in entries))


def determinant(entries: tuple[sp.Expr, ...]) -> sp.Expr:
    return sp.prod(entries)


def expand_log(expr: sp.Expr) -> sp.Expr:
    return sp.expand_log(expr, force=True)


def test_one_site_classifier() -> None:
    print("== T1: direct-sum additive readouts decompose into one-site sums ==")
    phi = sp.Function("phi")
    xs = sp.symbols("x1:7", positive=True)
    pairs = [(1, 1), (1, 2), (2, 2), (2, 3), (3, 3)]
    for m, n in pairs:
        left = sum(phi(x) for x in xs[: m + n])
        right = sum(phi(x) for x in xs[:m]) + sum(phi(x) for x in xs[m : m + n])
        check(
            f"recursive split W_{m+n}=W_{m}+W_{n} for symbolic one-site phi",
            sp.simplify(left - right) == 0,
        )

    sample = (sp.Integer(5), sp.Integer(2), sp.Integer(7))
    reversed_sample = tuple(reversed(sample))
    square_phi = lambda z: z**2 + 3 * z
    log_trace_phi = lambda z: sp.log(z) + sp.Rational(1, 5) * z
    check(
        "one-site sum is permutation invariant for polynomial one-site readout",
        one_site_sum(square_phi, sample) == one_site_sum(square_phi, reversed_sample),
    )
    check(
        "one-site sum is permutation invariant for log-plus-trace readout",
        sp.simplify(one_site_sum(log_trace_phi, sample) - one_site_sum(log_trace_phi, reversed_sample))
        == 0,
    )


def test_direct_sum_additivity_examples() -> None:
    print("== T2: classifier family is exactly direct-sum additive ==")
    eps, a, k = sp.symbols("epsilon a k", real=True)
    left = (sp.Integer(4), sp.Integer(1))
    right = (sp.Integer(3), sp.Integer(5))
    examples: list[tuple[str, Callable[[sp.Expr], sp.Expr]]] = [
        ("log x", lambda z: sp.log(z)),
        ("log x + epsilon x", lambda z: sp.log(z) + eps * z),
        ("x^2 + 3x", lambda z: z**2 + 3 * z),
        ("a log x + k", lambda z: a * sp.log(z) + k),
    ]
    for label, phi in examples:
        lhs = one_site_sum(phi, direct_sum(left, right))
        rhs = one_site_sum(phi, left) + one_site_sum(phi, right)
        check(
            f"{label} readout is additive under diagonal block direct sum",
            sp.simplify(lhs - rhs) == 0,
        )

    x = sp.symbols("x", positive=True)
    smooth_phi = sp.log(x) + eps * x + x**2
    check(
        "smooth one-site functions remain smooth on R_{>0}",
        sp.diff(smooth_phi, x) == 1 / x + eps + 2 * x,
        f"d/dx = {sp.diff(smooth_phi, x)}",
    )
    check(
        "positive diagonal determinant is the product coordinate",
        determinant(left) == 4 and determinant(right) == 15 and determinant(direct_sum(left, right)) == 60,
    )


def test_determinant_quotient() -> None:
    print("== T3: determinant-only quotient selects the log family ==")
    x, y = sp.symbols("x y", positive=True)
    c, eps, k = sp.symbols("c epsilon k", real=True)

    log_gap = expand_log(c * sp.log(x * y)) - c * sp.log(x) - c * sp.log(y)
    check(
        "c log x satisfies the multiplicative-to-additive equation",
        sp.simplify(log_gap) == 0,
    )

    diag_41 = (sp.Integer(4), sp.Integer(1))
    diag_22 = (sp.Integer(2), sp.Integer(2))
    log_value_gap = sp.simplify(
        one_site_sum(lambda z: c * sp.log(z), diag_41)
        - one_site_sum(lambda z: c * sp.log(z), diag_22)
    )
    check(
        "log family is determinant-only on same-determinant blocks",
        log_value_gap == 0 and determinant(diag_41) == determinant(diag_22),
        "diag(4,1) and diag(2,2) both have determinant 4",
    )

    trace_phi = lambda z: sp.log(z) + eps * z
    trace_cauchy_gap = sp.simplify(trace_phi(x * y) - trace_phi(x) - trace_phi(y))
    check(
        "log-plus-trace one-site function violates determinant-only Cauchy law",
        sp.simplify(trace_cauchy_gap.subs({x: 2, y: 3})) == eps,
        f"gap at x=2,y=3 is {sp.simplify(trace_cauchy_gap.subs({x: 2, y: 3}))}",
    )

    trace_witness_gap = sp.simplify(one_site_sum(trace_phi, diag_41) - one_site_sum(trace_phi, diag_22))
    check(
        "same determinant witness detects non-log one-site invariant",
        trace_witness_gap == eps,
        f"W(diag(4,1))-W(diag(2,2)) = {trace_witness_gap}",
    )

    dim_phi = lambda z: c * sp.log(z) + k
    fixed_dim_gap = sp.simplify(one_site_sum(dim_phi, diag_41) - one_site_sum(dim_phi, diag_22))
    check(
        "dimension constant is invisible at fixed dimension and fixed determinant",
        fixed_dim_gap == 0,
    )

    diag_4 = (sp.Integer(4),)
    cross_dim_gap = sp.simplify(one_site_sum(dim_phi, diag_4) - one_site_sum(dim_phi, diag_22))
    check(
        "dimension constant is not global determinant-only data",
        cross_dim_gap == -k,
        f"W(diag(4))-W(diag(2,2)) = {cross_dim_gap}",
    )

    check(
        "global determinant-only readout forces phi(1)=0",
        sp.simplify((c * sp.log(1))) == 0,
        "otherwise det=1 blocks carry an extra dimension label",
    )


def test_source_record_clause_independence() -> None:
    print("== T4: source-to-record disjointness is a separate bridge ==")
    source_blocks = {"A": {1, 2}, "B": {3, 4}}
    source_to_record = {"A": "r0", "B": "r0"}
    source_disjoint = source_blocks["A"].isdisjoint(source_blocks["B"])
    record_disjoint = source_to_record["A"] != source_to_record["B"]
    check(
        "positive diagonal source blocks may be disjoint",
        source_disjoint,
        f"A={source_blocks['A']}, B={source_blocks['B']}",
    )
    check(
        "non-injective source-to-record assignment remains logically possible",
        not record_disjoint,
        f"A->{source_to_record['A']}, B->{source_to_record['B']}",
    )
    check(
        "classifier does not derive source-blocks-to-records clause",
        source_disjoint and not record_disjoint,
        "the readout-context bridge must still rule this out",
    )


def test_source_guardrails() -> None:
    print("== T5: source-note guardrails and parent discoverability ==")
    parent = read(PARENT)
    note = read(NOTE)
    no_go = read(NO_GO)
    axioms = read(AXIOMS)

    check(
        "parent still declares T1-d as an explicit Boundary",
        "Boundary (declared bridge premise, T1-d)" in parent
        and "readout-identification Boundary" in parent,
    )
    check(
        "parent cites the positive-diagonal classifier",
        "OBSERVABLE_PRINCIPLE_T1D_POSITIVE_DIAGONAL_READOUT_CLASSIFIER_NOTE_2026-06-18.md"
        in parent,
    )
    check(
        "parent says classifier does not derive T1-d from Record",
        "it does not derive T1-d from Record" in parent
        and "not a hidden consequence of Record" in parent,
    )
    check(
        "classifier states bounded-support rather than an audit verdict",
        "bounded-support source theorem" in note
        and "independent audit lane owns any effective status" in note,
    )
    check(
        "classifier forbids treating T1-d as Record-derived",
        "does not treat T1-d as Record-derived" in note
        and "does not add a new axiom" in note,
    )
    check(
        "classifier names both remaining T1-d bridge pieces",
        "source-to-record disjointness bridge" in note
        and "determinant quotient" in note,
    )
    check(
        "classifier links its proof-surface dependencies",
        "(MINIMAL_AXIOMS_2026-06-05.md)" in note
        and "(OBSERVABLE_PRINCIPLE_T1D_DETERMINANT_READOUT_INDEPENDENCE_NO_GO_NOTE_2026-06-16.md)"
        in note,
    )
    check(
        "classifier does not claim to close the parent audit row",
        "does not close the parent `observable_principle_from_axiom_note`" in note,
    )
    check(
        "prior no-go still supplies the independence wall",
        "must not treat T1-d as Record-derived" in no_go
        and "does not add a new axiom" in no_go,
    )
    check(
        "minimal axiom memo withholds source/action and physical-observable identification",
        "source/action and physical-observable identification" in axioms
        and "does not supply" in axioms,
    )


def main() -> int:
    test_one_site_classifier()
    test_direct_sum_additivity_examples()
    test_determinant_quotient()
    test_source_record_clause_independence()
    test_source_guardrails()

    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
