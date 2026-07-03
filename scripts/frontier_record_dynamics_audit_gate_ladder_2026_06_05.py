#!/usr/bin/env python3
"""Record dynamics audit gate ladder classifier."""

from __future__ import annotations

from pathlib import Path


PASS = 0
FAIL = 0


def emit(line: str = "") -> None:
    print(line)


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" ({detail})" if detail else ""
    emit(f"  [{tag}] {label}{suffix}")


def section(title: str) -> None:
    emit()
    emit("-" * 78)
    emit(title)
    emit("-" * 78)


GATES = {
    "kernel",
    "produced_record",
    "history",
    "local_observability",
    "reset_resource",
    "open_reset_channel",
    "epsilon_reset",
    "clock_rate",
}


ARTIFACT_GATES = {
    "record_instrument_kernel_interface": {"kernel"},
    "record_history_time_rate_firewall": {"history"},
    "record_local_observability_decoder": {"local_observability"},
    "record_reset_sink_entropy_ledger": {"reset_resource"},
    "record_open_system_reset_channel_interface": {"reset_resource", "open_reset_channel"},
    "record_asymptotic_reset_convergence_ledger": {"epsilon_reset"},
}


CLAIM_REQUIREMENTS = {
    "probability_over_possible_records": {"kernel"},
    "post_record_history": {"produced_record", "history"},
    "local_objective_record": {"local_observability"},
    "reusable_clean_production": {"reset_resource", "open_reset_channel"},
    "epsilon_reset": {"epsilon_reset"},
    "physical_rate": {"clock_rate"},
}


EXPECTED_CLASSIFICATION = {
    "probability_over_possible_records": "support_available",
    "post_record_history": "conditional_on_produced_record",
    "local_objective_record": "support_available_when_broadcast",
    "reusable_clean_production": "bounded_support_cost_rate_open",
    "epsilon_reset": "bounded_support_exact_endpoint_open",
    "physical_rate": "open",
}


def supplied_gates() -> set[str]:
    out: set[str] = set()
    for gates in ARTIFACT_GATES.values():
        out |= gates
    return out


def classify(claim: str) -> str:
    required = CLAIM_REQUIREMENTS[claim]
    supplied = supplied_gates()
    if claim == "post_record_history" and "produced_record" not in supplied:
        return "conditional_on_produced_record"
    if claim == "local_objective_record" and required <= supplied:
        return "support_available_when_broadcast"
    if claim == "reusable_clean_production" and required <= supplied:
        return "bounded_support_cost_rate_open"
    if claim == "epsilon_reset" and required <= supplied:
        return "bounded_support_exact_endpoint_open"
    if required <= supplied:
        return "support_available"
    return "open"


def main() -> int:
    emit("=" * 78)
    emit("RECORD DYNAMICS AUDIT GATE LADDER")
    emit("bounded-support / classifier runner")
    emit("=" * 78)

    section("1. Gate vocabulary and coverage")
    supplied = supplied_gates()
    check("gate vocabulary has eight entries", len(GATES) == 8)
    check("all artifact gates are recognized", all(gate in GATES for gates in ARTIFACT_GATES.values() for gate in gates))
    check("current stack supplies reset_resource", "reset_resource" in supplied)
    check("current stack supplies open_reset_channel", "open_reset_channel" in supplied)
    check("current stack supplies epsilon_reset", "epsilon_reset" in supplied)
    check("current stack does not supply clock_rate", "clock_rate" not in supplied)
    check("produced_record remains lane-specific", "produced_record" not in supplied)
    check("six artifacts are classified", len(ARTIFACT_GATES) == 6)

    section("2. Claim requirement classification")
    for claim, required in CLAIM_REQUIREMENTS.items():
        check(f"{claim}: has required-gate declaration", bool(required))
        check(
            f"{claim}: expected classification",
            classify(claim) == EXPECTED_CLASSIFICATION[claim],
            classify(claim),
        )

    section("3. Overclaim pruning rules")
    overclaims = {
        "kernel_implies_produced_record": "produced_record" not in ARTIFACT_GATES["record_instrument_kernel_interface"],
        "local_observability_implies_reset": "reset_resource" not in ARTIFACT_GATES["record_local_observability_decoder"],
        "open_reset_implies_clock": "clock_rate" not in ARTIFACT_GATES["record_open_system_reset_channel_interface"],
        "epsilon_reset_implies_exact": classify("epsilon_reset") == "bounded_support_exact_endpoint_open",
        "step_count_implies_rate": classify("physical_rate") == "open",
        "gate_ladder_fixes_dial": "dial_selector" not in GATES,
    }
    for label, ok in overclaims.items():
        check(label.replace("_", " "), ok)

    section("4. Source note sanity")
    doc = Path("docs/RECORD_DYNAMICS_AUDIT_GATE_LADDER_2026-06-05.md")
    text = doc.read_text(encoding="utf-8")
    markers = [
        "actual_current_surface_status: bounded-support",
        "trace_class: upstream_support",
        "branch-local dynamics gate classifier",
        "Does not update repo-wide authority surfaces",
        "`clock_rate` gate is absent",
        "audit_required_before_effective_retained: true",
    ]
    check("source note exists", doc.exists(), str(doc))
    for marker in markers:
        check(f"note contains marker: {marker}", marker in text)
    forbidden_wording = [
        ("audit verdict", "promoted to " + "retained"),
        ("rate closure", "physical rate is " + "derived"),
        ("cost closure", "thermodynamic cost is " + "derived"),
        ("record production closure", "produced records are " + "derived"),
        ("dial closure", "dial location is " + "selected"),
        ("authority edit", "updates repo-wide " + "authority"),
    ]
    for label, phrase in forbidden_wording:
        check(f"forbidden wording absent: {label}", phrase not in text)

    section("SCORECARD")
    emit(f"SCORECARD PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
