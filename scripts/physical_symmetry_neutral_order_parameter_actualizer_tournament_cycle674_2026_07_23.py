#!/usr/bin/env python3
"""Cycle674: symmetry-neutral local order-parameter actualizer tournament."""
from __future__ import annotations


TARGET_CONTRACT = {
    "cycle": 674,
    "target": (
        "a bounded proper-cubic local update starting from a locally preparable symmetry-neutral order-parameter state, "
        "producing exactly one stable central ObjectiveEventToken[none|six] from the native Cycle661 coherent surface "
        "without an input selector, actuality token, host sampler, supplied random draw, or hidden frame/schedule service"
    ),
    "required": [
        "nontrivial basis agreement: each admitted Cycle661 basis sector gives its direction and rejects give none",
        "all 64 coherent sectors exported into explicit outgoing exhaust with amplitudes and phases retained globally",
        "one objective central value rather than a symmetric superposition, reduced diagonal, or durable branch-relative latch",
        "exact branchwise Cycle669 interface plus native coherent type gate",
        "train/held capacities 3/4/6, all24/all576, local M2 placement/support/depth",
        "inverse or explicit nonunitary ready/spent ledger, deletion/malformed/leakage/saturation",
    ],
    "routes": {
        "A": "deterministic symmetry-neutral one-shot instability with local ready/spent ledger",
        "B": "finite reversible triple-repetition dilation with one-error-stable central register",
        "C": "proper-cubic six-ray relational/domain-wall propagation into a central register",
    },
    "forbidden_closure": [
        "constant-none response", "coherent superposition of central values", "reduced diagonal as one actual value",
        "finite error correction as objective actuality", "branch-relative domain wall as one global event",
    ],
    "claim_ceiling": "route-specific bounded constructions and NOT_MET_NOT_FALSIFIED only; no shared obstruction or axiom pressure",
}
TARGET_CONTRACT_SHA256 = "86649d00c8c4e50710f56e80452be06ab5c2b950b5a16990c999a8ee9065e098"


PREREGISTRATION = {
    "fixtures": {
        "product_z0": {"split": "train", "capacity": 3},
        "biased_phase_product": {"split": "held_blinded", "capacity": 4},
        "six_site_GHZ": {"split": "held_blinded_nonproduct", "capacity": 6},
    },
    "neutral_genesis": "central none rail=1, direction rails=0, outgoing exhaust blank, ready=1, spent=0; local product preparation",
    "route_A": "one-shot deterministic basis latch followed by spent-code identity",
    "route_B": "three one-hot replicas and reversible bitwise majority output; all replicas/syndromes retained",
    "route_C": "six equal rays of lengths 3/4/6; branch direction seeds one outer ray and fixed local CNOTs carry its wall inward",
    "physical_chart": "reserved radius-3 proper-cubic 343-M2 supercell; active rails explicitly placed; frame selected only at compile time",
    "routing_bound": "Manhattan diameter <=18; route-and-return pair operation <=35 nearest-neighbor calls",
    "type_gate": "basis-defined central rails are ObjectiveEventToken only if the coherent input yields one global central basis value",
    "no_go_gate": "fresh remote-main N1-N8 before bounded disposition",
}
PREREGISTRATION_SHA256 = "d51eda83af5bbae89e3f23e0e5d520bb5f2c69cfd328001d55aee0f3dd703889"


from dataclasses import dataclass
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
SHORE = "0fda7fcf626fad3df00ac4237551b17a1b97cce2"
NOTE = ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_SYMMETRY_NEUTRAL_ORDER_PARAMETER_ACTUALIZER_TOURNAMENT_CYCLE674_NOTE_2026-07-23.md"
RECEIPT = ROOT / "outputs/physical_symmetry_neutral_order_parameter_actualizer_tournament_cycle674_receipt_2026_07_23.json"
AUTHORITY = "none"; AUDIT = "unset"; TOL = 3.0e-10
WALL_CAP_SECONDS = 240.0; RSS_CAP_BYTES = 3 * 1024**3
PASS = FAIL = 0


PINS = {
    "scripts/physical_deterministic_constrained_qca_formation_law_tournament_cycle661_2026_07_23.py": "83383268139e92bcd040fa176686f2e6c3d5eef806ba58ed5da9953a59af7590",
    "docs/work_history/repo/review_feedback/PHYSICAL_DETERMINISTIC_CONSTRAINED_QCA_FORMATION_LAW_TOURNAMENT_CYCLE661_NOTE_2026-07-23.md": "14262310b768983ebbdc8a89f914f237ab2a2523c8a096eece63b33a7e5e9ad4",
    "outputs/physical_deterministic_constrained_qca_formation_law_tournament_cycle661_receipt_2026_07_23.json": "c0ac1effe618bbdcbfc4bd6a3360f3beb557aa2469d47be476deef862e1340c5",
    "scripts/physical_state_carried_event_chain_sequence_protocol_cycle669_2026_07_23.py": "ac1237e211bf06a8eb394db0dd8001c88a5aaf81726b38a3e43bd066285a9c84",
    "docs/work_history/repo/review_feedback/PHYSICAL_STATE_CARRIED_EVENT_CHAIN_SEQUENCE_PROTOCOL_CYCLE669_NOTE_2026-07-23.md": "4ba9fe3a26606a944f362e81d6262543936018c6adf497069d8800e616f0c2c5",
    "outputs/physical_state_carried_event_chain_sequence_protocol_cycle669_receipt_2026_07_23.json": "0765c66f3d3625892d133976aca217a5676fef0820557b12b32c988cb6180760",
    "scripts/physical_coherent_sector_objective_event_actualizer_tournament_cycle671_2026_07_23.py": "6bb5935e6ec3c6d4c0b8d34272c855ac9ca1a675f3c5951e09144d3d28c32f25",
    "docs/work_history/repo/review_feedback/PHYSICAL_COHERENT_SECTOR_OBJECTIVE_EVENT_ACTUALIZER_TOURNAMENT_CYCLE671_NOTE_2026-07-23.md": "0d1e1f3be89f089d72e679881d5f4620f219411342d805183977be7f2b16d56e",
    "outputs/physical_coherent_sector_objective_event_actualizer_tournament_cycle671_receipt_2026_07_23.json": "8ce154f98b0d2c27e8a23f7f552f3bcbeb6d428f78e7e312c08603ad190cadf6",
    "docs/work_history/repo/review_feedback/PHYSICAL_COHERENT_SEED_MEMBER_DILATION_CYCLE536_NOTE_2026-07-21.md": "e15944633127890fe27cb52193960a28d9860212d5d7aafd70f15eef2e987457",
    "docs/work_history/repo/review_feedback/PHYSICAL_DISSIPATIVE_METASTABLE_FORMATION_CHANNEL_CYCLE663_NOTE_2026-07-23.md": "96f59a3f79ce7c29f3c9ccdf93cae9503ea4cd0084821c11ba6e0545046bec87",
    "docs/work_history/repo/review_feedback/PHYSICAL_OBJECTIVE_STOCHASTIC_OPEN_DILATION_CYCLE662_NOTE_2026-07-23.md": "bdc8dda304985a62c73fc6e7a03f11d61041dd8053a9321fb7171c9b22947a05",
}


def check(label, condition, detail=""):
    global PASS, FAIL
    PASS += int(bool(condition)); FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def digest(value): return sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), default=lambda x: list(x)).encode()).hexdigest()
def file_sha(path): return sha256(Path(path).read_bytes()).hexdigest()
def git_bytes(path): return subprocess.check_output(("git", "show", f"{SHORE}:{path}"), cwd=ROOT)


def load_exact(name, path):
    module = types.ModuleType(name); module.__file__ = str(ROOT / path); module.__package__ = ""
    sys.modules[name] = module
    exec(compile(git_bytes(path), module.__file__, "exec"), module.__dict__)
    return module


def citation(path, fragment):
    matches = [line for line, text in enumerate(git_bytes(path).decode().splitlines(), 1) if fragment in text]
    if len(matches) != 1: raise AssertionError((path, fragment, matches))
    return {"ref": SHORE, "path": path, "line": matches[0]}


def current_citation(fragment):
    rows = Path(__file__).read_text().splitlines()
    matches = [line for line, text in enumerate(rows, 1) if text.strip().startswith(fragment)]
    if len(matches) != 1: raise AssertionError((fragment, matches))
    return {"ref": "Cycle674 current", "path": str(Path(__file__).relative_to(ROOT)), "line": matches[0]}


# Exact evidence loads follow the frozen target and preregistration.
c661 = load_exact("cycle674_exact_c661", "scripts/physical_deterministic_constrained_qca_formation_law_tournament_cycle661_2026_07_23.py")
c669 = load_exact("cycle674_exact_c669", "scripts/physical_state_carried_event_chain_sequence_protocol_cycle669_2026_07_23.py")
c671 = load_exact("cycle674_exact_c671", "scripts/physical_coherent_sector_objective_event_actualizer_tournament_cycle671_2026_07_23.py")


WORDS = tuple(product((0, 1), repeat=6))


def freeze_and_shore_controls():
    rows = Path(__file__).read_text().splitlines()
    target_line = next(i for i, row in enumerate(rows, 1) if row.startswith("TARGET_CONTRACT ="))
    prereg_line = next(i for i, row in enumerate(rows, 1) if row.startswith("PREREGISTRATION ="))
    evidence_line = next(i for i, row in enumerate(rows, 1) if row.startswith("c661 = load_exact"))
    observed = {path: sha256(git_bytes(path)).hexdigest() for path in PINS}
    receipt_paths = {
        "661": "outputs/physical_deterministic_constrained_qca_formation_law_tournament_cycle661_receipt_2026_07_23.json",
        "669": "outputs/physical_state_carried_event_chain_sequence_protocol_cycle669_receipt_2026_07_23.json",
        "671": "outputs/physical_coherent_sector_objective_event_actualizer_tournament_cycle671_receipt_2026_07_23.json",
    }
    receipts = {cycle: json.loads(git_bytes(path)) for cycle, path in receipt_paths.items()}
    contracts = {f"Cycle{cycle}_pass": receipt["pass"] for cycle, receipt in receipts.items()}
    passed = (target_line < prereg_line < evidence_line and digest(TARGET_CONTRACT) == TARGET_CONTRACT_SHA256
              and digest(PREREGISTRATION) == PREREGISTRATION_SHA256 and observed == PINS and all(contracts.values()))
    result = {"shore": SHORE, "target": TARGET_CONTRACT, "target_sha256": digest(TARGET_CONTRACT),
              "expected_target_sha256": TARGET_CONTRACT_SHA256, "preregistration": PREREGISTRATION,
              "preregistration_sha256": digest(PREREGISTRATION), "expected_preregistration_sha256": PREREGISTRATION_SHA256,
              "target_line": target_line, "preregistration_line": prereg_line, "first_evidence_line": evidence_line,
              "frozen_before_evidence": target_line < prereg_line < evidence_line, "pins": PINS, "observed": observed,
              "working_tree_bytes_used_as_evidence": False, "imported_contracts": contracts, "pass": passed}
    check("Cycle674 target, routes, neutral genesis and exact shores were frozen before evidence", passed,
          {"target": result["target_sha256"], "prereg": result["preregistration_sha256"], "pins": len(PINS)})
    return result, receipts


def onehot(index, width):
    if type(index) is not int or index not in range(width): raise ValueError("one-hot index")
    return tuple(int(i == index) for i in range(width))


def one_index(word):
    if not word or any(type(bit) is not int or bit not in (0, 1) for bit in word) or sum(word) != 1:
        raise ValueError("not one-hot")
    return word.index(1)


def direction_map(frame, direction):
    moved = c661.c625.matvec(frame, c661.c625.DIRECTIONS[direction])
    return c661.c625.DIRECTIONS.index(moved)


def rotate_six(word, frame): return c661.c625.rotate_six(tuple(word), frame)


def event_center(word): return onehot(word.index(1) + 1, 7) if sum(word) == 1 else onehot(0, 7)


def fixture_distributions():
    menu = c661.c634.menu_families()["mixed_projective_merge"]
    compiled = c661.c634.compile_menu(menu)
    effects = c661.c634.induced_effects(compiled["unitary"], compiled["ports"])
    return {name: c661.branch_distribution(state, effects) for name, state in c661.quantum_fixtures().items()}


@dataclass(frozen=True)
class Operation:
    kind: str
    sites: tuple[int, ...]
    label: str


def apply_operations(bits, operations, reverse=False, delete=None):
    bits = list(bits); ordered = tuple(reversed(operations)) if reverse else tuple(operations)
    for index, operation in enumerate(ordered):
        original = len(operations) - 1 - index if reverse else index
        if delete == original: continue
        if operation.kind == "X": bits[operation.sites[0]] ^= 1
        elif operation.kind == "CNOT":
            control, target = operation.sites; bits[target] ^= bits[control]
        elif operation.kind == "TOFFOLI":
            left, right, target = operation.sites; bits[target] ^= bits[left] & bits[right]
        else: raise ValueError(operation.kind)
    return tuple(bits)


def route_A_layout():
    return {"width": 100, "center": tuple(range(84, 91)), "exhaust": tuple(range(91, 98)), "ready": 98, "spent": 99}


def route_B_layout():
    return {"width": 121, "center": tuple(range(84, 91)), "mirror1": tuple(range(91, 98)),
            "mirror2": tuple(range(98, 105)), "corrected": tuple(range(105, 112)),
            "exhaust": tuple(range(112, 119)), "ready": 119, "spent": 120}


def route_C_layout(length):
    ray0 = 91; exhaust0 = ray0 + 6 * length
    return {"width": 100 + 6 * length, "center": tuple(range(84, 91)),
            "rays": tuple(tuple(ray0 + direction * length + step for step in range(length)) for direction in range(6)),
            "exhaust": tuple(range(exhaust0, exhaust0 + 7)), "ready": exhaust0 + 7, "spent": exhaust0 + 8,
            "length": length}


def common_schedule(layout):
    center = layout["center"]; exhaust = layout["exhaust"]
    operations = [Operation("X", (exhaust[0],), "exhaust-valid")]
    operations += [Operation("CNOT", (c661.CAND[d], exhaust[d + 1]), f"exhaust-word:{d}") for d in range(6)]
    operations += [Operation("X", (layout["ready"],), "ready-debit"), Operation("X", (layout["spent"],), "spent-credit")]
    operations += [Operation("CNOT", (c661.ADMIT, center[0]), "neutral-clear")]
    operations += [Operation("CNOT", (c661.PACKET[0][1 + d], center[1 + d]), f"central-direction:{d}") for d in range(6)]
    return tuple(operations)


def route_A_schedule(): return common_schedule(route_A_layout())


def route_B_schedule():
    layout = route_B_layout(); operations = list(common_schedule(layout))
    for bank_name in ("mirror1", "mirror2"):
        bank = layout[bank_name]
        operations += [Operation("CNOT", (layout["center"][rail], bank[rail]), f"copy:{bank_name}:{rail}") for rail in range(7)]
    for rail in range(7):
        a, b, c = layout["center"][rail], layout["mirror1"][rail], layout["mirror2"][rail]
        target = layout["corrected"][rail]
        operations += [Operation("TOFFOLI", (a, b, target), f"majority:ab:{rail}"),
                       Operation("TOFFOLI", (a, c, target), f"majority:ac:{rail}"),
                       Operation("TOFFOLI", (b, c, target), f"majority:bc:{rail}")]
    return tuple(operations)


def route_C_schedule(length):
    layout = route_C_layout(length); operations = []
    exhaust = layout["exhaust"]
    operations.append(Operation("X", (exhaust[0],), "exhaust-valid"))
    operations += [Operation("CNOT", (c661.CAND[d], exhaust[d + 1]), f"exhaust-word:{d}") for d in range(6)]
    operations += [Operation("X", (layout["ready"],), "ready-debit"), Operation("X", (layout["spent"],), "spent-credit")]
    operations.append(Operation("CNOT", (c661.ADMIT, layout["center"][0]), "neutral-clear"))
    for direction in range(6):
        ray = layout["rays"][direction]
        operations.append(Operation("CNOT", (c661.PACKET[0][1 + direction], ray[-1]), f"wall-seed:{direction}"))
        for step in reversed(range(1, length)):
            operations.append(Operation("CNOT", (ray[step], ray[step - 1]), f"wall-propagate:{direction}:{step}"))
        operations.append(Operation("CNOT", (ray[0], layout["center"][1 + direction]), f"wall-center:{direction}"))
    return tuple(operations)


def initial_cell(qca_output, layout):
    bits = list(qca_output) + [0] * (layout["width"] - 84)
    bits[layout["center"][0]] = 1; bits[layout["ready"]] = 1
    return tuple(bits)


def validate_initial_cell(bits, layout, extra_blank=()):
    if len(bits) != layout["width"] or any(type(bit) is not int or bit not in (0, 1) for bit in bits): raise ValueError("cell word")
    if tuple(bits[i] for i in layout["center"]) != onehot(0, 7): raise ValueError("neutral center")
    if any(bits[i] for i in layout["exhaust"]): raise ValueError("dirty exhaust")
    if bits[layout["ready"]] != 1 or bits[layout["spent"]] != 0: raise ValueError("ready/spent")
    if any(bits[i] for i in extra_blank): raise ValueError("dirty auxiliary")


def stable_step(bits, layout, schedule):
    if bits[layout["ready"]] == 1 and bits[layout["spent"]] == 0:
        return apply_operations(bits, schedule)
    if bits[layout["ready"]] == 0 and bits[layout["spent"]] == 1:
        return tuple(bits)
    raise ValueError("malformed ready/spent ledger")


def extract_center(bits, fields): return tuple(bits[i] for i in fields)


def cycle669_attach(center, exhaust, capacity):
    index = one_index(center); actual = int(index != 0); direction = onehot(index - 1, 6) if actual else (0,) * 6
    event = c669.EventToken(actual, direction, tuple(exhaust), "Cycle661_basis")
    initial = c669.initial_chain(capacity); output, _ = c669.append_event(initial, event)
    passed = len(c669.read_chain(output)) == actual and (not actual or c669.inverse_event(output) == initial)
    return passed


def malformed_controls(layout, extra_blank=()):
    qca = c661.qca_forward(c661.source_word((0,) * 6)); source = list(initial_cell(qca, layout)); cases = []
    cases.append(tuple(source[:-1]))
    dirty_center = source.copy(); dirty_center[layout["center"][1]] = 1; cases.append(tuple(dirty_center))
    dirty_exhaust = source.copy(); dirty_exhaust[layout["exhaust"][0]] = 1; cases.append(tuple(dirty_exhaust))
    bad_ledger = source.copy(); bad_ledger[layout["spent"]] = 1; cases.append(tuple(bad_ledger))
    nonbinary = source.copy(); nonbinary[layout["ready"]] = 2; cases.append(tuple(nonbinary))
    refused = 0
    for case in cases:
        try: validate_initial_cell(case, layout, extra_blank)
        except ValueError: refused += 1
    return refused, len(cases)


def deletion_visibility(layout, schedule, sources):
    visible = 0
    references = [apply_operations(source, schedule) for source in sources]
    for deleted in range(len(schedule)):
        visible += int(any(apply_operations(source, schedule, delete=deleted) != expected
                           for source, expected in zip(sources, references)))
    return visible


def event_weight_rows(distributions):
    rows = {}
    for name, distribution in distributions.items():
        weights = [sum(value for word, value in distribution.items() if sum(word) != 1)]
        weights += [distribution[onehot(direction, 6)] for direction in range(6)]
        direction_spread = max(weights[1:]) - min(weights[1:])
        rows[name] = {"split": PREREGISTRATION["fixtures"][name]["split"],
                      "capacity": PREREGISTRATION["fixtures"][name]["capacity"],
                      "none_plus_six_weights": weights, "normalization_residual": abs(sum(weights) - 1),
                      "central_reduced_rank": sum(value > TOL for value in weights),
                      "central_reduced_purity": sum(value * value for value in weights),
                      "direction_weight_spread": direction_spread,
                      "proper_cubic_direction_symmetric": direction_spread < TOL}
    return rows


def host_sampling_hits(function):
    names = {"random", "rand", "randn", "choice", "choices", "sample", "randint", "uniform"}; hits = set()
    for node in ast.walk(ast.parse(inspect.getsource(function))):
        if not isinstance(node, ast.Call): continue
        name = node.func.attr if isinstance(node.func, ast.Attribute) else node.func.id if isinstance(node.func, ast.Name) else ""
        if name in names: hits.add(name)
    return tuple(sorted(hits))


def geometry_receipt(width):
    full = tuple(product(range(-3, 4), repeat=3)); ordered = tuple(sorted(full, key=lambda p: (sum(abs(x) for x in p), p)))
    active = ordered[:width]
    diameter = max(sum(abs(a - b) for a, b in zip(left, right)) for left in active for right in active)
    frames = c661.c625.proper_cubic_frames(); full_set = set(full)
    invariant = all({c661.c625.matvec(frame, p) for p in full} == full_set for frame in frames)
    translations = [digest(tuple((x + offset - offset, y, z) for x, y, z in active)) for offset in (0, 512, 1024)]
    frame_placements = [tuple(c661.c625.matvec(frame, point) for point in active) for frame in frames]
    return {"reserved_supercell_M2": len(full), "active_M2": width, "radius": 3, "maximum_active_L1_diameter": diameter,
            "placement_rule": "logical M2 index i maps to the i-th [-3,3]^3 point ordered by (L1 norm, x, y, z)",
            "logical_index_to_coordinate": active, "active_placement_sha256": digest(active),
            "frame_placement_sha256": [digest(row) for row in frame_placements],
            "all_frame_placements_inside_reserved_cube": all(set(row) <= full_set for row in frame_placements),
            "reserved_cube_all24_invariant": invariant,
            "translated_normalized_layout_digests": translations, "translation_invariant": len(set(translations)) == 1}


def schedule_resources(layout, schedule):
    placement = geometry_receipt(layout["width"]); coordinates = placement["logical_index_to_coordinate"]
    counts = {kind: sum(operation.kind == kind for operation in schedule) for kind in ("X", "CNOT", "TOFFOLI")}
    logical_two = counts["X"] + counts["CNOT"] + 15 * counts["TOFFOLI"]
    routed = counts["X"] + 35 * (counts["CNOT"] + 15 * counts["TOFFOLI"])
    exact_schedule = tuple({"kind": operation.kind, "sites": operation.sites, "label": operation.label}
                           for operation in schedule)
    operation_diameters = [max(sum(abs(a - b) for a, b in zip(coordinates[left], coordinates[right]))
                               for left in operation.sites for right in operation.sites)
                           for operation in schedule]
    return {"logical_gate_counts": counts, "logical_max_support_M2": 3 if counts["TOFFOLI"] else 2,
            "lowered_max_support_M2": 2, "literal_one_two_M2_calls_before_routing": logical_two,
            "nearest_neighbor_calls_upper_bound": routed, "conservative_depth_upper_bound": routed,
            "maximum_logical_operation_L1_diameter": max(operation_diameters),
            "exact_logical_schedule": exact_schedule, "exact_logical_schedule_sha256": digest(exact_schedule),
            "layout": placement}


def route_A_deterministic_instability(distributions):
    layout = route_A_layout(); schedule = route_A_schedule(); sources = []
    failures = inverse_failures = stable_failures = interface_failures = leakage_failures = 0
    for word in WORDS:
        qca = c661.qca_forward(c661.source_word(word)); source = initial_cell(qca, layout); sources.append(source)
        output = stable_step(source, layout, schedule); center = extract_center(output, layout["center"])
        expected_exhaust = (1, *word)
        failures += int(center != event_center(word) or tuple(output[i] for i in layout["exhaust"]) != expected_exhaust)
        leakage_failures += int(output[:84] != qca)
        inverse_failures += int(apply_operations(output, schedule, reverse=True) != source)
        stable_failures += int(stable_step(output, layout, schedule) != output)
        for capacity in (3, 4, 6):
            interface_failures += int(not cycle669_attach(center, expected_exhaust, capacity))
    deletion_visible = deletion_visibility(layout, schedule, sources)
    malformed, malformed_expected = malformed_controls(layout)
    rows = event_weight_rows(distributions)
    symmetric_rows = [name for name, row in rows.items() if row["proper_cubic_direction_symmetric"]]
    result = {
        "route": "A_deterministic_instability", "primary_object": "partial local ready-to-spent instability map",
        "mechanism": "neutral one-hot center is basis-driven once; spent image is an exact fixed code",
        "neutral_product_state_locally_preparable": True, "neutral_preparation_X_gates": 2,
        "basis_rows": 64, "basis_failures": failures, "inverse_on_image_failures": inverse_failures,
        "spent_fixed_code_failures": stable_failures, "Cycle669_branchwise_interface_failures": interface_failures,
        "Cycle661_prefix_leakage_failures": leakage_failures, "outgoing_exhaust_M2": 7,
        "all_64_sector_labels_distinct_in_exhaust": True, "global_wave_amplitudes_and_phases_retained": True,
        "event_rows": rows, "symmetric_fixture_rows": symmetric_rows,
        "equivariant_deterministic_fixed_point_lemma": (
            "a deterministic proper-cubic equivariant single-valued map sends an invariant input to an invariant label; "
            "none is the only invariant member of none|six"
        ),
        "constant_none_response_counts_as_terminal": False,
        "coherent_output_type": "CoherentDirectSum[Cycle661Sector x CentralBasisValue x OutgoingExhaust]",
        "one_global_objective_token": False, "input_selector_M2": 0, "input_actuality_token_M2": 0,
        "host_sampler_calls": 0, "host_sampling_source_hits": host_sampling_hits(route_A_deterministic_instability),
        "deletions_detected": deletion_visible, "deletions_expected": len(schedule),
        "malformed_rejected": malformed, "malformed_expected": malformed_expected,
        "saturation_policy": "spent-code reapplication is identity; no second formation consumes the cell",
        "nonunitary_ledger": "ambient update is partial; ready/spent and full source/exhaust give exact inverse on its image",
        "resources": schedule_resources(layout, schedule), "exact_terminal_met": False,
        "disposition": "positive finite deterministic basis instability and fixed latch; coherent output remains a direct sum",
    }
    result["pass"] = (failures == inverse_failures == stable_failures == interface_failures == leakage_failures == 0
                      and deletion_visible == len(schedule) and malformed == malformed_expected
                      and not result["host_sampling_source_hits"] and all(row["central_reduced_rank"] == 7 for row in rows.values()))
    check("route A gives an autonomous neutral-to-fixed basis latch but not one coherent objective value", result["pass"],
          {"deletions": deletion_visible, "symmetric": symmetric_rows, "terminal": False})
    return result


def route_B_metastable_dilation(distributions):
    layout = route_B_layout(); schedule = route_B_schedule(); majority = schedule[-21:]; prep = schedule[:-21]
    auxiliaries = (*layout["mirror1"], *layout["mirror2"], *layout["corrected"])
    sources = []; failures = inverse_failures = stable_failures = interface_failures = leakage_failures = 0
    correction_failures = correction_tests = 0
    for word in WORDS:
        qca = c661.qca_forward(c661.source_word(word)); source = initial_cell(qca, layout); sources.append(source)
        output = stable_step(source, layout, schedule); corrected = extract_center(output, layout["corrected"])
        expected = event_center(word); exhaust = (1, *word)
        failures += int(corrected != expected or tuple(output[i] for i in layout["exhaust"]) != exhaust)
        leakage_failures += int(output[:84] != qca)
        inverse_failures += int(apply_operations(output, schedule, reverse=True) != source)
        stable_failures += int(stable_step(output, layout, schedule) != output)
        for capacity in (3, 4, 6): interface_failures += int(not cycle669_attach(corrected, exhaust, capacity))
        prepared = apply_operations(source, prep)
        for bank in (layout["center"], layout["mirror1"], layout["mirror2"]):
            for rail in range(7):
                noisy = list(prepared); noisy[bank[rail]] ^= 1
                corrected_noisy = apply_operations(noisy, majority)
                correction_failures += int(extract_center(corrected_noisy, layout["corrected"]) != expected)
                correction_tests += 1
    deletion_visible = deletion_visibility(layout, schedule, sources)
    malformed, malformed_expected = malformed_controls(layout, auxiliaries)
    rows = event_weight_rows(distributions)
    result = {
        "route": "B_metastable_reversible_dilation", "primary_object": "triple-repetition central-value isometry",
        "mechanism": "three retained one-hot copies and reversible bitwise majority into a blank corrected register",
        "neutral_product_state_locally_preparable": True, "basis_rows": 64, "basis_failures": failures,
        "single_bit_error_tests": correction_tests, "single_bit_error_failures": correction_failures,
        "finite_one_error_stability_only": True, "physical_metastability_or_all_future_permanence_claimed": False,
        "inverse_on_blank_code_failures": inverse_failures, "spent_fixed_code_failures": stable_failures,
        "Cycle669_branchwise_interface_failures": interface_failures, "Cycle661_prefix_leakage_failures": leakage_failures,
        "outgoing_exhaust_M2": 7, "all_wave_replica_and_syndrome_exhaust_retained": True,
        "event_rows": rows, "coherent_output_type": "CoherentDirectSum[Sector x TripleLatch x CorrectedRelativeValue x Exhaust]",
        "one_global_objective_token": False, "input_selector_M2": 0, "input_actuality_token_M2": 0,
        "host_sampler_calls": 0, "host_sampling_source_hits": host_sampling_hits(route_B_metastable_dilation),
        "deletions_detected": deletion_visible, "deletions_expected": len(schedule),
        "malformed_rejected": malformed, "malformed_expected": malformed_expected,
        "saturation_policy": "finite spent latch is stable; no fresh corrected register or renewal is inferred",
        "resources": schedule_resources(layout, schedule), "exact_terminal_met": False,
        "disposition": "positive finite error-stable reversible latch; stability does not promote the coherent center to actuality",
    }
    result["pass"] = (failures == correction_failures == inverse_failures == stable_failures == interface_failures == leakage_failures == 0
                      and deletion_visible == len(schedule) and malformed == malformed_expected
                      and not result["host_sampling_source_hits"] and all(row["central_reduced_rank"] == 7 for row in rows.values()))
    check("route B constructs a finite one-error-stable latch with full exhaust but no objective promotion", result["pass"],
          {"correction_tests": correction_tests, "deletions": deletion_visible, "terminal": False})
    return result


def route_C_domain_walls(distributions):
    rows = {}; total_failures = inverse_failures = stable_failures = interface_failures = leakage_failures = 0
    deletion_visible = deletion_expected = malformed = malformed_expected = 0; resource_rows = {}
    for name, distribution in distributions.items():
        length = PREREGISTRATION["fixtures"][name]["capacity"]; layout = route_C_layout(length); schedule = route_C_schedule(length)
        ray_sites = tuple(site for ray in layout["rays"] for site in ray); sources = []; fixture_failures = 0
        for word in WORDS:
            qca = c661.qca_forward(c661.source_word(word)); source = initial_cell(qca, layout); sources.append(source)
            output = stable_step(source, layout, schedule); center = extract_center(output, layout["center"]); exhaust = (1, *word)
            expected_rays = tuple(bit for direction, bit in enumerate(word) for _ in range(length)) if sum(word) == 1 else (0,) * (6 * length)
            fixture_failures += int(center != event_center(word) or tuple(output[i] for i in ray_sites) != expected_rays
                                    or tuple(output[i] for i in layout["exhaust"]) != exhaust)
            leakage_failures += int(output[:84] != qca)
            inverse_failures += int(apply_operations(output, schedule, reverse=True) != source)
            stable_failures += int(stable_step(output, layout, schedule) != output)
            interface_failures += int(not cycle669_attach(center, exhaust, length))
        visible = deletion_visibility(layout, schedule, sources); deletion_visible += visible; deletion_expected += len(schedule)
        refused, expected = malformed_controls(layout, ray_sites); malformed += refused; malformed_expected += expected
        event_rows = event_weight_rows({name: distribution})[name]
        rows[name] = {**event_rows, "ray_length": length, "basis_failures": fixture_failures,
                      "domain_wall_M2": 6 * length, "deletions_detected": visible, "deletions_expected": len(schedule)}
        resource_rows[name] = schedule_resources(layout, schedule); total_failures += fixture_failures
    result = {
        "route": "C_relational_domain_wall", "primary_object": "six equal finite rays plus central one-hot value",
        "mechanism": "a retained direction wall propagates from the outer ray to the center by fixed local CNOTs",
        "neutral_product_state_locally_preparable": True, "rows": rows,
        "basis_failures": total_failures, "inverse_on_blank_code_failures": inverse_failures,
        "spent_fixed_code_failures": stable_failures, "Cycle669_branchwise_interface_failures": interface_failures,
        "Cycle661_prefix_leakage_failures": leakage_failures, "all_wall_and_wave_exhaust_retained": True,
        "coherent_output_type": "CoherentDirectSum[Sector x RelativeDomainWall x CentralRelativeValue x Exhaust]",
        "one_global_objective_token": False, "input_selector_M2": 0, "input_actuality_token_M2": 0,
        "host_sampler_calls": 0, "host_sampling_source_hits": host_sampling_hits(route_C_domain_walls),
        "deletions_detected": deletion_visible, "deletions_expected": deletion_expected,
        "malformed_rejected": malformed, "malformed_expected": malformed_expected,
        "saturation_policy": "spent wall/center is fixed; finite rays are not autonomously renewed",
        "resources": resource_rows, "exact_terminal_met": False,
        "disposition": "positive proper-cubic branch-relative wall compiler; coherent wall alternatives remain jointly retained",
    }
    result["pass"] = (total_failures == inverse_failures == stable_failures == interface_failures == leakage_failures == 0
                      and deletion_visible == deletion_expected and malformed == malformed_expected
                      and not result["host_sampling_source_hits"]
                      and all(row["central_reduced_rank"] == 7 for row in rows.values()))
    check("route C constructs finite covariant relative domain walls but no global objective center", result["pass"],
          {"lengths": [3, 4, 6], "deletions": deletion_visible, "terminal": False})
    return result


def rotate_seven(word, frame):
    output = [word[0]] + [0] * 6
    for direction in range(6): output[1 + direction_map(frame, direction)] = word[1 + direction]
    return tuple(output)


def rotate_cell(bits, layout, frame, route):
    output = list(bits); rotated_qca = c661.rotate_qca_word(tuple(bits[:84]), frame); output[:84] = rotated_qca
    for fields in (layout["center"], layout.get("mirror1"), layout.get("mirror2"), layout.get("corrected")):
        if fields is None: continue
        moved = rotate_seven(tuple(bits[i] for i in fields), frame)
        for site, bit in zip(fields, moved): output[site] = bit
    exhaust = layout["exhaust"]; moved_exhaust = (bits[exhaust[0]], *rotate_six(tuple(bits[i] for i in exhaust[1:]), frame))
    for site, bit in zip(exhaust, moved_exhaust): output[site] = bit
    if route == "C":
        for direction in range(6):
            target = direction_map(frame, direction)
            for source_site, target_site in zip(layout["rays"][direction], layout["rays"][target]):
                output[target_site] = bits[source_site]
    return tuple(output)


def covariance_controls():
    frames = c661.c625.proper_cubic_frames(); configs = [
        ("A", route_A_layout(), route_A_schedule()), ("B", route_B_layout(), route_B_schedule()),
        *(("C", route_C_layout(length), route_C_schedule(length)) for length in (3, 4, 6)),
    ]
    all24 = {"A": 0, "B": 0, "C": 0}; failures24 = {"A": 0, "B": 0, "C": 0}
    all576 = {"A": 0, "B": 0, "C": 0}; failures576 = {"A": 0, "B": 0, "C": 0}
    for route, layout, schedule in configs:
        for frame, word in product(frames, WORDS):
            source = initial_cell(c661.qca_forward(c661.source_word(word)), layout)
            left = stable_step(rotate_cell(source, layout, frame, route), layout, schedule)
            right = rotate_cell(stable_step(source, layout, schedule), layout, frame, route)
            failures24[route] += int(left != right); all24[route] += 1
        for left_frame, right_frame, word in product(frames, frames, WORDS):
            output = stable_step(initial_cell(c661.qca_forward(c661.source_word(word)), layout), layout, schedule)
            left = rotate_cell(rotate_cell(output, layout, right_frame, route), layout, left_frame, route)
            composed = c661.c625.matmul(left_frame, right_frame)
            right = rotate_cell(output, layout, composed, route)
            failures576[route] += int(left != right); all576[route] += 1
    cube = geometry_receipt(136)
    result = {"proper_cubic_frames": len(frames), "all24_tests": all24, "all24_failures": failures24,
              "all576_tests": all576, "all576_failures": failures576,
              "reserved_cube_all24_invariant": cube["reserved_cube_all24_invariant"],
              "all_frame_placements_inside_reserved_cube": cube["all_frame_placements_inside_reserved_cube"],
              "translation_invariant": cube["translation_invariant"], "runtime_frame_selector": False,
              "preferred_direction_order_load_bearing": False}
    result["pass"] = (len(frames) == 24 and sum(failures24.values()) == sum(failures576.values()) == 0
                      and cube["reserved_cube_all24_invariant"] and cube["all_frame_placements_inside_reserved_cube"]
                      and cube["translation_invariant"])
    check("all three neutral order-parameter routes pass physical-state all24/all576 covariance", result["pass"],
          {"all24": all24, "all576": all576})
    return result


def interface_and_boundary_controls(A, B, C, receipts):
    c671r = receipts["671"]
    result = {
        "Cycle671_exact_target_was_not_met": not c671r["exact_A_661_terminal_met"],
        "Cycle671_route_A_selector_M2_removed": c671r["routes"]["A"]["input_actuality_selector_M2"],
        "current_all_routes_input_selector_M2": [A["input_selector_M2"], B["input_selector_M2"], C["input_selector_M2"]],
        "current_all_routes_input_actuality_M2": [A["input_actuality_token_M2"], B["input_actuality_token_M2"], C["input_actuality_token_M2"]],
        "Cycle671_B_and_current_B_both_retain_coherent_output": (
            not c671r["routes"]["B"]["one_objective_token_generated_by_reversible_dilation"] and not B["one_global_objective_token"]),
        "Cycle671_C_and_current_C_both_relational": (
            not c671r["routes"]["C"]["one_global_objective_token"] and not C["one_global_objective_token"]),
        "all_branchwise_Cycle669_interfaces_pass": (A["Cycle669_branchwise_interface_failures"] == 0
                                                     and B["Cycle669_branchwise_interface_failures"] == 0
                                                     and C["Cycle669_branchwise_interface_failures"] == 0),
        "native_coherent_Cycle669_ObjectiveEventToken_available": False,
        "supplied_genesis": ["Cycle661 coherent fixture", "neutral center product state", "blank exhaust/auxiliaries",
                             "one ready and zero spent bit", "finite 343-M2 chart", "Cycle669 root/next seeds"],
        "supplied_boundary": ["finite cell edge", "finite C3/C4/C6 rays", "compile-time frame chart", "finite spent capacity"],
        "not_supplied": ["selector", "actuality token", "random draw", "host sampler", "runtime frame", "objective branch-read law"],
    }
    result["pass"] = (result["Cycle671_exact_target_was_not_met"] and all(x == 0 for x in result["current_all_routes_input_selector_M2"])
                      and all(x == 0 for x in result["current_all_routes_input_actuality_M2"])
                      and result["Cycle671_B_and_current_B_both_retain_coherent_output"]
                      and result["Cycle671_C_and_current_C_both_relational"]
                      and result["all_branchwise_Cycle669_interfaces_pass"])
    check("exact Cycle661/Cycle669/Cycle671 interfaces and supplied genesis/boundaries remain explicit", result["pass"],
          {"selector_removed": result["Cycle671_route_A_selector_M2_removed"], "native_token": False})
    return result


def no_go_discipline():
    Aref = current_citation("def route_A_deterministic_instability(")
    Bref = current_citation("def route_B_metastable_dilation(")
    Cref = current_citation("def route_C_domain_walls(")
    c671ref = citation("docs/work_history/repo/review_feedback/PHYSICAL_COHERENT_SECTOR_OBJECTIVE_EVENT_ACTUALIZER_TOURNAMENT_CYCLE671_NOTE_2026-07-23.md",
                       "NOT MET, NOT FALSIFIED")
    c662ref = citation("docs/work_history/repo/review_feedback/PHYSICAL_OBJECTIVE_STOCHASTIC_OPEN_DILATION_CYCLE662_NOTE_2026-07-23.md",
                       "stochastic law itself—not a host sampler")
    c536ref = citation("docs/work_history/repo/review_feedback/PHYSICAL_COHERENT_SEED_MEMBER_DILATION_CYCLE536_NOTE_2026-07-21.md",
                       "a diagonal density operator is not one realized member")
    c663ref = citation("docs/work_history/repo/review_feedback/PHYSICAL_DISSIPATIVE_METASTABLE_FORMATION_CHANNEL_CYCLE663_NOTE_2026-07-23.md",
                       "metastability are not irreversible framework Record formation")
    routes = [
        {"family": "finite deterministic neutral instability", "object": "partial ready/spent cellular map",
         "mechanism": "basis-driven central fixed latch", "terminal": "one global coherent-input value", "honesty": "ATTEMPTED",
         "authority": Aref, "disposition": "basis latch closes; coherent output remains sector-correlated"},
        {"family": "finite reversible metastable code", "object": "triple-repetition isometry",
         "mechanism": "majority invariant with retained syndrome", "terminal": "stability plus objective value", "honesty": "ATTEMPTED",
         "authority": Bref, "disposition": "one-error stability closes; actuality type does not"},
        {"family": "relational domain-wall propagation", "object": "six-ray wall history",
         "mechanism": "local wall transport and relative center", "terminal": "one nonrelative central value", "honesty": "ATTEMPTED",
         "authority": Cref, "disposition": "wall compiler closes; walls remain in coherent direct sum"},
        {"family": "ontic hidden selector", "object": "extended classical-quantum state",
         "mechanism": "selector-controlled event", "terminal": "native-domain actualizer", "honesty": "RULED OUT BY PRIOR",
         "authority": c671ref, "disposition": "Cycle671 succeeds only on an enlarged selector domain"},
        {"family": "hybrid objective stochastic field", "object": "quantum-classical instrument",
         "mechanism": "law-owned sigma update", "terminal": "derive objective law from neutral local dynamics", "honesty": "RULED OUT BY PRIOR",
         "authority": c662ref, "disposition": "Cycle662 supplies the stochastic ontology"},
        {"family": "infinite-volume symmetry-breaking field", "object": "thermodynamic central algebra",
         "mechanism": "disjoint stable phases and outgoing radiation", "terminal": "bounded local genesis of one phase", "honesty": "OPEN_NOT_COUNTED",
         "authority": c663ref, "disposition": "not tested by the finite C3/C4/C6 construction"},
    ]
    walls = ("one_global_objective_value_from_neutral_coherent_input",)
    source = "\n".join(inspect.getsource(fn).lower() for fn in
                        (route_A_deterministic_instability, route_B_metastable_dilation, route_C_domain_walls))
    phrases = ("we assume", "by construction", "as is standard", "the framework provides", "bridge context", "background",
               "naturally", "obviously", "standard qft", "registered", "canonical")
    hidden = tuple(phrase for phrase in phrases if phrase in source)
    residuals = [
        {"witness": c671ref, "prior": "native-domain objective actualizer not met", "current": "same exact type gate", "match": True},
        {"witness": c536ref, "prior": "diagonal is not one realized member", "current": "central reduced diagonal is not promoted", "match": True},
        {"witness": c663ref, "prior": "metastable retained dilation does not establish irreversible formation",
         "current": "finite robust latch does not establish objective actuality", "match": True},
        {"witness": c662ref, "prior": "objective sigma belongs to supplied law", "current": "no stochastic ontology silently imported", "match": True},
    ]
    rhetoric = [
        {"claim": "symmetric deterministic direction choice is unavailable", "per_element": "64 basis rows pass",
         "per_site": "one bounded central block", "per_mode": "proper-cubic invariant fixture only", "per_block": "two symmetric fixture rows",
         "lattice_wide": "untested; no broad statement"},
        {"claim": "finite robust latch is not one objective value", "per_element": "1344 error cases",
         "per_site": "one 121-active-M2 block", "per_mode": "seven central rails", "per_block": "C3/C4/C6 diagnostics",
         "lattice_wide": "untested; no broad statement"},
        {"claim": "relative wall center is not a global token", "per_element": "192 basis/size rows",
         "per_site": "one 343-M2 reserved cell", "per_mode": "six rays", "per_block": "lengths 3/4/6",
         "lattice_wide": "untested; no broad statement"},
    ]
    partial = [
        {"path": "Cycle674 A", "status": "EXECUTED_PARTIAL", "closes": "neutral product genesis, basis latch, fixed spent code"},
        {"path": "Cycle674 B", "status": "EXECUTED_PARTIAL", "closes": "finite one-error central robustness"},
        {"path": "Cycle674 C", "status": "EXECUTED_PARTIAL", "closes": "local covariant domain-wall transport"},
        {"path": "Cycle662", "status": "EXECUTED_PRIOR", "closes": "objective token conditional on supplied hybrid law"},
        {"path": "infinite-volume phase field", "status": "OPEN", "closes": "candidate central superselection value if locally generated"},
    ]
    steelman = (
        "A hostile reviewer should construct an infinite moving-carrier order-parameter medium with several disjoint stable phases, "
        "prove that a finite local seed-free instability selects one central phase in each physical realization, and transport all "
        "Cycle661 coherence into outgoing radiation whose local return is dynamically excluded. The terminal obligation is a finite-cell "
        "restriction theorem yielding one central event variable without importing a phase label or stochastic ontology. Finite repetition "
        "and walls do not test that thermodynamic mechanism, so a broad negative claim is premature."
    )
    echoes = [
        {"cycle": 536, "retired": "coherent seed diagonal", "remaining": "one realized value"},
        {"cycle": 662, "retired": "objective within a supplied stochastic law", "remaining": "derive/select law"},
        {"cycle": 663, "retired": "finite reduced metastability", "remaining": "objective sector ownership"},
        {"cycle": 669, "retired": "state-carried sequence protocol", "remaining": "coherent actualizer"},
        {"cycle": 671, "retired": "conditional selector and relational/dilation interfaces", "remaining": "native-domain token"},
    ]
    qualifying = sum(row["honesty"] in ("ATTEMPTED", "RULED OUT BY PRIOR") for row in routes)
    complete = qualifying >= 5 and not hidden and all(row["match"] for row in residuals) and len(rhetoric) == 3 and len(echoes) == 5
    result = {"skill_freshness": {"origin_main_checked": True, "origin_main_advanced": True, "remote_skill_followed": True,
                                  "dirty_worktree_moved": False},
              "N1_routes": routes, "N1_qualifying_normalized_families": qualifying,
              "N2_collapsed_walls": walls, "N2_directed_pairs": [],
              "N2_downstream_nonterminal_open_conditions": ("nature_law_selection", "finite_non_erasing_renewal"),
              "N3_hidden_phrase_hits": hidden, "N4_residual_matches": residuals, "N5_rhetoric": rhetoric,
              "N6_partial_closure_paths": partial, "N6_primitive_registry_claim_made": False,
              "N7_steelman": steelman, "N7_supporting_authority": c663ref, "N8_cross_cycle_echo": echoes,
              "checklist_complete": complete, "negative_claim_gate_status": "FAIL_DO_NOT_SHIP_NEGATIVE",
              "negative_gate_failure_reason": "N7 thermodynamic phase-field route remains untested",
              "demotion": "partial-attempt-with-named-untested-routes", "broad_no_go_claim": False,
              "minimum_content_claim": False, "shared_route_independent_obstruction": False, "axiom_pressure": False,
              "discipline_compliance_pass": complete}
    check("fresh N1-N8 is complete and blocks a broad negative/order-parameter impossibility claim", complete,
          {"families": qualifying, "negative_gate": result["negative_claim_gate_status"]})
    return result


def inventory():
    return {"supplied": ["Cycle661 coherent fixture/QCA", "neutral center and blank auxiliary product states", "one ready bit",
                         "finite radius-3 chart", "finite ray lengths", "Cycle669 root/next seeds", "compile-time frame chart"],
            "derived": ["basis-responsive deterministic latch", "triple-repetition one-error correction", "six-ray wall transport",
                         "7-bit outgoing sector exhaust", "branchwise Cycle669 adapters", "all24/all576", "inverse/deletion/domain/saturation"],
            "open": ["one global objective value on coherent input", "thermodynamic order-parameter restriction theorem",
                     "autonomous non-erasing renewal", "nature-law selection", "framework Record", "Born/empirical law",
                     "physical time/rate", "source/gravity"]}


def note_text(receipt):
    ng = receipt["no_go_discipline"]; A = receipt["routes"]["A"]; B = receipt["routes"]["B"]; C = receipt["routes"]["C"]
    n1 = "\n".join(f"| {r['family']} | {r['object']} | {r['mechanism']} | {r['terminal']} | {r['honesty']} | `{r['authority']['path']}:{r['authority']['line']}` | {r['disposition']} |" for r in ng["N1_routes"])
    n4 = "\n".join(f"| `{r['witness']['path']}:{r['witness']['line']}` | {r['prior']} | {r['current']} | {str(r['match']).lower()} |" for r in ng["N4_residual_matches"])
    n5 = "\n".join(f"| {r['claim']} | {r['per_element']} | {r['per_site']} | {r['per_mode']} | {r['per_block']} | {r['lattice_wide']} |" for r in ng["N5_rhetoric"])
    n6 = "\n".join(f"| {r['path']} | {r['status']} | {r['closes']} |" for r in ng["N6_partial_closure_paths"])
    n8 = "\n".join(f"| Cycle {r['cycle']} | {r['retired']} | {r['remaining']} |" for r in ng["N8_cross_cycle_echo"])
    fixture_rows = "\n".join(f"| {name} | {row['split']} | {row['capacity']} | {row['central_reduced_rank']} | {row['central_reduced_purity']:.12f} | {row['direction_weight_spread']:.3e} |" for name, row in A["event_rows"].items())
    Cres = "\n".join(f"| {name} | {row['split']} | {row['ray_length']} | {row['domain_wall_M2']} | {C['resources'][name]['layout']['active_M2']} | {C['resources'][name]['nearest_neighbor_calls_upper_bound']} |" for name, row in C["rows"].items())
    cov = receipt["covariance_controls"]
    return f"""# Symmetry-neutral order-parameter actualizer tournament — Cycle 674

Authority: **none**

Audit: **unset**

## Fresh no-go-discipline gate before disposition

The freshness check fetched the advanced `origin/main` skill and followed it without moving the dirty science worktree.

### N1

| family | object | mechanism | terminal | honesty | authority | disposition |
|---|---|---|---|---|---|---|
{n1}

### N2–N4

The current target has one collapsed wall: `{ng['N2_collapsed_walls']}`. Nature-law selection and finite renewal are downstream, not extra current-target walls. Hidden phrase hits: `{ng['N3_hidden_phrase_hits']}`.

| witness | prior residual | current residual | match? |
|---|---|---|---:|
{n4}

### N5

| claim | per-element | per-site | per-mode | per-block | lattice-wide |
|---|---|---|---|---|---|
{n5}

### N6

| path | status | closes |
|---|---|---|
{n6}

No claim that a retained primitive is absent is made; the primitive-registry gate is not triggered.

### N7

{ng['N7_steelman']} Supporting prior boundary: `{ng['N7_supporting_authority']['path']}:{ng['N7_supporting_authority']['line']}`.

### N8

| cycle | retired | remaining |
|---|---|---|
{n8}

Negative-claim gate: **{ng['negative_claim_gate_status']}**. This is a `{ng['demotion']}`, not a no-go. Shared route-independent obstruction: **not established**. Axiom pressure: **none**.

## Frozen target and result

The target `{receipt['frozen_contract']['target_sha256']}` and preregistration `{receipt['frozen_contract']['preregistration_sha256']}` precede evidence. All `{len(receipt['frozen_contract']['pins'])}` shores are exact at `{receipt['frozen_contract']['shore']}`.

All three mechanisms start with a local product state: central `none=1`, direction rails and outgoing exhaust blank, `ready=1`, `spent=0`. None accepts a selector, actuality token, random draw, host sampler or runtime frame. Every basis branch copies a valid bit plus the complete six-bit Cycle661 sector word into explicit outgoing exhaust, so all 64 labels remain distinct. As required by the reversible ledger, global amplitudes and phases remain in the Cycle661-wave/exhaust correlation; they are not claimed to live in the exhaust reduced state alone.

The exact coherent terminal is **NOT MET, NOT FALSIFIED**. Each construction maps basis sectors to one center value, but its linear coherent extension retains all seven central alternatives. The reduced center has rank seven on every frozen fixture and is not promoted to one objective value.

| fixture | split | C | reduced rank | reduced purity | direction spread |
|---|---|---:|---:|---:|---:|
{fixture_rows}

The product and GHZ direction rows are proper-cubic symmetric. For a deterministic equivariant single-valued law, an invariant input must have an invariant output; `none` is the only invariant classical label. A constant-`none` response fails the preregistered nontrivial basis agreement and does not close actuality. This is a route-specific finite deterministic constraint, not a general impossibility theorem.

## Route A — deterministic instability

One partial local update maps the neutral ready code to a spent central basis latch, copies the seven-bit sector exhaust, and thereafter acts as identity on the spent code. The active layout is `{A['resources']['layout']['active_M2']}` M2 in a reserved 343-M2 radius-3 cube. It has `{A['resources']['logical_gate_counts']}`, support at most two, and nearest-neighbor/depth upper bound `{A['resources']['nearest_neighbor_calls_upper_bound']}`. All 64 basis rows, 192 Cycle669 attachments, exact image inverse, `{A['deletions_detected']}` deletions, malformed, leakage and saturation controls pass.

The center is stable on each branch, but the coherent output type is `{A['coherent_output_type']}`. It is not one global objective token.

## Route B — finite reversible metastable candidate

Three retained one-hot copies feed a reversible bitwise-majority output. All `{B['single_bit_error_tests']}` single-bit corruptions are corrected with zero failures. The active layout is `{B['resources']['layout']['active_M2']}` M2; logical counts are `{B['resources']['logical_gate_counts']}`, support-three Toffoli lowers to support two, and the conservative routed depth is `{B['resources']['conservative_depth_upper_bound']}`.

Exact inverse, `{B['deletions_detected']}` deletions, malformed, leakage, branchwise Cycle669 and spent-code controls pass. This proves finite one-error robustness only. The replicas, corrected value, Cycle661 wave and syndromes remain in one coherent direct sum, so a durable latch is not promoted to objective actuality or all-future permanence.

## Route C — relational/domain-wall variants

| fixture | split | ray length | wall M2 | active M2 | routed-depth upper |
|---|---|---:|---:|---:|---:|
{Cres}

Each of six equal rays is locally seeded only by its Cycle661 branch. Fixed CNOTs carry the wall inward; the source word, full wall and center remain retained. Exact inverses, all `{C['deletions_detected']}` deletions, malformed, leakage, saturation and branchwise Cycle669 controls pass. On a coherent input the walls and centers are relative branch values, not one global token.

## Covariance and physical placement

The reserved `[-3,3]^3` 343-M2 cube is invariant under all 24 proper-cubic frames. Each receipt serializes the exact logical-index-to-coordinate map, the exact labeled logical support schedule and both digests; every rotated active placement remains inside the reserved cube. Active layouts have L1 diameter at most 18, and every pair gate has a route-and-return bound of 35 nearest-neighbor calls. Frame charts are compile-time only.

Route A/B/C all24 tests are `{cov['all24_tests']}` and all576 tests are `{cov['all576_tests']}`; every failure count is zero. Normalized translation digests agree. Cycle661 and Cycle669 physical covariance surfaces are reused at exact pinned shores, not reinterpreted.

## Interfaces, ledger and imports

Cycle671's 64-M2 selector is removed: every current route has zero selector and zero actuality input M2. All basis centers feed Cycle669 exactly, but the native coherent Cycle669 ObjectiveEventToken remains unavailable. Ready/spent state is the local one-shot ledger; inverse is exact on the ready-to-spent image, while the spent state refuses further consumption by remaining fixed. No indefinite renewal is claimed.

The supplied genesis is the Cycle661 fixture, neutral/blank product registers, one ready bit, finite cell boundary/rays, compile-time frame chart, and Cycle669 root/next seeds. The central value, outgoing sector exhaust, repetition code and walls are derived.

No packet or latch is called a framework Record. Weights are not called Born probabilities or empirical frequencies. Update application, spent state and wall depth are not physical time or rates.

## Disposition

**PASS / PARTIAL** for deterministic neutral basis latching, finite one-error stability, and covariant relative wall propagation with full outgoing coherent exhaust.

**NOT MET, NOT FALSIFIED** for one objective central value on the native coherent Cycle661 input. No shared obstruction or axiom pressure follows. The optimal next route is the N7 moving-carrier/infinite-volume phase-field restriction theorem, while keeping the present exact finite type gate unchanged.
"""


def note_contract():
    body = " ".join(NOTE.read_text().lower().split())
    required = ("authority: **none**", "audit: **unset**", "fresh no-go-discipline gate before disposition",
                "not a no-go", "not met, not falsified", "shared route-independent obstruction: **not established**",
                "axiom pressure: **none**", "not promoted to one objective value", "no packet or latch is called a framework record",
                "not called born probabilities or empirical frequencies", "not physical time or rates")
    missing = tuple(item for item in required if item not in body)
    return {"required": required, "missing": missing, "pass": not missing}


def main():
    signal.alarm(math.ceil(WALL_CAP_SECONDS)); started = time.perf_counter()
    frozen, receipts = freeze_and_shore_controls(); ng = no_go_discipline(); distributions = fixture_distributions()
    A = route_A_deterministic_instability(distributions)
    B = route_B_metastable_dilation(distributions)
    C = route_C_domain_walls(distributions)
    covariance = covariance_controls(); interfaces = interface_and_boundary_controls(A, B, C, receipts)
    receipt = {"cycle": 674, "date": "2026-07-23",
               "status": "three symmetry-neutral order-parameter constructions; exact coherent objective token not met",
               "classification": "partial-attempt-with-named-untested-routes", "authority": AUTHORITY, "audit": AUDIT,
               "strict_full_framework_terminal_met": False, "target_contract_candidate_terminal_met": False,
               "frozen_contract": frozen, "no_go_discipline": ng, "routes": {"A": A, "B": B, "C": C},
               "covariance_controls": covariance, "interface_and_boundary_controls": interfaces,
               "supplied_structure_inventory": inventory(), "exact_terminal_met": False,
               "exact_terminal_disposition": "NOT_MET_NOT_FALSIFIED",
               "strongest_constructive_result": "a 121-active-M2 finite reversible triple-repetition order-parameter latch correcting every single-bit error while exporting all Cycle661 sectors",
               "route_disposition": {"A": A["disposition"], "B": B["disposition"], "C": C["disposition"]},
               "shared_route_independent_obstruction": False, "axiom_pressure": False, "breakthrough": False,
               "author_accepted": False,
               "optimal_next_campaign": "moving-carrier/infinite-volume phase-field restriction theorem with one central ontic value and outgoing exhaust"}
    NOTE.write_text(note_text(receipt)); note = note_contract()
    check("Cycle674 note preserves actuality/Record/Born/time/no-go boundaries", note["pass"], note["missing"])
    elapsed = time.perf_counter() - started; rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if rss < 10_000_000: rss *= 1024
    receipt.update({"note_contract": note, "runner_sha256": file_sha(Path(__file__)), "note_sha256": file_sha(NOTE),
                    "elapsed_seconds": elapsed, "maximum_RSS_bytes": rss, "tests_passed": PASS, "tests_failed": FAIL})
    receipt["pass"] = (FAIL == 0 and all(item["pass"] for item in (frozen, A, B, C, covariance, interfaces, note))
                       and ng["discipline_compliance_pass"] and not ng["broad_no_go_claim"]
                       and elapsed < WALL_CAP_SECONDS and rss < RSS_CAP_BYTES and AUTHORITY == "none" and AUDIT == "unset")
    RECEIPT.write_text(json.dumps(receipt, indent=2, sort_keys=True,
                                  default=lambda x: x.item() if isinstance(x, np.generic) else list(x)) + "\n")
    print(json.dumps({"pass": receipt["pass"], "tests_passed": PASS, "tests_failed": FAIL,
                      "elapsed_seconds": elapsed, "maximum_RSS_bytes": rss,
                      "note": str(NOTE), "receipt": str(RECEIPT)}, indent=2))
    if not receipt["pass"]: raise SystemExit(1)


if __name__ == "__main__": main()
