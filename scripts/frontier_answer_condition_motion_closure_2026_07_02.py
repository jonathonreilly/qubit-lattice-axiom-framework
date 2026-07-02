#!/usr/bin/env python3
"""Exact toy checks for the 2026-07-02 final derivation note."""

from fractions import Fraction
from itertools import permutations, product
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
NOTE_PATH = (
    ROOT
    / "docs"
    / "READING_NOTE_FINAL_DERIVATIONS_MOTION_CLOSURE_BOUNDED_NOTE_2026-07-02.md"
)


def compact(text):
    return " ".join(text.split())


AXIOM_TEXT = AXIOM_PATH.read_text(encoding="utf-8")
AXIOM_COMPACT = compact(AXIOM_TEXT)
try:
    NOTE_TEXT = NOTE_PATH.read_text(encoding="utf-8")
except FileNotFoundError:
    NOTE_TEXT = ""


LATTICE_MOTION = (
    "Physical sites are the points of the cubic lattice `Z^3`, with "
    "nearest-neighbor adjacency, standard translations, and proper cubic "
    "rotations about each site."
)
LATTICE_DISTINCTION = (
    "No site is privileged. Sites are distinguished by the supplied lattice "
    "structure alone."
)
QUBIT_DOMAIN = "Each site has a domain of local possibilities."
QUBIT_DISTINCTION = (
    "No possibility is privileged. Possibilities are distinguished by the "
    "supplied algebraic structure alone."
)
QUBIT_SHARED_DOMAIN = (
    "The full one-site possibility domain has algebraic presentation `M_2(C)`."
)
QUBIT_EQUIVALENCE = (
    "A `Cl(3,0)`-compatible real-algebra presentation may be used equivalently "
    "and adds no further primitive structure."
)
ADMISSIBILITY_COVARIANCE = (
    "There is one fixed nearest-neighbor admissibility rule, covariant under "
    "lattice translations and proper cubic rotations."
)
RECORD_ABSENCE = "A site need not carry a record."
RECORD_LOCK = (
    "When present, a record locks exactly one local possibility from the subset "
    "available at that site under Admissibility; the locked possibility is "
    "invariant under repeated readout."
)
READABILITY = (
    "Only records are readable. A readout value is determined by record content "
    "alone. For any finite collection of pairwise-disjoint records, scalar "
    "readout `I` is additive, with `I(empty)=0`."
)
MINIMALITY = (
    "These axioms state only their named primitive content. Further physical "
    "structure requires derivation, bridge, explicit admission, or approved "
    "primitive registration before use as a premise."
)
STATE_DEFINITION = "A state is a configuration of records."
LAW_SENTENCE = (
    "A law privileges no states. Its domain is a supplied condition, and at "
    "every state where the condition holds it gives exactly one answer."
)


def has_sentence(sentence):
    return sentence in AXIOM_COMPACT


# Bounded wraparound model for exhaustive finite checks, not a new premise.
N = 2
SITES = tuple(product(range(N), repeat=3))
SITE_INDEX = {site: index for index, site in enumerate(SITES)}
POSSIBILITIES = ("p", "q")
VALUES = {None: None, "p": Fraction(1, 1), "q": Fraction(2, 1)}


def add_site(left, right):
    return tuple((left[i] + right[i]) % N for i in range(3))


def neighbors(site):
    result = set()
    for axis in range(3):
        for delta in (-1, 1):
            shifted = list(site)
            shifted[axis] = (shifted[axis] + delta) % N
            result.add(tuple(shifted))
    return frozenset(result)


def permutation_sign(perm):
    inversions = 0
    for i in range(3):
        for j in range(i + 1, 3):
            if perm[i] > perm[j]:
                inversions += 1
    return -1 if inversions % 2 else 1


ROTATIONS = []
for perm in permutations(range(3)):
    for signs in product((-1, 1), repeat=3):
        if permutation_sign(perm) * signs[0] * signs[1] * signs[2] == 1:
            ROTATIONS.append((perm, signs))


def rotate(site, rotation):
    perm, signs = rotation
    return tuple((signs[i] * site[perm[i]]) % N for i in range(3))


MOTIONS = []
seen_motions = set()
for rotation in ROTATIONS:
    for translation in SITES:
        image = tuple(
            SITE_INDEX[add_site(rotate(site, rotation), translation)]
            for site in SITES
        )
        if image not in seen_motions:
            seen_motions.add(image)
            MOTIONS.append(image)
MOTIONS = tuple(MOTIONS)
TRANSLATE_X = tuple(SITE_INDEX[add_site(site, (1, 0, 0))] for site in SITES)


def record_content(state, site):
    return state[SITE_INDEX[site]]


def transport(state, motion):
    carried = [None] * len(SITES)
    for old_index, new_index in enumerate(motion):
        carried[new_index] = state[old_index]
    return tuple(carried)


def neighbor_record_count(state, site):
    return sum(1 for neighbor in neighbors(site) if record_content(state, neighbor))


def available(state, site):
    if neighbor_record_count(state, site) % 2 == 0:
        return frozenset(POSSIBILITIES)
    return frozenset(("p",))


def is_state(state):
    for site in SITES:
        content = record_content(state, site)
        if content is not None and content not in available(state, site):
            return False
    return True


ALL_ASSIGNMENTS = tuple(product((None,) + POSSIBILITIES, repeat=len(SITES)))
VALID_STATES = tuple(state for state in ALL_ASSIGNMENTS if is_state(state))
EMPTY_STATE = tuple(None for _ in SITES)
S0 = (0, 0, 0)


def state_with(site, possibility):
    state = [None] * len(SITES)
    state[SITE_INDEX[site]] = possibility
    return tuple(state)


def readout_value(state, site):
    content = record_content(state, site)
    if content is None:
        raise ValueError("only records are readable")
    return VALUES[content]


def any_record(state):
    return any(content is not None for content in state)


def record_neighbor_free(state):
    for site in SITES:
        if record_content(state, site) is not None:
            if any(record_content(state, neighbor) is None for neighbor in neighbors(site)):
                return True
    return False


def unique_record_p(state):
    records = [content for content in state if content is not None]
    return len(records) == 1 and records[0] == "p"


def every_q_has_record_neighbors(state):
    for site in SITES:
        if record_content(state, site) == "q":
            if any(record_content(state, neighbor) is None for neighbor in neighbors(site)):
                return False
    return True


def extension_closed(condition):
    for state in VALID_STATES:
        expected = condition(state)
        for motion in MOTIONS:
            if condition(transport(state, motion)) != expected:
                return False
    return True


def extension_motion_closed(extension):
    for state in VALID_STATES:
        expected = state in extension
        for motion in MOTIONS:
            if (transport(state, motion) in extension) != expected:
                return False
    return True


def exactly_one_answer_law(condition, answer_objects, answer_domain=None):
    for state in VALID_STATES:
        if condition(state):
            answers = tuple(answer_objects(state))
            if len(answers) != 1:
                return False
            if answer_domain is not None and not answer_domain(answers[0]):
                return False
    return True


class ToyCondition:
    def __init__(self, description, func=None, uses_non_state=False):
        self.description = description
        self.func = func
        self.uses_non_state = uses_non_state

    def extension(self, states):
        if self.uses_non_state or self.func is None:
            return None
        return frozenset(state for state in states if self.func(state))


def supplied_answer_domain(answer):
    return isinstance(answer, frozenset)


def absence_predicate_statewise():
    condition = ToyCondition(
        "site S0 lacks a record",
        lambda state: record_content(state, S0) is None,
    )
    extension = condition.extension(VALID_STATES)
    return extension is not None and EMPTY_STATE in extension and state_with(S0, "p") not in extension


def non_state_condition_has_no_state_set():
    condition = ToyCondition("depends on an external clock", uses_non_state=True)
    return condition.extension(VALID_STATES) is None


def readability_scopes_values_only():
    absent_condition = record_content(EMPTY_STATE, S0) is None
    try:
        readout_value(EMPTY_STATE, S0)
        absence_unreadable = False
    except ValueError:
        absence_unreadable = True
    present_state = state_with(S0, "p")
    return absent_condition and absence_unreadable and readout_value(present_state, S0) == Fraction(1, 1)


def motion_preserves_statehood():
    return all(is_state(transport(state, motion)) for state in VALID_STATES for motion in MOTIONS)


def anchored_condition_is_moved_and_flagged():
    anchored = lambda state: record_content(state, S0) is not None
    moved = transport(state_with(S0, "p"), TRANSLATE_X)
    recovered_anchor = {
        site
        for site in SITES
        if all(
            record_content(state, site) is not None
            for state in VALID_STATES
            if anchored(state)
        )
    }
    return (
        anchored(state_with(S0, "p"))
        and not anchored(moved)
        and not extension_closed(anchored)
        and recovered_anchor == {S0}
    )


def rigid_state_list_generically_fails_with_empty_exception():
    singleton = state_with(S0, "p")
    moved_singleton = transport(singleton, TRANSLATE_X)
    rigid_list = frozenset((singleton,))
    empty_list = frozenset((EMPTY_STATE,))
    rigid_fails = singleton in rigid_list and moved_singleton not in rigid_list
    empty_exception = all(transport(EMPTY_STATE, motion) in empty_list for motion in MOTIONS)
    return rigid_fails and empty_exception


def axiom_expressible_profile(condition):
    extension = condition.extension(VALID_STATES)
    return (
        extension,
        len(extension),
        EMPTY_STATE in extension,
        extension_motion_closed(extension),
    )


def coextensional_conditions_get_same_axiom_verdicts():
    condition_a = ToyCondition("some site carries a record", any_record)
    condition_b = ToyCondition("not the empty configuration", lambda state: state != EMPTY_STATE)
    return (
        condition_a.extension(VALID_STATES) == condition_b.extension(VALID_STATES)
        and axiom_expressible_profile(condition_a) == axiom_expressible_profile(condition_b)
    )


def vocabulary_sensitive_judge_requires_unsupplied_attribute():
    condition_a = ToyCondition("some site carries a record", any_record)
    condition_b = ToyCondition("not the empty configuration", lambda state: state != EMPTY_STATE)

    def vocabulary_judge(condition):
        return "empty" not in condition.description

    return (
        condition_a.extension(VALID_STATES) == condition_b.extension(VALID_STATES)
        and vocabulary_judge(condition_a) != vocabulary_judge(condition_b)
    )


N3 = 3
SITES3 = tuple(product(range(N3), repeat=3))
SITE_INDEX3 = {site: index for index, site in enumerate(SITES3)}


def add_site3(left, right):
    return tuple((left[i] + right[i]) % N3 for i in range(3))


def neighbors3(site):
    result = set()
    for axis in range(3):
        for delta in (-1, 1):
            shifted = list(site)
            shifted[axis] = (shifted[axis] + delta) % N3
            result.add(tuple(shifted))
    return frozenset(result)


def rotate3(site, rotation):
    perm, signs = rotation
    return tuple((signs[i] * site[perm[i]]) % N3 for i in range(3))


ROT3_PLAIN = ((1, 2, 0), (1, 1, 1))
ROT3_SIGNED = ((1, 0, 2), (-1, 1, 1))
assert permutation_sign(ROT3_PLAIN[0]) * ROT3_PLAIN[1][0] * ROT3_PLAIN[1][1] * ROT3_PLAIN[1][2] == 1
assert permutation_sign(ROT3_SIGNED[0]) * ROT3_SIGNED[1][0] * ROT3_SIGNED[1][1] * ROT3_SIGNED[1][2] == 1


def motion3(rotation, translation):
    return tuple(
        SITE_INDEX3[add_site3(rotate3(site, rotation), translation)]
        for site in SITES3
    )


MOTIONS3 = (
    motion3(ROT3_PLAIN, (0, 0, 0)),
    motion3(ROT3_SIGNED, (0, 0, 0)),
    motion3(((0, 1, 2), (1, 1, 1)), (1, 0, 0)),
)


def transport3(state, motion):
    carried = [None] * len(SITES3)
    for old_index, new_index in enumerate(motion):
        carried[new_index] = state[old_index]
    return tuple(carried)


def record_content3(state, site):
    return state[SITE_INDEX3[site]]


def available3(state, site):
    count = sum(1 for neighbor in neighbors3(site) if record_content3(state, neighbor))
    return frozenset(POSSIBILITIES) if count % 2 == 0 else frozenset(("p",))


def is_state3(state):
    for site in SITES3:
        content = record_content3(state, site)
        if content is not None and content not in available3(state, site):
            return False
    return True


def state3_with(assignments):
    state = [None] * len(SITES3)
    for site, possibility in assignments:
        state[SITE_INDEX3[site]] = possibility
    return tuple(state)


def sampled_states3():
    samples = [tuple(None for _ in SITES3)]
    for site in SITES3:
        for possibility in POSSIBILITIES:
            samples.append(state3_with(((site, possibility),)))
    pool = ((0, 0, 0), (1, 1, 0), (0, 1, 2), (2, 2, 2), (1, 0, 2), (2, 1, 0))
    for i in range(len(pool)):
        for j in range(i + 1, len(pool)):
            samples.append(state3_with(((pool[i], "p"), (pool[j], "q"))))
    return tuple(state for state in samples if is_state3(state))


def any_record3(state):
    return any(content is not None for content in state)


def record_neighbor_free3(state):
    for site in SITES3:
        if record_content3(state, site) is not None:
            if any(record_content3(state, neighbor) is None for neighbor in neighbors3(site)):
                return True
    return False


def unique_record_p3(state):
    records = [content for content in state if content is not None]
    return len(records) == 1 and records[0] == "p"


def n3_neighbor_count_is_six():
    return all(len(neighbors3(site)) == 6 for site in SITES3)


def n3_sampled_pattern_closure():
    conditions = (any_record3, record_neighbor_free3, unique_record_p3)
    for state in sampled_states3():
        for motion in MOTIONS3:
            moved = transport3(state, motion)
            if not is_state3(moved):
                return False
            for condition in conditions:
                if condition(moved) != condition(state):
                    return False
    return True


def note_boundary_phrases_present():
    lowered = NOTE_TEXT.lower()
    return all(
        phrase in lowered
        for phrase in (
            "does not adjudicate",
            "no axiom sentence is proposed",
            "escape",
            "generically",
        )
    )


def note_avoids_disallowed_status_words():
    lowered = NOTE_TEXT.lower()
    return "retained" not in lowered and "verified" not in lowered


CHECKS = (
    ("lattice motion sentence is present", lambda: has_sentence(LATTICE_MOTION)),
    ("lattice distinction clause is present", lambda: has_sentence(LATTICE_DISTINCTION)),
    ("qubit domain sentence is present", lambda: has_sentence(QUBIT_DOMAIN)),
    ("qubit distinction clause is present", lambda: has_sentence(QUBIT_DISTINCTION)),
    ("Admissibility covariance sentence is present", lambda: has_sentence(ADMISSIBILITY_COVARIANCE)),
    ("record absence and lock sentences are present", lambda: has_sentence(RECORD_ABSENCE) and has_sentence(RECORD_LOCK)),
    ("readability sentence is present", lambda: has_sentence(READABILITY)),
    ("Qualification minimality sentence is present", lambda: has_sentence(MINIMALITY)),
    ("state definition sentence is present", lambda: has_sentence(STATE_DEFINITION)),
    ("law sentence with supplied condition and exactly one answer is present", lambda: has_sentence(LAW_SENTENCE)),
    (
        "qubit shared-domain and presentation-equivalence sentences are present",
        lambda: has_sentence(QUBIT_SHARED_DOMAIN) and has_sentence(QUBIT_EQUIVALENCE),
    ),
    (
        "set-valued verdicts count as one answer object through a supplied answer-domain",
        lambda: exactly_one_answer_law(
            any_record,
            lambda state: (frozenset((("left", Fraction(1, 2)), ("right", Fraction(1, 2)))),),
            supplied_answer_domain,
        ),
    ),
    (
        "two verdict objects at one in-domain state are rejected",
        lambda: not exactly_one_answer_law(
            lambda state: state == EMPTY_STATE,
            lambda state: (frozenset(("left",)), frozenset(("right",))),
            supplied_answer_domain,
        ),
    ),
    ("absence-referencing predicate is statewise and well-defined", absence_predicate_statewise),
    ("non-state-dependent condition has no state set", non_state_condition_has_no_state_set),
    ("readability is exercised on values only, not condition domains", readability_scopes_values_only),
    ("motion action preserves statehood under the covariant admissibility rule", motion_preserves_statehood),
    ("N=3 lattice has six distinct nearest neighbors per site", n3_neighbor_count_is_six),
    ("sampled N=3 states: statehood and pattern closure under proper, sign-bearing, and translated motions", n3_sampled_pattern_closure),
    ("pattern condition 'some site carries a record' is motion-closed", lambda: extension_closed(any_record)),
    ("pattern condition 'a record has a record-free neighbor' is motion-closed", lambda: extension_closed(record_neighbor_free)),
    ("pattern condition 'the unique record has possibility p' is motion-closed", lambda: extension_closed(unique_record_p)),
    ("per-site universally quantified structural rule is motion-closed", lambda: extension_closed(every_q_has_record_neighbors)),
    ("bare site anchor fails motion closure and is recoverable from its own extension", anchored_condition_is_moved_and_flagged),
    ("rigid state-list fails motion closure while the empty singleton is the honest exception", rigid_state_list_generically_fails_with_empty_exception),
    ("co-extensional toy conditions receive identical axiom-expressible verdicts", coextensional_conditions_get_same_axiom_verdicts),
    ("vocabulary-sensitive judge requires a condition attribute no axiom text supplies", vocabulary_sensitive_judge_requires_unsupplied_attribute),
    ("note contains boundary phrases for adjudication, procedure, escape, and genericity", note_boundary_phrases_present),
    ("note avoids disallowed audit-result vocabulary", note_avoids_disallowed_status_words),
)


def main():
    fail = 0
    for index, (description, predicate) in enumerate(CHECKS, start=1):
        try:
            ok = bool(predicate())
        except Exception:
            ok = False
        if not ok:
            fail += 1
        status = "PASS" if ok else "FAIL"
        print(f"CHECK {index:02d}: {status} — {description}")
    print(f"TOTAL: PASS={len(CHECKS) - fail} FAIL={fail}")
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main())
