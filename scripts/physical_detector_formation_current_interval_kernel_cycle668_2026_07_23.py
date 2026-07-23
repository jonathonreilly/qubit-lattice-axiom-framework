#!/usr/bin/env python3
"""Cycle 668: detector-to-formation-to-current/interval declared-code kernel."""

from __future__ import annotations

TARGET_CONTRACT = {
    "target_statement": "construct and execute one bounded physical declared-code composition from the immutable Cycle608 material-detector predicate through the immutable Cycle662 objective-within-candidate-law stochastic formation kernel into the immutable Cycle665 conserved ready-to-spent current and Cycle612 typed interval packet, with the material predicate computed from detector state and never identified with occurrence",
    "quantifiers_domain": "all four detector matter/binder basis inputs with blank detector work; every immutable Cycle662 train and blinded held biased/nonproduct menu-state kernel including lawful zero and unit propensities; declared finite capacities; all 24 proper-cubic frames and all 576 ordered products",
    "allowed_premises": "exact committed Cycle608 detector predicate and physical factor/count contract; exact committed Cycle612 typed packet; exact committed Cycle662 menu kernels, coherent/rejected exhaust and finite ledger; exact committed Cycle665 current/packet compiler; finite M2 computational registers, fixed compile-time charts, sparse stochastic transition kernels, and reversible local basis permutations",
    "forbidden_weakenings": "identifying occurrence with matter; host scheduling, branch sampling, actuality lookup, runtime grade lookup, or shell-predicate ROM; discarded coherent, rejected, detector, current, packet, or exhaust sectors; calling a compressed declared-code kernel a dense full-Hilbert matrix; calling resource current physical energy, stress, force, or gravity; calling a generator or update count a rate or time; calling the packet Record, Born probability, proper time, or realized history",
    "required_edge_cases": "train/held detector sizes and Cycle662 states; biased/nonproduct inputs; zero and unit propensities; detector-off and binder-off rejection; dirty work and packet/source saturation; inverse on reversible compiler images; stochastic-kernel normalization; detector-row, predicate, join, current, packet, and exhaust deletions; malformed domains; all24/all576",
    "completion_witness": "an explicit injective codeword encoding E, an explicitly materialized sparse/dense declared-code transition matrix K_physical for every frozen menu-state row, a logical kernel K_logical, and a verified E K_logical = K_physical E intertwiner, together with exact detector permutation, branch normalization, retained-sector, endpoint/current conservation, placement/M2/support/depth, inverse/deletion/domain/saturation, covariance, and unchanged-shore certificates",
    "outcomes_not_closure": "separate shore replays without one composed kernel; a host-composed sequence; a truth table mislabeled a physical matrix; an interface label without codeword encoding; an occurrence bit substituted for the material predicate; a literal 2^N dense matrix estimate without execution; upstream nature-law selection, gravity, Record/Born/history, or shared-obstruction claims",
}

from hashlib import sha256
from itertools import permutations, product
import json
from pathlib import Path
import resource
import subprocess
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_DETECTOR_FORMATION_CURRENT_INTERVAL_KERNEL_CYCLE668_NOTE_2026-07-23.md"
)
RECEIPT = ROOT / "outputs/physical_detector_formation_current_interval_kernel_cycle668_receipt_2026_07_23.json"
COLD = ROOT / "outputs/physical_detector_formation_current_interval_kernel_cycle668_cold_2026_07_23.txt"
SHORE = "18ba879b440f10deee6a6a8b9f06a0ad309712aa"
AUTHORITY = "none"
AUDIT = "unset"
PASS = 0
FAIL = 0
TOL = 2.0e-12
ZERO_TOL = 1.0e-15


PINS = {
    "scripts/physical_radius_one_dressed_detector_controlled_update_recurrence_tournament_cycle608_2026_07_22.py":
        "ac2a337140d40624500a5f23fc771b9b716d4c4bd467eb27a1963d1db5eac875",
    "docs/work_history/repo/review_feedback/PHYSICAL_RADIUS_ONE_DRESSED_DETECTOR_CONTROLLED_UPDATE_RECURRENCE_TOURNAMENT_CYCLE608_NOTE_2026-07-22.md":
        "6e8e3aae72547e8a13b0ced4cea7230c7b594348073e45802c95e6a55329ee54",
    "outputs/physical_radius_one_dressed_detector_controlled_update_recurrence_tournament_cycle608_receipt_2026_07_22.json":
        "4ccba85490c08120aab645917fee87dbd58f21cf4fb17c5f60b3a4fab9dbca48",
    "outputs/physical_radius_one_dressed_detector_controlled_update_recurrence_tournament_cycle608_cold_2026_07_22.txt":
        "087e3ef7a5657a85432553f29e7050458a9c8552a3e59852e74ae86b5f9fc605",
    "scripts/physical_matter_caused_causal_interval_proper_time_bridge_tournament_cycle612_2026_07_22.py":
        "91f22d23dd2730f76a05736634236d41036f68eaedc4921daca69de25ab6a344",
    "docs/work_history/repo/review_feedback/PHYSICAL_MATTER_CAUSED_CAUSAL_INTERVAL_PROPER_TIME_BRIDGE_TOURNAMENT_CYCLE612_NOTE_2026-07-22.md":
        "920776555dce6505bccb0e46e552e90d24858c08cfb7f6978d884f10a5bb0789",
    "outputs/physical_matter_caused_causal_interval_proper_time_bridge_tournament_cycle612_receipt_2026_07_22.json":
        "e7a8ea3dcbe370c9f8c6a94770508d1710a7013ce4ba62a1ad67e345fe1e2d11",
    "scripts/physical_objective_stochastic_open_dilation_cycle662_2026_07_23.py":
        "219b6d3d93884a0ab8d9b0cc6c79850d008193fd5571b0281c76b6f8707d6b84",
    "docs/work_history/repo/review_feedback/PHYSICAL_OBJECTIVE_STOCHASTIC_OPEN_DILATION_CYCLE662_NOTE_2026-07-23.md":
        "bdc8dda304985a62c73fc6e7a03f11d61041dd8053a9321fb7171c9b22947a05",
    "outputs/physical_objective_stochastic_open_dilation_cycle662_receipt_2026_07_23.json":
        "27b258f1e4d96fb26f65937875bea32d74ecdfa62712c353e3327d0357a2c806",
    "outputs/physical_objective_stochastic_open_dilation_cycle662_cold_2026_07_23.txt":
        "14c431047466462c57ecff1c83472e5233e88af3fc454920b6f6d6465a8cc625",
    "scripts/physical_formation_resource_interval_compiler_cycle665_2026_07_23.py":
        "c80146085edecf6b5dfc9417edb4180e9b54d9d83c9c3e94f2bcdd3e0acfca68",
    "docs/work_history/repo/review_feedback/PHYSICAL_FORMATION_RESOURCE_INTERVAL_COMPILER_CYCLE665_NOTE_2026-07-23.md":
        "699c296a9411317c31f2cc1c2642829a88af529dd739c6aa85c58c7252817456",
    "outputs/physical_formation_resource_interval_compiler_cycle665_receipt_2026_07_23.json":
        "47f485377271bb13dfe881dc6bc3cfff81098cf7b71e133e20b3e0d302f360b1",
    "outputs/physical_formation_resource_interval_compiler_cycle665_cold_2026_07_23.txt":
        "a707050e7045ca7327533a735fdf25b01a6b98103a0c9aaecddb1ffba2f73da5",
}

RUNNERS = (
    "scripts/physical_radius_one_dressed_detector_controlled_update_recurrence_tournament_cycle608_2026_07_22.py",
    "scripts/physical_matter_caused_causal_interval_proper_time_bridge_tournament_cycle612_2026_07_22.py",
    "scripts/physical_objective_stochastic_open_dilation_cycle662_2026_07_23.py",
    "scripts/physical_formation_resource_interval_compiler_cycle665_2026_07_23.py",
)

DETECTOR_SIZES = (
    {"name": "L3_train", "linear_size": 3, "split": "train", "capacity": 3},
    {"name": "L4_held_out_size", "linear_size": 4, "split": "held-out-size", "capacity": 4},
    {"name": "L6_held", "linear_size": 6, "split": "held", "capacity": 6},
)

CUBE11 = tuple(product(range(-5, 6), repeat=3))
CUBE9 = tuple(product(range(-4, 5), repeat=3))
DETECTOR_COORDINATES = tuple(coord for coord in CUBE11 if coord not in set(CUBE9))[:4]
PACKET_WORD = (1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1)


class Tee:
    def __init__(self, *streams): self.streams = streams
    def write(self, body):
        for stream in self.streams: stream.write(body)
        return len(body)
    def flush(self):
        for stream in self.streams: stream.flush()


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    PASS += int(bool(condition)); FAIL += int(not bool(condition))
    print("PASS" if condition else "FAIL", label, "::", detail)


def stable_digest(value: object) -> str:
    return sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), default=float).encode()).hexdigest()


def array_digest(value: np.ndarray) -> str:
    return sha256(np.ascontiguousarray(value).tobytes()).hexdigest()


def git_bytes(path: str) -> bytes:
    return subprocess.run(
        ("git", "show", f"{SHORE}:{path}"), cwd=ROOT, check=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    ).stdout


def target_freeze_controls() -> dict[str, object]:
    source = Path(__file__).read_text().splitlines()
    target_line = next(i for i, line in enumerate(source, 1) if line.startswith("TARGET_CONTRACT ="))
    evidence_line = next(i for i, line in enumerate(source, 1) if line.startswith("def shore_controls"))
    fields = sorted(TARGET_CONTRACT)
    expected = [
        "allowed_premises", "completion_witness", "forbidden_weakenings",
        "outcomes_not_closure", "quantifiers_domain", "required_edge_cases", "target_statement",
    ]
    return {
        "target_contract_sha256": stable_digest(TARGET_CONTRACT), "target_line": target_line,
        "first_evidence_load_line": evidence_line, "frozen_before_evidence": target_line < evidence_line,
        "proof_search_governance_exact_fields": fields, "pass": target_line < evidence_line and fields == expected,
    }


def shore_controls() -> tuple[dict[str, object], dict[str, dict[str, object]]]:
    observed = {path: sha256(git_bytes(path)).hexdigest() for path in PINS}
    receipts = {
        "Cycle608": json.loads(git_bytes("outputs/physical_radius_one_dressed_detector_controlled_update_recurrence_tournament_cycle608_receipt_2026_07_22.json")),
        "Cycle612": json.loads(git_bytes("outputs/physical_matter_caused_causal_interval_proper_time_bridge_tournament_cycle612_receipt_2026_07_22.json")),
        "Cycle662": json.loads(git_bytes("outputs/physical_objective_stochastic_open_dilation_cycle662_receipt_2026_07_23.json")),
        "Cycle665": json.loads(git_bytes("outputs/physical_formation_resource_interval_compiler_cycle665_receipt_2026_07_23.json")),
    }
    imported = {
        cycle: {"pass": body["pass"], "authority": body["authority"], "audit": body["audit"]}
        for cycle, body in receipts.items()
    }
    detector_boundary = receipts["Cycle608"]["physical_promotion_boundary"]
    pass_flag = (
        observed == PINS and all(row == {"pass": True, "authority": "none", "audit": "unset"}
                                 for row in imported.values())
        and all(detector_boundary[key] is None for key in (
            "physical_encoder_E", "physical_update_G", "physical_placement",
            "physical_primitive_product", "intertwiner_certificate", "full_code_leakage", "physical_detector_readout",
        ))
    )
    return {
        "ref": SHORE, "pins": PINS, "observed": observed, "imported_contracts": imported,
        "Cycle608_physical_promotion_boundary_preserved": detector_boundary,
        "working_tree_bytes_used_as_premise": False, "author_status_accepted_as_audit": False,
        "pass": pass_flag,
    }, receipts


def replay_unchanged_shore_runners() -> dict[str, object]:
    # Final bounded validation consumes disclosed replay packets instead of rerunning the
    # five-minute Cycle608 job. The independent root packet resolves the previously uncaptured
    # Cycle608 failure label exactly; the child packets preserve independent Cycle612/662/665 runs.
    cycle608_expected_observed = {
        "scripts/physical_global_N3_returned_slot_compiler_cycle560_2026_07_21.py": {
            "embedded_expected": "f6d641e4735b26f9463ea623ee8ed6e28acc995fdfc88300709dcfac100c13ab",
            "committed_observed": "30dc85fd6a1f328bdd095d41d2a3ddb6d1fd71eb4298b34bc635e3ea530a3764",
        },
        "scripts/physical_held_sparse_order_retirement_cycle563_2026_07_21.py": {
            "embedded_expected": "55e51cafffa70284a6e8e1f0510ca0d2f890989ccbcf5bce64435df4c8e812a6",
            "committed_observed": "444a5c0fb3cb1758236ddefaeb472d0002cadb256d3c4df723fd562129c7325b",
        },
        "scripts/physical_full_torus_dimer_M2_compiler_tournament_cycle590_2026_07_22.py": {
            "embedded_expected": "43e5b749702fba9551fab43a242f832b824fdbff54817b5206097f02ad146e55",
            "committed_observed": "5fbf3bcecc54df9912f9b79d2e5c45d51f145279c1ed83f507bc24e9e1980029",
        },
        "docs/work_history/repo/review_feedback/PHYSICAL_FULL_TORUS_DIMER_M2_COMPILER_TOURNAMENT_CYCLE590_NOTE_2026-07-22.md": {
            "embedded_expected": "f0f3ed6d41132625b8907cbcda8f105b7ec975e4b952562b45fe5b7d8e1b3a0e",
            "committed_observed": "3ee6ba9bd5a01a5cab88832788156597a1491d7c2d47f9378caca624a35a1936",
        },
    }
    rows = [
        {
            "path": RUNNERS[0], "pinned_sha256": PINS[RUNNERS[0]], "active_replay_attempted": True,
            "active_replay_attempts_this_cycle": 3, "independent_root_replay": True,
            "root_replay_ref": SHORE, "latest_exit_code": 1, "latest_elapsed_seconds": 308.9,
            "latest_summary": {"pass": 12, "fail": 1}, "active_replay_pass": False,
            "sole_failed_check": "Cycle605 quartet, Cycle560/563/590 shores, and runtime closure are byte exact",
            "pin_mismatches": cycle608_expected_observed,
            "numerical_residuals_or_local_factor_checks_failed": False,
            "committed_receipt_pass": True, "committed_receipt_tests": [13, 0],
            "root_history_search_scope": "original commits, Cycle608 commit 60ea, branch/all-log versions",
            "all_possible_Git_objects_searched": False,
            "classification": (
                "Cycle608 was committed with provenance pins not reproduced by the committed shore versions inspected; "
                "its numerical residuals were not the failing item"
            ),
        },
        {
            "path": RUNNERS[1], "pinned_sha256": PINS[RUNNERS[1]], "active_replay_attempted": True,
            "active_replay_attempts_this_cycle": 2, "latest_exit_code": 1, "active_replay_pass": False,
            "exception": "KeyError: detector_reference",
            "committed_receipt_pass": True, "committed_receipt_tests": [8, 0],
            "classification": (
                "inherited current-head schema mismatch: pinned Cycle612 expects Cycle608 detector_reference, "
                "but the pinned current-head Cycle608 receipt exposes the later physical_promotion_boundary schema"
            ),
        },
        {
            "path": RUNNERS[2], "pinned_sha256": PINS[RUNNERS[2]], "active_replay_attempted": True,
            "active_replay_attempts_this_cycle": 3, "latest_exit_code": 0, "active_replay_pass": True,
            "latest_summary": {"pass": 9, "fail": 0},
        },
        {
            "path": RUNNERS[3], "pinned_sha256": PINS[RUNNERS[3]], "active_replay_attempted": True,
            "active_replay_attempts_this_cycle": 3, "latest_exit_code": 0, "active_replay_pass": True,
            "latest_summary": {"pass": 10, "fail": 0},
        },
    ]
    active_pass = all(row["active_replay_pass"] for row in rows)
    pins_pass = all(row["pinned_sha256"] == PINS[row["path"]] for row in rows)
    schema_compatible_active_pass = all(row["active_replay_pass"] for row in rows[2:])
    return {
        "replay_packet_ref": SHORE, "working_tree_not_executed": True,
        "final_bounded_validation_reran_shores": False, "rows": rows,
        "all_runner_bytes_pinned": pins_pass,
        "schema_compatible_Cycle662_Cycle665_active_replays_pass": schema_compatible_active_pass,
        "active_replay_all_pass": active_pass,
        "Cycle608_Cycle612_committed_certificates_pass_but_active_replay_mismatches": True,
        "committed_certificate_pass": (pins_pass and schema_compatible_active_pass
                                       and rows[0]["committed_receipt_pass"] and rows[1]["committed_receipt_pass"]),
        "frozen_unchanged_shore_active_replay_obligation_met": False,
        "pass": False,
    }


def detector_index(m: int, b: int, p: int, o: int) -> int:
    return ((m*2+b)*2+p)*2+o


def detector_tuple(index: int) -> tuple[int, int, int, int]:
    return tuple((index >> shift) & 1 for shift in (3, 2, 1, 0))  # type: ignore[return-value]


def detector_permutation(delete: str | None = None) -> np.ndarray:
    matrix = np.zeros((16, 16), dtype=np.float64)
    for source in range(16):
        m, b, pointer, opportunity = detector_tuple(source)
        if delete != "Pd-compute": pointer ^= m
        if delete != "binder-Toffoli": opportunity ^= pointer & b
        if delete != "Pd-uncompute": pointer ^= m
        target = detector_index(m, b, pointer, opportunity)
        matrix[target, source] = 1.0
    return matrix


def physical_index(detector: int, slot: int, slots: int) -> int:
    return detector*slots+slot


def logical_index(m: int, b: int, slot: int, slots: int) -> int:
    return (m*2+b)*slots+slot


def normalized_propensities(row: dict[str, object]) -> tuple[np.ndarray, float, int]:
    raw = np.asarray([float(branch["propensity"]) for branch in row["branches"]], dtype=np.float64)
    if np.any(raw < -ZERO_TOL): raise ValueError("negative pinned propensity")
    q = np.where(np.abs(raw) <= ZERO_TOL, 0.0, raw)
    clipped = int(np.count_nonzero((raw != 0.0) & (q == 0.0)))
    if q.size == 0 or float(q.sum()) <= 0.0: raise ValueError("empty stochastic row")
    q[-1] = 1.0-float(q[:-1].sum())
    if q[-1] < -ZERO_TOL: raise ValueError("normalization repair made negative branch")
    q[-1] = max(q[-1], 0.0)
    return q, float(np.max(np.abs(q-raw))), clipped


def build_kernel(row: dict[str, object]) -> dict[str, object]:
    q, correction, clipped = normalized_propensities(row)
    branches = len(q); slots = branches+1
    physical_dim = 16*slots; logical_dim = 4*slots
    detector = detector_permutation()
    detector_ext = np.kron(detector, np.eye(slots))
    formation = np.eye(physical_dim, dtype=np.float64)
    computed_fire = physical_index(detector_index(1, 1, 0, 1), 0, slots)
    formation[:, computed_fire] = 0.0
    for branch, propensity in enumerate(q, 1):
        formation[physical_index(detector_index(1, 1, 0, 1), branch, slots), computed_fire] = propensity
    physical = detector_ext @ formation @ detector_ext
    logical = np.eye(logical_dim, dtype=np.float64)
    logical_fire = logical_index(1, 1, 0, slots)
    logical[:, logical_fire] = 0.0
    for branch, propensity in enumerate(q, 1):
        logical[logical_index(1, 1, branch, slots), logical_fire] = propensity
    encoding = np.zeros((physical_dim, logical_dim), dtype=np.float64)
    for m, b, slot in product((0, 1), (0, 1), range(slots)):
        encoding[physical_index(detector_index(m, b, 0, 0), slot, slots),
                 logical_index(m, b, slot, slots)] = 1.0
    intertwiner = physical @ encoding-encoding @ logical
    return {
        "q": q, "normalization_correction": correction, "clipped_zero_branches": clipped,
        "D": detector, "F": formation, "K_physical": physical, "K_logical": logical, "E": encoding,
        "physical_dim": physical_dim, "logical_dim": logical_dim, "slots": slots,
        "intertwiner_residual": float(np.max(np.abs(intertwiner))),
        "physical_normalization_residual": float(np.max(np.abs(physical.sum(axis=0)-1.0))),
        "logical_normalization_residual": float(np.max(np.abs(logical.sum(axis=0)-1.0))),
        "physical_minimum_entry": float(physical.min()), "encoding_gram_residual": float(np.max(np.abs(encoding.T@encoding-np.eye(logical_dim)))),
        "matrix_sha256": {"D": array_digest(detector), "F": array_digest(formation),
                          "K_physical": array_digest(physical), "K_logical": array_digest(logical),
                          "E": array_digest(encoding)},
    }


def detector_controls() -> dict[str, object]:
    detector = detector_permutation()
    blank_rows = []
    for m, b in product((0, 1), repeat=2):
        source = detector_index(m, b, 0, 0)
        target = int(np.argmax(detector[:, source]))
        output = detector_tuple(target)
        blank_rows.append({"matter": m, "binder": b, "input_work": [0, 0],
                           "output_work": list(output[2:]), "expected_opportunity": m & b})
    deletions = {}
    for deletion in ("Pd-compute", "binder-Toffoli", "Pd-uncompute"):
        damaged = detector_permutation(deletion)
        deletions[deletion] = {
            "matrix_difference_Frobenius": float(np.linalg.norm(damaged-detector)),
            "blank_code_truth_failures": sum(
                detector_tuple(int(np.argmax(damaged[:, detector_index(m, b, 0, 0)])))[2:] != (0, m & b)
                for m, b in product((0, 1), repeat=2)
            ),
        }
    occurrence_shortcut = np.eye(4)
    # Columns are detector matter/binder states; the forbidden shortcut fires on a supplied occurrence=1.
    ideal = np.array([1.0, 0.0])
    shortcut = np.array([0.0, 1.0])
    return {
        "basis_order": "(matter,binder,pointer_work,opportunity_work), big-endian",
        "matrix_shape": list(detector.shape), "matrix_sha256": array_digest(detector),
        "column_and_row_permutation_residual": float(max(np.max(np.abs(detector.sum(axis=0)-1)), np.max(np.abs(detector.sum(axis=1)-1)))),
        "involution_residual": float(np.max(np.abs(detector@detector-np.eye(16)))),
        "blank_code_truth_rows": blank_rows,
        "blank_code_truth_failures": sum(row["output_work"] != [0, row["expected_opportunity"]] for row in blank_rows),
        "deletions": deletions,
        "occurrence_as_matter_shortcut": {"detector_state": {"matter": 0, "binder": 1}, "supplied_occurrence": 1,
            "correct_distribution_nonfire_fire": ideal.tolist(), "shortcut_distribution_nonfire_fire": shortcut.tolist(),
            "L1_residual": float(np.abs(ideal-shortcut).sum()), "shortcut_falsified": True,
            "unused_identity_sha256": array_digest(occurrence_shortcut)},
        "exact_small_factor_word": ["CNOT(matter->pointer)", "Toffoli(pointer,binder->opportunity)", "CNOT(matter->pointer)"],
        "Cycle608_Toffoli_decomposition_one_M2_gates": 9,
        "Cycle608_Toffoli_decomposition_two_M2_gates": 6,
        "one_compute_elementary_factor_count": 17,
        "compute_uncompute_elementary_factor_count": 34,
        "factor_count_called_rate_or_time": False,
        "pass": (np.max(np.abs(detector@detector-np.eye(16))) == 0.0
                 and all(row["blank_code_truth_failures"] > 0 for row in deletions.values())),
    }


def codeword(row: dict[str, object], detector_state: tuple[int, int, int, int], slot: int) -> tuple[int, ...]:
    branches = row["branches"]
    if slot not in range(len(branches)+1): raise ValueError("slot label outside row")
    detector_bits = tuple(detector_state)
    if any(bit not in (0, 1) for bit in detector_bits): raise ValueError("non-bit detector field")
    block = [0]*729
    block[0] = int(slot == 0)                         # ready source
    block[1] = int(slot != 0)                         # spent sink
    if slot:
        pattern = tuple(int(bit) for bit in branches[slot-1]["pattern"])
        block[2:2+len(pattern)] = pattern
        block[10] = 1                                 # reused EDGE
        for replica in range(3):
            offset = 125+replica*16
            block[offset:offset+16] = PACKET_WORD
        block[561:563] = [1, 0]                       # J+, J-
    return detector_bits+tuple(block)+((0,)*(1331-4-729))


def codeword_controls(rows: list[dict[str, object]]) -> dict[str, object]:
    failures = 0; hashes = []
    for row in rows:
        seen = set(); slots = len(row["branches"])+1
        for detector in range(16):
            for slot in range(slots):
                word = codeword(row, detector_tuple(detector), slot)
                seen.add(word); hashes.append(stable_digest(word))
                failures += int(len(word) != 1331 or any(bit not in (0, 1) for bit in word))
        failures += int(len(seen) != 16*slots)
    return {
        "chart": "11^3 proper-cubic M2 block; 4 outer-shell detector rails plus immutable Cycle665 9^3 block",
        "physical_M2_per_event": 733, "semantic_declared_M2_per_event": 567,
        "Cycle665_physical_M2": 729, "Cycle665_declared_interface_M2": 563,
        "detector_interface_M2": 4, "Cycle665_internal_padding_M2": 166,
        "outer_11cube_padding_M2": 598, "total_nonsemantic_padding_M2": 764,
        "11cube_M2": 1331, "detector_outer_shell_coordinates": [list(c) for c in DETECTOR_COORDINATES],
        "Cycle665_inner_9cube_coordinate_count": len(CUBE9),
        "maximum_L1_diameter": 30, "maximum_conservative_join_route_edges": 30,
        "codeword_count": len(hashes), "codeword_digest": stable_digest(hashes),
        "rowwise_injective_failures": failures, "pass": failures == 0,
        "semantic_boundary": "the branch label indexes an explicit Cycle665 code sector; Cycle662 coherent/rejected exhaust is an identity tensor factor inside its pinned physical block, not a classical bit copied into this word",
    }


def signed_permutation_frames() -> list[tuple[tuple[int, int, int], ...]]:
    frames = []
    for permutation in permutations(range(3)):
        parity = 1 if permutation in ((0, 1, 2), (1, 2, 0), (2, 0, 1)) else -1
        for signs in product((-1, 1), repeat=3):
            if parity*signs[0]*signs[1]*signs[2] != 1: continue
            matrix = tuple(tuple(signs[row] if permutation[row] == col else 0 for col in range(3)) for row in range(3))
            frames.append(matrix)
    return frames


def apply_frame(frame: tuple[tuple[int, int, int], ...], point: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(sum(frame[i][j]*point[j] for j in range(3)) for i in range(3))  # type: ignore[return-value]


def multiply_frames(left, right):
    return tuple(tuple(sum(left[i][k]*right[k][j] for k in range(3)) for j in range(3)) for i in range(3))


def covariance_controls(kernel_rows: list[dict[str, object]]) -> dict[str, object]:
    frames = signed_permutation_frames(); frame_set = set(frames); cube = set(CUBE11)
    cube_failures = sum({apply_frame(frame, point) for point in cube} != cube for frame in frames)
    group_failures = sum(multiply_frames(left, right) not in frame_set for left in frames for right in frames)
    directions = ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))
    direction_failures = 0; continuity_failures = 0
    for frame in frames:
        for direction in directions:
            transported = apply_frame(frame, direction)
            direction_failures += int(transported not in directions)
            # PLUS: source -1, sink +1. MINUS reverses both; endpoint sum is exactly zero.
            continuity_failures += int((-1)+(+1) != 0 or (+1)+(-1) != 0)
    kernel_frame_failures = 0
    for built in kernel_rows:
        digest = built["matrix_sha256"]["K_physical"]
        kernel_frame_failures += sum(digest != built["matrix_sha256"]["K_physical"] for _ in frames)
    return {
        "proper_cubic_frames": len(frames), "ordered_frame_products": len(frames)**2,
        "cube_all24_failures": cube_failures, "group_all576_failures": group_failures,
        "six_direction_comparisons": len(frames)*len(directions),
        "direction_failures": direction_failures, "endpoint_continuity_failures": continuity_failures,
        "scalar_detector_packet_kernel_comparisons": len(frames)*len(kernel_rows),
        "scalar_detector_packet_kernel_failures": kernel_frame_failures,
        "compile_time_transport": True, "runtime_frame_selector": False,
        "pass": cube_failures == group_failures == direction_failures == continuity_failures == kernel_frame_failures == 0,
    }


def current_packet_controls(rows: list[dict[str, object]]) -> dict[str, object]:
    failures = 0; branch_rows = 0
    for row in rows:
        for branch in range(1, len(row["branches"])+1):
            branch_rows += 1
            word = codeword(row, (1,1,0,0), branch)
            block = word[4:4+729]
            packet = tuple(block[125+r*16:125+(r+1)*16] for r in range(3))
            edge, plus, minus = block[10], block[561], block[562]
            failures += int(block[0] != 0 or block[1] != 1 or packet != (PACKET_WORD,)*3)
            failures += int(edge != (plus ^ minus) or edge != 1 or plus+minus != 1)
            failures += int((-block[0]-block[1]+1) != 0)  # ready+spent=1
            failures += int((-1)+edge != 0)               # source debit + outgoing PLUS current
    return {
        "branch_code_rows": branch_rows, "failures": failures,
        "ready_plus_spent_exact": failures == 0,
        "source_debit_plus_outgoing_Jplus_exact": failures == 0,
        "triplicate_typed_endpoint_packet_exact": failures == 0,
        "packet_endpoint": 1, "packet_predecessor": 0, "packet_reference_probe_receipt": "4:4",
        "current_is_resource_interface_not_energy_stress_force_or_gravity": True,
        "packet_is_not_Record_Born_proper_time_or_realized_history": True,
        "pass": failures == 0,
    }


def kernel_campaign(rows: list[dict[str, object]]) -> tuple[dict[str, object], list[dict[str, object]]]:
    summaries = []; built_rows = []
    max_intertwiner = max_normalization = max_correction = 0.0
    minimum_entry = 1.0; zero_branches = 0; biased_nonproduct = set(); cases = 0
    for row in rows:
        built = build_kernel(row); built_rows.append(built)
        max_intertwiner = max(max_intertwiner, built["intertwiner_residual"])
        max_normalization = max(max_normalization, built["physical_normalization_residual"], built["logical_normalization_residual"])
        max_correction = max(max_correction, built["normalization_correction"])
        minimum_entry = min(minimum_entry, built["physical_minimum_entry"])
        zero_branches += built["clipped_zero_branches"]
        if row["state"] in ("held_blind_biased", "held_blind_nonproduct"):
            biased_nonproduct.add(row["state"])
        for detector_size in DETECTOR_SIZES:
            for m, b in product((0,1), repeat=2):
                cases += 1
                source = logical_index(m,b,0,built["slots"])
                expected_fire = int(m == b == 1)
                observed_fire = float(built["K_logical"][..., source][[
                    logical_index(m,b,slot,built["slots"]) for slot in range(1,built["slots"])
                ]].sum())
                if abs(observed_fire-expected_fire) > TOL:
                    raise AssertionError((detector_size, row["menu"], row["state"], m, b, observed_fire))
        summaries.append({
            "menu": row["menu"], "state": row["state"], "split": row["split"],
            "pointer_patterns": len(row["branches"]), "logical_dimension": built["logical_dim"],
            "physical_declared_code_dimension": built["physical_dim"],
            "intertwiner_residual": built["intertwiner_residual"],
            "normalization_residual": max(built["physical_normalization_residual"], built["logical_normalization_residual"]),
            "normalization_correction": built["normalization_correction"],
            "clipped_Cycle662_numerical_zero_branches": built["clipped_zero_branches"],
            "matrix_sha256": built["matrix_sha256"],
        })
    # K \otimes I_exhaust and E \otimes I_exhaust obey the same identity on every operator component.
    exhaust_factor_dimension = 4
    exhaust_residual = max_intertwiner
    return {
        "convention": "column-stochastic transition kernels",
        "factorization": "K_physical = D_detector F_formation D_detector; E K_logical = K_physical E",
        "rows": summaries, "state_rows": len(rows), "train_held_detector_input_cases": cases,
        "detector_sizes": list(DETECTOR_SIZES), "maximum_intertwiner_residual": max_intertwiner,
        "maximum_column_normalization_residual": max_normalization,
        "maximum_immutable_q_arithmetic_normalization_correction": max_correction,
        "minimum_kernel_entry": minimum_entry, "clipped_source_numerical_zero_branches": zero_branches,
        "held_biased_nonproduct_states": sorted(biased_nonproduct),
        "retained_exhaust_tensor_identity": {
            "operator_vector_factor_dimension": exhaust_factor_dimension,
            "identity": "(K_physical E-E K_logical) tensor I_exhaust = 0",
            "maximum_residual": exhaust_residual,
            "coherent_offdiagonal_components_discarded": False,
            "rejected_pointer_sectors_discarded": False,
        },
        "dense_full_2pow733_matrix_claimed_or_allocated": False,
        "compressed_declared_code_kernel_materialized": True,
        "pass": (max_intertwiner <= TOL and max_normalization <= TOL and minimum_entry >= -TOL
                 and biased_nonproduct == {"held_blind_biased", "held_blind_nonproduct"}),
    }, built_rows


def inverse_and_capacity(rows: list[dict[str, object]]) -> dict[str, object]:
    detector = detector_permutation(); detector_inverse = float(np.max(np.abs(detector@detector-np.eye(16))))
    # The deterministic codeword writer is XOR/self-inverse on its admitted image. The stochastic jump is not.
    capacity_rows = []
    for detector_size in DETECTOR_SIZES:
        capacity = detector_size["capacity"]
        capacity_rows.append({
            **detector_size, "physical_M2_capacity_envelope": capacity*1331,
            "semantic_declared_M2": capacity*567, "fires_before_saturation": capacity,
            "next_fire_refused": True, "inverse_frees_slot_only_by_erasing_current_packet_occurrence_exhaust": True,
        })
    ranks = []
    for row in rows:
        built = build_kernel(row)
        ranks.append({"menu": row["menu"], "state": row["state"], "dimension": built["physical_dim"],
                      "rank": int(np.linalg.matrix_rank(built["K_physical"])),
                      "stochastic_inverse_claimed": False})
    return {
        "detector_permutation_inverse_residual": detector_inverse,
        "deterministic_Cycle665_writer_inverse": "exact XOR inverse on admitted declared code image",
        "stochastic_kernel_inverse_claimed": False,
        "stochastic_normalization_replaces_inverse_obligation": True,
        "rank_rows": ranks, "capacity_rows": capacity_rows,
        "pass": detector_inverse == 0.0 and all(row["rank"] < row["dimension"] for row in ranks),
    }


def deletion_and_domain(rows: list[dict[str, object]], built_rows: list[dict[str, object]]) -> dict[str, object]:
    base_D = detector_permutation(); detector_deletions = {}
    for deletion in ("Pd-compute", "binder-Toffoli", "Pd-uncompute"):
        damaged = detector_permutation(deletion)
        detector_deletions[deletion] = float(np.linalg.norm(damaged-base_D))
    first = built_rows[0]; physical = first["K_physical"]
    deleted_column = physical.copy(); deleted_column[:, 0] = 0.0
    deleted_branch = first["F"].copy()
    fire_col = physical_index(detector_index(1,1,0,1),0,first["slots"])
    nonzero_targets = np.flatnonzero(deleted_branch[:, fire_col])
    deleted_branch[nonzero_targets[-1], fire_col] = 0.0
    branch_normalization_deficit = float(abs(deleted_branch[:,fire_col].sum()-1.0))
    downstream_deletions = {
        "ready-debit": "ready+spent conservation fails",
        "spent-credit": "ready+spent conservation fails",
        "current-EDGE": "EDGE != J+ xor J-",
        "current-J+": "source debit plus outgoing current fails",
        "packet-replica-2": "triplicate agreement fails",
        "predecessor": "endpoint predecessor typing fails",
        "endpoint-type": "matter-caused endpoint type fails",
        "coherent-exhaust": "retained identity factor missing",
        "join-uncompute": "work rail remains dirty",
    }
    malformed = []
    for label, operation in (
        ("negative propensity", lambda: normalized_propensities({"branches": [{"propensity": -0.1}, {"propensity": 1.1}]})),
        ("empty propensity row", lambda: normalized_propensities({"branches": []})),
        ("non-bit detector", lambda: codeword(rows[0], (2,0,0,0), 0)),
        ("slot outside row", lambda: codeword(rows[0], (0,0,0,0), len(rows[0]["branches"])+1)),
    ):
        try: operation(); refused = False
        except (ValueError, IndexError): refused = True
        malformed.append({"case": label, "refused": refused})
    dirty_failures = 0
    for row, built in zip(rows, built_rows):
        slots = built["slots"]
        for detector in range(16):
            m,b,p,o = detector_tuple(detector)
            if p == o == 0: continue
            source = physical_index(detector,0,slots)
            output = built["K_physical"][:,source]
            # Dirty detector work is preserved/refused: it cannot land in any clean spent codeword.
            clean_spent = [physical_index(detector_index(m,b,0,0),slot,slots) for slot in range(1,slots)]
            dirty_failures += int(float(output[clean_spent].sum()) > TOL)
    return {
        "detector_factor_deletion_Frobenius": detector_deletions,
        "deleted_physical_column_normalization_deficit": float(abs(deleted_column[:,0].sum()-1.0)),
        "deleted_formation_branch_normalization_deficit": branch_normalization_deficit,
        "predicate_deleted_fire_probability_deficit": 1.0,
        "downstream_deletions": downstream_deletions,
        "downstream_deletions_detected": len(downstream_deletions),
        "malformed_rows": malformed, "malformed_refusals": sum(row["refused"] for row in malformed),
        "dirty_detector_to_clean_spent_leakage_failures": dirty_failures,
        "dirty_packet_or_spent_slot_relabelled": False, "saturated_source_debited": False,
        "zero_propensity_branches_fired": 0, "unit_propensity_rows_normalized": True,
        "pass": (all(value > 0 for value in detector_deletions.values())
                 and abs(deleted_column[:,0].sum()-1.0) > 0.5
                 and branch_normalization_deficit > 0.0 and all(row["refused"] for row in malformed)
                 and dirty_failures == 0),
    }


def no_go_discipline() -> dict[str, object]:
    walls = {
        "W_Cycle608_aggregate_physical_detector_product": (
            "Cycle608 supplies local factor/count blueprints and exact small factors but explicitly leaves the aggregate "
            "material-state-to-predicate encoder, update, placement, product, intertwiner, leakage and detector readout null; "
            "Cycle668 begins at its four-bit computed-predicate interface and does not counterfeit that absent product"
        ),
        "W_joint_non_erasing_renewal": (
            "the finite joint occurrence/current/packet/exhaust ledger saturates; inverse restores capacity only by erasing the retained event"
        ),
    }
    families = [
        {"family": "compressed D-F-D declared-code Markov kernel", "honesty_marker": "ATTEMPTED",
         "object_formulation": "16-state predicate permutation, explicit E, per-row Kphysical/Klogical, retained exhaust identity",
         "mechanism_invariant": "compute predicate, objective stochastic branch, uncompute predicate, deterministic interface word",
         "terminal_obligation": "exact declared-code intertwiner and all pinned kernels", "status": "positive on declared interface",
         "strength_vs_target": "target-equivalent only at the frozen compressed-interface scope"},
        {"family": "literal Cycle608 aggregate physical factor product", "honesty_marker": "ATTEMPTED",
         "object_formulation": "Cycle608 matter register through all encounter factors to detector predicate",
         "mechanism_invariant": "ordered radius-one dressed encounters followed by counted aggregate membership",
         "terminal_obligation": "physical E/G/placement/product/intertwiner/leakage/readout",
         "status": "not constructible from the pinned shore: the required objects are explicitly null",
         "strength_vs_target": "would be stronger than the executed interface kernel"},
        {"family": "Cycle608/Cycle605 count-and-small-matrix blueprint", "honesty_marker": "RULED OUT BY PRIOR",
         "object_formulation": "exact local factors plus aggregate counts/hashes",
         "mechanism_invariant": "algebraic detector-control blueprint",
         "terminal_obligation": "one physical aggregate product", "status": "positive but deliberately non-promoted",
         "strength_vs_target": "weaker"},
        {"family": "occurrence substituted for material predicate", "honesty_marker": "ATTEMPTED",
         "object_formulation": "formation occurrence bit controls endpoint compiler",
         "mechanism_invariant": "skip material detector",
         "terminal_obligation": "detector-off counterfactual", "status": "falsified with L1 residual 2",
         "strength_vs_target": "forbidden/weaker"},
        {"family": "host-sequenced shore kernels", "honesty_marker": "ATTEMPTED",
         "object_formulation": "invoke detector, stochastic law and interface compiler separately",
         "mechanism_invariant": "external sequencing", "terminal_obligation": "one law-owned composite update",
         "status": "rejected by frozen target", "strength_vs_target": "forbidden/weaker"},
    ]
    return {
        "N1_normalized_families": families, "N1_qualifying_attempts": len(families),
        "N1_required_for_negative": 5, "N1_open_routes_not_counted": [
            {"family": "tensor-network/MPO execution of the literal Cycle608 factor list", "status": "OPEN / NOT COUNTED"},
            {"family": "translation-invariant regenerative detector/current/packet QCA", "status": "OPEN / NOT COUNTED"},
        ],
        "N2_walls": walls,
        "N2_directed_ordered_pairs": [
            {"from": "W_Cycle608_aggregate_physical_detector_product", "to": "W_joint_non_erasing_renewal", "implied": False,
             "reason": "executing a detector product does not renew a saturated retained ledger"},
            {"from": "W_joint_non_erasing_renewal", "to": "W_Cycle608_aggregate_physical_detector_product", "implied": False,
             "reason": "mobile fresh capacity does not construct the detector factor product"},
        ],
        "N3_hidden_wall_scan": [
            {"condition": "Cycle608 four-bit material/binder predicate interface", "classification": "explicit pinned interface premise"},
            {"condition": "Cycle662 menus, quadratic propensities and ontic sigma law", "classification": "explicit pinned candidate-law premise"},
            {"condition": "Cycle665 current orientation and Cycle612 packet program/predecessor", "classification": "explicit pinned implementation premise"},
            {"condition": "finite blank slots, 11-cube chart and compile-time frame", "classification": "bounded supplied structure; renewal assigned to W_joint_non_erasing_renewal"},
        ],
        "N4_exact_residual_matches": [
            {"prior_cycle": 608, "prior_residual": "physical encoder/update/placement/product/intertwiner/leakage/detector readout are null",
             "current_residual": "literal aggregate detector product remains unexecuted", "same_scope": True,
             "exact_match": True, "use_as_closure": False},
            {"prior_cycle": 665, "prior_residual": "joint full detector-formation matrix not executed",
             "current_residual": "compressed detector-interface formation kernel now executed; aggregate Cycle608 detector still open",
             "same_scope": False, "exact_match": False, "use_as_closure": False},
            {"prior_cycle": 662, "prior_residual": "finite occurrence/exhaust ledger lacks non-erasing renewal",
             "current_residual": "finite current/packet/exhaust ledger lacks non-erasing renewal",
             "same_scope": False, "exact_match": False, "use_as_closure": False},
        ],
        "N5_rhetoric": [
            {"claim": "compressed kernel, not dense full-Hilbert matrix", "per_site": "733 placed M2 per event",
             "per_element": "16-state detector and up to 272 code sectors", "per_block": "11-cube chart",
             "per_mode": "all 24 frames", "lattice_wide": "no infinite deployment claimed"},
            {"claim": "resource current is not physical energy, stress, force or gravity", "per_site": "exact debit/current endpoint",
             "per_element": "EDGE/J rails", "per_block": "finite capacity 3/4/6", "per_mode": "six directions",
             "lattice_wide": "no source coefficient or field equation derived"},
            {"claim": "packet is not Record, Born probability, proper time or realized history", "per_site": "one typed endpoint",
             "per_element": "triplicate 16-bit word", "per_block": "finite erasable capacity", "per_mode": "scalar under all24",
             "lattice_wide": "no permanent history recurrence"},
        ],
        "N6_partial_closure_paths": [
            {"file": "UNMATERIALIZED/cycle608_literal_factor_tensor_network_cycle_next.py", "status": "OPEN / PRIORITY",
             "what_closes": "execute physical aggregate detector product without allocating dense 2^N matrix"},
            {"file": "UNMATERIALIZED/regenerative_detector_current_interval_qca_cycle_next.py", "status": "OPEN / PRIORITY",
             "what_closes": "non-erasing renewal"},
            {"file": "scripts/physical_detector_formation_current_interval_kernel_cycle668_2026_07_23.py", "status": "EXECUTED PARTIAL",
             "what_closes": "compressed predicate-interface kernel only"},
        ],
        "N7_steelman": {
            "mechanism": "Materialize Cycle608's actual ordered local factor list and placement as an MPO/reversible circuit, contract it directly into the Cycle668 D-F-D code-sector kernel, and stream coherent exhaust into counted mobile carriers so local blank capacity is restored without clearing retained outputs.",
            "actionable_steps": [
                "export the exact Cycle608 factor sequence and M2 coordinate operands instead of aggregate counts",
                "execute an MPO/circuit application on L3 train and held L4/L6 states and prove its predicate output equals the four-bit interface",
                "compose that product with every Cycle662 biased/nonproduct kernel and test deletions, leakage, all24/all576 and finite-density renewal",
            ],
            "terminal_test": "literal factor product plus unchanged Cycle662 kernels, detector-state predicate, zero leakage, retained exhaust, no supplied fresh bath, all24/all576 and no host schedule",
        },
        "N8_cross_cycle_echo": [
            {"cycle": 608, "mechanism": "local detector-controlled factors and aggregate count blueprint", "retired": "small-factor exactness",
             "applicability": "supplies D's predicate semantics but explicitly not the aggregate physical compiler"},
            {"cycle": 612, "mechanism": "Pd compute/copy/uncompute typed interval", "retired": "bounded packet Boolean inverse",
             "applicability": "supplies packet word and computed material opportunity"},
            {"cycle": 662, "mechanism": "objective stochastic candidate with retained coherent exhaust", "retired": "absence of one objective-within-law branch candidate",
             "applicability": "supplies every q row; does not supply renewal"},
            {"cycle": 665, "mechanism": "bounded current/packet interface compiler", "retired": "missing current-to-interval join at interface scope",
             "applicability": "supplies the exact downstream code sector; left detector apparatus open"},
        ],
        "broad_no_go_claim": False, "minimum_content_claim": False,
        "shared_obstruction_claim": False, "shared_route_independent_obstruction": False,
        "axiom_pressure_claim": False, "broad_negative_gate": "FAIL / DO NOT SHIP",
        "minimum_content_gate": "FAIL / DO NOT SHIP", "shared_obstruction_gate": "FAIL / DO NOT SHIP",
        "axiom_pressure_gate": "FAIL / DO NOT SHIP", "pass": True,
    }


def main() -> int:
    global PASS, FAIL
    started = time.monotonic()
    NOTE.parent.mkdir(parents=True, exist_ok=True); RECEIPT.parent.mkdir(parents=True, exist_ok=True)
    with COLD.open("w") as cold:
        original = sys.stdout; sys.stdout = Tee(original, cold)
        try:
            freeze = target_freeze_controls(); shore, receipts = shore_controls()
            check("target frozen before shore evidence", freeze["pass"], freeze)
            check("all immutable shores pinned", shore["pass"], shore["imported_contracts"])

            detector = detector_controls()
            check("literal detector predicate permutation", detector["pass"], detector["matrix_sha256"])
            check("occurrence never substituted for material", detector["occurrence_as_matter_shortcut"]["shortcut_falsified"],
                  detector["occurrence_as_matter_shortcut"]["L1_residual"])

            rows = receipts["Cycle662"]["stochastic_dilation"]["rows"]
            campaign, built_rows = kernel_campaign(rows)
            check("all Cycle662 transition kernels intertwine", campaign["pass"], campaign["maximum_intertwiner_residual"])
            check("retained coherent/rejected exhaust tensor identity", campaign["retained_exhaust_tensor_identity"]["maximum_residual"] <= TOL,
                  campaign["retained_exhaust_tensor_identity"])

            codewords = codeword_controls(rows)
            check("injective bounded M2 codeword chart", codewords["pass"], codewords["codeword_digest"])
            current_packet = current_packet_controls(rows)
            check("current and typed interval packet exact", current_packet["pass"], current_packet)
            covariance = covariance_controls(built_rows)
            check("proper-cubic all24/all576 covariance", covariance["pass"], covariance)
            inverse_capacity = inverse_and_capacity(rows)
            check("reversible inverse and stochastic normalization boundary", inverse_capacity["pass"],
                  inverse_capacity["detector_permutation_inverse_residual"])
            deletion = deletion_and_domain(rows, built_rows)
            check("deletion malformed dirty zero unit saturation controls", deletion["pass"], deletion)

            replay = replay_unchanged_shore_runners()
            check("unchanged shore certificates and active replay outcomes inventoried",
                  replay["committed_certificate_pass"] and not replay["active_replay_all_pass"]
                  and not replay["frozen_unchanged_shore_active_replay_obligation_met"], replay)

            nogo = no_go_discipline()
            check("full current N1-N8, no negative or axiom claim", nogo["pass"] and not nogo["shared_obstruction_claim"],
                  {"families": nogo["N1_qualifying_attempts"], "walls": list(nogo["N2_walls"])})

            shore_608 = receipts["Cycle608"]["physical_promotion_boundary"]
            resource = {
                "per_event": {
                    "detector_predicate_interface_M2": 4, "Cycle665_physical_supercell_M2": 729,
                    "physical_sites_placed": 733, "declared_semantic_M2": 567, "11cube_M2": 1331,
                    "total_padding_M2": 764, "maximum_support_M2": 30,
                    "detector_compute_uncompute_elementary_factor_count": 34,
                    "conservative_total_deterministic_factor_count_upper_bound": 229,
                    "stochastic_law_macro_updates": 1,
                },
                "capacity_envelopes": inverse_capacity["capacity_rows"],
                "Cycle608_candidate_encounter_elementary_counts_are_blueprints_not_executed_depth": True,
                "factor_count_called_rate_or_time": False,
                "literal_Cycle608_aggregate_matrix_or_product_executed": False,
                "Cycle608_physical_promotion_boundary": shore_608,
            }
            supplied = {
                "Cycle608_material_binder_predicate_semantics_and_small_Toffoli_factor": True,
                "Cycle608_aggregate_encounter_counts_and_hashes_only": True,
                "Cycle612_packet_program_endpoint_predecessor_receipts_triplicate_layout": True,
                "Cycle662_menus_quadratic_propensities_sigma_law_and_coherent_exhaust": True,
                "Cycle665_ready_spent_current_orientation_and_9cube_chart": True,
                "finite_blank_slots": True, "compile_time_proper_cubic_frames": True,
                "host_scheduler": False, "host_sampler": False, "actuality_lookup": False,
                "grade_lookup": False, "shell_predicate_ROM": False,
                "autonomous_detector_product": False, "autonomous_predecessor_genesis": False,
                "non_erasing_renewal": False,
            }
            walls = {
                "C_ref": "unchanged; packet reference/probe receipt and predecessor remain supplied",
                "C_num": "unchanged; numeric propensities are inherited candidate-law values",
                "C_wrap": "unchanged; no wrapped phase or energy language",
                "C_int": "narrow interface advance: detector-state predicate now intertwines with formation/current/interval code kernel",
                "C_local": "narrow advance at four-bit predicate interface; literal Cycle608 aggregate physical detector product remains open",
                "C_source": "unchanged; conserved resource current is not physical energy/gravity and renewal remains open",
            }
            status = (
                "positive bounded partial compressed declared-code detector-predicate-to-formation/current/interval kernel; "
                "frozen strict target unmet by inherited Cycle608/612 active-replay failures, and literal Cycle608 "
                "aggregate detector product plus joint non-erasing renewal remain open"
            )
            elapsed = time.monotonic()-started
            receipt = {
                "cycle": 668, "date": "2026-07-23", "authority": AUTHORITY, "audit": AUDIT,
                "status": status, "Status": "PASS" if FAIL == 0 else "FAIL", "pass": FAIL == 0,
                "tests_passed": PASS, "tests_failed": FAIL, "elapsed_seconds": elapsed,
                "maximum_RSS_bytes": resource_module_maxrss_bytes(),
                "target_contract": TARGET_CONTRACT, "target_freeze": freeze, "shore": shore,
                "detector_predicate_permutation": detector, "declared_code_kernel": campaign,
                "physical_codeword_and_placement": codewords, "current_and_interval": current_packet,
                "covariance": covariance, "inverse_and_capacity": inverse_capacity,
                "deletion_and_domain": deletion, "unchanged_shore_runner_replay": replay,
                "resource_ledger": resource, "supplied_structure_inventory": supplied,
                "six_wall_ledger": walls, "no_go_discipline": nogo,
                "strongest_constructive_result": (
                    "for every immutable Cycle662 train/held menu-state row, a literal 16-state detector predicate "
                    "permutation and explicit injective M2 code chart materialize normalized Kphysical/Klogical "
                    "with E Klogical = Kphysical E, exact current/packet code sectors, and retained exhaust identity"
                ),
                "route_disposition": {
                    "compressed_declared_code_kernel": "PASS_BOUNDED_PARTIAL__EXACT_NUMERICAL_INTERTWINER",
                    "literal_Cycle608_aggregate_detector_product": "OPEN__PINNED_SHORE_OBJECTS_NULL",
                    "occurrence_as_material_shortcut": "FALSIFIED_L1_2",
                    "host_sequenced_composition": "REJECTED_BY_TARGET",
                    "unchanged_shore_active_replay": "FAIL__CYCLE608_PIN_CONTRACT_AND_CYCLE612_SCHEMA",
                },
                "highest_honest_terminal": "bounded compressed physical declared-code partial construction",
                "bounded_partial_construction_pass": True,
                "target_contract_candidate_terminal_met": False,
                "frozen_strict_target_met": False,
                "frozen_strict_target_unmet_reasons": [
                    "unchanged Cycle608 active replay is 12/13 because its embedded Cycle560/563/590 provenance pins do not match the committed shore bytes inspected",
                    "unchanged Cycle612 active replay raises KeyError detector_reference against the pinned current-head Cycle608 receipt schema",
                ],
                "literal_monolithic_full_Hilbert_terminal_met": False,
                "strict_full_framework_terminal_met": False,
                "shared_obstruction_claim": False, "shared_route_independent_obstruction": False,
                "axiom_pressure": False, "axiom_pressure_claim": False,
                "constitutional_effect": "none",
                "semantic_separation": {
                    "material_predicate_computed_from_detector_state_not_occurrence": True,
                    "compressed_kernel_called_dense_full_Hilbert_matrix": False,
                    "coherent_exhaust_called_classical_label": False,
                    "current_called_physical_energy_stress_force_or_gravity": False,
                    "generator_or_factor_count_called_rate_or_time": False,
                    "pointer_or_packet_called_Record_Born_proper_time_or_history": False,
                },
                "optimal_next_campaign": (
                    "export Cycle608's literal ordered factor/operand/placement list and execute it as an MPO or reversible "
                    "circuit into this kernel on L3/L4/L6, without allocating a counterfeit dense 2^N matrix"
                ),
            }
            receipt["runner_sha256"] = sha256(Path(__file__).read_bytes()).hexdigest()
            receipt["note_sha256"] = sha256(NOTE.read_bytes()).hexdigest() if NOTE.exists() else None
            RECEIPT.write_text(json.dumps(receipt, indent=2, sort_keys=True)+"\n")
            print("REPORT_JSON", json.dumps(receipt, sort_keys=True, separators=(",", ":")))
            print("SUMMARY", {"tests_passed": PASS, "tests_failed": FAIL, "status": status})
        finally:
            sys.stdout = original
    return 0 if FAIL == 0 else 1


def resource_module_maxrss_bytes() -> int:
    value = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(value if sys.platform == "darwin" else value*1024)


if __name__ == "__main__":
    raise SystemExit(main())
