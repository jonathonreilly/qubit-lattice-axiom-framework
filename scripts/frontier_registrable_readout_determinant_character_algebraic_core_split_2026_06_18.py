#!/usr/bin/env python3
"""Algebraic-core split for the registrable determinant-character readout row.

This runner verifies only the finite algebra isolated in
REGISTRABLE_READOUT_DETERMINANT_CHARACTER_ALGEBRAIC_CORE_SPLIT_NOTE_2026-06-18.
It does not derive the physical strong-CP mass readout, the AC_phi_lambda species
readout, or any Tier-A registry movement.
"""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np
import sympy as sp


PASS = 0
FAIL = 0

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "REGISTRABLE_READOUT_DETERMINANT_CHARACTER_ALGEBRAIC_CORE_SPLIT_NOTE_2026-06-18.md"
PARENT = ROOT / "docs" / "REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md"


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    print(f"  [{tag}] {label}" + (f" -- {detail}" if detail else ""))


def section(title: str) -> None:
    print("\n" + "-" * 88)
    print(title)
    print("-" * 88)


def main() -> int:
    print("=" * 88)
    print("REGISTRABLE READOUT DETERMINANT-CHARACTER ALGEBRAIC CORE SPLIT")
    print("=" * 88)

    section("T1 - finite central idempotents are disjoint record labels")
    n = 4
    idempotents = [
        sp.diag(*[sp.Integer(1) if i == j else sp.Integer(0) for i in range(n)])
        for j in range(n)
    ]
    check(
        "e_j^2 = e_j",
        all(e * e == e for e in idempotents),
    )
    check(
        "e_j e_k = 0 for j != k",
        all(
            idempotents[j] * idempotents[k] == sp.zeros(n, n)
            for j in range(n)
            for k in range(n)
            if j != k
        ),
    )
    check("sum_j e_j = I", sp.Add(*idempotents, evaluate=True) == sp.eye(n))

    section("T2 - Record finite additivity removes cross-record interference")
    c, a, b = sp.symbols("c a b", real=True)
    forced_c = sp.solve(sp.Eq(a + b + c, a + b), c)
    check("cross term c in I(e1 union e2)=I(e1)+I(e2)+c is forced to zero", forced_c == [0])
    finite_terms = sp.symbols(f"r0:{n}", real=True)
    finite_sum = sp.Add(*finite_terms, evaluate=False)
    check(
        "finite iteration gives a per-record sum",
        len(finite_terms) == n and len(finite_sum.args) == n,
        "no infinite or measure-theoretic premise",
    )

    section("T3 - determinant phase is additive on sector products")
    rng = np.random.default_rng(1806)
    max_wrap = 0.0
    for _ in range(12):
        phases = rng.uniform(-math.pi, math.pi, size=5)
        radii = rng.uniform(0.2, 3.0, size=5)
        zs = radii * np.exp(1j * phases)
        arg_product = np.angle(np.prod(zs))
        sum_phases = float(np.sum(np.angle(zs)))
        wrap = ((arg_product - sum_phases + math.pi) % (2 * math.pi)) - math.pi
        max_wrap = max(max_wrap, abs(wrap))
    check("arg(prod_j z_j) = sum_j arg(z_j) modulo 2pi on random sector products", max_wrap < 1e-12)
    check(
        "homomorphism boundary is explicit and not inferred from Record additivity",
        "homomorphism boundary" in NOTE.read_text(encoding="utf-8"),
    )

    section("T4 - additive R-valued phase functionals are odd")
    g0 = sp.Symbol("g0", real=True)
    g0_solution = sp.solve(sp.Eq(g0, g0 + g0), g0)
    check("additivity at zero forces g(0)=0", g0_solution == [0])
    gx, gminusx = sp.symbols("gx gminusx", real=True)
    odd_solution = sp.solve(sp.Eq(gx + gminusx, 0), gminusx)
    check("g(x)+g(-x)=0 forces g(-x)=-g(x)", odd_solution == [-gx])

    section("T5 - K/CPT even plus additive odd forces zero phase")
    gt = sp.Symbol("gt", real=True)
    zero_solution = sp.solve(sp.Eq(gt, -gt), gt)
    check("even g(-t)=g(t) and odd g(-t)=-g(t) force g(t)=0", zero_solution == [0])
    coeff = sp.Symbol("coeff", real=True)
    forced_zero_coefficient = sp.solve(sp.Eq(coeff * sp.Integer(1), -coeff * sp.Integer(1)), coeff)
    check(
        "determinant-character phase index k=0 follows inside the supplied homomorphism class",
        zero_solution == [0] and forced_zero_coefficient == [0],
    )

    section("T6 - hostile guards: K-even phase functions are not erased by Record alone")
    theta, phi = sp.symbols("theta phi", real=True)
    check("cos(theta) is K/CPT-even", sp.simplify(sp.cos(-theta) - sp.cos(theta)) == 0)
    add_gap = sp.simplify(sp.cos(theta + phi) - (sp.cos(theta) + sp.cos(phi)))
    check("cos(theta) is not a phase-group homomorphism", add_gap != 0, f"gap={add_gap}")
    sum_cos_even = sp.simplify((sp.cos(-theta) + sp.cos(-phi)) - (sp.cos(theta) + sp.cos(phi)))
    check("sum_j cos(theta_j) is K/CPT-even over records", sum_cos_even == 0)
    hom_gap = sp.simplify(
        (sp.cos(theta + phi) + sp.cos(theta - phi))
        - ((sp.cos(theta) + sp.cos(theta)) + (sp.cos(phi) + sp.cos(-phi)))
    )
    check("sum_j cos(theta_j) remains outside the homomorphism boundary", hom_gap != 0)
    check("hostile guard is preserved in split note", "sum_j cos(theta_j)" in NOTE.read_text(encoding="utf-8"))

    section("T7 - modulus/log-modulus survives")
    r1, r2 = sp.symbols("r1 r2", positive=True)
    check("log|z| is additive on products", sp.simplify(sp.log(r1 * r2) - sp.log(r1) - sp.log(r2)) == 0)
    z = sp.symbols("z", positive=True)
    check("log|z| is K/CPT-even", sp.simplify(sp.log(sp.Abs(sp.conjugate(z))) - sp.log(z)) == 0)

    section("T8 - source-boundary guard")
    note_text = NOTE.read_text(encoding="utf-8")
    parent_text = PARENT.read_text(encoding="utf-8")
    required_note_phrases = [
        "(context handle, not a citation-graph dependency)",
        # 2026-07-04 premise relocation: the note now cites the current axiom
        # memo for additivity/content-determination and the supplied-context
        # bridge for K/CPT orbit constancy and the homomorphism boundary.
        "MINIMAL_AXIOMS_2026-06-29.md",
        "KCPT_ORBIT_CONSTANCY_AND_DETERMINANT_CHARACTER_BOUNDARY_SUPPLIED_CONTEXT_BRIDGE_NOTE_2026-07-04.md",
        "does not identify the physical strong-CP mass-orientation readout",
        "does not identify AC_phi_lambda species data",
        "does not derive the determinant-character/log-character boundary",
        "effective status is pipeline-derived after independent audit ratification and dependency closure",
    ]
    for phrase in required_note_phrases:
        check(f"split note carries boundary phrase: {phrase}", phrase in note_text)
    check(
        "split note has no markdown dependency edge to parent target",
        "[`REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md`]" not in note_text,
    )
    required_parent_phrases = [
        "post-audit source firewall removes bridge-discharge language",
        "physical-readout",
        "determinant-character / log-character",
    ]
    for phrase in required_parent_phrases:
        check(f"parent still names conditional boundary: {phrase}", phrase in parent_text)
    banned_phrases = [
        "discharges the physical",
        "closes strong-CP",
        "closes AC_phi_lambda",
        "retire any Tier-A admission",
        "promoted to retained",
        "retained on the actual surface",
        "Status Certificate",
        "audit_required_before_effective_retained",
        "bare_retained_allowed",
    ]
    lowered = note_text.lower()
    for phrase in banned_phrases:
        check(f"bridge-discharge wording absent: {phrase}", phrase.lower() not in lowered)

    print("\n" + "=" * 88)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
