#!/usr/bin/env python3
"""Verifier for the Record production interface principle.

The runner checks a narrow proof packet:

* the source note;
* the accepted Minimal Axioms premise;
* finite type-set checks for the axiom-supplied interface, plus an explicitly
  supplied two-label encoding whose Fraction arithmetic illustrates the
  distinction between predictive weights and locked-record count updates.

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
EXPECTED_CHECKS = 28


PATHS = {
    "gate_note": ROOT / "docs" / "RECORD_PRODUCTION_INTERFACE_PRINCIPLE_2026-06-06.md",
    "minimal_axioms": ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md",
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
    global FAIL_COUNT
    print("Record production interface principle")
    print("=" * 64)

    gate = read_text("gate_note")
    minimal = read_text("minimal_axioms")

    check(
        "gate status is bounded support but not axiom or closure",
        has(gate, "bounded support theorem for the stated typing interface")
        and has(gate, "not a new\naxiom")
        and has(gate, "not a record-production closure"),
    )
    check(
        "gate states the four-stage interface",
        has(gate, "pre-record Qubit possibility surface constrained by Admissibility")
        and has(gate, "record-production bridge or instrument")
        and has(gate, "record locking one admissible local possibility")
        and has(gate, "post-record permanent record/readout surface"),
    )
    check(
        "gate cites Minimal Axioms as accepted axiom premise",
        has(gate, "Accepted axiom premise, load-bearing")
        and has(gate, "MINIMAL_AXIOMS_2026-06-29.md"),
    )
    check(
        "gate says companion Record-stack notes are context only",
        has(gate, "Context only, not load-bearing")
        and has(gate, "no longer reads them as proof dependencies"),
    )
    check(
        "gate keeps probability on predictive, ensemble, or bridge surfaces",
        has(gate, "Probability can enter through separately supplied predictive")
        and has(gate, "It is not the\nindividual permanent record"),
    )
    check(
        "gate preserves dial non-forcing",
        has(gate, "stable post-record location as a permitted setting")
        and has(gate, "without claiming that record content or readout forces the dial"),
    )

    check(
        "minimal axioms provide the Qubit possibility algebra",
        has(minimal, "Each site has a domain of local possibilities")
        and has(minimal, "full one-site possibility domain has algebraic presentation `M_2(C)`"),
    )
    check(
        "minimal axioms provide neighbor-dependent Admissibility",
        has(minimal, "There is one fixed nearest-neighbor admissibility rule")
        and has(minimal, "available possibilities are determined by, and vary with"),
    )
    check(
        "minimal axioms define permanent admissible Record locking",
        has(minimal, "Records form")
        and has(minimal, "a record locks exactly one admissible local possibility")
        and has(minimal, "records are permanent"),
    )
    check(
        "minimal axioms provide finite scalar additivity",
        has(minimal, "For any finite collection of pairwise-disjoint records")
        and has(minimal, "Only records are readable")
        and has(minimal, "A readout value is determined by record content")
        and has(minimal, "scalar readout\n`I` is additive"),
    )
    check(
        "minimal axioms keep formation rules and dynamics outside the axioms",
        has(minimal, "context selection, measurement basis selection, Born weights, probability")
        and has(minimal, "decoherence mechanisms, and formation rules")
        and has(minimal, "record-production dynamics, physical persistence dynamics")
        and has(minimal, "any sector\n  generation rule are downstream")
        and has(minimal, "These axioms state only their named primitive content")
        and has(minimal, "A choice not fixed by the\nsupplied structure remains a named conditional or open dependency"),
    )

    pre_record_outputs = {
        "predictive_density_operator",
        "effect",
        "predictive_weight",
        "coherence",
        "ensemble_probability",
    }
    formation_outputs = {
        "record_production_process",
        "instrument_W",
        "Kraus_family",
        "pointer_non_demolition",
        "context_choice",
    }
    post_record_outputs = {
        "permanent_record",
        "readable_record_content",
        "finite_disjoint_record_collection",
        "additive_scalar_readout",
    }
    forbidden_post_record_outputs = {
        "probability_law",
        "production_rate",
        "instrument_W",
        "carrier_choice",
        "generation_dial",
        "next_record_content_selector",
    }

    check(
        "typed output sets are pairwise distinct at the interface",
        pre_record_outputs.isdisjoint(formation_outputs)
        and pre_record_outputs.isdisjoint(post_record_outputs)
        and formation_outputs.isdisjoint(post_record_outputs),
    )
    check(
        "formation bridge overlaps neither predictive nor post-record outputs",
        formation_outputs.isdisjoint(pre_record_outputs)
        and formation_outputs.isdisjoint(post_record_outputs),
    )
    check("post-record layer does not supply forbidden outputs", post_record_outputs.isdisjoint(forbidden_post_record_outputs))
    check("formation layer is where instrument W belongs", "instrument_W" in formation_outputs and "instrument_W" not in post_record_outputs)
    check("dial remains outside post-record outputs", "generation_dial" in forbidden_post_record_outputs and "generation_dial" not in post_record_outputs)

    born = (Fraction(2, 3), Fraction(1, 3))
    locked0_encoding = (Fraction(1, 1), Fraction(0, 1))
    locked1_encoding = (Fraction(0, 1), Fraction(1, 1))
    start_counts = (3, 4)
    update0 = tuple(a + b for a, b in zip(start_counts, locked0_encoding))
    update1 = tuple(a + b for a, b in zip(start_counts, locked1_encoding))
    expected_update = tuple(start_counts[i] + born[i] for i in range(2))

    check("Born weights are normalized predictive weights", sum(born) == 1 and born[0] not in (0, 1))
    check("supplied locked-record encoding 0 is one-hot, not Born vector", locked0_encoding != born and sum(locked0_encoding) == 1)
    check("supplied locked-record encoding 1 is one-hot, not Born vector", locked1_encoding != born and sum(locked1_encoding) == 1)
    check("conditional count update for encoding 0 is integral", update0 == (4, 4), str(update0))
    check("conditional count update for encoding 1 is integral", update1 == (3, 5), str(update1))
    check("predictive expected update is fractional ensemble data", expected_update == (Fraction(11, 3), Fraction(13, 3)), str(expected_update))
    check("expected update is neither single-record update", expected_update != update0 and expected_update != update1)
    check("each conditional append increments total count by one", sum(update0) == sum(start_counts) + 1 and sum(update1) == sum(start_counts) + 1)
    check("supplied one-hot encodings distinguish record contents", locked0_encoding[0] * locked1_encoding[0] + locked0_encoding[1] * locked1_encoding[1] == 0)
    check("principle is a type split, not a probability derivation", "probability_law" not in post_record_outputs)

    if PASS_COUNT + FAIL_COUNT != EXPECTED_CHECKS:
        print(
            f"[FAIL] check inventory changed "
            f"(expected={EXPECTED_CHECKS}, actual={PASS_COUNT + FAIL_COUNT})"
        )
        FAIL_COUNT += 1

    print("=" * 64)
    print("INTERFACE:")
    print("  pre_record: Qubit possibilities filtered by Admissibility")
    print("  formation:  separate record-writing bridge or instrument")
    print("  post_record: permanent record -> content/readout")
    print("  bookkeeping: labels/count updates require a separately supplied encoding")
    print("STATUS: bounded support typing/interface theorem; audit_required_before_effective_retained=true")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    if FAIL_COUNT:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
