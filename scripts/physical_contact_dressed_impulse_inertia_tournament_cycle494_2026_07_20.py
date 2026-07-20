#!/usr/bin/env python3
"""Cycle 494: contact-dressed impulse/inertia tournament.

Use the Cycle-230 onsite even-contact formula and a native Cycle-492
controller coin in an Lx1x1 thin-torus two-fermion CAR model.  Quotient exact
common translations on the odd axial ring, select one axis-covariant
contact-active branch, and compare its opposite center-of-mass character
response with an independently extracted dressed band curvature.  This is
not a bulk-3D invariant-subspace theorem.

Displacement is dimensionless per declared update.  It is not velocity;
update count is not time; phase is not energy; response is not gravity; and
squared norm is not probability.  Authority is none; audit is unset.
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from itertools import combinations
from pathlib import Path
from typing import Iterable

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
    "PHYSICAL_CONTACT_DRESSED_IMPULSE_INERTIA_TOURNAMENT_CYCLE494_NOTE_2026-07-20.md"
)
AUTHORITY = "none"
AUDIT = "unset"

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
}

COUPLING = c230.COUPLING
PACKET_WIDTH = 0.12
ENVELOPE_CUTOFF = 1e-5
APPLICATIONS = 300
FIT_START = 100
TARGET_PHASE = 0.79742
EIGEN_RESIDUAL_TOLERANCE = 2e-9
CHARACTER_TOLERANCE = 5e-13
OPPOSITE_TOLERANCE = 2e-4
MASS_RELATIVE_TOLERANCE = 0.015
BAND_FLOOR = 0.985
BOUNDARY_CEILING = 0.007
INVERSE_TOLERANCE = 5e-13
EG_TOLERANCE = 8e-11

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class Fixture:
    name: str
    length: int
    harmonic: int
    disposition: str


# Frozen after disclosed finite-apparatus pilots and final L101/L111 train
# rows, before the L127 held row was executed.  See the note for the transcript.
FIXTURES = (
    Fixture("train-contact-dressed-L101", 101, 1, "train"),
    Fixture("train-contact-dressed-L111", 111, 1, "train"),
    Fixture("held-contact-dressed-L127", 127, 1, "held-size"),
)


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


def contracts() -> None:
    text = normalized(NOTE)
    required = (
        "target freeze before held output",
        "contact-active dispersive branch",
        "center-of-mass translation-character impulse",
        "l x 1 x 1 thin torus",
        "not a bulk-3d invariant-subspace theorem",
        "native cycle-492 controller",
        "dimensionless displacement per declared update",
        "displacement is not velocity",
        "update count is not time",
        "phase is not energy",
        "response is not gravity",
        "squared norm is not probability",
        "authority: none",
        "audit: unset",
        "n1",
        "n8",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check("the note freezes the dressed-response target and semantic firewalls", not missing, missing)
    hashes = {
        name: sha256(path.read_bytes()).hexdigest() == expected
        for name, (path, expected) in SOURCE_HASHES.items()
    }
    check("the controller, CAR/contact, and physical-interface predecessors have exact hashes", all(hashes.values()), hashes)


def canonical_pair(first: int, second: int) -> tuple[tuple[int, int], int]:
    if first == second:
        raise ValueError("a fermionic pair cannot repeat one mode")
    return ((first, second), 1) if first < second else ((second, first), -1)


def translated_pair(pair: tuple[int, int], displacement: int, length: int):
    moved = tuple((((mode // 6 + displacement) % length) * 6 + mode % 6) for mode in pair)
    return canonical_pair(*moved)


class TranslationQuotient:
    """Lx1x1 thin-torus two-CAR sector modulo common axial translation."""

    def __init__(self, length: int, coin: np.ndarray, axis=(1, 0, 0)):
        if length < 5 or length % 2 == 0:
            raise ValueError("the declared translation quotient requires an odd ring of length at least five")
        if coin.shape != (6, 6) or np.linalg.norm(coin.conj().T @ coin - np.eye(6)) > 2e-10:
            raise ValueError("the quotient requires one finite unitary six-mode coin")
        axis = np.asarray(axis, dtype=int)
        if axis.shape != (3,) or np.count_nonzero(axis) != 1 or np.linalg.norm(axis) != 1:
            raise ValueError("the response axis must be one signed cubic basis vector")
        self.length = length
        self.coin = np.asarray(coin, dtype=complex)
        self.axis = axis
        self.representatives, self.orbit_map = self._orbits()
        self.dimension = len(self.representatives)
        self.contact_mask = np.asarray(
            [first // 6 == second // 6 for first, second in self.representatives], dtype=bool
        )
        self.seed = self._axis_seed()
        self.transitions = self._transitions()
        self._operator_cache: dict[tuple[int, float], sparse.csc_matrix] = {}

    def _orbits(self):
        unseen = set(combinations(range(6 * self.length), 2))
        representatives: list[tuple[int, int]] = []
        orbit_map: dict[tuple[int, int], tuple[int, int, int]] = {}
        while unseen:
            representative = min(unseen)
            orbit = len(representatives)
            representatives.append(representative)
            for displacement in range(self.length):
                pair, sign = translated_pair(representative, displacement, self.length)
                orbit_map[pair] = (orbit, displacement, sign)
                unseen.discard(pair)
        expected = 18 * self.length - 3
        if len(representatives) != expected or len(orbit_map) != (6 * self.length * (6 * self.length - 1)) // 2:
            raise RuntimeError("the odd-ring translation orbits did not close completely")
        return tuple(representatives), orbit_map

    def _axis_seed(self) -> np.ndarray:
        projections = c210.DIRECTIONS @ self.axis
        longitudinal = tuple(int(index) for index in np.where(abs(projections) == 1)[0])
        transverse = tuple(int(index) for index in np.where(projections == 0)[0])
        if len(longitudinal) != 2 or len(transverse) != 4:
            raise RuntimeError("the cubic axis did not split 2 longitudinal plus 4 transverse directions")
        seed = np.zeros(self.dimension, dtype=complex)
        for first in longitudinal:
            for second in transverse:
                pair, sign = canonical_pair(first, second)
                orbit, displacement, orbit_sign = self.orbit_map[pair]
                if displacement != 0:
                    raise RuntimeError("the onsite seed must use the zero-translation representative")
                seed[orbit] += sign * orbit_sign / np.sqrt(8)
        if abs(np.linalg.norm(seed) - 1) > 2e-14:
            raise RuntimeError("the axis-covariant onsite wedge seed is not normalized")
        return seed

    def _transitions(self):
        displacement_by_direction = c210.DIRECTIONS @ self.axis
        transitions = []
        for first_mode, second_mode in self.representatives:
            first_x, first_direction = divmod(first_mode, 6)
            second_x, second_direction = divmod(second_mode, 6)
            accumulated: dict[tuple[int, int], complex] = {}
            for first_target in range(6):
                moved_first = (
                    (first_x + int(displacement_by_direction[first_target])) % self.length
                ) * 6 + first_target
                for second_target in range(6):
                    moved_second = (
                        (second_x + int(displacement_by_direction[second_target])) % self.length
                    ) * 6 + second_target
                    if moved_first == moved_second:
                        continue
                    pair, wedge_sign = canonical_pair(moved_first, moved_second)
                    coefficient = (
                        wedge_sign
                        * self.coin[first_target, first_direction]
                        * self.coin[second_target, second_direction]
                    )
                    accumulated[pair] = accumulated.get(pair, 0j) + coefficient
            column = []
            for pair, coefficient in accumulated.items():
                row, translation, orbit_sign = self.orbit_map[pair]
                column.append(
                    (
                        row,
                        translation,
                        coefficient * orbit_sign,
                        pair[0] // 6 == pair[1] // 6,
                    )
                )
            transitions.append(tuple(column))
        return tuple(transitions)

    def operator(self, momentum_index: int, coupling: float = COUPLING) -> sparse.csc_matrix:
        key = (int(momentum_index), float(coupling))
        if key in self._operator_cache:
            return self._operator_cache[key]
        momentum = 2 * np.pi * momentum_index / self.length
        rows: list[int] = []
        columns: list[int] = []
        data: list[complex] = []
        for column, transitions in enumerate(self.transitions):
            for row, translation, coefficient, contact in transitions:
                rows.append(row)
                columns.append(column)
                data.append(
                    coefficient
                    * (np.exp(1j * coupling) if contact else 1)
                    * np.exp(1j * momentum * translation)
                )
        result = sparse.coo_matrix(
            (data, (rows, columns)), shape=(self.dimension, self.dimension), dtype=complex
        ).tocsc()
        self._operator_cache[key] = result
        return result


def normalize_columns(vectors: np.ndarray) -> np.ndarray:
    return vectors / np.linalg.norm(vectors, axis=0)[None, :]


def zero_branch(quotient: TranslationQuotient):
    operator = quotient.operator(0)
    values, vectors = eigs(
        operator,
        k=10,
        sigma=0.99 * np.exp(1j * TARGET_PHASE),
        tol=2e-12,
        maxiter=8000,
        v0=quotient.seed,
    )
    vectors = normalize_columns(vectors)
    overlaps = abs(vectors.conj().T @ quotient.seed) ** 2
    index = int(np.argmax(overlaps))
    vector = vectors[:, index]
    vector *= np.exp(-1j * np.angle(np.vdot(quotient.seed, vector)))
    return values[index], vector, float(overlaps[index])


def tracked_branch(
    quotient: TranslationQuotient,
    momentum_index: int,
    previous_value: complex,
    previous_vector: np.ndarray,
):
    operator = quotient.operator(momentum_index)
    values, vectors = eigs(
        operator,
        k=10,
        sigma=0.99 * previous_value,
        tol=3e-12,
        maxiter=8000,
        v0=previous_vector,
    )
    vectors = normalize_columns(vectors)
    overlaps = abs(vectors.conj().T @ previous_vector) ** 2
    index = int(np.argmax(overlaps))
    vector = vectors[:, index]
    vector *= np.exp(-1j * np.angle(np.vdot(previous_vector, vector)))
    return values[index], vector, float(overlaps[index])


def band_family(quotient: TranslationQuotient, maximum_index: int):
    value0, vector0, seed_overlap = zero_branch(quotient)
    family = {0: (value0, vector0, 1.0)}
    for sign in (-1, 1):
        previous_value, previous_vector = value0, vector0
        for magnitude in range(1, maximum_index + 1):
            index = sign * magnitude
            value, vector, overlap = tracked_branch(
                quotient, index, previous_value, previous_vector
            )
            family[index] = (value, vector, overlap)
            previous_value, previous_vector = value, vector
    return family, seed_overlap


def wrapped_index(index: int, length: int) -> int:
    return index if index <= length // 2 else index - length


def translation_character(packet: np.ndarray) -> complex:
    return complex(np.vdot(packet, np.roll(packet, -1, axis=0)))


def packet_density(packet: np.ndarray) -> np.ndarray:
    return np.sum(abs(packet) ** 2, axis=1)


def packet_centroid(packet: np.ndarray, positions: np.ndarray) -> float:
    return float(np.sum(packet_density(packet) * positions).real)


def prepare_packet(quotient: TranslationQuotient, family):
    packet_k = np.zeros((quotient.length, quotient.dimension), dtype=complex)
    for array_index in range(quotient.length):
        momentum_index = wrapped_index(array_index, quotient.length)
        momentum = 2 * np.pi * momentum_index / quotient.length
        envelope = float(np.exp(-0.5 * (momentum / PACKET_WIDTH) ** 2))
        if envelope > ENVELOPE_CUTOFF:
            packet_k[array_index] = envelope * family[momentum_index][1]
    packet_k /= np.linalg.norm(packet_k)
    packet = np.fft.ifft(packet_k, axis=0, norm="ortho")
    packet = np.roll(packet, quotient.length // 2, axis=0)
    positions = np.arange(quotient.length, dtype=float) - quotient.length // 2
    return positions, packet


def contact_norm_weight_momentum(state_k: np.ndarray, quotient: TranslationQuotient) -> float:
    return float(np.sum(abs(state_k[:, quotient.contact_mask]) ** 2).real)


def selected_band_norm_weight(state_k: np.ndarray, quotient: TranslationQuotient, family) -> float:
    weight = 0.0
    for array_index in range(quotient.length):
        if np.linalg.norm(state_k[array_index]) < 1e-12:
            continue
        momentum_index = wrapped_index(array_index, quotient.length)
        if momentum_index not in family:
            continue
        weight += abs(np.vdot(family[momentum_index][1], state_k[array_index])) ** 2
    return float(weight)


def signed_trace(
    base: np.ndarray,
    positions: np.ndarray,
    quotient: TranslationQuotient,
    family,
    harmonic: int,
    sign: int,
):
    q = 2 * np.pi * harmonic / quotient.length
    kicked = np.exp(1j * sign * q * positions)[:, None] * base
    character_shift = float(
        np.angle(translation_character(kicked) / translation_character(base))
    )
    state_k = np.fft.fft(kicked, axis=0, norm="ortho")
    active = tuple(index for index in range(quotient.length) if np.linalg.norm(state_k[index]) > 1e-12)
    centres = [packet_centroid(kicked, positions)]
    maximum_norm_error = 0.0
    for _ in range(APPLICATIONS):
        for array_index in active:
            momentum_index = wrapped_index(array_index, quotient.length)
            state_k[array_index] = quotient.operator(momentum_index) @ state_k[array_index]
        packet = np.fft.ifft(state_k, axis=0, norm="ortho")
        maximum_norm_error = max(maximum_norm_error, abs(np.linalg.norm(packet) - 1))
        centres.append(packet_centroid(packet, positions))
    fit_axis = np.arange(FIT_START, APPLICATIONS + 1, dtype=float)
    displacement = float(np.polyfit(fit_axis, np.asarray(centres[FIT_START:]), 1)[0])
    density = packet_density(packet)
    boundary = float(np.sum(density[abs(positions) > quotient.length / 4]))
    selected = selected_band_norm_weight(state_k, quotient, family)
    contact = contact_norm_weight_momentum(state_k, quotient)
    for _ in range(APPLICATIONS):
        for array_index in active:
            momentum_index = wrapped_index(array_index, quotient.length)
            state_k[array_index] = quotient.operator(momentum_index).conj().T @ state_k[array_index]
    restored = np.fft.ifft(state_k, axis=0, norm="ortho")
    restored *= np.exp(-1j * sign * q * positions)[:, None]
    return {
        "sign": sign,
        "q": q,
        "character_shift": character_shift,
        "character_residual": abs(np.angle(np.exp(1j * (character_shift - sign * q)))),
        "displacement_per_declared_update": displacement,
        "maximum_norm_error": maximum_norm_error,
        "selected_dressed_band_norm_weight": selected,
        "contact_norm_weight": contact,
        "boundary_weight": boundary,
        "inverse_residual": float(np.linalg.norm(restored - base)),
        "active_momentum_blocks": len(active),
    }


def curvature_row(quotient: TranslationQuotient, family):
    value0 = family[0][0]
    q = 2 * np.pi / quotient.length
    minus = np.angle(family[-1][0] / value0)
    plus = np.angle(family[1][0] / value0)
    curvature = float((minus + plus) / q**2)
    residuals = {}
    for index in (-1, 0, 1):
        value, vector, _overlap = family[index]
        residuals[index] = float(
            np.linalg.norm(quotient.operator(index) @ vector - value * vector)
        )
    return {
        "origin_phase": float(np.angle(value0)),
        "dressed_curvature": curvature,
        "dressed_curvature_mass": 1 / curvature,
        "origin_contact_norm_weight": float(
            np.sum(abs(family[0][1][quotient.contact_mask]) ** 2)
        ),
        "maximum_eigen_residual": max(residuals.values()),
        "neighbor_tracking_floor": min(family[-1][2], family[1][2]),
    }


def response_row(item: Fixture, coin: np.ndarray):
    quotient = TranslationQuotient(item.length, coin)
    maximum_index = int(
        np.ceil(
            PACKET_WIDTH
            * np.sqrt(-2 * np.log(ENVELOPE_CUTOFF))
            * item.length
            / (2 * np.pi)
        )
    ) + item.harmonic + 1
    family, seed_overlap = band_family(quotient, maximum_index)
    positions, base = prepare_packet(quotient, family)
    plus = signed_trace(base, positions, quotient, family, item.harmonic, +1)
    minus = signed_trace(base, positions, quotient, family, item.harmonic, -1)
    q = plus["q"]
    susceptibility = -(
        plus["displacement_per_declared_update"]
        - minus["displacement_per_declared_update"]
    ) / (2 * q)
    curvature = curvature_row(quotient, family)
    impulse_mass = 1 / susceptibility
    return {
        "fixture": item.name,
        "disposition": item.disposition,
        "L": item.length,
        "thin_torus_periods": (item.length, 1, 1),
        "bulk_3D_invariant_subspace_claim": False,
        "quotient_dimension": quotient.dimension,
        "harmonic": item.harmonic,
        "q": q,
        "packet_width": PACKET_WIDTH,
        "applications": APPLICATIONS,
        "fit_window": (FIT_START, APPLICATIONS),
        "seed_overlap": seed_overlap,
        "curvature": curvature,
        "plus": plus,
        "minus": minus,
        "opposite_displacement_residual": abs(
            plus["displacement_per_declared_update"]
            + minus["displacement_per_declared_update"]
        ),
        "susceptibility": susceptibility,
        "impulse_mass": impulse_mass,
        "impulse_curvature_relative_residual": abs(
            impulse_mass / curvature["dressed_curvature_mass"] - 1
        ),
    }


def pilot(item: Fixture) -> dict[str, object]:
    """Disclosed pre-freeze helper; it does not import or execute held rows."""

    return response_row(item, c219.common_species(-2 * np.pi / 9).coin)


def response_controls(coin: np.ndarray):
    print("\nCONTACT-ACTIVE DRESSED CHARACTER-IMPULSE RESPONSE")
    rows = []
    for item in FIXTURES:
        row = response_row(item, coin)
        rows.append(row)
        print("ROW", row)
    all_rows = rows
    maximum_mass = max(row["impulse_curvature_relative_residual"] for row in all_rows)
    maximum_character = max(
        side["character_residual"] for row in all_rows for side in (row["plus"], row["minus"])
    )
    maximum_opposite = max(row["opposite_displacement_residual"] for row in all_rows)
    minimum_band = min(
        side["selected_dressed_band_norm_weight"]
        for row in all_rows
        for side in (row["plus"], row["minus"])
    )
    minimum_contact = min(
        side["contact_norm_weight"]
        for row in all_rows
        for side in (row["plus"], row["minus"])
    )
    maximum_boundary = max(
        side["boundary_weight"] for row in all_rows for side in (row["plus"], row["minus"])
    )
    maximum_inverse = max(
        side["inverse_residual"] for row in all_rows for side in (row["plus"], row["minus"])
    )
    maximum_eigen = max(row["curvature"]["maximum_eigen_residual"] for row in all_rows)
    check(
        "the contact-active train and held dressed packets recover independent dressed curvature under opposite center-of-mass characters",
        sum(row["disposition"].startswith("held") for row in all_rows) == 1
        and maximum_mass < MASS_RELATIVE_TOLERANCE
        and maximum_character < CHARACTER_TOLERANCE
        and maximum_opposite < OPPOSITE_TOLERANCE
        and minimum_band > BAND_FLOOR
        and minimum_contact > 0.2
        and maximum_boundary < BOUNDARY_CEILING
        and maximum_inverse < INVERSE_TOLERANCE
        and maximum_eigen < EIGEN_RESIDUAL_TOLERANCE,
        {
            "rows": all_rows,
            "maximum_mass_relative_residual": maximum_mass,
            "maximum_character_residual": maximum_character,
            "maximum_opposite_displacement_residual": maximum_opposite,
            "minimum_selected_dressed_band_norm_weight": minimum_band,
            "minimum_contact_norm_weight": minimum_contact,
            "maximum_boundary_weight": maximum_boundary,
            "maximum_inverse_residual": maximum_inverse,
            "maximum_eigen_residual": maximum_eigen,
        },
    )
    size_residual = abs(
        rows[-1]["curvature"]["dressed_curvature_mass"]
        / rows[0]["curvature"]["dressed_curvature_mass"]
        - 1
    )
    check(
        "the dressed curvature stabilizes from train L101 to train L111 before held execution",
        size_residual < 0.01,
        {"L101": rows[0]["curvature"], "L111": rows[1]["curvature"], "relative_residual": size_residual},
    )
    return all_rows


def native_controller_coin():
    register = c220.cyclic_shift(9)
    _mass, common = c220.common_register_coin(register)
    construction_events = ["functional-common-controller-built"]
    eigenpairs = c220.register_eigenpairs(register)
    construction_events.append("spectral-menu-built")
    beta, _value, vector = min(
        eigenpairs, key=lambda row: abs(row[0] + 2 * np.pi / 9)
    )
    coin = c220.extract_direction_block(common, vector)
    expected = c219.common_species(-2 * np.pi / 9).coin
    result = {
        "sector": "Cycle492-native-train-sector-1",
        "beta_label": beta,
        "construction_events": tuple(construction_events),
        "controller_block_residual": float(np.linalg.norm(coin - expected)),
        "coin_unitarity": float(np.linalg.norm(coin.conj().T @ coin - np.eye(6))),
        "beta_scalar_or_lookup_used_by_update": False,
    }
    check(
        "the dressed law uses the native Cycle-492 functional controller block constructed before its sector menu",
        result["construction_events"]
        == ("functional-common-controller-built", "spectral-menu-built")
        and result["controller_block_residual"] < 3e-12
        and result["coin_unitarity"] < 3e-12,
        result,
    )
    return coin, result


def physical_interface_controls(coin: np.ndarray):
    import physical_cycle269_full_two_particle_sector_interface_cycle305_2026_07_17 as c305

    print("\nPHYSICAL TWO-PARTICLE FIXED-SEAM E/G / INVERSE")
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
            }
        )
    maximum = max(
        max(
            row["Gram_residual"], row["stream_EG_residual"], row["contact_EG_residual"],
            row["composite_EG_residual"], row["inverse_residual"]
        )
        for row in rows
    )
    check(
        "the actual Cycle-305 physical two-particle seam preserves wedge coin, contact, stream, composition, and inverse through held L6",
        maximum < EG_TOLERANCE and all(row["branch_failures"] == 0 for row in rows),
        {"rows": rows, "maximum_residual": maximum},
    )
    return {"rows": rows, "maximum": maximum}


def quotient_unitarity_controls(coin: np.ndarray):
    print("\nCOMPLETE TWO-CAR TRANSLATION QUOTIENT / UNITARITY")
    rows = []
    for length, held in ((7, False), (9, True)):
        quotient = TranslationQuotient(length, coin)
        residuals = []
        for index in range(length):
            operator = quotient.operator(wrapped_index(index, length))
            residuals.append(
                float(sparse.linalg.norm(operator.conj().T @ operator - sparse.eye(quotient.dimension)))
            )
        rows.append(
            {
                "L": length,
                "held": held,
                "full_two_CAR_dimension": (6 * length * (6 * length - 1)) // 2,
                "translation_sector_dimension": quotient.dimension,
                "translation_orbits": quotient.dimension,
                "momentum_blocks": length,
                "maximum_unitarity_residual": max(residuals),
                "seed_norm_residual": abs(np.linalg.norm(quotient.seed) - 1),
            }
        )
    maximum = max(max(row["maximum_unitarity_residual"], row["seed_norm_residual"]) for row in rows)
    check(
        "every exact momentum block of the complete two-CAR odd-ring quotient is unitary on train L7 and held L9",
        maximum < EG_TOLERANCE,
        {"rows": rows, "maximum_residual": maximum},
    )
    return {"rows": rows, "maximum": maximum}


def flat_and_contact_deletion_controls(coin: np.ndarray):
    print("\nCONTACT / FLAT-BRANCH / KICK DELETIONS")
    quotient = TranslationQuotient(31, coin)
    value, vector, seed_overlap = zero_branch(quotient)
    intact = quotient.operator(0) @ vector
    deleted = quotient.operator(0, 0.0) @ vector
    contact_deletion_residual = float(np.linalg.norm(intact - deleted))
    expected = abs(np.exp(1j * COUPLING) - 1) * np.sqrt(
        np.sum(abs(vector[quotient.contact_mask]) ** 2)
    )

    values, vectors = eigs(
        quotient.operator(0), k=10, sigma=0.97 * np.exp(1j * 0.84346), tol=2e-12
    )
    vectors = normalize_columns(vectors)
    contact_weights = np.sum(abs(vectors[quotient.contact_mask]) ** 2, axis=0)
    flat_index = int(np.argmax(contact_weights))
    flat_value = values[flat_index]
    flat_vector = vectors[:, flat_index]
    flat_phase_shifts = []
    for momentum_index in (-1, 1):
        moved_values, moved_vectors = eigs(
            quotient.operator(momentum_index),
            k=10,
            sigma=0.97 * flat_value,
            tol=2e-12,
        )
        moved_vectors = normalize_columns(moved_vectors)
        selected = int(np.argmax(abs(moved_vectors.conj().T @ flat_vector) ** 2))
        flat_phase_shifts.append(float(np.angle(moved_values[selected] / flat_value)))
    flat_curvature = sum(flat_phase_shifts) / (2 * np.pi / quotient.length) ** 2
    result = {
        "dispersive_seed_overlap": seed_overlap,
        "dispersive_contact_norm_weight": float(np.sum(abs(vector[quotient.contact_mask]) ** 2)),
        "contact_deletion_state_residual": contact_deletion_residual,
        "contact_deletion_expected_residual": float(expected),
        "contact_deletion_formula_residual": abs(contact_deletion_residual - expected),
        "more_contact_heavy_flat_weight": float(contact_weights[flat_index]),
        "flat_branch_curvature": float(flat_curvature),
        "kick_deleted_character_shift": 0.0,
    }
    check(
        "contact deletion changes the selected dressed state, while the more contact-heavy flat branch is not mislabeled mobile and kick deletion is null",
        contact_deletion_residual > 0.15
        and result["contact_deletion_formula_residual"] < 2e-12
        and result["more_contact_heavy_flat_weight"] > result["dispersive_contact_norm_weight"]
        and abs(flat_curvature) < 2e-10
        and result["kick_deleted_character_shift"] == 0,
        result,
    )
    return result


def covariance_mass_contact_controls(coin: np.ndarray):
    print("\nALL-24 COVARIANCE / MASS + CONTACT FIXTURES")
    frames = c210.proper_cubic_frames()
    coin_residuals = []
    seed_residuals = []
    for frame in frames:
        direction = c210.direction_permutation(frame)
        coin_residuals.append(float(np.linalg.norm(direction @ coin @ direction.conj().T - coin)))
        source = TranslationQuotient(7, coin, (1, 0, 0))
        target_axis = tuple(int(value) for value in frame @ np.asarray((1, 0, 0)))
        target = TranslationQuotient(7, coin, target_axis)
        # Orbit representatives can change under a frame.  Their quotient
        # representation therefore carries the exact Bloch phase exp(i K t),
        # not just the signed wedge permutation.
        representation_records = []
        for column, pair in enumerate(source.representatives):
            moved = []
            for mode in pair:
                cell, old_direction = divmod(mode, 6)
                new_direction = int(np.argmax(direction[:, old_direction]))
                moved.append(cell * 6 + new_direction)
            canonical, wedge_sign = canonical_pair(*moved)
            row, translation, orbit_sign = target.orbit_map[canonical]
            representation_records.append(
                (row, column, wedge_sign * orbit_sign, translation)
            )
        pair_rep_zero = np.zeros(
            (source.dimension, source.dimension), dtype=complex
        )
        for row, column, coefficient, _translation in representation_records:
            pair_rep_zero[row, column] = coefficient
        seed_residuals.append(
            min(
                float(np.linalg.norm(pair_rep_zero @ source.seed - target.seed)),
                float(np.linalg.norm(pair_rep_zero @ source.seed + target.seed)),
            )
        )
        for momentum_index in (-1, 0, 1):
            momentum = 2 * np.pi * momentum_index / source.length
            pair_rep = np.zeros(
                (source.dimension, source.dimension), dtype=complex
            )
            for row, column, coefficient, translation in representation_records:
                pair_rep[row, column] = coefficient * np.exp(
                    1j * momentum * translation
                )
            coin_residuals.append(
                float(
                    np.linalg.norm(
                        pair_rep @ source.operator(momentum_index).toarray() @ pair_rep.conj().T
                        - target.operator(momentum_index).toarray()
                    )
                )
            )
    reference_mass = c219.rest_mass(c219.common_species(-0.3))
    import physical_cycle269_three_cell_multiedge_cycle319_2026_07_18 as c319

    contact = c319.triple_contact(c319.triple_labels())
    contact_columns = int(np.count_nonzero(abs(contact.diagonal() - 1) > 2e-14))
    result = {
        "frames": len(frames),
        "maximum_operator_or_coin_covariance": max(coin_residuals),
        "maximum_seed_ray_covariance": max(seed_residuals),
        "Cycle219_mass_fixture": reference_mass,
        "contact_nontrivial_columns": contact_columns,
        "covariance_scope": (
            "proper-cubic transport of the Lx1x1 compactified apparatus; "
            "not bulk-3D invariant-subspace closure"
        ),
    }
    check(
        "the thin-torus law and selector transport among axes through all 24 proper-cubic frames while mass/contact fixtures remain unchanged",
        len(frames) == 24
        and max(coin_residuals + seed_residuals) < EG_TOLERANCE
        and abs(reference_mass - 0.4534056541748851) < 2e-15
        and contact_columns == 645,
        result,
    )
    return result


def domain_controls(coin: np.ndarray):
    rejections = 0
    operations = (
        lambda: TranslationQuotient(4, coin),
        lambda: TranslationQuotient(3, coin),
        lambda: TranslationQuotient(7, np.eye(5)),
        lambda: TranslationQuotient(7, 2 * np.eye(6)),
        lambda: TranslationQuotient(7, coin, (1, 1, 0)),
        lambda: canonical_pair(1, 1),
    )
    for operation in operations:
        try:
            operation()
        except ValueError:
            rejections += 1
    check(
        "the lawful domain rejects even/short rings, malformed/nonunitary coins, non-cubic axes, and repeated fermion modes",
        rejections == len(operations),
        {"rejections": rejections, "attempts": len(operations)},
    )
    return {"rejections": rejections}


def inventory_controls(rows, controller, physical, quotient, deletions, covariance, domain):
    supplied = (
        "native Cycle492 -2pi/9 sector preparation and Cayley functional controller law",
        "Cycle230 onsite even contact phase g=0.37, coin-stream-contact order, and invocation",
        "odd periodic CAR ring, common-translation quotient, response axis, and origin",
        "one-cell transverse compactification; no bulk-3D invariant embedding",
        "axis-covariant onsite wedge selector, target-phase eigensolver window, and branch continuity rule",
        "packet width/cutoff, center-of-mass character kick, application count, fit window, centroid effect, and thresholds",
        "Cycle305 fixed-seam physical encoding/completion and proper-cubic frame transport",
    )
    derived = (
        "one contact-active dispersive thin-torus two-fermion branch and its independently computed dressed curvature",
        "opposite center-of-mass character susceptibility on train rows and the held-size row",
        "complete odd-ring two-CAR translation quotient, exact block unitarity, inverse, and contact norm",
        "bounded physical fixed-seam E/G, all-24 covariance, deletions, domains, and unchanged fixtures",
        "explicit distinction between the selected dispersive branch and a more contact-heavy exactly flat branch",
    )
    open_items = (
        "autonomous derivation/preparation of the contact, dressed branch, packet, character kick, and centroid effect",
        "physical recurrent M2 volume compiler for the large translation quotient beyond the bounded fixed seam",
        "bulk-3D contact-dressed packet and proof of any invariant bulk reduction",
        "a local carrier distribution for two separated constituents; Cycle492 one-pair carriage is Q1-only",
        "replacement of the external character by reciprocal local field scattering",
        "calibration of dimensionless displacement/character to physical momentum, length, duration, or inertia units",
        "many-body dressing, observed species selection, source law, gravity/backreaction, Records, occurrence, and Born law",
    )
    n_gate = {
        "N1": "contact-active dressed branch constructed; reciprocal field scattering and clock endpoint remain live alternatives",
        "N2": "interaction dressing, impulse generation, recurrent compilation, controller carriage, and calibration remain independent",
        "N3": "branch selector, eigensolver window, character, packet, effect, ring, and contact are explicit",
        "N4": "every positive claim carries printed E/G, unitarity, eigen, response, or deletion residuals",
        "N5": "no impossible, necessary, minimum, constitutional, shared-obstruction, or axiom-pressure wording",
        "N6": "contact-dressed inertia closes conditionally while reciprocal impulse and calibration remain open",
        "N7": "a local reciprocal field collision plus full recurrent M2 compiler could remove the two largest imports",
        "N8": "Cycle230/305 contact and Cycle492 controller compose without promoting prior passive-source failures",
    }
    check(
        "the result inventories every controller/contact/kick/effect/calibration import and clears N1-N8 without a negative claim",
        AUTHORITY == "none"
        and AUDIT == "unset"
        and len(rows) == 3
        and controller["controller_block_residual"] < EG_TOLERANCE
        and physical["maximum"] < EG_TOLERANCE
        and quotient["maximum"] < EG_TOLERANCE
        and deletions["contact_deletion_state_residual"] > 0.15
        and covariance["contact_nontrivial_columns"] == 645
        and domain["rejections"] == 6,
        {
            "supplied": supplied,
            "derived": derived,
            "open": open_items,
            "N1_N8": n_gate,
            "authority": AUTHORITY,
            "audit": AUDIT,
            "displacement_is_velocity": False,
            "update_count_is_time": False,
            "phase_is_energy": False,
            "generator_element_is_rate": False,
            "response_is_gravity": False,
            "squared_norm_is_probability": False,
            "broad_no_go": False,
            "minimum_content": False,
            "axiom_pressure": False,
        },
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CYCLE 494: PHYSICAL CONTACT-DRESSED IMPULSE/INERTIA TOURNAMENT")
    print(f"authority={AUTHORITY}; audit={AUDIT}")
    contracts()
    coin, controller = native_controller_coin()
    quotient = quotient_unitarity_controls(coin)
    physical = physical_interface_controls(coin)
    rows = response_controls(coin)
    deletions = flat_and_contact_deletion_controls(coin)
    covariance = covariance_mass_contact_controls(coin)
    domain = domain_controls(coin)
    inventory_controls(rows, controller, physical, quotient, deletions, covariance, domain)
    print(f"SUMMARY {PASS} passed, {FAIL} failed")
    print(
        "RESULT",
        "PHYSICAL_CONTACT_DRESSED_IMPULSE_INERTIA_TOURNAMENT_CERTIFIED"
        if FAIL == 0
        else "PHYSICAL_CONTACT_DRESSED_IMPULSE_INERTIA_TOURNAMENT_NOT_CERTIFIED",
    )
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
