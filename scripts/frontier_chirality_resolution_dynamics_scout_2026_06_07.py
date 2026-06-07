#!/usr/bin/env python3
"""Finite scout for chirality-resolution dynamics.

The exercise question is whether an enzyme-style "blend / flip / filter" idea
can help the chirality lane.  This runner keeps the analogy honest on finite
models: blends and symmetric flips do not select a hand; filters and dynamic
kinetic resolution select only because an asymmetric section/sink is supplied.

No audit verdict and no new axiom are encoded here.  The checks are guardrails
for the accompanying scout note.
"""

from __future__ import annotations

import itertools
import math
import sys
from dataclasses import dataclass


PASS: list[str] = []
FAIL: list[str] = []


def check(name: str, cond: bool, detail: str = "") -> bool:
    bucket = PASS if cond else FAIL
    bucket.append(name)
    suffix = f" -- {detail}" if detail else ""
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}{suffix}")
    return cond


def normalize(pair: tuple[float, float]) -> tuple[float, float]:
    plus, minus = pair
    total = plus + minus
    if total <= 0:
        raise ValueError("cannot normalize empty two-hand population")
    return plus / total, minus / total


def total_mass(pair: tuple[float, float]) -> float:
    return pair[0] + pair[1]


def ee(pair: tuple[float, float]) -> float:
    plus, minus = normalize(pair)
    return plus - minus


def symmetric_flip_raw(pair: tuple[float, float], rate: float, steps: int) -> tuple[float, float]:
    plus, minus = pair
    for _ in range(steps):
        plus, minus = (1.0 - rate) * plus + rate * minus, rate * plus + (1.0 - rate) * minus
    return plus, minus


def symmetric_flip(pair: tuple[float, float], rate: float, steps: int) -> tuple[float, float]:
    plus, minus = symmetric_flip_raw(pair, rate, steps)
    return normalize((plus, minus))


def filter_raw(pair: tuple[float, float], sink_plus: float, sink_minus: float) -> tuple[float, float]:
    plus, minus = pair
    return (1.0 - sink_plus) * plus, (1.0 - sink_minus) * minus


def filter_step(pair: tuple[float, float], sink_plus: float, sink_minus: float) -> tuple[float, float]:
    return normalize(filter_raw(pair, sink_plus, sink_minus))


def dynamic_resolution(
    pair: tuple[float, float],
    flip_rate: float,
    sink_plus: float,
    sink_minus: float,
    steps: int,
) -> tuple[tuple[float, float], float]:
    state = normalize(pair)
    for _ in range(steps):
        state = symmetric_flip_raw(state, flip_rate, 1)
        state = filter_raw(state, sink_plus, sink_minus)
    return normalize(state), total_mass(state)


def block1_blend_and_flip() -> None:
    print("\n[BLOCK 1] Blend and symmetric flip do not select chirality")
    blend = (0.5, 0.5)
    check("racemic blend has zero signed excess", abs(ee(blend)) < 1e-12, f"ee={ee(blend):.3g}")

    relaxed = symmetric_flip((0.9, 0.1), rate=0.2, steps=80)
    check(
        "symmetric flip relaxes toward the unbiased fixed point",
        abs(relaxed[0] - 0.5) < 1e-12 and abs(relaxed[1] - 0.5) < 1e-12,
        f"state=({relaxed[0]:.6f}, {relaxed[1]:.6f})",
    )

    no_filter, no_filter_mass = dynamic_resolution((0.5, 0.5), flip_rate=0.12, sink_plus=0.0, sink_minus=0.0, steps=30)
    check(
        "flip without a filter remains unbiased",
        abs(ee(no_filter)) < 1e-12 and abs(no_filter_mass - 1.0) < 1e-12,
        f"state=({no_filter[0]:.6f}, {no_filter[1]:.6f}), retained_mass={no_filter_mass:.6f}",
    )


def block2_filter_is_selector() -> None:
    print("\n[BLOCK 2] A filter can enrich one hand, but the filter is the selector")
    raw_filtered = filter_raw((0.5, 0.5), sink_plus=0.0, sink_minus=0.45)
    filtered = normalize(raw_filtered)
    check(
        "asymmetric filter enriches the unsunk hand and lowers retained mass",
        filtered[0] > 0.64 and ee(filtered) > 0.28 and total_mass(raw_filtered) < 1.0,
        f"state=({filtered[0]:.6f}, {filtered[1]:.6f}), ee={ee(filtered):.6f}, retained_mass={total_mass(raw_filtered):.6f}",
    )

    raw_symmetric = filter_raw((0.5, 0.5), sink_plus=0.45, sink_minus=0.45)
    symmetric = normalize(raw_symmetric)
    check(
        "symmetric filter changes retained mass but not handedness",
        abs(ee(symmetric)) < 1e-12 and abs(total_mass(raw_symmetric) - 0.55) < 1e-12,
        f"state=({symmetric[0]:.6f}, {symmetric[1]:.6f}), retained_mass={total_mass(raw_symmetric):.6f}",
    )

    dkr, dkr_mass = dynamic_resolution((0.5, 0.5), flip_rate=0.08, sink_plus=0.0, sink_minus=0.35, steps=80)
    check(
        "dynamic kinetic resolution works only with an asymmetric sink",
        dkr[0] > 0.80 and ee(dkr) > 0.60 and dkr_mass < 1.0,
        f"state=({dkr[0]:.6f}, {dkr[1]:.6f}), ee={ee(dkr):.6f}, retained_mass={dkr_mass:.6f}",
    )

    symmetric_dkr, symmetric_dkr_mass = dynamic_resolution((0.5, 0.5), flip_rate=0.08, sink_plus=0.35, sink_minus=0.35, steps=80)
    check(
        "dynamic protocol with symmetric sinks still has no selector",
        abs(ee(symmetric_dkr)) < 1e-12 and symmetric_dkr_mass < 1.0,
        f"state=({symmetric_dkr[0]:.6f}, {symmetric_dkr[1]:.6f}), retained_mass={symmetric_dkr_mass:.6f}",
    )


def anticommutator_zero(w_a: int, w_b: int) -> bool:
    # D is the one-link massless hop [[0,1],[1,0]] and gamma5 is diag(w_a,w_b).
    d = ((0, 1), (1, 0))
    g = ((w_a, 0), (0, w_b))
    dg = (
        (d[0][0] * g[0][0] + d[0][1] * g[1][0], d[0][0] * g[0][1] + d[0][1] * g[1][1]),
        (d[1][0] * g[0][0] + d[1][1] * g[1][0], d[1][0] * g[0][1] + d[1][1] * g[1][1]),
    )
    gd = (
        (g[0][0] * d[0][0] + g[0][1] * d[1][0], g[0][0] * d[0][1] + g[0][1] * d[1][1]),
        (g[1][0] * d[0][0] + g[1][1] * d[1][0], g[1][0] * d[0][1] + g[1][1] * d[1][1]),
    )
    anti = (
        (dg[0][0] + gd[0][0], dg[0][1] + gd[0][1]),
        (dg[1][0] + gd[1][0], dg[1][1] + gd[1][1]),
    )
    return all(entry == 0 for row in anti for entry in row)


def block3_staggered_filter() -> None:
    print("\n[BLOCK 3] Staggered one-bond selector: anticommutation is the filter")
    assignments = list(itertools.product((1, -1), repeat=2))
    bare_classes = {
        "trivial/vector-like" if w_a == w_b else "staggered/chiral"
        for w_a, w_b in assignments
    }
    anticommute_survivors = [(w_a, w_b) for w_a, w_b in assignments if anticommutator_zero(w_a, w_b)]
    canonical_survivors = {
        pair if pair[0] > 0 else tuple(-x for x in pair)
        for pair in anticommute_survivors
    }

    check(
        "without {D,gamma5}=0 there are two inequivalent sign classes",
        bare_classes == {"trivial/vector-like", "staggered/chiral"},
        f"classes={sorted(bare_classes)}",
    )
    check(
        "matrix anticommutator {D,gamma5}=0 holds exactly for opposite signs",
        len(anticommute_survivors) == 2 and all(w_a == -w_b for w_a, w_b in anticommute_survivors),
        f"survivors={anticommute_survivors}",
    )
    check(
        "the two surviving assignments are one class up to global gauge",
        canonical_survivors == {(1, -1)},
        "the remaining distinction is the global sign",
    )


def block4_orientation_torsor() -> None:
    print("\n[BLOCK 4] Orientation host does not choose its section")
    sections = (+1, -1)
    hosted_source_vectors = {s: (1, s) for s in sections}
    check("orientation line hosts two coherent sections", len(hosted_source_vectors) == 2)
    check(
        "desired odd source is present only after choosing a section",
        hosted_source_vectors[-1] == (1, -1),
        f"chosen={hosted_source_vectors[-1]}",
    )
    check(
        "opposite section is equally coherent before a source theorem",
        hosted_source_vectors[+1] == (1, 1),
        f"unchosen={hosted_source_vectors[+1]}",
    )


@dataclass(frozen=True)
class Record:
    label: str
    observed_plus: float
    observed_minus: float


def append_record(label: str, carrier: tuple[float, float]) -> tuple[tuple[float, float], Record]:
    plus, minus = carrier
    return carrier, Record(label=label, observed_plus=plus, observed_minus=minus)


def block5_record_consumer() -> None:
    print("\n[BLOCK 5] Record consumes realized labels; it does not create a carrier chirality")
    carrier = (0.37, 0.63)
    after, rec = append_record("post-realization chirality tally", carrier)
    check("record append preserves the carrier distribution", after == carrier)
    check(
        "record stores the realized split without selecting a hand",
        math.isclose(rec.observed_plus, carrier[0]) and math.isclose(rec.observed_minus, carrier[1]),
        f"record=({rec.observed_plus:.2f}, {rec.observed_minus:.2f})",
    )


def block6_signed_readout_guardrail() -> None:
    print("\n[BLOCK 6] Signed readout guardrail")
    # A signed spectral label can be diagonal in the same basis as the C3
    # generator.  Then it is a commuting classifier, not an anticommuting
    # chirality operator in this toy readout.
    omega = complex(-0.5, math.sqrt(3.0) / 2.0)
    c3 = (1.0 + 0j, omega, omega.conjugate())
    signed_readout = (1, -1, -1)
    commute_entries = [c3[i] * signed_readout[i] - signed_readout[i] * c3[i] for i in range(3)]
    check(
        "toy signed C3 readout commutes with the C3 labels",
        all(abs(x) < 1e-12 for x in commute_entries),
        "commuting signed readout is not by itself chirality",
    )


def main() -> int:
    print("=" * 88)
    print("Chirality-resolution dynamics scout: blend/flip/filter boundary")
    print("=" * 88)
    block1_blend_and_flip()
    block2_filter_is_selector()
    block3_staggered_filter()
    block4_orientation_torsor()
    block5_record_consumer()
    block6_signed_readout_guardrail()
    print("\n" + "=" * 88)
    print(f"SCORECARD: PASS={len(PASS)} FAIL={len(FAIL)}")
    if FAIL:
        print("FAILURES:", FAIL)
    print("=" * 88)
    return 0 if not FAIL else 1


if __name__ == "__main__":
    sys.exit(main())
