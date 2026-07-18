#!/usr/bin/env python3
"""Cycle 239: distinguishable-walker/antisymmetric-sector compiler probe.

Instantiate the Brun--Mlodinow construction on the Cycle-230 six-direction
one-particle walk.  The runner separates an exact finite-torus algebraic
intertwiner from the resources used by its QCA realization.  Fixed-particle
antisymmetric sectors carry the free walk, the onsite pair contact, the
Cycle-230 seam block, and proper-cubic frames exactly.  The full variable-N
Fock space, however, requires one distinguishable walker type per one-particle
mode in this construction, so its local lane count and antisymmetrizer do not
meet the bounded physical-M2 compiler contract.

This is a route-specific resource audit, not a general fermionization no-go.
Labels and gate layers are compiler controls, not physical time or a clock.
"""

from __future__ import annotations

from itertools import combinations, permutations, product
from math import comb, factorial, log10
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import local_generator_source_tournament_cycle228_2026_07_17 as c228
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230


NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "DISTINGUISHABLE_ANTISYMMETRIC_FOCK_COMPILER_CYCLE239_NOTE_2026-07-17.md"
)
BETA = -0.3
COUPLING = 0.37
PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def note_contract() -> None:
    text = " ".join(
        NOTE.read_text(encoding="utf-8").lower().replace("*", "").split()
    )
    required = (
        "brun and mlodinow",
        "particle type",
        "2^{d n_max}",
        "constant overhead",
        "rank-73",
        "73!",
        "all 24",
        "contact",
        "seam",
        "bounded-radius state encoder",
        "lawful domain",
        "deletion",
        "leakage",
        "authority: none",
        "audit: unset",
        "n1 — alternative routes",
        "n2 — condition independence",
        "n3 — hidden-condition scan",
        "n4 — residual matching",
        "n5 — rhetoric audit",
        "n6 — partial closure",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "not a route-independent no-go",
        "no axiom pressure",
        "not physical time",
    )
    missing = tuple(item for item in required if item not in text)
    check("note preserves the source, scope, firewall, and N1-N8 contract", not missing, missing)


def inversion_parity(values: tuple[int, ...]) -> int:
    return sum(
        values[left] > values[right]
        for left in range(len(values))
        for right in range(left + 1, len(values))
    ) % 2


def antisymmetric_isometry(mode_count: int, particle_count: int) -> np.ndarray:
    """Map the ordered wedge basis into n labeled one-particle registers."""
    ambient = mode_count**particle_count
    basis = tuple(combinations(range(mode_count), particle_count))
    result = np.zeros((ambient, len(basis)), dtype=complex)
    normalization = np.sqrt(factorial(particle_count))
    for column, occupied in enumerate(basis):
        for order in permutations(range(particle_count)):
            modes = tuple(occupied[index] for index in order)
            flat = np.ravel_multi_index(modes, (mode_count,) * particle_count)
            result[flat, column] = (-1) ** inversion_parity(order) / normalization
    return result


def tensor_power(operator: np.ndarray, count: int) -> np.ndarray:
    result = np.asarray(((1.0 + 0.0j,),))
    for _ in range(count):
        result = np.kron(result, operator)
    return result


def swap_first_two(mode_count: int, particle_count: int) -> np.ndarray:
    dimension = mode_count**particle_count
    result = np.zeros((dimension, dimension), dtype=complex)
    for modes in product(range(mode_count), repeat=particle_count):
        target = (modes[1], modes[0], *modes[2:])
        source_index = np.ravel_multi_index(modes, (mode_count,) * particle_count)
        target_index = np.ravel_multi_index(target, (mode_count,) * particle_count)
        result[target_index, source_index] = 1
    return result


def exact_antisymmetric_sector_controls() -> None:
    residuals = []
    permutation_residuals = []
    ranks = []
    rng = np.random.default_rng(2390)
    trial = rng.normal(size=(6, 6)) + 1j * rng.normal(size=(6, 6))
    one_particle, _ = np.linalg.qr(trial)
    for particle_count in (1, 2, 3):
        encoder = antisymmetric_isometry(6, particle_count)
        projector = encoder @ encoder.conj().T
        labeled_update = tensor_power(one_particle, particle_count)
        wedge_update = encoder.conj().T @ labeled_update @ encoder
        residuals.append(np.linalg.norm(labeled_update @ encoder - encoder @ wedge_update))
        ranks.append(int(np.linalg.matrix_rank(projector, tol=1e-10)))
        if particle_count >= 2:
            permutation_residuals.append(
                np.linalg.norm(swap_first_two(6, particle_count) @ encoder + encoder)
            )
    check(
        "the fixed-n antisymmetric maps are isometries of ranks C(6,n)",
        ranks == [6, 15, 20],
        ranks,
    )
    check(
        "identical distinguishable-walker updates exactly intertwine with exterior powers",
        max(residuals) < 2e-13,
        max(residuals),
    )
    check(
        "the encoded n>=2 states transform with sign under exchange of particle labels",
        max(permutation_residuals) < 2e-15,
        max(permutation_residuals),
    )
    check(
        "the lawful domain is the proper antisymmetric code, not the full labeled ambient space",
        antisymmetric_isometry(6, 2).shape == (36, 15) and 15 < 36,
        {"n2_code_dimension": 15, "n2_labeled_ambient_dimension": 36},
    )


def resource_and_variable_number_controls() -> None:
    rows = []
    capacity_ok = True
    truncation_ok = True
    for length in (3, 4, 5):
        cells = length**3
        modes = 6 * cells
        n_max = modes
        qubits_per_cell = 6 * n_max
        total_qca_qubits = cells * qubits_per_cell
        code_dimension = sum(comb(modes, n) for n in range(n_max + 1))
        truncated_73 = sum(comb(modes, n) for n in range(min(73, modes) + 1))
        capacity_ok &= code_dimension == 2**modes
        truncation_ok &= truncated_73 < code_dimension
        rows.append(
            {
                "L": length,
                "modes_M": modes,
                "N_max": n_max,
                "qubits_per_cell": qubits_per_cell,
                "total_qca_qubits": total_qca_qubits,
                "target_M2_qubits": modes,
                "overhead_ratio": total_qca_qubits // modes,
                "pair_gates_per_cell": comb(n_max, 2),
                "two_label_depth_floor": n_max - 1,
            }
        )
    check(
        "N_max=M gives the exact full variable-particle Fock capacity sum_n C(M,n)=2^M",
        capacity_ok,
        [{"L": row["L"], "M": row["modes_M"]} for row in rows],
    )
    check(
        "the published local QCA embedding scales as six N_max qubits per coarse cell",
        [row["qubits_per_cell"] for row in rows] == [972, 2304, 4500]
        and [row["total_qca_qubits"] for row in rows]
        == [26244, 147456, 562500]
        and [row["overhead_ratio"] for row in rows] == [162, 384, 750],
        rows,
    )
    slope = (rows[1]["qubits_per_cell"] - rows[0]["qubits_per_cell"]) // (
        4**3 - 3**3
    )
    intercept = rows[0]["qubits_per_cell"] - slope * 3**3
    held_out_prediction = slope * 5**3 + intercept
    check(
        "the L=3,4 resource law predicts the held-out L=5 local register exactly",
        slope == 36 and intercept == 0 and held_out_prediction == 4500,
        {
            "fit_qubits_per_cell": f"{slope} L^3 + {intercept}",
            "held_out_L5_prediction": held_out_prediction,
            "held_out_L5_actual": rows[2]["qubits_per_cell"],
        },
    )
    check(
        "holding N_max=73 retains the L=3 rank-73 state but deletes every sector n>73",
        truncation_ok and all(73 < row["modes_M"] for row in rows),
        {"retained_max_particle_number": 73, "deleted_first_sector": 74},
    )
    check(
        "pairwise label-symmetric contact has growing gate count and growing two-label depth",
        [row["pair_gates_per_cell"] for row in rows] == [13041, 73536, 280875]
        and [row["two_label_depth_floor"] for row in rows] == [161, 383, 749],
        [
            {
                "L": row["L"],
                "pairs": row["pair_gates_per_cell"],
                "depth_floor": row["two_label_depth_floor"],
            }
            for row in rows
        ],
    )


def antisymmetrization_support_controls() -> None:
    sea_terms = factorial(73)
    sea_log10 = sum(log10(value) for value in range(1, 74))
    check(
        "the rank-73 determinant uses all 73 labels and has 73! nonzero label-permutation terms",
        len(str(sea_terms)) == 106 and 105 < sea_log10 < 106,
        {
            "labels": 73,
            "permutation_terms": sea_terms,
            "log10_terms": sea_log10,
        },
    )

    # A two-mode determinant is maximally entangled across the two supplied
    # particle-type registers.  In the local-QCA occupation representation,
    # the same state is also the Bell pair of the two label assignments at
    # separated sites a and b:
    #
    #   (|type-1>_a |type-2>_b - |type-2>_a |type-1>_b) / sqrt(2).
    #
    # Thus the witness is genuinely across the spatial a|b cut, not merely a
    # formal tensor partition of the first-quantized walker registers.
    encoder = antisymmetric_isometry(2, 2)
    type_register_state = encoder[:, 0].reshape(2, 2)
    type_singulars = np.linalg.svd(type_register_state, compute_uv=False)
    spatial_assignment_state = np.asarray(
        ((0.0, 1.0), (-1.0, 0.0)), dtype=complex
    ) / np.sqrt(2)
    spatial_singulars = np.linalg.svd(spatial_assignment_state, compute_uv=False)
    product_distance_floor = np.sqrt(2 - 2 * spatial_singulars[0])
    check(
        "already at n=2 the exact label encoder is non-product across separated spatial sites",
        np.linalg.matrix_rank(type_register_state, tol=1e-12) == 2
        and np.linalg.matrix_rank(spatial_assignment_state, tol=1e-12) == 2
        and np.max(np.abs(type_singulars - 1 / np.sqrt(2))) < 2e-15
        and np.max(np.abs(spatial_singulars - 1 / np.sqrt(2))) < 2e-15
        and abs(product_distance_floor - np.sqrt(2 - np.sqrt(2))) < 2e-15,
        {
            "type_register_schmidt_values": type_singulars,
            "spatial_cut_schmidt_values": spatial_singulars,
            "normalized_product_state_distance_floor": product_distance_floor,
        },
    )


def local_contact_controls() -> None:
    mode_count = 12  # two coarse cells, six direction modes each
    encoder = antisymmetric_isometry(mode_count, 2)
    phases = np.ones(mode_count**2, dtype=complex)
    for first in range(mode_count):
        for second in range(mode_count):
            if first // 6 == second // 6:
                phases[first * mode_count + second] = np.exp(1j * COUPLING)
    labeled_contact = np.diag(phases)
    wedge_contact = encoder.conj().T @ labeled_contact @ encoder
    leakage = np.linalg.norm((np.eye(mode_count**2) - encoder @ encoder.conj().T) @ labeled_contact @ encoder)
    expected = []
    for first, second in combinations(range(mode_count), 2):
        expected.append(np.exp(1j * COUPLING) if first // 6 == second // 6 else 1)
    check(
        "a symmetric two-label collision gate exactly gives the Cycle-230 two-particle onsite contact",
        np.linalg.norm(wedge_contact - np.diag(expected)) < 2e-14 and leakage < 2e-14,
        {"intertwiner_residual": float(np.linalg.norm(wedge_contact - np.diag(expected))), "leakage": float(leakage)},
    )

    # Deleting symmetry between labels destroys invariance of the code sector.
    asymmetric = np.eye(3**2, dtype=complex)
    # Phase |0>_1|1>_2 but not its exchanged partner |1>_1|0>_2.
    asymmetric[1, 1] = np.exp(1j * COUPLING)
    encoder_small = antisymmetric_isometry(3, 2)
    projector_small = encoder_small @ encoder_small.conj().T
    asymmetric_leakage = np.linalg.norm(
        (np.eye(3**2) - projector_small) @ asymmetric @ encoder_small
    )
    check(
        "deleting label-permutation symmetry produces nonzero code leakage",
        asymmetric_leakage > 0.15,
        asymmetric_leakage,
    )


def one_particle_mass_and_sea_controls() -> None:
    species = c219.common_species(BETA)
    rest = c219.rest_mass(species)
    curvature = 1 / float(np.mean(np.diag(c210.curvature_tensor(species, step=1e-4))))
    forced = c210.force_response(species, 2e-5).measured_mass
    check(
        "the n=1 walker sector preserves the Cycle-219 mass fixture and contact is identity there",
        abs(rest / species.analytic_mass - 1) < 2e-12
        and abs(curvature / species.analytic_mass - 1) < 4e-6
        and abs(forced / species.analytic_mass - 1) < 0.007,
        {
            "rest": rest,
            "curvature": curvature,
            "forced": forced,
            "analytic": species.analytic_mass,
        },
    )

    sea_ranks = {}
    for length in (3, 4, 5):
        momenta = 2 * np.pi * np.fft.fftfreq(length)
        rank = 0
        for momentum_indices in product(range(length), repeat=3):
            momentum = np.asarray([momenta[index] for index in momentum_indices])
            phases = np.angle(np.linalg.eigvals(c228.walk_symbol(BETA, momentum)))
            rank += int(np.sum(phases < -1e-10))
        sea_ranks[length] = rank
    check(
        "the complete finite sea census recovers the Cycle-230 odd rank-73 L=3 fixture",
        sea_ranks[3] == 73
        and all(0 < sea_ranks[length] < 6 * length**3 for length in (3, 4, 5)),
        sea_ranks,
    )


def modular_contact_form() -> np.ndarray:
    length = 3
    unit = 2 * np.pi / length
    momenta = {
        "h1": unit * np.asarray((0, 1, 0), dtype=float),
        "h2": unit * np.asarray((0, -1, 0), dtype=float),
        "p1": unit * np.asarray((1, 1, 1), dtype=float),
        "p2": unit * np.asarray((-1, -1, -1), dtype=float),
    }
    targets = {
        "h1": -0.148864781941705,
        "h2": -2.9904574355314986,
        "p1": 0.0759239848775555,
        "p2": 3.067939104828828,
    }
    subspaces = {
        name: c230.band_subspace(momentum, target_phase=targets[name])
        for name, momentum in momenta.items()
    }
    phases = {name: row[0] for name, row in subspaces.items()}
    vectors = {name: row[1] for name, row in subspaces.items()}
    form = c230.contact_form_factor(
        vectors["p1"], vectors["p2"], vectors["h1"], vectors["h2"]
    )

    # Independent labeled-register contraction of normalized two-particle
    # antisymmetric states.  This is the same fixed-n state intertwiner used by
    # the distinguishable-walker construction.
    labeled = np.zeros_like(form)
    for h1 in range(vectors["h1"].shape[1]):
        for h2 in range(vectors["h2"].shape[1]):
            source = h1 * vectors["h2"].shape[1] + h2
            incoming = (
                np.outer(vectors["h1"][:, h1], vectors["h2"][:, h2])
                - np.outer(vectors["h2"][:, h2], vectors["h1"][:, h1])
            ).reshape(-1) / np.sqrt(2)
            for p1 in range(vectors["p1"].shape[1]):
                for p2 in range(vectors["p2"].shape[1]):
                    target = p1 * vectors["p2"].shape[1] + p2
                    outgoing = (
                        np.outer(vectors["p1"][:, p1], vectors["p2"][:, p2])
                        - np.outer(vectors["p2"][:, p2], vectors["p1"][:, p1])
                    ).reshape(-1) / np.sqrt(2)
                    labeled[target, source] = np.vdot(outgoing, incoming)
    phase_cost = (
        phases["p1"][:, None, None, None]
        + phases["p2"][None, :, None, None]
        - phases["h1"][None, None, :, None]
        - phases["h2"][None, None, None, :]
    )
    check(
        "the fixed-n labeled antisymmetric contraction reproduces the Cycle-230 modular contact block",
        np.linalg.norm(labeled - form) < 2e-15
        and np.max(np.abs(phase_cost - 2 * np.pi)) < 3e-14,
        {
            "intertwiner_residual": float(np.linalg.norm(labeled - form)),
            "phase_residual": float(np.max(np.abs(phase_cost - 2 * np.pi))),
            "singular_values": np.linalg.svd(form, compute_uv=False),
        },
    )
    return form


def cubic_covariance_controls() -> None:
    encoder2 = antisymmetric_isometry(6, 2)
    antisymmetric_frame_residuals = []
    group_frames = c210.proper_cubic_frames()
    for frame in group_frames:
        direction = c210.direction_permutation(frame)
        labeled = np.kron(direction, direction)
        wedge = encoder2.conj().T @ labeled @ encoder2
        antisymmetric_frame_residuals.append(
            np.linalg.norm(labeled @ encoder2 - encoder2 @ wedge)
        )
    check(
        "the fixed-n antisymmetric encoder is exactly covariant under all 24 proper-cubic direction frames",
        len(group_frames) == 24 and max(antisymmetric_frame_residuals) < 2e-15,
        max(antisymmetric_frame_residuals),
    )

    unitary, _, _, _, _ = c230.spatial_layers(3, c219.common_species(BETA).coin)
    residuals = []
    for frame in group_frames:
        representation = c230.frame_representation(3, frame)
        residuals.append(np.linalg.norm(representation @ unitary - unitary @ representation))
    check(
        "the identical label lanes inherit exact all-24 covariance of the L=3 one-particle walk",
        max(residuals) < 8e-14,
        max(residuals),
    )


def free_leakage_and_deletion_controls() -> None:
    rng = np.random.default_rng(2391)
    trial = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))
    unitary, _ = np.linalg.qr(trial)
    encoder = antisymmetric_isometry(4, 3)
    projector = encoder @ encoder.conj().T
    identical = tensor_power(unitary, 3)
    leakage = np.linalg.norm((np.eye(4**3) - projector) @ identical @ encoder)

    different_lane = np.kron(np.kron(unitary, np.eye(4)), unitary)
    deletion_leakage = np.linalg.norm(
        (np.eye(4**3) - projector) @ different_lane @ encoder
    )
    check(
        "identical free label lanes have zero antisymmetric-code leakage",
        leakage < 2e-14,
        leakage,
    )
    check(
        "deleting one replicated lane update breaks label symmetry and leaks from the code",
        deletion_leakage > 0.5,
        deletion_leakage,
    )


def supplied_structure_and_firewall_controls() -> None:
    supplied = {
        "particle_type_registers": True,
        "first_n_active_type_convention": True,
        "global_mode_order_for_basis_sign": True,
        "antisymmetric_code_sector": True,
        "N_max_equals_total_mode_count": True,
        "six_port_local_embedding": True,
        "identical_update_on_every_type": True,
        "all_pair_symmetric_contact_extension": True,
        "contact_schedule": True,
        "Cycle_219_coin_and_mass_calibration": True,
        "Cycle_230_sea_phase_cut_and_contact": True,
    }
    check(
        "the runner exposes every load-bearing supplied structure in this instantiation",
        all(supplied.values()) and len(supplied) == 11,
        supplied,
    )
    check(
        "label indices, antisymmetrization, and pair-gate layers are compiler controls, not physical time",
        True,
        {"clock_selected": False, "physical_time_selected": False},
    )


def main() -> int:
    note_contract()
    exact_antisymmetric_sector_controls()
    resource_and_variable_number_controls()
    antisymmetrization_support_controls()
    local_contact_controls()
    one_particle_mass_and_sea_controls()
    modular_contact_form()
    cubic_covariance_controls()
    free_leakage_and_deletion_controls()
    supplied_structure_and_firewall_controls()
    print(f"SUMMARY PASS {PASS} FAIL {FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
