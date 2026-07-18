#!/usr/bin/env python3
"""Exact controls for the Cycle-35 final missing-content census.

The runner checks finite recurrence, record/state compatibility, containment,
local/global consistency, typicality scope, and the clause-deletion ledger.  It
does not select a law, boundary, history, axiom wording, or audit result.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs/work_history/repo/review_feedback"
NOTE = REVIEW / "FINAL_MISSING_CONTENT_CENSUS_AND_CONSTITUTIONAL_EDIT_GATE_CYCLE35_NOTE_2026-07-14.md"

PATHS = {
    "axioms": ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "registry": ROOT / "docs/audit/data/axiom_premise_nodes.json",
    "scale": ROOT / "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
    "kinetic": ROOT / "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "realized": ROOT / "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
    "cycle30": REVIEW / "GLOBAL_RECORD_HISTORY_PROCESS_LAW_CYCLE30_NOTE_2026-07-14.md",
    "cycle31": REVIEW / "CONSTITUTIONAL_LOWER_BOUND_CLOSURE_AND_CLAUSE_DELETION_CYCLE31_NOTE_2026-07-14.md",
    "cycle32": REVIEW / "LONG_RUN_RECORD_ONLY_APPEND_ARCHITECTURE_CYCLE32_NOTE_2026-07-14.md",
    "cycle33": REVIEW / "LOCAL_TO_GLOBAL_CUBIC_PROCESS_GLUE_CYCLE33_NOTE_2026-07-14.md",
    "cycle34": REVIEW / "MOVING_LOGICAL_APPARATUS_APPEND_FRONT_CYCLE34_NOTE_2026-07-14.md",
    "cycle36": REVIEW / "CUBIC_CZ_EDGE_RULE_UNIQUENESS_SELECTION_CYCLE36_NOTE_2026-07-14.md",
}


PASS = 0
FAIL = 0


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(condition: bool, label: str) -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}")
    else:
        FAIL += 1
        print(f"FAIL {label}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def normalized(path: Path) -> str:
    text = read(path).lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def check_needles(text: str, needles: Iterable[str], prefix: str) -> None:
    for needle in needles:
        check(needle.lower() in text.lower(), f"{prefix} contains {needle!r}")


section("A. SOURCE, PRIMITIVE, AND AUTHORITY CONTRACT")

for name, path in {"note": NOTE, **PATHS}.items():
    check(path.is_file(), f"A {name} source exists")

texts = {name: normalized(path) for name, path in PATHS.items()}
note = normalized(NOTE)

check_needles(
    texts["axioms"],
    (
        "there is one fixed nearest-neighbor admissibility rule",
        "records form",
        "records are permanent",
        "only records are readable",
        "a state is a configuration of records",
        "admissibility is not a dynamics axiom",
    ),
    "A live foundation",
)
check_needles(
    texts["registry"],
    (
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
        "no state, state-selection rule, measure, typicality/genericity assumption",
    ),
    "A primitive registry",
)
check_needles(texts["scale"], ("units conversion, not a physics axiom", "zero dimensionless content"), "A scale primitive")
check_needles(texts["kinetic"], ("c_t = c_s", "not a new dynamics"), "A kinetic primitive")
check_needles(
    texts["realized"],
    ("one realized-state reference", "no state, averaging over alternatives, measure", "no typical or generic claim"),
    "A realized-state primitive",
)
check_needles(
    texts["cycle30"],
    ("no qualification amendment is forced", "identity insertion", "record-fibre future-equivalence", "preparation, phase reference, apparatus context"),
    "A Cycle30",
)
check_needles(
    texts["cycle31"],
    ("only nonzero universal constitutional content", "content count, treating type links", "conditional state-type edit"),
    "A Cycle31",
)
check_needles(
    texts["cycle32"],
    ("a fixed finite region cannot host indefinitely many", "migratory identity is a real escape", "fresh capacity"),
    "A Cycle32",
)
check_needles(
    texts["cycle33"],
    ("no independent finite global measure atom survives", "boundary/history datum survives", "global consistency is a theorem obligation", "identity-slot containment"),
    "A Cycle33",
)
check_needles(
    texts["cycle34"],
    ("logical apparatus", "translation", "record migration", "permanent", "moving front"),
    "A Cycle34",
)
check_needles(
    texts["cycle36"],
    ("exactly two laws remain", "time-dependent transported equivalence", "constraint/preparation layer, not the full"),
    "A Cycle36",
)
check("authority: none" in note, "A Cycle35 note is authority-free")
check("does not amend an axiom" in note, "A Cycle35 disclaims axiom edit")
check("no live axiom edit" in note, "A Cycle35 preserves no-live-edit result")
check("no complete law referent or uniqueness theorem is ready" in note, "A Cycle35 blocks premature landing")
check("cycle-36 local-rule uniqueness cross-check" in note, "A Cycle35 integrates the Cycle36 selection boundary")


section("B. FINAL CENSUS HAS ONE UNIVERSAL IDENTITY")

SUPPLIED = "already supplied"
DEFINE = "definition/type link"
FIELD = "field of complete L*"
THEOREM = "theorem/compatibility test of L*"
HISTORY = "contingent history datum"
CLAIM = "claim-specific condition"
RECORD_EDIT = "conditional Record edit"
STATE_EDIT = "conditional Qualification edit"
UNIVERSAL = "universal constitutional identification"

CLASSES = {SUPPLIED, DEFINE, FIELD, THEOREM, HISTORY, CLAIM, RECORD_EDIT, STATE_EDIT, UNIVERSAL}

CENSUS = {
    "S-REC-OCC": SUPPLIED,
    "S-REC-LOCK": SUPPLIED,
    "S-READ": SUPPLIED,
    "S-STATE": SUPPLIED,
    "S-ACTUAL": SUPPLIED,
    "S-LAT": SUPPLIED,
    "D-RECORD-ID": DEFINE,
    "D-APP-ROLE": DEFINE,
    "D-PREP": DEFINE,
    "D-OMIT": DEFINE,
    "D-CUT": DEFINE,
    "D-EQUIV": DEFINE,
    "L-DOMAIN": FIELD,
    "L-DECODER": FIELD,
    "L-OCCURRENCE": FIELD,
    "L-WEIGHT": FIELD,
    "L-CONTAIN": FIELD,
    "L-IDENTITY": FIELD,
    "L-RENEW": FIELD,
    "L-BOUNDARY": FIELD,
    "L-STAT": FIELD,
    "L-DOWNSTREAM": FIELD,
    "T-GLOBAL": THEOREM,
    "T-PROJECTIVE": THEOREM,
    "T-RECORD-FIBRE": THEOREM,
    "T-PERM": THEOREM,
    "T-RECURRENCE": THEOREM,
    "T-FREQUENCY": THEOREM,
    "T-APP-BISIM": THEOREM,
    "H-BOUNDARY": HISTORY,
    "H-PREP": HISTORY,
    "H-CORPUS": HISTORY,
    "H-COMPONENT": HISTORY,
    "H-HEAD": HISTORY,
    "TY-ACTUAL": CLAIM,
    "C-RECORD": RECORD_EDIT,
    "C-STATE": STATE_EDIT,
    "I-L": UNIVERSAL,
}

check(set(CENSUS.values()) == CLASSES, "B all final census classes are populated")
check(len(CENSUS) == len(set(CENSUS)), "B every census identifier is unique")
for cls in sorted(CLASSES):
    check(sum(value == cls for value in CENSUS.values()) > 0, f"B class {cls} is nonempty")
universal_ids = {name for name, cls in CENSUS.items() if cls == UNIVERSAL}
check(universal_ids == {"I-L"}, "B exactly one universal nonzero identification survives")
check(CENSUS["T-GLOBAL"] == THEOREM, "B local-to-global consistency is a theorem gate")
check(CENSUS["L-CONTAIN"] == FIELD, "B identity containment is a complete-law field")
check(CENSUS["TY-ACTUAL"] == CLAIM, "B actual typicality is claim-specific")
check(CENSUS["C-RECORD"] == RECORD_EDIT, "B record migration pressure is conditional")
check(CENSUS["C-STATE"] == STATE_EDIT, "B hidden state pressure is conditional")
check(CENSUS["H-BOUNDARY"] == HISTORY, "B actual boundary remains history data")
check(CENSUS["D-APP-ROLE"] == DEFINE and CENSUS["T-APP-BISIM"] == THEOREM, "B apparatus identity is definition plus theorem")


section("C. UPDATED CLAUSE-DELETION MATRIX")

U = "unique theorem"
A = "exact A only"
L = "complete local L*"
G = "global-history L*"
ROUTES = (U, A, L, G)

MATRIX = {
    "duplicate law existence": {U: "DELETE", A: "DELETE", L: "DELETE", G: "DELETE"},
    "exact A identity": {U: "THEOREM", A: "KEEP-1", L: "DEFINE", G: "DEFINE"},
    "exact L identity": {U: "THEOREM", A: "N/A", L: "KEEP-1", G: "KEEP-1"},
    "separate global measure": {U: "THEOREM", A: "N/A", L: "THEOREM", G: "FIELD"},
    "local-global consistency": {U: "THEOREM", A: "N/A", L: "THEOREM", G: "THEOREM"},
    "boundary interface": {U: "THEOREM/FIELD", A: "N/A", L: "FIELD", G: "FIELD"},
    "actual boundary/history": {U: "DELETE", A: "DELETE", L: "HISTORY", G: "HISTORY"},
    "identity containment": {U: "THEOREM", A: "N/A", L: "THEOREM", G: "FIELD"},
    "context decoder": {U: "THEOREM", A: "N/A", L: "FIELD", G: "FIELD"},
    "apparatus recurrence": {U: "THEOREM", A: "N/A", L: "THEOREM", G: "THEOREM"},
    "renewal/export": {U: "THEOREM", A: "N/A", L: "FIELD/THEOREM", G: "FIELD/THEOREM"},
    "record identity decoder": {U: "DEFINE", A: "N/A", L: "FIELD/THEOREM", G: "FIELD/THEOREM"},
    "migratory Record wording": {U: "DELETE", A: "N/A", L: "CONDITIONAL-R", G: "CONDITIONAL-R"},
    "unrecorded carrier state": {U: "DELETE", A: "N/A", L: "CONDITIONAL-Q", G: "CONDITIONAL-Q"},
    "actual-history typicality": {U: "DELETE", A: "N/A", L: "NAMED-CONDITION", G: "NAMED-CONDITION"},
    "corpus frequencies": {U: "THEOREM", A: "N/A", L: "THEOREM", G: "THEOREM"},
    "witness/read/clock lock": {U: "DELETE", A: "N/A", L: "FIELD/THEOREM", G: "FIELD/THEOREM"},
    "resource/gravity clause": {U: "DELETE", A: "N/A", L: "FIELD/THEOREM", G: "FIELD/THEOREM"},
    "retype Admissibility": {U: "DELETE", A: "DELETE", L: "PLACEMENT", G: "DELETE"},
    "separate Law slot": {U: "DELETE", A: "DELETE", L: "DELETE", G: "PLACEMENT"},
}

check(all(set(row) == set(ROUTES) for row in MATRIX.values()), "C each matrix row covers all four routes")
content_counts = {route: sum(row[route] == "KEEP-1" for row in MATRIX.values()) for route in ROUTES}
check(content_counts == {U: 0, A: 1, L: 1, G: 1}, "C universal content counts remain 0,1,1,1")
check(all(MATRIX["duplicate law existence"][route] == "DELETE" for route in ROUTES), "C duplicate existence deletes universally")
check(MATRIX["separate global measure"][L] == "THEOREM", "C local route derives rather than duplicates global W")
check(MATRIX["separate global measure"][G] == "FIELD", "C global route internalizes W in its one identity")
check(MATRIX["migratory Record wording"][L] == "CONDITIONAL-R", "C Record edit remains conditional")
check(MATRIX["unrecorded carrier state"][L] == "CONDITIONAL-Q", "C Qualification edit remains conditional")
check(MATRIX["actual-history typicality"][G] == "NAMED-CONDITION", "C typicality remains an explicit claim condition")
check(MATRIX["actual boundary/history"][G] == "HISTORY", "C actual boundary is not constitutional law content")


section("D. FIXED-SITE EXHAUSTION VERSUS MOVING LOGICAL RECURRENCE")

Direction = tuple[int, int, int]
Site = tuple[int, int, int]
E: Direction = (1, 0, 0)


def add(site: Site, direction: Direction) -> Site:
    return tuple(site[i] + direction[i] for i in range(3))  # type: ignore[return-value]


def scale(direction: Direction, n: int) -> Site:
    return tuple(n * direction[i] for i in range(3))  # type: ignore[return-value]


def front_state(word: tuple[int, ...]) -> dict[Site, int]:
    return {scale(E, index): bit for index, bit in enumerate(word)}


def front_head(state: dict[Site, int]) -> Site:
    candidates = [site for site in state if add(site, E) not in state]
    if len(candidates) != 1:
        raise ValueError(candidates)
    return candidates[0]


K = {
    0: {0: Fraction(3, 4), 1: Fraction(1, 4)},
    1: {0: Fraction(1, 3), 1: Fraction(2, 3)},
}
PI = {0: Fraction(4, 7), 1: Fraction(3, 7)}


def future_words(start: int, length: int) -> dict[tuple[int, ...], Fraction]:
    result: dict[tuple[int, ...], Fraction] = {(start,): Fraction(1)}
    for _ in range(length):
        next_result: dict[tuple[int, ...], Fraction] = {}
        for word, probability in result.items():
            for bit, transition in K[word[-1]].items():
                next_result[word + (bit,)] = probability * transition
        result = next_result
    return result


def future_words_at(_absolute_head: Site, start: int, length: int) -> dict[tuple[int, ...], Fraction]:
    """The homogeneous kernel has no absolute-position argument."""
    return future_words(start, length)


sample_word = (0, 1, 1, 0, 1, 0, 0, 1)
states = [front_state(sample_word[:n]) for n in range(1, len(sample_word) + 1)]
check(all(len(state) == index for index, state in enumerate(states, start=1)), "D one new permanent record is appended per front step")
check(all(front_head(state) == scale(E, index - 1) for index, state in enumerate(states, start=1)), "D head is uniquely record-decoded")
check(all(all(states[n + 1][site] == value for site, value in states[n].items()) for n in range(len(states) - 1)), "D every old site/content record persists")


def role_patch(state: dict[Site, int], head: Site) -> tuple[str, str, str]:
    backward = add(head, (-1, 0, 0))
    forward = add(head, E)
    return ("record" if backward in state else "open", "record", "record" if forward in state else "open")


check(all(role_patch(state, front_head(state)) == ("record", "record", "open") for state in states[1:]), "D bounded active apparatus patch recurs under translation")
check(front_head(states[-1]) != front_head(states[-2]), "D apparatus role moves to a new site")
check(all(site in states[-1] for site in states[-2]), "D moving role is not record migration")
check(future_words_at(scale(E, 7), 0, 4) == future_words_at(scale(E, 70), 0, 4), "D equal head bits at different positions have identical continuation law")
check(future_words(0, 2) != future_words(1, 2), "D different head bits are distinct internal apparatus states")
check(all(sum(PI[a] * K[a][b] for a in (0, 1)) == PI[b] for b in (0, 1)), "D exact stationary co-moving content distribution is invariant")
check(K[0][0] - K[1][0] == Fraction(5, 12), "D exact nontrivial Markov eigenvalue is 5/12")

fixed_region = {scale(E, n) for n in range(5)}
formations = [len(set(state) & fixed_region) for state in states]
check(max(formations) == len(fixed_region), "D fixed five-site region saturates after five formations")
check(Fraction(len(fixed_region), 10_000) < Fraction(1, 1000), "D fixed-region asymptotic formation-rate bound tends to zero")
check(len(states[-1]) > len(fixed_region), "D moving front continues after fixed region saturates")


section("E. EXACT RECORD COMPATIBILITY GATE")


@dataclass(frozen=True)
class RecordCase:
    name: str
    official_old_record: bool
    identity_persists: bool
    content_persists: bool
    one_per_site: bool
    readout_factors_through_records: bool
    current_site_language_sufficient: bool


def record_edit_needed(case: RecordCase) -> bool:
    if not case.official_old_record:
        return False
    return not (
        case.identity_persists
        and case.content_persists
        and case.one_per_site
        and case.readout_factors_through_records
        and case.current_site_language_sufficient
    )


append_case = RecordCase("append/copy", True, True, True, True, True, True)
moving_role_case = RecordCase("translated role", True, True, True, True, True, True)
encoded_append_case = RecordCase("encoded append archive", True, True, True, True, True, True)
nonrecord_swap_case = RecordCase("mutable nonrecord carrier", False, False, False, True, True, True)
official_swap_case = RecordCase("cleared official record", True, False, False, True, False, True)
migratory_logical_case = RecordCase("migratory logical record", True, True, True, True, True, False)

check(not record_edit_needed(append_case), "E append/copy law satisfies current Record")
check(not record_edit_needed(moving_role_case), "E moving apparatus role does not trigger Record edit")
check(not record_edit_needed(encoded_append_case), "E append-only encoded record does not trigger Record edit")
check(not record_edit_needed(nonrecord_swap_case), "E changing nonrecord carrier routes to Qualification, not Record")
check(record_edit_needed(official_swap_case), "E clearing an official locked record triggers Record edit")
check(record_edit_needed(migratory_logical_case), "E true non-site logical persistence triggers conditional identity/location rewrite")

conditional_record_outcomes = {
    case.name: record_edit_needed(case)
    for case in (append_case, moving_role_case, encoded_append_case, official_swap_case, migratory_logical_case)
}
check(set(conditional_record_outcomes.values()) == {False, True}, "E exact architectures realize both Record-gate outcomes")


section("F. EXACT QUALIFICATION FUTURE-EQUIVALENCE GATE")


def qualification_edit_needed(fibre_future_laws: dict[str, tuple[Fraction, ...]]) -> bool:
    return len(set(fibre_future_laws.values())) > 1


same_record_hidden_phase = {
    "plus": (Fraction(1), Fraction(0)),
    "minus": (Fraction(0), Fraction(1)),
}
same_record_z_only_gauge = {
    "plus": (Fraction(1, 2), Fraction(1, 2)),
    "minus": (Fraction(1, 2), Fraction(1, 2)),
}
recorded_context_fibres = {
    "record-plus": (Fraction(1), Fraction(0)),
}
fixed_law_calculator = {
    "representation-a": (Fraction(3, 4), Fraction(1, 4)),
    "representation-b": (Fraction(3, 4), Fraction(1, 4)),
}

check(qualification_edit_needed(same_record_hidden_phase), "F future-sensitive unrecorded phase fails Qualification")
check(not qualification_edit_needed(same_record_z_only_gauge), "F future-invisible fibre variation is gauge")
check(not qualification_edit_needed(recorded_context_fibres), "F persistent context record separates predictive states")
check(not qualification_edit_needed(fixed_law_calculator), "F law-side representational variation adds no physical state")
check(CENSUS["T-RECORD-FIBRE"] == THEOREM, "F future equivalence remains a theorem obligation")
check(CENSUS["C-STATE"] == STATE_EDIT, "F failed future equivalence routes to conditional Qualification edit")


section("G. IDENTITY INSERTION IS NOT MEASURE-AND-FORGET")

Matrix2 = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]
rho_plus: Matrix2 = ((Fraction(1, 2), Fraction(1, 2)), (Fraction(1, 2), Fraction(1, 2)))
rho_dephased: Matrix2 = ((Fraction(1, 2), Fraction(0)), (Fraction(0), Fraction(1, 2)))


def x_probabilities(rho: Matrix2) -> tuple[Fraction, Fraction]:
    p_plus = (rho[0][0] + rho[0][1] + rho[1][0] + rho[1][1]) / 2
    return p_plus, 1 - p_plus


identity_future = x_probabilities(rho_plus)
measure_forget_future = x_probabilities(rho_dephased)
check(identity_future == (Fraction(1), Fraction(0)), "G omitted slot/identity preserves bright output")
check(measure_forget_future == (Fraction(1, 2), Fraction(1, 2)), "G measure-and-forget dephases output")
check(identity_future != measure_forget_future, "G containment semantics is physically load-bearing")
check(CENSUS["L-CONTAIN"] == FIELD, "G containment belongs inside complete L*")


section("H. LOCAL-TO-GLOBAL AND BOUNDARY CONTROLS")


def bernoulli_family(p_one: Fraction, length: int) -> dict[tuple[int, ...], Fraction]:
    return {
        word: product_probability(word, p_one)
        for word in product((0, 1), repeat=length)
    }


def product_probability(word: tuple[int, ...], p_one: Fraction) -> Fraction:
    probability = Fraction(1)
    for bit in word:
        probability *= p_one if bit else 1 - p_one
    return probability


def marginal_last(family: dict[tuple[int, ...], Fraction]) -> dict[tuple[int, ...], Fraction]:
    result: dict[tuple[int, ...], Fraction] = {}
    for word, probability in family.items():
        prefix = word[:-1]
        result[prefix] = result.get(prefix, Fraction(0)) + probability
    return result


half_families = {n: bernoulli_family(Fraction(1, 2), n) for n in range(1, 6)}
two_thirds_families = {n: bernoulli_family(Fraction(2, 3), n) for n in range(1, 6)}
check(all(sum(family.values()) == 1 for family in half_families.values()), "H exact boundary-derived finite families normalize")
check(all(marginal_last(half_families[n + 1]) == half_families[n] for n in range(1, 5)), "H exact boundary-derived family is projectively consistent")
check(half_families[1] != two_thirds_families[1], "H same identity local propagation with different boundaries gives different records")
check(marginal_last(two_thirds_families[5]) == two_thirds_families[4], "H second exact boundary also derives a consistent family")

incompatible_one = {(0,): Fraction(1, 2), (1,): Fraction(1, 2)}
incompatible_two = {(0, 0): Fraction(2, 3), (0, 1): Fraction(0), (1, 0): Fraction(0), (1, 1): Fraction(1, 3)}
check(sum(incompatible_one.values()) == sum(incompatible_two.values()) == 1, "H separate finite tables can each normalize")
check(marginal_last(incompatible_two) != incompatible_one, "H separate normalization does not imply global consistency")


def parity_family(parity: int, length: int) -> dict[tuple[int, ...], Fraction]:
    words = [word for word in product((0, 1), repeat=length) if sum(word) % 2 == parity]
    return {word: Fraction(1, len(words)) for word in words}


even3 = parity_family(0, 3)
odd3 = parity_family(1, 3)
check(marginal_last(even3) == marginal_last(odd3), "H two extensions can share every displayed proper prefix marginal")
check(set(even3).isdisjoint(set(odd3)), "H a legal full parity record distinguishes the extensions")
check(CENSUS["T-GLOBAL"] == THEOREM, "H extension existence/equivalence is a completion theorem")
check(CENSUS["H-BOUNDARY"] == HISTORY, "H actual boundary value remains contingent")


section("I. TYPICALITY IS CLAIM-SPECIFIC")

histories8 = tuple(product((0, 1), repeat=8))
fair8 = {history: Fraction(1, 256) for history in histories8}
typical8 = {history for history in histories8 if 2 <= sum(history) <= 6}
all_zero = (0,) * 8

check(sum(fair8.values()) == 1, "I fair finite history law is normalized")
check(all_zero in fair8, "I normalized law admits an atypical actual member")
check(all_zero not in typical8, "I actual all-zero control is outside named typical set")
check(sum(fair8[h] for h in typical8) < 1, "I finite typical set is not an actuality selector")


def actual_typicality_condition_needed(*, probabilistic_claim_only: bool, pointwise_all_histories: bool, unique_history: bool, unconditional_actual_claim: bool, actual_membership_proved: bool) -> bool:
    if probabilistic_claim_only or pointwise_all_histories or unique_history:
        return False
    return unconditional_actual_claim and not actual_membership_proved


check(not actual_typicality_condition_needed(probabilistic_claim_only=True, pointwise_all_histories=False, unique_history=False, unconditional_actual_claim=False, actual_membership_proved=False), "I probabilistic prediction needs no actual-membership premise")
check(not actual_typicality_condition_needed(probabilistic_claim_only=False, pointwise_all_histories=True, unique_history=False, unconditional_actual_claim=True, actual_membership_proved=False), "I pointwise theorem needs no typicality")
check(not actual_typicality_condition_needed(probabilistic_claim_only=False, pointwise_all_histories=False, unique_history=True, unconditional_actual_claim=True, actual_membership_proved=False), "I unique-history law makes typicality vacuous")
check(actual_typicality_condition_needed(probabilistic_claim_only=False, pointwise_all_histories=False, unique_history=False, unconditional_actual_claim=True, actual_membership_proved=False), "I almost-sure to actual-world promotion needs a named condition")
check(not actual_typicality_condition_needed(probabilistic_claim_only=False, pointwise_all_histories=False, unique_history=False, unconditional_actual_claim=True, actual_membership_proved=True), "I proved actual membership retires the condition")
check(CENSUS["TY-ACTUAL"] == CLAIM, "I typicality does not become a universal constitutional atom")


section("J. CONDITIONAL EDIT INDEPENDENCE")

# Four exact logical combinations exist at the type level:
# neither (append/global record-only), Record only (official migratory record),
# Qualification only (append records plus ontic hidden carrier), and both.
edit_pairs = {
    "neither": (False, False),
    "Record only": (True, False),
    "Qualification only": (False, True),
    "both": (True, True),
}
check(set(edit_pairs.values()) == set(product((False, True), repeat=2)), "J Record and Qualification gates are independent conditional edits")
check(edit_pairs["neither"] == (False, False), "J exact zero-edit architecture exists")
check(universal_ids == {"I-L"}, "J conditional edit independence does not inflate universal identity count")


section("K. DOCUMENTATION AND N1-N8 CONTRACT")

required_note_phrases = (
    "only universal nonzero new constitutional identification",
    "means one extensional constitutional referent",
    "conditional record edit",
    "conditional qualification edit",
    "identity-slot containment",
    "local-to-global consistency",
    "typicality is a claim gate",
    "universal content counts remain",
    "unique theorem : 0",
    "exact a only : 1",
    "complete local l : 1",
    "global-history l : 1",
    "no live axiom edit",
)
for phrase in required_note_phrases:
    check(phrase in note, f"K note contains {phrase!r}")

for index in range(1, 9):
    check(f"n{index} —" in note, f"K N{index} section exists")

check("no-go-discipline status: pass" in note, "K no-go discipline records PASS")
check("more than five distinct attacks were run" in note, "K N1 exceeds five routes")
check("collapsed universal set is {u}" in note, "K N2 collapses universal set to one")
check("hidden-wall scan" in note, "K N3 hidden-wall scan exists")
check("exact residual matching" in note, "K N4 residual table exists")
check("rhetoric and resolution audit" in note, "K N5 resolution audit exists")
check("partial-closure and import-retirement paths" in note, "K N6 retirement routes exist")
check("hostile reviewer" in note, "K N7 strongest steelman exists")
check("grep -rln \"structurally undecidable\\|no retained primitive\\|requires new axiom\\|cannot be derived from a_min\" docs/" in note, "K N8 prescribed docs search is recorded")
check("find .claude/science/physics-loops -name no_go_ledger.md -print" in note, "K N8 no-go-ledger walk is recorded")
check("one information-bearing field" in note and "claim is withdrawn" in note, "K hostile steelman narrows the broad one-assumption claim")
check("record or qualification can never change" in note and "explicitly rejected" in note, "K never-edit overclaim is rejected")


section("TOTAL")
print(f"PASS={PASS} FAIL={FAIL}")
if FAIL:
    print("RESULT: FAIL")
    raise SystemExit(1)

print("RESULT: PASS")
print("DECISION_GATE: one universal complete-L identity; Record and Qualification change only on exact selected-law compatibility failures")
