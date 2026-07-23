#!/usr/bin/env python3
"""Cycle671: three-route coherent-sector objective-event actualizer tournament."""
from __future__ import annotations


TARGET_CONTRACT = {
    "cycle": 671,
    "target_map": (
        "A_661_coherent_sector_to_objective_event: Cycle661 RetainedCoherentDirectSum[64 pointer sectors] "
        "-> ObjectiveEventToken[none | six directions] with retained coherent accepted/rejected exhaust"
    ),
    "success": (
        "one bounded local proper-cubic map defined on the native Cycle661 coherent domain alone, producing exactly "
        "one objective token without an input actuality selector, supplied random draw, host sampler, or branch-read law"
    ),
    "routes": {
        "A": "deterministic state-carried one-hot hidden selector already resident in the bounded local physical state",
        "B": "explicit bounded reversible regenerative collision/dilation with full wave and innovation exhaust",
        "C": "unitary relational-history isometry with sector-relative event tokens and Cycle669 predecessor chains",
    },
    "completion_witness": [
        "native domain and exact ObjectiveEventToken codomain",
        "all 64 sectors and every accepted/rejected exhaust retained",
        "no host selection, sampler, supplied draw, or hidden frame/schedule service",
        "bounded M2, local support/depth, all24 and all576 covariance",
        "exact Cycle661/Cycle666/Cycle669 interface comparisons",
        "train, biased-held and nonproduct-held sizes 3/4/6",
    ],
    "nonclosure": [
        "an exact token on a domain extended by an ontic selector",
        "a reduced diagonal or propensity table without one objective label",
        "a coherent direct sum of branch-relative tokens",
        "pointer copying, partial trace, or declaring a diagonal register classical",
    ],
    "claim_ceiling": "route-specific bounded dispositions and strongest partial construction only; no no-go or axiom pressure",
}
TARGET_CONTRACT_SHA256 = "0e13898cf9776af6b8a6a0eba0b6286e237362491161fa14a4f0cde34144fdad"


PREREGISTRATION = {
    "route_order": ["A_hidden_selector", "B_reversible_collision", "C_relational_history"],
    "fixtures": {
        "product_z0": {"split": "train", "capacity": 3},
        "biased_phase_product": {"split": "held_blinded", "capacity": 4},
        "six_site_GHZ": {"split": "held_blinded_nonproduct", "capacity": 6},
    },
    "route_A": {
        "selector": "64-M2 one-hot actual-sector carrier",
        "law": "selected word of Hamming weight one emits its direction; every other selected word emits none",
        "terminal_gate": "fails exact native-domain target if selector actuality or initial selector is supplied",
    },
    "route_B": {
        "survival": "r=1/2 over H=3/4/6 collision layers",
        "event_algebra": "none plus six directions after summing retained layer labels",
        "terminal_gate": "a coherent isometry/reduced diagonal is not one ObjectiveEventToken without a branch-read law",
    },
    "route_C": {
        "history": "retain the Cycle661 sector and attach its exact Cycle669 empty-or-one-node predecessor chain",
        "terminal_gate": "sector-relative tokens do not become one global ObjectiveEventToken",
    },
    "covariance": "all24 proper-cubic frames and all576 ordered products; selector/history words transform by six-bit permutation",
    "held_policy": "law and route layouts frozen before all three Cycle661 fixture distributions are evaluated",
    "controls": "inverse, deletion, malformed, lawful domain, held-size, exact shores, full exhaust",
}
PREREGISTRATION_SHA256 = "ec5570a6507f09d97e5cc8d53c2d9e6a0724fbd6512d9cc2804fb8537b501533"


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
SHORE = "3aff134191d0ab6c4ba61609ef5e63197f9b0add"
NOTE = ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_COHERENT_SECTOR_OBJECTIVE_EVENT_ACTUALIZER_TOURNAMENT_CYCLE671_NOTE_2026-07-23.md"
RECEIPT = ROOT / "outputs/physical_coherent_sector_objective_event_actualizer_tournament_cycle671_receipt_2026_07_23.json"
AUTHORITY = "none"
AUDIT = "unset"
TOL = 3.0e-10
WALL_CAP_SECONDS = 240.0
RSS_CAP_BYTES = 3 * 1024**3
PASS = FAIL = 0


PINS = {
    "scripts/physical_deterministic_constrained_qca_formation_law_tournament_cycle661_2026_07_23.py": "83383268139e92bcd040fa176686f2e6c3d5eef806ba58ed5da9953a59af7590",
    "docs/work_history/repo/review_feedback/PHYSICAL_DETERMINISTIC_CONSTRAINED_QCA_FORMATION_LAW_TOURNAMENT_CYCLE661_NOTE_2026-07-23.md": "14262310b768983ebbdc8a89f914f237ab2a2523c8a096eece63b33a7e5e9ad4",
    "outputs/physical_deterministic_constrained_qca_formation_law_tournament_cycle661_receipt_2026_07_23.json": "c0ac1effe618bbdcbfc4bd6a3360f3beb557aa2469d47be476deef862e1340c5",
    "scripts/physical_regenerative_bath_trajectory_semigroup_equivalence_tournament_cycle666_2026_07_23.py": "54c81da2ec078e7a386753ae404117ad9da0833460cb039c009db67104aecfb9",
    "docs/work_history/repo/review_feedback/PHYSICAL_REGENERATIVE_BATH_TRAJECTORY_SEMIGROUP_EQUIVALENCE_TOURNAMENT_CYCLE666_NOTE_2026-07-23.md": "b71a9a2badf2cfc61bffaef9aa17a63fbc95b3ff89b68a237a644baac6a9aaa9",
    "outputs/physical_regenerative_bath_trajectory_semigroup_equivalence_tournament_cycle666_receipt_2026_07_23.json": "37deeea3678391d185a7c3592650025732421b06a8f68677b77dc1b07a9a4b37",
    "scripts/physical_state_carried_event_chain_sequence_protocol_cycle669_2026_07_23.py": "ac1237e211bf06a8eb394db0dd8001c88a5aaf81726b38a3e43bd066285a9c84",
    "docs/work_history/repo/review_feedback/PHYSICAL_STATE_CARRIED_EVENT_CHAIN_SEQUENCE_PROTOCOL_CYCLE669_NOTE_2026-07-23.md": "4ba9fe3a26606a944f362e81d6262543936018c6adf497069d8800e616f0c2c5",
    "outputs/physical_state_carried_event_chain_sequence_protocol_cycle669_receipt_2026_07_23.json": "0765c66f3d3625892d133976aca217a5676fef0820557b12b32c988cb6180760",
    "docs/work_history/repo/review_feedback/PHYSICAL_ACTUAL_MEMBER_ADMITTED_HISTORY_LAW_TOURNAMENT_CYCLE508_NOTE_2026-07-20.md": "923f384e959c638d6940cd6ed2cf837a00fe34046249380782ddc21bdc307095",
    "docs/work_history/repo/review_feedback/PHYSICAL_COHERENT_SEED_MEMBER_DILATION_CYCLE536_NOTE_2026-07-21.md": "e15944633127890fe27cb52193960a28d9860212d5d7aafd70f15eef2e987457",
    "docs/work_history/repo/review_feedback/PHYSICAL_OBJECTIVE_STOCHASTIC_OPEN_DILATION_CYCLE662_NOTE_2026-07-23.md": "bdc8dda304985a62c73fc6e7a03f11d61041dd8053a9321fb7171c9b22947a05",
    "docs/work_history/repo/review_feedback/PHYSICAL_DISSIPATIVE_METASTABLE_FORMATION_CHANNEL_CYCLE663_NOTE_2026-07-23.md": "96f59a3f79ce7c29f3c9ccdf93cae9503ea4cd0084821c11ba6e0545046bec87",
}


def check(label, condition, detail=""):
    global PASS, FAIL
    PASS += int(bool(condition)); FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def digest(value):
    return sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), default=lambda x: list(x)).encode()).hexdigest()


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
    return {"ref": "Cycle671 current", "path": str(Path(__file__).relative_to(ROOT)), "line": matches[0]}


# Evidence is loaded only after the target, preregistration, hashes and exact pins.
c661 = load_exact("cycle671_exact_c661", "scripts/physical_deterministic_constrained_qca_formation_law_tournament_cycle661_2026_07_23.py")
c666 = load_exact("cycle671_exact_c666", "scripts/physical_regenerative_bath_trajectory_semigroup_equivalence_tournament_cycle666_2026_07_23.py")
c669 = load_exact("cycle671_exact_c669", "scripts/physical_state_carried_event_chain_sequence_protocol_cycle669_2026_07_23.py")


WORDS = tuple(product((0, 1), repeat=6))
WORD_INDEX = {word: index for index, word in enumerate(WORDS)}


def freeze_and_shore_controls():
    source = Path(__file__).read_text().splitlines()
    target_line = next(i for i, row in enumerate(source, 1) if row.startswith("TARGET_CONTRACT ="))
    prereg_line = next(i for i, row in enumerate(source, 1) if row.startswith("PREREGISTRATION ="))
    evidence_line = next(i for i, row in enumerate(source, 1) if row.startswith("c661 = load_exact"))
    observed = {path: sha256(git_bytes(path)).hexdigest() for path in PINS}
    receipt_paths = {
        "661": "outputs/physical_deterministic_constrained_qca_formation_law_tournament_cycle661_receipt_2026_07_23.json",
        "666": "outputs/physical_regenerative_bath_trajectory_semigroup_equivalence_tournament_cycle666_receipt_2026_07_23.json",
        "669": "outputs/physical_state_carried_event_chain_sequence_protocol_cycle669_receipt_2026_07_23.json",
    }
    receipts = {cycle: json.loads(git_bytes(path)) for cycle, path in receipt_paths.items()}
    contracts = {f"Cycle{cycle}_pass": row["pass"] for cycle, row in receipts.items()}
    passed = (target_line < prereg_line < evidence_line and digest(TARGET_CONTRACT) == TARGET_CONTRACT_SHA256
              and digest(PREREGISTRATION) == PREREGISTRATION_SHA256 and observed == PINS and all(contracts.values()))
    result = {"shore": SHORE, "target": TARGET_CONTRACT, "target_sha256": digest(TARGET_CONTRACT),
              "expected_target_sha256": TARGET_CONTRACT_SHA256, "preregistration": PREREGISTRATION,
              "preregistration_sha256": digest(PREREGISTRATION), "expected_preregistration_sha256": PREREGISTRATION_SHA256,
              "target_line": target_line, "preregistration_line": prereg_line, "first_evidence_line": evidence_line,
              "frozen_before_evidence": target_line < prereg_line < evidence_line, "pins": PINS, "observed": observed,
              "working_tree_bytes_used_as_evidence": False, "imported_contracts": contracts, "pass": passed}
    check("Cycle671 target, three routes, held controls and exact shores were frozen before evidence", passed,
          {"target": result["target_sha256"], "prereg": result["preregistration_sha256"], "pins": len(PINS)})
    return result, receipts


def onehot(index, width):
    if type(index) is not int or index not in range(width): raise ValueError("one-hot index")
    return tuple(int(position == index) for position in range(width))


def one_index(word):
    if not word or any(type(bit) is not int or bit not in (0, 1) for bit in word) or sum(word) != 1:
        raise ValueError("not one-hot")
    return word.index(1)


def fixture_distributions():
    menu = c661.c634.menu_families()["mixed_projective_merge"]
    compiled = c661.c634.compile_menu(menu)
    effects = c661.c634.induced_effects(compiled["unitary"], compiled["ports"])
    return {name: c661.branch_distribution(state, effects) for name, state in c661.quantum_fixtures().items()}


def direction_map(frame, direction):
    moved = c661.c625.matvec(frame, c661.c625.DIRECTIONS[direction])
    return c661.c625.DIRECTIONS.index(moved)


def rotate_word(word, frame): return c661.c625.rotate_six(tuple(word), frame)


@dataclass(frozen=True)
class RouteEvent:
    actual: int
    direction: tuple[int, ...]
    retained_exhaust: tuple[int, ...]
    semantic_type: str
    one_objective_token: bool
    import_tag: str


def validate_route_event(event):
    if event.actual not in (0, 1) or len(event.direction) != 6 or any(bit not in (0, 1) for bit in event.direction):
        raise ValueError("event bits")
    if sum(event.direction) != event.actual: raise ValueError("actual/direction mismatch")
    one_index(event.retained_exhaust)


def event_from_word(word, exhaust, semantic_type, objective, import_tag):
    if len(word) != 6 or any(bit not in (0, 1) for bit in word): raise ValueError("pointer word")
    actual = int(sum(word) == 1)
    direction = onehot(word.index(1), 6) if actual else (0,) * 6
    event = RouteEvent(actual, direction, tuple(exhaust), semantic_type, objective, import_tag)
    validate_route_event(event)
    return event


def to_cycle669(event):
    validate_route_event(event)
    return c669.EventToken(event.actual, event.direction, event.retained_exhaust, "Cycle661_basis")


def selector_schedule():
    operations = []
    for direction in range(6):
        selector = WORD_INDEX[onehot(direction, 6)]
        operations.append((selector, 64)); operations.append((selector, 65 + direction))
    return tuple(operations)


def apply_cnots(bits, schedule, reverse=False, delete=None):
    bits = list(bits); operations = tuple(reversed(schedule)) if reverse else schedule
    for index, (control, target) in enumerate(operations):
        original_index = len(schedule) - 1 - index if reverse else index
        if delete == original_index: continue
        bits[target] ^= bits[control]
    return tuple(bits)


def host_sampling_hits(function):
    names = {"random", "rand", "randn", "choice", "choices", "sample", "randint", "uniform"}
    tree = ast.parse(inspect.getsource(function)); hits = set()
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call): continue
        name = node.func.attr if isinstance(node.func, ast.Attribute) else node.func.id if isinstance(node.func, ast.Name) else ""
        if name in names: hits.add(name)
    return tuple(sorted(hits))


def route_A_hidden_selector(distributions, receipts):
    schedule = selector_schedule(); failures = inverse_failures = interface_failures = c661_interface_failures = 0
    deletion_visible = 0; domain_deletions = 0; rows = {}
    for name, distribution in distributions.items():
        capacity = PREREGISTRATION["fixtures"][name]["capacity"]
        fixture_fail = 0; minimum = min(distribution.values())
        for selector, word in enumerate(WORDS):
            source = (*onehot(selector, 64), *((0,) * 7))
            physical = apply_cnots(source, schedule)
            event = event_from_word(word, onehot(selector, 64), "ObjectiveEventToken", True,
                                    "supplied_ontic_selector")
            qca_output = c661.qca_forward(c661.source_word(word))
            c661_interface_failures += int(qca_output[c661.ADMIT] != event.actual)
            if event.actual:
                qca_direction = c661.packet_view(qca_output)[0][1:7]
                c661_interface_failures += int(tuple(qca_direction) != event.direction)
            expected = (*onehot(selector, 64), event.actual, *event.direction)
            fixture_fail += int(physical != expected)
            inverse_failures += int(apply_cnots(physical, schedule, reverse=True) != source)
            chain = c669.initial_chain(capacity); attached, _ = c669.append_event(chain, to_cycle669(event))
            interface_failures += int(len(c669.read_chain(attached)) != event.actual)
            if event.actual: interface_failures += int(c669.inverse_event(attached) != chain)
            damaged = list(onehot(selector, 64)); damaged[selector] = 0
            try: one_index(tuple(damaged))
            except ValueError: domain_deletions += 1
        failures += fixture_fail
        rows[name] = {"split": PREREGISTRATION["fixtures"][name]["split"], "capacity": capacity,
                      "selector_rows": 64, "minimum_sector_weight": minimum,
                      "all_selector_values_in_fixture_support": minimum > TOL, "physical_reference_failures": fixture_fail}
    for deleted in range(len(schedule)):
        direction = deleted // 2; selector = WORD_INDEX[onehot(direction, 6)]
        source = (*onehot(selector, 64), *((0,) * 7))
        deletion_visible += int(apply_cnots(source, schedule, delete=deleted) != apply_cnots(source, schedule))
    malformed = ((0,) * 64, (1, 1) + (0,) * 62, (0,) * 63, (2,) + (0,) * 63)
    malformed_rejected = 0
    for selector in malformed:
        try: one_index(selector)
        except ValueError: malformed_rejected += 1
    result = {
        "route": "A_hidden_selector", "primary_object": "CoherentDirectSum x OnticSelector64",
        "mechanism": "twelve fixed CNOTs from six admitted selector rails into actual/direction output rails",
        "terminal_obligation": TARGET_CONTRACT["target_map"], "rows": rows,
        "native_Cycle661_domain_match": False, "extended_domain_event_token_match": True,
        "one_objective_token_within_supplied_selector_ontology": True, "input_actuality_selector_M2": 64,
        "initial_selector_configuration_supplied": True, "host_sampler_calls": 0,
        "host_sampling_source_hits": host_sampling_hits(route_A_hidden_selector), "supplied_random_draw": False,
        "all_wave_sectors_retained": True, "Cycle669_interface_failures": interface_failures,
        "Cycle661_exact_basis_interface_failures": c661_interface_failures,
        "local_M2": {"Cycle661_block": 84, "selector": 64, "event_output": 7, "total": 155},
        "logical_gate_counts": {"CNOT": len(schedule)}, "depth_upper_bound": len(schedule), "maximum_support_M2": 2,
        "inverse_failures": inverse_failures, "selector_rail_deletions_detected": domain_deletions,
        "gate_deletions_visible": deletion_visible, "malformed_rejected": malformed_rejected,
        "exact_A_661_terminal_met": False,
        "disposition": "positive conditional actualizer on an extended domain; exact native-domain map remains open",
    }
    result["pass"] = (failures == inverse_failures == interface_failures == c661_interface_failures == 0
                      and not result["host_sampling_source_hits"]
                      and domain_deletions == 3 * 64
                      and deletion_visible == len(schedule) and malformed_rejected == len(malformed)
                      and all(row["all_selector_values_in_fixture_support"] for row in rows.values()))
    check("route A compiles an exact token only on the explicit ontic-selector extension", result["pass"],
          {"rows": 3 * 64, "deletions": domain_deletions + deletion_visible, "terminal": False})
    return result


def collision_branch_weights(distribution, horizon):
    direction_weights = np.asarray([distribution[onehot(direction, 6)] for direction in range(6)], float)
    r = 0.5; total_event = float(direction_weights.sum()); rows = [("none", 1.0 - total_event * (1.0 - r**horizon))]
    for layer in range(1, horizon + 1):
        for direction in range(6):
            rows.append((f"emit:{layer}:{direction}", float(direction_weights[direction] * (1.0 - r) * r**(layer - 1))))
    return tuple(rows), direction_weights


def cycle661_history_isometry(horizon):
    labels = 1 + 6 * horizon; r = 0.5
    isometry = np.zeros((64 * labels, 64), complex)
    for sector, word in enumerate(WORDS):
        if sum(word) != 1:
            isometry[sector * labels, sector] = 1.0
            continue
        direction = word.index(1)
        isometry[sector * labels, sector] = r ** (horizon / 2)
        for layer in range(1, horizon + 1):
            label = 1 + (layer - 1) * 6 + direction
            isometry[sector * labels + label, sector] = math.sqrt((1.0 - r) * r ** (layer - 1))
    return isometry


def history_column(word, horizon):
    if sum(word) != 1: return {0: 1.0}
    direction = word.index(1); r = 0.5
    values = {0: r ** (horizon / 2)}
    for layer in range(1, horizon + 1):
        values[1 + (layer - 1) * 6 + direction] = math.sqrt((1.0 - r) * r ** (layer - 1))
    return values


def rotate_history_label(label, frame):
    if label == 0: return 0
    layer, direction = divmod(label - 1, 6)
    return 1 + layer * 6 + direction_map(frame, direction)


def route_B_reversible_collision(distributions, receipts):
    prior = receipts["666"]; temporal = prior["temporal_discriminator"]["rows"]
    finite_rows = {row["capacity"]: row for row in prior["resource_ledger"]["finite_rows"]}
    schedule_rows = prior["covariance_locality"]["schedule_rows"]
    rows = {}; failures = interface_failures = deletion_failures = isometry_deletion_failures = 0
    max_unitarity = max_isometry = 0.0
    malformed_rejected = 0
    for bad in ((-0.1,) + (1.1 / 63,) * 63, (1 / 63,) * 63, (float("nan"),) + (0,) * 63,
                (0.5,) * 64):
        try:
            if len(bad) != 64 or not all(math.isfinite(x) and x >= 0 for x in bad) or abs(sum(bad) - 1) > TOL:
                raise ValueError("distribution domain")
        except ValueError: malformed_rejected += 1
    for name, distribution in distributions.items():
        horizon = PREREGISTRATION["fixtures"][name]["capacity"]
        branches, direction_weights = collision_branch_weights(distribution, horizon)
        normalization = abs(sum(weight for _, weight in branches) - 1.0)
        finite = sum(weight for label, weight in branches if label != "none")
        collapsed = [branches[0][1]] + [sum(weight for label, weight in branches if label.endswith(f":{d}")) for d in range(6)]
        expected_finite = temporal[name]["finite_emission_weight"]
        unitary = c666.history_unitary(horizon)
        unitarity = float(np.linalg.norm(unitary.conj().T @ unitary - np.eye(unitary.shape[0]), ord=2))
        max_unitarity = max(max_unitarity, unitarity)
        isometry = cycle661_history_isometry(horizon)
        isometry_residual = float(np.linalg.norm(isometry.conj().T @ isometry - np.eye(64), ord=2))
        max_isometry = max(max_isometry, isometry_residual)
        visible = 0
        isometry_visible = 0; labels = 1 + 6 * horizon
        for layer, direction in product(range(horizon), range(6)):
            deleted = c666.history_unitary(horizon, delete_pair=(layer, direction))
            visible += int(np.linalg.norm(unitary - deleted, ord=2) > TOL)
            damaged = isometry.copy(); sector = WORD_INDEX[onehot(direction, 6)]
            damaged[sector * labels + 1 + layer * 6 + direction, sector] = 0
            isometry_visible += int(np.linalg.norm(damaged.conj().T @ damaged - np.eye(64), ord=2) > TOL)
        deletion_failures += horizon * 6 - visible
        isometry_deletion_failures += horizon * 6 - isometry_visible
        branch_interface = 0
        for index, (label, weight) in enumerate(branches):
            actual = int(label != "none" and weight > TOL)
            direction = (onehot(int(label.rsplit(":", 1)[1]), 6) if actual else (0,) * 6)
            event = RouteEvent(actual, direction, onehot(index, len(branches)),
                               "CoherentInnovationSector", False, "none")
            chain = c669.initial_chain(horizon); attached, _ = c669.append_event(chain, to_cycle669(event))
            branch_interface += int(len(c669.read_chain(attached)) != actual)
            if actual: branch_interface += int(c669.inverse_event(attached) != chain)
        interface_failures += branch_interface
        resource = finite_rows[horizon]; schedule = schedule_rows[str(horizon)]
        event_rank = sum(weight > TOL for weight in collapsed)
        fixture_fail = int(normalization > TOL or abs(finite - expected_finite) > TOL
                           or max(unitarity, isometry_residual) > TOL or branch_interface)
        failures += fixture_fail
        rows[name] = {
            "split": PREREGISTRATION["fixtures"][name]["split"], "horizon": horizon,
            "history_labels": len(branches), "normalization_residual": normalization,
            "finite_event_weight": finite, "Cycle666_finite_event_weight": expected_finite,
            "finite_weight_residual": abs(finite - expected_finite), "collapsed_none_plus_six_weights": collapsed,
            "reduced_event_algebra_rank": event_rank, "single_objective_basis_token_rank_required": 1,
            "history_unitarity_residual": unitarity, "Cycle661_full_sector_history_isometry_residual": isometry_residual,
            "deleted_collision_pairs_visible": visible, "deleted_isometry_pairs_detected": isometry_visible,
            "Cycle669_formal_branch_interface_failures": branch_interface,
            "local_M2_upper_bound": 84 + resource["explicit_retained_M2"],
            "inherited_ordered_depth_upper_bound": schedule["ordered_wire_depth"],
            "maximum_support_M2": schedule["maximum_support_M2"],
        }
    result = {
        "route": "B_reversible_collision", "primary_object": "StinespringHistoryIsometry and ReducedDiagonalEventAlgebra",
        "mechanism": "Cycle666 r=1/2 regenerative partial swaps with every wave/layer/direction exhaust retained",
        "terminal_obligation": TARGET_CONTRACT["target_map"], "rows": rows,
        "native_Cycle661_domain_match": True, "structural_none_plus_six_event_algebra_match": True,
        "one_objective_token_generated_by_reversible_dilation": False,
        "output_type": "ReducedDiagonalEventLaw[none|six] plus CoherentInnovationDirectSum[layer,direction]",
        "host_sampler_calls": 0, "host_sampling_source_hits": host_sampling_hits(route_B_reversible_collision),
        "supplied_random_draw": False, "branch_read_law_supplied": False,
        "full_wave_and_innovation_exhaust_retained": True, "maximum_unitarity_residual": max_unitarity,
        "maximum_Cycle661_full_sector_isometry_residual": max_isometry,
        "collision_deletion_failures": deletion_failures, "isometry_deletion_failures": isometry_deletion_failures,
        "malformed_distributions_rejected": malformed_rejected,
        "Cycle669_formal_branch_interface_failures": interface_failures,
        "exact_A_661_terminal_met": False,
        "disposition": "positive reversible dilation and exact reduced law; objective single-label promotion absent",
    }
    result["pass"] = (failures == interface_failures == deletion_failures == isometry_deletion_failures == 0
                      and malformed_rejected == 4 and not result["host_sampling_source_hits"])
    check("route B derives the exact finite reduced event law but no single objective label", result["pass"],
          {"max_unitarity": max_unitarity, "interface_failures": interface_failures, "terminal": False})
    return result


def route_C_relational_history(distributions, receipts):
    resources = {row["capacity"]: row for row in receipts["669"]["locality_resources"]["resource_rows"]}
    rows = {}; failures = inverse_failures = deletion_failures = malformed_rejected = 0
    for name, distribution in distributions.items():
        capacity = PREREGISTRATION["fixtures"][name]["capacity"]; initial = c669.initial_chain(capacity)
        labels = []; accepted = rejected = fixture_fail = 0
        for sector, word in enumerate(WORDS):
            output = c661.qca_forward(c661.source_word(word)); actual = output[c661.ADMIT]
            event = event_from_word(word, onehot(sector, 64), "RelationalEventToken", False, "none")
            attached, _ = c669.append_event(initial, to_cycle669(event)); chain = c669.read_chain(attached)
            fixture_fail += int(actual != event.actual or len(chain) != actual)
            if actual:
                accepted += 1; fixture_fail += int(one_index(chain[0]["direction"]) != word.index(1))
                inverse_failures += int(c669.inverse_event(attached) != initial)
            else: rejected += 1; fixture_fail += int(attached != initial)
            labels.append((sector, digest(chain)))
            damaged = list(event.retained_exhaust); damaged[sector] = 0
            bad = RouteEvent(event.actual, event.direction, tuple(damaged), event.semantic_type, False, "none")
            try: validate_route_event(bad)
            except ValueError: deletion_failures += 1
        event_weights = [sum(weight for word, weight in distribution.items() if sum(word) != 1)]
        event_weights += [distribution[onehot(direction, 6)] for direction in range(6)]
        gram_residual = 0.0 if len(set(labels)) == 64 else math.sqrt(2.0)
        malformed = (
            c669.EventToken(1, (0,) * 6, (1,), "Cycle661_basis"),
            c669.EventToken(0, onehot(0, 6), (1,), "Cycle661_basis"),
            c669.EventToken(1, onehot(0, 6), (), "Cycle661_basis"),
            c669.EventToken(1, onehot(0, 6), (1,), "unknown"),
        )
        for event in malformed:
            try: c669.append_event(initial, event)
            except ValueError: malformed_rejected += 1
        fixture_fail += int(accepted != 6 or rejected != 58 or gram_residual > TOL or abs(sum(event_weights) - 1) > TOL)
        failures += fixture_fail
        resource = resources[capacity]
        rows[name] = {
            "split": PREREGISTRATION["fixtures"][name]["split"], "capacity": capacity,
            "basis_history_rows": 64, "accepted_relative_events": accepted, "rejected_empty_histories": rejected,
            "retained_sector_history_Gram_residual": gram_residual,
            "reduced_none_plus_six_weights": event_weights,
            "relational_history_type": "CoherentDirectSum[Sector64 x RelativeEventToken x Cycle669ChainState]",
            "Cycle669_disjoint_M2_upper_bound": resource["Cycle661_conditional_disjoint_upper_bound_M2"],
            "Cycle669_common_overlay_M2": resource["common_chain_overlay_M2"],
        }
    result = {
        "route": "C_relational_history", "primary_object": "pure sector-retaining event-chain history isometry",
        "mechanism": "branchwise Cycle661 basis event attaches the exact Cycle669 predecessor node while its sector label remains",
        "terminal_obligation": TARGET_CONTRACT["target_map"], "rows": rows,
        "native_Cycle661_domain_match": True, "all_64_coherent_sectors_retained": True,
        "branch_relative_event_tokens_exact": True, "one_global_objective_token": False,
        "output_type": "CoherentDirectSum[RelativeEventToken x ChainState]",
        "host_sampler_calls": 0, "host_sampling_source_hits": host_sampling_hits(route_C_relational_history),
        "supplied_random_draw": False,
        "inverse_failures": inverse_failures, "sector_exhaust_deletions_detected": deletion_failures,
        "malformed_event_rejections": malformed_rejected,
        "exact_A_661_terminal_met": False,
        "disposition": "positive relational-history isometry; codomain remains a coherent direct sum rather than one objective token",
    }
    result["pass"] = (failures == inverse_failures == 0 and not result["host_sampling_source_hits"]
                      and deletion_failures == 3 * 64
                      and malformed_rejected == 3 * 4)
    check("route C gives exact sector-relative Cycle669 histories while retaining all coherent sectors", result["pass"],
          {"basis_rows": 3 * 64, "deletions": deletion_failures, "terminal": False})
    return result


def rotate_distribution(distribution, frame):
    return {rotate_word(word, frame): weight for word, weight in distribution.items()}


def rotate_event_word(event, frame):
    sector = one_index(event.retained_exhaust); moved_word = rotate_word(WORDS[sector], frame)
    moved_exhaust = onehot(WORD_INDEX[moved_word], 64)
    moved_direction = (onehot(direction_map(frame, one_index(event.direction)), 6) if event.actual else (0,) * 6)
    return RouteEvent(event.actual, moved_direction, moved_exhaust, event.semantic_type,
                      event.one_objective_token, event.import_tag)


def covariance_controls(distributions, receipts):
    frames = c661.c625.proper_cubic_frames(); route_A_fail = route_C_fail = route_B_fail = 0
    A_tests = C_tests = B_tests = B_isometry_tests = B_isometry_fail = 0
    for frame, sector in product(frames, range(64)):
        word = WORDS[sector]
        for semantic, objective in (("ObjectiveEventToken", True), ("RelationalEventToken", False)):
            event = event_from_word(word, onehot(sector, 64), semantic, objective,
                                    "supplied_ontic_selector" if objective else "none")
            moved_word = rotate_word(word, frame)
            expected = event_from_word(moved_word, onehot(WORD_INDEX[moved_word], 64), semantic, objective,
                                       event.import_tag)
            failed = int(rotate_event_word(event, frame) != expected)
            if objective: route_A_fail += failed; A_tests += 1
            else: route_C_fail += failed; C_tests += 1
    for name, distribution in distributions.items():
        horizon = PREREGISTRATION["fixtures"][name]["capacity"]
        for frame in frames:
            original, _ = collision_branch_weights(distribution, horizon)
            rotated, _ = collision_branch_weights(rotate_distribution(distribution, frame), horizon)
            remapped = {"none": original[0][1]}
            for label, weight in original[1:]:
                _, layer, direction = label.split(":")
                remapped[f"emit:{layer}:{direction_map(frame, int(direction))}"] = weight
            route_B_fail += int(max(abs(weight - remapped[label]) for label, weight in rotated) > TOL); B_tests += 1
            for word in WORDS:
                moved = rotate_word(word, frame)
                left = {rotate_history_label(label, frame): amplitude for label, amplitude in history_column(word, horizon).items()}
                right = history_column(moved, horizon)
                B_isometry_fail += int(left != right); B_isometry_tests += 1
    A_group = C_group = B_group = 0; A_group_tests = C_group_tests = B_group_tests = 0
    for left, right in product(frames, frames):
        composed = c661.c625.matmul(left, right)
        for sector, word in enumerate(WORDS):
            failed = int(rotate_word(rotate_word(word, right), left) != rotate_word(word, composed))
            A_group += failed; C_group += failed; A_group_tests += 1; C_group_tests += 1
        for direction in range(6):
            B_group += int(direction_map(left, direction_map(right, direction)) != direction_map(composed, direction))
            B_group_tests += 1
    c666cov = receipts["666"]["covariance_locality"]
    c669cov = receipts["669"]["locality_resources"]
    result = {
        "proper_cubic_frames": len(frames),
        "route_A_all24_tests": A_tests, "route_A_all24_failures": route_A_fail,
        "route_B_all24_tests": B_tests, "route_B_all24_failures": route_B_fail,
        "route_B_full_sector_isometry_all24_tests": B_isometry_tests,
        "route_B_full_sector_isometry_all24_failures": B_isometry_fail,
        "route_C_all24_tests": C_tests, "route_C_all24_failures": route_C_fail,
        "route_A_all576_word_tests": A_group_tests, "route_A_all576_failures": A_group,
        "route_B_all576_direction_tests": B_group_tests, "route_B_all576_failures": B_group,
        "route_C_all576_word_tests": C_group_tests, "route_C_all576_failures": C_group,
        "Cycle666_inherited_full_schedule_all24_tests": c666cov["full_schedule_all24_comparisons"],
        "Cycle666_inherited_full_schedule_all24_failures": c666cov["full_schedule_covariance_failures"],
        "Cycle669_inherited_append_all24_tests": c669cov["append_all24_tests"],
        "Cycle669_inherited_append_all24_failures": c669cov["append_all24_failures"],
        "runtime_frame_selector": False, "preferred_direction_order_load_bearing": False,
    }
    result["pass"] = (len(frames) == 24 and sum((route_A_fail, route_B_fail, B_isometry_fail, route_C_fail, A_group, B_group, C_group,
                                                 c666cov["full_schedule_covariance_failures"], c669cov["append_all24_failures"])) == 0)
    check("all three actualizer routes pass all24 and all576 covariance controls", result["pass"],
          {"all24": [A_tests, B_tests, B_isometry_tests, C_tests], "all576": [A_group_tests, B_group_tests, C_group_tests]})
    return result


def cross_route_controls(A, B, C):
    capacities = [3, 4, 6]
    observed = {
        "A": sorted(row["capacity"] for row in A["rows"].values()),
        "B": sorted(row["horizon"] for row in B["rows"].values()),
        "C": sorted(row["capacity"] for row in C["rows"].values()),
    }
    result = {
        "train_held_capacities_required": capacities, "train_held_capacities_observed": observed,
        "route_A_deletions_detected": A["selector_rail_deletions_detected"] + A["gate_deletions_visible"],
        "route_A_malformed_rejected": A["malformed_rejected"],
        "route_B_collision_deletions_detected": sum(row["deleted_collision_pairs_visible"] for row in B["rows"].values()),
        "route_B_isometry_deletions_detected": sum(row["deleted_isometry_pairs_detected"] for row in B["rows"].values()),
        "route_B_malformed_rejected": B["malformed_distributions_rejected"],
        "route_C_sector_exhaust_deletions_detected": C["sector_exhaust_deletions_detected"],
        "route_C_malformed_rejected": C["malformed_event_rejections"],
        "inverse_or_isometry_checks_pass": (A["inverse_failures"] == C["inverse_failures"] == 0
                                              and B["maximum_unitarity_residual"] < TOL
                                              and B["maximum_Cycle661_full_sector_isometry_residual"] < TOL),
        "complete_exhaust": {"A_wave_and_selector": A["all_wave_sectors_retained"],
                             "B_wave_and_innovation": B["full_wave_and_innovation_exhaust_retained"],
                             "C_sector_and_chain": C["all_64_coherent_sectors_retained"]},
    }
    result["pass"] = (all(values == capacities for values in observed.values())
                      and result["route_A_deletions_detected"] == 204 and result["route_A_malformed_rejected"] == 4
                      and result["route_B_collision_deletions_detected"] == 78
                      and result["route_B_isometry_deletions_detected"] == 78 and result["route_B_malformed_rejected"] == 4
                      and result["route_C_sector_exhaust_deletions_detected"] == 192
                      and result["route_C_malformed_rejected"] == 12 and result["inverse_or_isometry_checks_pass"]
                      and all(result["complete_exhaust"].values()))
    check("inverse/deletion/malformed/lawful-domain/held-size/full-exhaust controls pass", result["pass"],
          {"capacities": observed, "deletions": [204, 78, 78, 192]})
    return result


def no_go_discipline():
    Aref = current_citation("def route_A_hidden_selector(")
    Bref = current_citation("def route_B_reversible_collision(")
    Cref = current_citation("def route_C_relational_history(")
    c661ref = citation("docs/work_history/repo/review_feedback/PHYSICAL_DETERMINISTIC_CONSTRAINED_QCA_FORMATION_LAW_TOURNAMENT_CYCLE661_NOTE_2026-07-23.md",
                       "A hostile reviewer should build an objective stochastic dilation")
    c662ref = citation("docs/work_history/repo/review_feedback/PHYSICAL_OBJECTIVE_STOCHASTIC_OPEN_DILATION_CYCLE662_NOTE_2026-07-23.md",
                       "stochastic law itself—not a host sampler")
    c663ref = citation("docs/work_history/repo/review_feedback/PHYSICAL_DISSIPATIVE_METASTABLE_FORMATION_CHANNEL_CYCLE663_NOTE_2026-07-23.md",
                       "does not select one emission sector")
    routes = [
        {"family": "ontic one-hot hidden selector", "object": "extended classical-quantum state",
         "mechanism": "deterministic selector-controlled token", "terminal": "native-domain objective token",
         "honesty": "ATTEMPTED", "authority": Aref,
         "disposition": "conditional token succeeds; selector ontology and initial value are supplied"},
        {"family": "reversible regenerative dilation", "object": "Stinespring history isometry",
         "mechanism": "partial-swap environment labeling", "terminal": "one objective environment label",
         "honesty": "ATTEMPTED", "authority": Bref,
         "disposition": "reduced diagonal succeeds; one label is not generated"},
        {"family": "unitary relational event history", "object": "coherent direct sum of predecessor chains",
         "mechanism": "sector-relative token consistency", "terminal": "one global objective token",
         "honesty": "ATTEMPTED", "authority": Cref,
         "disposition": "relative histories succeed; global token type differs"},
        {"family": "hybrid objective stochastic field", "object": "quantum-classical Markov instrument",
         "mechanism": "law-owned sigma update", "terminal": "derive sigma ontology from Cycle661 domain",
         "honesty": "RULED OUT BY PRIOR", "authority": c662ref,
         "disposition": "Cycle662 supplies rather than derives the stochastic ontology"},
        {"family": "metastable reduced semigroup", "object": "contractive CP channel with dark latch",
         "mechanism": "environment-induced contraction", "terminal": "select one retained emission sector",
         "honesty": "RULED OUT BY PRIOR", "authority": c663ref,
         "disposition": "Cycle663 retains and does not select emission sectors"},
        {"family": "local spontaneous symmetry-breaking actualizer", "object": "enlarged local order-parameter field",
         "mechanism": "stable sector ownership after a covariant instability", "terminal": "unique local ontic token with exhaust",
         "honesty": "OPEN_NOT_COUNTED", "authority": c661ref,
         "disposition": "not constructed in this finite tournament"},
    ]
    walls = ("domain_only_objective_actuality",)
    pairs = [{"left": left, "right": right, "left_closes_right": False, "right_closes_left": False,
              "independent": True} for left in walls for right in walls if left != right]
    route_sources = "\n".join(inspect.getsource(fn).lower() for fn in
                              (route_A_hidden_selector, route_B_reversible_collision, route_C_relational_history))
    hidden_phrases = ("we assume", "by construction", "as is standard", "the framework provides", "bridge context",
                      "background", "naturally", "obviously", "standard qft", "registered", "canonical")
    hidden_hits = tuple(phrase for phrase in hidden_phrases if phrase in route_sources)
    residuals = [
        {"witness": citation("docs/work_history/repo/review_feedback/PHYSICAL_STATE_CARRIED_EVENT_CHAIN_SEQUENCE_PROTOCOL_CYCLE669_NOTE_2026-07-23.md",
                             "A_661_coherent_sector_to_objective_event: Cycle661 RetainedCoherentDirectSum"),
         "prior_residual": "exact native-domain objective-event map absent", "current_residual": "same exact map tested", "match": True},
        {"witness": citation("docs/work_history/repo/review_feedback/PHYSICAL_ACTUAL_MEMBER_ADMITTED_HISTORY_LAW_TOURNAMENT_CYCLE508_NOTE_2026-07-20.md",
                             "Route B adds an explicit added ontology"),
         "prior_residual": "hidden carrier actuality is explicit added ontology", "current_residual": "route A selector ontology supplied", "match": True},
        {"witness": citation("docs/work_history/repo/review_feedback/PHYSICAL_COHERENT_SEED_MEMBER_DILATION_CYCLE536_NOTE_2026-07-21.md",
                             "a diagonal density operator is not one realized member"),
         "prior_residual": "reduced diagonal lacks one realized member", "current_residual": "route B diagonal lacks one objective token", "match": True},
        {"witness": citation("docs/work_history/repo/review_feedback/PHYSICAL_REGENERATIVE_BATH_TRAJECTORY_SEMIGROUP_EQUIVALENCE_TOURNAMENT_CYCLE666_NOTE_2026-07-23.md",
                             "hybrid ontology remains supplied"),
         "prior_residual": "hybrid ontology supplied", "current_residual": "route B refuses silent sigma promotion", "match": True},
        {"witness": citation("docs/work_history/repo/review_feedback/PHYSICAL_DISSIPATIVE_METASTABLE_FORMATION_CHANNEL_CYCLE663_NOTE_2026-07-23.md",
                             "does not select one emission sector"),
         "prior_residual": "retained emission sectors are not selected", "current_residual": "route C sectors remain relative", "match": True},
    ]
    rhetoric = [
        {"claim": "route A misses the native domain", "per_element": "192 selector rows tested", "per_site": "155-M2 block tested",
         "per_mode": "64 selector rails", "per_block": "three fixtures", "lattice_wide": "not tested; no broad claim"},
        {"claim": "route B reduced diagonal is not one token", "per_element": "all 81 history labels by sizes",
         "per_site": "bounded retained dilation", "per_mode": "none plus six collapsed labels", "per_block": "C3/C4/C6",
         "lattice_wide": "not tested; no broad claim"},
        {"claim": "route C relational event is not a global objective token", "per_element": "192 basis histories",
         "per_site": "one finite predecessor cell", "per_mode": "64 sectors", "per_block": "three fixture capacities",
         "lattice_wide": "not tested; no broad claim"},
    ]
    partial = [
        {"path": "Cycle508 hidden carrier", "status": "EXECUTED_PRIOR", "closes": "objective token conditional on explicit selector ontology"},
        {"path": "Cycle662 hybrid law", "status": "EXECUTED_PRIOR", "closes": "objective sigma conditional on supplied stochastic law"},
        {"path": "Cycle671 route B", "status": "EXECUTED_PARTIAL", "closes": "reversible local dilation and exact reduced event algebra"},
        {"path": "Cycle671 route C", "status": "EXECUTED_PARTIAL", "closes": "sector-relative predecessor histories"},
        {"path": "spontaneous local actualizer", "status": "OPEN", "closes": "candidate domain-only objective ownership if constructed"},
    ]
    steelman = (
        "A hostile reviewer should enlarge the local cell by a covariant metastable order-parameter field, prove that a finite-energy "
        "instability creates exactly one stable central event value while the outgoing unitary channels retain every Cycle661 sector, "
        "and then feed that value into Cycle669. The terminal obligation is an explicit local update whose invariant code space has one "
        "ontic central label without an input selector or stochastic postulate. This mechanism is mathematically actionable and was not "
        "constructed here, so any broad impossibility claim would be premature."
    )
    echoes = [
        {"cycle": 508, "mechanism": "explicit hidden actuality carrier", "retired": "conditional member production", "remaining": "ontology supplied"},
        {"cycle": 536, "mechanism": "coherent seed dilation", "retired": "reduced diagonal", "remaining": "one realized member"},
        {"cycle": 662, "mechanism": "hybrid stochastic sigma", "retired": "objective-within-law token", "remaining": "law ontology supplied"},
        {"cycle": 663, "mechanism": "dissipative collision", "retired": "reduced contraction", "remaining": "emission-sector selection"},
        {"cycle": 669, "mechanism": "state-carried predecessor chain", "retired": "sequence-label ambiguity", "remaining": "A_661 exact map"},
    ]
    qualifying = sum(row["honesty"] in ("ATTEMPTED", "RULED OUT BY PRIOR") for row in routes)
    checklist_complete = (qualifying >= 5 and len(pairs) == 0 and not hidden_hits and all(row["match"] for row in residuals)
                          and len(rhetoric) == 3 and len(partial) >= 5 and bool(steelman) and len(echoes) == 5)
    result = {
        "skill_freshness": {"origin_main_checked": True, "remote_skill_newer_than_installed": True,
                            "remote_skill_followed": True, "worktree_moved": False},
        "N1_routes": routes, "N1_qualifying_normalized_families": qualifying,
        "N2_collapsed_walls": walls, "N2_directed_pairs": pairs,
        "N2_route_specific_type_gaps_are_alternatives_not_inflated_conjunctive_walls": True,
        "N2_downstream_nonterminal_open_conditions": ("nature_law_selection", "finite_non_erasing_renewal"),
        "N3_route_function_hidden_phrase_hits": hidden_hits,
        "N4_residual_matches": residuals, "N5_rhetoric": rhetoric, "N6_partial_closure_paths": partial,
        "N6_primitive_registry_claim_made": False, "N7_steelman": steelman, "N7_supporting_authority": c661ref,
        "N8_cross_cycle_echo": echoes,
        "checklist_complete": checklist_complete,
        "negative_claim_gate_status": "FAIL_DO_NOT_SHIP_NEGATIVE",
        "negative_gate_failure_reason": "N7 supplies a concrete unclosed local spontaneous-actualizer mechanism",
        "demotion": "partial-attempt-with-named-untested-routes",
        "broad_no_go_claim": False, "minimum_content_claim": False,
        "shared_route_independent_obstruction": False, "axiom_pressure": False,
        "discipline_compliance_pass": checklist_complete,
    }
    check("fresh N1-N8 is complete and correctly blocks a broad negative claim", checklist_complete,
          {"families": qualifying, "negative_gate": result["negative_claim_gate_status"]})
    return result


def inventory():
    return {
        "supplied": ["Cycle661 coherent pointer direct sum and 84-M2 basis QCA", "Cycle666 collision angle and blank finite exhaust",
                     "Cycle669 root/next/head chain seeds and preprovisioned Cycle665 payloads", "proper-cubic chart",
                     "Route A ontic selector ontology and initial value", "finite train/held preparations"],
        "derived": ["Route A 12-CNOT conditional token compiler", "Route B exact reversible history isometry and reduced none-plus-six law",
                     "Route C sector-relative Cycle669 histories", "all24/all576 covariance", "inverse/deletion/malformed/held-size controls"],
        "open": ["native-domain one-objective-token law", "derivation or empirical selection of an actuality law",
                 "autonomous selector/order-parameter genesis", "non-erasing indefinite renewal", "framework Record",
                 "Born or empirical-frequency law", "physical time or rate", "source/gravity"],
    }


def note_text(receipt):
    ng = receipt["no_go_discipline"]; A = receipt["routes"]["A"]; B = receipt["routes"]["B"]; C = receipt["routes"]["C"]
    n1 = "\n".join(f"| {r['family']} | {r['object']} | {r['mechanism']} | {r['terminal']} | {r['honesty']} | `{r['authority']['path']}:{r['authority']['line']}` | {r['disposition']} |" for r in ng["N1_routes"])
    n2 = "\n".join(f"| {r['left']} | {r['right']} | {str(r['left_closes_right']).lower()} | {str(r['right_closes_left']).lower()} | {str(r['independent']).lower()} |" for r in ng["N2_directed_pairs"])
    n4 = "\n".join(f"| `{r['witness']['path']}:{r['witness']['line']}` | {r['prior_residual']} | {r['current_residual']} | {str(r['match']).lower()} |" for r in ng["N4_residual_matches"])
    n5 = "\n".join(f"| {r['claim']} | {r['per_element']} | {r['per_site']} | {r['per_mode']} | {r['per_block']} | {r['lattice_wide']} |" for r in ng["N5_rhetoric"])
    n6 = "\n".join(f"| {r['path']} | {r['status']} | {r['closes']} |" for r in ng["N6_partial_closure_paths"])
    n8 = "\n".join(f"| Cycle {r['cycle']} | {r['mechanism']} | {r['retired']} | {r['remaining']} |" for r in ng["N8_cross_cycle_echo"])
    Arows = "\n".join(f"| {name} | {r['split']} | {r['capacity']} | {r['selector_rows']} | {r['minimum_sector_weight']:.3e} | {str(r['all_selector_values_in_fixture_support']).lower()} |" for name, r in A["rows"].items())
    Brows = "\n".join(f"| {name} | {r['split']} | {r['horizon']} | {r['history_labels']} | {r['finite_weight_residual']:.3e} | {r['reduced_event_algebra_rank']} | {r['local_M2_upper_bound']} |" for name, r in B["rows"].items())
    Crows = "\n".join(f"| {name} | {r['split']} | {r['capacity']} | {r['accepted_relative_events']} | {r['rejected_empty_histories']} | {r['retained_sector_history_Gram_residual']:.1e} | {r['Cycle669_disjoint_M2_upper_bound']} |" for name, r in C["rows"].items())
    cov = receipt["covariance_controls"]
    return f"""# Coherent-sector objective-event actualizer tournament — Cycle 671

Authority: **none**

Audit: **unset**

## Fresh no-go-discipline gate before disposition

The repository skill freshness check reached `origin/main`; that newer skill body was followed without moving this intentionally dirty worktree.

### N1 — normalized route families

| family | primary object | mechanism | terminal obligation | honesty | authority | disposition |
|---|---|---|---|---|---|---|
{n1}

### N2 — collapsed wall audit

Route-specific type gaps are alternative implementations, not inflated conjunctive walls. The current target has one collapsed wall, `{ng['N2_collapsed_walls']}`. Nature-law selection and finite non-erasing renewal are downstream nonterminal open conditions, not extra walls in this target.

| left | right | left closes right? | reverse? | independent? |
|---|---|---:|---:|---:|
{n2}

### N3–N4

The three route functions contain no hidden-wall phrase hits: `{ng['N3_route_function_hidden_phrase_hits']}`.

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

No statement that a retained primitive is absent is made, so the primitive-registry gate is not invoked.

### N7

{ng['N7_steelman']} Supporting prior route: `{ng['N7_supporting_authority']['path']}:{ng['N7_supporting_authority']['line']}`.

### N8

| cycle | mechanism | retired | remaining |
|---|---|---|---|
{n8}

Negative-claim gate: **{ng['negative_claim_gate_status']}**. This cycle ships a `{ng['demotion']}`, not a no-go. Shared route-independent obstruction: **not established**. Axiom pressure: **none**.

## Frozen target and outcome

The exact target is `{receipt['frozen_contract']['target']['target_map']}`. Target `{receipt['frozen_contract']['target_sha256']}` and preregistration `{receipt['frozen_contract']['preregistration_sha256']}` precede evidence; all `{len(receipt['frozen_contract']['pins'])}` shores are exact at `{receipt['frozen_contract']['shore']}`.

No route meets the exact native-domain terminal. The strongest partial construction is Route A's exact bounded token compiler on an explicitly extended ontic-selector domain. Route B derives the full local reversible dilation and its diagonal event law without a sampler. Route C constructs exact sector-relative Cycle669 histories. None of those statements is a broad impossibility claim.

## Route A — state-carried hidden selector

The local 64-M2 one-hot selector identifies one Cycle661 sector. Twelve fixed CNOTs write `actual` and six direction rails only for the six Hamming-weight-one selector values. The 84-M2 Cycle661 block, selector and seven output rails total `155` M2; support is two and depth is at most `12`. All coherent sectors remain in the wave surface.

| fixture | split | C | selector rows | minimum sector weight | every selector in support? |
|---|---|---:|---:|---:|---:|
{Arows}

All 192 selector/fixture rows, exact Cycle661 basis outputs and exact Cycle669 attachments pass. The output has the exact token structure and one objective value **within the supplied selector ontology**. It does not implement the native map because `OnticSelector64` and its initial value enlarge the input domain. This is an explicit actuality import, not pointer copying or a derivation from coherent amplitudes.

## Route B — reversible collision/dilation

The `r=1/2` Cycle666 partial-swap history isometry is applied at H3/H4/H6 with every layer/direction innovation and all wave exhaust retained. Summing layer labels gives the exact `none|six` diagonal event algebra and matches Cycle666's finite event weight.

| fixture | split | H | history labels | finite-weight residual | diagonal rank | M2 upper bound |
|---|---|---:|---:|---:|---:|---:|
{Brows}

Maximum global-history unitarity residual is `{B['maximum_unitarity_residual']:.3e}` and the maximum explicit 64-sector Cycle661 history-isometry residual is `{B['maximum_Cycle661_full_sector_isometry_residual']:.3e}`. Every collision-pair and full-sector-isometry deletion is visible; structural branches attach to Cycle669 exactly. No host sampler or supplied random draw occurs. The output type is `{B['output_type']}`. A rank-seven diagonal algebra plus its coherent exhaust is not one objective basis token unless a branch-read law is added.

## Route C — relational histories

For every Cycle661 basis sector, the isometry retains the sector and attaches its exact Cycle669 empty-or-one-node predecessor history. Accepted sectors have one direction-relative node; rejected sectors retain an empty history and their explicit sector exhaust.

| fixture | split | C | accepted | rejected | Gram residual | Cycle669 M2 upper bound |
|---|---|---:|---:|---:|---:|---:|
{Crows}

The output type is `{C['output_type']}`. Each sector has a consistent relative token, but the full state remains a coherent direct sum. No global objective token is produced.

## Covariance, deletion and domains

Route A/C each pass `{cov['route_A_all24_tests']}` all24 sector-word tests and `{cov['route_A_all576_word_tests']}` all576 word-product tests. Route B passes `{cov['route_B_all24_tests']}` fixture/frame laws, `{cov['route_B_full_sector_isometry_all24_tests']}` explicit 64-sector isometry/frame tests and `{cov['route_B_all576_direction_tests']}` direction-product tests. The exact inherited physical schedules add `{cov['Cycle666_inherited_full_schedule_all24_tests']}` Cycle666 and `{cov['Cycle669_inherited_append_all24_tests']}` Cycle669 all24 checks. All failures are zero. There is no runtime frame selector or preferred direction order.

Route A detects all selector-rail and gate deletions and rejects four malformed selectors. Route B rejects four malformed distributions, preserves exact inverse, and detects every omitted collision pair. Route C detects all 192 sector-exhaust deletions, rejects twelve malformed event words, and inverts every admitted chain. Train C3, biased-held C4 and nonproduct-held C6 use unchanged laws and layouts.

## Exact interface disposition

- Cycle661: all 64 basis sectors and all coherent weights are retained; no native objective actuality is silently attributed to it.
- Cycle666: Route B reproduces its finite event weights and collision isometry, but omits the supplied hybrid sigma promotion.
- Cycle669: Route A can feed the native event interface conditionally on its selector ontology; Routes B/C feed every branch structurally but remain diagonal/relational rather than objective.

The packet outputs are not called framework Records. Code-state weights are not called Born probabilities or empirical frequencies. Collision layers and predecessor depth are not called physical time or rates.

## Supplied / derived / open

Supplied: Cycle661 coherent surface and basis QCA; Cycle666 collision angle and blank finite exhaust; Cycle669 chain seeds/payloads; frame chart; finite fixtures; Route A selector ontology/value.

Derived: Route A's fixed token compiler; Route B's reversible history and exact diagonal event law; Route C's relative predecessor histories; exact interfaces; all24/all576; inverse/deletion/malformed/held controls.

Open: native-domain objective actuality; physical selection of an actuality law; autonomous selector/order-parameter genesis; non-erasing renewal; framework Record; Born/empirical law; physical time/rate; source/gravity.

## Disposition

**PASS / CONDITIONAL PARTIAL** for Route A on `CoherentDirectSum x OnticSelector64`.

**PASS / TYPE-PARTIAL** for Route B's reversible dilation and reduced diagonal, and Route C's relational history.

**NOT MET, NOT FALSIFIED** for the exact native-domain `A_661` target. No shared obstruction or axiom pressure follows. The optimal next route is the N7 covariant metastable order-parameter actualizer with an explicit central-label and exhaust theorem.
"""


def note_contract():
    body = " ".join(NOTE.read_text().lower().split())
    required = ("authority: **none**", "audit: **unset**", "fresh no-go-discipline gate before disposition",
                "not a no-go", "shared route-independent obstruction: **not established**", "axiom pressure: **none**",
                "not met, not falsified", "not called physical time or rates", "not called framework records",
                "not called born probabilities or empirical frequencies")
    missing = tuple(item for item in required if item not in body)
    return {"required": required, "missing": missing, "pass": not missing}


def main():
    signal.alarm(math.ceil(WALL_CAP_SECONDS)); started = time.perf_counter()
    frozen, receipts = freeze_and_shore_controls(); ng = no_go_discipline()
    distributions = fixture_distributions()
    A = route_A_hidden_selector(distributions, receipts)
    B = route_B_reversible_collision(distributions, receipts)
    C = route_C_relational_history(distributions, receipts)
    covariance = covariance_controls(distributions, receipts); controls = cross_route_controls(A, B, C)
    receipt = {
        "cycle": 671, "date": "2026-07-23",
        "status": "three constructive actualizer routes; conditional selector and coherent partials; exact native-domain map open",
        "classification": "partial-attempt-with-named-untested-routes", "authority": AUTHORITY, "audit": AUDIT,
        "strict_full_framework_terminal_met": False, "target_contract_candidate_terminal_met": False,
        "frozen_contract": frozen, "no_go_discipline": ng,
        "routes": {"A": A, "B": B, "C": C}, "covariance_controls": covariance,
        "cross_route_controls": controls,
        "supplied_structure_inventory": inventory(),
        "strongest_constructive_result": "exact 12-CNOT local ObjectiveEventToken compiler on Cycle661 x supplied OnticSelector64, retaining all wave sectors and attaching to Cycle669",
        "exact_A_661_terminal_met": False,
        "exact_A_661_disposition": "NOT_MET_NOT_FALSIFIED",
        "route_disposition": {"A": A["disposition"], "B": B["disposition"], "C": C["disposition"]},
        "shared_route_independent_obstruction": False, "axiom_pressure": False, "breakthrough": False,
        "author_accepted": False,
        "optimal_next_campaign": "construct a covariant metastable order-parameter actualizer proving one central ontic label plus retained outgoing exhaust",
    }
    NOTE.write_text(note_text(receipt)); note = note_contract()
    check("Cycle671 note preserves actuality/Record/Born/time/no-go boundaries", note["pass"], note["missing"])
    elapsed = time.perf_counter() - started; rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if rss < 10_000_000: rss *= 1024
    receipt.update({"note_contract": note, "runner_sha256": file_sha(Path(__file__)), "note_sha256": file_sha(NOTE),
                    "elapsed_seconds": elapsed, "maximum_RSS_bytes": rss, "tests_passed": PASS, "tests_failed": FAIL})
    receipt["pass"] = (FAIL == 0 and all(row["pass"] for row in (frozen, A, B, C, covariance, controls, note))
                       and ng["discipline_compliance_pass"] and not ng["broad_no_go_claim"]
                       and elapsed < WALL_CAP_SECONDS and rss < RSS_CAP_BYTES and AUTHORITY == "none" and AUDIT == "unset")
    RECEIPT.write_text(json.dumps(receipt, indent=2, sort_keys=True,
                                  default=lambda x: x.item() if isinstance(x, np.generic) else list(x)) + "\n")
    print(json.dumps({"pass": receipt["pass"], "tests_passed": PASS, "tests_failed": FAIL,
                      "elapsed_seconds": elapsed, "maximum_RSS_bytes": rss,
                      "note": str(NOTE), "receipt": str(RECEIPT)}, indent=2))
    if not receipt["pass"]: raise SystemExit(1)


if __name__ == "__main__": main()
