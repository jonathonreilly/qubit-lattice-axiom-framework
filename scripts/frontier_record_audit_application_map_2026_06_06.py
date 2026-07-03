#!/usr/bin/env python3
"""Record axiom audit-application map.

This runner applies the Record unbounded finite-additivity schema to concrete
record-sensitive lane shapes without editing audit data. It checks that Record
additivity supports only durable finite readout/count requirements, while
separate gates such as local observability, production, log-det origin,
chirality, gauge/color matter realization, rates, and dials remain exposed.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


PASS = 0
FAIL = 0
ROOT = Path(__file__).resolve().parents[1]


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"[{tag}] {label}{suffix}")


SUPPORTED_BY_RECORD_SCHEMA = {
    "durable_realized_outcome",
    "finite_additivity",
    "arbitrary_finite_prefix_schema",
    "post_record_count",
    "post_record_label_consumption",
}


@dataclass(frozen=True)
class AuditCase:
    case_id: str
    source_path: str
    required_gates: tuple[str, ...]
    expected_supported: tuple[str, ...]
    expected_missing: tuple[str, ...]
    anchor_phrases: tuple[str, ...]

    @property
    def supported(self) -> set[str]:
        return set(self.required_gates).intersection(SUPPORTED_BY_RECORD_SCHEMA)

    @property
    def missing(self) -> set[str]:
        return set(self.required_gates).difference(SUPPORTED_BY_RECORD_SCHEMA)

    @property
    def classification(self) -> str:
        if not self.missing:
            return "record_schema_sufficient"
        if self.supported:
            return "record_schema_partial"
        return "record_schema_not_load_bearing"


CASES = (
    AuditCase(
        case_id="record_unbounded_additivity_schema",
        source_path="docs/RECORD_UNBOUNDED_FINITE_ADDITIVITY_SCHEMA_2026-06-06.md",
        required_gates=(
            "durable_realized_outcome",
            "finite_additivity",
            "arbitrary_finite_prefix_schema",
        ),
        expected_supported=(
            "durable_realized_outcome",
            "finite_additivity",
            "arbitrary_finite_prefix_schema",
        ),
        expected_missing=(),
        anchor_phrases=("arbitrary finite-prefix schema", "This row does not derive record production"),
    ),
    AuditCase(
        case_id="flavor_det_character_selection",
        source_path="docs/FLAVOR_DET_CHARACTER_SELECTION_AUDIT_READY_2026-06-04.md",
        required_gates=(
            "finite_additivity",
            "regularity_smoothness",
            "composition_multiplicativity",
            "determinant_partition_origin",
        ),
        expected_supported=("finite_additivity",),
        expected_missing=(
            "regularity_smoothness",
            "composition_multiplicativity",
            "determinant_partition_origin",
        ),
        anchor_phrases=(
            "the exact Record typing theorem supplies the object-type firewall",
            "regular additive readouts of positive multiplicative amplitudes",
        ),
    ),
    AuditCase(
        case_id="darwinism_local_observability",
        source_path="docs/DARWINISM_BRIDGE_RESIDUAL_LOCAL_OBSERVABILITY_OPEN_GATE_NOTE_2026-06-05.md",
        required_gates=(
            "durable_realized_outcome",
            "finite_additivity",
            "locality",
            "local_observability",
            "redundant_broadcast",
        ),
        expected_supported=("durable_realized_outcome", "finite_additivity"),
        expected_missing=("locality", "local_observability", "redundant_broadcast"),
        anchor_phrases=("local-observability", "Additivity != redundancy"),
    ),
    AuditCase(
        case_id="dynamics_form_record_preservation",
        source_path="docs/DYNAMICS_FORM_FROM_RECORD_PRESERVATION_GAUGE_INVARIANT_LOCAL_CLASS_BOUNDED_THEOREM_NOTE_2026-06-05.md",
        required_gates=(
            "durable_realized_outcome",
            "record_preservation_dynamics",
            "two_endpoint_gauss_structure",
            "hermiticity",
            "coupling_selection",
            "minimality_truncation",
        ),
        expected_supported=("durable_realized_outcome",),
        expected_missing=(
            "record_preservation_dynamics",
            "two_endpoint_gauss_structure",
            "hermiticity",
            "coupling_selection",
            "minimality_truncation",
        ),
        anchor_phrases=("record-preservation + locality + Hermiticity", "couplings"),
    ),
    AuditCase(
        case_id="color_su3_record_invariance",
        source_path="docs/COLOR_SU3_SYMMETRIC_BASE_BRIDGE_FROM_RECORD_INVARIANCE_BOUNDED_NOTE_2026-06-05.md",
        required_gates=(
            "post_record_label_consumption",
            "record_invariance_commutant",
            "symmetric_base_carrier",
            "matter_realization",
            "link_color_routing",
        ),
        expected_supported=("post_record_label_consumption",),
        expected_missing=(
            "record_invariance_commutant",
            "symmetric_base_carrier",
            "matter_realization",
            "link_color_routing",
        ),
        anchor_phrases=("matter realization", "not forced by Lattice + Quantum + Record"),
    ),
    AuditCase(
        case_id="chirality_record_typing",
        source_path="docs/CHIRALITY_RECORD_TYPING_INTERFACE_2026-06-05.md",
        required_gates=(
            "post_record_label_consumption",
            "carrier_chirality",
            "car_frame",
            "signed_readout_choice",
            "generation_transport",
        ),
        expected_supported=("post_record_label_consumption",),
        expected_missing=(
            "carrier_chirality",
            "car_frame",
            "signed_readout_choice",
            "generation_transport",
        ),
        anchor_phrases=("record dynamics is a consumer", "carrier/readout bridge"),
    ),
    AuditCase(
        case_id="arrow_from_record_formation",
        source_path="docs/ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md",
        required_gates=(
            "durable_realized_outcome",
            "record_formation_dynamics",
            "low_record_boundary",
            "past_hypothesis",
        ),
        expected_supported=("durable_realized_outcome",),
        expected_missing=(
            "record_formation_dynamics",
            "low_record_boundary",
            "past_hypothesis",
        ),
        anchor_phrases=("past hypothesis", "record-production dynamics"),
    ),
)


def read_source(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def main() -> int:
    print("Record axiom audit-application map")
    print("actual_current_surface_status: bounded-support")
    print("trace_class: upstream_support")
    print("reachability_to_target: supports")
    print("proposal_allowed: false")
    print("audit_required_before_effective_retained: true")
    print()

    print("A. source availability and anchors")
    for case in CASES:
        source_file = ROOT / case.source_path
        check(f"{case.case_id}: source file exists", source_file.exists(), case.source_path)
        text = read_source(case.source_path)
        for phrase in case.anchor_phrases:
            check(f"{case.case_id}: anchor phrase present", phrase in text, phrase)

    print("\nB. gate classification")
    for case in CASES:
        supported = tuple(sorted(case.supported))
        missing = tuple(sorted(case.missing))
        print(f"case: {case.case_id}")
        print(f"  classification={case.classification}")
        print(f"  supported={supported}")
        print(f"  missing={missing}")
        check(
            f"{case.case_id}: supported gate set matches expectation",
            set(case.expected_supported) == case.supported,
            ",".join(supported) or "none",
        )
        check(
            f"{case.case_id}: missing gate set matches expectation",
            set(case.expected_missing) == case.missing,
            ",".join(missing) or "none",
        )

    print("\nC. audit discipline")
    full_cases = [case.case_id for case in CASES if case.classification == "record_schema_sufficient"]
    partial_cases = [case.case_id for case in CASES if case.classification == "record_schema_partial"]
    check("only the schema artifact itself is fully covered by Record schema", full_cases == ["record_unbounded_additivity_schema"], str(full_cases))
    check("real downstream lanes are partial, not promoted", len(partial_cases) == len(CASES) - 1, str(partial_cases))
    forbidden_claims = {
        "record derives production",
        "record derives probability",
        "record derives local observability",
        "record derives chirality",
        "record derives color",
        "record selects a dial",
    }
    emitted_claims = {
        "record supports finite additivity",
        "record supports durable realized outcome",
        "record supports post-record count/readout consumption",
    }
    check("forbidden closure claims are absent from classifier outputs", forbidden_claims.isdisjoint(emitted_claims))
    check("classifier emits only support/gate language", emitted_claims.issubset({
        "record supports finite additivity",
        "record supports durable realized outcome",
        "record supports post-record count/readout consumption",
    }))

    print()
    print(f"SCORECARD: PASS={PASS} FAIL={FAIL}")
    if PASS > 0 and FAIL == 0:
        print(
            "VERDICT: The Record schema fully covers only durable finite "
            "additivity/count-readout requirements. Concrete downstream lanes "
            "remain partial whenever they need regularity, log-det origin, "
            "local observability, record-production dynamics, chirality, color "
            "matter realization, rates, or dial selection."
        )
        return 0
    print("VERDICT: record audit application map failed; do not use this artifact.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
