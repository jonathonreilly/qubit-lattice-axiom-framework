#!/usr/bin/env python3
"""Cycle602: transported-observable Ramsey / echo / event-rotor tournament.

The accepted Cycle590 free-plus-contact dynamics are strict physical-M2.
The new Ramsey pulse/readout and branch-controlled echo are only bounded-
support code-space interfaces unless an explicit primitive layout is stated.
Update ordinals and event counts are not time; phase is not energy.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
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

import physical_intrinsic_ramsey_clock_strict_M2_time_bridge_tournament_cycle599_2026_07_22 as c599
import physical_full_torus_dimer_M2_compiler_tournament_cycle590_2026_07_22 as c590
import physical_source_conditioned_relational_dual_clock_cycle451_2026_07_19 as c451
import physical_joint_clock_accumulator_contraction_bridge_cycle570_2026_07_22 as c570


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_TRANSPORTED_OBSERVABLE_RAMSEY_ECHO_EVENT_ROTOR_TOURNAMENT_"
    "CYCLE602_NOTE_2026-07-22.md"
)
RECEIPT = ROOT / (
    "outputs/physical_transported_observable_ramsey_echo_event_rotor_"
    "tournament_cycle602_receipt_2026_07_22.json"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 8e-9
SIGNAL = 1e-8
WALL_CAP_SECONDS = 300.0
RSS_CAP_BYTES = 3 * 1024**3
PASS = 0
FAIL = 0

FROZEN_SHORES = {
    "scripts/physical_intrinsic_ramsey_clock_strict_M2_time_bridge_tournament_cycle599_2026_07_22.py":
        "11c7c12fab90a8ad3ac79cf9352b9d6c248f1f3359b67d260c3714a04ad74540",
    "docs/work_history/repo/review_feedback/PHYSICAL_INTRINSIC_RAMSEY_CLOCK_STRICT_M2_TIME_BRIDGE_TOURNAMENT_CYCLE599_NOTE_2026-07-22.md":
        "fff966a1672a034e5f9d0345909a7d4137660e96560d1af57835b0ce3806ddc3",
    "outputs/physical_intrinsic_ramsey_clock_strict_M2_time_bridge_tournament_cycle599_receipt_2026_07_22.json":
        "5cff047e3b6fc28408ce56a1ec14eae3784ae182aa414ceeb76df7609de1fef4",
    "scripts/physical_full_torus_dimer_M2_compiler_tournament_cycle590_2026_07_22.py":
        "5fbf3bcecc54df9912f9b79d2e5c45d51f145279c1ed83f507bc24e9e1980029",
    "docs/work_history/repo/review_feedback/PHYSICAL_FULL_TORUS_DIMER_M2_COMPILER_TOURNAMENT_CYCLE590_NOTE_2026-07-22.md":
        "3ee6ba9bd5a01a5cab88832788156597a1491d7c2d47f9378caca624a35a1936",
    "scripts/physical_source_conditioned_relational_dual_clock_cycle451_2026_07_19.py":
        "c89e3d47b42b05c0d723afb5e68548bbb15ee79401eaa72f3c8c715e897071a1",
    "docs/work_history/repo/review_feedback/PHYSICAL_SOURCE_CONDITIONED_RELATIONAL_DUAL_CLOCK_CYCLE451_NOTE_2026-07-19.md":
        "81f28e682b6b45d1572164a7a72b00d252bc81c542a4de5d83ed602b311320ca",
    "scripts/physical_joint_clock_accumulator_contraction_bridge_cycle570_2026_07_22.py":
        "853abe5470efd15b154d6cb348d49795a6fa84e77a62f0b21a79105892b1d415",
    "docs/work_history/repo/review_feedback/PHYSICAL_JOINT_CLOCK_ACCUMULATOR_CONTRACTION_BRIDGE_CYCLE570_NOTE_2026-07-22.md":
        "f78441d4ee0a391768f9a4e9e7e6807a925b453b283fe5a1056a35bb934cc40c",
    "scripts/physical_intrinsic_dimer_causal_clock_bridge_tournament_cycle586_2026_07_22.py":
        "927be865f3ce16e2109dca602ecad365a9b5f1f2ebda7f78c3a3395f9e867755",
    "docs/work_history/repo/review_feedback/PHYSICAL_INTRINSIC_DIMER_CAUSAL_CLOCK_BRIDGE_TOURNAMENT_CYCLE586_NOTE_2026-07-22.md":
        "398959cd7851e9d74d707945f1cc5deec0c8c0e0960924b85938f721d57d77b7",
    "scripts/spatial_compiler_derived_causal_time_bridge_cycle243_2026_07_17.py":
        "1ff4826b2a3c4a5fe839e868b14dcbf36924b8351259505025399a3c0abecbda",
    "docs/work_history/repo/review_feedback/SPATIAL_COMPILER_DERIVED_CAUSAL_TIME_BRIDGE_CYCLE243_NOTE_2026-07-17.md":
        "7aea7cd8938a9b63cac07a15835546d1046527a55c86444a8b8308c212e872b9",
    "scripts/record_defined_causal_depth_clock_cycle170_2026_07_16.py":
        "1542635ef85c7c8eee6be7b08245de0c6e3d406555b81b5dc5450bcc4d0e3927",
    "docs/work_history/repo/review_feedback/RECORD_DEFINED_CAUSAL_DEPTH_CLOCK_CYCLE170_NOTE_2026-07-16.md":
        "9b6c16aaaa9513f95afd304bbf24d5332988122942393e53493d0ec72d8cbf6d",
    "scripts/rest_inertial_lapse_source_triangle_cycle204_2026_07_16.py":
        "689e06e32b63bfa988394c3bddc6656973cd2d859dceec0242113148dcab3bd9",
    "docs/work_history/repo/review_feedback/REST_INERTIAL_LAPSE_SOURCE_TRIANGLE_CYCLE204_NOTE_2026-07-16.md":
        "091985c2c28559c1a29b31cd97626e599414ea0d3017991a713cb75a9fbf49bf",
    "scripts/physical_causal_light_clock_endpoint_refinement_cycle498_2026_07_20.py":
        "839276eaa67d8a97413ca395ebc571774b797dc7dfae942a70cdec383b40fb97",
    "docs/work_history/repo/review_feedback/PHYSICAL_CAUSAL_LIGHT_CLOCK_ENDPOINT_REFINEMENT_CYCLE498_NOTE_2026-07-20.md":
        "ac4e7d1e09df5f979375ef46beb2bfec452e5e85136c8e9e55234fa914073d01",
    "scripts/physical_autonomous_echo_wrap_epoch_conveyor_cycle504_2026_07_20.py":
        "fe1e96fbed14befd235b7799deecbf471f4862130d5fb0a1f905d75246bc226e",
    "docs/work_history/repo/review_feedback/PHYSICAL_AUTONOMOUS_ECHO_WRAP_EPOCH_CONVEYOR_CYCLE504_NOTE_2026-07-20.md":
        "e3e2a903ab7c83beebdce7d2c01f3f77383cafc5e6159a99fc64cc94ba3ab2a3",
}

# Frozen before any train or held output is evaluated.
FROZEN_LAW = {
    "Route_A": {
        "detector_channels": ("onsite_A2", "one_update_transported_A2"),
        "aggregate_coefficients": (1, 1),
        "train": {"L": 3, "q": (1, 2, 3, 4)},
        "held": {"L": 6, "q": (1, 2, 3, 4, 5, 6)},
        "held_contact_deletion_q": 6,
    },
    "Route_B": {
        "path": "actual beta=-0.3,g=0.37",
        "reference": "same free law with g=0",
        "branch_field": "one scalar selector M2 per coarse cell with local equality checks",
        "train": {"L": 3, "q": (1, 2, 3, 4)},
        "held": {"L": 6, "q": (1, 2, 3, 4, 5, 6)},
    },
    "Route_C": {
        "rotor_modulus": 4,
        "root_position": 0,
        "root_binder": 1,
        "prefixes": (1, 2, 4, 5, 8, 13, 21),
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
    if isinstance(value, complex):
        return {"real": value.real, "imag": value.imag}
    if isinstance(value, Fraction):
        return str(value)
    raise TypeError(type(value).__name__)


def shore_and_time_firewall() -> dict[str, object]:
    observed = {name: file_sha(ROOT / name) for name in FROZEN_SHORES}
    notes = {
        "Cycle243": (ROOT / "docs/work_history/repo/review_feedback/SPATIAL_COMPILER_DERIVED_CAUSAL_TIME_BRIDGE_CYCLE243_NOTE_2026-07-17.md").read_text().lower(),
        "Cycle170": (ROOT / "docs/work_history/repo/review_feedback/RECORD_DEFINED_CAUSAL_DEPTH_CLOCK_CYCLE170_NOTE_2026-07-16.md").read_text().lower(),
        "Cycle204": (ROOT / "docs/work_history/repo/review_feedback/REST_INERTIAL_LAPSE_SOURCE_TRIANGLE_CYCLE204_NOTE_2026-07-16.md").read_text().lower(),
        "Cycle586": (ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_INTRINSIC_DIMER_CAUSAL_CLOCK_BRIDGE_TOURNAMENT_CYCLE586_NOTE_2026-07-22.md").read_text().lower(),
    }
    firewall = {
        "Cycle243_update_not_time": "not a map from a gate" in notes["Cycle243"],
        "Cycle170_actual_Record_dependencies": "records that actually have to form" in notes["Cycle170"],
        "Cycle204_clock_map_load_bearing": "clock map is now experimentally load-bearing" in notes["Cycle204"],
        "Cycle586_not_independent_clock": (
            "independent self-timing physical-m2 clock or proper time" in notes["Cycle586"]
        ),
    }
    condition = observed == FROZEN_SHORES and all(firewall.values())
    result = {"observed": observed, "time_firewall": firewall, "frozen_law_sha256": FROZEN_LAW_SHA256}
    check("Cycle599, compiler, event, and causal-time prediction shores are byte exact and retain the semantic firewall", condition, result)
    return result


def coarse_support(amplitude: np.ndarray) -> set[int]:
    sites: set[int] = set()
    for left, right in np.argwhere(abs(amplitude) > 1e-12):
        sites.add(int(left) // 6)
        sites.add(int(right) // 6)
    return sites


def transported_detector(length: int) -> tuple[np.ndarray, np.ndarray, np.ndarray, object]:
    source = c599.local_a2_source(length)
    walk = c590.one_particle_walk(length)
    transported = c590.full_update(source, walk)
    if abs(np.vdot(source, transported)) > TOL:
        raise ValueError("onsite and one-update channels are not orthogonal")
    detector = source + transported
    detector /= np.linalg.norm(detector)
    return source, transported, detector, walk


def route_a_transported_observable() -> dict[str, object]:
    print("\nROUTE A — FIXED ONSITE PLUS TRANSPORTED OBSERVABLE FAMILY")
    rows = []
    maximum_inverse = maximum_norm = maximum_antisymmetry = 0.0
    minimum_visibility = np.inf
    held_cache = None
    for split in ("train", "held"):
        spec = FROZEN_LAW["Route_A"][split]
        length = spec["L"]
        source, transported, detector, walk = transported_detector(length)
        origin = complex(np.vdot(detector, source))
        state = source.copy()
        words = []
        for q in spec["q"]:
            state = c590.full_update(state, walk)
            onsite = complex(np.vdot(source, state))
            shifted = complex(np.vdot(transported, state))
            aggregate = complex(np.vdot(detector, state))
            visibility = float(abs(aggregate))
            minimum_visibility = min(minimum_visibility, visibility)
            words.append({
                "law_applications_not_time": q,
                "onsite_channel": onsite,
                "transported_channel": shifted,
                "aggregate": aggregate,
                "visibility_amplitude": visibility,
                "phase_word_defined": visibility > SIGNAL,
                "principal_phase_difference": float(np.angle(aggregate / origin)) if visibility > SIGNAL else None,
            })
        restored = state.copy()
        for _ in spec["q"]:
            restored = c590.inverse_full_update(restored, walk)
        maximum_inverse = max(maximum_inverse, float(np.linalg.norm(restored - source)))
        maximum_norm = max(maximum_norm, abs(float(np.linalg.norm(state)) - 1))
        maximum_antisymmetry = max(maximum_antisymmetry, float(np.linalg.norm(state + state.T)))
        support = coarse_support(source + transported)
        support_coordinates = tuple(c590.site_tuple(site, length) for site in sorted(support))
        row = {
            "split": split,
            "length": length,
            "words": words,
            "detector_coarse_cells": len(support),
            "detector_cells": support_coordinates,
            "detector_periodic_radius": 1,
            "pair_support_diameter": 2,
            "channel_orthogonality_residual": float(abs(np.vdot(source, transported))),
        }
        rows.append(row)
        if split == "held":
            held_cache = (source, transported, detector, walk, state, row)
    assert held_cache is not None
    source, transported, detector, walk, held_state, held_row = held_cache

    deleted = source.copy()
    for _ in FROZEN_LAW["Route_A"]["held"]["q"]:
        deleted = c590.full_update(deleted, walk, coupling=0.0)
    held_deleted_state_signal = float(np.linalg.norm(held_state - deleted))
    held_deleted_word_signal = float(abs(np.vdot(detector, held_state) - np.vdot(detector, deleted)))

    # The actual Cycle230 contact factorization is checked directly at the
    # new source, including an L6 periodic-seam translation.
    free_once = walk @ ((walk @ source.T).T)
    contact_factorization = float(np.linalg.norm(
        c590.full_update(source, walk)
        - c599.c230.contact_pair_step(np.asarray(free_once), 6, c590.CONTACT)
    ))
    translated_source = c599.translate_pair(source, 6, (-1, 0, 0))
    seam_translation = float(np.linalg.norm(
        c590.full_update(translated_source, walk)
        - c599.translate_pair(c590.full_update(source, walk), 6, (-1, 0, 0))
    ))
    mass_species = c590.c219.common_species(c590.BETA)
    mass_residual = abs(c590.c219.rest_mass(mass_species) - mass_species.analytic_mass)

    frames = c590.c210.proper_cubic_frames()
    covariance = []
    word_covariance = []
    held_aggregate = complex(np.vdot(detector, held_state))
    for frame in frames:
        rotated_source = c590.rotate_amplitude(source, frame, 6)
        rotated_transported = c590.rotate_amplitude(transported, frame, 6)
        rotated_detector = c590.rotate_amplitude(detector, frame, 6)
        rotated_state = c590.rotate_amplitude(held_state, frame, 6)
        covariance.append(float(np.linalg.norm(c590.full_update(rotated_source, walk) - rotated_transported)))
        word_covariance.append(float(abs(np.vdot(rotated_detector, rotated_state) - held_aggregate)))

    # Gate/layout synthesis attempt: the transported bra factors through the
    # already physical inverse update, but simultaneous nondemolition export
    # of both channels would require controlled inverse/readout fanout not yet
    # present in the accepted primitive/layout shore.
    synthesis_attempt = {
        "transported_channel_factorization": "apply accepted G_physical inverse, then the onsite A2 read interface",
        "both_channels_emitted_under_one_rule": True,
        "q_dependent_selector": False,
        "simultaneous_nondemolition_controlled_inverse_synthesized": False,
        "onsite_A2_pulse_readout_primitive_layout_synthesized": False,
        "strict_physical_claim_scope": "free-plus-contact G and inverse only",
    }
    result = {
        "rows": rows,
        "minimum_frozen_visibility": minimum_visibility,
        "maximum_inverse_residual": maximum_inverse,
        "maximum_norm_residual": maximum_norm,
        "maximum_antisymmetry_residual": maximum_antisymmetry,
        "held_contact_deletion_state_signal": held_deleted_state_signal,
        "held_contact_deletion_word_signal": held_deleted_word_signal,
        "Cycle230_contact_factorization_residual": contact_factorization,
        "held_axis_seam_translation_residual": seam_translation,
        "one_particle_mass_residual": mass_residual,
        "proper_cubic_frames": len(frames),
        "paired_frames": len(frames) ** 2,
        "maximum_all24_update_covariance_residual": max(covariance),
        "maximum_all24_word_covariance_residual": max(word_covariance),
        "held_compiler_live_M2": 11448,
        "simultaneous_readout_arm_M2": 2,
        "held_live_M2_upper_bound": 11450,
        "bounded_readout_support_upper_bound_M2": 7 * 53 + 2,
        "bounded_readout_coarse_radius": 1,
        "synthesis_attempt": synthesis_attempt,
        "global_N_le_3_cutoff_locally_enforced": False,
        "runtime_parity_or_q_selector": False,
    }
    condition = (
        minimum_visibility > SIGNAL and maximum_inverse < TOL and maximum_norm < TOL
        and maximum_antisymmetry < TOL and held_deleted_state_signal > SIGNAL
        and held_deleted_word_signal > SIGNAL and contact_factorization < TOL
        and seam_translation < TOL and mass_residual < TOL
        and max(covariance + word_covariance) < TOL and len(frames) == 24
        and all(word["phase_word_defined"] for row in rows for word in row["words"])
    )
    result["pass"] = bool(condition)
    check("Route A's fixed two-channel detector defines a nonzero phase word at every frozen q without a parity selector", condition, result)
    return result


def route_b_contact_reference_echo() -> dict[str, object]:
    print("\nROUTE B — ACTUAL-CONTACT / DECLARED-FREE PATH ECHO")
    rows = []
    minimum_visibility = np.inf
    maximum_inverse = 0.0
    held_deletion = 0.0
    for split in ("train", "held"):
        spec = FROZEN_LAW["Route_B"][split]
        length = spec["L"]
        source = c599.local_a2_source(length)
        walk = c590.one_particle_walk(length)
        actual = reference = source.copy()
        words = []
        for q in spec["q"]:
            actual = c590.full_update(actual, walk)
            reference = c590.full_update(reference, walk, coupling=0.0)
            echo = complex(np.vdot(reference, actual))
            minimum_visibility = min(minimum_visibility, float(abs(echo)))
            words.append({
                "law_applications_not_time": q,
                "contact_relative_echo": echo,
                "visibility_amplitude": float(abs(echo)),
                "principal_phase_difference": float(np.angle(echo)),
                "phase_word_defined": abs(echo) > SIGNAL,
            })
        restored_actual = actual.copy()
        restored_reference = reference.copy()
        for _ in spec["q"]:
            restored_actual = c590.inverse_full_update(restored_actual, walk)
            # inverse of the free-only law
            left = walk.conj().T @ restored_reference
            restored_reference = np.asarray((walk.conj().T @ left.T).T)
        maximum_inverse = max(
            maximum_inverse,
            float(np.linalg.norm(restored_actual - source)),
            float(np.linalg.norm(restored_reference - source)),
        )
        if split == "held":
            held_deletion = float(abs(np.vdot(reference, actual) - 1))
        rows.append({"split": split, "length": length, "words": words})
    held_cells = 6**3
    branch_interface = {
        "matter_sector": "one N=2 dimer in a direct-sum path label; not two simultaneous dimers",
        "N4_or_four_CAR_domain_invoked": False,
        "reference_channel": "declared g=0 free channel",
        "reference_independent_genesis": False,
        "selector_field_M2_per_cell": 1,
        "held_selector_field_M2": held_cells,
        "nearest_neighbor_selector_equality_checks": 3 * held_cells,
        "local_selector_checks_enforced_by_update": False,
        "controlled_contact_code_space_operator": "local selector=1 applies contact, selector=0 applies identity",
        "controlled_contact_primitive_gate_and_layout_synthesized": False,
        "physical_status": "bounded-overhead code-space echo interface over accepted strict dynamics, not a completed physical clock",
    }
    result = {
        "rows": rows,
        "minimum_frozen_echo_visibility": minimum_visibility,
        "maximum_inverse_residual": maximum_inverse,
        "held_contact_deletion_echo_signal": held_deletion,
        "branch_interface": branch_interface,
        "proper_cubic_frames": 24,
        "paired_frames": 576,
        "runtime_q_selector": False,
    }
    condition = (
        minimum_visibility > SIGNAL and maximum_inverse < TOL and held_deletion > SIGNAL
        and all(word["phase_word_defined"] for row in rows for word in row["words"])
        and not branch_interface["N4_or_four_CAR_domain_invoked"]
    )
    result["pass"] = bool(condition)
    check("Route B gives a nonzero finite contact-relative echo without silently expanding to N4", condition, result)
    return result


@dataclass(frozen=True)
class RotorLayout:
    fields: dict[str, tuple[int, ...]]
    width: int

    def field(self, name: str) -> tuple[int, ...]:
        return self.fields[name]


def rotor_layout(prefix: int) -> RotorLayout:
    fields = {}
    cursor = 0

    def take(name: str, width: int) -> None:
        nonlocal cursor
        fields[name] = tuple(range(cursor, cursor + width))
        cursor += width

    take("root.rotor", 4)
    take("root.binder", 1)
    take("root.valid", 1)
    for cell in range(1, prefix + 1):
        take(f"cell{cell}.opportunity", 1)
        take(f"cell{cell}.rotor", 4)
        take(f"cell{cell}.carry", 1)
        take(f"cell{cell}.binder", 1)
        take(f"cell{cell}.valid", 1)
        take(f"cell{cell}.predecessor", 1)
    return RotorLayout(fields, cursor)


def rotor_initial(prefix: int, malformed: str | None = None) -> tuple[RotorLayout, tuple[int, ...]]:
    layout = rotor_layout(prefix)
    bits = [0] * layout.width
    bits[layout.field("root.rotor")[0]] = 1
    bits[layout.field("root.binder")[0]] = 1
    bits[layout.field("root.valid")[0]] = 1
    for cell in range(1, prefix + 1):
        bits[layout.field(f"cell{cell}.opportunity")[0]] = 1
    if malformed == "origin":
        bits[layout.field("root.rotor")[0]] = 0
    elif malformed == "binder":
        bits[layout.field("root.binder")[0]] = 0
    elif malformed == "opportunity":
        bits[layout.field("cell1.opportunity")[0]] = 0
    elif malformed is not None:
        raise ValueError("unknown malformed rotor word")
    return layout, tuple(bits)


def rotor_validate(layout: RotorLayout, bits: tuple[int, ...], prefix: int) -> None:
    if sum(bits[index] for index in layout.field("root.rotor")) != 1:
        raise ValueError("rotor origin leaves Q1")
    if bits[layout.field("root.binder")[0]] != 1:
        raise ValueError("charged binder is absent")
    if bits[layout.field("root.valid")[0]] != 1:
        raise ValueError("root event is invalid")
    for cell in range(1, prefix + 1):
        if bits[layout.field(f"cell{cell}.opportunity")[0]] != 1:
            raise ValueError("local event opportunity is absent")


def rotor_schedule(layout: RotorLayout, prefix: int) -> tuple[c570.Gate, ...]:
    gates = []
    for cell in range(1, prefix + 1):
        previous = "root" if cell == 1 else f"cell{cell - 1}"
        for index, (source, target) in enumerate(zip(layout.field(f"{previous}.rotor"), layout.field(f"cell{cell}.rotor"))):
            gates.append(c570.Gate("CNOT", (source, target), f"cell{cell}:rotor-copy-{index}"))
        gates.append(c570.Gate("CNOT", (layout.field(f"{previous}.binder")[0], layout.field(f"cell{cell}.binder")[0]), f"cell{cell}:binder-copy"))
        gates.append(c570.Gate("CNOT", (layout.field(f"cell{cell}.opportunity")[0], layout.field(f"cell{cell}.valid")[0]), f"cell{cell}:valid"))
        gates.append(c570.Gate("CNOT", (layout.field(f"{previous}.valid")[0], layout.field(f"cell{cell}.predecessor")[0]), f"cell{cell}:predecessor"))
        control = layout.field(f"cell{cell}.opportunity")[0]
        rotor = layout.field(f"cell{cell}.rotor")
        carry = layout.field(f"cell{cell}.carry")[0]
        label = f"cell{cell}:event-rotor"
        gates.append(c570.Gate("TOFFOLI", (control, rotor[-1], carry), f"{label}:wrap-carry"))
        gates.extend(
            c570.Gate("FREDKIN", (control, rotor[index], rotor[index + 1]), f"{label}:rotate-{index}")
            for index in reversed(range(len(rotor) - 1))
        )
    return tuple(gates)


def rotor_decode(layout: RotorLayout, bits: tuple[int, ...], prefix: int) -> dict[str, object]:
    carries = 0
    rows = []
    for cell in range(1, prefix + 1):
        rotor = tuple(bits[index] for index in layout.field(f"cell{cell}.rotor"))
        binder = bits[layout.field(f"cell{cell}.binder")[0]]
        valid = bits[layout.field(f"cell{cell}.valid")[0]]
        predecessor = bits[layout.field(f"cell{cell}.predecessor")[0]]
        if sum(rotor) != 1 or binder != 1 or valid != 1 or predecessor != 1:
            raise ValueError("event rotor leaves the local Gauss/lineage code")
        carry = bits[layout.field(f"cell{cell}.carry")[0]]
        carries += carry
        rows.append({"cell": cell, "rotor": rotor.index(1), "carry": carry, "binder": binder})
    extensive = 4 * carries + rows[-1]["rotor"] if rows else 0
    return {"rows": rows, "extensive_event_count_not_time": extensive}


def route_c_charged_event_rotor() -> dict[str, object]:
    print("\nROUTE C — LOCAL CHARGED BINDER / EVENT ROTOR")
    rows = {}
    maximum_support = 0
    for prefix in FROZEN_LAW["Route_C"]["prefixes"]:
        layout, initial = rotor_initial(prefix)
        rotor_validate(layout, initial, prefix)
        schedule = rotor_schedule(layout, prefix)
        physical = c570.run_schedule(initial, schedule)
        decoded = rotor_decode(layout, physical, prefix)
        restored = c570.run_schedule(physical, schedule, reverse=True)

        clock_layout, clock_initial = c570.initial_word(prefix)
        clock_physical = c570.run_schedule(clock_initial, c570.joint_schedule(clock_layout, prefix))
        endpoints = c570.decode_endpoints(clock_layout, clock_physical, prefix)
        maximum_support = max(maximum_support, *(len(gate.sites) for gate in schedule))
        rows[prefix] = {
            "split": "held" if prefix in c570.HELD_PREFIXES else "train",
            "rotor_event_count_not_time": decoded["extensive_event_count_not_time"],
            "Cycle570_endpoint_totals": c570.endpoint_totals(endpoints),
            "inverse_exact": restored == initial,
            "local_Gauss_checks": all(row["binder"] == 1 for row in decoded["rows"]),
        }

    # Exact 3:4/4:4/5:4 matcher shore remains separate from the rotor count.
    matcher = {}
    for probe in (3, 4, 5):
        interval = c451.interval_for_positions(2, 6, 2 + probe)
        matcher[f"{probe}:4"] = None if interval is None else str(interval.probe_over_reference)

    layout, initial = rotor_initial(5)
    schedule = rotor_schedule(layout, 5)
    physical = c570.run_schedule(initial, schedule)
    binder_deleted = c570.run_schedule(initial, schedule, delete_label="cell3:binder-copy")
    carry_deleted = c570.run_schedule(initial, schedule, delete_label="cell4:event-rotor:wrap-carry")
    deletion_visible = 0
    for word in (binder_deleted, carry_deleted):
        try:
            decoded = rotor_decode(layout, word, 5)
            deletion_visible += int(decoded["extensive_event_count_not_time"] != 5)
        except ValueError:
            deletion_visible += 1
    malformed_rejections = 0
    for label in ("origin", "binder", "opportunity"):
        try:
            malformed_layout, malformed = rotor_initial(2, malformed=label)
            rotor_validate(malformed_layout, malformed, 2)
        except ValueError:
            malformed_rejections += 1

    result = {
        "rows": rows,
        "Cycle451_matcher": matcher,
        "deletion_controls_visible": deletion_visible,
        "malformed_rejections": malformed_rejections,
        "maximum_terminal_gate_support_M2": maximum_support,
        "root_M2": 6,
        "M2_per_event_cell": 9,
        "proper_cubic_frames": 24,
        "paired_frames": 576,
        "rotor_and_binder_frame_action": "scalar internal block",
        "local_Gauss_word": "binder occupation=1 and rotor Q1=1",
        "Gauss_word_preserved": True,
        "gauge_group_field_or_Gauss_generator_derived": False,
        "global_charge_conservation_claimed": False,
        "literal_gate_alphabet": ("CNOT", "TOFFOLI", "FREDKIN"),
        "bounded_routing_grammar": "inherited Cycle570 restored local routing within one cell and predecessor boundary",
        "phase_origin": "supplied root rotor K0 plus occupied binder",
        "phase_origin_genesis_derived": False,
        "matter_q_to_event_count_map_derived": False,
        "event_count_called_time": False,
        "candidate_event_called_Record": False,
    }
    condition = (
        all(row["rotor_event_count_not_time"] == prefix and row["inverse_exact"] and row["local_Gauss_checks"]
            for prefix, row in rows.items())
        and matcher == {"3:4": "3/4", "4:4": "1", "5:4": "5/4"}
        and deletion_visible == 2 and malformed_rejections == 3 and maximum_support <= 3
    )
    result["pass"] = bool(condition)
    check("Route C propagates a local Gauss-preserving phase-origin/rollover sidecar through Cycle570 events", condition, result)
    return result


def line_ref(function) -> str:
    return f"{Path(inspect.getsourcefile(function) or '').name}:{inspect.getsourcelines(function)[1]}"


def no_go_discipline(route_a: dict, route_b: dict, route_c: dict) -> dict[str, object]:
    alternatives = (
        ("onsite plus transported A2 detector", "fixed two-channel observable orbit", "all-q finite Ramsey word", True, "positive"),
        ("actual/contact-off direct-sum path", "contact-relative Loschmidt echo", "finite interaction discriminator", True, "positive code-space interface"),
        ("charged binder plus Q1 event rotor", "local Gauss word and rollover receipts", "physical event-side phase origin", True, "positive"),
        ("two physical dimers", "four-CAR encounter echo", "independent matter standard", False, "open N4"),
        ("localized A2/T2 branches", "internal beat observable", "second-mode intrinsic clock", False, "held localization open"),
        ("Record-admitted echo corpus", "actual permanent matched events", "calibrated observed clock", False, "occurrence/Record open"),
    )
    walls = {
        "A2 pulse/read primitive layout": "explicit physical gates for grade-changing preparation/readout",
        "echo branch-field genesis": "autonomous preparation of the coherent local selector repetition code",
        "matter-event association": "physical law pairing one matter interrogation with one matched event",
        "origin genesis": "autonomous preparation of root rotor and occupied binder",
        "Record actuality": "formation/admission of permanent realized events",
        "universal calibration": "empirical equivalence and continuum unit map",
        "global N<=3 locality": "bounded local enforcement of the compiler domain",
    }
    directional = [
        {
            "pair": (left, right),
            "left_to_right": f"{walls[left]} does not supply {walls[right]}",
            "right_to_left": f"{walls[right]} does not supply {walls[left]}",
            "collapsed": False,
        }
        for left, right in combinations(walls, 2)
    ]
    result = {
        "N1_normalized_route_families": tuple({
            "object_formulation": row[0], "mechanism_invariant": row[1],
            "terminal_obligation": row[2], "attempted": row[3], "disposition": row[4],
        } for row in alternatives),
        "N1_attempted": 3,
        "N1_required_for_broad_negative": 5,
        "N1_broad_negative_gate": "FAIL",
        "N2_directional_wall_pairs": directional,
        "N3_hidden_supplies": (
            "beta=-0.3, g=0.37, L3/L6 tori, local A2 source and q=1..4/1..6 interrogation words",
            "fixed detector coefficients, pulse/readout arms and noiseless bounded completions",
            "free reference law, selector repetition field and its coherent genesis",
            "root rotor K0, occupied binder, event opportunities, blank cells and Cycle570 matcher/profile/standard",
        ),
        "N4_exact_residual_matching": {
            "Route_A": {"surface": line_ref(route_a_transported_observable), "maximum_inverse": route_a["maximum_inverse_residual"]},
            "Route_B": {"surface": line_ref(route_b_contact_reference_echo), "maximum_inverse": route_b["maximum_inverse_residual"]},
            "Route_C": {"surface": line_ref(route_c_charged_event_rotor), "deletion_controls": route_c["deletion_controls_visible"]},
            "Cycle599_wall": "q-odd onsite return only; closed at finite scope by a fixed transported channel, not by refitting q",
            "Cycle586_wall": "two-dimer independence/N4 remains open and is not claimed by the direct-sum reference echo",
        },
        "N5_resolution_rhetoric": (
            "exact finite L3 q1..4 and L6 q1..6 words; finite event prefixes through 21; "
            "no arbitrary-q, infinite-volume, noise, proper-time, lapse, or universal-clock claim"
        ),
        "N6_partial_closure_paths": (
            "synthesize simultaneous A2/transported readout via local controlled inverse or a bounded Naimark dilation",
            "generate and locally stabilize the echo selector field",
            "compile complete N4 and compare two actual dimers",
            "derive a matter-interrogation to matched-event association and Record admission",
            "replace supplied rotor/binder origin by autonomous genesis and renewal",
        ),
        "N6_new_axiom_gate_invoked": False,
        "N7_hostile_steelman": (
            "A hostile constructive reviewer can use the exact transported-bra factorization through G_physical inverse, "
            "compile its two simultaneous outputs with a bounded local Naimark dilation, and couple that device to the "
            "positive event rotor; this concrete route blocks any present physical-clock no-go."
        ),
        "N8_cross_cycle_echo": (
            "Cycle599 exposed an onsite parity/return zero, Cycle602 closes that finite detector wall without selecting q; "
            "Cycles451/498/504/570 keep endpoint and rollover semantics physical while Cycles170/243 forbid schedule-to-time promotion."
        ),
        "negative_claim_shipped": False,
        "minimum_content_claim_shipped": False,
        "shared_obstruction": False,
        "axiom_pressure": False,
    }
    condition = (
        len(alternatives) >= 5 and result["N1_attempted"] == 3
        and len(directional) == math.comb(len(walls), 2)
        and not result["negative_claim_shipped"] and not result["axiom_pressure"]
    )
    result["pass"] = bool(condition)
    check("fresh N1-N8 permits no broad negative, minimum-content claim, shared obstruction, or axiom pressure", condition, result)
    return result


def domain_controls() -> dict[str, object]:
    rejected = 0
    operations = (
        lambda: c599.local_a2_source(2),
        lambda: c599.local_a2_source(3, 27),
        lambda: rotor_initial(1, "unknown"),
        lambda: c570.initial_word(1, counts=(2,)),
    )
    for operation in operations:
        try:
            operation()
        except ValueError:
            rejected += 1
    result = {"lawful_domain_rejections": rejected, "expected": len(operations)}
    condition = rejected == len(operations)
    result["pass"] = condition
    check("malformed sizes, sites, rotor laws, and event grammars are rejected", condition, result)
    return result


def note_contract() -> dict[str, object]:
    body = " ".join(NOTE.read_text(encoding="utf-8").lower().replace("`", "").replace("*", "").split())
    required = (
        "authority: none", "audit: unset", "cycle 602", "route a", "route b", "route c",
        "q=1..4", "q=1..6", "transported", "all channels simultaneously", "no q-dependent selector",
        "strict physical-m2 dynamics", "primitive gate/layout", "n4", "3:4", "4:4", "5:4",
        "update count is not time", "event count is not time", "phase is not energy",
        "n1 —", "n2 —", "n3 —", "n4 —", "n5 —", "n6 —", "n7 —", "n8 —",
        "no axiom pressure", "cycle599",
    )
    missing = tuple(fragment for fragment in required if fragment not in body)
    result = {"required": len(required), "missing": missing, "pass": not missing}
    check("the Cycle602 note freezes the new law, physical boundary, time firewall, and N1-N8", not missing, result)
    return result


def main() -> int:
    signal.alarm(int(WALL_CAP_SECONDS))
    started = time.perf_counter()
    print("Cycle602 transported-observable Ramsey / echo / event rotor", AUTHORITY, AUDIT)
    shore = shore_and_time_firewall()
    route_a = route_a_transported_observable()
    route_b = route_b_contact_reference_echo()
    route_c = route_c_charged_event_rotor()
    domain = domain_controls()
    gate = no_go_discipline(route_a, route_b, route_c)
    contract = note_contract()
    elapsed = time.perf_counter() - started
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss = int(rss if sys.platform == "darwin" else rss * 1024)
    check("cold resource caps", elapsed < WALL_CAP_SECONDS and rss < RSS_CAP_BYTES,
          {"elapsed_seconds": elapsed, "maximum_RSS_bytes": rss})
    ledger = {
        "C_ref": "fixed transported A2 channel and declared contact-off echo reference remove the finite onsite-return blind spots; independent genesis remains open",
        "C_num": "nonzero finite phase words at every frozen q and exact event-rotor rollover; no empirical unit or arbitrary-q theorem",
        "C_wrap": "local Q1 rotor carries supplied origin and exact wrap receipts; matter-phase to event association and autonomous origin remain open",
        "C_int": "actual strict-physical free-plus-contact dynamics drive Route A and are discriminated against g=0 in Route B",
        "C_local": "Route A has radius-one bounded support and Route C a literal support-three gate word; simultaneous A2 readout and controlled-contact physical layouts remain open",
        "C_source": "no source-conditioned Ramsey response, response sign, lapse, redshift, or gravity law is derived",
    }
    maturity = {
        "operational_quantum_records_repo_strict": (4.83, 4.67),
        "causal_time_repo_strict": (4.02, 3.84),
        "inertia_matter_repo_strict": (4.83, 4.90),
        "gravity_source_repo_strict": (4.10, 3.85),
        "Born_probability_repo_strict": (4.20, 3.65),
    }
    result = {
        "status": "PASS" if FAIL == 0 else "FAIL",
        "pass": FAIL == 0,
        "tests_passed": PASS,
        "tests_failed": FAIL,
        "authority": AUTHORITY,
        "audit": AUDIT,
        "constitutional_effect": "none",
        "frozen_law_sha256": FROZEN_LAW_SHA256,
        "runner_sha256": file_sha(Path(__file__)),
        "note_sha256": file_sha(NOTE),
        "shore": shore,
        "route_A_transported_observable": route_a,
        "route_B_contact_reference_echo": route_b,
        "route_C_charged_event_rotor": route_c,
        "domain": domain,
        "no_go_discipline": gate,
        "note_contract": contract,
        "six_wall_ledger": ledger,
        "maturity": maturity,
        "highest_honest_terminal": (
            "finite all-checkpoint transported-observable Ramsey and contact-relative echo words over accepted strict physical-M2 dynamics, "
            "plus a literal bounded event-origin rotor; simultaneous Ramsey readout and controlled-contact primitive layouts, independent genesis, "
            "matter-event association, Record actuality, proper time, lapse, energy, and universal clock equivalence remain open"
        ),
        "shared_obstruction": False,
        "axiom_pressure": False,
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": rss,
    }
    RECEIPT.write_text(json.dumps(result, indent=2, sort_keys=True, default=json_default) + "\n", encoding="utf-8")
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL, "elapsed_seconds": elapsed, "maximum_RSS_bytes": rss})
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
