#!/usr/bin/env python3
"""Cycle 442: physical common-mass passive-trajectory tournament.

Construct the source and test functional controls from two represented copies
of the Cycle-441 nine-M2 register before inspecting any beta eigenray.  Route
A1 then joins those controls to two disjoint three-M64 one-particle blocks and
one actual Q=1 hard-core field.  It records the receiver centroid at every
declared update and distinguishes an arrival impulse from sustained
acceleration with frozen held-out criteria.

The wide-packet lane is an operational host-force comparator.  No update
count is time, no field occupation is energy/gravity, no phase is proper time,
and no latch or pointer is a Record.  Authority is none and audit is unset.
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

import coherent_multibeta_physical_mass_controller_tournament_cycle441_2026_07_19 as c441
import physical_quadrupole_packet_width_bridge_cycle435_2026_07_19 as c435


c220 = c441.c220
c210 = c441.c210
c219 = c441.c437.c311.c219
c319 = c435.c319
c322 = c441.c429.c322
c396 = c435.c396
c425 = c435.c425
c432 = c435.c432

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_MASS_PASSIVE_TRAJECTORY_TOURNAMENT_CYCLE442_NOTE_2026-07-19.md"
)
AUTHORITY = "none"
AUDIT = "unset"
REGISTER_DIM = 9
SOURCE_SCALE = c441.SOURCE_SCALE
TOL = 1.2e-9
NUMERICAL_FLOOR = 8e-13
PASS = 0
FAIL = 0

# Frozen before any result row is evaluated.
BIC_ADVANTAGE = 6.0
TAIL_CV_MAXIMUM = 0.25
DURATION_RATIO_FRACTION = 0.25
CURVATURE_FLOOR_MULTIPLIER = 1000.0
MINIMUM_SECOND_DIFFERENCES = 4
WIDE_PACKET_LENGTHS = (127, 255)
WIDE_PACKET_DURATION = 40
WIDE_FORCE_GRADIENT = 1e-7


@dataclass(frozen=True)
class Geometry:
    name: str
    length: int
    source_cells: tuple[tuple[int, int, int], ...]
    receiver_cells: tuple[tuple[int, int, int], ...]
    depth: int
    arrival_tick: int
    held: bool


TRAIN = Geometry(
    "train-L7-r3-D9",
    7,
    ((0, 0, 6), (0, 0, 0), (0, 0, 1)),
    ((2, 0, 0), (3, 0, 0), (4, 0, 0)),
    9,
    3,
    False,
)
HELD = Geometry(
    "held-L11-r5-D13",
    11,
    ((0, 0, 10), (0, 0, 0), (0, 0, 1)),
    ((4, 0, 0), (5, 0, 0), (6, 0, 0)),
    13,
    5,
    True,
)
GEOMETRIES = (TRAIN, HELD)
POSITIONS = np.asarray((-1.0, 0.0, 1.0))


@dataclass(frozen=True)
class FunctionalPair:
    register_source: np.ndarray
    register_test: np.ndarray
    mass_source: np.ndarray
    mass_test: np.ndarray
    source_coin: np.ndarray
    test_coin: np.ndarray
    source_generator: sparse.csc_matrix
    test_generators: tuple[sparse.csc_matrix, ...]
    source_mass_joint: np.ndarray
    test_mass_joint: np.ndarray
    construction_events: tuple[str, ...]


@dataclass(frozen=True)
class ProjectedLaw:
    name: str
    source_mass: float
    test_mass: float
    source_coin: np.ndarray
    test_coin: np.ndarray
    source_vertex: np.ndarray
    test_vertices: tuple[np.ndarray, ...]
    lookup_rows: tuple[str, ...]


@dataclass(frozen=True)
class FitResult:
    samples: int
    linear_bic: float
    quadratic_bic: float
    linear_slope: float
    quadratic_curvature: float
    first_difference_cv: float
    second_difference_cv: float
    same_sign_second_differences: int
    duration_ratio: float
    genuine_acceleration: bool
    impulse_like: bool
    disposition: str


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


def note_contract() -> None:
    required = (
        "authority: none",
        "audit: unset",
        "source and test functional operators are constructed before sector analysis",
        "smallest fully physical a1 route",
        "arrival impulse",
        "genuine acceleration",
        "interaction-minus-free centroid",
        "four coherent sectors",
        "held alias",
        "b3",
        "b4",
        "all 24 proper-cubic frames",
        "wide operational comparator",
        "host force",
        "cycle204",
        "coordinate phase is not a lapse",
        "update count is not time",
        "receiver occupation or direction alone is not a trajectory",
        "no no-go, minimum-content, shared-obstruction, or axiom-pressure claim",
    )
    missing = required if not NOTE.exists() else tuple(
        phrase for phrase in required if phrase not in normalized(NOTE)
    )
    check("the Cycle-442 note freezes the physical trajectory tournament and semantic boundary", not missing, missing)


def validate_geometry(geometry: Geometry) -> None:
    cells = geometry.source_cells + geometry.receiver_cells
    if geometry.length < 7 or len(cells) != 6 or len(set(cells)) != 6:
        raise ValueError("A1 requires six distinct cells on L>=7")
    if geometry.arrival_tick < 1 or geometry.depth - geometry.arrival_tick < 4:
        raise ValueError("A1 requires at least four post-arrival differences")
    if any(value not in range(geometry.length) for cell in cells for value in cell):
        raise ValueError("A1 coordinate lies outside its periodic cube")


# One-particle labels across three M64 cells.  This is the same 18-column
# physical subcode used by the Cycle-435/439 receiver.
ONE_LABELS = c435.RECEIVER_LABELS
ONE_INDICES = c435.RECEIVER_INDICES
ONE_INDEX = {label: index for index, label in enumerate(ONE_LABELS)}
ONE_DIM = len(ONE_LABELS)


def register_mass(register: np.ndarray) -> np.ndarray:
    identity = np.eye(register.shape[0], dtype=complex)
    mass = 3j * (register - identity) @ np.linalg.solve(register + identity, identity)
    return np.asarray((mass + mass.conj().T) / 2, dtype=complex)


def register_common_coin(register: np.ndarray, mass: np.ndarray) -> np.ndarray:
    rest = linalg.expm(1j * mass / 3)
    return np.kron(rest, c210.P_SCALAR - c210.P_EVEN) + np.kron(
        rest @ register, c210.P_VECTOR
    )


def embed_register_coin(common: np.ndarray) -> np.ndarray:
    """Embed a register x six-direction coin into three position labels."""
    output = np.zeros((REGISTER_DIM * ONE_DIM, REGISTER_DIM * ONE_DIM), dtype=complex)
    for position in range(3):
        for left_register in range(REGISTER_DIM):
            left = slice((left_register * 3 + position) * 6, (left_register * 3 + position + 1) * 6)
            for right_register in range(REGISTER_DIM):
                right = slice((right_register * 3 + position) * 6, (right_register * 3 + position + 1) * 6)
                output[left, right] = common[
                    6 * left_register : 6 * (left_register + 1),
                    6 * right_register : 6 * (right_register + 1),
                ]
    return output


@lru_cache(maxsize=None)
def embedded_one_particle_generator(cell_index: int) -> sparse.csc_matrix:
    if cell_index not in range(3):
        raise ValueError("one-particle generator cell must be 0, 1, or 2")
    local = c441.local_exchange_generator().tocsc()
    rows: list[int] = []
    columns: list[int] = []
    values: list[complex] = []
    for matter_source, label in enumerate(ONE_LABELS):
        specs = list(c319.label_specs(label))
        local_source = c396.LOCAL_SPEC_INDEX[specs[cell_index]]
        for q_source in range(7):
            column = 7 * local_source + q_source
            targets = local[:, column].nonzero()[0]
            for target in targets:
                local_target, q_target = divmod(int(target), 7)
                target_specs = list(specs)
                target_specs[cell_index] = c322.LOCAL_LABELS[local_target]
                target_label = tuple(item for spec in target_specs for item in spec)
                if target_label not in ONE_INDEX:
                    continue
                rows.append(7 * ONE_INDEX[target_label] + q_target)
                columns.append(7 * matter_source + q_source)
                values.append(local[target, column])
    dimension = 7 * ONE_DIM
    result = sparse.coo_matrix(
        (values, (rows, columns)), shape=(dimension, dimension), dtype=complex
    ).tocsc()
    if sparse.linalg.norm(result - result.getH()) > 2e-13:
        raise RuntimeError("embedded recoil generator is not Hermitian")
    return result


def construct_functional_pair() -> FunctionalPair:
    """Construct both represented controls before any sector menu exists."""
    source_register = c220.cyclic_shift(REGISTER_DIM)
    test_register = c220.cyclic_shift(REGISTER_DIM)
    source_mass = register_mass(source_register)
    test_mass = register_mass(test_register)
    source_common = register_common_coin(source_register, source_mass)
    test_common = register_common_coin(test_register, test_mass)
    source_coin = embed_register_coin(source_common)
    test_coin = embed_register_coin(test_common)
    source_generator = embedded_one_particle_generator(1)
    test_generators = tuple(embedded_one_particle_generator(index) for index in range(3))
    source_mass_joint = np.kron(source_mass, np.eye(REGISTER_DIM))
    test_mass_joint = np.kron(np.eye(REGISTER_DIM), test_mass)
    return FunctionalPair(
        source_register,
        test_register,
        source_mass,
        test_mass,
        source_coin,
        test_coin,
        source_generator,
        test_generators,
        source_mass_joint,
        test_mass_joint,
        (
            "source-S-represented",
            "test-S-represented",
            "source-M(S)-constructed",
            "test-M(S)-constructed",
            "source/test-coins-constructed",
            "source/test-functional-generators-constructed",
        ),
    )


def sector_menu(register: np.ndarray) -> tuple[c441.Sector, ...]:
    rows = c220.register_eigenpairs(register)
    sectors = []
    for index, target in enumerate(c441.TARGET_BETAS):
        beta, _eigenvalue, vector = min(rows, key=lambda row: abs(row[0] - target))
        if abs(beta - target) > 2e-12:
            raise ValueError("represented register lacks the frozen Cycle-441 sector")
        cayley = float(-3 * np.tan(beta / 2))
        principal = float(3 * np.angle(np.exp(1j * cayley / 3)))
        sectors.append(
            c441.Sector(
                f"{'held' if index == 3 else 'train'}-sector-{index + 1}",
                beta,
                vector,
                cayley,
                principal,
                index == 3,
            )
        )
    return tuple(sectors)


def project_register_coin(operator: np.ndarray, vector: np.ndarray) -> np.ndarray:
    reshaped = operator.reshape(REGISTER_DIM, ONE_DIM, REGISTER_DIM, ONE_DIM)
    return np.einsum("a,aibj,b->ij", vector.conj(), reshaped, vector, optimize=True)


_FUNCTIONAL_VERTEX_CACHE: dict[tuple[float, int], np.ndarray] = {}


def functional_vertex(mass: float, generator: sparse.spmatrix) -> np.ndarray:
    # Generators are the four frozen embedded objects constructed before the
    # sector menu.  Caching their matrix functions does not add a beta table.
    key = (round(float(mass), 13), id(generator))
    if key not in _FUNCTIONAL_VERTEX_CACHE:
        _FUNCTIONAL_VERTEX_CACHE[key] = linalg.expm(
            1j * SOURCE_SCALE * mass * generator.toarray()
        )
    return _FUNCTIONAL_VERTEX_CACHE[key]


def projected_functional_law(
    functional: FunctionalPair,
    source_vector: np.ndarray,
    test_vector: np.ndarray,
    *,
    name: str,
    source_mass_operator: np.ndarray | None = None,
    test_mass_operator: np.ndarray | None = None,
    source_coin_operator: np.ndarray | None = None,
    test_coin_operator: np.ndarray | None = None,
    lookup_rows: tuple[str, ...] = (),
) -> ProjectedLaw:
    source_mass_matrix = functional.mass_source if source_mass_operator is None else source_mass_operator
    test_mass_matrix = functional.mass_test if test_mass_operator is None else test_mass_operator
    source_coin_matrix = functional.source_coin if source_coin_operator is None else source_coin_operator
    test_coin_matrix = functional.test_coin if test_coin_operator is None else test_coin_operator
    source_mass = float(np.vdot(source_vector, source_mass_matrix @ source_vector).real)
    test_mass = float(np.vdot(test_vector, test_mass_matrix @ test_vector).real)
    return ProjectedLaw(
        name,
        source_mass,
        test_mass,
        project_register_coin(source_coin_matrix, source_vector),
        project_register_coin(test_coin_matrix, test_vector),
        functional_vertex(source_mass, functional.source_generator),
        tuple(functional_vertex(test_mass, generator) for generator in functional.test_generators),
        lookup_rows,
    )


def table_operators(
    sectors: tuple[c441.Sector, ...], count: int
) -> tuple[np.ndarray, np.ndarray, tuple[str, ...]]:
    if count not in (3, 4):
        raise ValueError("table comparator must use B3 or B4")
    mass = np.zeros((REGISTER_DIM, REGISTER_DIM), dtype=complex)
    common = np.eye(REGISTER_DIM * 6, dtype=complex)
    included = []
    for sector in sectors[:count]:
        projector = np.outer(sector.vector, sector.vector.conj())
        mass += sector.cayley * projector
        common += np.kron(projector, c219.common_species(sector.beta).coin - np.eye(6))
        included.append(sector.name)
    return mass, embed_register_coin(common), tuple(included)


def principal_mass(functional: FunctionalPair) -> np.ndarray:
    rest = linalg.expm(1j * functional.mass_source / 3)
    result = -3j * linalg.logm(rest)
    return np.asarray((result + result.conj().T) / 2, dtype=complex)


def state_norm(state: dict[int, np.ndarray]) -> float:
    return float(sum(np.vdot(value, value).real for value in state.values()))


def state_residual(left: dict[int, np.ndarray], right: dict[int, np.ndarray]) -> float:
    zero = np.zeros((ONE_DIM, ONE_DIM), dtype=complex)
    return float(
        np.sqrt(
            sum(
                np.vdot(left.get(key, zero) - right.get(key, zero), left.get(key, zero) - right.get(key, zero)).real
                for key in left.keys() | right.keys()
            )
        )
    )


def prune(state: dict[int, np.ndarray], threshold: float = 2e-13) -> dict[int, np.ndarray]:
    return {key: value for key, value in state.items() if np.linalg.norm(value) > threshold}


def apply_matter(state: dict[int, np.ndarray], left: np.ndarray, right: np.ndarray) -> dict[int, np.ndarray]:
    return prune({key: left @ value @ right.T for key, value in state.items()})


def field_coin(state: dict[int, np.ndarray], length: int, *, inverse: bool = False) -> dict[int, np.ndarray]:
    coin = c396.c214.FIELD_COIN.conj().T if inverse else c396.c214.FIELD_COIN
    output: dict[int, np.ndarray] = {}
    for key, value in state.items():
        if key < 0 or key < length**3:
            output[key] = output.get(key, 0) + value
            continue
        cell, source_direction = c432.decode_field(key, length)
        for target_direction in range(6):
            coefficient = coin[target_direction, source_direction]
            if abs(coefficient) > 1e-15:
                target = c425.field_index(cell, target_direction, length)
                output[target] = output.get(target, 0) + coefficient * value
    return prune(output)


def field_stream(
    state: dict[int, np.ndarray], length: int, *, inverse: bool = False, enabled: bool = True
) -> dict[int, np.ndarray]:
    if not enabled:
        return {key: value.copy() for key, value in state.items()}
    return prune(
        {
            key if key < 0 else c432.stream_target(key, length, inverse=inverse): value
            for key, value in state.items()
        }
    )


def vertex_keys(cell: tuple[int, int, int], length: int) -> tuple[int, ...]:
    return (c425.reservoir_index(cell, length),) + tuple(
        c425.field_index(cell, direction, length) for direction in range(6)
    )


def apply_vertex(
    state: dict[int, np.ndarray],
    cell: tuple[int, int, int],
    length: int,
    operator: np.ndarray,
    side: str,
    *,
    inverse: bool = False,
    enabled: bool = True,
) -> dict[int, np.ndarray]:
    if not enabled:
        return {key: value.copy() for key, value in state.items()}
    active = vertex_keys(cell, length)
    zero = np.zeros((ONE_DIM, ONE_DIM), dtype=complex)
    packed = np.stack([state.get(key, zero) for key in active], axis=2)
    transformed = np.empty_like(packed)
    matrix = operator.conj().T if inverse else operator
    if side == "source":
        for test_index in range(ONE_DIM):
            transformed[:, test_index, :] = (
                matrix @ packed[:, test_index, :].reshape(-1)
            ).reshape((ONE_DIM, 7))
    elif side == "test":
        for source_index in range(ONE_DIM):
            transformed[source_index, :, :] = (
                matrix @ packed[source_index, :, :].reshape(-1)
            ).reshape((ONE_DIM, 7))
    else:
        raise ValueError("vertex side must be source or test")
    output = {key: value.copy() for key, value in state.items() if key not in active}
    for local, key in enumerate(active):
        output[key] = transformed[:, :, local]
    return prune(output)


@lru_cache(maxsize=1)
def radial_fswaps() -> tuple[np.ndarray, np.ndarray]:
    first = c319.triple_fswap(c435.LABELS, ((0, 0), (1, 1)))[np.ix_(ONE_INDICES, ONE_INDICES)].toarray()
    second = c319.triple_fswap(c435.LABELS, ((1, 0), (2, 1)))[np.ix_(ONE_INDICES, ONE_INDICES)].toarray()
    return first, second


def logical_step(
    state: dict[int, np.ndarray],
    geometry: Geometry,
    law: ProjectedLaw,
    *,
    source_enabled: bool = True,
    receiver_enabled: bool = True,
    transport_enabled: bool = True,
    packet_stream_enabled: bool = True,
    mass_law_enabled: bool = True,
) -> dict[int, np.ndarray]:
    validate_geometry(geometry)
    source_coin = law.source_coin if mass_law_enabled else np.eye(ONE_DIM)
    test_coin = law.test_coin if mass_law_enabled else np.eye(ONE_DIM)
    output = apply_matter(state, source_coin, test_coin)
    output = field_coin(output, geometry.length)
    output = apply_vertex(
        output,
        geometry.source_cells[1],
        geometry.length,
        law.source_vertex,
        "source",
        enabled=source_enabled and mass_law_enabled,
    )
    for cell, vertex in zip(geometry.receiver_cells, law.test_vertices):
        output = apply_vertex(
            output,
            cell,
            geometry.length,
            vertex,
            "test",
            enabled=receiver_enabled and mass_law_enabled,
        )
    if packet_stream_enabled:
        first, second = radial_fswaps()
        output = apply_matter(output, np.eye(ONE_DIM), first)
        output = apply_matter(output, np.eye(ONE_DIM), second)
    return field_stream(output, geometry.length, enabled=transport_enabled)


def logical_inverse(state: dict[int, np.ndarray], geometry: Geometry, law: ProjectedLaw) -> dict[int, np.ndarray]:
    output = field_stream(state, geometry.length, inverse=True)
    first, second = radial_fswaps()
    output = apply_matter(output, np.eye(ONE_DIM), second.conj().T)
    output = apply_matter(output, np.eye(ONE_DIM), first.conj().T)
    for cell, vertex in reversed(tuple(zip(geometry.receiver_cells, law.test_vertices))):
        output = apply_vertex(output, cell, geometry.length, vertex, "test", inverse=True)
    output = apply_vertex(
        output,
        geometry.source_cells[1],
        geometry.length,
        law.source_vertex,
        "source",
        inverse=True,
    )
    output = field_coin(output, geometry.length, inverse=True)
    return apply_matter(output, law.source_coin.conj().T, law.test_coin.conj().T)


def rest_packet() -> np.ndarray:
    vector = np.zeros(ONE_DIM, dtype=complex)
    vector[6:12] = c210.UNIFORM
    return vector


def initial_state(geometry: Geometry, interacting: bool) -> dict[int, np.ndarray]:
    matter = np.outer(rest_packet(), rest_packet())
    key = c425.reservoir_index(geometry.source_cells[1], geometry.length) if interacting else -1
    return {key: matter}


def packet_weights(state: dict[int, np.ndarray]) -> np.ndarray:
    weights = np.zeros(3, dtype=float)
    for value in state.values():
        for position in range(3):
            block = value[:, 6 * position : 6 * (position + 1)]
            weights[position] += float(np.vdot(block, block).real)
    return weights


def packet_moments(state: dict[int, np.ndarray]) -> dict[str, object]:
    weights = packet_weights(state)
    total = float(np.sum(weights))
    centroid = float(weights @ POSITIONS / total)
    second = float(weights @ (POSITIONS**2) / total)
    return {
        "weights": tuple(float(value) for value in weights),
        "centroid": centroid,
        "width": float(np.sqrt(max(0.0, second - centroid**2))),
        "total": total,
    }


def trace(
    geometry: Geometry,
    law: ProjectedLaw,
    *,
    interacting: bool,
    **kwargs,
) -> tuple[list[dict[str, object]], dict[int, np.ndarray], dict[int, np.ndarray]]:
    initial = initial_state(geometry, interacting)
    state = initial
    rows = []
    for tick in range(geometry.depth + 1):
        rows.append({"tick": tick, **packet_moments(state), "state_norm": state_norm(state)})
        if tick < geometry.depth:
            state = logical_step(state, geometry, law, **kwargs)
    return rows, initial, state


def safe_cv(values: np.ndarray) -> float:
    if len(values) == 0:
        return float("inf")
    scale = abs(float(np.mean(values)))
    return float(np.std(values) / scale) if scale > NUMERICAL_FLOOR else float("inf")


def bic(residual: np.ndarray, parameters: int) -> float:
    count = len(residual)
    rss = max(float(np.vdot(residual, residual).real), NUMERICAL_FLOOR**2)
    return float(count * np.log(rss / count) + parameters * np.log(count))


def classify_trace(delta: np.ndarray, geometry: Geometry) -> FitResult:
    post = np.asarray(delta[geometry.arrival_tick :], dtype=float)
    samples = len(post)
    if samples < 6:
        return FitResult(samples, float("inf"), float("inf"), 0.0, 0.0, float("inf"), float("inf"), 0, float("nan"), False, False, "unresolved-too-few-postarrival-samples")
    elapsed = np.arange(samples, dtype=float)
    linear_design = np.column_stack((np.ones(samples), elapsed))
    quadratic_design = np.column_stack((np.ones(samples), elapsed, elapsed**2))
    linear_coeff = np.linalg.lstsq(linear_design, post, rcond=None)[0]
    quadratic_coeff = np.linalg.lstsq(quadratic_design, post, rcond=None)[0]
    linear_residual = post - linear_design @ linear_coeff
    quadratic_residual = post - quadratic_design @ quadratic_coeff
    linear_bic = bic(linear_residual, 2)
    quadratic_bic = bic(quadratic_residual, 3)
    first = np.diff(post)
    second = np.diff(post, n=2)
    nonzero_second = second[np.abs(second) > CURVATURE_FLOOR_MULTIPLIER * NUMERICAL_FLOOR]
    same_sign = 0
    if len(nonzero_second):
        same_sign = int(max(np.count_nonzero(nonzero_second > 0), np.count_nonzero(nonzero_second < 0)))
    midpoint = max(1, (samples - 1) // 2)
    denominator = post[midpoint] - post[0]
    duration_ratio = float((post[-1] - post[0]) / denominator) if abs(denominator) > NUMERICAL_FLOOR else float("nan")
    first_cv = safe_cv(first[-max(3, len(first) // 2) :])
    second_cv = safe_cv(second)
    acceleration = bool(
        linear_bic - quadratic_bic > BIC_ADVANTAGE
        and abs(quadratic_coeff[2]) > CURVATURE_FLOOR_MULTIPLIER * NUMERICAL_FLOOR
        and same_sign >= MINIMUM_SECOND_DIFFERENCES
        and second_cv < TAIL_CV_MAXIMUM
        and np.isfinite(duration_ratio)
        and abs(duration_ratio - 4) < 4 * DURATION_RATIO_FRACTION
    )
    impulse = bool(
        quadratic_bic - linear_bic > BIC_ADVANTAGE
        and first_cv < TAIL_CV_MAXIMUM
        and np.isfinite(duration_ratio)
        and abs(duration_ratio - 2) < 2 * DURATION_RATIO_FRACTION
    )
    disposition = "genuine-acceleration" if acceleration else "arrival-impulse" if impulse else "transient-or-oscillatory-unresolved"
    return FitResult(
        samples,
        linear_bic,
        quadratic_bic,
        float(linear_coeff[1]),
        float(2 * quadratic_coeff[2]),
        first_cv,
        second_cv,
        same_sign,
        duration_ratio,
        acceleration,
        impulse,
        disposition,
    )


def construction_and_projection_controls(
    functional: FunctionalPair, sectors: tuple[c441.Sector, ...]
) -> None:
    print("\nFUNCTIONAL SOURCE/TEST OPERATORS BEFORE SECTOR ANALYSIS")
    source_identity = np.eye(REGISTER_DIM)
    joint_commutator = np.linalg.norm(
        functional.source_mass_joint @ functional.test_mass_joint
        - functional.test_mass_joint @ functional.source_mass_joint
    )
    menu = np.column_stack([sector.vector for sector in sectors])
    menu_gram = np.linalg.norm(menu.conj().T @ menu - np.eye(len(sectors)))
    coin_rows = []
    for sector in sectors:
        projected = project_register_coin(functional.source_coin, sector.vector)
        expected = c219.common_species(sector.beta).coin
        coin_rows.append(
            {
                "sector": sector.name,
                "mass_operator_residual": float(
                    np.linalg.norm(functional.mass_source @ sector.vector - sector.cayley * sector.vector)
                ),
                "coin_family_residual": float(np.linalg.norm(projected - np.kron(np.eye(3), expected))),
            }
        )

    # Validate one functional exponential action without constructing a table
    # of angles.  The full sparse Kronecker generator acts on an arbitrary
    # coherent register/local vector; eigenray projection is checked only
    # after that operator exists.
    rng = np.random.default_rng(44201)
    local_probe = rng.normal(size=7 * ONE_DIM) + 1j * rng.normal(size=7 * ONE_DIM)
    local_probe /= np.linalg.norm(local_probe)
    coherent_register = sum(
        ((index + 1j * (index + 1)) * sector.vector for index, sector in enumerate(sectors)),
        start=np.zeros(REGISTER_DIM, dtype=complex),
    )
    coherent_register /= np.linalg.norm(coherent_register)
    functional_generator = sparse.kron(
        sparse.csc_matrix(functional.mass_source), functional.source_generator, format="csc"
    )
    functional_output = sparse.linalg.expm_multiply(
        1j * SOURCE_SCALE * functional_generator,
        np.kron(coherent_register, local_probe),
    ).reshape(REGISTER_DIM, -1)
    projected_residuals = []
    for sector in sectors:
        amplitude = np.vdot(sector.vector, coherent_register)
        observed = sector.vector.conj() @ functional_output
        expected = amplitude * functional_vertex(sector.cayley, functional.source_generator) @ local_probe
        projected_residuals.append(float(np.linalg.norm(observed - expected)))
    check(
        "two represented S/M controls are constructed before the orthogonal sector menu and their common exponential predicts every later eigenray block",
        functional.construction_events[-1] == "source/test-functional-generators-constructed"
        and np.linalg.norm(functional.register_source - functional.register_test) == 0
        and np.linalg.norm(functional.mass_source - functional.mass_test) == 0
        and np.linalg.norm(functional.source_mass_joint - np.kron(functional.mass_source, source_identity)) == 0
        and joint_commutator == 0
        and menu_gram < 2e-14
        and max(max(row["mass_operator_residual"], row["coin_family_residual"]) for row in coin_rows) < 4e-12
        and max(projected_residuals) < 4e-12,
        {
            "construction_events_before_sector_analysis": functional.construction_events,
            "source_test_joint_mass_commutator": joint_commutator,
            "sector_menu_Gram": menu_gram,
            "projection_rows": coin_rows,
            "functional_exponential_projection_residuals": projected_residuals,
            "beta_specific_scalar_angles_used_to_construct_operator": False,
        },
    )


def build_laws(
    functional: FunctionalPair, sectors: tuple[c441.Sector, ...]
) -> dict[str, tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, tuple[str, ...]]]:
    principal = principal_mass(functional)
    b3_mass, b3_coin, b3_rows = table_operators(sectors, 3)
    b4_mass, b4_coin, b4_rows = table_operators(sectors, 4)
    return {
        "cayley-functional": (
            functional.mass_source,
            functional.mass_test,
            functional.source_coin,
            functional.test_coin,
            (),
        ),
        "principal-functional": (
            principal,
            principal.copy(),
            functional.source_coin,
            functional.test_coin,
            (),
        ),
        "lookup-B3": (b3_mass, b3_mass.copy(), b3_coin, b3_coin.copy(), b3_rows),
        "lookup-B4": (b4_mass, b4_mass.copy(), b4_coin, b4_coin.copy(), b4_rows),
    }


def make_law(
    functional: FunctionalPair,
    specification,
    source_sector: c441.Sector,
    test_sector: c441.Sector,
    name: str,
) -> ProjectedLaw:
    source_mass, test_mass, source_coin, test_coin, rows = specification
    return projected_functional_law(
        functional,
        source_sector.vector,
        test_sector.vector,
        name=name,
        source_mass_operator=source_mass,
        test_mass_operator=test_mass,
        source_coin_operator=source_coin,
        test_coin_operator=test_coin,
        lookup_rows=rows,
    )


def trace_delta(
    geometry: Geometry, law: ProjectedLaw, **kwargs
) -> tuple[np.ndarray, list[dict[str, object]], list[dict[str, object]], dict[int, np.ndarray], dict[int, np.ndarray]]:
    free, _free_initial, free_final = trace(geometry, law, interacting=False, **kwargs)
    interacting, interacting_initial, interacting_final = trace(
        geometry, law, interacting=True, **kwargs
    )
    delta = np.asarray(
        [row["centroid"] for row in interacting], dtype=float
    ) - np.asarray([row["centroid"] for row in free], dtype=float)
    return delta, free, interacting, interacting_initial, interacting_final


def a1_tournament_controls(
    functional: FunctionalPair,
    sectors: tuple[c441.Sector, ...],
    specifications,
) -> dict[str, object]:
    print("\nA1 FULLY PHYSICAL Q1 SOURCE -> RADIAL THREE-M64 PACKET TRACE")
    print(
        "FROZEN FIT CRITERIA",
        {
            "BIC_advantage": BIC_ADVANTAGE,
            "tail_CV_maximum": TAIL_CV_MAXIMUM,
            "duration_ratio_fraction": DURATION_RATIO_FRACTION,
            "curvature_floor_multiplier": CURVATURE_FLOOR_MULTIPLIER,
            "minimum_second_differences": MINIMUM_SECOND_DIFFERENCES,
            "fit_target": "interaction-minus-free centroid",
        },
    )
    rows = []
    traces: dict[tuple[str, str, str], object] = {}
    inverse_rows = []
    cases = (
        tuple(("cayley-functional", sector) for sector in sectors)
        + (("principal-functional", sectors[0]), ("principal-functional", sectors[-1]))
        + (("lookup-B3", sectors[-1]), ("lookup-B4", sectors[-1]))
    )
    for law_name, sector in cases:
        specification = specifications[law_name]
        print("A1 CASE", law_name, sector.name, flush=True)
        law = make_law(functional, specification, sector, sector, law_name)
        for geometry in GEOMETRIES:
            delta, free, interacting, initial, final = trace_delta(geometry, law)
            fit = classify_trace(delta, geometry)
            one_step = logical_step(initial, geometry, law)
            restored = logical_inverse(one_step, geometry, law)
            inverse_residual = state_residual(restored, initial)
            norm_error = max(
                max(abs(row["state_norm"] - 1) for row in free),
                max(abs(row["state_norm"] - 1) for row in interacting),
            )
            row = {
                "law": law_name,
                "sector": sector.name,
                "held_mass_sector": sector.held,
                "geometry": geometry.name,
                "held_geometry": geometry.held,
                "source_mass": law.source_mass,
                "test_mass": law.test_mass,
                "fit": asdict(fit),
                "maximum_abs_delta_centroid": float(np.max(np.abs(delta))),
                "final_delta_centroid": float(delta[-1]),
                "final_delta_width": float(interacting[-1]["width"] - free[-1]["width"]),
                "inverse_residual": inverse_residual,
                "norm_error": norm_error,
            }
            rows.append(row)
            inverse_rows.append(max(inverse_residual, norm_error))
            traces[(law_name, sector.name, geometry.name)] = {
                "free": free,
                "interacting": interacting,
                "delta_centroid": tuple(float(value) for value in delta),
            }

    # Source/test swaps are predictions of the same already-built law.
    swap_rows = []
    for source_sector, test_sector in ((sectors[0], sectors[-1]), (sectors[-1], sectors[0])):
        law = make_law(
            functional,
            specifications["cayley-functional"],
            source_sector,
            test_sector,
            "cayley-functional",
        )
        delta, _free, _interacting, _initial, _final = trace_delta(HELD, law)
        swap_rows.append(
            {
                "source_sector": source_sector.name,
                "test_sector": test_sector.name,
                "source_mass": law.source_mass,
                "test_mass": law.test_mass,
                "maximum_abs_delta_centroid": float(np.max(np.abs(delta))),
                "final_delta_centroid": float(delta[-1]),
                "fit": asdict(classify_trace(delta, HELD)),
            }
        )

    alpha = np.asarray((0.37, 0.41j, -0.52, 0.64j), dtype=complex)
    alpha /= np.linalg.norm(alpha)
    cayley_matched = [
        row
        for row in rows
        if row["law"] == "cayley-functional" and row["geometry"] == HELD.name
    ]
    coherent_inverse_bound = float(
        np.sqrt(sum(abs(alpha[index]) ** 2 * cayley_matched[index]["inverse_residual"] ** 2 for index in range(4)))
    )
    coherent_norm_bound = float(
        sum(abs(alpha[index]) ** 2 * cayley_matched[index]["norm_error"] for index in range(4))
    )
    held_rows = [row for row in rows if row["held_geometry"]]
    acceleration_rows = [row for row in held_rows if row["fit"]["genuine_acceleration"]]
    impulse_rows = [row for row in held_rows if row["fit"]["impulse_like"]]
    unresolved_rows = [
        row
        for row in held_rows
        if not row["fit"]["genuine_acceleration"] and not row["fit"]["impulse_like"]
    ]
    check(
        "the fully physical A1 tournament produces exact depth traces, inverse/norm controls, coherent held blocks, and a frozen route-specific trajectory disposition",
        len(rows) == len(cases) * 2
        and max(inverse_rows) < TOL
        and coherent_inverse_bound < TOL
        and coherent_norm_bound < TOL
        and all(len(traces[(name, sector.name, geometry.name)]["free"]) == geometry.depth + 1 for name, sector in cases for geometry in GEOMETRIES)
        and len(acceleration_rows) + len(impulse_rows) + len(unresolved_rows) == len(held_rows),
        {
            "rows": rows,
            "source_test_swap_rows": swap_rows,
            "coherent_amplitudes": alpha,
            "coherent_held_inverse_bound": coherent_inverse_bound,
            "coherent_held_norm_bound": coherent_norm_bound,
            "held_genuine_acceleration_rows": len(acceleration_rows),
            "held_impulse_rows": len(impulse_rows),
            "held_unresolved_rows": len(unresolved_rows),
            "receiver_occupation_or_direction_alone_called_trajectory": False,
        },
    )
    return {
        "rows": rows,
        "traces": traces,
        "swap_rows": swap_rows,
        "held_acceleration_rows": acceleration_rows,
        "held_impulse_rows": impulse_rows,
        "held_unresolved_rows": unresolved_rows,
    }


def deletion_controls(
    functional: FunctionalPair, sectors: tuple[c441.Sector, ...], specifications, a1
) -> None:
    print("\nA1 SOURCE / TRANSPORT / PASSIVE VERTEX / FREE STREAM / MASS DELETIONS")
    sector = sectors[1]
    law = make_law(
        functional, specifications["cayley-functional"], sector, sector, "cayley-functional"
    )
    baseline, *_ = trace_delta(HELD, law)
    deletion_rows = {}
    for name, kwargs in {
        "source": {"source_enabled": False},
        "transport": {"transport_enabled": False},
        "passive_vertex": {"receiver_enabled": False},
        "free_stream": {"packet_stream_enabled": False},
        "mass_law": {"mass_law_enabled": False},
    }.items():
        deleted, *_ = trace_delta(HELD, law, **kwargs)
        deletion_rows[name] = {
            "maximum_abs_delta": float(np.max(np.abs(deleted))),
            "state_trace_residual_from_baseline": float(np.linalg.norm(deleted - baseline)),
        }
    check(
        "source, field transport, passive receiver vertex, packet free stream, and mass-law deletions are independently visible",
        all(deletion_rows[name]["maximum_abs_delta"] < 3e-11 for name in ("source", "transport", "passive_vertex", "free_stream", "mass_law"))
        and max(abs(baseline)) > 100 * NUMERICAL_FLOOR,
        {"baseline_maximum_abs_delta": float(np.max(np.abs(baseline))), "deletions": deletion_rows},
    )


def physical_completion_vector(vector: np.ndarray, encoding: sparse.spmatrix, operator: np.ndarray, inverse: bool = False) -> np.ndarray:
    decoded = encoding.getH() @ vector
    matrix = operator.conj().T if inverse else operator
    return vector + encoding @ (matrix @ decoded - decoded)


def physical_completion_joint(matrix: np.ndarray, encoding: sparse.spmatrix, operator: np.ndarray, inverse: bool = False) -> np.ndarray:
    decoded = encoding.getH() @ matrix
    transform = operator.conj().T if inverse else operator
    moved = (transform @ decoded.reshape(-1)).reshape(decoded.shape)
    return matrix + encoding @ (moved - decoded)


def physical_eg_controls(
    functional: FunctionalPair, sectors: tuple[c441.Sector, ...], specifications
) -> None:
    print("\nA1 TRAIN/HELD PHYSICAL E/G / INVERSE / LEAKAGE")
    rng = np.random.default_rng(44202)
    rows = []
    input_embedding = c441.c311.fock_input_embedding()
    one_columns = [c441.c311.FOCK_INDEX[(1, (direction,))] for direction in range(6)]
    for length in (c441.c437.TRAIN_LENGTH, c441.c437.HELD_LENGTH):
        code = c441.c437.build_matter_code(length)
        one = np.asarray(code.constrained @ input_embedding[:, one_columns])
        full = np.asarray(code.constrained @ input_embedding)
        for law_name, sector in (
            ("cayley-functional", sectors[0]),
            ("cayley-functional", sectors[-1]),
            ("principal-functional", sectors[-1]),
            ("lookup-B3", sectors[-1]),
            ("lookup-B4", sectors[-1]),
        ):
            law = make_law(functional, specifications[law_name], sector, sector, law_name)
            coin = law.test_coin[:6, :6]
            logical = rng.normal(size=6) + 1j * rng.normal(size=6)
            logical /= np.linalg.norm(logical)
            physical = one @ logical
            decoded = one.conj().T @ physical
            coin_physical = physical + one @ (coin @ decoded - decoded)
            coin_expected = one @ (coin @ logical)
            inverse_decoded = one.conj().T @ coin_physical
            coin_restored = coin_physical + one @ (coin.conj().T @ inverse_decoded - inverse_decoded)

            local_vertex = c322.local_source_blocks(SOURCE_SCALE * law.test_mass)[1]
            joint = rng.normal(size=(64, 7)) + 1j * rng.normal(size=(64, 7))
            joint /= np.linalg.norm(joint)
            physical_joint = full @ joint
            decoded_joint = full.conj().T @ physical_joint
            moved = (local_vertex @ decoded_joint.reshape(-1)).reshape((64, 7))
            vertex_physical = physical_joint + full @ (moved - decoded_joint)
            vertex_expected = full @ moved
            inverse_joint = full.conj().T @ vertex_physical
            restored_logical = (local_vertex.conj().T @ inverse_joint.reshape(-1)).reshape((64, 7))
            vertex_restored = vertex_physical + full @ (restored_logical - inverse_joint)
            rows.append(
                {
                    "compiler_length": length,
                    "held": length == c441.c437.HELD_LENGTH,
                    "law": law_name,
                    "sector": sector.name,
                    "one_encoding_shape": one.shape,
                    "full_encoding_shape": full.shape,
                    "support_M2": code.matter_union_m2,
                    "one_Gram": float(np.linalg.norm(one.conj().T @ one - np.eye(6))),
                    "full_Gram": float(np.linalg.norm(full.conj().T @ full - np.eye(64))),
                    "coin_EG": float(np.linalg.norm(coin_physical - coin_expected)),
                    "coin_inverse": float(np.linalg.norm(coin_restored - physical)),
                    "coin_leakage": float(np.linalg.norm(coin_physical - one @ (one.conj().T @ coin_physical))),
                    "vertex_EG": float(np.linalg.norm(vertex_physical - vertex_expected)),
                    "vertex_inverse": float(np.linalg.norm(vertex_restored - physical_joint)),
                    "vertex_leakage": float(np.linalg.norm(vertex_physical - full @ (full.conj().T @ vertex_physical))),
                }
            )
    check(
        "train/held local M64 factors have exact functional coin/source E/G, inverse, Gram, and leakage controls before composition into the inherited physical three-cell shell",
        max(value for row in rows for key, value in row.items() if key in ("one_Gram", "full_Gram", "coin_EG", "coin_inverse", "coin_leakage", "vertex_EG", "vertex_inverse", "vertex_leakage")) < TOL,
        {
            "rows": rows,
            "three_cell_FSWAP_physical_compiler": "inherited Cycle319/435, rotated family checked separately below",
            "primitive_dense_completion": "supplied/open",
            "global_tensor_materialized": False,
        },
    )


def covariance_mass_contact_controls(
    functional: FunctionalPair, sectors: tuple[c441.Sector, ...], specifications
) -> None:
    print("\nALL-24 COVARIANCE / MASS / CONTACT")
    sector = sectors[1]
    law = make_law(
        functional, specifications["cayley-functional"], sector, sector, "cayley-functional"
    )

    frame_rows = []
    first, second = radial_fswaps()
    for frame in c210.proper_cubic_frames():
        direction = c210.direction_permutation(frame)
        matter = np.kron(np.eye(3), direction)
        field = linalg.block_diag(np.ones((1, 1)), direction)
        joint = np.kron(matter, field)
        coin_residual = max(
            np.linalg.norm(matter @ law.source_coin @ matter.conj().T - law.source_coin),
            np.linalg.norm(matter @ law.test_coin @ matter.conj().T - law.test_coin),
        )
        vertex_residual = max(
            np.linalg.norm(joint @ law.source_vertex @ joint.conj().T - law.source_vertex),
            *(np.linalg.norm(joint @ item @ joint.conj().T - item) for item in law.test_vertices),
        )
        mapped_plus = int(np.argmax(direction[:, 0]))
        mapped_minus = int(np.argmax(direction[:, 1]))
        mapped_first = c319.triple_fswap(c435.LABELS, ((0, mapped_plus), (1, mapped_minus)))[np.ix_(ONE_INDICES, ONE_INDICES)].toarray()
        mapped_second = c319.triple_fswap(c435.LABELS, ((1, mapped_plus), (2, mapped_minus)))[np.ix_(ONE_INDICES, ONE_INDICES)].toarray()
        fswap_residual = max(
            np.linalg.norm(matter @ first @ matter.conj().T - mapped_first),
            np.linalg.norm(matter @ second @ matter.conj().T - mapped_second),
        )
        frame_rows.append((coin_residual, vertex_residual, fswap_residual))

    _updates, _coin, _first, _second, contact, _forward, _reverse = c319.update_controls(c435.LABELS, "path")
    restricted_contact = contact[np.ix_(ONE_INDICES, ONE_INDICES)]
    contact_one_residual = sparse.linalg.norm(restricted_contact - sparse.eye(ONE_DIM, format="csc"))
    full_diagonal = contact.diagonal()
    nontrivial_contact_columns = int(np.count_nonzero(abs(full_diagonal - 1) > 1e-13))
    mass_fixture = c219.common_species(sector.beta).analytic_mass
    check(
        "the functional source/test law, radial FSWAP family, mass fixture, and inherited contact are proper-cubic and preserve the one-particle code in all 24 frames",
        len(frame_rows) == 24
        and max(max(row) for row in frame_rows) < 4e-11
        and abs(mass_fixture - sector.cayley) < 3e-13
        and contact_one_residual < 2e-13
        and nontrivial_contact_columns == 645,
        {
            "frames": len(frame_rows),
            "maximum_coin_covariance": max(row[0] for row in frame_rows),
            "maximum_vertex_covariance": max(row[1] for row in frame_rows),
            "maximum_radial_FSWAP_covariance": max(row[2] for row in frame_rows),
            "mass_fixture": mass_fixture,
            "one_particle_contact_residual": float(contact_one_residual),
            "full_code_nontrivial_contact_columns": nontrivial_contact_columns,
        },
    )


def wide_packet_trace(
    species: c210.Species, force: float, length: int
) -> dict[str, object]:
    positions, momenta, interacting = c210.prepare_molecular_packet(
        species, length, 0.04
    )
    free = interacting.copy()
    start_interacting = c210.mean_position(interacting, positions)
    start_free = c210.mean_position(free, positions)
    interacting_centres = [start_interacting]
    free_centres = [start_free]
    half = np.exp(0.5j * force * positions)[:, None]
    for _ in range(WIDE_PACKET_DURATION):
        interacting = half * c210.local_molecular_step(half * interacting, species.coin)
        free = c210.local_molecular_step(free, species.coin)
        interacting_centres.append(c210.mean_position(interacting, positions))
        free_centres.append(c210.mean_position(free, positions))
    delta = np.asarray(interacting_centres) - np.asarray(free_centres)
    dummy = Geometry(
        "operational-host-force", 7, TRAIN.source_cells, TRAIN.receiver_cells, WIDE_PACKET_DURATION, 0, length == WIDE_PACKET_LENGTHS[-1]
    )
    density = c210.position_density(interacting)
    return {
        "delta_centroid": tuple(float(value) for value in delta),
        "fit": asdict(classify_trace(delta, dummy)),
        "norm": float(np.linalg.norm(interacting)),
        "band_probability": c210.branch_probability(interacting, momenta, species),
        "boundary": float(np.sum(density[np.abs(positions) > length / 4])),
        "final_displacement": float(delta[-1]),
    }


def wide_operational_comparator(
    sectors: tuple[c441.Sector, ...], specifications, functional: FunctionalPair
) -> dict[str, object]:
    print("\nWIDE N127/N255 OPERATIONAL HOST-FORCE COMPARATOR")
    rows = []
    pairs = tuple((sector, sector) for sector in sectors) + (
        (sectors[0], sectors[-1]),
        (sectors[-1], sectors[0]),
    )
    for source_sector, test_sector in pairs:
        for law_name in ("cayley-functional", "principal-functional"):
            law = make_law(
                functional,
                specifications[law_name],
                source_sector,
                test_sector,
                law_name,
            )
            species = c219.common_species(test_sector.beta)
            force = WIDE_FORCE_GRADIENT * law.source_mass * law.test_mass
            for length in WIDE_PACKET_LENGTHS:
                result = wide_packet_trace(species, force, length)
                fit = result["fit"]
                # This is deliberately not the A1 genuine-acceleration label.
                # The supplied-force lane is a comparator for the quadratic
                # envelope of a wide packet.  Its exact QCA trace retains
                # finite-step micromotion and can therefore fail the frozen
                # pointwise second-difference CV gate even when the envelope
                # wins decisively and has the expected duration scaling.
                quadratic_envelope = bool(
                    fit["linear_bic"] - fit["quadratic_bic"] > BIC_ADVANTAGE
                    and abs(fit["quadratic_curvature"])
                    > CURVATURE_FLOOR_MULTIPLIER * NUMERICAL_FLOOR
                    and fit["first_difference_cv"] < TAIL_CV_MAXIMUM
                    and np.isfinite(fit["duration_ratio"])
                    and abs(fit["duration_ratio"] - 4)
                    < 4 * DURATION_RATIO_FRACTION
                )
                rows.append(
                    {
                        "law": law_name,
                        "source_sector": source_sector.name,
                        "test_sector": test_sector.name,
                        "length": length,
                        "held_size": length == WIDE_PACKET_LENGTHS[-1],
                        "source_mass": law.source_mass,
                        "passive_mass": law.test_mass,
                        "independent_coin_inertia": species.analytic_mass,
                        "supplied_force_per_tick": force,
                        "supplied_onsite_profile": "exp(+i F x/2) before and after every free update",
                        "quadratic_envelope": quadratic_envelope,
                        "strict_pointwise_acceleration": fit["genuine_acceleration"],
                        **result,
                    }
                )
    held = [row for row in rows if row["held_size"]]
    held_envelopes = [row for row in held if row["quadratic_envelope"]]
    held_strict = [row for row in held if row["strict_pointwise_acceleration"]]
    check(
        "the wide packet comparator supplies a per-update force/profile and gives a held quadratic envelope with reported finite-step micromotion, without calling it strict pointwise acceleration or promoting the source/field to physical M2",
        len(rows) == len(pairs) * 2 * 2
        and max(abs(row["norm"] - 1) for row in rows) < 3e-12
        and min(row["band_probability"] for row in rows) > 0.98
        and max(row["boundary"] for row in held) < 0.02
        and len(held_envelopes) > 0
        and len(held_strict) == 0,
        {
            "rows": rows,
            "held_quadratic_envelope_rows": len(held_envelopes),
            "held_strict_pointwise_acceleration_rows": len(held_strict),
            "physical_source_compiler": False,
            "physical_field_compiler": False,
            "host_force_profile_supplied_each_update": True,
            "update_count_called_time": False,
        },
    )
    return {"rows": rows}


def cycle204_prediction_ledger() -> dict[str, object]:
    print("\nEXACT CYCLE-204 PREDICTION LEDGER")
    hamiltonian = (
        (0.25, 1.0000, 1.0024),
        (0.40, 1.0000, 0.9988),
        (0.65, 1.0000, 0.9985),
    )
    strict_qca = (
        (0.25, 0.9786, 0.9808),
        (0.40, 0.9429, 0.9422),
        (0.65, 0.8273, 0.8268),
    )
    source_mass = 0.65
    qca_accelerations = tuple(
        float(source_mass * np.sqrt(1 - mass**2)) for mass, _predicted, _measured in strict_qca
    )
    ledger = {
        "Hamiltonian_a_over_g_rows": hamiltonian,
        "strict_QCA_a_over_g_rows": strict_qca,
        "source_mass_0p65_Hamiltonian_accelerations": (0.65, 0.65, 0.65),
        "source_mass_0p65_QCA_accelerations": qca_accelerations,
        "bound_composite_U_rows": (
            (0.4, 1.193),
            (0.7, 1.111),
            (1.0, 1.000),
            (1.5, 0.789),
            (2.0, 0.581),
        ),
        "exact_legacy_Hamiltonian_rows_reproduced": False,
        "exact_legacy_QCA_rows_reproduced": False,
        "exact_bound_composite_rows_reproduced": False,
        "linear_additive_source_amplitude_reproduced_at_finite_coupling": False,
        "linear_source_generator_derivative_present": True,
        "reason": "Cycle442 uses the four Cycle441 register sectors and physical recoil/operational comparator laws, not the Cycle202 m=.25/.4/.65 legacy packet fixtures or the Cycle204 composite fixture",
    }
    check(
        "every exact Cycle204 numeric row is retained as a comparison and none is silently claimed by the new mass menu",
        ledger["source_mass_0p65_Hamiltonian_accelerations"] == (0.65, 0.65, 0.65)
        and np.allclose(qca_accelerations, (0.6293597937587053, 0.5957348403442592, 0.49395723499104655))
        and not ledger["exact_legacy_Hamiltonian_rows_reproduced"]
        and not ledger["exact_legacy_QCA_rows_reproduced"]
        and not ledger["exact_bound_composite_rows_reproduced"],
        ledger,
    )
    return ledger


def law_deletion_and_domain_controls(
    functional: FunctionalPair, sectors: tuple[c441.Sector, ...], specifications
) -> None:
    print("\nFUNCTIONAL / LOOKUP / LAWFUL-DOMAIN CONTROLS")
    held = sectors[-1]
    cayley = make_law(
        functional, specifications["cayley-functional"], held, held, "cayley-functional"
    )
    principal = make_law(
        functional, specifications["principal-functional"], held, held, "principal-functional"
    )
    b3 = make_law(functional, specifications["lookup-B3"], held, held, "lookup-B3")
    b4 = make_law(functional, specifications["lookup-B4"], held, held, "lookup-B4")
    rejections = 0
    for probe in (
        lambda: embedded_one_particle_generator(3),
        lambda: validate_geometry(Geometry("bad", 6, TRAIN.source_cells, TRAIN.receiver_cells, 9, 3, False)),
        lambda: table_operators(sectors, 2),
        lambda: c441.validate_register_code_mask(0),
        lambda: c441.validate_register_code_mask(3),
    ):
        try:
            probe()
        except ValueError:
            rejections += 1
    check(
        "principal/Cayley and B3/B4 dependencies remain distinct while malformed register, geometry, table, and local-cell domains are rejected",
        abs(cayley.source_mass - held.cayley) < 3e-12
        and abs(principal.source_mass - held.principal) < 3e-12
        and abs(b3.source_mass) < 3e-12
        and abs(b4.source_mass - held.cayley) < 3e-12
        and np.linalg.norm(cayley.source_coin - b4.source_coin) < 3e-12
        and rejections == 5,
        {
            "held_cayley": cayley.source_mass,
            "held_principal": principal.source_mass,
            "held_B3": b3.source_mass,
            "held_B4": b4.source_mass,
            "B3_rows": b3.lookup_rows,
            "B4_rows": b4.lookup_rows,
            "lawful_domain_rejections": rejections,
        },
    )


def inventory_controls(a1, wide, cycle204) -> None:
    inventory = {
        "supplied": (
            "two nine-M2 Q=1 cyclic registers, internal orientation/population, Cayley/principal matrix functions, SOURCE_SCALE=.05, and dense bounded functional controls",
            "two disjoint three-M64 shells, physical code completions, radial cell coordinates, scalar-rest source/test preparation, and factor order",
            "one prepared Q1 source reservoir, blank remaining field, Cycle425 field coin/stream, and no-refresh finite periodic boundary",
            "arrival ticks, depths, centroid/width effects, BIC/CV/scaling thresholds, numerical floor, and train/held split",
            "wide comparator packet widths/lengths/duration and its per-update linear onsite phase profile",
        ),
        "derived": (
            "two source/test functional laws constructed before sector analysis and their four coherent eigenray predictions",
            "fully joint physical Q1 source/receiver depth traces with free subtraction, exact inverse/norm, deletions, held geometry, and fit disposition",
            "factorwise physical E/G, inverse, leakage, all24 covariance, mass/contact, B3/B4, swap, and lawful-domain controls",
            "wide operational trajectory comparator and exact Cycle204 reproduced/not-reproduced ledger",
        ),
        "open": (
            "a wide fully physical M64 packet compiler with a sustained autonomous source and stable held quadratic trajectory",
            "physical preparation of a mass-conditioned Cycle425 dressed source and stationarity under the joined test interaction",
            "matched physical clock/Record protocol, lapse/proper-time bridge, physical time, energy/stress/source calibration, metric, and gravity",
            "Born/occurrence/realized-history selection and empirical choice of register/mass law/coupling",
        ),
        "A2_executed": False,
        "A2_reason": "the inherited dressed eigenstate requires global host selection/preparation and is not stationary under the new receiver gate; A1 and the operator audits are completed without silently importing its Green amplitude",
        "clock_or_lapse_constructed": False,
        "coordinate_phase_called_lapse": False,
        "proper_time_constructed": False,
        "update_count_called_time": False,
        "occupation_called_energy_or_gravity": False,
        "receiver_weight_called_trajectory": False,
        "actual_Record": False,
        "Born_claim": False,
        "authority": AUTHORITY,
        "audit": AUDIT,
        "no_go": False,
        "minimum_content": False,
        "shared_obstruction": False,
        "axiom_pressure": False,
    }
    check(
        "the supplied/derived/open inventory preserves the trajectory, clock, resource, and constitutional boundary",
        AUTHORITY == "none"
        and AUDIT == "unset"
        and not inventory["clock_or_lapse_constructed"]
        and not inventory["coordinate_phase_called_lapse"]
        and not inventory["proper_time_constructed"]
        and not inventory["update_count_called_time"]
        and not inventory["occupation_called_energy_or_gravity"]
        and not inventory["receiver_weight_called_trajectory"]
        and not inventory["no_go"]
        and not inventory["minimum_content"]
        and not inventory["shared_obstruction"]
        and not inventory["axiom_pressure"],
        {
            "inventory": inventory,
            "A1_held_acceleration_rows": len(a1["held_acceleration_rows"]),
            "A1_held_impulse_rows": len(a1["held_impulse_rows"]),
            "A1_held_unresolved_rows": len(a1["held_unresolved_rows"]),
            "wide_rows": len(wide["rows"]),
            "Cycle204_exact_rows_reproduced": any(
                cycle204[key]
                for key in (
                    "exact_legacy_Hamiltonian_rows_reproduced",
                    "exact_legacy_QCA_rows_reproduced",
                    "exact_bound_composite_rows_reproduced",
                )
            ),
        },
    )


def main() -> int:
    print("CYCLE 442: PHYSICAL COMMON-MASS PASSIVE-TRAJECTORY TOURNAMENT")
    note_contract()

    # This ordering is part of the scientific contract.
    functional = construct_functional_pair()
    construction_snapshot = functional.construction_events
    sectors = sector_menu(functional.register_source)
    if construction_snapshot != functional.construction_events:
        raise RuntimeError("sector analysis mutated the preconstructed functional law")

    construction_and_projection_controls(functional, sectors)
    specifications = build_laws(functional, sectors)
    law_deletion_and_domain_controls(functional, sectors, specifications)
    a1 = a1_tournament_controls(functional, sectors, specifications)
    deletion_controls(functional, sectors, specifications, a1)
    physical_eg_controls(functional, sectors, specifications)
    covariance_mass_contact_controls(functional, sectors, specifications)
    wide = wide_operational_comparator(sectors, specifications, functional)
    cycle204 = cycle204_prediction_ledger()
    inventory_controls(a1, wide, cycle204)
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL, "authority": AUTHORITY, "audit": AUDIT})
    if FAIL:
        print("RESULT PHYSICAL_MASS_PASSIVE_TRAJECTORY_TOURNAMENT_NOT_CERTIFIED")
        return 1
    print("RESULT PHYSICAL_MASS_PASSIVE_TRAJECTORY_TOURNAMENT_CERTIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
