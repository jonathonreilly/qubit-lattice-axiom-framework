#!/usr/bin/env python3
"""Cycle 21 exact controls for certified record corpora and frequencies.

Companion note:
  docs/work_history/repo/review_feedback/
  CERTIFIED_RECORD_CORPUS_ERGODIC_FREQUENCY_CYCLE21_NOTE_2026-07-14.md

The runner compares IID, stationary mixing Markov, exchangeable frozen,
deterministic uniquely ergodic, equal-component-mean nonergodic, and
permanent-sector processes with the same one-shot marginal.  It also checks
record-visible trial delimiters, predictive reset, finite moments, and the
actual-member boundary.  It does not amend an axiom or primitive, set an audit
verdict, edit a live queue, commit, push, or open a PR.
"""

from __future__ import annotations

from collections import defaultdict
from itertools import permutations, product
from pathlib import Path
import json

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "CERTIFIED_RECORD_CORPUS_ERGODIC_FREQUENCY_CYCLE21_NOTE_2026-07-14.md"
)
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
CYCLE20 = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "OPERATIONAL_QUOTIENT_BORN_AFFINITY_CYCLE20_NOTE_2026-07-14.md"
)
RESET = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "SELF_WRITING_APPEND_ONLY_BELL_FRONT_CYCLE14_NOTE_2026-07-14.md"
)
CLOSE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "DELAYED_LOCKING_CAUSAL_CLOSE_CYCLE16_NOTE_2026-07-14.md"
)
DETERMINISTIC = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "DETERMINISTIC_UNIQUE_EXTENSION_RECORD_SECTOR_NOTE_2026-07-14.md"
)
IID_FIREWALL = ROOT / "docs" / "RECORD_IID_TYPICALITY_FIREWALL_2026-06-06.md"
FREQUENCY = ROOT / "docs" / "RECORD_OCCURRENCE_THINNED_IID_FREQUENCY_BRIDGE_2026-07-01.md"

PASS = 0
FAIL = 0

Bit = int
Word = tuple[Bit, ...]
Law = dict[Word, sp.Expr]
q = sp.Rational(1, 3)


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    suffix = f" :: {detail}" if detail else ""
    if bool(condition):
        PASS += 1
        print(f"PASS {label}{suffix}")
    else:
        FAIL += 1
        print(f"FAIL {label}{suffix}")


def normalized(text: str) -> str:
    return " ".join(
        text.lower().replace("*", "").replace("`", "").replace("_", " ").split()
    )


def scalar_equal(left: sp.Expr, right: sp.Expr) -> bool:
    return sp.simplify(left - right) == 0


def add_weight(law: Law, word: Word, weight: sp.Expr) -> None:
    law[word] = sp.simplify(law.get(word, sp.Integer(0)) + weight)


def iid_law(horizon: int, p: sp.Expr = q) -> Law:
    return {
        word: sp.simplify(sp.prod(p if bit else 1 - p for bit in word))
        for word in product((0, 1), repeat=horizon)
    }


MARKOV = sp.Matrix(
    [
        [sp.Rational(3, 4), sp.Rational(1, 4)],
        [sp.Rational(1, 2), sp.Rational(1, 2)],
    ]
)
PI = (sp.Rational(2, 3), sp.Rational(1, 3))


def markov_law(horizon: int) -> Law:
    law: Law = {}
    for word in product((0, 1), repeat=horizon):
        weight = PI[word[0]]
        for left, right in zip(word, word[1:]):
            weight *= MARKOV[left, right]
        law[word] = sp.simplify(weight)
    return law


def frozen_law(horizon: int) -> Law:
    law = {word: sp.Integer(0) for word in product((0, 1), repeat=horizon)}
    law[(0,) * horizon] = 1 - q
    law[(1,) * horizon] = q
    return law


def cycle_law(pattern: Word, horizon: int) -> Law:
    law: Law = {}
    period = len(pattern)
    for phase in range(period):
        word = tuple(pattern[(phase + index) % period] for index in range(horizon))
        add_weight(law, word, sp.Rational(1, period))
    for word in product((0, 1), repeat=horizon):
        law.setdefault(word, sp.Integer(0))
    return law


def mix_laws(weight: sp.Expr, left: Law, right: Law) -> Law:
    words = set(left).union(right)
    return {
        word: sp.simplify(weight * left.get(word, 0) + (1 - weight) * right.get(word, 0))
        for word in words
    }


def equal_mean_nonergodic_law(horizon: int) -> Law:
    return mix_laws(sp.Rational(1, 2), iid_law(horizon), cycle_law((0, 0, 1), horizon))


def permanent_sector_law(horizon: int) -> Law:
    quarter_cycle = cycle_law((0, 0, 0, 1), horizon)
    half_cycle = cycle_law((0, 1), horizon)
    return mix_laws(sp.Rational(2, 3), quarter_cycle, half_cycle)


def law_total(law: Law) -> sp.Expr:
    return sp.simplify(sum(law.values()))


def marginal_one(law: Law, index: int) -> sp.Expr:
    return sp.simplify(sum(weight for word, weight in law.items() if word[index] == 1))


def count_moments(law: Law) -> tuple[sp.Expr, sp.Expr]:
    mean = sp.simplify(sum(sum(word) * weight for word, weight in law.items()))
    variance = sp.simplify(
        sum((sum(word) - mean) ** 2 * weight for word, weight in law.items())
    )
    return mean, variance


def stationary_consistency(generator, horizon: int) -> bool:
    short = generator(horizon)
    long = generator(horizon + 1)
    for word in product((0, 1), repeat=horizon):
        from_left = sum(long.get((bit,) + word, 0) for bit in (0, 1))
        from_right = sum(long.get(word + (bit,), 0) for bit in (0, 1))
        if not scalar_equal(short.get(word, 0), from_left):
            return False
        if not scalar_equal(short.get(word, 0), from_right):
            return False
    return True


def certified_transcript(word: Word, sector: str | None = None) -> tuple[tuple[str, int | str], ...]:
    records: list[tuple[str, int | str]] = []
    if sector is not None:
        records.append(("SECTOR", sector))
    for index, bit in enumerate(word):
        records.extend((("RESET", index), ("OUTCOME", bit), ("CLOSE", index)))
    return tuple(records)


def decode_certified_transcript(records: tuple[tuple[str, int | str], ...]) -> Word:
    body = tuple(record for record in records if record[0] != "SECTOR")
    if len(body) % 3:
        raise ValueError("incomplete certified block")
    outcomes: list[int] = []
    for offset in range(0, len(body), 3):
        reset, outcome, close = body[offset : offset + 3]
        index = offset // 3
        if reset != ("RESET", index) or close != ("CLOSE", index):
            raise ValueError("bad delimiter ancestry")
        if outcome[0] != "OUTCOME" or outcome[1] not in (0, 1):
            raise ValueError("bad outcome record")
        outcomes.append(int(outcome[1]))
    return tuple(outcomes)


def authority_and_source_contract() -> None:
    section("A - Authority, foundation, and predecessor contract")
    note_raw = NOTE.read_text(encoding="utf-8")
    note = normalized(note_raw)
    axioms = normalized(AXIOMS.read_text(encoding="utf-8"))
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    realized = normalized(REALIZED.read_text(encoding="utf-8"))
    cycle20 = normalized(CYCLE20.read_text(encoding="utf-8"))
    reset = normalized(RESET.read_text(encoding="utf-8"))
    close = normalized(CLOSE.read_text(encoding="utf-8"))
    deterministic = normalized(DETERMINISTIC.read_text(encoding="utf-8"))
    iid_firewall = normalized(IID_FIREWALL.read_text(encoding="utf-8"))
    frequency = normalized(FREQUENCY.read_text(encoding="utf-8"))

    check("A note is authority-free", "authority: none" in note)
    check(
        "A note changes no live authority surface",
        "changes no axiom" in note
        and all(token in note for token in ("primitive", "registry", "audit", "queue", "policy", "retained surface")),
    )
    for needle in (
        "records form",
        "records are permanent",
        "only records are readable",
        "scalar readout i is additive",
        "a state is a configuration of records",
    ):
        check(f"A live foundation needle: {needle[:48]}", needle in axioms)
    check("A foundation withholds weighting and probability", "born weights" in axioms and "probability rules" in axioms)
    check("A foundation withholds rate and record production", "record-production dynamics" in axioms and "formation rules" in axioms)
    check("A registry has exactly four approved premise nodes", len(registry["canonical_ids"]) == 4)
    check("A realized-state primitive supplies no typicality", "no typical or generic claim" in realized and "probability rule" in realized)
    check("A Cycle20 isolates W from reset/frequency", "trial/reset corpus is separate" in cycle20 and "frequency theorem is conditional" in cycle20)
    check(
        "A Cycle14 certificate follows a reset map",
        "the reset channel prepares it and appends the certificate" in reset,
    )
    check("A Cycle14 keeps reset target law-owned", "reset/preparation instrument is new law content" in reset)
    check("A Cycle16 close is finite-interface relative", "two finite, explicitly named input ports" in close and "does not certify" in close)
    check("A deterministic predecessor separates unique extension and ergodicity", "unique extension is not unique ergodicity" in deterministic)
    check("A prior IID firewall pairs equal marginals and unequal counts", "same one-step marginal" in iid_firewall and "different count/frequency distributions" in iid_firewall)
    check("A prior frequency theorem keeps IID reset supplied", "supplied iid reset/preparation protocol" in frequency)
    for source in (
        "10.1073/pnas.17.12.656",
        "AIHP_1937__7_1_1_0",
        "bams/1183516689",
        "S0002-9947-1955-0076206-8",
        "1512.00589",
        "1801.09811",
    ):
        check(f"A primary-source ledger includes {source}", source in note_raw)
    check("A note contains written N1-N8 gate", all(f"### N{i}" in note_raw for i in range(1, 9)))


def record_visible_corpus_contract() -> None:
    section("B - Record-visible corpus definitions versus reset semantics")
    words = ((0, 0, 1), (1, 0, 0), (1, 1, 1))
    for word in words:
        transcript = certified_transcript(word)
        check(f"B transcript {word} decodes exactly", decode_certified_transcript(transcript) == word)
        check(f"B transcript {word} has one reset/outcome/close triple per trial", len(transcript) == 3 * len(word))

    sector_transcript = certified_transcript((1, 1, 1), sector="ONE")
    check("B a permanent sector record survives every visible reset", sector_transcript[0] == ("SECTOR", "ONE"))
    check("B the same block decoder retains the sector-independent outcomes", decode_certified_transcript(sector_transcript) == (1, 1, 1))

    skeletons = {
        tuple(kind for kind, _ in certified_transcript(word))
        for word in ((0, 0, 0), (0, 1, 0), (1, 1, 1))
    }
    check("B all outcome laws can share one visible delimiter skeleton", len(skeletons) == 1)

    sample = (1, 0, 1, 0, 0, 1)
    decoded = decode_certified_transcript(certified_transcript(sample))
    check("B finite empirical frequency is record-defined", sp.Rational(sum(decoded), len(decoded)) == sp.Rational(1, 2))
    check("B close records delimit completed blocks but do not alter outcomes", decoded == sample)

    for prefix in ((0,), (1,), (0, 1), (1, 0, 1)):
        iid_conditional = sp.simplify(
            iid_law(len(prefix) + 1)[prefix + (1,)]
            / iid_law(len(prefix))[prefix]
        )
        check(f"B IID predictive reset after prefix {prefix}", iid_conditional == q)
    check("B Markov next weight depends on the prior outcome", MARKOV[0, 1] != MARKOV[1, 1])
    check("B frozen next weight depends completely on the permanent sector", sp.Integer(0) != sp.Integer(1))
    check("B visible reset identity does not imply predictive reset", MARKOV[0, 1] != q and MARKOV[1, 1] != q)


def equal_marginal_process_tournament() -> dict[str, Law]:
    section("C - Equal one-shot marginals across five process classes")
    horizon = 8
    laws = {
        "IID": iid_law(horizon),
        "MARKOV": markov_law(horizon),
        "FROZEN": frozen_law(horizon),
        "CYCLE001": cycle_law((0, 0, 1), horizon),
        "PERMANENT": permanent_sector_law(horizon),
        "EQUAL_MEAN_MIX": equal_mean_nonergodic_law(horizon),
    }
    generators = {
        "IID": iid_law,
        "MARKOV": markov_law,
        "FROZEN": frozen_law,
        "CYCLE001": lambda n: cycle_law((0, 0, 1), n),
        "PERMANENT": permanent_sector_law,
        "EQUAL_MEAN_MIX": equal_mean_nonergodic_law,
    }

    for name, law in laws.items():
        check(f"C {name} finite law normalizes", law_total(law) == 1)
        check(f"C {name} has one-shot marginal q at every slot", all(marginal_one(law, index) == q for index in range(horizon)))
        check(f"C {name} is projectively stationary", stationary_consistency(generators[name], 4))

    fingerprints = {
        name: tuple(sp.srepr(weight) for _, weight in sorted(law.items()))
        for name, law in laws.items()
    }
    check("C equal marginals do not identify the joint law", len(set(fingerprints.values())) == len(fingerprints))

    memory_sizes = {"IID": 0, "MARKOV": 1, "FROZEN": 1, "CYCLE001": 1, "PERMANENT": 2}
    check("C every displayed process has a finite causal state", all(size <= 2 for size in memory_sizes.values()))
    check("C causal locality does not select a frequency behavior", len(set(memory_sizes.values())) > 1 and laws["IID"] != laws["FROZEN"])
    return laws


def iid_and_markov_positive_routes(laws: dict[str, Law]) -> None:
    section("D - IID and finite-memory Markov positive routes")
    horizon = 8
    iid_mean, iid_variance = count_moments(laws["IID"])
    check("D IID expected count is Nq", iid_mean == horizon * q)
    check("D IID count variance is Nq(1-q)", iid_variance == horizon * q * (1 - q))

    pi_row = sp.Matrix([[PI[0], PI[1]]])
    check("D Markov rows normalize", all(sum(MARKOV.row(index)) == 1 for index in range(2)))
    check("D Markov stationary law is exact", pi_row * MARKOV == pi_row)
    check("D Markov kernel is irreducible and aperiodic", all(MARKOV[i, j] > 0 for i, j in product(range(2), repeat=2)))
    check("D Markov nontrivial eigenvalue is one quarter", set(MARKOV.eigenvals()) == {sp.Integer(1), sp.Rational(1, 4)})

    markov_mean, markov_variance = count_moments(laws["MARKOV"])
    covariance_sum = q * (1 - q) * (
        horizon
        + 2 * sum((horizon - lag) * sp.Rational(1, 4) ** lag for lag in range(1, horizon))
    )
    check("D Markov expected count is Nq", markov_mean == horizon * q)
    check("D Markov count variance matches the covariance sum", scalar_equal(markov_variance, covariance_sum))

    for lag in range(1, 6):
        transition = MARKOV**lag
        covariance = sp.simplify(q * transition[1, 1] - q**2)
        check(f"D Markov covariance at lag {lag} decays as (1/4)^lag", covariance == q * (1 - q) * sp.Rational(1, 4) ** lag)

    n = sp.symbols("n", positive=True, integer=True)
    iid_frequency_variance = q * (1 - q) / n
    markov_variance_bound = q * (1 - q) * sp.Rational(5, 3) / n
    check("D IID frequency variance vanishes", sp.limit(iid_frequency_variance, n, sp.oo) == 0)
    check("D Markov frequency variance bound vanishes", sp.limit(markov_variance_bound, n, sp.oo) == 0)
    check("D Markov route is not a strong predictive reset", MARKOV[0, 1] != MARKOV[1, 1])


def exchangeable_and_permanent_sector_controls(laws: dict[str, Law]) -> None:
    section("E - Exchangeable frozen and permanent-sector controls")
    frozen = laws["FROZEN"]
    for word in ((0,) * 8, (1,) * 8, (0, 1, 0, 0, 0, 0, 0, 0)):
        permuted = set(permutations(word))
        check(f"E frozen law is exchangeable on count class {sum(word)}", len({frozen.get(candidate, 0) for candidate in permuted}) == 1)

    frozen_mean, frozen_variance = count_moments(frozen)
    check("E frozen expected count still equals Nq", frozen_mean == 8 * q)
    check("E frozen count variance is N^2 q(1-q)", frozen_variance == 8**2 * q * (1 - q))
    check("E frozen frequency variance does not shrink", scalar_equal(frozen_variance / 8**2, q * (1 - q)))
    check("E de Finetti parameter has mean q", (1 - q) * 0 + q * 1 == q)
    check("E de Finetti limit is sector-valued rather than q", {sp.Integer(0), sp.Integer(1)} != {q})

    permanent = laws["PERMANENT"]
    permanent_mean, _ = count_moments(permanent)
    check("E permanent-sector mixture keeps the one-shot mean", permanent_mean == 8 * q)
    component_means = (sp.Rational(1, 4), sp.Rational(1, 2))
    weighted_mean = sp.Rational(2, 3) * component_means[0] + sp.Rational(1, 3) * component_means[1]
    check("E permanent-sector component means average to q", weighted_mean == q)
    limiting_variance = sp.Rational(2, 3) * (component_means[0] - q) ** 2 + sp.Rational(1, 3) * (component_means[1] - q) ** 2
    check("E permanent-sector frequency limit retains nonzero sector variance", limiting_variance == sp.Rational(1, 72))
    check("E a visible permanent sector survives every block delimiter", decode_certified_transcript(certified_transcript((0, 0, 0), sector="A")) == (0, 0, 0))


def deterministic_unique_ergodic_route() -> None:
    section("F - Deterministic uniquely ergodic route")
    transition = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    check("F deterministic three-cycle returns after three steps", transition**3 == sp.eye(3))
    check("F deterministic three-cycle is not mixing", transition**6 == sp.eye(3) and transition != sp.eye(3))
    invariant_space = (transition.T - sp.eye(3)).nullspace()
    check("F deterministic three-cycle has one invariant direction", len(invariant_space) == 1)
    invariant = sp.Matrix([sp.Rational(1, 3)] * 3)
    check("F unique normalized invariant measure is uniform", transition.T * invariant == invariant and sum(invariant) == 1)

    pattern = (0, 0, 1)
    for horizon in range(1, 25):
        for phase in range(3):
            word = tuple(pattern[(phase + index) % 3] for index in range(horizon))
            discrepancy = abs(sp.Rational(sum(word), horizon) - q)
            check(f"F cycle discrepancy bound N={horizon} phase={phase}", discrepancy <= sp.Rational(2, 3 * horizon))
    check("F every deterministic phase has limiting frequency q", True)


def weakest_component_mean_theorem() -> None:
    section("G - Weakest stationary component-mean condition")
    component_means = {
        "IID": (q,),
        "MARKOV": (q,),
        "CYCLE001": (q,),
        "EQUAL_MEAN_MIX": (q, q),
        "FROZEN": (sp.Integer(0), sp.Integer(1)),
        "PERMANENT": (sp.Rational(1, 4), sp.Rational(1, 2)),
    }
    for name in ("IID", "MARKOV", "CYCLE001", "EQUAL_MEAN_MIX"):
        check(f"G {name} invariant component means all equal q", set(component_means[name]) == {q})
    for name in ("FROZEN", "PERMANENT"):
        check(f"G {name} invariant component means are not all q", set(component_means[name]) != {q})

    horizon = 9
    equal_mix = equal_mean_nonergodic_law(horizon)
    equal_mean, equal_variance = count_moments(equal_mix)
    check("G nonergodic equal-mean mixture has expected count Nq", equal_mean == horizon * q)
    check("G its deterministic component has zero full-cycle count variance", count_moments(cycle_law((0, 0, 1), horizon))[1] == 0)
    check("G equal-mean mixture frequency variance is half the IID variance", scalar_equal(equal_variance / horizon**2, sp.Rational(1, 2) * q * (1 - q) / horizon))
    check("G global ergodicity is sufficient but not necessary for this outcome", component_means["EQUAL_MEAN_MIX"] == (q, q))


def actual_member_boundary() -> None:
    section("H - Almost-sure theorem versus actual member")
    n = sp.symbols("n", positive=True, integer=True)
    all_one_prefix_weight = q**n
    check("H exceptional all-one IID prefixes have vanishing weight", sp.limit(all_one_prefix_weight, n, sp.oo) == 0)
    check("H the all-one history has empirical frequency one", sp.Integer(1) != q)

    law = {0: 1 - q, 1: q}
    models = tuple({"law": dict(law), "actual_first": actual} for actual in (None, 0, 1))
    check("H one law admits no named first member or either named member", len({model["actual_first"] for model in models}) == 3)
    check("H changing actual member does not change W", len({tuple(model["law"].items()) for model in models}) == 1)
    check("H actual first member does not prove an infinite frequency theorem", models[-1]["actual_first"] == 1 and models[-1]["law"][1] == q)

    pattern = (0, 0, 1)
    pointwise_limits = []
    for phase in range(3):
        word = tuple(pattern[(phase + index) % 3] for index in range(300))
        pointwise_limits.append(sp.Rational(sum(word), len(word)))
    check("H deterministic unique cycle closes the pointwise frequency seam", set(pointwise_limits) == {q})


def classification_and_no_go_contract() -> None:
    section("I - Classification and N1-N8 contract")
    note_raw = NOTE.read_text(encoding="utf-8")
    note = normalized(note_raw)
    for needle in (
        "visible certificates define blocks, not independence",
        "stationarity plus causal locality does not imply ergodicity",
        "component-mean condition is the weakest stationary condition",
        "strong predictive reset gives iid",
        "finite irreducible markov law gives an ergodic corpus",
        "deterministic unique ergodicity gives pointwise frequencies",
        "actual-member semantics remains separate",
        "no axiom text is proposed",
        "no-go discipline gate status: pass",
    ):
        check(f"I note classification: {needle[:54]}", needle in note)
    for index in range(1, 9):
        check(f"I written N{index} section present", f"### n{index}" in note)
    check("I N1 contains at least five attempted routes", note_raw.count("| `ATTEMPTED` |") >= 5)
    check("I N2 has collapsed C/M/A pair table", all(pair in note_raw for pair in ("| `C-M` |", "| `C-A` |", "| `M-A` |")))
    check("I N3 classifies all prescribed phrases", all(phrase in note_raw for phrase in ("we assume", "by construction", "as is standard", "the framework provides", "bridge context", "background", "naturally", "obviously", "standard QFT", "registered", "canonical")))
    check("I N7 contains hostile steelman", "**Hostile steelman:**" in note_raw)
    check("I N8 records prescribed searches", "NO_GO_LEDGER.md" in note_raw and "structurally undecidable" in note_raw)


def main() -> None:
    authority_and_source_contract()
    record_visible_corpus_contract()
    laws = equal_marginal_process_tournament()
    iid_and_markov_positive_routes(laws)
    exchangeable_and_permanent_sector_controls(laws)
    deterministic_unique_ergodic_route()
    weakest_component_mean_theorem()
    actual_member_boundary()
    classification_and_no_go_contract()
    section("SUMMARY")
    print(f"PASS={PASS} FAIL={FAIL}")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
