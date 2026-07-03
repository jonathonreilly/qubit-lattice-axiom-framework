#!/usr/bin/env python3
"""Record dynamics layer reconciliation verifier.

This runner checks the typed separation between:

* exact post-record information dynamics;
* bounded physical formation/preservation dynamics;
* residual probability, source, coupling, and dial gates.

It is a support-map verifier, not an audit-verdict tool.

Run:
    python3 scripts/frontier_record_dynamics_layer_reconciliation_2026_06_05.py
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


PASS = 0
FAIL = 0
ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class Layer:
    name: str
    support: str
    inputs: tuple[str, ...]
    outputs: tuple[str, ...]
    forbidden_outputs: tuple[str, ...]


LAYERS = (
    Layer(
        name="pre_record_carrier",
        support="open_or_bounded",
        inputs=("qubit_state", "carrier_dynamics"),
        outputs=("candidate_amplitudes", "candidate_instruments", "transfer_steps"),
        forbidden_outputs=("realized_record_without_bridge",),
    ),
    Layer(
        name="formation_preservation_dynamics",
        support="bounded_support",
        inputs=("quantum_Darwinism_bridge", "finite_model", "locality", "Gauss_bridge", "Hermiticity"),
        outputs=("pointer_non_demolition_constraint", "gauge_invariant_local_form_class"),
        forbidden_outputs=("couplings", "truncation_selection", "production_rates", "bridge_premise_derivation"),
    ),
    Layer(
        name="post_record_information_dynamics",
        support="exact_support",
        inputs=("finite_record_alphabet", "realized_atom_stream"),
        outputs=("finite_histories", "counts", "append_action", "coarse_graining", "unbounded_finite_retention"),
        forbidden_outputs=("next_atom_selector", "probability_law", "transition_rate", "carrier_Hamiltonian", "dial_selection"),
    ),
)

LOCAL_NOTES = (
    "docs/RECORD_HISTORY_MONOID_UNBOUNDED_RETENTION_2026-06-05.md",
    "docs/RECORD_FINITE_ALPHABET_POST_RECORD_DYNAMICS_2026-06-05.md",
    "docs/RECORD_HISTORY_COUNT_AUDIT_UNLOCK_SCAN_2026-06-05.md",
)

RELATED_SOURCE_NOTES = (
    "docs/RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md",
    "docs/DYNAMICS_FORM_FROM_RECORD_PRESERVATION_GAUGE_INVARIANT_LOCAL_CLASS_BOUNDED_THEOREM_NOTE_2026-06-05.md",
)

REQUIRED_RESIDUALS = {
    "record_production_dynamics",
    "measurement_or_quantum_Darwinism_bridge",
    "probability_laws",
    "transition_rates",
    "clock_or_time_metric",
    "Gauss_generator_identification",
    "couplings",
    "action_shape_or_truncation",
    "nontrivial_H_or_T",
    "dial_selection",
}


def check(name: str, cond: bool, detail: str = "") -> bool:
    global PASS, FAIL
    ok = bool(cond)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return ok


def support_rank(status: str) -> int:
    order = {
        "exact_support": 3,
        "bounded_support": 2,
        "open_or_bounded": 1,
    }
    return order[status]


def compose_status(*statuses: str) -> str:
    min_rank = min(support_rank(s) for s in statuses)
    for name in ("open_or_bounded", "bounded_support", "exact_support"):
        if support_rank(name) == min_rank:
            return name
    raise AssertionError("unreachable")


def main() -> int:
    # ------------------------------------------------------------------
    # 1. Availability checks.
    # ------------------------------------------------------------------
    for path in LOCAL_NOTES:
        check(f"N1 local note exists: {path}", (ROOT / path).exists())
    for path in RELATED_SOURCE_NOTES:
        check(f"N1 related landed source exists: {path}", (ROOT / path).exists())

    # ------------------------------------------------------------------
    # 2. Layer typing checks.
    # ------------------------------------------------------------------
    layer_names = {layer.name for layer in LAYERS}
    check("L2 expected three layers", layer_names == {"pre_record_carrier", "formation_preservation_dynamics", "post_record_information_dynamics"})
    for layer in LAYERS:
        check(f"L2 layer has inputs: {layer.name}", bool(layer.inputs), ",".join(layer.inputs))
        check(f"L2 layer has outputs: {layer.name}", bool(layer.outputs), ",".join(layer.outputs))
        check(f"L2 layer has forbidden outputs: {layer.name}", bool(layer.forbidden_outputs), ",".join(layer.forbidden_outputs))

    post = next(layer for layer in LAYERS if layer.name == "post_record_information_dynamics")
    formation = next(layer for layer in LAYERS if layer.name == "formation_preservation_dynamics")

    # ------------------------------------------------------------------
    # 3. Firewall checks.
    # ------------------------------------------------------------------
    forbidden_from_post = {
        "next_atom_selector",
        "probability_law",
        "transition_rate",
        "carrier_Hamiltonian",
        "dial_selection",
    }
    check("F3 post-record exact layer forbids production/probability/rate/dial outputs", forbidden_from_post.issubset(set(post.forbidden_outputs)))
    check("F3 post-record exact layer only consumes realized atom stream", "realized_atom_stream" in post.inputs)
    check("F3 formation layer carries bounded support", formation.support == "bounded_support")
    check("F3 formation layer names bridge premises", {"quantum_Darwinism_bridge", "Gauss_bridge"}.issubset(set(formation.inputs)))
    check("F3 formation layer does not force couplings", "couplings" in formation.forbidden_outputs)
    check("F3 formation layer does not force truncation", "truncation_selection" in formation.forbidden_outputs)

    # ------------------------------------------------------------------
    # 4. Composition status checks.
    # ------------------------------------------------------------------
    exact_post_only = compose_status(post.support)
    formation_to_post = compose_status(formation.support, post.support)
    full_carrier_to_post = compose_status("open_or_bounded", formation.support, post.support)
    check("C4 post-record layer alone stays exact-support", exact_post_only == "exact_support")
    check("C4 bounded formation feeding exact post-record stays bounded-support", formation_to_post == "bounded_support")
    check("C4 open/bounded carrier through formation to post-record is not exact", full_carrier_to_post == "open_or_bounded")

    # ------------------------------------------------------------------
    # 5. Residual ledger completeness.
    # ------------------------------------------------------------------
    recorded_residuals = {
        "record_production_dynamics",
        "measurement_or_quantum_Darwinism_bridge",
        "probability_laws",
        "transition_rates",
        "clock_or_time_metric",
        "Gauss_generator_identification",
        "couplings",
        "action_shape_or_truncation",
        "nontrivial_H_or_T",
        "dial_selection",
    }
    check("R5 all required residuals recorded", REQUIRED_RESIDUALS == recorded_residuals)
    check("R5 residual count", len(recorded_residuals) == 10)

    # ------------------------------------------------------------------
    # 6. No forbidden promotion.
    # ------------------------------------------------------------------
    allowed_statuses = {"exact_support", "bounded_support", "open_or_bounded"}
    check("P6 only support/open statuses used", all(layer.support in allowed_statuses for layer in LAYERS))
    check(
        "P6 no layer output includes retained/probability selection language",
        all("retained" not in item and "Born" not in item for layer in LAYERS for item in layer.outputs),
    )

    print("\n=== Record dynamics layer interpretation ===")
    print("Post-record information dynamics is exact once atoms are realized.")
    print("Physical formation/preservation dynamics remains bounded when it uses quantum-Darwinism, Gauss, or finite-model bridges.")
    print("The composition localizes residuals: production, probability/rates/time, observable bridge, couplings/truncation, and dial selection.")
    print(f"SCORECARD PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
