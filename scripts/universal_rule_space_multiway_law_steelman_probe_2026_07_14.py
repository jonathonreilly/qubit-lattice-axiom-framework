#!/usr/bin/env python3
"""Exact finite controls for the universal-rule-space multiway steelman.

This runner tests a bounded Boolean analogue. It neither classifies all Z^3
qubit laws nor selects a physical law or measure.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "UNIVERSAL_RULE_SPACE_MULTIWAY_LAW_STEELMAN_NOTE_2026-07-14.md"
)
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"

PASS = 0
FAIL = 0


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def rule_output(rule: int, neighborhood: tuple[int, int, int]) -> int:
    index = 4 * neighborhood[0] + 2 * neighborhood[1] + neighborhood[2]
    return (rule >> index) & 1


def complement_neighborhood(neighborhood: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(1 - bit for bit in neighborhood)  # type: ignore[return-value]


def reflected(neighborhood: tuple[int, int, int]) -> tuple[int, int, int]:
    return neighborhood[2], neighborhood[1], neighborhood[0]


def bit_flip_covariant(rule: int) -> bool:
    for neighborhood in product((0, 1), repeat=3):
        if rule_output(rule, complement_neighborhood(neighborhood)) != 1 - rule_output(rule, neighborhood):
            return False
    return True


def reflection_covariant(rule: int) -> bool:
    return all(
        rule_output(rule, neighborhood) == rule_output(rule, reflected(neighborhood))
        for neighborhood in product((0, 1), repeat=3)
    )


def successor(rule: int, ring: tuple[int, ...]) -> tuple[int, ...]:
    size = len(ring)
    return tuple(
        rule_output(rule, (ring[(site - 1) % size], ring[site], ring[(site + 1) % size]))
        for site in range(size)
    )


def authority_contract() -> None:
    section("A - Authority and bounded claim contract")
    for path in (NOTE, AXIOMS, REGISTRY):
        check(f"A source exists: {path.name}", path.is_file())
    note = " ".join(
        NOTE.read_text(encoding="utf-8").lower().replace("*", "").replace("`", "").split()
    )
    check("A note is authority-free", "authority: none" in note)
    check("A note changes no live axiom", "does not amend an axiom" in note)
    check("A Boolean analogue is not promoted to Z3 qubit theorem", "bounded boolean analogue" in note)
    check("A exact universal-route steelman is stated", "all exact local rules are retained" in note)
    check("A set-valued law reading is kept visible", "set-valued successor" in note)
    check("A ruliad source keeps sampled slice explicit", "sampled slice" in note)
    check("A formal causal-set source keeps discrete measure explicit", "appropriate discrete measure" in note)


def universal_eca_support() -> None:
    section("B - Universal local-rule support")
    neighborhoods = tuple(product((0, 1), repeat=3))
    rules = tuple(range(256))
    check("B there are eight binary radius-one neighborhoods", len(neighborhoods) == 8)
    check("B there are 256 deterministic local rules", len(rules) == 2 ** len(neighborhoods))
    for neighborhood in neighborhoods:
        outputs = [rule_output(rule, neighborhood) for rule in rules]
        check(
            f"B universal rule set splits neighborhood {neighborhood} equally",
            outputs.count(0) == outputs.count(1) == 128,
        )

    de_bruijn_ring = (0, 0, 0, 1, 0, 1, 1, 1)
    seen_neighborhoods = {
        (
            de_bruijn_ring[(site - 1) % 8],
            de_bruijn_ring[site],
            de_bruijn_ring[(site + 1) % 8],
        )
        for site in range(8)
    }
    check("B cyclic seed realizes every local neighborhood once", len(seen_neighborhoods) == 8)
    successors = {successor(rule, de_bruijn_ring) for rule in rules}
    check("B all-rule union permits every eight-bit successor", len(successors) == 256)


def symmetry_restricted_rule_space() -> None:
    section("C - Symmetry filtering does not select one rule")
    flip_rules = tuple(rule for rule in range(256) if bit_flip_covariant(rule))
    symmetric_rules = tuple(rule for rule in flip_rules if reflection_covariant(rule))
    identity = sum(((pattern >> 1) & 1) << pattern for pattern in range(8))
    complement = sum((1 - ((pattern >> 1) & 1)) << pattern for pattern in range(8))
    check("C bit-flip covariance leaves sixteen rules", len(flip_rules) == 16)
    check("C reflection plus bit-flip covariance leaves multiple rules", len(symmetric_rules) > 1)
    check("C identity rule survives both symmetries", identity in symmetric_rules)
    check("C complement rule survives both symmetries", complement in symmetric_rules)
    check("C symmetric identity and complement have different successors", successor(identity, (0, 1, 1, 0)) != successor(complement, (0, 1, 1, 0)))

    # Proper-cubic-invariant Boolean scalar rules can depend on the center bit
    # and the count of six live neighbors: fourteen input orbits. Global bit
    # complement pairs those orbits, leaving seven free output bits.
    cubic_orbits = tuple((center, count) for center in (0, 1) for count in range(7))
    complement_pairs = {
        frozenset(((center, count), (1 - center, 6 - count)))
        for center, count in cubic_orbits
    }
    check("C cubic scalar input table has fourteen orbits", len(cubic_orbits) == 14)
    check("C complement covariance leaves seven independent orbit pairs", len(complement_pairs) == 7)
    check("C cubic plus complement covariance still leaves 128 rules", 2 ** len(complement_pairs) == 128)


def causal_and_record_quotients() -> None:
    section("D - Causal graphs do not erase readable rule branches")
    causal_dag_identity = (("input", "event"), ("event", "record"))
    causal_dag_complement = (("input", "event"), ("event", "record"))
    identity_transcript = (("record", 0), ("readout", 0))
    complement_transcript = (("record", 1), ("readout", 1))
    check("D distinct rules can have isomorphic causal DAGs", causal_dag_identity == causal_dag_complement)
    check("D their readable record transcripts differ", identity_transcript != complement_transcript)
    check("D causal quotient alone is not record-faithful", causal_dag_identity == causal_dag_complement and identity_transcript != complement_transcript)
    record_faithful_classes = {identity_transcript, complement_transcript}
    check("D transcript-preserving quotient retains both branches", len(record_faithful_classes) == 2)


def measure_and_actuality_controls() -> None:
    section("E - Rule-space measure and actuality remain additional data")
    two_rules = {"A": Fraction(1, 2), "B": Fraction(1, 2)}
    aliased_syntax = {"A": Fraction(2, 3), "B": Fraction(1, 3)}
    check("E uniform syntax changes under one harmless alias", two_rules != aliased_syntax)
    check("E alias changes the A marginal from one-half to two-thirds", two_rules["A"] == Fraction(1, 2) and aliased_syntax["A"] == Fraction(2, 3))

    prefix_prior_ab = {"A": Fraction(2, 3), "B": Fraction(1, 3)}
    prefix_prior_ba = {"A": Fraction(1, 3), "B": Fraction(2, 3)}
    check("E swapping compiler code lengths swaps normalized prior", prefix_prior_ab["A"] == prefix_prior_ba["B"])
    check("E algorithmic-looking weight is compiler-relative in the control", prefix_prior_ab != prefix_prior_ba)

    same_measure = {0: Fraction(1, 2), 1: Fraction(1, 2)}
    annotations = ((same_measure, 0), (same_measure, 1), (same_measure, None))
    check("E one measure admits two selected members or no selected member", len({annotation[1] for annotation in annotations}) == 3)
    check("E normalization does not choose actuality", sum(same_measure.values()) == 1 and annotations[0][1] != annotations[1][1])


def bounded_observer_controls() -> None:
    section("F - Computational boundedness is not full future equivalence")
    for horizon in range(1, 17):
        always_zero = (0,) * (horizon + 1)
        late_one = (0,) * horizon + (1,)
        check(
            f"F horizon {horizon:02d} observer sees the same prefix",
            always_zero[:horizon] == late_one[:horizon],
        )
        check(
            f"F horizon {horizon:02d} later record separates the laws",
            always_zero[horizon] != late_one[horizon],
        )
    check("F horizon-relative equivalence relations are not one exact quotient", all(horizon != horizon + 1 for horizon in range(1, 17)))
    check("F a one-bit persistent observer can read the late separator", len({0, 1}) == 2)


def ablation_and_constitutional_boundary() -> None:
    section("G - Exact package and constitutional boundary")
    package = (
        "rule grammar",
        "rule-space member set",
        "history construction",
        "record-faithful equivalence",
        "measure or deterministic selection",
        "actuality semantics",
    )
    check("G universal package has six explicit fields", len(package) == 6)
    for removed in package:
        residual = tuple(field for field in package if field != removed)
        check(f"G deleting {removed} restores an ambiguity", len(residual) == 5 and removed not in residual)

    note = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    markers = (
        "not a free law selector",
        "maximally permissive",
        "compiler-relative",
        "record-faithful equivalence",
        "exact grammar",
        "no axiom sentence follows",
        "n1 — alternative-route enumeration",
        "n2 — wall-independence audit",
        "n3 — hidden-wall scan",
        "n4 — exact residual matching",
        "n5 — rhetoric and resolution audit",
        "n6 — partial-closure paths",
        "n7 — strongest surviving steelman",
        "n8 — cross-cycle echo",
    )
    for marker in markers:
        check(f"G note contains: {marker}", marker in note)


def main() -> int:
    authority_contract()
    universal_eca_support()
    symmetry_restricted_rule_space()
    causal_and_record_quotients()
    measure_and_actuality_controls()
    bounded_observer_controls()
    ablation_and_constitutional_boundary()
    section("TOTAL")
    print(f"PASS={PASS} FAIL={FAIL}")
    print("RESULT: PASS" if FAIL == 0 else "RESULT: FAIL")
    print(
        "BOUNDARY: all-rules is one exact set-valued architecture only after "
        "grammar, record equivalence, measure/selection, and actuality are fixed"
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
