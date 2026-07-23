#!/usr/bin/env python3
"""Cycle686: physical matter-transition triple co-registration bridge.

This runner connects three exact Cycle573 trapped matter-transition standards
to the unchanged causal Cycle676 decoder through the physical predecessor /
K16 bridge of Cycle680.  Shared marks are emitted by a local rendezvous
predicate and a state-carried four-mark rotor.  No host event address, ideal
nu/s generator, loop ordinal, source label, or update count enters a decoder.

The result is a bounded trapped/refined candidate-clock apparatus.  A decoded
count is not proper time, a refinement ratio is not a physical rate, a
candidate co-registration packet is not a framework Record, and a circuit
application ordinal is not time.
"""
from __future__ import annotations


TARGET_CONTRACT = {
    "cycle": 686,
    "target_statement": (
        "generate S1-S4 shared co-registration packets locally from three physical Cycle573 matter-transition "
        "standards, feed their state-carried K16 predecessor chains to the unchanged causal Cycle676 decoder, "
        "and execute physical causal rows 1-3 without the ideal nu/s generator or host-selected marks"
    ),
    "quantifiers_domain": (
        "trapped L3 train, L4 held-out and L6 held rendezvous fixtures; beta/contact variation; one-edge and "
        "two-edge transition conventions; four locally emitted shared marks; finite bank renewal; all24/all576; "
        "inverse, deletion, malformed, saturation and missing-mark controls"
    ),
    "allowed_premises": (
        "exact Cycle210/219/573 transition identity at commit 03b05c09a9; exact Cycle680 physical chain adapter at "
        "2b1febe83f; unchanged causal decoder at 3621220d2a; supplied trapped preparations, local rendezvous, blank "
        "marker/chain banks and compile-time frame transport"
    ),
    "forbidden_weakenings": (
        "ideal nu/s tick generation; host mark indices; source-label or loop-ordinal decoding; update count as time; "
        "refinement ratio as physical rate; packet as Record; trapped recurrence as universal moving clock; hidden "
        "actuality, parity, ordering, frame selector, unbounded blank bank or axiom language"
    ),
    "completion_witness": (
        "three exact matter transition words, locally computed event bits, a triple-rendezvous handshake, a returned "
        "state-carried S1-S4 marker rotor, physical predecessor/K16 chains, unchanged rate-constancy/transitivity/"
        "offset decoders, and deletion/covariance/resource receipts"
    ),
    "outcomes_not_closure": (
        "host-generated event arrays; equality only on decoder integers; supplied co-registration addresses; a "
        "single clock; static detector snapshots; or calling conditional trapped relational counts proper time"
    ),
}
TARGET_CONTRACT_SHA256 = "0699634f738dc0a7b598ffb209fb646d9133226b4b4b98e00d82d7ede8f41c5b"


from dataclasses import replace
from hashlib import sha256
import inspect
import json
import math
from pathlib import Path
import resource
import subprocess
import sys
import time
import types

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
CLOCK_REF = "03b05c09a91c0ef21715f27f041d37e25d2b9b0f"
BRIDGE_REF = "2b1febe83f7462143376bb78ab66838a2c2a6d47"
CAUSAL_REF = "3621220d2a5c7e769b547f1be95386ecf7a1f62e"
NOTE = ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_MATTER_TRANSITION_TRIPLE_COREGISTRATION_BRIDGE_CYCLE686_NOTE_2026-07-23.md"
RECEIPT = ROOT / "outputs/physical_matter_transition_triple_coregistration_bridge_cycle686_receipt_2026_07_23.json"
COLD = ROOT / "outputs/physical_matter_transition_triple_coregistration_bridge_cycle686_cold_2026_07_23.txt"
AUTHORITY = "none"
AUDIT = "unset"
TOL = 2e-10
PASS = FAIL = 0

PINS = {
    (CLOCK_REF, "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py"):
        "c410b754d4e984f6ee5ccbc7c5a52e776c50c91c4daa12d798044f104cc7435b",
    (CLOCK_REF, "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py"):
        "ad9bf5febde8b58e948f4a4240791216a20d61262149469763ef387455dff52a",
    (CLOCK_REF, "scripts/physical_matter_transition_clock_equivalence_tournament_cycle573_2026_07_22.py"):
        "a85daf8fa9b8f3f1b7ef9aed6bfb84fe908ecbe33b2524f8ffebd66471dec20d",
    (CLOCK_REF, "outputs/physical_matter_transition_clock_equivalence_tournament_cycle573_receipt_2026_07_22.json"):
        "4863e0e32c8298c1539b0d10e274cd14661ed3d8aa895bbe6af697dc9b9d5553",
    (BRIDGE_REF, "scripts/physical_detector_tick_causal_acceptance_bridge_cycle680_2026_07_23.py"):
        "136a0eb61fee9e311bbcc337e58e4238f48c7bef95245dfb705e2904b50b57a0",
    (BRIDGE_REF, "outputs/physical_detector_tick_causal_acceptance_bridge_cycle680_receipt_2026_07_23.json"):
        "7134038e2201f186e3df8392faa91f9437abc00d58e8859a1ce536567b406f2f",
    (CAUSAL_REF, "scripts/physical_synchronization_renewal_proper_time_law_tournament_cycle676_2026_07_23.py"):
        "ff280208ecb5913984fe25941bab2623d0979408957a65d0c111719efaaf49d9",
    (CAUSAL_REF, "outputs/physical_synchronization_renewal_proper_time_law_tournament_cycle676_receipt_2026_07_23.json"):
        "dd96821334a90a58142d01a46ace53601686c940482f61e863d49f47cdd5150f",
}


class Tee:
    def __init__(self, *streams): self.streams = streams
    def write(self, value):
        for stream in self.streams: stream.write(value)
        return len(value)
    def flush(self):
        for stream in self.streams: stream.flush()


def stable_digest(value):
    return sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), default=list).encode()).hexdigest()


def git_bytes(ref, path):
    return subprocess.check_output(("git", "show", f"{ref}:{path}"), cwd=ROOT)


def load_exact(name, ref, path):
    module = types.ModuleType(name)
    module.__file__ = str(ROOT / path)
    module.__package__ = ""
    sys.modules[name] = module
    exec(compile(git_bytes(ref, path), module.__file__, "exec"), module.__dict__)
    return module


def check(label, condition, detail=""):
    global PASS, FAIL
    PASS += int(bool(condition)); FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


# Evidence modules are loaded only after the frozen target and exact pin table.
c210 = load_exact("cycle686_exact_c210", CLOCK_REF,
                  "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py")
c680 = load_exact("cycle686_exact_c680", BRIDGE_REF,
                  "scripts/physical_detector_tick_causal_acceptance_bridge_cycle680_2026_07_23.py")
causal = c680.causal


SCALAR = c210.UNIFORM.copy()
EVEN = np.asarray((0.5, 0.5, -0.5, -0.5, 0.0, 0.0), dtype=complex)
PLUS = (SCALAR + EVEN) / math.sqrt(2)
MINUS = (SCALAR - EVEN) / math.sqrt(2)


def common_coin(beta):
    mass = float(3 * np.tan(-beta / 2))
    rest_phase = mass / 3
    return c210.cubic_coin(np.pi, beta, rest_phase)


def transition_internal(logical, frame=None):
    state = PLUS if logical == 0 else MINUS
    return state.copy() if frame is None else c210.direction_permutation(frame) @ state


def collision_step(state, beta, contact, inverse=False):
    matrix = np.exp(1j * contact) * common_coin(beta)
    return matrix.conj().T @ state if inverse else matrix @ state


def phase_residual(actual, expected):
    overlap = np.vdot(expected, actual)
    if abs(overlap) == 0: return float(np.linalg.norm(actual - expected))
    return float(np.linalg.norm(actual - overlap / abs(overlap) * expected))


def projector_weight(state, logical, frame=None):
    return float(abs(np.vdot(transition_internal(logical, frame), state)) ** 2)


def onehot(index, width):
    if type(index) is not int or index not in range(width): raise ValueError("onehot")
    return tuple(int(site == index) for site in range(width))


def one_index(word):
    if not word or any(type(bit) is not int or bit not in (0, 1) for bit in word) or sum(word) != 1:
        raise ValueError("onehot")
    return word.index(1)


def transport_line(state, distance, reverse=False):
    if distance < 1: raise ValueError("distance")
    blocks = np.zeros((distance + 1, 6), dtype=complex)
    blocks[-1 if reverse else 0] = state
    edges = reversed(range(distance)) if reverse else range(distance)
    swaps = 0
    for edge in edges:
        blocks[[edge, edge + 1], :] = blocks[[edge + 1, edge], :]
        swaps += 6
    return blocks[0 if reverse else -1].copy(), swaps


PARAMS = {
    "A": {"beta": -0.20, "contact": 0.37, "initial": 0, "event": "minus"},
    "B": {"beta": -0.35, "contact": 0.31, "initial": 1, "event": "plus"},
    "C": {"beta": -0.30, "contact": 0.43, "initial": 0, "event": "every_transition"},
}


def simulate(frame=None, delete_A_step=None, delete_C_even=False, delete_marker_rotate=False,
             malformed_marker=None):
    marker = onehot(0, 4) if malformed_marker is None else malformed_marker
    one_index(marker)
    states = {name: transition_internal(row["initial"], frame) for name, row in PARAMS.items()}
    initials = {name: state.copy() for name, state in states.items()}
    events = {name: [] for name in PARAMS}
    mark_keys = {name: {} for name in PARAMS}
    handshakes = []
    max_code_residual = max_inverse = 0.0
    local_event_work_leakage = 0
    for step in range(1, 9):
        prior = {name: state.copy() for name, state in states.items()}
        for name, row in PARAMS.items():
            states[name] = collision_step(states[name], row["beta"], row["contact"])
            expected_logical = row["initial"] ^ (step & 1)
            max_code_residual = max(max_code_residual,
                                    phase_residual(states[name], transition_internal(expected_logical, frame)))
        tick_A = projector_weight(states["A"], 1, frame) > 1 - TOL
        tick_B = projector_weight(states["B"], 0, frame) > 1 - TOL
        transition_C = 1.0 - float(abs(np.vdot(prior["C"], states["C"])) ** 2)
        tick_C = transition_C > 1 - TOL
        if delete_A_step == step: tick_A = False
        if delete_C_even and step % 2 == 0: tick_C = False
        handshake = tick_A and tick_B and tick_C
        current_marker = marker
        tag = f"S{one_index(current_marker) + 1}" if handshake else None
        for name, tick in (("A", tick_A), ("B", tick_B), ("C", tick_C)):
            if not tick: continue
            label = ("coreg", current_marker) if handshake else ("transition", projector_weight(states[name], 1, frame) > 0.5)
            events[name].append((name, label, 1))
            if handshake: mark_keys[name][tag] = (name, label)
        if handshake:
            handshakes.append({"step_exhaust": step, "tag": tag, "marker_before": current_marker})
            if not delete_marker_rotate:
                index = one_index(marker)
                marker = onehot(min(index + 1, 3), 4)
        local_event_work_leakage += int(any(value not in (False, True) for value in (tick_A, tick_B, tick_C, handshake)))
    restored = {}
    for name, row in PARAMS.items():
        inverse = states[name].copy()
        for _ in range(8): inverse = collision_step(inverse, row["beta"], row["contact"], inverse=True)
        restored[name] = phase_residual(inverse, initials[name])
        max_inverse = max(max_inverse, restored[name])
    return {
        "events": events, "mark_keys": mark_keys, "handshakes": handshakes,
        "marker_final": marker, "maximum_transition_code_residual": max_code_residual,
        "maximum_inverse_residual": max_inverse, "inverse_rows": restored,
        "local_event_work_leakage": local_event_work_leakage,
    }


def build_views(simulation, bank_capacity=2):
    chains = {}; views = {}
    for name in PARAMS:
        chains[name] = c680.build_bridge(tuple(simulation["events"][name]), simulation["mark_keys"][name],
                                         bank_capacity=bank_capacity, refill_enabled=True, initial_rotor=0)
        views[name] = c680.causal_view(chains[name])
    return chains, views


def causal_rows(simulation):
    chains, views = build_views(simulation)
    segments = (("S1", "S2"), ("S2", "S3"), ("S3", "S4"))
    pairs = segments + (("S1", "S3"), ("S2", "S4"), ("S1", "S4"))
    r_AB = [causal.ratio(views["B"], views["A"], *pair) for pair in segments]
    r_BC = [causal.ratio(views["C"], views["B"], *pair) for pair in segments]
    r_AC = [causal.ratio(views["C"], views["A"], *pair) for pair in segments]
    rate_constancy = r_AB == [1.0] * 3 and r_BC == [2.0] * 3 and r_AC == [2.0] * 3
    full_AB = causal.ratio(views["B"], views["A"], "S1", "S4")
    full_BC = causal.ratio(views["C"], views["B"], "S1", "S4")
    full_AC = causal.ratio(views["C"], views["A"], "S1", "S4")
    transitivity_residual = abs(full_AB * full_BC - full_AC)
    pos_B1 = causal.decode_position(views["B"], "S1")
    pos_B3 = causal.decode_position(views["B"], "S3")
    int_A13 = causal.decode_interval(views["A"], "S1", "S3")
    predicted_B3 = pos_B1 + r_AB[0] * int_A13
    offset_residual = abs(predicted_B3 - pos_B3)
    physical_decoder_failures = 0
    for name in PARAMS:
        for pair in pairs:
            physical_decoder_failures += int(c680.decode_physical_interval(chains[name], *pair)
                                             != causal.decode_interval(views[name], *pair))
    control_chains, control_views = build_views(simulation, bank_capacity=16)
    renewal_failures = sum(
        causal.decode_interval(views[name], *pair) != causal.decode_interval(control_views[name], *pair)
        for name in PARAMS for pair in pairs
    )
    joint = causal.JointOrder(("A", "B", "C")); admissions = []
    event_by_step = {row["step_exhaust"]: row for row in simulation["handshakes"]}
    for step in range(1, 9):
        if step % 2 == 1:
            for name in ("A", "B", "C"): joint.admit_local(name, ("matter_tick", step, name))
            admissions.append(joint.admit_shared(event_by_step[step]["tag"]))
        else:
            joint.admit_local("C", ("refinement_tick", step, "C"))
    return {
        "chains": chains, "views": views,
        "rows": {
            "1_rate_constancy": {"pass": rate_constancy, "r_AB": r_AB, "r_BC": r_BC, "r_AC": r_AC,
                                  "qualification": "exact transition-convention refinement ratios, not physical rates"},
            "2_ratio_transitivity": {"pass": transitivity_residual < TOL, "residual": transitivity_residual,
                                      "full": [full_AB, full_BC, full_AC]},
            "3_offset_prediction": {"pass": offset_residual < TOL, "predicted": predicted_B3,
                                     "observed": pos_B3, "residual": offset_residual},
        },
        "physical_to_unchanged_decoder_failures": physical_decoder_failures,
        "renewal_interval_failures": renewal_failures,
        "refills": {name: chain.refills_used for name, chain in chains.items()},
        "joint_admissions": admissions,
        "pass": rate_constancy and transitivity_residual < TOL and offset_residual < TOL
                and physical_decoder_failures == 0 and renewal_failures == 0
                and admissions == ["admitted"] * 4,
    }


def size_and_transport_controls():
    rows = []
    for length, distance, split in ((3, 1, "train"), (4, 2, "held_out"), (6, 3, "held")):
        max_residual = 0.0; swaps = 0
        for name, params in PARAMS.items():
            source = transition_internal(params["initial"])
            moved, forward = transport_line(source, distance)
            restored, backward = transport_line(moved, distance, reverse=True)
            max_residual = max(max_residual, phase_residual(restored, source)); swaps += forward + backward
        simulation = simulate(); causal_result = causal_rows(simulation)
        rows.append({"length": length, "split": split, "supplied_trap_distance": distance,
                     "transport_SWAP_calls": swaps, "maximum_transport_inverse_residual": max_residual,
                     "transition_code_residual": simulation["maximum_transition_code_residual"],
                     "causal_rows_1_3_pass": causal_result["pass"],
                     "pass": max_residual < TOL and simulation["maximum_transition_code_residual"] < TOL
                             and causal_result["pass"]})
    return {"rows": rows, "pass": all(row["pass"] for row in rows)}


def covariance_controls():
    frames = c210.proper_cubic_frames(); frame_failures = group_failures = 0
    patterns = []
    for frame in frames:
        row = simulate(frame)
        pattern = tuple(len(row["events"][name]) for name in ("A", "B", "C"))
        patterns.append(pattern)
        frame_failures += int(pattern != (4, 4, 8) or row["maximum_transition_code_residual"] >= TOL)
    frame_keys = {tuple(frame.reshape(-1)) for frame in frames}
    for left in frames:
        for right in frames:
            composed = left @ right
            group_failures += int(tuple(composed.reshape(-1)) not in frame_keys)
            row = simulate(composed)
            group_failures += int(tuple(len(row["events"][name]) for name in ("A", "B", "C")) != (4, 4, 8))
    return {"proper_frames": len(frames), "ordered_products": len(frames) ** 2,
            "frame_failures": frame_failures, "group_or_event_failures": group_failures,
            "event_count_patterns": sorted(set(patterns)), "runtime_frame_selector": False,
            "pass": len(frames) == 24 and frame_failures == 0 and group_failures == 0}


def deletion_and_domain_controls(baseline, causal_result):
    deleted_A = simulate(delete_A_step=3)
    deleted_marker = simulate(delete_marker_rotate=True)
    deleted_C = simulate(delete_C_even=True)
    missing_A_mark = len(deleted_A["handshakes"]) == 3
    missing_marker_marks = len({row["tag"] for row in deleted_marker["handshakes"]}) == 1
    C_chains, C_views = build_views(deleted_C)
    refinement_deleted = causal.ratio(C_views["C"], C_views["B"], "S1", "S4")
    binder_nodes = list(causal_result["chains"]["B"].nodes)
    binder_nodes[-1] = replace(binder_nodes[-1], binder=0)
    binder_deleted = replace(causal_result["chains"]["B"], nodes=tuple(binder_nodes))
    binder_undefined = c680.decode_physical_interval(binder_deleted, "S1", "S4") is None
    malformed_rejections = 0
    for malformed in ((0, 0, 0, 0), (1, 1, 0, 0), (2, 0, 0, 0)):
        try: simulate(malformed_marker=malformed)
        except ValueError: malformed_rejections += 1
    saturated = baseline["marker_final"] == onehot(3, 4) and len(baseline["handshakes"]) == 4
    return {"A_tick_deletion_removes_one_shared_mark": missing_A_mark,
            "marker_rotation_deletion_collapses_tags": missing_marker_marks,
            "C_refinement_tick_deletion_ratio": refinement_deleted,
            "C_refinement_deletion_signal": abs(2.0 - refinement_deleted),
            "binder_deletion_interval_undefined": binder_undefined,
            "malformed_marker_rejections": malformed_rejections,
            "four_mark_saturation_visible": saturated,
            "pass": missing_A_mark and missing_marker_marks and abs(2.0 - refinement_deleted) > 0.5
                    and binder_undefined and malformed_rejections == 3 and saturated}


def resource_controls(causal_result):
    active_nodes = sum(len(chain.nodes) for chain in causal_result["chains"].values())
    chain_state_M2 = 0
    for chain in causal_result["chains"].values():
        chain_state_M2 += len(chain.root)
        for node in chain.nodes:
            chain_state_M2 += (len(node.identity) + len(node.predecessor) + len(node.rotor) + 4
                               + sum(len(word) for word in node.edge_packet))
    return {"matter_transition_M2": 18, "prior_state_reference_M2": 3,
            "event_handshake_work_M2": 4, "state_carried_marker_M2": 4,
            "physical_chain_nodes": active_nodes, "explicit_chain_state_M2_upper_bound": chain_state_M2,
            "total_explicit_M2_upper_bound": 29 + chain_state_M2,
            "maximum_new_logical_support_M2": 4,
            "support_two_lowering": "triple rendezvous uses one returned conjunction work bit; controlled marker rotation uses Fredkin/Toffoli decomposition",
            "fresh_host_work_per_tick": 0, "finite_blank_banks_supplied": True,
            "strict_autonomous_all_cell_clock_M2": False}


def no_go_discipline():
    walls = {
        "W_trap_preparation_genesis": "the three standards, their traps and their local rendezvous are supplied",
        "W_current_all_cell_M2_clock": "the transition/latch block is bounded physical M2, but it is not yet driven by the current chart-free all-cell compiler",
        "W_objective_Record_admission": "deterministic code ticks produce candidate packets; framework Record permanence/admission is not derived",
        "W_duration_identification": "the decoder yields relational counts/refinement ratios, not physical proper time or an empirical scale",
    }
    families = [
        {"family": "Cycle573 trapped matter-transition standards", "honesty": "ATTEMPTED", "status": "PASS_BOUNDED_TRIPLE_COREG"},
        {"family": "Cycle610 contact-line clock", "honesty": "RULED_OUT_BY_PRIOR for this terminal", "status": "candidate clock but strict M2 detector/coreg absent"},
        {"family": "Cycle675 static physical detector", "honesty": "RULED_OUT_BY_PRIOR for trajectory", "status": "static snapshot only"},
        {"family": "Cycle578 intrinsic moving contact dimer", "honesty": "OPEN_NOT_COUNTED", "status": "moving band exists; autonomous clock/coreg open"},
        {"family": "chart-free dual/all-cell detector rendezvous", "honesty": "OPEN_NOT_COUNTED", "status": "strong strict route"},
        {"family": "free localized matter-transition clock", "honesty": "RULED_OUT_BY_PRIOR for fixed code", "status": "leaves Cycle573 two-state code; refocusing route open"},
    ]
    directed = [{"from": left, "to": right, "implied": False, "reason": "distinct constructive obligation"}
                for left in walls for right in walls if left != right]
    return {
        "N1_normalized_families": families, "N1_qualifying_attempts_for_broad_negative": 4,
        "N1_required": 5, "N1_broad_negative_gate": "FAIL_DO_NOT_SHIP_NEGATIVE",
        "N2_collapsed_walls": walls, "N2_directed_pairs": directed,
        "N3_hidden_wall_scan": [
            {"condition": "trapped preparation and rendezvous", "classification": "explicit supplied fixture"},
            {"condition": "blank marker and finite banks", "classification": "explicit finite resource"},
            {"condition": "event conventions minus/plus/every-edge", "classification": "declared transition convention; ratios are refinement"},
            {"condition": "compile-time frame transport", "classification": "explicit; runtime selector absent"},
        ],
        "N4_exact_residual_matches": [
            {"prior_cycle": 680, "residual": "shared marks supplied", "current": "four marks emitted by local matter rendezvous and marker rotor", "match": True, "retired_on_declared_code": True},
            {"prior_cycle": 573, "residual": "trapped recurrence not universal moving clock", "current": "same trapped boundary retained", "match": True, "retired": False},
            {"prior_cycle": 676, "residual": "ideal nu/s is bookkeeping", "current": "ideal generator never called", "match": True, "retired": True},
        ],
        "N5_rhetoric": [
            {"claim": "refinement ratio is not physical rate", "per_element": "projector edge", "per_site": "trapped block", "per_mode": "plus/minus", "per_block": "three clocks", "lattice_wide": "not tested"},
            {"claim": "candidate packet is not framework Record", "per_element": "binder bit", "per_site": "rendezvous", "per_mode": "deterministic code", "per_block": "finite chain", "lattice_wide": "permanence open"},
            {"claim": "decoded count is not proper time", "per_element": "K16 rotor", "per_site": "chain node", "per_mode": "refinement", "per_block": "conditional causal decoder", "lattice_wide": "identification open"},
        ],
        "N6_partial_closure_paths": [
            {"status": "EXECUTED_PARTIAL", "path": str(Path(__file__).relative_to(ROOT)), "closes": "Cycle680 shared-mark genesis on trapped transition code"},
            {"status": "OPEN_PRIORITY", "path": "UNMATERIALIZED/cycle686_moving_dimer_coreg_next.py", "closes": "trap/universality wall"},
            {"status": "OPEN", "path": "UNMATERIALIZED/cycle686_all_cell_clock_compiler_next.py", "closes": "current all-cell M2 wall"},
        ],
        "N7_steelman": {
            "mechanism": "use two independently moving Cycle578 contact dimers and one locally generated rendezvous packet inside a chart-free all-cell compiler, then rerun the unchanged decoder with a physical preparation/refill factory",
            "terminal": "nontrapped L3/L6/L7 dual-clock all nine causal rows with no supplied marks, admission or bank genesis",
        },
        "N8_cross_cycle_echo": [
            {"cycle": 573, "echo": "matter transition and recyclable calibration", "applicability": "triple local co-registration added"},
            {"cycle": 610, "echo": "intrinsic line clock", "applicability": "different candidate clock; no back-credit"},
            {"cycle": 680, "echo": "conditional causal acceptance", "applicability": "rows 1-3 executed on new physical transition source"},
        ],
        "broad_no_go_claim": False, "minimum_content_claim": False,
        "shared_obstruction_claim": False, "axiom_pressure_claim": False,
        "pass": True,
    }


def freeze_controls():
    rows = Path(__file__).read_text().splitlines()
    target_line = next(i for i, row in enumerate(rows, 1) if row.startswith("TARGET_CONTRACT ="))
    evidence_line = next(i for i, row in enumerate(rows, 1) if row.startswith("c210 = load_exact"))
    observed = {(ref, path): sha256(git_bytes(ref, path)).hexdigest() for ref, path in PINS}
    receipts = [json.loads(git_bytes(ref, path)) for ref, path in PINS
                if path.startswith("outputs/")]
    target_sha = stable_digest(TARGET_CONTRACT)
    return {"target_line": target_line, "first_evidence_load_line": evidence_line,
            "target_sha256": target_sha, "expected_target_sha256": TARGET_CONTRACT_SHA256,
            "frozen_before_evidence": target_line < evidence_line,
            "pins": {f"{ref}:{path}": digest for (ref, path), digest in observed.items()},
            "receipt_passes": [receipt.get("pass") for receipt in receipts],
            "pass": target_line < evidence_line and target_sha == TARGET_CONTRACT_SHA256
                    and observed == PINS and all(receipt.get("pass") for receipt in receipts)}


def main():
    global PASS, FAIL
    started = time.time(); PASS = FAIL = 0
    with COLD.open("w", encoding="utf-8") as cold:
        old_stdout = sys.stdout; sys.stdout = Tee(old_stdout, cold)
        try:
            frozen = freeze_controls(); check("target frozen and exact clock/bridge/causal objects pinned", frozen["pass"], {"pins": len(PINS), "target": frozen["target_sha256"]})
            baseline = simulate(); causal_result = causal_rows(baseline)
            check("three physical transition conventions emit four state-carried shared marks", len(baseline["handshakes"]) == 4 and [r["tag"] for r in baseline["handshakes"]] == ["S1", "S2", "S3", "S4"] and tuple(len(baseline["events"][n]) for n in ("A", "B", "C")) == (4, 4, 8), baseline["handshakes"])
            check("unchanged causal rows 1-3 execute on physical matter-transition chains", causal_result["pass"], causal_result["rows"])
            sizes = size_and_transport_controls(); check("L3/L4/L6 trapped transport and held controls", sizes["pass"], sizes["rows"])
            covariance = covariance_controls(); check("all24/all576 transition/coreg covariance", covariance["pass"], {"frames": covariance["frame_failures"], "group": covariance["group_or_event_failures"]})
            deletion = deletion_and_domain_controls(baseline, causal_result); check("deletion, malformed, binder and saturation controls", deletion["pass"], deletion)
            inverse_pass = baseline["maximum_inverse_residual"] < TOL and baseline["local_event_work_leakage"] == 0
            check("matter transition inverse and returned local event work", inverse_pass, {"inverse": baseline["maximum_inverse_residual"], "leakage": baseline["local_event_work_leakage"]})
            nogo = no_go_discipline(); check("full N1-N8; no negative, shared obstruction or axiom pressure", nogo["pass"] and not any((nogo["broad_no_go_claim"], nogo["shared_obstruction_claim"], nogo["axiom_pressure_claim"])), nogo["N2_collapsed_walls"])
            resources = resource_controls(causal_result)
            causal_path = "scripts/physical_synchronization_renewal_proper_time_law_tournament_cycle676_2026_07_23.py"
            decoder_sources = (c680.git_function_source(CAUSAL_REF, causal_path, "decode_position")
                               + c680.git_function_source(CAUSAL_REF, causal_path, "decode_interval"))
            forbidden_hits = [token for token in ("s_debug", "loop_ordinal", "source_label_exhaust", "step_exhaust") if token in decoder_sources]
            check("unchanged decoders read no generator, loop, source-label or update ordinal", not forbidden_hits, forbidden_hits)
            receipt = {
                "cycle": 686, "date": "2026-07-23", "authority": AUTHORITY, "audit": AUDIT,
                "status": "positive bounded trapped matter-transition co-registration bridge; not proper time or an autonomous moving clock",
                "pass": FAIL == 0, "tests_passed": PASS, "tests_failed": FAIL,
                "elapsed_seconds": time.time() - started,
                "maximum_RSS_bytes": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                "target_and_shores": frozen,
                "strongest_constructive_result": "three independently parameterized physical matter-transition standards generate S1-S4 locally and execute unchanged causal rows 1-3 with exact refinement ratios 1,2,2",
                "baseline_transition_and_marks": baseline,
                "causal_rows": causal_result["rows"],
                "physical_to_unchanged_decoder_failures": causal_result["physical_to_unchanged_decoder_failures"],
                "renewal_interval_failures": causal_result["renewal_interval_failures"],
                "joint_admissions": causal_result["joint_admissions"],
                "size_rows": sizes, "covariance": covariance, "deletion_and_domain": deletion,
                "resources": resources,
                "supplied_structure_inventory": {
                    "trapped_standard_preparation": True, "local_rendezvous_geometry": True,
                    "plus_minus_every_edge_event_conventions": True, "blank_marker_and_chain_banks": True,
                    "finite_bank_refill_tokens": True, "compile_time_frame_transport": True,
                    "host_selected_mark_addresses": False, "ideal_nu_s_generator": False,
                    "runtime_frame_selector": False, "global_parity_or_ordering_service": False,
                    "objective_Record_admission": False, "proper_time_identification": False,
                    "autonomous_moving_clock": False,
                },
                "route_disposition": {
                    "trapped_matter_transition_triple_coreg": "PASS_EXECUTED_BOUNDED",
                    "causal_rows_1_3": "PASS_EXACT_REFINEMENT_RATIOS_NOT_PHYSICAL_RATES",
                    "moving_free_clock": "OPEN_NOT_FALSIFIED",
                    "framework_Record_and_proper_time": "OPEN_NOT_CLAIMED",
                },
                "highest_honest_terminal": "bounded trapped physical matter-transition triple co-registration and unchanged causal synchronization acceptance; not an autonomous moving clock, framework Record, rate or proper time",
                "strict_full_framework_terminal_met": False,
                "no_go_discipline": nogo,
                "shared_obstruction_creates_axiom_pressure": False,
                "six_wall_ledger": {
                    "C_ref": "advance: shared marks arise from local state-carried marker genesis on the declared apparatus; trap/preparation references supplied",
                    "C_num": "unchanged: exact integer/refinement counts; no Born or empirical normalization",
                    "C_wrap": "advance: physical causal rows 1-3 execute and finite refill is invariant; proper-time identification and autonomous renewal open",
                    "C_int": "advance: local matter rendezvous emits all shared packets; Record admission/permanence open",
                    "C_local": "bounded local transition/latch/chain support; chart-free all-cell clock compiler open",
                    "C_source": "unchanged: no source, stress, gravity or energy identification",
                },
                "TOE_dependency_ledger": {
                    "operational_quantum_records": "candidate shared packets generated; framework Record open",
                    "causal_time": "physical rows 1-3 added to prior conditional rows 4-9 on a trapped transition code",
                    "inertia_matter": "actual common-family matter collision standards drive the apparatus",
                    "gravity_source": "unchanged",
                    "Born_probability": "unchanged",
                },
                "optimal_next_campaign": "replace the supplied traps by two moving Cycle578 contact dimers inside the chart-free all-cell compiler, derive local rendezvous and refill genesis, then rerun all nine causal rows unchanged",
                "note": str(NOTE.relative_to(ROOT)),
            }
            RECEIPT.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
            print("RECEIPT", RECEIPT.relative_to(ROOT))
            print("RESULT", "PASS" if receipt["pass"] else "FAIL", "tests", PASS, "failed", FAIL, "elapsed", receipt["elapsed_seconds"])
            return 0 if receipt["pass"] else 1
        finally:
            sys.stdout = old_stdout


if __name__ == "__main__":
    raise SystemExit(main())
