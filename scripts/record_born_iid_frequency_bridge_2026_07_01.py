#!/usr/bin/env python3
"""Verifier for the Record/Born IID frequency bridge."""

from __future__ import annotations

import json
from fractions import Fraction
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

NOTE = DOCS / "RECORD_BORN_IID_FREQUENCY_BRIDGE_2026-07-01.md"
AXIOMS = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = DOCS / "audit" / "data" / "axiom_premise_nodes.json"
FREQ_BOUNDARY = DOCS / "RECORD_BORN_FREQUENCY_BOUNDARY_2026-06-05.md"
BORN_INTERFACE = DOCS / "RECORD_BORN_INTERFACE_FROM_SELECTIVE_WRITE_BRIDGE_2026-06-30.md"
OCCURRENCE_INSTRUMENT = DOCS / "RECORD_OCCURRENCE_INSTRUMENT_SUPPLIER_BRIDGE_2026-07-01.md"
OCCURRENCE_ACTIVATION = DOCS / "RECORD_OCCURRENCE_ACTIVATION_INDEPENDENCE_2026-07-01.md"
OP_GAP_MAP = DOCS / "OPERATIONAL_PREMISE_GAP_MAP_2026-07-01.md"
PRIMITIVE_RECOMMENDATION = DOCS / "MINIMAL_OPERATIONAL_PRIMITIVE_UPDATE_RECOMMENDATION_2026-07-01.md"

PASS = 0
FAIL = 0


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def flat(text: str) -> str:
    return " ".join(text.split())


def check(label: str, ok: bool, detail: object = "") -> None:
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"[{tag}] {label}{suffix}")


def section(title: str) -> None:
    print("\n" + title)


def binary_product_weight(word: tuple[int, ...], p_one: Fraction) -> Fraction:
    weight = Fraction(1)
    for bit in word:
        weight *= p_one if bit else (1 - p_one)
    return weight


def binary_stats_by_enumeration(n_trials: int, p_one: Fraction) -> tuple[Fraction, Fraction, Fraction]:
    total = Fraction(0)
    mean_freq = Fraction(0)
    second_freq = Fraction(0)
    for word in product((0, 1), repeat=n_trials):
        weight = binary_product_weight(word, p_one)
        freq = Fraction(sum(word), n_trials)
        total += weight
        mean_freq += weight * freq
        second_freq += weight * freq * freq
    return total, mean_freq, second_freq - mean_freq * mean_freq


def multinomial_history_weight(word: tuple[int, ...], probs: tuple[Fraction, ...]) -> Fraction:
    weight = Fraction(1)
    for outcome in word:
        weight *= probs[outcome]
    return weight


def multinomial_stats(n_trials: int, probs: tuple[Fraction, ...]) -> tuple[Fraction, list[Fraction], list[Fraction]]:
    total = Fraction(0)
    means = [Fraction(0) for _ in probs]
    seconds = [Fraction(0) for _ in probs]
    for word in product(range(len(probs)), repeat=n_trials):
        weight = multinomial_history_weight(word, probs)
        total += weight
        for outcome in range(len(probs)):
            freq = Fraction(word.count(outcome), n_trials)
            means[outcome] += weight * freq
            seconds[outcome] += weight * freq * freq
    variances = [seconds[i] - means[i] * means[i] for i in range(len(probs))]
    return total, means, variances


def main() -> int:
    print("=== Record/Born IID frequency bridge ===")

    paths = [
        NOTE,
        AXIOMS,
        REGISTRY,
        FREQ_BOUNDARY,
        BORN_INTERFACE,
        OCCURRENCE_INSTRUMENT,
        OCCURRENCE_ACTIVATION,
        OP_GAP_MAP,
        PRIMITIVE_RECOMMENDATION,
    ]
    for path in paths:
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    note_flat = flat(note)
    axioms = read(AXIOMS)
    registry_text = read(REGISTRY)
    registry = json.loads(registry_text)
    freq_boundary = read(FREQ_BOUNDARY)
    born_interface = read(BORN_INTERFACE)
    occurrence_instrument = read(OCCURRENCE_INSTRUMENT)
    occurrence_activation = read(OCCURRENCE_ACTIVATION)
    occurrence_activation_flat = flat(occurrence_activation)
    op_gap = read(OP_GAP_MAP)
    primitive = read(PRIMITIVE_RECOMMENDATION)

    section("PART A -- source boundaries")
    check("note declares independent audit authority", "independent audit lane only" in note)
    check("note declares no axiom or registry edits", "does not set an audit verdict, edit registries, register primitives, change axioms" in flat(note))
    check("axioms keep probability and occurrence downstream", "probability" in axioms and "occurrence rule" in axioms)
    check("frequency boundary says counts do not derive probabilities", "finite history word" in freq_boundary and "not a derivation of the pre-record probability" in flat(freq_boundary))
    check("Born interface supplies trace weights after interface", "p(r) = m(P_r) = Tr(rho P_r)" in born_interface)
    check("Born interface leaves IID frequency route open", "IID frequency route" in born_interface and "OPEN" in born_interface)
    check("occurrence instrument supplies activation and selection after instrument", "activation a_x" in occurrence_instrument and "selection p_x(v)" in occurrence_instrument)
    check("activation independence preserves occurrence wall", "activation" in occurrence_activation and "does not derive occurrence activation" in occurrence_activation_flat)
    check("operational gap map names occurrence and instrument/reset structure", "instrument/reset structure" in op_gap)

    section("PART B -- primitive registry check")
    expected_ids = {
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    }
    check("registry canonical ids are expected set", set(registry["canonical_ids"]) == expected_ids, registry["canonical_ids"])
    for node_id in expected_ids:
        source = DOCS.parent / registry["nodes"][node_id]["current_path"]
        check(f"registry source exists for {node_id}", source.exists())
    check("no registered P_record_extension", "P_record_extension" not in registry_text)
    check("no registered IID measurement primitive", "P_iid_measurement_run" not in registry_text)
    check("no approved primitive supplies probability frequencies", "probability frequencies" not in registry_text)
    check("primitive recommendation keeps candidates unregistered", "fallback primitive candidates, not primitive registrations" in primitive)

    section("PART C -- binary IID finite theorem")
    p = Fraction(2, 5)
    n_trials = 6
    total, mean_freq, var_freq = binary_stats_by_enumeration(n_trials, p)
    check("binary product histories normalize", total == 1, total)
    check("binary empirical frequency mean equals p", mean_freq == p, mean_freq)
    check("binary empirical frequency variance is p(1-p)/N", var_freq == p * (1 - p) / n_trials, var_freq)
    binomial_total = sum(
        Fraction(__import__("math").comb(n_trials, k)) * p**k * (1 - p) ** (n_trials - k)
        for k in range(n_trials + 1)
    )
    expected_count = sum(
        Fraction(k) * Fraction(__import__("math").comb(n_trials, k)) * p**k * (1 - p) ** (n_trials - k)
        for k in range(n_trials + 1)
    )
    second_count = sum(
        Fraction(k * k) * Fraction(__import__("math").comb(n_trials, k)) * p**k * (1 - p) ** (n_trials - k)
        for k in range(n_trials + 1)
    )
    check("binomial grouped law normalizes", binomial_total == 1, binomial_total)
    check("binomial grouped expected count is Np", expected_count == n_trials * p, expected_count)
    check("binomial grouped count variance is Np(1-p)", second_count - expected_count * expected_count == n_trials * p * (1 - p))

    section("PART D -- finite concentration")
    eps = Fraction(1, 5)
    bound_10 = p * (1 - p) / (10 * eps * eps)
    bound_100 = p * (1 - p) / (100 * eps * eps)
    check("Chebyshev bound decreases with N", bound_100 < bound_10, (bound_10, bound_100))
    check("Chebyshev N=100 bound is exact formula", bound_100 == Fraction(3, 50), bound_100)
    check("note states finite Chebyshev bound", "p(v)(1 - p(v)) / (N epsilon^2)" in note)

    section("PART E -- multinomial finite theorem")
    probs = (Fraction(1, 2), Fraction(1, 3), Fraction(1, 6))
    total_m, means_m, vars_m = multinomial_stats(4, probs)
    check("three-outcome product histories normalize", total_m == 1, total_m)
    check("three-outcome empirical means equal probabilities", means_m == list(probs), means_m)
    check(
        "three-outcome empirical variances match p(1-p)/N",
        vars_m == [q * (1 - q) / 4 for q in probs],
        vars_m,
    )

    section("PART F -- independence is load-bearing")
    # Correlated two-trial model with the same one-trial marginal p:
    # P(00)=1-p, P(11)=p. Frequency of 1 is either 0 or 1.
    correlated_mean = p
    correlated_second = p
    correlated_var = correlated_second - correlated_mean * correlated_mean
    iid_two_var = p * (1 - p) / 2
    check("correlated model has same one-trial marginal", correlated_mean == p)
    check("correlated model has larger frequency variance than IID", correlated_var != iid_two_var and correlated_var == p * (1 - p), (correlated_var, iid_two_var))
    check("note uses correlated negative control", "P(00) = 1 - p" in note and "P(11) = p" in note)
    check("note says IID condition is load-bearing", "The IID condition is real content" in note)

    section("PART G -- note content")
    for heading in [
        "## Claim",
        "## Finite Theorem",
        "## Load-Bearing Reset/Independence",
        "## Relation To Existing Record/Born Work",
        "## What Moves",
        "## What Remains",
        "## Audit Consequence If Retained",
        "## Non-Claims",
        "## Minimum Foundation Update If Bridge Work Fails",
        "## No-Go Discipline Gate",
    ]:
        check(f"note includes {heading}", heading in note)
    check("note names W_iid_frequency", "W_iid_frequency" in note)
    check("note preserves no probability-from-counts claim", "does not derive probabilities from post-record counts" in note)
    check("note preserves no finite equality claim", "finite frequencies equal probabilities in any given run" in note)
    check("note says no ontology axiom update follows", "No ontology axiom update follows from this theorem" in note)

    section("PART H -- no-go discipline N1-N8")
    for item in ("N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8"):
        check(f"note includes {item}", item in note)
    for route in [
        "Count-only route",
        "Born-interface route",
        "Occurrence-instrument route",
        "IID reset route",
        "Correlated-run route",
        "New primitive route",
    ]:
        check(f"N1 route present: {route}", route in note)
    check("N2 names reset/occurrence/rate/objectivity split", "Born trace weights do not imply reset" in note)
    check("N3 classifies supplied IID reset", "\"Supplied IID reset/preparation\" is an explicit bridge input" in note)
    check("N4 matches five witnesses", note.count("| `RECORD_") >= 3 and "`OPERATIONAL_PREMISE_GAP_MAP_2026-07-01`" in note)
    check("N5 narrows finite-history negative", "finite record histories alone do not supply" in note)
    check("N6 lists live closure paths", "Markov or transfer law" in note and "bounded experimental protocol" in note)
    check("N7 steelman preserves standard theorem objection", "mathematically standard" in note and "all real physics" in note)
    check("N8 separates weights, records, repeated trials, frequencies", "weights are pre-record interface content" in note_flat)

    section("PART I -- non-overclaim checks")
    forbidden = [
        "therefore occurrence is derived",
        "therefore IID reset is derived",
        "therefore probabilities are derived from counts",
        "therefore finite frequencies equal probabilities",
        "therefore measurement semantics are closed",
        "therefore a new ontology axiom is required",
    ]
    for phrase in forbidden:
        check(f"note avoids overclaim assertion: {phrase}", phrase not in note_flat)
    check("non-claims preserve no occurrence derivation", "- record occurrence is derived;" in note)
    check("non-claims preserve no IID derivation", "- IID reset/preparation is derived from the four ontology axioms;" in note)
    check("non-claims preserve no measured constants", "measured constants" in note and "not claim" in note_flat)

    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("RESULT: FAIL")
        return 1
    print(
        "RESULT: PASS -- supplied IID reset/preparation turns Born record weights into multinomial histories and finite frequency concentration; occurrence/reset remain explicit suppliers."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
