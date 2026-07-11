#!/usr/bin/env python3
"""Universal-floor classification support runner for species identification.

This runner is intentionally small and deterministic. It mirrors the parent
species runner's C3 parity checks at the label level, then guards the live text
needed for the owner-gated classification argument.
"""

from __future__ import annotations

import json
import pathlib
import re
import sys
from fractions import Fraction


ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

ARROW = DOCS / "ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md"
PARENT = DOCS / "SPECIES_BRIDGE_MINIMUM_DECOMPOSITION_BOUNDED_THEOREM_NOTE_2026-06-13.md"
REGISTRY = DOCS / "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md"
DECISION_HISTORY = DOCS / "audit" / "data" / "premise_decision_history.json"

PASS = 0
FAIL = 0


def normalized_text(path: pathlib.Path) -> str:
    raw = path.read_text(encoding="utf-8")
    return " ".join(raw.split())


def check(num: int, ok: bool, desc: str, detail: str = "") -> None:
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    suffix = f" -- {detail}" if detail else ""
    print(f"CHECK {num:02d}: {tag} - {desc}{suffix}")


def spread(values: list[Fraction]) -> Fraction:
    return max(values) - min(values)


def c3_action(label: int, power: int = 1) -> int:
    return (label + power) % 3


def orbit(start: int) -> list[int]:
    seen: list[int] = []
    current = start
    for _ in range(3):
        seen.append(current)
        current = c3_action(current)
    return seen


def reynolds_average_diagonal(diagonal: list[Fraction]) -> list[Fraction]:
    averaged: list[Fraction] = []
    for label in range(3):
        total = sum(diagonal[c3_action(label, power)] for power in range(3))
        averaged.append(total / 3)
    return averaged


def section(text: str, start: str, stop: str) -> str:
    begin = text.find(start)
    end = text.find(stop, begin + len(start)) if begin != -1 else -1
    if begin == -1 or end == -1:
        return ""
    return text[begin:end]


def main() -> int:
    arrow = normalized_text(ARROW)
    parent = normalized_text(PARENT)
    registry = normalized_text(REGISTRY)

    labels = [0, 1, 2]
    label_orbit = orbit(0)
    check(
        1,
        sorted(label_orbit) == labels and c3_action(c3_action(c3_action(0))) == 0,
        "single C3 orbit on the three corner labels",
        f"orbit={label_orbit}",
    )

    raw_diagonal = [Fraction(0), Fraction(3), Fraction(6)]
    averaged_diagonal = reynolds_average_diagonal(raw_diagonal)
    check(
        2,
        spread(raw_diagonal) == Fraction(6) and spread(averaged_diagonal) == Fraction(0),
        "Reynolds average of diagonal corner-weight has spread 0",
        f"raw_spread={spread(raw_diagonal)}, averaged={averaged_diagonal}",
    )

    arrow_quote = (
        "This open input is **universal-floor**: every theory with time-symmetric "
        "microdynamics (CM, QM, QFT, GR) needs the same boundary input for a "
        "thermodynamic arrow. It is **not** a framework-specific gap."
    )
    check(
        3,
        arrow_quote in arrow,
        "live quote guard: arrow universal-floor sentence",
    )

    historical_registry_quote = (
        "the past hypothesis sits with the universal-floor admissions (scale "
        "reference / strong-CP-style shared problems), not the framework-specific "
        "Tier A-1 derivation targets (AC_phi_lambda, theta)."
    )
    check(
        4,
        historical_registry_quote in arrow,
        "historical quote guard: superseded past-hypothesis placement sentence",
    )

    parent_same_id_quote = (
        "It is the same identification every gauge theory makes between its abstract "
        "representation-theoretic content and the named physical species at the "
        "C₃-structural grade; if that universal identification is not counted as a "
        "framework-specific admission elsewhere, AC_φλ(iii) need not be either — "
        "but this note does not make that governance call; it only fixes the tested "
        "C₃-grade content to zero."
    )
    check(
        5,
        parent_same_id_quote in parent,
        "live quote guard: parent same-identification sentence",
    )

    species_no_number_quote = (
        "a single interpretive identification of an already-derived irreducible "
        "C₃-structure with the physical fermion generations, carrying no tested "
        "C₃-grade number, selector, ordering, or weight."
    )
    check(
        6,
        species_no_number_quote in parent,
        "direct text extraction: species residual statement names no tested number",
    )

    history = json.loads(DECISION_HISTORY.read_text(encoding="utf-8"))
    theta_section = json.dumps(
        history["retired_derivation_targets"]["strong_cp_theta_zero_note"],
        ensure_ascii=False,
    )
    theta_names_number = (
        "theta_bar = theta_gauge + arg det(M_q)" in theta_section
        and "theta_gauge = 0" in theta_section
        and "arg det M in {0, pi}" in theta_section
        and "orientation arg det M" in theta_section
    )
    check(
        7,
        theta_names_number,
        "historical provenance preserves the former theta decomposition",
    )

    ckm_quote = (
        "**Not** a claim about across-fermion-type alignment (the CKM/PMNS "
        "mixing structure) — a separate residual, not addressed here."
    )
    check(
        8,
        ckm_quote in parent,
        "direct text extraction: CKM/PMNS remains separate",
    )

    all_files = ", ".join(path.name for path in (ARROW, PARENT, REGISTRY))
    total_checks = PASS + FAIL
    print(f"files: {all_files}")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print(
        "classification claim: AC_phi_lambda(iii)'s C3-grade species "
        "identification belongs beside the past hypothesis as a universal-floor "
        "candidate, subject to owner ruling."
    )
    print(
        "counterargument: every theory needing an input does not make it free; "
        "the defense is the past-hypothesis precedent plus the no-number "
        "discriminator."
    )
    print(
        "uncertainties: owner registry ruling, audit-lane handling, and any "
        "above-C3 or CKM/PMNS content remain outside this runner."
    )
    return 0 if FAIL == 0 and total_checks == 8 else 1


if __name__ == "__main__":
    sys.exit(main())
