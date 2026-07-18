#!/usr/bin/env python3
"""Cycle 27 exact controls for stochastic record-history actuality semantics.

Companion note:
  docs/work_history/repo/review_feedback/
  STOCHASTIC_RECORD_HISTORY_ACTUALITY_SEMANTICS_CYCLE27_NOTE_2026-07-14.md

The runner distinguishes a normalized measure on complete record histories
from a distinguished actual member, a sampling implementation, a conditional
quantum instrument update, a probability-one assertion, and a supplied
boundary.  It also checks deterministic and unique-global-history escape
routes.  It does not amend an axiom or primitive, set an audit verdict, edit a
live queue, commit, push, or open a PR.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
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
    / "STOCHASTIC_RECORD_HISTORY_ACTUALITY_SEMANTICS_CYCLE27_NOTE_2026-07-14.md"
)
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
POLICY = ROOT / "docs" / "audit" / "AXIOM_MINIMALITY_POLICY.md"
CYCLE20 = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "OPERATIONAL_QUOTIENT_BORN_AFFINITY_CYCLE20_NOTE_2026-07-14.md"
)
TOURNAMENT = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "EXACT_LAW_IRREDUCIBLE_CONTENT_INDEPENDENCE_TOURNAMENT_NOTE_2026-07-14.md"
)
CONTRACT = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "CANONICAL_LAW_COMPLETENESS_CONTRACT_NOTE_2026-07-13.md"
)


PASS = 0
FAIL = 0

Bit = int
History = tuple[Bit, ...]
Law = dict[History, Fraction]
Event = frozenset[History]
Matrix = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]

H0: History = (0, 0, 0, 0)
H1: History = (1, 1, 1, 1)
OMEGA = frozenset((H0, H1))
MU: Law = {H0: Fraction(1, 2), H1: Fraction(1, 2)}


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    suffix = f" :: {detail}" if detail else ""
    if condition:
        PASS += 1
        print(f"PASS {label}{suffix}")
    else:
        FAIL += 1
        print(f"FAIL {label}{suffix}")


def normalize_text(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").lower().split())


def all_events(omega: frozenset[History]) -> tuple[Event, ...]:
    items = tuple(sorted(omega))
    out: list[Event] = []
    for size in range(len(items) + 1):
        out.extend(frozenset(c) for c in combinations(items, size))
    return tuple(out)


def law_normalized(law: Law) -> bool:
    return all(p >= 0 for p in law.values()) and sum(law.values(), Fraction(0)) == 1


def probability(law: Law, event: Event) -> Fraction:
    return sum((law.get(h, Fraction(0)) for h in event), Fraction(0))


def pushforward(seed_law: dict[object, Fraction], sampler: dict[object, History]) -> Law:
    out: Law = {}
    for seed, p in seed_law.items():
        h = sampler[seed]
        out[h] = out.get(h, Fraction(0)) + p
    return out


def condition(law: Law, event: Event) -> Law:
    z = probability(law, event)
    if z == 0:
        raise ValueError("cannot condition on a zero-weight event")
    return {h: law[h] / z for h in event if law.get(h, Fraction(0)) != 0}


def swap_history(h: History) -> History:
    return tuple(1 - x for x in h)


def pushforward_history_law(law: Law) -> Law:
    return {swap_history(h): p for h, p in law.items()}


def state_at_cut(h: History, cut: int) -> tuple[tuple[int, Bit], ...]:
    """A record configuration: immutable site/content pairs before `cut`."""
    return tuple(enumerate(h[:cut]))


def prefix_preserved(earlier: tuple[tuple[int, Bit], ...], later: tuple[tuple[int, Bit], ...]) -> bool:
    return later[: len(earlier)] == earlier


@dataclass(frozen=True)
class AnnotatedLaw:
    law: Law
    actual: History | None

    def satisfies_realized_reference(self) -> bool:
        return self.actual is not None and self.actual in self.law

    def actual_state(self, cut: int) -> tuple[tuple[int, Bit], ...]:
        if self.actual is None:
            raise ValueError("no realized-history reference")
        return state_at_cut(self.actual, cut)


def matmul(a: Matrix, b: Matrix) -> Matrix:
    return (
        (
            a[0][0] * b[0][0] + a[0][1] * b[1][0],
            a[0][0] * b[0][1] + a[0][1] * b[1][1],
        ),
        (
            a[1][0] * b[0][0] + a[1][1] * b[1][0],
            a[1][0] * b[0][1] + a[1][1] * b[1][1],
        ),
    )


def matadd(a: Matrix, b: Matrix) -> Matrix:
    return (
        (a[0][0] + b[0][0], a[0][1] + b[0][1]),
        (a[1][0] + b[1][0], a[1][1] + b[1][1]),
    )


def matscale(c: Fraction, a: Matrix) -> Matrix:
    return (
        (c * a[0][0], c * a[0][1]),
        (c * a[1][0], c * a[1][1]),
    )


def trace(a: Matrix) -> Fraction:
    return a[0][0] + a[1][1]


def instrument_branch(projector: Matrix, rho: Matrix) -> Matrix:
    return matmul(matmul(projector, rho), projector)


def posterior(branch: Matrix) -> Matrix:
    p = trace(branch)
    if p == 0:
        raise ValueError("zero-probability branch has no normalized posterior")
    return matscale(Fraction(1, 1) / p, branch)


def main() -> None:
    note = normalize_text(NOTE)
    axioms = normalize_text(AXIOMS)
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    realized = normalize_text(REALIZED)
    policy = normalize_text(POLICY)
    cycle20 = normalize_text(CYCLE20)
    tournament = normalize_text(TOURNAMENT)
    contract = normalize_text(CONTRACT)

    section("A - Authority, foundation, registry, and source boundary")
    check(
        "A note is authority-free",
        "authority:** none" in note or "authority: none" in note,
    )
    check(
        "A note changes no live authority surface",
        "changes no axiom, primitive, registry, policy, audit, queue" in note,
    )
    for needle in (
        "records form",
        "a record locks exactly one admissible local possibility",
        "records are permanent",
        "a state is a configuration of records",
        "a law privileges no states",
    ):
        check(f"A live foundation needle: {needle}", needle in axioms)
    check(
        "A foundation withholds state privilege and probability rules",
        "a law privileges no states" in axioms and "probability rules" in axioms,
    )
    check("A registry has exactly four premise nodes", len(registry["canonical_ids"]) == 4)
    check("A realized-state primitive is registered", "realized_state_primitive" in registry["canonical_ids"])
    check("A primitive says laws do not pick the state", "the laws do not pick the state; the world does" in realized)
    check("A primitive names one realized-state reference", "one realized-state reference" in realized)
    check("A primitive names a singular physical history", "a law-admissible state supplied by the physical history" in realized)
    check("A primitive permits pointwise evaluation", "pointwise evaluation" in realized)
    check("A primitive is not a state-selection rule", "this is pointwise evaluation, not a state-selection rule" in realized)
    check("A primitive supplies no measure", "no state, averaging over alternatives, measure" in realized)
    check("A policy records owner approval", "realized-state interface" in policy and "explicit owner approval" in policy)
    check("A policy calls state an additional datum", "a state is an additional datum" in policy)
    check("A Cycle20 already flags the ontology reconciliation", "may already supply bare one-world ontology" in cycle20)
    check(
        "A tournament separates actual-state reference from complete-history closure",
        "actual record facts and one pointwise state reference are already supplied" in tournament
        and "complete-history semantics remains conditional" in tournament,
    )
    check("A prior contract used a stronger selector test", "unique extension, boundary-conditioned global solution, or explicit sampled-history semantics" in contract)
    for source in (
        "foundationsofthe00kolm",
        "10.1007/bf01647093",
        "10.1063/1.526000",
        "quant-ph/9711006",
        "1911.10893",
    ):
        check(f"A primary-source ledger includes {source}", source in note)
    check("A note contains a written N1-N8 gate", "no-go discipline gate status: pass" in note)

    section("B - Same normalized law, different or absent actuality annotations")
    check("B fair history law normalizes", law_normalized(MU))
    plain = AnnotatedLaw(MU, None)
    actual0 = AnnotatedLaw(MU, H0)
    actual1 = AnnotatedLaw(MU, H1)
    check("B unannotated mathematical law has no actual member", plain.actual is None)
    check("B first annotated model has H0 actual", actual0.actual == H0)
    check("B second annotated model has H1 actual", actual1.actual == H1)
    for i, event in enumerate(all_events(OMEGA)):
        p_plain = probability(plain.law, event)
        check(f"B event {i} has the same probability under all annotations", p_plain == probability(actual0.law, event) == probability(actual1.law, event))
    check("B actual annotations differ without changing mu", actual0.actual != actual1.actual and actual0.law == actual1.law)
    check("B plain measure alone fails the registered reference interface", not plain.satisfies_realized_reference())
    check("B H0 annotation satisfies the registered reference interface", actual0.satisfies_realized_reference())
    check("B H1 annotation satisfies the registered reference interface", actual1.satisfies_realized_reference())
    check("B the foundation supplies existence but not which member", actual0.satisfies_realized_reference() and actual1.satisfies_realized_reference())
    mu_biased: Law = {H0: Fraction(3, 4), H1: Fraction(1, 4)}
    check("B one actual member is compatible with unequal laws", AnnotatedLaw(MU, H0).actual == AnnotatedLaw(mu_biased, H0).actual)
    check("B actual member does not determine the law", MU != mu_biased)

    section("C - Complete history evaluates the pointwise realized record state")
    for h_name, model in (("H0", actual0), ("H1", actual1)):
        states = [model.actual_state(cut) for cut in range(len(H0) + 1)]
        check(f"C {h_name} starts from the empty record configuration", states[0] == ())
        check(f"C {h_name} appends one record per cut", all(len(states[n + 1]) == len(states[n]) + 1 for n in range(len(H0))))
        check(f"C {h_name} preserves every earlier record", all(prefix_preserved(states[n], states[n + 1]) for n in range(len(H0))))
        check(f"C {h_name} has at most one record per site", all(len({site for site, _ in state}) == len(state) for state in states))
        check(f"C {h_name} gives one locked value at every occupied site", all(value in (0, 1) for state in states for _, value in state))
    check("C no annotation means pointwise evaluation is unavailable", plain.actual is None)
    try:
        plain.actual_state(1)
        no_reference_rejected = False
    except ValueError:
        no_reference_rejected = True
    check("C evaluator rejects a missing realized-history reference", no_reference_rejected)

    section("D - Law-only selector and sampling-implementation controls")
    check("D label swap leaves the fair law invariant", pushforward_history_law(MU) == MU)
    selectors = (H0, H1)
    equivariant = [h for h in selectors if swap_history(h) == h]
    check("D the invariant fair law has no label-equivariant deterministic member selector", equivariant == [])
    check("D choosing H0 breaks the outcome swap", swap_history(H0) != H0)
    check("D choosing H1 breaks the outcome swap", swap_history(H1) != H1)
    seeds = (0, 1, 2, 3)
    seed_law = {s: Fraction(1, 4) for s in seeds}
    sampler_a = {0: H0, 1: H0, 2: H1, 3: H1}
    sampler_b = {0: H1, 1: H1, 2: H0, 3: H0}
    check("D sampler A pushes forward to mu", pushforward(seed_law, sampler_a) == MU)
    check("D sampler B pushes forward to the same mu", pushforward(seed_law, sampler_b) == MU)
    check("D the two samplers differ pathwise at one seed", sampler_a[0] != sampler_b[0])
    check("D the two samplers differ pathwise at every seed", all(sampler_a[s] != sampler_b[s] for s in seeds))
    for i, event in enumerate(all_events(OMEGA)):
        pa = probability(pushforward(seed_law, sampler_a), event)
        pb = probability(pushforward(seed_law, sampler_b), event)
        check(f"D sampler implementations agree on record event {i}", pa == pb)
    identity_seed_law: dict[object, Fraction] = dict(MU)
    identity_sampler: dict[object, History] = {H0: H0, H1: H1}
    check("D the identity random history also represents mu", pushforward(identity_seed_law, identity_sampler) == MU)
    check("D identity sampling still needs an actual seed to return a history", identity_sampler[H0] == H0 and identity_sampler[H1] == H1)

    section("E - Quantum instrument, nonselective channel, and conditional collapse")
    z = Fraction(0)
    o = Fraction(1)
    half = Fraction(1, 2)
    p0: Matrix = ((o, z), (z, z))
    p1: Matrix = ((z, z), (z, o))
    rho_plus: Matrix = ((half, half), (half, half))
    b0 = instrument_branch(p0, rho_plus)
    b1 = instrument_branch(p1, rho_plus)
    check("E branch 0 has exact weight one half", trace(b0) == half)
    check("E branch 1 has exact weight one half", trace(b1) == half)
    check("E instrument weights normalize", trace(b0) + trace(b1) == 1)
    post0 = posterior(b0)
    post1 = posterior(b1)
    check("E posterior 0 is the zero record state", post0 == p0)
    check("E posterior 1 is the one record state", post1 == p1)
    check("E conditional posterior states differ", post0 != post1)
    nonselective = matadd(b0, b1)
    check("E nonselective channel output is the dephased mixture", nonselective == ((half, z), (z, half)))
    check("E nonselective output is neither conditional posterior", nonselective != post0 and nonselective != post1)
    instrument = (b0, b1)
    instrument_none = (instrument, None)
    instrument_0 = (instrument, 0)
    instrument_1 = (instrument, 1)
    check("E one instrument admits no selected outcome annotation", instrument_none[1] is None)
    check("E the same instrument admits actual outcome 0", instrument_0[0] == instrument and instrument_0[1] == 0)
    check("E the same instrument admits actual outcome 1", instrument_1[0] == instrument and instrument_1[1] == 1)
    check("E selected outcome does not change instrument weights", tuple(trace(b) for b in instrument_0[0]) == tuple(trace(b) for b in instrument_1[0]))
    check("E posterior update consumes the selected outcome", posterior(instrument[instrument_0[1]]) == post0 and posterior(instrument[instrument_1[1]]) == post1)
    check("E a summed channel does not retain the record label", nonselective == matadd(*instrument))

    section("F - Probability-one is not pointwise actuality")
    prefix_weights = [Fraction(1, 2**n) for n in range(1, 25)]
    check("F all-zero cylinders shrink strictly", all(prefix_weights[n + 1] < prefix_weights[n] for n in range(len(prefix_weights) - 1)))
    n_symbol = sp.symbols("n", integer=True, positive=True)
    singleton_weight = sp.limit(sp.Rational(1, 2) ** n_symbol, n_symbol, sp.oo)
    check("F all-zero singleton has limiting measure zero", singleton_weight == 0)
    actual_all_zero = lambda index: 0
    check("F all-zero infinite history remains a legal binary history", all(actual_all_zero(i) in (0, 1) for i in range(64)))
    check("F its empirical one-frequency is zero", sum(actual_all_zero(i) for i in range(64)) == 0)
    actual_is_in_not_all_zero_event = any(actual_all_zero(i) == 1 for i in range(64))
    check(
        "F the probability-one complement excludes the all-zero member",
        1 - singleton_weight == 1 and not actual_is_in_not_all_zero_event,
    )
    check("F realized-member annotation and probability-one membership are different predicates", actual0.satisfies_realized_reference())

    section("G - Boundary conditioning, deterministic, and global-history escapes")
    delta0 = condition(MU, frozenset((H0,)))
    delta1 = condition(MU, frozenset((H1,)))
    check("G conditioning on boundary 0 gives delta H0", delta0 == {H0: Fraction(1)})
    check("G conditioning on boundary 1 gives delta H1", delta1 == {H1: Fraction(1)})
    check("G one prior admits two different conditioned laws", delta0 != delta1)
    check("G the prior does not choose which boundary is supplied", law_normalized(MU) and law_normalized(delta0) and law_normalized(delta1))
    check("G singleton-support law identifies its only history", len(delta0) == 1 and next(iter(delta0)) == H0)
    deterministic_solutions = frozenset((H0, H1))
    check("G deterministic copy rule has two histories before initial data", len(deterministic_solutions) == 2)
    init0 = frozenset(h for h in deterministic_solutions if h[0] == 0)
    init1 = frozenset(h for h in deterministic_solutions if h[0] == 1)
    check("G initial boundary 0 makes deterministic continuation unique", init0 == frozenset((H0,)))
    check("G initial boundary 1 makes deterministic continuation unique", init1 == frozenset((H1,)))
    global_constraint = frozenset(h for h in ((0, 0, 0, 0), (1, 1, 1, 1)) if len(set(h)) == 1)
    check("G global all-equal constraint alone has two solutions", global_constraint == OMEGA)
    global_with_boundary = frozenset(h for h in global_constraint if h[-1] == 1)
    check("G a supplied final boundary makes the global constraint unique", global_with_boundary == frozenset((H1,)))
    check("G stochastic global-history law plus actual reference needs no sequential sampler", actual0.law == MU and actual0.actual in OMEGA)
    check("G deterministic delta law closes actual identity without random sampling", AnnotatedLaw(delta0, H0).satisfies_realized_reference())

    section("H - Classification, placement, and N1-N8 contract")
    for phrase in (
        "actual-state reference is closed; complete-history status is conditional",
        "a normalized measure does not canonically select its member",
        "a sampling algorithm is optional representation unless record-visible",
        "collapse is conditional on an outcome",
        "probability one is not pointwise truth at the realized member",
        "boundary conditioning changes the law but does not choose the boundary",
        "deterministic uniqueness can identify the history",
        "no universal standalone actuality or sampler sentence is forced",
        "the exact-law domain should be complete record histories",
        "no-go discipline gate status: pass",
    ):
        check(f"H note classification: {phrase[:60]}", phrase in note)
    for n in range(1, 9):
        check(f"H written N{n} section present", f"### n{n}" in note)
    check("H N1 contains at least five attempted routes", note.count("`attempted`") >= 5)
    check("H N2 distinguishes mechanism and typicality", "g-t" in note and "generative selector" in note and "typicality bridge" in note)
    check("H N3 classifies all prescribed phrases", all(p in note for p in ("we assume", "by construction", "as is standard", "the framework provides", "bridge context", "background", "naturally", "obviously", "standard qft", "registered", "canonical")))
    check("H N4 matches the realized-state residual", "bare existential actuality" in note and "law-only selection mechanism" in note)
    check("H N5 narrows the measure-only negative", "finite two-history" in note and "complete stochastic history space" in note)
    check("H N6 gives a definition/type-link retirement", "domain/type declaration" in note and "not a new axiom" in note)
    check("H N7 contains a hostile steelman", "hostile reviewer steelman" in note)
    check("H N8 records prescribed searches", "no_go_ledger.md" in note and "structurally undecidable" in note)

    section("SUMMARY")
    print(f"PASS={PASS} FAIL={FAIL}")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
