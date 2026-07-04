#!/usr/bin/env python3
"""Mechanical checks for the landed Record-formation certification note.

The runner is intentionally narrow: exact text needles plus deterministic toy
models. Interpretive verdicts live in the companion note prose.
"""

from itertools import combinations
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
AXIOMS_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
NOTE_PATH = ROOT / "docs" / "RECORD_FORMATION_APPEND_CERTIFICATION_BOUNDED_NOTE_2026-07-04.md"
POLICY_PATH = ROOT / "docs" / "audit" / "AXIOM_MINIMALITY_POLICY.md"

LANDED_FORMATION_SENTENCE = "Records form."
POLICY_ENTRY_NEEDLE = "2026-07-04 -- Formation sentence"

PREMISE_NEEDLES = [
    (
        "state definition",
        "A state is a configuration of records.",
    ),
    (
        "per-site uniqueness plus permanence",
        "A\nsite never carries more than one record; records are permanent.",
    ),
    (
        "law-form sentence",
        "A law privileges no states. Its domain is a supplied condition, and at every\n"
        "state where the condition holds it gives exactly one answer.",
    ),
    (
        "named-primitive-content sentence",
        "These axioms state only their named primitive content. Further physical\n"
        "structure requires derivation, bridge, explicit admission, or approved\n"
        "primitive registration before use as a premise.",
    ),
]

NOTE_QUOTE_NEEDLES = [
    (
        "landed formation sentence",
        "Records form.",
    ),
    (
        "record-locking sentence",
        "When present, a record locks exactly one admissible local possibility.",
    ),
    (
        "per-site uniqueness plus permanence quote",
        "A\nsite never carries more than one record; records are permanent.",
    ),
    (
        "empty readout quote",
        "For any finite collection of pairwise-disjoint records, scalar readout\n"
        "`I` is additive, with `I(empty)=0`.",
    ),
    *PREMISE_NEEDLES,
]

NOTE_PROSE_NEEDLES = [
    (
        "occurrence-strength verdict",
        "the realized record history\nis not empty-forever",
    ),
    (
        "empty-state boundary",
        "The empty configuration remains a valid state",
    ),
    (
        "extension lemma verdict",
        "Succession, wherever\nit exists, is monotone. This does NOT assert that successors exist at every state.",
    ),
    (
        "saturation wall",
        '"no state is final" is FALSE in the landed state space',
    ),
    (
        "law-form over-supply wall",
        "any law-form\nreading over-supplies the landed sentence",
    ),
    (
        "owner ruling occurrence strength",
        "occurrence strength as the unique non-over-supplying form",
    ),
    (
        "formation-rule residual",
        "a formation rule: which admissible possibility, which site, what weight, or\n  what rate",
    ),
    (
        "sweep consequence formation family",
        'the 2026-06-06 "formation not unconditionally\nforced" family narrows its residual to the formation rule',
    ),
    (
        "sweep consequence past-hypothesis",
        "the Past-Hypothesis\nvacuous-empty-history hole closes at occurrence strength",
    ),
    (
        "sweep consequence single-clock",
        "the single-clock\nnote's claim that \"at least one record exists\" is not an axiom consequence flips",
    ),
]

WINDOW = tuple(range(4))


def read_text(path):
    try:
        return path.read_text(encoding="utf-8"), ""
    except OSError as exc:
        return "", str(exc)


def check(results, label, condition, detail=""):
    results.append((label, bool(condition), detail))


def all_window_configs():
    configs = []
    for size in range(len(WINDOW) + 1):
        for occupied in combinations(WINDOW, size):
            configs.append({site: f"r{site}" for site in occupied})
    return configs


def is_state(config):
    return isinstance(config, dict) and len(config) == len(set(config))


def extends_config(previous, successor):
    return all(site in successor and successor[site] == value for site, value in previous.items())


def strict_extension(previous, successor):
    return extends_config(previous, successor) and len(successor) > len(previous)


def valid_formation_successors(config, window=WINDOW):
    successors = []
    for site in window:
        if site not in config:
            successor = dict(config)
            successor[site] = f"r{site}"
            successors.append(successor)
    return successors


def first_unrecorded_successor(config, window=WINDOW):
    successors = valid_formation_successors(config, window)
    return successors[0] if successors else None


def no_unrecorded_site(config, window=WINDOW):
    return all(site in config for site in window)


def history_has_occurrence(history):
    return any(len(after) > len(before) for before, after in zip(history, history[1:]))


def extension_lemma_checks(results):
    configs = all_window_configs()
    non_saturated = [config for config in configs if not no_unrecorded_site(config)]
    successors = [
        (config, successor)
        for config in non_saturated
        for successor in valid_formation_successors(config)
    ]

    check(results, "extension lemma enumerates non-saturated finite configurations", len(non_saturated) == 15)
    check(results, "extension lemma enumerates all one-site formation successors", len(successors) == 32)
    check(
        results,
        "extension lemma successors strictly extend predecessors",
        all(strict_extension(config, successor) for config, successor in successors),
    )
    check(
        results,
        "extension lemma successors increase size by one",
        all(len(successor) == len(config) + 1 for config, successor in successors),
    )
    check(
        results,
        "extension lemma successors do not overwrite old records",
        all(
            all(successor[site] == value for site, value in config.items())
            for config, successor in successors
        ),
    )


def saturation_exhibit_checks(results):
    saturated = {site: f"r{site}" for site in WINDOW}
    successors = valid_formation_successors(saturated)

    check(results, "infinite-lattice saturation shadow is fully recorded in finite window", no_unrecorded_site(saturated))
    check(results, "infinite-lattice saturation shadow is still a state", is_state(saturated))
    check(
        results,
        "infinite-lattice saturation shadow has no valid successor under permanence plus uniqueness",
        successors == [],
    )


def law_form_oversupply_checks(results):
    configs = all_window_configs()
    non_saturated = [config for config in configs if not no_unrecorded_site(config)]
    universal_domain_map = {
        frozenset(config.items()): first_unrecorded_successor(config)
        for config in non_saturated
    }
    fired = [successor for successor in universal_domain_map.values() if successor is not None]

    check(
        results,
        "rejected law-form exhibit fires on every non-saturated state of the window",
        len(fired) == len(non_saturated),
        "this is what the rejected reading forces: maximal rate",
    )
    check(
        results,
        "rejected law-form exhibit count equals all non-saturated states",
        len(fired) == (2 ** len(WINDOW)) - 1,
    )
    check(
        results,
        "rejected law-form exhibit has no supplied silence inside its domain",
        all(successor is not None for successor in universal_domain_map.values()),
    )
    check(
        results,
        "rejected law-form exhibit still preserves extension where it fires",
        all(
            strict_extension(dict(key), successor)
            for key, successor in universal_domain_map.items()
            if successor is not None
        ),
    )


def rejector_checks(results):
    drop_permanence_previous = {0: "r0", 1: "r1"}
    drop_permanence_successor = {1: "r1", 2: "r2"}
    drop_uniqueness_previous = {0: "r0"}
    drop_uniqueness_overwrite_successor = {0: "r1"}
    empty = {}
    empty_forever_history = [empty, empty, empty]
    occurrence_history = [empty, {0: "r0"}]

    check(
        results,
        "rejector: drop permanence and extension can fail",
        not extends_config(drop_permanence_previous, drop_permanence_successor),
    )
    check(
        results,
        "rejector: drop uniqueness and overwrite becomes possible",
        not extends_config(drop_uniqueness_previous, drop_uniqueness_overwrite_successor),
    )
    check(
        results,
        "rejector: empty-forever history violates occurrence",
        not history_has_occurrence(empty_forever_history),
    )
    check(
        results,
        "rejector: empty-as-a-state remains valid while occurrence history can fire",
        is_state(empty) and history_has_occurrence(occurrence_history),
    )


def main():
    results = []
    axioms, axioms_error = read_text(AXIOMS_PATH)
    note, note_error = read_text(NOTE_PATH)
    policy, policy_error = read_text(POLICY_PATH)

    check(results, "axiom file readable", not axioms_error, axioms_error)
    check(results, "note file readable", not note_error, note_error)
    check(results, "policy file readable", not policy_error, policy_error)

    check(
        results,
        "landed guard: axiom file contains Records form.",
        LANDED_FORMATION_SENTENCE in axioms,
    )
    check(results, "policy entry needle present", POLICY_ENTRY_NEEDLE in policy)

    for label, needle in PREMISE_NEEDLES:
        check(results, f"premise present in landed axiom file: {label}", needle in axioms)

    for label, needle in NOTE_QUOTE_NEEDLES:
        check(results, f"note contains verbatim quote: {label}", needle in note)

    for label, needle in NOTE_PROSE_NEEDLES:
        check(results, f"note prose verdict present: {label}", needle in note)

    extension_lemma_checks(results)
    saturation_exhibit_checks(results)
    law_form_oversupply_checks(results)
    rejector_checks(results)

    passed = 0
    failed = 0
    for index, (label, ok, detail) in enumerate(results, start=1):
        status = "PASS" if ok else "FAIL"
        if ok:
            passed += 1
        else:
            failed += 1
        suffix = f" -- {detail}" if detail else ""
        print(f"CHECK {index:02d}: {status} - {label}{suffix}")

    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
