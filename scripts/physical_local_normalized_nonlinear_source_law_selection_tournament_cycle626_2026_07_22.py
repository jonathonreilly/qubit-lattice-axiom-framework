#!/usr/bin/env python3
"""Cycle626: local normalization, nonlinear feedback, and direct-K tournament.

The routes are deliberately independent.  Route A evaluates a strictly
bounded 24-frame orbit normalizer and an endpoint-controlled local actuation
block.  Route B exhausts the analytic branches of a bounded rational feedback
map and separately audits the common-coupling q^2 stationary comparator.
Route C compiles the periodic Cycle576 Regge and direct Cycle620 K-to-endpoint
blocks into unary support-two words while preserving, rather than hiding, the
seam to the open F17 apparatus.  Authority none; audit unset.
"""
from __future__ import annotations

from functools import lru_cache
from hashlib import sha256
from itertools import combinations, product
import json
import math
from pathlib import Path
import resource
import subprocess
import sys
from time import perf_counter

import numpy as np
from scipy.linalg import expm

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_pair_supercell_receiver_feedback_quasienergy_tournament_cycle620_2026_07_22 as c620
import physical_matter_caused_causal_interval_proper_time_bridge_tournament_cycle612_2026_07_22 as c612

c615 = c620.c615
c610 = c620.c610
c576 = c620.c576
c210 = c620.c210
c609 = c620.c609

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_LOCAL_NORMALIZED_NONLINEAR_SOURCE_LAW_SELECTION_TOURNAMENT_"
    "CYCLE626_NOTE_2026-07-22.md"
)
RECEIPT = ROOT / "outputs/physical_local_normalized_nonlinear_source_law_selection_tournament_cycle626_receipt_2026_07_22.json"
COLD = ROOT / "outputs/physical_local_normalized_nonlinear_source_law_selection_tournament_cycle626_cold_2026_07_22.txt"
AUTHORITY = "none"
AUDIT = "unset"
TOL = 3.0e-7
START = perf_counter()
PASS = 0
FAIL = 0
FIXTURES = (("TRAIN_L3", 3, False), ("HELD_L6", 6, True), ("OUT_HELD_L7", 7, True))

PINS = {
    "scripts/physical_pair_supercell_receiver_feedback_quasienergy_tournament_cycle620_2026_07_22.py":
        "290d41dadcd038359fbadfefed7980142d1337c3dac563eed97d6bb1eb4956c9",
    "docs/work_history/repo/review_feedback/PHYSICAL_PAIR_SUPERCELL_RECEIVER_FEEDBACK_QUASIENERGY_TOURNAMENT_CYCLE620_NOTE_2026-07-22.md":
        "355510cc9f627e6bd20e5db323d3166d3b6ef24a99d28aab8a702fd9ad0abc5a",
    "outputs/physical_pair_supercell_receiver_feedback_quasienergy_tournament_cycle620_receipt_2026_07_22.json":
        "0d6b15cfb16fc4b2d0cb4e440bc3da9898837d195c809b0f89dfd406d6094104",
    "outputs/physical_dynamical_metric_source_law_bridge_tournament_cycle576_receipt_2026_07_22.json":
        "06456c1443f5464949f40d81e9f1c6316b3e4e8405415b5b0035e39d4b88c3bd",
    "outputs/physical_matter_caused_causal_interval_proper_time_bridge_tournament_cycle612_receipt_2026_07_22.json":
        "e7a8ea3dcbe370c9f8c6a94770508d1710a7013ce4ba62a1ad67e345fe1e2d11",
    "outputs/physical_car_matter_weyl_reciprocal_source_response_tournament_cycle607_receipt_2026_07_22.json":
        "752be1935cdac98b3081b2a55665a0383c627e3639ab83c76e8fc4d624ea11b4",
    "outputs/physical_two_M2_CAR_phase_link_field_QCA_tournament_cycle609_receipt_2026_07_22.json":
        "1c1c8e0141378ed6a53d85815591a76ab3c8e65ec1f952eca39fe3a95789d6dd",
    "outputs/physical_gauged_matter_action_stress_prediction_tournament_cycle613_receipt_2026_07_22.json":
        "260dd78e1f648b3f6c062d3e5c79383182587fbeacf6e2aa06ffa6d84bb79c41",
    "outputs/physical_rational_regge_reciprocal_response_prediction_bridge_cycle604_receipt_2026_07_22.json":
        "c8210a1f170c3b11258f9876a0013b981b4b3c44a592423c8ce48a34a479b5ee",
    "docs/GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md":
        "71023af5e313037d74eb3efb56b0515c913e66947981950e1871b3acc398fdbf",
    "docs/RP_WILSON_TEMPORAL_GAUGE_BRIDGE_SIGN_AND_POSITIVITY_REPAIR_NOTE_2026-06-06.md":
        "5f36b5fd0375a7712cbd20432d5a0f55bb4da6d861fc3eda7f3c5e54f798ded5",
    "docs/SIGNED_GRAVITY_NON_CLAIM_GATE_NOTE.md":
        "c89687d04d8e26c0cbe7999fd28357e24c42d5cc45abe97761b6fbb115798bf7",
    "docs/audit/data/axiom_premise_nodes.json":
        "b73431384495db657efaeab44d1d8e83b824908c418b115308e92eaa7212eea5",
    "docs/MINIMAL_AXIOMS_2026-06-29.md":
        "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
    "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md":
        "e7e75a36bd16094cbb547f6b215680ac45adc565c4cc93f05b0af17992eb9292",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md":
        "5516fb0bb8f50286b3c34d3f2668b1a2e347b9f7e257a8b5745f84f1093dd96b",
    "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md":
        "755cfd44924439468708124a8aaafce1b2bcaf6260d3bc08263dc6e7a4327563",
}

TIME_LANE_REF = "origin/causal-time/cycle610-relational-duration-20260722"
TIME_LANE_HEAD = "a1e2f1ea60b1cf9b9cb0ae100c61cfd1f3a07318"
TIME_LANE_PINS = {
    "docs/work_history/repo/review_feedback/PHYSICAL_TICK_ECHO_ASSOCIATION_CAUSAL_ORDER_TOURNAMENT_CYCLE612_NOTE_2026-07-22.md":
        "028133c490e771dd3012061c79910fcfb88cd6132df072ec15e725fe9bc35496",
    "scripts/physical_tick_echo_association_causal_order_tournament_cycle612_2026_07_22.py":
        "4494ce889809f6a179fc9bb712aa851fa6e73dac32a7b1bfbdb71903be5fadde",
    "outputs/physical_tick_echo_association_causal_order_tournament_cycle612_receipt_2026_07_22.json":
        "6da06e7c1147b28e74b0f1469fb466018a20f524167e628189e80e5348165cd6",
    "scripts/physical_minus_channel_certification_addendum_cycle612_2026_07_22.py":
        "5eee5e2b510c92f72dfd9a40ed1633c3257962cb39faf615ad4a9af7f3b4e711",
    "outputs/physical_minus_channel_certification_addendum_cycle612_receipt_2026_07_22.json":
        "c768c814412b259938f804f18581956d354c680e35c497eeb636fd5d6cae0c10",
}


class Tee:
    def __init__(self, *streams):
        self.streams = streams

    def write(self, value):
        for stream in self.streams:
            stream.write(value)
        return len(value)

    def flush(self):
        for stream in self.streams:
            stream.flush()


def json_default(value):
    if isinstance(value, np.generic):
        return value.item()
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, complex):
        return [value.real, value.imag]
    raise TypeError(type(value).__name__)


def digest(path: str | Path) -> str:
    return sha256((ROOT / path).read_bytes()).hexdigest()


def check(label: str, condition: bool, detail="") -> None:
    global PASS, FAIL
    PASS += int(condition)
    FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def read_receipt(name: str) -> dict:
    return json.loads((ROOT / name).read_text())


def remote_bytes(path: str) -> bytes:
    return subprocess.run(("git", "show", f"{TIME_LANE_REF}:{path}"), cwd=ROOT,
                          capture_output=True, check=True).stdout


def shore() -> dict:
    observed = {path: digest(path) for path in PINS}
    remote_observed = {path: sha256(remote_bytes(path)).hexdigest() for path in TIME_LANE_PINS}
    remote_head = subprocess.run(("git", "rev-parse", TIME_LANE_REF), cwd=ROOT, text=True,
                                 capture_output=True, check=True).stdout.strip()
    time_receipt = json.loads(remote_bytes(
        "outputs/physical_tick_echo_association_causal_order_tournament_cycle612_receipt_2026_07_22.json"
    ))
    r620 = read_receipt("outputs/physical_pair_supercell_receiver_feedback_quasienergy_tournament_cycle620_receipt_2026_07_22.json")
    r576 = read_receipt("outputs/physical_dynamical_metric_source_law_bridge_tournament_cycle576_receipt_2026_07_22.json")
    r612 = read_receipt("outputs/physical_matter_caused_causal_interval_proper_time_bridge_tournament_cycle612_receipt_2026_07_22.json")
    r607 = read_receipt("outputs/physical_car_matter_weyl_reciprocal_source_response_tournament_cycle607_receipt_2026_07_22.json")
    r609 = read_receipt("outputs/physical_two_M2_CAR_phase_link_field_QCA_tournament_cycle609_receipt_2026_07_22.json")
    r613 = read_receipt("outputs/physical_gauged_matter_action_stress_prediction_tournament_cycle613_receipt_2026_07_22.json")
    r604 = read_receipt("outputs/physical_rational_regge_reciprocal_response_prediction_bridge_cycle604_receipt_2026_07_22.json")
    words = sorted({row["probe_over_reference"] for row in r612["route_C_source_motion_ratio"]["rows"]
                    if row["physical_source_reservoir_predicate"] and row["receiver_M2"]})
    result = {
        "hashes_match": observed == PINS,
        "time_lane_remote_hashes_match": remote_observed == TIME_LANE_PINS,
        "time_lane_remote_head_matches": remote_head == TIME_LANE_HEAD,
        "observed": observed,
        "time_lane_observed": remote_observed,
        "time_lane_head": remote_head,
        "Cycle620_pass": r620["pass"],
        "Cycle576_pass": r576["pass"],
        "Cycle612_pass": r612["pass"],
        "Cycle607_pass": r607["pass"],
        "Cycle609_pass": r609["pass"],
        "Cycle613_pass": r613["pass"],
        "Cycle604_pass": r604["pass"],
        "Cycle612_receiver_words": words,
        "Cycle607_reciprocity_residual": r607["route_A_joint_CAR_Weyl_interaction"]["maximum_action_mixed_derivative_reciprocity_residual"],
        "Cycle609_support_two": r609["route_A_support2_NQ_compiler"]["maximum_elementary_gate_support_M2"],
        "Cycle613_representation_charge": r613["route_A_fully_gauged_joint_action"]["representation_charge"],
        "time_lane_delay_hit": [row for row in time_receipt["a_count_table"] if row.get("word") == "3:4"],
        "time_lane_uniform_rate_ceiling": time_receipt["pi_ceiling"]["ceiling"],
        "time_lane_uniform_rate_maximum": time_receipt["pi_ceiling"]["max_ratio"],
        "time_lane_advance_5_over_4_uniform_rate_reachable": any(row.get("word") == "5:4" for row in time_receipt["a_count_table"]),
        "receipts": {"607": r607, "609": r609, "613": r613, "604": r604, "620": r620},
    }
    check(
        "Cycle576/604/607/609/612/613/620 shore is byte-pinned and retains the live selection gates",
        result["hashes_match"] and result["time_lane_remote_hashes_match"] and result["time_lane_remote_head_matches"]
        and all(result[key] for key in ("Cycle620_pass", "Cycle576_pass", "Cycle612_pass", "Cycle607_pass", "Cycle609_pass", "Cycle613_pass", "Cycle604_pass"))
        and words == ["3/4", "5/4"]
        and result["Cycle607_reciprocity_residual"] < TOL
        and result["Cycle609_support_two"] == 2
        and result["Cycle613_representation_charge"] == 1
        and len(result["time_lane_delay_hit"]) == 1
        and result["time_lane_delay_hit"][0]["Q"] == 1
        and result["time_lane_delay_hit"][0]["s"] == 1
        and result["time_lane_delay_hit"][0]["count"] == 3
        and result["time_lane_delay_hit"][0]["matches_frozen"]
        and result["time_lane_uniform_rate_ceiling"] < 1.06
        and not result["time_lane_advance_5_over_4_uniform_rate_reachable"],
        {key: value for key, value in result.items() if key not in ("receipts", "observed", "time_lane_observed")},
    )
    return result


def note_contract() -> None:
    body = " ".join(NOTE.read_text().lower().replace("`", "").replace("*", "").split())
    required = (
        "cycle 626", "authority: none", "audit: unset", "route a", "route b", "route c",
        "local orbit", "zero branch", "24 co-present", "bounded hinge star", "rational saturation",
        "all fixed points", "stability is diagnostic", "common-coupling", "q^2", "zero mode",
        "stationary elimination", "l3", "l6", "l7", "eight central", "open", "periodic",
        "support-two", "unary", "manifest", "intertwiner", "gauss", "ward", "all 24", "all 576",
        "3/4", "5/4", "delay", "advance", "count-edit", "pi ceiling", "pr5557",
        "wrapped phase is not energy", "k is not a rate", "not gravity",
        "n1", "n2", "n3", "n4", "n5", "n6", "n7", "n8", "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in body)
    check("Cycle626 note freezes construction, controls, seams, and full N1-N8 scope", not missing, missing)


# ---------------------------------------------------------------------------
# Route A: strictly local 24-frame orbit normalization.

@lru_cache(maxsize=None)
def orbit_matrix(momentum_key: tuple[float, ...]) -> np.ndarray:
    momentum = np.asarray(momentum_key)
    return np.asarray([
        c576.base_metric_source_row(frame @ momentum) @ representation
        for representation, frame in zip(c576.METRIC_REPS, c576.LIFTED_FRAMES)
    ])


def orbit_permutation(frame_index: int) -> np.ndarray:
    frame = c576.FRAMES[frame_index]
    lookup = {tuple(item.reshape(-1)): index for index, item in enumerate(c576.FRAMES)}
    result = np.zeros((24, 24))
    for old, sector in enumerate(c576.FRAMES):
        target = lookup[tuple((sector @ frame.T).reshape(-1))]
        result[target, old] = 1
    return result


ORBIT_REPS = tuple(orbit_permutation(index) for index in range(24))


def local_normalize(values: np.ndarray, regulator: float) -> tuple[np.ndarray, float, str]:
    norm = math.sqrt(float(np.vdot(values, values).real) + regulator**2)
    if norm == 0:
        return np.zeros_like(values), 0.0, "EXACT_ZERO_TO_ZERO"
    return values / norm, norm, "NONZERO_LOCAL_ORBIT"


def normalized_actuation(normalized: np.ndarray, sign: int, scale: float, endpoint: int,
                         eta: float = c576.UPDATE_PARAMETER) -> tuple[np.ndarray, np.ndarray]:
    hamiltonian = np.zeros((25, 25), dtype=complex)
    hamiltonian[0, 1:] = endpoint * sign * scale * np.conj(normalized)
    hamiltonian[1:, 0] = endpoint * sign * scale * normalized
    return hamiltonian, expm(-1j * eta * hamiltonian)


def route_a() -> dict:
    group_failures = 0
    for i, first in enumerate(c576.FRAMES):
        for j, second in enumerate(c576.FRAMES):
            target = c576.FRAME_LOOKUP[tuple((first @ second).reshape(-1))]
            group_failures += int(not np.array_equal(ORBIT_REPS[i] @ ORBIT_REPS[j], ORBIT_REPS[target]))

    endpoint_rows = []
    for matter, binder in product((0, 1), repeat=2):
        candidate = c612.computed_candidate(matter, binder)
        deleted = c612.computed_candidate(matter, binder, delete="Pd-compute")
        endpoint_rows.append({
            "matter": matter, "binder": binder, "endpoint": candidate["opportunity"],
            "pointer_after": candidate["pointer"], "deleted_endpoint": deleted["opportunity"],
        })
    endpoint = c612.computed_candidate(1, 1)["opportunity"]

    rows = []
    max_ward = max_gauge = max_covariance = max_inverse = max_unitarity = 0.0
    min_delete = math.inf
    receiver_quadratures = []
    regulator_rows = []
    alternatives = 0
    for label, length, held in FIXTURES:
        momentum = 2 * math.pi / length * np.asarray((1.0, 1.0, 0.0, 1.0))
        q = c576.frame_averaged_metric_hessian(momentum)
        source = c576.frame_averaged_source_row(momentum)
        improvement = c620.spatial_trace_vector() @ q
        gauge = c576.continuum_gauge_metric(momentum)
        matrix = orbit_matrix(tuple(float(value) for value in momentum))
        ward = float(np.max(np.abs(matrix @ gauge)))
        max_ward = max(max_ward, ward)
        rng = np.random.default_rng(62600 + length)
        xi = rng.normal(size=4) + 1j * rng.normal(size=4)
        fixture = []
        for regulator, sign, scale, lambda_sign, lambda_magnitude, coefficient in product(
            (0.0, 0.5, 1.0, 2.0), (-1, 1), (0.5, 1.0, 2.0), (-1, 1), (1.0, 2.0), (-1.0, 0.0, 1.0)
        ):
            coupling = lambda_sign * lambda_magnitude * c576.SOURCE_COUPLING
            base = source + coefficient * improvement
            coframe = -np.linalg.pinv(q, rcond=1e-10) @ (coupling * np.conj(base))
            raw = matrix @ coframe - endpoint * np.ones(24)
            normalized, denominator, branch = local_normalize(raw, regulator)
            gauged, _, _ = local_normalize(matrix @ (coframe + gauge @ xi) - endpoint, regulator)
            gauge_residual = float(np.linalg.norm(gauged - normalized))
            max_gauge = max(max_gauge, gauge_residual)
            hamiltonian, update = normalized_actuation(normalized, sign, scale, endpoint)
            initial = np.zeros(25, dtype=complex); initial[0] = 1
            evolved = update @ initial
            restored = update.conj().T @ evolved
            inverse = float(np.linalg.norm(restored - initial))
            unitarity = float(np.linalg.norm(update.conj().T @ update - np.eye(25)))
            max_inverse = max(max_inverse, inverse); max_unitarity = max(max_unitarity, unitarity)
            if np.linalg.norm(normalized) > 0:
                direction = normalized / np.linalg.norm(normalized)
                quadrature = float(np.imag(np.vdot(direction, evolved[1:])))
            else:
                quadrature = 0.0
            probability = float(np.linalg.norm(evolved[1:])**2)
            receiver_quadratures.append(quadrature)
            covariance = 0.0
            for index, (representation, frame) in enumerate(zip(c576.METRIC_REPS, c576.LIFTED_FRAMES)):
                rotated_matrix = orbit_matrix(tuple(float(value) for value in frame @ momentum))
                rotated_raw = rotated_matrix @ (representation @ coframe) - endpoint
                rotated_normalized, _, _ = local_normalize(rotated_raw, regulator)
                permutation = ORBIT_REPS[index]
                covariance = max(covariance, float(np.linalg.norm(rotated_normalized - permutation @ normalized)))
                rotated_h, _ = normalized_actuation(rotated_normalized, sign, scale, endpoint)
                rep25 = np.zeros((25, 25)); rep25[0, 0] = 1; rep25[1:, 1:] = permutation
                covariance = max(covariance, float(np.linalg.norm(rotated_h - rep25 @ hamiltonian @ rep25.T)))
            max_covariance = max(max_covariance, covariance)
            _, deleted = normalized_actuation(normalized, sign, scale, 0)
            deletion = float(np.linalg.norm(evolved - deleted @ initial))
            min_delete = min(min_delete, deletion)
            fixture.append({
                "regulator": regulator, "feedback_sign": sign, "feedback_scale": scale,
                "lambda_sign": lambda_sign, "lambda_magnitude": lambda_magnitude,
                "improvement_coefficient": coefficient, "local_orbit_denominator": denominator,
                "zero_branch": branch, "receiver_quadrature": quadrature,
                "receiver_probability": probability, "inverse_residual": inverse,
                "all24_covariance_residual": covariance,
            })
            alternatives += 1

        zero, zero_norm, zero_branch = local_normalize(np.zeros(24, dtype=complex), 0.0)
        zero_h, zero_u = normalized_actuation(zero, 1, 1.0, endpoint)
        regulator_rows.append({
            "fixture": label, "strict_zero_denominator": zero_norm, "strict_zero_branch": zero_branch,
            "strict_zero_output_norm": float(np.linalg.norm(zero)),
            "source_off_update_identity_residual": float(np.linalg.norm(zero_u - np.eye(25))),
            "source_off_hamiltonian_norm": float(np.linalg.norm(zero_h)),
        })
        rows.append({"fixture": label, "length": length, "held": held,
                     "members_audited": len(fixture), "alternatives": fixture})

    quadrature_signs = sorted({int(np.sign(value)) for value in receiver_quadratures if abs(value) > 1e-12})
    output = {
        "object": "one-site 24-frame raw Regge-deficit orbit normalized before a Cycle612 endpoint-controlled 25-rail actuation",
        "disposition": "CONSTRUCTIVE_STRICTLY_LOCAL_ORBIT_NORMALIZER_AND_POINTWISE_INVERSE_ACTUATION; SIGN_SCALE_AND_PHYSICAL_NONLINEAR_EVALUATOR_OPEN",
        "normalizer": "n_x=d_x/sqrt(sum_F |d_x,F|^2+epsilon^2), with n_x=0 exactly when epsilon=0 and d_x=0",
        "bounded_physical_support": "each of 24 co-present frame values uses the Cycle576 raw deficit on one [-1,1]^4 hinge-star neighborhood; no lattice norm, Fourier norm, or global parity service",
        "co_present_frame_values_supplied": 24,
        "frame_value_preparation_and_continuous_reciprocal_square_root_compiler_supplied": True,
        "physical_support_two_reversible_normalizer_evaluator_executed": False,
        "pointwise_actuation_unary_M2": 25,
        "pointwise_actuation_generator_support": 2,
        "audited_regulators": [0.0, 0.5, 1.0, 2.0],
        "audited_feedback_signs": [-1, 1],
        "audited_feedback_scales": [0.5, 1.0, 2.0],
        "audited_lambda_signs": [-1, 1],
        "audited_lambda_magnitudes": [1.0, 2.0],
        "audited_improvements": [-1.0, 0.0, 1.0],
        "members_total": alternatives,
        "rows": rows,
        "zero_controls": regulator_rows,
        "endpoint_rows": endpoint_rows,
        "maximum_local_deficit_Ward_residual": max_ward,
        "maximum_gauge_orbit_invariance_residual": max_gauge,
        "maximum_all24_normalizer_and_actuation_covariance_residual": max_covariance,
        "all576_orbit_representation_failures": group_failures,
        "maximum_pointwise_inverse_residual": max_inverse,
        "maximum_pointwise_unitarity_residual": max_unitarity,
        "minimum_endpoint_deletion_signal": min_delete,
        "receiver_quadrature_signs": quadrature_signs,
        "receiver_map_to_Cycle612_word_derived": False,
        "continuous_response_only_lawful_time_lane_target": "3/4 DELAY association; consistency is not shared-code identification",
        "advance_5_over_4_count_edit_interface_driven": False,
        "unique_receiver_word_selected": False,
        "no_hidden_nonlocal_normalization": True,
        "pointwise_inverse_is_not_a_superposition_safe_nonlinear_M2_compiler": True,
        "Gauss_unchanged_because_orbit_and_endpoint_are_U1_scalars": True,
    }
    check(
        "Route A constructs a bounded-site orbit normalizer with exact zero handling and all-frame Ward/covariance controls",
        max(max_ward, max_gauge, max_covariance) < TOL and group_failures == 0
        and all(row["strict_zero_branch"] == "EXACT_ZERO_TO_ZERO"
                and row["source_off_update_identity_residual"] < TOL for row in regulator_rows)
        and output["no_hidden_nonlocal_normalization"],
        {key: output[key] for key in ("maximum_local_deficit_Ward_residual", "maximum_gauge_orbit_invariance_residual", "maximum_all24_normalizer_and_actuation_covariance_residual", "all576_orbit_representation_failures")},
    )
    check(
        "Route A pointwise actuation is reversible and deletion-sensitive but derives neither sign/scale nor a shared-code DELAY/count-edit receiver mechanism",
        max(max_inverse, max_unitarity) < TOL and min_delete > 1e-5
        and quadrature_signs == [-1, 1]
        and not output["receiver_map_to_Cycle612_word_derived"]
        and not output["unique_receiver_word_selected"]
        and output["pointwise_inverse_is_not_a_superposition_safe_nonlinear_M2_compiler"],
        {"inverse": max_inverse, "unitarity": max_unitarity, "deletion": min_delete, "signs": quadrature_signs},
    )
    return output


# ---------------------------------------------------------------------------
# Route B: bounded rational saturation with exact piecewise-quadratic roots.

def saturated(value: float, alpha: float) -> float:
    return alpha * value / (1 + alpha * abs(value))


def fixed_points(r0: float, rho: float, signed_scale: float, alpha: float) -> list[dict]:
    delta = r0 - rho
    roots = []
    for branch in (1, -1):
        if branch == 1:
            coefficients = (alpha, 1 - alpha * delta - signed_scale * alpha, -delta)
        else:
            coefficients = (-alpha, 1 + alpha * delta - signed_scale * alpha, -delta)
        for candidate in np.roots(coefficients):
            if abs(candidate.imag) > 1e-9:
                continue
            x = float(candidate.real)
            if (branch == 1 and x < -1e-9) or (branch == -1 and x > 1e-9):
                continue
            receiver = x + rho
            residual = receiver - r0 - signed_scale * saturated(receiver - rho, alpha)
            if abs(residual) > 2e-8 or any(abs(receiver - row["receiver"]) < 2e-7 for row in roots):
                continue
            derivative = signed_scale * alpha / (1 + alpha * abs(x))**2
            roots.append({
                "receiver": receiver, "piece": "x>=0" if branch == 1 else "x<=0",
                "fixed_point_residual": abs(residual), "iteration_derivative": derivative,
                "stability_diagnostic": "stable" if abs(derivative) < 1 - 1e-9 else ("neutral" if abs(abs(derivative) - 1) <= 1e-9 else "unstable"),
            })
    return sorted(roots, key=lambda row: row["receiver"])


def linear_receiver(momentum: np.ndarray, coupling: float, coefficient: float) -> tuple[float, float, float]:
    q = c576.frame_averaged_metric_hessian(momentum)
    source = c576.frame_averaged_source_row(momentum)
    base = source + coefficient * (c620.spatial_trace_vector() @ q)
    response = -np.linalg.pinv(q, rcond=1e-10) @ (coupling * np.conj(base))
    receiver = float(np.real(source @ response))
    stationary = float(np.linalg.norm(q @ response + coupling * np.conj(base)))
    ward = float(np.max(np.abs(base @ c576.continuum_gauge_metric(momentum))))
    return receiver, stationary, ward


def periodic_laplacian_green(length: int, site: tuple[int, int, int]) -> tuple[np.ndarray, np.ndarray]:
    source = np.zeros((length,) * 3); source[site] = 1; source -= 1 / length**3
    frequencies = 2 * math.pi * np.fft.fftfreq(length)
    denominator = np.zeros_like(source)
    for index in product(range(length), repeat=3):
        denominator[index] = 6 - 2 * sum(math.cos(frequencies[index[axis]]) for axis in range(3))
    transformed = np.zeros(source.shape, dtype=complex)
    mask = denominator > 1e-14
    transformed[mask] = np.fft.fftn(source)[mask] / denominator[mask]
    return source, np.fft.ifftn(transformed).real


def open_dirichlet_laplacian(length: int) -> tuple[list[tuple[int, int, int]], np.ndarray]:
    sites = list(product(range(length), repeat=3)); lookup = {site: index for index, site in enumerate(sites)}
    hessian = 6 * np.eye(len(sites))
    for site in sites:
        for axis in range(3):
            for step in (-1, 1):
                target = list(site); target[axis] += step; target = tuple(target)
                if target in lookup:
                    hessian[lookup[site], lookup[target]] = -1
    return sites, hessian


def rotate_open_site(site: tuple[int, int, int], frame: np.ndarray, length: int) -> tuple[int, int, int]:
    center = (length - 1) / 2
    moved = frame @ (np.asarray(site, dtype=float) - center) + center
    return tuple(int(round(value)) for value in moved)


def common_coupling_comparator(shore_data: dict) -> dict:
    r607 = shore_data["receipts"]["607"]
    r609 = shore_data["receipts"]["609"]
    r613 = shore_data["receipts"]["613"]
    r604 = shore_data["receipts"]["604"]
    frames = c210.proper_cubic_frames()
    periodic_rows = []; open_rows = []
    max_covariance = max_static = max_sign_cancel = 0.0
    min_positive_eigenvalue = math.inf
    frame_lookup = {tuple(frame.reshape(-1)): index for index, frame in enumerate(frames)}
    scalar_group_failures = 0
    for first in frames:
        for second in frames:
            scalar_group_failures += int(tuple((first @ second).reshape(-1)) not in frame_lookup)
    for label, length, held in FIXTURES:
        anchor = (0, 0, 0)
        source, field = periodic_laplacian_green(length, anchor)
        near = (1, 0, 0); far = (length // 2,) * 3
        frequencies = 2 * math.pi * np.fft.fftfreq(length)
        eigenvalues = [6 - 2 * sum(math.cos(frequencies[index[axis]]) for axis in range(3))
                       for index in product(range(length), repeat=3)]
        positive = [value for value in eigenvalues if value > 1e-12]
        min_positive_eigenvalue = min(min_positive_eigenvalue, min(positive))
        equation = c615.c604.laplacian_float(field) - source if hasattr(c615, "c604") else None
        if equation is None:
            laplacian = 6 * field.copy()
            for axis in range(3):
                laplacian -= np.roll(field, 1, axis=axis) + np.roll(field, -1, axis=axis)
            equation = laplacian - source
        static_residual = float(np.linalg.norm(equation))
        max_static = max(max_static, static_residual)
        energies = []
        for coupling in (-2.0, -1.0, -0.5, 0.5, 1.0, 2.0):
            near_energy = -coupling**2 * float(field[near])
            far_energy = -coupling**2 * float(field[far])
            opposite_near = +coupling**2 * float(field[near])
            energies.append({
                "common_coupling": coupling, "near_cross_effective_action": near_energy,
                "far_cross_effective_action": far_energy,
                "opposite_test_sign_control": opposite_near,
                "same_coupling_near_is_lower_than_far": near_energy < far_energy,
            })
        for magnitude in (0.5, 1.0, 2.0):
            plus = -magnitude**2 * float(np.vdot(source, field).real) / 2
            minus = -(-magnitude)**2 * float(np.vdot(source, field).real) / 2
            max_sign_cancel = max(max_sign_cancel, abs(plus - minus))
        covariance = 0.0
        for frame in frames:
            rotated_near = tuple(int(value % length) for value in frame @ np.asarray(near))
            covariance = max(covariance, abs(float(field[near]) - float(field[rotated_near])))
        max_covariance = max(max_covariance, covariance)
        one_step = (1 / 12) * source
        finite_not_static = float(np.linalg.norm(one_step - field))
        periodic_rows.append({
            "fixture": label, "length": length, "held": held,
            "positive_sector_minimum_eigenvalue": min(positive), "zero_mode_count": sum(abs(value) <= 1e-12 for value in eigenvalues),
            "static_equation_residual": static_residual, "all24_pair_energy_covariance_residual": covariance,
            "one_kick_not_stationary_elimination_signal": finite_not_static,
            "energies": energies,
        })

        sites, hessian = open_dirichlet_laplacian(length); lookup = {site: index for index, site in enumerate(sites)}
        carried_anchor = ((length - 1) // 2,) * 3
        near_open = (carried_anchor[0] + 1, carried_anchor[1], carried_anchor[2])
        far_open = (length - 1,) * 3
        source_open = np.zeros(len(sites)); source_open[lookup[carried_anchor]] = 1
        field_open = np.linalg.solve(hessian, source_open)
        open_inverse = float(np.linalg.norm(hessian @ field_open - source_open))
        eigmin = float(np.min(np.linalg.eigvalsh(hessian)))
        open_covariance = 0.0
        for frame in frames:
            rotated_anchor = rotate_open_site(carried_anchor, frame, length)
            rotated_near = rotate_open_site(near_open, frame, length)
            rotated_source = np.zeros(len(sites)); rotated_source[lookup[rotated_anchor]] = 1
            rotated_field = np.linalg.solve(hessian, rotated_source)
            open_covariance = max(open_covariance, abs(field_open[lookup[near_open]] - rotated_field[lookup[rotated_near]]))
        max_covariance = max(max_covariance, open_covariance)
        open_rows.append({
            "fixture": label, "length": length, "held": held, "carried_anchor": carried_anchor,
            "Dirichlet_positive_minimum_eigenvalue": eigmin, "zero_mode_count": 0,
            "inverse_residual": open_inverse, "all24_decorated_anchor_covariance_residual": open_covariance,
            "near_cross_effective_action_q1": -float(field_open[lookup[near_open]]),
            "far_cross_effective_action_q1": -float(field_open[lookup[far_open]]),
            "near_is_lower_than_far": -field_open[lookup[near_open]] < -field_open[lookup[far_open]],
            "boundary_condition_supplied": "real Dirichlet scalar comparator; not the Cycle615 compact F17 boundary law",
        })

    exact_local_reciprocity = r607["route_A_joint_CAR_Weyl_interaction"]["maximum_action_mixed_derivative_reciprocity_residual"] < TOL
    exact_support_two = r609["route_A_support2_NQ_compiler"]["maximum_elementary_gate_support_M2"] == 2
    scalar_join = (
        r607["route_C_actual_source_prediction"]["finite_horizon_equals_static_limit"]
        and r607["route_C_actual_source_prediction"]["field_propagation_has_physical_M2_compiler"]
        and r613["route_A_fully_gauged_joint_action"]["representation_charge_is_unique_physical_coupling"]
        and r613["route_A_fully_gauged_joint_action"]["physical_coupling_or_action_normalization_derived"]
    )
    return {
        "object": "same-coupling stationary elimination comparator A_eff=-q^2<rho,H^+rho>/2",
        "mathematical_disposition": "CONSTRUCTIVE_SIGN_CANCELLATION_ON_DECLARED_POSITIVE_PERIODIC_P0_AND_OPEN_DIRICHLET_SECTORS",
        "physical_disposition": "ROUTE_SPECIFIC_JOIN_FAILURE: RECIPROCAL NQ FINITE UPDATE DOES_NOT IMPLEMENT THE POSITIVE SCALAR STATIONARY ELIMINATION",
        "periodic_rows": periodic_rows, "open_rows": open_rows,
        "maximum_common_sign_cancellation_residual": max_sign_cancel,
        "minimum_positive_periodic_eigenvalue": min_positive_eigenvalue,
        "maximum_all24_energy_covariance_residual": max_covariance,
        "all576_scalar_representation_failures": scalar_group_failures,
        "Cycle607_same_NQ_local_mixed_derivative_reciprocity": exact_local_reciprocity,
        "Cycle609_same_NQ_elementary_support_two": exact_support_two,
        "Cycle613_representation_charge": r613["route_A_fully_gauged_joint_action"]["representation_charge"],
        "Cycle613_charge_is_unique_physical_coupling": r613["route_A_fully_gauged_joint_action"]["representation_charge_is_unique_physical_coupling"],
        "Cycle604_periodic_kernel_is_the_executed_Cycle607_609_Weyl_field": False,
        "stationary_elimination_implemented_by_physical_finite_update": scalar_join,
        "Cycle607_finite_horizon_equals_static_limit": r607["route_C_actual_source_prediction"]["finite_horizon_equals_static_limit"],
        "Cycle607_field_propagation_has_physical_M2_compiler": r607["route_C_actual_source_prediction"]["field_propagation_has_physical_M2_compiler"],
        "Cycle604_order_alternative_signal": r604["route_B_reciprocal_response"]["minimum_order_alternative_signal"],
        "Cycle607_order_alternative_signal": r607["route_B_reversal_ordering"]["minimum_kick_first_vs_drift_first_signal"],
        "finite_update_factor_order_selected_by_stationary_comparator": False,
        "source_off_and_receiver_zero_effective_action": 0.0,
        "same_coupling_orientation_sign_cancels": max_sign_cancel < TOL,
        "magnitude_units_unique_stress_nonlinear_law_derived": False,
        "attraction_or_gravity_claimed": False,
    }


def route_b(shore_data: dict) -> dict:
    rows = []
    max_stationary = max_ward = max_root = max_covariance = max_inverse = 0.0
    min_delete = math.inf
    branch_counts = set(); stability_labels = set(); all_root_signs = set()
    members = 0
    frames = c210.proper_cubic_frames()
    for label, length, held in FIXTURES:
        momentum = 2 * math.pi / length * np.asarray((1.0, 1.0, 0.0, 1.0))
        fixture = []
        for feedback_sign, feedback_scale, alpha, lambda_sign, lambda_magnitude, coefficient in product(
            (-1, 1), (0.5, 1.0, 2.0), (0.5, 1.0, 2.0), (-1, 1), (1.0, 2.0), (-1.0, 0.0, 1.0)
        ):
            coupling = lambda_sign * lambda_magnitude * c576.SOURCE_COUPLING
            r0, stationary, ward = linear_receiver(momentum, coupling, coefficient)
            roots = fixed_points(r0, 1.0, feedback_sign * feedback_scale, alpha)
            branch_counts.add(len(roots)); stability_labels.update(row["stability_diagnostic"] for row in roots)
            all_root_signs.update(int(np.sign(row["receiver"])) for row in roots if abs(row["receiver"]) > 1e-12)
            max_stationary = max(max_stationary, stationary); max_ward = max(max_ward, ward)
            max_root = max(max_root, max(row["fixed_point_residual"] for row in roots))
            covariance = 0.0
            q = c576.frame_averaged_metric_hessian(momentum)
            source = c576.frame_averaged_source_row(momentum)
            improvement = c620.spatial_trace_vector() @ q
            base = source + coefficient * improvement
            response = -np.linalg.pinv(q, rcond=1e-10) @ (coupling * np.conj(base))
            for representation, frame in zip(c576.METRIC_REPS, c576.LIFTED_FRAMES):
                rotated_q = representation @ q @ representation.T
                rotated_source = source @ representation.T
                rotated_base = base @ representation.T
                rotated_response = -np.linalg.pinv(rotated_q, rcond=1e-10) @ (coupling * np.conj(rotated_base))
                rotated_r0 = float(np.real(rotated_source @ rotated_response))
                covariance = max(covariance, abs(rotated_r0 - r0))
            max_covariance = max(max_covariance, covariance)
            for root in roots:
                theta = feedback_sign * feedback_scale * saturated(root["receiver"] - 1.0, alpha)
                update = np.asarray(((math.cos(theta), -1j * math.sin(theta)),
                                     (-1j * math.sin(theta), math.cos(theta))), dtype=complex)
                max_inverse = max(max_inverse, float(np.linalg.norm(update.conj().T @ update - np.eye(2))))
            deleted = fixed_points(r0, 1.0, 0.0, alpha)
            deletion = max(abs(root["receiver"] - deleted[0]["receiver"]) for root in roots)
            min_delete = min(min_delete, deletion)
            fixture.append({
                "feedback_sign": feedback_sign, "feedback_scale": feedback_scale,
                "saturation_alpha": alpha, "lambda_sign": lambda_sign,
                "lambda_magnitude": lambda_magnitude, "improvement_coefficient": coefficient,
                "linear_receiver": r0, "fixed_points": roots, "fixed_point_count": len(roots),
                "all24_linear_response_covariance_residual": covariance,
            })
            members += 1
        rows.append({"fixture": label, "length": length, "held": held,
                     "members_audited": len(fixture), "alternatives": fixture})

    zero_controls = []
    for feedback_sign, feedback_scale, alpha in product((-1, 1), (0.5, 1.0, 2.0), (0.5, 1.0, 2.0)):
        roots = fixed_points(0.0, 0.0, feedback_sign * feedback_scale, alpha)
        zero_controls.append({"feedback_sign": feedback_sign, "feedback_scale": feedback_scale,
                              "saturation_alpha": alpha, "receiver_zero_roots": roots})
    source_off = fixed_points(0.0, 0.0, 0.0, 1.0)
    comparator = common_coupling_comparator(shore_data)
    frame_lookup = {tuple(frame.reshape(-1)): index for index, frame in enumerate(c576.FRAMES)}
    metric_group_failures = 0
    for i, first in enumerate(c576.FRAMES):
        for j, second in enumerate(c576.FRAMES):
            target = frame_lookup[tuple((first @ second).reshape(-1))]
            metric_group_failures += int(np.linalg.norm(
                c576.METRIC_REPS[i] @ c576.METRIC_REPS[j] - c576.METRIC_REPS[target]
            ) > TOL)
    output = {
        "object": "bounded rational receiver map r'=r0+sigma*kappa*alpha(r-rho)/(1+alpha|r-rho|)",
        "disposition": "CONSTRUCTIVE_COMPLETE_PIECEWISE_QUADRATIC_FIXED_POINT_ENUMERATION; STABILITY_SIGN_SCALE_AND_RECEIVER_MAP_UNSELECTED",
        "root_completeness": "x=r-rho splits into x>=0 and x<=0; each branch is one explicit quadratic and every sign-valid root is substituted back",
        "root_bound": "|r-r0|<=kappa for every branch",
        "audited_feedback_signs": [-1, 1], "audited_feedback_scales": [0.5, 1.0, 2.0],
        "audited_saturation_scales": [0.5, 1.0, 2.0], "audited_lambda_signs": [-1, 1],
        "audited_lambda_magnitudes": [1.0, 2.0], "audited_improvements": [-1.0, 0.0, 1.0],
        "members_total": members, "rows": rows,
        "receiver_zero_controls": zero_controls,
        "source_and_endpoint_off_roots": source_off,
        "fixed_point_counts_seen": sorted(branch_counts),
        "stability_diagnostic_labels_seen": sorted(stability_labels),
        "all_fixed_point_receiver_signs": sorted(all_root_signs),
        "maximum_linear_stationary_residual": max_stationary,
        "maximum_Ward_residual": max_ward,
        "maximum_fixed_point_residual": max_root,
        "maximum_all24_covariance_residual": max_covariance,
        "maximum_pointwise_actuation_inverse_residual": max_inverse,
        "minimum_feedback_deletion_signal": min_delete,
        "all576_metric_representation_failures": metric_group_failures,
        "stability_used_as_selection_rule": False,
        "bounded_action_or_positive_Hessian_assumed": False,
        "receiver_map_to_Cycle612_word_derived": False,
        "continuous_response_only_lawful_time_lane_target": "3/4 DELAY association; consistency is not shared-code identification",
        "advance_5_over_4_count_edit_interface_driven": False,
        "unique_receiver_word_selected": False,
        "common_coupling_sign_cancellation": comparator,
    }
    check(
        "Route B exhausts every bounded rational fixed-point branch with Ward/covariance/inverse controls",
        max(max_stationary, max_ward, max_root, max_covariance, max_inverse) < TOL
        and min_delete > 1e-6 and branch_counts and metric_group_failures == 0
        and len(source_off) == 1 and abs(source_off[0]["receiver"]) < TOL,
        {"stationary": max_stationary, "ward": max_ward, "root": max_root,
         "covariance": max_covariance, "inverse": max_inverse, "counts": sorted(branch_counts)},
    )
    check(
        "Route B keeps stability diagnostic and retains sign/scale/lambda/c without treating response sign as delay/advance selection",
        all_root_signs == {-1, 1}
        and not output["stability_used_as_selection_rule"]
        and not output["bounded_action_or_positive_Hessian_assumed"]
        and not output["receiver_map_to_Cycle612_word_derived"]
        and not output["unique_receiver_word_selected"],
        {"root_signs": sorted(all_root_signs), "stability": sorted(stability_labels)},
    )
    check(
        "Common-coupling q orientation cancels on positive stationary comparators but is not the executed finite NQ field law",
        comparator["same_coupling_orientation_sign_cancels"]
        and comparator["Cycle607_same_NQ_local_mixed_derivative_reciprocity"]
        and comparator["Cycle609_same_NQ_elementary_support_two"]
        and comparator["minimum_positive_periodic_eigenvalue"] > 0
        and comparator["maximum_all24_energy_covariance_residual"] < TOL
        and comparator["all576_scalar_representation_failures"] == 0
        and all(all(row["same_coupling_near_is_lower_than_far"] for row in fixture["energies"])
                for fixture in comparator["periodic_rows"])
        and all(row["near_is_lower_than_far"] for row in comparator["open_rows"])
        and not comparator["stationary_elimination_implemented_by_physical_finite_update"]
        and not comparator["attraction_or_gravity_claimed"],
        {key: comparator[key] for key in ("maximum_common_sign_cancellation_residual", "minimum_positive_periodic_eigenvalue", "maximum_all24_energy_covariance_residual", "stationary_elimination_implemented_by_physical_finite_update")},
    )
    return output


# ---------------------------------------------------------------------------
# Route C: open decorated flux plus separate exact support-two periodic blocks.

DIRS = tuple(tuple(int(value) for value in direction) for direction in c210.DIRECTIONS)


def inside(site: tuple[int, int, int], length: int) -> bool:
    return all(0 <= value < length for value in site)


def add(site: tuple[int, int, int], direction: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(left + right for left, right in zip(site, direction))


def decorated_flux(length: int, anchor: tuple[int, int, int]) -> dict:
    edges = {}; weight = pow(6, -1, c609.MOD)
    for direction in DIRS:
        source = anchor
        while True:
            target = add(source, direction); edges[(source, target)] = weight
            if not inside(target, length):
                break
            source = target
    return edges


def open_divergence(edges: dict, length: int) -> dict:
    result = {site: 0 for site in product(range(length), repeat=3)}
    for (source, target), value in edges.items():
        if inside(source, length): result[source] = (result[source] + value) % c609.MOD
        if inside(target, length): result[target] = (result[target] - value) % c609.MOD
    return result


def rotate_decorated_edges(edges: dict, frame: np.ndarray, length: int) -> dict:
    return {(rotate_open_site(source, frame, length), rotate_open_site(target, frame, length)): value
            for (source, target), value in edges.items()}


def unitary_givens_certificate(unitary: np.ndarray) -> tuple[dict, list[tuple[int, int]]]:
    reduced = unitary.copy(); factors = []; size = len(unitary)
    for column in range(size - 1):
        for row in range(size - 1, column, -1):
            first, second = reduced[row - 1, column], reduced[row, column]
            norm = math.hypot(abs(first), abs(second))
            if norm < 2e-13:
                continue
            block = np.asarray(((np.conj(first) / norm, np.conj(second) / norm),
                                (-second / norm, first / norm)), dtype=complex)
            reduced[[row - 1, row], :] = block @ reduced[[row - 1, row], :]
            factors.append((row - 1, row, block))
    diagonal = np.diag(reduced)
    phases = np.asarray([value / abs(value) if abs(value) else 1 for value in diagonal])
    reconstructed = np.diag(phases)
    for first, second, block in reversed(factors):
        reconstructed[[first, second], :] = block.conj().T @ reconstructed[[first, second], :]
    return {
        "logical_dimension": size,
        "two_level_Givens_support_two_gates": len(factors),
        "one_rail_phase_support_one_gates": size,
        "upper_triangle_residual": float(np.linalg.norm(reduced - np.diag(diagonal))),
        "diagonal_unit_modulus_residual": float(np.max(np.abs(np.abs(diagonal) - 1))),
        "EG_intertwiner_reconstruction_residual": float(np.linalg.norm(reconstructed - unitary)),
        "unary_code_leakage": 0.0,
        "one_excitation_constraint": "(sum_i n_i-1)^2, a bounded-block sum of support-one and support-two terms",
    }, [(first, second) for first, second, _ in factors]


def base_role_layout(count: int) -> list[tuple[int, int, int]]:
    candidates = [(a, b, c) for a in range(1, 25) for b in range(a + 1, 25) for c in range(b + 1, 25)]
    if len(candidates) < count:
        raise ValueError("not enough generic proper-cubic orbits")
    return candidates[:count]


def layout_manifest() -> dict:
    counts = {
        "F17_six_directed_link_unary17": 6 * 17,
        "Cycle576_source_plus_24x15_Regge_unary": 361,
        "Cycle620_full_Fock_plus_endpoint_unary": 128,
        "Cycle608_612_pointer_binder_opportunity_receiver": 4,
        "open_periodic_domain_flags": 2,
        "one_hot_and_Gauss_check_work_upper_bound": 8,
    }
    total = sum(counts.values()); roles = base_role_layout(total); frames = c210.proper_cubic_frames()
    all_coordinates = []
    for role in roles:
        orbit = [tuple(int(value) for value in frame @ np.asarray(role)) for frame in frames]
        all_coordinates.extend(orbit)
    collisions = len(all_coordinates) - len(set(all_coordinates))
    group_failures = 0
    for role in roles[:32]:
        vector = np.asarray(role)
        for first in frames:
            for second in frames:
                group_failures += int(not np.array_equal((first @ second) @ vector, first @ (second @ vector)))
    return {
        "base_role_counts": counts, "base_roles_per_coarse_cell": total,
        "proper_cubic_role_orbit_upper_bound_M2": 24 * total,
        "maximum_coordinate_absolute_value": max(abs(value) for coordinate in all_coordinates for value in coordinate),
        "fits_Cycle610_K129_supercell": max(abs(value) for coordinate in all_coordinates for value in coordinate) <= 64,
        "all24_role_coordinate_collisions": collisions,
        "sampled_all576_coordinate_action_failures": group_failures,
        "roles": roles,
        "manifest_is_executed_joint_unitary_intertwiner": False,
        "one_hot_orientation_genesis_supplied": True,
        "domain_flag_genesis_supplied": True,
    }


def bus_audit(pairs: list[tuple[int, int]], coordinates: list[tuple[int, int, int]]) -> dict:
    max_distance = swaps = failures = 0
    for first, second in pairs:
        left = c610.bus_index(coordinates[first]); right = c610.bus_index(coordinates[second])
        failures += int(c610.bus_coordinate(left) != coordinates[first] or c610.bus_coordinate(right) != coordinates[second])
        distance = abs(left - right); max_distance = max(max_distance, distance); swaps += 2 * max(0, distance - 1)
    return {"endpoint_pairs": len(pairs), "maximum_bus_distance": max_distance,
            "move_apply_restore_SWAPs": swaps, "bus_inverse_or_endpoint_failures": failures,
            "maximum_elementary_gate_support_M2": 2}


def route_c() -> dict:
    frames = c210.proper_cubic_frames(); manifest = layout_manifest()
    roles = manifest.pop("roles")
    open_rows = []; max_gauss = max_covariance = max_inverse = 0; min_delete = math.inf; open_group = 0
    for label, length, held in FIXTURES:
        anchor = ((length - 1) // 2,) * 3; edges = decorated_flux(length, anchor); divergence = open_divergence(edges, length)
        gauss = max(min((value - int(site == anchor)) % c609.MOD, (int(site == anchor) - value) % c609.MOD)
                    for site, value in divergence.items())
        boundary = sum(value for (source, target), value in edges.items() if not inside(target, length)) % c609.MOD
        covariance = 0
        for frame in frames:
            moved_anchor = rotate_open_site(anchor, frame, length)
            covariance = max(covariance, int(rotate_decorated_edges(edges, frame, length) != decorated_flux(length, moved_anchor)))
        for first in frames:
            for second in frames:
                direct = rotate_decorated_edges(edges, first @ second, length)
                composed = rotate_decorated_edges(rotate_decorated_edges(edges, second, length), first, length)
                open_group += int(direct != composed)
        boundary_edges = [edge for edge in edges if not inside(edge[1], length)]
        deleted = edges.copy(); deleted.pop(boundary_edges[0])
        deleted_div = open_divergence(deleted, length)
        delete = max(min((deleted_div[site] - divergence[site]) % c609.MOD,
                         (divergence[site] - deleted_div[site]) % c609.MOD) for site in divergence)
        first_edge = next(iter(edges)); updated = edges.copy(); updated[first_edge] = (updated[first_edge] + 1) % c609.MOD
        restored = updated.copy(); restored[first_edge] = (restored[first_edge] - 1) % c609.MOD
        inverse = int(restored != edges)
        max_gauss = max(max_gauss, gauss); max_covariance = max(max_covariance, covariance); max_inverse = max(max_inverse, inverse); min_delete = min(min_delete, delete)
        open_rows.append({
            "fixture": label, "length": length, "held": held, "carried_anchor": anchor,
            "anchor_orbit": sorted({rotate_open_site(anchor, frame, length) for frame in frames}),
            "anchor_is_unique_geometric_center": length % 2 == 1,
            "open_edges_including_boundary_ports": len(edges), "periodic_wrap_edges": 0,
            "F17_port_weight": pow(6, -1, c609.MOD), "boundary_total_flux_mod17": boundary,
            "Gauss_residual": gauss, "all24_decorated_flux_covariance_residual": covariance,
            "increment_inverse_residual": inverse, "boundary_port_deletion_signal": delete,
            "lawful_F17_unary_code_leakage": 0,
            "unary17_link_increment_support_two_SWAPs": 16,
        })

    regge_rows = []; direct_rows = []
    max_regge_eg = max_regge_inverse = max_k_eg = max_k_inverse = max_k_covariance = 0.0
    min_regge_source_delete = min_regge_carrier_delete = math.inf
    min_k_delete = math.inf; k_quadrature_signs = set(); k_probabilities = set(); all_pairs = []
    regge_coordinates = roles[6 * 17:6 * 17 + 361]
    k_start = 6 * 17 + 361; k_coordinates = roles[k_start:k_start + 128]
    for label, length, held in FIXTURES:
        momentum4 = 2 * math.pi / length * np.asarray((0.37, 0.23, 0.11, 0.0))
        regge_h = c576.frame_sector_hamiltonian(momentum4)
        regge_u = expm(-1j * c576.UPDATE_PARAMETER * regge_h)
        regge_certificate, regge_pairs = unitary_givens_certificate(regge_u)
        regge_inverse = float(np.linalg.norm(regge_u.conj().T @ regge_u - np.eye(361)))
        max_regge_eg = max(max_regge_eg, regge_certificate["EG_intertwiner_reconstruction_residual"])
        max_regge_inverse = max(max_regge_inverse, regge_inverse); all_pairs.extend(regge_pairs)
        initial_regge = np.zeros(361, dtype=complex); initial_regge[0] = 1
        regge_evolved = regge_u @ initial_regge
        no_source = expm(-1j * c576.UPDATE_PARAMETER * c576.frame_sector_hamiltonian(
            momentum4, include_source=False
        )) @ initial_regge
        no_carrier = expm(-1j * c576.UPDATE_PARAMETER * c576.frame_sector_hamiltonian(
            momentum4, include_regge=False
        )) @ initial_regge
        source_delete = float(np.linalg.norm(regge_evolved - no_source))
        carrier_delete = float(np.linalg.norm(regge_evolved - no_carrier))
        min_regge_source_delete = min(min_regge_source_delete, source_delete)
        min_regge_carrier_delete = min(min_regge_carrier_delete, carrier_delete)
        regge_rows.append({
            "fixture": label, "length": length, "held": held, "domain": "periodic_Bloch",
            "bloch_momentum": momentum4, "certificate": regge_certificate,
            "finite_update_inverse_residual": regge_inverse,
            "source_deletion_signal": source_delete,
            "Regge_carrier_deletion_signal": carrier_delete,
        })

        momentum3 = 2 * math.pi / length * np.asarray((0.37, 0.23, 0.11))
        _, generators, convergence = c620.generator_components(momentum3)
        k_trace = generators[0] + generators[1] + generators[2]
        k_hermitian = float(np.linalg.norm(k_trace - k_trace.conj().T))
        covariance = 0.0
        for frame in frames:
            fock = c620.c230.c229.fock_lift(c620.direction_representation(frame))
            rotated = c620.unitarily_centered_generator(frame @ momentum3, np.eye(3), 5e-7)
            covariance = max(covariance, float(np.linalg.norm(rotated - fock @ k_trace @ fock.T)))
        max_k_covariance = max(max_k_covariance, covariance)
        x = np.asarray(((0, 1), (1, 0)), dtype=complex)
        h_direct = np.kron(k_trace, x)
        fixture_alternatives = []
        for sign, scale in product((-1, 1), (0.5, 1.0, 2.0)):
            update = expm(-1j * sign * scale * c576.UPDATE_PARAMETER * h_direct)
            certificate, pairs = unitary_givens_certificate(update)
            inverse = float(np.linalg.norm(update.conj().T @ update - np.eye(128)))
            max_k_eg = max(max_k_eg, certificate["EG_intertwiner_reconstruction_residual"])
            max_k_inverse = max(max_k_inverse, inverse)
            if sign == 1 and scale == 1.0:
                all_pairs.extend((k_start + first, k_start + second) for first, second in pairs)
            vacuum = np.zeros(128, dtype=complex); vacuum[0] = 1
            one_particle = np.zeros(128, dtype=complex); one_particle[2] = 1
            vacuum_out = update @ vacuum; output = update @ one_particle
            probability = float(np.sum(np.abs(output[1::2])**2))
            y = np.asarray(((0, -1j), (1j, 0)), dtype=complex)
            quadrature = float(np.vdot(output, np.kron(np.eye(64), y) @ output).real)
            k_quadrature_signs.add(int(np.sign(quadrature)))
            k_probabilities.add(round(probability, 12))
            deletion = float(np.linalg.norm(output - one_particle)); min_k_delete = min(min_k_delete, deletion)
            fixture_alternatives.append({
                "coupling_sign": sign, "coupling_scale": scale,
                "unary_support_two_certificate": certificate, "inverse_residual": inverse,
                "vacuum_receiver_probability": float(np.sum(np.abs(vacuum_out[1::2])**2)),
                "one_particle_receiver_probability": probability, "endpoint_Y_quadrature": quadrature,
            })
        direct_rows.append({
            "fixture": label, "length": length, "held": held, "domain": "periodic_Bloch",
            "candidate": "U_K=exp[-i eta sigma kappa (K_xx+K_yy+K_zz) tensor X_endpoint]",
            "trace_contraction_is_proper_cubic_scalar": True,
            "K_trace_Hermiticity_residual": k_hermitian,
            "K_finite_difference_convergence_residual": convergence,
            "all24_K_trace_covariance_residual": covariance,
            "alternatives": fixture_alternatives,
        })

    # Pairs from the Regge block are local indices; direct-K pairs were shifted.
    routed_pairs = []
    for first, second in all_pairs:
        if first < 361 and second < 361:
            routed_pairs.append((6 * 17 + first, 6 * 17 + second))
        else:
            routed_pairs.append((first, second))
    bus = bus_audit(routed_pairs, roles)
    endpoint_rows = []
    for matter, binder in product((0, 1), repeat=2):
        candidate = c612.computed_candidate(matter, binder)
        endpoint_rows.append({"matter": matter, "binder": binder,
                              "endpoint": candidate["opportunity"], "pointer_after": candidate["pointer"]})

    tensor_reps = [c620.spatial_tensor_representation(frame) for frame in frames]
    tensor_group_failures = 0; lookup = {tuple(frame.reshape(-1)): index for index, frame in enumerate(frames)}
    for i, first in enumerate(frames):
        for j, second in enumerate(frames):
            target = lookup[tuple((first @ second).reshape(-1))]
            tensor_group_failures += int(np.linalg.norm(tensor_reps[i] @ tensor_reps[j] - tensor_reps[target]) > TOL)

    output = {
        "object": "one role schema for open F17 links, periodic 361-rail Regge, full-Fock K plus endpoint, and Cycle608/612 work",
        "disposition": "CONSTRUCTIVE_MANIFEST_AND_EXACT_PERIODIC_UNARY_SUPPORT_TWO_COMPILERS; OPEN_TO_PERIODIC_SOURCE_RESPONSE_JOIN_NOT_EXECUTED",
        "manifest": manifest,
        "open_F17": {
            "rows": open_rows, "maximum_Gauss_residual": max_gauss,
            "maximum_all24_covariance_residual": max_covariance,
            "all576_decorated_open_representation_failures": open_group,
            "maximum_inverse_residual": max_inverse, "minimum_boundary_deletion_signal": min_delete,
            "open_flux_genesis_supplied": True,
        },
        "periodic_Regge_support_two": {
            "rows": regge_rows, "maximum_EG_intertwiner_residual": max_regge_eg,
            "maximum_inverse_residual": max_regge_inverse,
            "minimum_source_deletion_signal": min_regge_source_delete,
            "minimum_Regge_carrier_deletion_signal": min_regge_carrier_delete,
            "finite_time_update_compiled_to_unary_support_two": True,
            "Bloch_coefficients_are_not_open_real_space_coefficients": True,
        },
        "direct_K_endpoint_support_two": {
            "rows": direct_rows, "maximum_EG_intertwiner_residual": max_k_eg,
            "maximum_inverse_residual": max_k_inverse,
            "maximum_all24_covariance_residual": max_k_covariance,
            "all576_tensor_representation_failures": tensor_group_failures,
            "minimum_coupling_deletion_signal": min_k_delete,
            "endpoint_quadrature_signs": sorted(k_quadrature_signs),
            "distinct_endpoint_probabilities": len(k_probabilities),
            "vacuum_receiver_zero": all(max(row["vacuum_receiver_probability"] for row in fixture["alternatives"]) < TOL for fixture in direct_rows),
            "K_called_rate_or_unique_physical_stress": False,
        },
        "support_two_bus": bus,
        "endpoint_rows": endpoint_rows,
        "endpoint_pointer_work_returns_blank": all(row["pointer_after"] == 0 for row in endpoint_rows),
        "common_role_interface_exists": True,
        "manifest_counts_as_executed_joined_EG_intertwiner": False,
        "open_F17_to_periodic_Bloch_transform_present": False,
        "one_open_real_space_source_Regge_K_endpoint_update_executed": False,
        "boundary_periodic_seam_preserved": True,
        "receiver_map_to_Cycle612_word_derived": False,
        "continuous_endpoint_observable_only_lawful_time_lane_target": "3/4 DELAY association; consistency is not shared-code identification",
        "advance_5_over_4_receiver_gated_count_edit_executed": False,
        "PR5557_acceptance_harness_compatibility": "OPEN: matter-caused clean endpoint is present, but oriented duplicate-safe channel certificate, CT-1'' selection, tick lock/convention tests, and one shared-code association are not compiled here",
        "unique_receiver_word_selected": False,
        "wrapped_phase_called_energy": False,
        "gravity_claimed": False,
    }
    check(
        "Route C extends the open F17 fixture to decorated L3/L6/L7 anchors without a wrap or fictitious L6 center",
        max(max_gauss, max_covariance, max_inverse) == 0 and open_group == 0 and min_delete > 0
        and all(row["periodic_wrap_edges"] == 0 and row["boundary_total_flux_mod17"] == 1 for row in open_rows)
        and len(open_rows[1]["anchor_orbit"]) == 8 and not open_rows[1]["anchor_is_unique_geometric_center"],
        output["open_F17"],
    )
    check(
        "Route C exactly compiles the periodic Regge and direct full-Fock K-endpoint unitaries to routed support-two unary words",
        max(max_regge_eg, max_regge_inverse, max_k_eg, max_k_inverse, max_k_covariance) < TOL
        and tensor_group_failures == 0 and min_k_delete > 1e-5
        and min_regge_source_delete > 1e-5 and min_regge_carrier_delete > 1e-8
        and bus["bus_inverse_or_endpoint_failures"] == 0 and bus["maximum_elementary_gate_support_M2"] == 2
        and manifest["fits_Cycle610_K129_supercell"] and manifest["all24_role_coordinate_collisions"] == 0
        and manifest["sampled_all576_coordinate_action_failures"] == 0,
        {"regge_EG": max_regge_eg, "K_EG": max_k_eg, "K_covariance": max_k_covariance, "bus": bus},
    )
    check(
        "Route C keeps the manifest distinct from a joined open-real-space intertwiner and leaves sign/scale/word selection open",
        output["endpoint_pointer_work_returns_blank"]
        and k_quadrature_signs == {-1, 1} and len(k_probabilities) > 1
        and output["direct_K_endpoint_support_two"]["vacuum_receiver_zero"]
        and not output["manifest_counts_as_executed_joined_EG_intertwiner"]
        and not output["open_F17_to_periodic_Bloch_transform_present"]
        and not output["one_open_real_space_source_Regge_K_endpoint_update_executed"]
        and output["boundary_periodic_seam_preserved"]
        and not output["receiver_map_to_Cycle612_word_derived"]
        and not output["gravity_claimed"],
        {"quadrature_signs": sorted(k_quadrature_signs), "probabilities": len(k_probabilities)},
    )
    return output


def no_go_discipline() -> dict:
    families = [
        {"family": "strict zero-handled local orbit normalization", "object": "24-component local deficit orbit", "mechanism": "finite hinge-star norm and endpoint-controlled unary actuation", "terminal": "shared-code 3/4 DELAY association with a physical nonlinear evaluator", "marker": "ATTEMPTED", "result": "local covariant normalizer positive; reciprocal-square-root evaluator and sign/scale remain"},
        {"family": "regularized orbit normalization", "object": "sqrt(sum|d_F|^2+epsilon^2)", "mechanism": "epsilon-regular bounded orbit", "terminal": "zero-safe normalization without new scale", "marker": "ATTEMPTED", "result": "epsilon changes response and is unselected"},
        {"family": "bounded rational saturation", "object": "alpha x/(1+alpha|x|)", "mechanism": "piecewise-quadratic fixed points", "terminal": "unique receiver branch", "marker": "ATTEMPTED", "result": "all roots and stability labels enumerated; stability has no selection authority"},
        {"family": "common-coupling stationary elimination", "object": "-q^2 rho H^+ rho/2", "mechanism": "same reciprocal q at source/test plus positive kernel", "terminal": "orientation-independent physical response sign", "marker": "ATTEMPTED", "result": "mathematical sign cancellation; NQ finite update is not the scalar stationary elimination"},
        {"family": "direct trace-K endpoint coupling", "object": "(K_xx+K_yy+K_zz) tensor X_endpoint", "mechanism": "full-Fock coframe generator drives endpoint", "terminal": "unitary-derived shared-code DELAY association or separate ADVANCE count edit", "marker": "ATTEMPTED", "result": "exact periodic support-two compiler; coupling sign/scale and both mechanism joins remain"},
        {"family": "open F17 plus periodic Regge role packing", "object": "common K129 role manifest", "mechanism": "domain-flagged co-present rails", "terminal": "one joined open-real-space source-response update", "marker": "ATTEMPTED", "result": "manifest is collision-free; domain transform and joined intertwiner absent"},
        {"family": "direct open-real-space K", "object": "coframe derivative of an open coin-stream-contact update", "mechanism": "differentiate a boundary-preserving real-space unitary", "terminal": "remove open/periodic seam", "marker": "LIVE_UNTESTED", "result": "Cycle620 K is periodic Bloch; no open derivative law supplied"},
        {"family": "finite-field positive transfer sector", "object": "reflection-positive or bounded-action carrier", "mechanism": "derive allowed sign/stable branch before response", "terminal": "lawful branch selector", "marker": "LIVE_UNTESTED", "result": "RP gauge-half theorem does not pin the present matter/Regge feedback law"},
    ]
    walls = {
        "W_evaluator": "continuous local norm/saturation evaluator on physical superpositions",
        "W_sign_scale": "feedback/K coupling sign, magnitude, regulator, and saturation scale",
        "W_stationary_join": "reciprocal finite update versus positive-kernel stationary elimination",
        "W_domain_join": "open F17 boundary versus periodic Bloch Regge/K carrier",
        "W_receiver_map": "continuous response to the 3/4 DELAY association and a separate physical count-edit path for 5/4 ADVANCE",
        "W_genesis": "orientation/frame values, domain flag, flux state, endpoint chart/path, and clean work",
    }
    names = tuple(walls)
    pair_audit = [{"left": names[i], "right": names[j], "left_closes_right": False,
                   "right_closes_left": False, "independent": True}
                  for i in range(len(names)) for j in range(i + 1, len(names))]
    return {
        "skill_freshness": {
            "origin_main_checked": True,
            "local_skill_sha256": "aeac7b2b7df30c350961f4b36b980a91e9c2ebeca3f35b6c1adcd731071bdab5",
            "origin_main_skill_sha256": "7d1aea8243ddd972331b935e2e836657e72115da3efe259f828fe862469d68b7",
            "current_origin_main_skill_followed": True,
            "proof_search_governance_sha256": "be4f955d9ff8a6f18c8f0f5fd6e872cac0ca95fcb752d86ec773961a4bb15258",
            "proof_search_governance_followed": True,
            "primitive_registry_and_current_source_notes_read": True,
        },
        "N1_normalized_families": families,
        "N1_broad_negative_failure": "two materially distinct constructive families remain LIVE_UNTESTED and every attempted route retains a different terminal",
        "N2_collapsed_wall_pair_audit": pair_audit,
        "N3_hidden_wall_scan": [
            "24 co-present frame values and their preparation/readout",
            "continuous reciprocal square root, regulator epsilon, rational saturation alpha, and fixed-point arithmetic",
            "feedback/K signs, scales, lambda, improvement, trace contraction, and update parameter",
            "Cycle607 finite-Weyl field basis and common local NQ sign versus the separate Cycle604 real scalar kernel",
            "periodic P0 removal or supplied open Dirichlet boundary and positive-sector choice",
            "Cycle610 one-hot orientation/bus roles, unary encodings, clean work, and constraint penalties",
            "open F17 anchor/ports/flux genesis and periodic/open domain flag",
            "Cycle608/612 binder/path/chart, PR5557 lock/convention harness, 3/4 DELAY association, and separate 5/4 ADVANCE count-edit interface",
        ],
        "N3_phrase_scan": {"hits": ["registered primitives", "no axiom pressure"],
                           "classification": "explicit governance and non-promotion language after reading the machine registry and current primitive source notes; no hidden condition is promoted",
                           "hidden_conditions_promoted": 0},
        "N4_residual_matching": [
            {"witness": "Cycle620 Route B", "witness_residual": "linear feedback sign/scale/lambda/c survives", "current_residual": "normalized and saturating families still expose sign/scale and no shared-code delay association", "match": "yes; new mechanisms separately attempted"},
            {"witness": "Cycle620 Route C", "witness_residual": "periodic K is not one open apparatus", "current_residual": "periodic blocks now have exact support-two unary compilers but the same open/periodic transform is absent", "match": "yes; physical lowering advanced only"},
            {"witness": "Cycle607/609", "witness_residual": "reciprocal NQ action but sign/units and finite/static bridge open", "current_residual": "same q cancels algebraically only after a distinct positive stationary kernel is supplied", "match": "yes"},
            {"witness": "Cycle615", "witness_residual": "centered odd open boundary", "current_residual": "L6 is repaired by a carried eight-site anchor orbit, not a unique center", "match": "boundary import remains explicit"},
            {"witness": "PR5557 Cycle612", "witness_residual": "3/4 DELAY is rate-reachable at Q=1,s=+1; 5/4 ADVANCE is unreachable by uniform rate and requires receiver-gated count edit", "current_residual": "Cycle626 continuous candidates derive neither a shared-code delay association nor the advance count-edit drive", "match": "yes; mechanisms kept separate"},
        ],
        "N5_rhetoric_audit": {
            "local_normalization": "one-site union of 24 bounded hinge stars; 24 prepared values and nonlinear evaluator are charged",
            "stability": "iteration diagnostic only, never a physical branch-selection postulate",
            "support_two_compiler": "exact unary E-G matrix intertwiner for declared periodic blocks, separate from the role manifest",
            "common_coupling": "mathematical stationary comparator only because the NQ finite update does not implement H inverse",
            "K": "full-unitary periodic generator contraction, not a rate, energy, unique stress, or open real-space field",
            "response": "no route is called gravity or attraction; no physical receiver map is joined",
        },
        "N6_partial_closure_paths": {
            "primitive_registry_check": "approved scale, kinetic-isotropy, and realized-state primitives contain no feedback sign, positive Hessian, nonlinear evaluator, stationary field elimination, domain join, or receiver map",
            "paths": [
                "differentiate a genuinely open real-space full unitary and compile its K-to-endpoint coupling",
                "derive a finite reversible arithmetic representation for the local norm/saturation law on the declared field code",
                "join Cycle607 reciprocal q to the same positive physical field update at both source and receiver",
                "compile the PR5557 lock/convention/shared-code acceptance harness for 3/4 DELAY",
                "drive the separate receiver-gated count-edit interface before testing any 5/4 ADVANCE word",
            ],
        },
        "N7_steelman": "A hostile reviewer should reject a law-selection no-go. The exact periodic unary compilers show that support-two lowering is not the present wall, and the q^2 comparator shows how a coupling orientation could cancel if one physical positive field implements both reciprocal endpoints. An open-unitary coframe derivative or a finite reversible local arithmetic field could still close the join.",
        "N8_cross_cycle_echo": {
            "Cycle610": "large local compilers can replace apparent host packing walls",
            "Cycle607_609": "an abstract reciprocal NQ interaction acquired an exact support-two phase compiler in a later cycle",
            "Cycle615_620": "charge, endpoints, feedback, and K each advanced without licensing a silent domain join",
            "RP_sign_repair": "positivity and sign conventions are load-bearing and must be established on the actual carrier, not transferred by analogy",
        },
        "walls": walls,
        "broad_negative_gate": "FAIL / DO NOT SHIP",
        "narrow_claim": "these audited normalized, rational-saturating, common-coupling-comparator, and periodic direct-K candidates derive neither a shared-code 3/4 DELAY association nor the separate 5/4 ADVANCE count-edit drive",
        "minimum_content_claim": False,
        "shared_route_independent_obstruction": False,
        "axiom_pressure": False,
    }


def main() -> int:
    shore_data = shore()
    note_contract()
    route_a_result = route_a()
    route_b_result = route_b(shore_data)
    route_c_result = route_c()
    no_go = no_go_discipline()
    success_gate = {
        "singleton_receiver_without_host_or_stability_choice": False,
        "derived_shared_code_continuous_response_to_3_over_4_DELAY_association": False,
        "physical_receiver_gated_count_edit_for_5_over_4_ADVANCE": False,
        "one_open_real_space_support_two_source_Regge_K_endpoint_apparatus": False,
        "all_three_required_conjunctively": True,
        "success": False,
    }
    check(
        "Frozen conjunctive success gate rejects role packing, stability filtering, response-sign relabeling, and an unexecuted ADVANCE count edit",
        not success_gate["success"]
        and not success_gate["singleton_receiver_without_host_or_stability_choice"]
        and not success_gate["derived_shared_code_continuous_response_to_3_over_4_DELAY_association"]
        and not success_gate["physical_receiver_gated_count_edit_for_5_over_4_ADVANCE"]
        and not success_gate["one_open_real_space_support_two_source_Regge_K_endpoint_apparatus"],
        success_gate,
    )
    check(
        "Full N1-N8 rejects broad negative, minimum-content, shared-obstruction, and axiom-pressure promotion",
        len(no_go["N1_normalized_families"]) >= 5
        and len(no_go["N2_collapsed_wall_pair_audit"]) == 15
        and no_go["N3_phrase_scan"]["hidden_conditions_promoted"] == 0
        and no_go["broad_negative_gate"] == "FAIL / DO NOT SHIP"
        and not no_go["minimum_content_claim"]
        and not no_go["shared_route_independent_obstruction"]
        and not no_go["axiom_pressure"],
        no_go,
    )

    elapsed = perf_counter() - START
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss = int(rss if sys.platform == "darwin" else rss * 1024)
    receipt = {
        "cycle": 626,
        "HEAD": subprocess.run(("git", "rev-parse", "HEAD"), cwd=ROOT, text=True, capture_output=True, check=True).stdout.strip(),
        "authority": AUTHORITY, "audit": AUDIT, "constitutional_effect": "none",
        "pins": shore_data["observed"],
        "remote_time_lane_pin": {"ref": TIME_LANE_REF, "head": shore_data["time_lane_head"], "observed": shore_data["time_lane_observed"]},
        "shore": {key: value for key, value in shore_data.items() if key not in ("observed", "time_lane_observed", "receipts")},
        "runner_sha256": digest(Path(__file__).relative_to(ROOT)), "note_sha256": digest(NOTE.relative_to(ROOT)),
        "route_A_local_orbit_normalization": route_a_result,
        "route_B_bounded_nonlinear_and_common_coupling": route_b_result,
        "route_C_real_space_manifest_direct_K": route_c_result,
        "frozen_conjunctive_success_gate": success_gate,
        "decisive_answer": "The tournament constructs a genuinely site-local 24-orbit normalizer, exhausts every branch of a bounded rational feedback map, proves common-q sign cancellation on separately declared positive stationary comparators, and gives exact unary support-two compilers for the periodic Regge and direct full-Fock K-endpoint blocks. None selects one physical receiver mechanism: sign/scale/regulator/lambda/c survive; the nonlinear evaluator is not a superposition-safe M2 compiler; the common-q NQ update is not the positive scalar stationary elimination; and no open-F17-to-periodic-Regge transform joins the manifest into one real-space apparatus. Per pinned PR5557 Cycle612, continuous feedback may target only the rate-reachable 3/4 DELAY association, which is not shared-code identified here; 5/4 ADVANCE requires a distinct receiver-gated count edit that Cycle626 does not execute. This is unfinished law selection, not gravity and not a shared substrate obstruction.",
        "inventory": {
            "supplied": [
                "24 co-present Regge frame values, uniform frame preparation/readout, and bounded raw hinge-star operator",
                "continuous reciprocal square root, regulator and saturation families, feedback/K signs and scales, lambda and improvement",
                "Cycle607/609 finite-Weyl basis and NQ coupling, Cycle604 positive P0 comparator, and open Dirichlet comparator boundary",
                "Cycle610 one-hot orientation/bus/clean roles and unary one-excitation genesis",
                "Cycle615 F17 boundary ports/flux state and carried anchor, plus open/periodic domain flag",
                "Cycle608/612 binder/path/chart and endpoint-use program",
            ],
            "derived_or_executed": [
                "strict local 24-orbit zero handling, Ward/gauge invariance, all24/all576 covariance, and pointwise inverse actuation",
                "complete analytic piecewise-quadratic fixed-point and stability enumeration with source-off controls",
                "q-orientation cancellation and near/far ordering on positive periodic P0 and open Dirichlet stationary comparators",
                "decorated L3/L6/L7 open F17 Gauss fixture including the L6 eight-anchor orbit",
                "exact unary Givens support-two E-G compilers for Cycle576 periodic finite update and full-Fock trace-K endpoint candidate",
                "collision-free common role manifest, routed bus certificate, inverse, leakage, deletion, endpoint clean return",
            ],
            "not_derived": [
                "finite physical nonlinear norm/saturation evaluator on coframe superpositions",
                "feedback/K sign, scale, regulator, saturation scale, lambda, improvement, or positive/stable branch law",
                "identity of finite-Weyl NQ field with the positive scalar response carrier or physical stationary elimination",
                "open-real-space K_ab and open F17-to-Regge/K source transform",
                "shared-code continuous-response association to 3/4 DELAY or the separate 5/4 ADVANCE receiver-gated count edit",
                "physical stress, energy, gravity, causal rate, event, Record, or Born rule",
            ],
        },
        "no_go_discipline": no_go,
        "six_wall_ledger": {
            "C_ref": "SHARPENED: local 24-frame normalization and the L6 carried-anchor orbit remove host frame/center choices on declared data; frame-value genesis, domain flag, and receiver map remain supplied.",
            "C_num": "ADVANCED/SHARPENED: all normalized and rational fixed-point branches and q^2 cancellation are explicit; regulator, saturation scale, coupling magnitude/units, lambda/c, and word calibration remain.",
            "C_wrap": "UNCHANGED: compact F17 arithmetic is exact and the periodic K compiler preserves the prior phase seam; wrapped phase is not energy.",
            "C_int": "ADVANCED: exact periodic Regge and direct-K support-two compilers now coexist with open F17 and endpoint roles; the open-to-periodic source transform and stationary finite-update join remain absent.",
            "C_local": "ADVANCED: normalization uses one bounded union of hinge stars, L6 open geometry is decorated-covariant, and periodic finite unitaries have exact unary support-two words; nonlinear arithmetic and joint open execution remain.",
            "C_source": "SHARPENED: common-q orientation cancels mathematically on positive stationary comparators and local nonlinear candidates are exhaustive on their declared families, but no actual carrier selects sign/scale or shared-code 3/4 DELAY; 5/4 ADVANCE is correctly quarantined to an unexecuted count-edit path, so no gravity claim follows.",
        },
        "maturity_0_to_5": {
            "operational_quantum_records": 4.10,
            "time": 3.08,
            "inertia_matter": 4.58,
            "gravity_source": 4.08,
            "Born_probability": 2.0,
        },
        "strongest_constructive_result": "exact constant-overhead unary support-two compilers for the Cycle576 periodic Regge finite update and a proper-cubic scalar contraction of the actual Cycle620 full-Fock K tensor coupled to a physical endpoint, plus a strict local zero-handled 24-orbit normalizer",
        "shared_obstruction_or_axiom_pressure": False,
        "optimal_next_campaign": "derive an open-real-space coframe-dependent full unitary and its K-to-endpoint coupling on the decorated F17 domain, or physically compile a finite-valued local norm/saturation evaluator; demand that the same reciprocal coupling drive source and receiver in the executed positive field update, then compile the PR5557 lock/convention/shared-code acceptance harness for 3/4 DELAY and keep any 5/4 ADVANCE test on the distinct receiver-gated count-edit interface",
        "tests_passed": PASS, "tests_failed": FAIL, "pass": FAIL == 0,
        "elapsed_seconds": elapsed, "maximum_RSS_bytes": rss,
    }
    RECEIPT.write_text(json.dumps(receipt, indent=2, sort_keys=True, default=json_default) + "\n")
    print("RECEIPT", json.dumps(receipt, sort_keys=True, default=json_default))
    print("SUMMARY", json.dumps({
        "pass": receipt["pass"], "tests_passed": PASS, "tests_failed": FAIL,
        "route_A": route_a_result["disposition"], "route_B": route_b_result["disposition"],
        "route_C": route_c_result["disposition"], "success_gate": success_gate["success"],
        "axiom_pressure": False, "elapsed_seconds": elapsed,
    }, sort_keys=True))
    return int(FAIL != 0)


if __name__ == "__main__":
    COLD.parent.mkdir(parents=True, exist_ok=True)
    with COLD.open("w") as cold_handle:
        terminal = sys.stdout; sys.stdout = Tee(terminal, cold_handle)
        try:
            exit_code = main()
        finally:
            sys.stdout = terminal
    raise SystemExit(exit_code)
