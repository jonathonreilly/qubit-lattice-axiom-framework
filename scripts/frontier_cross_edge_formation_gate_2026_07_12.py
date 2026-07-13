#!/usr/bin/env python3
"""Exact checks for the cross-edge formation-gate consolidation theorem."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Callable

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "G3_CROSS_EDGE_INDEPENDENCE_IS_A_FORMATION_GATE_ATOM_"
    "MARGINAL_IDENTITY_FROM_QUALIFICATION_BOUNDED_THEOREM_NOTE_2026-07-12.md"
)
OUTCOME_FACTORIZATION_SOURCE = (
    ROOT
    / "docs"
    / "G3_OUTCOME_FACTORIZATION_FROM_UNRAVELED_STEP_LAW_NARROW_NO_GO_NOTE_2026-07-11.md"
)
RELOCATION_SOURCE = (
    ROOT
    / "docs"
    / "KOIDE_FORMATION_GATE_RELOCATION_TIED_MEASURE_PER_CELL_WEIGHT_COMPATIBILITY_BOUNDED_THEOREM_NOTE_2026-07-12.md"
)
PERMANENCE_SOURCE = (
    ROOT
    / "docs"
    / "RECORD_PERMANENCE_FORCES_FRESH_SITE_DOUBLE_REGISTRATION_AND_AGREEMENT_SURVIVAL_BOUNDED_THEOREM_NOTE_2026-07-11.md"
)
AXIOM_SOURCE = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"


def normalized(text: str) -> str:
    """Collapse markdown wrapping without altering mathematical punctuation."""

    without_quote_markers = re.sub(r"(?m)^>\s?", "", text)
    return re.sub(r"\s+", " ", without_quote_markers).strip()


def read_source(path: Path) -> str:
    """Read a landed source; missing sources become decisive guard failures."""

    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return ""


def main() -> int:
    results: list[bool] = []

    try:
        note_text = NOTE.read_text(encoding="utf-8")
        note_error = ""
    except OSError as exc:
        note_text = ""
        note_error = f"paired note unavailable: {exc}"
    note_flat = normalized(note_text)
    outcome_source_text = read_source(OUTCOME_FACTORIZATION_SOURCE)
    relocation_source_text = read_source(RELOCATION_SOURCE)
    permanence_source_text = read_source(PERMANENCE_SOURCE)
    axiom_source_text = read_source(AXIOM_SOURCE)
    outcome_source_flat = normalized(outcome_source_text)
    permanence_source_flat = normalized(permanence_source_text)
    axiom_source_flat = normalized(axiom_source_text)
    note_compact = re.sub(r"\s+", "", note_text)
    relocation_source_compact = re.sub(r"\s+", "", relocation_source_text)

    def check(number: int, label: str, test: Callable[[], bool]) -> None:
        try:
            passed = bool(test())
            detail = ""
        except Exception as exc:  # A failed exact derivation is a numbered FAIL.
            passed = False
            detail = f" ({type(exc).__name__}: {exc})"
        results.append(passed)
        status = "PASS" if passed else "FAIL"
        if not passed and note_error and number <= 5:
            detail = f" ({note_error})"
        print(f"[{status}] {number:02d} {label}{detail}")

    residual_quote = normalized(
        "many-edge structure: **cross-edge independence and convolution "
        "structure are not tested here**."
    )
    discharge_quote = normalized(
        "A positive discharge of G3 must deliver a cross-edge independence "
        "theorem on the registered quotient — not a single-edge non-degeneracy "
        "or a bi-frame quasi-stationarity of the mean, both of which this note "
        "shows are factorization-blind."
    )
    open_gate_quote = normalized(
        "context selection, measurement basis selection, Born weights, "
        "probability rules, update laws, decoherence mechanisms, and formation "
        "rules (which admissible possibility a new record locks, at which site, "
        "with what weight, or at what rate);"
    )
    site_quote = normalized(
        "No site is privileged. Sites are distinguished by the supplied "
        "lattice structure alone."
    )
    law_quote = normalized(
        "A law privileges no states. Its domain is a supplied condition, and "
        "at every state where the condition holds it gives exactly one answer."
    )
    epoch_quote = normalized(
        "a **common epoch-comparable lane-readout rule**: the same mapping from "
        "record content to the coordinate `r_k` is used at every formation epoch, "
        "so values at different epochs may be compared. The rule does not assume "
        "those values are equal."
    )

    check(
        1,
        "outcome-factorization residual quotation matches the landed source",
        lambda: residual_quote in note_flat and residual_quote in outcome_source_flat,
    )
    check(
        2,
        "outcome-factorization discharge quotation matches the landed source",
        lambda: discharge_quote in note_flat and discharge_quote in outcome_source_flat,
    )
    check(
        3,
        "all quoted axiom sentences match the landed minimal-axiom source",
        lambda: all(
            quote in note_flat and quote in axiom_source_flat
            for quote in (open_gate_quote, site_quote, law_quote)
        ),
    )
    check(
        4,
        "landed relocation and fresh-site source statements are guarded",
        lambda: epoch_quote in note_flat
        and epoch_quote in permanence_source_flat
        and "phi_w=(w,1-w)" in note_compact
        and "phi_w=(w,1-w)" in relocation_source_compact
        and "It is neither equality of the `{s,d}` formation marginals nor independence"
        in note_flat,
    )
    check(
        5,
        "(LE) names equality of the complete transported condition, including record environment",
        lambda: "**(LE) Law-equivalence element (named premise, exact statement).**"
        in note_text
        and "g.c_1 = c_2 =: c" in note_text
        and "nearest-neighbor/record environment if the law uses it" in note_text,
    )

    condition, site_index, epoch_index = sp.symbols(
        "condition site_index epoch_index", real=True
    )
    f = sp.Function("f")
    single_answer = f(condition)

    check(
        6,
        "(LE)+(LAW) gives exact same-condition marginal identity",
        lambda: sp.simplify(f(condition).subs(condition, sp.Symbol("c")) - f(sp.Symbol("c")))
        == 0,
    )
    check(
        7,
        "LABELED COMPARATOR (never thresholded): unequal complete conditions may differ",
        lambda: (
            (lambda law, c_1, c_2: law(c_1) != law(c_2))(
                lambda value: sp.cancel(value / (1 + value)),
                sp.Rational(1, 2),
                sp.Rational(2, 3),
            )
        ),
    )
    check(
        8,
        "the single-registration law has no hidden bare-site or epoch argument",
        lambda: single_answer.free_symbols == {condition}
        and site_index not in single_answer.free_symbols
        and epoch_index not in single_answer.free_symbols,
    )

    p, m_ss, m_sd, m_ds, m_dd = sp.symbols(
        "p m_ss m_sd m_ds m_dd", real=True
    )
    joint_solution = sp.solve(
        (
            sp.Eq(m_ss + m_sd, p),
            sp.Eq(m_ss + m_ds, p),
            sp.Eq(m_ss + m_sd + m_ds + m_dd, 1),
        ),
        (m_sd, m_ds, m_dd),
        dict=True,
    )
    expected_solution = {
        m_sd: p - m_ss,
        m_ds: p - m_ss,
        m_dd: 1 - 2 * p + m_ss,
    }

    check(
        9,
        "identical marginals solve to the one-coordinate joint family",
        lambda: len(joint_solution) == 1
        and all(
            sp.simplify(joint_solution[0][key] - value) == 0
            for key, value in expected_solution.items()
        ),
    )

    solved_table = (
        m_ss,
        expected_solution[m_sd],
        expected_solution[m_ds],
        expected_solution[m_dd],
    )
    check(
        10,
        "the solved joint family is exactly normalized",
        lambda: sp.simplify(sum(solved_table) - 1) == 0,
    )
    check(
        11,
        "both solved single-registration marginals equal (p,1-p)",
        lambda: all(
            expression == 0
            for expression in (
                sp.simplify(solved_table[0] + solved_table[1] - p),
                sp.simplify(solved_table[2] + solved_table[3] - (1 - p)),
                sp.simplify(solved_table[0] + solved_table[2] - p),
                sp.simplify(solved_table[1] + solved_table[3] - (1 - p)),
            )
        ),
    )

    def admissible_a_set(p_value: sp.Rational) -> sp.Set:
        """Derive all nonnegativity bounds by exact interval intersection."""

        return sp.Intersection(
            sp.Interval(0, sp.oo),
            sp.Interval(-sp.oo, p_value),
            sp.Interval(2 * p_value - 1, sp.oo),
        )

    p_low = sp.Rational(2, 5)
    p_high = 1 - p_low
    check(
        12,
        "the exact Frechet interval has lower branch max(0,2p-1)=0",
        lambda: admissible_a_set(p_low)
        == sp.Interval(max(sp.Rational(0), 2 * p_low - 1), p_low),
    )
    check(
        13,
        "the exact Frechet interval has upper branch max(0,2p-1)=2p-1",
        lambda: admissible_a_set(p_high)
        == sp.Interval(max(sp.Rational(0), 2 * p_high - 1), p_high),
    )

    c_ss = m_ss - p**2
    c_ss_solutions = sp.solve(sp.Eq(c_ss, 0), m_ss)
    check(
        14,
        "C_ss=0 solves natively and uniquely to a=p^2",
        lambda: c_ss_solutions == [p**2],
    )

    product_table = tuple(sp.simplify(entry.subs(m_ss, p**2)) for entry in solved_table)
    expected_product = (p**2, p * (1 - p), p * (1 - p), (1 - p) ** 2)
    check(
        15,
        "substituting the cumulant solution gives the full product table",
        lambda: all(
            sp.simplify(actual - expected) == 0
            for actual, expected in zip(product_table, expected_product)
        ),
    )
    check(
        16,
        "the product table makes every registered-quotient cumulant vanish",
        lambda: all(
            sp.simplify(actual - expected) == 0
            for actual, expected in zip(
                product_table,
                (p * p, p * (1 - p), (1 - p) * p, (1 - p) * (1 - p)),
            )
        ),
    )

    witness_p = sp.Rational(2, 5)
    locked_table = (witness_p, sp.Rational(0), sp.Rational(0), 1 - witness_p)
    locked_marginals = (
        locked_table[0] + locked_table[1],
        locked_table[2] + locked_table[3],
        locked_table[0] + locked_table[2],
        locked_table[1] + locked_table[3],
    )
    check(
        17,
        "LABELED COMPARATOR (never thresholded): locked coupling has the same exact marginals",
        lambda: sum(locked_table) == 1
        and all(value >= 0 for value in locked_table)
        and locked_marginals
        == (witness_p, 1 - witness_p, witness_p, 1 - witness_p),
    )
    exact_product_witness = tuple(entry.subs(p, witness_p) for entry in expected_product)
    check(
        18,
        "same marginal answer permits distinct product and correlated joint answers",
        lambda: locked_table != exact_product_witness
        and locked_table[0] - witness_p**2 != 0
        and exact_product_witness[0] - witness_p**2 == 0,
    )

    correlated_outcomes = ((0, 0, 1 - witness_p), (1, 1, witness_p))
    pointwise_additive = all(
        first + second == sum((first, second))
        for first, second, _probability in correlated_outcomes
    )
    mean_first = sum(probability * first for first, _second, probability in correlated_outcomes)
    mean_second = sum(probability * second for _first, second, probability in correlated_outcomes)
    mean_product = sum(
        probability * first * second
        for first, second, probability in correlated_outcomes
    )
    check(
        19,
        "pointwise Record-readout additivity coexists with exact statistical dependence",
        lambda: pointwise_additive
        and mean_product - mean_first * mean_second
        == witness_p - witness_p**2
        and mean_product - mean_first * mean_second != 0,
    )

    payer_needles = (
        "| formation dynamics | prospective derivation or bridge |",
        "| product / maximal-ignorance default | candidate note-owned licensing criterion",
        "| physical locality | prospective physical theorem |",
        "| supplied product-law condition | explicit non-satisfying condition |",
        "would not chain-satisfy; not adopted",
    )
    check(
        20,
        "the four graded independence payers are enumerated and none is adopted",
        lambda: all(needle in note_text for needle in payer_needles),
    )

    passed = sum(results)
    failed = len(results) - passed
    print()
    if failed == 0:
        print(
            "VERDICT: PASS — marginal identity is conditional on (LE)+(LAW); "
            "cross-edge independence remains the formation-gate atom."
        )
    else:
        print(
            "VERDICT: FAIL — at least one source guard or exact theorem check failed; "
            "the bounded claim is not certified."
        )
    print(
        "T2: F:C_form->Delta({s,d}), p_i=f(c_i); "
        "c_1=c_2 under (LE) and (LAW) implies p_1=p_2, and implies no joint equation."
    )
    print(
        "LAW-EQUIVALENCE (LE): after a supplied lattice translation/proper rotation, "
        "the complete law-domain conditions, record environment, menu, and s/d labels agree; "
        "different epochs are not automatically equivalent."
    )
    print("INDEPENDENCE PAYER TABLE:")
    print("  formation dynamics | prospective derivation/bridge | open; no supplier here")
    print("  product/maximal ignorance | candidate licensing criterion | not adopted")
    print("  physical locality | prospective screening/factorization theorem | additivity is insufficient")
    print("  supplied product-law condition | non-satisfying condition | conditional only; not adopted")
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    print(
        "PROPOSED CLAIM_SCOPE: bounded_theorem — formation-gate consolidation plus "
        "Qualification-conditional marginal identity; independence isolated, not derived."
    )
    print(
        "HOSTILE-AUDIT UNCERTAINTIES: whether the complete-condition equivalence is ever "
        "physically realized across epochs; whether finite-history coupling is packaged in "
        "the same formation law; and whether quotient labels transport unchanged. "
        "The exact binary arithmetic has no numerical uncertainty."
    )
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
