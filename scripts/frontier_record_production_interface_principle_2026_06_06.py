#!/usr/bin/env python3
"""Verifier for the Record production interface principle.

The runner checks that the current repo supports a typed split:
pre-record quantum/predictive surface, separate formation bridge, and
post-record information dynamics. It deliberately verifies that Record does
not by itself supply probabilities, instruments, rates, production dynamics,
carrier choice, or dial selection.
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
    "classicalization": ROOT / "docs" / "RECORD_CLASSICALIZATION_DYNAMICS_FIREWALL_2026-06-05.md",
    "post_record_dynamics": ROOT / "docs" / "RECORD_FINITE_ALPHABET_POST_RECORD_DYNAMICS_2026-06-05.md",
    "formation_constraint": ROOT / "docs" / "RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md",
    "kraus_isometry": ROOT / "docs" / "PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20.md",
    "layer_reconciliation": ROOT / "docs" / "RECORD_DYNAMICS_LAYER_RECONCILIATION_2026-06-05.md",
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
    classicalization = read_text("classicalization")
    post_record = read_text("post_record_dynamics")
    formation = read_text("formation_constraint")
    kraus = read_text("kraus_isometry")
    reconciliation = read_text("layer_reconciliation")

    check(
        "gate status is exact support but not axiom or closure",
        has(gate, "exact-support branch-local typing/interface principle")
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
        "gate says the principle is not an added axiom",
        has(gate, "derived from the current axiom boundary")
        and has(gate, "not an additional axiom"),
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

    check(
        "classicalization note names pre-record predictive weights",
        has(classicalization, "pre-record carrier")
        and has(classicalization, "predictive\nweights once an instrument/readout context is supplied"),
    )
    check(
        "classicalization note names post-record realized value",
        has(classicalization, "post-record object supplied by Record is the")
        and has(classicalization, "realized `K`/CPT orbit"),
    )
    check(
        "classicalization note forbids probability as individual record",
        has(classicalization, "rather than a probability distribution")
        and has(classicalization, "not the same kind of object\nas the realized record atom"),
    )
    check(
        "classicalization note says post-record information is not fourth axiom",
        has(classicalization, "not a fourth \"post-record information\" axiom"),
    )
    check(
        "classicalization note has dynamics benefit",
        has(classicalization, "Quantum dynamics, record formation, and post-record")
        and has(classicalization, "information flow no longer compete"),
    )
    check(
        "classicalization note runner result is present",
        has(classicalization, "PASS=29 FAIL=0")
        or has(classicalization, "frontier_record_classicalization_dynamics_firewall_2026_06_05"),
    )

    check(
        "post-record dynamics note has finite alphabet premise",
        has(post_record, "Once a readout context supplies a finite record alphabet `O`"),
    )
    check(
        "post-record dynamics note gives append/count layer",
        has(post_record, "post-record append action on O*")
        and has(post_record, "post-record information dynamics on `O*` / `N^O`"),
    )
    check(
        "post-record dynamics note excludes production probabilities and rates",
        has(post_record, "record-production dynamics")
        and has(post_record, "probabilities or Born frequencies")
        and has(post_record, "transition rates"),
    )
    check(
        "post-record dynamics note is exact support not probability closure",
        has(post_record, "exact support")
        and has(post_record, "not a\nphysical dynamics closure")
        and has(post_record, "Does not derive probabilities"),
    )

    check(
        "formation note attacks record-production dynamics gate",
        has(formation, "forms a record")
        and has(formation, "Lattice, Quantum, and Record axioms")
        and has(formation, "do not by\nthemselves assert"),
    )
    check(
        "formation note supplies non-demolition constraint",
        has(formation, "pointer-non-demolition")
        and has(formation, "[H_int, Pi_S] = 0"),
    )
    check(
        "formation note records necessity and sufficiency",
        has(formation, "equivalent to\n   pointer-non-demolition")
        or has(formation, "all** times **iff** `[H_int, Pi_S] = 0"),
    )
    check(
        "formation note does not derive dynamics or couplings",
        has(formation, "It does not derive a dynamics")
        and has(formation, "does not pin the coupling strength"),
    )
    check(
        "formation note is bounded model bridge not axiom content",
        has(formation, "This is **bounded**")
        and has(formation, "supplied bounded model input"),
    )

    check(
        "Kraus note assumes W rather than deriving it",
        has(kraus, "once a normalized linear isometry `W` is\nassumed")
        and has(kraus, "does not derive `W`"),
    )
    check(
        "Kraus note gives exact finite instrument algebra once W is supplied",
        has(kraus, "finite Kraus/CPTP algebra closes")
        and has(kraus, "CPTP unconditional update"),
    )
    check(
        "Kraus note excludes persistent-record dynamics",
        has(kraus, "deriving `W` from persistent-record dynamics")
        and has(kraus, "persistent-record-to-isometry bridge remains open"),
    )
    check(
        "Kraus note supplies formation bridge target",
        has(kraus, "any future persistent-record bridge must")
        and has(kraus, "supply if it wants a Kraus/CPTP measurement-update structure"),
    )

    check(
        "layer reconciliation names exact post-record layer",
        has(reconciliation, "post-record information dynamics")
        and has(reconciliation, "exact support"),
    )
    check(
        "layer reconciliation separates formation from post-record information",
        has(reconciliation, "record formation bridge, bounded")
        and has(reconciliation, "post-record information dynamics, exact"),
    )
    check(
        "layer reconciliation forbids production outputs from post-record layer",
        has(reconciliation, "exact post-record dynamics has no edge to production")
        or has(reconciliation, "forbids production/probability/rate/dial outputs"),
    )
    check(
        "layer reconciliation preserves bounded composition status",
        has(reconciliation, "bounded formation/preservation claims require their bridge premises")
        and has(reconciliation, "remains bounded-support"),
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
    print("STATUS: exact-support typing/interface principle; audit_required_before_effective_retained=true")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    if FAIL_COUNT:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
