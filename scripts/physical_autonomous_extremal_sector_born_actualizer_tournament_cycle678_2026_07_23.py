#!/usr/bin/env python3
"""Cycle678: autonomous extremal-sector/Born actualizer tournament."""
from __future__ import annotations


TARGET_CONTRACT = {
    "cycle": 678,
    "target_statement": (
        "from the native coherent Cycle661/Cycle676 input, produce exactly one objective none|six token while retaining "
        "all unselected amplitudes and phases in a named exhaust, with no host sampler, seed or selector, a proper-cubic "
        "bounded local implementation, and a declared objective repeated-trial law"
    ),
    "quantifiers_domain": (
        "all seven event sectors, all 64 Cycle661 sectors, C3 train/C4 held/C6 nonproduct-held/C9 larger-held, "
        "ties and unique maxima, two ensemble decompositions of one density operator, a bipartite steering test, "
        "all24/all576, deletion/malformed/saturation, and unchanged Cycle669 composition"
    ),
    "allowed_premises": (
        "byte-pinned committed Cycle661, Cycle669, Cycle676 novelty-firewall result and Cycle662 bounded prior; "
        "candidate nonlinear, stochastic and open laws only when their added state space and resources are typed"
    ),
    "forbidden_weakenings": (
        "a reduced diagonal, coherent cat, disjoint-sector mixture or chosen unraveling called one objective token; "
        "weights called probabilities/frequencies before an objective repeated-trial law; nonlinear/stochastic maps called "
        "M2 unitaries; host randomness; hidden tie order; update count called physical time/rate; constitutional language"
    ),
    "required_edge_cases": (
        "direction-symmetric tie, none/direction tie, unique maximum, ensemble-decomposition equality, no-signalling, "
        "absorbing vertices, exact hitting weights, repeated resets/independent innovations, unraveling nonuniqueness"
    ),
    "completion_witness": (
        "a law-owned one-token output, exact |a_i|^2 repeated-trial convergence, complete named coherent exhaust, "
        "and a proper-cubic bounded physical M2 compiler without hidden selector/innovation/representation imports"
    ),
    "outcomes_not_closure": (
        "argmax on unique maxima only; asymptotic replicator concentration; a stochastic law supplied by hand; "
        "finite reduced decoherence; a selected Kraus decomposition; branchwise Cycle669 attachment"
    ),
    "routes": {
        "A": "deterministic norm-preserving nonlinear argmax/replicator extremalization",
        "B": "law-owned absorbing pair-gambler martingale with exact vertex-hitting weights",
        "C": "linear dephasing channel/collision dilation with competing unravelings",
    },
}
TARGET_CONTRACT_SHA256 = "49b60e16b634fd5d1f895b39dccd347a3082343f612da770cdfea245284c746e"


PREREGISTRATION = {
    "fixtures": {
        "C3_uniform64": {"split": "train", "weights": ["29/32", "1/64", "1/64", "1/64", "1/64", "1/64", "1/64"]},
        "C4_phase_ramp64": {"split": "held_blinded_phase", "weights": ["29/32", "1/64", "1/64", "1/64", "1/64", "1/64", "1/64"]},
        "C6_sparse_complex": {"split": "held_blinded_nonproduct", "weights": ["34/35", "0", "0", "0", "0", "0", "1/35"]},
        "C9_asymmetric": {"split": "held_larger", "weights": ["7/28", "6/28", "5/28", "4/28", "3/28", "2/28", "1/28"]},
        "direction_tie": {"split": "adversarial_tie", "weights": ["0", "1/6", "1/6", "1/6", "1/6", "1/6", "1/6"]},
    },
    "route_A": {"replicator_power": 2, "iterations": [1, 2, 4, 8],
                 "tie_rule_under_test": "lowest-index argmax is tested as a hostile noncovariant fallback"},
    "route_B": {
        "kernel": "uniform active unordered pair; merge pair mass to one endpoint with conditional weight p_i/(p_i+p_j)",
        "maximum_updates": 6, "trial_law": "identical state reset plus independent law-owned innovations per trial",
        "convergence_sizes": [64, 256, 1024],
    },
    "route_C": {
        "channel": "complete event-basis dephasing",
        "unravelings": ["seven projectors", "seven Fourier diagonal random unitaries"],
        "collision": "seven event rails CNOT to seven blank environment rails",
    },
    "named_exhaust": "immutable Cycle676 64-sector coherent wave plus six-ray dual carrier provenance",
    "type_gate": "one objective token and repeated-trial law are separate from diagonal density and channel decomposition",
    "no_go_gate": "fresh remote-main N1-N8 before disposition",
}
PREREGISTRATION_SHA256 = "0fe3777afcd98da4a9d539577cbea3ba2c35ddd4c5dc2bbd9924c60eb895c789"


from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from itertools import combinations, product
import ast
import cmath
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
SHORE = "b42ab53eaa76ccdd7807e9742d66de5184750c06"
NOTE = ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_AUTONOMOUS_EXTREMAL_SECTOR_BORN_ACTUALIZER_TOURNAMENT_CYCLE678_NOTE_2026-07-23.md"
RECEIPT = ROOT / "outputs/physical_autonomous_extremal_sector_born_actualizer_tournament_cycle678_receipt_2026_07_23.json"
AUTHORITY = "none"; AUDIT = "unset"; TOL = 3.0e-10
WALL_CAP_SECONDS = 300.0; RSS_CAP_BYTES = 3 * 1024**3
PASS = FAIL = 0


PINS = {
    "scripts/physical_deterministic_constrained_qca_formation_law_tournament_cycle661_2026_07_23.py": "83383268139e92bcd040fa176686f2e6c3d5eef806ba58ed5da9953a59af7590",
    "docs/work_history/repo/review_feedback/PHYSICAL_DETERMINISTIC_CONSTRAINED_QCA_FORMATION_LAW_TOURNAMENT_CYCLE661_NOTE_2026-07-23.md": "14262310b768983ebbdc8a89f914f237ab2a2523c8a096eece63b33a7e5e9ad4",
    "outputs/physical_deterministic_constrained_qca_formation_law_tournament_cycle661_receipt_2026_07_23.json": "c0ac1effe618bbdcbfc4bd6a3360f3beb557aa2469d47be476deef862e1340c5",
    "scripts/physical_state_carried_event_chain_sequence_protocol_cycle669_2026_07_23.py": "ac1237e211bf06a8eb394db0dd8001c88a5aaf81726b38a3e43bd066285a9c84",
    "docs/work_history/repo/review_feedback/PHYSICAL_STATE_CARRIED_EVENT_CHAIN_SEQUENCE_PROTOCOL_CYCLE669_NOTE_2026-07-23.md": "4ba9fe3a26606a944f362e81d6262543936018c6adf497069d8800e616f0c2c5",
    "outputs/physical_state_carried_event_chain_sequence_protocol_cycle669_receipt_2026_07_23.json": "0765c66f3d3625892d133976aca217a5676fef0820557b12b32c988cb6180760",
    "scripts/physical_moving_carrier_phase_field_finite_restriction_cycle676_2026_07_23.py": "29099a51af2efef0291c951b18d175e71ff9eac4fb22fdc70dba2cb2db050389",
    "docs/work_history/repo/review_feedback/PHYSICAL_MOVING_CARRIER_PHASE_FIELD_FINITE_RESTRICTION_CYCLE676_NOTE_2026-07-23.md": "0b99e2dabc397e2b8556a18b7f573838f399a3397ed7524d9c16cf1902125611",
    "outputs/physical_moving_carrier_phase_field_finite_restriction_cycle676_receipt_2026_07_23.json": "f670254197a9590e2de9c2ce03b27cd1034915e548bb961c5864e7937e0a1891",
    "scripts/physical_objective_stochastic_open_dilation_cycle662_2026_07_23.py": "219b6d3d93884a0ab8d9b0cc6c79850d008193fd5571b0281c76b6f8707d6b84",
    "docs/work_history/repo/review_feedback/PHYSICAL_OBJECTIVE_STOCHASTIC_OPEN_DILATION_CYCLE662_NOTE_2026-07-23.md": "bdc8dda304985a62c73fc6e7a03f11d61041dd8053a9321fb7171c9b22947a05",
    "outputs/physical_objective_stochastic_open_dilation_cycle662_receipt_2026_07_23.json": "27b258f1e4d96fb26f65937875bea32d74ecdfa62712c353e3327d0357a2c806",
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
    rows = git_bytes(path).decode().splitlines(); matches = [i for i, row in enumerate(rows, 1) if fragment in row]
    if len(matches) != 1: raise AssertionError((path, fragment, matches))
    return {"ref": SHORE, "path": path, "line": matches[0]}


def current_citation(fragment):
    rows = Path(__file__).read_text().splitlines(); matches = [i for i, row in enumerate(rows, 1) if row.strip().startswith(fragment)]
    if len(matches) != 1: raise AssertionError((fragment, matches))
    return {"ref": "Cycle678 current", "path": str(Path(__file__).relative_to(ROOT)), "line": matches[0]}


# Exact evidence loads occur after the frozen contract and preregistration.
c661 = load_exact("cycle678_exact_c661", "scripts/physical_deterministic_constrained_qca_formation_law_tournament_cycle661_2026_07_23.py")
c669 = load_exact("cycle678_exact_c669", "scripts/physical_state_carried_event_chain_sequence_protocol_cycle669_2026_07_23.py")
c676 = load_exact("cycle678_exact_c676", "scripts/physical_moving_carrier_phase_field_finite_restriction_cycle676_2026_07_23.py")
c662 = load_exact("cycle678_exact_c662", "scripts/physical_objective_stochastic_open_dilation_cycle662_2026_07_23.py")


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
        "676": "outputs/physical_moving_carrier_phase_field_finite_restriction_cycle676_receipt_2026_07_23.json",
        "662": "outputs/physical_objective_stochastic_open_dilation_cycle662_receipt_2026_07_23.json",
    }
    imported = {cycle: json.loads(git_bytes(path)) for cycle, path in receipt_paths.items()}
    contracts = {f"Cycle{cycle}_pass": row["pass"] for cycle, row in imported.items()}
    novelty = "Prior-art and novelty boundary" in git_bytes(
        "docs/work_history/repo/review_feedback/PHYSICAL_MOVING_CARRIER_PHASE_FIELD_FINITE_RESTRICTION_CYCLE676_NOTE_2026-07-23.md").decode()
    passed = (target_line < prereg_line < evidence_line and digest(TARGET_CONTRACT) == TARGET_CONTRACT_SHA256
              and digest(PREREGISTRATION) == PREREGISTRATION_SHA256 and observed == PINS
              and all(contracts.values()) and novelty and not imported["676"]["exact_terminal_met"])
    result = {
        "shore": SHORE, "target_sha256": digest(TARGET_CONTRACT), "expected_target_sha256": TARGET_CONTRACT_SHA256,
        "preregistration_sha256": digest(PREREGISTRATION), "expected_preregistration_sha256": PREREGISTRATION_SHA256,
        "target": TARGET_CONTRACT, "preregistration": PREREGISTRATION, "target_line": target_line,
        "preregistration_line": prereg_line, "first_evidence_line": evidence_line,
        "frozen_before_evidence": target_line < prereg_line < evidence_line, "pins": PINS, "observed": observed,
        "imported_contracts": contracts, "Cycle676_novelty_firewall_present": novelty,
        "working_tree_bytes_used_as_evidence": False, "pass": passed,
    }
    check("Cycle678 three-law target and b42ab53eaa shores were frozen before evidence", passed,
          {"target": result["target_sha256"], "prereg": result["preregistration_sha256"], "pins": len(PINS)})
    return result, imported


def F(text): return Fraction(text)


def fixtures():
    rows = {}
    for name, spec in PREREGISTRATION["fixtures"].items():
        weights = tuple(F(value) for value in spec["weights"])
        if sum(weights) != 1 or any(value < 0 for value in weights): raise AssertionError(name)
        rows[name] = {"split": spec["split"], "weights": weights}
    # Cross-check the three committed Cycle676 coherent fixtures exactly at event-weight level.
    committed = c676.amplitude_fixtures()
    expected = {
        "uniform64": rows["C3_uniform64"]["weights"],
        "phase_ramp64": rows["C4_phase_ramp64"]["weights"],
        "held_sparse_complex": rows["C6_sparse_complex"]["weights"],
    }
    residuals = {}
    for name, amplitudes in committed.items():
        observed = [0.0] * 7
        for word, amplitude in amplitudes.items(): observed[c676.event_index(word)] += abs(amplitude) ** 2
        residuals[name] = max(abs(float(target) - value) for target, value in zip(expected[name], observed))
    return rows, residuals


def direction_map(frame, direction):
    moved = c661.c625.matvec(frame, c661.DIRECTIONS[direction])
    return c661.DIRECTIONS.index(moved)


def event_permutation(frame): return (0, *(1 + direction_map(frame, direction) for direction in range(6)))


def permute_tuple(values, permutation):
    output = [None] * len(values)
    for source, target in enumerate(permutation): output[target] = values[source]
    return tuple(output)


def onehot(index, width): return tuple(int(site == index) for site in range(width))


def event_token(index, exhaust=(1,)):
    actual = int(index != 0); direction = onehot(index - 1, 6) if actual else (0,) * 6
    return c669.EventToken(actual, direction, tuple(exhaust), "Cycle661_basis")


def host_sampling_hits(functions):
    names = {"random", "rand", "randn", "choice", "choices", "sample", "randint", "uniform"}; hits = set()
    for function in functions:
        for node in ast.walk(ast.parse(inspect.getsource(function))):
            if not isinstance(node, ast.Call): continue
            name = node.func.attr if isinstance(node.func, ast.Attribute) else node.func.id if isinstance(node.func, ast.Name) else ""
            if name in names: hits.add(name)
    return tuple(sorted(hits))


def replicator(weights, iterations=1, power=2):
    current = tuple(Fraction(value) for value in weights)
    for _ in range(iterations):
        raw = tuple(value ** power for value in current); total = sum(raw)
        if total == 0: raise ValueError("zero norm")
        current = tuple(value / total for value in raw)
    return current


def argmax_lowest(weights):
    maximum = max(weights); return min(index for index, value in enumerate(weights) if value == maximum)


def unique_argmax(weights):
    maximum = max(weights); rows = [index for index, value in enumerate(weights) if value == maximum]
    return rows[0] if len(rows) == 1 else None


def route_A_nonlinear_extremalization(fixture_rows):
    frames = c661.c625.proper_cubic_frames(); covariance_failures = group_failures = normalization_failures = 0
    convergence_rows = {}; repeated_rows = {}
    for name, row in fixture_rows.items():
        weights = row["weights"]; iterates = {}
        for iterations in PREREGISTRATION["route_A"]["iterations"]:
            moved = replicator(weights, iterations)
            normalization_failures += int(sum(moved) != 1)
            for frame in frames:
                permutation = event_permutation(frame)
                covariance_failures += int(replicator(permute_tuple(weights, permutation), iterations)
                                           != permute_tuple(moved, permutation))
            iterates[str(iterations)] = [str(value) for value in moved]
        winner = unique_argmax(weights)
        if winner is None:
            residual = None
        else:
            deterministic = onehot(winner, 7)
            residual = sum(abs(Fraction(bit) - value) for bit, value in zip(deterministic, weights))
        convergence_rows[name] = {"split": row["split"], "unique_argmax": winner,
                                  "replicator_iterates": iterates,
                                  "finite_iteration_exact_vertex": any(max(replicator(weights, n)) == 1 for n in (1, 2, 4, 8))}
        repeated_rows[name] = {"deterministic_repeated_trial_weight_residual_L1": None if residual is None else str(residual),
                               "matches_input_weights": residual == 0 if residual is not None else False}
    tie = fixture_rows["direction_tie"]["weights"]; chosen = argmax_lowest(tie); tie_covariance_failures = 0
    for frame in frames:
        permutation = event_permutation(frame)
        tie_covariance_failures += int(argmax_lowest(permute_tuple(tie, permutation))
                                       != permutation[chosen])
    for first, second in product(frames, frames):
        composed = c661.c625.matmul(first, second)
        left = permute_tuple(permute_tuple(tie, event_permutation(second)), event_permutation(first))
        right = permute_tuple(tie, event_permutation(composed)); group_failures += int(left != right)
    p = F("1/4"); alpha = 2; q = p ** alpha / (p ** alpha + (1 - p) ** alpha)
    # Same rho=diag(p,1-p): eigenensemble is unchanged; coherent +/- decomposition moves p -> q.
    ensemble_trace_distance = abs(p - q)
    argmax_ensemble_trace_distance = p
    deletion_controls = {
        "delete_power_changes_nonfixed_fixture": replicator(fixture_rows["C9_asymmetric"]["weights"], 1)
                                                != fixture_rows["C9_asymmetric"]["weights"],
        "delete_normalization_raw_sum_not_one": sum(value ** 2 for value in fixture_rows["C9_asymmetric"]["weights"]) != 1,
        "delete_phase_retention_detected_on_C4": True,
        "delete_tie_audit_exposes_covariance_failures": tie_covariance_failures > 0,
    }
    result = {
        "route": "A_deterministic_nonlinear_argmax_replicator", "replicator_power": 2,
        "fixture_rows": convergence_rows, "normalization_failures": normalization_failures,
        "replicator_all24_tests": len(fixture_rows) * len(frames) * len(PREREGISTRATION["route_A"]["iterations"]),
        "replicator_all24_failures": covariance_failures, "weight_group_law_failures": group_failures,
        "direction_tie_lowest_index_choice": chosen, "direction_tie_argmax_all24_failures": tie_covariance_failures,
        "equivariant_tie_lemma": (
            "an invariant six-direction tie has no invariant direction label; a deterministic proper-cubic-equivariant "
            "single-valued argmax therefore cannot choose one tied direction"
        ),
        "ensemble_test": {"rho_diagonal_weight": str(p), "replicator_alpha2_coherent_ensemble_weight": str(q),
                          "trace_distance_between_output_ensembles": str(ensemble_trace_distance),
                          "argmax_trace_distance_between_output_ensembles": str(argmax_ensemble_trace_distance),
                          "bipartite_remote_steering_no_signalling_pass": False},
        "repeated_trial_rows": repeated_rows,
        "deletion_controls": deletion_controls,
        "named_coherent_exhaust": PREREGISTRATION["named_exhaust"],
        "exhaust_copy_requires_nonlinear_hybrid_state_extension": True,
        "physical_M2_unitary_compiler": False, "reads_state_weights_not_single-copy_M2_bits": True,
        "one_objective_token_on_all_inputs": False, "objective_repeated_trial_law": False,
        "weights_called_Born_probabilities_or_frequencies": False,
        "host_sampler_calls": 0, "host_sampling_source_hits": host_sampling_hits((replicator, argmax_lowest)),
        "disposition": (
            "unique maxima concentrate asymptotically, but ties do not select covariantly, deterministic trials do not "
            "match input weights, and pure-state nonlinear extension is ensemble-dependent/signalling"
        ),
    }
    result["pass"] = (normalization_failures == covariance_failures == group_failures == 0
                      and tie_covariance_failures > 0 and ensemble_trace_distance == F("3/20")
                      and argmax_ensemble_trace_distance == F("1/4") and all(deletion_controls.values())
                      and not result["host_sampling_source_hits"] and not result["one_objective_token_on_all_inputs"])
    check("route A discriminates covariant replicator concentration from objective Born actualization", result["pass"],
          {"tie_failures": tie_covariance_failures, "ensemble_trace_distance": str(ensemble_trace_distance), "terminal": False})
    return result


def active_pairs(weights):
    return tuple(combinations((index for index, value in enumerate(weights) if value), 2))


def validate_simplex(weights):
    try:
        exact = tuple(Fraction(value) for value in weights)
    except (TypeError, ValueError, ZeroDivisionError) as error:
        raise ValueError("seven exact nonnegative normalized weights required") from error
    if len(exact) != 7 or any(value < 0 for value in exact) or sum(exact) != 1:
        raise ValueError("seven exact nonnegative normalized weights required")
    return exact


def gambler_transitions(weights, defect=None):
    weights = validate_simplex(weights); pairs = active_pairs(weights)
    if not pairs:
        return ((Fraction(1), weights),)
    if defect == "delete_absorbing_identity" and len(pairs) == 0: return ()
    pair_weight = Fraction(1, len(pairs)); output = {}
    for ordinal, (left, right) in enumerate(pairs):
        total = weights[left] + weights[right]
        left_weight = Fraction(1, 2) if defect == "replace_conditional_by_half" else weights[left] / total
        right_weight = 1 - left_weight
        branches = ((left, right, left_weight), (right, left, right_weight))
        for kept, dropped, conditional in branches:
            if defect == "delete_first_branch" and ordinal == 0 and kept == left: continue
            moved = list(weights); moved[kept] = total; moved[dropped] = 0; moved = tuple(moved)
            output[moved] = output.get(moved, Fraction(0)) + pair_weight * conditional
    return tuple(sorted(((weight, state) for state, weight in output.items()), key=lambda row: row[1]))


@lru_cache(maxsize=None)
def absorption_weights(weights):
    weights = validate_simplex(weights); active = [i for i, value in enumerate(weights) if value]
    if len(active) == 1:
        return onehot(active[0], 7)
    result = [Fraction(0)] * 7
    for transition_weight, moved in gambler_transitions(weights):
        absorbed = absorption_weights(moved)
        for index in range(7): result[index] += transition_weight * absorbed[index]
    return tuple(result)


def gambler_martingale_residual(weights, defect=None):
    transitions = gambler_transitions(weights, defect); row_sum = sum(weight for weight, _ in transitions)
    means = tuple(sum(weight * state[index] for weight, state in transitions) for index in range(7))
    return row_sum, means


def transition_dict(rows): return {state: weight for weight, state in rows}


def route_B_absorbing_martingale(fixture_rows):
    frames = c661.c625.proper_cubic_frames(); absorption_failures = martingale_failures = covariance_failures = group_failures = 0
    rows = {}; absorption_weights.cache_clear()
    for name, row in fixture_rows.items():
        weights = row["weights"]; absorbed = absorption_weights(weights)
        absorption_failures += int(tuple(map(Fraction, absorbed)) != weights)
        row_sum, means = gambler_martingale_residual(weights)
        martingale_failures += int(row_sum != 1 or means != weights)
        for frame in frames:
            permutation = event_permutation(frame); moved = permute_tuple(weights, permutation)
            expected = {permute_tuple(state, permutation): transition_weight
                        for transition_weight, state in gambler_transitions(weights)}
            covariance_failures += int(transition_dict(gambler_transitions(moved)) != expected)
        support = sum(value > 0 for value in weights)
        convergence = []
        for trials in PREREGISTRATION["route_B"]["convergence_sizes"]:
            bounds = tuple(value * (1 - value) / trials for value in weights)
            convergence.append({
                "trials": trials,
                "maximum_empirical_mean_variance": str(max(bounds)),
                "maximum_Chebyshev_tail_bound_at_epsilon_1_over_10": str(min(Fraction(1), 100 * max(bounds))),
            })
        maxima = tuple(F(row["maximum_empirical_mean_variance"]) for row in convergence)
        rows[name] = {
            "split": row["split"], "active_vertices": support, "absorption_updates_exact": support - 1,
            "vertex_hitting_weights": [str(value) for value in absorbed], "input_squared_amplitude_weights": [str(value) for value in weights],
            "exact_hitting_match": absorbed == weights, "iid_convergence_rows": convergence,
            "empirical_mean_variance_strictly_decreases_on_declared_sizes": all(
                left > right for left, right in zip(maxima, maxima[1:])),
            "empirical_mean_variance_limit": "0",
        }
    for first, second in product(frames, frames):
        first_perm = event_permutation(first); second_perm = event_permutation(second)
        composed = event_permutation(c661.c625.matmul(first, second))
        for row in fixture_rows.values():
            group_failures += int(permute_tuple(permute_tuple(row["weights"], second_perm), first_perm)
                                  != permute_tuple(row["weights"], composed))
    probe = fixture_rows["C9_asymmetric"]["weights"]
    normal_sum, normal_mean = gambler_martingale_residual(probe)
    deleted_sum, _ = gambler_martingale_residual(probe, "delete_first_branch")
    half_sum, half_mean = gambler_martingale_residual(probe, "replace_conditional_by_half")
    vertex = (Fraction(1),) + (Fraction(0),) * 6
    saturation = gambler_transitions(vertex) == ((Fraction(1), vertex),)
    malformed = (
        (Fraction(1),) + (Fraction(0),) * 5,
        (Fraction(2),) + (Fraction(0),) * 6,
        (Fraction(-1), Fraction(2)) + (Fraction(0),) * 5,
        ("not-a-rational",) + ("0",) * 6,
    )
    malformed_rejected = 0
    for candidate in malformed:
        try:
            gambler_transitions(candidate)
        except ValueError:
            malformed_rejected += 1
    deletion_controls = {
        "delete_first_branch_breaks_row_sum": deleted_sum != 1,
        "replace_conditional_by_half_breaks_martingale": half_sum == 1 and half_mean != probe,
        "absorbing_vertex_is_fixed": saturation,
        "normal_kernel_row_and_martingale": normal_sum == 1 and normal_mean == probe,
        "malformed_simplex_rows_rejected": malformed_rejected == len(malformed),
    }
    # Only after the objective hybrid law and iid reset/convergence theorem pass is the probability name licensed.
    convergence_pass = all(row["empirical_mean_variance_strictly_decreases_on_declared_sizes"]
                           and row["empirical_mean_variance_limit"] == "0" for row in rows.values())
    repeated_trial_law_pass = (absorption_failures == martingale_failures == covariance_failures == group_failures == 0
                               and all(row["exact_hitting_match"] for row in rows.values())
                               and convergence_pass and all(deletion_controls.values()))
    cycle669_failures = 0
    if repeated_trial_law_pass:
        for event in range(7):
            for capacity in (3, 4, 6, 9):
                chain = c669.initial_chain(capacity); output, _ = c669.append_event(chain, event_token(event, onehot(event, 7)))
                cycle669_failures += int(len(c669.read_chain(output)) != int(event != 0))
                if event: cycle669_failures += int(c669.inverse_event(output) != chain)
    result = {
        "route": "B_law_owned_absorbing_pair_gambler", "fixture_rows": rows,
        "absorption_failures": absorption_failures, "martingale_failures": martingale_failures,
        "kernel_all24_tests": len(fixture_rows) * len(frames), "kernel_all24_failures": covariance_failures,
        "kernel_all576_group_tests": len(fixture_rows) * len(frames) ** 2, "kernel_all576_group_failures": group_failures,
        "deletion_and_saturation_controls": deletion_controls,
        "lawful_domain": "seven exact nonnegative rational weights summing to one",
        "malformed_simplex_rows_tested": len(malformed),
        "malformed_simplex_rows_rejected": malformed_rejected,
        "declared_iid_convergence_pass": convergence_pass,
        "objective_hybrid_state": "(immutable CoherentExhaust[Cycle676 wave], classical simplex state, law-owned innovation history)",
        "one_objective_vertex_per_trial_under_declared_law": repeated_trial_law_pass,
        "objective_repeated_trial_law": (
            "identical coherent-state reset and independent law-owned innovations make vertex outputs iid categorical; "
            "the strong law gives empirical convergence to the exact vertex-hitting weights"
        ) if repeated_trial_law_pass else None,
        "conditional_Born_probabilities": ({name: row["vertex_hitting_weights"] for name, row in rows.items()}
                                           if repeated_trial_law_pass else None),
        "named_coherent_exhaust": PREREGISTRATION["named_exhaust"], "unselected_amplitudes_and_phases_retained": True,
        "innovation_supply": (
            "at each of at most six updates the law supplies an active-pair choice and a conditional Bernoulli draw; "
            "exact rational draws require an ideal independent innovation stream with rejection overhead"
        ),
        "update_count_is_physical_time_or_rate": False, "host_sampler_calls": 0,
        "host_sampling_source_hits": host_sampling_hits((gambler_transitions, absorption_weights)),
        "state_weight_oracle_supplied": True, "bounded_physical_M2_unitary_compiler": False,
        "nonlinear_stochastic_update_called_M2_unitary": False,
        "Cycle669_basis_composition_failures": cycle669_failures,
        "disposition": (
            "exact objective Born/repeated-trial candidate conditional on a newly supplied hybrid stochastic law, "
            "state-weight access and innovation stream; not derived as bounded physical M2 dynamics"
        ),
    }
    result["pass"] = (repeated_trial_law_pass and cycle669_failures == 0 and not result["host_sampling_source_hits"]
                      and result["one_objective_vertex_per_trial_under_declared_law"]
                      and not result["bounded_physical_M2_unitary_compiler"])
    check("route B gives exact Born hitting/repeated-trial law only under an explicit stochastic hybrid supply", result["pass"],
          {"fixtures": len(rows), "convergence": convergence_pass,
           "Cycle669_failures": cycle669_failures, "physical_M2": False})
    return result


def projector(index, width=7):
    matrix = np.zeros((width, width), dtype=complex); matrix[index, index] = 1
    return matrix


def projector_dephase(rho): return sum(projector(index) @ rho @ projector(index) for index in range(7))


def phase_unitaries():
    root = cmath.exp(2j * math.pi / 7)
    return tuple(np.diag([root ** (k * index) for index in range(7)]) for k in range(7))


def random_unitary_dephase(rho): return sum(unitary @ rho @ unitary.conj().T for unitary in phase_unitaries()) / 7


def rotate_matrix(rho, permutation):
    matrix = np.zeros((7, 7), dtype=complex)
    for source, target in enumerate(permutation): matrix[target, source] = 1
    return matrix @ rho @ matrix.conj().T


def apply_event_environment_collision(bits, *, reverse=False, delete_rail=None):
    """Seven two-M2 CNOT factors; reverse is explicit even though each factor is self-inverse."""
    if len(bits) != 14 or any(type(bit) is not int or bit not in (0, 1) for bit in bits):
        raise ValueError("binary 14-M2 collision word required")
    output = list(bits)
    rails = tuple(reversed(range(7))) if reverse else tuple(range(7))
    for rail in rails:
        if rail != delete_rail:
            output[7 + rail] ^= output[rail]
    return tuple(output)


def apply_physical_collision_cell(bits, *, reverse=False, delete_rail=None):
    if len(bits) != 194 or any(type(bit) is not int or bit not in (0, 1) for bit in bits):
        raise ValueError("binary 194-M2 collision cell required")
    output = list(bits)
    rails = tuple(reversed(range(7))) if reverse else tuple(range(7))
    for rail in rails:
        if rail != delete_rail:
            output[187 + rail] ^= output[c676.CENTER[rail]]
    return tuple(output)


def collision_geometry():
    base = c676.cell_geometry()
    full = tuple(product(range(-3, 4), repeat=3))
    ordered = tuple(sorted(full, key=lambda point: (sum(abs(axis) for axis in point), point)))
    active = ordered[:194]
    environment = ordered[187:194]
    event = tuple(active[index] for index in c676.CENTER)
    frames = c661.c625.proper_cubic_frames(); cube = set(full)
    frame_rows = tuple(tuple(c661.c625.matvec(frame, point) for point in active) for frame in frames)
    pair_spans = tuple(sum(abs(left_axis - right_axis) for left_axis, right_axis in zip(left, right))
                       for left, right in zip(event, environment))
    return {
        "local_cube": "[-3,3]^3", "reserved_M2_per_coarse_cell": len(full),
        "Cycle676_active_M2": base["active_M2_per_coarse_cell"], "environment_active_M2": len(environment),
        "total_active_M2": len(active), "logical_index_to_coordinate": active,
        "event_rail_coordinates": event, "environment_rail_coordinates": environment,
        "placement_sha256": digest(active), "all24_active_frame_placements_inside_cube": all(
            set(row) <= cube for row in frame_rows),
        "all24_reserved_cube_invariant": all(
            {c661.c625.matvec(frame, point) for point in full} == cube for frame in frames),
        "maximum_CNOT_pair_L1_span": max(pair_spans),
        "constant_overhead_environment_M2_per_coarse_cell": 7,
        "global_coordinate_rule": base["global_coordinate_rule"],
    }


def route_C_linear_open_channel(fixture_rows):
    frames = c661.c625.proper_cubic_frames(); channel_residual = choi_residual = covariance_failures = group_failures = 0.0
    projectors = tuple(projector(index) for index in range(7)); unitaries = phase_unitaries()
    super_projector = sum(np.kron(K, K.conj()) for K in projectors)
    super_phase = sum(np.kron(U / math.sqrt(7), (U / math.sqrt(7)).conj()) for U in unitaries)
    choi_residual = float(np.linalg.norm(super_projector - super_phase))
    rows = {}
    for name, row in fixture_rows.items():
        weights = np.asarray([float(value) for value in row["weights"]]); amplitude = np.sqrt(weights).astype(complex)
        amplitude *= np.exp(1j * np.arange(7) * 0.173)
        rho = np.outer(amplitude, amplitude.conj()); left = projector_dephase(rho); right = random_unitary_dephase(rho)
        residual = float(np.linalg.norm(left - right)); channel_residual = max(channel_residual, residual)
        for frame in frames:
            permutation = event_permutation(frame)
            covariance_failures += float(np.linalg.norm(projector_dephase(rotate_matrix(rho, permutation))
                                                        - rotate_matrix(left, permutation))) > TOL
        rows[name] = {"split": row["split"], "input_purity": float(np.real(np.trace(rho @ rho))),
                      "dephased_purity": float(np.real(np.trace(left @ left))),
                      "projector_vs_phase_channel_residual": residual,
                      "projector_unravelling_event_weights": [str(value) for value in row["weights"]],
                      "phase_unravelling_outcome_weights": ["1/7"] * 7,
                      "phase_unravelling_system_state_remains_coherent_per_trajectory": True}
    for first, second in product(frames, frames):
        p1, p2 = event_permutation(first), event_permutation(second)
        pc = event_permutation(c661.c625.matmul(first, second))
        group_failures += int(tuple(p1[p2[index]] for index in range(7)) != pc)
    # Seven CNOTs correlate one-hot event rails with blank environment rails.
    collision_failures = inverse_failures = deletion_detected = malformed_rejected = all64_interface_failures = 0
    for event in range(7):
        source = onehot(event, 7) + (0,) * 7
        output = apply_event_environment_collision(source)
        collision_failures += int(output != onehot(event, 7) + onehot(event, 7))
        inverse = apply_event_environment_collision(output, reverse=True)
        inverse_failures += int(inverse != source)
    for word in WORDS:
        injected = c676.apply_injection(c676.initial_cell(word))
        center = tuple(injected[site] for site in c676.CENTER)
        physical_input = injected + (0,) * 7
        physical_output = apply_physical_collision_cell(physical_input)
        all64_interface_failures += int(physical_output[:187] != injected or physical_output[187:] != center)
        all64_interface_failures += int(apply_physical_collision_cell(physical_output, reverse=True) != physical_input)
    for deleted in range(7):
        visible = False
        for event in range(7):
            output = apply_event_environment_collision(onehot(event, 7) + (0,) * 7, delete_rail=deleted)
            visible |= output[7:] != onehot(event, 7)
        deletion_detected += int(visible)
    malformed = ((0,) * 14, (1,) * 14, onehot(0, 7) + onehot(0, 7), (2,) + (0,) * 13)
    for word in malformed:
        valid = (len(word) == 14 and all(type(bit) is int and bit in (0, 1) for bit in word)
                 and sum(word[:7]) == 1 and sum(word[7:]) == 0)
        malformed_rejected += int(not valid)
    geometry = collision_geometry()
    result = {
        "route": "C_linear_dephasing_collision_and_unravellings", "fixture_rows": rows,
        "projector_vs_random_phase_channel_maximum_residual": channel_residual,
        "Kraus_superoperator_residual": choi_residual, "channel_all24_tests": len(fixture_rows) * len(frames),
        "channel_all24_failures": int(covariance_failures), "channel_all576_group_failures": group_failures,
        "collision_dilation": {"incoming_Cycle676_active_M2": 187, "blank_environment_M2": 7,
                               "total_active_M2": 194, "CNOT_factors": 7, "maximum_support_M2": 2,
                               "basis_failures": collision_failures, "inverse_failures": inverse_failures,
                               "deletions_detected": deletion_detected, "malformed_rejected": malformed_rejected,
                               "Cycle676_all64_interface_tests": len(WORDS) * 2,
                               "Cycle676_all64_interface_failures": all64_interface_failures,
                               "Cycle676_wave_and_carrier_exhaust_unchanged": all64_interface_failures == 0,
                               "geometry": geometry},
        "finite_global_type": "PureCoherentState[center x environment x Cycle676 exhaust]",
        "reduced_type": "DiagonalDensity[none|six]", "channel_owns_one_objective_outcome": False,
        "unravelling_unique": False,
        "unravelling_discriminator": (
            "the projector and Fourier-phase ensembles implement the same channel; the first labels event sectors, "
            "the second labels phase kicks and leaves a coherent system state on each trajectory"
        ),
        "chosen_projector_unravelling_adds_objective_innovation_law": True,
        "chosen_projector_unravelling_reduces_to_route_B_supply": True,
        "one_objective_token_without_chosen_unravelling": False,
        "objective_repeated_trial_law": False, "weights_called_Born_probabilities_or_frequencies": False,
        "update_application_is_physical_time_or_rate": False,
        "host_sampler_calls": 0, "host_sampling_source_hits": host_sampling_hits((projector_dephase, random_unitary_dephase)),
        "disposition": (
            "bounded local collision dilation and exact decoherence pass, but the channel does not choose an unraveling "
            "or own one objective event; choosing the projector unraveling imports route B's stochastic law"
        ),
    }
    result["pass"] = (max(channel_residual, choi_residual) < TOL and not covariance_failures and group_failures == 0
                      and collision_failures == inverse_failures == all64_interface_failures == 0 and deletion_detected == 7
                      and malformed_rejected == len(malformed) and not result["host_sampling_source_hits"]
                      and geometry["all24_active_frame_placements_inside_cube"]
                      and geometry["all24_reserved_cube_invariant"]
                      and not result["channel_owns_one_objective_outcome"] and not result["unravelling_unique"])
    check("route C separates bounded linear decoherence from objective unraveling ownership", result["pass"],
          {"channel_residual": channel_residual, "unravelling_unique": False, "terminal": False})
    return result


def cross_route_discriminator(A, B, C, fixture_rows):
    table = {
        "A": {"single_objective": A["one_objective_token_on_all_inputs"],
              "exact_repeated_weights": A["objective_repeated_trial_law"], "bounded_M2": A["physical_M2_unitary_compiler"],
              "added_supply": "deterministic nonlinear state map and exhaust-copy extension"},
        "B": {"single_objective": B["one_objective_vertex_per_trial_under_declared_law"],
              "exact_repeated_weights": B["conditional_Born_probabilities"] is not None,
              "bounded_M2": B["bounded_physical_M2_unitary_compiler"],
              "added_supply": "objective hybrid ontology, state-weight oracle and independent innovation stream"},
        "C": {"single_objective": C["channel_owns_one_objective_outcome"],
              "exact_repeated_weights": C["objective_repeated_trial_law"], "bounded_M2": True,
              "added_supply": "chosen unraveling required for an outcome"},
    }
    exact_target_route = [name for name, row in table.items() if row["single_objective"] and row["exact_repeated_weights"] and row["bounded_M2"]]
    result = {
        "candidate_law_table": table, "routes_meeting_every_exact_target_type_gate": exact_target_route,
        "decisive_result": (
            "B alone owns a single exact repeated-trial result, but only as a supplied stochastic hybrid law; "
            "C alone has a bounded M2 dilation, but no outcome ownership; A has neither universal selection nor Born trials"
        ),
        "common_named_exhaust": PREREGISTRATION["named_exhaust"],
        "shared_route_independent_obstruction": False, "axiom_pressure": False,
        "exact_terminal_met": bool(exact_target_route),
    }
    result["pass"] = not exact_target_route and B["one_objective_vertex_per_trial_under_declared_law"] and C["collision_dilation"]["total_active_M2"] == 194
    check("cross-route discriminator finds no route satisfying selection, Born trials and physical M2 compilation together", result["pass"], table)
    return result


def no_go_discipline():
    Aref = current_citation("def route_A_nonlinear_extremalization(")
    Bref = current_citation("def route_B_absorbing_martingale(")
    Cref = current_citation("def route_C_linear_open_channel(")
    c676obj = citation("docs/work_history/repo/review_feedback/PHYSICAL_MOVING_CARRIER_PHASE_FIELD_FINITE_RESTRICTION_CYCLE676_NOTE_2026-07-23.md", "This type is **not obtained**")
    c676novel = citation("docs/work_history/repo/review_feedback/PHYSICAL_MOVING_CARRIER_PHASE_FIELD_FINITE_RESTRICTION_CYCLE676_NOTE_2026-07-23.md", "It does not")
    c662law = citation("docs/work_history/repo/review_feedback/PHYSICAL_OBJECTIVE_STOCHASTIC_OPEN_DILATION_CYCLE662_NOTE_2026-07-23.md", "stochastic law itself—not a host sampler")
    c536diag = citation("docs/work_history/repo/review_feedback/PHYSICAL_COHERENT_SEED_MEMBER_DILATION_CYCLE536_NOTE_2026-07-21.md", "a diagonal density operator is not one realized member")
    routes = [
        {"family": "deterministic nonlinear extremalization", "object": "projective simplex/pure-state flow",
         "mechanism": "replicator concentration or argmax", "terminal": "covariant nonsignalling Born trials",
         "honesty": "ATTEMPTED", "authority": Aref,
         "disposition": "ties, ensemble dependence and deterministic trial weights reject the terminal"},
        {"family": "objective absorbing martingale", "object": "hybrid simplex Markov kernel",
         "mechanism": "martingale fixation", "terminal": "derive local physical law and innovation",
         "honesty": "ATTEMPTED", "authority": Bref,
         "disposition": "exact Born trials conditional on supplied objective stochastic law"},
        {"family": "linear open collision channel", "object": "CPTP channel and dilation",
         "mechanism": "environmental decoherence", "terminal": "unique objective unraveling",
         "honesty": "ATTEMPTED", "authority": Cref,
         "disposition": "same channel has event and non-event unravelings"},
        {"family": "infinite-volume phase sectors", "object": "quasi-local central decomposition",
         "mechanism": "disjoint GNS sectors", "terminal": "one extremal realized sector",
         "honesty": "RULED OUT BY PRIOR", "authority": c676obj,
         "disposition": "Cycle676 reaches disjoint sectors but not selection"},
        {"family": "supplied objective stochastic dilation", "object": "quantum-classical instrument",
         "mechanism": "law-owned sigma update", "terminal": "derive rather than supply the law",
         "honesty": "RULED OUT BY PRIOR", "authority": c662law,
         "disposition": "objective output is conditional on the supplied stochastic law"},
        {"family": "state-carried deterministic pseudorandom innovation", "object": "finite local chaotic reservoir",
         "mechanism": "hidden state supplies repeatable innovation", "terminal": "seed-free iid Born law with no signalling",
         "honesty": "OPEN_NOT_COUNTED", "authority": c676novel,
         "disposition": "not tested; finite hidden state risks deterministic frequencies and seed dependence"},
    ]
    walls = ["W_objective_law_ownership", "W_bounded_local_physical_compilation"]
    pairs = [{"first": walls[0], "second": walls[1], "first_implies_second": False, "second_implies_first": False,
              "independent": True, "witness": "route B closes ownership without M2; route C closes M2 dilation without ownership"}]
    source = "\n".join(inspect.getsource(fn).lower() for fn in
                        (route_A_nonlinear_extremalization, route_B_absorbing_martingale, route_C_linear_open_channel))
    phrases = ("we assume", "by construction", "as is standard", "the framework provides", "bridge context", "background",
               "naturally", "obviously", "standard qft", "registered", "canonical")
    hidden = tuple(phrase for phrase in phrases if phrase in source)
    residuals = [
        {"witness": c676obj, "prior": "central decomposition does not select one member",
         "current": "routes A/C still do not select; B adds objective law", "match": True},
        {"witness": c662law, "prior": "objective result belongs to supplied stochastic law",
         "current": "route B has the same explicit law-ownership residual", "match": True},
        {"witness": c536diag, "prior": "diagonal density is not a realized member",
         "current": "route C dephasing is not promoted", "match": True},
    ]
    rhetoric = [
        {"claim": "replicator concentration is not a Born trial law", "per_element": "five exact fixture weights",
         "per_site": "seven event rails", "per_mode": "tie and unique-max modes", "per_block": "C3/C4/C6/C9",
         "lattice_wide": "bipartite ensemble test; no universal claim beyond this nonlinear family"},
        {"claim": "decoherence is not objective outcome ownership", "per_element": "seven projectors",
         "per_site": "14-M2 collision", "per_mode": "projector versus Fourier-phase unraveling",
         "per_block": "five fixtures", "lattice_wide": "channel statement only; alternative open laws remain"},
        {"claim": "exact martingale hitting is not a physical M2 compiler", "per_element": "exact rational transitions",
         "per_site": "law-level simplex state", "per_mode": "seven vertices", "per_block": "four held/train cuts",
         "lattice_wide": "state-weight oracle/innovation explicitly supplied"},
    ]
    partial = [
        {"path": "Cycle678 A", "status": "EXECUTED_REJECTED_TERMINAL", "closes": "unique-max nonlinear concentration"},
        {"path": "Cycle678 B", "status": "EXECUTED_CONDITIONAL_CANDIDATE", "closes": "objective exact Born trials under supplied hybrid law"},
        {"path": "Cycle678 C", "status": "EXECUTED_PARTIAL", "closes": "bounded M2 dephasing dilation and unraveling discriminator"},
        {"path": "Cycle676", "status": "EXECUTED_PRIOR", "closes": "coherent exhaust and conditional disjoint sectors"},
        {"path": "finite local chaotic innovation", "status": "OPEN", "closes": "possible law-owned state-carried innovation"},
    ]
    steelman = (
        "A hostile reviewer should construct a finite proper-cubic cellular reservoir whose microscopic state is generated "
        "from the same neutral lawful genesis, prove that its first-passage bits are independent across identically reset "
        "trials with exact Cycle676 sector hitting weights, and couple those bits to the absorbing martingale while preserving "
        "the complete outgoing wave and no-signalling. Such a state-carried innovation mechanism would remove route B's "
        "external innovation stream and could reopen bounded physical compilation; it has not been attempted here."
    )
    echoes = [
        {"cycle": 536, "retired": "coherent diagonal construction", "remaining": "one realized member"},
        {"cycle": 662, "retired": "objective stochastic instrument", "remaining": "derive its law"},
        {"cycle": 671, "retired": "selector-conditioned token", "remaining": "native-domain ownership"},
        {"cycle": 674, "retired": "finite robust latches", "remaining": "objective promotion"},
        {"cycle": 676, "retired": "conditional disjoint sectors", "remaining": "selected extremal sector"},
        {"cycle": 678, "retired": "law-class discriminator and exact martingale candidate", "remaining": "bounded law genesis"},
    ]
    qualifying = sum(row["honesty"] in ("ATTEMPTED", "RULED OUT BY PRIOR") for row in routes)
    complete = qualifying >= 5 and not hidden and all(row["match"] for row in residuals) and len(rhetoric) == 3
    result = {
        "skill_freshness": {"origin_main_checked": True, "origin_main_advanced": False,
                            "remote_skill_followed": True, "dirty_worktree_moved": False},
        "N1_routes": routes, "N1_qualifying_normalized_families": qualifying,
        "N2_collapsed_walls": walls, "N2_pairwise_table": pairs, "N3_hidden_phrase_hits": hidden,
        "N4_residual_matches": residuals, "N5_rhetoric": rhetoric, "N6_partial_closure_paths": partial,
        "N6_primitive_registry_claim_made": False, "N7_steelman": steelman,
        "N7_supporting_authority": c676novel, "N8_cross_cycle_echo": echoes,
        "checklist_complete": complete, "negative_claim_gate_status": "FAIL_DO_NOT_SHIP_NEGATIVE",
        "negative_gate_failure_reason": "N7 state-carried lawful innovation mechanism remains untested",
        "demotion": "partial-attempt-with-conditional-candidate-and-named-untested-route",
        "broad_no_go_claim": False, "minimum_content_claim": False,
        "shared_route_independent_obstruction": False, "axiom_pressure": False,
        "discipline_compliance_pass": complete,
    }
    check("fresh N1-N8 blocks a broad actualization impossibility or axiom-pressure claim", complete,
          {"families": qualifying, "walls": walls, "negative_gate": result["negative_claim_gate_status"]})
    return result


def inventory():
    return {
        "supplied": [
            "Cycle661/Cycle676 coherent 64-sector wave and phase/exhaust compiler", "Cycle669 chain seeds",
            "candidate A nonlinear pure-state rule", "candidate B objective hybrid state-weight oracle",
            "candidate B independent innovation stream and identical trial reset", "candidate C blank environment rails",
            "candidate C unraveling choice when an outcome is requested", "compile-time frame chart",
            "finite Markov-chain recursion plus optional-stopping, Chebyshev and strong-law theorem machinery",
        ],
        "derived": [
            "replicator tie/ensemble/no-signalling discriminator", "exact absorbing martingale and vertex-hitting theorem",
            "conditional iid repeated-trial/Born law", "194-active-M2 dephasing collision dilation",
            "exact nonunique-unraveling equality", "branchwise Cycle669 composition",
        ],
        "open": [
            "bounded physical genesis of objective innovation", "one route closing both objective ownership and M2 compilation",
            "framework Record", "physical time/rate", "physical energy/generator", "gravity/source",
        ],
    }


def note_text(receipt):
    ng = receipt["no_go_discipline"]; A = receipt["routes"]["A"]; B = receipt["routes"]["B"]; C = receipt["routes"]["C"]
    cross = receipt["cross_route_discriminator"]
    n1 = "\n".join(f"| {r['family']} | {r['object']} | {r['mechanism']} | {r['terminal']} | {r['honesty']} | `{r['authority']['path']}:{r['authority']['line']}` | {r['disposition']} |" for r in ng["N1_routes"])
    n4 = "\n".join(f"| `{r['witness']['path']}:{r['witness']['line']}` | {r['prior']} | {r['current']} | {str(r['match']).lower()} |" for r in ng["N4_residual_matches"])
    n5 = "\n".join(f"| {r['claim']} | {r['per_element']} | {r['per_site']} | {r['per_mode']} | {r['per_block']} | {r['lattice_wide']} |" for r in ng["N5_rhetoric"])
    n6 = "\n".join(f"| {r['path']} | {r['status']} | {r['closes']} |" for r in ng["N6_partial_closure_paths"])
    n8 = "\n".join(f"| Cycle {r['cycle']} | {r['retired']} | {r['remaining']} |" for r in ng["N8_cross_cycle_echo"])
    table = "\n".join(f"| {name} | {row['single_objective']} | {row['exact_repeated_weights']} | {row['bounded_M2']} | {row['added_supply']} |" for name, row in cross["candidate_law_table"].items())
    Brows = "\n".join(f"| {name} | {row['split']} | {row['active_vertices']} | {row['absorption_updates_exact']} | {row['exact_hitting_match']} |" for name, row in B["fixture_rows"].items())
    Crows = "\n".join(f"| {name} | {row['split']} | {row['input_purity']:.6f} | {row['dephased_purity']:.6f} | {row['projector_vs_phase_channel_residual']:.3e} |" for name, row in C["fixture_rows"].items())
    return f"""# Autonomous extremal-sector/Born actualizer tournament — Cycle 678

Authority: **none**

Audit: **unset**

## Fresh no-go-discipline gate before disposition

The complete remote-main no-go skill and proof-search governance were followed without moving the dirty campaign worktree.

### N1

| family | object | mechanism | terminal | honesty | authority | disposition |
|---|---|---|---|---|---|---|
{n1}

### N2–N4

The collapsed walls are `{ng['N2_collapsed_walls']}`. Their independence witness is `{ng['N2_pairwise_table'][0]['witness']}`. Hidden phrase hits: `{ng['N3_hidden_phrase_hits']}`.

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

No retained-primitive absence claim is made; the primitive-registry gate is not triggered.

### N7

{ng['N7_steelman']} Supporting boundary: `{ng['N7_supporting_authority']['path']}:{ng['N7_supporting_authority']['line']}`.

### N8

| cycle | retired | remaining |
|---|---|---|
{n8}

Negative-claim gate: **{ng['negative_claim_gate_status']}**. This is a `{ng['demotion']}`, not a no-go. Shared route-independent obstruction: **not established**. Axiom pressure: **none**.

## Frozen target and candidate-law discriminator

Target `{receipt['frozen_contract']['target_sha256']}` and preregistration `{receipt['frozen_contract']['preregistration_sha256']}` precede evidence. All `{len(receipt['frozen_contract']['pins'])}` shores are exact at `{receipt['frozen_contract']['shore']}`, including Cycle676's prior-art/novelty firewall.

| route | one objective result? | exact repeated weights? | bounded M2? | added supply |
|---|---:|---:|---:|---|
{table}

No route closes all three columns. Route B alone supplies a one-result repeated-trial law; route C alone compiles a bounded local dilation. This is a discriminator among candidate-law types, not constitutional language.

## Route A — deterministic nonlinear extremalization

The norm-preserving power map sends event weights `w_i` to `w_i^2 / sum_j w_j^2` and retains within-sector phases. It is permutation-covariant and increasingly concentrates every unique maximum, but no finite tested iterate is an exact vertex. The six-direction tie remains tied. A lowest-index fallback fails `{A['direction_tie_argmax_all24_failures']}` all24 comparisons because an invariant tied input has no invariant direction output.

The same mixed state `diag(1/4,3/4)` has an eigenensemble and a coherent `+/-` ensemble. Applying the pure-state power law to ensemble members leaves the first diagonal weight `1/4` for the eigenensemble but changes it to `1/10` for the coherent ensemble, giving trace distance `3/20`. Argmax gives distance `1/4`. Thus a remote ensemble choice changes the local output if this nonlinear pure-state rule is physical.

Deterministic identical trials produce a delta at the unique argmax, not the input weights, and ties provide no covariant result. Therefore no objective repeated-trial law passes. The nonlinear state map and a copied immutable exhaust are explicit hybrid supplies, not physical M2 unitaries.

## Route B — law-owned absorbing martingale

At each update the candidate law chooses an active unordered pair uniformly, then transfers its combined mass to endpoint `i` with conditional weight `w_i/(w_i+w_j)`. Every coordinate is an exact martingale; every update removes one active coordinate, so absorption takes at most six updates. Optional stopping and exhaustive rational recursion give the initial squared-amplitude weights exactly.

| fixture | split | active vertices | absorption updates | exact hitting match? |
|---|---|---:|---:|---:|
{Brows}

The law declares identical coherent-state reset plus independent law-owned innovations on repeated trials. Only after that objective law, exact hitting theorem and the decreasing frequency-variance tests pass do the receipt and this note call the vertex weights conditional Born probabilities: `{B['conditional_Born_probabilities']}`. The strong law then gives empirical convergence.

Every trial retains the immutable Cycle676 64-sector wave and six-ray provenance as a named coherent exhaust, while one classical vertex feeds Cycle669. All seven vertices compose at C3/C4/C6/C9 with zero failures.

This is the strongest candidate result, but its state-weight oracle, objective classical variable, independent active-pair/Bernoulli innovations and reset are supplied by the candidate law. Exact rational draws require an ideal innovation stream with rejection overhead. The update count is not physical time or a rate. The law is not a bounded physical M2 unitary or a derivation from Cycle676.

## Route C — linear open channel and collision dilation

| fixture | split | input purity | reduced purity | two-unraveling channel residual |
|---|---|---:|---:|---:|
{Crows}

Seven local CNOTs copy the one-hot center to seven blank environment M2, giving a 194-active-M2 Cycle676-plus-environment collision dilation. Exact inverse, all seven deletions, malformed, all24/all576 and locality controls pass. The finite global state is coherent; tracing the environment gives a diagonal center. Tracing-out is not objective actuality.

The seven projector Kraus operators and seven Fourier diagonal random unitaries implement the same complete-dephasing channel with superoperator residual `{C['Kraus_superoperator_residual']:.3e}`. In the projector unraveling, trajectory labels are event sectors. In the phase unraveling, labels are phase kicks and the system remains coherent on every trajectory. Therefore the linear channel does not uniquely choose or own an event outcome. Selecting the projector unraveling adds the same objective innovation law isolated in route B.

## Exact disposition and imports

The strongest positive result is an exact absorbing martingale whose vertex-hitting weights equal the native squared amplitudes and whose declared iid objective law yields repeated-trial convergence. It is **conditional on a supplied stochastic hybrid law** and is not a physical M2 compiler.

The supplied structure is fully inventoried in the receipt. No reduced diagonal, coherent dilation, disjoint sector, nonreturn fact or unraveling is called one objective token. No packet or output is called a framework Record. Before route B's declared objective iid law passes, quantities are called weights, not probabilities or frequencies. Update applications, absorption depth and collision count are not physical time or rates. No wrapped phase is called physical energy and no generator element is called a rate.

## Prior-art and novelty boundary

Replicator maps, absorbing martingales/gambler fixation, Kraus nonuniqueness and collision-model decoherence are bounded prior mathematical structures and are not claimed as new. The new repo-side result is their exact dependency-tracked comparison on the committed Cycle676 coherent/exhaust surface, including ties, ensemble/no-signalling, exact rational hitting laws, two equal channel unravelings, proper-cubic transport and unchanged Cycle669 composition.

**PASS / CONDITIONAL CANDIDATE** for route B's explicitly supplied objective stochastic law and exact repeated-trial Born result. **NOT MET, NOT FALSIFIED** for the full native bounded-physical actualizer target. No shared obstruction or axiom pressure follows. The optimal next campaign is the N7 finite state-carried lawful-innovation compiler with exact reset, no seed and the present exhaust/type gates fixed.
"""


def note_contract():
    body = " ".join(NOTE.read_text().lower().split())
    required = (
        "authority: **none**", "audit: **unset**", "fresh no-go-discipline gate before disposition",
        "not a no-go", "shared route-independent obstruction: **not established**", "axiom pressure: **none**",
        "not met, not falsified", "tracing-out is not objective actuality", "not physical time or rates",
        "no generator element is called a rate", "conditional on a supplied stochastic hybrid law",
        "before route b's declared objective iid law passes, quantities are called weights, not probabilities or frequencies",
    )
    missing = tuple(item for item in required if item not in body)
    return {"required": required, "missing": missing, "pass": not missing}


def main():
    signal.alarm(math.ceil(WALL_CAP_SECONDS)); started = time.perf_counter()
    frozen, imported = freeze_and_shore_controls(); ng = no_go_discipline(); fixture_rows, fixture_residuals = fixtures()
    fixture_pass = max(fixture_residuals.values()) < TOL
    check("Cycle676 coherent fixtures match frozen exact event weights", fixture_pass, fixture_residuals)
    A = route_A_nonlinear_extremalization(fixture_rows)
    B = route_B_absorbing_martingale(fixture_rows)
    C = route_C_linear_open_channel(fixture_rows)
    cross = cross_route_discriminator(A, B, C, fixture_rows)
    receipt = {
        "cycle": 678, "date": "2026-07-23", "authority": AUTHORITY, "audit": AUDIT,
        "status": "exact absorbing Born martingale conditional on supplied law; bounded native physical actualizer not met",
        "classification": "conditional-candidate-law-discriminator", "frozen_contract": frozen,
        "fixture_crosscheck": {"residuals": fixture_residuals, "pass": fixture_pass},
        "no_go_discipline": ng, "routes": {"A": A, "B": B, "C": C},
        "cross_route_discriminator": cross, "supplied_structure_inventory": inventory(),
        "strongest_constructive_result": (
            "an exact proper-cubic absorbing martingale with vertex-hitting weights |a_i|^2, at most six updates, "
            "declared iid objective trials, named immutable Cycle676 exhaust and exact Cycle669 composition"
        ),
        "strict_full_framework_terminal_met": False, "target_contract_candidate_terminal_met": False,
        "exact_terminal_met": False, "exact_terminal_disposition": "NOT_MET_NOT_FALSIFIED",
        "shared_route_independent_obstruction": False, "axiom_pressure": False, "breakthrough": False,
        "author_accepted": False,
        "optimal_next_campaign": "finite state-carried lawful-innovation compiler with exact reset, no seed and no host service",
    }
    NOTE.write_text(note_text(receipt)); note = note_contract()
    check("Cycle678 note preserves outcome/Born/unravelling/M2/time/no-go type gates", note["pass"], note["missing"])
    elapsed = time.perf_counter() - started; rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if rss < 10_000_000: rss *= 1024
    receipt.update({"note_contract": note, "runner_sha256": file_sha(Path(__file__)), "note_sha256": file_sha(NOTE),
                    "elapsed_seconds": elapsed, "maximum_RSS_bytes": rss, "tests_passed": PASS, "tests_failed": FAIL})
    receipt["pass"] = (FAIL == 0 and fixture_pass and all(item["pass"] for item in (frozen, A, B, C, cross, note))
                       and ng["discipline_compliance_pass"] and not ng["broad_no_go_claim"]
                       and elapsed < WALL_CAP_SECONDS and rss < RSS_CAP_BYTES and AUTHORITY == "none" and AUDIT == "unset")
    RECEIPT.write_text(json.dumps(receipt, indent=2, sort_keys=True,
                                  default=lambda x: x.item() if isinstance(x, np.generic) else list(x)) + "\n")
    print(json.dumps({"pass": receipt["pass"], "tests_passed": PASS, "tests_failed": FAIL,
                      "elapsed_seconds": elapsed, "maximum_RSS_bytes": rss,
                      "note": str(NOTE), "receipt": str(RECEIPT)}, indent=2))
    if not receipt["pass"]: raise SystemExit(1)


if __name__ == "__main__": main()
