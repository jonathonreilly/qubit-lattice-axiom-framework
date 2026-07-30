#!/usr/bin/env python3
"""Exact Boolean receiver-success and Cycle-610 gate-adapter theorem.

The theorem is deliberately limited to pinned executable interfaces and a
complete six-bit truth table. It assigns no physical meaning to the derived
bit.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120
NOTE_PATH = (
    "docs/CYCLE332_RECEIVER_SUCCESS_CYCLE610_GATE_ADAPTER_"
    "BOUNDED_THEOREM_NOTE_2026-07-30.md"
)
AUDIT_INPUT_PATHS = (
    "docs/CYCLE332_RECEIVER_SUCCESS_CYCLE610_GATE_ADAPTER_BOUNDED_THEOREM_NOTE_2026-07-30.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17.py",
    "scripts/active_cubic_source_response_cycle211_2026_07_16.py",
    "scripts/archive_carrier_source_ledger_cycle227_2026_07_17.py",
    "scripts/autonomous_cubic_field_emission_cycle214_2026_07_16.py",
    "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py",
    "scripts/connected_edge_autonomous_apparatus_law_cycle282_2026_07_17.py",
    "scripts/connected_edge_same_code_local_instrument_cycle278_2026_07_17.py",
    "scripts/contact_close_typed_record_dag_cycle287_2026_07_17.py",
    "scripts/contractible_lightcone_wilson_quotient_cycle271_2026_07_17.py",
    "scripts/exact_3d_higher_form_bosonization_cycle235_2026_07_17.py",
    "scripts/finite_coin_scalar_wave_dilation_cycle215_2026_07_16.py",
    "scripts/fock_modular_boundary_current_cycle229_2026_07_17.py",
    "scripts/local_conservative_commit_resource_gravity_cycle9_2026_07_14.py",
    "scripts/local_generator_source_tournament_cycle228_2026_07_17.py",
    "scripts/locally_matched_wilson_sector_states_cycle275_2026_07_17.py",
    "scripts/matter_coupling_faithful_close_record_candidate_cycle281_2026_07_17.py",
    "scripts/outgoing_carrier_nonrecurrence_cycle286_2026_07_17.py",
    "scripts/physical_autonomous_localized_refocused_matter_transition_tournament_cycle575_2026_07_22.py",
    "scripts/physical_contact_dimer_infinite_internal_content_tournament_cycle583_2026_07_22.py",
    "scripts/physical_cycle269_coherent_cubic_pair_orbit_2026_07_17.py",
    "scripts/physical_cycle269_coin_stream_contact_common_refinement_cycle304_2026_07_17.py",
    "scripts/physical_cycle269_collision_safe_auxiliary_ports_2026_07_17.py",
    "scripts/physical_cycle269_common_m64_fixed_seam_cycle311_2026_07_18.py",
    "scripts/physical_cycle269_full_two_particle_sector_interface_cycle305_2026_07_17.py",
    "scripts/physical_cycle269_higher_number_fixed_seam_cycle308_2026_07_17.py",
    "scripts/physical_cycle269_joint_six_mode_coin_lift_cycle302_2026_07_17.py",
    "scripts/physical_cycle269_local_contact_intertwiner_2026_07_17.py",
    "scripts/physical_cycle269_local_fock_extension_cycle312_2026_07_18.py",
    "scripts/physical_cycle269_position_growing_recurrent_compiler_cycle307_2026_07_17.py",
    "scripts/physical_cycle269_reference_relative_localized_pair_lift_2026_07_17.py",
    "scripts/physical_cycle269_staggered_reservoir_catchup_2026_07_17.py",
    "scripts/physical_event_to_append_commit_candidate_cycle326_2026_07_18.py",
    "scripts/physical_intrinsic_contact_bound_moving_transition_tournament_cycle578_2026_07_22.py",
    "scripts/physical_intrinsic_tick_event_relational_duration_tournament_cycle610_2026_07_22.py",
    "scripts/physical_m64_reversible_event_sidecar_cycle314_2026_07_18.py",
    "scripts/physical_matter_transition_clock_equivalence_tournament_cycle573_2026_07_22.py",
    "scripts/physical_support_matcher_predecessor_controls_cycle329_2026_07_18.py",
    "scripts/physical_tick_echo_association_causal_order_tournament_cycle612_2026_07_22.py",
    "scripts/physical_transition_occurrence_close_tournament_cycle332_2026_07_18.py",
    "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py",
    "scripts/retarded_cubic_mass_field_cycle213_2026_07_16.py",
    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py",
    "scripts/virtual_exchange_green_kernel_cycle216_2026_07_16.py",
    "scripts/wilson_subsystem_sector_free_compiler_cycle269_2026_07_17.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import sys
from time import perf_counter

import physical_event_to_append_commit_candidate_cycle326_2026_07_18 as C326
import physical_intrinsic_tick_event_relational_duration_tournament_cycle610_2026_07_22 as C610
import physical_support_matcher_predecessor_controls_cycle329_2026_07_18 as C329


ROOT = Path(__file__).resolve().parents[1]
SELF = Path(__file__).resolve()
SOURCE_PINS = {
    "scripts/physical_event_to_append_commit_candidate_cycle326_2026_07_18.py":
        "8762609f9e9e85fb9311ed467bbc91fd5905f2ac5d160997555e8623c5e7f44c",
    "scripts/physical_intrinsic_tick_event_relational_duration_tournament_cycle610_2026_07_22.py":
        "36fcb1655bbdcd758b69ea1e273821e5c820f738eb63199570c8f36c7e294bac",
    "scripts/physical_support_matcher_predecessor_controls_cycle329_2026_07_18.py":
        "2cf6370f72cd4025fcfba8f0edefff1c577ad2bf5c5b93f996ef23c5affbab0b",
    "scripts/physical_transition_occurrence_close_tournament_cycle332_2026_07_18.py":
        "de7883fe45ce248427e8e44294d77fce56394e5ed14724e9056a65b43e0a4415",
}
PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def digest(relative: str) -> str:
    return sha256((ROOT / relative).read_bytes()).hexdigest()


def normalized_text(relative: str) -> str:
    body = (ROOT / relative).read_text(encoding="utf-8").lower()
    return " ".join(body.replace("`", "").replace("*", "").split())


def note_contract() -> dict[str, object]:
    required = (
        "claim type: bounded_theorem",
        "receiver_success = e and p and q and m and r and t",
        "framework admissibility and objective physical admission are outside the conclusion",
        "no separate naming convention is introduced",
        "ships no authored pass transcript or claim-status receipt",
    )
    forbidden = (
        "admiss_predicate",
        "second acceptance supply falls",
        "two flags down",
        "genuinely absent",
        "forcing-ledger",
        "minimal-missing-content",
    )
    try:
        text = normalized_text(NOTE_PATH)
    except OSError:
        return {"exists": False, "missing": list(required), "forbidden": []}
    return {
        "exists": True,
        "missing": [phrase for phrase in required if phrase not in text],
        "forbidden": [phrase for phrase in forbidden if phrase in text],
    }


def source_pin_check() -> dict[str, object]:
    observed = {path: digest(path) for path in SOURCE_PINS}
    return {
        "expected": SOURCE_PINS,
        "observed": observed,
        "all_match": observed == SOURCE_PINS,
    }


def direct_function(tree: ast.Module, name: str) -> ast.FunctionDef:
    matches = [
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(matches) != 1:
        raise ValueError(f"expected one top-level function {name}")
    return matches[0]


def cycle332_delegate_shape() -> dict[str, object]:
    path = SOURCE_PINS.keys() - {
        "scripts/physical_event_to_append_commit_candidate_cycle326_2026_07_18.py",
        "scripts/physical_intrinsic_tick_event_relational_duration_tournament_cycle610_2026_07_22.py",
        "scripts/physical_support_matcher_predecessor_controls_cycle329_2026_07_18.py",
    }
    relative = path.pop()
    actual_tree = ast.parse((ROOT / relative).read_text(encoding="utf-8"))
    actual = direct_function(actual_tree, "boundary_certificate")
    expected = ast.parse(
        """
def boundary_certificate(
    pre_code: int,
    transition: int,
    post_code: int,
    match: int,
    ready: int,
    *,
    deleted_stage: int | None = None,
) -> int:
    return c329.causal_certificate(
        (pre_code, transition, post_code, match, ready),
        (1, 1, 1, 1, 1),
        deleted_stage=deleted_stage,
    )[0]
"""
    ).body[0]
    exact = ast.dump(actual, include_attributes=False) == ast.dump(
        expected, include_attributes=False
    )
    return {
        "path": relative,
        "function": "boundary_certificate",
        "exact_delegate": exact,
    }


def actual_receiver_success(bits: tuple[int, ...]) -> tuple[int, int]:
    event_ready, pre_code, post_code, match, ready, transition = bits
    certificate = C329.causal_certificate(
        (pre_code, transition, post_code, match, ready),
        (1, 1, 1, 1, 1),
    )[0]
    fresh, candidate = C326.run_local_close(
        event_ready=event_ready,
        identity_match=match,
        dependencies_ready=ready,
        occurrence=transition,
        close_law=certificate,
    )
    return int((fresh, candidate) == (0, 1)), certificate


def receiver_truth_table() -> dict[str, object]:
    rows = []
    mismatches = 0
    certificate_ones = 0
    receiver_ones = 0
    for bits in product((0, 1), repeat=6):
        receiver, certificate = actual_receiver_success(bits)
        expected = int(all(bits))
        mismatches += receiver != expected
        certificate_ones += certificate
        receiver_ones += receiver
        rows.append((bits, certificate, receiver, expected))
    all_one = (1, 1, 1, 1, 1, 1)
    deletions = []
    for index in range(6):
        mutated = list(all_one)
        mutated[index] = 0
        receiver, _certificate = actual_receiver_success(tuple(mutated))
        deletions.append(receiver)
    return {
        "rows": len(rows),
        "mismatches": mismatches,
        "certificate_ones": certificate_ones,
        "receiver_ones": receiver_ones,
        "single_control_deletion_survivors": sum(deletions),
    }


def adapter_status(receiver_success: int, **overrides: int) -> str:
    values = {
        "certificate": 1,
        "binder": 1,
        "actuality": 1,
        "law_domain": 1,
    }
    values.update(overrides)
    chain = C610.EventChain(bank=1)
    return chain.admit(
        tick_id=0,
        orientation=1,
        certificate=values["certificate"],
        binder=values["binder"],
        actuality=values["actuality"],
        admissibility=receiver_success,
        law_domain=values["law_domain"],
    )


def adapter_controls() -> dict[str, object]:
    two_rows = {
        str(bit): adapter_status(bit)
        for bit in (0, 1)
    }
    supplied_deletions = {
        name: adapter_status(1, **{name: 0})
        for name in ("certificate", "binder", "actuality", "law_domain")
    }
    exhausted = C610.EventChain(bank=0).admit(
        tick_id=0,
        orientation=1,
        certificate=1,
        binder=1,
        actuality=1,
        admissibility=1,
        law_domain=1,
    )
    repeated = C610.EventChain(bank=2)
    first = repeated.admit(
        tick_id=0,
        orientation=1,
        certificate=1,
        binder=1,
        actuality=1,
        admissibility=1,
        law_domain=1,
    )
    second = repeated.admit(
        tick_id=0,
        orientation=1,
        certificate=1,
        binder=1,
        actuality=1,
        admissibility=1,
        law_domain=1,
    )
    expected_deletions = {
        "certificate": "no_opportunity",
        "binder": "no_opportunity",
        "actuality": "refused_supplied",
        "law_domain": "refused_supplied",
    }
    return {
        "two_rows": two_rows,
        "supplied_deletions": supplied_deletions,
        "exhausted_capacity": exhausted,
        "repeated_tick": (first, second),
        "all_match": (
            two_rows == {"0": "refused_supplied", "1": "admitted"}
            and supplied_deletions == expected_deletions
            and exhausted == "exhausted"
            and (first, second) == ("admitted", "refused_fresh")
        ),
    }


def repository_modules_loaded() -> tuple[str, ...]:
    loaded = set()
    for module in tuple(sys.modules.values()):
        raw = getattr(module, "__file__", None)
        if not raw:
            continue
        try:
            path = Path(raw).resolve()
            relative = path.relative_to(ROOT)
        except (OSError, ValueError):
            continue
        if path != SELF and relative.suffix == ".py":
            loaded.add(relative.as_posix())
    return tuple(sorted(loaded))


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    started = perf_counter()

    note = note_contract()
    check(
        "A note binds the exact Boolean scope and semantic firewall",
        note["exists"] and not note["missing"] and not note["forbidden"],
        note,
    )

    pins = source_pin_check()
    check("B four load-bearing executable sources match their pins", pins["all_match"], pins)

    delegate = cycle332_delegate_shape()
    check(
        "C Cycle-332 boundary certificate remains the exact five-bit delegate",
        delegate["exact_delegate"],
        delegate,
    )

    receiver = receiver_truth_table()
    check(
        "D complete six-bit receiver table equals the conjunction",
        receiver
        == {
            "rows": 64,
            "mismatches": 0,
            "certificate_ones": 2,
            "receiver_ones": 1,
            "single_control_deletion_survivors": 0,
        },
        receiver,
    )

    adapter = adapter_controls()
    check(
        "E Cycle-610 adapter and boundary controls match the named conditions",
        adapter["all_match"],
        adapter,
    )

    loaded = repository_modules_loaded()
    undeclared = sorted(set(loaded) - set(AUDIT_INPUT_PATHS))
    check(
        "F every runtime-loaded repository module is cache-fingerprinted",
        not undeclared,
        {
            "loaded_repository_modules": len(loaded),
            "declared_inputs": len(AUDIT_INPUT_PATHS),
            "undeclared": undeclared,
        },
    )

    runtime = perf_counter() - started
    check(
        "G runtime remains within the declared audit timeout",
        runtime <= AUDIT_TIMEOUT_SEC,
        {"runtime_sec": round(runtime, 6), "timeout_sec": AUDIT_TIMEOUT_SEC},
    )

    summary = {
        "all_pass": FAIL == 0,
        "adapter_rows": adapter["two_rows"],
        "audit_input_count": len(AUDIT_INPUT_PATHS),
        "fail": FAIL,
        "pass": PASS,
        "receiver_rows": receiver["rows"],
        "receiver_mismatches": receiver["mismatches"],
        "receiver_successes": receiver["receiver_ones"],
        "runtime_loaded_repository_modules": len(loaded),
        "runtime_sec": round(runtime, 6),
        "scope": "finite Boolean receiver-success and conditional Cycle-610 gate adapter",
    }
    print("SUMMARY_JSON", json.dumps(summary, sort_keys=True, separators=(",", ":")))
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
