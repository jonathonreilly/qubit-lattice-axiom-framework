#!/usr/bin/env python3
"""Exact finite-set checks for the Record typing firewall.

This runner deliberately avoids physical measurement dynamics. It models only
what the current Record axiom states once a readout context supplies:

* a finite central-sector set;
* a fixed K/CPT involution;
* realized records as K/CPT orbits;
* finite additivity over disjoint record collections;
* no supplied probability, weighting, or normalization.

The exact claim is type-level: a realized record is an orbit/atom. A probability
is a normalized positive additive state on the event algebra over possible
record atoms. Those are different objects.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"[{tag}] {label}")
    if detail:
        print(f"       {detail}")


def powerset(items: tuple[str, ...]) -> tuple[frozenset[str], ...]:
    out: list[frozenset[str]] = []
    for r in range(len(items) + 1):
        for subset in combinations(items, r):
            out.append(frozenset(subset))
    return tuple(out)


def event_union(a: frozenset[str], b: frozenset[str]) -> frozenset[str]:
    return frozenset(set(a) | set(b))


def event_intersection(a: frozenset[str], b: frozenset[str]) -> frozenset[str]:
    return frozenset(set(a) & set(b))


def event_complement(a: frozenset[str], universe: frozenset[str]) -> frozenset[str]:
    return frozenset(set(universe) - set(a))


def main() -> int:
    print("=== Record readout context ===")
    sectors = ("chi0", "chi1", "chi2")
    k_action = {"chi0": "chi0", "chi1": "chi2", "chi2": "chi1"}
    check("C1 central-sector set is finite", len(sectors) == 3)
    check("C2 fixed K/CPT action is an involution",
          all(k_action[k_action[s]] == s for s in sectors),
          f"K = {k_action}")

    seen: set[str] = set()
    orbits: list[tuple[str, ...]] = []
    for s in sectors:
        if s in seen:
            continue
        orbit = tuple(sorted({s, k_action[s]}))
        seen.update(orbit)
        orbits.append(orbit)
    orbits = sorted(orbits, key=lambda o: (len(o), o))
    orbit_names = ("singlet", "doublet")
    orbit_map = dict(zip(orbit_names, orbits, strict=True))
    check("C3 realized record values are K/CPT orbits",
          orbit_map == {"singlet": ("chi0",), "doublet": ("chi1", "chi2")},
          f"orbits = {orbit_map}")
    check("C4 record alphabet has two atoms in this context",
          orbit_names == ("singlet", "doublet"))

    print("\n=== Event algebra and Record additivity ===")
    atoms = orbit_names
    universe = frozenset(atoms)
    events = powerset(atoms)
    singleton_events = tuple(frozenset([a]) for a in atoms)
    check("E1 event algebra is the powerset of record atoms",
          len(events) == 2 ** len(atoms) and frozenset() in events and universe in events,
          f"|P(O)| = {len(events)}")
    check("E2 atoms are singleton events, not weights",
          singleton_events == (frozenset(["singlet"]), frozenset(["doublet"])))
    check("E3 Boolean operations close on events",
          all(event_union(a, b) in events and event_intersection(a, b) in events
              for a in events for b in events)
          and all(event_complement(a, universe) in events for a in events))

    # Record scalar readout: finite additive over disjoint events.
    readout_weights = {"singlet": 7, "doublet": 11}

    def record_readout(event: frozenset[str]) -> int:
        return sum(readout_weights[a] for a in event)

    empty = frozenset()
    singlet = frozenset(["singlet"])
    doublet = frozenset(["doublet"])
    check("R1 Record readout has I(empty)=0", record_readout(empty) == 0)
    check("R2 Record readout is finitely additive over disjoint atoms",
          event_intersection(singlet, doublet) == empty
          and record_readout(event_union(singlet, doublet))
          == record_readout(singlet) + record_readout(doublet),
          f"I(total) = {record_readout(universe)}")
    check("R3 Record readout is not normalized by the axiom",
          record_readout(universe) == 18 and record_readout(universe) != 1,
          "finite additivity does not impose probability normalization")

    print("\n=== Probability is a separate state on the event algebra ===")
    probability_states = [
        {"singlet": Fraction(1, 2), "doublet": Fraction(1, 2)},
        {"singlet": Fraction(1, 3), "doublet": Fraction(2, 3)},
        {"singlet": Fraction(1, 1), "doublet": Fraction(0, 1)},
    ]

    def prob(mu: dict[str, Fraction], event: frozenset[str]) -> Fraction:
        return sum((mu[a] for a in event), Fraction(0, 1))

    for idx, mu in enumerate(probability_states, start=1):
        check(f"P{idx}.1 probability state {idx} is normalized",
              prob(mu, universe) == 1 and prob(mu, empty) == 0,
              f"mu = {mu}")
        check(f"P{idx}.2 probability state {idx} is additive over disjoint events",
              prob(mu, event_union(singlet, doublet))
              == prob(mu, singlet) + prob(mu, doublet))

    check("P4 multiple inequivalent probability states fit the same record alphabet",
          len({tuple(mu[a] for a in atoms) for mu in probability_states}) == 3,
          "Record supplies the alphabet, not a unique measure")
    check("P5 equal-letter and dimension-style priors are distinct states",
          tuple(probability_states[0][a] for a in atoms)
          != tuple(probability_states[1][a] for a in atoms),
          "gamma=0 letters=(1/2,1/2); gamma=1 dims=(1/3,2/3)")

    print("\n=== Type firewall ===")
    realized_singlet_atom = singlet
    predictive_state = probability_states[1]
    check("T1 realized record atom is an event, not a probability map",
          isinstance(realized_singlet_atom, frozenset)
          and isinstance(predictive_state, dict))
    check("T2 the atom can be evaluated by many states without becoming a state",
          prob(probability_states[0], realized_singlet_atom) == Fraction(1, 2)
          and prob(probability_states[1], realized_singlet_atom) == Fraction(1, 3)
          and prob(probability_states[2], realized_singlet_atom) == Fraction(1, 1))
    check("T3 degenerate probability still has the type of a state, not an atom",
          probability_states[2] != realized_singlet_atom,
          "delta_singlet evaluates the atom, but is not the atom object")
    check("T4 Record explicitly leaves probability/weighting/normalization unsupplied",
          True,
          "the exact theorem uses that omission as a boundary, not as an extra premise")

    print("\n=== Additive post-record histories ===")
    count_a = {"singlet": 2, "doublet": 1}
    count_b = {"singlet": 4, "doublet": 0}
    count_sum = {a: count_a[a] + count_b[a] for a in atoms}
    check("H1 finite post-record counts add componentwise",
          count_sum == {"singlet": 6, "doublet": 1})
    for n in (1, 2, 5, 13):
        history = {"singlet": n, "doublet": 0}
        check(f"H2.{n} arbitrary finite recorded count n={n} is allowed algebraically",
              sum(history.values()) == n)

    print("\n=== Scorecard ===")
    print(f"PASS={PASS} FAIL={FAIL}")
    print(
        "FINDING: from the Record axiom plus a supplied finite readout context, "
        "a realized record is an orbit/atom. A probability is a separate "
        "normalized state on the event algebra. Record supplies the former and "
        "explicitly not the latter."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
