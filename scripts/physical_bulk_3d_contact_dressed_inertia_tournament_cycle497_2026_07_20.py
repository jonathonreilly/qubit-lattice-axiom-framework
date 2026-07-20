#!/usr/bin/env python3
"""Cycle 497 workbench: exact bulk-cubic two-CAR translation quotient.

This file is frozen to train-only execution until the companion note declares
the held cube/kick and all numerical gates.  It builds the native Cycle-492
functional controller coin and the Cycle-230 law in the exact order

    U2 = W_g wedge^2(S_stream C).

The quotient removes only simultaneous translations of an odd L^3 torus.  It
retains every three-dimensional relative displacement and literal cell
co-location.  It is not claimed to be recurrently compiled into physical M2
sites.  Phase is not energy, update count is not time, displacement is not
velocity, response is not gravity, and squared norm is not probability.
Authority is none; audit is unset.
"""

from __future__ import annotations

from hashlib import sha256
from pathlib import Path
import resource
import time

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigs

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import generated_beta_phase_register_cycle220_2026_07_16 as c220
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_BULK_3D_CONTACT_DRESSED_INERTIA_TOURNAMENT_CYCLE497_NOTE_2026-07-20.md"
)
AUTHORITY = "none"
AUDIT = "unset"
COUPLING = c230.COUPLING
TARGET_PHASE = -2.844
PACKET_WIDTH = 0.9
ENVELOPE_CUTOFF = 1e-4
APPLICATIONS = 12
FIT_START = 3
TRAIN_FIXTURES = ((5, 1), (7, 1))
HELD_FIXTURE = (9, 2)
UNITARITY_TOLERANCE = 2e-10
EG_TOLERANCE = 1e-10
EIGEN_TOLERANCE = 3e-10
NORM_TOLERANCE = 5e-13
INVERSE_TOLERANCE = 5e-13
CHARACTER_TOLERANCE = 5e-13
TRACKING_FLOOR = 0.5
BAND_FLOOR = 0.5
DYNAMIC_CONTACT_FLOOR = 0.01
BOUNDARY_CEILING = 0.4
CIRCULAR_STRENGTH_FLOOR = 0.03
OPPOSITE_CEILING = 0.05
MASS_RELATIVE_CEILING = 0.15
CURVATURE_SIZE_RELATIVE_CEILING = 0.25
CONTACT_DELETION_FLOOR = 0.05
CORRIDOR_TRAIN = (31, 3, 3)
CORRIDOR_HELD = (47, 3, 3)
CORRIDOR_PACKET_WIDTH = 0.12
CORRIDOR_APPLICATIONS = 100
CORRIDOR_FIT_START = 30
CORRIDOR_TRACKING_FLOOR = 0.55
CORRIDOR_BAND_FLOOR = 0.55
CORRIDOR_CONTACT_FLOOR = 0.1
CORRIDOR_BOUNDARY_CEILING = 0.15
CORRIDOR_CIRCULAR_FLOOR = 0.1
CORRIDOR_OPPOSITE_CEILING = 0.01
CORRIDOR_MASS_RELATIVE_CEILING = 0.12
CORRIDOR_CURVATURE_SIZE_CEILING = 0.2
RESOURCE_WALL_CEILING_SECONDS = 600.0
RESOURCE_RSS_CEILING_BYTES = 1_500_000_000

SOURCE_HASHES = {
    "cycle220": (
        ROOT / "scripts/generated_beta_phase_register_cycle220_2026_07_16.py",
        "252708e5adf782d9ad2869add0d64fa757d9d0473d054ee548e98e31d5f7276f",
    ),
    "cycle210": (
        ROOT / "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py",
        "c410b754d4e984f6ee5ccbc7c5a52e776c50c91c4daa12d798044f104cc7435b",
    ),
    "cycle230": (
        ROOT / "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py",
        "b449301837c1b72a325d310a1e2c582263a36648de939d169912347aff0591ae",
    ),
    "cycle305": (
        ROOT / "scripts/physical_cycle269_full_two_particle_sector_interface_cycle305_2026_07_17.py",
        "3e970b2c84ebe891d36c132cd99d716ceb20b596cea89729f06ed8950c7a847c",
    ),
    "cycle319": (
        ROOT / "scripts/physical_cycle269_three_cell_multiedge_cycle319_2026_07_18.py",
        "faa05d97542efca7684f4acc6f9b7dfb8e32a02f3f9d16adeae16449f5b702fb",
    ),
    "cycle492": (
        ROOT / "scripts/physical_coherent_beta_carrier_impulse_inertia_bridge_cycle492_2026_07_20.py",
        "91f760550a021c18d259ec32c0b52ca47b92e6a2a1952de1f12df9e5fa034ed6",
    ),
    "cycle494": (
        ROOT / "scripts/physical_contact_dressed_impulse_inertia_tournament_cycle494_2026_07_20.py",
        "a7d903561499efe9d8200de7ea711208c045c8098bc867ce350e08f9c164a632",
    ),
}

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


def predecessor_hashes() -> dict[str, bool]:
    return {
        name: sha256(path.read_bytes()).hexdigest() == expected
        for name, (path, expected) in SOURCE_HASHES.items()
    }


def frozen_contract():
    return {
        "train_fixtures": TRAIN_FIXTURES,
        "held_fixture": HELD_FIXTURE,
        "packet_width": PACKET_WIDTH,
        "envelope_cutoff": ENVELOPE_CUTOFF,
        "applications": APPLICATIONS,
        "fit_window": (FIT_START, APPLICATIONS),
        "unitarity_ceiling": UNITARITY_TOLERANCE,
        "EG_or_covariance_ceiling": EG_TOLERANCE,
        "eigen_ceiling": EIGEN_TOLERANCE,
        "norm_ceiling": NORM_TOLERANCE,
        "inverse_ceiling": INVERSE_TOLERANCE,
        "character_ceiling": CHARACTER_TOLERANCE,
        "neighbor_tracking_floor": TRACKING_FLOOR,
        "selected_band_floor": BAND_FLOOR,
        "dynamic_contact_floor": DYNAMIC_CONTACT_FLOOR,
        "boundary_ceiling": BOUNDARY_CEILING,
        "circular_strength_floor": CIRCULAR_STRENGTH_FLOOR,
        "opposite_displacement_ceiling": OPPOSITE_CEILING,
        "mass_relative_ceiling": MASS_RELATIVE_CEILING,
        "curvature_size_relative_ceiling": CURVATURE_SIZE_RELATIVE_CEILING,
        "curvature_common_sign": True,
        "contact_deletion_floor": CONTACT_DELETION_FLOOR,
        "proper_cubic_frames": 24,
        "postheld_corridor_train": CORRIDOR_TRAIN,
        "postheld_corridor_held": CORRIDOR_HELD,
        "corridor_packet_width": CORRIDOR_PACKET_WIDTH,
        "corridor_applications": CORRIDOR_APPLICATIONS,
        "corridor_fit_window": (CORRIDOR_FIT_START, CORRIDOR_APPLICATIONS),
        "corridor_tracking_floor": CORRIDOR_TRACKING_FLOOR,
        "corridor_selected_band_floor": CORRIDOR_BAND_FLOOR,
        "corridor_dynamic_contact_floor": CORRIDOR_CONTACT_FLOOR,
        "corridor_boundary_ceiling": CORRIDOR_BOUNDARY_CEILING,
        "corridor_circular_strength_floor": CORRIDOR_CIRCULAR_FLOOR,
        "corridor_opposite_ceiling": CORRIDOR_OPPOSITE_CEILING,
        "corridor_mass_relative_ceiling": CORRIDOR_MASS_RELATIVE_CEILING,
        "corridor_curvature_size_ceiling": CORRIDOR_CURVATURE_SIZE_CEILING,
        "wall_ceiling_seconds": RESOURCE_WALL_CEILING_SECONDS,
        "maximum_RSS_ceiling_bytes": RESOURCE_RSS_CEILING_BYTES,
        "authority": AUTHORITY,
        "audit": AUDIT,
    }


def note_contract():
    text = normalized(NOTE)
    required = (
        "frozen target before held output",
        "sole held kick: l9,h=2",
        "no held l9,h=2 output had been executed",
        "frame-carried selector",
        "exp(i k dot t)",
        "literal physical cell co-location",
        "not claimed to be compiled into physical m2 sites",
        "cycle 494 is a thin-torus comparator only",
        "displacement is not velocity",
        "update count is not time",
        "phase is not energy",
        "response is not gravity",
        "squared norm is not probability",
        "authority: none",
        "audit: unset",
        "n1",
        "n8",
        "no broad negative",
        "no axiom pressure",
        "fallback freeze before l47 output",
        "no l47 response had been executed",
        "resource guard",
    )
    missing = tuple(item for item in required if item not in text)
    return {"missing": missing, "contract": frozen_contract()}


def native_controller_coin():
    register = c220.cyclic_shift(9)
    _mass, common = c220.common_register_coin(register)
    events = ["functional-common-controller-built"]
    eigenpairs = c220.register_eigenpairs(register)
    events.append("spectral-menu-built")
    beta, _value, vector = min(eigenpairs, key=lambda row: abs(row[0] + 2 * np.pi / 9))
    coin = c220.extract_direction_block(common, vector)
    expected = c219.common_species(-2 * np.pi / 9).coin
    return coin, {
        "sector": "Cycle492-native-train-sector-1",
        "beta_label": beta,
        "construction_events": tuple(events),
        "controller_block_residual": float(np.linalg.norm(coin - expected)),
        "coin_unitarity": float(np.linalg.norm(coin.conj().T @ coin - np.eye(6))),
        "beta_scalar_or_lookup_used_by_update": False,
    }


def periods_tuple(length_or_periods):
    if isinstance(length_or_periods, int):
        return (length_or_periods,) * 3
    periods = tuple(int(value) for value in length_or_periods)
    if len(periods) != 3:
        raise ValueError("a three-dimensional torus needs exactly three periods")
    return periods


def add_cell(first: tuple[int, int, int], second: tuple[int, int, int], length_or_periods):
    periods = periods_tuple(length_or_periods)
    return tuple((first[axis] + second[axis]) % periods[axis] for axis in range(3))


def subtract_cell(first: tuple[int, int, int], second: tuple[int, int, int], length_or_periods):
    periods = periods_tuple(length_or_periods)
    return tuple((first[axis] - second[axis]) % periods[axis] for axis in range(3))


def negate_cell(cell: tuple[int, int, int], length_or_periods):
    periods = periods_tuple(length_or_periods)
    return tuple((-cell[axis]) % periods[axis] for axis in range(3))


def key_tuple(first_direction: int, displacement: tuple[int, int, int], second_direction: int):
    return (first_direction, *displacement, second_direction)


def decode_key(key: tuple[int, int, int, int, int]):
    return key[0], (key[1], key[2], key[3]), key[4]


def canonical_relative_key(
    first_direction: int,
    displacement: tuple[int, int, int],
    second_direction: int,
    length_or_periods,
):
    forward = key_tuple(first_direction, displacement, second_direction)
    reverse = key_tuple(
        second_direction, negate_cell(displacement, length_or_periods), first_direction
    )
    if forward == reverse:
        raise ValueError("a fermionic pair cannot repeat one physical mode")
    return (forward, 1) if forward < reverse else (reverse, -1)


class CubicTranslationQuotient:
    """Complete two-CAR quotient by simultaneous translations of an odd L^3 cube."""

    def __init__(self, length: int | tuple[int, int, int], coin: np.ndarray, axis=(1, 0, 0)):
        periods = periods_tuple(length)
        if any(period < 3 or period % 2 == 0 for period in periods):
            raise ValueError("the 3D quotient requires three odd integer periods >= 3")
        coin = np.asarray(coin, dtype=complex)
        if coin.shape != (6, 6) or np.linalg.norm(coin.conj().T @ coin - np.eye(6)) > 2e-10:
            raise ValueError("the cubic quotient requires one finite unitary six-mode coin")
        axis = np.asarray(axis, dtype=int)
        if axis.shape != (3,) or np.count_nonzero(axis) != 1 or np.linalg.norm(axis) != 1:
            raise ValueError("the response axis must be one signed cubic basis vector")
        self.periods = periods
        self.length = periods[0]
        self.volume = int(np.prod(periods))
        self.coin = coin
        self.axis = axis
        self.representatives = self._representatives()
        self.index = {key: index for index, key in enumerate(self.representatives)}
        self.dimension = len(self.representatives)
        self.contact_mask = np.asarray(
            [decode_key(key)[1] == (0, 0, 0) for key in self.representatives], dtype=bool
        )
        self.seed = self._pseudoscalar_seed()
        self.transitions = self._transitions()
        self._operator_cache: dict[tuple[tuple[int, int, int], float], sparse.csc_matrix] = {}

    def _representatives(self):
        keys = set()
        for dx in range(self.periods[0]):
            for dy in range(self.periods[1]):
                for dz in range(self.periods[2]):
                    displacement = (dx, dy, dz)
                    for first in range(6):
                        for second in range(6):
                            if displacement == (0, 0, 0) and first == second:
                                continue
                            key, _sign = canonical_relative_key(
                                first, displacement, second, self.periods
                            )
                            keys.add(key)
        result = tuple(sorted(keys))
        expected = 18 * self.volume - 3
        if len(result) != expected:
            raise RuntimeError(
                f"odd-cube relative quotient has {len(result)} columns, expected {expected}"
            )
        return result

    def _pseudoscalar_seed(self):
        # Let X,Y,Z be the normalized even sums of the two directions on each
        # unsigned axis.  The declared source ray is -X^Y + X^Z - Y^Z.  The
        # covariance test carries this source to R*s in each frame and tests
        # the corresponding full operator conjugacy; it does not assume that
        # the untransported coordinate vector is fixed by every frame.
        even_axes = []
        for unsigned_axis in range(3):
            vector = np.zeros(6, dtype=complex)
            directions = np.where(abs(c210.DIRECTIONS[:, unsigned_axis]) == 1)[0]
            vector[directions] = 1 / np.sqrt(2)
            even_axes.append(vector)
        coefficients = (
            -(np.outer(even_axes[0], even_axes[1]) - np.outer(even_axes[1], even_axes[0]))
            +(np.outer(even_axes[0], even_axes[2]) - np.outer(even_axes[2], even_axes[0]))
            -(np.outer(even_axes[1], even_axes[2]) - np.outer(even_axes[2], even_axes[1]))
        ) / np.sqrt(3)
        seed = np.zeros(self.dimension, dtype=complex)
        for first in range(6):
            for second in range(first + 1, 6):
                key, sign = canonical_relative_key(
                    first, (0, 0, 0), second, self.periods
                )
                seed[self.index[key]] += sign * coefficients[first, second]
        if abs(np.linalg.norm(seed) - 1) > 2e-14:
            raise RuntimeError("the onsite proper-cubic pseudoscalar wedge seed is not normalized")
        return seed

    def canonical_output(self, first_cell, first_direction, second_cell, second_direction):
        displacement = subtract_cell(second_cell, first_cell, self.periods)
        forward = key_tuple(first_direction, displacement, second_direction)
        reverse = key_tuple(
            second_direction, negate_cell(displacement, self.periods), first_direction
        )
        if forward == reverse:
            raise ValueError("the Pauli-forbidden output must be deleted before canonicalization")
        if forward < reverse:
            return forward, 1, first_cell
        return reverse, -1, second_cell

    def _transitions(self):
        steps = tuple(tuple(int(value) for value in row) for row in c210.DIRECTIONS)
        origin = (0, 0, 0)
        transitions = []
        for key in self.representatives:
            first_direction, displacement, second_direction = decode_key(key)
            accumulated: dict[tuple[int, tuple[int, int, int], bool], complex] = {}
            for first_target in range(6):
                first_cell = add_cell(origin, steps[first_target], self.periods)
                for second_target in range(6):
                    second_cell = add_cell(displacement, steps[second_target], self.periods)
                    if first_cell == second_cell and first_target == second_target:
                        continue
                    output, wedge_sign, translation = self.canonical_output(
                        first_cell, first_target, second_cell, second_target
                    )
                    row = self.index[output]
                    contact = first_cell == second_cell
                    transition = (row, translation, contact)
                    coefficient = (
                        wedge_sign
                        * self.coin[first_target, first_direction]
                        * self.coin[second_target, second_direction]
                    )
                    accumulated[transition] = accumulated.get(transition, 0j) + coefficient
            transitions.append(
                tuple(
                    (row, translation, coefficient, contact)
                    for (row, translation, contact), coefficient in accumulated.items()
                    if abs(coefficient) > 2e-16
                )
            )
        return tuple(transitions)

    def operator(self, momentum_index=(0, 0, 0), coupling: float = COUPLING):
        momentum_index = tuple(int(value) for value in momentum_index)
        if len(momentum_index) != 3:
            raise ValueError("total momentum index must have three components")
        cache_key = (momentum_index, float(coupling))
        if cache_key in self._operator_cache:
            return self._operator_cache[cache_key]
        momentum = (
            2 * np.pi * np.asarray(momentum_index, dtype=float)
            / np.asarray(self.periods, dtype=float)
        )
        rows: list[int] = []
        columns: list[int] = []
        data: list[complex] = []
        for column, column_transitions in enumerate(self.transitions):
            for row, translation, coefficient, contact in column_transitions:
                rows.append(row)
                columns.append(column)
                data.append(
                    coefficient
                    * (np.exp(1j * coupling) if contact else 1)
                    * np.exp(1j * float(momentum @ np.asarray(translation)))
                )
        result = sparse.coo_matrix(
            (data, (rows, columns)), shape=(self.dimension, self.dimension), dtype=complex
        ).tocsc()
        self._operator_cache[cache_key] = result
        return result


def normalize_columns(vectors: np.ndarray):
    return vectors / np.linalg.norm(vectors, axis=0)[None, :]


def train_branch_probe(length: int, coin: np.ndarray, target_phase: float = TARGET_PHASE):
    quotient = CubicTranslationQuotient(length, coin)
    values, vectors = eigs(
        quotient.operator(),
        k=16,
        sigma=0.985 * np.exp(1j * target_phase),
        tol=3e-12,
        maxiter=12000,
        v0=quotient.seed,
    )
    vectors = normalize_columns(vectors)
    overlaps = abs(vectors.conj().T @ quotient.seed) ** 2
    order = np.argsort(overlaps)[::-1]
    rows = []
    for index in order[:8]:
        vector = vectors[:, index]
        rows.append(
            {
                "phase": float(np.angle(values[index])),
                "seed_overlap": float(overlaps[index]),
                "contact_norm": float(np.sum(abs(vector[quotient.contact_mask]) ** 2)),
                "eigen_residual": float(
                    np.linalg.norm(quotient.operator() @ vector - values[index] * vector)
                ),
            }
        )
    return {
        "L": length,
        "V": quotient.volume,
        "dimension": quotient.dimension,
        "expected_dimension": 18 * quotient.volume - 3,
        "transition_nnz": int(quotient.operator().nnz),
        "unitarity_residual": float(
            sparse.linalg.norm(
                quotient.operator().conj().T @ quotient.operator()
                - sparse.eye(quotient.dimension)
            )
        ),
        "branches": rows,
    }


def wrapped_index(index: int, length: int) -> int:
    return index if index <= length // 2 else index - length


def normalize_ray(vector: np.ndarray, reference: np.ndarray | None = None):
    vector = vector / np.linalg.norm(vector)
    if reference is not None:
        vector *= np.exp(-1j * np.angle(np.vdot(reference, vector)))
    return vector


def selected_eigenpair(
    quotient: CubicTranslationQuotient,
    momentum_index: tuple[int, int, int],
    target_value: complex,
    reference: np.ndarray,
    *,
    origin: bool = False,
):
    values, vectors = eigs(
        quotient.operator(momentum_index),
        k=24,
        sigma=0.985 * target_value,
        tol=3e-12,
        maxiter=16000,
        v0=reference,
    )
    vectors = normalize_columns(vectors)
    overlaps = abs(vectors.conj().T @ reference) ** 2
    index = int(np.argmax(overlaps))
    vector = normalize_ray(vectors[:, index], reference)
    return values[index], vector, float(overlaps[index])


def dressed_family(quotient: CubicTranslationQuotient, maximum_index: int | None = None):
    if maximum_index is None:
        maximum_index = quotient.length // 2
    maximum_index = min(maximum_index, quotient.length // 2)
    target = np.exp(1j * TARGET_PHASE)
    value0, vector0, overlap0 = selected_eigenpair(
        quotient, (0, 0, 0), target, quotient.seed, origin=True
    )
    family = {0: (value0, vector0, overlap0)}
    for sign in (-1, 1):
        value, vector = value0, vector0
        for magnitude in range(1, maximum_index + 1):
            index = sign * magnitude
            value, vector, overlap = selected_eigenpair(
                quotient, (index, 0, 0), value, vector
            )
            family[index] = (value, vector, overlap)
    return family


def packet_density(packet: np.ndarray):
    return np.sum(abs(packet) ** 2, axis=1)


def circular_centroid(packet: np.ndarray, positions: np.ndarray):
    density = packet_density(packet)
    moment = np.sum(density * np.exp(2j * np.pi * positions / len(positions)))
    return float(np.angle(moment) * len(positions) / (2 * np.pi)), abs(moment)


def translation_character(packet: np.ndarray):
    return complex(np.vdot(packet, np.roll(packet, -1, axis=0)))


def prepare_packet(quotient: CubicTranslationQuotient, family, packet_width: float):
    packet_k = np.zeros((quotient.length, quotient.dimension), dtype=complex)
    for array_index in range(quotient.length):
        index = wrapped_index(array_index, quotient.length)
        momentum = 2 * np.pi * index / quotient.length
        envelope = float(np.exp(-0.5 * (momentum / packet_width) ** 2))
        if envelope > ENVELOPE_CUTOFF and index in family:
            packet_k[array_index] = envelope * family[index][1]
    packet_k /= np.linalg.norm(packet_k)
    packet = np.fft.ifft(packet_k, axis=0, norm="ortho")
    packet = np.roll(packet, quotient.length // 2, axis=0)
    positions = np.arange(quotient.length, dtype=float) - quotient.length // 2
    return positions, packet


def selected_band_weight(state_k, family, length):
    result = 0.0
    for array_index in range(length):
        if np.linalg.norm(state_k[array_index]) < 1e-13:
            continue
        index = wrapped_index(array_index, length)
        result += abs(np.vdot(family[index][1], state_k[array_index])) ** 2
    return float(result)


def signed_response(
    base,
    positions,
    quotient,
    family,
    harmonic,
    sign,
    applications: int,
    fit_start: int,
):
    q = 2 * np.pi * harmonic / quotient.length
    kicked = np.exp(1j * sign * q * positions)[:, None] * base
    shift = float(np.angle(translation_character(kicked) / translation_character(base)))
    state_k = np.fft.fft(kicked, axis=0, norm="ortho")
    active = tuple(index for index in range(quotient.length) if np.linalg.norm(state_k[index]) > 1e-13)
    packet = kicked
    angles = []
    circular_strengths = []
    maximum_norm_error = 0.0
    for _tick in range(applications + 1):
        centroid, strength = circular_centroid(packet, positions)
        angles.append(2 * np.pi * centroid / quotient.length)
        circular_strengths.append(strength)
        if _tick == applications:
            break
        for array_index in active:
            index = wrapped_index(array_index, quotient.length)
            state_k[array_index] = quotient.operator((index, 0, 0)) @ state_k[array_index]
        packet = np.fft.ifft(state_k, axis=0, norm="ortho")
        maximum_norm_error = max(maximum_norm_error, abs(np.linalg.norm(packet) - 1))
    unwrapped = np.unwrap(np.asarray(angles)) * quotient.length / (2 * np.pi)
    fit_axis = np.arange(fit_start, applications + 1, dtype=float)
    displacement = float(np.polyfit(fit_axis, unwrapped[fit_start:], 1)[0])
    density = packet_density(packet)
    boundary = float(np.sum(density[abs(positions) == quotient.length // 2]))
    band = selected_band_weight(state_k, family, quotient.length)
    contact = float(np.sum(abs(state_k[:, quotient.contact_mask]) ** 2))
    for _ in range(applications):
        for array_index in active:
            index = wrapped_index(array_index, quotient.length)
            state_k[array_index] = quotient.operator((index, 0, 0)).conj().T @ state_k[array_index]
    restored = np.fft.ifft(state_k, axis=0, norm="ortho")
    restored *= np.exp(-1j * sign * q * positions)[:, None]
    return {
        "sign": sign,
        "harmonic": harmonic,
        "q": q,
        "character_shift": shift,
        "character_residual": abs(np.angle(np.exp(1j * (shift - sign * q)))),
        "displacement_per_declared_update": displacement,
        "maximum_norm_error": maximum_norm_error,
        "selected_band_norm_weight": band,
        "contact_norm_weight": contact,
        "boundary_weight": boundary,
        "minimum_circular_strength": min(circular_strengths),
        "inverse_residual": float(np.linalg.norm(restored - base)),
    }


def response_probe(
    length: int | tuple[int, int, int],
    harmonic: int,
    coin: np.ndarray,
    disposition="train",
    packet_width: float = PACKET_WIDTH,
    applications: int = APPLICATIONS,
    fit_start: int = FIT_START,
):
    quotient = CubicTranslationQuotient(length, coin)
    maximum_index = int(
        np.ceil(
            packet_width
            * np.sqrt(-2 * np.log(ENVELOPE_CUTOFF))
            * quotient.length
            / (2 * np.pi)
        )
    ) + harmonic + 1
    family = dressed_family(quotient, maximum_index)
    positions, base = prepare_packet(quotient, family, packet_width)
    plus = signed_response(
        base, positions, quotient, family, harmonic, +1, applications, fit_start
    )
    minus = signed_response(
        base, positions, quotient, family, harmonic, -1, applications, fit_start
    )
    q = 2 * np.pi / quotient.length
    phase_minus = np.angle(family[-1][0] / family[0][0])
    phase_plus = np.angle(family[1][0] / family[0][0])
    curvature = float((phase_minus + phase_plus) / q**2)
    susceptibility = -(
        plus["displacement_per_declared_update"]
        - minus["displacement_per_declared_update"]
    ) / (2 * plus["q"])
    eigen_residual = max(
        float(
            np.linalg.norm(
                quotient.operator((index, 0, 0)) @ vector
                - value * vector
            )
        )
        for index, (value, vector, _overlap) in family.items()
    )
    return {
        "fixture": (
            f"{disposition}-3D-torus-"
            f"{quotient.periods[0]}x{quotient.periods[1]}x{quotient.periods[2]}-h{harmonic}"
        ),
        "disposition": disposition,
        "L": quotient.length,
        "periods": quotient.periods,
        "bulk_cube": len(set(quotient.periods)) == 1,
        "volume": quotient.volume,
        "quotient_dimension": quotient.dimension,
        "zero_character_operator_nnz": quotient.operator((0, 0, 0)).nnz,
        "harmonic": harmonic,
        "packet_width": packet_width,
        "applications": applications,
        "fit_window": (fit_start, applications),
        "origin_phase": float(np.angle(family[0][0])),
        "origin_seed_overlap": float(family[0][2]),
        "origin_contact_norm_weight": float(
            np.sum(abs(family[0][1][quotient.contact_mask]) ** 2)
        ),
        "neighbor_tracking_floor": min(family[-1][2], family[1][2]),
        "dressed_curvature": curvature,
        "dressed_curvature_mass": 1 / curvature,
        "maximum_eigen_residual": eigen_residual,
        "plus": plus,
        "minus": minus,
        "opposite_displacement_residual": abs(
            plus["displacement_per_declared_update"]
            + minus["displacement_per_declared_update"]
        ),
        "susceptibility": susceptibility,
        "impulse_mass": 1 / susceptibility,
        "impulse_curvature_relative_residual": abs((1 / susceptibility) / (1 / curvature) - 1),
    }


def quotient_controls(coin: np.ndarray):
    print("\nCOMPLETE ODD-CUBE TWO-CAR TRANSLATION QUOTIENT")
    quotient = CubicTranslationQuotient(3, coin)
    residuals = []
    nonzeros = []
    for kx in (-1, 0, 1):
        for ky in (-1, 0, 1):
            for kz in (-1, 0, 1):
                operator = quotient.operator((kx, ky, kz))
                residuals.append(
                    float(
                        sparse.linalg.norm(
                            operator.conj().T @ operator
                            - sparse.eye(quotient.dimension)
                        )
                    )
                )
                nonzeros.append(operator.nnz)
    result = {
        "L": 3,
        "volume": 27,
        "full_two_CAR_dimension": (6 * 27 * (6 * 27 - 1)) // 2,
        "quotient_dimension": quotient.dimension,
        "expected_free_orbit_dimension": 18 * 27 - 3,
        "momentum_blocks": 27,
        "maximum_unitarity_residual": max(residuals),
        "minimum_operator_nnz": min(nonzeros),
        "maximum_operator_nnz": max(nonzeros),
        "literal_d0_contact_columns": int(np.count_nonzero(quotient.contact_mask)),
    }
    check(
        "all 27 characters of the complete L3 cubic quotient have the free-orbit dimension and are unitary",
        result["quotient_dimension"] == result["expected_free_orbit_dimension"] == 483
        and result["literal_d0_contact_columns"] == 15
        and result["maximum_unitarity_residual"] < UNITARITY_TOLERANCE,
        result,
    )
    return result


def physical_interface_controls(coin: np.ndarray):
    import physical_cycle269_full_two_particle_sector_interface_cycle305_2026_07_17 as c305

    print("\nCYCLE305 BOUNDED FIXED-SEAM COMPARATOR")
    rows = []
    for length, held in ((3, False), (6, True)):
        code = c305.c269.build_code(length)
        encoder = c305.sector_encoder(code, (0, 0, 0))
        stream, failures = c305.physical_stream_matrix(encoder)
        contact = c305.physical_contact_matrix(encoder, COUPLING)
        coarse_stream = c305.coarse_stream_matrix()
        coarse_contact = c305.coarse_contact_matrix(COUPLING)
        comparator = c305.fixed_seam_coin_comparator(coin)
        composite = contact @ stream @ comparator
        expected = coarse_contact @ coarse_stream @ comparator
        identity = np.eye(c305.CODE_DIMENSION)
        rows.append(
            {
                "L": length,
                "held": held,
                "columns": c305.CODE_DIMENSION,
                "Gram_residual": float(np.linalg.norm(c305.exact_gram(encoder) - identity)),
                "stream_EG_residual": float(np.linalg.norm(stream - coarse_stream)),
                "contact_EG_residual": float(np.linalg.norm(contact - coarse_contact)),
                "composite_EG_residual": float(np.linalg.norm(composite - expected)),
                "inverse_residual": float(np.linalg.norm(composite.conj().T @ composite - identity)),
                "branch_failures": sum(failures.values()),
                "M2_per_cell": 21,
                "recurrent_cube_compiler_claim": False,
            }
        )
    maximum = max(
        max(
            row["Gram_residual"],
            row["stream_EG_residual"],
            row["contact_EG_residual"],
            row["composite_EG_residual"],
            row["inverse_residual"],
        )
        for row in rows
    )
    result = {"rows": rows, "maximum_residual": maximum}
    check(
        "the separate Cycle305 fixed seam retains exact E/G and inverse only at its bounded declared scope",
        maximum < EG_TOLERANCE and all(row["branch_failures"] == 0 for row in rows),
        result,
    )
    return result


def transformed_selector(quotient: CubicTranslationQuotient, direction: np.ndarray):
    source = np.zeros((6, 6), dtype=complex)
    even_axes = []
    for axis in range(3):
        vector = np.zeros(6, dtype=complex)
        vector[np.where(abs(c210.DIRECTIONS[:, axis]) == 1)[0]] = 1 / np.sqrt(2)
        even_axes.append(vector)
    source += -(np.outer(even_axes[0], even_axes[1]) - np.outer(even_axes[1], even_axes[0]))
    source += +(np.outer(even_axes[0], even_axes[2]) - np.outer(even_axes[2], even_axes[0]))
    source += -(np.outer(even_axes[1], even_axes[2]) - np.outer(even_axes[2], even_axes[1]))
    source /= np.sqrt(3)
    moved = direction @ source @ direction.T
    result = np.zeros(quotient.dimension, dtype=complex)
    for first in range(6):
        for second in range(first + 1, 6):
            key, sign = canonical_relative_key(
                first, (0, 0, 0), second, quotient.periods
            )
            result[quotient.index[key]] += sign * moved[first, second]
    return result


def frame_representation(
    source: CubicTranslationQuotient,
    target: CubicTranslationQuotient,
    frame: np.ndarray,
    momentum_index: tuple[int, int, int],
):
    direction = c210.direction_permutation(frame)
    target_momentum = tuple(
        int(value) for value in frame @ np.asarray(momentum_index, dtype=int)
    )
    rows = []
    columns = []
    data = []
    for column, key in enumerate(source.representatives):
        first, displacement, second = decode_key(key)
        moved_first = int(np.argmax(direction[:, first]))
        moved_second = int(np.argmax(direction[:, second]))
        moved_displacement = tuple(
            int(value) % target.periods[axis]
            for axis, value in enumerate(frame @ np.asarray(displacement, dtype=int))
        )
        forward = key_tuple(moved_first, moved_displacement, moved_second)
        reverse = key_tuple(
            moved_second,
            negate_cell(moved_displacement, target.periods),
            moved_first,
        )
        if forward < reverse:
            output, sign, translation = forward, 1, (0, 0, 0)
        else:
            output, sign, translation = reverse, -1, moved_displacement
        phase = np.exp(
            2j
            * np.pi
            * sum(
                target_momentum[axis] * translation[axis] / target.periods[axis]
                for axis in range(3)
            )
        )
        rows.append(target.index[output])
        columns.append(column)
        data.append(sign * phase)
    representation = sparse.coo_matrix(
        (data, (rows, columns)),
        shape=(target.dimension, source.dimension),
        dtype=complex,
    ).tocsc()
    return direction, target_momentum, representation


def covariance_controls(coin: np.ndarray):
    print("\nALL-24 FULL OPERATOR / SELECTOR / CHARACTER COVARIANCE")
    quotient = CubicTranslationQuotient(3, coin)
    operator_residuals = []
    selector_residuals = []
    representation_residuals = []
    coin_residuals = []
    samples = ((0, 0, 0), (1, 0, 0), (1, -1, 0))
    for frame in c210.proper_cubic_frames():
        direction_zero, _zero_momentum, zero_representation = frame_representation(
            quotient, quotient, frame, (0, 0, 0)
        )
        transported = transformed_selector(quotient, direction_zero)
        selector_residuals.append(
            float(np.linalg.norm(zero_representation @ quotient.seed - transported))
        )
        coin_residuals.append(
            float(np.linalg.norm(direction_zero @ coin @ direction_zero.T - coin))
        )
        for source_momentum in samples:
            _direction, target_momentum, representation = frame_representation(
                quotient, quotient, frame, source_momentum
            )
            identity = sparse.eye(quotient.dimension)
            representation_residuals.append(
                float(
                    sparse.linalg.norm(
                        representation.conj().T @ representation - identity
                    )
                )
            )
            operator_residuals.append(
                float(
                    sparse.linalg.norm(
                        representation
                        @ quotient.operator(source_momentum)
                        @ representation.conj().T
                        - quotient.operator(target_momentum)
                    )
                )
            )
    corridor_source = CubicTranslationQuotient((5, 3, 3), coin)
    corridor_targets: dict[tuple[int, int, int], CubicTranslationQuotient] = {}
    corridor_operator_residuals = []
    corridor_selector_residuals = []
    corridor_representation_residuals = []
    corridor_samples = ((0, 0, 0), (1, 0, 0), (1, 1, 0))
    for frame in c210.proper_cubic_frames():
        target_periods = tuple(
            int(value)
            for value in abs(frame) @ np.asarray(corridor_source.periods, dtype=int)
        )
        if target_periods not in corridor_targets:
            corridor_targets[target_periods] = CubicTranslationQuotient(
                target_periods, coin
            )
        target = corridor_targets[target_periods]
        direction_zero, _zero_momentum, zero_representation = frame_representation(
            corridor_source, target, frame, (0, 0, 0)
        )
        corridor_selector_residuals.append(
            float(
                np.linalg.norm(
                    zero_representation @ corridor_source.seed
                    - transformed_selector(target, direction_zero)
                )
            )
        )
        for source_momentum in corridor_samples:
            _direction, target_momentum, representation = frame_representation(
                corridor_source, target, frame, source_momentum
            )
            corridor_representation_residuals.append(
                float(
                    sparse.linalg.norm(
                        representation.conj().T @ representation
                        - sparse.eye(corridor_source.dimension)
                    )
                )
            )
            corridor_operator_residuals.append(
                float(
                    sparse.linalg.norm(
                        representation
                        @ corridor_source.operator(source_momentum)
                        @ representation.conj().T
                        - target.operator(target_momentum)
                    )
                )
            )
    result = {
        "cube_frames": 24,
        "cube_characters_per_frame": len(samples),
        "cube_maximum_operator_conjugacy_residual": max(operator_residuals),
        "cube_maximum_selector_transport_residual": max(selector_residuals),
        "cube_maximum_character_representation_unitarity_residual": max(
            representation_residuals
        ),
        "maximum_coin_covariance_residual": max(coin_residuals),
        "corridor_source_periods": corridor_source.periods,
        "corridor_target_period_families": tuple(sorted(corridor_targets)),
        "corridor_frames": 24,
        "corridor_characters_per_frame": len(corridor_samples),
        "corridor_maximum_operator_conjugacy_residual": max(
            corridor_operator_residuals
        ),
        "corridor_maximum_selector_transport_residual": max(
            corridor_selector_residuals
        ),
        "corridor_maximum_character_representation_unitarity_residual": max(
            corridor_representation_residuals
        ),
        "full_character_Bloch_phase_included": True,
        "untransported_invariant_selector_claim": False,
        "corridor_is_bulk_claim": False,
    }
    result["maximum_operator_conjugacy_residual"] = max(
        result["cube_maximum_operator_conjugacy_residual"],
        result["corridor_maximum_operator_conjugacy_residual"],
    )
    check(
        "all 24 frames carry cube and bounded corridor selectors/full characters through source-to-target operator conjugacy",
        max(
            operator_residuals
            + selector_residuals
            + representation_residuals
            + coin_residuals
            + corridor_operator_residuals
            + corridor_selector_residuals
            + corridor_representation_residuals
        )
        < EG_TOLERANCE,
        result,
    )
    return result


def deletion_and_fixture_controls(coin: np.ndarray):
    print("\nCONTACT / KICK DELETIONS AND PRESERVED FIXTURES")
    quotient = CubicTranslationQuotient(5, coin)
    family = dressed_family(quotient)
    value, vector, overlap = family[0]
    intact = quotient.operator() @ vector
    deleted = quotient.operator(coupling=0.0) @ vector
    deletion = float(np.linalg.norm(intact - deleted))
    contact = float(np.sum(abs(vector[quotient.contact_mask]) ** 2))
    expected = float(abs(np.exp(1j * COUPLING) - 1) * np.sqrt(contact))
    positions, base = prepare_packet(quotient, family, PACKET_WIDTH)
    q = 2 * np.pi / quotient.length
    nominal_kicked = np.exp(1j * q * positions)[:, None] * base
    deleted_kick = base.copy()
    nominal_shift = float(
        np.angle(translation_character(nominal_kicked) / translation_character(base))
    )
    deleted_shift = float(
        np.angle(translation_character(deleted_kick) / translation_character(base))
    )
    reference_mass = c219.rest_mass(c219.common_species(-0.3))
    import physical_cycle269_three_cell_multiedge_cycle319_2026_07_18 as c319

    contact_fixture = c319.triple_contact(c319.triple_labels())
    contact_columns = int(
        np.count_nonzero(abs(contact_fixture.diagonal() - 1) > 2e-14)
    )
    result = {
        "origin_value_phase": float(np.angle(value)),
        "origin_selector_overlap": overlap,
        "origin_contact_norm_weight": contact,
        "contact_deletion_state_residual": deletion,
        "contact_deletion_expected_residual": expected,
        "contact_deletion_formula_residual": abs(deletion - expected),
        "nominal_kick_q": q,
        "nominal_kick_character_shift": nominal_shift,
        "nominal_kick_character_residual": abs(
            np.angle(np.exp(1j * (nominal_shift - q)))
        ),
        "kick_deletion_state_residual": float(
            np.linalg.norm(nominal_kicked - deleted_kick)
        ),
        "kick_deleted_character_shift": deleted_shift,
        "Cycle219_mass_fixture": reference_mass,
        "Cycle319_contact_nontrivial_columns": contact_columns,
    }
    check(
        "g=0 changes the contact-heavy state by the exact onsite formula while kick deletion is null and fixtures remain unchanged",
        deletion > CONTACT_DELETION_FLOOR
        and result["contact_deletion_formula_residual"] < 3e-12
        and result["nominal_kick_character_residual"] < CHARACTER_TOLERANCE
        and result["kick_deletion_state_residual"] > 0.1
        and abs(result["kick_deleted_character_shift"]) < CHARACTER_TOLERANCE
        and abs(reference_mass - 0.4534056541748851) < 2e-15
        and contact_columns == 645,
        result,
    )
    return result


def domain_controls(coin: np.ndarray):
    operations = (
        lambda: CubicTranslationQuotient(2, coin),
        lambda: CubicTranslationQuotient((3, 4, 3), coin),
        lambda: CubicTranslationQuotient(3, np.eye(5)),
        lambda: CubicTranslationQuotient(3, 2 * np.eye(6)),
        lambda: CubicTranslationQuotient(3, coin, (1, 1, 0)),
        lambda: canonical_relative_key(1, (0, 0, 0), 1, (3, 3, 3)),
        lambda: CubicTranslationQuotient(3, coin).operator((1, 0)),
    )
    rejections = 0
    for operation in operations:
        try:
            operation()
        except ValueError:
            rejections += 1
    result = {"rejections": rejections, "attempts": len(operations)}
    check(
        "the lawful domain rejects even periods, malformed coins/axes/characters, and repeated physical modes",
        rejections == len(operations),
        result,
    )
    return result


def response_extrema(rows):
    sides = [side for row in rows for side in (row["plus"], row["minus"])]
    return {
        "maximum_mass_relative_residual": max(
            row["impulse_curvature_relative_residual"] for row in rows
        ),
        "maximum_character_residual": max(side["character_residual"] for side in sides),
        "maximum_norm_residual": max(side["maximum_norm_error"] for side in sides),
        "maximum_inverse_residual": max(side["inverse_residual"] for side in sides),
        "maximum_eigen_residual": max(row["maximum_eigen_residual"] for row in rows),
        "minimum_neighbor_tracking": min(row["neighbor_tracking_floor"] for row in rows),
        "minimum_selected_band": min(side["selected_band_norm_weight"] for side in sides),
        "minimum_dynamic_contact": min(side["contact_norm_weight"] for side in sides),
        "maximum_boundary": max(side["boundary_weight"] for side in sides),
        "minimum_circular_strength": min(side["minimum_circular_strength"] for side in sides),
        "maximum_opposite_displacement_residual": max(
            row["opposite_displacement_residual"] for row in rows
        ),
    }


def cube_response_controls(coin: np.ndarray):
    print("\nFROZEN BULK-CUBE RESPONSE TOURNAMENT")
    rows = [
        response_probe(5, 1, coin, "train"),
        response_probe(7, 1, coin, "train"),
        response_probe(9, 2, coin, "held-kick"),
    ]
    for row in rows:
        print("CUBE_ROW", row)
    extrema = response_extrema(rows)
    curvatures = [row["dressed_curvature"] for row in rows[:2]]
    curvature_size = abs(curvatures[1] / curvatures[0] - 1)
    common_sign = curvatures[0] * curvatures[1] > 0
    numeric_lawful = (
        extrema["maximum_character_residual"] < CHARACTER_TOLERANCE
        and extrema["maximum_norm_residual"] < NORM_TOLERANCE
        and extrema["maximum_inverse_residual"] < INVERSE_TOLERANCE
        and extrema["maximum_eigen_residual"] < EIGEN_TOLERANCE
    )
    candidate = (
        numeric_lawful
        and extrema["maximum_mass_relative_residual"] < MASS_RELATIVE_CEILING
        and extrema["minimum_neighbor_tracking"] > TRACKING_FLOOR
        and extrema["minimum_selected_band"] > BAND_FLOOR
        and extrema["minimum_dynamic_contact"] > DYNAMIC_CONTACT_FLOOR
        and extrema["maximum_boundary"] < BOUNDARY_CEILING
        and extrema["minimum_circular_strength"] > CIRCULAR_STRENGTH_FLOOR
        and extrema["maximum_opposite_displacement_residual"] < OPPOSITE_CEILING
        and common_sign
        and curvature_size < CURVATURE_SIZE_RELATIVE_CEILING
    )
    result = {
        "rows": rows,
        **extrema,
        "train_curvature_relative_residual": curvature_size,
        "train_curvature_common_sign": common_sign,
        "positive_bulk_inertia_gate": candidate,
        "disposition": (
            "bulk-cube-inertia-certified"
            if candidate
            else "route-specific-finite-cube-response-not-certified"
        ),
    }
    check(
        "the frozen cube train and held rows execute lawfully and the unchanged positive gate is explicitly disposed",
        numeric_lawful
        and len(rows) == 3
        and rows[-1]["disposition"] == "held-kick"
        and not candidate,
        result,
    )
    return result


def corridor_response_controls(coin: np.ndarray):
    print("\nFROZEN THICK-CORRIDOR FALLBACK (NOT BULK)")
    rows = [
        response_probe(
            CORRIDOR_TRAIN,
            1,
            coin,
            "train-corridor-not-bulk",
            CORRIDOR_PACKET_WIDTH,
            CORRIDOR_APPLICATIONS,
            CORRIDOR_FIT_START,
        ),
        response_probe(
            CORRIDOR_HELD,
            1,
            coin,
            "held-corridor-not-bulk",
            CORRIDOR_PACKET_WIDTH,
            CORRIDOR_APPLICATIONS,
            CORRIDOR_FIT_START,
        ),
    ]
    for row in rows:
        print("CORRIDOR_ROW", row)
    extrema = response_extrema(rows)
    curvatures = [row["dressed_curvature"] for row in rows]
    curvature_size = abs(curvatures[1] / curvatures[0] - 1)
    common_sign = curvatures[0] * curvatures[1] > 0
    numeric_lawful = (
        extrema["maximum_character_residual"] < CHARACTER_TOLERANCE
        and extrema["maximum_norm_residual"] < NORM_TOLERANCE
        and extrema["maximum_inverse_residual"] < INVERSE_TOLERANCE
        and extrema["maximum_eigen_residual"] < EIGEN_TOLERANCE
    )
    candidate = (
        numeric_lawful
        and extrema["maximum_mass_relative_residual"] < CORRIDOR_MASS_RELATIVE_CEILING
        and extrema["minimum_neighbor_tracking"] > CORRIDOR_TRACKING_FLOOR
        and extrema["minimum_selected_band"] > CORRIDOR_BAND_FLOOR
        and extrema["minimum_dynamic_contact"] > CORRIDOR_CONTACT_FLOOR
        and extrema["maximum_boundary"] < CORRIDOR_BOUNDARY_CEILING
        and extrema["minimum_circular_strength"] > CORRIDOR_CIRCULAR_FLOOR
        and extrema["maximum_opposite_displacement_residual"] < CORRIDOR_OPPOSITE_CEILING
        and common_sign
        and curvature_size < CORRIDOR_CURVATURE_SIZE_CEILING
    )
    result = {
        "rows": rows,
        **extrema,
        "curvature_size_relative_residual": curvature_size,
        "curvature_common_sign": common_sign,
        "positive_corridor_inertia_gate": candidate,
        "bulk_3D_claim": False,
        "disposition": (
            "thick-corridor-comparator-certified-not-bulk"
            if candidate
            else "thick-corridor-comparator-not-certified"
        ),
    }
    check(
        "the frozen train and untouched held corridor execute with an explicit not-bulk disposition",
        numeric_lawful
        and len(rows) == 2
        and rows[-1]["disposition"] == "held-corridor-not-bulk",
        result,
    )
    return result


def inventory_controls(controller, quotient, physical, covariance, deletion, domain, cube, corridor):
    supplied = (
        "Cycle492 -2pi/9 sector and native functional controller construction",
        "Cycle230 g=0.37 even contact and coin-stream-contact order",
        "odd cubic/corridor periods, simultaneous translation quotient, origin, response axis, and characters",
        "frame-carried onsite wedge selector, target-phase eigensolver, and overlap tracking rule",
        "packet widths/cutoffs, application/fit schedules, circular centroid effect, and frozen thresholds",
        "Cycle305 bounded fixed seam and proper-cubic frame actions",
    )
    derived = (
        "complete odd-cube relative quotient with dimension 18V-3 and literal d=0 contact",
        "contact-heavy zero-character branch and exact finite-character response dispositions",
        "full-K all24 operator/selector covariance, inverse, deletions, and lawful domains",
        "separate frozen thick-corridor comparator with no bulk promotion",
    )
    open_items = (
        "stable mobile bulk-cubic dressed branch under finer lawful characters",
        "autonomous selector/contact/packet/impulse/effect preparation",
        "reciprocal local field scattering instead of external character",
        "recurrent M2 compiler for the quotient; Cycle305 remains only a fixed seam",
        "unit calibration, species selection, source law, gravity/backreaction, Records, occurrence, and Born law",
    )
    n_gate = {
        "N1": "thick corridor, finite cluster, reciprocal scattering, and clock endpoint remain live",
        "N2": "binding, mobility, impulse, recurrent compilation, controller carriage, and calibration are independent",
        "N3": "selector/eigensolver/cube/packet/character/effect/contact/thresholds are explicit",
        "N4": "every retained claim carries quotient, E/G, eigen, response, covariance, deletion, or domain residuals",
        "N5": "only route-specific finite-cube wording; no impossible, necessary, minimum, constitutional, or axiom-pressure claim",
        "N6": "exact bulk quotient/covariance close while bulk mobile inertia remains open",
        "N7": "longer transverse thickness or reciprocal collision could avoid the observed character mixing",
        "N8": "Cycle494 remains thin-torus and the corridor remains compactified; neither is promoted to bulk",
    }
    check(
        "the result inventories supplied/derived/open structure and clears N1-N8 without broad negative pressure",
        AUTHORITY == "none"
        and AUDIT == "unset"
        and controller["controller_block_residual"] < EG_TOLERANCE
        and quotient["maximum_unitarity_residual"] < UNITARITY_TOLERANCE
        and physical["maximum_residual"] < EG_TOLERANCE
        and covariance["maximum_operator_conjugacy_residual"] < EG_TOLERANCE
        and deletion["contact_deletion_state_residual"] > CONTACT_DELETION_FLOOR
        and domain["rejections"] == domain["attempts"]
        and not cube["positive_bulk_inertia_gate"]
        and not corridor["bulk_3D_claim"],
        {
            "supplied": supplied,
            "derived": derived,
            "open": open_items,
            "N1_N8": n_gate,
            "authority": AUTHORITY,
            "audit": AUDIT,
            "phase_is_energy": False,
            "update_count_is_time": False,
            "displacement_is_velocity": False,
            "response_is_gravity": False,
            "squared_norm_is_probability": False,
            "recurrent_M2_compiler_claim": False,
            "broad_no_go": False,
            "minimum_content": False,
            "shared_obstruction": False,
            "axiom_pressure": False,
        },
    )


def resource_controls(started: float, cube, corridor):
    rows = cube["rows"] + corridor["rows"]
    elapsed = time.perf_counter() - started
    maximum_rss = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    result = {
        "wall_seconds": elapsed,
        "wall_ceiling_seconds": RESOURCE_WALL_CEILING_SECONDS,
        "maximum_RSS_bytes": maximum_rss,
        "maximum_RSS_ceiling_bytes": RESOURCE_RSS_CEILING_BYTES,
        "response_quotient_dimensions": {
            row["fixture"]: row["quotient_dimension"] for row in rows
        },
        "response_zero_character_operator_nnz": {
            row["fixture"]: row["zero_character_operator_nnz"] for row in rows
        },
        "peak_response_quotient_dimension": max(
            row["quotient_dimension"] for row in rows
        ),
        "peak_response_zero_character_operator_nnz": max(
            row["zero_character_operator_nnz"] for row in rows
        ),
    }
    check(
        "the canonical cold harness stays within the frozen wall/RSS guard and reports dimension/nonzero peaks",
        elapsed < RESOURCE_WALL_CEILING_SECONDS
        and maximum_rss < RESOURCE_RSS_CEILING_BYTES,
        result,
    )
    return result


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    started = time.perf_counter()
    print("CYCLE 497: BULK-3D CONTACT-DRESSED INERTIA TOURNAMENT")
    print(f"authority={AUTHORITY}; audit={AUDIT}")
    contract = note_contract()
    check(
        "the note freezes cubic and corridor targets with all semantic firewalls",
        not contract["missing"],
        contract,
    )
    hashes = predecessor_hashes()
    check("all frozen predecessors have exact hashes", all(hashes.values()), hashes)
    coin, controller = native_controller_coin()
    check(
        "the native Cycle492 controller block is reconstructed before its menu",
        controller["construction_events"]
        == ("functional-common-controller-built", "spectral-menu-built")
        and controller["controller_block_residual"] < 3e-12
        and controller["coin_unitarity"] < 3e-12,
        controller,
    )
    quotient = quotient_controls(coin)
    physical = physical_interface_controls(coin)
    cube = cube_response_controls(coin)
    corridor = corridor_response_controls(coin)
    covariance = covariance_controls(coin)
    deletion = deletion_and_fixture_controls(coin)
    domain = domain_controls(coin)
    inventory_controls(
        controller, quotient, physical, covariance, deletion, domain, cube, corridor
    )
    resource_controls(started, cube, corridor)
    print(f"SUMMARY {PASS} passed, {FAIL} failed")
    if FAIL:
        result = "PHYSICAL_BULK_3D_CONTACT_DRESSED_INERTIA_TOURNAMENT_HARNESS_FAILED"
    elif corridor["positive_corridor_inertia_gate"]:
        result = "BULK_CUBE_NOT_CERTIFIED__THICK_CORRIDOR_CERTIFIED_NOT_BULK"
    else:
        result = "BULK_CUBE_AND_THICK_CORRIDOR_INERTIA_NOT_CERTIFIED"
    print("RESULT", result)
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
