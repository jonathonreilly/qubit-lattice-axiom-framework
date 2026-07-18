#!/usr/bin/env python3
"""Extended-mode existence hunt in the carried one-matter relative update.

Enumerate bounded K=0 and nonzero-total-momentum spectral windows of the
actual carried coin/exchange/stream update.  Score three proper-cubic scalar
direction-pair projections, plus their explicitly adaptive linear span,
against the residual-matched shifted-Green shape.  The construction is a
finite-volume search witness, not a continuing branch or a gravity result.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from pathlib import Path

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigs

import stationary_dressed_carried_source_relative_mode_2026_07_17 as base


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "CARRIED_RELATIVE_EXTENDED_GREEN_BRANCH_HUNT_NOTE_2026-07-17.md"
)

TRAINING_SIZES = (3, 4)
HELD_SIZES = (5, 6)
SIZES = TRAINING_SIZES + HELD_SIZES
K_ZERO = (0, 0, 0)
K_AXIS = (1, 0, 0)
K_FACE = (1, 1, 0)
K_BODY = (1, 1, 1)
K0_TARGET_FRACTIONS = (0.08, 0.20, 0.32, 0.44, 0.56, 0.68, 0.80)
K_AXIS_TARGET_FRACTIONS = (0.08, 0.18, 0.28, 0.38, 0.48, 0.58, 0.68, 0.78, 0.88)
OTHER_TARGET_FRACTIONS = (0.12, 0.28, 0.44, 0.60, 0.76, 0.88)
EIGENPAIRS_PER_WINDOW = 8
EXTENDED_CONTACT_MAXIMUM = 0.60
GREEN_OVERLAP_MINIMUM = 0.50
PROJECTION_WEIGHT_MINIMUM = 1e-6
POLE_MARGIN_FRACTION = 0.02
SIMPLE_EIGENVALUE_GAP = 1e-7
TOLERANCE = 3e-10

PASS = 0
FAIL = 0

DirectionIndex = tuple[int, int, int]


@dataclass
class Candidate:
    length: int
    momentum_index: DirectionIndex
    target_fraction: float
    target_phase: float
    eigenvalue: complex
    state: np.ndarray
    eigen_residual: float
    local_gap: float
    shift: float
    pole_margin: float
    fixed_projection_metrics: dict[str, dict[str, float]]
    projection_coefficients: np.ndarray
    profile: np.ndarray
    projection_weight: float
    contact_fraction: float
    green_overlap: float
    green_residual: float


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
    if not NOTE.exists():
        check("the extended-branch note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "actual carried update",
        "q=n_e+n_f=1",
        "nonzero total momentum",
        "proper-cubic scalar projection",
        "adaptive projection",
        "search witness",
        "not a continuing spectral branch",
        "residual-matched shifted-green comparator",
        "contact fraction",
        "selector stability",
        "basis-spanning",
        "all 24 proper-cubic frames",
        "held l=5,6",
        "declared held-size",
        "not a prospective preregistration",
        "supplied-window inventory",
        "not physical energy",
        "eigenphase is not a rate",
        "not gravity",
        "no no-go claim",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check(
        "the note pins the search, comparator, controls, and scope",
        not missing,
        missing,
    )


def first_nonzero_laplacian(length: int) -> float:
    symbols, _lazy = base.c211.c9.fourier_symbols(length)
    return float(np.min(symbols[symbols > 1e-14]))


def pole_phase(length: int) -> float:
    return float(np.arccos(1.0 - first_nonzero_laplacian(length) / 6.0))


def momentum(length: int, index: DirectionIndex) -> np.ndarray:
    if length < 3:
        raise ValueError("periodic relative streams require L>=3")
    values = np.asarray(index)
    if values.shape != (3,) or not np.issubdtype(values.dtype, np.integer):
        raise ValueError("total momentum must be supplied by three integer torus indices")
    return 2 * np.pi * values.astype(float) / length


def carried_update(
    length: int,
    momentum_index: DirectionIndex,
    angle: float = base.ANGLE,
) -> sparse.csr_matrix:
    """Actual carried relative update at a lawful discrete total momentum."""

    total_momentum = momentum(length, momentum_index)
    cells = length**3
    pair_coin = sparse.kron(
        sparse.eye(cells, dtype=complex, format="csr"),
        sparse.csr_matrix(np.kron(base.SPECIES.coin, base.c214.FIELD_COIN)),
        format="csr",
    )
    coin = sparse.block_diag(
        (sparse.csr_matrix(base.SPECIES.coin), pair_coin), format="csr"
    )
    _exchange, local_vertex, _charge = base.carried.active_blocks(angle)
    vertex = sparse.eye(6 + 36 * cells, dtype=complex, format="lil")
    vertex[:42, :42] += local_vertex - np.eye(42, dtype=complex)
    return (
        base.relative_stream_matrix(length, total_momentum)
        @ vertex.tocsr()
        @ coin
    ).tocsr()


def momentum_lift_isometry(
    length: int, momentum_index: DirectionIndex
) -> sparse.csr_matrix:
    """Lift a relative block into its full discrete-total-momentum sector."""

    total_momentum = momentum(length, momentum_index)
    cells = length**3
    rows: list[int] = []
    columns: list[int] = []
    values: list[complex] = []
    scale = 1 / np.sqrt(cells)
    for body in product(range(length), repeat=3):
        phase = scale * np.exp(1j * np.dot(total_momentum, body))
        for matter_direction in range(6):
            rows.append(base.full_excited_index(body, matter_direction, length))
            columns.append(matter_direction)
            values.append(complex(phase))
        for relative in product(range(length), repeat=3):
            field = tuple(
                (body[axis] + relative[axis]) % length for axis in range(3)
            )
            relative_flat = base.site_index(relative, length)
            for matter_direction in range(6):
                for field_direction in range(6):
                    rows.append(
                        base.full_pair_index(
                            body,
                            field,
                            matter_direction,
                            field_direction,
                            length,
                        )
                    )
                    columns.append(
                        6
                        + 36 * relative_flat
                        + 6 * matter_direction
                        + field_direction
                    )
                    values.append(complex(phase))
    return sparse.csr_matrix(
        (values, (rows, columns)),
        shape=(6 * cells + 36 * cells**2, 6 + 36 * cells),
    )


DIRECTION_DOTS = base.c210.DIRECTIONS @ base.c210.DIRECTIONS.T
ORBIT_NAMES = ("same", "opposite", "perpendicular")
ORBIT_MASKS = (
    DIRECTION_DOTS == 1,
    DIRECTION_DOTS == -1,
    DIRECTION_DOTS == 0,
)


def scalar_orbit_basis_controls() -> None:
    """Exhaust the simultaneous proper-cubic orbits of ordered directions."""

    frames = base.c210.proper_cubic_frames()
    orbit_sizes = []
    failures = 0
    representatives = ((0, 0), (0, 1), (0, 2))
    for mask, representative in zip(ORBIT_MASKS, representatives):
        expected = {
            tuple(int(value) for value in pair)
            for pair in np.argwhere(mask)
        }
        orbit = set()
        for frame in frames:
            direction_map = []
            for direction in base.c210.DIRECTIONS:
                target = frame @ direction
                matches = np.flatnonzero(
                    np.all(base.c210.DIRECTIONS == target, axis=1)
                )
                failures += len(matches) != 1
                if len(matches) == 1:
                    direction_map.append(int(matches[0]))
            if len(direction_map) == 6:
                orbit.add(
                    (
                        direction_map[representative[0]],
                        direction_map[representative[1]],
                    )
                )
                for left, right in product(range(6), repeat=2):
                    failures += bool(mask[left, right]) != bool(
                        mask[direction_map[left], direction_map[right]]
                    )
        orbit_sizes.append(len(orbit))
        failures += orbit != expected
    check(
        "the three declared direction-pair contractions are exactly the complete simultaneous proper-cubic orbit basis",
        len(frames) == 24 and orbit_sizes == [6, 6, 24] and failures == 0,
        {"proper_frames": len(frames), "orbit_sizes": orbit_sizes, "failures": failures},
    )


def scalar_orbit_profiles(state: np.ndarray, length: int) -> np.ndarray:
    """Three invariant contractions of the ordered direction-pair matrix."""

    _excited, pair = base.split_state(state, length)
    matrices = pair.reshape(length**3, 6, 6)
    profiles = np.column_stack(
        tuple(
            np.sum(matrices[:, mask], axis=1) / np.sqrt(np.sum(mask))
            for mask in ORBIT_MASKS
        )
    )
    return profiles - np.mean(profiles, axis=0, keepdims=True)


def adaptive_scalar_projection(
    state: np.ndarray, length: int, comparator: np.ndarray
) -> tuple[
    dict[str, dict[str, float]],
    np.ndarray,
    np.ndarray,
    float,
    float,
    float,
    float,
] | None:
    """Best comparator overlap in the declared three-scalar projection span."""

    profiles = scalar_orbit_profiles(state, length)
    target = comparator.reshape(-1).astype(complex)
    target -= np.mean(target)
    fixed_metrics: dict[str, dict[str, float]] = {}
    for name, profile in zip(ORBIT_NAMES, profiles.T):
        weight = float(np.vdot(profile, profile).real)
        if weight < 1e-16:
            fixed_metrics[name] = {
                "projection_weight": weight,
                "contact_fraction": float("nan"),
                "green_overlap": float("nan"),
                "green_residual": float("nan"),
            }
            continue
        overlap = float(
            abs(np.vdot(profile, target))
            / (np.linalg.norm(profile) * np.linalg.norm(target))
        )
        fixed_metrics[name] = {
            "projection_weight": weight,
            "contact_fraction": float(abs(profile[0]) ** 2 / weight),
            "green_overlap": overlap,
            "green_residual": float(np.sqrt(max(0.0, 2 - 2 * overlap))),
        }
    left, singular, _right = np.linalg.svd(profiles, full_matrices=False)
    if singular.size == 0 or singular[0] < 1e-13:
        return None
    rank = int(np.sum(singular > max(1e-12, 1e-10 * singular[0])))
    target_projection = left[:, :rank] @ (left[:, :rank].conj().T @ target)
    coefficients = np.linalg.lstsq(profiles, target_projection, rcond=1e-10)[0]
    coefficient_norm = float(np.linalg.norm(coefficients))
    if coefficient_norm < 1e-13:
        return None
    coefficients /= coefficient_norm
    profile = profiles @ coefficients
    weight = float(np.vdot(profile, profile).real)
    if weight < PROJECTION_WEIGHT_MINIMUM:
        return None
    overlap = float(
        abs(np.vdot(profile, target))
        / (np.linalg.norm(profile) * np.linalg.norm(target))
    )
    residual = float(np.sqrt(max(0.0, 2 - 2 * overlap)))
    contact = float(abs(profile[0]) ** 2 / weight)
    return fixed_metrics, coefficients, profile, weight, contact, overlap, residual


def target_fractions(length: int, momentum_index: DirectionIndex) -> tuple[float, ...]:
    if momentum_index == K_ZERO:
        return K0_TARGET_FRACTIONS
    if momentum_index == K_AXIS:
        return K_AXIS_TARGET_FRACTIONS
    if length in (4, 5) and momentum_index in (K_FACE, K_BODY):
        return OTHER_TARGET_FRACTIONS
    return ()


def momentum_indices(length: int) -> tuple[DirectionIndex, ...]:
    if length in (4, 5):
        return (K_ZERO, K_AXIS, K_FACE, K_BODY)
    return (K_ZERO, K_AXIS)


def deterministic_start(dimension: int, variant: int = 0) -> np.ndarray:
    indices = np.arange(dimension, dtype=float) + 1
    if variant == 0:
        vector = np.sin(0.37 * indices) + 1j * np.cos(0.19 * indices)
    else:
        vector = np.cos(0.23 * indices) - 1j * np.sin(0.41 * indices)
    return vector / np.linalg.norm(vector)


def enumerate_window(
    length: int,
    momentum_index: DirectionIndex,
    target_fraction: float,
    *,
    candidates: int = EIGENPAIRS_PER_WINDOW,
    start_variant: int = 0,
) -> tuple[list[Candidate], int, int]:
    update = carried_update(length, momentum_index)
    target_phase = target_fraction * pole_phase(length)
    eigenvalues, eigenvectors = eigs(
        update,
        k=candidates,
        sigma=np.exp(-1j * target_phase),
        which="LM",
        v0=deterministic_start(update.shape[0], start_variant),
        tol=2e-11,
        maxiter=50000,
        ncv=max(48, 2 * candidates + 8),
    )
    pole = first_nonzero_laplacian(length)
    accepted: list[Candidate] = []
    negative_phase_count = 0
    for index, eigenvalue in enumerate(eigenvalues):
        phase = float(-np.angle(eigenvalue))
        if phase <= 0:
            continue
        negative_phase_count += 1
        shift = float(6 * (1 - np.cos(phase)))
        pole_margin = pole - shift
        if pole_margin <= POLE_MARGIN_FRACTION * pole:
            continue
        state = eigenvectors[:, index]
        state /= np.linalg.norm(state)
        residual = float(np.linalg.norm(update @ state - eigenvalue * state))
        other = np.delete(eigenvalues, index)
        local_gap = float(np.min(abs(other - eigenvalue)))
        comparator = base.fixed.shifted_green_profile(length, shift)
        projected = adaptive_scalar_projection(state, length, comparator)
        if projected is None:
            continue
        (
            fixed_metrics,
            coefficients,
            profile,
            weight,
            contact,
            overlap,
            green_residual,
        ) = projected
        accepted.append(
            Candidate(
                length=length,
                momentum_index=momentum_index,
                target_fraction=target_fraction,
                target_phase=target_phase,
                eigenvalue=complex(eigenvalue),
                state=state,
                eigen_residual=residual,
                local_gap=local_gap,
                shift=shift,
                pole_margin=pole_margin,
                fixed_projection_metrics=fixed_metrics,
                projection_coefficients=coefficients,
                profile=profile,
                projection_weight=weight,
                contact_fraction=contact,
                green_overlap=overlap,
                green_residual=green_residual,
            )
        )
    return accepted, len(eigenvalues), negative_phase_count


def eligible(candidate: Candidate) -> bool:
    return (
        candidate.eigen_residual < 2e-8
        and candidate.local_gap > SIMPLE_EIGENVALUE_GAP
        and candidate.contact_fraction <= EXTENDED_CONTACT_MAXIMUM
        and candidate.green_overlap >= GREEN_OVERLAP_MINIMUM
    )


def search_controls() -> tuple[dict[int, Candidate], dict[str, int]]:
    print("\nBROAD K=0 / NONZERO-K EXTENDED-MODE SEARCH")
    best: dict[int, Candidate] = {}
    raw = 0
    negative = 0
    accepted = 0
    simple_extended = 0
    unique_keys: set[tuple[int, DirectionIndex, int, int]] = set()
    by_sector: dict[tuple[int, DirectionIndex], list[Candidate]] = {}
    windows = 0
    for length in SIZES:
        for momentum_index in momentum_indices(length):
            sector: list[Candidate] = []
            for fraction in target_fractions(length, momentum_index):
                rows, raw_count, negative_count = enumerate_window(
                    length, momentum_index, fraction
                )
                windows += 1
                raw += raw_count
                negative += negative_count
                accepted += len(rows)
                for row in rows:
                    unique_keys.add(
                        (
                            length,
                            momentum_index,
                            int(round(row.eigenvalue.real * 1e9)),
                            int(round(row.eigenvalue.imag * 1e9)),
                        )
                    )
                sector.extend(rows)
            by_sector[(length, momentum_index)] = sector
        candidates = [
            row
            for (row_length, _index), rows in by_sector.items()
            if row_length == length
            for row in rows
            if eligible(row)
        ]
        simple_extended += len(candidates)
        if candidates:
            best[length] = max(candidates, key=lambda row: row.green_overlap)

    counts = {
        "sizes": len(SIZES),
        "momentum_sectors": len(by_sector),
        "windows": windows,
        "raw_eigenpairs": raw,
        "negative_phase_eigenpairs": negative,
        "projection_accepted": accepted,
        "unique_eigenvalues": len(unique_keys),
        "simple_extended_candidates_with_window_duplicates": simple_extended,
        "fixed_scalar_projections_per_eigenpair": len(ORBIT_NAMES),
    }
    check(
        "the declared tournament enumerates broad K=0 windows and three nonzero momentum shells",
        windows == 88
        and raw == windows * EIGENPAIRS_PER_WINDOW
        and all((length, K_ZERO) in by_sector for length in SIZES)
        and all((length, K_AXIS) in by_sector for length in SIZES)
        and (4, K_FACE) in by_sector
        and (5, K_BODY) in by_sector,
        counts,
    )
    details = {}
    for length, row in best.items():
        details[length] = {
            "domain": "training" if length in TRAINING_SIZES else "held",
            "K_index": row.momentum_index,
            "target_fraction": row.target_fraction,
            "eigenphase": float(-np.angle(row.eigenvalue)),
            "mu": row.shift,
            "pole_margin": row.pole_margin,
            "fixed_projection_metrics": row.fixed_projection_metrics,
            "projection_coefficients_same_opposite_perpendicular": tuple(
                complex(value) for value in row.projection_coefficients
            ),
            "projection_weight": row.projection_weight,
            "contact_fraction": row.contact_fraction,
            "green_overlap": row.green_overlap,
            "green_residual": row.green_residual,
            "eigen_residual": row.eigen_residual,
            "local_eigenvalue_gap": row.local_gap,
        }
    check(
        "the declared selector returns simple extended search witnesses on every training and held size",
        set(best) == set(SIZES)
        and all(row.momentum_index != K_ZERO for row in best.values())
        and all(row.green_overlap >= GREEN_OVERLAP_MINIMUM for row in best.values())
        and all(row.contact_fraction <= EXTENDED_CONTACT_MAXIMUM for row in best.values()),
        details,
    )
    check(
        "the declared held-size L=5,6 search witnesses survive every supplied acceptance gate",
        all(
            length in best
            and best[length].pole_margin
            > POLE_MARGIN_FRACTION * first_nonzero_laplacian(length)
            and best[length].projection_weight >= PROJECTION_WEIGHT_MINIMUM
            and best[length].local_gap > SIMPLE_EIGENVALUE_GAP
            and best[length].eigen_residual < 2e-8
            and best[length].contact_fraction <= EXTENDED_CONTACT_MAXIMUM
            and best[length].green_overlap >= GREEN_OVERLAP_MINIMUM
            for length in HELD_SIZES
        ),
        {length: details.get(length) for length in HELD_SIZES},
    )
    return best, counts


def selector_stability_controls(best: dict[int, Candidate]) -> None:
    print("\nSELECTOR STABILITY")
    details = {}
    all_stable = True
    for length, reference in best.items():
        repeats = []
        for candidates, variant in ((8, 1), (10, 1)):
            rows, _raw, _negative = enumerate_window(
                length,
                reference.momentum_index,
                reference.target_fraction,
                candidates=candidates,
                start_variant=variant,
            )
            repeat = min(rows, key=lambda row: abs(row.eigenvalue - reference.eigenvalue))
            eigenvalue_delta = float(abs(repeat.eigenvalue - reference.eigenvalue))
            state_overlap = float(abs(np.vdot(repeat.state, reference.state)))
            profile_overlap = float(
                abs(np.vdot(repeat.profile, reference.profile))
                / (np.linalg.norm(repeat.profile) * np.linalg.norm(reference.profile))
            )
            repeats.append(
                {
                    "k": candidates,
                    "eigenvalue_delta": eigenvalue_delta,
                    "state_overlap": state_overlap,
                    "profile_overlap": profile_overlap,
                    "green_overlap_delta": abs(
                        repeat.green_overlap - reference.green_overlap
                    ),
                    "contact_delta": abs(
                        repeat.contact_fraction - reference.contact_fraction
                    ),
                }
            )
        details[length] = repeats
        all_stable &= all(
            item["eigenvalue_delta"] < 2e-10
            and item["state_overlap"] > 1 - 2e-8
            and item["profile_overlap"] > 1 - 2e-8
            and item["green_overlap_delta"] < 2e-8
            and item["contact_delta"] < 2e-8
            for item in repeats
        )
    check(
        "the selected simple eigenpairs and adaptive scalar profiles are stable under start-vector and candidate-count changes",
        all_stable,
        details,
    )


def spatial_frame_profile(
    profile: np.ndarray, length: int, frame: np.ndarray
) -> np.ndarray:
    output = np.zeros(length**3, dtype=complex)
    for cell in product(range(length), repeat=3):
        target = tuple(int(value % length) for value in frame @ np.asarray(cell))
        output[base.site_index(target, length)] = profile[base.site_index(cell, length)]
    return output


def covariance_controls(best: dict[int, Candidate]) -> None:
    print("\nPROPER-CUBIC COVARIANCE")
    length = 3
    witness = best[length]
    index = np.asarray(witness.momentum_index)
    update = carried_update(length, witness.momentum_index)
    comparator = base.fixed.shifted_green_profile(length, witness.shift)
    operator_residuals = []
    state_residuals = []
    profile_residuals = []
    coefficient_residuals = []
    for frame in base.c210.proper_cubic_frames():
        representation = base.frame_permutation(length, frame)
        rotated_index = tuple(int(value) for value in frame @ index)
        rotated_update = carried_update(length, rotated_index)
        operator_residuals.append(
            float(sparse.linalg.norm(rotated_update @ representation - representation @ update))
        )
        rotated_state = representation @ witness.state
        state_residuals.append(
            float(
                np.linalg.norm(
                    rotated_update @ rotated_state
                    - witness.eigenvalue * rotated_state
                )
            )
        )
        projected = adaptive_scalar_projection(rotated_state, length, comparator)
        assert projected is not None
        (
            _fixed_metrics,
            coefficients,
            profile,
            _weight,
            _contact,
            _overlap,
            _residual,
        ) = projected
        expected = spatial_frame_profile(witness.profile, length, frame)
        phase = np.vdot(profile, expected)
        phase /= abs(phase)
        profile_residuals.append(float(np.linalg.norm(profile - phase * expected)))
        coefficient_residuals.append(
            float(
                np.linalg.norm(
                    coefficients
                    - phase * witness.projection_coefficients
                )
            )
        )
    check(
        "the nonzero-K update, eigenstate orbit, and adaptive scalar profile are covariant under all 24 proper-cubic frames",
        len(operator_residuals) == 24
        and max(operator_residuals) < 3e-12
        and max(state_residuals) < 3e-10
        and max(profile_residuals) < 3e-9
        and max(coefficient_residuals) < 3e-9,
        {
            "K_index": witness.momentum_index,
            "max_operator_frobenius_residual": max(operator_residuals),
            "max_eigenstate_residual": max(state_residuals),
            "max_profile_residual": max(profile_residuals),
            "max_coefficient_residual": max(coefficient_residuals),
        },
    )


def lift_and_domain_controls(best: dict[int, Candidate]) -> None:
    print("\nFULL-LIFT / LAWFUL-DOMAIN / COUPLING-ENDPOINT CONTROLS")
    length = 3
    momentum_index = K_AXIS
    update = carried_update(length, momentum_index)
    k_zero_regression = float(
        sparse.linalg.norm(
            carried_update(length, K_ZERO)
            - base.carried_relative_update(length)
        )
    )
    full_update = base.full_periodic_update(length)
    lift = momentum_lift_isometry(length, momentum_index)
    identity = sparse.eye(update.shape[0], dtype=complex, format="csr")
    unitarity = float(sparse.linalg.norm(update.conj().T @ update - identity))
    isometry = float(sparse.linalg.norm(lift.conj().T @ lift - identity))
    intertwiner = float(sparse.linalg.norm(full_update @ lift - lift @ update))
    check(
        "the relative-sector basis-spanning L=3 nonzero-K lift is an isometry and intertwines the full periodic carried update",
        lift.nnz == full_update.shape[0]
        and k_zero_regression < 4e-13
        and unitarity < 4e-13
        and isometry < 4e-13
        and intertwiner < 4e-12,
        {
            "K_index": momentum_index,
            "relative_dimension": update.shape[0],
            "full_dimension": full_update.shape[0],
            "K0_predecessor_update_residual": k_zero_regression,
            "unitarity_residual": unitarity,
            "isometry_residual": isometry,
            "intertwiner_frobenius_residual": intertwiner,
        },
    )

    invalid_length = False
    invalid_momentum = False
    try:
        momentum_lift_isometry(2, K_AXIS)
    except ValueError:
        invalid_length = True
    try:
        momentum(4, (1.0, 0.5, 0.0))  # type: ignore[arg-type]
    except ValueError:
        invalid_momentum = True
    check(
        "the nonzero-K construction rejects undersized tori and nondiscrete momentum labels",
        invalid_length and invalid_momentum,
        {"L=2_rejected": invalid_length, "fractional_index_rejected": invalid_momentum},
    )

    witness = best[length]
    endpoint = carried_update(length, witness.momentum_index, angle=0.0)
    endpoint_residual = float(
        np.linalg.norm(endpoint @ witness.state - witness.eigenvalue * witness.state)
    )
    check(
        "the selected extended witness depends on the nonzero local exchange parameter endpoint",
        endpoint_residual > 1e-3,
        {"theta_zero_old_eigenpair_residual": endpoint_residual},
    )


def inventory_controls(counts: dict[str, int]) -> None:
    print("\nSUPPLIED-WINDOW INVENTORY")
    inventory = {
        "actual_update_inputs": (
            "Cycle219 common matter coin",
            "Cycle214 six-direction field coin",
            "carried local e <-> g+field exchange",
            "matter and field streams",
        ),
        "fixed_parameters": {
            "beta": base.BETA,
            "mediator_coupling": base.MEDIATOR_COUPLING,
            "angle": base.ANGLE,
        },
        "search_sizes": {"training": TRAINING_SIZES, "held": HELD_SIZES},
        "momentum_indices": {
            "K0_all_sizes": K_ZERO,
            "axis_all_sizes": K_AXIS,
            "face_L4_L5": K_FACE,
            "body_L4_L5": K_BODY,
        },
        "target_fractions": {
            "K0": K0_TARGET_FRACTIONS,
            "axis": K_AXIS_TARGET_FRACTIONS,
            "face_body": OTHER_TARGET_FRACTIONS,
        },
        "eigenpairs_per_window": EIGENPAIRS_PER_WINDOW,
        "projection_orbits": ORBIT_NAMES,
        "orbit_profile_normalization": "sum of orbit amplitudes divided by sqrt(orbit cardinality)",
        "adaptive_rule": "least-squares projection of the comparator into the three-orbit scalar span",
        "adaptive_projection_shape_freedom": "one per-eigenpair normalized complex three-vector; at most CP^2 = four real shape degrees",
        "per_eigenpair_comparator_shift": "mu=6(1-cos(eigenphase)); derived from each searched eigenpair",
        "extension_gate": EXTENDED_CONTACT_MAXIMUM,
        "green_overlap_minimum": GREEN_OVERLAP_MINIMUM,
        "projection_weight_minimum": PROJECTION_WEIGHT_MINIMUM,
        "pole_margin_fraction": POLE_MARGIN_FRACTION,
        "simple_eigenvalue_gap": SIMPLE_EIGENVALUE_GAP,
        "comparator": "3 (Delta_L - mu I)^-1 (delta_0 - 1/L^3), shape only",
        "enumeration_counts": counts,
    }
    check(
        "the executable prints the supplied search windows, selector gates, projection freedom, and comparator inventory",
        counts["windows"] == 88
        and counts["raw_eigenpairs"] == 704
        and GREEN_OVERLAP_MINIMUM == 0.50
        and len(ORBIT_MASKS) == 3
        and sum(int(np.sum(mask)) for mask in ORBIT_MASKS) == 36,
        inventory,
    )


def main() -> int:
    print("CARRIED RELATIVE EXTENDED GREEN-SHAPE MODE-EXISTENCE HUNT")
    print("authority=none; audit=unset")
    note_contract()
    scalar_orbit_basis_controls()
    best, counts = search_controls()
    if set(best) == set(SIZES):
        selector_stability_controls(best)
        covariance_controls(best)
        lift_and_domain_controls(best)
    else:
        check("downstream controls have selected witnesses on all sizes", False, sorted(best))
    inventory_controls(counts)
    print(f"\nSUMMARY: {PASS} passed, {FAIL} failed")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
