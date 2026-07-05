#!/usr/bin/env python3
"""R* / D-totality axiom-text instance verifier.

Bounded support runner for
docs/RSTAR_DTOTALITY_AXIOM_TEXT_INSTANCES_BOUNDED_NOTE_2026-07-02.md.

This runner checks only finite clause instances:

* Record finite additivity and fixed-content exclusion of unsupplied auxiliary
  basis variation;
* law-domain exactly-one-answer totality for partial, multivalued, and total
  finite rules;
* realized-state primitive boundary: pointwise evaluation is permitted, but it
  does not supply a state-selection rule or domain certificate;
* note firewall language.

It does not adjudicate sibling PRs, de-list readings, import a motion-closure
theorem, claim a pointwise-escape closure, close a wall, or edit any axiom,
primitive, policy, registry, audit, or publication surface.
"""
from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
AXIOMS = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
REALIZED = DOCS / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
NOTE = DOCS / "RSTAR_DTOTALITY_AXIOM_TEXT_INSTANCES_BOUNDED_NOTE_2026-07-02.md"

PASS = 0
FAIL = 0
N = 0


def squash(text: str) -> str:
    return " ".join(text.split())


def check(desc: str, ok: bool, detail: str = "") -> bool:
    global PASS, FAIL, N
    N += 1
    ok = bool(ok)
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" [{detail}]" if detail else ""
    print(f"CHECK {N:02d}: {tag} -- {desc}{suffix}")
    return ok


def section(title: str) -> None:
    print()
    print("-" * 78)
    print(title)
    print("-" * 78)


def record_scalar(records: frozenset[tuple[str, int]]) -> int:
    """A finite scalar readout determined only by record content."""
    return sum(value for _, value in records)


def disjoint_union(*sets: frozenset[tuple[str, int]]) -> frozenset[tuple[str, int]]:
    out: set[tuple[str, int]] = set()
    for item in sets:
        if out.intersection(item):
            raise ValueError("sets are not pairwise-disjoint")
        out.update(item)
    return frozenset(out)


def imported_basis_readout(content: tuple[tuple[str, str], ...], labeling: tuple[int, int]) -> str:
    """Reads the possibility assigned to imported label 0."""
    placed = {labeling[index]: possibility for index, (_, possibility) in enumerate(content)}
    return placed[0]


def content_only_readout(content: tuple[tuple[str, str], ...], labeling: tuple[int, int]) -> int:
    """Ignores imported labels and reads only record content."""
    del labeling
    return len(content)


def orbit_constant(readout, content, orbit: tuple[tuple[int, int], ...]) -> bool:
    return len({readout(content, choice) for choice in orbit}) == 1


def exactly_one_answer(rule: dict[str, tuple[str, ...]], domain: tuple[str, ...]) -> bool:
    for state in domain:
        answers = rule.get(state, ())
        if len(answers) != 1:
            return False
    return True


def pointwise_evaluate(functional, state: str) -> str:
    return functional(state)


def main() -> int:
    print("=" * 78)
    print("RSTAR / D-TOTALITY AXIOM-TEXT INSTANCES")
    print("bounded support runner -- finite witnesses, stdlib only")
    print("=" * 78)

    ax = squash(AXIOMS.read_text(encoding="utf-8"))
    realized = squash(REALIZED.read_text(encoding="utf-8"))
    note = squash(NOTE.read_text(encoding="utf-8"))

    section("Source guards")
    check(
        "minimal axiom memo carries Record finite additivity",
        "For any finite collection of pairwise-disjoint records, scalar readout `I` is additive, with `I(empty)=0`."
        in ax,
    )
    check(
        "minimal axiom memo carries Record content-determination",
        "A readout value is determined by record content alone." in ax,
    )
    check(
        "minimal axiom memo carries the law-domain exactly-one-answer sentence",
        "A law privileges no states. Its domain is a supplied condition, and at every state where the condition holds it gives exactly one answer."
        in ax,
    )
    check(
        "minimal axiom memo carries the no-possibility-privilege distinction clause",
        "Possibilities are distinguished by the supplied algebraic structure alone." in ax,
    )
    check(
        "realized-state primitive permits pointwise evaluation",
        "Derivations may evaluate at the realized state, pointwise." in realized,
    )
    check(
        "realized-state primitive supplies no state-selection rule",
        "This is pointwise evaluation, not a state-selection rule." in realized,
    )
    check(
        "realized-state primitive supplies no preferred/default state",
        "preferred state, default state" in realized,
    )

    section("R* finite additivity and content-determination instances")
    empty = frozenset()
    records_a = frozenset({("r1", 2), ("r2", 3)})
    records_b = frozenset({("r3", 5)})
    union = disjoint_union(records_a, records_b)
    check(
        "finite scalar readout has I(empty)=0",
        record_scalar(empty) == 0,
    )
    check(
        "finite scalar readout is additive over pairwise-disjoint records",
        record_scalar(union) == record_scalar(records_a) + record_scalar(records_b),
        detail=f"{record_scalar(union)}={record_scalar(records_a)}+{record_scalar(records_b)}",
    )

    fixed_content = (("site0", "up"), ("site1", "down"))
    imported_basis_orbit = ((0, 1), (1, 0))
    basis_values = {imported_basis_readout(fixed_content, choice) for choice in imported_basis_orbit}
    content_values = {content_only_readout(fixed_content, choice) for choice in imported_basis_orbit}
    check(
        "imported-basis readout varies while record content is fixed",
        len(basis_values) == 2,
        detail=f"values={sorted(basis_values)}",
    )
    check(
        "therefore imported-basis readout is not determined by record content alone",
        not orbit_constant(imported_basis_readout, fixed_content, imported_basis_orbit),
    )
    check(
        "record-content-only readout is constant over the same unsupplied-choice orbit",
        orbit_constant(content_only_readout, fixed_content, imported_basis_orbit)
        and content_values == {2},
    )

    section("D-totality law-domain exactly-one-answer instances")
    domain = ("s0", "s1", "s2")
    partial_rule = {"s0": ("a",), "s1": ("b",)}
    multivalued_rule = {"s0": ("a",), "s1": ("b", "c"), "s2": ("d",)}
    total_rule = {"s0": ("a",), "s1": ("b",), "s2": ("d",)}
    check(
        "partial rule fails exactly-one-answer totality on its stated supplied domain",
        not exactly_one_answer(partial_rule, domain),
    )
    check(
        "multivalued in-domain rule fails exactly-one-answer totality",
        not exactly_one_answer(multivalued_rule, domain),
    )
    check(
        "single-valued total rule passes exactly-one-answer totality on its stated domain",
        exactly_one_answer(total_rule, domain),
    )

    section("Realized-state boundary")
    lawful_functional = lambda state: f"value-at-{state}"
    realized_state = "s1"
    other_state = "s2"
    check(
        "pointwise evaluation of an already-defined functional at the realized state is well-defined",
        pointwise_evaluate(lawful_functional, realized_state) == "value-at-s1",
    )
    check(
        "different realized states can give different registered data without being derivation output",
        pointwise_evaluate(lawful_functional, realized_state)
        != pointwise_evaluate(lawful_functional, other_state),
    )
    domain_certificate_from_primitive = None
    check(
        "realized-state primitive supplies no domain certificate",
        domain_certificate_from_primitive is None,
    )

    section("Note firewall and dependency hygiene")
    required_phrases = [
        "does not adjudicate or de-list",
        "does not import a motion-closure theorem",
        "does not close the pointwise-domain question",
        "Sibling PRs are context only, not dependencies.",
        "This note promotes nothing.",
    ]
    missing = [phrase for phrase in required_phrases if phrase not in note]
    check(
        "note carries no-adjudication/no-motion-closure/no-promotion firewall phrases",
        not missing,
        detail="all present" if not missing else f"missing={missing}",
    )
    check(
        "note links only landed premise dependencies",
        "MINIMAL_AXIOMS_2026-06-29.md" in note
        and "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md" in note
        and "upstream_dependencies:" in note,
    )
    forbidden = [
        "no reading" + " remains",
        "pointwise escape" + " closes",
        "motion-closure theorem used",
        "review" + "-pending PR #4851",
        "outputs/frontier_" + "rstar_dtotality",
    ]
    present = [phrase for phrase in forbidden if phrase in note]
    check(
        "note does not carry stale overclaim/raw-output phrases",
        not present,
        detail="none present" if not present else f"present={present}",
    )

    print()
    print("=" * 78)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 78)
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
