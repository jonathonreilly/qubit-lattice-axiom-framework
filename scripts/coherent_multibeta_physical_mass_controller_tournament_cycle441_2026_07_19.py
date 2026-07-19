#!/usr/bin/env python3
"""Cycle 441: coherent multi-beta physical mass-controller tournament.

Physicalize the Cycle-220 nine-state phase register as the complete Q=1
sector of nine hard-core M2 on an internally oriented ring.  Construct a
common physical M64 x register coin and clock/source controls from matrix
functions of the represented register before any spectral preparation.
Compare that functional route with explicit three- and four-entry lookup
controls on coherent superpositions of four beta/rest sectors.

The one-hot population, nine-cycle orientation, matrix functions, conversion
scales, dense bounded completions, preparation, and factor order are supplied.
Update count is not time, phase is not energy, a latch is not a Record, and
active recoil is not gravity.  Authority is none; audit is unset.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
import inspect
from pathlib import Path
import sys

import numpy as np
from scipy import linalg, sparse
from scipy.sparse.linalg import expm_multiply


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import generated_beta_phase_register_cycle220_2026_07_16 as c220
import physical_matter_inertia_clock_composition_bridge_cycle437_2026_07_19 as c437
import physical_mass_clock_active_source_receiver_tournament_cycle438_2026_07_19 as c438


c311 = c437.c311
c429 = c438.c429
c428 = c437.c428
c210 = c220.c210

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "COHERENT_MULTIBETA_PHYSICAL_MASS_CONTROLLER_TOURNAMENT_CYCLE441_NOTE_2026-07-19.md"
)
SOURCES = {
    "cycle220": ROOT / "docs/work_history/repo/review_feedback/GENERATED_BETA_PHASE_REGISTER_CYCLE220_NOTE_2026-07-16.md",
    "cycle221": ROOT / "docs/work_history/repo/review_feedback/OPERATOR_MASS_EQUIVALENCE_CYCLE221_NOTE_2026-07-17.md",
    "cycle311": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_CYCLE269_COMMON_M64_FIXED_SEAM_CYCLE311_NOTE_2026-07-18.md",
    "cycle437": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_MATTER_INERTIA_CLOCK_COMPOSITION_BRIDGE_CYCLE437_NOTE_2026-07-19.md",
    "cycle438": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_MASS_CLOCK_ACTIVE_SOURCE_RECEIVER_TOURNAMENT_CYCLE438_NOTE_2026-07-19.md",
}

AUTHORITY = "none"
AUDIT = "unset"
REGISTER_DIM = 9
CLOCK_SCALE = 8.0
SOURCE_SCALE = 0.05
DEPTH = 3
TOL = 2.5e-9
PASS = 0
FAIL = 0
CONSTRUCTION_EVENTS: list[str] = []

TARGET_BETAS = (-2 * np.pi / 9, -4 * np.pi / 9, -2 * np.pi / 3, -8 * np.pi / 9)
TRAIN_COUNT = 3
REGISTER_SWAP_SCHEDULE = tuple((site, site + 1) for site in reversed(range(REGISTER_DIM - 1)))


@dataclass(frozen=True)
class FunctionalRoute:
    register: np.ndarray
    cayley_mass: np.ndarray
    rest_unitary: np.ndarray
    principal_mass: np.ndarray
    common_coin: np.ndarray
    cayley_clock: np.ndarray
    principal_clock: np.ndarray


@dataclass(frozen=True)
class Sector:
    name: str
    beta: float
    vector: np.ndarray
    cayley: float
    principal: float
    held: bool


@dataclass(frozen=True)
class LookupRoute:
    name: str
    mass: np.ndarray
    common_coin: np.ndarray
    included: tuple[str, ...]


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
    required = (
        "authority: none",
        "audit: unset",
        "positive coherent multi-beta physical tournament",
        "complete q=1 sector of nine hard-core m2",
        "one common physical m64 x register coin",
        "route a: operator functional calculus",
        "route b: explicit finite lookup table",
        "constructed before spectral analysis",
        "four coherent beta/rest sectors",
        "held alias prediction without refit",
        "principal-phase and cayley coordinates remain unselected",
        "basis rays and coherent superpositions",
        "exact e/g and inverse",
        "all 24 proper-cubic frames",
        "q=0 and q=2",
        "mass-observable, functional-law, controller-source, clock, and receiver deletions",
        "cycle-219 mass fixture",
        "cycle-230 contact block",
        "primitive synthesis remains open",
        "update count is not time",
        "phase is not energy",
        "latch is not a record",
        "active recoil is not gravity",
        "no no-go, minimum-content, shared-obstruction, or axiom-pressure claim",
    )
    missing = required if not NOTE.exists() else tuple(
        phrase for phrase in required if phrase not in normalized(NOTE)
    )
    check("the Cycle-441 note freezes the coherent physical tournament and semantic boundary", not missing, missing)

    source = {name: normalized(path) for name, path in SOURCES.items()}
    check(
        "the cited bridge stack distinguishes the abstract generated register, physical M64 code, and beta-specific predecessor",
        all(path.is_file() for path in SOURCES.values())
        and "one fixed phase-register law" in source["cycle220"]
        and "nine-state block or strict one-qubit nearest-neighbour encoding" in source["cycle221"]
        and "complete 64-dimensional input code" in source["cycle311"]
        and "held alias sector" in source["cycle437"]
        and "precomputed beta-specific scalar" in source["cycle438"],
        {
            "abstract_near_side": "Cycle220/221 S and M(S)",
            "physical_near_side": "Cycle311 constrained M64 plus literal nine-M2 Q=1 register",
            "predecessor_limit": "Cycle438 scalar theta supplied separately per beta",
        },
    )


def validate_register(register: np.ndarray) -> None:
    if register.ndim != 2 or register.shape[0] != register.shape[1]:
        raise ValueError("phase register must be one square matrix")
    if register.shape[0] % 2 == 0:
        raise ValueError("declared Cayley register must have odd dimension")
    if not np.all(np.isfinite(register)):
        raise ValueError("phase register must be finite")
    identity = np.eye(register.shape[0], dtype=complex)
    if np.linalg.norm(register.conj().T @ register - identity) > 2e-11:
        raise ValueError("phase register must be unitary")
    if np.linalg.svd(register + identity, compute_uv=False)[-1] < 1e-10:
        raise ValueError("Cayley register cannot contain eigenvalue -1")


def functional_route(register: np.ndarray) -> FunctionalRoute:
    """Construct Route A solely from the represented operator, before sectors."""
    validate_register(register)
    identity = np.eye(register.shape[0], dtype=complex)
    mass = 3j * (register - identity) @ np.linalg.solve(register + identity, identity)
    mass = (mass + mass.conj().T) / 2
    rest = linalg.expm(1j * mass / 3)
    principal = -3j * linalg.logm(rest)
    principal = np.asarray((principal + principal.conj().T) / 2, dtype=complex)
    common = np.kron(rest, c210.P_SCALAR - c210.P_EVEN) + np.kron(
        rest @ register, c210.P_VECTOR
    )
    result = FunctionalRoute(
        register,
        mass,
        rest,
        principal,
        common,
        linalg.expm(1j * mass / CLOCK_SCALE),
        linalg.expm(1j * principal / CLOCK_SCALE),
    )
    CONSTRUCTION_EVENTS.append("functional-route-built")
    return result


def sector_menu(register: np.ndarray) -> tuple[Sector, ...]:
    if CONSTRUCTION_EVENTS != ["functional-route-built"]:
        raise RuntimeError("Route A must be constructed before spectral analysis")
    rows = c220.register_eigenpairs(register)
    sectors = []
    for index, target in enumerate(TARGET_BETAS):
        beta, _eigenvalue, vector = min(rows, key=lambda row: abs(row[0] - target))
        if abs(beta - target) > 2e-12:
            raise ValueError("the nine-cycle does not contain the frozen beta menu")
        cayley = float(-3 * np.tan(beta / 2))
        principal = float(3 * np.angle(np.exp(1j * cayley / 3)))
        sectors.append(
            Sector(
                f"{'held' if index == 3 else 'train'}-sector-{index + 1}",
                beta,
                vector,
                cayley,
                principal,
                index == 3,
            )
        )
    CONSTRUCTION_EVENTS.append("spectral-menu-built")
    return tuple(sectors)


def lookup_route(sectors: tuple[Sector, ...], count: int) -> LookupRoute:
    if count not in (TRAIN_COUNT, len(sectors)):
        raise ValueError("lookup route must contain the three train rows or all four rows")
    mass = np.zeros((REGISTER_DIM, REGISTER_DIM), dtype=complex)
    common = np.eye(REGISTER_DIM * 6, dtype=complex)
    included = []
    for sector in sectors[:count]:
        projector = np.outer(sector.vector, sector.vector.conj())
        mass += sector.cayley * projector
        common += np.kron(projector, c437.c311.c219.common_species(sector.beta).coin - np.eye(6))
        included.append(sector.name)
    return LookupRoute(f"lookup-{count}", mass, common, tuple(included))


def validate_register_code_mask(mask: int) -> int:
    if not isinstance(mask, int) or mask < 0 or mask >= 1 << REGISTER_DIM:
        raise ValueError("register occupation mask is outside nine M2")
    if mask.bit_count() != 1:
        raise ValueError("mass-controller register requires exactly Q=1")
    return mask.bit_length() - 1


def register_ring_controls(register: np.ndarray, sectors: tuple[Sector, ...]) -> None:
    print("\nNINE-M2 Q=1 REGISTER / RING SCHEDULE / DOMAIN")
    schedule = np.eye(REGISTER_DIM, dtype=complex)
    for left, right in REGISTER_SWAP_SCHEDULE:
        swap = np.eye(REGISTER_DIM, dtype=complex)
        swap[[left, right]] = swap[[right, left]]
        schedule = swap @ schedule

    def shift_mask(mask: int) -> int:
        return sum(((mask >> source) & 1) << ((source + 1) % REGISTER_DIM) for source in range(REGISTER_DIM))

    q0 = shift_mask(0)
    q2 = tuple(shift_mask((1 << left) | (1 << right)) for left in range(REGISTER_DIM) for right in range(left + 1, REGISTER_DIM))
    menu = np.column_stack([sector.vector for sector in sectors])
    gram = np.linalg.norm(menu.conj().T @ menu - np.eye(len(sectors)))
    deleted = menu.copy()
    deleted[0, 0] = 0
    deleted_gram = np.linalg.norm(deleted.conj().T @ deleted - np.eye(len(sectors)))
    check(
        "the internally oriented nine-M2 ring gives one exact Q=1 register while Q=0/Q=2 are preserved by S but rejected by the mass-control code",
        np.linalg.norm(schedule - register) < 2e-14
        and q0 == 0
        and len(set(q2)) == 36
        and all(mask.bit_count() == 2 for mask in q2)
        and tuple(validate_register_code_mask(1 << site) for site in range(REGISTER_DIM)) == tuple(range(REGISTER_DIM))
        and gram < 2e-14
        and deleted_gram > 0.05,
        {
            "register_M2": REGISTER_DIM,
            "declared_code": "complete Q=1 sector of nine hard-core M2",
            "ring_orientation": "site j maps to j+1 modulo 9",
            "nearest_neighbor_SWAP_schedule": REGISTER_SWAP_SCHEDULE,
            "Q0_fixed": q0 == 0,
            "Q2_states_preserved": len(set(q2)),
            "menu_Gram_residual": gram,
            "deleted_amplitude_Gram_residual": deleted_gram,
            "one_hot_population_preparation": "supplied/open",
            "ring_orientation_derived_from_cubic_geometry": False,
        },
    )


def anti_lookup_controls(route: FunctionalRoute, sectors: tuple[Sector, ...], b3: LookupRoute, b4: LookupRoute) -> None:
    print("\nROUTE-A FUNCTIONAL DEPENDENCIES / ROUTE-B LOOKUP COMPARATOR")
    source = inspect.getsource(functional_route).lower()
    forbidden = ("register_eigenpairs", "target_betas", "sector_menu", "lookup_route", "np.outer")
    menu = np.column_stack([sector.vector for sector in sectors])
    projector = menu @ menu.conj().T
    a_on_menu = projector @ route.cayley_mass @ projector
    b3_train = np.column_stack([sector.vector for sector in sectors[:3]])
    held = sectors[-1].vector
    check(
        "Route A is constructed by operator functional calculus before spectral analysis, whereas B3/B4 are explicit projector tables",
        not any(token in source for token in forbidden)
        and CONSTRUCTION_EVENTS == ["functional-route-built", "spectral-menu-built"]
        and np.linalg.norm(a_on_menu - projector @ b4.mass @ projector) < 2e-12
        and np.linalg.norm(
            b3_train.conj().T @ (route.cayley_mass - b3.mass) @ b3_train
        ) < 2e-12
        and abs(np.vdot(held, b3.mass @ held)) < 2e-12
        and abs(np.vdot(held, route.cayley_mass @ held) - sectors[-1].cayley) < 2e-12,
        {
            "construction_events": tuple(CONSTRUCTION_EVENTS),
            "Route_A_forbidden_dependency_hits": tuple(token for token in forbidden if token in source),
            "Route_A_formula": "M=3i(S-I)(S+I)^-1; functions by solve/logm/expm/Kronecker",
            "Route_B3_rows": b3.included,
            "Route_B4_rows": b4.included,
            "B3_held_coordinate": complex(np.vdot(held, b3.mass @ held)),
            "A_held_coordinate": complex(np.vdot(held, route.cayley_mass @ held)),
            "primitive_matrix_function_synthesis": "supplied/open",
        },
    )


def matter_code():
    code = c437.build_matter_code(c437.HELD_LENGTH)
    input_embedding = c311.fock_input_embedding()
    one_indices = [c311.FOCK_INDEX[(1, (direction,))] for direction in range(6)]
    one = code.constrained @ input_embedding[:, one_indices]
    full = code.constrained @ input_embedding
    rest = np.ones(6, dtype=complex) / np.sqrt(6)
    return code, one, full, rest


def encode_direction(logical: np.ndarray, encoding: np.ndarray) -> np.ndarray:
    return logical @ encoding.T


def decode_direction(physical: np.ndarray, encoding: np.ndarray) -> np.ndarray:
    return physical @ encoding.conj()


def physical_completion(
    physical: np.ndarray, encoding: np.ndarray, operator: np.ndarray, *, inverse: bool = False
) -> np.ndarray:
    decoded = decode_direction(physical, encoding)
    matrix = operator.conj().T if inverse else operator
    transformed = (matrix @ decoded.reshape(-1)).reshape(decoded.shape)
    return physical + encode_direction(transformed - decoded, encoding)


def array_residual(left: np.ndarray, right: np.ndarray) -> float:
    return float(np.linalg.norm(left - right))


def array_norm(value: np.ndarray) -> float:
    return float(np.vdot(value, value).real)


def common_coin_physical_controls(
    route: FunctionalRoute, sectors: tuple[Sector, ...], code, one: np.ndarray, rest: np.ndarray
) -> None:
    print("\nCOMMON PHYSICAL M64 x REGISTER COIN / COHERENT E-G")
    alpha = np.asarray((0.37, 0.41j, -0.52, 0.64j), dtype=complex)
    alpha /= np.linalg.norm(alpha)
    states = [sector.vector for sector in sectors] + [sum((alpha[i] * sector.vector for i, sector in enumerate(sectors)), start=np.zeros(REGISTER_DIM, dtype=complex))]
    full_forward_squared = 0.0
    full_inverse_squared = 0.0
    full_leakage_squared = 0.0
    for source in range(REGISTER_DIM * 6):
        logical_basis = np.zeros((REGISTER_DIM, 6), dtype=complex)
        logical_basis.reshape(-1)[source] = 1
        physical_basis = encode_direction(logical_basis, one)
        logical_moved = (route.common_coin @ logical_basis.reshape(-1)).reshape(logical_basis.shape)
        physical_moved = physical_completion(physical_basis, one, route.common_coin)
        expected_moved = encode_direction(logical_moved, one)
        restored_basis = physical_completion(physical_moved, one, route.common_coin, inverse=True)
        reconstructed = encode_direction(decode_direction(physical_moved, one), one)
        full_forward_squared += np.linalg.norm(physical_moved - expected_moved) ** 2
        full_inverse_squared += np.linalg.norm(restored_basis - physical_basis) ** 2
        full_leakage_squared += np.linalg.norm(physical_moved - reconstructed) ** 2
    full_matrix = {
        "54D_forward_intertwiner_Frobenius": float(np.sqrt(full_forward_squared)),
        "54D_inverse_Frobenius": float(np.sqrt(full_inverse_squared)),
        "54D_code_leakage_Frobenius": float(np.sqrt(full_leakage_squared)),
        "54D_common_coin_unitarity": float(
            np.linalg.norm(route.common_coin.conj().T @ route.common_coin - np.eye(REGISTER_DIM * 6))
        ),
        "54D_encoding_Gram": float(
            np.linalg.norm(one.conj().T @ one - np.eye(6)) * np.sqrt(REGISTER_DIM)
        ),
    }
    rows = []
    for index, register_state in enumerate(states):
        logical = np.outer(register_state, rest)
        physical = encode_direction(logical, one)
        logical_output = (route.common_coin @ logical.reshape(-1)).reshape(logical.shape)
        physical_output = physical_completion(physical, one, route.common_coin)
        expected = encode_direction(logical_output, one)
        restored = physical_completion(physical_output, one, route.common_coin, inverse=True)
        reconstructed = encode_direction(decode_direction(physical_output, one), one)
        rows.append(
            {
                "state": sectors[index].name if index < len(sectors) else "seeded-coherent-four-sector",
                "forward_EG_residual": array_residual(physical_output, expected),
                "inverse_residual": array_residual(restored, physical),
                "norm_drift": abs(array_norm(physical_output) - 1),
                "code_leakage": array_residual(physical_output, reconstructed),
            }
        )
    maximum = max(
        [value for row in rows for key, value in row.items() if key != "state"]
        + list(full_matrix.values())
    )
    check(
        "one common physical M64 x register coin has exact E/G and inverse on four beta/rest basis rays and their coherent superposition",
        maximum < TOL
        and np.linalg.norm(one.conj().T @ one - np.eye(6)) < 3e-14
        and np.linalg.norm(code.constraint @ one - one) < 3e-14,
        {
            "logical_common_coin_shape": route.common_coin.shape,
            "physical_register_x_M64_ambient_shape": (REGISTER_DIM * one.shape[0],) * 2,
            "physical_matrix_materialized": False,
            "M64_n1_Gram": np.linalg.norm(one.conj().T @ one - np.eye(6)),
            "role_constraint_residual": np.linalg.norm(code.constraint @ one - one),
            "complete_Q1_x_n1_matrix_controls": full_matrix,
            "rows": rows,
            "maximum": maximum,
        },
    )


def add_state(output: dict, key, value: np.ndarray) -> None:
    output[key] = output.get(key, np.zeros_like(value)) + value


def state_norm(state: dict) -> float:
    return float(sum(np.vdot(value, value).real for value in state.values()))


def state_residual(left: dict, right: dict) -> float:
    total = 0.0
    for key in left.keys() | right.keys():
        if key in left:
            lvalue = left[key]
            rvalue = right.get(key, np.zeros_like(lvalue))
        else:
            rvalue = right[key]
            lvalue = np.zeros_like(rvalue)
        total += float(np.linalg.norm(lvalue - rvalue) ** 2)
    return float(np.sqrt(total))


def map_clock_keys(state: dict, operation) -> dict:
    output = {}
    for key, value in state.items():
        add_state(output, operation(key), value)
    return output


def clock_sweep(state: dict, *, inverse: bool = False) -> dict:
    operation = c428.clock_inverse if inverse else c428.clock_forward
    return map_clock_keys(state, lambda key: replace(key, clock=operation(key.clock)))


def beam(state: dict) -> dict:
    output = {}
    for key, value in state.items():
        position = c428.clock_position(key.clock)
        for target, coefficient in c437.beam_targets(position):
            add_state(output, replace(key, clock=c428.one_hot(target)), coefficient * value)
    return output


def latch(state: dict, *, inverse: bool = False, enabled: bool = True) -> dict:
    if not enabled:
        return {key: value.copy() for key, value in state.items()}
    operation = c428.invert_latch if inverse else c428.apply_latch
    return map_clock_keys(state, operation)


def calibrate(state: dict, operator: np.ndarray, *, inverse: bool = False, enabled: bool = True) -> dict:
    matrix = operator.conj().T if inverse else operator
    output = {}
    for key, value in state.items():
        moved = matrix @ value if enabled and c428.clock_position(key.clock) == c437.DARK_POSITION else value
        add_state(output, key, moved)
    return output


def clock_forward(
    state: dict,
    common: np.ndarray,
    clock_operator: np.ndarray,
    *,
    physical_encoding: np.ndarray | None = None,
    delete_functional: bool = False,
    delete_clock: bool = False,
    delete_latch: bool = False,
) -> dict:
    if physical_encoding is None:
        output = {
            key: ((np.eye(REGISTER_DIM * 6) if delete_functional else common) @ value.reshape(-1)).reshape(value.shape)
            for key, value in state.items()
        }
    else:
        output = {
            key: value.copy() if delete_functional else physical_completion(value, physical_encoding, common)
            for key, value in state.items()
        }
    output = clock_sweep(output)
    output = beam(output)
    output = calibrate(output, clock_operator, enabled=not (delete_functional or delete_clock))
    output = beam(output)
    return latch(output, enabled=not delete_latch)


def clock_inverse(state: dict, common: np.ndarray, clock_operator: np.ndarray, physical_encoding=None) -> dict:
    output = latch(state, inverse=True)
    output = beam(output)
    output = calibrate(output, clock_operator, inverse=True)
    output = beam(output)
    output = clock_sweep(output, inverse=True)
    if physical_encoding is None:
        return {key: (common.conj().T @ value.reshape(-1)).reshape(value.shape) for key, value in output.items()}
    return {key: physical_completion(value, physical_encoding, common, inverse=True) for key, value in output.items()}


def clock_weights(state: dict) -> dict[int, float]:
    weights = {position: 0.0 for position in range(c428.CLOCK_BITS)}
    for key, value in state.items():
        weights[c428.clock_position(key.clock)] += float(np.vdot(value, value).real)
    return weights


def clock_controls(
    route: FunctionalRoute, sectors: tuple[Sector, ...], one: np.ndarray, rest: np.ndarray
) -> dict[str, dict[str, dict[int, float]]]:
    print("\nCOMMON MASS OPERATOR -> COMPLETE CLOCK WORDS / PHYSICAL E-G")
    alpha = np.asarray((0.37, 0.41j, -0.52, 0.64j), dtype=complex)
    alpha /= np.linalg.norm(alpha)
    register_state = sum((alpha[i] * sector.vector for i, sector in enumerate(sectors)), start=np.zeros(REGISTER_DIM, dtype=complex))
    key = c437.blank_key(c437.INITIAL_CLOCK_POSITION)
    logical_initial = {key: np.outer(register_state, rest)}
    physical_initial = {key: encode_direction(logical_initial[key], one)}
    laws = {
        "cayley-functional": route.cayley_clock,
        "principal-functional": route.principal_clock,
    }
    predictions = {}
    rows = []
    menu = np.column_stack([sector.vector for sector in sectors])
    for name, operator in laws.items():
        logical_output = clock_forward(logical_initial, route.common_coin, operator)
        physical_output = clock_forward(
            physical_initial, route.common_coin, operator, physical_encoding=one
        )
        expected = {item: encode_direction(value, one) for item, value in logical_output.items()}
        restored = clock_inverse(physical_output, route.common_coin, operator, physical_encoding=one)
        rows.append(
            {
                "law": name,
                "forward_EG_residual": state_residual(physical_output, expected),
                "inverse_residual": state_residual(restored, physical_initial),
                "norm_drift": abs(state_norm(physical_output) - 1),
            }
        )
        law_predictions = {}
        for index, sector in enumerate(sectors):
            branch = {}
            for out_key, value in logical_output.items():
                projected = sector.vector.conj() @ value / alpha[index]
                branch[out_key] = projected
            law_predictions[sector.name] = clock_weights(branch)
        predictions[name] = law_predictions

    held_c = predictions["cayley-functional"][sectors[-1].name][c437.DARK_POSITION]
    held_p = predictions["principal-functional"][sectors[-1].name][c437.DARK_POSITION]
    train_difference = max(
        abs(
            predictions["cayley-functional"][sector.name][c437.DARK_POSITION]
            - predictions["principal-functional"][sector.name][c437.DARK_POSITION]
        )
        for sector in sectors[:3]
    )
    check(
        "the same common physical controller gives exact clock E/G/inverse and predicts the held principal/Cayley split without refit",
        max(value for row in rows for key, value in row.items() if key != "law") < TOL
        and train_difference < 2e-13
        and abs(held_c - held_p) > 0.7
        and np.linalg.norm(menu.conj().T @ route.cayley_clock @ menu - np.diag(np.exp(1j * np.asarray([s.cayley for s in sectors]) / CLOCK_SCALE))) < 3e-12,
        {
            "rows": rows,
            "predictions": predictions,
            "maximum_train_dark_weight_difference": train_difference,
            "held_cayley_dark_weight": held_c,
            "held_principal_dark_weight": held_p,
            "held_dark_weight_difference": abs(held_c - held_p),
            "coordinate_law_selected": False,
        },
    )
    return predictions


def local_exchange_generator() -> sparse.csc_matrix:
    rows = []
    columns = []
    data = []
    for source_index, mask in enumerate(c429.c322.LOCAL_MASKS):
        for direction in range(6):
            hopped = c429.c322.fermion_hop(mask, direction, c429.c322.REVERSE[direction])
            if hopped is None:
                continue
            target_mask, sign = hopped
            target_index = c429.c322.LOCAL_INDEX[target_mask]
            reservoir_index = 7 * source_index
            field_index = 7 * target_index + 1 + direction
            rows.extend((field_index, reservoir_index))
            columns.extend((reservoir_index, field_index))
            data.extend((sign, sign))
    return sparse.coo_matrix(
        (data, (rows, columns)), shape=(448, 448), dtype=complex
    ).tocsc()


LOCAL_EXCHANGE = local_exchange_generator()


def embedded_generator(cell: int) -> sparse.csc_matrix:
    if cell not in c429.CELLS:
        raise ValueError("source cell must be A, B, or C")
    exchange = LOCAL_EXCHANGE
    rows = []
    columns = []
    data = []
    for matter_source, label in enumerate(c429.LABELS):
        specs = list(c429.c319.label_specs(label))
        local_source = c429.c396.LOCAL_SPEC_INDEX[specs[cell]]
        for q_source in range(7):
            column = 7 * local_source + q_source
            for target in exchange[:, column].nonzero()[0]:
                local_target, q_target = divmod(int(target), 7)
                target_specs = list(specs)
                target_specs[cell] = c429.c322.LOCAL_LABELS[local_target]
                target_label = tuple(item for spec in target_specs for item in spec)
                matter_target = c429.LABEL_INDEX[target_label]
                rows.append(7 * matter_target + q_target)
                columns.append(7 * matter_source + q_source)
                data.append(exchange[target, column])
    dimension = 7 * c429.MATTER_DIM
    return sparse.coo_matrix((data, (rows, columns)), shape=(dimension, dimension), dtype=complex).tocsc()


EMBEDDED_GENERATORS = {cell: embedded_generator(cell) for cell in c429.CELLS}


def joint_prune(state: dict, threshold: float = 2e-13) -> dict:
    return {key: value for key, value in state.items() if np.linalg.norm(value) > threshold}


def joint_apply_register(state: dict, operator: np.ndarray) -> dict:
    return {key: operator @ value for key, value in state.items()}


def joint_apply_matter(state: dict, factor) -> dict:
    return joint_prune({key: (factor @ value.T).T for key, value in state.items()})


def joint_field_coin(state: dict, *, inverse: bool = False) -> dict:
    output = {}
    for site, value in state.items():
        for target, coefficient in c429.field_coin_transitions(site, inverse=inverse):
            add_state(output, target, coefficient * value)
    return joint_prune(output)


def joint_transport(state: dict, *, inverse: bool = False, enabled_edges=(True, True)) -> dict:
    order = tuple(reversed(c429.edge_order("A_to_C"))) if inverse else c429.edge_order("A_to_C")
    output = {key: value.copy() for key, value in state.items()}
    for edge in order:
        if enabled_edges[edge]:
            output = {c429.swap_edge_site(key, edge): value for key, value in output.items()}
    return joint_prune(output)


def joint_source(
    state: dict,
    mass: np.ndarray,
    cell: int,
    *,
    inverse: bool = False,
    enabled: bool = True,
    coupling_enabled: bool = True,
) -> dict:
    if not enabled or not coupling_enabled:
        return {key: value.copy() for key, value in state.items()}
    active = (c429.reservoir_site(cell),) + tuple(c429.field_site(cell, d) for d in range(6))
    zero = np.zeros((REGISTER_DIM, c429.MATTER_DIM), dtype=complex)
    joint = np.stack([state.get(key, zero) for key in active], axis=2)
    generator = sparse.kron(sparse.csc_matrix(mass), EMBEDDED_GENERATORS[cell], format="csc")
    sign = -1 if inverse else 1
    transformed = expm_multiply(
        sign * 1j * SOURCE_SCALE * generator,
        joint.reshape(-1),
        traceA=0.0,
    ).reshape(joint.shape)
    output = {key: value.copy() for key, value in state.items() if key not in active}
    for local, key in enumerate(active):
        output[key] = transformed[:, :, local]
    return joint_prune(output)


def joint_step(
    state: dict,
    mass: np.ndarray,
    rest_unitary: np.ndarray,
    factors,
    *,
    source_enabled=(True, True, True),
    coupling_enabled: bool = True,
    enabled_edges=(True, True),
) -> dict:
    coin, first, second, contact = factors
    output = joint_apply_register(state, rest_unitary)
    output = joint_apply_matter(output, coin)
    output = joint_field_coin(output)
    for cell in c429.role_cells("A_to_C"):
        output = joint_source(
            output,
            mass,
            cell,
            enabled=source_enabled[cell],
            coupling_enabled=coupling_enabled,
        )
    output = joint_apply_matter(output, first)
    output = joint_apply_matter(output, second)
    output = joint_transport(output, enabled_edges=enabled_edges)
    return joint_apply_matter(output, contact)


def joint_inverse(state: dict, mass: np.ndarray, rest_unitary: np.ndarray, factors) -> dict:
    coin, first, second, contact = factors
    output = joint_apply_matter(state, contact.getH())
    output = joint_transport(output, inverse=True)
    output = joint_apply_matter(output, second.getH())
    output = joint_apply_matter(output, first.getH())
    for cell in reversed(c429.role_cells("A_to_C")):
        output = joint_source(output, mass, cell, inverse=True)
    output = joint_field_coin(output, inverse=True)
    output = joint_apply_matter(output, coin.getH())
    return joint_apply_register(output, rest_unitary.conj().T)


def joint_evolve(state: dict, mass: np.ndarray, rest: np.ndarray, factors, depth=DEPTH, **kwargs) -> dict:
    output = state
    for _ in range(depth):
        output = joint_step(output, mass, rest, factors, **kwargs)
    return output


def joint_unevolve(state: dict, mass: np.ndarray, rest: np.ndarray, factors, depth=DEPTH) -> dict:
    output = state
    for _ in range(depth):
        output = joint_inverse(output, mass, rest, factors)
    return output


def joint_initial(register_state: np.ndarray) -> dict:
    base = c429.initial_state("A_to_C")
    site, vector = next(iter(base.items()))
    return {site: np.outer(register_state, vector)}


def sector_branch(state: dict, sector: Sector, coefficient: complex) -> dict:
    return {key: sector.vector.conj() @ value / coefficient for key, value in state.items()}


def receiver_weight(state: dict) -> float:
    value = state.get(c429.reservoir_site(c429.receiver_cell("A_to_C")))
    return 0.0 if value is None else float(np.vdot(value, value).real)


def receiver_controls(
    route: FunctionalRoute,
    sectors: tuple[Sector, ...],
    b3: LookupRoute,
    b4: LookupRoute,
    factors,
) -> dict:
    print("\nCOMMON FUNCTIONAL CONTROLLER -> ACTIVE SOURCE / DISTINCT RECEIVER")
    alpha = np.asarray((0.37, 0.41j, -0.52, 0.64j), dtype=complex)
    alpha /= np.linalg.norm(alpha)
    register_state = sum((alpha[i] * sector.vector for i, sector in enumerate(sectors)), start=np.zeros(REGISTER_DIM, dtype=complex))
    initial = joint_initial(register_state)
    routes = {
        "cayley-functional": (route.cayley_mass, route.rest_unitary),
        "principal-functional": (route.principal_mass, route.rest_unitary),
        "lookup-B3": (b3.mass, linalg.expm(1j * b3.mass / 3)),
    }
    outputs = {}
    predictions = {}
    rows = []
    for name, (mass, rest) in routes.items():
        output = joint_evolve(initial, mass, rest, factors)
        outputs[name] = output
        predictions[name] = {
            sector.name: receiver_weight(sector_branch(output, sector, alpha[index]))
            for index, sector in enumerate(sectors)
        }
        rows.append({"route": name, "joint_norm": state_norm(output)})

    restored = joint_unevolve(outputs["cayley-functional"], route.cayley_mass, route.rest_unitary, factors)
    b4_menu_residual = np.linalg.norm(
        np.column_stack([sector.vector for sector in sectors]).conj().T
        @ (route.cayley_mass - b4.mass)
        @ np.column_stack([sector.vector for sector in sectors])
    )
    train_difference = max(
        abs(predictions["cayley-functional"][sector.name] - predictions["principal-functional"][sector.name])
        for sector in sectors[:3]
    )
    held_c = predictions["cayley-functional"][sectors[-1].name]
    held_p = predictions["principal-functional"][sectors[-1].name]
    held_b3 = predictions["lookup-B3"][sectors[-1].name]
    check(
        "one coherent four-sector physical mass controller drives the source/receiver law with exact inverse and held prediction while B3 has no held coordinate",
        max(abs(row["joint_norm"] - 1) for row in rows) < 4e-11
        and state_residual(restored, initial) < 4e-10
        and train_difference < 2e-12
        and abs(held_c - held_p) > 1e-4
        and held_c > 1e-4
        and held_b3 < 1e-20
        and b4_menu_residual < 3e-12,
        {
            "rows": rows,
            "predictions": predictions,
            "coherent_inverse_residual": state_residual(restored, initial),
            "maximum_train_functional_law_difference": train_difference,
            "held_cayley_receiver": held_c,
            "held_principal_receiver": held_p,
            "held_receiver_difference": abs(held_c - held_p),
            "held_B3_receiver": held_b3,
            "B4_matches_A_on_four_sector_code": b4_menu_residual,
            "B4_uses_held_table_row": True,
        },
    )
    return {"outputs": outputs, "predictions": predictions, "initial": initial, "alpha": alpha}


def global_receiver_physical_eg_controls(
    route: FunctionalRoute, sectors: tuple[Sector, ...], factors
) -> None:
    print("\nIMPLICIT COHERENT DIRECT-SUM PHYSICAL RECEIVER E-G")
    encodings, _reducer, support, gram = c429.c396.build_shell(c437.HELD_LENGTH)
    encoding = encodings[c429.c319.ORDER_INDEX[(0, 1, 2)]]
    logical_initial = c429.initial_state("A_to_C")
    physical_initial = c429.encode_state(logical_initial, encoding)
    alpha = np.asarray((0.37, 0.41j, -0.52, 0.64j), dtype=complex)
    alpha /= np.linalg.norm(alpha)
    rows = []
    for sector in sectors:
        coordinate = float(np.vdot(sector.vector, route.cayley_mass @ sector.vector).real)
        theta = SOURCE_SCALE * coordinate
        logical_output = c438.logical_step(logical_initial, theta, factors)
        physical_output = c438.physical_step(physical_initial, encoding, theta, factors)
        expected = c429.encode_state(logical_output, encoding)
        restored = c438.physical_inverse(physical_output, encoding, theta, factors)
        decoded = {key: encoding.getH() @ value for key, value in physical_output.items()}
        reconstructed = c429.encode_state(decoded, encoding)
        rows.append(
            {
                "sector": sector.name,
                "theta_from_operator_eigenray": theta,
                "forward_EG_residual": c429.state_residual(physical_output, expected),
                "inverse_residual": c429.state_residual(restored, physical_initial),
                "norm_drift": abs(c429.state_norm(physical_output) - 1),
                "code_leakage": c429.state_residual(physical_output, reconstructed),
            }
        )
    coherent = {
        key: float(
            np.sqrt(
                sum(abs(alpha[index]) ** 2 * row[key] ** 2 for index, row in enumerate(rows))
            )
        )
        for key in ("forward_EG_residual", "inverse_residual", "code_leakage")
    }
    coherent["norm_drift_bound"] = sum(
        abs(alpha[index]) ** 2 * row["norm_drift"] for index, row in enumerate(rows)
    )
    maximum = max(
        [value for row in rows for key, value in row.items() if key not in ("sector", "theta_from_operator_eigenray")]
        + list(coherent.values())
        + [max(gram)]
    )
    check(
        "the full Cycle429 physical receiver update has exact E/G, inverse, leakage, and norm on each operator eigenray and the implicit coherent direct sum",
        maximum < TOL,
        {
            "network_matter_encoding_shape": encoding.shape,
            "matter_support": support,
            "Kronecker_register_x_network_array_materialized": False,
            "coherent_direct_sum_identity": "orthogonal register eigenrays make squared residuals add with |alpha_j|^2",
            "rows": rows,
            "coherent_four_sector_bounds": coherent,
            "maximum": maximum,
        },
    )


def local_joint_source(
    logical: np.ndarray, mass: np.ndarray, *, inverse: bool = False
) -> np.ndarray:
    generator = sparse.kron(sparse.csc_matrix(mass), LOCAL_EXCHANGE, format="csc")
    sign = -1 if inverse else 1
    return expm_multiply(
        sign * 1j * SOURCE_SCALE * generator,
        logical.reshape(-1),
        traceA=0.0,
    ).reshape(logical.shape)


def encode_local(logical: np.ndarray, encoding: np.ndarray) -> np.ndarray:
    return np.einsum("pm,rmq->rpq", encoding, logical, optimize=True)


def decode_local(physical: np.ndarray, encoding: np.ndarray) -> np.ndarray:
    return np.einsum("pm,rpq->rmq", encoding.conj(), physical, optimize=True)


def physical_local_source(
    physical: np.ndarray, encoding: np.ndarray, mass: np.ndarray, *, inverse: bool = False
) -> np.ndarray:
    before = decode_local(physical, encoding)
    after = local_joint_source(before, mass, inverse=inverse)
    return physical + encode_local(after - before, encoding)


def source_intertwiner_and_sector_family_controls(
    route: FunctionalRoute, sectors: tuple[Sector, ...], full: np.ndarray, rest: np.ndarray
) -> None:
    print("\nFUNCTIONAL RECOIL EXPONENTIAL / PHYSICAL E-G / SCALAR-FAMILY MATCH")
    rest64 = np.zeros(64, dtype=complex)
    for direction in range(6):
        rest64[c311.FOCK_INDEX[(1, (direction,))]] = rest[direction]
    alpha = np.asarray((0.37, 0.41j, -0.52, 0.64j), dtype=complex)
    alpha /= np.linalg.norm(alpha)
    states = [sector.vector for sector in sectors] + [sum((alpha[i] * sector.vector for i, sector in enumerate(sectors)), start=np.zeros(REGISTER_DIM, dtype=complex))]
    rows = []
    for index, register_state in enumerate(states):
        logical = np.zeros((REGISTER_DIM, 64, 7), dtype=complex)
        logical[:, :, 0] = np.outer(register_state, rest64)
        physical = encode_local(logical, full)
        logical_output = local_joint_source(logical, route.cayley_mass)
        physical_output = physical_local_source(physical, full, route.cayley_mass)
        expected = encode_local(logical_output, full)
        restored = physical_local_source(physical_output, full, route.cayley_mass, inverse=True)
        reconstructed = encode_local(decode_local(physical_output, full), full)
        rows.append(
            {
                "state": sectors[index].name if index < len(sectors) else "seeded-coherent-four-sector",
                "forward_EG_residual": np.linalg.norm(physical_output - expected),
                "inverse_residual": np.linalg.norm(restored - physical),
                "norm_drift": abs(array_norm(physical_output) - 1),
                "code_leakage": np.linalg.norm(physical_output - reconstructed),
            }
        )

    family_rows = []
    rng = np.random.default_rng(441)
    probe = rng.normal(size=448) + 1j * rng.normal(size=448)
    probe /= np.linalg.norm(probe)
    for coordinate_name, mass in (
        ("cayley", route.cayley_mass),
        ("principal", route.principal_mass),
    ):
        for sector in sectors:
            joint = np.outer(sector.vector, probe).reshape((REGISTER_DIM, 64, 7))
            output = local_joint_source(joint, mass).reshape(REGISTER_DIM, 448)
            coordinate = sector.cayley if coordinate_name == "cayley" else sector.principal
            scalar = c429.c322.local_source_blocks(SOURCE_SCALE * coordinate)[1] @ probe
            expected = np.outer(sector.vector, scalar)
            family_rows.append(
                {
                    "coordinate": coordinate_name,
                    "sector": sector.name,
                    "operator_eigen_residual": abs(np.vdot(sector.vector, mass @ sector.vector) - coordinate),
                    "scalar_vertex_residual": np.linalg.norm(output - expected),
                }
            )

    maximum = max(
        [value for row in rows for key, value in row.items() if key != "state"]
        + [value for row in family_rows for key, value in row.items() if key not in ("coordinate", "sector")]
    )
    check(
        "the common operator recoil exponential has exact physical E/G/inverse on basis and coherent states and reduces to every inherited scalar local vertex",
        maximum < TOL,
        {"rows": rows, "sectorwise_family_rows": family_rows, "maximum": maximum},
    )


def covariance_support_controls(route: FunctionalRoute, code, one: np.ndarray) -> None:
    print("\nALL-24 PROPER-CUBIC COVARIANCE / BOUNDED SUPPORT")
    frames = c429.c210.proper_cubic_frames()
    reducer = c311.c305.StabilizerReducer(code.encoder.code)
    old_one_indices = [c311.SEAM_INDEX[(1, (direction,), 0)] for direction in range(6)]
    old_one = code.flagged[:, old_one_indices]
    covariance = []
    encoder_covariance = []
    failures = 0
    for frame in frames:
        direction = c311.exterior_representation(frame, 1)
        representation = np.kron(np.eye(REGISTER_DIM), direction)
        covariance.append(
            np.linalg.norm(representation @ route.common_coin @ representation.conj().T - route.common_coin)
        )
        old_rep, frame_failures = c311.flagged_frame_representation(
            code.encoder, code.basis, {}, frame, reducer
        )
        failures += frame_failures
        encoder_covariance.append(np.linalg.norm(old_rep @ old_one - old_one @ direction))
        recoil_rep = c429.c426.recoil_frame(1, frame)
        recoil = c429.c426.recoil_generator(1)
        covariance.append(sparse.linalg.norm(recoil_rep @ recoil @ recoil_rep.getH() - recoil))
    check(
        "the internal register is a proper-cubic scalar and the common M64 coin plus recoil geometry are covariant in all 24 frames",
        len(frames) == 24
        and failures == 0
        and max(covariance + encoder_covariance) < TOL,
        {
            "proper_cubic_frames": len(frames),
            "maximum_common_coin_or_recoil_covariance": max(covariance),
            "maximum_M64_encoder_covariance": max(encoder_covariance),
            "frame_failures": failures,
            "register_frame_action": "I9 scalar internal block",
            "register_ring_orientation_from_geometry": False,
            "controller_rest_support_M2": code.matter_union_m2 + REGISTER_DIM,
            "common_coin_control_support_M2": code.matter_union_m2 + REGISTER_DIM,
            "clock_control_support_M2": REGISTER_DIM + 1,
            "controller_source_support_M2": REGISTER_DIM + 25,
            "train_total_clock_receiver_patch_M2": 248 + REGISTER_DIM,
            "held_total_clock_receiver_patch_M2": 252 + REGISTER_DIM,
            "primitive_synthesis": "supplied/open",
        },
    )


def deletion_domain_mass_contact_controls(
    route: FunctionalRoute,
    sectors: tuple[Sector, ...],
    clock_predictions,
    receiver_result,
    factors,
) -> None:
    print("\nDELETIONS / LAWFUL DOMAIN / MASS + CONTACT PRESERVATION")
    held = sectors[-1]
    key = c437.blank_key(c437.INITIAL_CLOCK_POSITION)
    rest = np.ones(6, dtype=complex) / np.sqrt(6)
    clock_initial = {key: np.outer(held.vector, rest)}
    zero_clock = linalg.expm(np.zeros_like(route.cayley_mass))
    mass_deleted_clock = clock_forward(clock_initial, np.eye(54), zero_clock)
    functional_deleted_clock = clock_forward(
        clock_initial, route.common_coin, route.cayley_clock, delete_functional=True
    )
    clock_deleted = clock_forward(
        clock_initial, route.common_coin, route.cayley_clock, delete_clock=True
    )
    latch_deleted = clock_forward(
        clock_initial, route.common_coin, route.cayley_clock, delete_latch=True
    )

    held_initial = joint_initial(held.vector)
    mass_deleted_receiver = joint_evolve(
        held_initial, np.zeros_like(route.cayley_mass), np.eye(REGISTER_DIM), factors
    )
    coupling_deleted_receiver = joint_evolve(
        held_initial,
        route.cayley_mass,
        route.rest_unitary,
        factors,
        coupling_enabled=False,
    )
    receiver_deleted = joint_evolve(
        held_initial,
        route.cayley_mass,
        route.rest_unitary,
        factors,
        source_enabled=(True, True, False),
    )

    update_rows, _coin, _first, _second, contact, _forward, _reverse = c429.c319.update_controls(
        c429.LABELS, "path"
    )
    mass_residual = abs(update_rows["three_cell_rest_mass"] - update_rows["Cycle219_mass_fixture"])

    rejections = 0
    operations = (
        lambda: validate_register(np.eye(8)),
        lambda: validate_register(np.diag([1] * 8 + [-1])),
        lambda: validate_register(np.ones((9, 8))),
        lambda: validate_register(np.full((9, 9), np.nan)),
        lambda: lookup_route(sectors, 2),
        lambda: joint_source({}, route.cayley_mass, 3),
        lambda: c429.validate_state({0: np.zeros((2, c429.MATTER_DIM))}),
        lambda: validate_register_code_mask(0),
        lambda: validate_register_code_mask(0b11),
    )
    for operation in operations:
        try:
            operation()
        except ValueError:
            rejections += 1

    valid_latch = sum(
        np.vdot(value, value).real for latch_key, value in latch_deleted.items() if latch_key.valid
    )
    baseline = receiver_result["predictions"]["cayley-functional"][held.name]
    check(
        "mass-observable, functional-law, controller-source, clock, receiver, and latch deletions are visible while mass/contact and lawful domain remain exact",
        clock_weights(mass_deleted_clock)[c437.DARK_POSITION] < 2e-14
        and clock_weights(functional_deleted_clock)[c437.DARK_POSITION] < 2e-14
        and clock_weights(clock_deleted)[c437.DARK_POSITION] < 2e-14
        and valid_latch == 0
        and receiver_weight(mass_deleted_receiver) < 2e-20
        and receiver_weight(coupling_deleted_receiver) < 2e-20
        and receiver_weight(receiver_deleted) < 2e-20
        and baseline > 1e-4
        and mass_residual < 3e-13
        and update_rows["contact_nontrivial_columns"] == 645
        and rejections == len(operations),
        {
            "mass_observable_deleted_clock_dark": clock_weights(mass_deleted_clock)[c437.DARK_POSITION],
            "functional_law_deleted_clock_dark": clock_weights(functional_deleted_clock)[c437.DARK_POSITION],
            "clock_control_deleted_dark": clock_weights(clock_deleted)[c437.DARK_POSITION],
            "latch_deleted_valid_weight": float(valid_latch),
            "mass_observable_deleted_receiver": receiver_weight(mass_deleted_receiver),
            "controller_source_coupling_deleted_receiver": receiver_weight(coupling_deleted_receiver),
            "receiver_vertex_deleted": receiver_weight(receiver_deleted),
            "baseline_held_cayley_receiver": baseline,
            "Cycle219_mass_fixture": update_rows["Cycle219_mass_fixture"],
            "three_cell_rest_mass": update_rows["three_cell_rest_mass"],
            "mass_residual": mass_residual,
            "contact_nontrivial_columns": update_rows["contact_nontrivial_columns"],
            "contact_shape": contact.shape,
            "lawful_domain_rejections": rejections,
        },
    )


def boundaries_inventory() -> None:
    print("\nSUPPLIED / DERIVED / OPEN / TYPED BOUNDARY")
    inventory = {
        "supplied": (
            "existence and dimension of the nine-M2 register, one-hot population, internal ring orientation, and eight-SWAP schedule",
            "Cayley resolvent, principal logarithm, CLOCK_SCALE=8, SOURCE_SCALE=0.05, signs, zeros, and invocation",
            "Cycle311 reference/role preparation and dense bounded common-coin completion",
            "prepared source reservoir, blank field, receiver matter column, factor order, path, contact, and readouts",
            "clock initial word, Ramsey arms, latch trigger, event identity, and blank sidecar",
        ),
        "derived": (
            "physical nine-M2 Q=1 register and common M64 x register coherent code",
            "functional Cayley/principal common controls with held prediction and no beta lookup",
            "basis/coherent E/G, inverse, scalar recoil-family equality, covariance, support, deletions, leakage, and domain controls",
            "exact distinction between predictive functional Route A, train-only B3, and held-consuming B4",
        ),
        "open": (
            "selection/derivation of the register, its orientation, either coordinate law, both scales, and initial population",
            "autonomous generation/change/combination of beta populations and primitive sparse synthesis of dense bounded functions",
            "source preparation, common lapse, passive response, physical energy/stress calibration, metric/proper time, gravity, and empirical selection",
            "Record formation, occurrence, Born law, and observed spectrum/species interpretation",
        ),
        "authority": AUTHORITY,
        "audit": AUDIT,
        "no_go": False,
        "minimum_content": False,
        "axiom_pressure": False,
    }
    check(
        "the positive coherent controller closes beta lookup only for supplied candidate functions and leaves every far-side interpretation open",
        AUTHORITY == "none" and AUDIT == "unset",
        {
            "inventory": inventory,
            "Cayley_selected_over_principal": False,
            "update_count_called_time": False,
            "phase_called_energy": False,
            "latch_called_Record": False,
            "active_recoil_called_gravity": False,
            "axiom_or_foundation_edit": False,
        },
    )


def main() -> int:
    contracts()
    register = c220.cyclic_shift(REGISTER_DIM)
    route = functional_route(register)
    sectors = sector_menu(register)
    b3 = lookup_route(sectors, 3)
    b4 = lookup_route(sectors, 4)
    register_ring_controls(register, sectors)
    anti_lookup_controls(route, sectors, b3, b4)
    code, one, full, rest = matter_code()
    common_coin_physical_controls(route, sectors, code, one, rest)
    clock_predictions = clock_controls(route, sectors, one, rest)
    source_intertwiner_and_sector_family_controls(route, sectors, full, rest)
    update_rows, coin, first, second, contact, _forward, _reverse = c429.c319.update_controls(
        c429.LABELS, "path"
    )
    factors = (coin, first, second, contact)
    receiver_result = receiver_controls(route, sectors, b3, b4, factors)
    global_receiver_physical_eg_controls(route, sectors, factors)
    covariance_support_controls(route, code, one)
    deletion_domain_mass_contact_controls(
        route, sectors, clock_predictions, receiver_result, factors
    )
    boundaries_inventory()
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL, "authority": AUTHORITY, "audit": AUDIT})
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
