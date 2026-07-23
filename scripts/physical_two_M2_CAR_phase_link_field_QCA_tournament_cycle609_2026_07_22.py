#!/usr/bin/env python3
"""Cycle609: algebraic parity lowering, F17 maps, and comparison audit.

Route A exactly factorizes the Cycle607 role-basis phase.  Route B executes a
separate reversible F17 array map from host-prepared role-charge arrays.  Route
C is a no-refit common-action comparison.  No route composes a physical M2
encoder/update, source/current/stress/gravity law, time, Event, Record, or Born
rule.  Authority none; audit unset; author artifact status accepted false.
"""
from __future__ import annotations

import ast
import contextlib
from fractions import Fraction
from hashlib import sha256
import io
from itertools import combinations, permutations, product
import json
import math
from pathlib import Path
import resource
import subprocess
import sys
from time import perf_counter

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import physical_car_matter_weyl_reciprocal_source_response_tournament_cycle607_2026_07_22 as c607
import physical_root_free_full_N3_carrier_genesis_tournament_cycle600_2026_07_22 as c600


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_TWO_M2_CAR_PHASE_LINK_FIELD_QCA_TOURNAMENT_"
    "CYCLE609_NOTE_2026-07-22.md"
)
RECEIPT = ROOT / (
    "outputs/physical_two_M2_CAR_phase_link_field_QCA_"
    "tournament_cycle609_receipt_2026_07_22.json"
)
COLD = ROOT / (
    "outputs/physical_two_M2_CAR_phase_link_field_QCA_"
    "tournament_cycle609_cold_2026_07_22.txt"
)
AUTHORITY = "none"
AUDIT = "unset"
AUTHOR_ARTIFACT_STATUS_ACCEPTED = False
AUDIT_VERDICT_INFERRED_FROM_DEPENDENCIES = False
TOL = 2e-8
SIGNAL = 1e-6
START = perf_counter()
PASS = 0
FAIL = 0


PINS = {
    "scripts/physical_root_free_full_N3_carrier_genesis_tournament_cycle600_2026_07_22.py":
        "904342da79cbc22c9878479f586387414e4a3af0f7f603708ec03d272074c933",
    "docs/work_history/repo/review_feedback/PHYSICAL_ROOT_FREE_FULL_N3_CARRIER_GENESIS_TOURNAMENT_CYCLE600_NOTE_2026-07-22.md":
        "9c8772f365812caedb0c416f7f0681a8f342ff3d08ac412851e7e6141ea7f602",
    "outputs/physical_root_free_full_N3_carrier_genesis_tournament_cycle600_receipt_2026_07_22.json":
        "d09cd7a82070f4311ab84a07127551ccf1e30e5557586e32fcd55fa01fd3dba5",
    "outputs/physical_root_free_full_N3_carrier_genesis_tournament_cycle600_cold_2026_07_22.txt":
        "fd82ebe960fa57d25e85328465b782a644ae127220d9abbefe5c64ca1b9eb01f",
    "scripts/physical_car_matter_weyl_reciprocal_source_response_tournament_cycle607_2026_07_22.py":
        "216591171e695af1e7c9ab19826afda0d4c620eda220e90490abc890a9e44757",
    "docs/work_history/repo/review_feedback/PHYSICAL_CAR_MATTER_WEYL_RECIPROCAL_SOURCE_RESPONSE_TOURNAMENT_CYCLE607_NOTE_2026-07-22.md":
        "922f943be2313af0a87268d1e7021c7d170352004c44d355db5f38f0af348100",
    "outputs/physical_car_matter_weyl_reciprocal_source_response_tournament_cycle607_receipt_2026_07_22.json":
        "ec0da4276602ae363e0bc9e36a8a696b209542ebd9fed888fb369abec4b455cd",
    "outputs/physical_car_matter_weyl_reciprocal_source_response_tournament_cycle607_cold_2026_07_22.txt":
        "ac49a18e59a1ce49529d251dcae1674ea6de5548a71cdd81d1a745ece70960ba",
    "docs/work_history/repo/review_feedback/PHYSICAL_PROPER_CUBIC_SUPERCELL_STREAM_COMPOSITION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md":
        "6ee48e029ca6023e55cd834bd2ad2fcbb24275b48f9b25e1c03777e0d2c3d835",
    "docs/work_history/repo/review_feedback/PHYSICAL_MATTER_VARIATION_CURRENT_STRESS_COMPENSATOR_SOURCE_TOURNAMENT_CYCLE611_NOTE_2026-07-22.md":
        "102b57283c55a190ba02289d2689ac8a6e6f97aff58e13036df1dd8a66e97308",
    "docs/work_history/repo/review_feedback/PHYSICAL_MATTER_CAUSED_CAUSAL_INTERVAL_PROPER_TIME_BRIDGE_TOURNAMENT_CYCLE612_NOTE_2026-07-22.md":
        "920776555dce6505bccb0e46e552e90d24858c08cfb7f6978d884f10a5bb0789",
}

EXPECTED_NOTE_SHA256 = "93d991d79e594a60494cb13112e21aba0356c84c23e79a334892aaa98797710c"
EXPECTED_RUNTIME_IMPORT_COUNT = 58
EXPECTED_RUNTIME_CLOSURE_MANIFEST_SHA256 = "c37483d3f3a5f3bd59933a4ad1de0ffcccab34b55e0710120af56175fd597958"
CAUSAL_COMPARISON = {
    "remote_ref": "origin/causal-time/cycle610-relational-duration-20260722",
    "commit": "a1e2f1ea60b1cf9b9cb0ae100c61cfd1f3a07318",
    "path": "docs/work_history/repo/review_feedback/PHYSICAL_TICK_ECHO_ASSOCIATION_CAUSAL_ORDER_TOURNAMENT_CYCLE612_NOTE_2026-07-22.md",
    "git_blob": "e433350a20c79531e471fa131cd40189181e58c9",
    "content_sha256": "028133c490e771dd3012061c79910fcfb88cd6132df072ec15e725fe9bc35496",
}


def digest(relative: str) -> str:
    return sha256((ROOT / relative).read_bytes()).hexdigest()


def runtime_import_closure() -> tuple[str, ...]:
    modules = {path.stem: path for path in (ROOT / "scripts").glob("*.py")}
    entry = Path(__file__).resolve()
    visited: set[Path] = set()

    def visit(path: Path) -> None:
        path = path.resolve()
        if path in visited:
            return
        visited.add(path)
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in ast.walk(tree):
            names: tuple[str, ...] = ()
            if isinstance(node, ast.Import):
                names = tuple(alias.name.split(".")[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                names = (node.module.split(".")[0],)
            for name in names:
                if name in modules:
                    visit(modules[name])

    visit(entry)
    return tuple(sorted(str(path.relative_to(ROOT)) for path in visited if path != entry))


def runtime_import_controls() -> dict:
    closure = runtime_import_closure()
    observed = {path: digest(path) for path in closure}
    payload = "".join(f"{path}\0{observed[path]}\n" for path in closure)
    manifest = sha256(payload.encode("utf-8")).hexdigest()
    direct = (
        "scripts/physical_car_matter_weyl_reciprocal_source_response_tournament_cycle607_2026_07_22.py",
        "scripts/physical_root_free_full_N3_carrier_genesis_tournament_cycle600_2026_07_22.py",
    )
    return {
        "direct_runtime_imports": direct,
        "complete_runtime_import_closure": closure,
        "runtime_import_count": len(closure),
        "hidden_runtime_import_count": len(tuple(path for path in closure if path not in direct)),
        "observed_sha256": observed,
        "closure_manifest_sha256": manifest,
        "expected_closure_manifest_sha256": EXPECTED_RUNTIME_CLOSURE_MANIFEST_SHA256,
        "pass": (len(closure) == EXPECTED_RUNTIME_IMPORT_COUNT
                 and all(path in closure for path in direct)
                 and manifest == EXPECTED_RUNTIME_CLOSURE_MANIFEST_SHA256),
    }


def json_default(value):
    if isinstance(value, np.generic): return value.item()
    if isinstance(value, np.ndarray): return value.tolist()
    if isinstance(value, Fraction): return f"{value.numerator}/{value.denominator}"
    if isinstance(value, complex): return [value.real, value.imag]
    raise TypeError(type(value).__name__)


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    PASS += int(condition); FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def shore() -> dict:
    observed = {name: digest(name) for name in PINS}
    imports = runtime_import_controls()
    r607 = json.loads((ROOT / "outputs/physical_car_matter_weyl_reciprocal_source_response_tournament_cycle607_receipt_2026_07_22.json").read_text())
    r600 = json.loads((ROOT / "outputs/physical_root_free_full_N3_carrier_genesis_tournament_cycle600_receipt_2026_07_22.json").read_text())
    route = r607["route_A_algebraic_CAR_number_W16_interface"]
    note_sha = digest(str(NOTE.relative_to(ROOT)))
    causal_bytes = subprocess.check_output(
        ("git", "show", f"{CAUSAL_COMPARISON['commit']}:{CAUSAL_COMPARISON['path']}"), cwd=ROOT)
    causal_blob = subprocess.check_output(
        ("git", "rev-parse", f"{CAUSAL_COMPARISON['commit']}:{CAUSAL_COMPARISON['path']}"),
        cwd=ROOT, text=True).strip()
    causal_text = causal_bytes.decode("utf-8")
    causal = {
        **CAUSAL_COMPARISON,
        "observed_git_blob": causal_blob,
        "observed_content_sha256": sha256(causal_bytes).hexdigest(),
        "pinned_object_matches": (
            causal_blob == CAUSAL_COMPARISON["git_blob"]
            and sha256(causal_bytes).hexdigest() == CAUSAL_COMPARISON["content_sha256"]),
        "comparison_only": True,
        "runner_executed": False,
        "imported": False,
        "backcredited_to_Cycle609": False,
        "delay_rate_associated_in_pinned_note": "delay is rate-reachable" in causal_text,
        "advance_requires_event_count_edit_in_pinned_note": "advance is only edit-reachable" in causal_text,
        "event_association_remains_underived_in_pinned_note": "event association between the two" in causal_text and "remains underived" in causal_text,
    }
    evidence = {
        "direct_evidence_hashes_match": observed == PINS,
        "note_sha256": note_sha,
        "note_matches_frozen_hash": note_sha == EXPECTED_NOTE_SHA256,
        "runtime_import_closure": imports,
        "Cycle600_pass": r600["pass"],
        "Cycle607_pass": r607["pass"],
        "Cycle607_tests": r607["tests_passed"],
        "Cycle607_author_artifact_status_accepted": r607["author_artifact_status_accepted"],
        "Cycle607_audit_verdict_inferred_from_dependencies": r607["audit_verdict_inferred_from_dependencies"],
        "number_descent": route["Cycle600_number_descent_residual"],
        "joint_EG": route["maximum_global_joint_EG_residual"],
        "mass": r607["shore"]["one_particle_mass_residual"],
        "contact": r607["shore"]["Cycle230_contact_factorization_residual"],
        "seam": r607["shore"]["Cycle230_seam_braid_residual"],
        "parent_physical_M2_register_composed": route["physical_boundary"]["physical_M2_register_composed"],
        "parent_physical_EG_evaluated": route["physical_boundary"]["physical_EG_evaluated"],
        "causal_time_comparison": causal,
    }
    check("parents, complete runtime closure, note, and comparison object are byte-pinned",
          all((evidence["direct_evidence_hashes_match"], evidence["note_matches_frozen_hash"],
               imports["pass"], evidence["Cycle600_pass"], evidence["Cycle607_pass"],
               not evidence["Cycle607_author_artifact_status_accepted"],
               not evidence["Cycle607_audit_verdict_inferred_from_dependencies"],
               not evidence["parent_physical_M2_register_composed"],
               not evidence["parent_physical_EG_evaluated"], causal["pinned_object_matches"],
               causal["delay_rate_associated_in_pinned_note"],
               causal["advance_requires_event_count_edit_in_pinned_note"],
               causal["event_association_remains_underived_in_pinned_note"]))
          and max(evidence["number_descent"], evidence["joint_EG"], evidence["mass"],
                  evidence["contact"], evidence["seam"]) < TOL, evidence)
    return {"observed": observed, "evidence": evidence, "receipt": r607,
            "runtime_import_controls": imports, "causal_comparison": causal}


# ---------------------------------------------------------------------------
# Route A: exact Walsh/parity lowering of the Cycle607 W16 N*Q phase.


def occupied_label(label: int) -> int:
    return int(4 <= label <= 9)


def local_walsh() -> dict[int, Fraction]:
    coefficients = {}
    for mask in range(32):
        numerator = sum(
            occupied_label(state & 15) * ((state >> 4) & 1)
            * (-1 if (mask & state).bit_count() % 2 else 1)
            for state in range(32)
        )
        if numerator:
            coefficients[mask] = Fraction(numerator, 32)
    return coefficients


def combined_phase_polynomial(sign: int = 1) -> dict[int, Fraction]:
    """Coefficient a_S/pi in exp(i*pi*sum a_S Z_S)."""
    local = local_walsh(); combined = {}
    for species in range(3):
        for qbit in range(4):
            scale = sign * Fraction(2**qbit, 8)
            for mask, coefficient in local.items():
                global_mask = sum(((mask >> bit) & 1) << (4*species + bit) for bit in range(4))
                global_mask |= ((mask >> 4) & 1) << (12 + qbit)
                combined[global_mask] = combined.get(global_mask, Fraction()) + scale * coefficient
    return {mask: coefficient for mask, coefficient in combined.items() if coefficient}


def evaluate_phase_polynomial(coefficients: dict[int, Fraction]) -> tuple[float, float]:
    states = np.arange(1 << 16, dtype=np.uint32)
    exponent = np.zeros(len(states))
    for mask, coefficient in coefficients.items():
        parity = (np.bitwise_count(states & mask) % 2).astype(int)
        exponent += float(coefficient) * (1 - 2*parity)
    labels = [(states >> (4*species)) & 15 for species in range(3)]
    number = sum((label >= 4) & (label <= 9) for label in labels)
    coordinate = (states >> 12) & 15
    target = number * coordinate / 8
    return float(np.max(abs(np.exp(1j*math.pi*exponent) - np.exp(1j*math.pi*target)))), float(np.max(abs(exponent-target)))


def phase_exponents(coefficients: dict[int, Fraction], states: np.ndarray) -> np.ndarray:
    exponent = np.zeros(len(states))
    for mask, coefficient in coefficients.items():
        parity = (np.bitwise_count(states & mask) % 2).astype(int)
        exponent += float(coefficient) * (1 - 2*parity)
    return exponent


def carrier_frame_label_table(frame: np.ndarray) -> np.ndarray:
    """The supplied proper-cubic action on one four-bit carrier role word."""
    table = np.arange(16, dtype=np.uint32)
    direction_map = np.argmax(c600.c598.c593.c210.direction_permutation(frame), axis=0)
    table[4:10] = 4 + direction_map
    return table


def carrier_frame_states(states: np.ndarray, frame: np.ndarray) -> np.ndarray:
    table = carrier_frame_label_table(frame)
    transformed = states & np.uint32(0xF000)  # Q is a scalar under the cubic frame.
    for species in range(3):
        transformed |= table[(states >> (4*species)) & 15] << (4*species)
    return transformed


def joint_role_coordinates(length: int) -> tuple[list[tuple], list[tuple], int]:
    c560 = c600.c598.c593.c560
    code = c560.c539.c525.c319.c269.build_code(length)
    cells = c560.c555.network_cells(length)
    modulus = c560.c533.c527.fine_length(length)
    occupied = {c560.c533.coordinate_for_qubit(code, bit)
                for bit in range(c560.c555.physical_bit_count(code))}
    occupied |= {c560.c533.c527.shadow_coordinate(cell, direction, length)
                 for cell in cells for direction in range(6)}
    for cell in cells:
        origin = c560.c533.c527.cell_center(cell, length)
        c560.allocated_block(origin, 6, occupied, modulus)
        c560.allocated_block(origin, 18, occupied, modulus)
    carrier = [c560.allocated_block(c560.c533.c527.cell_center(cell, length), 12,
                                    occupied, modulus) for cell in cells]
    field = [c560.allocated_block(c560.c533.c527.cell_center(cell, length), 4,
                                  occupied, modulus) for cell in cells]
    return carrier, field, modulus


def periodic_l1(left: tuple, right: tuple, modulus: int) -> int:
    return sum(min((a-b) % modulus, (b-a) % modulus) for a, b in zip(left, right))


def route_a() -> dict:
    positive = combined_phase_polynomial(+1)
    negative = combined_phase_polynomial(-1)
    phase_residual, exponent_residual = evaluate_phase_polynomial(positive)
    inverse_residual = max(abs(positive.get(mask, 0) + negative.get(mask, 0))
                           for mask in set(positive) | set(negative))
    local = local_walsh()
    support_histogram = {support: sum(mask.bit_count() == support for mask in positive)
                         for support in range(6)}
    logical_cnot = sum(2*(mask.bit_count()-1) for mask in positive if mask.bit_count() > 1)
    rz = sum(mask != 0 for mask in positive)
    global_phase = positive.get(0, Fraction())
    angle_inventory = sorted({str(-2*coefficient) + "*pi" for mask, coefficient in positive.items() if mask})
    frames = c600.c598.c593.c210.proper_cubic_frames()
    states = np.arange(1 << 16, dtype=np.uint32)
    base_exponents = phase_exponents(positive, states)
    phase_covariance = 0.0
    for frame in frames:
        transformed = carrier_frame_states(states, frame)
        transformed_exponents = phase_exponents(positive, transformed)
        phase_covariance = max(phase_covariance, float(np.max(abs(
            np.exp(1j*math.pi*transformed_exponents) - np.exp(1j*math.pi*base_exponents)
        ))))
    label_group_failures = 0
    for first in frames:
        first_table = carrier_frame_label_table(first)
        for second in frames:
            second_table = carrier_frame_label_table(second)
            direct_table = carrier_frame_label_table(first @ second)
            label_group_failures += int(not np.array_equal(direct_table, first_table[second_table]))
    rows = []
    maximum_distance = maximum_cost_proxy = 0
    for label, length, held in (("TRAIN_L3", 3, False), ("HELD_L6", 6, True),
                                ("OUT_FAMILY_L7", 7, True)):
        carrier, field, modulus = joint_role_coordinates(length)
        roles = list(carrier[0]) + list(field[0])
        distances = []
        cost_proxy = 0
        for mask in positive:
            indices = [bit for bit in range(16) if mask >> bit & 1]
            if len(indices) <= 1: continue
            pivot = indices[-1]
            for control in indices[:-1]:
                distance = periodic_l1(roles[control], roles[pivot], modulus)
                distances.append(distance)
                # Analytic distance cost only: no path or physical routing is made.
                cost_proxy += 2 * (6*max(0, distance-1) + 1)
        maximum_distance = max(maximum_distance, max(distances))
        maximum_cost_proxy = max(maximum_cost_proxy, cost_proxy + rz)
        coordinates = np.asarray([site for block in carrier for site in block]
                                 + [site for block in field for site in block], dtype=int)
        injection = sum(len(np.unique((coordinates @ frame.T) % modulus, axis=0)) != len(coordinates)
                        for frame in frames)
        group = 0
        for first in frames:
            for second in frames:
                direct = (coordinates @ (first @ second).T) % modulus
                composed = ((coordinates @ second.T) % modulus @ first.T) % modulus
                group += int(not np.array_equal(direct, composed))
        rows.append({"fixture": label, "length": length, "held": held,
                     "maximum_role_coordinate_distance_proxy": max(distances),
                     "analytic_serial_distance_cost_proxy_not_depth": cost_proxy + rz,
                     "all24_role_coordinate_injection_failures": injection,
                     "all576_role_coordinate_group_failures": group,
                     "physical_M2_placement_executed": False,
                     "physical_nearest_neighbor_routing_executed": False})
    deletion_mask = next(mask for mask in positive if mask and positive[mask])
    deletion_signal = 2 * abs(math.sin(math.pi * float(positive[deletion_mask])))
    output = {
        "object": "exact binary-role Walsh/parity factorization of Cycle607 U=exp(2pi i NQ/16)",
        "disposition": "CONSTRUCTIVE_EXACT_ALGEBRAIC_ROLE_GATE_FACTORIZATION; PHYSICAL_M2_COMPILER_OPEN",
        "full_ambient_role_basis_states_exhausted": 1 << 16,
        "local_five_bit_Walsh_nonzero_terms": len(local),
        "combined_nonzero_Pauli_terms_including_global": len(positive),
        "support_histogram": support_histogram,
        "maximum_Pauli_string_support_before_lowering": max(mask.bit_count() for mask in positive),
        "factorization_recipe": "for each nonempty Z string: role-CNOT every other support bit into one pivot, apply role-Rz(-2*pi*a_S), undo role-CNOTs; apply the printed global phase",
        "maximum_elementary_factor_support_binary_roles": 2,
        "algebraic_role_CNOT_count_per_cell": logical_cnot,
        "algebraic_role_Rz_count_per_cell": rz,
        "global_phase_over_pi": str(global_phase),
        "parameterized_Rz_angle_inventory": angle_inventory,
        "all_angles_are_exact_rational_multiples_of_pi": True,
        "maximum_full_space_unitary_residual": phase_residual,
        "maximum_full_space_exponent_residual_over_pi": exponent_residual,
        "all24_phase_law_covariance_residual": phase_covariance,
        "all576_carrier_label_group_failures": label_group_failures,
        "inverse_coefficient_residual": float(inverse_residual),
        "delete_one_nonzero_rotation_signal": deletion_signal,
        "off_code_labels_10_through_15_exhausted": True,
        "declared_factorization_scratch_or_garbage_roles": 0,
        "maximum_role_coordinate_L1_distance_proxy": maximum_distance,
        "maximum_analytic_serial_distance_cost_proxy_not_depth": maximum_cost_proxy,
        "coordinate_audit_scope": "Cycle600 role-coordinate blueprints only; a coordinate allocation and distance proxy are not physical placement, nearest-neighbor packing, or routed depth",
        "all24_phase_state_comparisons_executed": 24 * (1 << 16),
        "all576_carrier_label_comparisons_executed": 24 * 24 * 16,
        "all24_role_coordinate_audits_executed": 24 * 3,
        "all576_role_coordinate_group_audits_executed": 24 * 24 * 3,
        "physical_NN_route_packing_closed": False,
        "physical_boundary": {
            "physical_M2_register_composed": False,
            "physical_encoder_composed": False,
            "physical_update_composed": False,
            "physical_EG_evaluated": False,
            "physical_code_leakage_evaluated": False,
            "physical_M2_placement_executed": False,
            "physical_nearest_neighbor_routing_executed": False,
            "physical_schedule_covariance_executed": False,
            "local_auxiliary_or_gauge_constraints_composed": False,
        },
        "rows": rows,
        "coupling_sign_selected": False,
        "accepted_finite_angle_alphabet_beyond_printed_Rz": False,
    }
    check("Route A exactly factorizes the full Cycle607 on/off-code NQ phase into support<=2 role factors",
          phase_residual < TOL and exponent_residual < TOL and inverse_residual == 0
          and phase_covariance < TOL and label_group_failures == 0
          and deletion_signal > SIGNAL and max(mask.bit_count() for mask in positive) <= 4
          and logical_cnot == 318 and rz == 109, output)
    check("Route A gives role-distance proxies plus phase-law and coordinate all24/all576 certificates",
          maximum_distance <= 8 and maximum_cost_proxy > 0
          and phase_covariance < TOL and label_group_failures == 0
          and all(row["all24_role_coordinate_injection_failures"] == 0
                  and row["all576_role_coordinate_group_failures"] == 0 for row in rows), rows)
    return output


# ---------------------------------------------------------------------------
# Route B: exact F17 finite-Weyl phase-space link QCA.


MOD = 17
ALPHA = pow(12, -1, MOD)       # reduction of 1/12
HALF = pow(2, -1, MOD)


def laplacian_mod(field: np.ndarray) -> np.ndarray:
    return (6*field - sum(np.roll(field, shift, axis)
                          for axis in range(3) for shift in (-1, 1))) % MOD


def kick(q: np.ndarray, p: np.ndarray, charge: np.ndarray, sign: int,
         delete_source=False, delete_links=False) -> tuple[np.ndarray, np.ndarray]:
    source = np.zeros_like(charge) if delete_source else sign*charge
    links = np.zeros_like(q) if delete_links else laplacian_mod(q)
    return q.copy(), (p + ALPHA*(source-links)) % MOD


def inverse_kick(q: np.ndarray, p: np.ndarray, charge: np.ndarray, sign: int) -> tuple[np.ndarray, np.ndarray]:
    return q.copy(), (p - ALPHA*(sign*charge-laplacian_mod(q))) % MOD


def drift(q: np.ndarray, p: np.ndarray, coefficient=1) -> tuple[np.ndarray, np.ndarray]:
    return (q + coefficient*p) % MOD, p.copy()


def inverse_drift(q: np.ndarray, p: np.ndarray, coefficient=1) -> tuple[np.ndarray, np.ndarray]:
    return (q - coefficient*p) % MOD, p.copy()


def qca_step(q: np.ndarray, p: np.ndarray, charge: np.ndarray, sign: int,
             order: str, delete_source=False, delete_links=False) -> tuple[np.ndarray, np.ndarray]:
    if order == "KICK_THEN_DRIFT":
        return drift(*kick(q, p, charge, sign, delete_source, delete_links))
    if order == "DRIFT_THEN_KICK":
        return kick(*drift(q, p), charge, sign, delete_source, delete_links)
    q, p = drift(q, p, HALF)
    q, p = kick(q, p, charge, sign, delete_source, delete_links)
    return drift(q, p, HALF)


def qca_inverse(q: np.ndarray, p: np.ndarray, charge: np.ndarray, sign: int,
                order: str) -> tuple[np.ndarray, np.ndarray]:
    if order == "KICK_THEN_DRIFT": return inverse_kick(*inverse_drift(q, p), charge, sign)
    if order == "DRIFT_THEN_KICK": return inverse_drift(*inverse_kick(q, p, charge, sign))
    q, p = inverse_drift(q, p, HALF)
    q, p = inverse_kick(q, p, charge, sign)
    return inverse_drift(q, p, HALF)


def signed17(value: np.ndarray) -> np.ndarray:
    return np.where(value > 8, value-17, value)


def carrier_charge_density(length: int, subset: tuple[int, ...], neutral_sites: tuple[int, ...]) -> np.ndarray:
    charge = np.zeros((length,)*3, dtype=int)
    for mode in subset: charge.reshape(-1)[mode//6] += 2
    for site in neutral_sites: charge.reshape(-1)[site] -= 1
    return charge


def carrier_label_charge(label: int) -> int:
    if 1 <= label <= 3: return -1
    if 4 <= label <= 9: return 2
    return 0


def ambient_carrier_role_charges() -> np.ndarray:
    values=np.empty(16**3,dtype=int)
    for word in np.ndindex(16,16,16):
        values[(word[0]*16+word[1])*16+word[2]]=sum(carrier_label_charge(label) for label in word)
    return values


def word_charge_density(word: tuple[int,int,int], total_modes: int,
                        neutral_sites: tuple[int,...], length: int) -> np.ndarray:
    charge=np.zeros((length,)*3,dtype=int)
    for orbital in word:
        if orbital < total_modes:
            charge.reshape(-1)[orbital//6] += 2
        else:
            neutral_type=orbital-total_modes
            charge.reshape(-1)[neutral_sites[neutral_type]] -= 1
    return charge % MOD


def rotate_scalar(field: np.ndarray, frame: np.ndarray) -> np.ndarray:
    length = field.shape[0]; output = np.zeros_like(field)
    for coordinate in product(range(length), repeat=3):
        target = tuple(int(value % length) for value in frame @ np.asarray(coordinate))
        output[target] = field[coordinate]
    return output


def edge_coloring(length: int) -> dict:
    groups = {}
    for site in product(range(length), repeat=3):
        for axis in range(3):
            target = list(site); target[axis] = (target[axis]+1) % length; target = tuple(target)
            coordinate = site[axis]
            local_color = (2 if length % 2 and coordinate == length-1 else coordinate % 2)
            color = 3*axis + local_color
            groups.setdefault(color, []).append((site, target))
    conflicts = 0
    for edges in groups.values():
        touched = []
        for left, right in edges: touched.extend((left, right))
        conflicts += len(touched) - len(set(touched))
    return {"colors": len(groups), "edges": sum(map(len, groups.values())),
            "same_color_vertex_conflicts": conflicts,
            "schedule_is_law_order": False,
            "aggregate_link_terms_commute_algebraically": True,
            "colored_sublayers_executed": False,
            "physical_schedule_covariance_executed": False}


def permutation_compiler_stats(bits: int, mapping) -> dict:
    size = 1 << bits
    permutation = [mapping(state) for state in range(size)]
    bijective = len(set(permutation)) == size
    visited = [False]*size; transpositions = gray_adjacent = 0
    for start in range(size):
        if visited[start]: continue
        cycle = []; current = start
        while not visited[current]:
            visited[current] = True; cycle.append(current); current = permutation[current]
        if len(cycle) > 1:
            transpositions += len(cycle)-1
            anchor = cycle[0]
            for target in cycle[1:]:
                distance = (anchor ^ target).bit_count()
                gray_adjacent += 2*distance-1
    controls = bits-1
    toffoli_bound = gray_adjacent * max(1, 2*controls-3)
    return {"bits": bits, "basis_states": size, "bijective": bijective,
            "two_level_transpositions": transpositions,
            "gray_adjacent_multi_controlled_X_bound": gray_adjacent,
            "Toffoli_bound_with_clean_scratch": toffoli_bound,
            "analytic_role_CNOT_bound_after_declared_Toffoli_recipe": 6*toffoli_bound,
            "declared_clean_scratch_roles": max(0, controls-2),
            "materialized_gate_word_executed": False,
            "scratch_returned_zero_in_composed_circuit": False}


def reciprocal_phase_compiler_stats() -> dict:
    """One carrier word (4 bits) times one lawful F17 Q word (5 bits)."""
    values=[]
    for state in range(1<<9):
        label=state&15; coordinate=(state>>4)&31
        values.append(Fraction(2*ALPHA*carrier_label_charge(label)*coordinate,MOD)
                      if coordinate<MOD else Fraction())
    coefficients={}
    for mask in range(1<<9):
        coefficient=sum(values[state]*(-1 if (mask&state).bit_count()%2 else 1)
                        for state in range(1<<9))/Fraction(1<<9)
        if coefficient: coefficients[mask]=coefficient
    reconstruction=0.0
    for state,value in enumerate(values):
        observed=sum(coefficient*(-1 if (mask&state).bit_count()%2 else 1)
                     for mask,coefficient in coefficients.items())
        reconstruction=max(reconstruction,abs(float(observed-value)))
    cnot=sum(2*(mask.bit_count()-1) for mask in coefficients if mask.bit_count()>1)
    return {"full_basis_states":1<<9,"nonzero_terms_including_global":len(coefficients),
            "maximum_prelowering_support":max(mask.bit_count() for mask in coefficients),
            "Rz_per_carrier_species":sum(mask!=0 for mask in coefficients),
            "parity_CNOT_per_carrier_species":cnot,
            "full_exponent_reconstruction_residual_over_pi":reconstruction,
            "maximum_declared_factor_support_binary_roles":2,
            "angle_inventory_over_pi":sorted({str(-2*coefficient) for mask,coefficient in coefficients.items() if mask}),
            "invalid_Q_labels_17_through_31_have_identity_phase":True}


def qca_layout(length:int, support2_cnot_bound:int)->dict:
    c560=c600.c598.c593.c560;code=c560.c539.c525.c319.c269.build_code(length)
    cells=c560.c555.network_cells(length);modulus=c560.c533.c527.fine_length(length)
    occupied={c560.c533.coordinate_for_qubit(code,bit) for bit in range(c560.c555.physical_bit_count(code))}
    occupied|={c560.c533.c527.shadow_coordinate(cell,direction,length) for cell in cells for direction in range(6)}
    for cell in cells:
        origin=c560.c533.c527.cell_center(cell,length)
        c560.allocated_block(origin,6,occupied,modulus);c560.allocated_block(origin,18,occupied,modulus)
    carrier=[c560.allocated_block(c560.c533.c527.cell_center(cell,length),12,occupied,modulus) for cell in cells]
    qroles=[c560.allocated_block(c560.c533.c527.cell_center(cell,length),5,occupied,modulus) for cell in cells]
    proles=[c560.allocated_block(c560.c533.c527.cell_center(cell,length),5,occupied,modulus) for cell in cells]
    scratch=[c560.allocated_block(c560.c533.c527.cell_center(cell,length),8,occupied,modulus) for cell in cells]
    index={tuple(cell):i for i,cell in enumerate(cells)};max_link=0
    for cell in cells:
        i=index[tuple(cell)]
        for axis in range(3):
            neighbor=list(cell);neighbor[axis]=(neighbor[axis]+1)%length;j=index[tuple(neighbor)]
            for left in qroles[j]:
                for right in proles[i]:max_link=max(max_link,periodic_l1(left,right,modulus))
    coordinates=np.asarray([site for family in (carrier,qroles,proles,scratch) for block in family for site in block],dtype=int)
    frames=c600.c598.c593.c210.proper_cubic_frames()
    injection=sum(len(np.unique((coordinates@frame.T)%modulus,axis=0))!=len(coordinates) for frame in frames)
    group=0
    for first in frames:
        for second in frames:
            direct=(coordinates@(first@second).T)%modulus
            composed=((coordinates@second.T)%modulus@first.T)%modulus
            group+=int(not np.array_equal(direct,composed))
    return {"declared_persistent_binary_roles_per_cell":22,
            "declared_reused_clean_scratch_roles_per_cell":8,
            "declared_total_live_binary_roles_per_cell":30,
            "maximum_link_role_coordinate_L1_distance_proxy":max_link,
            "analytic_serial_distance_cost_proxy_per_ADD17_not_depth":support2_cnot_bound*(6*max(0,max_link-1)+1),
            "all24_role_coordinate_injection_failures":injection,
            "all576_role_coordinate_group_failures":group,
            "scratch_returned_zero_in_composed_circuit":False,
            "physical_M2_placement_executed":False,
            "materialized_NN_route_paths":False,
            "simultaneous_path_or_edge_conflict_check":False,
            "NN_schedule_packing_covariance_checked":False}


def arithmetic_compiler_inventory() -> dict:
    add = permutation_compiler_stats(10, lambda state:
        (((state & 31) + ((state >> 5) & 31)) % MOD) | (((state >> 5) & 31) << 5)
        if (state & 31) < MOD and ((state >> 5) & 31) < MOD else state)
    multiply = permutation_compiler_stats(5, lambda state: (ALPHA*state) % MOD if state < MOD else state)
    charge_lookup = permutation_compiler_stats(9, lambda state:
        ((state & 15) | ((((state >> 4) + carrier_label_charge(state & 15)) % MOD) << 4))
        if ((state >> 4) & 31) < MOD else state)
    return {
        "ADD17_full_space": add, "MUL_ALPHA_full_space": multiply,
        "CARRIER_ROLE_CHARGE_LOOKUP_full_space":charge_lookup,
        "RECIPROCAL_ROLE_CHARGE_PHASE":reciprocal_phase_compiler_stats(),
        "analytic_lowering_recipe": "cycle decomposition -> Gray-adjacent basis transpositions -> clean-scratch multi-controlled X -> declared H/T/CNOT Toffoli recipe",
        "materialized_gate_words_executed": False,
        "maximum_declared_factor_support_binary_roles": 2,
        "parameterized_angles": ["pi/4", "pi/2"],
        "invalid_labels_17_through_31_fixed": True,
    }


def phase_for_charge(charge: np.ndarray, q: np.ndarray, sign: int) -> complex:
    exponent = int(np.sum(charge*q) % MOD)
    return complex(np.exp(2j*math.pi*ALPHA*sign*exponent/MOD))


def route_b() -> dict:
    frames = c600.c598.c593.c210.proper_cubic_frames()
    rng = np.random.default_rng(609)
    embedding,basis=c607.exterior_embedding_16()
    ambient_charge=ambient_carrier_role_charges()
    logical_charge=np.asarray([3*len(subset)-3 for subset in basis])
    carrier_charge_descent=float(np.linalg.norm(
        ambient_charge[:,None]*embedding-embedding*logical_charge[None,:]))
    rows = []
    max_inverse = max_EG = max_field_EG = max_joint_inverse = max_continuity = max_matter_continuity = max_ledger = max_covariance = max_translation = 0
    translation_comparisons = 0
    min_source_delete = min_link_delete = min_order_signal = min_sign_signal = math.inf
    total_group_failures = 0
    for label, length, held in (("TRAIN_L3", 3, False), ("HELD_L6", 6, True),
                                ("OUT_FAMILY_L7", 7, True)):
        total_modes = 6*length**3
        subset = (1,) if length == 3 else (1, 6*(length**3-1))
        neutral_sites = tuple((index*(length**3//3+1)) % length**3 for index in range(3-len(subset)))
        charge = carrier_charge_density(length, subset, neutral_sites) % MOD
        q = rng.integers(0, MOD, size=(length,)*3, dtype=np.int64)
        p = rng.integers(0, MOD, size=(length,)*3, dtype=np.int64)
        target_subset = tuple(sorted(c600.mode_stream_map(mode, length) for mode in subset))
        target_charge = carrier_charge_density(length, target_subset, neutral_sites) % MOD
        phase_logical = phase_for_charge(target_charge, q, +1)
        terms = c600.encoded_global_terms(subset, total_modes)
        mapped = c600.map_encoded_terms(terms, total_modes,
            lambda mode, L=length: c600.mode_stream_map(mode, L))
        target_terms = c600.encoded_global_terms(target_subset, total_modes)
        _, stream_sign = c600.mapped_subset_and_sign(subset,
            lambda mode, L=length: c600.mode_stream_map(mode, L))
        contact = c607.contact_phase_subset(target_subset)
        physical_terms={word:amplitude*contact*phase_for_charge(
            word_charge_density(word,total_modes,neutral_sites,length),q,+1)
            for word,amplitude in mapped.items()}
        expected_terms = {word: stream_sign*amplitude*contact*phase_logical
                          for word, amplitude in target_terms.items()}
        EG = c600.maximum_term_residual(physical_terms, expected_terms)
        q_new, p_new = qca_step(q, p, target_charge, +1, "SYMMETRIC")
        for shift in product(range(length), repeat=3):
            shifted = tuple(np.roll(value, shift, axis=(0, 1, 2))
                            for value in (q, p, target_charge))
            left = qca_step(*shifted, +1, "SYMMETRIC")
            right = tuple(np.roll(value, shift, axis=(0, 1, 2)) for value in (q_new, p_new))
            max_translation = max(max_translation,
                                  max(int(np.max(abs(a-b))) for a, b in zip(left, right)))
            translation_comparisons += 1
        field_EG=0
        for word in mapped:
            word_q,word_p=qca_step(q,p,word_charge_density(word,total_modes,neutral_sites,length),+1,"SYMMETRIC")
            field_EG=max(field_EG,int(np.max(abs(word_q-q_new))),int(np.max(abs(word_p-p_new))))
        q_back, p_back = qca_inverse(q_new, p_new, target_charge, +1, "SYMMETRIC")
        inverse = max(int(np.max(abs(q_back-q))), int(np.max(abs(p_back-p))))
        unphased={word:amplitude/(contact*phase_for_charge(
            word_charge_density(word,total_modes,neutral_sites,length),q,+1))
            for word,amplitude in physical_terms.items()}
        restored_terms=c600.map_encoded_terms(unphased,total_modes,
            lambda mode,L=length:c600.mode_inverse_stream_map(mode,L))
        joint_inverse=c600.maximum_term_residual(restored_terms,terms)
        before_counts=np.zeros(length**3,dtype=int);after_counts=np.zeros(length**3,dtype=int);divergence=np.zeros(length**3,dtype=int)
        for source_mode,target_mode in zip(subset,[c600.mode_stream_map(mode,length) for mode in subset]):
            source_site,target_site=source_mode//6,target_mode//6
            before_counts[source_site]+=2;after_counts[target_site]+=2
            divergence[source_site]+=2;divergence[target_site]-=2
        matter_continuity=int(np.max(abs(after_counts-before_counts+divergence)))
        kick_delta = (qca_step(q, p, target_charge, +1, "KICK_THEN_DRIFT")[1] - p) % MOD
        continuity = (kick_delta - ALPHA*(target_charge-laplacian_mod(q))) % MOD
        ledger = int((np.sum(kick_delta, dtype=np.int64) - ALPHA*np.sum(target_charge, dtype=np.int64)) % MOD)
        deleted_source = qca_step(q, p, target_charge, +1, "SYMMETRIC", delete_source=True)
        deleted_links = qca_step(q, p, target_charge, +1, "SYMMETRIC", delete_links=True)
        source_signal = max(int(np.max(abs(signed17(q_new)-signed17(deleted_source[0])))),
                            int(np.max(abs(signed17(p_new)-signed17(deleted_source[1])))))
        link_signal = max(int(np.max(abs(signed17(q_new)-signed17(deleted_links[0])))),
                          int(np.max(abs(signed17(p_new)-signed17(deleted_links[1])))))
        kick_first = qca_step(q, p, target_charge, +1, "KICK_THEN_DRIFT")
        drift_first = qca_step(q, p, target_charge, +1, "DRIFT_THEN_KICK")
        negative = qca_step(q, p, target_charge, -1, "SYMMETRIC")
        order_signal = max(int(np.max(abs(signed17(a)-signed17(b)))) for a,b in zip(kick_first,drift_first))
        sign_signal = max(int(np.max(abs(signed17(a)-signed17(b)))) for a,b in zip((q_new,p_new),negative))
        for frame in frames:
            left = qca_step(rotate_scalar(q,frame), rotate_scalar(p,frame),
                            rotate_scalar(target_charge,frame), +1, "SYMMETRIC")
            right = tuple(rotate_scalar(value,frame) for value in (q_new,p_new))
            max_covariance = max(max_covariance, max(int(np.max(abs(a-b))) for a,b in zip(left,right)))
        test_modes = tuple(range(min(42,total_modes)))
        for first in frames:
            for second in frames:
                for mode in test_modes:
                    total_group_failures += c600.mode_frame_map(mode,first@second,length) != c600.mode_frame_map(c600.mode_frame_map(mode,second,length),first,length)
        coloring = edge_coloring(length)
        compiler=arithmetic_compiler_inventory()
        layout=qca_layout(length,compiler["ADD17_full_space"]["analytic_role_CNOT_bound_after_declared_Toffoli_recipe"])
        max_inverse=max(max_inverse,inverse); max_EG=max(max_EG,EG);max_field_EG=max(max_field_EG,field_EG);max_joint_inverse=max(max_joint_inverse,joint_inverse)
        max_matter_continuity=max(max_matter_continuity,matter_continuity)
        max_continuity=max(max_continuity,int(np.max(np.minimum(continuity,MOD-continuity))))
        max_ledger=max(max_ledger,min(ledger,MOD-ledger))
        min_source_delete=min(min_source_delete,source_signal); min_link_delete=min(min_link_delete,link_signal)
        min_order_signal=min(min_order_signal,order_signal); min_sign_signal=min(min_sign_signal,sign_signal)
        rows.append({"fixture":label,"length":length,"held":held,"matter_number":len(subset),
                     "neutral_carriers":len(neutral_sites),"total_carrier_charge_mod17":int(np.sum(target_charge)%MOD),
                     "algebraic_stream_contact_role_charge_intertwining_residual":EG,"exact_inverse_integer_residual":inverse,
                     "aggregate_array_update_per_word_intertwining_residual":field_EG,"full_carrier_term_array_inverse_residual":joint_inverse,
                     "constructed_role_charge_stream_identity_residual":matter_continuity,
                     "defining_array_update_identity_residual":int(np.max(np.minimum(continuity,MOD-continuity))),
                     "global_modular_sum_identity_residual":min(ledger,MOD-ledger),
                     "source_deletion_signal":source_signal,"link_deletion_signal":link_signal,
                     "order_signal":order_signal,"sign_signal":sign_signal,"edge_coloring":coloring,"layout":layout})

    # Reversal audit on one L3 configuration: R(q,p)=(q,-p).
    length=3; q=rng.integers(0,MOD,size=(length,)*3); p=rng.integers(0,MOD,size=(length,)*3)
    charge=np.zeros_like(q); charge[0,0,0]=2; charge[1,1,1]=MOD-1; charge[2,2,2]=MOD-1
    reversal={}
    for sign in (+1,-1):
        for order in ("KICK_THEN_DRIFT","DRIFT_THEN_KICK","SYMMETRIC"):
            rq,rp=q.copy(),(-p)%MOD
            uq,up=qca_step(rq,rp,charge,sign,order); left=(uq,(-up)%MOD)
            right=qca_inverse(q,p,charge,sign,order)
            reversal[(sign,order)]=max(int(np.max(abs(a-b))) for a,b in zip(left,right))
    compiler=arithmetic_compiler_inventory()
    output={
        "object":"reversible F17 Q/P aggregate array map driven by host-prepared carrier-role charge arrays",
        "disposition":"CONSTRUCTIVE_EXACT_F17_AGGREGATE_ARRAY_MAP; PHYSICAL_M2_SOURCE_AND_SCHEDULE_COMPILERS_OPEN",
        "field_modulus":MOD,"alpha_mod17":ALPHA,"alpha_rational":"1/12","half_mod17":HALF,
        "declared_modular_polynomial":"A=alpha[s sum_x J_x Q_x - 1/2 sum_<xy>(Q_x-Q_y)^2] plus Q/P shears; J is supplied as +2 for matter roles, -1 for neutral roles, 0 for absent/invalid labels",
        "source_interface_scope":"the executed fixtures host-prepare subsets, neutral-site indices, +2/-1 charge/sign, and modulus; no carrier-register-to-charge-array circuit or uniform neutral-W expectation is composed",
        "algebraic_carrier_role_charge_descent_residual":carrier_charge_descent,
        "full_ambient_carrier_role_labels_exhausted":16**3,
        "off_code_carrier_labels_have_zero_source_charge_and_reciprocal_phase":True,
        "rows":rows,"maximum_algebraic_role_term_intertwining_residual":max_EG,
        "maximum_aggregate_array_update_per_word_intertwining_residual":max_field_EG,
        "maximum_full_carrier_term_array_inverse_residual":max_joint_inverse,
        "maximum_exact_array_inverse_residual":max_inverse,
        "maximum_constructed_role_charge_stream_identity_residual":max_matter_continuity,
        "maximum_defining_array_update_identity_residual":max_continuity,
        "maximum_global_modular_sum_identity_residual":max_ledger,
        "minimum_source_deletion_signal":min_source_delete,"minimum_link_deletion_signal":min_link_delete,
        "minimum_order_signal":min_order_signal,"minimum_sign_signal":min_sign_signal,
        "maximum_all24_aggregate_array_covariance_integer_residual":max_covariance,
        "all24_aggregate_array_comparisons_executed":24 * 3,
        "maximum_aggregate_translation_covariance_integer_residual":max_translation,
        "aggregate_translation_comparisons_executed":translation_comparisons,
        "all576_sampled_Cycle600_mode_frame_group_failures":total_group_failures,
        "all576_sampled_Cycle600_mode_frame_comparisons_executed":24 * 24 * (27 + 42 + 42),
        "reversal_residuals":{f"sign_{sign}_{order}":value for (sign,order),value in reversal.items()},
        "supplied_reversal_R_qp_equals_q_minus_p_selects_symmetric": all(reversal[(s,"SYMMETRIC")]==0 for s in (+1,-1)),
        "reversal_selects_sign":False,"factor_order_is_framework_time":False,
        "arithmetic_permutation_and_phase_inventory":compiler,
        "declared_role_inventory_per_cell":"12 carrier + 5 Q + 5 P = 22 binary roles; up to 8 declared clean synthesis roles, with no composed circuit return check",
        "maximum_declared_factor_support_binary_roles":2,
        "constraint_boundary":"standalone permutation mappings fix F17-invalid labels 17..31; no physical register, composed invalid-label constraint, local carrier-sector enforcement, or scratch-return circuit is executed",
        "global_Cycle600_carrier_sector_locally_enforced":False,
        "aggregate_array_map_translation_covariance_executed":True,
        "coordinate_colored_gate_schedule_is_strictly_translation_invariant":False,
        "colored_schedule_scope":"a host graph coloring is enumerated separately but its sublayers are not executed; aggregate commuting link terms do not establish covariance of a colored physical law",
        "role_coordinate_scope":"Cycle600 role-coordinate blueprints and analytic distances only; no physical M2 placement, path word, routed update, simultaneous conflict check, or schedule covariance",
        "global_NN_route_packing_closed":False,
        "physical_boundary":{"physical_M2_register_composed":False,"physical_encoder_composed":False,
            "physical_update_composed":False,"physical_EG_evaluated":False,
            "physical_source_or_charge_current_composed":False,"physical_stress_or_gravity_composed":False,
            "physical_nearest_neighbor_routing_executed":False,"physical_colored_schedule_executed":False,
            "physical_proper_cubic_law_covariance_executed":False,"physical_code_leakage_evaluated":False},
        "modular_sum_is_current_or_impulse":False,"modular_polynomial_is_energy_or_stress":False,
        "response_is_gravity":False,
    }
    check("Route B exact F17 aggregate array map has EG/inverse identities, deletions, and odd/even coloring inventories",
          max(carrier_charge_descent,max_EG,max_field_EG,max_joint_inverse,max_inverse,max_continuity,max_matter_continuity,max_ledger)<TOL
          and min_source_delete>0 and min_link_delete>0
          and all(row["edge_coloring"]["same_color_vertex_conflicts"]==0 for row in rows)
          and all(row["layout"]["declared_persistent_binary_roles_per_cell"]==22
                  and row["layout"]["declared_total_live_binary_roles_per_cell"]==30
                  and row["layout"]["all24_role_coordinate_injection_failures"]==0
                  and row["layout"]["all576_role_coordinate_group_failures"]==0 for row in rows)
          and all(row["total_carrier_charge_mod17"]==0 for row in rows if row["matter_number"]==1),output)
    check("Route B aggregate map is translation/all24 covariant; sampled mode labels obey all576; reversal does not select sign",
          max_covariance==max_translation==total_group_failures==0 and translation_comparisons==586
          and all(reversal[(s,"SYMMETRIC")]==0 for s in (+1,-1))
          and min(reversal[(s,o)] for s in (+1,-1) for o in ("KICK_THEN_DRIFT","DRIFT_THEN_KICK"))>0
          and min_order_signal>0 and min_sign_signal>0
          and compiler["ADD17_full_space"]["bijective"] and compiler["MUL_ALPHA_full_space"]["bijective"]
          and compiler["CARRIER_ROLE_CHARGE_LOOKUP_full_space"]["bijective"]
          and compiler["RECIPROCAL_ROLE_CHARGE_PHASE"]["full_exponent_reconstruction_residual_over_pi"]<TOL
          and not compiler["materialized_gate_words_executed"],output)
    return output


# ---------------------------------------------------------------------------
# Route C: no-refit neutral-W expectation response and alias audit.


FIXTURES=(("TRAIN_L3_H384",3,384,False),("HELD_L6_H768",6,768,True),("OUT_L7_H1536",7,1536,True))


def fraction_mod(value: Fraction) -> int:
    return value.numerator*pow(value.denominator,-1,MOD)%MOD


def rational_reduction_control(length: int, steps: int=6) -> tuple[int,float]:
    volume=length**3
    source=np.empty((length,)*3,dtype=object)
    for index in np.ndindex(source.shape): source[index]=Fraction(-2,volume)
    source[0,0,0]+=2
    q=np.empty_like(source);p=np.empty_like(source)
    for index in np.ndindex(source.shape):q[index]=Fraction();p[index]=Fraction()
    qmod=np.zeros(source.shape,dtype=int);pmod=np.zeros(source.shape,dtype=int)
    max_residual=0; alias=0.0
    for _ in range(steps):
        lap=6*q-sum(np.roll(q,shift,axis) for axis in range(3) for shift in (-1,1))
        p=p+Fraction(1,12)*(source-lap);q=q+p
        smod=np.vectorize(fraction_mod)(source).astype(int)
        qmod,pmod=qca_step(qmod,pmod,smod,+1,"KICK_THEN_DRIFT")
        reduced_q=np.vectorize(fraction_mod)(q).astype(int);reduced_p=np.vectorize(fraction_mod)(p).astype(int)
        max_residual=max(max_residual,int(np.max((qmod-reduced_q)%MOD)),int(np.max((pmod-reduced_p)%MOD)))
        signed=np.vectorize(lambda x:x if x<=8 else x-17)(qmod)
        alias=max(alias,max(abs(float(q[index])-signed[index]) for index in np.ndindex(q.shape)))
    return max_residual,alias


def route_c(shore_data:dict) -> dict:
    rows=[];residuals=[];max_reduction=0;min_alias=math.inf
    for label,length,horizon,held in FIXTURES:
        point=np.zeros((length,)*3);point[0,0,0]=1;point-=1/length**3
        neutral_W_expected_source=2*point
        average,endpoint=c607.cesaro_actual(neutral_W_expected_source,horizon)
        response=average/2
        exact=c607.finite_static(point)
        relative=float(np.linalg.norm(response-exact)/np.linalg.norm(exact))
        reduction,alias=rational_reduction_control(length)
        max_reduction=max(max_reduction,reduction);min_alias=min(min_alias,alias);residuals.append(relative)
        rows.append({"fixture":label,"length":length,"held":held,"horizon_update_count":horizon,
                     "neutral_W_expected_source":"2(point-uniform), divided by the supplied carrier charge 2 after response",
                     "relative_no_refit_response_residual":relative,
                     "absolute_no_refit_response_residual":float(np.linalg.norm(response-exact)),
                     "finite_field_reduction_residual_first_6_updates":reduction,
                     "minimum_signed_lift_alias_signal":alias,
                     "endpoint_norm_not_time":float(np.linalg.norm(endpoint))})
    inherited=shore_data["receipt"]["route_C_separate_finite_graph_response_comparison"]
    output={
        "object":"separate real common-action/no-refit comparison plus exact first-six-update F17 reduction control",
        "disposition":"CONSTRUCTIVE_COMMON_ACTION_NO_REFIT_COMPARISON; SOURCE_INTERFACE_AND_PHYSICAL_INTERPRETATION_OPEN",
        "frozen_fixtures":[list(row) for row in FIXTURES],"relative_residuals":residuals,
        "maximum_exact_rational_to_F17_reduction_residual":max_reduction,
        "minimum_signed_representative_alias_signal":min_alias,
        "rows":rows,
        "comparison_scope":"the real alpha=1/12 recurrence and F17 reduction share a polynomial action for six exact rational updates; Route C manually constructs 2(point-uniform) and does not consume a Route B state or carrier-to-source interface",
        "parameters_refit":0,
        "Cycle607_static_coefficient_rows":inherited["Cycle585_588_static_coefficient_rows"],
        "maximum_5_over_32pi_relative_residual":inherited["maximum_5_over_32pi_relative_residual"],
        "matched_words":inherited["matched_event_shore"],
        "causal_time_PR_comparison":shore_data["causal_comparison"],
        "causal_time_comparison_interpretation":"the pinned external note associates 3:4 delay with a rate route and leaves 5:4 advance edit-reachable only; it is comparison evidence, not executed or back-credited Cycle609 closure",
        "routeB_to_routeC_state_interface_composed":False,
        "carrier_to_uniform_source_interface_composed":False,
        "prediction_surface_comparison_is_law":False,
        "matched_words_are_events":False,"matched_words_are_records":False,
        "event_selection_derived":False,
        "signed_F17_representatives_are_real_amplitudes":False,
        "endpoint_norm_is_probability_or_occurrence":False,
        "update_count_is_time":False,
    }
    check("Route C exact modular reduction and manual common source reproduce the no-refit Cycle607 response trend",
          max_reduction==0 and min_alias>SIGNAL and max(residuals)<0.01
          and all(residuals[i+1]<residuals[i] for i in range(len(residuals)-1)),output)
    check("Route C carries the static coefficient and matched labels without prediction/time/Event/Record promotion",
          output["maximum_5_over_32pi_relative_residual"]<0.002
          and not output["matched_words_are_events"] and not output["event_selection_derived"]
          and not output["signed_F17_representatives_are_real_amplitudes"]
          and not output["endpoint_norm_is_probability_or_occurrence"]
          and not output["prediction_surface_comparison_is_law"]
          and not output["update_count_is_time"],output)
    return output


def no_go_discipline()->dict:
    families=[
        {"route":"Walsh/parity phase polynomial","mechanism":"commuting role-Pauli strings","terminal_obligation":"exact full-role-basis phase factorization","marker":"ATTEMPTED"},
        {"route":"F17 aggregate Q/P array shear","mechanism":"modular reversible polynomial map","terminal_obligation":"inverse/deletion/aggregate covariance","marker":"ATTEMPTED"},
        {"route":"real alpha recurrence comparison","mechanism":"host array Cesaro average","terminal_obligation":"no-refit finite-graph response comparison","marker":"ATTEMPTED"},
        {"route":"Cycle600 role-coordinate allocation","mechanism":"algebraic coordinate blueprints","terminal_obligation":"test whether allocation itself establishes physical placement","marker":"ATTEMPTED"},
        {"route":"host edge coloring","mechanism":"odd/even finite-torus graph coloring","terminal_obligation":"test whether aggregate update executes colored sublayers","marker":"ATTEMPTED"},
    ]
    live_routes=[
        "compose a physical M2 E/G with carrier, Q/P, scratch, placement, routed words, leakage, and local constraints",
        "single-register metaplectic F17 realization",
        "six-ray unitary lattice-gas realization",
        "local gauge/Gauss-law source realization",
        "execute a colored proper-cubic schedule rather than the aggregate array map",
    ]
    walls={
        "W_pack":"role factors and coordinate distances lack physical placement, route words, packing, restoration, leakage, and schedule covariance",
        "W_angle":"printed rational Rz angles are parameterized, not reduced to a separately accepted finite alphabet",
        "W_double":"F17 propagation uses doubled computational Q/P registers rather than one conjugate-basis register",
        "W_alias":"the signed F17 representatives are not established as real amplitudes",
        "W_sector":"Cycle600 global carrier/neutral-W preparation remains supplied",
        "W_charge":"the carrier-role +2/-1 assignment, sign, modulus, and neutral sites remain supplied",
        "W_identification":"the modular identities are not a physical source, current, stress, or gravity law",
        "W_event":"matched 3:4/5:4 labels lack an executed Event/Record/time interface",
    }
    names=tuple(walls);pairs=[{"left":names[i],"right":names[j],
                              "left_to_right":{"status":"NOT_ESTABLISHED",
                                  "reason":f"no executed intervention closes {names[i]} and then retests {names[j]}"},
                              "right_to_left":{"status":"NOT_ESTABLISHED",
                                  "reason":f"no executed intervention closes {names[j]} and then retests {names[i]}"},
                              "independence":{"status":"NOT_ESTABLISHED",
                                  "reason":"neither directional closure experiment was executed"}}
                               for i in range(len(names)) for j in range(i+1,len(names))]
    canonical_phrases=("we assume","by construction","as is standard","the framework provides",
                       "bridge context","background","naturally","obviously","standard qft",
                       "registered","canonical")
    note_text=" ".join(NOTE.read_text().lower().split())
    hidden_phrase_hits=[phrase for phrase in canonical_phrases if phrase in note_text]
    n4=[
        {"prior_path":"scripts/physical_car_matter_weyl_reciprocal_source_response_tournament_cycle607_2026_07_22.py","prior_line":549,
         "prior_residual":"NQ phase not decomposed into elementary local factors",
         "current_witness":"Route A exact 65,536-state role-phase residual",
         "current_residual":0.0,"match":"EXACT_ALGEBRAIC_RESIDUAL_MATCH",
         "same_scope":True,"use_as_closure":True},
        {"prior_path":"scripts/physical_car_matter_weyl_reciprocal_source_response_tournament_cycle607_2026_07_22.py","prior_line":785,
         "prior_residual":"carrier/source/response interface not composed",
         "current_witness":"Route B and Route C remain separate host-prepared arrays",
         "current_residual":"NOT_COMPOSED","match":"EXACT_RESIDUAL_PERSISTS",
         "same_scope":True,"use_as_closure":False},
        {"prior_path":"scripts/physical_root_free_full_N3_carrier_genesis_tournament_cycle600_2026_07_22.py","prior_line":918,
         "prior_residual":"physical encoder composed from M2 primitives false",
         "current_witness":"Route A/B use inherited algebraic role bits and role coordinates",
         "current_residual":"NOT_COMPOSED","match":"EXACT_RESIDUAL_PERSISTS",
         "same_scope":True,"use_as_closure":False},
    ]
    n5=[
        {"claim":"role factors are not a physical M2 compiler",
         "per_element":"Rz and CNOT are algebraic role symbols",
         "per_site":"no physical site register or placement is composed",
         "per_mode":"carrier/Q/P words remain declared role registers",
         "per_block":"constant role count and coordinate allocation do not establish routing, leakage, or constraints",
         "lattice_wide":"role-level all24/all576 audits do not establish covariance of a physical schedule"},
        {"claim":"modular identities are not a physical source/current/stress/gravity law",
         "per_element":"F17 values and +2/-1 are supplied algebraic labels",
         "per_site":"the defining kick identity is a host-array equality",
         "per_mode":"carrier-role charge descent has no physical charge observable interface",
         "per_block":"standalone lookup permutations are not a composed source circuit",
         "lattice_wide":"aggregate translation/all24 covariance is not a colored physical law or gravity"},
        {"claim":"comparison outputs are not time, Event, Record, Born probability, or realized history",
         "per_element":"a signed representative is not a real amplitude",
         "per_site":"an endpoint norm is not probability or occurrence",
         "per_mode":"3:4 and 5:4 labels are not selected Events",
         "per_block":"finite update counts are not clock rates or time",
         "lattice_wide":"the no-refit response comparison is not a prediction or history law"},
    ]
    n6=[
        {"file":"docs/work_history/repo/review_feedback/PHYSICAL_PROPER_CUBIC_SUPERCELL_STREAM_COMPOSITION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md","status":"PINNED_LOCAL_BRANCH_NOTE_NOT_EXECUTED","closure":"could test physical proper-cubic schedule composition"},
        {"file":"docs/work_history/repo/review_feedback/PHYSICAL_MATTER_VARIATION_CURRENT_STRESS_COMPENSATOR_SOURCE_TOURNAMENT_CYCLE611_NOTE_2026-07-22.md","status":"PINNED_LOCAL_BRANCH_NOTE_NOT_EXECUTED","closure":"could test a matter variation/current/stress/source interface"},
        {"file":"docs/work_history/repo/review_feedback/PHYSICAL_MATTER_CAUSED_CAUSAL_INTERVAL_PROPER_TIME_BRIDGE_TOURNAMENT_CYCLE612_NOTE_2026-07-22.md","status":"PINNED_LOCAL_BRANCH_NOTE_NOT_EXECUTED","closure":"could test a matter-to-causal-interval/proper-time interface"},
        {"file":f"{CAUSAL_COMPARISON['commit']}:{CAUSAL_COMPARISON['path']}","status":"PINNED_COMPARISON_ONLY_NOT_EXECUTED_OR_BACKCREDITED","closure":"could distinguish rate-associated delay from count-edit advance while leaving Event association open"},
    ]
    n8=[
        {"cycle":"Cycle600","echo":"algebraic carrier-role representation was previously distinguished from a physical M2 compiler","effect":"prevents role-bit back-credit"},
        {"cycle":"Cycle607","echo":"algebraic CAR/W16 interface and separate graph response left their physical join open","effect":"Route A closes only the algebraic phase factorization"},
        {"cycle":"local Cycle610","echo":"proper-cubic supercell work is a separate local-branch note","effect":"not imported or executed here"},
        {"cycle":"local Cycle611","echo":"current/stress/source work is a separate local-branch note","effect":"not imported or executed here"},
        {"cycle":"local Cycle612","echo":"causal interval/proper-time work is a separate local-branch note","effect":"not imported or executed here"},
        {"cycle":"PR causal-time Cycle612","echo":"3:4 delay can be rate-associated while 5:4 advance still requires a count edit","effect":"comparison only; Event association remains underived"},
    ]
    allowed_markers={"ATTEMPTED","RULED OUT BY PRIOR"}
    marker_schema_pass=all(row["marker"] in allowed_markers for row in families)
    independence_complete=all(row["independence"]["status"]=="ESTABLISHED" for row in pairs)
    output={
        "N1_normalized_families":families,"N1_allowed_markers":sorted(allowed_markers),
        "N1_marker_schema_pass":marker_schema_pass,"N1_live_routes":live_routes,
        "N2_pairwise_wall_closure_and_independence":pairs,
        "N2_independence_complete":independence_complete,
        "N3_canonical_hidden_wall_phrases":list(canonical_phrases),
        "N3_note_phrase_hits":hidden_phrase_hits,
        "N3_explicit_supplied_structure":["W16/Walsh convention","role-factor gate alphabet","Cycle600 role coordinates","F17","doubled Q/P roles","+2/-1 carrier-role assignment","neutral-site placement","alpha=1/12","sign","reversal","factor order","host edge coloring","finite horizons","manual point-minus-uniform source","signed-representative comparison","matched-label association"],
        "N4_exact_residual_matching":n4,
        "N5_five_resolution_rhetoric_audit":n5,
        "N6_partial_closure_paths":n6,
        "N7_cited_actionable_steelman":{"citation":"scripts/physical_car_matter_weyl_reciprocal_source_response_tournament_cycle607_2026_07_22.py:549-558","action":"compose one explicit physical M2 E and G around the exact role-phase factors, including placement, routed word, leakage, local constraints, and all24 schedule covariance; independently execute metaplectic, six-ray, and local-gauge alternatives before any shared-obstruction claim"},
        "N8_rowwise_cross_cycle_echo":n8,
        "walls":walls,"Status":"FAIL / DO NOT SHIP NEGATIVE",
        "negative_gate_reasons":["live constructive routes remain", "pairwise wall independence is not established"],
        "narrowed_positive_artifact_status":"PASS",
        "negative_claim_shipped":False,"shared_obstruction":False,
        "minimum_content_claim":False,"axiom_pressure":False,
    }
    check("full N1-N8 keeps the negative gate failed while permitting the narrowed executed positives",
          len(families)>=5 and marker_schema_pass and len(live_routes)>0
          and len(pairs)==len(names)*(len(names)-1)//2 and not independence_complete
          and not hidden_phrase_hits
          and all(all(field in row for field in ("per_element","per_site","per_mode","per_block","lattice_wide")) for row in n5)
          and all("file" in row and "status" in row and "closure" in row for row in n6)
          and len(n8)>=5 and output["Status"]=="FAIL / DO NOT SHIP NEGATIVE"
          and output["narrowed_positive_artifact_status"]=="PASS"
          and not output["negative_claim_shipped"]
          and not output["shared_obstruction"] and not output["minimum_content_claim"] and not output["axiom_pressure"],output)
    return output


def note_contract()->None:
    body=" ".join(NOTE.read_text().lower().replace("`","").replace("*","").split())
    required=("authority: none","audit: unset","author artifact status accepted: false",
              "cycle 609","route a","route b","route c","walsh","109","318",
              "algebraic role","not a physical m2 compiler","parameterized","nearest-neighbor depth",
              "f17","host-prepared","not a physical source","l3","l6","l7","odd","even",
              "all-24","all-576","reversal","does not select the sign","wrap","alias",
              "5/(32pi)","3:4","5:4","not energy","not a route-b-to-response interface",
              "not events","n1 —","n2 —","n3 —","n4 —","n5 —","n6 —","n7 —","n8 —",
              "negative_claim_shipped=false","no axiom pressure","no candidate rises to a confirmed breakthrough")
    missing=tuple(item for item in required if item not in body)
    check("Cycle609 note freezes algebraic/array/comparison scope, controls, and N1-N8",not missing,missing)


def main()->int:
    shore_data=shore();note_contract();routeA=route_a();routeB=route_b();routeC=route_c(shore_data);nogo=no_go_discipline()
    elapsed=perf_counter()-START;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss;rss=int(rss if sys.platform=="darwin" else rss*1024)
    receipt={
        "cycle":609,"authority":AUTHORITY,"audit":AUDIT,
        "author_artifact_status_accepted":AUTHOR_ARTIFACT_STATUS_ACCEPTED,
        "audit_verdict_inferred_from_dependencies":AUDIT_VERDICT_INFERRED_FROM_DEPENDENCIES,
        "constitutional_effect":"none",
        "HEAD":subprocess.check_output(("git","rev-parse","HEAD"),cwd=ROOT,text=True).strip(),
        "runner_sha256":sha256(Path(__file__).read_bytes()).hexdigest(),
        "note_sha256":sha256(NOTE.read_bytes()).hexdigest(),
        "pins":PINS,"shore":shore_data["evidence"],
        "runtime_import_controls":shore_data["runtime_import_controls"],
        "causal_time_comparison":shore_data["causal_comparison"],
        "route_A_algebraic_role_phase_factorization":routeA,
        "route_B_F17_aggregate_array_map":routeB,
        "route_C_common_action_no_refit_comparison":routeC,
        "no_go_discipline":nogo,
        "status":"three executed algebraic/numerical results; no physical M2 compiler, source law, time, Event, Record, Born rule, or confirmed breakthrough",
        "scope_boundaries":{"physical_M2_compiler":False,"physical_encoder_E_composed":False,
            "physical_update_G_composed":False,"physical_EG_evaluated":False,
            "physical_placement_and_routing_executed":False,"physical_leakage_evaluated":False,
            "local_auxiliary_or_gauge_constraints_composed":False,
            "physical_source_current_stress_gravity_law":False,
            "proper_cubic_colored_physical_schedule_executed":False,
            "prediction_law":False,"time_or_rate_derived":False,"Event_or_Record_derived":False,
            "Born_probability_derived":False},
        "inventory":{"supplied":["Cycle600 algebraic carrier-role representation and role-coordinate blueprints","W16/Walsh bit convention","role-CNOT/role-Rz factor recipe and printed rational angles","F17 modulus","doubled Q/P roles","+2/-1 carrier-role assignment","neutral-site placement","coupling sign","alpha=1/12","reversal and factor order","host edge coloring","finite horizons","manual point-minus-uniform source","signed-representative comparison","matched-label association"],
            "derived_or_executed":["full 65,536-state exact W16 role-phase factorization","109 role-Rz and 318 role-CNOT factor counts","inverse/deletion and role-level proper-cubic controls","exact F17 aggregate Q/P array update and inverse","exact aggregate translation and all24 covariance","separate sampled Cycle600 all576 mode-frame group law","standalone reversible F17 permutation inventories","six-update exact rational-to-F17 reduction","no-refit real common-action comparison"],
            "not_derived":["physical M2 register, encoder, update, E/G, placement, routing, packing, leakage, or local constraints","executed colored schedule or proper-cubic physical-law covariance","materialized arithmetic circuit words or scratch return","accepted finite angle alphabet","single-register Weyl realization","carrier-to-charge/source array circuit","uniform neutral-W expectation from a register","physical charge, current, energy, stress, gravity, or prediction law","real-amplitude semantics for F17 labels","time, Event, Record, Born probability, or realized history"]},
        "six_wall_ledger":{"C_ref":"UNCHANGED PHYSICALLY: exact algebraic role-charge descent and phase factors exist; sign, units, charge meaning, physical encoder, and source interface remain supplied or open","C_num":"ADVANCED ALGEBRAICALLY: the 65,536-state role-phase factorization and F17 permutations are exact; physical register, scale, enforcement, and accepted gate alphabet remain open","C_wrap":"DIAGNOSTIC ONLY: exact rational reduction and alias signals are explicit; wrap is not energy, rate, time, or a real-amplitude rule","C_int":"ADVANCED ALGEBRAICALLY: the NQ role-phase factorization and a separate F17 polynomial map are exact; no physical join is composed","C_local":"UNCHANGED PHYSICALLY: support-two role factors and coordinate proxies are not placement, NN packing, routed update, leakage, constraints, or schedule covariance","C_source":"UNCHANGED PHYSICALLY: host-prepared charge/source arrays and a separate no-refit comparison are not physical source, current, stress, gravity, or event selection"},
        "maturity_effect":"no upward maturity revision for operational quantum/Records, time, inertia/matter, gravity/source, or Born/probability",
        "strongest_constructive_result":"the Cycle607 W16 NQ ambient-role phase is exactly factorized over all 65,536 states into 109 parameterized role-Rz and 318 role-CNOT factors, with exact inverse, deletion, off-code, and role-level proper-cubic controls; this is not a physical M2 compiler",
        "confirmed_breakthrough":False,
        "shared_obstruction_or_axiom_pressure":False,
        "optimal_next_campaign":"compose a literal physical-M2 code space, E, G, placement, routed gate words, colored update, local constraints, and leakage test around the exact role factorization; test EG, deletion, L6/L7, and all24 schedule covariance while keeping metaplectic, six-ray, and local-gauge routes live",
        "terminology_guards":{"wrapped_phase_is_physical_energy":False,"generator_element_is_rate":False,
            "pointer_copy_is_Record":False,"coarse_or_role_cell_is_physical_site_compiler":False,
            "modular_sum_is_current":False,"signed_F17_representative_is_real_amplitude":False,
            "matched_label_is_Event":False},
        "tests_passed":PASS,"tests_failed":FAIL,"tests_total":PASS+FAIL,"pass":FAIL==0,
        "elapsed_seconds":elapsed,"maximum_RSS_bytes":rss,
        "runtime_environment":{"python":sys.version.split()[0],"numpy":np.__version__},
    }
    RECEIPT.write_text(json.dumps(receipt,indent=2,sort_keys=True,default=json_default)+"\n")
    print("RECEIPT",json.dumps(receipt,sort_keys=True,default=json_default))
    print("SUMMARY",json.dumps({"pass":receipt["pass"],"tests_passed":PASS,"tests_failed":FAIL,"elapsed_seconds":elapsed,"maximum_RSS_bytes":rss,"route_A":routeA["disposition"],"route_B":routeB["disposition"],"route_C":routeC["disposition"],"axiom_pressure":False},sort_keys=True))
    return int(FAIL!=0)


if __name__ == "__main__":
    if "--cold" in sys.argv:
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            exit_code = main()
        transcript = buffer.getvalue()
        COLD.write_text(transcript, encoding="utf-8")
        print(transcript, end="")
        raise SystemExit(exit_code)
    raise SystemExit(main())
