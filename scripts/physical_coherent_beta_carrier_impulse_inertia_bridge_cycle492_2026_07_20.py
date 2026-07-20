#!/usr/bin/env python3
"""Cycle 492: coherent beta-carrier impulse/inertia bridge.

Compose the Cycle-441 nine-M2 Q=1 functional controller with the Cycle-489
translation-character response.  A bounded composite adapter carries one
six-mode matter excitation and its nine-M2 controller excitation together.
The update uses the common C(S), never a beta scalar or sector coin lookup.

Displacement is dimensionless per declared update.  Update count is not
time, phase is not energy, the response is not gravity, and squared norm is
not probability.  Authority is none; audit is unset.
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
import inspect
from pathlib import Path
from typing import Iterable

import numpy as np

import coherent_multibeta_physical_mass_controller_tournament_cycle441_2026_07_19 as c441
import physical_m2_translation_impulse_inertia_bridge_cycle489_2026_07_20 as c489


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_COHERENT_BETA_CARRIER_IMPULSE_INERTIA_BRIDGE_CYCLE492_NOTE_2026-07-20.md"
)
AUTHORITY = "none"
AUDIT = "unset"

c220 = c441.c220
c210 = c441.c210
c311 = c441.c311
c319 = c489.c319

SOURCE_HASHES = {
    "cycle220": (
        ROOT / "scripts/generated_beta_phase_register_cycle220_2026_07_16.py",
        "252708e5adf782d9ad2869add0d64fa757d9d0473d054ee548e98e31d5f7276f",
    ),
    "cycle311": (
        ROOT / "scripts/physical_cycle269_common_m64_fixed_seam_cycle311_2026_07_18.py",
        "4495bf39e1e2661866501e377b8ec1aefff656e261e428fa5b6738f73b49699c",
    ),
    "cycle319": (
        ROOT / "scripts/physical_cycle269_three_cell_multiedge_cycle319_2026_07_18.py",
        "faa05d97542efca7684f4acc6f9b7dfb8e32a02f3f9d16adeae16449f5b702fb",
    ),
    "cycle441": (
        ROOT / "scripts/coherent_multibeta_physical_mass_controller_tournament_cycle441_2026_07_19.py",
        "c274f75ff2b2fe427f04598b84a01247765c562f7ab014ffee2d63af2f27b5d4",
    ),
    "cycle489": (
        ROOT / "scripts/physical_m2_translation_impulse_inertia_bridge_cycle489_2026_07_20.py",
        "8e1d042b68f6505e62cb6c0c92469cd5fa3bdb84779f6ba7e96144a4254b69f0",
    ),
}

PACKET_WIDTH = 0.01
APPLICATIONS = 160
FIT_START = 40
MASS_RELATIVE_TOLERANCE = 0.02
BAND_FLOOR = c489.BAND_FLOOR
BOUNDARY_CEILING = c489.BOUNDARY_CEILING
CHARACTER_TOLERANCE = c489.CHARACTER_TOLERANCE
OPPOSITE_SYMMETRY_TOLERANCE = c489.OPPOSITE_SYMMETRY_TOLERANCE
EG_TOLERANCE = 3e-10
CELL_MATTER_M2 = 6
CELL_CARRIER_M2 = 9
CELL_M2 = CELL_MATTER_M2 + CELL_CARRIER_M2

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class Fixture:
    name: str
    sector_index: int
    length: int
    harmonic: int
    disposition: str


FIXTURES = (
    Fixture("train-native-beta-2pi9", 0, 4096, 2, "train"),
    Fixture("train-native-beta-4pi9", 1, 4096, 2, "train"),
    Fixture("train-native-beta-2pi3", 2, 4096, 2, "train"),
    Fixture("held-native-beta-8pi9-and-L8192", 3, 8192, 3, "held-beta-and-size"),
)
SIZE_CONTROL = Fixture("size-control-native-beta-4pi9", 1, 8192, 4, "size-control")


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
        "target freeze before held execution",
        "native cycle-441 eigenrays",
        "held beta and held size",
        "15 m2 per cell",
        "30-m2 two-cell stream support",
        "no beta scalar or lookup enters the update",
        "dimensionless displacement per declared update",
        "phase is not energy",
        "update count is not time",
        "response is not gravity",
        "squared norm is not probability",
        "authority: none",
        "audit: unset",
        "n1",
        "n8",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check("the note freezes the carrier-response target and semantic firewalls", not missing, missing)
    hashes = {
        name: sha256(path.read_bytes()).hexdigest() == expected
        for name, (path, expected) in SOURCE_HASHES.items()
    }
    check("the controller, response, and physical-M2 predecessors have exact hashes", all(hashes.values()), hashes)


def build_controller():
    c441.CONSTRUCTION_EVENTS.clear()
    register = c220.cyclic_shift(c441.REGISTER_DIM)
    route = c441.functional_route(register)
    sectors = c441.sector_menu(register)
    b3 = c441.lookup_route(sectors, 3)
    return register, route, sectors, b3


def extracted_coin(route, sector) -> np.ndarray:
    return c220.extract_direction_block(route.common_coin, sector.vector)


def controller_construction_controls(route, sectors, b3) -> dict[str, object]:
    print("\nFUNCTIONAL CONTROLLER / NO HOST BETA COIN")
    source = inspect.getsource(c441.functional_route).lower()
    forbidden = ("common_species", "register_eigenpairs", "target_betas", "sector_menu", "lookup_route")
    rows = []
    for sector in sectors:
        block = extracted_coin(route, sector)
        embedding = np.kron(sector.vector[:, None], np.eye(6))
        coordinate = float(np.vdot(sector.vector, route.cayley_mass @ sector.vector).real)
        curvature = curvature_mass_from_coin(block)
        rows.append(
            {
                "sector": sector.name,
                "beta_label": sector.beta,
                "held": sector.held,
                "block_intertwiner": float(np.linalg.norm(route.common_coin @ embedding - embedding @ block)),
                "curvature_mass": curvature,
                "controller_coordinate": coordinate,
                "curvature_coordinate_relative_residual": abs(curvature / coordinate - 1),
            }
        )
    held = sectors[-1]
    held_functional = extracted_coin(route, held)
    held_lookup = c220.extract_direction_block(b3.common_coin, held.vector)
    held_lookup_miss = float(np.linalg.norm(held_functional - held_lookup))
    maximum = max(
        max(row["block_intertwiner"], row["curvature_coordinate_relative_residual"])
        for row in rows
    )
    check(
        "C(S) is constructed before the sector menu and its native eigenrays actuate four coins without a beta lookup",
        c441.CONSTRUCTION_EVENTS == ["functional-route-built", "spectral-menu-built"]
        and not any(token in source for token in forbidden)
        and maximum < 2e-5
        and held_lookup_miss > 1.0,
        {
            "construction_events": tuple(c441.CONSTRUCTION_EVENTS),
            "forbidden_dependency_hits": tuple(token for token in forbidden if token in source),
            "rows": rows,
            "train_only_B3_held_coin_miss": held_lookup_miss,
            "beta_used_by_update": False,
        },
    )
    return {"rows": rows, "held_lookup_miss": held_lookup_miss, "maximum": maximum}


def branch_eigenpair_coin(momentum: np.ndarray, coin: np.ndarray) -> tuple[float, np.ndarray]:
    values, vectors = np.linalg.eig(c210.molecular_bloch(momentum, coin))
    overlaps = np.abs(vectors.conj().T @ c210.UNIFORM)
    index = int(np.argmax(overlaps))
    vector = vectors[:, index]
    vector *= np.exp(-1j * np.angle(np.vdot(c210.UNIFORM, vector)))
    return float(np.angle(values[index])), vector / np.linalg.norm(vector)


def curvature_mass_from_coin(coin: np.ndarray, step: float = 1e-4) -> float:
    origin_phase, _ = branch_eigenpair_coin(np.zeros(3), coin)
    diagonal = []
    for axis in range(3):
        displacement = np.zeros(3)
        displacement[axis] = step
        plus, _ = branch_eigenpair_coin(displacement, coin)
        minus, _ = branch_eigenpair_coin(-displacement, coin)
        plus = origin_phase + angular_difference(plus, origin_phase)
        minus = origin_phase + angular_difference(minus, origin_phase)
        diagonal.append((plus - 2 * origin_phase + minus) / step**2)
    return 1 / float(np.mean(diagonal))


def prepare_packet(coin: np.ndarray, length: int):
    momenta = 2 * np.pi * np.fft.fftfreq(length)
    packet_k = np.zeros((length, 6), dtype=complex)
    for index, momentum in enumerate(momenta):
        wrapped = float(np.angle(np.exp(1j * momentum)))
        envelope = float(np.exp(-0.5 * (wrapped / PACKET_WIDTH) ** 2))
        if envelope <= 1e-14:
            continue
        _phase, vector = branch_eigenpair_coin(np.asarray((momentum, 0.0, 0.0)), coin)
        packet_k[index] = envelope * vector
    packet_k /= np.linalg.norm(packet_k)
    packet = np.fft.ifft(packet_k, axis=0, norm="ortho")
    packet = np.roll(packet, length // 2, axis=0)
    positions = np.arange(length, dtype=float) - length // 2
    return momenta, positions, packet


def translation_character(packet: np.ndarray) -> complex:
    return complex(np.vdot(packet, np.roll(packet, -1, axis=0)))


def packet_density(packet: np.ndarray) -> np.ndarray:
    return np.sum(abs(packet) ** 2, axis=tuple(range(1, packet.ndim)))


def packet_centroid(packet: np.ndarray, positions: np.ndarray) -> float:
    return float(np.sum(packet_density(packet) * positions).real)


def selected_branch_norm_weight(packet: np.ndarray, momenta: np.ndarray, coin: np.ndarray) -> float:
    packet_k = np.fft.fft(packet, axis=0, norm="ortho")
    weight = 0.0
    for index, momentum in enumerate(momenta):
        if np.linalg.norm(packet_k[index]) < 1e-12:
            continue
        _phase, vector = branch_eigenpair_coin(np.asarray((momentum, 0.0, 0.0)), coin)
        weight += abs(np.vdot(vector, packet_k[index])) ** 2
    return float(weight)


def free_step(packet: np.ndarray, coin: np.ndarray, *, inverse: bool = False) -> np.ndarray:
    if inverse:
        unstreamed = np.zeros_like(packet)
        for direction in range(6):
            unstreamed[:, direction] = np.roll(packet[:, direction], -int(c210.DIRECTIONS[direction, 0]))
        return np.einsum("ab,xb->xa", coin.conj().T, unstreamed, optimize=True)
    return c210.local_molecular_step(packet, coin)


def signed_trace(base, positions, momenta, coin, q: float, sign: int) -> dict[str, object]:
    kicked = np.exp(1j * sign * q * positions)[:, None] * base
    shift = angular_difference(float(np.angle(translation_character(kicked))), float(np.angle(translation_character(base))))
    packet = kicked.copy()
    centroids = [packet_centroid(packet, positions)]
    maximum_norm_error = 0.0
    for _ in range(APPLICATIONS):
        packet = free_step(packet, coin)
        maximum_norm_error = max(maximum_norm_error, abs(np.linalg.norm(packet) - 1))
        centroids.append(packet_centroid(packet, positions))
    fit_axis = np.arange(FIT_START, APPLICATIONS + 1, dtype=float)
    displacement = float(np.polyfit(fit_axis, np.asarray(centroids[FIT_START:]), 1)[0])
    density = packet_density(packet)
    boundary = float(np.sum(density[abs(positions) > len(positions) / 4]))
    restored = packet.copy()
    for _ in range(APPLICATIONS):
        restored = free_step(restored, coin, inverse=True)
    restored *= np.exp(-1j * sign * q * positions)[:, None]
    return {
        "sign": sign,
        "q": q,
        "character_shift": shift,
        "character_residual": abs(angular_difference(shift, sign * q)),
        "displacement_per_declared_update": displacement,
        "maximum_norm_error": maximum_norm_error,
        "selected_branch_norm_weight": selected_branch_norm_weight(packet, momenta, coin),
        "boundary_weight": boundary,
        "inverse_residual": float(np.linalg.norm(restored - base)),
    }


def response_row(item: Fixture, route, sectors) -> dict[str, object]:
    sector = sectors[item.sector_index]
    coin = extracted_coin(route, sector)
    momenta, positions, base = prepare_packet(coin, item.length)
    q = 2 * np.pi * item.harmonic / item.length
    plus = signed_trace(base, positions, momenta, coin, q, +1)
    minus = signed_trace(base, positions, momenta, coin, q, -1)
    susceptibility = -(
        plus["displacement_per_declared_update"] - minus["displacement_per_declared_update"]
    ) / (2 * q)
    impulse_mass = 1 / susceptibility
    curvature_mass = curvature_mass_from_coin(coin)
    controller_coordinate = float(np.vdot(sector.vector, route.cayley_mass @ sector.vector).real)
    return {
        "fixture": item.name,
        "disposition": item.disposition,
        "sector": sector.name,
        "beta_label": sector.beta,
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
            plus["displacement_per_declared_update"] + minus["displacement_per_declared_update"]
        ),
        "susceptibility": susceptibility,
        "impulse_mass": impulse_mass,
        "curvature_mass": curvature_mass,
        "controller_coordinate": controller_coordinate,
        "impulse_curvature_relative_residual": abs(impulse_mass / curvature_mass - 1),
        "curvature_coordinate_relative_residual": abs(curvature_mass / controller_coordinate - 1),
        "update_coin_source": "sector reduction of preconstructed C(S)",
    }


def response_controls(route, sectors) -> tuple[list[dict[str, object]], dict[str, object]]:
    print("\nNATIVE-SECTOR CHARACTER-IMPULSE RESPONSE")
    rows = []
    for fixture in FIXTURES:
        row = response_row(fixture, route, sectors)
        rows.append(row)
        print("ROW", row)
    maximum_character = max(side["character_residual"] for row in rows for side in (row["plus"], row["minus"]))
    maximum_opposite = max(row["opposite_displacement_residual"] for row in rows)
    maximum_mass = max(row["impulse_curvature_relative_residual"] for row in rows)
    minimum_band = min(side["selected_branch_norm_weight"] for row in rows for side in (row["plus"], row["minus"]))
    maximum_boundary = max(side["boundary_weight"] for row in rows for side in (row["plus"], row["minus"]))
    maximum_inverse = max(side["inverse_residual"] for row in rows for side in (row["plus"], row["minus"]))
    held = [row for row in rows if row["disposition"] == "held-beta-and-size"]
    check(
        "the native train eigenrays and held beta-and-size eigenray recover controller-coin curvature mass from opposite character kicks",
        len(held) == 1
        and maximum_character < CHARACTER_TOLERANCE
        and maximum_opposite < OPPOSITE_SYMMETRY_TOLERANCE
        and maximum_mass < MASS_RELATIVE_TOLERANCE
        and minimum_band > BAND_FLOOR
        and maximum_boundary < BOUNDARY_CEILING
        and maximum_inverse < 4e-12,
        {
            "rows": rows,
            "maximum_character_residual": maximum_character,
            "maximum_opposite_displacement_residual": maximum_opposite,
            "maximum_impulse_curvature_relative_residual": maximum_mass,
            "minimum_selected_branch_norm_weight": minimum_band,
            "maximum_boundary_weight": maximum_boundary,
            "maximum_inverse_residual": maximum_inverse,
        },
    )
    size = response_row(SIZE_CONTROL, route, sectors)
    reference = rows[1]
    size_residual = abs(size["impulse_mass"] / reference["impulse_mass"] - 1)
    check(
        "doubling L at fixed native sector and exact character q preserves the impulse mass",
        abs(size["q"] - reference["q"]) < 2e-15 and size_residual < 3e-5,
        {"reference": reference, "size_control": size, "relative_residual": size_residual},
    )
    return rows, size


def logical_forward(state: np.ndarray, common_coin: np.ndarray, q: float) -> np.ndarray:
    length = state.shape[0]
    x = np.arange(length, dtype=float) - length // 2
    kicked = np.exp(1j * q * x)[:, None, None, None, None] * state
    flat = kicked.reshape(*kicked.shape[:3], 54)
    mixed = np.einsum("ab,xyzb->xyza", common_coin, flat, optimize=True).reshape(state.shape)
    output = np.zeros_like(mixed)
    for direction, vector in enumerate(c210.DIRECTIONS):
        output[..., direction] = np.roll(
            mixed[..., direction], tuple(int(value) for value in vector), axis=(0, 1, 2)
        )
    return output


def logical_inverse(state: np.ndarray, common_coin: np.ndarray, q: float) -> np.ndarray:
    length = state.shape[0]
    unstreamed = np.zeros_like(state)
    for direction, vector in enumerate(c210.DIRECTIONS):
        unstreamed[..., direction] = np.roll(
            state[..., direction], tuple(-int(value) for value in vector), axis=(0, 1, 2)
        )
    flat = unstreamed.reshape(*state.shape[:3], 54)
    unkicked = np.einsum("ab,xyzb->xyza", common_coin.conj().T, flat, optimize=True).reshape(state.shape)
    x = np.arange(length, dtype=float) - length // 2
    return np.exp(-1j * q * x)[:, None, None, None, None] * unkicked


def word_for(cell: int, register_site: int, direction: int) -> int:
    offset = CELL_M2 * cell
    return (1 << (offset + direction)) | (1 << (offset + CELL_MATTER_M2 + register_site))


def decode_word(word: int, cells: int) -> tuple[int, int, int]:
    if not isinstance(word, int) or word <= 0 or word.bit_count() != 2:
        raise ValueError("carrier code requires exactly two occupied M2")
    positions = tuple(index for index in range(word.bit_length()) if (word >> index) & 1)
    if positions[-1] >= CELL_M2 * cells:
        raise ValueError("occupied M2 lies outside the declared apparatus")
    divided = tuple(divmod(position, CELL_M2) for position in positions)
    matter = tuple((cell, offset) for cell, offset in divided if offset < CELL_MATTER_M2)
    carrier = tuple((cell, offset - CELL_MATTER_M2) for cell, offset in divided if CELL_MATTER_M2 <= offset < CELL_M2)
    if len(matter) != 1 or len(carrier) != 1 or matter[0][0] != carrier[0][0]:
        raise ValueError("matter and its beta carrier must be co-located")
    return matter[0][0], carrier[0][1], matter[0][1]


def carrier_encode(state: np.ndarray) -> dict[int, complex]:
    output: dict[int, complex] = {}
    # Keep the declared finite encoding exactly linear.  In particular, do
    # not prune small coherent amplitudes merely to make the sparse carrier
    # dictionary shorter.
    for index in np.argwhere(state != 0):
        x, y, z, register_site, direction = (int(value) for value in index)
        cell = (x * state.shape[1] + y) * state.shape[2] + z
        output[word_for(cell, register_site, direction)] = complex(state[tuple(index)])
    return output


def carrier_decode(words: dict[int, complex], shape) -> tuple[np.ndarray, float, int]:
    length, side_y, side_z, register_dim, directions = shape
    if (side_y, side_z, register_dim, directions) != (3, 3, 9, 6):
        raise ValueError("carrier adapter requires an Lx3x3x9x6 logical shape")
    output = np.zeros(shape, dtype=complex)
    leakage_squared = 0.0
    leakage_words = 0
    for word, amplitude in words.items():
        try:
            cell, register_site, direction = decode_word(word, length * side_y * side_z)
        except ValueError:
            leakage_squared += abs(amplitude) ** 2
            leakage_words += 1
            continue
        x, remainder = divmod(cell, side_y * side_z)
        y, z = divmod(remainder, side_z)
        output[x, y, z, register_site, direction] += amplitude
    return output, float(np.sqrt(leakage_squared)), leakage_words


def add_word(output: dict[int, complex], word: int, amplitude: complex) -> None:
    output[word] = output.get(word, 0j) + amplitude


def physical_forward(
    words: dict[int, complex],
    shape,
    common_coin: np.ndarray,
    q: float,
    *,
    carry: bool = True,
    deleted_source_cell: int | None = None,
):
    length, side_y, side_z, register_dim, directions = shape
    if (side_y, side_z, register_dim, directions) != (3, 3, 9, 6):
        raise ValueError("carrier adapter requires an Lx3x3x9x6 logical shape")
    output: dict[int, complex] = {}
    for word, amplitude in words.items():
        cell, register_site, source_direction = decode_word(word, length * side_y * side_z)
        x, remainder = divmod(cell, side_y * side_z)
        y, z = divmod(remainder, side_z)
        phase = np.exp(1j * q * (x - length // 2))
        source = 6 * register_site + source_direction
        for target, coefficient in enumerate(common_coin[:, source]):
            target_register, target_direction = divmod(target, 6)
            vector = c210.DIRECTIONS[target_direction]
            tx = (x + int(vector[0])) % length
            ty = (y + int(vector[1])) % side_y
            tz = (z + int(vector[2])) % side_z
            target_cell = (tx * side_y + ty) * side_z + tz
            if carry and cell != deleted_source_cell:
                target_word = word_for(target_cell, target_register, target_direction)
            else:
                matter_bit = 1 << (CELL_M2 * target_cell + target_direction)
                carrier_bit = 1 << (CELL_M2 * cell + CELL_MATTER_M2 + target_register)
                target_word = matter_bit | carrier_bit
            add_word(output, target_word, amplitude * phase * coefficient)
    return output


def physical_inverse(words: dict[int, complex], shape, common_coin: np.ndarray, q: float):
    length, side_y, side_z, register_dim, directions = shape
    if (side_y, side_z, register_dim, directions) != (3, 3, 9, 6):
        raise ValueError("carrier adapter requires an Lx3x3x9x6 logical shape")
    output: dict[int, complex] = {}
    for word, amplitude in words.items():
        cell, target_register, target_direction = decode_word(word, length * side_y * side_z)
        x, remainder = divmod(cell, side_y * side_z)
        y, z = divmod(remainder, side_z)
        vector = c210.DIRECTIONS[target_direction]
        sx = (x - int(vector[0])) % length
        sy = (y - int(vector[1])) % side_y
        sz = (z - int(vector[2])) % side_z
        source_cell = (sx * side_y + sy) * side_z + sz
        target = 6 * target_register + target_direction
        phase = np.exp(-1j * q * (sx - length // 2))
        for source, coefficient in enumerate(common_coin.conj().T[:, target]):
            source_register, source_direction = divmod(source, 6)
            add_word(output, word_for(source_cell, source_register, source_direction), amplitude * phase * coefficient)
    return output


def state_residual(left: dict[int, complex], right: dict[int, complex]) -> float:
    return float(np.sqrt(sum(abs(left.get(key, 0j) - right.get(key, 0j)) ** 2 for key in left.keys() | right.keys())))


def full_column_controls(shape, common_coin: np.ndarray, q: float) -> dict[str, object]:
    """Check every position x register x direction code column without ray selection."""

    length, side_y, side_z, register_dim, directions = shape
    cells = length * side_y * side_z
    forward_squared = inverse_squared = leakage_squared = 0.0
    leakage_words = 0
    columns = 0
    for cell in range(cells):
        x, remainder = divmod(cell, side_y * side_z)
        y, z = divmod(remainder, side_z)
        phase = np.exp(1j * q * (x - length // 2))
        for register_site in range(register_dim):
            for source_direction in range(directions):
                source = 6 * register_site + source_direction
                encoded = {word_for(cell, register_site, source_direction): 1 + 0j}
                expected: dict[int, complex] = {}
                for target, coefficient in enumerate(common_coin[:, source]):
                    target_register, target_direction = divmod(target, 6)
                    vector = c210.DIRECTIONS[target_direction]
                    tx = (x + int(vector[0])) % length
                    ty = (y + int(vector[1])) % side_y
                    tz = (z + int(vector[2])) % side_z
                    target_cell = (tx * side_y + ty) * side_z + tz
                    add_word(expected, word_for(target_cell, target_register, target_direction), phase * coefficient)
                physical = physical_forward(encoded, shape, common_coin, q)
                restored = physical_inverse(physical, shape, common_coin, q)
                _decoded, leakage, count = carrier_decode(physical, shape)
                forward_squared += state_residual(physical, expected) ** 2
                inverse_squared += state_residual(restored, encoded) ** 2
                leakage_squared += leakage**2
                leakage_words += count
                columns += 1
    return {
        "columns": columns,
        "expected_columns": cells * 54,
        "full_column_forward_Frobenius": float(np.sqrt(forward_squared)),
        "full_column_inverse_Frobenius": float(np.sqrt(inverse_squared)),
        "full_column_leakage_Frobenius": float(np.sqrt(leakage_squared)),
        "full_column_leakage_words": leakage_words,
    }


def carrier_adapter_controls(route) -> dict[str, object]:
    print("\nBOUNDED COMPOSITE BETA-CARRIER ADAPTER / E-G / INVERSE")
    rng = np.random.default_rng(492)
    rows = []
    for length, held in ((4, False), (6, True)):
        shape = (length, 3, 3, 9, 6)
        q = 2 * np.pi / length
        state = rng.normal(size=shape) + 1j * rng.normal(size=shape)
        state /= np.linalg.norm(state)
        encoded = carrier_encode(state)
        logical = logical_forward(state, route.common_coin, q)
        physical_words = physical_forward(encoded, shape, route.common_coin, q)
        physical, leakage, leakage_words = carrier_decode(physical_words, shape)
        restored_words = physical_inverse(physical_words, shape, route.common_coin, q)
        restored, inverse_leakage, inverse_leakage_words = carrier_decode(restored_words, shape)
        logical_restored = logical_inverse(logical, route.common_coin, q)
        full_columns = full_column_controls(shape, route.common_coin, q)
        rows.append(
            {
                "L": length,
                "held": held,
                "logical_columns": int(np.prod(shape)),
                "physical_M2": CELL_M2 * length * 3 * 3,
                "EG_residual": float(np.linalg.norm(physical - logical)),
                "physical_inverse_residual": float(np.linalg.norm(restored - state)),
                "physical_word_inverse_residual": state_residual(restored_words, encoded),
                "logical_inverse_residual": float(np.linalg.norm(logical_restored - state)),
                "norm_residual": abs(np.linalg.norm(physical) - 1),
                "leakage_norm": leakage + inverse_leakage,
                "leakage_words": leakage_words + inverse_leakage_words,
                "onsite_support_M2": CELL_M2,
                "two_cell_stream_support_M2": 2 * CELL_M2,
                "constant_overhead_M2_per_cell": CELL_M2,
                "global_matter_population_per_codeword": 1,
                "global_carrier_population_per_codeword": 1,
                "register_cloned_per_cell": False,
                "pair_stream_declared_as_atomic_bounded_gate": True,
                "exposed_intermediate_off_code_layers": 0,
                "primitive_sparse_pair_stream_schedule": "open",
                "full_internal_column_controls": full_columns,
            }
        )
    maximum = max(
        max(
            row["EG_residual"], row["physical_inverse_residual"],
            row["physical_word_inverse_residual"], row["logical_inverse_residual"],
            row["norm_residual"], row["leakage_norm"],
            row["full_internal_column_controls"]["full_column_forward_Frobenius"],
            row["full_internal_column_controls"]["full_column_inverse_Frobenius"],
            row["full_internal_column_controls"]["full_column_leakage_Frobenius"],
        )
        for row in rows
    )
    check(
        "the 15-M2-per-cell composite code satisfies E G = G_physical E and inverse on train L4 and held L6 tori",
        maximum < EG_TOLERANCE
        and all(row["leakage_words"] == 0 for row in rows)
        and all(row["full_internal_column_controls"]["full_column_leakage_words"] == 0 for row in rows)
        and all(
            row["full_internal_column_controls"]["columns"]
            == row["full_internal_column_controls"]["expected_columns"]
            for row in rows
        ),
        {
            "rows": rows,
            "maximum_residual": maximum,
            "local_constraint": "Q_matter=Q_carrier in {0,1}, occupied excitations co-located",
            "global_code": "exactly one matter excitation and one correlated controller excitation, coherently delocalized",
            "cloned_registers": False,
            "edge_factor": "one atomic bounded 30-M2 code-space permutation/completion",
            "intermediate_off_code_use": False,
            "primitive_edge_decomposition": "supplied/open",
            "global_Jordan_Wigner_order": False,
            "global_parity_service": False,
            "host_side_control": False,
        },
    )
    return {"rows": rows, "maximum": maximum}


def physical_m64_controller_controls(route) -> dict[str, object]:
    print("\nACTUAL CYCLE-441 M64 x NINE-M2 LOCAL CONTROLLER")
    code, one, _full, _rest = c441.matter_code()
    forward_squared = inverse_squared = leakage_squared = 0.0
    for source in range(54):
        logical = np.zeros((9, 6), dtype=complex)
        logical.reshape(-1)[source] = 1
        physical = c441.encode_direction(logical, one)
        expected = c441.encode_direction((route.common_coin @ logical.reshape(-1)).reshape(9, 6), one)
        moved = c441.physical_completion(physical, one, route.common_coin)
        restored = c441.physical_completion(moved, one, route.common_coin, inverse=True)
        reconstructed = c441.encode_direction(c441.decode_direction(moved, one), one)
        forward_squared += np.linalg.norm(moved - expected) ** 2
        inverse_squared += np.linalg.norm(restored - physical) ** 2
        leakage_squared += np.linalg.norm(moved - reconstructed) ** 2
    result = {
        "54D_forward_Frobenius": float(np.sqrt(forward_squared)),
        "54D_inverse_Frobenius": float(np.sqrt(inverse_squared)),
        "54D_leakage_Frobenius": float(np.sqrt(leakage_squared)),
        "M64_n1_Gram": float(np.linalg.norm(one.conj().T @ one - np.eye(6))),
        "role_constraint_residual": float(np.linalg.norm(code.constraint @ one - one)),
        "controller_support_M2": code.matter_union_m2 + 9,
        "primitive_dense_completion_materialized": False,
    }
    check(
        "the actual Cycle-441 M64 one-particle embedding retains exact common-controller E/G, inverse, and role constraint",
        max(value for key, value in result.items() if key.endswith(("Frobenius", "Gram", "residual"))) < EG_TOLERANCE
        and result["controller_support_M2"] == 53,
        result,
    )
    return result


def coherent_carried_trace_controls(route, sectors) -> dict[str, object]:
    print("\nCOHERENT FOUR-SECTOR CARRIED TRACE")
    length = 512
    applications = 32
    q = 4 * np.pi / length
    alpha = np.asarray((0.37, 0.41j, -0.52, 0.64j), dtype=complex)
    alpha /= np.linalg.norm(alpha)
    branches = []
    full = np.zeros((length, 9, 6), dtype=complex)
    for index, sector in enumerate(sectors):
        coin = extracted_coin(route, sector)
        _momenta, positions, packet = prepare_packet(coin, length)
        branches.append(packet)
        full += alpha[index] * np.einsum("r,xd->xrd", sector.vector, packet)
    initial = full.copy()
    phase = np.exp(1j * q * positions)
    full *= phase[:, None, None]
    branches = [phase[:, None] * packet for packet in branches]
    full_centroids = [packet_centroid(full, positions)]
    branch_centroids = [sum(abs(alpha[i]) ** 2 * packet_centroid(branches[i], positions) for i in range(4))]
    for _ in range(applications):
        mixed = (route.common_coin @ full.reshape(length, 54).T).T.reshape(length, 9, 6)
        moved = np.zeros_like(mixed)
        for direction in range(6):
            moved[..., direction] = np.roll(mixed[..., direction], int(c210.DIRECTIONS[direction, 0]), axis=0)
        full = moved
        for index, sector in enumerate(sectors):
            branches[index] = free_step(branches[index], extracted_coin(route, sector))
        full_centroids.append(packet_centroid(full, positions))
        branch_centroids.append(sum(abs(alpha[i]) ** 2 * packet_centroid(branches[i], positions) for i in range(4)))
    for _ in range(applications):
        unstreamed = np.zeros_like(full)
        for direction in range(6):
            unstreamed[..., direction] = np.roll(full[..., direction], -int(c210.DIRECTIONS[direction, 0]), axis=0)
        full = (route.common_coin.conj().T @ unstreamed.reshape(length, 54).T).T.reshape(length, 9, 6)
    full *= phase.conj()[:, None, None]
    result = {
        "applications": applications,
        "coherent_trace_residual": float(np.max(abs(np.asarray(full_centroids) - np.asarray(branch_centroids)))),
        "inverse_residual": float(np.linalg.norm(full - initial)),
        "initial_norm_residual": abs(np.linalg.norm(initial) - 1),
        "coefficient_squared_norms": tuple(float(abs(value) ** 2) for value in alpha),
        "coefficient_squared_norms_called_probability": False,
    }
    check(
        "one coherent four-sector carrier evolves under C(S) as the exact orthogonal branch sum and inverts",
        max(result["coherent_trace_residual"], result["inverse_residual"], result["initial_norm_residual"]) < 2e-10,
        result,
    )
    return result


def covariance_mass_contact_controls(route, sectors, rows: Iterable[dict[str, object]]) -> dict[str, object]:
    print("\nALL-24 COVARIANCE / MASS + CONTACT PRESERVATION")
    frames = c210.proper_cubic_frames()
    residuals = []
    for frame in frames:
        direction = c210.direction_permutation(frame)
        representation = np.kron(np.eye(9), direction)
        residuals.append(float(np.linalg.norm(representation @ route.common_coin @ representation.conj().T - route.common_coin)))
        for source in range(6):
            target = int(np.argmax(direction[:, source]))
            residuals.append(float(np.linalg.norm(frame @ c210.DIRECTIONS[source] - c210.DIRECTIONS[target])))
    for row in rows:
        coin = extracted_coin(route, next(sector for sector in sectors if sector.name == row["sector"]))
        q = row["q"]
        reference_plus, _ = branch_eigenpair_coin(np.asarray((q, 0.0, 0.0)), coin)
        reference_minus, _ = branch_eigenpair_coin(np.asarray((-q, 0.0, 0.0)), coin)
        for frame in frames:
            axis = frame @ np.asarray((1.0, 0.0, 0.0))
            plus, _ = branch_eigenpair_coin(q * axis, coin)
            minus, _ = branch_eigenpair_coin(-q * axis, coin)
            residuals.extend((abs(angular_difference(plus, reference_plus)), abs(angular_difference(minus, reference_minus))))
    reference_mass = c489.c219.rest_mass(c489.c219.common_species(-0.3))
    contact = c319.triple_contact(c319.triple_labels())
    contact_nontrivial = int(np.count_nonzero(abs(contact.diagonal() - 1) > 2e-14))
    result = {
        "frames": len(frames),
        "maximum_covariance_residual": max(residuals),
        "Cycle219_mass_fixture": reference_mass,
        "contact_nontrivial_columns": contact_nontrivial,
        "carrier_frame_action": "I9 proper-cubic scalar",
    }
    check(
        "the composite carrier law and response transport through all 24 proper-cubic frames while mass/contact fixtures remain unchanged",
        len(frames) == 24
        and result["maximum_covariance_residual"] < 4e-11
        and abs(reference_mass - 0.4534056541748851) < 2e-15
        and contact_nontrivial == 645,
        result,
    )
    return result


def deletion_domain_controls(route, sectors) -> dict[str, object]:
    print("\nBETA-CARRIER DELETION / MALFORMED DOMAIN")
    shape = (4, 3, 3, 9, 6)
    state = np.zeros(shape, dtype=complex)
    state[0, 0, 0, 0, 0] = 1 / np.sqrt(2)
    state[1, 1, 1, 0, 0] = 1j / np.sqrt(2)
    encoded = carrier_encode(state)
    intact = physical_forward(encoded, shape, route.common_coin, 0.173)
    deleted = physical_forward(encoded, shape, route.common_coin, 0.173, carry=False)
    _decoded, deleted_leakage, deleted_words = carrier_decode(deleted, shape)
    deleted_cell = (1 * shape[1] + 1) * shape[2] + 1
    one_cell_deleted = physical_forward(
        encoded, shape, route.common_coin, 0.173, deleted_source_cell=deleted_cell
    )
    _one_cell_decoded, one_cell_leakage, one_cell_words = carrier_decode(one_cell_deleted, shape)

    # Negative control: one controller excitation anchored at cell zero cannot
    # lawfully accompany matter amplitudes at remote cells.  This is a bounded
    # route-specific failure of the wrong adapter, not a no-go statement.
    remote_cell = deleted_cell
    wrong_global_word = (
        (1 << (CELL_M2 * remote_cell))
        | (1 << CELL_MATTER_M2)
    )
    _wrong_decoded, wrong_global_leakage, wrong_global_words = carrier_decode(
        {wrong_global_word: 1 + 0j}, shape
    )
    held = sectors[-1]
    controller_deleted_residual = float(np.linalg.norm(extracted_coin(route, held) - np.eye(6)))
    _momenta, _positions, kick_probe = prepare_packet(extracted_coin(route, sectors[0]), 256)
    kick_deleted_character_shift = abs(
        angular_difference(
            float(np.angle(translation_character(kick_probe))),
            float(np.angle(translation_character(kick_probe))),
        )
    )
    cells = shape[0] * shape[1] * shape[2]
    malformed = (
        0,
        1,
        (1 << 0) | (1 << 1),
        (1 << 0) | (1 << (CELL_M2 + CELL_MATTER_M2)),
        (1 << (CELL_M2 * cells)) | (1 << (CELL_M2 * cells + CELL_MATTER_M2)),
    )
    rejections = 0
    for word in malformed:
        try:
            decode_word(word, cells)
        except ValueError:
            rejections += 1
    shape_rejections = 0
    for malformed_shape in ((4, 3, 3, 8, 6), (4, 2, 3, 9, 6)):
        try:
            carrier_decode({}, malformed_shape)
        except ValueError:
            shape_rejections += 1
    register_rejections = 0
    for mask in (0, 0b11):
        try:
            c441.validate_register_code_mask(mask)
        except ValueError:
            register_rejections += 1
    result = {
        "carrier_deleted_leakage_norm": deleted_leakage,
        "carrier_deleted_malformed_words": deleted_words,
        "carrier_deleted_state_residual": state_residual(intact, deleted),
        "one_spatial_carrier_deleted_leakage_norm": one_cell_leakage,
        "one_spatial_carrier_deleted_malformed_words": one_cell_words,
        "one_spatial_carrier_deleted_state_residual": state_residual(intact, one_cell_deleted),
        "wrong_fixed_global_register_leakage_norm": wrong_global_leakage,
        "wrong_fixed_global_register_malformed_words": wrong_global_words,
        "controller_deleted_held_coin_residual": controller_deleted_residual,
        "kick_deleted_character_shift": kick_deleted_character_shift,
        "composite_word_rejections": rejections,
        "shape_rejections": shape_rejections,
        "register_Q0_Q2_rejections": register_rejections,
    }
    check(
        "deleting carrier transport or controller actuation is visible, kick deletion is null, and malformed/Q0/Q2 words are rejected",
        deleted_leakage > 0.99
        and deleted_words > 0
        and result["carrier_deleted_state_residual"] > 1.0
        and one_cell_leakage > 0.7
        and one_cell_words > 0
        and result["one_spatial_carrier_deleted_state_residual"] > 0.9
        and wrong_global_leakage > 0.99
        and wrong_global_words == 1
        and controller_deleted_residual > 1.0
        and kick_deleted_character_shift < 2e-15
        and rejections == len(malformed)
        and shape_rejections == 2
        and register_rejections == 2,
        result,
    )
    return result


def inventory_controls(controller, adapter, m64, coherent, covariance, deletions) -> None:
    print("\nSUPPLIED / DERIVED / OPEN / N1-N8 GATE")
    supplied = (
        "nine-M2 Q1 register existence, one-hot preparation, ring orientation, and beta-sector preparation",
        "Cayley coordinate law, dense matrix functions, common-coin factor order, and primitive invocation",
        "six-mode Q1 matter interpretation, blank M2, composite co-location constraint, and initial packet",
        "periodic Lx3x3 apparatus, origin/axis, character kick, harmonics, packet width, and update count",
        "centroid effect, fit window, curvature comparator, thresholds, and proper-cubic frame transport",
        "Cycle311 role-gauge preparation/completion and Cycle319 contact coupling",
    )
    derived = (
        "functional C(S) block actuation on three native train rays and one held beta-and-size ray",
        "15-M2 local composite encoding with exact finite-volume E/G, inverse, leakage, and local constraint",
        "co-transported coherent four-sector trace and train/held character-impulse susceptibility",
        "agreement of impulse susceptibility with controller-coin curvature and Cayley coordinate",
        "all-24 covariance, beta-carrier deletion, malformed-domain, mass, and contact controls",
    )
    open_items = (
        "derivation or empirical selection of the nine-cycle, its orientation, Cayley law, and populated sectors",
        "primitive sparse synthesis of dense bounded C(S) and the actual local carrier-stream gate schedule",
        "autonomous packet, lattice-character kick, effect, controller, and apparatus preparation",
        "calibration of character impulse and dimensionless displacement to physical momentum, length, or duration",
        "full-number interacting recurrent volume beyond Q1, interaction-dressed inertia, and observed species spectrum",
        "source law, passive gravity/backreaction, Record formation, occurrence, Born law, and realized history",
    )
    n_gate = {
        "N1_alternative_routes": "global fixed register rejected as nonlocal; bounded co-carrier constructed; staggered/time-multiplex remains an unneeded alternative",
        "N2_wall_independence": "carrier locality, primitive synthesis, preparation, calibration, and interpretation are distinct",
        "N3_hidden_wall_scan": "internal ring orientation and co-location/carry schedule are supplied",
        "N4_residual_matching": "all positive claims carry exact E/G or declared numerical residuals",
        "N5_rhetoric_audit": "no impossible, necessary, minimum, constitutional, or axiom-pressure wording",
        "N6_partial_closure": "bounded carried controller and same-law inertia response close; far-side calibrations remain open",
        "N7_steelman": "an autonomous sparse controller/stream compiler could replace the supplied bounded dense factors",
        "N8_cross_cycle_echo": "Cycle441 local controller plus Cycle489 response compose through a new adapter without promoting Cycle442/447 failures",
    }
    check(
        "the result inventories every calibration, kick, effect, and controller import and clears N1-N8 without a negative claim",
        AUTHORITY == "none"
        and AUDIT == "unset"
        and controller["held_lookup_miss"] > 1
        and adapter["maximum"] < EG_TOLERANCE
        and m64["controller_support_M2"] == 53
        and coherent["inverse_residual"] < EG_TOLERANCE
        and covariance["contact_nontrivial_columns"] == 645
        and deletions["composite_word_rejections"] == 5
        and deletions["shape_rejections"] == 2,
        {
            "supplied": supplied,
            "derived": derived,
            "open": open_items,
            "N1_N8": n_gate,
            "authority": AUTHORITY,
            "audit": AUDIT,
            "global_Jordan_Wigner_order": False,
            "global_parity_service": False,
            "phase_is_energy": False,
            "update_count_is_time": False,
            "displacement_is_velocity": False,
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
    print("CYCLE 492: PHYSICAL COHERENT BETA-CARRIER IMPULSE/INERTIA BRIDGE")
    print(f"authority={AUTHORITY}; audit={AUDIT}")
    contracts()
    _register, route, sectors, b3 = build_controller()
    controller = controller_construction_controls(route, sectors, b3)
    adapter = carrier_adapter_controls(route)
    m64 = physical_m64_controller_controls(route)
    rows, _size = response_controls(route, sectors)
    coherent = coherent_carried_trace_controls(route, sectors)
    covariance = covariance_mass_contact_controls(route, sectors, rows)
    deletions = deletion_domain_controls(route, sectors)
    inventory_controls(controller, adapter, m64, coherent, covariance, deletions)
    print(f"SUMMARY {PASS} passed, {FAIL} failed")
    print(
        "RESULT",
        "PHYSICAL_COHERENT_BETA_CARRIER_IMPULSE_INERTIA_BRIDGE_CERTIFIED"
        if FAIL == 0
        else "PHYSICAL_COHERENT_BETA_CARRIER_IMPULSE_INERTIA_BRIDGE_NOT_CERTIFIED",
    )
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
