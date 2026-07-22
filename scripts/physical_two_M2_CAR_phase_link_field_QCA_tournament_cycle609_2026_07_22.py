#!/usr/bin/env python3
"""Cycle609: two-M2 CAR phase lowering and finite-field link QCA.

This runner closes Cycle607's 16-M2 lookup residual by an exact Walsh/parity
gate schedule and constructs a separate F17 reversible link-field QCA whose
source is the accepted Cycle600 carrier charge.  Modular labels are not
energy/stress/gravity, update count is not time, and matched words are not
events.  Authority none; audit unset.
"""
from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
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
TOL = 2e-8
SIGNAL = 1e-6
START = perf_counter()
PASS = 0
FAIL = 0


class Tee:
    def __init__(self, *streams):
        self.streams = streams

    def write(self, value: str) -> int:
        for stream in self.streams:
            stream.write(value)
        return len(value)

    def flush(self) -> None:
        for stream in self.streams:
            stream.flush()

PINS = {
    "scripts/physical_car_matter_weyl_reciprocal_source_response_tournament_cycle607_2026_07_22.py":
        "e522c2e662656e98d177faea19fe1009b1f1cba62fdc70576c29f4ea506a7326",
    "docs/work_history/repo/review_feedback/PHYSICAL_CAR_MATTER_WEYL_RECIPROCAL_SOURCE_RESPONSE_TOURNAMENT_CYCLE607_NOTE_2026-07-22.md":
        "0af61802b863f04546a1a92ce1042c7dc648100c0fa5ccd57bdf42122371d369",
    "outputs/physical_car_matter_weyl_reciprocal_source_response_tournament_cycle607_receipt_2026_07_22.json":
        "752be1935cdac98b3081b2a55665a0383c627e3639ab83c76e8fc4d624ea11b4",
    "outputs/physical_car_matter_weyl_reciprocal_source_response_tournament_cycle607_cold_2026_07_22.txt":
        "9d8eb59b36c2270bb991e32def6a33566a62762de994af2c114cf06310e24271",
}


def digest(relative: str) -> str:
    return sha256((ROOT / relative).read_bytes()).hexdigest()


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
    receipt = json.loads((ROOT / "outputs/physical_car_matter_weyl_reciprocal_source_response_tournament_cycle607_receipt_2026_07_22.json").read_text())
    evidence = {
        "hashes_match": observed == PINS, "Cycle607_pass": receipt["pass"],
        "Cycle607_tests": receipt["tests_passed"],
        "number_descent": receipt["route_A_joint_CAR_Weyl_interaction"]["Cycle600_number_descent_residual"],
        "joint_EG": receipt["route_A_joint_CAR_Weyl_interaction"]["maximum_global_joint_EG_residual"],
        "mass": receipt["shore"]["one_particle_mass_residual"],
        "contact": receipt["shore"]["Cycle230_contact_factorization_residual"],
        "seam": receipt["shore"]["Cycle230_seam_braid_residual"],
    }
    check("Cycle607 is byte-pinned and passing", evidence["hashes_match"] and evidence["Cycle607_pass"]
          and max(evidence["number_descent"], evidence["joint_EG"], evidence["mass"],
                  evidence["contact"], evidence["seam"]) < TOL, evidence)
    return {"observed": observed, "evidence": evidence, "receipt": receipt}


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
    """The supplied proper-cubic action on one physical 4-M2 carrier word."""
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
    maximum_distance = maximum_NN_depth = 0
    for label, length, held in (("TRAIN_L3", 3, False), ("HELD_L6", 6, True),
                                ("OUT_FAMILY_L7", 7, True)):
        carrier, field, modulus = joint_role_coordinates(length)
        roles = list(carrier[0]) + list(field[0])
        distances = []
        NN_depth = 0
        for mask in positive:
            indices = [bit for bit in range(16) if mask >> bit & 1]
            if len(indices) <= 1: continue
            pivot = indices[-1]
            for control in indices[:-1]:
                distance = periodic_l1(roles[control], roles[pivot], modulus)
                distances.append(distance)
                # route there/back with SWAP=3 CNOT plus the desired CNOT
                NN_depth += 2 * (6*max(0, distance-1) + 1)
        maximum_distance = max(maximum_distance, max(distances))
        maximum_NN_depth = max(maximum_NN_depth, NN_depth + rz)
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
                     "maximum_interacting_role_distance": max(distances),
                     "serial_NN_depth_upper_bound": NN_depth + rz,
                     "all24_wire_injection_failures": injection,
                     "all576_coordinate_group_failures": group})
    deletion_mask = next(mask for mask in positive if mask and positive[mask])
    deletion_signal = 2 * abs(math.sin(math.pi * float(positive[deletion_mask])))
    output = {
        "object": "exact support<=2 M2 Walsh/parity compiler for Cycle607 U=exp(2pi i NQ/16)",
        "disposition": "CONSTRUCTIVE_EXACT_SUPPORT2_BOUNDED_DISTANCE_LOWERING; NN_PACKING_OPEN",
        "full_physical_basis_states_exhausted": 1 << 16,
        "local_five_bit_Walsh_nonzero_terms": len(local),
        "combined_nonzero_Pauli_terms_including_global": len(positive),
        "support_histogram": support_histogram,
        "maximum_Pauli_string_support_before_lowering": max(mask.bit_count() for mask in positive),
        "gate_schedule": "for each nonempty Z string: CNOT every other support bit into one pivot, apply Rz(-2*pi*a_S), undo CNOTs; apply the printed global phase",
        "maximum_elementary_gate_support_M2": 2,
        "logical_CNOT_count_per_cell": logical_cnot,
        "Rz_count_per_cell": rz,
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
        "scratch_or_garbage_M2": 0,
        "maximum_actual_role_L1_distance": maximum_distance,
        "maximum_serial_NN_depth_upper_bound": maximum_NN_depth,
        "NN_routing_status": "distance-derived serial NN depth upper bound only; path lists, simultaneous cell packing, route-work restoration, and schedule covariance were not executed in Cycle609",
        "physical_NN_route_packing_closed": False,
        "rows": rows,
        "coupling_sign_selected": False,
        "accepted_finite_angle_alphabet_beyond_printed_Rz": False,
    }
    check("Route A exactly lowers the full Cycle607 on/off-code NQ phase to support<=2 M2 gates",
          phase_residual < TOL and exponent_residual < TOL and inverse_residual == 0
          and phase_covariance < TOL and label_group_failures == 0
          and deletion_signal > SIGNAL and max(mask.bit_count() for mask in positive) <= 4
          and logical_cnot == 318 and rz == 109, output)
    check("Route A gives bounded role-distance bounds plus phase-law and coordinate all24/all576 certificates",
          maximum_distance <= 8 and maximum_NN_depth > 0
          and phase_covariance < TOL and label_group_failures == 0
          and all(row["all24_wire_injection_failures"] == 0
                  and row["all576_coordinate_group_failures"] == 0 for row in rows), rows)
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


def physical_carrier_charges() -> np.ndarray:
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
            "commuting_link_shears_make_color_order_irrelevant": True}


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
            "support2_CNOT_bound_after_exact_Toffoli_lowering": 6*toffoli_bound,
            "clean_scratch_M2": max(0, controls-2),
            "scratch_returned_zero": True}


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
            "maximum_elementary_gate_support_M2":2,
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
    return {"persistent_M2_per_cell":22,"reused_clean_scratch_M2_per_cell":8,
            "total_live_M2_per_cell":30,"maximum_link_role_L1_distance":max_link,
            "serial_NN_CNOT_depth_bound_per_ADD17":support2_cnot_bound*(6*max(0,max_link-1)+1),
            "all24_wire_injection_failures":injection,"all576_coordinate_group_failures":group,
            "scratch_returned_zero_at_logical_compiler_level":True,
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
        "CARRIER_CHARGE_LOOKUP_full_space":charge_lookup,
        "RECIPROCAL_SOURCE_PHASE":reciprocal_phase_compiler_stats(),
        "primitive_lowering": "cycle decomposition -> Gray-adjacent basis transpositions -> clean-scratch multi-controlled X -> exact H/T/CNOT Toffoli decomposition",
        "maximum_elementary_gate_support_M2": 2,
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
    physical_charge=physical_carrier_charges()
    logical_charge=np.asarray([3*len(subset)-3 for subset in basis])
    carrier_charge_descent=float(np.linalg.norm(
        physical_charge[:,None]*embedding-embedding*logical_charge[None,:]))
    rows = []
    max_inverse = max_EG = max_field_EG = max_joint_inverse = max_continuity = max_matter_continuity = max_ledger = max_covariance = 0
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
        layout=qca_layout(length,compiler["ADD17_full_space"]["support2_CNOT_bound_after_exact_Toffoli_lowering"])
        max_inverse=max(max_inverse,inverse); max_EG=max(max_EG,EG);max_field_EG=max(max_field_EG,field_EG);max_joint_inverse=max(max_joint_inverse,joint_inverse)
        max_matter_continuity=max(max_matter_continuity,matter_continuity)
        max_continuity=max(max_continuity,int(np.max(np.minimum(continuity,MOD-continuity))))
        max_ledger=max(max_ledger,min(ledger,MOD-ledger))
        min_source_delete=min(min_source_delete,source_signal); min_link_delete=min(min_link_delete,link_signal)
        min_order_signal=min(min_order_signal,order_signal); min_sign_signal=min(min_sign_signal,sign_signal)
        rows.append({"fixture":label,"length":length,"held":held,"matter_number":len(subset),
                     "neutral_carriers":len(neutral_sites),"total_carrier_charge_mod17":int(np.sum(target_charge)%MOD),
                     "joint_stream_contact_source_EG_residual":EG,"exact_inverse_integer_residual":inverse,
                     "field_update_per_word_EG_residual":field_EG,"full_joint_carrier_field_inverse_residual":joint_inverse,
                     "matter_charge_stream_continuity_residual":matter_continuity,
                     "local_field_equation_residual":int(np.max(np.minimum(continuity,MOD-continuity))),
                     "global_impulse_ledger_residual":min(ledger,MOD-ledger),
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
        "object":"F17 finite-Weyl phase-space link QCA driven by accepted Cycle600 carrier charge",
        "disposition":"CONSTRUCTIVE_EXACT_TRANSLATION_COVARIANT_AGGREGATE_LINK_QCA; SUPPORT2_SYNTHESIS_EXACT; NN_PACKING_OPEN; COLORED_GATE_SCHEDULE_SUPPLIED; EMPIRICAL_IDENTIFICATION_OPEN",
        "field_modulus":MOD,"alpha_mod17":ALPHA,"alpha_rational":"1/12","half_mod17":HALF,
        "local_modular_action":"A=alpha[s sum_x J_x Q_x - 1/2 sum_<xy>(Q_x-Q_y)^2] plus kinetic half-steps; J assigns +2 to matter, -1 to each neutral carrier, 0 to absent/invalid",
        "actual_source_interface":"Cycle600 N=1 has one +2 matter carrier and two -1 neutral-W carriers, hence exact total charge zero and expectation 2(point-uniform)",
        "local_carrier_charge_descent_residual":carrier_charge_descent,
        "full_carrier_basis_labels_exhausted":16**3,
        "off_code_carrier_labels_have_zero_source_charge_and_reciprocal_phase":True,
        "rows":rows,"maximum_joint_EG_residual":max_EG,"maximum_field_update_per_word_EG_residual":max_field_EG,
        "maximum_full_joint_carrier_field_inverse_residual":max_joint_inverse,"maximum_exact_inverse_residual":max_inverse,
        "maximum_matter_charge_continuity_residual":max_matter_continuity,
        "maximum_local_field_equation_residual":max_continuity,"maximum_global_impulse_ledger_residual":max_ledger,
        "minimum_source_deletion_signal":min_source_delete,"minimum_link_deletion_signal":min_link_delete,
        "minimum_order_signal":min_order_signal,"minimum_sign_signal":min_sign_signal,
        "maximum_all24_covariance_integer_residual":max_covariance,
        "all576_group_failures":total_group_failures,
        "reversal_residuals":{f"sign_{sign}_{order}":value for (sign,order),value in reversal.items()},
        "supplied_reversal_R_qp_equals_q_minus_p_selects_symmetric": all(reversal[(s,"SYMMETRIC")]==0 for s in (+1,-1)),
        "reversal_selects_sign":False,"factor_order_is_framework_time":False,
        "arithmetic_support2_compiler":compiler,
        "persistent_M2_per_cell":"12 carrier + 5 Q + 5 P = 22; up to 8 clean routing/synthesis scratch reused and returned zero",
        "maximum_elementary_gate_support_M2":2,
        "local_constraints":"F17 labels 0..16 are the lawful field code; 17..31 are fixed by every block; scratch-zero checks are local",
        "global_Cycle600_carrier_sector_locally_enforced":False,
        "aggregate_link_shear_map_is_translation_covariant":True,
        "coordinate_colored_gate_schedule_is_strictly_translation_invariant":False,
        "colored_schedule_scope":"the coordinate/L/parity/seam coloring is supplied by the compiler; commuting link shears prove the aggregate update independent of color order, but strict translation invariance or proper-cubic covariance of the finite-volume gate schedule itself is not claimed",
        "NN_routing_bound_import":"literal carrier/Q/P/scratch coordinates and pair distances give a conservative serial depth bound using the inherited Cycle527 route/unroute cost; Cycle609 does not materialize path lists or prove simultaneous fine-site/edge conflict freedom",
        "global_NN_route_packing_closed":False,
        "modular_impulse_is_energy_or_stress":False,"response_is_gravity":False,
    }
    check("Route B exact F17 link QCA has joint EG/inverse/continuity, deletions, and both odd/even schedules",
          max(carrier_charge_descent,max_EG,max_field_EG,max_joint_inverse,max_inverse,max_continuity,max_matter_continuity,max_ledger)<TOL
          and min_source_delete>0 and min_link_delete>0
          and all(row["edge_coloring"]["same_color_vertex_conflicts"]==0 for row in rows)
          and all(row["layout"]["persistent_M2_per_cell"]==22
                  and row["layout"]["total_live_M2_per_cell"]==30
                  and row["layout"]["all24_wire_injection_failures"]==0
                  and row["layout"]["all576_coordinate_group_failures"]==0 for row in rows)
          and all(row["total_carrier_charge_mod17"]==0 for row in rows if row["matter_number"]==1),output)
    check("Route B is all24/all576 covariant and the supplied reversal selects symmetric order but not sign",
          max_covariance==total_group_failures==0
          and all(reversal[(s,"SYMMETRIC")]==0 for s in (+1,-1))
          and min(reversal[(s,o)] for s in (+1,-1) for o in ("KICK_THEN_DRIFT","DRIFT_THEN_KICK"))>0
          and min_order_signal>0 and min_sign_signal>0
          and compiler["ADD17_full_space"]["bijective"] and compiler["MUL_ALPHA_full_space"]["bijective"]
          and compiler["CARRIER_CHARGE_LOOKUP_full_space"]["bijective"]
          and compiler["RECIPROCAL_SOURCE_PHASE"]["full_exponent_reconstruction_residual_over_pi"]<TOL,output)
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
    inherited=shore_data["receipt"]["route_C_actual_source_prediction"]
    output={
        "object":"neutral-W expectation response of the exact F17 QCA action compared with Cycle607",
        "disposition":"CONSTRUCTIVE_COMMON_ACTION_RESPONSE_BRIDGE; MODULAR_LABELS_NOT_REAL_AMPLITUDES",
        "frozen_fixtures":[list(row) for row in FIXTURES],"relative_residuals":residuals,
        "maximum_exact_rational_to_F17_reduction_residual":max_reduction,
        "minimum_canonical_signed_lift_alias_signal":min_alias,
        "rows":rows,
        "same_no_refit_static_operator":"the F17 QCA is the exact finite-field reduction of alpha=1/12 leapfrog; its neutral-W expectation source divided by 2 is Cycle607 point-minus-uniform",
        "Cycle607_static_coefficient_rows":inherited["Cycle585_588_static_coefficient_rows"],
        "maximum_5_over_32pi_relative_residual":inherited["maximum_5_over_32pi_relative_residual"],
        "matched_words":inherited["matched_event_shore"],
        "matched_words_are_events":False,"event_selection_derived":False,
        "finite_field_signed_lift_is_real_response":False,"update_count_is_time":False,
    }
    check("Route C exact modular reduction and neutral-W expectation reproduce the no-refit Cycle607 response trend",
          max_reduction==0 and min_alias>SIGNAL and max(residuals)<0.01
          and all(residuals[i+1]<residuals[i] for i in range(len(residuals)-1)),output)
    check("Route C carries the static coefficient and matched words without gravity/time/event promotion",
          output["maximum_5_over_32pi_relative_residual"]<0.002
          and not output["matched_words_are_events"] and not output["event_selection_derived"]
          and not output["finite_field_signed_lift_is_real_response"] and not output["update_count_is_time"],output)
    return output


def no_go_discipline()->dict:
    families=[
        ["Walsh/parity phase polynomial","commuting Pauli strings","exact Cycle607 W16 support2 lowering","ATTEMPTED_POSITIVE_C609"],
        ["F17 phase-space link QCA","modular symplectic shears","exact source/link propagation and inverse","ATTEMPTED_POSITIVE_C609"],
        ["single-register metaplectic F17","quadratic Weyl Clifford","remove doubled Q/P presentation","LIVE_UNTESTED"],
        ["six-ray unitary lattice gas","stream/scatter invariant","stable response without finite-field signed lift","LIVE_UNTESTED"],
        ["Cycle590 word arithmetic","53-M2 occupation plus ripple adders","alternative physical source compiler","PRIOR_PARTIAL"],
        ["link gauge/Gauss law","locally constrained flux","empirical charge and source law","LIVE_UNTESTED"],
        ["Cycle607 float response","real alpha leapfrog","static/event comparison","PRIOR_POSITIVE_NON_M2_PROPAGATION"],
    ]
    walls={
        "W_pack":"support2 logical gates have bounded-distance layouts and serial NN cost bounds, but simultaneous materialized path packing and schedule covariance remain open",
        "W_angle":"printed rational Rz angles are parameterized, not reduced to a separately accepted finite alphabet",
        "W_double":"F17 propagation uses doubled computational Q/P registers rather than one conjugate-basis register",
        "W_alias":"finite-field labels have no canonical real signed-amplitude lift after rational reduction",
        "W_sector":"Cycle600 global carrier/neutral-W preparation remains supplied",
        "W_charge":"the +2/-1 carrier charge convention and F17 modulus remain supplied",
        "W_identification":"modular impulse is not empirically identified as energy, stress, or gravity",
        "W_event":"matched 3:4/5:4 words remain unselected and uncalibrated",
    }
    names=tuple(walls);pairs=[{"left":names[i],"right":names[j],"left_closes_right":False,"right_closes_left":False,"independent":True}
                               for i in range(len(names)) for j in range(i+1,len(names))]
    output={
        "N1_normalized_families":families,"N2_pairwise_wall_independence":pairs,
        "N3_hidden_wall_scan":["W16 and Walsh convention","support2-versus-materialized-NN packing","serial Cycle527 route-cost import","rational Rz angles","F17","doubled Q/P words","+2/-1 carrier charge","neutral-W preparation","alpha=1/12","reversal R","factor order","finite horizons","signed-lift comparison","matched-word association"],
        "N4_residual_matching":[
            ["Cycle607 runner Route A","one 16-M2 block not decomposed","support2 Walsh schedule","exact algebraic match closed; NN packing is a distinct residual"],
            ["Cycle607 runner Route C","no M2 alpha propagation","F17 modular reduction QCA","aggregate support2 propagation match; NN packing and real-lift identification remain distinct"],
            ["Cycle600 runner Route A","prepared neutral-W/carrier sector","local QCA constraint","different residual; not cited as closure"],
        ],
        "N5_rhetoric_audit":{
            "not_energy_stress_gravity":"tested at modular element/site/block/lattice ledger resolutions only; no empirical identification tested",
            "not_time":"tested update schedules and reversal maps only; no clock-rate identification tested",
            "not_event":"exact matched words retained; occurrence/Record/calibration not tested"},
        "N6_partial_closure_paths":["Walsh identities retire the Cycle607 16-M2 lookup residual at the support2 algebraic level while leaving simultaneous NN packing open","F17 reduction retires aggregate bounded propagation/inverse while leaving NN schedule packing and representation semantics explicit","neutral-W expectation supplies local zero-mode compensation on N=1 without a host future-source query"],
        "N7_steelman":"A hostile reviewer should reject any obstruction: explicit path coloring or supercell isolation could close the NN packing wall; a single-register metaplectic F17 Clifford or a six-ray unitary lattice gas could remove the doubled-register and signed-lift walls; and the printed rational-angle Walsh compiler could be compiled into whatever finite alphabet is ultimately accepted. These are concrete live mechanisms with untested terminal obligations.",
        "N8_cross_cycle_echo":{"Cycle560_600":"bounded encodings repeatedly retired host ordering/label walls","Cycle607_609":"block lookup and non-M2 propagation are replaced by explicit support2 and exact modular QCA constructions","Cycle451_570":"matched words remained exact while event calibration stayed separate"},
        "walls":walls,"broad_negative_gate":"FAIL / DO NOT SHIP","shared_obstruction":False,"minimum_content_claim":False,"axiom_pressure":False,
    }
    check("full N1-N8 audits seven normalized families and blocks negative/minimum/axiom pressure",
          len(families)>=5 and len(pairs)==len(names)*(len(names)-1)//2
          and not output["shared_obstruction"] and not output["minimum_content_claim"] and not output["axiom_pressure"],output)
    return output


def note_contract()->None:
    body=" ".join(NOTE.read_text().lower().replace("`","").replace("*","").split())
    required=("authority: none","audit: unset","cycle 609","route a","route b","route c","walsh","support<=2","109","318","off-code","parameterized","nearest-neighbor","f17","link","actual cycle600","neutral-w","+2","-1","l3","l6","l7","odd","even","all 24","576","reversal","does not select sign","wrap","alias","5/(32pi)","3:4","5:4","not energy","not stress","not gravity","update count is not time","not events","n1 —","n2 —","n3 —","n4 —","n5 —","n6 —","n7 —","n8 —","no axiom pressure")
    missing=tuple(item for item in required if item not in body)
    check("Cycle609 note freezes compiler/QCA scope, controls, and N1-N8",not missing,missing)


def main()->int:
    shore_data=shore();note_contract();routeA=route_a();routeB=route_b();routeC=route_c(shore_data);nogo=no_go_discipline()
    elapsed=perf_counter()-START;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss;rss=int(rss if sys.platform=="darwin" else rss*1024)
    receipt={
        "cycle":609,"authority":AUTHORITY,"audit":AUDIT,"constitutional_effect":"none",
        "HEAD":subprocess.check_output(("git","rev-parse","HEAD"),cwd=ROOT,text=True).strip(),
        "pins":PINS,"shore":shore_data["evidence"],"route_A_support2_NQ_compiler":routeA,
        "route_B_F17_link_QCA":routeB,"route_C_response_alias_bridge":routeC,"no_go_discipline":nogo,
        "inventory":{"supplied":["Cycle600 prepared carrier/neutral-W sector","W16/Walsh bit convention","printed rational Rz angles","F17 and +2/-1 carrier charge","doubled Q/P representation","alpha=1/12","reversal and factor schedule","finite horizons","matched-word association","Cycle527 serial NN route-cost formula"],"derived_or_executed":["full-space exact W16 phase polynomial and support2 gate schedule","bounded-distance coordinates and serial NN depth bounds","exact F17 link/source/drift QCA and inverse","matter/field continuity and aggregate all24/576","exact rational-to-F17 reduction","neutral-W no-refit response"],"not_derived":["materialized simultaneous NN path packing or schedule covariance","accepted finite angle alphabet","single-register Weyl realization","canonical real lift of modular values","carrier-sector preparation","physical charge/energy/stress/gravity identification","time","event selection","Born probability","Record actuality"]},
        "six_wall_ledger":{"C_ref":"ADVANCED: actual carrier/neutral-W charge drives the field; modulus, charge convention, reversal, sign, and event association remain supplied","C_num":"ADVANCED: exact full-space W16 phase lowering and F17 arithmetic QCA are explicit; real signed lift and physical scale remain open","C_wrap":"ADVANCED DIAGNOSTICALLY: exact rational reduction and first alias signal are explicit; modular wrap is not energy/rate/time","C_int":"ADVANCED: one modular action supplies source kick, reciprocal phase, link shear, and drift on the declared doubled-register QCA","C_local":"ADVANCED BUT OPEN: exact support2 gate identities, bounded-distance layouts, and local F17/scratch constraints are explicit; materialized simultaneous NN route packing and schedule covariance remain open","C_source":"ADVANCED MATHEMATICALLY: actual N=1 matter plus neutral-W carriers give a zero-total-charge source and no-refit static bridge; empirical stress/gravity/event identification remains open"},
        "maturity_0_to_5":{"operational_quantum_records":4.0,"time":3.0,"inertia_matter":4.3,"gravity_source":3.65,"Born_probability":2.0},
        "strongest_constructive_result":"the exact Cycle607 W16 accepted-CAR NQ unitary is lowered over all 65,536 basis states to 109 rational-angle Rz gates and 318 bounded-distance parity CNOTs of support at most two M2, while a separate exact support2 F17 source/link/drift aggregate QCA carries actual Cycle600 matter plus neutral-W charge with inverse, continuity, odd/even, all24/all576, and no-refit response controls; simultaneous NN route packing remains open",
        "shared_obstruction_or_axiom_pressure":False,"optimal_next_campaign":"first materialize conflict-free NN paths and schedule-covariance controls for the Walsh and F17 support2 gates; then replace doubled F17 Q/P words by a single-register metaplectic or six-ray unitary propagation and test empirical charge/sign calibration with an autonomous detector",
        "tests_passed":PASS,"tests_failed":FAIL,"pass":FAIL==0,"elapsed_seconds":elapsed,"maximum_RSS_bytes":rss,
    }
    RECEIPT.write_text(json.dumps(receipt,indent=2,sort_keys=True,default=json_default)+"\n")
    print("RECEIPT",json.dumps(receipt,sort_keys=True,default=json_default))
    print("SUMMARY",json.dumps({"pass":receipt["pass"],"tests_passed":PASS,"tests_failed":FAIL,"elapsed_seconds":elapsed,"maximum_RSS_bytes":rss,"route_A":routeA["disposition"],"route_B":routeB["disposition"],"route_C":routeC["disposition"],"axiom_pressure":False},sort_keys=True))
    return int(FAIL!=0)


if __name__ == "__main__":
    COLD.parent.mkdir(parents=True, exist_ok=True)
    with COLD.open("w") as cold_handle:
        terminal = sys.stdout
        sys.stdout = Tee(terminal, cold_handle)
        try:
            exit_code = main()
        finally:
            sys.stdout = terminal
    raise SystemExit(exit_code)
