#!/usr/bin/env python3
"""Cycle 489: physical-M2 translation-impulse inertia bridge.

The target and every numerical threshold below were frozen before the final
beta=-0.37, L=12288, h=7 row was executed.  Positive/negative onsite number
phase gradients shift the exact lattice translation character.  Their
opposite signed packet-displacement responses are combined into one
dimensionless inverse susceptibility and only then compared with the
independently derived Cycle-219 origin-curvature mass.

This is not an energy, rate, duration, force, lapse, or gravity construction.
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path
from typing import Iterable

import numpy as np
from scipy import sparse

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import physical_cycle269_common_m64_fixed_seam_cycle311_2026_07_18 as c311
import physical_cycle269_overlap_aware_two_cell_cycle315_2026_07_18 as c315
import physical_cycle269_three_cell_multiedge_cycle319_2026_07_18 as c319
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_M2_TRANSLATION_IMPULSE_INERTIA_BRIDGE_CYCLE489_NOTE_2026-07-20.md"
)
AUTHORITY = "none"
AUDIT = "unset"

SOURCE_HASHES = {
    "cycle219": (
        ROOT / "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py",
        "ad9bf5febde8b58e948f4a4240791216a20d61262149469763ef387455dff52a",
    ),
    "cycle311": (
        ROOT / "scripts/physical_cycle269_common_m64_fixed_seam_cycle311_2026_07_18.py",
        "4495bf39e1e2661866501e377b8ec1aefff656e261e428fa5b6738f73b49699c",
    ),
    "cycle315": (
        ROOT / "scripts/physical_cycle269_overlap_aware_two_cell_cycle315_2026_07_18.py",
        "52c18f96a1f8db9b79e4d0fba5ff76905170e6a8dc8c3e818fdf69984a1778c3",
    ),
    "cycle319": (
        ROOT / "scripts/physical_cycle269_three_cell_multiedge_cycle319_2026_07_18.py",
        "faa05d97542efca7684f4acc6f9b7dfb8e32a02f3f9d16adeae16449f5b702fb",
    ),
}

PACKET_WIDTH = 0.01
APPLICATIONS = 160
FIT_START = 40
MASS_RELATIVE_TOLERANCE = 0.01
BAND_FLOOR = 0.9995
BOUNDARY_CEILING = 1e-16
CHARACTER_TOLERANCE = 3e-13
OPPOSITE_SYMMETRY_TOLERANCE = 3e-11
EG_TOLERANCE = 2e-10


@dataclass(frozen=True)
class Fixture:
    name: str
    beta: float
    length: int
    harmonic: int
    disposition: str


FIXTURES = (
    Fixture("train-beta-0.2-kick-2", -0.2, 4096, 2, "train"),
    Fixture("train-beta-0.2-kick-4", -0.2, 4096, 4, "train"),
    Fixture("train-beta-0.3-kick-2", -0.3, 4096, 2, "train"),
    Fixture("train-beta-0.3-kick-4", -0.3, 4096, 4, "train"),
    Fixture("train-beta-0.4-kick-2", -0.4, 4096, 2, "train"),
    Fixture("train-beta-0.4-kick-4", -0.4, 4096, 4, "train"),
    # This row was touched during exploration and is deliberately not held.
    Fixture("disclosed-pilot-beta-0.35", -0.35, 8192, 3, "pilot"),
    # The final no-look row.  Do not move it before the train/pilot rows.
    Fixture("held-beta-0.37-size-12288", -0.37, 12288, 7, "held"),
)
SIZE_CONTROL = Fixture("larger-L-beta-0.3", -0.3, 8192, 4, "size-control")

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


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def angular_difference(left: float, right: float) -> float:
    return float(np.angle(np.exp(1j * (left - right))))


def contracts() -> None:
    text = normalized(NOTE)
    required = (
        "target freeze before the final held row",
        "translation-character impulse",
        "dimensionless displacement per declared update",
        "same free coin",
        "beta preparation remains supplied",
        "phase is not energy",
        "update count is not time",
        "response is not gravity",
        "norm weights are not probability",
        "authority: none",
        "audit: unset",
        "no axiom pressure",
        "no-go discipline gate",
    )
    missing = tuple(item for item in required if item not in text)
    check("note freezes the target and semantic firewalls", not missing, missing)
    hash_rows = {
        name: sha256(path.read_bytes()).hexdigest() == expected
        for name, (path, expected) in SOURCE_HASHES.items()
    }
    check("frozen physical-matter predecessors have exact hashes", all(hash_rows.values()), hash_rows)


def prepare_packet(item: Fixture):
    species = c219.common_species(item.beta)
    momenta = 2 * np.pi * np.fft.fftfreq(item.length)
    packet_k = np.zeros((item.length, 6), dtype=complex)
    for index, momentum in enumerate(momenta):
        wrapped = float(np.angle(np.exp(1j * momentum)))
        envelope = float(np.exp(-0.5 * (wrapped / PACKET_WIDTH) ** 2))
        if envelope <= 1e-14:
            continue
        _phase, vector = c210.branch_eigenpair(
            np.asarray((momentum, 0.0, 0.0)), species
        )
        packet_k[index] = envelope * vector
    packet_k /= np.linalg.norm(packet_k)
    packet = np.fft.ifft(packet_k, axis=0, norm="ortho")
    packet = np.roll(packet, item.length // 2, axis=0)
    positions = np.arange(item.length, dtype=float) - item.length // 2
    return species, momenta, positions, packet


def translation_character(packet: np.ndarray) -> complex:
    return complex(np.vdot(packet, np.roll(packet, -1, axis=0)))


def packet_density(packet: np.ndarray) -> np.ndarray:
    return np.sum(abs(packet) ** 2, axis=1)


def packet_centroid(packet: np.ndarray, positions: np.ndarray) -> float:
    return float(np.sum(packet_density(packet) * positions).real)


def selected_branch_norm_weight(packet, momenta, species) -> float:
    """Squared projection norm on the selected analytic branch."""

    packet_k = np.fft.fft(packet, axis=0, norm="ortho")
    weight = 0.0
    for index, momentum in enumerate(momenta):
        if np.linalg.norm(packet_k[index]) < 1e-12:
            continue
        _phase, vector = c210.branch_eigenpair(
            np.asarray((momentum, 0.0, 0.0)), species
        )
        weight += abs(np.vdot(vector, packet_k[index])) ** 2
    return float(weight)


def free_step(packet: np.ndarray, coin: np.ndarray, *, inverse: bool = False) -> np.ndarray:
    if inverse:
        unstreamed = np.zeros_like(packet)
        for direction in range(6):
            unstreamed[:, direction] = np.roll(
                packet[:, direction], -int(c210.DIRECTIONS[direction, 0])
            )
        return np.einsum("ab,xb->xa", coin.conj().T, unstreamed, optimize=True)
    return c210.local_molecular_step(packet, coin)


def signed_trace(
    base: np.ndarray,
    positions: np.ndarray,
    momenta: np.ndarray,
    species,
    q: float,
    sign: int,
) -> dict[str, object]:
    kicked = np.exp(1j * sign * q * positions)[:, None] * base
    base_character = translation_character(base)
    kicked_character = translation_character(kicked)
    character_shift = angular_difference(
        float(np.angle(kicked_character)), float(np.angle(base_character))
    )
    packet = kicked.copy()
    centroids = [packet_centroid(packet, positions)]
    maximum_norm_error = 0.0
    for _ in range(APPLICATIONS):
        packet = free_step(packet, species.coin)
        maximum_norm_error = max(maximum_norm_error, abs(np.linalg.norm(packet) - 1))
        centroids.append(packet_centroid(packet, positions))
    fit_axis = np.arange(FIT_START, APPLICATIONS + 1, dtype=float)
    displacement_per_update = float(
        np.polyfit(fit_axis, np.asarray(centroids[FIT_START:]), 1)[0]
    )
    density = packet_density(packet)
    boundary = float(np.sum(density[abs(positions) > len(positions) / 4]))
    restored = packet.copy()
    for _ in range(APPLICATIONS):
        restored = free_step(restored, species.coin, inverse=True)
    restored *= np.exp(-1j * sign * q * positions)[:, None]
    return {
        "sign": sign,
        "q": q,
        "character_shift": character_shift,
        "character_residual": abs(angular_difference(character_shift, sign * q)),
        "displacement_per_update": displacement_per_update,
        "final_centroid": centroids[-1],
        "maximum_norm_error": maximum_norm_error,
        "selected_branch_norm_weight": selected_branch_norm_weight(
            packet, momenta, species
        ),
        "boundary_weight": boundary,
        "inverse_residual": float(np.linalg.norm(restored - base)),
    }


def response_row(item: Fixture) -> dict[str, object]:
    species, momenta, positions, base = prepare_packet(item)
    q = 2 * np.pi * item.harmonic / item.length
    plus = signed_trace(base, positions, momenta, species, q, +1)
    minus = signed_trace(base, positions, momenta, species, q, -1)
    # Positive exp(+iqx) shifts the translation character by +q but, under
    # the repository stream/FFT convention, produces negative x displacement.
    susceptibility = -(
        plus["displacement_per_update"] - minus["displacement_per_update"]
    ) / (2 * q)
    impulse_mass = 1 / susceptibility
    curvature = c210.curvature_tensor(species, step=1e-4)
    curvature_mass = 1 / float(np.mean(np.diag(curvature)))
    analytic_mass = float(species.analytic_mass)
    return {
        "fixture": item.name,
        "disposition": item.disposition,
        "beta": item.beta,
        "L": item.length,
        "transverse_periods": (3, 3),
        "harmonic": item.harmonic,
        "q": q,
        "packet_width": PACKET_WIDTH,
        "applications": APPLICATIONS,
        "fit_window": (FIT_START, APPLICATIONS),
        "plus": plus,
        "minus": minus,
        "opposite_displacement_residual": abs(
            plus["displacement_per_update"] + minus["displacement_per_update"]
        ),
        "susceptibility": susceptibility,
        "impulse_mass": impulse_mass,
        "curvature_mass": curvature_mass,
        "analytic_mass": analytic_mass,
        "impulse_curvature_relative_residual": abs(impulse_mass / curvature_mass - 1),
        "curvature_analytic_relative_residual": abs(curvature_mass / analytic_mass - 1),
        "apparatus_cells": 9 * item.length,
        "direct_Q1_M2": 54 * item.length,
    }


def response_controls() -> tuple[list[dict[str, object]], dict[str, object]]:
    print("\nTRANSLATION-CHARACTER IMPULSE / DISPLACEMENT RESPONSE")
    rows = [response_row(item) for item in FIXTURES]
    for row in rows:
        print("ROW", row)
    maximum_character = max(
        side["character_residual"]
        for row in rows
        for side in (row["plus"], row["minus"])
    )
    maximum_mass = max(row["impulse_curvature_relative_residual"] for row in rows)
    minimum_band = min(
        side["selected_branch_norm_weight"]
        for row in rows
        for side in (row["plus"], row["minus"])
    )
    maximum_boundary = max(
        side["boundary_weight"] for row in rows for side in (row["plus"], row["minus"])
    )
    maximum_inverse = max(
        side["inverse_residual"] for row in rows for side in (row["plus"], row["minus"])
    )
    maximum_opposite = max(row["opposite_displacement_residual"] for row in rows)
    held = [row for row in rows if row["disposition"] == "held"]
    check(
        "exact lattice-character kicks produce opposite displacement susceptibility and recover curvature mass on train, disclosed pilot, and final held row",
        len(held) == 1
        and maximum_character < CHARACTER_TOLERANCE
        and maximum_opposite < OPPOSITE_SYMMETRY_TOLERANCE
        and maximum_mass < MASS_RELATIVE_TOLERANCE
        and minimum_band > BAND_FLOOR
        and maximum_boundary < BOUNDARY_CEILING
        and maximum_inverse < 3e-12,
        {
            "rows": rows,
            "maximum_character_residual": maximum_character,
            "maximum_opposite_displacement_residual": maximum_opposite,
            "maximum_impulse_curvature_relative_residual": maximum_mass,
            "minimum_selected_band_weight": minimum_band,
            "maximum_boundary_weight": maximum_boundary,
            "maximum_inverse_residual": maximum_inverse,
        },
    )

    size_row = response_row(SIZE_CONTROL)
    reference = next(row for row in rows if row["fixture"] == "train-beta-0.3-kick-2")
    size_residual = abs(size_row["impulse_mass"] / reference["impulse_mass"] - 1)
    check(
        "doubling the longitudinal size at the same beta and exact q does not move the impulse mass",
        abs(size_row["q"] - reference["q"]) < 2e-15 and size_residual < 2e-5,
        {"reference": reference, "larger_L": size_row, "relative_residual": size_residual},
    )
    return rows, size_row


def full_fock_number_phase(qx: float) -> np.ndarray:
    phases = [np.exp(1j * qx * number) for number, _label in c311.FOCK_LABELS]
    return np.diag(phases)


def single_cell_physical_controls() -> dict[str, object]:
    print("\nLOCAL PHYSICAL M64 COIN / NUMBER-PHASE COMPILER")
    rows = []
    for length, held in ((3, False), (6, True)):
        code = c311.c269.build_code(length)
        encoder = c311.common_encoder(code)
        basis, flagged, occurrence = c311.flagged_basis_and_encoding(encoder)
        exchange = c311.exchange_matrix(encoder, occurrence)
        constrained = c311.constrained_encoding(flagged, exchange)
        constraint = c311.role_constraint(exchange)
        fock_input = c311.fock_input_embedding()
        physical_encoding = constrained @ fock_input
        projector = physical_encoding @ physical_encoding.conj().T
        local_rows = []
        for name, logical in (
            ("coin", c311.logical_coin(c219.common_species(-0.3).coin)),
            ("kick", c311.logical_coin(np.exp(1j * 0.173) * np.eye(6))),
        ):
            physical, _old = c311.physical_coin(flagged, logical, exchange)
            output = physical @ physical_encoding
            expected = constrained @ (logical @ fock_input)
            restored = physical.conj().T @ output
            local_rows.append(
                {
                    "factor": name,
                    "EG_residual": float(np.linalg.norm(output - expected)),
                    "inverse_residual": float(np.linalg.norm(restored - physical_encoding)),
                    "leakage": float(np.linalg.norm(output - projector @ output)),
                    "constraint_residual": float(np.linalg.norm(constraint @ output - output)),
                }
            )
        logical_kick = full_fock_number_phase(0.173)
        logical_contact = np.diag(
            [
                np.exp(1j * c311.COUPLING * (number * (number - 1) // 2))
                for number, _label in c311.FOCK_LABELS
            ]
        )
        rows.append(
            {
                "L": length,
                "held": held,
                "physical_encoding_shape": physical_encoding.shape,
                "Gram_residual": float(
                    np.linalg.norm(
                        physical_encoding.conj().T @ physical_encoding - np.eye(64)
                    )
                ),
                "factor_rows": local_rows,
                "kick_contact_commutator": float(
                    np.linalg.norm(logical_kick @ logical_contact - logical_contact @ logical_kick)
                ),
                "installed_M2_per_cell": 23,
            }
        )
    maximum = max(
        max(
            row["Gram_residual"],
            row["kick_contact_commutator"],
            *(value for factor in row["factor_rows"] for value in (
                factor["EG_residual"], factor["inverse_residual"],
                factor["leakage"], factor["constraint_residual"]
            )),
        )
        for row in rows
    )
    check(
        "the actual Cycle311 M64 local coin and number-phase kick intertwine, invert, preserve the local role gauge, and commute with contact at train and held compiler sizes",
        maximum < EG_TOLERANCE,
        {"rows": rows, "maximum_residual": maximum},
    )
    return {"rows": rows, "maximum_residual": maximum}


def pair_encoding(length: int, labels):
    code = c315.c269.build_code(length)
    reducer = c315.RayReducer(code)
    encoding = c315.joint_encoding(code, labels, reducer, False)
    if encoding.shape[0] < len(reducer.row_by_aux):
        encoding.resize((len(reducer.row_by_aux), encoding.shape[1]))
    return code, encoding


def pair_physical_controls() -> dict[str, object]:
    print("\nLOCAL PHYSICAL EDGE / KICK AMBIENT COMPLETIONS")
    labels = c315.joint_labels(1)
    species = c219.common_species(-0.3)
    coin = c315.logical_coin_matrix(labels, species.coin)
    stream = c315.edge_fswap_matrix(labels, 0)
    contact = c315.contact_matrix(labels, c311.COUPLING)
    update = contact @ stream @ coin
    q = 0.173
    kick = sparse.diags(
        [
            np.exp(1j * q * right_number)
            for _left_number, _left_label, right_number, _right_label in labels
        ],
        format="csc",
    )
    rows = []
    for length, held in ((3, False), (6, True)):
        code, encoding = pair_encoding(length, labels)
        identity = sparse.eye(len(labels), format="csc")
        gram = encoding.conj().T @ encoding
        local = []
        for name, operator in (("free-plus-contact-edge", update), ("character-kick", kick)):
            ambient = c315.ambient_completion_controls(encoding, operator)
            local.append({"factor": name, **ambient})
        support = c315.physical_support_and_constraint_controls(code, labels)
        rows.append(
            {
                "L": length,
                "held": held,
                "logical_columns": len(labels),
                "physical_rays": encoding.shape[0],
                "Gram_residual": c315.largest_singular(gram - identity),
                "ambient_rows": local,
                "support": support,
            }
        )
    covariance = c315.covariance_translation_controls(labels, coin, contact, update)
    maximum = max(
        max(
            row["Gram_residual"],
            *(factor["intertwining_residual"] for factor in row["ambient_rows"]),
            *(factor["maximum_randomized_ambient_inverse_residual"] for factor in row["ambient_rows"]),
        )
        for row in rows
    )
    check(
        "the actual bounded two-cell physical edge and kick completions intertwine and invert, with all-24 carried edge covariance",
        maximum < EG_TOLERANCE
        and covariance["proper_cubic_frames"] == 24
        and covariance["maximum_update_covariance_residual"] < EG_TOLERANCE
        and covariance["edge_role_group_law_failures"] == 0
        and covariance["L3_translation_edge_role_failures"] == 0,
        {"rows": rows, "covariance": covariance, "maximum_residual": maximum},
    )
    return {"rows": rows, "covariance": covariance, "maximum_residual": maximum}


def direct_q1_compiler_controls() -> dict[str, object]:
    """Literal M2 occupation compiler used by the corridor response sector.

    The local code is vacuum plus one excitation of six M2.  The complete
    64-state local M64 coin/contact controls above remain separate.  On the
    declared global Q=1 corridor, every onsite coin uses six M2 and every
    nearest-neighbor stream is one two-M2 FSWAP (equal to SWAP on Q<=1).
    """

    species = c219.common_species(-0.3)
    local_encoding = sparse.coo_matrix(
        (
            np.ones(7),
            (
                (0,) + tuple(1 << direction for direction in range(6)),
                tuple(range(7)),
            ),
        ),
        shape=(64, 7),
        dtype=complex,
    ).tocsc()
    local_logical = sparse.block_diag((np.ones((1, 1)), species.coin), format="csc")
    local_physical = sparse.eye(64, format="lil", dtype=complex)
    indices = [1 << direction for direction in range(6)]
    local_physical[np.ix_(indices, indices)] = species.coin
    local_physical = local_physical.tocsc()
    eg = c315.largest_singular(local_physical @ local_encoding - local_encoding @ local_logical)
    inverse = c315.largest_singular(
        local_physical.conj().T @ (local_physical @ local_encoding) - local_encoding
    )

    # Two physical M2 FSWAP truth table in |00>,|01>,|10>,|11> order.
    fswap = np.asarray(
        ((1, 0, 0, 0), (0, 0, 1, 0), (0, 1, 0, 0), (0, 0, 0, -1)),
        dtype=complex,
    )
    fswap_inverse = float(np.linalg.norm(fswap.conj().T @ fswap - np.eye(4)))
    q1_swap_residual = float(
        np.linalg.norm(fswap[np.ix_((0, 1, 2), (0, 1, 2))] - np.asarray(
            ((1, 0, 0), (0, 0, 1), (0, 1, 0)), dtype=complex
        ))
    )
    frames = c210.proper_cubic_frames()
    covariance = []
    for frame in frames:
        representation = c210.direction_permutation(frame)
        covariance.append(
            float(np.linalg.norm(representation @ species.coin @ representation.conj().T - species.coin))
        )
    check(
        "the response corridor has an explicit direct Q1 M2 occupation encoding with six-M2 onsite coin, two-M2 FSWAP stream, inverse, and all-24 coin covariance",
        eg < EG_TOLERANCE
        and inverse < EG_TOLERANCE
        and fswap_inverse < EG_TOLERANCE
        and q1_swap_residual < EG_TOLERANCE
        and len(frames) == 24
        and max(covariance) < EG_TOLERANCE,
        {
            "local_encoding_shape": local_encoding.shape,
            "local_EG_residual": eg,
            "local_inverse_residual": inverse,
            "FSWAP_inverse_residual": fswap_inverse,
            "Q_le_1_FSWAP_equals_SWAP_residual": q1_swap_residual,
            "maximum_coin_covariance": max(covariance),
            "onsite_support_M2": 6,
            "stream_support_M2": 2,
            "constant_overhead_M2_per_cell": 6,
            "global_Jordan_Wigner_order": False,
            "global_parity_service": False,
        },
    )
    return {
        "local_EG": eg,
        "local_inverse": inverse,
        "FSWAP_inverse": fswap_inverse,
        "maximum_covariance": max(covariance),
    }


def direct_volume_logical_forward(state: np.ndarray, q: float) -> np.ndarray:
    """Kick, onsite coin, and physical nearest-neighbor stream on Lx3x3."""

    length = state.shape[0]
    x = np.arange(length, dtype=float) - length // 2
    kicked = np.exp(1j * q * x)[:, None, None, None] * state
    coin = c219.common_species(-0.3).coin
    mixed = np.einsum("ab,xyzb->xyza", coin, kicked, optimize=True)
    output = np.zeros_like(mixed)
    axes = (0, 1, 2)
    for direction, vector in enumerate(c210.DIRECTIONS):
        output[..., direction] = np.roll(
            mixed[..., direction], tuple(int(value) for value in vector), axis=axes
        )
    return output


def direct_volume_logical_inverse(state: np.ndarray, q: float) -> np.ndarray:
    length = state.shape[0]
    unstreamed = np.zeros_like(state)
    axes = (0, 1, 2)
    for direction, vector in enumerate(c210.DIRECTIONS):
        unstreamed[..., direction] = np.roll(
            state[..., direction], tuple(-int(value) for value in vector), axis=axes
        )
    coin = c219.common_species(-0.3).coin
    unkicked = np.einsum("ab,xyzb->xyza", coin.conj().T, unstreamed, optimize=True)
    x = np.arange(length, dtype=float) - length // 2
    return np.exp(-1j * q * x)[:, None, None, None] * unkicked


def direct_volume_encode(state: np.ndarray) -> dict[int, complex]:
    output: dict[int, complex] = {}
    for mode, amplitude in enumerate(state.reshape(-1)):
        if abs(amplitude) > 2e-14:
            output[1 << mode] = complex(amplitude)
    return output


def direct_volume_decode(words: dict[int, complex], shape) -> tuple[np.ndarray, int]:
    output = np.zeros(int(np.prod(shape)), dtype=complex)
    leakage = 0
    for word, amplitude in words.items():
        if word <= 0 or word.bit_count() != 1:
            leakage += 1
            continue
        mode = word.bit_length() - 1
        if mode >= len(output):
            leakage += 1
            continue
        output[mode] += amplitude
    return output.reshape(shape), leakage


def direct_volume_physical_forward(words: dict[int, complex], shape, q: float):
    length, side_y, side_z, directions = shape
    if (side_y, side_z, directions) != (3, 3, 6):
        raise ValueError("the declared direct compiler uses an Lx3x3 six-direction torus")
    coin = c219.common_species(-0.3).coin
    output: dict[int, complex] = {}
    for word, amplitude in words.items():
        if word.bit_count() != 1:
            raise ValueError("the direct corridor compiler is declared on global Q1")
        mode = word.bit_length() - 1
        cell, source_direction = divmod(mode, 6)
        x, remainder = divmod(cell, side_y * side_z)
        y, z = divmod(remainder, side_z)
        phase = np.exp(1j * q * (x - length // 2))
        for target_direction, coefficient in enumerate(coin[:, source_direction]):
            if abs(coefficient) <= 2e-14:
                continue
            vector = c210.DIRECTIONS[target_direction]
            target_x = (x + int(vector[0])) % length
            target_y = (y + int(vector[1])) % side_y
            target_z = (z + int(vector[2])) % side_z
            target_cell = (target_x * side_y + target_y) * side_z + target_z
            target_mode = 6 * target_cell + target_direction
            target_word = 1 << target_mode
            output[target_word] = output.get(target_word, 0j) + amplitude * phase * coefficient
    return output


def direct_volume_physical_inverse(words: dict[int, complex], shape, q: float):
    length, side_y, side_z, directions = shape
    if (side_y, side_z, directions) != (3, 3, 6):
        raise ValueError("the declared direct compiler uses an Lx3x3 six-direction torus")
    coin = c219.common_species(-0.3).coin
    unstreamed: dict[tuple[int, int, int, int], complex] = {}
    for word, amplitude in words.items():
        if word.bit_count() != 1:
            raise ValueError("the direct corridor compiler is declared on global Q1")
        mode = word.bit_length() - 1
        cell, direction = divmod(mode, 6)
        x, remainder = divmod(cell, side_y * side_z)
        y, z = divmod(remainder, side_z)
        vector = c210.DIRECTIONS[direction]
        source = (
            (x - int(vector[0])) % length,
            (y - int(vector[1])) % side_y,
            (z - int(vector[2])) % side_z,
            direction,
        )
        unstreamed[source] = unstreamed.get(source, 0j) + amplitude
    output: dict[int, complex] = {}
    for (x, y, z, target_direction), amplitude in unstreamed.items():
        phase = np.exp(-1j * q * (x - length // 2))
        for source_direction, coefficient in enumerate(coin.conj().T[:, target_direction]):
            if abs(coefficient) <= 2e-14:
                continue
            cell = (x * side_y + y) * side_z + z
            word = 1 << (6 * cell + source_direction)
            output[word] = output.get(word, 0j) + amplitude * phase * coefficient
    return output


def direct_volume_compiler_controls() -> dict[str, object]:
    print("\nDIRECT FINITE-VOLUME Q1 E/G / INVERSE")
    rng = np.random.default_rng(489)
    rows = []
    for length, held in ((4, False), (6, True)):
        shape = (length, 3, 3, 6)
        q = 2 * np.pi / length
        state = rng.normal(size=shape) + 1j * rng.normal(size=shape)
        state /= np.linalg.norm(state)
        encoded = direct_volume_encode(state)
        logical = direct_volume_logical_forward(state, q)
        physical_words = direct_volume_physical_forward(encoded, shape, q)
        physical, leakage = direct_volume_decode(physical_words, shape)
        restored_words = direct_volume_physical_inverse(physical_words, shape, q)
        restored, inverse_leakage = direct_volume_decode(restored_words, shape)
        logical_restored = direct_volume_logical_inverse(logical, q)
        rows.append(
            {
                "L": length,
                "held": held,
                "logical_Q1_columns": int(np.prod(shape)),
                "physical_M2": int(np.prod(shape)),
                "EG_residual": float(np.linalg.norm(physical - logical)),
                "physical_inverse_residual": float(np.linalg.norm(restored - state)),
                "logical_inverse_residual": float(np.linalg.norm(logical_restored - state)),
                "norm_residual": abs(np.linalg.norm(physical) - 1),
                "leakage_words": leakage + inverse_leakage,
                "onsite_support_M2": 6,
                "stream_support_M2": 2,
                "contact_support_M2": 6,
                "constant_overhead_M2_per_cell": 6,
            }
        )
    maximum = max(
        max(
            row["EG_residual"], row["physical_inverse_residual"],
            row["logical_inverse_residual"], row["norm_residual"]
        )
        for row in rows
    )
    check(
        "the literal finite-volume direct Q1 encoding satisfies E G = G_physical E and the inverse on train and held Lx3x3 M2 tori",
        maximum < 3e-13 and all(row["leakage_words"] == 0 for row in rows),
        {"rows": rows, "maximum_residual": maximum},
    )
    return {"rows": rows, "maximum_residual": maximum}


def covariance_mass_contact_controls(rows: Iterable[dict[str, object]]) -> dict[str, object]:
    print("\nALL-24 RESPONSE COVARIANCE / MASS / CONTACT")
    frames = c210.proper_cubic_frames()
    response_covariance = []
    for row in rows:
        species = c219.common_species(row["beta"])
        q = row["q"]
        for frame in frames:
            axis = frame @ np.asarray((1.0, 0.0, 0.0))
            plus_phase, _ = c210.branch_eigenpair(q * axis, species)
            minus_phase, _ = c210.branch_eigenpair(-q * axis, species)
            reference_plus, _ = c210.branch_eigenpair(np.asarray((q, 0.0, 0.0)), species)
            reference_minus, _ = c210.branch_eigenpair(np.asarray((-q, 0.0, 0.0)), species)
            response_covariance.extend(
                (
                    abs(angular_difference(plus_phase, reference_plus)),
                    abs(angular_difference(minus_phase, reference_minus)),
                )
            )
    reference_species = c219.common_species(-0.3)
    mass = c219.rest_mass(reference_species)
    labels = c319.triple_labels()
    contact = c319.triple_contact(labels)
    contact_nontrivial = int(np.count_nonzero(abs(contact.diagonal() - 1) > 2e-14))
    check(
        "all response axes carry through 24 proper-cubic frames while the reference mass and 645-column contact fixtures remain unchanged",
        len(frames) == 24
        and max(response_covariance) < 3e-12
        and abs(mass - 0.4534056541748851) < 2e-15
        and contact_nontrivial == 645,
        {
            "frames": len(frames),
            "maximum_response_covariance": max(response_covariance),
            "reference_mass_fixture": mass,
            "contact_nontrivial_columns": contact_nontrivial,
        },
    )
    return {
        "frames": len(frames),
        "maximum_response_covariance": max(response_covariance),
        "mass_fixture": mass,
        "contact_nontrivial_columns": contact_nontrivial,
    }


def deletion_and_domain_controls(reference: dict[str, object]) -> dict[str, object]:
    print("\nDELETIONS / MALFORMED DOMAINS")
    item = next(item for item in FIXTURES if item.name == reference["fixture"])
    species, momenta, positions, base = prepare_packet(item)
    q = reference["q"]
    # Kick deletion gives identical plus/minus traces and hence zero numerator.
    deleted_plus = signed_trace(base, positions, momenta, species, 0.0, +1)
    deleted_minus = signed_trace(base, positions, momenta, species, 0.0, -1)
    deleted_kick_numerator = abs(
        deleted_plus["displacement_per_update"] - deleted_minus["displacement_per_update"]
    )

    # Coin deletion: pure streaming has a different signed susceptibility.
    def deleted_coin_displacement(sign: int) -> float:
        packet = np.exp(1j * sign * q * positions)[:, None] * base
        centres = [packet_centroid(packet, positions)]
        for _ in range(APPLICATIONS):
            output = np.zeros_like(packet)
            for direction in range(6):
                output[:, direction] = np.roll(
                    packet[:, direction], int(c210.DIRECTIONS[direction, 0])
                )
            packet = output
            centres.append(packet_centroid(packet, positions))
        return float(
            np.polyfit(
                np.arange(FIT_START, APPLICATIONS + 1), centres[FIT_START:], 1
            )[0]
        )

    coin_deleted_numerator = abs(
        deleted_coin_displacement(+1) - deleted_coin_displacement(-1)
    )
    intact_numerator = abs(
        reference["plus"]["displacement_per_update"]
        - reference["minus"]["displacement_per_update"]
    )

    # Deleting one stream arm changes a generic state and breaks inverse.
    rng = np.random.default_rng(489)
    probe = rng.normal(size=(31, 6)) + 1j * rng.normal(size=(31, 6))
    probe /= np.linalg.norm(probe)
    intact = free_step(probe, species.coin)
    mixed = np.einsum("ab,xb->xa", species.coin, probe, optimize=True)
    deleted_stream = np.zeros_like(mixed)
    for direction in range(6):
        shift = 0 if direction == 0 else int(c210.DIRECTIONS[direction, 0])
        deleted_stream[:, direction] = np.roll(mixed[:, direction], shift)
    stream_deletion_residual = float(np.linalg.norm(intact - deleted_stream))

    malformed_character = 0.173
    seam_residual = abs(np.exp(1j * malformed_character * item.length) - 1)
    rejects = 0
    for bad in (
        Fixture("bad-beta", 0.0, 4096, 2, "malformed"),
        Fixture("bad-length", -0.3, 1, 2, "malformed"),
        Fixture("bad-harmonic", -0.3, 4096, 0, "malformed"),
    ):
        try:
            if not (-0.6 < bad.beta < -0.05):
                raise ValueError("beta outside declared massive branch")
            if bad.length < 16:
                raise ValueError("corridor too short")
            if bad.harmonic <= 0:
                raise ValueError("kick must be a nonzero lattice character")
        except ValueError:
            rejects += 1
    check(
        "kick, coin, and stream deletions are visible and malformed beta/size/character inputs are rejected",
        deleted_kick_numerator < 2e-14
        and abs(coin_deleted_numerator - intact_numerator) > 1e-4
        and stream_deletion_residual > 0.05
        and seam_residual > 0.1
        and rejects == 3,
        {
            "deleted_kick_response_numerator": deleted_kick_numerator,
            "intact_response_numerator": intact_numerator,
            "coin_deleted_response_numerator": coin_deleted_numerator,
            "stream_deletion_state_residual": stream_deletion_residual,
            "malformed_noncharacter_seam_residual": seam_residual,
            "lawful_domain_rejections": rejects,
        },
    )
    return {
        "deleted_kick_numerator": deleted_kick_numerator,
        "coin_deleted_numerator": coin_deleted_numerator,
        "stream_deletion_residual": stream_deletion_residual,
        "malformed_seam_residual": seam_residual,
        "rejects": rejects,
    }


def inventory_controls(rows, local, pair, direct, volume, covariance, deletions) -> None:
    held = next(row for row in rows if row["disposition"] == "held")
    supplied = (
        "Cycle219 one-parameter coin family and beta preparation",
        "direct Q1 occupation meaning and blank physical M2 preparation",
        "Cycle311/315 role-gauge encoders and off-code identity completions",
        "periodic Lx3x3 apparatus, origin, axis, packet width, kick harmonics",
        "160 applications, fit window, centroid effect, thresholds, tolerances",
        "proper-cubic frame transport and fixed factor order",
    )
    derived = (
        "exact translation-character shift under each lattice-character kick",
        "opposite-kick dimensionless displacement susceptibility",
        "train/pilot/held agreement with independently derived curvature mass",
        "direct Q1 M2 E/G plus full local M64 and two-cell gauge-compiler E/G",
        "inverse, leakage, all-24 covariance, size, deletion, and domain controls",
        "unchanged reference mass and 645-column contact fixtures",
    )
    open_items = (
        "physical generation or empirical selection of beta and a mass spectrum",
        "autonomous packet/kick/effect preparation and primitive synthesis",
        "full-number recurrent volume compiler beyond the declared Q1 corridor",
        "calibration of the dimensionless update displacement to duration or momentum",
        "interaction-dressed inertia, source law, passive gravity, and backreaction",
        "Record formation, occurrence, Born probability, and realized history",
    )
    check(
        "the result inventories supplied, derived, and open structure without semantic promotion",
        held["disposition"] == "held"
        and local["maximum_residual"] < EG_TOLERANCE
        and pair["maximum_residual"] < EG_TOLERANCE
        and direct["local_EG"] < EG_TOLERANCE
        and volume["maximum_residual"] < EG_TOLERANCE
        and covariance["contact_nontrivial_columns"] == 645
        and deletions["rejects"] == 3,
        {
            "supplied": supplied,
            "derived": derived,
            "open": open_items,
            "authority": AUTHORITY,
            "audit": AUDIT,
            "phase_is_energy": False,
            "update_count_is_time": False,
            "generator_element_is_rate": False,
            "response_is_gravity": False,
            "norm_weight_is_probability": False,
            "broad_no_go": False,
            "minimum_content": False,
            "axiom_pressure": False,
        },
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CYCLE 489: PHYSICAL M2 TRANSLATION-IMPULSE INERTIA BRIDGE")
    print(f"authority={AUTHORITY}; audit={AUDIT}")
    contracts()
    local = single_cell_physical_controls()
    pair = pair_physical_controls()
    direct = direct_q1_compiler_controls()
    volume = direct_volume_compiler_controls()
    rows, _size = response_controls()
    covariance = covariance_mass_contact_controls(rows)
    reference = next(row for row in rows if row["fixture"] == "train-beta-0.3-kick-2")
    deletions = deletion_and_domain_controls(reference)
    inventory_controls(rows, local, pair, direct, volume, covariance, deletions)
    print(f"SUMMARY {PASS} passed, {FAIL} failed")
    print(
        "RESULT",
        "PHYSICAL_M2_TRANSLATION_IMPULSE_INERTIA_BRIDGE_CERTIFIED"
        if FAIL == 0
        else "PHYSICAL_M2_TRANSLATION_IMPULSE_INERTIA_BRIDGE_NOT_CERTIFIED",
    )
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
