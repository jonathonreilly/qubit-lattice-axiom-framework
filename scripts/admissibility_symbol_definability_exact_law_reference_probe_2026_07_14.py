#!/usr/bin/env python3
"""Exact finite controls for rule-symbol, definability, and law-reference claims.

This runner is authority-free.  It exhausts a binary-projector quotient of the
six-neighbor condition space, constructs two admissibility expansions of one
foundation reduct, and checks the documentation/type-placement contract.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
from itertools import permutations, product
import json
from pathlib import Path
from typing import Callable


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "ADMISSIBILITY_SYMBOL_DEFINABILITY_AND_EXACT_LAW_REFERENCE_CHALLENGE_NOTE_2026-07-14.md"
)
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
SOURCES = (
    AXIOMS,
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "EXISTENCE_UNIQUENESS_AND_EXACT_LAW_REFERENCE_NOTE_2026-07-14.md",
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "EXACT_LAW_CONSTITUTIONAL_PLACEMENT_SCHEMA_PROBE_NOTE_2026-07-14.md",
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "BLIND_RESIDUAL_ATOM_PACKING_AND_ONE_LAW_CONSTITUTIONAL_SCHEMA_NOTE_2026-07-14.md",
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "EXACT_PREDICTIVE_SPECIFICATION_TOURNAMENT_NOTE_2026-07-14.md",
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "QUALITATIVE_SUBSTRATE_EXACT_LAW_SELECTION_NOTE_2026-07-14.md",
    ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md",
    ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
)

PASS = 0
FAIL = 0

Bit = int
Condition = tuple[Bit, Bit, Bit, Bit, Bit, Bit]
Menu = frozenset[Bit]
Vector = tuple[int, int, int]

DIRECTIONS: tuple[Vector, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
CONDITIONS: tuple[Condition, ...] = tuple(product((0, 1), repeat=6))


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool) -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}")
    else:
        FAIL += 1
        print(f"FAIL {label}")


def normalize(text: str) -> str:
    return " ".join(text.lower().replace("`", "").replace("*", "").split())


def permutation_sign(perm: tuple[int, int, int]) -> int:
    inversions = sum(perm[i] > perm[j] for i in range(3) for j in range(i + 1, 3))
    return -1 if inversions % 2 else 1


def proper_cubic_rotations() -> tuple[dict[Vector, Vector], ...]:
    rotations = []
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            if permutation_sign(perm) * signs[0] * signs[1] * signs[2] != 1:
                continue

            def rotate(vector: Vector, p=perm, s=signs) -> Vector:
                result = [0, 0, 0]
                for old_axis, component in enumerate(vector):
                    result[p[old_axis]] += s[old_axis] * component
                return tuple(result)  # type: ignore[return-value]

            rotations.append({direction: rotate(direction) for direction in DIRECTIONS})
    return tuple(rotations)


ROTATIONS = proper_cubic_rotations()


def rotate_condition(condition: Condition, rotation: dict[Vector, Vector]) -> Condition:
    old = dict(zip(DIRECTIONS, condition))
    new = {rotation[direction]: bit for direction, bit in old.items()}
    return tuple(new[direction] for direction in DIRECTIONS)  # type: ignore[return-value]


def majority_menu(condition: Condition) -> Menu:
    zeros = condition.count(0)
    ones = condition.count(1)
    if zeros == ones:
        return frozenset((0, 1))
    return frozenset((0 if zeros > ones else 1,))


def minority_menu(condition: Condition) -> Menu:
    zeros = condition.count(0)
    ones = condition.count(1)
    if zeros == ones:
        return frozenset((0, 1))
    return frozenset((1 if zeros > ones else 0,))


@dataclass(frozen=True)
class Rule:
    name: str
    evaluator: Callable[[Condition], Menu]

    def menu(self, condition: Condition) -> Menu:
        return self.evaluator(condition)

    def table(self) -> tuple[tuple[Condition, tuple[Bit, ...]], ...]:
        return tuple((condition, tuple(sorted(self.menu(condition)))) for condition in CONDITIONS)


MAJORITY = Rule("majority", majority_menu)
MINORITY = Rule("minority", minority_menu)
RULES = (MAJORITY, MINORITY)


def label_swap_menu(menu: Menu) -> Menu:
    return frozenset(1 - bit for bit in menu)


def is_fixed_covariant_varying(rule: Rule) -> bool:
    fixed = all(rule.menu(condition) == rule.menu(tuple(condition)) for condition in CONDITIONS)
    nonempty = all(rule.menu(condition) for condition in CONDITIONS)
    spatial = all(
        rule.menu(rotate_condition(condition, rotation)) == rule.menu(condition)
        for condition in CONDITIONS
        for rotation in ROTATIONS
    )
    label_covariant = all(
        rule.menu(tuple(1 - bit for bit in condition)) == label_swap_menu(rule.menu(condition))
        for condition in CONDITIONS
    )
    varying = len({rule.menu(condition) for condition in CONDITIONS}) > 1
    return fixed and nonempty and spatial and label_covariant and varying


@dataclass(frozen=True)
class FoundationReduct:
    """Everything held fixed when the admissibility symbol is forgotten."""

    site_sort: str
    local_algebra: str
    neighbor_directions: tuple[Vector, ...]
    existing_record_condition: Condition
    existing_record_content: Bit
    open_test_condition: Condition


@dataclass(frozen=True)
class AdmissibilityExpansion:
    reduct: FoundationReduct
    admissibility_interpretation: Rule

    def satisfies_displayed_fragment(self) -> bool:
        rule = self.admissibility_interpretation
        record_is_admissible = self.reduct.existing_record_content in rule.menu(
            self.reduct.existing_record_condition
        )
        return is_fixed_covariant_varying(rule) and record_is_admissible


REDUCT = FoundationReduct(
    site_sort="Z^3 with six nearest-neighbor directions",
    local_algebra="M_2(C), binary orthogonal-projector sector",
    neighbor_directions=DIRECTIONS,
    existing_record_condition=(0, 0, 0, 1, 1, 1),
    existing_record_content=1,
    open_test_condition=(0, 0, 0, 0, 1, 1),
)
EXPANSIONS = tuple(AdmissibilityExpansion(REDUCT, rule) for rule in RULES)


RecordSnapshot = tuple[tuple[str, Bit], ...]


def append_history(expansion: AdmissibilityExpansion) -> tuple[RecordSnapshot, RecordSnapshot]:
    initial = (("anchor", REDUCT.existing_record_content),)
    written = sole(expansion.admissibility_interpretation.menu(REDUCT.open_test_condition))
    final = initial + (("target", written),)
    return initial, final


def valid_append_only_record_history(history: tuple[RecordSnapshot, ...]) -> bool:
    if not history:
        return False
    prior: dict[str, Bit] = {}
    for snapshot in history:
        current = dict(snapshot)
        if len(current) != len(snapshot):
            return False
        if any(current.get(site) != content for site, content in prior.items()):
            return False
        prior = current
    return True


def scalar_readout(snapshot: RecordSnapshot) -> int:
    return sum(content for _, content in snapshot)


def sole(menu: Menu) -> Bit:
    if len(menu) != 1:
        raise ValueError(f"common write bridge requires a singleton menu, got {menu}")
    return next(iter(menu))


def table_digest(rule: Rule) -> str:
    payload = json.dumps(rule.table(), separators=(",", ":"), sort_keys=False)
    return "sha256:" + sha256(payload.encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class CompleteRecordLaw:
    admissibility: Rule
    zero_weight_at_tie: Fraction

    def next_record_weights(self, condition: Condition) -> tuple[Fraction, Fraction]:
        menu = self.admissibility.menu(condition)
        if menu == frozenset((0, 1)):
            return self.zero_weight_at_tie, 1 - self.zero_weight_at_tie
        bit = sole(menu)
        return (Fraction(1), Fraction(0)) if bit == 0 else (Fraction(0), Fraction(1))

    def digest(self) -> str:
        payload = f"{table_digest(self.admissibility)}|{self.zero_weight_at_tie}"
        return "sha256:" + sha256(payload.encode("utf-8")).hexdigest()


def rule_symbol_and_same_reduct_probe() -> None:
    section("A - One named interpretation per model is not one interpretation across models")
    check("A exactly 24 proper cubic rotations are enumerated", len(ROTATIONS) == 24)
    check("A each rotation permutes the six neighbor directions", all(set(r.values()) == set(DIRECTIONS) for r in ROTATIONS))
    for rule in RULES:
        check(f"A {rule.name} is fixed, nonempty, covariant, label-neutral, and varying", is_fixed_covariant_varying(rule))
    check("A each expansion contains exactly one interpretation of the named symbol", all(isinstance(e.admissibility_interpretation, Rule) for e in EXPANSIONS))
    check("A both expansions use the identical rule-free reduct object", EXPANSIONS[0].reduct is EXPANSIONS[1].reduct)
    check("A both expansions satisfy the displayed finite foundation fragment", all(e.satisfies_displayed_fragment() for e in EXPANSIONS))
    check("A their extensional admissibility tables differ", MAJORITY.table() != MINORITY.table())
    check("A the current structural property has two witnesses, not unique existence", sum(is_fixed_covariant_varying(rule) for rule in RULES) == 2)


def prediction_and_definability_probe() -> None:
    section("B - Paired expansions refute implicit definability and separate a record")
    test = REDUCT.open_test_condition
    menus = tuple(expansion.admissibility_interpretation.menu(test) for expansion in EXPANSIONS)
    writes = tuple(sole(menu) for menu in menus)
    check("B the test condition has a four-to-two neighbor split", test.count(0) == 4 and test.count(1) == 2)
    check("B majority and minority give singleton menus", all(len(menu) == 1 for menu in menus))
    check("B one common write bridge gives different next records", writes == (0, 1))
    check("B same reduct plus different A is an implicit-definability counterexample", EXPANSIONS[0].reduct is EXPANSIONS[1].reduct and MAJORITY.table() != MINORITY.table())
    check("B the neutral existing record is admissible in both expansions", all(REDUCT.existing_record_content in rule.menu(REDUCT.existing_record_condition) for rule in RULES))
    histories = tuple(append_history(expansion) for expansion in EXPANSIONS)
    check("B both completions contain a genuine record-formation append", all(len(final) == len(initial) + 1 for initial, final in histories))
    check("B both record histories are one-per-site and permanent", all(valid_append_only_record_history(history) for history in histories))
    check("B readout is content-only and empty-normalized", scalar_readout(()) == 0 and scalar_readout((("x", 1),)) == 1)
    check("B scalar readout is additive on disjoint records", all(scalar_readout(final) == scalar_readout(initial) + scalar_readout((final[-1],)) for initial, final in histories))


def unique_existence_parameter_probe() -> None:
    section("C - Unique existence relative to a parameter does not fix the parameter")

    def rule_selected_by_parameter(parameter: int) -> tuple[Rule, ...]:
        return tuple(rule for index, rule in enumerate(RULES) if index == parameter)

    for parameter in (0, 1):
        selected = rule_selected_by_parameter(parameter)
        check(f"C parameter {parameter} gives unique existence within its model", len(selected) == 1)
        check(f"C selected rule {parameter} still satisfies the structural property", is_fixed_covariant_varying(selected[0]))
    selected_writes = tuple(sole(rule_selected_by_parameter(p)[0].menu(REDUCT.open_test_condition)) for p in (0, 1))
    check("C the unfixed parameter leaves two record predictions across models", selected_writes == (0, 1))
    check("C fixing the parameter is additional extensional model data", len(set(selected_writes)) == 2)


def exact_a_is_not_complete_law_probe() -> None:
    section("D - Extensional admissibility does not fill the complete predictive-law type")
    tie = REDUCT.existing_record_condition
    half = CompleteRecordLaw(MAJORITY, Fraction(1, 2))
    biased = CompleteRecordLaw(MAJORITY, Fraction(2, 3))
    check("D both complete laws share the identical A object", half.admissibility is biased.admissibility)
    check("D shared A has both outcomes available at the tie", MAJORITY.menu(tie) == frozenset((0, 1)))
    check("D complete laws normalize", all(sum(law.next_record_weights(tie)) == 1 for law in (half, biased)))
    check("D complete laws disagree on record weights", half.next_record_weights(tie) != biased.next_record_weights(tie))
    check("D exact A digest is identical", table_digest(half.admissibility) == table_digest(biased.admissibility))
    check("D complete-law digests differ", half.digest() != biased.digest())


def stable_artifact_probe() -> None:
    section("E - A content-addressed reference selects, but does not retrospectively derive")
    artifacts = {table_digest(rule): rule for rule in RULES}
    check("E two extensional rule tables have two stable content digests", len(artifacts) == 2)
    selected_id = table_digest(MAJORITY)
    selected = artifacts[selected_id]
    check("E resolving the stable identifier selects one exact A", selected.table() == MAJORITY.table())
    check("E adding that selection reduces two admissibility expansions to one", sum(rule.table() == selected.table() for rule in RULES) == 1)
    completions = (
        CompleteRecordLaw(selected, Fraction(1, 2)),
        CompleteRecordLaw(selected, Fraction(2, 3)),
    )
    check("E an A-only artifact still admits two complete record laws", len({law.digest() for law in completions}) == 2)
    exact_law_id = completions[0].digest()
    check("E a complete-law digest selects one complete law", sum(law.digest() == exact_law_id for law in completions) == 1)


def source_and_documentation_contract() -> None:
    section("F - Live-source and documentation contract")
    for source in SOURCES:
        check(f"F source exists: {source.name}", source.is_file())

    axioms = normalize(AXIOMS.read_text(encoding="utf-8"))
    check(
        "F exact singular Admissibility sentence is live",
        "there is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations" in axioms,
    )
    check(
        "F exact availability sentence is live",
        "available possibilities are determined by, and vary with, the nearest-neighbor conditions" in axioms,
    )
    check("F live memo says Admissibility is not dynamics", "admissibility is not a dynamics axiom" in axioms)
    check("F live memo withholds transition weights", "supply transition probabilities or weights" in axioms)
    check("F live memo withholds record production", "provide a record-production process" in axioms)

    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    nodes = registry["nodes"]
    check("F minimal-axioms registry path is current", nodes["minimal_axioms"]["current_path"] == "docs/MINIMAL_AXIOMS_2026-06-29.md")
    check("F scale primitive path is current", nodes["scale_reference_primitive"]["current_path"] == "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md")
    check("F kinetic primitive path is current", nodes["kinetic_isotropy_primitive"]["current_path"] == "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md")
    check("F realized-state primitive path is current", nodes["realized_state_primitive"]["current_path"] == "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md")

    note = normalize(NOTE.read_text(encoding="utf-8"))
    for phrase in (
        "authority: none",
        "named function symbol",
        "extensional specification",
        "unique existence",
        "implicit definability",
        "explicit definability",
        "beth",
        "framework schema",
        "theory of our universe",
        "instantiated model",
        "stable external exact artifact",
        "no axiom edit is recommended",
        "the lower bound narrows",
    ):
        check(f"F note contains contract phrase: {phrase}", phrase in note)
    check("F note carries all N1-N8 headings", all(f"### n{index}" in note for index in range(1, 9)))
    check("F note states a PASS gate", "gate status: pass" in note)
    check("F note distinguishes conservative definition from theory selection", "conservative definitional extension" in note and "model-selection" in note)
    check("F note includes the Beth scope guard", "classical first-order" in note and "finite-only" in note)


def main() -> int:
    rule_symbol_and_same_reduct_probe()
    prediction_and_definability_probe()
    unique_existence_parameter_probe()
    exact_a_is_not_complete_law_probe()
    stable_artifact_probe()
    source_and_documentation_contract()
    section("TOTAL")
    print(f"PASS={PASS} FAIL={FAIL}")
    print("RESULT: " + ("PASS" if FAIL == 0 else "FAIL"))
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
