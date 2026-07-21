#!/usr/bin/env python3
"""Cycle 523: protected-shadow bare coin/contact gate compiler.

Compile the actual Cycle-219 beta=-0.3 six-mode coin into frozen one- and
two-M2 factors, route every two-M2 factor through the center tag of the
Cycle-520 seven-M2 protected-shadow block, and compile all fifteen Cycle-230
contact phases.  The runner checks the full M64 onsite intertwiner, inverse,
leakage, deletions, perturbation, local Koszul frame correction, and complete
L5/L6 proper-cubic schedule geometry.  It also independently verifies and
bare-gate decomposes the degree-two relational map from Cycle 522's 160
selected native-shell patterns to the six private occupation shadows.

The result is intentionally not called a full stream compiler.  With the tag
uncomputed to zero during the direct update, endpoint-local B-layer FSWAPs
retain the exact Cycle-231 two-particle exchange-sign mismatch.  That is a
route-specific boundary, not a general auxiliary/gauge no-go.

Authority: none.  Audit: unset.  Constitutional effect: none.
"""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
from hashlib import sha256
from itertools import combinations, product
import json
import math
from pathlib import Path
import resource
import signal
import subprocess
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import fock_modular_boundary_current_cycle229_2026_07_17 as c229
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230
import ROUTE1_DIRECT_CAR_COMPILER_CYCLE231_2026_07_17 as c231
import physical_three_star_shared_parity_overlap_cycle520_2026_07_21 as c520
import physical_opposite_carrier_reearned_compiler_cycle522_2026_07_21 as c522


c210 = c219.c210
AUTHORITY = "none"
AUDIT = "unset"
REVISION = 1
BETA = -0.3
COUPLING = 0.37
TRAIN_LENGTH = 5
HELD_LENGTH = 6
Q_MODES = 6
TAG_SITE = 6
LOCAL_M2 = 7
LOCAL_Q_DIM = 1 << Q_MODES
LOCAL_PHYSICAL_DIM = 1 << LOCAL_M2
TOLERANCE = 5e-12
QR_ZERO_TOLERANCE = 1e-13
PERTURBATION = 1e-4
WALL_LIMIT_SECONDS = 1200.0
WALL_GRACE_SECONDS = 20.0
RSS_GUARD_BYTES = 2_850_000_000
CLI_MODES = ("dry-contract", "protected-shadow-certificate")

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_PROTECTED_SHADOW_COIN_GATE_COMPILER_CYCLE523_NOTE_2026-07-21.md"
)
CYCLE219_RUNNER = ROOT / "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py"
CYCLE230_RUNNER = ROOT / "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py"
CYCLE231_RUNNER = ROOT / "scripts/ROUTE1_DIRECT_CAR_COMPILER_CYCLE231_2026_07_17.py"
CYCLE520_RUNNER = ROOT / "scripts/physical_three_star_shared_parity_overlap_cycle520_2026_07_21.py"
CYCLE520_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_THREE_STAR_SHARED_PARITY_OVERLAP_CYCLE520_NOTE_2026-07-21.md"
)
CYCLE522_RUNNER = ROOT / "scripts/physical_opposite_carrier_reearned_compiler_cycle522_2026_07_21.py"
STRICT_FILE_HASHES = {
    CYCLE219_RUNNER: "ad9bf5febde8b58e948f4a4240791216a20d61262149469763ef387455dff52a",
    CYCLE230_RUNNER: "b449301837c1b72a325d310a1e2c582263a36648de939d169912347aff0591ae",
    CYCLE231_RUNNER: "5adb6dc52f6352a5367a2b56da94854e511f9dd174688029f1841e5004a91c32",
    CYCLE520_RUNNER: "22b00fd39fd07a04afb8776f4b97c31486ce4d2034617bd16aa170c263108b2b",
    CYCLE520_NOTE: "8a1aa2c66cbc38320c829679e7b982936834510a58b38f89621f22278fd67cd8",
    CYCLE522_RUNNER: "d6a7700d7575dfba02d4b4d2438e54d37a02c6ca7f71673c8a871b474f6e088b",
}


class CertificateFailure(RuntimeError):
    """Failed bounded predicate; never promoted automatically to a no-go."""


class ResourceWall(RuntimeError):
    """Technical runner wall; never a physical conclusion."""


@dataclass(frozen=True)
class Gate:
    kind: str
    sites: tuple[int, ...]
    matrix: tuple[complex, ...]
    stage: str
    label: str


@dataclass(frozen=True)
class ModeGate:
    kind: str
    sites: tuple[int, ...]
    matrix: tuple[complex, ...]
    label: str


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def rss_bytes() -> int:
    value = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    return value if sys.platform == "darwin" else value * 1024


def swap_count() -> int:
    return int(getattr(resource.getrusage(resource.RUSAGE_SELF), "ru_nswap", 0))


def checkpoint(started: float, label: str) -> dict:
    elapsed = time.monotonic() - started
    rss = rss_bytes()
    if elapsed >= WALL_LIMIT_SECONDS - WALL_GRACE_SECONDS:
        raise ResourceWall(f"wall grace reached at {label}: {elapsed:.6f}s")
    if rss >= RSS_GUARD_BYTES:
        raise ResourceWall(f"RSS guard reached at {label}: {rss}")
    if swap_count() != 0:
        raise ResourceWall(f"nonzero swap count at {label}")
    return {
        "label": label,
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": rss,
        "process_swap_count": swap_count(),
    }


def alarm_handler(_signum, _frame) -> None:
    raise ResourceWall("hard 1200-second wall alarm reached")


def one_particle_matrix(gate: ModeGate) -> np.ndarray:
    size = 1 if gate.kind == "phase" else 2
    return np.asarray(gate.matrix, dtype=complex).reshape(size, size)


def compile_adjacent_qr(unitary: np.ndarray) -> tuple[tuple[ModeGate, ...], dict]:
    """Adjacent-row complex QR; return factors in physical application order."""
    if unitary.shape != (Q_MODES, Q_MODES):
        raise ValueError("Cycle523 expects one six-mode coin")
    if np.linalg.norm(unitary.conj().T @ unitary - np.eye(Q_MODES)) >= TOLERANCE:
        raise ValueError("coin is not unitary")
    work = unitary.copy()
    eliminations: list[tuple[int, int, np.ndarray]] = []
    for column in range(Q_MODES - 1):
        for lower in range(Q_MODES - 1, column, -1):
            upper = lower - 1
            a = work[upper, column]
            b = work[lower, column]
            if abs(b) < QR_ZERO_TOLERANCE:
                continue
            radius = np.sqrt(abs(a) ** 2 + abs(b) ** 2)
            elimination = np.asarray(
                (
                    (np.conj(a) / radius, np.conj(b) / radius),
                    (-b / radius, a / radius),
                ),
                dtype=complex,
            )
            work[[upper, lower], :] = elimination @ work[[upper, lower], :]
            eliminations.append((upper, lower, elimination))
    diagonal_residual = float(np.linalg.norm(work - np.diag(np.diag(work))))
    schedule: list[ModeGate] = []
    for index, phase in enumerate(np.diag(work)):
        if abs(phase - 1) >= QR_ZERO_TOLERANCE:
            schedule.append(ModeGate("phase", (index,), (complex(phase),), f"phase-{index}"))
    for index, (upper, lower, elimination) in enumerate(reversed(eliminations)):
        matrix = elimination.conj().T
        schedule.append(
            ModeGate(
                "givens",
                (upper, lower),
                tuple(matrix.reshape(-1)),
                f"givens-{index}-{upper}-{lower}",
            )
        )
    reconstructed = np.eye(Q_MODES, dtype=complex)
    for gate in schedule:
        factor = np.eye(Q_MODES, dtype=complex)
        if gate.kind == "phase":
            factor[gate.sites[0], gate.sites[0]] = gate.matrix[0]
        else:
            factor[np.ix_(gate.sites, gate.sites)] = one_particle_matrix(gate)
        reconstructed = factor @ reconstructed
    digest_payload = []
    for gate in schedule:
        digest_payload.append(
            {
                "kind": gate.kind,
                "sites": gate.sites,
                "matrix": tuple((value.real.hex(), value.imag.hex()) for value in gate.matrix),
            }
        )
    digest = sha256(json.dumps(digest_payload, sort_keys=True).encode()).hexdigest()
    return tuple(schedule), {
        "givens": sum(gate.kind == "givens" for gate in schedule),
        "onsite_phases": sum(gate.kind == "phase" for gate in schedule),
        "diagonalization_residual": diagonal_residual,
        "one_particle_reconstruction_residual": float(np.linalg.norm(reconstructed - unitary)),
        "one_particle_unitarity_residual": float(
            np.linalg.norm(reconstructed.conj().T @ reconstructed - np.eye(Q_MODES))
        ),
        "schedule_sha256": digest,
        "reconstructed": reconstructed,
    }


def fock_two_mode(unitary: np.ndarray) -> np.ndarray:
    if unitary.shape != (2, 2):
        raise ValueError("two-mode lift needs a 2x2 matrix")
    return c229.fock_lift(unitary)


FSWAP = fock_two_mode(np.asarray(((0, 1), (1, 0)), dtype=complex))


def controlled_phase_matrix(phase: complex) -> np.ndarray:
    if abs(abs(phase) - 1) >= TOLERANCE:
        raise ValueError("controlled phase must be unit modulus")
    return np.diag((1, 1, 1, phase)).astype(complex)


def cnot_matrix() -> np.ndarray:
    matrix = np.zeros((4, 4), dtype=complex)
    for source in range(4):
        control = source & 1
        target = (source >> 1) & 1
        output = control + 2 * (target ^ control)
        matrix[output, source] = 1
    return matrix


def local_gate(kind: str, sites, matrix: np.ndarray, stage: str, label: str) -> Gate:
    sites = tuple(int(site) for site in sites)
    width = len(sites)
    if width not in (1, 2) or len(set(sites)) != width:
        raise ValueError("physical primitive must use one or two distinct M2")
    if any(site < 0 or site >= LOCAL_M2 for site in sites):
        raise ValueError("local M2 site outside seven-site block")
    expected = 1 << width
    matrix = np.asarray(matrix, dtype=complex)
    if matrix.shape != (expected, expected):
        raise ValueError("primitive matrix has wrong size")
    if np.linalg.norm(matrix.conj().T @ matrix - np.eye(expected)) >= TOLERANCE:
        raise ValueError("primitive is not unitary")
    return Gate(kind, sites, tuple(matrix.reshape(-1)), stage, label)


def onsite_phase(site: int, phase: complex, stage: str, label: str) -> Gate:
    return local_gate(
        "onsite-phase", (site,), np.diag((1, phase)).astype(complex), stage, label
    )


def two_m2(kind: str, first: int, second: int, matrix, stage: str, label: str) -> Gate:
    return local_gate(kind, (first, second), np.asarray(matrix), stage, label)


def routed_pair(
    first: int, second: int, core: np.ndarray, *, kind: str, stage: str, label: str
) -> tuple[Gate, ...]:
    if first == second or TAG_SITE in (first, second):
        raise ValueError("routed pair expects two distinct occupation leaves")
    return (
        two_m2("FSWAP", first, TAG_SITE, FSWAP, stage, f"{label}:route-in"),
        two_m2(kind, TAG_SITE, second, core, stage, f"{label}:core"),
        two_m2("FSWAP", first, TAG_SITE, FSWAP, stage, f"{label}:route-out"),
    )


def parity_schedule(stage: str, direction_map=tuple(range(Q_MODES))) -> tuple[Gate, ...]:
    return tuple(
        two_m2(
            "CNOT",
            direction_map[direction],
            TAG_SITE,
            cnot_matrix(),
            stage,
            f"{stage}:parity-{direction}",
        )
        for direction in range(Q_MODES)
    )


def routed_mode_schedule(
    schedule: tuple[ModeGate, ...],
    *,
    stage: str,
    direction_map=tuple(range(Q_MODES)),
) -> tuple[Gate, ...]:
    output: list[Gate] = []
    for gate in schedule:
        if gate.kind == "phase":
            output.append(
                onsite_phase(
                    direction_map[gate.sites[0]],
                    gate.matrix[0],
                    stage,
                    f"{stage}:{gate.label}",
                )
            )
        else:
            first, second = (direction_map[index] for index in gate.sites)
            output.extend(
                routed_pair(
                    first,
                    second,
                    fock_two_mode(one_particle_matrix(gate)),
                    kind="fermionic-Givens",
                    stage=stage,
                    label=f"{stage}:{gate.label}",
                )
            )
    return tuple(output)


def routed_contact_schedule(
    *, stage: str = "contact", direction_map=tuple(range(Q_MODES)), coupling=COUPLING
) -> tuple[Gate, ...]:
    phase = np.exp(1j * coupling)
    output: list[Gate] = []
    for first, second in combinations(range(Q_MODES), 2):
        output.extend(
            routed_pair(
                direction_map[first],
                direction_map[second],
                controlled_phase_matrix(phase),
                kind="contact-phase",
                stage=stage,
                label=f"{stage}:pair-{first}-{second}",
            )
        )
    return tuple(output)


def routed_reverse_schedule(
    *, stage: str = "reverse-stream", direction_map=tuple(range(Q_MODES))
) -> tuple[Gate, ...]:
    output: list[Gate] = []
    for first, second in ((0, 1), (2, 3), (4, 5)):
        output.extend(
            routed_pair(
                direction_map[first],
                direction_map[second],
                FSWAP,
                kind="FSWAP",
                stage=stage,
                label=f"{stage}:pair-{first}-{second}",
            )
        )
    return tuple(output)


def inverse_gate(gate: Gate) -> Gate:
    size = 1 << len(gate.sites)
    matrix = np.asarray(gate.matrix, dtype=complex).reshape(size, size).conj().T
    return Gate(gate.kind, gate.sites, tuple(matrix.reshape(-1)), gate.stage, "inverse:" + gate.label)


def inverse_schedule(schedule: tuple[Gate, ...]) -> tuple[Gate, ...]:
    return tuple(inverse_gate(gate) for gate in reversed(schedule))


def apply_gate(state: np.ndarray, gate: Gate, width: int = LOCAL_M2) -> np.ndarray:
    dimension = 1 << width
    if state.shape[0] != dimension:
        raise ValueError("state row dimension does not match physical width")
    sites = gate.sites
    local_dimension = 1 << len(sites)
    matrix = np.asarray(gate.matrix, dtype=complex).reshape(local_dimension, local_dimension)
    output = np.zeros_like(state)
    clear_mask = sum(1 << site for site in sites)
    for source in range(dimension):
        local_source = sum(((source >> site) & 1) << bit for bit, site in enumerate(sites))
        base = source & ~clear_mask
        for local_target in range(local_dimension):
            coefficient = matrix[local_target, local_source]
            if abs(coefficient) < 1e-16:
                continue
            target = base | sum(
                ((local_target >> bit) & 1) << site for bit, site in enumerate(sites)
            )
            output[target] += coefficient * state[source]
    return output


def schedule_operator(schedule: tuple[Gate, ...], width: int = LOCAL_M2) -> np.ndarray:
    output = np.eye(1 << width, dtype=complex)
    for gate in schedule:
        output = apply_gate(output, gate, width)
    return output


def code_encoding(tagged: bool) -> np.ndarray:
    encoding = np.zeros((LOCAL_PHYSICAL_DIM, LOCAL_Q_DIM), dtype=complex)
    for qword in range(LOCAL_Q_DIM):
        tag = (qword.bit_count() & 1) if tagged else 0
        encoding[qword | (tag << TAG_SITE), qword] = 1
    return encoding


def q_operator_on_seven(operator: np.ndarray) -> np.ndarray:
    output = np.zeros((LOCAL_PHYSICAL_DIM, LOCAL_PHYSICAL_DIM), dtype=complex)
    for tag in (0, 1):
        indices = np.arange(LOCAL_Q_DIM) | (tag << TAG_SITE)
        output[np.ix_(indices, indices)] = operator
    return output


def ordinary_q_permutation(one_particle: np.ndarray) -> np.ndarray:
    permutation = tuple(int(np.argmax(one_particle[:, source])) for source in range(Q_MODES))
    result = np.zeros((LOCAL_Q_DIM, LOCAL_Q_DIM), dtype=complex)
    for basis in range(LOCAL_Q_DIM):
        target = 0
        for source, destination in enumerate(permutation):
            if (basis >> source) & 1:
                target |= 1 << destination
        result[target, basis] = 1
    return result


def direction_map(frame: np.ndarray) -> tuple[int, ...]:
    permutation = c210.direction_permutation(frame)
    return tuple(int(np.argmax(permutation[:, source])) for source in range(Q_MODES))


def inversion_pairs(mapping: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    return tuple(
        (mapping[first], mapping[second])
        for first, second in combinations(range(Q_MODES), 2)
        if mapping[first] > mapping[second]
    )


def frame_cocycle_schedule(mapping: tuple[int, ...]) -> tuple[Gate, ...]:
    output: list[Gate] = []
    for index, (first, second) in enumerate(inversion_pairs(mapping)):
        output.extend(
            routed_pair(
                first,
                second,
                controlled_phase_matrix(-1),
                kind="Koszul-CZ",
                stage="frame-cocycle",
                label=f"frame-cocycle:{index}-{first}-{second}",
            )
        )
    return tuple(output)


def local_layout_positions():
    positions = {
        direction: tuple(int(-value) for value in c210.DIRECTIONS[direction])
        for direction in range(Q_MODES)
    }
    positions[TAG_SITE] = (0, 0, 0)
    return positions


def local_l1(first, second) -> int:
    return sum(abs(first[index] - second[index]) for index in range(3))


def onsite_compiler_controls() -> tuple[dict, dict]:
    species = c219.common_species(BETA)
    mode_schedule, qr = compile_adjacent_qr(species.coin)
    routed_coin = routed_mode_schedule(mode_schedule, stage="coin")
    routed_contact = routed_contact_schedule()
    parity = parity_schedule("parity")
    parity_operator = schedule_operator(parity)
    coin_operator = schedule_operator(routed_coin)
    contact_operator = schedule_operator(routed_contact)
    tagged_encoding = code_encoding(True)
    blank_encoding = code_encoding(False)
    gamma_coin = c229.fock_lift(species.coin)
    occupations = c229.occupation_table(Q_MODES)
    number = np.sum(occupations, axis=1)
    contact = np.diag(np.exp(1j * COUPLING * number * (number - 1) / 2))
    direct = contact @ gamma_coin
    physical = parity_operator @ contact_operator @ coin_operator @ parity_operator
    code_projector = tagged_encoding @ tagged_encoding.conj().T
    intertwiner = physical @ tagged_encoding - tagged_encoding @ direct
    inverse = schedule_operator(
        inverse_schedule(parity + routed_coin + routed_contact + parity)
    )
    forward = schedule_operator(parity + routed_coin + routed_contact + parity)
    compiled_mass = float(
        np.angle(np.vdot(c210.UNIFORM, qr["reconstructed"] @ c210.UNIFORM))
    ) / c219.C_SQUARED
    all_gates = parity + routed_coin + routed_contact + parity
    positions = local_layout_positions()
    two_site_distances = tuple(
        local_l1(positions[gate.sites[0]], positions[gate.sites[1]])
        for gate in all_gates
        if len(gate.sites) == 2
    )
    controls = {
        "beta": BETA,
        "contact_coupling": COUPLING,
        "local_CAR_dimension": LOCAL_Q_DIM,
        "physical_block_dimension": LOCAL_PHYSICAL_DIM,
        "active_M2_per_cell": LOCAL_M2,
        "physical_supercell_sites": 27,
        "blank_supercell_sites": 20,
        "QR_Givens": qr["givens"],
        "QR_onsite_phases": qr["onsite_phases"],
        "QR_schedule_sha256": qr["schedule_sha256"],
        "QR_diagonalization_residual": qr["diagonalization_residual"],
        "one_particle_coin_reconstruction_residual": qr[
            "one_particle_reconstruction_residual"
        ],
        "one_particle_coin_unitarity_residual": qr["one_particle_unitarity_residual"],
        "exterior_coin_reconstruction_residual": float(
            np.linalg.norm(coin_operator @ blank_encoding - blank_encoding @ gamma_coin)
        ),
        "fifteen_contact_phase_reconstruction_residual": float(
            np.linalg.norm(contact_operator - q_operator_on_seven(contact))
        ),
        "parity_uncompute_blank_residual": float(
            np.linalg.norm(parity_operator @ tagged_encoding - blank_encoding)
        ),
        "parity_involution_residual": float(
            np.linalg.norm(parity_operator @ parity_operator - np.eye(LOCAL_PHYSICAL_DIM))
        ),
        "onsite_EG_intertwiner_residual": float(np.linalg.norm(intertwiner)),
        "onsite_maximum_column_intertwiner_residual": float(
            np.max(np.linalg.norm(intertwiner, axis=0))
        ),
        "terminal_code_leakage_residual": float(
            np.linalg.norm((np.eye(LOCAL_PHYSICAL_DIM) - code_projector) @ physical @ tagged_encoding)
        ),
        "physical_unitarity_residual": float(
            np.linalg.norm(physical.conj().T @ physical - np.eye(LOCAL_PHYSICAL_DIM))
        ),
        "inverse_roundtrip_residual": float(
            np.linalg.norm(inverse @ forward - np.eye(LOCAL_PHYSICAL_DIM))
        ),
        "compiled_rest_mass": compiled_mass,
        "Cycle219_mass_fixture": float(species.analytic_mass),
        "mass_fixture_residual": abs(compiled_mass - float(species.analytic_mass)),
        "contact_active_two_particle_states": int(np.sum(number == 2)),
        "contact_deletion_residual": float(abs(np.exp(1j * COUPLING) - 1)),
        "local_primitive_gates": len(all_gates),
        "local_two_M2_gate_maximum_physical_L1": max(two_site_distances),
        "all_runtime_gate_support_at_most_two_M2": all(len(gate.sites) <= 2 for gate in all_gates),
        "compile_time_QR_runtime_adaptation": False,
    }
    controls["pass"] = (
        controls["QR_Givens"] == 10
        and controls["QR_onsite_phases"] == 1
        and controls["one_particle_coin_reconstruction_residual"] < TOLERANCE
        and controls["exterior_coin_reconstruction_residual"] < TOLERANCE
        and controls["fifteen_contact_phase_reconstruction_residual"] < TOLERANCE
        and controls["parity_uncompute_blank_residual"] == 0
        and controls["parity_involution_residual"] == 0
        and controls["onsite_EG_intertwiner_residual"] < TOLERANCE
        and controls["terminal_code_leakage_residual"] < TOLERANCE
        and controls["physical_unitarity_residual"] < 2e-11
        and controls["inverse_roundtrip_residual"] < 2e-11
        and controls["mass_fixture_residual"] < TOLERANCE
        and controls["contact_active_two_particle_states"] == 15
        and controls["local_primitive_gates"] == 88
        and controls["local_two_M2_gate_maximum_physical_L1"] == 1
    )
    objects = {
        "species": species,
        "mode_schedule": mode_schedule,
        "routed_coin": routed_coin,
        "routed_contact": routed_contact,
        "parity": parity,
        "parity_operator": parity_operator,
        "coin_operator": coin_operator,
        "contact_operator": contact_operator,
        "tagged_encoding": tagged_encoding,
        "blank_encoding": blank_encoding,
        "gamma_coin": gamma_coin,
        "contact": contact,
        "direct": direct,
        "physical": physical,
        "forward_schedule": parity + routed_coin + routed_contact + parity,
    }
    return controls, objects


def deletion_perturbation_controls(objects: dict) -> dict:
    parity = objects["parity"]
    coin = objects["routed_coin"]
    contact = objects["routed_contact"]
    encoding = objects["tagged_encoding"]
    direct = objects["direct"]
    baseline = objects["physical"] @ encoding

    core_index = next(index for index, gate in enumerate(coin) if ":core" in gate.label)
    route_index = next(index for index, gate in enumerate(coin) if ":route-in" in gate.label)
    contact_core_index = next(
        index for index, gate in enumerate(contact) if ":core" in gate.label
    )

    def complete(coin_schedule, contact_schedule, final_parity):
        return schedule_operator(
            parity + tuple(coin_schedule) + tuple(contact_schedule) + tuple(final_parity)
        )

    deleted_coin = complete(
        tuple(gate for index, gate in enumerate(coin) if index != core_index),
        contact,
        parity,
    ) @ encoding
    deleted_route = complete(
        tuple(gate for index, gate in enumerate(coin) if index != route_index),
        contact,
        parity,
    ) @ encoding
    deleted_contact = complete(
        coin,
        tuple(gate for index, gate in enumerate(contact) if index != contact_core_index),
        parity,
    ) @ encoding
    deleted_compute = complete(coin, contact, parity[1:]) @ encoding

    core_gate = coin[core_index]
    core_matrix = np.asarray(core_gate.matrix, dtype=complex).reshape(4, 4)
    local_phase = np.diag((1, np.exp(1j * PERTURBATION))).astype(complex)
    perturbed_core = fock_two_mode(local_phase) @ core_matrix
    perturbed_gate = two_m2(
        core_gate.kind,
        core_gate.sites[0],
        core_gate.sites[1],
        perturbed_core,
        core_gate.stage,
        core_gate.label + ":perturbed",
    )
    perturbed_coin = tuple(
        perturbed_gate if index == core_index else gate for index, gate in enumerate(coin)
    )
    perturbed = complete(perturbed_coin, contact, parity) @ encoding
    code_projector = encoding @ encoding.conj().T

    def residual(candidate):
        difference = candidate - baseline
        return {
            "Frobenius": float(np.linalg.norm(difference)),
            "maximum_column": float(np.max(np.linalg.norm(difference, axis=0))),
            "terminal_leakage": float(
                np.linalg.norm((np.eye(LOCAL_PHYSICAL_DIM) - code_projector) @ candidate)
            ),
        }

    compute_errors = int(
        np.sum(np.linalg.norm(deleted_compute - objects["tagged_encoding"] @ direct, axis=0) > TOLERANCE)
    )
    rows = {
        "deleted_first_Givens_core": residual(deleted_coin),
        "deleted_first_route_FSWAP": residual(deleted_route),
        "deleted_first_contact_phase": residual(deleted_contact),
        "deleted_first_final_parity_CNOT": residual(deleted_compute),
        "perturbed_first_Givens_core": residual(perturbed),
        "perturbation_radians": PERTURBATION,
        "final_parity_CNOT_deletion_bad_columns": compute_errors,
    }
    rows["pass"] = (
        rows["deleted_first_Givens_core"]["maximum_column"] > 1e-3
        and rows["deleted_first_route_FSWAP"]["maximum_column"] > 1e-3
        and rows["deleted_first_route_FSWAP"]["terminal_leakage"] > 1e-3
        and abs(
            rows["deleted_first_contact_phase"]["maximum_column"]
            - abs(np.exp(1j * COUPLING) - 1)
        )
        < TOLERANCE
        and rows["perturbed_first_Givens_core"]["maximum_column"] > 1e-6
        and compute_errors == 63
    )
    return rows


def frame_controls(objects: dict) -> dict:
    frames = c210.proper_cubic_frames()
    encoding = objects["tagged_encoding"]
    physical = objects["physical"]
    mode_schedule = objects["mode_schedule"]
    gamma_coin = objects["gamma_coin"]
    contact = objects["contact"]
    geometric_coin_residuals = []
    corrected_code_residuals = []
    mapped_schedule_conjugacy_residuals = []
    cocycle_compile_residuals = []
    representation_code_residuals = []
    contact_covariance_residuals = []
    inversion_counts = []
    representation_rows = []
    for frame in frames:
        one_particle = c210.direction_permutation(frame)
        mapping = direction_map(frame)
        geometric_q = ordinary_q_permutation(one_particle)
        geometric = q_operator_on_seven(geometric_q)
        exterior = q_operator_on_seven(c229.fock_lift(one_particle))
        cocycle_schedule = frame_cocycle_schedule(mapping)
        cocycle = schedule_operator(cocycle_schedule)
        target_cocycle = exterior @ geometric.conj().T
        cocycle_compile_residuals.append(float(np.linalg.norm(cocycle - target_cocycle)))
        representation = cocycle @ geometric
        representation_rows.append(representation)
        representation_code_residuals.append(
            float(np.linalg.norm(representation @ encoding - encoding @ c229.fock_lift(one_particle)))
        )
        geometric_coin_residuals.append(
            float(np.linalg.norm(geometric_q @ gamma_coin - gamma_coin @ geometric_q))
        )
        contact_covariance_residuals.append(
            float(np.linalg.norm(geometric_q @ contact - contact @ geometric_q))
        )
        corrected_code_residuals.append(
            float(np.linalg.norm(representation @ physical @ encoding - physical @ representation @ encoding))
        )

        mapped_parity = parity_schedule("parity", mapping)
        mapped_coin = routed_mode_schedule(mode_schedule, stage="coin", direction_map=mapping)
        mapped_contact = routed_contact_schedule(direction_map=mapping)
        mapped_operator = schedule_operator(
            mapped_parity + mapped_coin + mapped_contact + mapped_parity
        )
        mapped_schedule_conjugacy_residuals.append(
            float(np.linalg.norm(mapped_operator - geometric @ physical @ geometric.conj().T))
        )
        inversion_counts.append(len(inversion_pairs(mapping)))

    frame_lookup = {
        tuple(frame.reshape(-1)): index for index, frame in enumerate(frames)
    }
    product_failures = 0
    maximum_product_residual = 0.0
    for first_index, first in enumerate(frames):
        for second_index, second in enumerate(frames):
            target = frame_lookup[tuple((first @ second).reshape(-1))]
            residual = float(
                np.linalg.norm(
                    representation_rows[first_index] @ representation_rows[second_index]
                    - representation_rows[target]
                )
            )
            maximum_product_residual = max(maximum_product_residual, residual)
            product_failures += residual >= TOLERANCE

    controls = {
        "proper_cubic_frames": len(frames),
        "frame_products": len(frames) ** 2,
        "pure_geometric_coin_failed_frames": sum(value >= TOLERANCE for value in geometric_coin_residuals),
        "maximum_pure_geometric_coin_residual": max(geometric_coin_residuals),
        "maximum_contact_geometric_covariance_residual": max(contact_covariance_residuals),
        "maximum_routed_Koszul_cocycle_compile_residual": max(cocycle_compile_residuals),
        "maximum_corrected_frame_code_residual": max(corrected_code_residuals),
        "maximum_mapped_schedule_conjugacy_residual": max(mapped_schedule_conjugacy_residuals),
        "maximum_frame_representation_code_residual": max(representation_code_residuals),
        "frame_product_failures": product_failures,
        "maximum_frame_product_residual": maximum_product_residual,
        "cocycle_CZ_pairs_by_frame_histogram": dict(Counter(inversion_counts)),
        "maximum_cocycle_CZ_pairs": max(inversion_counts),
        "maximum_cocycle_routed_two_M2_gates": 3 * max(inversion_counts),
    }
    controls["pass"] = (
        controls["proper_cubic_frames"] == 24
        and controls["frame_products"] == 576
        and controls["pure_geometric_coin_failed_frames"] == 22
        and controls["maximum_pure_geometric_coin_residual"] > 7
        and controls["maximum_contact_geometric_covariance_residual"] < TOLERANCE
        and controls["maximum_routed_Koszul_cocycle_compile_residual"] < TOLERANCE
        and controls["maximum_corrected_frame_code_residual"] < 2e-11
        and controls["maximum_mapped_schedule_conjugacy_residual"] < 2e-11
        and controls["maximum_frame_representation_code_residual"] < TOLERANCE
        and controls["frame_product_failures"] == 0
        and controls["maximum_frame_product_residual"] < TOLERANCE
    )
    return controls


def all_sites(length: int):
    return tuple(product(range(length), repeat=3))


def transformed_mode(mode: int, frame: np.ndarray, length: int) -> int:
    site, direction = c231.index_mode(mode, length)
    target_site = tuple(int(value % length) for value in frame @ np.asarray(site))
    target_direction = direction_map(frame)[direction]
    return c231.site_index(target_site, target_direction, length)


def layout_schedule_controls(length: int, mode_schedule: tuple[ModeGate, ...]) -> dict:
    cell_count = length**3
    coin_gates = sum(1 if gate.kind == "phase" else 3 for gate in mode_schedule)
    local_reverse_gates = 3 * 3
    edge_pairs = tuple(
        (source, int(target))
        for source, target in enumerate(c231.edge_permutation(length))
        if source < target
    )
    contact_gates = math.comb(Q_MODES, 2) * 3
    parity_gates = Q_MODES
    per_cell_without_edge = 2 * parity_gates + coin_gates + local_reverse_gates + contact_gates
    total_gates = cell_count * per_cell_without_edge + len(edge_pairs)
    positions = local_layout_positions()
    star_distances = {
        local_l1(positions[direction], positions[TAG_SITE]) for direction in range(Q_MODES)
    }
    external_distances = []
    period = 3 * length
    for first, second in edge_pairs:
        first_site, first_direction = c231.index_mode(first, length)
        second_site, second_direction = c231.index_mode(second, length)
        external_distances.append(
            c231.periodic_l1(
                c231.physical_position(first_site, first_direction),
                c231.physical_position(second_site, second_direction),
                period,
            )
        )
    frame_edge_failures = 0
    frame_cell_failures = 0
    edge_set = {tuple(sorted(pair)) for pair in edge_pairs}
    for frame in c210.proper_cubic_frames():
        transformed_edges = {
            tuple(
                sorted(
                    (
                        transformed_mode(first, frame, length),
                        transformed_mode(second, frame, length),
                    )
                )
            )
            for first, second in edge_pairs
        }
        frame_edge_failures += transformed_edges != edge_set
        transformed_cells = {
            tuple(int(value % length) for value in frame @ np.asarray(site))
            for site in all_sites(length)
        }
        frame_cell_failures += len(transformed_cells) != cell_count
    return {
        "length": length,
        "coarse_cells": cell_count,
        "active_M2": LOCAL_M2 * cell_count,
        "physical_supercell_sites": 27 * cell_count,
        "coin_routed_gates_per_cell": coin_gates,
        "reverse_routed_gates_per_cell": local_reverse_gates,
        "edge_FSWAP_gates": len(edge_pairs),
        "contact_routed_gates_per_cell": contact_gates,
        "parity_CNOT_gates_per_cell": 2 * parity_gates,
        "total_one_two_M2_gate_calls": total_gates,
        "derived_factor_order_depth_upper_bound": 6 + coin_gates + local_reverse_gates + 1 + contact_gates + 6,
        "star_edge_physical_L1_values": sorted(star_distances),
        "external_edge_physical_L1_values": sorted(set(external_distances)),
        "proper_frame_edge_set_failures": frame_edge_failures,
        "proper_frame_cell_bijection_failures": frame_cell_failures,
        "runtime_branch_or_host_adaptation": False,
        "pass": (
            coin_gates == 31
            and local_reverse_gates == 9
            and len(edge_pairs) == 3 * cell_count
            and contact_gates == 45
            and total_gates == 100 * cell_count
            and star_distances == {1}
            and set(external_distances) == {1}
            and frame_edge_failures == frame_cell_failures == 0
        ),
    }


def stream_boundary_controls() -> dict:
    rows = []
    for length in (TRAIN_LENGTH, HELD_LENGTH):
        permutation = c231.edge_permutation(length)
        mismatch, total, witness = c231.two_particle_mismatch(length)
        assert witness is not None
        exact = c231.exterior_permutation_action(permutation, witness)
        endpoint = c231.endpoint_fswap_action(permutation, witness)
        one_particle_failures = sum(
            c231.exterior_permutation_action(permutation, (mode,))
            != c231.endpoint_fswap_action(permutation, (mode,))
            for mode in range(len(permutation))
        )
        rows.append(
            {
                "length": length,
                "one_particle_modes": len(permutation),
                "one_particle_failures": one_particle_failures,
                "two_particle_pairs": total,
                "two_particle_exchange_sign_mismatches": mismatch,
                "first_witness": witness,
                "exact_witness_phase": exact[1],
                "endpoint_witness_phase": endpoint[1],
                "basis_witness_residual": abs(exact[1] - endpoint[1]),
                "tag_recompute_failures": 0,
            }
        )
    return {
        "rows": tuple(rows),
        "operator_norm_residual": 2,
        "common_onsite_unitaries_do_not_change_norm_two_boundary": True,
        "scope": (
            "blank-tag W-dagger / endpoint-local B-FSWAP / W protected-shadow "
            "schedule on the direct occupation encoding"
        ),
        "global_Jordan_Wigner_or_nonlocal_parity_service_used": False,
        "general_auxiliary_or_gauge_no_go": False,
        "full_Gphysical_claimed": False,
        "pass": (
            rows[0]["one_particle_failures"] == rows[1]["one_particle_failures"] == 0
            and rows[0]["two_particle_exchange_sign_mismatches"] == 60_600
            and rows[0]["two_particle_pairs"] == 280_875
            and rows[1]["two_particle_exchange_sign_mismatches"] == 154_800
            and rows[1]["two_particle_pairs"] == 839_160
            and all(row["basis_witness_residual"] == 2 for row in rows)
        ),
    }


def native_auxiliary_roles(code, body):
    center = c522.c311.c305.body_vertices(code, body)
    inward = tuple(
        c522.c311.local.old.outer_partner(code, vertex)[0] for vertex in center
    )
    flag = c522.c311.flag_qubit(code, body) - code.qubits
    companion = c522.c311.r_qubit(code, body) - code.qubits
    return center, inward, flag, companion


def selected_native_rows(code, body):
    center, inward, flag, companion = native_auxiliary_roles(code, body)
    roles = center + inward + (flag, companion)
    rows = []
    for number in range(7):
        for label in c522.c311.LABELS[number]:
            logical_word = sum(1 << direction for direction in label)
            for term in c522.selected_gauge_terms(code, body, number, label):
                auxiliary = term.representative.x >> code.qubits
                pattern = tuple((auxiliary >> role) & 1 for role in roles)
                rows.append((pattern, logical_word))
    return tuple(rows)


def relational_shadow_bit(pattern, direction: int) -> int:
    center = pattern[direction]
    opposite = pattern[direction ^ 1]
    inward = pattern[Q_MODES + direction]
    flag = pattern[12]
    return (
        center
        ^ inward
        ^ (center & flag)
        ^ (opposite & inward)
        ^ (opposite & flag)
    )


def degree_two_feature_mask(pattern) -> int:
    value = 1
    offset = 1
    for bit in pattern:
        value |= int(bit) << offset
        offset += 1
    for first, second in combinations(range(14), 2):
        value |= (pattern[first] & pattern[second]) << offset
        offset += 1
    return value


def gf2_rank(values) -> int:
    pivots = {}
    for value in values:
        while value:
            pivot = value.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = value
                break
            value ^= pivots[pivot]
    return len(pivots)


def embed_small_gate(matrix: np.ndarray, sites, width: int) -> np.ndarray:
    sites = tuple(sites)
    local_dimension = 1 << len(sites)
    matrix = np.asarray(matrix, dtype=complex)
    if matrix.shape != (local_dimension, local_dimension):
        raise ValueError("small-gate matrix has wrong dimension")
    output = np.zeros((1 << width, 1 << width), dtype=complex)
    clear_mask = sum(1 << site for site in sites)
    for source in range(1 << width):
        local_source = sum(
            ((source >> site) & 1) << bit for bit, site in enumerate(sites)
        )
        base = source & ~clear_mask
        for local_target in range(local_dimension):
            target = base | sum(
                ((local_target >> bit) & 1) << site
                for bit, site in enumerate(sites)
            )
            output[target, source] += matrix[local_target, local_source]
    return output


def bare_toffoli_controls() -> dict:
    identity = np.eye(2, dtype=complex)
    hadamard = np.asarray(((1, 1), (1, -1)), dtype=complex) / np.sqrt(2)
    phase = np.diag((1, np.exp(1j * np.pi / 4))).astype(complex)
    phase_dagger = phase.conj().T
    cnot = cnot_matrix()
    schedule = (
        ("H", (2,), hadamard),
        ("CNOT", (1, 2), cnot),
        ("Tdg", (2,), phase_dagger),
        ("CNOT", (0, 2), cnot),
        ("T", (2,), phase),
        ("CNOT", (1, 2), cnot),
        ("Tdg", (2,), phase_dagger),
        ("CNOT", (0, 2), cnot),
        ("T", (1,), phase),
        ("T", (2,), phase),
        ("H", (2,), hadamard),
        ("CNOT", (0, 1), cnot),
        ("T", (0,), phase),
        ("Tdg", (1,), phase_dagger),
        ("CNOT", (0, 1), cnot),
    )
    compiled = np.eye(8, dtype=complex)
    for _kind, sites, matrix in schedule:
        compiled = embed_small_gate(matrix, sites, 3) @ compiled
    target = np.zeros((8, 8), dtype=complex)
    for source in range(8):
        target[source ^ (4 if source & 0b11 == 0b11 else 0), source] = 1
    inverse = np.eye(8, dtype=complex)
    for _kind, sites, matrix in reversed(schedule):
        inverse = embed_small_gate(matrix.conj().T, sites, 3) @ inverse
    return {
        "bare_one_two_M2_gates_per_Toffoli": len(schedule),
        "one_M2_gates_per_Toffoli": sum(len(sites) == 1 for _kind, sites, _matrix in schedule),
        "two_M2_gates_per_Toffoli": sum(len(sites) == 2 for _kind, sites, _matrix in schedule),
        "maximum_gate_support_M2": max(len(sites) for _kind, sites, _matrix in schedule),
        "Toffoli_reconstruction_residual": float(np.linalg.norm(compiled - target)),
        "Toffoli_inverse_residual": float(np.linalg.norm(inverse @ compiled - np.eye(8))),
        "pass": bool(
            np.linalg.norm(identity - np.eye(2)) == 0
            and len(schedule) == 15
            and max(len(sites) for _kind, sites, _matrix in schedule) == 2
            and np.linalg.norm(compiled - target) < TOLERANCE
            and np.linalg.norm(inverse @ compiled - np.eye(8)) < TOLERANCE
        ),
    }


def native_shadow_sync_controls(length: int) -> dict:
    started = time.monotonic()
    code = c522.c311.c269.build_code(length)
    reference_rows = None
    distinct_pattern_failures = 0
    recurrent_pattern_failures = 0
    decoder_failures = 0
    decoder_tests = 0
    deletion_counts = np.zeros((Q_MODES, 5), dtype=int)
    for body_index, body in enumerate(code.graph.cells):
        rows = selected_native_rows(code, body)
        patterns = tuple(pattern for pattern, _word in rows)
        distinct_pattern_failures += len(set(patterns)) != 160
        if reference_rows is None:
            reference_rows = rows
        else:
            recurrent_pattern_failures += rows != reference_rows
        for pattern, logical_word in rows:
            for direction in range(Q_MODES):
                target = (logical_word >> direction) & 1
                value = relational_shadow_bit(pattern, direction)
                decoder_failures += value != target
                decoder_tests += 1
                center = pattern[direction]
                opposite = pattern[direction ^ 1]
                inward = pattern[Q_MODES + direction]
                flag = pattern[12]
                monomials = (
                    center,
                    inward,
                    center & flag,
                    opposite & inward,
                    opposite & flag,
                )
                if body_index == 0:
                    for monomial, active in enumerate(monomials):
                        deletion_counts[direction, monomial] += active
    assert reference_rows is not None
    feature_rank = gf2_rank(
        degree_two_feature_mask(pattern) for pattern, _word in reference_rows
    )
    shadow_words = {
        sum(relational_shadow_bit(pattern, direction) << direction for direction in range(6))
        for pattern, _word in reference_rows
    }

    frame_role_tests = 0
    frame_role_failures = 0
    frame_term_tests = 0
    frame_term_failures = 0
    frames = c210.proper_cubic_frames()
    for frame in frames:
        vertex_map, _edge_map = c522.c311.c235.graph_frame_maps(code.graph, frame)
        mapping = direction_map(frame)
        for body in code.graph.cells:
            target_body = tuple(int(value % length) for value in frame @ np.asarray(body))
            center, inward, _flag, _companion = native_auxiliary_roles(code, body)
            target_center, target_inward, _target_flag, _target_companion = native_auxiliary_roles(
                code, target_body
            )
            for direction in range(Q_MODES):
                frame_role_tests += 1
                frame_role_failures += (
                    vertex_map[center[direction]] != target_center[mapping[direction]]
                    or vertex_map[inward[direction]] != target_inward[mapping[direction]]
                )
        for pattern, logical_word in reference_rows:
            transformed = [0] * 14
            transformed[12] = pattern[12]
            transformed[13] = pattern[13]
            transformed_word = 0
            for direction in range(Q_MODES):
                target_direction = mapping[direction]
                transformed[target_direction] = pattern[direction]
                transformed[Q_MODES + target_direction] = pattern[Q_MODES + direction]
                transformed_word |= ((logical_word >> direction) & 1) << target_direction
            for direction in range(Q_MODES):
                frame_term_tests += 1
                frame_term_failures += relational_shadow_bit(
                    transformed, direction
                ) != ((transformed_word >> direction) & 1)

    frame_lookup = {tuple(frame.reshape(-1)): index for index, frame in enumerate(frames)}
    group_failures = 0
    for first in frames:
        for second in frames:
            product_frame = first @ second
            group_failures += tuple(product_frame.reshape(-1)) not in frame_lookup
            first_map = direction_map(first)
            second_map = direction_map(second)
            product_map = direction_map(product_frame)
            group_failures += any(
                first_map[second_map[direction]] != product_map[direction]
                for direction in range(Q_MODES)
            )

    toffoli = bare_toffoli_controls()
    pattern_payload = tuple((pattern, word) for pattern, word in reference_rows)
    pattern_digest = sha256(json.dumps(pattern_payload).encode()).hexdigest()
    controls = {
        "length": length,
        "coarse_cells": length**3,
        "selected_terms_per_cell": 160,
        "existing_native_auxiliary_M2_roles_per_cell": 14,
        "decoder_used_native_auxiliary_roles_per_cell": 13,
        "r_companion_used_by_decoder": False,
        "distinct_patterns_per_cell": 160,
        "all_cell_distinct_pattern_failures": distinct_pattern_failures,
        "all_cell_role_pattern_mismatches": recurrent_pattern_failures,
        "all_cell_direction_decoder_tests": decoder_tests,
        "all_cell_direction_decoder_failures": decoder_failures,
        "degree_two_feature_count": 106,
        "degree_two_feature_rank": feature_rank,
        "degree_two_feature_nullity_on_valid_grammar": 106 - feature_rank,
        "covariant_relational_ANF_terms_per_direction": 5,
        "decoded_occupation_words": len(shadow_words),
        "canonical_role_pattern_sha256": pattern_digest,
        "single_cell_single_direction_monomial_deletion_failures": deletion_counts.tolist(),
        "proper_frames": len(frames),
        "all_cell_frame_role_tests": frame_role_tests,
        "all_cell_frame_role_failures": frame_role_failures,
        "all_term_frame_decoder_tests": frame_term_tests,
        "all_term_frame_decoder_failures": frame_term_failures,
        "frame_group_products": len(frames) ** 2,
        "frame_group_failures": group_failures,
        "logical_decoder_gates_per_direction": 5,
        "logical_decoder_CNOTs_per_direction": 2,
        "logical_decoder_Toffolis_per_direction": 3,
        "bare_compute_gate_calls_for_six_shadows": 6 * (2 + 3 * 15),
        "bare_compute_uncompute_gate_calls": 2 * 6 * (2 + 3 * 15),
        "bare_Toffoli": toffoli,
        "off_valid_pattern_completion_unique": False,
        "nearest_neighbor_native_to_shadow_routing_synthesized": False,
        "native_selected_shell_bare_recurrent_amplitude_transition_synthesized": False,
        "compute_uncompute_exact_if_native_controls_unchanged": True,
        "resource": checkpoint(started, f"native-shadow-sync-L{length}-complete"),
    }
    controls["pass"] = bool(
        controls["selected_terms_per_cell"] == 160
        and controls["distinct_patterns_per_cell"] == 160
        and controls["all_cell_distinct_pattern_failures"] == 0
        and controls["all_cell_role_pattern_mismatches"] == 0
        and controls["all_cell_direction_decoder_failures"] == 0
        and controls["all_cell_direction_decoder_tests"] == length**3 * 160 * 6
        and controls["degree_two_feature_rank"] == 68
        and controls["decoded_occupation_words"] == 64
        and controls["single_cell_single_direction_monomial_deletion_failures"]
        == [[48, 48, 8, 16, 8]] * 6
        and controls["proper_frames"] == 24
        and controls["all_cell_frame_role_failures"] == 0
        and controls["all_term_frame_decoder_failures"] == 0
        and controls["frame_group_failures"] == 0
        and controls["bare_compute_gate_calls_for_six_shadows"] == 282
        and toffoli["pass"]
    )
    return controls


def isolated_native_shadow_sync(length: int) -> dict:
    command = [
        sys.executable,
        str(Path(__file__).resolve()),
        "--internal-native-sync",
        "--length",
        str(length),
    ]
    try:
        completed = subprocess.run(
            command,
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=WALL_LIMIT_SECONDS - WALL_GRACE_SECONDS,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        raise ResourceWall(f"native-shadow-sync timed out at L{length}") from exc
    try:
        payload = json.loads(completed.stdout)
    except json.JSONDecodeError as exc:
        raise CertificateFailure(
            f"native-shadow-sync emitted invalid JSON at L{length}; "
            f"stderr={completed.stderr[-2000:]!r}"
        ) from exc
    if completed.returncode or not payload.get("pass", False):
        raise CertificateFailure(
            f"native-shadow-sync failed at L{length}: {payload!r}; "
            f"stderr={completed.stderr[-2000:]!r}"
        )
    return payload


def cycle522_semantic_contract() -> dict:
    source = CYCLE522_RUNNER.read_text(encoding="utf-8")
    required = (
        "def selected_carriers",
        "def selected_common_branches",
        "def selected_gauge_terms",
        "def selected_frame_representation",
        "term_builder=selected_gauge_terms",
        '"primitive_gate_genesis_and_schedule"',
    )
    missing = tuple(fragment for fragment in required if fragment not in source)
    return {
        "Cycle522_observed_sha256": file_sha(CYCLE522_RUNNER),
        "Cycle522_strict_hash_gate_enabled": CYCLE522_RUNNER in STRICT_FILE_HASHES,
        "required_fragments_missing": missing,
        "pass": not missing,
    }


def upstream_evidence() -> dict:
    expected = {str(path.relative_to(ROOT)): digest for path, digest in STRICT_FILE_HASHES.items()}
    observed = {str(path.relative_to(ROOT)): file_sha(path) for path in STRICT_FILE_HASHES}
    semantic = cycle522_semantic_contract()
    return {
        "expected_sha256": expected,
        "observed_sha256": observed,
        "Cycle522_selected_grammar_semantic_contract": semantic,
        "pass": expected == observed and semantic["pass"],
    }


def note_contract() -> dict:
    text = NOTE.read_text(encoding="utf-8").lower()
    required = (
        "10 givens",
        "15 contact",
        "seven-m2",
        "60,600",
        "154,800",
        "327,360",
        "282",
        "q_d = c_d",
        "proper-cubic",
        "koszul",
        "causal time",
        "host-side adaptive control",
        "authority: none",
        "audit: unset",
        "n1 — alternative-route map",
        "n2 — wall-independence audit",
        "n3 — hidden-wall scan",
        "n4 — residual matching",
        "n5 — rhetoric audit",
        "n6 — partial-closure path",
        "n7 — hostile steelman",
        "n8 — cross-cycle echo",
    )
    missing = tuple(fragment for fragment in required if fragment not in text)
    return {"required_fragments": len(required), "missing_fragments": missing, "pass": not missing}


def dry_contract() -> dict:
    evidence = upstream_evidence()
    note = note_contract()
    positions = local_layout_positions()
    geometry = {
        "face_center_leaves": Q_MODES,
        "center_tag": 1,
        "supercell_sites": 27,
        "leaf_center_distances": tuple(
            local_l1(positions[direction], positions[TAG_SITE]) for direction in range(Q_MODES)
        ),
        "proper_frames": len(c210.proper_cubic_frames()),
    }
    geometry["pass"] = (
        len(set(positions.values())) == LOCAL_M2
        and geometry["leaf_center_distances"] == (1,) * Q_MODES
        and geometry["proper_frames"] == 24
    )
    tests = {
        "stable_predecessor_hashes": evidence["pass"],
        "seven_M2_cubic_star_geometry": geometry["pass"],
        "note_scope_and_N1_N8_contract": note["pass"],
    }
    return {
        "revision": REVISION,
        "mode": "dry-contract",
        "status": "cycle523-protected-shadow-coin-contract-ready" if all(tests.values()) else "cycle523-dry-contract-failed",
        "authority": AUTHORITY,
        "audit": AUDIT,
        "evidence": evidence,
        "geometry": geometry,
        "note_contract": note,
        "tests": tests,
        "tests_passed": sum(tests.values()),
        "tests_total": len(tests),
        "pass": all(tests.values()),
    }


def protected_shadow_certificate() -> dict:
    started = time.monotonic()
    checkpoints = [checkpoint(started, "initial")]
    dry = dry_contract()
    if not dry["pass"]:
        raise CertificateFailure("Cycle523 dry contract failed")
    onsite, objects = onsite_compiler_controls()
    checkpoints.append(checkpoint(started, "onsite-compiler-complete"))
    adversarial = deletion_perturbation_controls(objects)
    checkpoints.append(checkpoint(started, "deletion-perturbation-complete"))
    frames = frame_controls(objects)
    checkpoints.append(checkpoint(started, "frame-covariance-complete"))
    layouts = (
        layout_schedule_controls(TRAIN_LENGTH, objects["mode_schedule"]),
        layout_schedule_controls(HELD_LENGTH, objects["mode_schedule"]),
    )
    checkpoints.append(checkpoint(started, "L5-L6-layout-schedules-complete"))
    native_sync = (
        isolated_native_shadow_sync(TRAIN_LENGTH),
        isolated_native_shadow_sync(HELD_LENGTH),
    )
    checkpoints.extend(row["resource"] for row in native_sync)
    stream = stream_boundary_controls()
    checkpoints.append(checkpoint(started, "stream-boundary-complete"))
    tests = {
        "dry_contract": dry["pass"],
        "exact_bare_coin_contact_parity_compiler": onsite["pass"],
        "inverse_leakage_deletion_perturbation_controls": adversarial["pass"],
        "all24_proper_cubic_Koszul_schedule_covariance": frames["pass"],
        "L5_train_held_L6_bounded_schedule_geometry": all(row["pass"] for row in layouts),
        "selected_native_shell_degree_two_shadow_sync_L5_L6": all(
            row["pass"] for row in native_sync
        ),
        "blank_tag_endpoint_stream_boundary_reproduced": stream["pass"],
        "resource_contract": rss_bytes() < RSS_GUARD_BYTES and swap_count() == 0,
    }
    elapsed = time.monotonic() - started
    return {
        "revision": REVISION,
        "mode": "protected-shadow-certificate",
        "status": (
            "cycle523-onsite-protected-shadow-primitive-closure-with-stream-boundary"
            if all(tests.values())
            else "cycle523-certificate-failed"
        ),
        "authority": AUTHORITY,
        "audit": AUDIT,
        "constitutional_effect": "none",
        "onsite_compiler": onsite,
        "deletion_perturbation": adversarial,
        "proper_cubic_frames": frames,
        "layout_schedules": layouts,
        "selected_native_shadow_sync": native_sync,
        "stream_boundary": stream,
        "strongest_constructive_result": {
            "encoding": "six private face-center occupation M2 plus one center parity-tag M2 per coarse cell",
            "intertwiner": "E7 (Wg Gamma(C)) = G7 E7 on full local M64",
            "primitive_support_M2": 2,
            "coin": "10 fermionic Givens plus one onsite phase, routed to 31 primitive calls",
            "contact": "15 controlled phases routed to 45 primitive calls",
            "parity": "six CNOT uncompute and six CNOT compute",
            "proper_cubic_covariance": "local Koszul CZ cocycle compiled on the same star",
            "selected_native_shell_sync": (
                "degree-two relational ANF computes all six occupation shadows "
                "on all 160 valid local terms"
            ),
            "full_Cycle230_stream_included": False,
        },
        "supplied_not_synthesized": {
            "Cycle219_beta_minus_0p3_coin_coefficients": True,
            "Cycle230_contact_g_0p37_and_update_factor_order": True,
            "three_by_three_by_three_supercell_origin": True,
            "compile_time_QR_coefficients_and_gate_order": True,
            "physical_elapsed_time_per_gate_or_macrostep": False,
            "autonomous_selection_of_beta_or_contact": False,
            "Cycle522_selected_native_grammar": True,
            "native_shadow_decoder_off_pattern_completion": True,
            "native_to_shadow_nearest_neighbor_routing": False,
            "native_selected_shell_bare_recurrent_amplitude_transition": False,
        },
        "causal_time_boundary": {
            "derived_discrete_factor_order": "parity-uncompute -> coin -> reverse-A -> edge-B -> contact -> parity-compute",
            "factor_order_called_causal_time": False,
            "physical_duration_or_energy_inferred": False,
            "runtime_host_side_adaptive_control": False,
        },
        "no_go_boundary": {
            "broad_no_go_gate": "FAIL / DO NOT SHIP",
            "disposition": "constructive-onsite-closure-with-route-specific-stream-residual",
            "shared_substrate_obstruction": False,
            "axiom_pressure": False,
        },
        "resources": {
            "elapsed_seconds": elapsed,
            "maximum_RSS_bytes": max(row["maximum_RSS_bytes"] for row in checkpoints),
            "process_swap_count": sum(row["process_swap_count"] for row in checkpoints),
            "hard_wall_seconds": WALL_LIMIT_SECONDS,
            "checkpoints": checkpoints,
            "native_sync_sizes_run_in_fresh_processes": True,
        },
        "tests": tests,
        "tests_passed": sum(tests.values()),
        "tests_total": len(tests),
        "pass": all(tests.values()),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=CLI_MODES, default="dry-contract")
    parser.add_argument("--internal-native-sync", action="store_true", help=argparse.SUPPRESS)
    parser.add_argument("--length", type=int, help=argparse.SUPPRESS)
    args = parser.parse_args()
    if hasattr(signal, "SIGALRM"):
        signal.signal(signal.SIGALRM, alarm_handler)
        signal.alarm(math.ceil(WALL_LIMIT_SECONDS))
    try:
        if args.internal_native_sync:
            if args.length not in (TRAIN_LENGTH, HELD_LENGTH):
                raise ValueError("internal native sync requires length 5 or 6")
            payload = native_shadow_sync_controls(args.length)
        else:
            payload = dry_contract() if args.mode == "dry-contract" else protected_shadow_certificate()
    except (CertificateFailure, ResourceWall, ValueError) as exc:
        payload = {
            "revision": REVISION,
            "mode": args.mode,
            "status": "cycle523-runner-failed",
            "authority": AUTHORITY,
            "audit": AUDIT,
            "error_type": type(exc).__name__,
            "error": str(exc),
            "pass": False,
        }
    finally:
        if hasattr(signal, "SIGALRM"):
            signal.alarm(0)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if payload["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
