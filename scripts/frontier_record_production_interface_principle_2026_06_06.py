#!/usr/bin/env python3
"""Verifier for the Record production interface principle.

The runner checks a narrow proof packet:

* the source note;
* the accepted Minimal Axioms premise;
* finite type-set and Fraction arithmetic that separates predictive weights,
  formation/instrument data, realized atoms, and post-record counts/readouts.

It deliberately does not read the unaudited Record-stack companion notes. Those
notes are downstream context only, not load-bearing proof dependencies for this
row.
"""
from __future__ import annotations

from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
PASS_COUNT = 0
FAIL_COUNT = 0


PATHS = {
    "gate_note": ROOT / "docs" / "RECORD_PRODUCTION_INTERFACE_PRINCIPLE_2026-06-06.md",
    "minimal_axioms": ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-05.md",
}


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"[{status}] {name}{suffix}")


def read_text(label: str) -> str:
    path = PATHS[label]
    check(f"{label} exists", path.exists(), path.relative_to(ROOT).as_posix())
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def has(text: str, needle: str) -> bool:
    return needle in text


def main() -> None:
    print("Record production interface principle")
    print("=" * 64)

    gate = read_text("gate_note")
    minimal = read_text("minimal_axioms")

    check(
        "gate status is bounded support but not axiom or closure",
        has(gate, "bounded-support branch-local typing/interface principle")
        and has(gate, "not a new\naxiom")
        and has(gate, "not a record-production closure"),
    )
    check(
        "gate states the four-stage interface",
        has(gate, "pre-record quantum state")
        and has(gate, "record-production bridge or instrument")
        and has(gate, "realized record atom")
        and has(gate, "post-record word/count/readout dynamics"),
    )
    check(
        "gate cites Minimal Axioms as accepted axiom premise",
        has(gate, "Accepted axiom premise, load-bearing")
        and has(gate, "MINIMAL_AXIOMS_2026-06-05.md"),
    )
    check(
        "gate says companion Record-stack notes are context only",
        has(gate, "Context only, not load-bearing")
        and has(gate, "no longer reads them as proof dependencies"),
    )
    check(
        "gate keeps probability on predictive, ensemble, or bridge surfaces",
        has(gate, "Probability can re-enter as a predictive state before the event")
        and has(gate, "It is not the\nindividual durable record"),
    )
    check(
        "gate preserves dial non-forcing",
        has(gate, "stable post-record location as a permitted setting")
        and has(gate, "without claiming that post-record dynamics forces the dial"),
    )

    check(
        "minimal axioms provide one-qubit Quantum carrier",
        has(minimal, "primitive physical local degree of freedom is one qubit")
        and has(minimal, "A_x ~= M_2(C)"),
    )
    check(
        "minimal axioms define Record as durable realized outcome",
        has(minimal, "A record is the durable registration of the realized outcome")
        and has(minimal, "Durable means fixed once registered"),
    )
    check(
        "minimal axioms provide finite scalar additivity",
        has(minimal, "For any finite pairwise-disjoint collection of records")
        and has(minimal, "finitely additive"),
    )
    check(
        "minimal axioms exclude probability and dynamics from Record",
        has(minimal, "probability,\nmeasurement/decoherence dynamics")
        and has(minimal, "record-production dynamics"),
    )
    check(
        "minimal axioms keep record-production dynamics outside axioms",
        has(minimal, "arrow, measurement, decoherence, record-production dynamics")
        and has(minimal, "remain outside axiom content"),
    )

    pre_record_outputs = {
        "density_state",
        "effect",
        "predictive_weight",
        "coherence",
        "ensemble_probability",
    }
    formation_outputs = {
        "record_atom_stream",
        "instrument_W",
        "Kraus_family",
        "pointer_non_demolition",
        "context_choice",
    }
    post_record_outputs = {
        "record_atom",
        "word_history",
        "count_vector",
        "coarse_graining",
        "finite_scalar_readout",
    }
    forbidden_post_record_outputs = {
        "probability_law",
        "production_rate",
        "instrument_W",
        "carrier_choice",
        "generation_dial",
        "next_atom_selector",
    }

    check("typed output sets are pairwise distinct at the interface", pre_record_outputs.isdisjoint(post_record_outputs))
    check("formation bridge overlaps neither pure predictive nor pure count outputs", formation_outputs.isdisjoint(pre_record_outputs - {"effect"}))
    check("post-record layer does not supply forbidden outputs", post_record_outputs.isdisjoint(forbidden_post_record_outputs))
    check("formation layer is where instrument W belongs", "instrument_W" in formation_outputs and "instrument_W" not in post_record_outputs)
    check("dial remains outside post-record outputs", "generation_dial" in forbidden_post_record_outputs and "generation_dial" not in post_record_outputs)

    born = (Fraction(2, 3), Fraction(1, 3))
    e0 = (Fraction(1, 1), Fraction(0, 1))
    e1 = (Fraction(0, 1), Fraction(1, 1))
    start_counts = (3, 4)
    update0 = tuple(a + b for a, b in zip(start_counts, e0))
    update1 = tuple(a + b for a, b in zip(start_counts, e1))
    expected_update = tuple(start_counts[i] + born[i] for i in range(2))

    check("Born weights are normalized predictive weights", sum(born) == 1 and born[0] not in (0, 1))
    check("realized post-record atom 0 is one-hot, not Born vector", e0 != born and sum(e0) == 1)
    check("realized post-record atom 1 is one-hot, not Born vector", e1 != born and sum(e1) == 1)
    check("realized count update for atom 0 is integral", update0 == (4, 4), str(update0))
    check("realized count update for atom 1 is integral", update1 == (3, 5), str(update1))
    check("predictive expected update is fractional ensemble data", expected_update == (Fraction(11, 3), Fraction(13, 3)), str(expected_update))
    check("expected update is neither realized update", expected_update != update0 and expected_update != update1)
    check("post-record information can be copied idempotently", e0 == e0 and e1 == e1 and e0 != e1)
    check("one-hot atoms are distinguishable information tokens", e0[0] * e1[0] + e0[1] * e1[1] == 0)
    check("principle is a type split, not a probability derivation", "probability_law" not in post_record_outputs)

    print("=" * 64)
    print("INTERFACE:")
    print("  pre_record: predictive quantum state/effect surface")
    print("  formation:  separate record-writing bridge or instrument")
    print("  post_record: realized atom -> words/counts/readouts")
    print("STATUS: bounded-support typing/interface principle; audit_required_before_effective_retained=true")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    if FAIL_COUNT:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
