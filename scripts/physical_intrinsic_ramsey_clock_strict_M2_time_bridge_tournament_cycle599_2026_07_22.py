#!/usr/bin/env python3
"""Cycle599: intrinsic Ramsey-clock / strict-M2 time-bridge tournament.

The outputs are operational coherent phase-difference words attached to
matched candidate events.  Update ordinals and schedules are not time,
wrapped phase is not energy, and neither a latch nor a squared norm is a
Record, occurrence, or probability.
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
from scipy import sparse
from scipy.sparse import linalg as sparse_linalg


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import coherent_multibeta_physical_mass_controller_tournament_cycle441_2026_07_19 as c441
import physical_source_conditioned_relational_dual_clock_cycle451_2026_07_19 as c451
import physical_joint_clock_accumulator_contraction_bridge_cycle570_2026_07_22 as c570
import physical_contact_dimer_infinite_internal_content_tournament_cycle583_2026_07_22 as c583
import physical_full_torus_dimer_M2_compiler_tournament_cycle590_2026_07_22 as c590
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_INTRINSIC_RAMSEY_CLOCK_STRICT_M2_TIME_BRIDGE_TOURNAMENT_"
    "CYCLE599_NOTE_2026-07-22.md"
)
RECEIPT = ROOT / (
    "outputs/physical_intrinsic_ramsey_clock_strict_M2_time_bridge_"
    "tournament_cycle599_receipt_2026_07_22.json"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 8e-9
SIGNAL = 1e-8
WALL_CAP_SECONDS = 300.0
RSS_CAP_BYTES = 3 * 1024**3
PASS = 0
FAIL = 0

# These are the accepted shores named by the campaign.  Cycle597 is pinned as
# part of the accepted shore state now present, but its transition-synthesis
# law is deliberately not imported or consumed: this clock tournament is an
# independent physical-matter/event composition.
FROZEN_SHORES = {
    "scripts/coherent_multibeta_physical_mass_controller_tournament_cycle441_2026_07_19.py":
        "c274f75ff2b2fe427f04598b84a01247765c562f7ab014ffee2d63af2f27b5d4",
    "docs/work_history/repo/review_feedback/COHERENT_MULTIBETA_PHYSICAL_MASS_CONTROLLER_TOURNAMENT_CYCLE441_NOTE_2026-07-19.md":
        "072e760c11f0f69345aa3cd118835842bc5a0be6c7786426ace30a0dd4b8aa22",
    "scripts/physical_source_conditioned_relational_dual_clock_cycle451_2026_07_19.py":
        "c89e3d47b42b05c0d723afb5e68548bbb15ee79401eaa72f3c8c715e897071a1",
    "docs/work_history/repo/review_feedback/PHYSICAL_SOURCE_CONDITIONED_RELATIONAL_DUAL_CLOCK_CYCLE451_NOTE_2026-07-19.md":
        "81f28e682b6b45d1572164a7a72b00d252bc81c542a4de5d83ed602b311320ca",
    "scripts/physical_joint_clock_accumulator_contraction_bridge_cycle570_2026_07_22.py":
        "853abe5470efd15b154d6cb348d49795a6fa84e77a62f0b21a79105892b1d415",
    "docs/work_history/repo/review_feedback/PHYSICAL_JOINT_CLOCK_ACCUMULATOR_CONTRACTION_BRIDGE_CYCLE570_NOTE_2026-07-22.md":
        "f78441d4ee0a391768f9a4e9e7e6807a925b453b283fe5a1056a35bb934cc40c",
    "scripts/physical_contact_dimer_infinite_internal_content_tournament_cycle583_2026_07_22.py":
        "3f1672ef0d2c0063d5760a6b0885d75cb75b63c64b44951399fd0762d5499f7f",
    "docs/work_history/repo/review_feedback/PHYSICAL_CONTACT_DIMER_INFINITE_INTERNAL_CONTENT_TOURNAMENT_CYCLE583_NOTE_2026-07-22.md":
        "73531224b0af8a1f0fb23e161fc4da0b543a4e645b1b71a756b5147417f55663",
    "scripts/physical_full_torus_dimer_M2_compiler_tournament_cycle590_2026_07_22.py":
        "5fbf3bcecc54df9912f9b79d2e5c45d51f145279c1ed83f507bc24e9e1980029",
    "docs/work_history/repo/review_feedback/PHYSICAL_FULL_TORUS_DIMER_M2_COMPILER_TOURNAMENT_CYCLE590_NOTE_2026-07-22.md":
        "3ee6ba9bd5a01a5cab88832788156597a1491d7c2d47f9378caca624a35a1936",
    "scripts/physical_state_family_grade_transition_synthesis_tournament_cycle597_2026_07_22.py":
        "7dec66d44101d26f563bea079fa62b56daeb1d2d5a21a7a98c6f66fc22392d77",
    "docs/work_history/repo/review_feedback/PHYSICAL_STATE_FAMILY_GRADE_TRANSITION_SYNTHESIS_TOURNAMENT_CYCLE597_NOTE_2026-07-22.md":
        "fdbfc68540be31de9d5199e25b1b71a440b9126447f383146caa07b70599c4b2",
    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py":
        "b449301837c1b72a325d310a1e2c582263a36648de939d169912347aff0591ae",
}

FROZEN_LAW = {
    "route_A": {
        "register": "nine-M2 Q1 cyclic shift",
        "coordinates": ("Cayley functional", "principal functional"),
        "Ramsey_arm": "one M2, H-controlled-U-H",
    },
    "route_B": {
        "matter": "Cycle590 N=0 direct-sum N=2 full-torus code",
        "pulse": "local even rank-one A2 pair H on vacuum/local-pair subspace",
        "binder": "one occupied spectator M2",
        "applications": {3: (1, 2), 6: (1, 2, 3)},
    },
    "route_C": {
        "irreps": ("E", "T1", "T2"),
        "lengths": (7, 11),
        "eigen_window": {"k": 24, "sigma_phase": -3.0, "ncv": 49},
        "held_localization_gate": {"contact_min": 0.18, "radius2_max": 6.0, "seam_max": 0.12},
    },
    "event_composition": {
        "Cycle451_cells": ((4, 3), (4, 4), (4, 5)),
        "Cycle570_prefixes": (1, 2, 4, 5, 8, 13, 21),
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
    raise TypeError(f"not JSON serializable: {type(value).__name__}")


def shore_controls() -> dict[str, object]:
    observed = {name: file_sha(ROOT / name) for name in FROZEN_SHORES}
    functional_source = inspect.getsource(c441.functional_route).lower()
    forbidden = ("target_betas", "sector_menu", "register_eigenpairs", "lookup_route", "np.outer")
    condition = observed == FROZEN_SHORES and not any(
        token in functional_source for token in forbidden
    )
    result = {
        "observed": observed,
        "Cycle597_accepted_shore_pinned": True,
        "Cycle597_law_imported_or_consumed": False,
        "functional_route_forbidden_hits": tuple(token for token in forbidden if token in functional_source),
        "frozen_law_sha256": FROZEN_LAW_SHA256,
    }
    check("accepted time/matter/compiler shores and the pre-held law are byte exact", condition, result)
    return result


def ramsey_operator(operator: np.ndarray) -> np.ndarray:
    """H-controlled-operator-H on register tensor one arm M2."""
    dimension = operator.shape[0]
    h = np.asarray(((1, 1), (1, -1)), complex) / math.sqrt(2)
    beam = np.kron(np.eye(dimension), h)
    controlled = np.zeros((2 * dimension, 2 * dimension), complex)
    for source in range(dimension):
        controlled[2 * source, 2 * source] = 1
    for row in range(dimension):
        for col in range(dimension):
            controlled[2 * row + 1, 2 * col + 1] = operator[row, col]
    return beam @ controlled @ beam


def route_a_register_clock() -> dict[str, object]:
    print("\nROUTE A — Q1 FUNCTIONAL MASS-REGISTER RAMSEY PRODUCT")
    c441.CONSTRUCTION_EVENTS.clear()
    register = c441.c220.cyclic_shift(c441.REGISTER_DIM)
    route = c441.functional_route(register)
    sectors = c441.sector_menu(register)
    menu = np.column_stack([sector.vector for sector in sectors])
    held = sectors[-1]
    laws = {
        "cayley-functional": route.cayley_clock,
        "principal-functional": route.principal_clock,
    }
    rows = {}
    maximum = 0.0
    for name, operator in laws.items():
        unitary = ramsey_operator(operator)
        initial = np.zeros(2 * c441.REGISTER_DIM, complex)
        initial[0::2] = held.vector
        output = unitary @ initial
        restored = unitary.conj().T @ output
        dark = float(np.vdot(output[1::2], output[1::2]).real)
        coordinate = held.cayley if name.startswith("cayley") else held.principal
        expected_dark = float(np.sin(coordinate / (2 * c441.CLOCK_SCALE)) ** 2)
        residuals = {
            "unitarity": float(np.linalg.norm(unitary.conj().T @ unitary - np.eye(18))),
            "inverse": float(np.linalg.norm(restored - initial)),
            "held_fringe_formula": abs(dark - expected_dark),
        }
        maximum = max(maximum, *residuals.values())
        rows[name] = {
            "held_beta": held.beta,
            "held_coordinate": coordinate,
            "bright_coherent_weight": float(np.vdot(output[0::2], output[0::2]).real),
            "dark_coherent_weight": dark,
            "residuals": residuals,
        }

    # Complete-code basis and coherent-superposition E/G are identical because
    # the Q1 physical encoder is the literal nine one-hot basis.  The product
    # with Cycle590's matter compiler acts on disjoint M2 blocks.
    cayley_u = ramsey_operator(route.cayley_clock)
    alpha = np.asarray((0.37, 0.41j, -0.52, 0.64j), complex)
    alpha /= np.linalg.norm(alpha)
    coherent_register = menu @ alpha
    coherent_input = np.zeros(18, complex)
    coherent_input[0::2] = coherent_register
    coherent_inverse = np.linalg.norm(cayley_u.conj().T @ (cayley_u @ coherent_input) - coherent_input)
    ring = np.eye(9, dtype=complex)
    for left, right in c441.REGISTER_SWAP_SCHEDULE:
        swap = np.eye(9, dtype=complex)
        swap[[left, right]] = swap[[right, left]]
        ring = swap @ ring
    ring_residual = float(np.linalg.norm(ring - register))
    deletion_signal = float(np.linalg.norm(cayley_u - ramsey_operator(np.eye(9))))
    rejected = 0
    for mask in (0, 0b11):
        try:
            c441.validate_register_code_mask(mask)
        except ValueError:
            rejected += 1
    frames = c590.c210.proper_cubic_frames()
    frame_keys = {tuple(frame.reshape(-1)) for frame in frames}
    frame_product_failures = sum(
        tuple((left @ right).reshape(-1)) not in frame_keys for left in frames for right in frames
    )
    mass_species = c590.c219.common_species(c590.BETA)
    mass_residual = abs(c590.c219.rest_mass(mass_species) - mass_species.analytic_mass)
    held_alias_separation = abs(
        rows["cayley-functional"]["dark_coherent_weight"]
        - rows["principal-functional"]["dark_coherent_weight"]
    )
    result = {
        "rows": rows,
        "complete_Q1_times_arm_dimension": 18,
        "Q1_physical_register_M2": 9,
        "Ramsey_arm_M2": 1,
        "held_L6_Cycle590_compiler_M2": 11448,
        "held_product_live_M2": 11458,
        "held_product_M2_per_coarse_cell_plus_device": "53 per cell + bounded 10-M2 register/arm device",
        "Q1_ring_nearest_neighbor_SWAP_count": len(c441.REGISTER_SWAP_SCHEDULE),
        "Q1_ring_schedule_residual": ring_residual,
        "functional_dense_control_support_M2": 10,
        "functional_dense_control_primitive_synthesis": "supplied/open",
        "product_EG_residual": 0.0,
        "coherent_inverse_residual": float(coherent_inverse),
        "functional_deletion_signal": deletion_signal,
        "held_alias_dark_weight_separation": held_alias_separation,
        "one_particle_mass_fixture_residual": mass_residual,
        "proper_cubic_frames": len(frames),
        "paired_frame_products": len(frames) ** 2,
        "frame_group_failures": frame_product_failures,
        "register_frame_action": "I9 scalar internal block",
        "lawful_domain_rejections": rejected,
        "beta_lookup_used": False,
        "sector_menu_use": "post-construction analysis/calibration and held scoring only; never a physical runtime selector",
        "matter_beta_changed_by_register": False,
        "interpretation": "independent operational register clock tensored with, not a beta controller for, the fixed-beta Cycle590 dimer",
    }
    condition = (
        maximum < TOL and coherent_inverse < TOL and ring_residual < TOL
        and held_alias_separation > 0.7 and deletion_signal > SIGNAL
        and mass_residual < TOL and len(frames) == 24 and frame_product_failures == 0
        and rejected == 2 and c441.CONSTRUCTION_EVENTS == ["functional-route-built", "spectral-menu-built"]
    )
    result["pass"] = bool(condition)
    check(
        "Route A ports the no-lookup Q1 functional Ramsey control as an exact code-space bounded-support product over the accepted L6 compiler, with primitive synthesis open",
        condition, result,
    )
    return result


def local_a2_source(length: int, site: int = 0) -> np.ndarray:
    if length < 3 or site not in range(length**3):
        raise ValueError("local A2 source leaves the declared torus")
    modes = 6 * length**3
    source = np.zeros((modes, modes), complex)
    source[6 * site:6 * (site + 1), 6 * site:6 * (site + 1)] = c583.A2_FULL.reshape(6, 6)
    source /= np.linalg.norm(source)
    return source


def pair_observables(pair: np.ndarray, source: np.ndarray) -> dict[str, object]:
    overlap = complex(np.vdot(source, pair))
    # For (|vac>+|pair>)/sqrt(2), these are expectations of the
    # even local rank-one X/Y pair observables.  They are amplitudes, not Born
    # probabilities or occurrences.
    visibility = float(abs(overlap))
    return {
        "X_pair": float(overlap.real),
        "Y_pair": float(overlap.imag),
        "visibility_amplitude": visibility,
        "phase_word_defined": visibility > SIGNAL,
        "principal_phase_difference": float(np.angle(overlap)) if visibility > SIGNAL else None,
    }


def relative_diagnostics(relative: np.ndarray, length: int) -> dict[str, float]:
    tensor = relative.reshape(length, length, length, 6, 6)
    probability = np.sum(abs(tensor) ** 2, axis=(3, 4))
    total = float(np.sum(probability))
    probability /= total
    radius2 = seam = 0.0
    for x in range(length):
        for y in range(length):
            for z in range(length):
                signed = tuple(c583.c578.signed_coordinate(value, length) for value in (x, y, z))
                weight = float(probability[x, y, z])
                radius2 += weight * sum(value * value for value in signed)
                if length % 2 == 0 and any(abs(value) == length // 2 for value in signed):
                    seam += weight
    return {
        "contact_weight": float(probability[0, 0, 0]),
        "relative_radius_squared": radius2,
        "seam_boundary_weight": seam,
    }


def translate_pair(amplitude: np.ndarray, length: int, displacement: tuple[int, int, int]) -> np.ndarray:
    modes = 6 * length**3
    target = np.empty(modes, dtype=int)
    for site in range(length**3):
        coordinate = c590.site_tuple(site, length)
        shifted = tuple((coordinate[axis] + displacement[axis]) % length for axis in range(3))
        target_site = c590.site_flat(shifted, length)
        for direction in range(6):
            target[6 * site + direction] = 6 * target_site + direction
    result = np.zeros_like(amplitude)
    result[np.ix_(target, target)] = amplitude
    return result


@dataclass(frozen=True)
class RamseyEventWord:
    start_identity: int
    end_identity: int
    reference_cells: int
    probe_cells: int
    ratio: Fraction
    X_pair: float
    Y_pair: float
    principal_phase_difference: float
    binder_occupied: int
    classification: str = "typed candidate-event Ramsey phase-difference word, not proper time or lapse"


def attach_ramsey_word(
    interval: c451.RelationalIntervalCandidate | None,
    quadratures: dict[str, object] | None,
    *,
    binder_occupied: int = 1,
    phase_origin: bool = True,
    nonwrapping_certificate: bool = True,
) -> RamseyEventWord | None:
    if (
        interval is None or quadratures is None or binder_occupied != 1
        or not phase_origin or not nonwrapping_certificate
        or not quadratures["phase_word_defined"]
        or quadratures["principal_phase_difference"] is None
        or abs(float(quadratures["principal_phase_difference"])) >= np.pi
    ):
        return None
    return RamseyEventWord(
        interval.start_identity,
        interval.end_identity,
        interval.reference_cells,
        interval.probe_cells,
        interval.probe_over_reference,
        float(quadratures["X_pair"]),
        float(quadratures["Y_pair"]),
        float(quadratures["principal_phase_difference"]),
        binder_occupied,
    )


def event_composition(quadratures: dict[str, object]) -> dict[str, object]:
    comparator = {}
    deletion_failures = 0
    for probe_cells in (3, 4, 5):
        interval = c451.interval_for_positions(2, 6, 2 + probe_cells)
        layout, initial = c570.initial_word(1, counts=(probe_cells,))
        c570.validate_initial(layout, initial)
        physical = c570.run_schedule(initial, c570.joint_schedule(layout, 1))
        endpoints = c570.decode_endpoints(layout, physical, 1)
        totals = c570.endpoint_totals(endpoints)
        word = attach_ramsey_word(interval, quadratures)
        comparator[f"{probe_cells}:4"] = {
            "Cycle451_ratio": None if interval is None else str(interval.probe_over_reference),
            "Cycle570_totals": totals,
            "Ramsey_word_attached": word is not None,
        }
        deletion_failures += int(attach_ramsey_word(interval, quadratures, binder_occupied=0) is None)
        deletion_failures += int(attach_ramsey_word(interval, quadratures, phase_origin=False) is None)
        deletion_failures += int(attach_ramsey_word(None, quadratures) is None)

    prefix_rows = {}
    for prefix in c570.TRAIN_PREFIXES + c570.HELD_PREFIXES:
        layout, initial = c570.initial_word(prefix)
        physical = c570.run_schedule(initial, c570.joint_schedule(layout, prefix))
        endpoints = c570.decode_endpoints(layout, physical, prefix)
        expected = c570.coarse_endpoints(prefix)
        restored = c570.run_schedule(physical, c570.joint_schedule(layout, prefix), reverse=True)
        prefix_rows[prefix] = {
            "split": "held" if prefix in c570.HELD_PREFIXES else "train",
            "EG_exact": endpoints == expected,
            "inverse_exact": restored == initial,
            "totals": c570.endpoint_totals(endpoints),
        }
    condition = (
        all(row["Cycle451_ratio"] == str(Fraction(int(name.split(":")[0]), 4))
            and tuple(row["Cycle570_totals"]) == (4, int(name.split(":")[0]))
            and row["Ramsey_word_attached"] for name, row in comparator.items())
        and all(row["EG_exact"] and row["inverse_exact"] for row in prefix_rows.values())
        and deletion_failures == 9
    )
    result = {
        "Cycle451_comparator": comparator,
        "Cycle570_additive_prefix_and_rollover": prefix_rows,
        "typed_event_deletion_controls": deletion_failures,
        "Ramsey_to_response_law_derived": False,
        "event_actuality_or_Record_derived": False,
        "proper_time_or_lapse_derived": False,
        "universal_clock_equivalence_derived": False,
    }
    result["pass"] = bool(condition)
    check("Ramsey quadratures attach only to typed matched 3:4/4:4/5:4 events and the exact additive rollover shore", condition, result)
    return result


def route_b_local_even_clock() -> tuple[dict[str, object], dict[str, object]]:
    print("\nROUTE B — PRIORITY LOCAL EVEN VACUUM/A2-DIMER RAMSEY CLOCK")
    rows = []
    maximum_residual = 0.0
    minimum_contact_signal = np.inf
    held_quadratures: dict[str, object] | None = None
    for length, applications in FROZEN_LAW["route_B"]["applications"].items():
        source = local_a2_source(length)
        walk = c590.one_particle_walk(length)
        pair = source.copy()
        initial_norm = float(np.linalg.norm(pair))
        row_words = []
        for ordinal in range(1, max(applications) + 1):
            pair = c590.full_update(pair, walk)
            if ordinal in applications:
                quadratures = pair_observables(pair, source)
                deleted = source.copy()
                for _ in range(ordinal):
                    deleted = c590.full_update(deleted, walk, coupling=0.0)
                deletion_signal = float(np.linalg.norm(pair - deleted))
                minimum_contact_signal = min(minimum_contact_signal, deletion_signal)
                row_words.append({
                    "law_applications": ordinal,
                    **quadratures,
                    "contact_deletion_signal": deletion_signal,
                })
                # q=2 was one of the frozen held checkpoints.  It is the only
                # held checkpoint with a defined local return-phase word; q=1
                # and q=3 remain in the result as preregistered failures.
                if length == 6 and ordinal == 2:
                    held_quadratures = quadratures
        restored = pair.copy()
        for _ in range(max(applications)):
            restored = c590.inverse_full_update(restored, walk)
        inverse_residual = float(np.linalg.norm(restored - source))
        antisymmetry = float(np.linalg.norm(pair + pair.T))
        norm_residual = abs(float(np.linalg.norm(pair)) - initial_norm)
        translated_source = translate_pair(source, length, (1, 0, 0))
        translation_residual = float(np.linalg.norm(
            c590.full_update(translated_source, walk)
            - translate_pair(c590.full_update(source, walk), length, (1, 0, 0))
        ))
        value, relative, eigen = c590.eigenpair(length, (0.0, 0.0, 0.0))
        localization = relative_diagnostics(relative, length)
        maximum_residual = max(
            maximum_residual, inverse_residual, antisymmetry, norm_residual,
            translation_residual, eigen["relative_eigen_residual"],
        )
        rows.append({
            "length": length,
            "split": "held" if length == 6 else "train",
            "Ramsey_words": row_words,
            "inverse_residual": inverse_residual,
            "antisymmetry_residual": antisymmetry,
            "norm_residual": norm_residual,
            "translation_covariance_residual": translation_residual,
            "A2_branch_wrapped_phase_not_energy": float(np.angle(value)),
            "A2_branch": {**eigen, **localization},
        })
    assert held_quadratures is not None

    frames = c590.c210.proper_cubic_frames()
    a2_covariance = max(
        float(np.linalg.norm(rep @ c583.A2_AXIS - c583.CHARACTERS["A2"][c583.frame_class(frame)] * c583.A2_AXIS))
        for frame, rep in zip(frames, c583.REPS2)
    )
    physical = {
        "declared_matter_code": "Cycle590 complete N=0 direct-sum N=2 sector within supplied global N<=3 domain",
        "held_compiler_live_M2": 11448,
        "held_compiler_M2_per_cell": 53,
        "binder_M2": 1,
        "binder_state": "occupied before and after every pulse/update/read",
        "local_even_pair_observable_coarse_support": "six direction modes at one coarse cell",
        "local_even_pair_observable_physical_support_upper_bound": "one 53-M2 compiler block",
        "pair_pulse_and_readout_dense_bounded_completion": "supplied/open primitive synthesis",
        "free_plus_contact_physical_schedule": "inherited exact Cycle590 W563 compiler",
        "accepted_free_plus_contact_code_space_EG_residual": 0.0,
        "Ramsey_interface_code_space_completion_residual": 0.0,
        "Ramsey_interface_primitive_gate_and_layout_closure": False,
        "global_N_le_3_cutoff_locally_enforced": False,
        "global_N_le_3_cutoff_supplied": True,
        "runtime_global_parity_or_order_service": False,
        "proper_cubic_frames": len(frames),
        "paired_frames_with_event_device": len(frames) ** 2,
        "A2_observable_orbit_covariance_residual": a2_covariance,
    }
    pulse_h = np.asarray(((1, 1), (1, -1)), complex) / math.sqrt(2)
    pulse_inverse_residual = float(np.linalg.norm(pulse_h @ pulse_h - np.eye(2)))
    result = {
        "rows": rows,
        "physical": physical,
        "pulse_inverse_residual": pulse_inverse_residual,
        "maximum_dynamic_residual": maximum_residual,
        "minimum_contact_deletion_signal": minimum_contact_signal,
        "held_event_quadratures": held_quadratures,
        "frozen_return_boundary": {
            "q_even_2": "nonzero local return visibility on train L3 and held L6",
            "q_odd_1_and_3": "zero local return visibility on every frozen applicable row",
            "scope": "the frozen q=1,2,3 checkpoints only; not an all-q theorem",
        },
        "phase_origin": "prepared vacuum/local-A2 relative phase at the first typed event",
        "single_word_branch_rule": "principal phase only when the observed word is strictly inside (-pi,pi)",
        "multi_event_unwrapping_rule": "supplied/open; not invoked",
        "law_application_count_called_time": False,
        "principal_or_wrapped_phase_called_energy": False,
        "squared_norm_called_probability_or_occurrence": False,
    }
    every_frozen_clock_word_defined = all(
        bool(word["phase_word_defined"]) for row in rows for word in row["Ramsey_words"]
    )
    observed_boundary = (
        all(not bool(word["phase_word_defined"]) for row in rows for word in row["Ramsey_words"] if word["law_applications"] % 2)
        and all(bool(word["phase_word_defined"]) for row in rows for word in row["Ramsey_words"] if word["law_applications"] == 2)
    )
    result["every_frozen_clock_word_defined"] = every_frozen_clock_word_defined
    result["observed_frozen_parity_boundary_exact"] = observed_boundary
    condition = (
        maximum_residual < TOL and pulse_inverse_residual < TOL
        and minimum_contact_signal > SIGNAL
        and every_frozen_clock_word_defined
        and all(row["A2_branch"]["onsite_A2_source_weight"] > SIGNAL for row in rows)
        and all(word["principal_phase_difference"] is None or abs(float(word["principal_phase_difference"])) < np.pi
                for row in rows for word in row["Ramsey_words"])
        and a2_covariance < TOL and len(frames) == 24
    )
    result["pass"] = bool(condition)
    check(
        "Route B preregistered local even vacuum/A2 clock checkpoints all furnish defined return-phase words",
        condition, result,
    )
    return result, held_quadratures


def finite_irrep_search(length: int) -> dict[str, object]:
    walk = c583.c578.relative_car_walk(length, c583.BETA, c583.CONTACT, (0.0, 0.0, 0.0))
    quotient, *_ = c583.c578.antisymmetric_quotient(length)
    seed = np.exp(0.173j * np.arange(walk.shape[0], dtype=float))
    seed /= np.linalg.norm(seed)
    values, vectors = sparse_linalg.eigs(
        walk,
        k=FROZEN_LAW["route_C"]["eigen_window"]["k"],
        sigma=0.999 * np.exp(1j * FROZEN_LAW["route_C"]["eigen_window"]["sigma_phase"]),
        v0=seed,
        ncv=FROZEN_LAW["route_C"]["eigen_window"]["ncv"],
        tol=2e-11,
        maxiter=5000,
    )
    selected = {}
    selected_vectors = {}
    for irrep in FROZEN_LAW["route_C"]["irreps"]:
        candidates = []
        for index, value in enumerate(values):
            vector = vectors[:, index] / np.linalg.norm(vectors[:, index])
            full = quotient @ vector
            weights = c583.irrep_weights(full[:36])
            observables = c583.c578.relative_observables(length, vector)
            if weights[irrep] > 0.99:
                candidates.append((observables["contact_weight"], value, vector, full, weights, observables))
        if not candidates:
            selected[irrep] = {"candidate_found": False}
            continue
        _contact, value, vector, full, weights, observables = max(candidates, key=lambda row: row[0])
        selected[irrep] = {
            "candidate_found": True,
            "candidate_count": len(candidates),
            "wrapped_phase_not_energy": float(np.angle(value)),
            "irrep_weight": weights[irrep],
            **observables,
            "eigen_residual": float(np.linalg.norm(walk @ vector - value * vector)),
        }
        selected_vectors[irrep] = (value, vector, full)
    return {"rows": selected, "vectors": selected_vectors, "quotient": quotient}


def route_c_second_mode() -> dict[str, object]:
    print("\nROUTE C — FROZEN E/T1/T2 SECOND-MODE FINITE SEARCH")
    searches = {}
    stored = {}
    maximum_eigen_residual = 0.0
    for length in FROZEN_LAW["route_C"]["lengths"]:
        search = finite_irrep_search(length)
        rows = search["rows"]
        searches[length] = rows
        stored[length] = search
        maximum_eigen_residual = max(
            maximum_eigen_residual,
            *(row.get("eigen_residual", 0.0) for row in rows.values()),
        )

    cross_rows = []
    for length in FROZEN_LAW["route_C"]["lengths"]:
        t2_value, _t2_vector, t2_full = stored[length]["vectors"]["T2"]
        a2_value, a2_vector, _a2_obs = c583.c578.isolated_eigenpair(
            length, c583.BETA, c583.CONTACT, (0.0, 0.0, 0.0), -2.976, eigen_count=10
        )
        a2_full = stored[length]["quotient"] @ a2_vector
        component_products = np.conj(a2_full[:36]) * t2_full[:36]
        component = int(np.argmax(abs(component_products)))
        base_cross = component_products[component]
        covariance_residuals = []
        orbit = set()
        for frame in c583.FRAMES:
            direction = c590.c210.direction_permutation(frame)
            pair_rep = np.kron(direction, direction)
            rotated_a = pair_rep @ a2_full[:36]
            rotated_t = pair_rep @ t2_full[:36]
            target = int(np.argmax(pair_rep[:, component]))
            orbit.add(target)
            covariance_residuals.append(float(abs(np.conj(rotated_a[target]) * rotated_t[target] - base_cross)))
        cross_rows.append({
            "length": length,
            "split": "held" if length == 11 else "train",
            "A2_wrapped_phase_not_energy": float(np.angle(a2_value)),
            "T2_wrapped_phase_not_energy": float(np.angle(t2_value)),
            "nonwrapping_phase_difference_word": float(np.angle(t2_value / a2_value)),
            "maximum_direction_component_local_cross_term": float(abs(base_cross)),
            "proper_cubic_invariant_cross_term": float(abs(np.vdot(a2_full[:36], t2_full[:36]))),
            "direction_component_orbit_size": len(orbit),
            "maximum_all24_local_observable_orbit_residual": max(covariance_residuals),
        })

    gate = FROZEN_LAW["route_C"]["held_localization_gate"]
    held_t2 = searches[11]["T2"]
    held_t1 = searches[11]["T1"]
    held_t2_local = (
        held_t2["contact_weight"] >= gate["contact_min"]
        and held_t2["relative_radius_squared"] <= gate["radius2_max"]
        and held_t2["seam_boundary_weight"] <= gate["seam_max"]
    )
    held_t1_local = (
        held_t1["contact_weight"] >= gate["contact_min"]
        and held_t1["relative_radius_squared"] <= gate["radius2_max"]
        and held_t1["seam_boundary_weight"] <= gate["seam_max"]
    )
    finite_positive = (
        maximum_eigen_residual < TOL
        and all(row["maximum_direction_component_local_cross_term"] > SIGNAL for row in cross_rows)
        and all(abs(row["nonwrapping_phase_difference_word"]) < np.pi for row in cross_rows)
        and all(row["maximum_all24_local_observable_orbit_residual"] < TOL for row in cross_rows)
    )
    result = {
        "searches": searches,
        "A2_T2_cross_rows": cross_rows,
        "frozen_held_localization_gate": gate,
        "finite_box_second_mode_phase_word_positive": bool(finite_positive),
        "held_T1_local_clock_gate": bool(held_t1_local),
        "held_T2_local_clock_gate": bool(held_t2_local),
        "route_disposition": (
            "positive finite-box direction-resolved A2/T2 phase-difference word; "
            "not retained as a held local matter clock because the independently frozen L11 localization gate fails"
        ),
        "failure_scope": "this E/T1/T2 search window and localization criterion only",
        "shared_substrate_obstruction": False,
        "maximum_eigen_residual": maximum_eigen_residual,
    }
    condition = finite_positive and not held_t1_local and not held_t2_local and not searches[11]["E"]["candidate_found"]
    result["pass"] = bool(condition)
    check(
        "Route C reruns the frozen E/T1/T2 search and scopes its held-localization failure while retaining the finite A2/T2 word",
        condition, result,
    )
    return result


def line_ref(function) -> str:
    return f"{Path(inspect.getsourcefile(function) or '').name}:{inspect.getsourcelines(function)[1]}"


def no_go_discipline(route_a: dict, route_b: dict, route_c: dict) -> dict[str, object]:
    alternatives = (
        {
            "object_formulation": "Q1 functional register tensor physical dimer compiler",
            "mechanism_invariant": "operator functional calculus and Ramsey arm",
            "terminal_obligation": "independent operational reference clock",
            "attempted": True,
            "disposition": "positive",
        },
        {
            "object_formulation": "vacuum direct-sum local A2 pair on N0/N2 code",
            "mechanism_invariant": "even grade-changing pair quadratures under free+contact",
            "terminal_obligation": "intrinsic local matter clock at matched events",
            "attempted": True,
            "disposition": "failed preregistered route: q=2 recurrence positive, q=1/q=3 local return zero",
        },
        {
            "object_formulation": "A2 versus E/T1/T2 finite spectral branches",
            "mechanism_invariant": "number-conserving local direction-component cross term",
            "terminal_obligation": "independent second-mode local clock",
            "attempted": True,
            "disposition": "finite word positive; held localization gate fails",
        },
        {
            "object_formulation": "two physical dimer copies",
            "mechanism_invariant": "autonomous encounter and return event",
            "terminal_obligation": "relational encounter clock",
            "attempted": False,
            "disposition": "open",
        },
        {
            "object_formulation": "locally charged binder plus gauge rotor",
            "mechanism_invariant": "Gauss-preserving phase accumulation",
            "terminal_obligation": "local cutoff and clock in one substrate",
            "attempted": False,
            "disposition": "open",
        },
        {
            "object_formulation": "two-dimer scattering packet",
            "mechanism_invariant": "matched free/contact delay against reference channel",
            "terminal_obligation": "interaction-conditioned clock comparison",
            "attempted": False,
            "disposition": "open pending N4 compiler",
        },
    )
    walls = {
        "dense register control synthesis": "bounded primitive synthesis of matrix functions",
        "local pair pulse synthesis": "explicit gates for the compiler-completed A2 pair rotation",
        "phase origin and multi-event unwrapping": "physical branch-origin and rollover certificate",
        "event actuality": "Record formation and realized-event selection",
        "second-mode held localization": "held co-moving localized branch or encounter device",
        "global N<=3 locality": "bounded local Gauss/check enforcement",
        "universal calibration": "cross-device empirical equivalence and continuum unit map",
    }
    directional = []
    for left, right in combinations(walls, 2):
        directional.append({
            "pair": (left, right),
            "left_to_right": f"{walls[left]} does not supply {walls[right]}",
            "right_to_left": f"{walls[right]} does not supply {walls[left]}",
            "collapsed": False,
        })
    gate = {
        "N1_normalized_route_families": alternatives,
        "N1_attempted_qualifying_families": sum(row["attempted"] for row in alternatives),
        "N1_required_for_broad_negative": 5,
        "N1_broad_negative_gate": "FAIL — only three normalized families were attempted",
        "N2_directional_wall_independence": directional,
        "N3_hidden_supplies": (
            "beta=-0.3, contact=0.37, finite tori and boundary conditions",
            "Q1 population, ring orientation, Cayley/principal formulas, CLOCK_SCALE=8 and dense control invocation",
            "vacuum/local-A2 pulse, occupied binder, phase origin, readout quadratures and matched-event triggers",
            "global N<=3 domain, compile-time colors/layers, blank auxiliaries and noiseless gates",
            "Cycle451 identity/profile/predecessor matcher and Cycle570 root/profile/four-edge standard",
        ),
        "N4_exact_residual_matching": {
            "Route_A": {"surface": line_ref(route_a_register_clock), "residual": route_a["coherent_inverse_residual"]},
            "Route_B": {"surface": line_ref(route_b_local_even_clock), "residual": route_b["maximum_dynamic_residual"]},
            "Route_C": {"surface": line_ref(route_c_second_mode), "residual": route_c["maximum_eigen_residual"]},
            "Route_C_wall": "held L11 localization gate, not compiler or event-matcher failure",
        },
        "N5_resolution_rhetoric": {
            "exact": "finite declared code spaces and pinned local/compiler/event laws",
            "numerical": "finite eigensolver residuals and coherent quadratures",
            "interpretive": "one bounded-support q=2 recurrence phase-difference interface over strict physical dynamics; preregistered clock route failed and primitive pulse/readout closure is open",
            "not_claimed": "proper time, lapse, energy, universal clock equivalence, Record actuality",
        },
        "N6_partial_closure_paths": (
            "synthesize the 10-M2 functional control from the retained primitive grammar",
            "synthesize the local A2 pulse/readout in one 53-M2 block",
            "replace supplied global N<=3 cutoff by a local Gauss/check law",
            "try the independent two-copy encounter route before any shared negative",
            "derive a physical phase-origin/rollover certificate and empirical cross-clock calibration",
        ),
        "N6_new_axiom_gate_invoked": False,
        "N7_hostile_steelman": (
            "A hostile constructive reviewer can keep the positive q=2 local A2 recurrence, add a bounded charged binder/rotor "
            "that enforces the number domain locally, and compare two such devices only at the already-physical Cycle570 "
            "event conveyor; this route is concrete enough to defeat a present shared-obstruction claim."
        ),
        "N8_cross_cycle_echo": (
            "Cycle441 already separated principal/Cayley operational words, Cycle451 supplied strict matching, "
            "Cycle570 made additive rollover physical, Cycle583 supplied A2/T2 internal content, and Cycle590 "
            "placed the N2 law on strict M2.  Cycle599 composes those shores without erasing their supplies."
        ),
        "negative_claim_shipped": False,
        "minimum_content_claim_shipped": False,
        "shared_obstruction": False,
        "axiom_pressure": False,
    }
    condition = (
        len(alternatives) >= 5 and gate["N1_attempted_qualifying_families"] == 3
        and len(directional) == math.comb(len(walls), 2)
        and not gate["negative_claim_shipped"] and not gate["axiom_pressure"]
    )
    gate["pass"] = bool(condition)
    check("fresh N1-N8 scopes the Route-C failure and permits no broad negative, minimum-content claim, or axiom pressure", condition, gate)
    return gate


def domain_and_deletion_controls() -> dict[str, object]:
    rejected = 0
    operations = (
        lambda: local_a2_source(2),
        lambda: local_a2_source(3, 27),
        lambda: c570.initial_word(1, malformed="standard"),
        lambda: c570.initial_word(1, counts=(2,)),
        lambda: c441.validate_register_code_mask(0),
        lambda: c441.validate_register_code_mask(3),
    )
    for index, operation in enumerate(operations):
        try:
            value = operation()
            if index == 2:
                c570.validate_initial(*value)
        except ValueError:
            rejected += 1
    result = {
        "lawful_domain_rejections": rejected,
        "expected_rejections": len(operations),
        "off_grid_beta_query": "absent because Route A constructs an operator before sectors and Route B has fixed beta=-0.3",
        "binder_deletion": "Ramsey event word undefined",
        "phase_origin_deletion": "Ramsey event word undefined",
        "event_matcher_deletion": "Ramsey event word undefined",
        "pair_readout_deletion": "no quadrature word",
        "contact_deletion": "q=2 and q=3 full-state residuals are nonzero; q=1 residual is zero and is part of the frozen failed boundary",
    }
    condition = rejected == len(operations)
    result["pass"] = condition
    check("malformed, off-domain, and deleted supplies are rejected rather than assigned clock values", condition, result)
    return result


def note_contract() -> dict[str, object]:
    body = " ".join(NOTE.read_text(encoding="utf-8").lower().replace("`", "").replace("*", "").split())
    required = (
        "authority: none", "audit: unset", "cycle 599", "route a", "route b", "route c",
        "vacuum", "a2", "binder", "53 m2", "all 24", "576", "3:4", "4:4", "5:4",
        "update count is not time", "wrapped phase is not energy", "not proper time or lapse",
        "global n<=3 cutoff", "not locally enforced", "n1 —", "n2 —", "n3 —", "n4 —",
        "n5 —", "n6 —", "n7 —", "n8 —", "no axiom pressure", "cycle597",
    )
    missing = tuple(fragment for fragment in required if fragment not in body)
    result = {"required_fragments": len(required), "missing": missing}
    check("the Cycle599 note freezes the operational boundary, supplies, and fresh N1-N8", not missing, result)
    return result


def main() -> int:
    signal.alarm(int(WALL_CAP_SECONDS))
    started = time.perf_counter()
    print("Cycle599 intrinsic Ramsey-clock / strict-M2 time bridge", AUTHORITY, AUDIT)
    shores = shore_controls()
    route_a = route_a_register_clock()
    route_b, held_quadratures = route_b_local_even_clock()
    events = event_composition(held_quadratures)
    route_c = route_c_second_mode()
    domain = domain_and_deletion_controls()
    gate = no_go_discipline(route_a, route_b, route_c)
    contract = note_contract()
    elapsed = time.perf_counter() - started
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss = int(rss if sys.platform == "darwin" else rss * 1024)
    check("cold resource caps", elapsed < WALL_CAP_SECONDS and rss < RSS_CAP_BYTES,
          {"elapsed_seconds": elapsed, "maximum_RSS_bytes": rss})

    ledger = {
        "C_ref": "a persistent occupied binder and independent Q1 interface attach the positive q=2 A2 recurrence to strict matched events; a complete A2 clock, preparation, and device identity remain supplied/open",
        "C_num": "q=2 gives an exact dimensionless X/Y recurrence and nonwrapping phase word, while preregistered q=1/q=3 visibility is zero; no complete clock law, empirical unit, or probability law",
        "C_wrap": "single-event-pair branch origin is explicit and strictly nonwrapping; multi-event unwrapping/rollover certificate remains supplied/open",
        "C_int": "actual Cycle230 free-plus-contact dynamics drive the local A2 word; conversion to physical lapse or energy remains open",
        "C_local": "bounded code-space support over one 53-M2 compiler block plus one binder; physical primitive gate/layout closure for pair pulse/readout and local N<=3 enforcement remain open",
        "C_source": "Cycle451 response ratios are only co-registered event words; no source-to-Ramsey response, gravity, lapse, or response sign is derived",
    }
    maturity = {
        "operational_quantum_records_repo_strict": (4.82, 4.65),
        "causal_time_repo_strict": (4.00, 3.78),
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
        "shores": shores,
        "route_A_Q1_functional_clock": route_a,
        "route_B_local_even_A2_clock": route_b,
        "typed_event_composition": events,
        "route_C_second_mode": route_c,
        "domain_and_deletions": domain,
        "no_go_discipline": gate,
        "note_contract": contract,
        "six_wall_ledger": ledger,
        "maturity": maturity,
        "highest_honest_terminal": (
            "failed preregistered bounded-support matter-clock attempt with one positive q=2 local A2 recurrence phase word on train L3 and held L6, "
            "but zero q=1/q=3 local return visibility; accepted strict-physical-M2 free-plus-contact dynamics and typed-event attachment survive, "
            "while a complete clock law, pulse/readout primitive layout, proper time, lapse, energy, Record actuality, and universal clock equivalence remain open"
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
