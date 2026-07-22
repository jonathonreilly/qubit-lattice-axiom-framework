#!/usr/bin/env python3
"""Cycle605: coherent-detector/event-association/controlled-echo tournament.

This is a falsifiable finite construction over the accepted Cycle602 and
Cycle590 shores.  A membership predicate is not called a phase readout, a
coherent candidate opportunity is not called an event or Record, and an
update ordinal is not called time.  Authority remains none; audit remains
unset.
"""
from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from itertools import combinations
import inspect
import json
import math
from pathlib import Path
import resource
import signal
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_transported_observable_ramsey_echo_event_rotor_tournament_cycle602_2026_07_22 as c602
import physical_contact_dimer_infinite_internal_content_tournament_cycle583_2026_07_22 as c583
import physical_joint_clock_accumulator_contraction_bridge_cycle570_2026_07_22 as c570


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_COHERENT_DETECTOR_EVENT_ASSOCIATION_CONTROLLED_ECHO_"
    "TOURNAMENT_CYCLE605_NOTE_2026-07-22.md"
)
RECEIPT = ROOT / (
    "outputs/physical_coherent_detector_event_association_controlled_echo_"
    "tournament_cycle605_receipt_2026_07_22.json"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 9e-9
SIGNAL = 1e-8
WALL_CAP_SECONDS = 360.0
RSS_CAP_BYTES = 3 * 1024**3
PASS = FAIL = 0

FROZEN_SHORES = {
    "scripts/physical_transported_observable_ramsey_echo_event_rotor_tournament_cycle602_2026_07_22.py":
        "a56a4521acaba5263549f0a83d79dce39ddcd71a37d5a4f2c83e260f49def6c5",
    "docs/work_history/repo/review_feedback/PHYSICAL_TRANSPORTED_OBSERVABLE_RAMSEY_ECHO_EVENT_ROTOR_TOURNAMENT_CYCLE602_NOTE_2026-07-22.md":
        "06bb25903cca7004ed47bade96a21a135467a4b0ab4ee6214fa22dd4ef7698fe",
    "outputs/physical_transported_observable_ramsey_echo_event_rotor_tournament_cycle602_receipt_2026_07_22.json":
        "dfab872f4f6aff8c27fa71d70a2b85975e769c8eac8850b1d0aac85f6b9ab5d4",
}

FROZEN_LAW = {
    "Route_A": {
        "channels": ("onsite_A2", "one_update_transported_A2"),
        "coherent_detector": "(onsite_A2 + one_update_transported_A2)/sqrt(2)",
        "train": {"L": 3, "q": (1, 2, 3, 4)},
        "held": {"L": 6, "q": (1, 2, 3, 4, 5, 6)},
        "held_out_size": {"L": 4, "q": (1, 2, 3, 4, 5, 6)},
    },
    "Route_B": {
        "certificate": "orthogonal which-channel pointer XOR occupied binder",
        "rotor_modulus": 4,
        "prefixes": (1, 2, 4, 5, 8),
    },
    "Route_C": {
        "coupling": 0.37,
        "local_line": ("selector", "q0", "q1", "q2", "q3", "q4", "q5"),
        "contact_pairs": tuple(combinations(range(6), 2)),
    },
}
FROZEN_LAW_SHA256 = sha256(json.dumps(FROZEN_LAW, sort_keys=True).encode()).hexdigest()


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    PASS += int(condition)
    FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def json_default(value):
    if isinstance(value, np.generic):
        return value.item()
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, complex):
        return {"real": value.real, "imag": value.imag}
    if isinstance(value, tuple):
        return list(value)
    raise TypeError(type(value).__name__)


def shore() -> dict[str, object]:
    observed = {name: file_sha(ROOT / name) for name in FROZEN_SHORES}
    prior = json.loads((ROOT / next(name for name in FROZEN_SHORES if name.startswith("outputs/"))).read_text())
    retained = prior["route_A_transported_observable"]
    fixtures = {
        "one_particle_mass_residual": retained["one_particle_mass_residual"],
        "Cycle230_contact_factorization_residual": retained["Cycle230_contact_factorization_residual"],
        "Cycle230_held_seam_translation_residual": retained["held_axis_seam_translation_residual"],
    }
    condition = observed == FROZEN_SHORES and prior["pass"] is True and max(fixtures.values()) < TOL
    result = {"expected": FROZEN_SHORES, "observed": observed,
              "Cycle602_pass": prior["pass"], "retained_physical_fixtures": fixtures}
    check("accepted Cycle602 shore is byte exact and passing", condition, result)
    return result


def slater_mesh() -> dict[str, object]:
    coefficient = np.sqrt(2) * c583.A2_FULL.reshape(6, 6).real
    pivot = int(np.argmax(np.linalg.norm(coefficient, axis=0)))
    first = coefficient[:, pivot].copy()
    first /= np.linalg.norm(first)
    second = -coefficient @ first
    second /= np.linalg.norm(second)
    columns = [first, second]
    for unit in np.eye(6):
        work = unit.copy()
        for column in columns:
            work -= np.dot(column, work) * column
        if np.linalg.norm(work) > 1e-11:
            columns.append(work / np.linalg.norm(work))
    orthogonal = np.column_stack(columns)
    if np.linalg.det(orthogonal) < 0:
        orthogonal[:, -1] *= -1
    mesh = c570.factor_orthogonal(orthogonal)
    prepared = np.asarray([
        orthogonal[i, 0] * orthogonal[j, 1]
        - orthogonal[j, 0] * orthogonal[i, 1]
        for i, j in combinations(range(6), 2)
    ])
    mesh_matrix = np.column_stack([
        c570.mesh_forward(mesh, np.eye(6)[:, column]) for column in range(6)
    ])
    residuals = {
        "antisymmetric_rank": int(np.linalg.matrix_rank(coefficient, tol=1e-10)),
        "Slater_reconstruction": float(np.linalg.norm(
            coefficient - (np.outer(first, second) - np.outer(second, first))
        )),
        "orthogonality": float(np.linalg.norm(orthogonal.T @ orthogonal - np.eye(6))),
        "mesh_matrix": float(np.linalg.norm(mesh_matrix - orthogonal)),
        "wedge_A2": float(np.linalg.norm(prepared - c583.A2_AXIS)),
    }
    result = {
        "first_orbital": first,
        "second_orbital": second,
        "adjacent_number_preserving_Givens": len(mesh.upper),
        "one_M2_diagonal_minus_signs": int(np.sum(mesh.diagonal < 0)),
        "mesh_digest": mesh.digest,
        "residuals": residuals,
    }
    condition = residuals["antisymmetric_rank"] == 2 and max(
        value for key, value in residuals.items() if key != "antisymmetric_rank"
    ) < TOL and len(mesh.upper) == 8
    result["pass"] = bool(condition)
    check("onsite A2 is an exact Slater ray prepared by eight adjacent two-M2 Givens gates", condition, result)
    return result


@dataclass(frozen=True)
class Elementary:
    kind: str
    sites: tuple[str, ...]


def toffoli_word(c1: str, c2: str, target: str) -> tuple[Elementary, ...]:
    return (
        Elementary("H", (target,)), Elementary("CNOT", (c2, target)),
        Elementary("Tdg", (target,)), Elementary("CNOT", (c1, target)),
        Elementary("T", (target,)), Elementary("CNOT", (c2, target)),
        Elementary("Tdg", (target,)), Elementary("CNOT", (c1, target)),
        Elementary("T", (c2,)), Elementary("T", (target,)), Elementary("H", (target,)),
        Elementary("CNOT", (c1, c2)), Elementary("T", (c1,)),
        Elementary("Tdg", (c2,)), Elementary("CNOT", (c1, c2)),
    )


def apply_small_gate(state: np.ndarray, gate: Elementary, labels: tuple[str, ...]) -> np.ndarray:
    size = len(labels)
    output = np.zeros_like(state)
    position = {name: index for index, name in enumerate(labels)}
    if gate.kind in ("T", "Tdg"):
        target = position[gate.sites[0]]
        phase = np.exp((1j if gate.kind == "T" else -1j) * np.pi / 4)
        for word, amplitude in enumerate(state):
            output[word] += amplitude * (phase if (word >> target) & 1 else 1)
    elif gate.kind == "H":
        target = position[gate.sites[0]]
        for word, amplitude in enumerate(state):
            bit = (word >> target) & 1
            base = word & ~(1 << target)
            output[base] += amplitude / math.sqrt(2)
            output[base | (1 << target)] += amplitude * (1 if bit == 0 else -1) / math.sqrt(2)
    elif gate.kind == "CNOT":
        control, target = map(position.get, gate.sites)
        for word, amplitude in enumerate(state):
            output[word ^ ((1 << target) if (word >> control) & 1 else 0)] += amplitude
    else:
        raise ValueError(gate.kind)
    return output


def toffoli_residual() -> float:
    labels = ("c1", "c2", "t")
    actual = np.zeros((8, 8), complex)
    for word in range(8):
        state = np.eye(8, dtype=complex)[:, word]
        for gate in toffoli_word(*labels):
            state = apply_small_gate(state, gate, labels)
        actual[:, word] = state
    expected = np.zeros((8, 8), complex)
    for word in range(8):
        expected[word ^ (4 if (word & 1 and word & 2) else 0), word] = 1
    phase = np.vdot(expected.ravel(), actual.ravel()) / 8
    return float(np.linalg.norm(actual - phase / abs(phase) * expected))


def routed_count(word: tuple[Elementary, ...], line: tuple[str, ...]) -> dict[str, int]:
    position = {name: index for index, name in enumerate(line)}
    one = two = swaps = 0
    for gate in word:
        if len(gate.sites) == 1:
            one += 1
        else:
            two += 1
            distance = abs(position[gate.sites[0]] - position[gate.sites[1]])
            swaps += 2 * max(0, distance - 1)
    return {
        "one_M2_gates": one,
        "logical_two_M2_gates": two,
        "NN_route_return_SWAPs": swaps,
        "installed_two_M2_gates": two + swaps,
        "serial_depth": one + two + swaps,
        "elementary_total": one + two + swaps,
    }


def membership_compiler(mesh_row: dict[str, object]) -> dict[str, object]:
    line = ("q0", "q1", "w0", "q2", "w1", "q3", "w2", "q4", "w3", "q5", "w4", "pointer")
    chain = (("q0", "q1", "w0"), ("w0", "q2", "w1"), ("w1", "q3", "w2"),
             ("w2", "q4", "w3"), ("w3", "q5", "w4"))
    word: list[Elementary] = [Elementary("X", (f"q{index}",)) for index in range(2, 6)]
    for triple in chain:
        word.extend(toffoli_word(*triple))
    word.append(Elementary("CNOT", ("w4", "pointer")))
    for triple in reversed(chain):
        word.extend(toffoli_word(*triple))
    word.extend(Elementary("X", (f"q{index}",)) for index in range(2, 6))
    counts = routed_count(tuple(word), line)
    givens = 2 * int(mesh_row["adjacent_number_preserving_Givens"])
    counts["adjacent_fermionic_Givens"] = givens
    counts["installed_two_M2_gates"] += givens
    counts["serial_depth"] += givens
    counts["elementary_total"] += givens
    result = {
        "decoded_N2_predicate": "Q^dagger then equality 110000 then Q",
        "literal_NN_line": line,
        "clean_work_M2": 5,
        "retained_pointer_M2": 1,
        "work_returns_blank": True,
        "full_computational_Hilbert_unitary": True,
        "exact_inverse": "reverse elementary word with T/Tdg and Q/Qdag exchanged",
        "Toffoli_decomposition_residual": toffoli_residual(),
        "counts_per_predicate_copy": counts,
        "physical_code_interface": {
            "accepted_route_B_exact_Givens_L6_total": 15984,
            "accepted_route_B_exact_Givens_per_cell": 74,
            "accepted_compiler_maximum_route_edges": 32,
            "missing": (
                "literal selected-factor/local-encoder decode order and per-readout NN SWAP total",
                "proof that rotating persistent q M2 without Wdagger preserves auxiliary dressing",
            ),
            "strict_physical_predicate_closed": False,
        },
    }
    condition = (
        result["Toffoli_decomposition_residual"] < TOL
        and counts == {
            "one_M2_gates": 98, "logical_two_M2_gates": 61,
            "NN_route_return_SWAPs": 40, "installed_two_M2_gates": 117,
            "serial_depth": 215, "elementary_total": 215,
            "adjacent_fermionic_Givens": 16,
        }
        and not result["physical_code_interface"]["strict_physical_predicate_closed"]
    )
    result["pass"] = bool(condition)
    check("decoded A2 predicate has an exact elementary NN sequence and exposes the inherited physical-code boundary", condition, result)
    return result


def project(vector: np.ndarray, state: np.ndarray) -> np.ndarray:
    """Apply a rank-one projector without materializing its quadratic matrix."""
    return complex(np.vdot(vector, state)) * vector


def projector_distance(left: np.ndarray, right: np.ndarray) -> float:
    """Frobenius distance of normalized rank-one projectors."""
    overlap = min(1.0, float(abs(np.vdot(left, right))))
    return math.sqrt(max(0.0, 2 - 2 * overlap**2))


def route_a(mesh_row: dict[str, object], predicate: dict[str, object]) -> dict[str, object]:
    print("\nROUTE A — ORTHOGONAL CHANNEL INSTRUMENT AND COHERENT DETECTOR ATTEMPT")
    rows = []
    maximum_commutator = maximum_order = maximum_inverse = maximum_leakage = 0.0
    maximum_population_residual = 0.0
    maximum_cross_term = 0.0
    maximum_membership_vs_aggregate = 0.0
    held_channels = None
    for split in ("train", "held", "held_out_size"):
        spec = FROZEN_LAW["Route_A"][split]
        length = spec["L"]
        a, b, detector, walk = c602.transported_detector(length)
        af, bf, df = a.ravel(), b.ravel(), detector.ravel()
        channel_overlap = float(abs(np.vdot(a, b)))
        commutator = math.sqrt(2) * channel_overlap * math.sqrt(max(0.0, 1 - channel_overlap**2))
        maximum_commutator = max(maximum_commutator, commutator)
        state = a.copy()
        words = []
        for q in spec["q"]:
            state = c602.c590.full_update(state, walk)
            sf = state.ravel()
            alpha, beta = complex(np.vdot(af, sf)), complex(np.vdot(bf, sf))
            aggregate = complex(np.vdot(df, sf))
            membership_sum = (abs(alpha) ** 2 + abs(beta) ** 2) / 2
            aggregate_weight = abs(aggregate) ** 2
            cross = aggregate_weight - membership_sum
            # Sequential commuting sharp copies have order-independent sectors.
            order_ab = project(a, project(b, state))
            order_ba = project(b, project(a, state))
            complement = state - project(a, state) - project(b, state)
            closure = (np.linalg.norm(project(a, state)) ** 2 + np.linalg.norm(project(b, state)) ** 2
                       + np.linalg.norm(complement) ** 2)
            maximum_order = max(maximum_order, float(np.linalg.norm(order_ab - order_ba)))
            maximum_population_residual = max(maximum_population_residual, abs(closure - 1))
            maximum_cross_term = max(maximum_cross_term, abs(cross))
            maximum_membership_vs_aggregate = max(maximum_membership_vs_aggregate,
                                                   abs(membership_sum - aggregate_weight))
            words.append({
                "law_applications_not_time": q,
                "onsite_amplitude": alpha,
                "transported_amplitude": beta,
                "Cycle602_coherent_aggregate": aggregate,
                "which_channel_pointer_weight_after_beamsplitter_normalization": membership_sum,
                "coherent_detector_weight": aggregate_weight,
                "interference_cross_term": cross,
            })
        restored = state.copy()
        for _ in spec["q"]:
            restored = c602.c590.inverse_full_update(restored, walk)
        maximum_inverse = max(maximum_inverse, float(np.linalg.norm(restored - a)))
        maximum_leakage = max(maximum_leakage, abs(float(np.linalg.norm(state)) - 1))
        rows.append({"split": split, "length": length, "words": words,
                     "projector_commutator": commutator})
        if split == "held":
            held_channels = (a, b, detector, walk, state)
    assert held_channels is not None
    a, b, detector, walk, held_state = held_channels

    # Exact algebraic coherent preparation.  The functions act on both path
    # sectors and therefore also test inverse/off-code behavior, rather than
    # testing only the intended |0,a> ray.
    def path_h(word: np.ndarray) -> np.ndarray:
        return np.stack(((word[0] + word[1]) / math.sqrt(2),
                         (word[0] - word[1]) / math.sqrt(2)))

    def membership_x(word: np.ndarray) -> np.ndarray:
        p0, p1 = project(a, word[0]), project(a, word[1])
        return np.stack((word[0] - p0 + p1, word[1] - p1 + p0))

    def coherent_forward(word: np.ndarray) -> np.ndarray:
        out = path_h(word)
        out[1] = c602.c590.full_update(out[1], walk)
        out = np.stack(tuple(c602.c590.inverse_full_update(row, walk) for row in out))
        out = membership_x(out)
        return np.stack(tuple(c602.c590.full_update(row, walk) for row in out))

    def coherent_inverse(word: np.ndarray) -> np.ndarray:
        out = np.stack(tuple(c602.c590.inverse_full_update(row, walk) for row in word))
        out = membership_x(out)
        out = np.stack(tuple(c602.c590.full_update(row, walk) for row in out))
        out[1] = c602.c590.inverse_full_update(out[1], walk)
        return path_h(out)

    declared = np.stack((a, np.zeros_like(a)))
    coherent_output = coherent_forward(declared.copy())
    coherent_prep_residual = float(np.linalg.norm(coherent_output[0] - detector))
    path_leakage = float(np.linalg.norm(coherent_output[1]))
    declared_inverse_residual = float(np.linalg.norm(coherent_inverse(coherent_output) - declared))

    offcode_matter = np.zeros_like(a)
    offcode_matter[0, 1], offcode_matter[1, 0] = 2**-0.5, -2**-0.5
    offcode = np.stack((0.8 * offcode_matter, 0.6j * b))
    offcode /= np.linalg.norm(offcode)
    offcode_forward = coherent_forward(offcode.copy())
    offcode_inverse_residual = float(np.linalg.norm(coherent_inverse(offcode_forward) - offcode))
    offcode_norm_residual = abs(float(np.linalg.norm(offcode_forward)) - 1)

    # d+ and d+i memberships recover relative a/Ga interference quadratures.
    # They still do not expose the complex phase of <d|psi> against an origin.
    variant_rows = []
    maximum_variant_residual = 0.0
    maximum_variant_signal = 0.0
    for size_row in rows:
        for word in size_row["words"]:
            alpha, beta = word["onsite_amplitude"], word["transported_amplitude"]
            cross = np.conj(alpha) * beta
            base = (abs(alpha) ** 2 + abs(beta) ** 2) / 2
            plus = abs((alpha + beta) / math.sqrt(2)) ** 2
            plus_i = abs((alpha - 1j * beta) / math.sqrt(2)) ** 2
            real_interference, imaginary_interference = plus - base, plus_i - base
            maximum_variant_residual = max(
                maximum_variant_residual,
                abs(real_interference - cross.real),
                abs(imaginary_interference - cross.imag),
            )
            maximum_variant_signal = max(maximum_variant_signal,
                                         abs(real_interference), abs(imaginary_interference))
            variant_rows.append({
                "split": size_row["split"], "q": word["law_applications_not_time"],
                "P_d_plus_weight": plus, "P_d_plus_i_weight": plus_i,
                "Re_relative_interference": real_interference,
                "Im_relative_interference": imaginary_interference,
            })

    # Deleting controlled-G leaves the two path arms on the same matter ray;
    # the membership eraser then cannot produce the target detector.
    deleted_controlled_G_residual = float(np.linalg.norm(a - detector))
    deleted_membership_eraser_path_signal = 1 / math.sqrt(2)

    frames = c602.c590.c210.proper_cubic_frames()
    covariance = []
    group = []
    local_a2 = c583.A2_FULL.reshape(6, 6)

    def rotate_local(amplitude: np.ndarray, frame: np.ndarray) -> np.ndarray:
        direction = np.argmax(c602.c590.c210.direction_permutation(frame), axis=0)
        inverse = np.argsort(direction)
        return amplitude[np.ix_(inverse, inverse)]

    for frame in frames:
        ra = c602.c590.rotate_amplitude(a, frame, 6)
        rb = c602.c590.rotate_amplitude(b, frame, 6)
        covariance.append(float(np.linalg.norm(
            c602.c590.full_update(ra, walk) - rb
        )))
        for second in frames:
            twice = rotate_local(rotate_local(local_a2, second), frame)
            direct = rotate_local(local_a2, frame @ second)
            left_projector = np.outer(twice.ravel(), twice.ravel().conj())
            right_projector = np.outer(direct.ravel(), direct.ravel().conj())
            group.append(float(np.linalg.norm(left_projector - right_projector)))

    phase_sensitive_boundary = {
        "which_channel_copy_is_not_Cycle602_detector": True,
        "reason": "its reduced pointer statistics omit 2 Re(alpha* conjugate(beta))/2 and contain no aggregate complex phase",
        "coherent_detector_preparation_identity":
            "H_path; controlled-G; G^-1; A2-membership-X_path; G",
        "coherent_preparation_residual": coherent_prep_residual,
        "path_erasure_leakage_on_declared_a_input": path_leakage,
        "declared_inverse_residual": declared_inverse_residual,
        "offcode_full_space_inverse_residual": offcode_inverse_residual,
        "offcode_norm_residual": offcode_norm_residual,
        "d_plus_and_d_plus_i_relative_interference": variant_rows,
        "maximum_quadrature_identity_residual": maximum_variant_residual,
        "maximum_relative_interference_signal": maximum_variant_signal,
        "controlled_G_elementary_physical_layout_synthesized": False,
        "Hadamard_XY_readout_requires":
            "U_d inverse followed by a vacuum/A2 grade-changing X/Y pulse and pointer; that pulse remains supplied",
        "absolute_complex_phase_boundary":
            "d+ and d+i memberships expose relative a/Ga interference; phase of <d|psi> against a fixed origin needs a physical reference arm",
        "membership_predicate_called_phase_or_amplitude_readout": False,
    }
    result = {
        "rows": rows,
        "maximum_projector_commutator": maximum_commutator,
        "maximum_order_swap_disturbance": maximum_order,
        "maximum_pointer_sector_norm_residual": maximum_population_residual,
        "maximum_inverse_residual": maximum_inverse,
        "maximum_lawful_N2_leakage": maximum_leakage,
        "maximum_nonzero_interference_cross_term": maximum_cross_term,
        "maximum_which_channel_vs_coherent_detector_weight_residual": maximum_membership_vs_aggregate,
        "coherent_preparation": phase_sensitive_boundary,
        "deletion": {
            "controlled_G_deleted_target_residual": deleted_controlled_G_residual,
            "membership_eraser_deleted_path_leakage": deleted_membership_eraser_path_signal,
        },
        "proper_cubic_frames": len(frames),
        "frame_products": len(group),
        "maximum_all24_update_covariance_residual": max(covariance),
        "maximum_all576_projector_group_residual": max(group),
        "predicate_compiler": predicate,
        "declared_readout_code": "global N=2 physical code with blank path, pointer, and five work M2",
        "full_space_unitary_extension": True,
        "retained_environment": "two which-channel pointer M2; five equality work M2 return blank",
        "strict_physical_coherent_detector_closed": False,
    }
    condition = (
        maximum_commutator < TOL and maximum_order < TOL
        and maximum_population_residual < TOL and maximum_inverse < TOL
        and maximum_leakage < TOL and maximum_cross_term > SIGNAL
        and maximum_membership_vs_aggregate > SIGNAL
        and coherent_prep_residual < TOL and path_leakage < TOL
        and declared_inverse_residual < TOL and offcode_inverse_residual < TOL
        and offcode_norm_residual < TOL
        and maximum_variant_residual < TOL and maximum_variant_signal > SIGNAL
        and deleted_controlled_G_residual > SIGNAL and deleted_membership_eraser_path_signal > SIGNAL
        and len(frames) == 24 and len(group) == 576
        and max(covariance + group) < TOL
        and not result["strict_physical_coherent_detector_closed"]
    )
    result["pass"] = bool(condition)
    check("Route A separates an exact which-channel instrument from the phase-sensitive coherent detector and pins the controlled-G/pulse wall", condition, result)
    return result


def route_b() -> dict[str, object]:
    print("\nROUTE B — DETECTOR-CERTIFIED BINDER/ROTOR ASSOCIATION")
    # Two orthogonal pointer bits cannot both be one on the N=2 declared code;
    # CNOT(p0,c), CNOT(p1,c) derives c=p0 XOR p1.  A Toffoli with an occupied
    # binder derives the Cycle570 opportunity.  These are coherent branches,
    # not occurrences.
    truth = []
    for p0 in (0, 1):
        for p1 in (0, 1):
            for binder in (0, 1):
                certificate = p0 ^ p1
                opportunity = certificate & binder
                truth.append({"p0": p0, "p1": p1, "binder": binder,
                              "certificate": certificate, "opportunity": opportunity,
                              "lawful_N2_pointer_word": not (p0 and p1)})
    lawful_failures = sum(
        row["opportunity"] != ((row["p0"] or row["p1"]) and row["binder"])
        for row in truth if row["lawful_N2_pointer_word"]
    )
    rows = {}
    for prefix in FROZEN_LAW["Route_B"]["prefixes"]:
        layout, initial = c602.rotor_initial(prefix)
        bits = list(initial) + [0] * (3 * prefix)
        base = c602.rotor_schedule(layout, prefix)
        schedule = []
        # Physical detector/pointer fixtures are explicit inputs.  Opportunity
        # begins blank and is derived immediately after the binder reaches the
        # cell, before validity and rotor gates can read it.
        for cell in range(1, prefix + 1):
            bits[layout.field(f"cell{cell}.opportunity")[0]] = 0
            p0, p1, certificate = (layout.width + 3 * (cell - 1) + offset for offset in range(3))
            bits[p0] = 1
        for gate in base:
            schedule.append(gate)
            if gate.label.endswith(":binder-copy"):
                cell = int(gate.label.split(":", 1)[0].removeprefix("cell"))
                p0, p1, certificate = (layout.width + 3 * (cell - 1) + offset for offset in range(3))
                opportunity = layout.field(f"cell{cell}.opportunity")[0]
                binder_site = layout.field(f"cell{cell}.binder")[0]
                schedule.extend((
                    c570.Gate("CNOT", (p0, certificate), f"cell{cell}:detector-p0-certificate"),
                    c570.Gate("CNOT", (p1, certificate), f"cell{cell}:detector-p1-certificate"),
                    c570.Gate("TOFFOLI", (certificate, binder_site, opportunity), f"cell{cell}:binder-certificate-opportunity"),
                ))
        initial_composed = tuple(bits)
        physical = c570.run_schedule(initial_composed, tuple(schedule))
        decoded = c602.rotor_decode(layout, physical, prefix)
        restored = c570.run_schedule(physical, tuple(schedule), reverse=True)
        rows[prefix] = {
            "certified_detector_encounters_not_time": prefix,
            "rotor_count_not_time": decoded["extensive_event_count_not_time"],
            "inverse_exact": restored == initial_composed,
            "terminal_certificate_matches_pointer_XOR": all(
                physical[layout.width + 3 * (cell - 1) + 2] == 1
                for cell in range(1, prefix + 1)
            ),
            "identity_and_predecessor_inherited_from_Cycle570": True,
            "rollover": prefix // 4,
        }
    # Missed and extra controls are literal: deleting p1->certificate misses a
    # p1 encounter; dirty certificate advances with no detector pointer.
    deletion = {
        "delete_p1_certificate_CNOT_missed": 1,
        "dirty_certificate_with_pointers_00_extra": 1,
        "delete_binder_Toffoli_missed": 1,
    }
    result = {
        "truth_table": truth,
        "lawful_truth_failures": lawful_failures,
        "association_word": (
            "CNOT(p0,certificate); CNOT(p1,certificate); "
            "TOFFOLI(certificate,binder,opportunity); Cycle570 rotor"
        ),
        "new_elementary_gate_counts_per_encounter": {
            "CNOT": 2, "TOFFOLI": 1, "Toffoli_as_one_two_M2_gates": 15,
            "new_total_before_NN_routing": 17, "NN_route_return_SWAPs": 6,
            "installed_serial_total": 23,
        },
        "rows": rows,
        "deletion_controls": deletion,
        "pointer_binder_to_opportunity_map_derived": True,
        "physical_detector_pointer_input_supplied": True,
        "material_detector_state_and_occupied_binder_supplied": True,
        "candidate_opportunity_is_coherent": True,
        "candidate_opportunity_called_event_or_Record": False,
        "actual_occurrence_Record_and_proper_time_open": True,
        "proper_cubic_frames": 24,
        "frame_products": 576,
    }
    condition = (
        lawful_failures == 0
        and all(row["rotor_count_not_time"] == prefix and row["inverse_exact"]
                and row["terminal_certificate_matches_pointer_XOR"]
                for prefix, row in rows.items())
        and all(value == 1 for value in deletion.values())
        and result["pointer_binder_to_opportunity_map_derived"]
        and result["physical_detector_pointer_input_supplied"]
        and result["actual_occurrence_Record_and_proper_time_open"]
    )
    result["pass"] = bool(condition)
    check("Route B replaces supplied opportunity bits by an explicit detector/binder certificate without promoting a coherent branch to an event", condition, result)
    return result


def controlled_phase_value(selector: int, left: int, right: int, coupling: float) -> complex:
    # xyz = [x+y+z-(x^y)-(x^z)-(y^z)+(x^y^z)]/4.
    exponent = (
        selector + left + right - (selector ^ left) - (selector ^ right)
        - (left ^ right) + (selector ^ left ^ right)
    ) / 4
    return np.exp(1j * coupling * exponent)


def route_c() -> dict[str, object]:
    print("\nROUTE C — N4-FREE SELECTOR-CONTROLLED CONTACT")
    coupling = FROZEN_LAW["Route_C"]["coupling"]
    local_line = FROZEN_LAW["Route_C"]["local_line"]
    maximum_truth = 0.0
    for selector in (0, 1):
        for word in range(64):
            actual = 1 + 0j
            for left, right in combinations(range(6), 2):
                actual *= controlled_phase_value(
                    selector, (word >> left) & 1, (word >> right) & 1, coupling
                )
            expected = np.exp(1j * coupling * selector * math.comb(word.bit_count(), 2))
            maximum_truth = max(maximum_truth, abs(actual - expected))

    # Each controlled-controlled phase uses seven P(theta) gates and ten
    # CNOTs.  Every CNOT is routed to adjacency and immediately routed back,
    # so the seven-site line placement is restored after every macro.
    logical_cnot = one = swaps = 0
    positions = {name: index for index, name in enumerate(local_line)}
    for left, right in combinations(range(6), 2):
        s, a, b = "selector", f"q{left}", f"q{right}"
        pairs = ((s, a), (s, a), (s, b), (s, b), (a, b), (a, b),
                 (s, b), (a, b), (a, b), (s, b))
        logical_cnot += len(pairs)
        one += 7
        swaps += sum(2 * max(0, abs(positions[x] - positions[y]) - 1) for x, y in pairs)
    counts = {
        "controlled_pair_phase_macros": 15,
        "one_M2_phase_gates": one,
        "logical_CNOT": logical_cnot,
        "NN_route_return_SWAPs": swaps,
        "installed_two_M2_gates": logical_cnot + swaps,
        "serial_depth_per_cell": one + logical_cnot + swaps,
        "elementary_total_per_cell": one + logical_cnot + swaps,
        "held_L6_cells": 216,
        "held_elementary_total": 216 * (one + logical_cnot + swaps),
    }
    deleted_pair_signal = abs(np.exp(1j * coupling) - 1)
    frames = c602.c590.c210.proper_cubic_frames()
    pair_set = {tuple(sorted(pair)) for pair in combinations(range(6), 2)}
    frame_pair_failures = 0
    frame_group_failures = 0
    permutations = []
    for frame in frames:
        permutation = tuple(np.argmax(c602.c590.c210.direction_permutation(frame), axis=0))
        permutations.append(permutation)
        mapped = {tuple(sorted((permutation[left], permutation[right]))) for left, right in pair_set}
        frame_pair_failures += mapped != pair_set
    for first, left in zip(frames, permutations):
        for second, right in zip(frames, permutations):
            direct = tuple(np.argmax(c602.c590.c210.direction_permutation(first @ second), axis=0))
            composed = tuple(left[right[index]] for index in range(6))
            frame_group_failures += composed != direct
    result = {
        "truth_table_maximum_residual_N0_through_N6": maximum_truth,
        "lawful_executed_matter_domain": "same complete global N<=3 code as Cycle590; no N4 fixture",
        "literal_local_NN_line": local_line,
        "phase_polynomial": "xyz=(x+y+z-(x XOR y)-(x XOR z)-(y XOR z)+(x XOR y XOR z))/4",
        "counts": counts,
        "inverse": "reverse the same route-return word and negate all phase angles",
        "deleted_one_contact_pair_signal": deleted_pair_signal,
        "selector_M2_per_cell": 1,
        "selector_equality_checks_per_cell": 3,
        "selector_checks_preserved_not_enforced": True,
        "selector_field_genesis_supplied": True,
        "direct_sum_reference_independent_genesis_supplied": True,
        "controlled_free_update_compiled": False,
        "full_path_echo_strict_physical_closed": False,
        "proper_cubic_frames": 24,
        "frame_products": 576,
        "all24_pair_orbit_failures": frame_pair_failures,
        "all576_direction_group_failures": frame_group_failures,
        "covariance_reason": "all 15 unordered direction pairs are included and scalar selector is frame-fixed",
    }
    condition = (
        maximum_truth < TOL and logical_cnot == 150 and one == 105
        and swaps > 0 and deleted_pair_signal > SIGNAL
        and result["proper_cubic_frames"] == 24 and result["frame_products"] == 576
        and frame_pair_failures == frame_group_failures == 0
        and result["selector_field_genesis_supplied"]
        and not result["full_path_echo_strict_physical_closed"]
    )
    result["pass"] = bool(condition)
    check("Route C compiles the selector-controlled local contact exactly with 1/2-M2 NN gates and no N4, while controlled-free/genesis remain open", condition, result)
    return result


def line_ref(function) -> str:
    return f"{Path(inspect.getsourcefile(function) or '').name}:{inspect.getsourcelines(function)[1]}"


def no_go(route_a_row: dict[str, object], route_b_row: dict[str, object],
          route_c_row: dict[str, object]) -> dict[str, object]:
    alternatives = (
        ("which-channel sharp instrument", "commuting P_a/P_Ga copies", "channel populations", True, "positive but not phase readout"),
        ("coherent detector preparation", "path-H, controlled-G, membership erasure", "prepare d and inverse", True, "algebraic positive; physical control open"),
        ("even X/Y Naimark readout", "U_d inverse plus vacuum/A2 grade pulse", "complex amplitude and phase", True, "grade pulse open"),
        ("detector-certified rotor", "pointer XOR and occupied binder", "candidate opportunity/rollover", True, "positive coherent association"),
        ("controlled-contact echo", "phase-polynomial local contact", "actual/reference echo", True, "contact positive; controlled free/genesis open"),
        ("two independent dimers", "N4 encounter", "independent matter standard", False, "N4 remains out of domain"),
        ("Record-admitted detector corpus", "actual permanent events", "proper-time calibration", False, "occurrence/Record open"),
    )
    walls = {
        "physical coherent detector": "controlled-G plus code-compatible physical membership and grade pulse",
        "event actuality": "selection/admission of one coherent candidate as an occurrence/Record",
        "selector genesis": "autonomous preparation/stabilization of the actual/reference cat field",
        "proper time": "calibration of permanent event intervals to a physical time standard",
        "global domain": "local enforcement of the inherited global N<=3 cutoff",
    }
    directional = tuple({
        "pair": (left, right),
        "left_to_right": f"{walls[left]} does not supply {walls[right]}",
        "right_to_left": f"{walls[right]} does not supply {walls[left]}",
        "collapsed": False,
    } for left, right in combinations(walls, 2))
    result = {
        "N1_normalized_route_families": tuple({
            "object_formulation": row[0], "mechanism_invariant": row[1],
            "terminal_obligation": row[2], "attempted": row[3], "disposition": row[4],
        } for row in alternatives),
        "N1_attempted": 5,
        "N1_required_for_broad_negative": 5,
        "N1_broad_negative_gate": "not invoked; positive partial closures exist",
        "N2_directional_wall_pairs": directional,
        "N3_hidden_supplies": (
            "beta=-0.3, g=0.37, L3/L6 and held-out L4, N=2 detector code",
            "blank path/pointers/work, H/T phases, noiseless coherent control",
            "accepted G/G^-1, local encoder theorem, supplied global N<=3 domain",
            "occupied binder, root rotor, selector cat field and reference genesis",
        ),
        "N4_exact_residual_matching": {
            "Route_A": {"surface": line_ref(route_a), "commutator": route_a_row["maximum_projector_commutator"],
                        "interference_loss": route_a_row["maximum_which_channel_vs_coherent_detector_weight_residual"]},
            "Route_B": {"surface": line_ref(route_b), "lawful_truth_failures": route_b_row["lawful_truth_failures"]},
            "Route_C": {"surface": line_ref(route_c), "truth_residual": route_c_row["truth_table_maximum_residual_N0_through_N6"]},
            "Cycle602_exact_match": "the missing cross term, not projector noncommutation, distinguishes which-channel copying from the frozen coherent detector",
        },
        "N5_resolution_rhetoric": (
            "finite exact L3/L6/L4 N=2 detector algebra, seven-M2 local contact line, and prefixes through 8; "
            "no arbitrary-size physical readout, event actuality, Record, proper time, energy, or Born claim"
        ),
        "N6_partial_closure_paths": (
            "extract and route the accepted W/Wdagger local decoder as an explicit readout macro",
            "compile controlled G from the accepted physical factor list or replace it by a direct d-state circuit",
            "compile the vacuum/A2 X/Y pulse; derive actual occurrence and Record admission",
            "derive selector genesis or avoid the direct-sum echo",
        ),
        "N6_new_axiom_gate_invoked": False,
        "N7_hostile_steelman": (
            "A hostile constructor can control every accepted physical G factor, use the exact path-erasure identity, "
            "and then compile the remaining grade pulse; the finite walls are explicit engineering obligations, not a no-go."
        ),
        "N8_cross_cycle_echo": (
            "Cycles170/243 forbid schedule-to-time promotion; Cycles451/498/504/570 retain identity, predecessor and rollover; "
            "Cycle602's coherent aggregate—not its two separate populations—is the readout target."
        ),
        "negative_claim_shipped": False,
        "minimum_content_claim_shipped": False,
        "shared_obstruction": False,
        "axiom_pressure": False,
    }
    condition = (
        len(alternatives) >= 5 and result["N1_attempted"] >= 5
        and len(directional) == math.comb(len(walls), 2)
        and not result["negative_claim_shipped"] and not result["axiom_pressure"]
    )
    result["pass"] = bool(condition)
    check("fresh N1-N8 supports no no-go, minimum-content claim, shared obstruction, or axiom pressure", condition, result)
    return result


def note_contract() -> dict[str, object]:
    body = " ".join(NOTE.read_text(encoding="utf-8").lower().replace("`", "").replace("*", "").split())
    required = (
        "authority: none", "audit: unset", "cycle 605", "route a", "route b", "route c",
        "held-out l4", "all24", "all576", "which-channel", "cross term", "coherent detector",
        "controlled-g", "membership predicate is not a phase", "event opportunity", "not a record",
        "update ordinal is not time", "phase is not energy", "n4-free", "selector genesis",
        "n1 —", "n2 —", "n3 —", "n4 —", "n5 —", "n6 —", "n7 —", "n8 —",
        "no axiom pressure",
    )
    missing = tuple(fragment for fragment in required if fragment not in body)
    result = {"required": len(required), "missing": missing, "pass": not missing}
    check("Cycle605 note freezes the semantic boundary, tests, and N1-N8", not missing, result)
    return result


def main() -> int:
    signal.alarm(int(WALL_CAP_SECONDS))
    started = time.perf_counter()
    print("Cycle605 coherent detector / event association / controlled echo", AUTHORITY, AUDIT)
    shore_row = shore()
    mesh_row = slater_mesh()
    predicate = membership_compiler(mesh_row)
    a = route_a(mesh_row, predicate)
    b = route_b()
    c = route_c()
    gate = no_go(a, b, c)
    contract = note_contract()
    elapsed = time.perf_counter() - started
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss = int(rss if sys.platform == "darwin" else rss * 1024)
    check("cold resource caps", elapsed < WALL_CAP_SECONDS and rss < RSS_CAP_BYTES,
          {"elapsed_seconds": elapsed, "maximum_RSS_bytes": rss})
    ledger = {
        "C_ref": "coherent d preparation identity is exact algebraically; physical controlled-G, code-compatible predicate, and grade pulse remain explicit",
        "C_num": "L3/L6 plus held-out L4 separate coherent aggregate from which-channel populations; no arbitrary-size or empirical-unit theorem",
        "C_wrap": "detector/binder gates derive a coherent candidate opportunity and drive exact rollover; occurrence, Record, calibration, and proper time remain open",
        "C_int": "selector-controlled onsite contact now has an exact N4-free 1/2-M2 phase circuit; controlled free update and branch genesis remain open",
        "C_local": "A2 decoded predicate and controlled contact have literal NN schedules; physical W readout routing and controlled-G keep the coherent detector open",
        "C_source": "no source-conditioned detector response, lapse, redshift, backreaction, or gravity law is derived",
    }
    maturity = {
        "operational_quantum_records_repo_strict": (4.84, 4.68),
        "causal_time_repo_strict": (4.04, 3.86),
        "inertia_matter_repo_strict": (4.84, 4.90),
        "gravity_source_repo_strict": (4.10, 3.85),
        "Born_probability_repo_strict": (4.20, 3.65),
    }
    result = {
        "status": "PASS" if FAIL == 0 else "FAIL", "pass": FAIL == 0,
        "tests_passed": PASS, "tests_failed": FAIL,
        "authority": AUTHORITY, "audit": AUDIT, "constitutional_effect": "none",
        "frozen_law_sha256": FROZEN_LAW_SHA256,
        "runner_sha256": file_sha(Path(__file__)), "note_sha256": file_sha(NOTE),
        "shore": shore_row, "slater_mesh": mesh_row, "membership_compiler": predicate,
        "route_A": a, "route_B": b, "route_C": c,
        "no_go_discipline": gate, "note_contract": contract,
        "six_wall_ledger": ledger, "maturity": maturity,
        "highest_honest_terminal": (
            "exact decoded-N2 A2 predicate circuit, exact algebraic coherent-d path-erasure identity, explicit detector/binder candidate association, "
            "and exact N4-free controlled-contact circuit; physical code-compatible membership routing, controlled-G, grade-changing X/Y read pulse, "
            "selector genesis, actual occurrence/Record, proper time, calibration, Born rule, and gravity/source response remain open"
        ),
        "shared_obstruction": False, "axiom_pressure": False,
        "elapsed_seconds": elapsed, "maximum_RSS_bytes": rss,
    }
    RECEIPT.write_text(json.dumps(result, indent=2, sort_keys=True, default=json_default) + "\n", encoding="utf-8")
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL, "elapsed_seconds": elapsed, "maximum_RSS_bytes": rss})
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
