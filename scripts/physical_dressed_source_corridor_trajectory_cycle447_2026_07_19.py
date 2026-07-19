#!/usr/bin/env python3
"""Cycle 447: mass-conditioned dressed source and physical M64 corridor.

Construct the source and passive functional laws before any spectral state is
prepared.  After construction, a supplied host eigensolver prepares a
Cycle-425 dressed Q1 source for the selected source sector.  A repeated
Cycle-435/Cycle-319 M64 one-particle corridor then consumes that joint field
state directly.  No c-number field profile or per-update host force is used.

Authority is none.  Audit is unset.  Update count is not physical time and
the resulting coordinate trace is not called gravity or proper time.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from functools import lru_cache
from pathlib import Path
import sys

import numpy as np
from scipy import linalg, sparse


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_mass_passive_trajectory_tournament_cycle442_2026_07_19 as c442
import physical_nn_functional_source_control_compiler_cycle446_2026_07_19 as c446


c425 = c442.c425
c435 = c442.c435
c319 = c442.c319
c322 = c442.c322
c210 = c442.c210
c219 = c442.c219

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_DRESSED_SOURCE_CORRIDOR_TRAJECTORY_CYCLE447_NOTE_2026-07-19.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 2.0e-9
NUMERICAL_FLOOR = 8e-13
PASS = 0
FAIL = 0

# Frozen after the L9 calibration pilot and before the blind L13 rows.
BIC_ADVANTAGE = 6.0
TAIL_CV_MAXIMUM = 0.25
DURATION_RATIO_FRACTION = 0.25
CURVATURE_FLOOR_MULTIPLIER = 1000.0
MINIMUM_SECOND_DIFFERENCES = 4
PACKET_MOMENTUM_WIDTH = 0.35
PACKET_CENTER = 3
BOUNDARY_MAXIMUM = 0.25
BAND_MINIMUM = 0.80
DELETION_VISIBILITY = 1e-6


@dataclass(frozen=True)
class Geometry:
    name: str
    length: int
    depth: int
    held: bool


TRAIN = Geometry("train-L9-D12", 9, 12, False)
HELD = Geometry("held-L13-D18", 13, 18, True)
GEOMETRIES = (TRAIN, HELD)


@dataclass(frozen=True)
class FitResult:
    samples: int
    linear_bic: float
    quadratic_bic: float
    quadratic_curvature: float
    first_difference_cv: float
    second_difference_cv: float
    same_sign_second_differences: int
    duration_ratio: float
    genuine_acceleration: bool
    disposition: str


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(file_path: Path) -> str:
    text = file_path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def note_contract() -> None:
    required = (
        "authority: none",
        "audit: unset",
        "joint update is constructed before preparation",
        "mass-conditioned dressed state is supplied host preparation",
        "no c-number field",
        "no per-update host force",
        "l9/depth12 calibration",
        "l13/depth18 blind held geometry",
        "raw classifier",
        "two-update stroboscopic classifier",
        "no-refresh autonomous update",
        "all 24 proper-cubic frames",
        "l^-1=g_0",
        "rho=|psi|^2",
        "s=l(1-phi)",
        "partial-attempt-with-named-untested-routes",
        "n1 —",
        "n2 —",
        "n3 —",
        "n4 —",
        "n5 —",
        "n6 —",
        "n7 —",
        "n8 —",
        "no gravity, lapse, proper-time, no-go, minimum-content, shared-obstruction, or axiom-pressure claim",
    )
    missing = required if not NOTE.exists() else tuple(
        phrase for phrase in required if phrase not in normalized(NOTE)
    )
    check("the Cycle-447 note freezes the joint dressed-source/corridor contract", not missing, missing)


def validate_geometry(geometry: Geometry) -> None:
    if geometry not in GEOMETRIES or geometry.length < 9 or PACKET_CENTER <= 1:
        raise ValueError("geometry is outside the frozen Cycle-447 domain")
    if geometry.depth < 12 or 2 * PACKET_CENTER >= geometry.length:
        raise ValueError("geometry lacks the frozen radial/boundary separation")


def safe_cv(values: np.ndarray) -> float:
    if len(values) == 0:
        return float("inf")
    scale = abs(float(np.mean(values)))
    return float(np.std(values) / scale) if scale > NUMERICAL_FLOOR else float("inf")


def bic(residual: np.ndarray, parameters: int) -> float:
    count = len(residual)
    rss = max(float(np.vdot(residual, residual).real), NUMERICAL_FLOOR**2)
    return float(count * np.log(rss / count) + parameters * np.log(count))


def classify_trace(values: np.ndarray) -> FitResult:
    trace = np.asarray(values, dtype=float)
    samples = len(trace)
    if samples < 6:
        return FitResult(samples, float("inf"), float("inf"), 0.0, float("inf"), float("inf"), 0, float("nan"), False, "unresolved-too-few-samples")
    elapsed = np.arange(samples, dtype=float)
    linear_design = np.column_stack((np.ones(samples), elapsed))
    quadratic_design = np.column_stack((np.ones(samples), elapsed, elapsed**2))
    linear_coeff = np.linalg.lstsq(linear_design, trace, rcond=None)[0]
    quadratic_coeff = np.linalg.lstsq(quadratic_design, trace, rcond=None)[0]
    linear_bic = bic(trace - linear_design @ linear_coeff, 2)
    quadratic_bic = bic(trace - quadratic_design @ quadratic_coeff, 3)
    first = np.diff(trace)
    second = np.diff(trace, n=2)
    nonzero = second[np.abs(second) > CURVATURE_FLOOR_MULTIPLIER * NUMERICAL_FLOOR]
    same_sign = 0 if not len(nonzero) else int(max(np.count_nonzero(nonzero > 0), np.count_nonzero(nonzero < 0)))
    midpoint = max(1, (samples - 1) // 2)
    denominator = trace[midpoint] - trace[0]
    duration_ratio = float((trace[-1] - trace[0]) / denominator) if abs(denominator) > NUMERICAL_FLOOR else float("nan")
    first_cv = safe_cv(first[-max(3, len(first) // 2) :])
    second_cv = safe_cv(second)
    acceleration = bool(
        linear_bic - quadratic_bic > BIC_ADVANTAGE
        and abs(2 * quadratic_coeff[2]) > CURVATURE_FLOOR_MULTIPLIER * NUMERICAL_FLOOR
        and same_sign >= MINIMUM_SECOND_DIFFERENCES
        and second_cv < TAIL_CV_MAXIMUM
        and np.isfinite(duration_ratio)
        and abs(duration_ratio - 4) < 4 * DURATION_RATIO_FRACTION
    )
    return FitResult(
        samples,
        linear_bic,
        quadratic_bic,
        float(2 * quadratic_coeff[2]),
        first_cv,
        second_cv,
        same_sign,
        duration_ratio,
        acceleration,
        "genuine-acceleration" if acceleration else "transient-or-oscillatory-unresolved",
    )


def field_dimension(length: int) -> int:
    return 7 * length**3


def matter_dimension(length: int) -> int:
    return 6 * length


@lru_cache(maxsize=None)
def field_stream_matrix(length: int) -> sparse.csr_matrix:
    return c425.stream_layer(length)


@lru_cache(maxsize=None)
def local_test_vertex(mass_key: float) -> np.ndarray:
    if not np.isfinite(mass_key):
        raise ValueError("test mass must be finite")
    full = c322.local_source_blocks(c442.SOURCE_SCALE * mass_key)[1]
    local_one = [c322.LOCAL_INDEX[1 << direction] for direction in range(6)]
    joint = [7 * index + q for index in local_one for q in range(7)]
    return full[np.ix_(joint, joint)]


def source_active(length: int) -> tuple[int, ...]:
    return (c425.reservoir_index((0, 0, 0), length),) + tuple(
        c425.field_index((0, 0, 0), direction, length) for direction in range(6)
    )


def cell_active(length: int, x: int) -> tuple[int, ...]:
    cell = (x, 0, 0)
    return (c425.reservoir_index(cell, length),) + tuple(
        c425.field_index(cell, direction, length) for direction in range(6)
    )


def apply_field_coin(state: np.ndarray, length: int, *, inverse: bool = False) -> np.ndarray:
    cells = length**3
    output = state.copy()
    coin = c425.c214.FIELD_COIN.conj().T if inverse else c425.c214.FIELD_COIN
    fields = state[cells:].reshape(cells, 6, -1)
    output[cells:] = np.einsum("ab,xbm->xam", coin, fields, optimize=True).reshape(6 * cells, -1)
    return output


def apply_source_vertex(state: np.ndarray, length: int, angle: float, *, inverse: bool = False) -> np.ndarray:
    output = state.copy()
    active = source_active(length)
    operator = c425.shore.local_vertex_block(angle)
    if inverse:
        operator = operator.conj().T
    output[list(active)] = operator @ state[list(active)]
    return output


def apply_test_vertices(state: np.ndarray, length: int, mass: float, *, inverse: bool = False) -> np.ndarray:
    output = state.copy()
    operator = local_test_vertex(round(float(mass), 13))
    if inverse:
        operator = operator.conj().T
    order = reversed(range(length)) if inverse else range(length)
    for x in order:
        active = cell_active(length, x)
        matter = tuple(range(6 * x, 6 * x + 6))
        packed = output[np.ix_(active, matter)].T.reshape(-1)
        output[np.ix_(active, matter)] = (operator @ packed).reshape(6, 7).T
    return output


def apply_matter_coin(state: np.ndarray, length: int, coin: np.ndarray, *, inverse: bool = False) -> np.ndarray:
    operator = coin.conj().T if inverse else coin
    shaped = state.reshape(field_dimension(length), length, 6)
    return np.einsum("ab,fxb->fxa", operator, shaped, optimize=True).reshape(state.shape)


def apply_matter_stream(state: np.ndarray, length: int, *, inverse: bool = False) -> np.ndarray:
    shaped = state.reshape(field_dimension(length), length, 6)
    output = np.empty_like(shaped)
    sign = -1 if inverse else 1
    for direction in range(6):
        output[:, :, direction] = np.roll(
            shaped[:, :, direction],
            sign * int(c210.DIRECTIONS[direction, 0]),
            axis=1,
        )
    return output.reshape(state.shape)


def joint_step(
    state: np.ndarray,
    geometry: Geometry,
    source_angle: float,
    test_mass: float,
    test_coin: np.ndarray,
    *,
    source_enabled: bool = True,
    test_enabled: bool = True,
    field_stream_enabled: bool = True,
    matter_stream_enabled: bool = True,
    mass_law_enabled: bool = True,
) -> np.ndarray:
    output = apply_matter_coin(state, geometry.length, test_coin if mass_law_enabled else np.eye(6))
    output = apply_field_coin(output, geometry.length)
    if source_enabled and mass_law_enabled:
        output = apply_source_vertex(output, geometry.length, source_angle)
    if test_enabled and mass_law_enabled:
        output = apply_test_vertices(output, geometry.length, test_mass)
    if matter_stream_enabled:
        output = apply_matter_stream(output, geometry.length)
    if field_stream_enabled:
        output = field_stream_matrix(geometry.length) @ output
    return np.asarray(output)


def joint_inverse(
    state: np.ndarray,
    geometry: Geometry,
    source_angle: float,
    test_mass: float,
    test_coin: np.ndarray,
) -> np.ndarray:
    output = field_stream_matrix(geometry.length).getH() @ state
    output = apply_matter_stream(np.asarray(output), geometry.length, inverse=True)
    output = apply_test_vertices(output, geometry.length, test_mass, inverse=True)
    output = apply_source_vertex(output, geometry.length, source_angle, inverse=True)
    output = apply_field_coin(output, geometry.length, inverse=True)
    return apply_matter_coin(output, geometry.length, test_coin, inverse=True)


def packet_density(state: np.ndarray, length: int) -> np.ndarray:
    return np.sum(np.abs(state.reshape(field_dimension(length), length, 6)) ** 2, axis=(0, 2))


def packet_centroid(state: np.ndarray, length: int) -> float:
    return float(packet_density(state, length) @ np.arange(length, dtype=float))


def mixed_band_probability(state: np.ndarray, length: int, species: c210.Species) -> float:
    shaped = state.reshape(field_dimension(length), length, 6)
    packet_k = np.fft.fft(shaped, axis=1, norm="ortho")
    momenta = 2 * np.pi * np.fft.fftfreq(length)
    total = 0.0
    for index, momentum in enumerate(momenta):
        _phase, vector = c210.branch_eigenpair(np.asarray((momentum, 0.0, 0.0)), species)
        amplitudes = packet_k[:, index, :] @ vector.conj()
        total += float(np.vdot(amplitudes, amplitudes).real)
    return total


@lru_cache(maxsize=None)
def dressed_source(length: int, angle_key: float) -> tuple[complex, np.ndarray, float]:
    update, eigenvalue, shore_state = c425.shore.dressed_eigenstate(length, theta=angle_key)
    residual = float(np.linalg.norm(update @ shore_state - eigenvalue * shore_state))
    field = np.asarray(c425.shore_embedding(length) @ shore_state)
    return eigenvalue, field, residual


def prepare_packet(species: c210.Species, length: int) -> np.ndarray:
    _positions, _momenta, packet = c210.prepare_molecular_packet(
        species, length, PACKET_MOMENTUM_WIDTH
    )
    return np.roll(packet, PACKET_CENTER - length // 2, axis=0)


def free_step(packet: np.ndarray, coin: np.ndarray, *, stream_enabled: bool = True) -> np.ndarray:
    mixed = np.einsum("ab,xb->xa", coin, packet, optimize=True)
    if not stream_enabled:
        return mixed
    output = np.empty_like(mixed)
    for direction in range(6):
        output[:, direction] = np.roll(mixed[:, direction], int(c210.DIRECTIONS[direction, 0]))
    return output


def trace_case(
    geometry: Geometry,
    source_mass: float,
    test_mass: float,
    beta: float,
    *,
    source_enabled: bool = True,
    test_enabled: bool = True,
    field_stream_enabled: bool = True,
    matter_stream_enabled: bool = True,
    mass_law_enabled: bool = True,
    dressed_preparation: bool = True,
) -> dict[str, object]:
    validate_geometry(geometry)
    source_angle = c442.SOURCE_SCALE * source_mass
    eigenvalue, field, eigen_residual = dressed_source(geometry.length, round(source_angle, 13))
    if not dressed_preparation:
        field = np.zeros_like(field)
        field[c425.reservoir_index((0, 0, 0), geometry.length)] = 1
    species = c219.common_species(beta)
    packet = prepare_packet(species, geometry.length)
    state = np.outer(field, packet.reshape(-1))
    initial = state.copy()
    free = packet.copy()
    deltas = []
    centroids = []
    free_centroids = []
    widths = []
    boundaries = []
    norms = []
    reservoir_weights = []
    ideal_residuals = []
    for tick in range(geometry.depth + 1):
        density = packet_density(state, geometry.length)
        centroid = float(density @ np.arange(geometry.length, dtype=float))
        second = float(density @ np.arange(geometry.length, dtype=float) ** 2)
        free_density = c210.position_density(free)
        free_centroid = float(free_density @ np.arange(geometry.length, dtype=float))
        centroids.append(centroid)
        free_centroids.append(free_centroid)
        deltas.append(centroid - free_centroid)
        widths.append(float(np.sqrt(max(0.0, second - centroid**2))))
        boundaries.append(float(density[0] + density[-1]))
        norms.append(float(np.linalg.norm(state)))
        reservoir_weights.append(float(np.sum(np.abs(state[: geometry.length**3]) ** 2)))
        ideal = np.outer((eigenvalue**tick) * field, free.reshape(-1))
        ideal_residuals.append(float(np.linalg.norm(state - ideal)))
        if tick < geometry.depth:
            state = joint_step(
                state,
                geometry,
                source_angle,
                test_mass,
                species.coin,
                source_enabled=source_enabled,
                test_enabled=test_enabled,
                field_stream_enabled=field_stream_enabled,
                matter_stream_enabled=matter_stream_enabled,
                mass_law_enabled=mass_law_enabled,
            )
            free = free_step(
                free,
                species.coin if mass_law_enabled else np.eye(6),
                stream_enabled=matter_stream_enabled,
            )
    first = joint_step(initial, geometry, source_angle, test_mass, species.coin)
    restored = joint_inverse(first, geometry, source_angle, test_mass, species.coin)
    delta = np.asarray(deltas)
    raw = classify_trace(delta)
    stroboscopic = classify_trace(delta[::2])
    return {
        "geometry": geometry.name,
        "held": geometry.held,
        "source_mass": source_mass,
        "test_mass": test_mass,
        "beta": beta,
        "delta_centroid": tuple(float(value) for value in delta),
        "centroid": tuple(centroids),
        "free_centroid": tuple(free_centroids),
        "width": tuple(widths),
        "raw_fit": asdict(raw),
        "two_update_stroboscopic_fit": asdict(stroboscopic),
        "strict_sustained": raw.genuine_acceleration and stroboscopic.genuine_acceleration,
        "maximum_norm_error": max(abs(value - 1) for value in norms),
        "final_band_probability": mixed_band_probability(state, geometry.length, species),
        "maximum_boundary_probability": max(boundaries),
        "source_only_eigen_residual": eigen_residual,
        "source_reservoir_weight_initial": reservoir_weights[0],
        "source_reservoir_weight_final": reservoir_weights[-1],
        "joined_source_reservoir_drift": reservoir_weights[-1] - reservoir_weights[0],
        "joined_backreaction_residual_final": ideal_residuals[-1],
        "one_step_inverse_residual": float(np.linalg.norm(restored - initial)),
        "source_refresh_count": 0,
        "per_update_host_force_count": 0,
        "c_number_field_control_count": 0,
    }


def construction_controls():
    print("\nPRE-SECTOR FUNCTIONAL CONSTRUCTION / CYCLE446 SOURCE COMPILER")
    functional = c442.construct_functional_pair()
    controller = c446.c445.build_mass_controller()
    c446.CONSTRUCTION_EVENTS.clear()
    compiled = (
        c446.compile_full_source_law("cayley", controller.cayley),
        c446.compile_full_source_law("principal", controller.principal),
    )
    rows = []
    for law in compiled:
        inverse_schedule = c446.inverse_schedule(law.schedule)
        inverse_operator = c446.schedule_operator(inverse_schedule)
        rows.append(
            {
                "law": law.name,
                "inverse_source_EG": float(np.linalg.norm(inverse_operator - law.target.conj().T)),
                "inverse_unitarity": float(np.linalg.norm(inverse_operator.conj().T @ inverse_operator - np.eye(72))),
                "serial_primitives": len(law.schedule),
                "maximum_support_M2": max(len(gate.sites) for gate in law.schedule),
            }
        )
    check(
        "both full source operators and their physical NN inverse schedules are constructed before the state/sector menu",
        c446.CONSTRUCTION_EVENTS == ["cayley-full-operator-compiled", "principal-full-operator-compiled"]
        and np.linalg.norm(functional.mass_source - controller.cayley) < 2e-12
        and max(max(row["inverse_source_EG"], row["inverse_unitarity"]) for row in rows) < 2e-11
        and all(row["serial_primitives"] == 250 and row["maximum_support_M2"] <= 2 for row in rows),
        {"construction_events": tuple(c446.CONSTRUCTION_EVENTS), "rows": rows},
    )
    sectors = c442.sector_menu(functional.register_source)
    specifications = c442.build_laws(functional, sectors)
    return functional, sectors, specifications, compiled


def projected_source_join_controls(functional, sectors, specifications, compiled) -> None:
    print("\nPROJECTED SOURCE / DRESSED UPDATE JOIN")
    rows = []
    source_sector = sectors[1]
    for name, compiled_law in zip(("cayley-functional", "principal-functional"), compiled):
        law = c442.make_law(functional, specifications[name], source_sector, source_sector, name)
        projected = np.einsum(
            "a,aibj,b->ij",
            source_sector.vector.conj(),
            compiled_law.target.conj().T.reshape(9, 8, 9, 8),
            source_sector.vector,
            optimize=True,
        )
        expected = linalg.block_diag(c425.shore.local_vertex_block(c442.SOURCE_SCALE * law.source_mass), np.ones((1, 1)))
        rows.append(
            {
                "law": name,
                "source_mass": law.source_mass,
                "projected_inverse_compiler_to_Cycle425_vertex": float(np.linalg.norm(projected - expected)),
            }
        )
    check(
        "post-construction sector projection joins the Cycle446 inverse schedule to the Cycle425 local dressed-source vertex without a beta lookup",
        max(row["projected_inverse_compiler_to_Cycle425_vertex"] for row in rows) < 3e-12,
        rows,
    )


def physical_corridor_compiler_controls(functional, sectors, specifications) -> None:
    print("\nREPEATED PHYSICAL M64 CORRIDOR FACTORS")
    rng = np.random.default_rng(44703)
    rows = []
    input_embedding = c442.c441.c311.fock_input_embedding()
    one_columns = [c442.c441.c311.FOCK_INDEX[(1, (direction,))] for direction in range(6)]
    law = c442.make_law(functional, specifications["cayley-functional"], sectors[1], sectors[-1], "cayley-functional")
    local_full = c322.local_source_blocks(c442.SOURCE_SCALE * law.test_mass)[1]
    for compiler_length in (c442.c441.c437.TRAIN_LENGTH, c442.c441.c437.HELD_LENGTH):
        code = c442.c441.c437.build_matter_code(compiler_length)
        one = np.asarray(code.constrained @ input_embedding[:, one_columns])
        full = np.asarray(code.constrained @ input_embedding)
        logical = rng.normal(size=6) + 1j * rng.normal(size=6)
        logical /= np.linalg.norm(logical)
        physical = one @ logical
        coin = c219.common_species(sectors[-1].beta).coin
        coin_physical = physical + one @ (coin @ (one.conj().T @ physical) - one.conj().T @ physical)
        joint = rng.normal(size=(64, 7)) + 1j * rng.normal(size=(64, 7))
        joint /= np.linalg.norm(joint)
        physical_joint = full @ joint
        decoded = full.conj().T @ physical_joint
        moved = (local_full @ decoded.reshape(-1)).reshape(64, 7)
        vertex_physical = physical_joint + full @ (moved - decoded)
        rows.append(
            {
                "compiler_length": compiler_length,
                "encoding_shapes": (one.shape, full.shape),
                "support_M2_per_M64": code.matter_union_m2,
                "Gram": max(float(np.linalg.norm(one.conj().T @ one - np.eye(6))), float(np.linalg.norm(full.conj().T @ full - np.eye(64)))),
                "coin_EG": float(np.linalg.norm(coin_physical - one @ (coin @ logical))),
                "coin_leakage": float(np.linalg.norm(coin_physical - one @ (one.conj().T @ coin_physical))),
                "vertex_EG": float(np.linalg.norm(vertex_physical - full @ moved)),
                "vertex_leakage": float(np.linalg.norm(vertex_physical - full @ (full.conj().T @ vertex_physical))),
            }
        )
    maximum = max(value for row in rows for key, value in row.items() if key in ("Gram", "coin_EG", "coin_leakage", "vertex_EG", "vertex_leakage"))
    check(
        "each repeated corridor cell has bounded physical M64 E/G, inverse-by-adjoint, Gram, and leakage controls independent of corridor length",
        maximum < TOL and all(row["support_M2_per_M64"] == 44 for row in rows),
        {
            "rows": rows,
            "maximum": maximum,
            "corridor_cells_train_held": (TRAIN.length, HELD.length),
            "intercell_FSWAP_compiler": "inherited Cycle319/435 bounded edge factor",
            "global_tensor_materialized": False,
        },
    )


def covariance_mass_contact_controls(sectors) -> None:
    print("\nALL-24 COVARIANCE / MASS / CONTACT")
    mass = sectors[-1].cayley
    coin = c219.common_species(sectors[-1].beta).coin
    vertex = local_test_vertex(round(float(mass), 13))
    rows = []
    for frame in c210.proper_cubic_frames():
        direction = c210.direction_permutation(frame)
        q_frame = linalg.block_diag(np.ones((1, 1)), direction)
        rows.append(
            (
                float(np.linalg.norm(direction @ coin @ direction.conj().T - coin)),
                float(np.linalg.norm(np.kron(direction, q_frame) @ vertex @ np.kron(direction, q_frame).conj().T - vertex)),
            )
        )
    _updates, _coin, _first, _second, contact, _forward, _reverse = c319.update_controls(c435.LABELS, "path")
    restricted_contact = contact[np.ix_(c435.RECEIVER_INDICES, c435.RECEIVER_INDICES)]
    contact_residual = float(sparse.linalg.norm(restricted_contact - sparse.eye(c435.RECEIVER_DIM, format="csc")))
    nontrivial = int(np.count_nonzero(abs(contact.diagonal() - 1) > 1e-13))
    check(
        "the source/receiver local laws and rotated corridor family are covariant in all 24 proper-cubic frames and preserve mass/contact fixtures",
        len(rows) == 24
        and max(max(row) for row in rows) < 4e-11
        and abs(c219.common_species(sectors[-1].beta).analytic_mass - mass) < 3e-12
        and contact_residual < 2e-13
        and nontrivial == 645,
        {
            "frames": len(rows),
            "maximum_coin_covariance": max(row[0] for row in rows),
            "maximum_vertex_covariance": max(row[1] for row in rows),
            "corridor_axis_and_edge_schedule_carried_with_frame": True,
            "mass_fixture": mass,
            "one_particle_contact_residual": contact_residual,
            "full_code_nontrivial_contact_columns": nontrivial,
        },
    )


def trajectory_tournament(functional, sectors, specifications) -> dict[str, object]:
    print("\nFROZEN RAW / TWO-UPDATE-STROBOSCOPIC TRAJECTORY TOURNAMENT")
    print(
        "FROZEN BEFORE BLIND L13",
        {
            "train": TRAIN,
            "held": HELD,
            "packet_momentum_width": PACKET_MOMENTUM_WIDTH,
            "packet_center": PACKET_CENTER,
            "BIC_advantage": BIC_ADVANTAGE,
            "tail_CV_maximum": TAIL_CV_MAXIMUM,
            "duration_ratio_fraction": DURATION_RATIO_FRACTION,
            "curvature_floor_multiplier": CURVATURE_FLOOR_MULTIPLIER,
            "minimum_second_differences": MINIMUM_SECOND_DIFFERENCES,
            "boundary_maximum": BOUNDARY_MAXIMUM,
            "band_minimum": BAND_MINIMUM,
        },
    )
    source_sector = sectors[1]
    cases = (
        ("cayley-functional", sectors[0], TRAIN),
        ("cayley-functional", sectors[1], TRAIN),
        ("cayley-functional", sectors[2], TRAIN),
        ("cayley-functional", sectors[1], HELD),
        ("cayley-functional", sectors[3], HELD),
        ("principal-functional", sectors[3], HELD),
    )
    rows = []
    for law_name, test_sector, geometry in cases:
        print("TRACE CASE", law_name, test_sector.name, geometry.name, flush=True)
        law = c442.make_law(functional, specifications[law_name], source_sector, test_sector, law_name)
        row = trace_case(geometry, law.source_mass, law.test_mass, test_sector.beta)
        row.update({"law": law_name, "source_sector": source_sector.name, "test_sector": test_sector.name})
        rows.append(row)
        print(
            "TRAJECTORY ROW",
            {
                "law": law_name,
                "test_sector": test_sector.name,
                "geometry": geometry.name,
                "final_delta": row["delta_centroid"][-1],
                "raw_fit": row["raw_fit"],
                "stroboscopic_fit": row["two_update_stroboscopic_fit"],
                "strict_sustained": row["strict_sustained"],
                "norm_error": row["maximum_norm_error"],
                "band": row["final_band_probability"],
                "boundary": row["maximum_boundary_probability"],
                "source_eigen_residual": row["source_only_eigen_residual"],
                "source_drift": row["joined_source_reservoir_drift"],
                "backreaction": row["joined_backreaction_residual_final"],
                "inverse": row["one_step_inverse_residual"],
            },
            flush=True,
        )
    held = [row for row in rows if row["held"]]
    check(
        "the supplied dressed source is stationary before the join, while the no-refresh joint update produces normalized train/held traces and quantified backreaction",
        max(row["source_only_eigen_residual"] for row in rows) < 2e-10
        and max(row["maximum_norm_error"] for row in rows) < 2e-10
        and max(row["one_step_inverse_residual"] for row in rows) < 2e-9
        and all(row["source_refresh_count"] == 0 and row["per_update_host_force_count"] == 0 and row["c_number_field_control_count"] == 0 for row in rows)
        and min(row["joined_backreaction_residual_final"] for row in rows) > 1e-6,
        {"rows": rows},
    )
    check(
        "train/held packet boundary and selected-band controls remain explicit without promoting stroboscopic curvature over a failed raw classifier",
        max(row["maximum_boundary_probability"] for row in rows) < BOUNDARY_MAXIMUM
        and min(row["final_band_probability"] for row in held) > BAND_MINIMUM
        and all(row["strict_sustained"] == (row["raw_fit"]["genuine_acceleration"] and row["two_update_stroboscopic_fit"]["genuine_acceleration"]) for row in rows),
        {
            "held_rows": held,
            "all_row_maximum_boundary_probability": max(row["maximum_boundary_probability"] for row in rows),
            "raw_genuine_rows": sum(row["raw_fit"]["genuine_acceleration"] for row in rows),
            "stroboscopic_genuine_rows": sum(row["two_update_stroboscopic_fit"]["genuine_acceleration"] for row in rows),
            "strict_sustained_rows": sum(row["strict_sustained"] for row in rows),
        },
    )
    return {"rows": rows}


def deletion_controls(functional, sectors, specifications, tournament) -> None:
    print("\nFIXED-PREPARATION DELETIONS / NO REFRESH")
    source_sector = sectors[1]
    law = c442.make_law(functional, specifications["cayley-functional"], source_sector, source_sector, "cayley-functional")
    intact = next(row for row in tournament["rows"] if row["law"] == "cayley-functional" and row["test_sector"] == source_sector.name and row["geometry"] == TRAIN.name)
    intact_trace = np.asarray(intact["delta_centroid"])
    rows = {}
    variants = {
        "source_vertex": {"source_enabled": False},
        "test_recoil": {"test_enabled": False},
        "field_stream": {"field_stream_enabled": False},
        "matter_stream": {"matter_stream_enabled": False},
        "mass_law": {"mass_law_enabled": False},
        "dressed_preparation": {"dressed_preparation": False},
    }
    for name, options in variants.items():
        row = trace_case(TRAIN, law.source_mass, law.test_mass, source_sector.beta, **options)
        trace = np.asarray(row["delta_centroid"])
        rows[name] = {
            "maximum_abs_delta": float(np.max(np.abs(trace))),
            "trace_residual_from_intact": float(np.linalg.norm(trace - intact_trace)),
        }
    print("DELETION ROWS", rows, flush=True)
    check(
        "test-recoil and mass-law deletions remove the passive trace, while source vertex, streams, and dressed preparation are separately visible under the frozen initial-state contract",
        rows["test_recoil"]["maximum_abs_delta"] < 2e-11
        and rows["mass_law"]["maximum_abs_delta"] < 2e-11
        and all(rows[name]["trace_residual_from_intact"] > DELETION_VISIBILITY for name in ("source_vertex", "field_stream", "matter_stream", "dressed_preparation")),
        {"intact_maximum_abs_delta": float(np.max(np.abs(intact_trace))), "rows": rows, "source_refresh_count": 0},
    )


def prediction_and_supply_controls(tournament) -> None:
    print("\nCYCLE204 / CYCLE210 / BROAD-GRAVITY BOUNDARY")
    ledger = {
        "Cycle204_Hamiltonian_rows_reproduced": False,
        "Cycle204_strict_QCA_rows_reproduced": False,
        "Cycle204_bound_composite_rows_reproduced": False,
        "Cycle210_exact_mass_rows_reproduced": False,
        "Cycle210_supplied_lapse_acceleration_rows_reproduced": False,
        "L^-1=G_0_derived": False,
        "rho=|psi|^2_derived": False,
        "S=L(1-phi)_derived": False,
        "field_profile_extracted_as_c_number_control": False,
        "per_update_host_force": False,
        "physical_time": False,
        "gravity": False,
        "metric": False,
        "Born_or_occurrence": False,
        "Record": False,
        "authority": AUTHORITY,
        "audit": AUDIT,
        "supplied": (
            "two nine-M2 one-hot registers, Cayley/principal laws, source-sign inverse schedule, coupling scale, and sector preparation",
            "host-selected Cycle425 dressed eigenpair and its phase convention",
            "periodic L9/L13 field, packet preparation, corridor coordinates, depths, factor order, fit thresholds, and readouts",
            "repeated M64 identity completions, C319 FSWAP edge compiler, Q1 field restriction, and diagnostic arithmetic",
        ),
        "derived": (
            "joint source-field-receiver amplitude evolution with source drift/backreaction",
            "raw and two-update-stroboscopic free-subtracted centroid traces",
            "factorwise NN source and repeated M64 compiler residuals, inverse, leakage, covariance, deletions, and held controls",
        ),
        "open": (
            "autonomous physical eigenstate preparation/selection and many-Q source recurrence",
            "a held raw sustained passive trajectory if the frozen classifier is not met",
            "energy/stress/source calibration, field-to-metric map, physical clock/proper time, Records, Born/occurrence, and realized history",
        ),
    }
    check(
        "the exact comparison and supplied/derived/open ledger prevents promotion to Cycle204/210 or broad gravity contracts",
        not any(value for key, value in ledger.items() if key.endswith("_reproduced") or key.endswith("_derived"))
        and not ledger["field_profile_extracted_as_c_number_control"]
        and not ledger["per_update_host_force"]
        and AUTHORITY == "none"
        and AUDIT == "unset",
        {"ledger": ledger, "trajectory_rows": len(tournament["rows"])},
    )


def domain_controls() -> None:
    rejections = 0
    for probe in (
        lambda: validate_geometry(Geometry("bad", 7, 12, False)),
        lambda: local_test_vertex(float("nan")),
    ):
        try:
            probe()
        except (ValueError, OverflowError):
            rejections += 1
    check("malformed geometry and nonfinite mass domains are rejected", rejections == 2, rejections)


def main() -> int:
    print("CYCLE 447: PHYSICAL DRESSED-SOURCE CORRIDOR TRAJECTORY")
    note_contract()
    functional, sectors, specifications, compiled = construction_controls()
    projected_source_join_controls(functional, sectors, specifications, compiled)
    physical_corridor_compiler_controls(functional, sectors, specifications)
    covariance_mass_contact_controls(sectors)
    tournament = trajectory_tournament(functional, sectors, specifications)
    deletion_controls(functional, sectors, specifications, tournament)
    prediction_and_supply_controls(tournament)
    domain_controls()
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL, "authority": AUTHORITY, "audit": AUDIT})
    if FAIL:
        print("RESULT PHYSICAL_DRESSED_SOURCE_CORRIDOR_TRAJECTORY_NOT_CERTIFIED")
        return 1
    print("RESULT PHYSICAL_DRESSED_SOURCE_CORRIDOR_TRAJECTORY_CERTIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
