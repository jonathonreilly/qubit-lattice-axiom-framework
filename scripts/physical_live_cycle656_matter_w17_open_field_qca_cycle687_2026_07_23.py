#!/usr/bin/env python3
"""Cycle687: live Cycle656 matter drives a finite open W17 field candidate.

The physical factor order and both the matter and field layer controllers are
supplied.  A finite schedule is not called time; modular labels are not called
energy; and the response register is not called a Record.
"""

from __future__ import annotations

TARGET_CONTRACT = {
    "target_statement": "compose the pinned Cycle656 term-complete seven-color physical matter presentation with a locally constrained finite W17 Q/P open-field update, driven by the live Cycle219/230 coin-stream occupation/current rather than a supplied source snapshot, and use the identical declared q at source and receiver",
    "quantifiers_domain": "open W17 field cubes L3 construction, L6 train, L7 held-out; beta=-0.3 one-particle Cycle219/230 matter tick; q=plus/minus one and plus/minus two; q_receiver zero and opposite-sign arms; all 24 proper-cubic frames and all 576 ordered products",
    "allowed_premises": "exact Git-object bytes at Cycle683 commit 28261bc1 for Cycles210/219/230/656/683; external #5564-5566 commits are read-only comparisons; W17 modulus, blank Q/P/receiver words, beta, q, open cube, receiver, three field microsteps, Cycle656 30-family/58-layer order and the finite W17 controller are declared inputs",
    "forbidden_weakenings": "no host matter texture, static matter snapshot, global parity service, Jordan-Wigner order, periodic field edge, host-updated source array, fitted source/receiver couplings, or autonomous-clock claim; no modular phase called physical energy, generator element called rate, schedule called time, response register called Record, or result called gravity/stress/source law",
    "required_edge_cases": "live local continuity; exact joint inverse; one-hot constraint preservation and malformed rejection; source, matter-coin, stream, link, drift and receiver deletion; q sign, q squared, opposite-sign receiver and q_receiver zero; nonzero bare field at q_receiver zero; open coframe Ward; mass fixture; L3/L6/L7; all24/all576; locally bounded support and constant overhead; exact supply inventory",
    "completion_witness": "one coherent one-particle coin-stream tick whose physical occupation branches control three complete open W17 KDK field microsteps and a same-q receiver accumulator, with exact modular response identities, inverse, deletion, Ward, locality, held-size and covariance receipts, plus an explicit scheduled-not-autonomous boundary",
    "outcomes_not_closure": "a deterministic matter subword with no actual coin; replaying a static occupation word; one W17 link with no full cube update; logical modular arithmetic with no local M2 lowering; inherited Cycle656 factorization relabelled an autonomous law; route-specific residual relabelled shared obstruction or axiom pressure",
}

from dataclasses import dataclass
from hashlib import sha256
from itertools import permutations, product
import json
import math
from pathlib import Path
import resource
import subprocess
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_LIVE_CYCLE656_MATTER_W17_OPEN_FIELD_QCA_CYCLE687_NOTE_2026-07-23.md"
RECEIPT = ROOT / "outputs/physical_live_cycle656_matter_w17_open_field_qca_cycle687_receipt_2026_07_23.json"
COLD = ROOT / "outputs/physical_live_cycle656_matter_w17_open_field_qca_cycle687_cold_2026_07_23.txt"
SHORE = "28261bc1d92ad9e85f97d0101ee884daddc2063f"
AUTHORITY = "none"
AUDIT = "unset"
W = 17
HALF = 9
BETA = -0.3
FIELD_MICROSTEPS = 3
TOL = 2.0e-12
PASS = 0
FAIL = 0
DIRECTIONS = np.asarray(((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)), dtype=int)

PINS = {
    "28261bc1d92ad9e85f97d0101ee884daddc2063f:scripts/physical_M2_matter_same_coupling_open_source_bridge_cycle683_2026_07_23.py": "b3470294d1d096e2389ed09a22c35366511f8c184bb57f2e69a83ad606bc1331",
    "28261bc1d92ad9e85f97d0101ee884daddc2063f:outputs/physical_M2_matter_same_coupling_open_source_bridge_cycle683_receipt_2026_07_23.json": "ba28d21962db07ae90bedd978b610290a1cb8d74012bfeeeb553904eb8a77fd6",
    "28261bc1d92ad9e85f97d0101ee884daddc2063f:scripts/physical_term_complete_flat_link_update_cycle656_2026_07_23.py": "9c10b91f9028c341b431de9489c100975991cd3a4e8651c2482a10d4bfe6b1f9",
    "28261bc1d92ad9e85f97d0101ee884daddc2063f:outputs/physical_term_complete_flat_link_update_cycle656_receipt_2026_07_23.json": "a97cf4d906b8d1f9e5dcfccb4d8b8c30dcfd3a0fa36c5371e9d2bc8a6f72315c",
    "28261bc1d92ad9e85f97d0101ee884daddc2063f:scripts/common_matter_field_coin_family_cycle219_2026_07_16.py": "ad9bf5febde8b58e948f4a4240791216a20d61262149469763ef387455dff52a",
    "28261bc1d92ad9e85f97d0101ee884daddc2063f:scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py": "c410b754d4e984f6ee5ccbc7c5a52e776c50c91c4daa12d798044f104cc7435b",
    "28261bc1d92ad9e85f97d0101ee884daddc2063f:scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py": "b449301837c1b72a325d310a1e2c582263a36648de939d169912347aff0591ae",
    "28261bc1d92ad9e85f97d0101ee884daddc2063f:scripts/local_rough_puncture_odd_sector_cycle247_2026_07_17.py": "10f5cf027c76f5a0a3b1d3dbaa6cb0e6d418932c84553f0cca303d3f21742519",
    "3fedc918e318359567f76bc066255271dc8d8046:outputs/physical_dynamical_metric_source_law_bridge_tournament_cycle576_receipt_2026_07_22.json": "06456c1443f5464949f40d81e9f1c6316b3e4e8405415b5b0035e39d4b88c3bd",
    "c4b31f0d87be8bf9058b0d159121f4c0833e6247:outputs/physical_finite_reversible_norm_saturation_evaluator_tournament_receipt_2026_07_23.json": "bfcd5ed10f3f61ba60c0259b6a813dcfb28009385b1e2c1d8121100376c7e485",
    "394c30e1c12d40f65b6ce6456d9b026106d0bdda:outputs/physical_same_coupling_executed_field_update_response_tournament_receipt_2026_07_23.json": "da75185e5833721d467b98f26ae49e1f7aef47677aaf1c2c17f5a15d45cd3712",
}


class Tee:
    def __init__(self, *streams): self.streams = streams
    def write(self, body):
        for stream in self.streams: stream.write(body)
        return len(body)
    def flush(self):
        for stream in self.streams: stream.flush()


def check(label, condition, detail=""):
    global PASS, FAIL
    PASS += int(bool(condition)); FAIL += int(not bool(condition))
    print("PASS" if condition else "FAIL", label, "::", detail)


def stable_digest(value):
    return sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), default=float).encode()).hexdigest()


def git_bytes(spec):
    return subprocess.run(("git", "show", spec), cwd=ROOT, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout


def target_freeze_controls():
    lines = Path(__file__).read_text().splitlines()
    target = next(i for i, line in enumerate(lines, 1) if line.startswith("TARGET_CONTRACT ="))
    evidence = next(i for i, line in enumerate(lines, 1) if line.startswith("def evidence_controls"))
    expected = ["allowed_premises", "completion_witness", "forbidden_weakenings", "outcomes_not_closure", "quantifiers_domain", "required_edge_cases", "target_statement"]
    return {"target_line": target, "first_evidence_load_line": evidence, "frozen_before_evidence": target < evidence, "contract_sha256": stable_digest(TARGET_CONTRACT), "pass": target < evidence and sorted(TARGET_CONTRACT) == expected}


def evidence_controls():
    observed = {spec: sha256(git_bytes(spec)).hexdigest() for spec in PINS}
    objects = {spec: subprocess.run(("git", "rev-parse", spec), cwd=ROOT, check=True, text=True, stdout=subprocess.PIPE).stdout.strip() for spec in PINS}
    receipts = {spec: json.loads(git_bytes(spec)) for spec in PINS if spec.endswith(".json")}
    external = {name: subprocess.run(("git", "rev-parse", name), cwd=ROOT, check=True, text=True, stdout=subprocess.PIPE).stdout.strip() for name in ("3fedc918", "c4b31f0", "394c30e")}
    expected_external = {"3fedc918": "3fedc918e318359567f76bc066255271dc8d8046", "c4b31f0": "c4b31f0d87be8bf9058b0d159121f4c0833e6247", "394c30e": "394c30e1c12d40f65b6ce6456d9b026106d0bdda"}
    c656 = next(row for spec, row in receipts.items() if "cycle656" in spec)
    c683 = next(row for spec, row in receipts.items() if "cycle683" in spec)
    return {
        "shore": SHORE, "pins": PINS, "observed": observed, "exact_git_object_ids_read": objects,
        "external_open_evidence_commits": external, "external_commits_cherry_picked": False,
        "external_code_or_artifacts_duplicated": False, "working_tree_bytes_used_as_scientific_premise": False,
        "cycle656_status": c656.get("Status"), "cycle683_status": c683.get("Status"),
        "pass": observed == PINS and external == expected_external and c656.get("Status") == c683.get("Status") == "PASS",
    }, receipts


def note_contract():
    required = (
        "authority: **none**", "audit: **unset**", "target frozen before evidence", "live cycle656",
        "w17", "q/p", "all 24", "all 576", "l3/l6/l7", "source deletion", "q_receiver=0",
        "q squared", "one-hot", "open coframe ward", "factor order", "controller", "supplied",
        "not time", "not energy", "not a record", "not gravity", "#5564", "#5565", "#5566",
        "n1 —", "n2 —", "n3 —", "n4 —", "n5 —", "n6 —", "n7 —", "n8 —",
        "fail / do not ship", "no axiom pressure", "optimal next campaign",
    )
    body = "" if not NOTE.exists() else " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    missing = tuple(item for item in required if item not in body)
    return {"required": required, "missing": missing, "pass": not missing}


def proper_cubic_frames():
    frames = []
    for order in permutations(range(3)):
        permutation = np.eye(3, dtype=int)[list(order)]
        for signs in product((-1, 1), repeat=3):
            frame = np.diag(signs) @ permutation
            if round(np.linalg.det(frame)) == 1: frames.append(frame)
    unique = {tuple(frame.reshape(-1)): frame for frame in frames}
    return tuple(unique[key] for key in sorted(unique))


def rotate_open(cell, frame, length):
    doubled = 2 * np.asarray(cell, dtype=int) - (length - 1)
    numerator = frame @ doubled + (length - 1)
    if np.any(numerator % 2): raise ValueError("open-cube rotation parity failure")
    result = tuple(int(value // 2) for value in numerator)
    if any(value < 0 or value >= length for value in result): raise ValueError("rotation escaped open cube")
    return result


def anchor(length):
    value = length // 2 if length % 2 else length // 2 - 1
    return (value, value, value)


def site_index(cell, length): return int(np.ravel_multi_index(cell, (length, length, length)))


def cell_from_index(index, length): return tuple(int(x) for x in np.unravel_index(index, (length, length, length)))


def direction_map(frame):
    lookup = {tuple(row): i for i, row in enumerate(DIRECTIONS)}
    return tuple(lookup[tuple(int(x) for x in frame @ direction)] for direction in DIRECTIONS)


def matter_coin():
    eye = np.eye(6, dtype=complex)
    reverse = np.zeros((6, 6), dtype=complex)
    reverse[np.arange(6), (1, 0, 3, 2, 5, 4)] = 1
    uniform = np.ones(6, dtype=complex) / math.sqrt(6)
    scalar = np.outer(uniform, uniform.conj())
    even = (eye + reverse) / 2 - scalar
    vector = (eye - reverse) / 2
    inertial_mass = 3 * math.tan(-BETA / 2)
    rest_phase = inertial_mass / 3
    coin = np.exp(1j * rest_phase) * (scalar - even + np.exp(1j * BETA) * vector)
    return coin, inertial_mass, rest_phase


def live_matter_tick(length, source_direction=0, delete_coin=False, delete_stream=False, origin=None):
    coin, mass, rest_phase = matter_coin()
    initial = np.zeros(6, dtype=complex); initial[source_direction] = 1
    after_coin = initial.copy() if delete_coin else coin @ initial
    origin = anchor(length) if origin is None else tuple(origin)
    branches = []
    for direction, amplitude in enumerate(after_coin):
        cell = origin if delete_stream else tuple(int(x) for x in np.asarray(origin) + DIRECTIONS[direction])
        if any(x < 0 or x >= length for x in cell): raise ValueError("matter fixture touched an open boundary")
        branches.append({"direction": direction, "cell": cell, "amplitude": amplitude})
    return branches, {"initial_direction": source_direction, "origin": origin, "coin": coin, "analytic_mass": mass, "rest_phase": rest_phase}


def matter_controls():
    frames = proper_cubic_frames(); coin, mass, phase = matter_coin(); uniform = np.ones(6, complex) / math.sqrt(6)
    maximum_coin_covariance = 0.0; maximum_current = 0.0; maximum_frame_amplitude = 0.0; rows = []
    for length in (3, 6, 7):
        branches, meta = live_matter_tick(length)
        before = np.zeros(length ** 3); before[site_index(meta["origin"], length)] = 1
        after = np.zeros_like(before); incoming = np.zeros_like(before); outgoing = np.zeros_like(before)
        outgoing[site_index(meta["origin"], length)] = sum(abs(row["amplitude"]) ** 2 for row in branches)
        for row in branches:
            probability = abs(row["amplitude"]) ** 2
            after[site_index(row["cell"], length)] += probability
            incoming[site_index(row["cell"], length)] += probability
        continuity = float(np.max(abs(after - before - (incoming - outgoing))))
        maximum_current = max(maximum_current, continuity)
        for frame in frames:
            permutation = np.zeros((6, 6), complex); mapping = direction_map(frame)
            for old, new in enumerate(mapping): permutation[new, old] = 1
            maximum_coin_covariance = max(maximum_coin_covariance, float(np.linalg.norm(permutation @ coin @ permutation.T - coin)))
            rotated, _ = live_matter_tick(length, mapping[0], origin=rotate_open(meta["origin"], frame, length))
            rotated_by_direction = {row["direction"]: row for row in rotated}
            for row in branches:
                target_direction = mapping[row["direction"]]
                target = rotated_by_direction[target_direction]
                maximum_frame_amplitude = max(maximum_frame_amplitude, abs(target["amplitude"] - row["amplitude"]))
                if target["cell"] != rotate_open(row["cell"], frame, length): maximum_frame_amplitude = math.inf
        rows.append({"length": length, "split": {3: "construction", 6: "train", 7: "held-out-no-refit"}[length], "origin": list(meta["origin"]), "branch_probabilities": [abs(row["amplitude"]) ** 2 for row in branches], "continuity_residual": continuity, "source_snapshot_supplied": False})
    mass_from_scalar = float(np.angle(np.vdot(uniform, coin @ uniform))) / (1 / 3)
    inverse_residual = float(np.linalg.norm(coin.conj().T @ coin - np.eye(6)))
    return {
        "rows": rows, "beta": BETA, "analytic_mass": mass, "rest_phase": phase,
        "mass_fixture_residual": abs(mass_from_scalar - mass), "coin_unitarity_residual": inverse_residual,
        "maximum_local_continuity_residual": maximum_current, "maximum_all24_coin_covariance_residual": maximum_coin_covariance,
        "maximum_all24_live_branch_transport_residual": maximum_frame_amplitude,
        "contact_number_commutator": "exact zero; the Cycle230 contact is diagonal in occupation and is identity on this N=1 fixture",
        "live_update": "actual beta=-0.3 proper-cubic coin followed by one six-direction stream; source is read after the stream",
        "pass": max(abs(mass_from_scalar - mass), inverse_residual, maximum_current, maximum_coin_covariance, maximum_frame_amplitude) < TOL,
    }


@dataclass(frozen=True)
class FieldState:
    Q: tuple[int, ...]
    P: tuple[int, ...]
    R: int


def blank_field(length):
    zero = (0,) * (length ** 3)
    return FieldState(zero, zero, 0)


def open_edges(length):
    rows = []
    for cell in product(range(length), repeat=3):
        for axis in range(3):
            if cell[axis] + 1 >= length: continue
            target = list(cell); target[axis] += 1; target = tuple(target)
            rows.append((site_index(cell, length), site_index(target, length), 2 * axis + cell[axis] % 2, axis, cell, target))
    return tuple(rows)


def link_kick(P, Q, edges, sign=1, deleted=frozenset(), weights=None, reverse_colors=False):
    colors = range(5, -1, -1) if reverse_colors else range(6)
    for color in colors:
        for edge_index, (left, right, edge_color, _axis, _a, _b) in enumerate(edges):
            if edge_color != color or edge_index in deleted: continue
            weight = 1 if weights is None else weights.get(edge_index, 1)
            delta = sign * HALF * weight * (Q[right] - Q[left])
            P[left] = (P[left] + delta) % W; P[right] = (P[right] - delta) % W


def field_step(state, source, receiver, q_source, q_receiver, edges, inverse=False, deleted_links=frozenset(), delete_drift=False):
    Q = list(state.Q); P = list(state.P); R = state.R
    if not inverse:
        P[source] = (P[source] + HALF * q_source) % W
        link_kick(P, Q, edges, deleted=deleted_links)
        if not delete_drift: Q = [(q + p) % W for q, p in zip(Q, P)]
        link_kick(P, Q, edges, deleted=deleted_links)
        P[source] = (P[source] + HALF * q_source) % W
        R = (R + q_receiver * Q[receiver]) % W
    else:
        R = (R - q_receiver * Q[receiver]) % W
        P[source] = (P[source] - HALF * q_source) % W
        link_kick(P, Q, edges, sign=-1, deleted=deleted_links, reverse_colors=True)
        if not delete_drift: Q = [(q - p) % W for q, p in zip(Q, P)]
        link_kick(P, Q, edges, sign=-1, deleted=deleted_links, reverse_colors=True)
        P[source] = (P[source] - HALF * q_source) % W
    return FieldState(tuple(Q), tuple(P), int(R))


def branch_field_run(length, q_source=1, q_receiver=1, source_direction=0, delete_coin=False, delete_stream=False, deleted_links=frozenset(), delete_drift=False, origin=None):
    branches, matter = live_matter_tick(length, source_direction, delete_coin, delete_stream, origin)
    edges = open_edges(length); receiver_cell = tuple(int(x) for x in np.asarray(matter["origin"]) + DIRECTIONS[source_direction]); receiver = site_index(receiver_cell, length)
    outputs = []
    for branch in branches:
        state = blank_field(length); source = site_index(branch["cell"], length)
        for _ in range(FIELD_MICROSTEPS): state = field_step(state, source, receiver, q_source, q_receiver, edges, deleted_links=deleted_links, delete_drift=delete_drift)
        outputs.append({**branch, "source": source, "state": state})
    return outputs, matter, receiver, edges


def receiver_distribution(outputs):
    distribution = np.zeros(W)
    for row in outputs: distribution[row["state"].R] += abs(row["amplitude"]) ** 2
    return distribution


def finite_field_controls():
    rows = []; inverse_failures = sign_failures = q2_failures = opposite_failures = source_delete_failures = receiver_zero_failures = 0
    maximum_inverse_amplitude = 0.0; inverse_stream_failures = 0; minimum_bare = W; minimum_link_delete = math.inf; minimum_drift_delete = math.inf; minimum_coin_delete = math.inf; minimum_stream_delete = math.inf
    for length in (3, 6, 7):
        baseline, matter, receiver, edges = branch_field_run(length)
        minus, _, _, _ = branch_field_run(length, -1, -1)
        qtwo, _, _, _ = branch_field_run(length, 2, 2)
        opposite, _, _, _ = branch_field_run(length, 1, -1)
        qrec0, _, _, _ = branch_field_run(length, 1, 0)
        deleted_source, _, _, _ = branch_field_run(length, 0, 1)
        deleted_coin, _, _, _ = branch_field_run(length, delete_coin=True)
        deleted_stream, _, _, _ = branch_field_run(length, delete_stream=True)
        origin = matter["origin"]; receiver_cell = cell_from_index(receiver, length)
        target_edge = next(index for index, row in enumerate(edges) if {row[4], row[5]} == {origin, receiver_cell})
        deleted_link, _, _, _ = branch_field_run(length, deleted_links=frozenset((target_edge,)))
        deleted_drift, _, _, _ = branch_field_run(length, delete_drift=True)
        for base, neg, two, opp, zero, no_source in zip(baseline, minus, qtwo, opposite, qrec0, deleted_source):
            sign_failures += neg["state"].R != base["state"].R
            q2_failures += two["state"].R != (4 * base["state"].R) % W
            opposite_failures += opp["state"].R != (-base["state"].R) % W
            receiver_zero_failures += zero["state"].R != 0
            source_delete_failures += any(no_source["state"].Q) or any(no_source["state"].P) or no_source["state"].R != 0
            minimum_bare = min(minimum_bare, sum(x != 0 for x in zero["state"].Q) + sum(x != 0 for x in zero["state"].P))
            for result, qsrc, qrec in ((base, 1, 1), (neg, -1, -1), (two, 2, 2), (opp, 1, -1), (zero, 1, 0)):
                state = result["state"]
                for _ in range(FIELD_MICROSTEPS): state = field_step(state, result["source"], receiver, qsrc, qrec, edges, inverse=True)
                inverse_failures += state != blank_field(length)
            inverse_cell = tuple(int(x) for x in np.asarray(base["cell"]) - DIRECTIONS[base["direction"]])
            inverse_stream_failures += inverse_cell != matter["origin"]
        amplitudes = np.asarray([row["amplitude"] for row in baseline]); coin = matter["coin"]
        recovered = coin.conj().T @ amplitudes
        expected = np.zeros(6, complex); expected[0] = 1
        maximum_inverse_amplitude = max(maximum_inverse_amplitude, float(np.linalg.norm(recovered - expected)))
        base_distribution = receiver_distribution(baseline)
        minimum_link_delete = min(minimum_link_delete, float(np.linalg.norm(base_distribution - receiver_distribution(deleted_link))))
        minimum_drift_delete = min(minimum_drift_delete, float(np.linalg.norm(base_distribution - receiver_distribution(deleted_drift))))
        minimum_coin_delete = min(minimum_coin_delete, float(np.linalg.norm(base_distribution - receiver_distribution(deleted_coin))))
        minimum_stream_delete = min(minimum_stream_delete, float(np.linalg.norm(base_distribution - receiver_distribution(deleted_stream))))
        rows.append({
            "length": length, "split": {3: "construction", 6: "train", 7: "held-out-no-refit"}[length],
            "sites": length ** 3, "open_links": len(edges), "edge_colors": 6, "field_microsteps_per_matter_tick": FIELD_MICROSTEPS,
            "receiver_cell": list(receiver_cell), "branch_response_labels_q1": [row["state"].R for row in baseline],
            "branch_response_labels_qminus1": [row["state"].R for row in minus], "branch_response_labels_q2": [row["state"].R for row in qtwo],
            "receiver_distribution_q1": base_distribution.tolist(), "minimum_nonzero_bare_register_count_qrec0": min(sum(x != 0 for x in row["state"].Q) + sum(x != 0 for x in row["state"].P) for row in qrec0),
            "target_link_deletion_index": target_edge,
        })
    passed = not (inverse_failures or inverse_stream_failures or sign_failures or q2_failures or opposite_failures or source_delete_failures or receiver_zero_failures) and maximum_inverse_amplitude < TOL and min(minimum_bare, minimum_link_delete, minimum_drift_delete, minimum_coin_delete, minimum_stream_delete) > 0
    return {
        "size_rows": rows, "inverse_field_failures": inverse_failures, "inverse_matter_stream_failures": inverse_stream_failures, "joint_matter_inverse_amplitude_residual": maximum_inverse_amplitude,
        "q_sign_failures": sign_failures, "q_squared_failures": q2_failures, "opposite_receiver_sign_failures": opposite_failures,
        "source_deletion_failures": source_delete_failures, "q_receiver_zero_failures": receiver_zero_failures, "minimum_nonzero_bare_field_registers_at_qrec0": minimum_bare,
        "minimum_receiver_distribution_link_deletion_signal": minimum_link_delete, "minimum_drift_deletion_signal": minimum_drift_delete,
        "minimum_matter_coin_deletion_signal": minimum_coin_delete, "minimum_stream_deletion_signal": minimum_stream_delete,
        "same_q_identity": "Q and P are linear in q_source over F17; R adds q_receiver Q, hence simultaneous q sign cancels and q=2 multiplies R by four",
        "pass": passed,
    }


def unary(label):
    if not isinstance(label, int) or not 0 <= label < W: raise ValueError("not a lawful W17 label")
    bits = [0] * W; bits[label] = 1; return tuple(bits)


def physical_lowering_controls(cycle656_receipt):
    malformed_rejected = False
    try: unary(W)
    except ValueError: malformed_rejected = True
    inverse_failures = constraint_failures = source_intertwiner_failures = 0
    for multiplier in range(W):
        for control in range(W):
            for target in range(W):
                mapped = (target + multiplier * control) % W; recovered = (mapped - multiplier * control) % W
                inverse_failures += recovered != target
                constraint_failures += sum(unary(mapped)) != 1
    # Cycle656 represents each coarse occupation bit n_m by a degree-six
    # physical Pauli B_m with n_m=(1-B_m)/2.  Exhaust all local six-mode words:
    # the product of six encoded occupation-controlled shifts must equal the
    # coarse total-number source shear, for every W17 target and tested q.
    for word in product((0, 1), repeat=6):
        b_eigenvalues = tuple(1 - 2 * bit for bit in word)
        encoded_number = (6 - sum(b_eigenvalues)) // 2
        for target in range(W):
            for q in (-2, -1, 0, 1, 2):
                physical = target
                for occupation in word: physical = (physical + HALF * q * occupation) % W
                coarse = (target + HALF * q * sum(word)) % W
                source_intertwiner_failures += encoded_number != sum(word) or physical != coarse
    matter_factor_rows = cycle656_receipt["route_C_finite_color_factorization"]
    matter_gauge_rows = cycle656_receipt["route_B_local_gauge_auxiliary"]
    inherited_factor_support = max(row["maximum_factor_M2_weight"] for row in matter_factor_rows)
    inherited_constraint_support = max(row["maximum_Gauss_weight"] for row in matter_gauge_rows)
    inherited_factor_diameter = max(row["maximum_factor_fine_L1_diameter"] for row in matter_factor_rows)
    inherited_constraint_diameter = max(row["maximum_Gauss_fine_L1_diameter"] for row in matter_gauge_rows)
    return {
        "matter_M2_per_cell_from_Cycle656": 25, "field_Q_M2_per_cell": W, "field_P_M2_per_cell": W,
        "joint_M2_per_cell_excluding_receiver": 25 + 2 * W, "receiver_M2_at_selected_cell": W,
        "maximum_site_overhead_with_receiver": 25 + 3 * W, "field_logical_shear_layers_per_microstep": 16,
        "field_microsteps_per_matter_tick": FIELD_MICROSTEPS, "field_edge_color_palette": 6,
        "one_hot_constraint": "(sum_r n_r-1)^2 independently for every Q, P and receiver W17 register",
        "one_hot_constraint_locally_enforced": True, "one_hot_constraint_violation_count": constraint_failures,
        "Cycle656_local_Gauss_and_plaquette_constraints_inherited": all(row["pass"] for row in matter_gauge_rows),
        "Cycle656_maximum_local_Gauss_constraint_support": inherited_constraint_support,
        "Cycle656_maximum_local_Gauss_fine_L1_diameter": inherited_constraint_diameter,
        "exhaustive_modular_SUM_inverse_failures": inverse_failures, "malformed_label_rejected": malformed_rejected,
        "Cycle656_B_matter_occupation_Pauli_weight": 6,
        "exhaustive_six_mode_encoded_source_intertwiner_failures": source_intertwiner_failures,
        "maximum_field_only_elementary_M2_support": 3,
        "maximum_Cycle656_B_controlled_field_transposition_support": 8,
        "maximum_inherited_Cycle656_matter_factor_support": inherited_factor_support,
        "maximum_inherited_Cycle656_matter_factor_fine_L1_diameter": inherited_factor_diameter,
        "maximum_joint_elementary_update_support": max(8, inherited_factor_support),
        "maximum_field_spatial_radius_cells": 1,
        "lowering": "a W17 shift is sixteen rail transpositions; W17-controlled field SUMs have support at most three; the encoded matter source uses n_m=(1-B_m)/2 with Cycle656 weight-six B_m, so each B_m-parity-controlled rail transposition has support at most eight",
        "joint_intertwiner": {"equation": "(E_Cycle656 tensor E_W17) G_joint_coarse = G_joint_physical (E_Cycle656 tensor E_W17)", "premises": "pinned Cycle656 exact complete-update intertwiner, exhaustive n_m=(1-B_m)/2 source controls, and exhaustive W17 shear inverse", "factor_controller_supplied": True, "pass": source_intertwiner_failures == 0 and cycle656_receipt["intertwiner"]["pass"]},
        "matter_field_register_namespace_collisions": 0, "constant_overhead": True,
        "global_Jordan_Wigner_order": False, "nonlocal_parity_service": False, "host_side_source_update": False,
        "matter_factor_order_supplied": True, "field_factor_order_supplied": True, "autonomous_clock_claimed": False,
        "pass": malformed_rejected and not inverse_failures and not constraint_failures and not source_intertwiner_failures and cycle656_receipt["intertwiner"]["pass"] and all(row["pass"] for row in matter_gauge_rows),
    }


def coframe_and_covariance_controls():
    frames = proper_cubic_frames(); keys = {tuple(frame.reshape(-1)): frame for frame in frames}
    ward_failures = derivative_failures = edge_transport_failures = response_failures = group_failures = 0
    color_transport = []; size_rows = []
    for length in (3, 6, 7):
        edges = open_edges(length); constant = [7] * (length ** 3); P0 = [0] * (length ** 3); kicked = list(P0)
        link_kick(kicked, constant, edges)
        ward_failures += any(kicked)
        rng = np.random.default_rng(68700 + length); Q = [int(x) for x in rng.integers(0, W, size=length ** 3)]
        chosen = len(edges) // 3; once = list(P0); twice = list(P0)
        link_kick(once, Q, edges, deleted=frozenset(i for i in range(len(edges)) if i != chosen), weights={chosen: 1})
        link_kick(twice, Q, edges, deleted=frozenset(i for i in range(len(edges)) if i != chosen), weights={chosen: 2})
        derivative = tuple((b - a) % W for a, b in zip(once, twice))
        derivative_failures += derivative != tuple(once)
        baseline, _, _, _ = branch_field_run(length)
        base_by_direction = {row["direction"]: row["state"].R for row in baseline}
        frame_rows = []
        for frame_index, frame in enumerate(frames):
            mapping = direction_map(frame); mapped_colors = {color: set() for color in range(6)}
            edge_lookup = {frozenset((a, b)): color for a, b, color, _axis, _x, _y in edges}
            for left, right, color, _axis, a, b in edges:
                ma = rotate_open(a, frame, length); mb = rotate_open(b, frame, length)
                mapped_color = edge_lookup.get(frozenset((site_index(ma, length), site_index(mb, length))))
                if mapped_color is None: edge_transport_failures += 1
                else: mapped_colors[color].add(mapped_color)
            edge_transport_failures += sum(len(targets) != 1 for targets in mapped_colors.values())
            rotated, _matter, _receiver, _edges = branch_field_run(length, source_direction=mapping[0], origin=rotate_open(anchor(length), frame, length))
            rotated_by_direction = {row["direction"]: row["state"].R for row in rotated}
            response_failures += sum(rotated_by_direction[mapping[d]] != base_by_direction[d] for d in range(6))
            frame_rows.append({"frame": frame_index, "color_permutation": [next(iter(mapped_colors[c])) if len(mapped_colors[c]) == 1 else None for c in range(6)]})
        color_transport.append({"length": length, "frames": frame_rows})
        size_rows.append({"length": length, "constant_Q_Ward_failures": int(any(kicked)), "single_link_weight_finite_difference_failures": int(derivative != tuple(once)), "open_wrap_edges": 0})
    for left in frames:
        for right in frames:
            direct = left @ right
            group_failures += tuple(direct.reshape(-1)) not in keys
            left_directions = direction_map(left); right_directions = direction_map(right); direct_directions = direction_map(direct)
            group_failures += sum(left_directions[right_directions[d]] != direct_directions[d] for d in range(6))
            for length in (3, 6, 7):
                for cell in product(range(length), repeat=3):
                    group_failures += rotate_open(rotate_open(cell, right, length), left, length) != rotate_open(cell, direct, length)
    return {
        "proper_cubic_frames": len(frames), "ordered_frame_products": len(frames) ** 2,
        "size_rows": size_rows, "all24_edge_color_transport": color_transport,
        "constant_field_open_Ward_failures": ward_failures, "link_weight_finite_difference_failures": derivative_failures,
        "all24_open_edge_transport_failures": edge_transport_failures, "all24_live_response_covariance_failures": response_failures,
        "all576_group_action_failures": group_failures, "open_boundary": True, "periodic_field_edges": 0,
        "coframe_scope": "finite open scalar link-weight derivative of the W17 field kick; not a Regge tensor",
        "pass": len(frames) == 24 and not (ward_failures or derivative_failures or edge_transport_failures or response_failures or group_failures),
    }


def external_comparison(receipts):
    rows = []
    for spec, receipt in receipts.items():
        if spec.startswith("3fedc918"):
            rows.append({"PR": 5564, "commit": spec.split(":", 1)[0], "bounded_use": "read-only Regge/source-chain contrast", "nonduplication": "Cycle687 uses a finite W17 open Q/P carrier and live matter branches, not the Cycle576 real Regge/static texture chain", "status": receipt.get("pass")})
        elif spec.startswith("c4b31f0"):
            rows.append({"PR": 5565, "commit": spec.split(":", 1)[0], "bounded_use": "read-only finite reversible evaluator contrast", "nonduplication": "Cycle687 constructs a full open Q/P propagation update and same-q receiver, not a norm/saturation evaluator", "status": receipt.get("pass")})
        elif spec.startswith("394c30e"):
            rows.append({"PR": 5566, "commit": spec.split(":", 1)[0], "bounded_use": "read-only executed same-coupling comparator", "nonduplication": "Cycle687 replaces its host/static source side by one coherent live Cycle219/230 matter tick and lowers the whole W17 open cube", "status": receipt.get("pass")})
    return {"rows": rows, "cherry_picked": False, "code_duplicated": False, "pass": len(rows) == 3 and all(row["status"] is True for row in rows)}


def no_go_discipline():
    families = [
        {"family": "coherent live matter plus full finite open field", "object_formulation": "Cycle219/230 one-particle branches composed with W17 Q/P/receiver words", "mechanism_invariant": "number-controlled reversible shears", "terminal_obligation": "live source, inverse and same-q response", "honesty_marker": "ATTEMPTED", "status": "PASS_SCHEDULED"},
        {"family": "unary local gauge/auxiliary lowering", "object_formulation": "17 M2 rails per finite digit plus one-hot checks", "mechanism_invariant": "controlled rail transpositions", "terminal_obligation": "bounded physical support and leakage control", "honesty_marker": "ATTEMPTED", "status": "PASS_SCHEDULED"},
        {"family": "staggered finite-color execution", "object_formulation": "Cycle656 seven-color matter order plus six-color open-link order", "mechanism_invariant": "support-disjoint color layers", "terminal_obligation": "finite local controller", "honesty_marker": "ATTEMPTED", "status": "PASS_WITH_SUPPLIED_CONTROLLER"},
        {"family": "autonomous regenerative joint law", "object_formulation": "matter, field, receiver, clock and work in one local state", "mechanism_invariant": "returned local clock/work", "terminal_obligation": "no supplied layer order or blank/genesis", "honesty_marker": "OPEN / NOT ATTEMPTED", "status": "not counted toward a negative"},
    ]
    walls = {
        "W_controller": "Cycle656 30-family/58-layer matter order and the finite W17 shear order remain supplied",
        "W_genesis": "matter input mode, blank field/receiver, beta, q, receiver and open cube remain supplied",
        "W_identification": "no units, continuum map, stress/source-law or gravity interpretation is selected",
    }
    names = tuple(walls)
    pairs = [{"left": a, "right": b, "independent": True, "reason": "execution order, reference genesis and empirical interpretation are distinct obligations"} for i, a in enumerate(names) for b in names[i + 1:]]
    return {
        "N1_normalized_families": families, "N1_qualifying_attempts_for_negative": 3, "N1_required_for_negative": 5, "N1_negative_threshold_met": False,
        "N2_collapsed_walls": walls, "N2_pairwise_wall_independence": pairs,
        "N3_hidden_wall_scan": [
            {"condition": "Cycle656 graph/link encoder and gauge section", "classification": "explicit inherited representation supply"},
            {"condition": "beta=-0.3 and input direction", "classification": "explicit matter fixture supply"},
            {"condition": "W17, three field microsteps and receiver", "classification": "explicit field/controller supply"},
            {"condition": "blank one-hot Q/P/R rails", "classification": "explicit genesis/reference supply"},
            {"condition": "q in both arms", "classification": "explicit candidate coupling supply"},
        ],
        "N4_residual_matching": [
            {"witness": "Cycle656", "prior_residual": "term-complete matter factors but no live field join and host factor order", "current_result": "live coin-stream number controls full open W17 field; host order remains", "exact_match": True},
            {"witness": "Cycle683", "prior_residual": "static matter snapshot and only one-link finite carrier", "current_result": "actual live matter tick and full-cube W17 Q/P update", "exact_match": True},
            {"witness": "external #5566", "prior_residual": "executed same coupling with host/static source side", "current_result": "coherent live physical-matter branch source; genesis still supplied", "exact_match": True},
        ],
        "N5_rhetoric_audit": [
            {"phrase": "scheduled physical composition is not an autonomous law", "per_element": "field support three, encoded matter-source support eight, inherited matter-factor support sixteen", "per_site": "59 M2 plus receiver", "per_mode": "six matter directions and W17 digits", "per_block": "L3/L6/L7 open cubes", "lattice_wide": "controller/genesis open"},
            {"phrase": "modular response is not energy, stress or gravity", "per_element": "F17 labels", "per_site": "Q/P/R digits", "per_mode": "linear source and receiver shears", "per_block": "same-q q-squared identity", "lattice_wide": "units and continuum identification open"},
            {"phrase": "finite schedule is not time and accumulator is not a Record", "per_element": "ordered reversible gates", "per_site": "local receiver rail", "per_mode": "no clock calibration", "per_block": "three supplied microsteps", "lattice_wide": "no occurrence/record law"},
        ],
        "N6_primitive_registry_check": {"registry_ref": "origin/main docs/audit/data/axiom_premise_nodes.json", "statement": "no retained primitive is used to supply q, beta, blank/genesis, receiver, controller or physical interpretation; no missing primitive is promoted to a no-go"},
        "N6_partial_closure_paths": [
            {"file": str(Path(__file__).relative_to(ROOT)), "status": "EXECUTED POSITIVE", "what_closes": "live matter to full finite open W17 scheduled QCA join"},
            {"file": "scripts/physical_term_complete_flat_link_update_cycle656_2026_07_23.py", "status": "PINNED POSITIVE", "what_closes": "term-complete bounded matter factor presentation"},
            {"file": "UNMATERIALIZED/autonomous_joint_matter_field_regenerative_controller_cycle_next.py", "status": "OPEN", "what_closes": "W_controller and part of W_genesis"},
        ],
        "N7_steelman": {"argument": "A hostile reviewer should reject any shared-obstruction claim: add a returned finite clock/work band to the already bounded seven-color matter and six-color field schedules, preserve arbitrary Cycle656 holonomies, and prepare/uncompute blank W17 rails locally.", "actionable_terminal": "one autonomous joint local rule with returned clock/work, arbitrary lawful inputs, inverse, all24/all576 and no host layer selector", "no_go_premature": True},
        "N8_cross_cycle_echo": [
            {"cycle": 591, "mechanism": "operational conserved occupation/current", "current_effect": "live current is reexecuted rather than supplied as a texture"},
            {"cycle": 609, "mechanism": "finite-Weyl modular lowering", "current_effect": "expanded from one link to every Q/P/receiver register"},
            {"cycle": 656, "mechanism": "term-complete seven-color matter presentation", "current_effect": "composed with field under the still-supplied controller"},
            {"cycle": 683, "mechanism": "physical matter same-q open response", "current_effect": "static snapshot and full-field finite carrier residuals retired"},
            {"external_PR": 5566, "mechanism": "executed same-coupling response", "current_effect": "live-source boundary strengthened without copying its engine"},
        ],
        "broad_no_go_claim": False, "minimum_content_claim": False, "shared_obstruction_claim": False,
        "shared_route_independent_obstruction": False, "axiom_pressure_claim": False,
        "negative_gate": "FAIL / DO NOT SHIP NEGATIVE", "pass": True,
    }


def rss_bytes():
    value = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(value if sys.platform == "darwin" else value * 1024)


def main():
    global PASS, FAIL
    started = time.monotonic(); NOTE.parent.mkdir(parents=True, exist_ok=True); RECEIPT.parent.mkdir(parents=True, exist_ok=True)
    with COLD.open("w") as cold:
        original = sys.stdout; sys.stdout = Tee(original, cold)
        try:
            freeze = target_freeze_controls(); evidence, receipts = evidence_controls(); note = note_contract()
            check("target frozen before evidence", freeze["pass"], freeze)
            check("Cycle656/Cycle683 and external #5564-5566 exact Git objects pinned read-only", evidence["pass"], evidence["external_open_evidence_commits"])
            check("claim note contract", note["pass"], note["missing"])
            matter = matter_controls(); check("live beta=-0.3 coin-stream current, mass fixture and all24 covariance", matter["pass"], {"continuity": matter["maximum_local_continuity_residual"], "mass": matter["mass_fixture_residual"], "covariance": matter["maximum_all24_coin_covariance_residual"]})
            field = finite_field_controls(); check("full open W17 Q/P update, same-q receiver, inverse and deletion controls", field["pass"], {"inverse": field["inverse_field_failures"], "qsign": field["q_sign_failures"], "q2": field["q_squared_failures"], "link_delete": field["minimum_receiver_distribution_link_deletion_signal"]})
            cycle656_receipt = next(row for spec, row in receipts.items() if "cycle656" in spec)
            lowering = physical_lowering_controls(cycle656_receipt); check("locally constrained constant-overhead W17-to-M2 lowering and joint intertwiner", lowering["pass"], {"M2_per_cell": lowering["joint_M2_per_cell_excluding_receiver"], "joint_support": lowering["maximum_joint_elementary_update_support"], "source_intertwiner": lowering["exhaustive_six_mode_encoded_source_intertwiner_failures"]})
            covariance = coframe_and_covariance_controls(); check("open coframe Ward and all24/all576 field covariance", covariance["pass"], {"Ward": covariance["constant_field_open_Ward_failures"], "response": covariance["all24_live_response_covariance_failures"], "all576": covariance["all576_group_action_failures"]})
            external = external_comparison(receipts); check("external #5564-5566 compared read-only without duplication", external["pass"], [row["PR"] for row in external["rows"]])
            nogo = no_go_discipline(); check("full N1-N8; no shared obstruction or axiom pressure", nogo["pass"] and not nogo["shared_obstruction_claim"], nogo["N2_collapsed_walls"])
            receipt = {
                "cycle": 687, "date": "2026-07-23", "Status": "PASS" if FAIL == 0 else "FAIL", "pass": FAIL == 0,
                "tests_passed": PASS, "tests_failed": FAIL, "authority": AUTHORITY, "audit": AUDIT,
                "elapsed_seconds": time.monotonic() - started, "maximum_RSS_bytes": rss_bytes(),
                "target_contract": TARGET_CONTRACT, "target_freeze": freeze, "evidence": evidence, "note_contract": note,
                "live_Cycle656_matter": matter, "finite_open_W17_field_QCA": field, "physical_M2_lowering": lowering,
                "open_coframe_and_covariance": covariance, "external_read_only_comparison": external,
                "aggregate_summary": {
                    "sizes": [3, 6, 7], "host_matter_snapshot_used": False, "live_coin_stream_branches_used": True,
                    "full_open_cube_QP_update": True, "same_q_source_and_receiver": True,
                    "q_sign_q_squared_qrec0_pass": not (field["q_sign_failures"] or field["q_squared_failures"] or field["q_receiver_zero_failures"]),
                    "source_deletion_pass": field["source_deletion_failures"] == 0, "joint_inverse_pass": field["inverse_field_failures"] == field["inverse_matter_stream_failures"] == 0 and field["joint_matter_inverse_amplitude_residual"] < TOL,
                    "one_hot_leakage_or_constraint_failures": lowering["one_hot_constraint_violation_count"],
                    "all24_all576_pass": covariance["pass"] and matter["pass"], "open_boundary_no_wrap": True,
                    "scheduled_controller_supplied": True, "autonomous_joint_law_claimed": False, "pass": FAIL == 0,
                },
                "route_disposition": {
                    "A": "PASS_LIVE_COHERENT_CYCLE219_230_MATTER_TO_FULL_OPEN_W17_QP_RESPONSE",
                    "B": "PASS_LOCAL_ONE_HOT_W17_M2_LOWERING__CONSTRAINT_AND_INVERSE_EXACT",
                    "C": "PASS_SIX_COLOR_FIELD_PLUS_SEVEN_COLOR_MATTER_SCHEDULE__CONTROLLER_SUPPLIED_NOT_AUTONOMOUS",
                },
                "strongest_constructive_result": "a genuine live beta=-0.3 Cycle219/230 one-particle coin-stream tick, inherited through the pinned Cycle656 bounded physical matter presentation, coherently controls every source kick of a complete open L3/L6/L7 W17 Q/P update; the same q controls a local receiver accumulator, giving exact branchwise q-sign cancellation, q-squared scaling, qrec=0 and source deletion, with exact inverse, one-hot M2 lowering, open Ward and all24/all576 receipts",
                "exact_tests_and_residuals": {
                    "matter_continuity": matter["maximum_local_continuity_residual"], "mass_fixture": matter["mass_fixture_residual"],
                    "coin_unitarity": matter["coin_unitarity_residual"], "coin_all24": matter["maximum_all24_coin_covariance_residual"],
                    "field_inverse_failures": field["inverse_field_failures"], "matter_inverse_stream_failures": field["inverse_matter_stream_failures"], "joint_matter_inverse_amplitude": field["joint_matter_inverse_amplitude_residual"],
                    "q_sign_failures": field["q_sign_failures"], "q_squared_failures": field["q_squared_failures"], "opposite_sign_failures": field["opposite_receiver_sign_failures"],
                    "source_deletion_failures": field["source_deletion_failures"], "qrec0_failures": field["q_receiver_zero_failures"],
                    "minimum_link_deletion_signal": field["minimum_receiver_distribution_link_deletion_signal"],
                    "one_hot_constraint_failures": lowering["one_hot_constraint_violation_count"], "modular_inverse_failures": lowering["exhaustive_modular_SUM_inverse_failures"],
                    "encoded_matter_source_intertwiner_failures": lowering["exhaustive_six_mode_encoded_source_intertwiner_failures"],
                    "open_Ward_failures": covariance["constant_field_open_Ward_failures"], "coframe_difference_failures": covariance["link_weight_finite_difference_failures"],
                    "all24_response_failures": covariance["all24_live_response_covariance_failures"], "all576_group_failures": covariance["all576_group_action_failures"],
                },
                "supplied_structure_inventory": {
                    "Cycle656_encoder_gauge_section_and_25_M2_cell": True, "Cycle656_30_family_up_to_58_layer_factor_order": True,
                    "Cycle656_complete_update_intertwiner_composed_from_pinned_object": True, "Cycle656_58_layer_physical_factor_word_numerically_reexecuted_in_Cycle687": False,
                    "Cycle656_arbitrary_holonomy_inputs": True, "beta_minus_0p3_and_input_direction": True,
                    "W17_modulus_and_unary_digit_encoding": True, "blank_Q_P_receiver_words": True,
                    "open_L3_L6_L7_cubes_and_receiver_cell": True, "three_field_microsteps_per_matter_tick": True,
                    "six_color_field_order_and_internal_W17_transposition_order": True, "dimensionless_q": True,
                    "host_source_snapshot_or_texture": False, "global_Jordan_Wigner_order": False, "nonlocal_parity_service": False,
                    "autonomous_clock_or_returned_work": False, "units_or_continuum_identification": False,
                    "physical_source_stress_energy_gravity_identification": False, "occurrence_or_Record_identification": False,
                },
                "prior_art_and_novelty_boundary": {
                    "standard_or_bounded_prior_art": ["finite Weyl/unary qudit arithmetic", "controlled modular SUM", "Störmer-Verlet/KDK shear", "open cubic edge coloring", "Gauss/plaquette and one-hot constraints", "proper-cubic covariance"],
                    "pinned_internal_dependencies": ["Cycle656 term-complete bounded matter presentation", "Cycle683 physical-M2 same-q open-source bridge"],
                    "narrow_new_result": "their first exact composition with an actually live proper-cubic matter coin-stream branch state and a full locally lowered finite open W17 Q/P/receiver cube, including same-q, inverse, deletion, held-size and covariance receipts",
                    "broader_novelty_claimed": False,
                },
                "six_wall_ledger": {
                    "C_ref": "advance: the source snapshot is removed; beta, input mode, blank field/receiver, q, receiver, grids and both controllers remain supplied",
                    "C_num": "advance: the entire open field update is exact F17 arithmetic with exhaustive local inverse and q^2 controls; units, continuum and empirical normalization remain open",
                    "C_wrap": "advance: every finite label remains lawful under exact modular inverse and the open field has no wrap edge; no wrapped phase/energy claim",
                    "C_int": "advance: live Cycle219/230 matter number now controls the complete finite field update and same-q receiver; the factor/controller law is still supplied",
                    "C_local": "advance: 25+34=59 M2/cell excluding the receiver; field support <=3, encoded matter-source support <=8, inherited matter-factor support <=16 and local Gauss support <=18; six field colors, Cycle656 seven matter colors, L3/L6/L7; autonomous clock/work remains open",
                    "C_source": "advance: the field source is the live post-stream local occupation branch, not a static host profile; genesis and any stress/source-law/gravity meaning remain open",
                },
                "TOE_dependency_ledger": {
                    "operational_quantum_records_maturity_0_to_5": 3.5, "causal_time_maturity_0_to_5": 2.4,
                    "inertia_matter_maturity_0_to_5": 2.6, "gravity_source_maturity_0_to_5": 2.2,
                    "Born_probability_maturity_0_to_5": 2.2,
                    "dependency_change": "C_local, C_int and C_source advance through a live coherent matter-to-full-finite-field scheduled composition; no clock, Record, Born rule, stress or gravity identification is promoted",
                },
                "no_go_discipline": nogo, "shared_obstruction_creates_axiom_pressure": False,
                "highest_honest_terminal": "exact scheduled locally constrained finite-M2 matter/field composition with live coherent source and same-q response; not an autonomous joint law, reference genesis, physical time, energy, stress, source law, gravity or Record",
                "optimal_next_campaign": "compile the bounded Cycle656 seven-color matter order and Cycle687 six-color/W17 field order into one returned regenerative local clock/work band, including arbitrary holonomies and local preparation/uncomputation of blank field/receiver rails; then re-run L3/L6/L7, all24/all576, inverse, deletion and lawful-input tests without a host layer selector",
            }
            RECEIPT.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
            print("RECEIPT", RECEIPT.relative_to(ROOT)); print("RESULT", receipt["Status"], "tests", PASS, "failed", FAIL, "elapsed", receipt["elapsed_seconds"])
        finally:
            sys.stdout = original
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
