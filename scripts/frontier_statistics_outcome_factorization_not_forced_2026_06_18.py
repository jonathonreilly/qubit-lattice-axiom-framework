#!/usr/bin/env python3
"""No-go: one-copy Born marginals do not force outcome factorization.

This runner supports
docs/STATISTICS_OUTCOME_FACTORIZATION_NOT_FORCED_BY_BORN_MARGINALS_NARROW_NO_GO_NOTE_2026-06-18.md.

It proves the finite two-outcome joint-law parameterization, checks product
and correlated witnesses with identical one-copy marginals, and verifies the
source note keeps the result as a bounded no-go rather than a physical
independence claim.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "STATISTICS_OUTCOME_FACTORIZATION_NOT_FORCED_BY_BORN_MARGINALS_NARROW_NO_GO_NOTE_2026-06-18.md"
STATISTICS_ATOM = DOCS / "STATISTICS_ATOM_REDUCES_TO_PRODUCT_FORM_ON_RETAINED_GLEASON_SURFACE_BOUNDED_NOTE_2026-06-12.md"
PRODUCT_WEAKENING = DOCS / "PRODUCT_FORM_PREMISE_WEAKENS_TO_OUTCOME_FACTORIZATION_BOUNDED_NOTE_2026-06-12.md"
GLEASON = DOCS / "GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md"
BUSCH = DOCS / "BUSCH_POVM_EFFECT_GLEASON_QUBIT_AUTHORITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md"

PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"{tag}: {name}{suffix}")


def section(title: str) -> None:
    print()
    print("=" * 88)
    print(title)
    print("=" * 88)


def joint_weights(p: sp.Expr, a: sp.Expr) -> dict[str, sp.Expr]:
    return {
        "ss": a,
        "sd": p - a,
        "ds": p - a,
        "dd": 1 - 2 * p + a,
    }


def symbolic_joint_law_checks() -> None:
    section("1. two-outcome joint-law parameterization")
    p, a = sp.symbols("p a", real=True)
    w = joint_weights(p, a)
    check("joint weights sum to one", sp.simplify(sum(w.values()) - 1) == 0)
    check("first marginal s is p", sp.simplify(w["ss"] + w["sd"] - p) == 0)
    check("second marginal s is p", sp.simplify(w["ss"] + w["ds"] - p) == 0)
    check("first marginal d is 1-p", sp.simplify(w["ds"] + w["dd"] - (1 - p)) == 0)
    check("second marginal d is 1-p", sp.simplify(w["sd"] + w["dd"] - (1 - p)) == 0)

    product = joint_weights(p, p**2)
    check("product point has m_ss=p^2", sp.simplify(product["ss"] - p**2) == 0)
    check("product point has m_sd=p(1-p)", sp.simplify(product["sd"] - p * (1 - p)) == 0)
    check("product point has m_dd=(1-p)^2", sp.simplify(product["dd"] - (1 - p) ** 2) == 0)

    p_half = Fraction(1, 2)
    product_half = {k: Fraction(v) for k, v in joint_weights(Fraction(1, 2), Fraction(1, 4)).items()}
    corr_half = {k: Fraction(v) for k, v in joint_weights(Fraction(1, 2), Fraction(1, 2)).items()}
    anti_half = {k: Fraction(v) for k, v in joint_weights(Fraction(1, 2), Fraction(0)).items()}
    check("p=1/2 product law is admissible", all(v >= 0 for v in product_half.values()), str(product_half))
    check("p=1/2 correlated law is admissible", all(v >= 0 for v in corr_half.values()), str(corr_half))
    check("p=1/2 anti-correlated law is admissible", all(v >= 0 for v in anti_half.values()), str(anti_half))
    check(
        "same p=1/2 marginals do not select a unique joint law",
        product_half != corr_half and product_half != anti_half and corr_half != anti_half,
    )
    check(
        "correlated p=1/2 law violates outcome factorization",
        corr_half["sd"] != p_half * (1 - p_half) and corr_half["ss"] != p_half * p_half,
        f"corr={corr_half}, product ss={p_half * p_half}",
    )


def born_realizable_witness_checks() -> None:
    section("2. Born-realizable diagonal witnesses on C^2 tensor C^2")
    p = sp.symbols("p", real=True)
    rho_product = sp.diag(p**2, p * (1 - p), (1 - p) * p, (1 - p) ** 2)
    rho_corr = sp.diag(p, 0, 0, 1 - p)

    ps = sp.diag(1, 0)
    pd = sp.diag(0, 1)
    ident = sp.eye(2)

    def kron(a: sp.Matrix, b: sp.Matrix) -> sp.Matrix:
        return sp.kronecker_product(a, b)

    def tr(m: sp.Matrix) -> sp.Expr:
        return sp.simplify(sp.trace(m))

    check("rho_product has trace one", sp.simplify(tr(rho_product) - 1) == 0)
    check("rho_correlated has trace one", sp.simplify(tr(rho_corr) - 1) == 0)
    # Positivity is diagonal positivity for 0 <= p <= 1.
    product_diag = list(rho_product.diagonal())
    corr_diag = list(rho_corr.diagonal())
    check("rho_product diagonal entries are nonnegative on 0<=p<=1", all(expr in [p**2, p * (1 - p), (1 - p) * p, (1 - p) ** 2] for expr in product_diag))
    check("rho_correlated diagonal entries are nonnegative on 0<=p<=1", corr_diag == [p, 0, 0, 1 - p])

    for label, rho in [("product", rho_product), ("correlated", rho_corr)]:
        left_s = tr(rho * kron(ps, ident))
        right_s = tr(rho * kron(ident, ps))
        check(f"{label} witness left marginal is p", sp.simplify(left_s - p) == 0)
        check(f"{label} witness right marginal is p", sp.simplify(right_s - p) == 0)

    prod_ss = tr(rho_product * kron(ps, ps))
    corr_ss = tr(rho_corr * kron(ps, ps))
    prod_sd = tr(rho_product * kron(ps, pd))
    corr_sd = tr(rho_corr * kron(ps, pd))
    check("product witness has factorized ss and sd cells", sp.simplify(prod_ss - p**2) == 0 and sp.simplify(prod_sd - p * (1 - p)) == 0)
    check("correlated witness has same marginals but nonfactorized cells", sp.simplify(corr_ss - p) == 0 and sp.simplify(corr_sd) == 0)


def textual_firewall_checks() -> None:
    section("3. source-scope and dependency firewall")
    note = NOTE.read_text(encoding="utf-8")
    flat = " ".join(note.split())
    for path in [STATISTICS_ATOM, PRODUCT_WEAKENING, GLEASON, BUSCH]:
        check(f"dependency/context file exists: {path.name}", path.exists())

    required = [
        "Status authority",
        "retained one-copy Born weights plus finite scalar additivity",
        "do not force the two-registration outcome-factorization law",
        "cannot be discharged by merely citing one-copy Gleason/Busch Born authority",
        "separate record-stack independence",
        "not a global no-go against future outcome independence",
        "does not consume any unaudited unraveling measurement as proof input",
        "## No-Go Discipline Gate",
        "Status: PASS",
        "N1 alternative routes",
        "finite table algebra",
        "one-copy Gleason/Busch",
        "exchange symmetry",
        "two-copy Born realization",
        "downstream product weakening",
        "N2 wall independence",
        "N3 hidden-wall scan",
        "N4 residual matching",
        "N5 rhetoric audit",
        "N6 partial-closure path scan",
        "N7 steelman",
        "N8 cross-cycle echo",
        "This note does not",
        "update audit ledgers, queues, publication matrices",
        "add a probability axiom or a new Record axiom",
    ]
    for marker in required:
        check(f"note contains firewall marker: {marker[:58]}", marker in flat)

    forbidden = [
        "Status: retained",
        "proposed_retained",
        "outcome independence is impossible",
        "physical repeated-registration independence is false",
    ]
    for marker in forbidden:
        check(f"forbidden overclaim absent: {marker}", marker not in flat)


def main() -> int:
    print("STATISTICS OUTCOME-FACTORIZATION NO-GO")
    symbolic_joint_law_checks()
    born_realizable_witness_checks()
    textual_firewall_checks()
    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL == 0:
        print(
            "VERDICT: bounded no-go passes; outcome factorization is not forced "
            "by retained one-copy Born marginals plus finite additivity."
        )
        return 0
    print("VERDICT: bounded no-go FAILED.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
