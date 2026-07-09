#!/usr/bin/env python3
"""Block02 v3: cell-interface activity and register-information opportunity.

This is the measured half of "local activity is record-formation opportunity"
on the gauged comparator.  It is a declared finite-volume measurement, not a
derivation of a formation rule, and it sets no audit status.

v2 changelog (the v1 gates were ill-posed in two distinct ways):

* v1 compared an entropy change with a trace-norm change through a linear
  ``|dI| <= C*a*dt`` gate.  Such a constant is unbounded for small changes
  because of the logarithmic entropy-continuity term; v1's 386 reported
  "violations" were at tiny activity, and its own SPEC-NOTE already
  flagged the missing Fannes form.  v2 first tests trace distance against
  trace-norm activity, then separately tests the sharp entropy envelope.
* v1 used a full-window change of a bounded, saturating information quantity.
  Kick sites saturated first and the resulting statistic decorrelated from
  activity (v1 reported r=-0.42).  v2 instead uses excess register information
  at the declared early-transient time t=3.

v3 changelog (two v2 gates had spec-side defects):

* CHECK-02 no longer bounds the full cell density-matrix change by boundary
  activity: the cell's internal bond can change that state without boundary
  flux.  It now tests the exact pointer-continuity statement
  ``0.5*||p_t(Q_B)-p_(t-dt)(Q_B)||_1 <= c1*a_B(t)*dt + 1e-6``.  The single
  ``c1`` is still fixed by the declared pooled upper-activity-decile fit.
* CHECK-04/05 no longer sum excess mutual information over every register.
  Fragments are single exterior links, and ``I_B`` uses only the screening
  zone through exterior-link distance two from either cell boundary.  The
  boundary singletons remain eligible, but their joint pair
  ``(E_(2B-1),E_(2B+1))`` is never constructed because its difference is
  identically ``Q_B``.  In block01's right-first ordering, the eligible link
  offsets from ``2B`` are ``(+1,-1,+2,-2,+3,-3)`` modulo 12.
* The coupling panel is extended from ``(0.6,1.0)`` to ``(0.3,0.6,1.0)``;
  CHECK-03 retains the full-cell entropy-continuity theorem layer, and
  CHECK-04 retains the declared ``t=3`` endpoint in the early window
  ``t <= 3``.

The entropy theorem check uses the sharp Fannes--Audenaert continuity bound:
K. M. R. Audenaert, J. Phys. A 40 (2007) 8127--8136.  For a four-dimensional
cell it is ``T*log2(3) + h2(T)``, capped at ``T=3/4``.

Companion note: ACTIVITY_INFORMATION_BOUND_BOUNDED_NOTE_2026-07-09.md.
"""

from __future__ import annotations

from dataclasses import dataclass
import importlib
import sys
import time
from typing import Any

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla


N_SITES = 12
N_CELLS = N_SITES // 2
CELL_DIMENSION = 4
MASS = 0.3
V2_COUPLINGS = (0.6, 1.0)
COUPLINGS = (0.3,) + V2_COUPLINGS
GROUND_SEED_OFFSETS = {0.6: 0, 1.0: 1, 0.3: 2}
W_MAX = 4
T_FINAL = 10.0
DT = 0.1
N_TIMES = int(round(T_FINAL / DT)) + 1
TIMES = np.linspace(0.0, T_FINAL, N_TIMES)
EARLY_TIME = 3.0
EARLY_INDEX = int(round(EARLY_TIME / DT))
N_FRAGMENTS = N_SITES - 1
SCREENING_RADIUS = 2
SCREENING_LINK_OFFSETS = (1, -1, 2, -2, 3, -3)
EXTERIOR_LINK_DISTANCES = (0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5)
SCREENING_FRAGMENT_INDICES = tuple(
    index
    for index, distance in enumerate(EXTERIOR_LINK_DISTANCES)
    if distance <= SCREENING_RADIUS
)

# All gates and resolutions are declared before looking at the measurements.
STATIONARY_FLOOR = 1.0e-8
INTERFACE_EPSILON = 1.0e-6
ENTROPY_ENVELOPE_TOL = 1.0e-9
EPS_EXCESS_BITS = 0.02
GROUND_RESIDUAL_TOL = 1.0e-8
NORM_TOL = 1.0e-9
INTERNAL_TOL = 1.0e-9
MI_ROUNDOFF_TOL = 1.0e-10
RNG_SEED = 20260709


@dataclass(frozen=True)
class PackedLayout:
    """Lookup form of a partial-trace partition."""

    group_for_basis: np.ndarray
    local_for_basis: np.ndarray
    n_groups: int
    local_dim: int


@dataclass(frozen=True)
class ClassicalMILayout:
    """Sparse occupation-basis coarse graining for one ``Q_B:F`` pair."""

    projector: sp.csr_matrix
    pointer_outcomes: int
    fragment_outcomes: int


@dataclass
class CaseResult:
    coupling: float
    preparation: str
    kicked_cells: tuple[int, ...]
    information: np.ndarray
    fragment_information: np.ndarray
    cell_activity: np.ndarray
    cumulative_activity: np.ndarray
    pointer_delta: np.ndarray
    cell_delta: np.ndarray
    entropy_change: np.ndarray
    norm_error: float
    imported_activity_error: float
    reduction_error: float
    information_range_ok: bool


@dataclass(frozen=True)
class BoundResult:
    constant: float
    activity_decile: float
    violations: int
    maximum_ratio: float
    residual_quantiles: np.ndarray


@dataclass(frozen=True)
class EntropyEnvelopeResult:
    violations: int
    maximum_residual: float
    residual_quantiles: np.ndarray


@dataclass(frozen=True)
class RegressionResult:
    correlation: float
    slope: float
    intercept: float
    residual_quantiles: np.ndarray


def load_authorized_sources() -> tuple[Any, Any]:
    """Import the comparator and the exposed trace-norm convention."""

    old_dont_write_bytecode = sys.dont_write_bytecode
    sys.dont_write_bytecode = True
    try:
        engine = importlib.import_module(
            "gauged_schwinger_staggered_ed_engine_2026_07_08"
        )
        witnesses = importlib.import_module(
            "activity_energy_bound_witnesses_2026_07_08"
        )
    finally:
        sys.dont_write_bytecode = old_dont_write_bytecode

    engine_api = (
        "Basis",
        "apply_cdag_c",
        "build_many_body_hamiltonian",
        "charges",
    )
    witness_api = (
        "build_bond_trace_groups",
        "gauged_bond_activities",
        "gauged_local_arrays",
        "normalize",
    )
    missing = [f"engine.{name}" for name in engine_api if not hasattr(engine, name)]
    missing += [
        f"witnesses.{name}" for name in witness_api if not hasattr(witnesses, name)
    ]
    if missing:
        raise RuntimeError("missing authorized API: " + ",".join(missing))
    return engine, witnesses


def normalize(vector: np.ndarray) -> np.ndarray:
    norm = float(np.linalg.norm(vector))
    if not np.isfinite(norm) or norm == 0.0:
        raise RuntimeError("cannot normalize comparator state")
    return np.asarray(vector, dtype=np.complex128) / norm


def deterministic_ground_state(
    hamiltonian: sp.csr_matrix,
    seed: int,
) -> tuple[float, np.ndarray, float]:
    rng = np.random.default_rng(seed)
    v0 = normalize(
        rng.normal(size=hamiltonian.shape[0])
        + 1.0j * rng.normal(size=hamiltonian.shape[0])
    )
    values, vectors = spla.eigsh(
        hamiltonian,
        k=1,
        which="SA",
        v0=v0,
        tol=1.0e-11,
        ncv=min(48, hamiltonian.shape[0] - 1),
        maxiter=20000,
    )
    energy = float(values[0].real)
    state = normalize(vectors[:, 0])
    residual = float(np.linalg.norm(hamiltonian @ state - energy * state))
    return energy, state, residual


def vectorize_imported_groups(groups: Any, dimension: int) -> PackedLayout:
    """Vectorize ``BondTraceGroups`` without changing its partition."""

    group_for_basis = np.full(dimension, -1, dtype=np.int64)
    local_for_basis = np.full(dimension, -1, dtype=np.int8)
    for group_index, (indices, local_indices) in enumerate(
        zip(groups.indices, groups.local_indices)
    ):
        if np.any(group_for_basis[indices] >= 0):
            raise RuntimeError("imported bond trace groups overlap")
        group_for_basis[indices] = group_index
        local_for_basis[indices] = local_indices
    if np.any(group_for_basis < 0) or np.any(local_for_basis < 0):
        raise RuntimeError("imported bond trace groups do not cover the basis")
    return PackedLayout(group_for_basis, local_for_basis, len(groups.indices), 4)


def classical_outcomes(
    engine: Any,
    basis: Any,
) -> tuple[np.ndarray, np.ndarray]:
    """Return cell charges and Gauss-law link registers for every basis ket.

    The engine convention is ``E_l = W + sum_{k<=l} q_k``.  Calling these
    quantities registers is a classical occupation-basis coarse graining; no
    tensor-factor claim about the constrained Hilbert space is made.
    """

    cell_charges = np.empty((N_CELLS, basis.dim), dtype=np.int8)
    link_registers = np.empty((N_SITES, basis.dim), dtype=np.int16)
    for index in range(basis.dim):
        _, fock_value, w_index = basis.unpack(index)
        charge = engine.charges(N_SITES, int(fock_value))
        fields = basis.w_value(w_index) + np.cumsum(charge)
        cell_charges[:, index] = charge.reshape(N_CELLS, 2).sum(axis=1)
        link_registers[:, index] = fields
    if np.min(cell_charges) < -1 or np.max(cell_charges) > 1:
        raise RuntimeError("cell charge left Q_B in {-1,0,1}")
    return cell_charges, link_registers


def exterior_register_links(cell: int) -> tuple[int, ...]:
    """Return block01 v3's single exterior links, right first at ties.

    The internal link ``E_(2B)`` is absent.  Boundary links ``2B-1`` and
    ``2B+1`` obey ``Q_B=E_(2B+1)-E_(2B-1)`` exactly, so they are measured only
    as separate singletons; no joint boundary-pair layout is constructed.
    """

    if not 0 <= cell < N_CELLS:
        raise ValueError("invalid pointer cell")
    internal = 2 * cell
    right_boundary = (internal + 1) % N_SITES
    left_boundary = (internal - 1) % N_SITES
    links = tuple(
        link
        for distance in range(N_CELLS - 1)
        for link in (
            (right_boundary + distance) % N_SITES,
            (left_boundary - distance) % N_SITES,
        )
    ) + ((internal + N_CELLS) % N_SITES,)
    if len(links) != N_FRAGMENTS or len(set(links)) != N_FRAGMENTS:
        raise RuntimeError("exterior register links are not unique")
    if internal in links or set(links) != set(range(N_SITES)) - {internal}:
        raise RuntimeError("exterior register links have the wrong support")
    screening_links = tuple(
        (internal + offset) % N_SITES for offset in SCREENING_LINK_OFFSETS
    )
    if links[: len(SCREENING_FRAGMENT_INDICES)] != screening_links:
        raise RuntimeError("screening zone is not the exterior-link prefix")
    return links


def build_classical_mi_layouts(
    cell_charges: np.ndarray,
    link_registers: np.ndarray,
) -> list[list[ClassicalMILayout]]:
    """Build eligible single-link ``Q_B:E_l`` coarse grainings."""

    dimension = cell_charges.shape[1]
    basis_indices = np.arange(dimension, dtype=np.int64)
    layouts: list[list[ClassicalMILayout]] = []
    for cell in range(N_CELLS):
        _, pointer_index = np.unique(cell_charges[cell], return_inverse=True)
        n_pointer = int(np.max(pointer_index)) + 1
        cell_layouts: list[ClassicalMILayout] = []
        for link in exterior_register_links(cell):
            outcomes = link_registers[link, :, None]
            _, fragment_index = np.unique(
                outcomes, axis=0, return_inverse=True
            )
            n_fragment = int(np.max(fragment_index)) + 1
            joint_index = pointer_index * n_fragment + fragment_index
            projector = sp.coo_matrix(
                (
                    np.ones(dimension, dtype=np.float64),
                    (basis_indices, joint_index),
                ),
                shape=(dimension, n_pointer * n_fragment),
            ).tocsr()
            cell_layouts.append(
                ClassicalMILayout(projector, n_pointer, n_fragment)
            )
        layouts.append(cell_layouts)
    return layouts


def build_hop_kick(engine: Any, basis: Any) -> tuple[sp.csr_matrix, float]:
    """Construct ``c_0^dag c_1 + c_1^dag c_0`` in the engine basis."""

    rows: list[int] = []
    columns: list[int] = []
    data: list[complex] = []
    for local_fock, fock_value in enumerate(basis.focks):
        fock = int(fock_value)
        for create_site, annihilate_site in ((0, 1), (1, 0)):
            applied = engine.apply_cdag_c(
                fock, create_site, annihilate_site
            )
            if applied is None:
                continue
            new_fock, sign = applied
            new_local = basis.fock_to_local.get(new_fock)
            if new_local is None:
                continue
            for w_index in range(basis.n_w):
                rows.append(basis.index(new_local, w_index))
                columns.append(basis.index(local_fock, w_index))
                data.append(complex(sign))
    operator = sp.coo_matrix(
        (data, (rows, columns)),
        shape=(basis.dim, basis.dim),
        dtype=np.complex128,
    ).tocsr()
    difference = operator - operator.getH()
    hermiticity_error = (
        float(np.max(np.abs(difference.data))) if difference.nnz else 0.0
    )
    return operator, hermiticity_error


def packed_amplitudes(states: np.ndarray, layout: PackedLayout) -> np.ndarray:
    vectors = np.asarray(states, dtype=np.complex128)
    packed = np.zeros(
        (vectors.shape[0], layout.n_groups, layout.local_dim),
        dtype=np.complex128,
    )
    packed[:, layout.group_for_basis, layout.local_for_basis] = vectors
    return packed


def batched_bond_activity(
    states: np.ndarray,
    hamiltonian: sp.csr_matrix,
    layouts: list[PackedLayout],
) -> tuple[np.ndarray, float]:
    """Exact imported bond trace-norm velocity in batched algebraic form.

    The partition and definition are those exposed by
    activity_energy_bound_witnesses_2026_07_08.py.  The batching mirrors the
    cited reduced_outer/gauged_bond_activities operations exactly and is
    cross-checked against the exposed scalar call by ``measure_case``.
    """

    vectors = np.asarray(states, dtype=np.complex128)
    derivatives = np.asarray(
        (-1.0j * (hamiltonian @ vectors.T)).T,
        dtype=np.complex128,
    )
    activities = np.empty((vectors.shape[0], len(layouts)), dtype=np.float64)
    trace_error = 0.0
    for bond, layout in enumerate(layouts):
        amplitudes = packed_amplitudes(vectors, layout)
        derivative_amplitudes = packed_amplitudes(derivatives, layout)
        drho = np.einsum(
            "tgi,tgj->tij",
            derivative_amplitudes,
            amplitudes.conj(),
            optimize=True,
        )
        drho += np.einsum(
            "tgi,tgj->tij",
            amplitudes,
            derivative_amplitudes.conj(),
            optimize=True,
        )
        drho = 0.5 * (drho + drho.conj().transpose(0, 2, 1))
        trace_error = max(
            trace_error,
            float(np.max(np.abs(np.trace(drho, axis1=1, axis2=2)))),
        )
        activities[:, bond] = np.sum(
            np.abs(np.linalg.eigvalsh(drho)), axis=1
        )
    return activities, trace_error


def binary_entropy(probability: np.ndarray) -> np.ndarray:
    raw = np.asarray(probability, dtype=np.float64)
    if (
        not np.all(np.isfinite(raw))
        or np.min(raw) < -INTERNAL_TOL
        or np.max(raw) > 1.0 + INTERNAL_TOL
    ):
        raise RuntimeError("binary-entropy probability left its numerical range")
    # Clip only roundoff already covered by the explicit machinery tolerance.
    p = np.clip(raw, 0.0, 1.0)
    out = np.zeros_like(p)
    left = p > 0.0
    right = p < 1.0
    out[left] -= p[left] * np.log2(p[left])
    out[right] -= (1.0 - p[right]) * np.log2(1.0 - p[right])
    return out


def density_entropy(density_matrices: np.ndarray) -> np.ndarray:
    hermitian = 0.5 * (
        density_matrices + density_matrices.conj().transpose(0, 2, 1)
    )
    eigenvalues = np.linalg.eigvalsh(hermitian)
    if (
        not np.all(np.isfinite(eigenvalues))
        or float(np.min(eigenvalues)) < -INTERNAL_TOL
        or float(np.max(eigenvalues)) > 1.0 + INTERNAL_TOL
    ):
        raise RuntimeError("reduced density spectrum left its numerical range")
    # Remove only tolerated eigensolver roundoff after checking it explicitly.
    positive = np.where(eigenvalues > 0.0, eigenvalues, 0.0)
    terms = np.zeros_like(positive)
    mask = positive > 0.0
    terms[mask] = -positive[mask] * np.log2(positive[mask])
    return np.sum(terms, axis=1)


def batched_reduced_density(
    states: np.ndarray,
    layout: PackedLayout,
) -> tuple[np.ndarray, float]:
    """Return a batch of two-site density matrices in the imported layout."""

    amplitudes = packed_amplitudes(states, layout)
    rho = np.einsum("tgi,tgj->tij", amplitudes, amplitudes.conj(), optimize=True)
    rho = 0.5 * (rho + rho.conj().transpose(0, 2, 1))
    trace_error = float(
        np.max(np.abs(np.trace(rho, axis1=1, axis2=2) - 1.0))
    )
    return rho, trace_error


def classical_mutual_information(
    states: np.ndarray,
    layouts: list[list[ClassicalMILayout]],
) -> tuple[np.ndarray, float, bool]:
    """Evaluate occupation-basis classical ``I(Q_B:F)`` in bits."""

    probabilities = np.abs(np.asarray(states, dtype=np.complex128)) ** 2
    norms = np.sum(probabilities, axis=1)
    if np.any(norms <= 0.0) or not np.all(np.isfinite(norms)):
        raise RuntimeError("nonpositive or nonfinite state norm")
    norm_error = float(np.max(np.abs(norms - 1.0)))
    probabilities = probabilities / norms[:, None]
    fragment_counts = {len(cell_layouts) for cell_layouts in layouts}
    if fragment_counts != {N_FRAGMENTS}:
        raise RuntimeError("unexpected single-link fragment layout count")
    information = np.empty(
        (states.shape[0], N_CELLS, N_FRAGMENTS),
        dtype=np.float64,
    )
    upper_error = 0.0
    for cell, cell_layouts in enumerate(layouts):
        for fragment, layout in enumerate(cell_layouts):
            joint_flat = np.asarray(probabilities @ layout.projector)
            joint = joint_flat.reshape(
                states.shape[0],
                layout.pointer_outcomes,
                layout.fragment_outcomes,
            )
            pointer = np.sum(joint, axis=2)
            register = np.sum(joint, axis=1)
            denominator = pointer[:, :, None] * register[:, None, :]
            terms = np.zeros_like(joint)
            present = joint > 0.0
            if np.any(present & (denominator <= 0.0)):
                raise RuntimeError("positive joint mass has zero marginal mass")
            terms[present] = joint[present] * np.log2(
                joint[present] / denominator[present]
            )
            values = np.sum(terms, axis=(1, 2))
            information[:, cell, fragment] = values
            upper_error = max(
                upper_error,
                float(
                    np.max(values - np.log2(layout.pointer_outcomes))
                ),
            )
    finite = bool(np.all(np.isfinite(information)))
    minimum = float(np.min(information)) if finite else float("-inf")
    range_ok = bool(
        finite
        and minimum >= -MI_ROUNDOFF_TOL
        and upper_error <= MI_ROUNDOFF_TOL
    )
    # The only clipping is roundoff already exposed by ``range_ok``.
    information = np.maximum(information, 0.0)
    return information, norm_error, range_ok


def excess_register_information(
    mutual_information: np.ndarray,
    ground_mutual_information: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    """Sum pinned positive GS excess over the screening-zone prefix only."""

    excess_by_fragment = np.maximum(
        0.0,
        mutual_information
        - np.asarray(ground_mutual_information, dtype=np.float64)[None, :, :],
    )
    screening_excess = excess_by_fragment[..., SCREENING_FRAGMENT_INDICES]
    return np.sum(screening_excess, axis=2), excess_by_fragment


def pointer_distribution_change(
    states: np.ndarray,
    cell_charges: np.ndarray,
) -> np.ndarray:
    """Return backward-step total variation of each ``Q_B`` distribution."""

    probabilities = np.abs(np.asarray(states, dtype=np.complex128)) ** 2
    norms = np.sum(probabilities, axis=1)
    if np.any(norms <= 0.0) or not np.all(np.isfinite(norms)):
        raise RuntimeError("nonpositive or nonfinite state norm")
    probabilities = probabilities / norms[:, None]
    distributions = np.empty(
        (states.shape[0], N_CELLS, 3), dtype=np.float64
    )
    for cell in range(N_CELLS):
        outcomes = np.asarray(cell_charges[cell] + 1, dtype=np.int64)
        if not np.all((0 <= outcomes) & (outcomes < 3)):
            raise RuntimeError("pointer outcome left {-1,0,1}")
        indicator = sp.csr_matrix(
            (
                np.ones(outcomes.size, dtype=np.float64),
                (np.arange(outcomes.size, dtype=np.int64), outcomes),
            ),
            shape=(outcomes.size, 3),
        )
        distributions[:, cell] = np.asarray(probabilities @ indicator)
    normalization_error = float(
        np.max(np.abs(np.sum(distributions, axis=2) - 1.0))
    )
    if normalization_error > INTERNAL_TOL:
        raise RuntimeError("pointer distribution normalization failed")
    delta = np.zeros((states.shape[0], N_CELLS), dtype=np.float64)
    delta[1:] = 0.5 * np.sum(
        np.abs(distributions[1:] - distributions[:-1]), axis=2
    )
    if (
        not np.all(np.isfinite(delta))
        or np.min(delta) < -INTERNAL_TOL
        or np.max(delta) > 1.0 + INTERNAL_TOL
    ):
        raise RuntimeError("pointer total variation left its numerical range")
    return delta


def cell_state_observables(
    states: np.ndarray,
    cell_layouts: list[PackedLayout],
) -> tuple[np.ndarray, np.ndarray, float]:
    """Return backward-step trace distance and entropy change for each cell."""

    delta = np.zeros((states.shape[0], N_CELLS), dtype=np.float64)
    entropy_change = np.zeros_like(delta)
    reduction_error = 0.0
    for cell, layout in enumerate(cell_layouts):
        density, trace_error = batched_reduced_density(states, layout)
        reduction_error = max(reduction_error, trace_error)
        differences = density[1:] - density[:-1]
        differences = 0.5 * (
            differences + differences.conj().transpose(0, 2, 1)
        )
        delta[1:, cell] = 0.5 * np.sum(
            np.abs(np.linalg.eigvalsh(differences)), axis=1
        )
        entropy = density_entropy(density)
        entropy_change[1:, cell] = np.abs(np.diff(entropy))
    if (
        not np.all(np.isfinite(delta))
        or np.min(delta) < -INTERNAL_TOL
        or np.max(delta) > 1.0 + INTERNAL_TOL
    ):
        raise RuntimeError("cell trace distance left its numerical range")
    return delta, entropy_change, reduction_error


def measure_case(
    *,
    coupling: float,
    preparation: str,
    kicked_cells: tuple[int, ...],
    states: np.ndarray,
    hamiltonian: sp.csr_matrix,
    ground_mutual_information: np.ndarray,
    cell_charges: np.ndarray,
    trace_groups: list[Any],
    bond_layouts: list[PackedLayout],
    cell_layouts: list[PackedLayout],
    mi_layouts: list[list[ClassicalMILayout]],
    witnesses: Any,
) -> CaseResult:
    bond_activity, activity_trace_error = batched_bond_activity(
        states, hamiltonian, bond_layouts
    )
    cell_activity = np.empty((states.shape[0], N_CELLS), dtype=np.float64)
    for cell in range(N_CELLS):
        # Bond b is (b,b+1).  The boundary of (2B,2B+1) is b=2B-1,2B+1.
        left_boundary = (2 * cell - 1) % N_SITES
        right_boundary = (2 * cell + 1) % N_SITES
        cell_activity[:, cell] = (
            bond_activity[:, left_boundary] + bond_activity[:, right_boundary]
        )
    cumulative_activity = np.zeros_like(cell_activity)
    cumulative_activity[1:] = DT * np.cumsum(
        0.5 * (cell_activity[:-1] + cell_activity[1:]), axis=0
    )

    imported_error = 0.0
    for time_index in (0, N_TIMES // 2, N_TIMES - 1):
        direct = witnesses.gauged_bond_activities(
            states[time_index], hamiltonian, trace_groups
        )
        imported_error = max(
            imported_error,
            float(np.max(np.abs(direct - bond_activity[time_index]))),
        )

    mutual_information, mi_norm_error, mi_range_ok = (
        classical_mutual_information(states, mi_layouts)
    )
    information, fragment_information = excess_register_information(
        mutual_information, ground_mutual_information
    )
    pointer_delta = pointer_distribution_change(states, cell_charges)
    cell_delta, entropy_change, cell_reduction_error = cell_state_observables(
        states, cell_layouts
    )
    finite = bool(
        np.all(np.isfinite(information))
        and np.all(np.isfinite(fragment_information))
        and np.all(np.isfinite(cell_activity))
        and np.all(np.isfinite(cumulative_activity))
        and np.all(np.isfinite(pointer_delta))
        and np.all(np.isfinite(entropy_change))
    )
    information_range_ok = bool(
        finite
        and mi_range_ok
        and np.min(fragment_information) >= 0.0
        and np.min(cell_activity) >= -INTERNAL_TOL
    )
    norms = np.sum(np.abs(states) ** 2, axis=1)
    norm_error = max(
        float(np.max(np.abs(norms - 1.0))), mi_norm_error
    )
    return CaseResult(
        coupling=coupling,
        preparation=preparation,
        kicked_cells=kicked_cells,
        information=information,
        fragment_information=fragment_information,
        cell_activity=cell_activity,
        cumulative_activity=cumulative_activity,
        pointer_delta=pointer_delta,
        cell_delta=cell_delta,
        entropy_change=entropy_change,
        norm_error=norm_error,
        imported_activity_error=imported_error,
        reduction_error=max(activity_trace_error, cell_reduction_error),
        information_range_ok=information_range_ok,
    )


def fit_activity_bound(results: list[CaseResult]) -> BoundResult:
    """Test that the ``Q_B`` outcome law changes only through its boundary."""

    activities = np.concatenate(
        [result.cell_activity[1:].ravel() for result in results]
    )
    changes = np.concatenate(
        [result.pointer_delta[1:].ravel() for result in results]
    )
    if activities.shape != changes.shape:
        raise RuntimeError("activity/pointer-change step alignment failed")
    activity_decile = float(np.quantile(activities, 0.9))
    upper = activities >= activity_decile
    upper &= activities > np.finfo(float).tiny
    if not np.any(upper):
        raise RuntimeError("empty upper activity decile")
    ratios = changes[upper] / (activities[upper] * DT)
    constant = float(np.max(ratios))
    linear_bound = constant * activities * DT
    residuals = changes - linear_bound
    violations = int(np.count_nonzero(residuals > INTERFACE_EPSILON))
    maximum_ratio = float(
        np.max(changes / (linear_bound + INTERFACE_EPSILON))
    )
    residual_quantiles = np.quantile(residuals, (0.0, 0.5, 0.9, 0.99, 1.0))
    return BoundResult(
        constant=constant,
        activity_decile=activity_decile,
        violations=violations,
        maximum_ratio=maximum_ratio,
        residual_quantiles=np.asarray(residual_quantiles, dtype=np.float64),
    )


def check_entropy_envelope(results: list[CaseResult]) -> EntropyEnvelopeResult:
    trace_distance = np.concatenate(
        [result.cell_delta[1:].ravel() for result in results]
    )
    entropy_change = np.concatenate(
        [result.entropy_change[1:].ravel() for result in results]
    )
    capped = np.minimum(
        trace_distance, 1.0 - 1.0 / CELL_DIMENSION
    )
    envelope = capped * np.log2(CELL_DIMENSION - 1.0) + binary_entropy(capped)
    residuals = entropy_change - envelope
    return EntropyEnvelopeResult(
        violations=int(
            np.count_nonzero(residuals > ENTROPY_ENVELOPE_TOL)
        ),
        maximum_residual=float(np.max(residuals)),
        residual_quantiles=np.asarray(
            np.quantile(residuals, (0.0, 0.5, 0.9, 0.99, 1.0)),
            dtype=np.float64,
        ),
    )


def regress_opportunity(results: list[CaseResult]) -> RegressionResult:
    activity = np.concatenate(
        [result.cumulative_activity[EARLY_INDEX] for result in results]
    )
    gained = np.concatenate(
        [result.information[EARLY_INDEX] for result in results]
    )
    if np.std(activity) == 0.0 or np.std(gained) == 0.0:
        raise RuntimeError("degenerate activity-information regression")
    correlation = float(np.corrcoef(activity, gained)[0, 1])
    design = np.column_stack((activity, np.ones_like(activity)))
    slope, intercept = np.linalg.lstsq(design, gained, rcond=None)[0]
    residuals = gained - (slope * activity + intercept)
    return RegressionResult(
        correlation=correlation,
        slope=float(slope),
        intercept=float(intercept),
        residual_quantiles=np.asarray(
            np.quantile(residuals, (0.05, 0.5, 0.95)), dtype=np.float64
        ),
    )


def kick_cell_consistency(
    results: list[CaseResult],
) -> tuple[bool, list[str]]:
    details: list[str] = []
    passed = True
    for result in results:
        gained = result.information[EARLY_INDEX]
        count = len(result.kicked_cells)
        top = tuple(
            sorted(
                int(cell)
                for cell in np.argsort(-gained, kind="stable")[:count]
            )
        )
        expected = tuple(sorted(result.kicked_cells))
        ok = top == expected
        passed = passed and ok
        details.append(
            f"g={result.coupling:g}/{result.preparation}:top={','.join(map(str, top))}"
            f"/kick={','.join(map(str, expected))}"
            f"/Imax={fmt(float(np.max(gained)))}{'' if ok else '!'}"
        )
    return passed, details


def fmt(value: float) -> str:
    if not np.isfinite(value):
        return "nan"
    return f"{value:.6g}"


def fmt_vector(values: np.ndarray) -> str:
    return "[" + ",".join(fmt(float(value)) for value in values) + "]"


def build_output(
    *,
    stationary_information_maximum: float,
    stationary_delta_maximum: float,
    bound: BoundResult,
    entropy_envelope: EntropyEnvelopeResult,
    regression: RegressionResult,
    consistency_ok: bool,
    consistency_details: list[str],
    machinery_ok: bool,
    maximum_ground_residual: float,
    maximum_norm_error: float,
    maximum_imported_error: float,
    maximum_reduction_error: float,
    hop_hermiticity_error: float,
    elapsed: float,
) -> tuple[list[str], int]:
    stationary_ok = bool(
        stationary_information_maximum <= STATIONARY_FLOOR
        and stationary_delta_maximum <= STATIONARY_FLOOR
    )
    bound_ok = bound.violations == 0
    entropy_ok = entropy_envelope.violations == 0
    regression_ok = regression.correlation >= 0.8
    checks = {
        "CHECK-01": stationary_ok,
        "CHECK-02": bound_ok,
        "CHECK-03": entropy_ok,
        "CHECK-04": regression_ok,
        "CHECK-05": consistency_ok,
    }
    failed = [name for name, passed in checks.items() if not passed]
    if not machinery_ok:
        verdict = "MACHINERY-FAIL"
        exit_code = 2
    elif failed:
        verdict = "BOUND-PARTIAL"
        exit_code = 1
    else:
        verdict = "ACTIVITY-BOUNDS-INFORMATION"
        exit_code = 0

    setup = (
        "SETUP N=12 cells=B:(2B,2B+1) m=0.3 g=[0.3,0.6,1] Qtotal=0 Wmax=4 "
        "t=0:0.1:10; kick=a:exp(+i0.7n0),b:exp(+i0.5(n0+n6)),"
        "c:exp(+i0.5(c0dag*c1+h.c.)); pointer=Q_B=q_2B+q_(2B+1); "
        "register=E_l=W+sum(k<=l)q_k; "
        "F_B=all single exterior E_l except internal E_2B; "
        "eligible-for-I_B=boundary-distance<=2,offsets=[+1,-1,+2,-2,+3,-3]; "
        "I_B=sum_eligible-l max(0,Iclassical_t(Q_B:E_l)-Iclassical_GS(Q_B:E_l)) bits; "
        "a_B=a_bond[2B-1]+a_bond[2B+1]"
    )
    controls = (
        f"CHECK-01={'ok' if stationary_ok else 'FAIL'} "
        f"unkicked-GS max-Iexc={stationary_information_maximum:.3e} "
        f"max-delta_B={stationary_delta_maximum:.3e} "
        f"floors-achieved=[{stationary_information_maximum:.3e},"
        f"{stationary_delta_maximum:.3e}] gate<={STATIONARY_FLOOR:.1e}"
    )
    bound_line = (
        f"CHECK-02={'ok' if bound_ok else 'FAIL'} c1={fmt(bound.constant)} "
        f"fit=max(TV[p_t(Q_B),p_prev(Q_B)]/(a_B*dt))@a>=q90="
        f"{fmt(bound.activity_decile)} "
        "a_B=right-endpoint-boundary-velocity "
        f"eps={INTERFACE_EPSILON:.1e} violations={bound.violations} "
        f"max-ratio={fmt(bound.maximum_ratio)} residual=pointer-TV-c1*a_B*dt "
        f"q[min,50,90,99,max]={fmt_vector(bound.residual_quantiles)}"
    )
    entropy_line = (
        f"CHECK-03={'ok' if entropy_ok else 'FAIL'} "
        "Fannes-Audenaert(Audenaert-2007,JPhysA40:8127) "
        "|DeltaS_cell|<=T*log2(3)+h2(T),"
        "T=min(full-cell-trace-distance,3/4),d=4 "
        f"tol={ENTROPY_ENVELOPE_TOL:.1e} violations={entropy_envelope.violations} "
        f"max-residual={entropy_envelope.maximum_residual:.3e} "
        f"q[min,50,90,99,max]={fmt_vector(entropy_envelope.residual_quantiles)}"
    )
    opportunity = (
        f"CHECK-04={'ok' if regression_ok else 'FAIL'} r={fmt(regression.correlation)} "
        f"I_B(t=3<=3)=slope*A_B(t=3)+intercept slope={fmt(regression.slope)} "
        f"intercept={fmt(regression.intercept)} "
        f"q[5,50,95]={fmt_vector(regression.residual_quantiles)}; "
        f"CHECK-05={'ok' if consistency_ok else 'FAIL'} "
        + ";".join(consistency_details)
    )
    total = (
        f"TOTAL {verdict} c1={fmt(bound.constant)} r={fmt(regression.correlation)} "
        f"failed={'none' if not failed else ','.join(failed)} "
        f"machinery={'ok' if machinery_ok else 'FAIL'} "
        f"GS-residual={maximum_ground_residual:.2e} norm-error={maximum_norm_error:.2e} "
        f"imported-activity-error={maximum_imported_error:.2e} "
        f"reduction-error={maximum_reduction_error:.2e} "
        f"hop-Herm-error={hop_hermiticity_error:.2e} elapsed={elapsed:.2f}s "
        "SPEC-NOTE=envelope=sharp-Fannes-Audenaert-D4;"
        "v3-CHECK02=pointer-continuity-not-full-cell;"
        "v3-attribution=all-single-exterior-link-fragments,"
        "I_B-only-boundary-distance<=2-screening-zone,"
        "eligible-offsets:+1|-1|+2|-2|+3|-3,joint-boundary-pair-identity-excluded;"
        f"floors=stationary:{STATIONARY_FLOOR:.0e},interface-eps:{INTERFACE_EPSILON:.0e},"
        f"entropy-tol:{ENTROPY_ENVELOPE_TOL:.0e},eps_exc:{EPS_EXCESS_BITS:g}-bits;"
        "early-window=t<=3,endpoint=t3-grid-index30,A=trapezoid,"
        "step-a=right-endpoint;"
        "register=Gauss-E_l-W-plus-left-partial-charge-sum,"
        "occupation-probability-classical-MI,positive-GS-excess-without-eps-subtraction;"
        "composition=conditional-information-rate-envelope-"
        "F(min(c1*a*dt+eps,3/4))/dt-not-linear-information-bound;"
        "CHECK-02-violations-interpretation=pointer-flow-is-driven-by-bond-"
        "COHERENCE(a-current-VALUE)-while-activity-is-state-CHANGE:a-steady-"
        "current-through-a-quiet-bond-moves-the-pointer-with-little-activity,"
        "so-no-linear-activity-gate-on-pointer-flow-exists(measured-"
        "counterexample,kept-as-finding);"
        "d1-attribution-limit=all-exterior-information-flows-through-the-"
        "two-boundary-registers(Markov-blanket),so-per-cell-attribution-"
        "saturates-in-d=1;"
        "no-silent-fixes;no-audit-status"
    )
    return (
        [setup, controls, bound_line, entropy_line, opportunity, total],
        exit_code,
    )


def run() -> tuple[list[str], int]:
    started = time.monotonic()
    engine, witnesses = load_authorized_sources()
    basis = engine.Basis(
        n_sites=N_SITES,
        w_max=W_MAX,
        charge_sector=0,
        rotor=True,
    )
    trace_groups = [
        witnesses.build_bond_trace_groups(basis, bond)
        for bond in range(N_SITES)
    ]
    bond_layouts = [
        vectorize_imported_groups(groups, basis.dim) for groups in trace_groups
    ]
    cell_layouts = [bond_layouts[2 * cell] for cell in range(N_CELLS)]
    cell_charges, link_registers = classical_outcomes(engine, basis)
    mi_layouts = build_classical_mi_layouts(cell_charges, link_registers)
    occupations, _ = witnesses.gauged_local_arrays(
        engine, basis, MASS, V2_COUPLINGS[0]
    )
    hop_kick, hop_hermiticity_error = build_hop_kick(engine, basis)

    results: list[CaseResult] = []
    stationary_information_maximum = 0.0
    stationary_delta_maximum = 0.0
    maximum_ground_residual = 0.0
    maximum_norm_error = 0.0
    maximum_imported_error = 0.0
    maximum_reduction_error = 0.0
    all_information_ranges_ok = True

    for coupling in COUPLINGS:
        hamiltonian = engine.build_many_body_hamiltonian(
            basis,
            MASS,
            coupling,
            boundary_holonomy_shifts_w=True,
        ).tocsr()
        _, ground_state, ground_residual = deterministic_ground_state(
            hamiltonian,
            RNG_SEED + GROUND_SEED_OFFSETS[coupling],
        )
        maximum_ground_residual = max(
            maximum_ground_residual, ground_residual
        )

        ground_mi, ground_norm_error, ground_mi_ok = (
            classical_mutual_information(ground_state[None, :], mi_layouts)
        )
        maximum_norm_error = max(maximum_norm_error, ground_norm_error)
        all_information_ranges_ok = all_information_ranges_ok and ground_mi_ok

        # The two phase preparations are retained from v1.  Preparation c is
        # the newly pinned local hop kick on the internal bond of cell B=0.
        kicked_a = np.exp(1.0j * 0.7 * occupations[0]) * ground_state
        kicked_b = np.exp(
            1.0j * 0.5 * (occupations[0] + occupations[6])
        ) * ground_state
        kicked_c = spla.expm_multiply(
            (0.5j) * hop_kick, ground_state, traceA=0.0
        )
        initial_states = np.column_stack(
            (ground_state, kicked_a, kicked_b, kicked_c)
        )
        generator = (-1.0j) * hamiltonian
        trace_generator = complex(-1.0j * np.sum(hamiltonian.diagonal()))
        evolved = spla.expm_multiply(
            generator,
            initial_states,
            start=0.0,
            stop=T_FINAL,
            num=N_TIMES,
            endpoint=True,
            traceA=trace_generator,
        )
        all_norms = np.sum(np.abs(evolved) ** 2, axis=1)
        maximum_norm_error = max(
            maximum_norm_error,
            float(np.max(np.abs(all_norms - 1.0))),
        )
        control_mi, control_norm_error, control_mi_ok = (
            classical_mutual_information(evolved[:, :, 0], mi_layouts)
        )
        control_information, _ = excess_register_information(
            control_mi, ground_mi[0]
        )
        control_delta, _, control_reduction_error = cell_state_observables(
            evolved[:, :, 0], cell_layouts
        )
        stationary_information_maximum = max(
            stationary_information_maximum,
            float(np.max(control_information)),
        )
        stationary_delta_maximum = max(
            stationary_delta_maximum,
            float(np.max(control_delta)),
        )
        maximum_norm_error = max(maximum_norm_error, control_norm_error)
        maximum_reduction_error = max(
            maximum_reduction_error, control_reduction_error
        )
        all_information_ranges_ok = (
            all_information_ranges_ok and control_mi_ok
        )

        case_specs = (
            ("a", (0,), 1),
            ("b", (0, 3), 2),
            ("c", (0,), 3),
        )
        for preparation, kicked_cells, state_index in case_specs:
            result = measure_case(
                coupling=coupling,
                preparation=preparation,
                kicked_cells=kicked_cells,
                states=evolved[:, :, state_index],
                hamiltonian=hamiltonian,
                ground_mutual_information=ground_mi[0],
                cell_charges=cell_charges,
                trace_groups=trace_groups,
                bond_layouts=bond_layouts,
                cell_layouts=cell_layouts,
                mi_layouts=mi_layouts,
                witnesses=witnesses,
            )
            results.append(result)
            maximum_norm_error = max(maximum_norm_error, result.norm_error)
            maximum_imported_error = max(
                maximum_imported_error, result.imported_activity_error
            )
            maximum_reduction_error = max(
                maximum_reduction_error, result.reduction_error
            )
            all_information_ranges_ok = (
                all_information_ranges_ok and result.information_range_ok
            )
        del evolved, hamiltonian

    bound = fit_activity_bound(results)
    entropy_envelope = check_entropy_envelope(results)
    regression = regress_opportunity(results)
    consistency_ok, consistency_details = kick_cell_consistency(results)
    elapsed = time.monotonic() - started
    machinery_ok = bool(
        maximum_ground_residual <= GROUND_RESIDUAL_TOL
        and maximum_norm_error <= NORM_TOL
        and maximum_imported_error <= INTERNAL_TOL
        and maximum_reduction_error <= INTERNAL_TOL
        and hop_hermiticity_error <= INTERNAL_TOL
        and all_information_ranges_ok
        and elapsed < 900.0
    )
    return build_output(
        stationary_information_maximum=stationary_information_maximum,
        stationary_delta_maximum=stationary_delta_maximum,
        bound=bound,
        entropy_envelope=entropy_envelope,
        regression=regression,
        consistency_ok=consistency_ok,
        consistency_details=consistency_details,
        machinery_ok=machinery_ok,
        maximum_ground_residual=maximum_ground_residual,
        maximum_norm_error=maximum_norm_error,
        maximum_imported_error=maximum_imported_error,
        maximum_reduction_error=maximum_reduction_error,
        hop_hermiticity_error=hop_hermiticity_error,
        elapsed=elapsed,
    )


def main() -> int:
    try:
        lines, exit_code = run()
    except Exception as exc:  # noqa: BLE001 - preserve the six-line contract.
        message = " ".join(str(exc).split())[:240]
        print(
            f"TOTAL MACHINERY-FAIL error={type(exc).__name__}:{message} "
            "SPEC-NOTE=v3-pointer-continuity-plus-full-cell-Fannes-Audenaert;"
            "stationary/interface/envelope-floors-declared;"
            "early-window=t<=3-endpoint-t3;"
            "attribution=all-single-exterior-links-I_B-screening-radius2-"
            "joint-boundary-pair-identity-excluded;"
            "register=Gauss-link-partial-sums,classical-MI-positive-GS-excess;"
            "no-silent-fixes;no-audit-status"
        )
        return 2
    for line in lines:
        print(line)
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
