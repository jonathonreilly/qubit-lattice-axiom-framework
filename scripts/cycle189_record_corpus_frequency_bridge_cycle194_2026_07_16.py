#!/usr/bin/env python3
"""Cycle 194: compose the Cycle-189 process with record-corpus frequency laws.

This runner is authority-free.  It checks the exact one-block pointer
distributions from Cycle 189, constructs several projectively consistent
repeated-block extensions with those same marginals, and isolates the
component-mean condition that converts process weights into record
frequencies.  It does not derive the Born trace pairing, select an actual
history, amend an axiom, or edit any authority surface.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
from itertools import product
from math import lcm
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "CYCLE189_RECORD_CORPUS_FREQUENCY_BRIDGE_CYCLE194_NOTE_2026-07-16.md"
)
CYCLE189_RUNNER = ROOT / "scripts/preterminal_context_quantum_process_cycle189_2026_07_16.py"
CYCLE189_NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "PRETERMINAL_CONTEXT_QUANTUM_PROCESS_CYCLE189_NOTE_2026-07-16.md"
)
CYCLE21_RUNNER = ROOT / "scripts/certified_record_corpus_ergodic_frequency_cycle21_2026_07_14.py"
CYCLE21_NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "CERTIFIED_RECORD_CORPUS_ERGODIC_FREQUENCY_CYCLE21_NOTE_2026-07-14.md"
)
CYCLE27_RUNNER = ROOT / "scripts/stochastic_record_history_actuality_semantics_cycle27_2026_07_14.py"
CYCLE27_NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "STOCHASTIC_RECORD_HISTORY_ACTUALITY_SEMANTICS_CYCLE27_NOTE_2026-07-14.md"
)

FROZEN = {
    CYCLE189_RUNNER: "a06853a529723332c774112d5aad8e53d9a91ad486de70de201cfcb8b501fe34",
    CYCLE189_NOTE: "97c2e98f90cef08063a3589d31555fbe76a18cbbbd3b8fb677c3b03603c54ded",
    CYCLE21_RUNNER: "3ad66712181905819f02c658eec7c9b80156890835d2179251ff2f79156b1c02",
    CYCLE21_NOTE: "3bfe04c7ac2416d1d4586823ef9d1f23f2c15121cca55ad75f14277b65286d31",
    CYCLE27_RUNNER: "35791d8610ca498116bf49cde1ddcdd3ac36ba9ef639380e4b577d1116e945a4",
    CYCLE27_NOTE: "d065db31bc81a07cc0f292d76817446f04a620fd71a0412c75675d35473148f3",
}

PASS = 0
FAIL = 0

Outcome = tuple[int, int, int]
Word = tuple[Outcome, ...]
Distribution = dict[Outcome, Fraction]
Law = dict[Word, Fraction]


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    suffix = f" :: {detail}" if detail != "" else ""
    if condition:
        PASS += 1
        print(f"PASS {label}{suffix}")
    else:
        FAIL += 1
        print(f"FAIL {label}{suffix}")


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def load_cycle189():
    spec = spec_from_file_location("cycle189_frequency_source", CYCLE189_RUNNER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load Cycle 189")
    module = module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def as_fraction(value) -> Fraction:
    value = value.cancel()
    return Fraction(int(value.p), int(value.q))


def positive_support(distribution: Distribution) -> tuple[Outcome, ...]:
    return tuple(sorted(outcome for outcome, weight in distribution.items() if weight))


def add_weight(law: Law, word: Word, weight: Fraction) -> None:
    law[word] = law.get(word, Fraction(0)) + weight


def product_law(distribution: Distribution, horizon: int) -> Law:
    support = positive_support(distribution)
    return {
        word: product_fraction(distribution[outcome] for outcome in word)
        for word in product(support, repeat=horizon)
    }


def product_fraction(values) -> Fraction:
    out = Fraction(1)
    for value in values:
        out *= value
    return out


def sticky_markov_law(distribution: Distribution, horizon: int) -> Law:
    """Stationary P(i,j)=1/2 delta_ij + 1/2 p(j)."""
    support = positive_support(distribution)
    law: Law = {}
    for word in product(support, repeat=horizon):
        weight = distribution[word[0]]
        for left, right in zip(word, word[1:]):
            transition = distribution[right] / 2
            if left == right:
                transition += Fraction(1, 2)
            weight *= transition
        law[word] = weight
    return law


def frozen_law(distribution: Distribution, horizon: int) -> Law:
    return {
        (outcome,) * horizon: weight
        for outcome, weight in distribution.items()
        if weight
    }


def balanced_period(distribution: Distribution) -> tuple[Outcome, ...]:
    denominator = 1
    for weight in distribution.values():
        denominator = lcm(denominator, weight.denominator)
    period: list[Outcome] = []
    for outcome in sorted(distribution):
        weight = distribution[outcome]
        period.extend([outcome] * (weight.numerator * denominator // weight.denominator))
    if len(period) != denominator:
        raise AssertionError((distribution, denominator, period))
    return tuple(period)


def balanced_law(distribution: Distribution, horizon: int) -> Law:
    period = balanced_period(distribution)
    law: Law = {}
    for phase in range(len(period)):
        word = tuple(period[(phase + offset) % len(period)] for offset in range(horizon))
        add_weight(law, word, Fraction(1, len(period)))
    return law


def mixture_law(left: Law, right: Law) -> Law:
    words = set(left) | set(right)
    return {
        word: (left.get(word, Fraction(0)) + right.get(word, Fraction(0))) / 2
        for word in words
    }


def law_total(law: Law) -> Fraction:
    return sum(law.values(), Fraction(0))


def marginal(law: Law, index: int) -> Distribution:
    out: dict[Outcome, Fraction] = defaultdict(Fraction)
    for word, weight in law.items():
        out[word[index]] += weight
    return dict(out)


def projectively_stationary(generator, distribution: Distribution, horizon: int) -> bool:
    short = generator(distribution, horizon)
    long = generator(distribution, horizon + 1)
    support = positive_support(distribution)
    if law_total(short) != 1 or law_total(long) != 1:
        return False
    for word in product(support, repeat=horizon):
        left = sum((long.get((outcome,) + word, Fraction(0)) for outcome in support), Fraction(0))
        right = sum((long.get(word + (outcome,), Fraction(0)) for outcome in support), Fraction(0))
        if left != short.get(word, Fraction(0)) or right != short.get(word, Fraction(0)):
            return False
    return True


def empirical_distribution(word: Word) -> Distribution:
    out: dict[Outcome, Fraction] = defaultdict(Fraction)
    for outcome in word:
        out[outcome] += Fraction(1, len(word))
    return dict(out)


def complete_distribution(distribution: Distribution) -> Distribution:
    return {outcome: weight for outcome, weight in distribution.items() if weight}


def balanced_orbits_match(distribution: Distribution) -> bool:
    period = balanced_period(distribution)
    target = complete_distribution(distribution)
    for phase in range(len(period)):
        orbit = tuple(period[(phase + offset) % len(period)] for offset in range(len(period)))
        if empirical_distribution(orbit) != target:
            return False
    return True


def frozen_has_wrong_components(distribution: Distribution) -> bool:
    target = complete_distribution(distribution)
    support = positive_support(distribution)
    if len(support) <= 1:
        return False
    return all(empirical_distribution((outcome,)) != target for outcome in support)


def certified_records(
    preparation: str,
    context: str,
    word: Word,
) -> tuple[tuple[int, str, object], ...]:
    records: list[tuple[int, str, object]] = []
    for index, outcome in enumerate(word):
        records.extend(
            (
                (index, "PREPARATION", preparation),
                (index, "CONTEXT", context),
                (index, "POINTER", outcome),
                (index, "CLOSE", index),
            )
        )
    return tuple(records)


def decode_certified_records(
    preparation: str,
    context: str,
    records: tuple[tuple[int, str, object], ...],
) -> Word:
    if len(records) % 4:
        raise ValueError("incomplete trial block")
    outcomes: list[Outcome] = []
    for offset in range(0, len(records), 4):
        index = offset // 4
        prep, ctx, pointer, close = records[offset : offset + 4]
        if prep != (index, "PREPARATION", preparation):
            raise ValueError("bad preparation certificate")
        if ctx != (index, "CONTEXT", context):
            raise ValueError("bad context certificate")
        if close != (index, "CLOSE", index):
            raise ValueError("bad close certificate")
        if pointer[0] != index or pointer[1] != "POINTER":
            raise ValueError("bad pointer record")
        outcomes.append(pointer[2])
    return tuple(outcomes)


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    print("FROZEN PREDECESSORS")
    observed = {path: digest(path) for path in FROZEN}
    check(
        "Cycle 189, Cycle 21, and Cycle 27 remain frozen",
        observed == FROZEN,
        {path.name: value for path, value in observed.items()},
    )

    cycle189 = load_cycle189()
    protocols: dict[tuple[str, str], Distribution] = {}
    parity_failures = []
    for preparation in cycle189.PREPARATIONS:
        for context in cycle189.CONTEXT_BY_LABEL:
            raw = cycle189.context_outcome_distribution(preparation, context)
            distribution = {
                outcome: as_fraction(weight)
                for outcome, weight in raw.items()
            }
            protocols[(preparation, context)] = distribution
            sign = cycle189.CONTEXT_BY_LABEL[context].product_sign
            for outcome, weight in distribution.items():
                if weight and outcome[0] * outcome[1] * outcome[2] != sign:
                    parity_failures.append((preparation, context, outcome, weight))

    print("\nONE-BLOCK CYCLE-189 DISTRIBUTIONS")
    weight_set = {
        weight
        for distribution in protocols.values()
        for weight in distribution.values()
    }
    support_histogram: dict[int, int] = defaultdict(int)
    for distribution in protocols.values():
        support_histogram[len(positive_support(distribution))] += 1
    check(
        "all twelve preparation-context distributions are normalized exact records",
        len(protocols) == 12
        and all(sum(distribution.values(), Fraction(0)) == 1 for distribution in protocols.values()),
        {"protocols": len(protocols), "weights": sorted(weight_set)},
    )
    check(
        "all positive pointer records obey the signed context parity",
        not parity_failures,
        parity_failures[:4],
    )
    check(
        "the exact branch weights are deterministic, halves, or quarters",
        weight_set <= {Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(1)}
        and dict(support_histogram) == {1: 2, 2: 6, 4: 4},
        dict(support_histogram),
    )

    print("\nREPEATED CERTIFIED-BLOCK EXTENSIONS")
    generators = {
        "product": product_law,
        "sticky_markov": sticky_markov_law,
        "frozen": frozen_law,
        "balanced": balanced_law,
    }
    consistency_failures = []
    marginal_failures = []
    horizon = 5
    for protocol, distribution in protocols.items():
        wanted = complete_distribution(distribution)
        for name, generator in generators.items():
            law = generator(distribution, horizon)
            if law_total(law) != 1 or marginal(law, 0) != wanted:
                marginal_failures.append((protocol, name, law_total(law), marginal(law, 0), wanted))
            if not projectively_stationary(generator, distribution, horizon):
                consistency_failures.append((protocol, name))
        mixed = mixture_law(
            product_law(distribution, horizon),
            balanced_law(distribution, horizon),
        )
        if law_total(mixed) != 1 or marginal(mixed, 0) != wanted:
            marginal_failures.append((protocol, "equal-mean-mixture", law_total(mixed), marginal(mixed, 0), wanted))
    check(
        "product, sticky-Markov, frozen, and balanced laws are projectively stationary",
        not consistency_failures,
        consistency_failures[:5],
    )
    check(
        "all five repeated-process routes retain the exact Cycle-189 one-block marginal",
        not marginal_failures,
        marginal_failures[:3],
    )

    nontrivial = {
        protocol: distribution
        for protocol, distribution in protocols.items()
        if len(positive_support(distribution)) > 1
    }
    markov_differs = []
    for protocol, distribution in nontrivial.items():
        if sticky_markov_law(distribution, 2) == product_law(distribution, 2):
            markov_differs.append(protocol)
    check(
        "the sticky Markov extension is correlated but keeps every one-block weight",
        len(nontrivial) == 10 and not markov_differs,
        {"nontrivial_protocols": len(nontrivial), "failures": markov_differs},
    )

    print("\nCOMPONENT-MEAN DISCRIMINATOR")
    balanced_failures = [
        protocol
        for protocol, distribution in protocols.items()
        if not balanced_orbits_match(distribution)
    ]
    frozen_failures = [
        protocol
        for protocol, distribution in nontrivial.items()
        if not frozen_has_wrong_components(distribution)
    ]
    check(
        "every deterministic balanced orbit has the exact Cycle-189 frequency vector",
        not balanced_failures,
        balanced_failures,
    )
    check(
        "every nontrivial frozen extension has the same one-shot law but wrong component frequencies",
        not frozen_failures,
        frozen_failures,
    )
    check(
        "nonergodic equal-mean mixtures remain frequency-correct component by component",
        all(balanced_orbits_match(distribution) for distribution in protocols.values()),
        "",
    )

    print("\nRECORD-VISIBLE CORPUS")
    certificate_failures = []
    skeletons = set()
    for (preparation, context), distribution in protocols.items():
        period = balanced_period(distribution)
        word = tuple(period[index % len(period)] for index in range(8))
        records = certified_records(preparation, context, word)
        try:
            decoded = decode_certified_records(preparation, context, records)
        except ValueError as error:
            certificate_failures.append((preparation, context, str(error)))
            continue
        if decoded != word:
            certificate_failures.append((preparation, context, decoded, word))
        skeletons.add(tuple(kind for _index, kind, _content in records))
    check(
        "preparation, context, pointer, and close records define and decode every trial corpus",
        not certificate_failures and len(skeletons) == 1,
        certificate_failures[:3],
    )
    check(
        "identical certificate skeletons do not determine inter-trial memory",
        all(
            marginal(product_law(distribution, 3), 0)
            == marginal(frozen_law(distribution, 3), 0)
            for distribution in protocols.values()
        )
        and any(
            product_law(distribution, 3) != frozen_law(distribution, 3)
            for distribution in nontrivial.values()
        ),
        "",
    )

    print("\nACTUAL-HISTORY AND IMPORT FIREWALL")
    fair_distribution = next(
        distribution
        for distribution in protocols.values()
        if len(positive_support(distribution)) == 2
    )
    fair_frozen = frozen_law(fair_distribution, 4)
    fair_members = tuple(fair_frozen)
    check(
        "one normalized repeated-history law still has multiple possible actual members",
        len(fair_members) == 2
        and law_total(fair_frozen) == 1
        and all(fair_frozen[word] == Fraction(1, 2) for word in fair_members),
        fair_members,
    )

    note_text = NOTE.read_text(encoding="utf-8") if NOTE.is_file() else ""
    normalized = " ".join(note_text.lower().split())
    required = (
        "born trace pairing remains imported",
        "component-mean condition",
        "visible certificates define blocks, not independence",
        "deterministic balanced route",
        "actual-history membership remains separate",
        "fixed-protocol scope",
        "no axiom conclusion follows",
        "## n1",
        "## n2",
        "## n3",
        "## n4",
        "## n5",
        "## n6",
        "## n7",
        "## n8",
    )
    missing = tuple(phrase for phrase in required if phrase not in normalized)
    check(
        "the note preserves the import, scope, and N1-N8 firewall",
        not missing,
        missing,
    )

    print("\nACCOUNTING")
    print("PROTOCOLS", len(protocols))
    print("SUPPORT_HISTOGRAM", dict(sorted(support_histogram.items())))
    print("WEIGHTS", tuple(sorted(weight_set)))
    print("NONTRIVIAL_PROTOCOLS", len(nontrivial))
    print("HORIZON", horizon)
    print("PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "CYCLE194_RECORD_CORPUS_FREQUENCY_BRIDGE_GREEN"
        if FAIL == 0
        else "CYCLE194_OPEN",
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
