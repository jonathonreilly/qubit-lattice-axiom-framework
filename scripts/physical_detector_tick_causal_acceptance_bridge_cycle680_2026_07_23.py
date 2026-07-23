#!/usr/bin/env python3
"""Cycle680: detector/tick to causal synchronization acceptance bridge."""
from __future__ import annotations


TARGET_CONTRACT = {
    "cycle": 680,
    "decisive_question": (
        "can actual committed detector/tick outputs and state-carried predecessor packets be accepted by the causal "
        "Cycle676 synchronization/renewal decoder without substituting its ideal nu/s event generator for a physical "
        "source, while every objective-admission, co-registration, renewal and identification supply remains explicit"
    ),
    "quantifiers_domain": (
        "actual Cycle610 train L9 and held L13 purified detector words; committed Cycle602/672/675 detector surfaces "
        "including L3/L4/L6; two capacity-six blank banks; K16 carry wrap; train/held, forward/reversed, piecewise, "
        "missing-event, inverted-order, deletion, malformed, all24 and all576 controls"
    ),
    "allowed_premises": (
        "exact git-object bytes at current shore d2d16ab80b and causal shore 3621220d2a; candidate tick certificates; "
        "supplied actuality/admissibility/law-domain and co-registration packets only when typed; blank physical M2; "
        "Cycle669 support-two lowering and Cycle612/Cycle665 predecessor packet shape"
    ),
    "forbidden_weakenings": (
        "calling causal Cycle676 ideal nu/s crossings physical; reading detector update labels, loop ordinals or shared s "
        "inside a decoder; calling a candidate tick an occurrence; calling a packet a framework Record; calling a "
        "decoded count or ratio proper time; relabeling update/factor/count as rate, time or energy; hiding refill or marks"
    ),
    "completion_witness": (
        "regenerated detector-law tick certificates accepted by a bounded physical M2 predecessor/rotor/carry overlay; unchanged "
        "causal decoders pass every physically meaningful acceptance row; two physical clocks have lawfully generated "
        "shared co-registration events; and the causal identification law attaches without host ordinal or s"
    ),
    "outcomes_not_closure": (
        "law-level nu/s replay; host-chosen shared marks; a static detector snapshot called a clock; a supplied actuality "
        "bit hidden as detection; count additivity called proper time; finite bank extension called autonomous renewal"
    ),
}
TARGET_CONTRACT_SHA256 = "c82e450cce472956c9f1d417972cb826b4aff420ebef94537d8a5f0d7bff22ad"


PREREGISTRATION = {
    "actual_clock_rows": {
        "train_L9_rest": {"length": 9, "momentum": "K0", "steps": 4096, "split": "train"},
        "held_L13_rest": {"length": 13, "momentum": "K0", "steps": 2048, "split": "held"},
        "held_L13_moving": {"length": 13, "momentum": "K_HELD", "steps": 2048, "split": "held"},
    },
    "renewal": {
        "bank_capacity": 6, "banks": 2, "accepted_events": 12, "initial_rotor": 12,
        "mark_event_indices": {"S1": 0, "S2": 3, "S3": 8, "S4": 11},
        "required_refills": 1,
    },
    "causal_assertions": (
        "rate_constancy", "ratio_transitivity", "offset_prediction", "renewal_invariance", "reversal",
        "piecewise_additivity", "missing_shared_event", "inverted_coregistration", "no_ordinal_or_s_decoder",
    ),
    "held_static_detector_sizes": (3, 4, 6),
    "negative_gate": "fresh N1-N8 before any shared-obstruction, minimum-content or axiom-pressure claim",
}
PREREGISTRATION_SHA256 = "afd5c9c2d270533fc07248985720726edbc308429de98cc1e8c08d3afb44915a"


from dataclasses import dataclass, replace
from hashlib import sha256
from itertools import product
import ast
import inspect
import json
import math
from pathlib import Path
import resource
import signal
import subprocess
import sys
import time
import types

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
CURRENT_SHORE = "d2d16ab80b261c48cd7b9162cd08be0358a6d06e"
CAUSAL_SHORE = "3621220d2a5c7e769b547f1be95386ecf7a1f62e"
NOTE = ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_DETECTOR_TICK_CAUSAL_ACCEPTANCE_BRIDGE_CYCLE680_NOTE_2026-07-23.md"
RECEIPT = ROOT / "outputs/physical_detector_tick_causal_acceptance_bridge_cycle680_receipt_2026_07_23.json"
AUTHORITY = "none"
AUDIT = "unset"
WALL_CAP_SECONDS = 300.0
RSS_CAP_BYTES = 3 * 1024**3
TOL = 2.0e-8
PASS = FAIL = 0


CURRENT_PINS = {
    "docs/work_history/repo/review_feedback/PHYSICAL_CYCLE608_LITERAL_AGGREGATE_DETECTOR_PRODUCT_CYCLE672_NOTE_2026-07-23.md": "def730b1161028a584684482fdcadd76e86ad94e3c2590862a54aaf60e9d4263",
    "docs/work_history/repo/review_feedback/PHYSICAL_DETECTOR_FORMATION_CURRENT_INTERVAL_KERNEL_CYCLE668_NOTE_2026-07-23.md": "9d991077c7533c98fc65114e6c3f516f523eeaf547722151ae5af8e0a1fc51fd",
    "docs/work_history/repo/review_feedback/PHYSICAL_INTRINSIC_TICK_EVENT_RELATIONAL_DURATION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md": "63854c353f477f7beb8371d3a4489c02d8787c54679ab8963c7cc828972a4ea4",
    "docs/work_history/repo/review_feedback/PHYSICAL_OCCUPANCY_SIX_Q_SYNDROME_EXTRACTOR_CYCLE675_NOTE_2026-07-23.md": "dbabca9a1460950f9701462723679d696ef4b94a8cda7cd3a62b220f885d51f5",
    "docs/work_history/repo/review_feedback/PHYSICAL_STATE_CARRIED_EVENT_CHAIN_SEQUENCE_PROTOCOL_CYCLE669_NOTE_2026-07-23.md": "4ba9fe3a26606a944f362e81d6262543936018c6adf497069d8800e616f0c2c5",
    "docs/work_history/repo/review_feedback/PHYSICAL_TRANSPORTED_OBSERVABLE_RAMSEY_ECHO_EVENT_ROTOR_TOURNAMENT_CYCLE602_NOTE_2026-07-22.md": "c5971546e74165b98349791e0bcbbc910f40441855aa1181a2f14231cc674e37",
    "outputs/physical_cycle608_literal_aggregate_detector_product_cycle672_receipt_2026_07_23.json": "41d025b4c1b4cc89cc6c27b52157a4861189055e388f9f99c1929f997e07e745",
    "outputs/physical_detector_formation_current_interval_kernel_cycle668_receipt_2026_07_23.json": "f7f733820abdbcf5520a7edf9de9aca067aa7998374e02f3af07204c2718f6a0",
    "outputs/physical_intrinsic_tick_event_relational_duration_tournament_cycle610_receipt_2026_07_22.json": "0816073d1861bb8b36238ec4948c387801a75442c797baf4a52e335cf6d30ccc",
    "outputs/physical_occupancy_six_q_syndrome_extractor_cycle675_receipt_2026_07_23.json": "ac1e8585c48f8cd67366301be1837be3cdd80e21d9d47d4242c52f8db1481d64",
    "outputs/physical_state_carried_event_chain_sequence_protocol_cycle669_receipt_2026_07_23.json": "0765c66f3d3625892d133976aca217a5676fef0820557b12b32c988cb6180760",
    "outputs/physical_transported_observable_ramsey_echo_event_rotor_tournament_cycle602_receipt_2026_07_22.json": "db970ce03b88fdd7d6aa29bef2fd41c8df290b957c91181aec3f24e61e4f43b3",
    "scripts/physical_cycle608_literal_aggregate_detector_product_cycle672_2026_07_23.py": "c0af96a46e7f8a8641c0ec9de92da934fb24efc3887d9d5966e40ae91be44735",
    "scripts/physical_detector_formation_current_interval_kernel_cycle668_2026_07_23.py": "2e3402d01b1af725b51fcd8888c1c074f82bc6add07d34d2b020952308b1742b",
    "scripts/physical_intrinsic_tick_event_relational_duration_tournament_cycle610_2026_07_22.py": "61d624d3f47e371a3b99f55a3c60db68c1fe77f5d93a21651f9172b2d49f1458",
    "scripts/physical_occupancy_six_q_syndrome_extractor_cycle675_2026_07_23.py": "cf0ad89d0628878f1355754a419163400eda2710092f879bead34e1ed2643181",
    "scripts/physical_state_carried_event_chain_sequence_protocol_cycle669_2026_07_23.py": "ac1237e211bf06a8eb394db0dd8001c88a5aaf81726b38a3e43bd066285a9c84",
    "scripts/physical_transported_observable_ramsey_echo_event_rotor_tournament_cycle602_2026_07_22.py": "4b751525cd5918abbcc2ca47b71dba4bd3b2e9d2fbfd74deed0f932a8d75a137",
}

CAUSAL_PINS = {
    "docs/work_history/repo/review_feedback/PHYSICAL_BRANCH_TRACKED_ISOLATION_LABELED_VERNIER_CYCLE675_NOTE_2026-07-23.md": "f6e29bfb6d7082fdea7b2fb85ef2345b898df9b5a3fdf0fc83b79a0ef760e9dc",
    "docs/work_history/repo/review_feedback/PHYSICAL_SYNCHRONIZATION_RENEWAL_PROPER_TIME_LAW_TOURNAMENT_CYCLE676_NOTE_2026-07-23.md": "5f32c4a3f0e17583fc5549def66dca3ce06ac7f13df42fa297453c41152b9fe1",
    "outputs/physical_branch_tracked_isolation_labeled_vernier_cycle675_receipt_2026_07_23.json": "9f48bfc3ade8798d98535b5db11ab175e8580d35dffb8a42d3775fd086b23df3",
    "outputs/physical_synchronization_renewal_proper_time_law_tournament_cycle676_receipt_2026_07_23.json": "dd96821334a90a58142d01a46ace53601686c940482f61e863d49f47cdd5150f",
    "scripts/physical_branch_tracked_isolation_labeled_vernier_cycle675_2026_07_23.py": "7081a9cac970f06a6f38ab0ff57cfece986d8c29f986a7805d3f16259f6fbfe3",
    "scripts/physical_synchronization_renewal_proper_time_law_tournament_cycle676_2026_07_23.py": "ff280208ecb5913984fe25941bab2623d0979408957a65d0c111719efaaf49d9",
}


def check(label, condition, detail=""):
    global PASS, FAIL
    PASS += int(bool(condition)); FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def digest(value):
    return sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), default=lambda x: list(x)).encode()).hexdigest()


def file_sha(path): return sha256(Path(path).read_bytes()).hexdigest()


def git_bytes(ref, path):
    return subprocess.check_output(("git", "show", f"{ref}:{path}"), cwd=ROOT)


def load_exact(name, ref, path):
    module = types.ModuleType(name); module.__file__ = str(ROOT / path); module.__package__ = ""
    sys.modules[name] = module
    exec(compile(git_bytes(ref, path), module.__file__, "exec"), module.__dict__)
    return module


def citation(ref, path, fragment):
    rows = git_bytes(ref, path).decode().splitlines()
    matches = [line for line, body in enumerate(rows, 1) if fragment in body]
    if len(matches) != 1: raise AssertionError((path, fragment, matches))
    return {"ref": ref, "path": path, "line": matches[0]}


def git_function_source(ref, path, function_name):
    source = git_bytes(ref, path).decode(); tree = ast.parse(source)
    node = next(row for row in tree.body if isinstance(row, (ast.FunctionDef, ast.AsyncFunctionDef))
                and row.name == function_name)
    return ast.get_source_segment(source, node)


# Exact evidence modules are loaded only after frozen target/preregistration and pin tables.
c610 = load_exact("cycle680_exact_c610", CURRENT_SHORE,
                  "scripts/physical_intrinsic_tick_event_relational_duration_tournament_cycle610_2026_07_22.py")
c669 = load_exact("cycle680_exact_c669", CURRENT_SHORE,
                  "scripts/physical_state_carried_event_chain_sequence_protocol_cycle669_2026_07_23.py")
causal = load_exact("cycle680_exact_causal676", CAUSAL_SHORE,
                    "scripts/physical_synchronization_renewal_proper_time_law_tournament_cycle676_2026_07_23.py")


def freeze_controls():
    source = Path(__file__).read_text().splitlines()
    target_line = next(i for i, row in enumerate(source, 1) if row.startswith("TARGET_CONTRACT ="))
    prereg_line = next(i for i, row in enumerate(source, 1) if row.startswith("PREREGISTRATION ="))
    evidence_line = next(i for i, row in enumerate(source, 1) if row.startswith("c610 = load_exact"))
    current = {path: sha256(git_bytes(CURRENT_SHORE, path)).hexdigest() for path in CURRENT_PINS}
    causal_observed = {path: sha256(git_bytes(CAUSAL_SHORE, path)).hexdigest() for path in CAUSAL_PINS}
    current_receipts = {
        cycle: json.loads(git_bytes(CURRENT_SHORE, path)) for cycle, path in {
            "602": "outputs/physical_transported_observable_ramsey_echo_event_rotor_tournament_cycle602_receipt_2026_07_22.json",
            "610": "outputs/physical_intrinsic_tick_event_relational_duration_tournament_cycle610_receipt_2026_07_22.json",
            "668": "outputs/physical_detector_formation_current_interval_kernel_cycle668_receipt_2026_07_23.json",
            "669": "outputs/physical_state_carried_event_chain_sequence_protocol_cycle669_receipt_2026_07_23.json",
            "672": "outputs/physical_cycle608_literal_aggregate_detector_product_cycle672_receipt_2026_07_23.json",
            "675": "outputs/physical_occupancy_six_q_syndrome_extractor_cycle675_receipt_2026_07_23.json",
        }.items()
    }
    causal_receipts = {
        cycle: json.loads(git_bytes(CAUSAL_SHORE, path)) for cycle, path in {
            "675": "outputs/physical_branch_tracked_isolation_labeled_vernier_cycle675_receipt_2026_07_23.json",
            "676": "outputs/physical_synchronization_renewal_proper_time_law_tournament_cycle676_receipt_2026_07_23.json",
        }.items()
    }
    expected_current_pass = {"602": True, "610": False, "668": True, "669": True, "672": True, "675": True}
    observed_current_pass = {cycle: body["pass"] for cycle, body in current_receipts.items()}
    pass_flag = (
        target_line < prereg_line < evidence_line
        and digest(TARGET_CONTRACT) == TARGET_CONTRACT_SHA256
        and digest(PREREGISTRATION) == PREREGISTRATION_SHA256
        and current == CURRENT_PINS and causal_observed == CAUSAL_PINS
        and observed_current_pass == expected_current_pass
        and all(body["pass"] for body in causal_receipts.values())
    )
    result = {
        "current_shore": CURRENT_SHORE, "causal_shore": CAUSAL_SHORE,
        "target_sha256": digest(TARGET_CONTRACT), "expected_target_sha256": TARGET_CONTRACT_SHA256,
        "preregistration_sha256": digest(PREREGISTRATION),
        "expected_preregistration_sha256": PREREGISTRATION_SHA256,
        "target_line": target_line, "preregistration_line": prereg_line,
        "first_evidence_line": evidence_line, "frozen_before_evidence": target_line < prereg_line < evidence_line,
        "current_pins": CURRENT_PINS, "current_observed": current,
        "causal_pins": CAUSAL_PINS, "causal_observed": causal_observed,
        "current_receipt_pass_expected": expected_current_pass,
        "current_receipt_pass_observed": observed_current_pass,
        "Cycle610_nonpassing_shore_preserved_not_promoted": not current_receipts["610"]["pass"],
        "causal_receipts_pass": {cycle: body["pass"] for cycle, body in causal_receipts.items()},
        "working_tree_bytes_used_as_evidence": False, "pass": pass_flag,
    }
    check("Cycle680 target and both exact git-object shores were frozen before evidence", pass_flag,
          {"current_pins": len(CURRENT_PINS), "causal_pins": len(CAUSAL_PINS),
           "Cycle610_pass": current_receipts["610"]["pass"]})
    return result, current_receipts, causal_receipts


def actual_detector_clock_rows():
    specifications = {
        "train_L9_rest": (c610.L_TRAIN, c610.K_TRAIN_0, c610.BETA_TRAIN, c610.Q_TRAIN, "train"),
        "held_L13_rest": (c610.L_HELD, c610.K_TRAIN_0, c610.BETA_TRAIN, c610.Q_HELD, "held"),
        "held_L13_moving": (c610.L_HELD, c610.K_HELD, c610.BETA_TRAIN, c610.Q_HELD, "held"),
    }
    output = {}; private = {}; failures = 0
    for name, (length, momentum, beta, steps, split) in specifications.items():
        root = c610.bs_root(length, momentum, beta)
        state, eigen_residual = c610.bound_state(length, momentum, beta, root)
        run = c610.evolve_word(c610.free_stack(length, momentum, beta), state, steps, length=length)
        row = c610.clock_row(run["aggregate"], c610.Q_SKIP, "T1")
        events = tuple((int(label), int(orientation)) for label, orientation in row["events"])
        locked = bool(row["locked"] and eigen_residual < 1e-6 and len(events) >= 12
                      and run["norm_defect"] < 1e-9 and run["antisym_defect"] < 1e-9)
        failures += int(not locked)
        output[name] = {
            "split": split, "length": length, "detector_law_applications_not_time": steps,
            "event_count": len(events), "signed_count": sum(item[1] for item in events),
            "first_event_source_labels_not_decoder_inputs": [item[0] for item in events[:4]],
            "last_event_source_label_not_decoder_input": events[-1][0],
            "event_stream_sha256": digest(events), "lawful_domain_locked": bool(row["locked"]),
            "signed_tick_count_per_law_application_candidate": float(row["rate"]),
            "fine_lift_per_law_application_candidate": float(row["fine_rate"]),
            "bound_eigen_residual": float(eigen_residual), "norm_defect": float(run["norm_defect"]),
            "antisymmetry_defect": float(run["antisym_defect"]),
            "tick_certificate_called_occurrence": False,
            "strict_physical_M2_detector_compiler_attached": False,
            "pass": locked,
        }
        private[name] = events
    ratio = (output["held_L13_moving"]["fine_lift_per_law_application_candidate"]
             / output["held_L13_rest"]["fine_lift_per_law_application_candidate"])
    output["held_pair_ratio_relational_candidate"] = ratio
    passed = failures == 0 and len(private) == 3
    check("executed Cycle610 detector law regenerates one train and two held locked candidate-tick streams", passed,
          {name: row["event_count"] for name, row in output.items() if isinstance(row, dict)})
    return {"rows": output, "pass": passed}, private


def classify_input_surfaces(receipts):
    c602a = receipts["602"]["route_A_transported_observable"]
    c602c = receipts["602"]["route_C_reversible_one_hot_rotor"]
    c675s = receipts["675"]["aggregate_summary"]
    static_sizes = []
    for row in receipts["675"]["size_rows"]:
        first = row["cell_rows"][0]
        static_sizes.append({
            "length": row["length"], "split": row["split"], "selected_cells": row["selected_cell_count"],
            "global_radius_four_matter_rail_M2": row["global_radius_four_matter_rail_M2"],
            "placed_operand_M2_per_selected_cell": first["placement"]["placed_operand_M2"],
            "maximum_macro_support_M2": first["placement"]["maximum_macro_support"],
            "extractor_two_M2_factors": first["placement"]["extractor_two_M2_factors"],
            "detector_macro_factors": first["detector_factor_count"],
            "maximum_interface_residual": first["maximum_interface_residual"],
            "terminal_leakage_probability": first["maximum_terminal_leakage_probability"],
        })
    rows = {
        "Cycle602": {
            "executed_output": "finite transported/coarse detector phase words plus algebraic K4 rotor",
            "classification": "coarse N=2 observable and Boolean sidecar; not strict physical M2 detector or clock",
            "strict_physical_M2": False, "event_stream": False,
            "mass_residual": c602a["one_particle_mass_residual"],
            "contact_residual": c602a["Cycle230_contact_factorization_residual"],
            "seam_residual": c602a["held_axis_seam_translation_residual"],
            "rotor_physical_EG": c602c["physical_EG"],
        },
        "Cycle610": {
            "executed_output": "locked oriented tick certificates on regenerated purified train/held detector words",
            "classification": "candidate opportunities; overall committed receipt has 33 pass/3 fail and is not promoted",
            "shore_pass": receipts["610"]["pass"], "strict_physical_M2": False,
            "objective_occurrence": False,
        },
        "Cycle672": {
            "executed_output": "executed L3/L4/L6 origin aggregate detector macro on supplied q",
            "classification": "static detector macro; no physical matter-to-q encoder in that cycle and no tick stream",
            "strict_tick_stream": False, "supplied_q": True,
            "sizes": receipts["672"]["aggregate_summary"]["sizes"],
            "all24_all576_failures": receipts["672"]["aggregate_summary"]["all24_all576_failures"],
        },
        "Cycle675": {
            "executed_output": "bounded physical occupancy-to-q SWAP extractor plus local detector macro",
            "classification": "physical static detector snapshots on supplied matter rails; no autonomous trajectory/tick law",
            "static_size_rows": static_sizes,
            "signed_coordinate_only_covariance_failures": c675s["signed_coordinate_only_covariance_failures"],
            "closed_all24_all576_failures": (
                receipts["675"]["covariance"]["group_coordinate_failures"]
                + receipts["675"]["covariance"]["fermionic_wedge_group_law_failures"]
                + receipts["675"]["covariance"]["signed_local_phase_repaired_state_equivariance_failures"]),
            "incident_C_star_product_executed": c675s["incident_C_star_product_executed"],
            "same_unprogrammed_device": c675s["same_unprogrammed_all_cell_device_executed"],
            "strict_tick_stream": False,
        },
        "Cycle668": {
            "executed_output": "declared-code detector-to-formation/current/interval stochastic kernel",
            "classification": "objective only within supplied candidate law; no Cycle610 tick association or renewal",
            "target_terminal": receipts["668"]["target_contract_candidate_terminal_met"],
        },
        "Cycle669": {
            "executed_output": "physical support-two state-carried predecessor/current/packet overlay",
            "classification": "finite event-chain protocol; route enum has no native Cycle610 tick type and non-erasing renewal is open",
            "target_terminal": receipts["669"]["target_contract_candidate_terminal_met"],
            "all24_tests": receipts["669"]["locality_resources"]["append_all24_tests"],
            "all576_tests": receipts["669"]["locality_resources"]["all576_direction_tests"],
        },
    }
    passed = (set(row["length"] for row in static_sizes) == {3, 4, 6}
              and c602a["one_particle_mass_residual"] < TOL
              and c602a["Cycle230_contact_factorization_residual"] < TOL
              and c602a["held_axis_seam_translation_residual"] < TOL
              and c675s["signed_coordinate_only_covariance_failures"] == 48)
    check("Cycle602/610/672/675/668/669 outputs are classified without promoting static or coarse surfaces to clocks", passed,
          {name: row["classification"] for name, row in rows.items()})
    return {"rows": rows, "pass": passed}


def onehot(index, width):
    if type(index) is not int or index not in range(width): raise ValueError("onehot")
    return tuple(int(site == index) for site in range(width))


def one_index(word):
    if not word or any(type(bit) is not int or bit not in (0, 1) for bit in word) or sum(word) != 1:
        raise ValueError("onehot code")
    return word.index(1)


def rotor_step(source, opportunity, delete=None):
    source_index = one_index(source)
    target = [0] * 16; carry = 0
    if opportunity not in (0, 1): raise ValueError("opportunity")
    for rail, bit in enumerate(source):
        if delete != ("copy", rail): target[rail] ^= opportunity & bit
    if delete != ("carry", 15): carry ^= opportunity & source[15]
    if opportunity and delete != ("rotate", 0):
        target = [target[-1], *target[:-1]]
    return tuple(target), carry


def inverse_rotor_step(source, target, carry, opportunity, delete=None):
    target = list(target)
    if opportunity and delete != ("rotate", 0): target = [*target[1:], target[0]]
    expected_carry = opportunity & source[15] if delete != ("carry", 15) else 0
    if carry != expected_carry: raise ValueError("carry code")
    for rail, bit in enumerate(source):
        if delete != ("copy", rail): target[rail] ^= opportunity & bit
    return tuple(target), 0


@dataclass(frozen=True)
class BridgeNode:
    identity: tuple[int, ...]
    predecessor: tuple[int, ...]
    rotor: tuple[int, ...]
    carry_receipt: int
    binder: int
    valid: int
    orientation: int
    edge_packet: tuple[tuple[int, ...], ...]
    source_clock: str
    source_label_exhaust: int


@dataclass(frozen=True)
class BridgeChain:
    root: tuple[int, ...]
    nodes: tuple[BridgeNode, ...]
    marks: dict[str, tuple[int, ...]]
    bank_capacity: int
    refills_used: int
    refill_after_nodes: tuple[int, ...]
    statuses: tuple[str, ...]


def build_bridge(events, mark_keys, *, bank_capacity=6, refill_enabled=True, initial_rotor=12):
    width = len(events) + 2; root = onehot(0, width); predecessor = root
    rotor = onehot(initial_rotor, 16); nodes = []; statuses = []; refills = []; active_bank = 0
    packet = c669.local_edge_packet()
    if c669.c665.packet_read(packet) is None: raise ValueError("edge packet")
    marks = {}
    for source_clock, source_label, orientation in events:
        if len(nodes) == (active_bank + 1) * bank_capacity:
            if not refill_enabled:
                statuses.append("exhausted_refill_required"); break
            active_bank += 1; refills.append(len(nodes)); statuses.append("refill_token_consumed")
        target, carry = rotor_step(rotor, 1)
        identity = onehot(len(nodes) + 1, width)
        node = BridgeNode(identity, predecessor, target, carry, 1, 1, orientation, packet,
                          source_clock, source_label)
        nodes.append(node); predecessor = identity; rotor = target; statuses.append("accepted_supplied_actuality")
        for tag, key in mark_keys.items():
            if key == (source_clock, source_label): marks[tag] = identity
    return BridgeChain(root, tuple(nodes), marks, bank_capacity, len(refills), tuple(refills), tuple(statuses))


def decode_physical_interval(chain, tag_a, tag_b):
    if tag_a not in chain.marks or tag_b not in chain.marks: return None
    nodes = {node.identity: node for node in chain.nodes}

    def directed(first, second):
        cursor = second; path = []
        while cursor != first:
            node = nodes.get(cursor)
            if node is None or node.binder != 1 or node.valid != 1:
                return None
            try: one_index(node.rotor)
            except ValueError: return None
            if c669.c665.packet_read(node.edge_packet) is None: return None
            path.append(node); cursor = node.predecessor
        if first == chain.root:
            start_rotor = 0
        else:
            start_node = nodes.get(first)
            if start_node is None: return None
            try: start_rotor = one_index(start_node.rotor)
            except ValueError: return None
        end_node = nodes.get(second)
        if end_node is None: return None
        return 16 * sum(node.carry_receipt for node in path) + one_index(end_node.rotor) - start_rotor

    forward = directed(chain.marks[tag_a], chain.marks[tag_b])
    if forward is not None: return forward
    backward = directed(chain.marks[tag_b], chain.marks[tag_a])
    return None if backward is None else -backward


class CausalView:
    def __init__(self, cells, marks): self.cells = cells; self.marks = marks


def causal_view(chain):
    cells = []; by_identity = {chain.root: None}; cumulative_carries = 0
    tag_by_identity = {identity: tag for tag, identity in chain.marks.items()}
    marks = {}
    for node in chain.nodes:
        cumulative_carries += node.carry_receipt
        predecessor = by_identity.get(node.predecessor)
        state_carried_address = one_index(node.identity) - 1
        cell = causal.Cell(state_carried_address, predecessor, one_index(node.rotor), cumulative_carries, -1,
                           tag_by_identity.get(node.identity, "tick"), None)
        cells.append(cell); by_identity[node.identity] = cell
        if node.identity in tag_by_identity: marks[tag_by_identity[node.identity]] = state_carried_address
    return CausalView(cells, marks)


def bank_and_decoder_controls(clock_events):
    train = clock_events["train_L9_rest"][:12]
    normalized = tuple(("train_L9_rest", label, orientation) for label, orientation in train)
    mark_keys = {tag: ("train_L9_rest", train[index][0])
                 for tag, index in PREREGISTRATION["renewal"]["mark_event_indices"].items()}
    renewed = build_bridge(normalized, mark_keys, refill_enabled=True)
    preenabled = build_bridge(normalized, mark_keys, bank_capacity=12, refill_enabled=True)
    view_new = causal_view(renewed); view_control = causal_view(preenabled)
    pairs = (("S1", "S2"), ("S2", "S3"), ("S3", "S4"), ("S1", "S3"), ("S2", "S4"), ("S1", "S4"))
    physical_causal_failures = 0
    for pair in pairs:
        physical_causal_failures += int(decode_physical_interval(renewed, *pair) != causal.decode_interval(view_new, *pair))
    intervals_equal = all(causal.decode_interval(view_new, *pair) == causal.decode_interval(view_control, *pair)
                          for pair in pairs)
    ratios_equal = all(causal.ratio(view_new, view_control, *pair) == causal.ratio(view_control, view_control, *pair)
                       for pair in pairs)
    refill_inside = (renewed.refill_after_nodes == (6,) and renewed.refills_used == 1
                     and one_index(renewed.marks["S2"]) < 7 < one_index(renewed.marks["S3"]))
    carry_nodes = [index for index, node in enumerate(renewed.nodes) if node.carry_receipt]

    reversed_chain = build_bridge(tuple(reversed(normalized)), mark_keys, bank_capacity=12, refill_enabled=True)
    reverse_view = causal_view(reversed_chain)
    reversal_pass = all(causal.decode_interval(reverse_view, *pair) == -causal.decode_interval(view_new, *pair)
                        for pair in pairs)

    held = tuple(("held_L13_rest", label, orientation) for label, orientation in clock_events["held_L13_rest"][:6])
    piece_events = normalized[:6] + held
    piece_marks = {
        "P0": (piece_events[0][0], piece_events[0][1]),
        "PS": (piece_events[5][0], piece_events[5][1]),
        "PE": (piece_events[-1][0], piece_events[-1][1]),
    }
    piece = build_bridge(piece_events, piece_marks, refill_enabled=True)
    piece_view = causal_view(piece)
    first = causal.decode_interval(piece_view, "P0", "PS")
    second = causal.decode_interval(piece_view, "PS", "PE")
    total = causal.decode_interval(piece_view, "P0", "PE")
    piecewise_additive = first is not None and second is not None and total == first + second

    link_deleted_nodes = list(renewed.nodes); link_deleted_nodes[6] = replace(link_deleted_nodes[6], predecessor=renewed.root)
    link_deleted = replace(renewed, nodes=tuple(link_deleted_nodes))
    missing_undefined = decode_physical_interval(link_deleted, "S1", "S4") is None
    carry_deleted_nodes = list(renewed.nodes)
    wrap_index = carry_nodes[0]
    carry_deleted_nodes[wrap_index] = replace(carry_deleted_nodes[wrap_index], carry_receipt=0)
    carry_deleted = replace(renewed, nodes=tuple(carry_deleted_nodes))
    carry_deletion_signal = abs(decode_physical_interval(renewed, "S1", "S4")
                                - decode_physical_interval(carry_deleted, "S1", "S4"))
    refill_deleted = build_bridge(normalized, mark_keys, refill_enabled=False)
    refill_deletion_visible = (len(refill_deleted.nodes) == 6
                               and decode_physical_interval(refill_deleted, "S1", "S4") is None)
    binder_nodes = list(renewed.nodes); binder_nodes[7] = replace(binder_nodes[7], binder=0)
    binder_deleted = replace(renewed, nodes=tuple(binder_nodes))
    binder_deletion_visible = decode_physical_interval(binder_deleted, "S1", "S4") is None

    rotor_failures = inverse_failures = deletion_detected = 0
    for index in range(16):
        for opportunity in (0, 1):
            source = onehot(index, 16); target, carry = rotor_step(source, opportunity)
            if opportunity:
                rotor_failures += int(one_index(target) != (index + 1) % 16 or carry != int(index == 15))
            else:
                rotor_failures += int(sum(target) != 0 or carry != 0)
            inverse, clean = inverse_rotor_step(source, target, carry, opportunity)
            inverse_failures += int(inverse != (0,) * 16 or clean != 0)
    malformed_rejections = 0
    for word in ((0,) * 16, (1,) * 16, (2,) + (0,) * 15):
        try: rotor_step(word, 1)
        except ValueError: malformed_rejections += 1
    deleted_target, _ = rotor_step(onehot(3, 16), 1, delete=("copy", 3))
    deleted_carry = rotor_step(onehot(15, 16), 1, delete=("carry", 15))[1]
    deleted_rotate = rotor_step(onehot(3, 16), 1, delete=("rotate", 0))[0]
    deletion_detected += int(sum(deleted_target) != 1)
    deletion_detected += int(deleted_carry != 1)
    deletion_detected += int(one_index(deleted_rotate) != 4)

    jo = causal.JointOrder(["A", "B", "C"])
    for index in range(2):
        for device in ("A", "B", "C"): jo.admit_local(device, ("detector", index))
    admitted = tuple(jo.admit_shared(tag) for tag in ("S1", "S2", "S3", "S4"))
    adversary = causal.JointOrder(["A", "B", "C"])
    for index in range(4):
        for device in ("A", "B", "C"): adversary.admit_local(device, ("detector", index))
    first_shared = adversary.admit_shared("S1")
    adversary.force_shared("Sx", {"A": 1, "B": 9, "C": 1})
    inverted_refusal = adversary.admit_shared("S2")

    decoder_source = inspect.getsource(decode_physical_interval)
    causal_path = "scripts/physical_synchronization_renewal_proper_time_law_tournament_cycle676_2026_07_23.py"
    causal_source = (git_function_source(CAUSAL_SHORE, causal_path, "decode_position")
                     + git_function_source(CAUSAL_SHORE, causal_path, "decode_interval"))
    forbidden = ("source_label_exhaust", "loop_ordinal", "s_debug", "law_applications", "shared_parameter")
    decoder_hits = tuple(token for token in forbidden if token in decoder_source or token in causal_source)
    causal_state_carried_address_reads = causal_source.count(".index")
    signatures = {
        "physical": tuple(inspect.signature(decode_physical_interval).parameters),
        "causal_position": tuple(inspect.signature(causal.decode_position).parameters),
        "causal_interval": tuple(inspect.signature(causal.decode_interval).parameters),
    }

    assertions = [
        {"causal_row": 1, "name": "rate_constancy", "status": "UNRUN_PHYSICAL",
         "reason": "no physical shared co-registration apparatus joins two independent regenerated detector streams; ideal nu/s generator forbidden"},
        {"causal_row": 2, "name": "ratio_transitivity", "status": "UNRUN_PHYSICAL",
         "reason": "requires the same absent three-clock physical co-registration surface"},
        {"causal_row": 3, "name": "offset_prediction", "status": "UNRUN_PHYSICAL",
         "reason": "requires a physical calibration pair and shared event marks, not host-selected addresses"},
        {"causal_row": 4, "name": "renewal_invariance", "status": "CONDITIONAL_INTERFACE_PASS",
         "pass": intervals_equal and ratios_equal and refill_inside and bool(carry_nodes),
         "qualification": "regenerated detector-law tick certificates and physical carry/refill overlay; co-registration mark packets supplied"},
        {"causal_row": 5, "name": "reversal", "status": "CONDITIONAL_INTERFACE_PASS", "pass": reversal_pass,
         "qualification": "reversed accepted detector-event stream; mark packets supplied"},
        {"causal_row": 6, "name": "piecewise_additivity", "status": "CONDITIONAL_INTERFACE_PASS",
         "pass": piecewise_additive,
         "qualification": "count additivity only; physical switch and endpoint marks supplied; nu/s floor prediction not run"},
        {"causal_row": 7, "name": "missing_shared_event", "status": "CONDITIONAL_INTERFACE_PASS",
         "pass": missing_undefined, "qualification": "predecessor-link deletion on physical bridge"},
        {"causal_row": 8, "name": "inverted_coregistration", "status": "CONDITIONAL_INTERFACE_PASS",
         "pass": admitted == ("admitted",) * 4 and first_shared == "admitted" and inverted_refusal == "refused_inverted",
         "qualification": "unchanged causal JointOrder on state-carried positions; physical mark genesis supplied"},
        {"causal_row": 9, "name": "no_ordinal_or_s_decoder", "status": "PASS",
         "pass": not decoder_hits, "qualification": "unchanged causal decoder plus Cycle680 physical decoder source audit"},
    ]
    conditional_pass = all(row.get("pass", True) for row in assertions)
    resources = {
        "banks": 2, "capacity_per_bank": 6, "accepted_nodes": 12,
        "frozen_Cycle669_capacity6_overlay_M2_per_bank": 179,
        "two_Cycle669_overlay_M2": 358,
        "K16_root_and_per_node_rotor_carry_binder_valid_M2": 16 + 12 * 19,
        "cross_bank_global_identity_predecessor_M2": 2 * 14,
        "refill_token_M2": 1,
        "Cycle680_adapter_overlay_M2": 358 + (16 + 12 * 19) + 28 + 1,
        "logical_maximum_support_M2": 3, "lowered_maximum_support_M2": 2,
        "rotor_step_logical_factors_per_node": {"TOFFOLI": 17, "FREDKIN": 15},
        "new_rotor_placement": "node n rotor rail r at (n, r mod 4, floor(r/4)); adjacent bank blocks share a boundary",
        "maximum_within_rotor_route_edges": 6,
        "constant_overlay_per_node_M2": 19,
        "strict_end_to_end_detector_plus_adapter_M2": None,
        "why_total_is_null": "the Cycle610/Cycle602 tick detector has no strict physical M2 compiler; Cycle675 static detector has no trajectory-to-tick association",
    }
    result = {
        "executed_tick_certificates_consumed": len(normalized), "supplied_actuality_admissibility_law_domain": True,
        "native_Cycle669_Cycle610_route_tag_present": False,
        "Cycle669_packet_replicas_per_node": len(renewed.nodes[0].edge_packet),
        "refills_used": renewed.refills_used, "refill_after_nodes": renewed.refill_after_nodes,
        "carry_receipt_node_indices": carry_nodes, "physical_to_unchanged_causal_decoder_failures": physical_causal_failures,
        "renewal_intervals_equal": intervals_equal, "renewal_ratios_equal": ratios_equal,
        "reversal_intervals_negate": reversal_pass,
        "piecewise_count_rows": {"first": first, "second": second, "total": total, "additive": piecewise_additive,
                                  "called_proper_time": False},
        "deletion_controls": {
            "carry_receipt_deletion_signal": carry_deletion_signal,
            "refill_token_deletion_visible": refill_deletion_visible,
            "cross_bank_predecessor_deletion_undefined": missing_undefined,
            "binder_deletion_undefined": binder_deletion_visible,
            "rotor_factor_deletions_detected": deletion_detected,
        },
        "rotor_basis_tests": 32, "rotor_basis_failures": rotor_failures,
        "rotor_inverse_failures": inverse_failures, "rotor_malformed_rejections": malformed_rejections,
        "decoder_signatures": signatures, "decoder_forbidden_source_hits": decoder_hits,
        "causal_Cell_index_reads": causal_state_carried_address_reads,
        "causal_Cell_index_is_physical_onehot_address_not_loop_or_update_ordinal": True,
        "causal_acceptance_assertions": assertions, "resources": resources,
        "conditional_interface_pass": conditional_pass,
    }
    result["pass"] = (conditional_pass and physical_causal_failures == rotor_failures == inverse_failures == 0
                      and malformed_rejections == 3 and deletion_detected == 3
                      and carry_deletion_signal == 16 and refill_deletion_visible and binder_deletion_visible)
    check("bounded M2 carry/refill overlay feeds unchanged causal decoders on every semantically runnable row", result["pass"],
          {"conditional_rows": sum(row.get("pass") is True for row in assertions),
           "unrun_physical": sum(row["status"] == "UNRUN_PHYSICAL" for row in assertions),
           "carry_deletion": carry_deletion_signal})
    return result


def covariance_controls():
    frames = c610.c210.proper_cubic_frames(); directions = tuple(map(tuple, c610.c210.DIRECTIONS))
    failures24 = failures576 = rotor_failures = 0
    permutations = []
    for frame in frames:
        permutation = tuple(directions.index(tuple(frame @ np.asarray(direction))) for direction in directions)
        permutations.append(permutation)
        for direction in range(6):
            failures24 += int(permutation[direction] not in range(6))
        for rotor in range(16):
            moved, carry = rotor_step(onehot(rotor, 16), 1)
            rotor_failures += int(one_index(moved) != (rotor + 1) % 16 or carry != int(rotor == 15))
    for first, second in product(range(24), repeat=2):
        composed = c610.c210.proper_cubic_frames()[first] @ c610.c210.proper_cubic_frames()[second]
        expected = tuple(directions.index(tuple(composed @ np.asarray(direction))) for direction in directions)
        observed = tuple(permutations[first][permutations[second][direction]] for direction in range(6))
        failures576 += int(observed != expected)
    c669_receipt = json.loads(git_bytes(CURRENT_SHORE,
        "outputs/physical_state_carried_event_chain_sequence_protocol_cycle669_receipt_2026_07_23.json"))
    c675_receipt = json.loads(git_bytes(CURRENT_SHORE,
        "outputs/physical_occupancy_six_q_syndrome_extractor_cycle675_receipt_2026_07_23.json"))
    result = {
        "proper_cubic_frames": len(frames), "Cycle680_direction_all24_tests": 24 * 6,
        "Cycle680_direction_all24_failures": failures24,
        "Cycle680_direction_all576_tests": 576 * 6,
        "Cycle680_direction_all576_failures": failures576,
        "scalar_K16_rotor_frame_tests": 24 * 16, "scalar_K16_rotor_frame_failures": rotor_failures,
        "Cycle669_append_all24_tests": c669_receipt["locality_resources"]["append_all24_tests"],
        "Cycle669_append_all24_failures": c669_receipt["locality_resources"]["append_all24_failures"],
        "Cycle669_all576_tests": c669_receipt["locality_resources"]["all576_direction_tests"],
        "Cycle669_all576_failures": c669_receipt["locality_resources"]["all576_direction_failures"],
        "Cycle675_signed_coordinate_only_failures_preserved": c675_receipt["aggregate_summary"]["signed_coordinate_only_covariance_failures"],
        "Cycle675_bounded_local_CZ_sheath_closed": c675_receipt["aggregate_summary"]["bounded_local_fermionic_phase_repair_executed"],
        "compile_time_orientation_axis_chart_supplied": True, "runtime_frame_selector": False,
    }
    result["pass"] = (failures24 == failures576 == rotor_failures == 0
                      and result["Cycle669_append_all24_failures"] == result["Cycle669_all576_failures"] == 0
                      and result["Cycle675_signed_coordinate_only_failures_preserved"] == 48)
    check("new scalar carry overlay and direction provenance preserve the exact all24/all576 boundaries", result["pass"],
          {"new_failures": [failures24, failures576, rotor_failures], "raw_Cycle675": 48})
    return result


def no_go_discipline():
    c610tick = citation(CURRENT_SHORE,
        "docs/work_history/repo/review_feedback/PHYSICAL_INTRINSIC_TICK_EVENT_RELATIONAL_DURATION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md",
        "A tick certificate is a candidate opportunity, not an occurrence.")
    c602physical = citation(CURRENT_SHORE,
        "docs/work_history/repo/review_feedback/PHYSICAL_TRANSPORTED_OBSERVABLE_RAMSEY_ECHO_EVENT_ROTOR_TOURNAMENT_CYCLE602_NOTE_2026-07-22.md",
        "not a physical M2 update")
    c675device = citation(CURRENT_SHORE,
        "docs/work_history/repo/review_feedback/PHYSICAL_OCCUPANCY_SIX_Q_SYNDROME_EXTRACTOR_CYCLE675_NOTE_2026-07-23.md",
        "not promoted to a same unprogrammed all-cell device")
    c672detector = citation(CURRENT_SHORE,
        "docs/work_history/repo/review_feedback/PHYSICAL_CYCLE608_LITERAL_AGGREGATE_DETECTOR_PRODUCT_CYCLE672_NOTE_2026-07-23.md",
        "This is a bounded partial construction, not a physical matter detector.")
    c669renew = citation(CURRENT_SHORE,
        "docs/work_history/repo/review_feedback/PHYSICAL_STATE_CARRIED_EVENT_CHAIN_SEQUENCE_PROTOCOL_CYCLE669_NOTE_2026-07-23.md",
        "indefinite non-erasing renewal remains open")
    causalboundary = citation(CAUSAL_SHORE,
        "docs/work_history/repo/review_feedback/PHYSICAL_SYNCHRONIZATION_RENEWAL_PROPER_TIME_LAW_TOURNAMENT_CYCLE676_NOTE_2026-07-23.md",
        "generator parameter s is bookkeeping, not time")
    routes = [
        {"family": "Cycle610 transported detector tick certificates", "honesty": "ATTEMPTED",
         "object": "actual regenerated train/held detector words", "terminal": "physical objective clock stream",
         "status": "positive locked candidate ticks; physical detector and objective admission absent", "authority": c610tick},
        {"family": "Cycle602 transported observable and K4 rotor", "honesty": "RULED OUT BY PRIOR",
         "object": "coarse N=2 array plus Boolean sidecar", "terminal": "strict physical detector/clock",
         "status": "positive coarse result explicitly not physical M2", "authority": c602physical},
        {"family": "Cycle672 supplied-q detector macro", "honesty": "RULED OUT BY PRIOR",
         "object": "physical macro on supplied q", "terminal": "material tick stream",
         "status": "static supplied-q detector; no matter-to-q or stream in that cycle", "authority": c672detector},
        {"family": "Cycle675 occupancy-to-q detector", "honesty": "ATTEMPTED",
         "object": "physical L3/L4/L6 static detector snapshots", "terminal": "autonomous moving clock and generic device",
         "status": "positive bounded snapshot; no trajectory/tick association", "authority": c675device},
        {"family": "Cycle668/669 objective formation and predecessor chain", "honesty": "ATTEMPTED",
         "object": "supplied-law event and finite physical packet chain", "terminal": "native Cycle610 acceptance and renewal",
         "status": "finite protocol positive; Cycle610 route type and non-erasing renewal absent", "authority": c669renew},
        {"family": "causal Cycle676 ideal event-stream harness", "honesty": "RULED OUT BY PRIOR",
         "object": "nu/s-generated law-level chains", "terminal": "physical apparatus acceptance",
         "status": "nine law assertions pass but s is not physical and must not be replayed here", "authority": causalboundary},
        {"family": "Cycle680 two-bank K16 carry adapter", "honesty": "ATTEMPTED",
         "object": "regenerated tick certificates plus physical packet/rotor/carry overlay", "terminal": "all causal assertions",
         "status": "renewal/reversal/additivity/refusal decoder interface passes conditionally; sync rows unrun", "authority": c610tick},
        {"family": "matter-generated dual clock and co-registration apparatus", "honesty": "OPEN_NOT_COUNTED",
         "object": "two physical detectors coupled by local shared events", "terminal": "unchanged rate/offset assertions",
         "status": "not attempted", "authority": c675device},
    ]
    walls = {
        "W_tick_source_physical_M2": "Cycle610 ticks are actual coarse/fiber detector outputs but their detector compiler is not strict physical M2",
        "W_objective_admission": "tick certificate is a candidate opportunity; actuality/admissibility/law-domain are supplied",
        "W_shared_coregistration": "no physical interaction emits common marks for two independent clocks",
        "W_renewal_genesis": "the refill token and fresh blank bank are supplied",
        "W_duration_identification": "decoded count/ratio is only a relational duration candidate until causal identification and apparatus attach",
    }
    pairs = []
    names = tuple(walls)
    for left in names:
        for right in names:
            if left != right:
                pairs.append({"from": left, "to": right, "implied": False,
                              "reason": "distinct source, admission, co-registration, renewal or identification obligation"})
    hidden = [
        {"condition": "purified Cycle610 source", "classification": "supplied state preparation"},
        {"condition": "actuality/admissibility/law-domain", "classification": "supplied acceptance bits"},
        {"condition": "S1-S4 mark packets", "classification": "supplied co-registration; decoder does not read source labels"},
        {"condition": "blank second bank/refill token", "classification": "supplied finite renewal resource"},
        {"condition": "orientation-to-axis chart", "classification": "compile-time chart; all24 transported"},
        {"condition": "strong causal identification", "classification": "not attached; no output called proper time"},
    ]
    residuals = [
        {"prior": c610tick, "prior_residual": "tick certificate is not occurrence",
         "current": "Cycle680 supplies acceptance bits", "exact_match": True},
        {"prior": c602physical, "prior_residual": "coarse detector is not strict physical M2",
         "current": "end-to-end M2 total remains null", "exact_match": True},
        {"prior": c669renew, "prior_residual": "non-erasing renewal open",
         "current": "one finite supplied refill passes; autonomous indefinite renewal not claimed", "exact_match": True},
        {"prior": causalboundary, "prior_residual": "s is bookkeeping",
         "current": "Cycle680 never calls ideal generator", "exact_match": True},
    ]
    rhetoric = [
        {"claim": "detector tick certificate is not occurrence", "per_element": "one oriented crossing",
         "per_site": "detector output register", "per_mode": "train/held", "per_block": "L9/L13",
         "lattice_wide": "objective admission remains supplied"},
        {"claim": "decoded count is not proper time", "per_element": "K16 carry receipt", "per_site": "one bridge node",
         "per_mode": "forward/reversed", "per_block": "two capacity-six banks", "lattice_wide": "identification law absent"},
        {"claim": "static physical detector is not a clock stream", "per_element": "one occupancy-to-q snapshot",
         "per_site": "61 placed operands", "per_mode": "five detector profiles", "per_block": "L3/L4/L6",
         "lattice_wide": "matter trajectory and common marks absent"},
        {"claim": "finite supplied refill is not autonomous renewal", "per_element": "one refill token",
         "per_site": "adjacent bank boundary", "per_mode": "one K16 wrap", "per_block": "12 nodes",
         "lattice_wide": "indefinite blank genesis unclaimed"},
    ]
    partial = [
        {"path": "Cycle680 executed Cycle610 rerun", "status": "EXECUTED_PARTIAL", "closes": "regenerated tick-certificate input to causal decoder"},
        {"path": "Cycle680 K16 carry overlay", "status": "EXECUTED_CONDITIONAL", "closes": "one finite refill and persistent carry"},
        {"path": "Cycle675 physical detector snapshots", "status": "EXECUTED_PRIOR", "closes": "occupancy-to-q static detector"},
        {"path": "dual physical clock/co-registration apparatus", "status": "OPEN", "closes": "causal rows 1-3"},
        {"path": "autonomous blank-bank genesis", "status": "OPEN", "closes": "indefinite renewal"},
    ]
    steelman = (
        "Construct two local Cycle675 detector cells on independently moving Cycle230 matter histories, derive their "
        "successive physical occupancy words from the same M2 law, convert each detector opportunity into objective "
        "admission without a supplied bit, and create S1-S4 only when a bounded local rendezvous interaction emits the "
        "same protected packet into both Cycle669 chains. Add a local blank-bank factory whose output carries the prior "
        "terminal predecessor and K16 receipt. Then rerun causal rows 1-9 unchanged with no source-label or host mark map."
    )
    echoes = [
        {"cycle": 602, "retired": "finite detector phase word", "remaining": "physical detector"},
        {"cycle": 610, "retired": "oriented candidate ticks and additive chain", "remaining": "objective physical acceptance"},
        {"cycle": 668, "retired": "declared-code objective formation/current packet", "remaining": "tick association and renewal"},
        {"cycle": 669, "retired": "finite physical predecessor overlay", "remaining": "native Cycle610 type and non-erasing renewal"},
        {"cycle": 675, "retired": "physical static occupancy detector", "remaining": "trajectory and same-device apparatus"},
        {"cycle": 676, "retired": "law-level causal acceptance assertions", "remaining": "physical source and identification"},
        {"cycle": 680, "retired": "finite conditional acceptance adapter", "remaining": "physical sync rows 1-3"},
    ]
    qualifying = sum(row["honesty"] in ("ATTEMPTED", "RULED OUT BY PRIOR") for row in routes)
    result = {
        "skill_freshness": {"origin_main_checked": True, "origin_main_advanced": False,
                            "origin_main": "e42c5ec242a9b6eccde20af62692940fcf6c11f5", "remote_skill_followed": True},
        "N1_routes": routes, "N1_qualifying_normalized_families": qualifying,
        "N2_walls": walls, "N2_directed_pairwise_table": pairs,
        "N3_hidden_wall_scan": hidden, "N4_residual_matches": residuals,
        "N5_rhetoric": rhetoric, "N6_partial_closure_paths": partial,
        "N6_primitive_registry_claim_made": False, "N7_steelman": steelman,
        "N8_cross_cycle_echo": echoes,
        "negative_claim_gate_status": "FAIL_DO_NOT_SHIP_NEGATIVE",
        "negative_gate_failure_reason": "N7 physical dual-clock/co-registration and autonomous renewal constructions remain open",
        "broad_no_go_claim": False, "minimum_content_claim": False,
        "shared_route_independent_obstruction": False, "axiom_pressure": False,
    }
    result["pass"] = (qualifying >= 5 and len(pairs) == len(names) * (len(names) - 1)
                      and all(row["exact_match"] for row in residuals)
                      and not result["broad_no_go_claim"] and not result["axiom_pressure"])
    check("fresh N1-N8 prevents physical-acceptance incompleteness from becoming a no-go or axiom claim", result["pass"],
          {"families": qualifying, "walls": len(walls), "negative_gate": result["negative_claim_gate_status"]})
    return result


def supplied_inventory():
    return {
        "supplied": [
            "Cycle610 purified train/held preparations and candidate-tick law", "actuality/admissibility/law-domain bits",
            "S1-S4 co-registration mark packets", "two finite blank capacity-six banks and one refill token",
            "K16 root rotor state 12", "Cycle669 root/address seeds and preprovisioned Cycle612/Cycle665 packets",
            "compile-time orientation axis/frame chart", "causal Cycle676 decoder and JointOrder theorem machinery",
        ],
        "derived": [
            "three regenerated detector-law tick-certificate streams", "bounded reversible K16 node transition", "one persistent wrap receipt",
            "one finite cross-bank predecessor link", "unchanged causal decoder equality", "renewal/reversal/count-additivity",
            "missing/inverted/no-source-label refusal", "all24/all576 scalar/direction covariance",
        ],
        "open": [
            "strict physical M2 implementation of the Cycle610 detector", "native Cycle610 route type in Cycle669",
            "objective tick admission law", "physical dual-clock shared co-registration apparatus",
            "autonomous blank-bank genesis and indefinite non-erasing renewal", "causal proper-duration identification law",
            "framework Record", "physical time/rate/energy", "gravity/source",
        ],
    }


def ideal_generator_call_audit():
    tree = ast.parse(Path(__file__).read_text()); forbidden = {
        "constant_tick_s", "piecewise_tick_s", "order_events", "build_chain",
    }
    hits = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Attribute): continue
        if isinstance(node.func.value, ast.Name) and node.func.value.id == "causal" and node.func.attr in forbidden:
            hits.append(node.func.attr)
    result = {"forbidden_causal_generator_calls": tuple(sorted(hits)),
              "causal_ideal_nu_s_generator_called": bool(hits), "pass": not hits}
    check("Cycle680 source contains no call to the causal ideal nu/s event generator", result["pass"], hits)
    return result


def note_text(receipt):
    clocks = receipt["actual_detector_clocks"]["rows"]
    classifications = receipt["input_surface_classification"]["rows"]
    assertions = receipt["bank_and_causal_decoder"]["causal_acceptance_assertions"]
    ng = receipt["no_go_discipline"]
    clock_rows = "\n".join(
        f"| {name} | {row['split']} | {row['length']} | {row['event_count']} | {row['event_stream_sha256']} | {row['lawful_domain_locked']} |"
        for name, row in clocks.items() if isinstance(row, dict)
    )
    class_rows = "\n".join(
        f"| {name} | {row['executed_output']} | {row['classification']} |" for name, row in classifications.items()
    )
    assertion_rows = "\n".join(
        f"| {row['causal_row']} | {row['name']} | {row['status']} | {row.get('pass', 'not run')} | {row.get('qualification', row.get('reason'))} |"
        for row in assertions
    )
    n1 = "\n".join(
        f"| {row['family']} | {row['object']} | {row['terminal']} | {row['honesty']} | {row['status']} | `{row['authority']['path']}:{row['authority']['line']}` |"
        for row in ng["N1_routes"]
    )
    n4 = "\n".join(
        f"| `{row['prior']['path']}:{row['prior']['line']}` | {row['prior_residual']} | {row['current']} | {row['exact_match']} |"
        for row in ng["N4_residual_matches"]
    )
    n6 = "\n".join(f"| {row['path']} | {row['status']} | {row['closes']} |" for row in ng["N6_partial_closure_paths"])
    return f"""# Detector-tick causal acceptance bridge — Cycle 680

Authority: **none**

Audit: **unset**

## Frozen shores and scope

The target `{receipt['frozen_shores']['target_sha256']}` and preregistration `{receipt['frozen_shores']['preregistration_sha256']}` precede all evidence. Current shore `{CURRENT_SHORE}` contributes `{len(CURRENT_PINS)}` exact runner/note/receipt objects; causal shore `{CAUSAL_SHORE}` contributes `{len(CAUSAL_PINS)}` exact Cycle675/676 objects. Nothing was cherry-picked and the causal PR was not edited.

Cycle610's committed receipt is deliberately preserved as nonpassing. Cycle680 regenerates only the preregistered purified detector rows and does not back-credit the full Cycle610 tournament.

Terminology firewall: the frozen target's adjective `actual` means executed/regenerated output bytes, never objective actuality. The result prose uses “regenerated tick certificate”; `actuality` is reserved for the explicitly supplied objective-admission bit.

## Executed detector/tick-certificate inputs

| clock | split | lattice | candidate ticks | stream SHA256 | locked? |
|---|---|---:|---:|---|---:|
{clock_rows}

These are regenerated Cycle610 detector-law crossing outputs, not samples from causal Cycle676's ideal `nu/s` generator. Their source labels remain provenance exhaust and never enter either decoder. A tick certificate remains a candidate opportunity, not an occurrence. The bridge supplies actuality, admissibility and law-domain bits and says so.

| surface | executed output | honest classification |
|---|---|---|
{class_rows}

The Cycle675 physical snapshot rows cover L3 train, L4 held-out and L6 held with 61 placed operands per selected cell, 18 NN extractor factors, maximum macro support eight and zero terminal leakage. Coordinate-only transport still has the exact 48/72 failure boundary; the bounded local fermionic CZ sheath supplies the closed all24/all576 result. A static snapshot sequence is not silently promoted to a clock.

The adapter does not touch the matter law. Frozen Cycle602 residuals remain mass `{classifications['Cycle602']['mass_residual']:.3e}`, contact `{classifications['Cycle602']['contact_residual']:.3e}`, seam `{classifications['Cycle602']['seam_residual']:.3e}`.

## Bounded carry/refill adapter

Two capacity-six Cycle669 overlays are joined by one explicit refill token and one protected predecessor link. Each accepted node adds a 16-rail one-hot rotor, persistent carry bit, binder and validity bits. Seventeen Toffoli and fifteen Fredkin factors per node have logical support at most three and inherit Cycle669's support-two lowering. The declared adapter overlay is `{receipt['bank_and_causal_decoder']['resources']['Cycle680_adapter_overlay_M2']}` M2. The strict end-to-end total is null because the Cycle610 detector lacks a strict physical M2 compiler and Cycle675 lacks a trajectory-to-tick association.

The root rotor is supplied at 12. Twelve actual train ticks force one wrap and one blank-bank refill. The carry survives the refill. Deleting it changes the decoded interval by exactly 16; deleting the refill token blocks the second bank; deleting the cross-bank predecessor or binder makes the spanning interval undefined. All 32 rotor basis rows, their inverse, three factor deletions and three malformed inputs pass.

The exact causal `decode_position`, `decode_interval`, `ratio` and `JointOrder` functions are imported from `{CAUSAL_SHORE}` and not edited. Their `Cell.index` field is populated from the physical one-hot node identity, not from a loop or update ordinal; source-label exhaust, loop ordinal and shared `s` are absent from both decoders.

| causal row | assertion | Cycle680 status | pass? | boundary |
|---:|---|---|---:|---|
{assertion_rows}

Rows 1–3 are not failures: they are **unrun physical obligations**. Running them with the causal shore's ideal `nu/s` generator would counterfeit the requested bridge. Rows 4–9 are conditional interface passes because their mark packets, acceptance bits and refill are supplied. Row 6 proves additive decoded counts only; its `nu/s` floor-prediction half is unrun. The decoded count and any ratio are relational duration candidates, not proper time. No update, factor count or source label is called time, a rate or energy.

## Fresh N1–N8

### N1

| family | object | terminal | honesty | status | authority |
|---|---|---|---|---|---|
{n1}

### N2–N5

The independent walls are `{list(ng['N2_walls'])}`. All `{len(ng['N2_directed_pairwise_table'])}` directed pairs are audited non-implications. N3 exposes purified preparation, acceptance bits, mark packets, refill, frame chart and the unattached identification law.

| prior witness | prior residual | current residual | exact match? |
|---|---|---|---:|
{n4}

N5 keeps tick/occurrence, count/proper-time, snapshot/clock and finite-refill/renewal rhetoric separated at element, site, mode, block and lattice scales.

### N6–N8

| path | status | closes |
|---|---|---|
{n6}

N7 steelman: {ng['N7_steelman']}

N8 compares Cycles 602, 610, 668, 669, 675, 676 and 680 without back-credit. Negative gate: **{ng['negative_claim_gate_status']}**. This is not a no-go, minimum-content result or shared obstruction. Axiom pressure: **none**.

## Disposition and novelty boundary

The strongest constructive result is a finite physical-M2 acceptance overlay that carries regenerated Cycle610 detector-law tick certificates through one blank-bank refill into the unchanged causal decoder, with persistent physical carry, exact predecessor packets, deletion/refusal controls and all24/all576 covariance. It is conditional on supplied admission, co-registration and refill resources and is not a physical synchronization or proper-time result.

K16 rotors, predecessor chains, carry arithmetic, blank-bank renewal tests and causal ratio assertions are prior structures. The new repo-side result is their exact object-pinned adapter and acceptance matrix across the committed physics and causal shores, especially the refusal to substitute ideal `nu/s` events for physical ticks.

**PASS / CONDITIONAL INTERFACE** for causal rows 4–9. **NOT MET, NOT FALSIFIED** for full physical causal acceptance. No shared obstruction or axiom pressure. The next campaign should build the N7 dual physical detector/co-registration apparatus, then rerun rows 1–9 unchanged.
"""


def note_contract():
    body = " ".join(NOTE.read_text().lower().split())
    required = (
        "authority: **none**", "audit: **unset**", "regenerated cycle610 detector-law crossing outputs",
        "not samples from causal cycle676's ideal `nu/s` generator", "candidate opportunity, not an occurrence",
        "relational duration candidates, not proper time", "unrun physical obligations", "not a no-go",
        "axiom pressure: **none**", "not met, not falsified", "strict end-to-end total is null",
        "no update, factor count or source label is called time, a rate or energy",
    )
    missing = tuple(item for item in required if item not in body)
    return {"required": required, "missing": missing, "pass": not missing}


def main():
    signal.alarm(math.ceil(WALL_CAP_SECONDS)); started = time.perf_counter()
    frozen, receipts, causal_receipts = freeze_controls()
    ng = no_go_discipline()
    clocks, private_events = actual_detector_clock_rows()
    classification = classify_input_surfaces(receipts)
    bank = bank_and_decoder_controls(private_events)
    covariance = covariance_controls()
    generator_audit = ideal_generator_call_audit()
    receipt = {
        "cycle": 680, "date": "2026-07-23", "authority": AUTHORITY, "audit": AUDIT,
        "status": "finite regenerated-tick-certificate to causal-decoder acceptance overlay; physical synchronization rows 1-3 unrun",
        "classification": "conditional-physical-M2-acceptance-bridge",
        "frozen_shores": frozen, "no_go_discipline": ng,
        "actual_detector_clocks": clocks, "input_surface_classification": classification,
        "bank_and_causal_decoder": bank, "covariance": covariance,
        "ideal_generator_call_audit": generator_audit,
        "supplied_structure_inventory": supplied_inventory(),
        "strongest_constructive_result": (
            "regenerated Cycle610 train/held tick certificates pass through a 631-M2 two-bank predecessor/K16 carry overlay "
            "into unchanged causal decoders for renewal, reversal, additivity, missing/inverted and no-source-label rows"
        ),
        "causal_ideal_nu_s_generator_called": generator_audit["causal_ideal_nu_s_generator_called"],
        "terminology_firewall": {
            "frozen_target_actual_means_executed_output_not_objective_actuality": True,
            "result_term": "regenerated Cycle610 tick certificate",
            "actuality_reserved_for": "explicitly supplied objective-admission bit",
        },
        "physical_sync_rows_1_3_run": False,
        "decoded_count_or_ratio_called_proper_time": False,
        "strict_full_framework_terminal_met": False,
        "target_contract_candidate_terminal_met": False,
        "exact_terminal_met": False, "exact_terminal_disposition": "NOT_MET_NOT_FALSIFIED",
        "shared_route_independent_obstruction": False, "axiom_pressure": False,
        "breakthrough": False, "author_accepted": False,
        "optimal_next_campaign": "dual physical detector/co-registration apparatus plus autonomous blank-bank genesis",
    }
    NOTE.write_text(note_text(receipt))
    note = note_contract(); check("Cycle680 note preserves physical-source, causal, duration and no-go type gates", note["pass"], note["missing"])
    elapsed = time.perf_counter() - started; rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if rss < 10_000_000: rss *= 1024
    receipt.update({"note_contract": note, "runner_sha256": file_sha(Path(__file__)),
                    "note_sha256": file_sha(NOTE), "elapsed_seconds": elapsed,
                    "maximum_RSS_bytes": rss, "tests_passed": PASS, "tests_failed": FAIL})
    receipt["pass"] = (FAIL == 0 and all(row["pass"] for row in
                                         (frozen, ng, clocks, classification, bank, covariance, generator_audit, note))
                       and not receipt["causal_ideal_nu_s_generator_called"]
                       and not receipt["physical_sync_rows_1_3_run"]
                       and elapsed < WALL_CAP_SECONDS and rss < RSS_CAP_BYTES
                       and AUTHORITY == "none" and AUDIT == "unset")
    RECEIPT.write_text(json.dumps(receipt, indent=2, sort_keys=True,
                                  default=lambda value: value.item() if isinstance(value, np.generic) else list(value)) + "\n")
    print(json.dumps({"pass": receipt["pass"], "tests_passed": PASS, "tests_failed": FAIL,
                      "elapsed_seconds": elapsed, "maximum_RSS_bytes": rss,
                      "note": str(NOTE), "receipt": str(RECEIPT)}, indent=2))
    if not receipt["pass"]: raise SystemExit(1)


if __name__ == "__main__": main()
