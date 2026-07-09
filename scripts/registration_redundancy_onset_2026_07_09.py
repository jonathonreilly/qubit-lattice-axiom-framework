#!/usr/bin/env python3
"""Block01 of the registration-bar campaign: framework-native redundancy onset.

Revision changelog
------------------
v1 measured the one-site occupation pointer ``n_x`` and found NO redundancy
onset anywhere.  Its adjacent fragment carried only the static interacting-GS
correlation (about 0.2 bits, unchanged between kicked and unkicked sites), and
all farther fragments carried only about 1e-3 bits.  In this comparator that
negative result confirms the pointer-conservation necessity theorem in
``frontier_record_formation_dynamics_constraint_2026_06_05.py``: hopping does
not commute with ``n_x``, so the proposed site-occupation pointer was
demolished as written.  This v1 finding is retained rather than reinterpreted.

v2 uses the framework-native pointer and record substrate.  A physical
staggered cell ``B`` is the site pair ``(2B, 2B+1)`` and its gauge-invariant
pointer is the three-outcome charge

    Q_B = q_(2B) + q_(2B+1),       q_n = n_n - (n mod 2).

Internal hopping commutes with ``Q_B``; only hopping through either cell
boundary demolishes it.  In the link-eliminated engine, Gauss's law is
implemented exactly as ``E_n = W + sum_{k<=n} q_k``.  Since the ring basis is
restricted to total charge zero, ``E_11 = W``: link 11 is the reference link,
and only the hop across link 11 shifts ``W``.  Thus the diagonal electric-field
partial sums are the register chain and the constraint is its copying
mechanism.

For each pointer cell, the six fragments are a fixed tiling of the ring into
disjoint contiguous two-link intervals.  Register cells are ordered by ring
distance from ``B`` with clockwise ties first, offsets
``(0,+1,-1,+2,-2,+3)``; register cell ``C`` contributes
``(E_(2C+1), E_(2C+2 mod 12))``.  For ``B=0`` this is
``[(E1,E2),(E3,E4),(E11,E0),(E5,E6),(E9,E10),(E7,E8)]``.  The wrap fragment
therefore exposes the engine's reference-link convention rather than hiding
it.

``Q_B`` and every fragment field are diagonal in the engine's constrained
occupation/rotor basis.  The certification content is consequently the
CLASSICAL Shannon mutual information of their joint outcome distribution,
obtained directly by marginalizing ``|psi(fock,W)|^2``.  No reduced density
matrix or Holevo reconstruction is used in v2.

A fragment certifies at level ``delta`` only if it both contains at least
``(1-delta) H(Q_B)`` and exceeds its same-coupling GS mutual information by
``eps_exc=0.02`` bits.  Cells with ``H(Q_B)<0.05`` are skipped.  Registration
is the first sampled time at which two disjoint fragments certify.  The
effective ``theta*`` attached to an onset is the kappa runner's exact
GS-baseline-subtracted ``1-Tr(rho_cell^2)`` proxy on bond ``(2B,2B+1)``.

The runner reads conventions only from:

* ``gauged_schwinger_staggered_ed_engine_2026_07_08.py``;
* ``deposition_per_activity_kappa_2026_07_08.py``;
* ``frontier_record_formation_dynamics_constraint_2026_06_05.py``;
* ``activity_energy_bound_witnesses_2026_07_08.py``.

It is a bounded comparator measurement: no formation rule is chosen and no
audit status or gravity claim is set.
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
N_FRAGMENTS = N_CELLS
MASS = 0.3
COUPLINGS = (0.6, 1.0)
W_MAX = 4
T_FINAL = 10.0
DT = 0.1
N_TIMES = 101
TIMES = np.linspace(0.0, T_FINAL, N_TIMES)
DELTAS = (0.05, 0.1, 0.2)
HEADLINE_DELTA = 0.1
EPS_EXCESS = 0.02
H_FLOOR = 0.05
MIN_REDUNDANCY = 2
LOCALITY_TIME = 1.0
LOCALITY_RADIUS_CELLS = 3
SPARSE_WINDOW_FLOOR = 0.2
DELTA_FACTOR_LIMIT = 1.5
NUMERIC_TOL = 1.0e-10


@dataclass(frozen=True)
class ClassicalFragmentLayout:
    """Sparse marginalization map for one ``(Q_B, two-link F)`` pair."""

    links: tuple[int, int]
    n_fragment_outcomes: int
    joint_indicator: sp.csr_matrix


@dataclass(frozen=True)
class RegistrationEvent:
    delta: float
    cell: int
    time_index: int
    time: float
    theta_star: float


@dataclass
class ClassicalDiagnostics:
    joint_normalization_error: float = 0.0
    pointer_marginal_error: float = 0.0
    lower_bound_error: float = 0.0
    upper_bound_error: float = 0.0

    def absorb(self, other: "ClassicalDiagnostics") -> None:
        self.joint_normalization_error = max(
            self.joint_normalization_error,
            other.joint_normalization_error,
        )
        self.pointer_marginal_error = max(
            self.pointer_marginal_error,
            other.pointer_marginal_error,
        )
        self.lower_bound_error = max(
            self.lower_bound_error,
            other.lower_bound_error,
        )
        self.upper_bound_error = max(
            self.upper_bound_error,
            other.upper_bound_error,
        )


@dataclass
class CaseResult:
    coupling: float
    preparation: str
    centers: tuple[int, ...]
    events: dict[float, list[RegistrationEvent]]
    observable_error: float
    proxy_ok: bool
    excess_minimum: float
    excess_maximum: float
    maximum_content_ratio: float
    maximum_redundancy: dict[float, int]


@dataclass(frozen=True)
class DemolitionPanel:
    coupling: float
    occupation_minimum: float
    occupation_median: float
    occupation_maximum: float
    cell_charge_minimum: float
    cell_charge_median: float
    cell_charge_maximum: float
    gate: bool


def load_sources() -> tuple[Any, Any, Any, Any]:
    """Load only the four authorized modules and validate the used APIs."""

    old_dont_write_bytecode = sys.dont_write_bytecode
    sys.dont_write_bytecode = True
    try:
        engine = importlib.import_module(
            "gauged_schwinger_staggered_ed_engine_2026_07_08"
        )
        kappa = importlib.import_module("deposition_per_activity_kappa_2026_07_08")
        darwinism = importlib.import_module(
            "frontier_record_formation_dynamics_constraint_2026_06_05"
        )
        kappa_engine, witnesses = kappa.load_authorized_sources()
    finally:
        sys.dont_write_bytecode = old_dont_write_bytecode

    if kappa_engine is not engine:
        raise RuntimeError("kappa runner loaded a different gauged-engine module")
    required = {
        "engine": (
            engine,
            (
                "Basis",
                "apply_cdag_c",
                "build_many_body_hamiltonian",
                "charges",
            ),
        ),
        "kappa": (
            kappa,
            (
                "batched_bond_observables",
                "deterministic_ground_state",
                "ground_distinguishability",
                "imported_observable_error",
                "vectorize_trace_groups",
            ),
        ),
        "darwinism": (darwinism, ("shannon_bits",)),
        "witnesses": (
            witnesses,
            (
                "build_bond_trace_groups",
                "gauged_hopping_terms",
                "gauged_local_arrays",
                "normalize",
            ),
        ),
    }
    missing = [
        f"{label}.{name}"
        for label, (module, names) in required.items()
        for name in names
        if not hasattr(module, name)
    ]
    if missing:
        raise RuntimeError("missing authorized API: " + ",".join(missing))
    pinned = (
        kappa.N_SITES == N_SITES
        and kappa.MASS == MASS
        and tuple(kappa.COUPLINGS) == COUPLINGS
        and kappa.W_MAX == W_MAX
        and kappa.T_FINAL == T_FINAL
        and kappa.DT == DT
        and kappa.N_TIMES == N_TIMES
        and np.array_equal(kappa.TIMES, TIMES)
    )
    if not pinned:
        raise RuntimeError("authorized kappa conventions differ from pinned setup")
    return engine, kappa, darwinism, witnesses


def ordered_register_cells(pointer_cell: int) -> tuple[int, ...]:
    """Ring-distance order with clockwise member first at every tie."""

    if not 0 <= pointer_cell < N_CELLS:
        raise ValueError("invalid pointer cell")
    offsets = (0, 1, -1, 2, -2, N_CELLS // 2)
    cells = tuple((pointer_cell + offset) % N_CELLS for offset in offsets)
    if len(set(cells)) != N_CELLS:
        raise RuntimeError("register-cell ordering is not a permutation")
    return cells


def fragment_tiling(pointer_cell: int) -> tuple[tuple[int, int], ...]:
    """Return the declared six disjoint two-link intervals for ``B``."""

    fragments = tuple(
        ((2 * cell + 1) % N_SITES, (2 * cell + 2) % N_SITES)
        for cell in ordered_register_cells(pointer_cell)
    )
    flattened = [link for fragment in fragments for link in fragment]
    if sorted(flattened) != list(range(N_SITES)):
        raise RuntimeError("fragment tiling does not cover every link exactly once")
    return fragments


def build_diagonal_observables(
    engine: Any,
    basis: Any,
    occupations: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, float]:
    """Build ``Q_B`` and the engine's exact link partial sums on the basis."""

    cell_charges = (
        occupations[0::2] + occupations[1::2] - 1.0
    ).astype(np.int8)
    if not np.all(np.isin(cell_charges, (-1, 0, 1))):
        raise RuntimeError("cell charge is not three-outcome")

    fields = np.empty((N_SITES, basis.dim), dtype=np.int16)
    reference_error = 0.0
    for index in range(basis.dim):
        _, fock_value, w_index = basis.unpack(index)
        q = np.asarray(engine.charges(N_SITES, int(fock_value)), dtype=np.int64)
        w_value = int(basis.w_value(w_index))
        link_fields = w_value + np.cumsum(q)
        fields[:, index] = link_fields
        reference_error = max(
            reference_error,
            abs(float(link_fields[-1] - w_value)),
            abs(float(np.sum(q))),
        )
    return cell_charges, fields, reference_error


def build_classical_layouts(
    basis: Any,
    cell_charges: np.ndarray,
    fields: np.ndarray,
) -> list[list[ClassicalFragmentLayout]]:
    """Precompute sparse maps from basis probabilities to joint outcomes."""

    layouts: list[list[ClassicalFragmentLayout]] = []
    basis_indices = np.arange(basis.dim, dtype=np.int64)
    for cell in range(N_CELLS):
        pointer_outcome = np.asarray(cell_charges[cell] + 1, dtype=np.int64)
        cell_layouts: list[ClassicalFragmentLayout] = []
        for links in fragment_tiling(cell):
            field_pairs = fields[np.asarray(links, dtype=np.int64)].T
            _, fragment_outcome = np.unique(
                field_pairs,
                axis=0,
                return_inverse=True,
            )
            n_fragment_outcomes = int(np.max(fragment_outcome)) + 1
            joint_outcome = pointer_outcome * n_fragment_outcomes + fragment_outcome
            indicator = sp.csr_matrix(
                (
                    np.ones(basis.dim, dtype=np.float64),
                    (basis_indices, joint_outcome),
                ),
                shape=(basis.dim, 3 * n_fragment_outcomes),
            )
            cell_layouts.append(
                ClassicalFragmentLayout(
                    links=links,
                    n_fragment_outcomes=n_fragment_outcomes,
                    joint_indicator=indicator,
                )
            )
        layouts.append(cell_layouts)
    return layouts


def classical_joint_information(
    probabilities: np.ndarray,
    layout: ClassicalFragmentLayout,
    darwinism: Any,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, ClassicalDiagnostics]:
    """Return ``H(Q)``, ``I(Q:F)``, and ``p(Q)`` from a diagonal joint law."""

    joint_flat = np.asarray(layout.joint_indicator.T @ probabilities.T).T
    joint = joint_flat.reshape(
        probabilities.shape[0],
        3,
        layout.n_fragment_outcomes,
    )
    pointer = np.sum(joint, axis=2)
    fragment = np.sum(joint, axis=1)
    entropy = np.asarray(
        [darwinism.shannon_bits(row) for row in pointer],
        dtype=np.float64,
    )

    denominator = pointer[:, :, None] * fragment[:, None, :]
    positive = joint > 0.0
    information_terms = np.zeros_like(joint)
    information_terms[positive] = joint[positive] * np.log2(
        joint[positive] / denominator[positive]
    )
    information = np.sum(information_terms, axis=(1, 2))
    diagnostics = ClassicalDiagnostics(
        joint_normalization_error=float(
            np.max(np.abs(np.sum(joint, axis=(1, 2)) - 1.0))
        ),
        lower_bound_error=float(max(0.0, -float(np.min(information)))),
        upper_bound_error=float(
            max(0.0, float(np.max(information - entropy)))
        ),
    )
    return entropy, information, pointer, diagnostics


def record_content(
    states: np.ndarray,
    layouts: list[list[ClassicalFragmentLayout]],
    darwinism: Any,
) -> tuple[np.ndarray, np.ndarray, ClassicalDiagnostics, float]:
    """Measure all ``H(Q_B)`` and classical ``I(Q_B:F_j)`` time series."""

    vectors = np.asarray(states, dtype=np.complex128)
    if vectors.ndim != 2:
        raise ValueError("states must be a [sample,basis] matrix")
    probabilities = np.abs(vectors) ** 2
    norms = np.sum(probabilities, axis=1)
    if np.any(norms <= 0.0):
        raise RuntimeError("nonpositive state norm")
    norm_error = float(np.max(np.abs(norms - 1.0)))
    probabilities = probabilities / norms[:, None]

    entropy = np.empty((vectors.shape[0], N_CELLS), dtype=np.float64)
    information = np.empty(
        (vectors.shape[0], N_CELLS, N_FRAGMENTS),
        dtype=np.float64,
    )
    diagnostics = ClassicalDiagnostics()
    for cell in range(N_CELLS):
        reference_pointer: np.ndarray | None = None
        for fragment_index, layout in enumerate(layouts[cell]):
            local_entropy, local_information, pointer, local_diagnostics = (
                classical_joint_information(probabilities, layout, darwinism)
            )
            diagnostics.absorb(local_diagnostics)
            information[:, cell, fragment_index] = local_information
            if reference_pointer is None:
                reference_pointer = pointer
                entropy[:, cell] = local_entropy
            else:
                diagnostics.pointer_marginal_error = max(
                    diagnostics.pointer_marginal_error,
                    float(np.max(np.abs(pointer - reference_pointer))),
                    float(np.max(np.abs(local_entropy - entropy[:, cell]))),
                )
    return entropy, information, diagnostics, norm_error


def build_covariant_hop(engine: Any, basis: Any, link: int) -> sp.csr_matrix:
    """Build the engine's directional ``c_link^dag U_link c_right`` map.

    This mirrors ``build_many_body_hamiltonian`` exactly: the forward hop on
    the reference/boundary link raises ``W`` by one; every other link leaves
    it unchanged.  The requested preparation uses link 0, but retaining the
    boundary rule makes the convention explicit and testable.
    """

    if not 0 <= link < N_SITES:
        raise ValueError("invalid link")
    right = (link + 1) % N_SITES
    delta_w = 1 if (basis.rotor and link == N_SITES - 1) else 0
    rows: list[int] = []
    cols: list[int] = []
    data: list[complex] = []
    for local_f, fock_value in enumerate(basis.focks):
        applied = engine.apply_cdag_c(int(fock_value), link, right)
        if applied is None:
            continue
        new_fock, fermion_sign = applied
        new_local = basis.fock_to_local.get(new_fock)
        if new_local is None:
            continue
        for w_index in range(basis.n_w):
            new_w_index = basis.w_index_from_value(
                basis.w_value(w_index) + delta_w
            )
            if new_w_index is None:
                continue
            rows.append(basis.index(new_local, new_w_index))
            cols.append(basis.index(local_f, w_index))
            data.append(complex(fermion_sign))
    return sp.coo_matrix(
        (data, (rows, cols)),
        shape=(basis.dim, basis.dim),
        dtype=np.complex128,
    ).tocsr()


def sparse_frobenius(matrix: sp.spmatrix) -> float:
    values = np.asarray(matrix.data)
    return float(np.sqrt(np.sum(np.abs(values) ** 2)))


def normalized_diagonal_commutator(
    hamiltonian: sp.csr_matrix,
    diagonal: np.ndarray,
) -> float:
    """Centered dimensionless Frobenius size of ``[H,O]``.

    ``C_F(H,O)=||[H,O]||_F/(||H||_F ||O-Tr(O)I/d||_F)``.  Centering removes
    an identity offset, which never affects a commutator, before comparing the
    differently offset observables ``n_x`` and ``Q_B``.
    """

    centered = np.asarray(diagonal, dtype=np.float64) - float(np.mean(diagonal))
    observable_norm = float(np.linalg.norm(centered))
    hamiltonian_norm = sparse_frobenius(hamiltonian)
    if observable_norm == 0.0 or hamiltonian_norm == 0.0:
        raise RuntimeError("zero Frobenius normalization")
    coo = hamiltonian.tocoo()
    commutator_data = coo.data * (centered[coo.col] - centered[coo.row])
    commutator_norm = float(np.sqrt(np.sum(np.abs(commutator_data) ** 2)))
    return commutator_norm / (hamiltonian_norm * observable_norm)


def demolition_panel(
    hamiltonian: sp.csr_matrix,
    occupations: np.ndarray,
    cell_charges: np.ndarray,
    coupling: float,
) -> DemolitionPanel:
    occupation_sizes = np.asarray(
        [
            normalized_diagonal_commutator(hamiltonian, occupations[site])
            for site in range(N_SITES)
        ],
        dtype=np.float64,
    )
    cell_sizes = np.asarray(
        [
            normalized_diagonal_commutator(hamiltonian, cell_charges[cell])
            for cell in range(N_CELLS)
        ],
        dtype=np.float64,
    )
    return DemolitionPanel(
        coupling=coupling,
        occupation_minimum=float(np.min(occupation_sizes)),
        occupation_median=float(np.median(occupation_sizes)),
        occupation_maximum=float(np.max(occupation_sizes)),
        cell_charge_minimum=float(np.min(cell_sizes)),
        cell_charge_median=float(np.median(cell_sizes)),
        cell_charge_maximum=float(np.max(cell_sizes)),
        gate=bool(np.max(cell_sizes) < np.min(occupation_sizes)),
    )


def registration_events(
    entropy: np.ndarray,
    information: np.ndarray,
    ground_information: np.ndarray,
    excess_distinguishability: np.ndarray,
    delta: float,
) -> list[RegistrationEvent]:
    """Return each cell's first sampled excess-gated redundancy onset."""

    events: list[RegistrationEvent] = []
    excess_information = information - ground_information[None, :, :]
    for cell in range(N_CELLS):
        nontrivial = entropy[:, cell] >= H_FLOOR
        content_gate = (
            information[:, cell, :] + NUMERIC_TOL
            >= (1.0 - delta) * entropy[:, cell, None]
        )
        excess_gate = (
            excess_information[:, cell, :] + NUMERIC_TOL >= EPS_EXCESS
        )
        redundancy = np.count_nonzero(
            nontrivial[:, None] & content_gate & excess_gate,
            axis=1,
        )
        onset_indices = np.flatnonzero(redundancy >= MIN_REDUNDANCY)
        if onset_indices.size == 0:
            continue
        time_index = int(onset_indices[0])
        events.append(
            RegistrationEvent(
                delta=delta,
                cell=cell,
                time_index=time_index,
                time=float(TIMES[time_index]),
                theta_star=float(
                    excess_distinguishability[time_index, 2 * cell]
                ),
            )
        )
    return sorted(events, key=lambda event: (event.time, event.cell))


def measure_case(
    *,
    coupling: float,
    preparation: str,
    centers: tuple[int, ...],
    states: np.ndarray,
    entropy: np.ndarray,
    information: np.ndarray,
    ground_information: np.ndarray,
    hamiltonian: sp.csr_matrix,
    trace_groups: list[Any],
    bond_layouts: list[Any],
    ground_distinguishability: np.ndarray,
    kappa: Any,
    witnesses: Any,
) -> CaseResult:
    """Attach v2 onsets to the imported kappa proxy on bond ``2B``."""

    activity, raw_distinguishability, internal_error, proxy_ok = (
        kappa.batched_bond_observables(states, hamiltonian, bond_layouts)
    )
    direct_error = kappa.imported_observable_error(
        states[0],
        hamiltonian,
        trace_groups,
        activity[0],
        raw_distinguishability[0],
        witnesses,
    )
    excess = raw_distinguishability - np.asarray(
        ground_distinguishability,
        dtype=np.float64,
    )[None, :]
    finite = bool(np.all(np.isfinite(excess)))
    events = {
        delta: registration_events(
            entropy,
            information,
            ground_information,
            excess,
            delta,
        )
        for delta in DELTAS
    }
    ratios = np.divide(
        information,
        entropy[:, :, None],
        out=np.zeros_like(information),
        where=entropy[:, :, None] > 0.0,
    )
    eligible_ratios = ratios[entropy >= H_FLOOR]
    maximum_content_ratio = (
        float(np.max(eligible_ratios)) if eligible_ratios.size else float("nan")
    )
    excess_information = information - ground_information[None, :, :]
    maximum_redundancy: dict[float, int] = {}
    for delta in DELTAS:
        certifies = (
            (entropy[:, :, None] >= H_FLOOR)
            & (ratios + NUMERIC_TOL >= 1.0 - delta)
            & (excess_information + NUMERIC_TOL >= EPS_EXCESS)
        )
        maximum_redundancy[delta] = int(
            np.max(np.count_nonzero(certifies, axis=2))
        )
    return CaseResult(
        coupling=coupling,
        preparation=preparation,
        centers=centers,
        events=events,
        observable_error=max(float(internal_error), float(direct_error)),
        proxy_ok=bool(proxy_ok and finite),
        excess_minimum=float(np.min(excess)),
        excess_maximum=float(np.max(excess)),
        maximum_content_ratio=maximum_content_ratio,
        maximum_redundancy=maximum_redundancy,
    )


def fmt_number(value: float) -> str:
    if not np.isfinite(value):
        return "nan"
    return f"{value:.6g}"


def fmt_vector(values: Any) -> str:
    array = np.asarray(values).ravel()
    return "[" + ",".join(fmt_number(float(value)) for value in array) + "]"


def case_label(result: CaseResult) -> str:
    return f"g={result.coupling:g}/{result.preparation}"


def theta_values(result: CaseResult, delta: float) -> np.ndarray:
    return np.asarray(
        [event.theta_star for event in result.events[delta]],
        dtype=np.float64,
    )


def theta_summary(values: np.ndarray) -> tuple[float, float, float]:
    if values.size == 0 or not np.all(np.isfinite(values)):
        return float("nan"), float("nan"), float("nan")
    return float(np.median(values)), float(np.min(values)), float(np.max(values))


def delta_medians(results: list[CaseResult]) -> tuple[dict[float, float], float]:
    medians: dict[float, float] = {}
    for delta in DELTAS:
        arrays = [
            values
            for result in results
            if (values := theta_values(result, delta)).size > 0
        ]
        joined = np.concatenate(arrays) if arrays else np.array([], dtype=np.float64)
        medians[delta] = theta_summary(joined)[0]
    values = np.asarray([medians[delta] for delta in DELTAS], dtype=np.float64)
    if not np.all(np.isfinite(values)) or np.any(values <= 0.0):
        factor = float("inf")
    else:
        factor = float(np.max(values) / np.min(values))
    return medians, factor


def circular_cell_distance(cell: int, center: int) -> int:
    direct = abs(cell - center)
    return min(direct, N_CELLS - direct)


def hop_kick_locality(results: list[CaseResult]) -> tuple[bool, int, int]:
    distances: list[int] = []
    for result in results:
        if result.preparation != "c":
            continue
        for event in result.events[HEADLINE_DELTA]:
            if event.time <= LOCALITY_TIME + 10.0 * np.finfo(float).eps:
                distances.append(
                    min(
                        circular_cell_distance(event.cell, center)
                        for center in result.centers
                    )
                )
    maximum = max(distances, default=0)
    return maximum <= LOCALITY_RADIUS_CELLS, len(distances), maximum


def format_event(event: RegistrationEvent) -> str:
    return f"B{event.cell}@{event.time:g}/{fmt_number(event.theta_star)}"


def build_output(
    *,
    results: list[CaseResult],
    panels: list[DemolitionPanel],
    control_counts: dict[float, int],
    diagnostics: ClassicalDiagnostics,
    maximum_ground_residual: float,
    maximum_norm_error: float,
    maximum_phase_probability_error: float,
    reference_error: float,
    hop_operator_error: float,
    elapsed: float,
) -> tuple[list[str], int]:
    delta_median, sensitivity_factor = delta_medians(results)
    locality_ok, early_count, early_maximum = hop_kick_locality(results)
    hop_results = [result for result in results if result.preparation == "c"]
    hop_event_each_coupling = bool(
        len(hop_results) == len(COUPLINGS)
        and all(result.events[HEADLINE_DELTA] for result in hop_results)
    )

    check_01 = all(control_counts[delta] == 0 for delta in DELTAS)
    check_02 = all(panel.gate for panel in panels)
    check_03 = hop_event_each_coupling and locality_ok
    check_04 = bool(
        np.isfinite(sensitivity_factor)
        and sensitivity_factor < DELTA_FACTOR_LIMIT
    )

    case_bars: list[tuple[CaseResult, float, float, float, str]] = []
    eventful_window_flags: list[bool] = []
    for result in results:
        values = theta_values(result, HEADLINE_DELTA)
        median, minimum, maximum = theta_summary(values)
        if values.size == 0:
            status = "no-event"
        elif median >= SPARSE_WINDOW_FLOOR:
            status = "inside"
            eventful_window_flags.append(True)
        else:
            status = "BAR-BELOW-WINDOW"
            eventful_window_flags.append(False)
        case_bars.append((result, median, minimum, maximum, status))
    check_05 = bool(eventful_window_flags and all(eventful_window_flags))
    below_window = bool(eventful_window_flags and not all(eventful_window_flags))

    observable_error = max(result.observable_error for result in results)
    proxy_ok = all(result.proxy_ok for result in results)
    numerical_machinery = bool(
        maximum_ground_residual <= 1.0e-8
        and maximum_norm_error <= 1.0e-9
        and maximum_phase_probability_error <= 1.0e-14
        and reference_error == 0.0
        and hop_operator_error <= 1.0e-12
        and observable_error <= NUMERIC_TOL
        and proxy_ok
        and diagnostics.joint_normalization_error <= 1.0e-9
        and diagnostics.pointer_marginal_error <= 1.0e-9
        and diagnostics.lower_bound_error <= 1.0e-9
        and diagnostics.upper_bound_error <= 1.0e-9
        and elapsed < 900.0
    )
    machinery_ok = numerical_machinery and check_01 and check_02 and check_03

    setup = (
        "SETUP N=12 cells=6 m=0.3 g=[0.6,1] Qtotal=0 Wmax=4 t=0:0.1:10; "
        "pointer=Q_B=q_2B+q_(2B+1) outcomes=[-1,0,1]; "
        "register=E_n=W+sum_(k<=n)q_k,E11=W; "
        "F(B0)=[E1E2,E3E4,E11E0,E5E6,E9E10,E7E8] order=[0,+1,-1,+2,-2,+3]; "
        "kick=a:exp(+i0.7n0),b:exp(+i0.5(n0+n6)),c:exp(+i0.5(h01+h01dag)); "
        "cert=I>=(1-delta)H AND I-I_GS>=0.02,Hfloor=0.05,Rdelta>=2,delta=[0.05,0.1,0.2]"
    )

    event_parts: list[str] = []
    for result in results:
        counts = [len(result.events[delta]) for delta in DELTAS]
        headline = ",".join(
            format_event(event) for event in result.events[HEADLINE_DELTA]
        )
        event_parts.append(
            f"{case_label(result)} N={counts} d0.1=[{headline or 'none'}]"
        )
    events_line = (
        "EVENTS N-order=d[0.05,0.1,0.2],entry=B@sampled-t/theta*_cell; "
        + "; ".join(event_parts)
    )

    panel_parts = [
        (
            f"g={panel.coupling:g} n med={fmt_number(panel.occupation_median)}"
            f"[{fmt_number(panel.occupation_minimum)},{fmt_number(panel.occupation_maximum)}] "
            f"Q med={fmt_number(panel.cell_charge_median)}"
            f"[{fmt_number(panel.cell_charge_minimum)},{fmt_number(panel.cell_charge_maximum)}]"
        )
        for panel in panels
    ]
    demolition_line = (
        "DEMOLITION C_F=||[H,O]||F/(||H||F*||O-Tr(O)I/d||F); "
        + "; ".join(panel_parts)
        + f"; CHECK-02={'ok' if check_02 else 'FAIL'}(max-Q<min-n)"
    )

    global_bars = " ".join(
        f"d={delta:g}:{fmt_number(delta_median[delta])}" for delta in DELTAS
    )
    case_bar_parts = [
        (
            f"{case_label(result)} med={fmt_number(median)} "
            f"range=[{fmt_number(minimum)},{fmt_number(maximum)}] {status}"
        )
        for result, median, minimum, maximum, status in case_bars
    ]
    bar_line = (
        f"BAR global-medians {global_bars} delta-factor={fmt_number(sensitivity_factor)}(<1.5); "
        + "; ".join(case_bar_parts)
    )

    control_vector = [control_counts[delta] for delta in DELTAS]
    hop_probe = ",".join(
        f"g={result.coupling:g}:maxI/H={fmt_number(result.maximum_content_ratio)}"
        f"/maxR(d0.2)={result.maximum_redundancy[0.2]}"
        for result in hop_results
    )
    check_05_label = "ok" if check_05 else (
        "BAR-BELOW-WINDOW" if below_window else "no-event"
    )
    checks_line = (
        f"CHECKS CHECK-01={'ok' if check_01 else 'FAIL'}"
        f"(GS-events={control_vector},excess-subtraction=exact); "
        f"CHECK-02={'ok' if check_02 else 'FAIL'}; "
        f"CHECK-03={'ok' if check_03 else 'FAIL'}"
        f"(hop-headline-each-g={hop_event_each_coupling},early={early_count},"
        f"max-cell-dist={early_maximum},probe=[{hop_probe}]); "
        f"CHECK-04={'ok' if check_04 else 'FAIL'}(factor={fmt_number(sensitivity_factor)}); "
        f"CHECK-05={check_05_label}; MACHINERY={'ok' if numerical_machinery else 'FAIL'}"
        f"(GSres={maximum_ground_residual:.2e},norm={maximum_norm_error:.2e},"
        f"phase-p={maximum_phase_probability_error:.2e},Eref={reference_error:.1e},"
        f"hop={hop_operator_error:.2e},proxy={observable_error:.2e},"
        f"joint={diagnostics.joint_normalization_error:.2e},"
        f"marg={diagnostics.pointer_marginal_error:.2e},"
        f"MIbounds=[{diagnostics.lower_bound_error:.2e},{diagnostics.upper_bound_error:.2e}])"
    )

    headline_global = delta_median[HEADLINE_DELTA]
    if not eventful_window_flags:
        window_flag = "unavailable"
    elif below_window:
        window_flag = "below"
    else:
        window_flag = "inside"
    if not machinery_ok:
        verdict = "MACHINERY-FAIL"
        exit_code = 2
    elif not check_04:
        verdict = "BAR-NOT-PINNED"
        exit_code = 1
    else:
        verdict = "BAR-DERIVED-EFFECTIVE"
        exit_code = 0
    failed = [
        name
        for name, passed in (
            ("CHECK-01", check_01),
            ("CHECK-02", check_02),
            ("CHECK-03", check_03),
            ("CHECK-04", check_04),
            ("MACHINERY", numerical_machinery),
        )
        if not passed
    ]
    finding_flags = ["BAR-BELOW-WINDOW"] if below_window else []
    total = (
        f"TOTAL {verdict} theta*={fmt_number(headline_global)} window={window_flag} "
        f"flags={','.join(finding_flags) if finding_flags else 'none'} "
        f"failed={','.join(failed) if failed else 'none'} elapsed={elapsed:.2f}s "
        "SPEC-NOTE=engine-register:E_n=W+sum(k<=n)q_k,E11=W,link11-hop-shifts-W;"
        "fragments:disjoint-two-link-ring-tiling-distance-ordered;eps_exc=0.02;"
        "classical-MI:joint-marginal-of-|psi(fock,W)|^2,no-RDM;"
        "kick-asymmetry:phase-p(t0)=GS-exact,hop-kick-writes-registers-directly;"
        "v1:n_x-no-onset,adjacent~0.2bit-static,far~1e-3bit,[H,n_x]!=0-confirms-2026-06-05-necessity;"
        "onset:sampled-first-hit;theta*:GS-subtracted-1-purity-on-cell-bond;"
        "finite-Wmax=4;no-formation-rule,no-gravity-claim,no-audit-status"
    )
    return [
        setup,
        events_line,
        demolition_line,
        bar_line,
        checks_line,
        total,
    ], exit_code


def run() -> tuple[list[str], int]:
    started = time.monotonic()
    engine, kappa, darwinism, witnesses = load_sources()
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
        kappa.vectorize_trace_groups(groups, basis.dim)
        for groups in trace_groups
    ]
    occupations, _ = witnesses.gauged_local_arrays(
        engine,
        basis,
        MASS,
        COUPLINGS[0],
    )
    cell_charges, fields, reference_error = build_diagonal_observables(
        engine,
        basis,
        occupations,
    )
    classical_layouts = build_classical_layouts(
        basis,
        cell_charges,
        fields,
    )

    hop_01 = build_covariant_hop(engine, basis, 0)
    hop_plus_hc = (hop_01 + hop_01.getH()).tocsr()
    imported_hopping = witnesses.gauged_hopping_terms(engine, basis)[0]
    expected_hopping = ((-0.5j) * (hop_01 - hop_01.getH())).tocsr()
    hop_operator_error = sparse_frobenius(imported_hopping - expected_hopping)

    results: list[CaseResult] = []
    panels: list[DemolitionPanel] = []
    control_counts = {delta: 0 for delta in DELTAS}
    diagnostics = ClassicalDiagnostics()
    maximum_ground_residual = 0.0
    maximum_norm_error = 0.0
    maximum_phase_probability_error = 0.0

    for coupling_index, coupling in enumerate(COUPLINGS):
        hamiltonian = engine.build_many_body_hamiltonian(
            basis,
            MASS,
            coupling,
            boundary_holonomy_shifts_w=True,
        ).tocsr()
        panels.append(
            demolition_panel(
                hamiltonian,
                occupations,
                cell_charges,
                coupling,
            )
        )
        _, ground_state, ground_residual = kappa.deterministic_ground_state(
            hamiltonian,
            witnesses,
            kappa.RNG_SEED + coupling_index,
        )
        maximum_ground_residual = max(maximum_ground_residual, ground_residual)
        ground_d = kappa.ground_distinguishability(
            ground_state,
            trace_groups,
            witnesses,
        )

        kicked_a = np.exp(1.0j * 0.7 * occupations[0]) * ground_state
        kicked_b = np.exp(
            1.0j * 0.5 * (occupations[0] + occupations[6])
        ) * ground_state
        kicked_c = spla.expm_multiply(
            (0.5j) * hop_plus_hc,
            ground_state,
        )
        ground_probabilities = np.abs(ground_state) ** 2
        maximum_phase_probability_error = max(
            maximum_phase_probability_error,
            float(np.max(np.abs(np.abs(kicked_a) ** 2 - ground_probabilities))),
            float(np.max(np.abs(np.abs(kicked_b) ** 2 - ground_probabilities))),
        )

        initial_states = np.column_stack((kicked_a, kicked_b, kicked_c))
        trace_generator = complex(-1.0j * np.sum(hamiltonian.diagonal()))
        evolved = spla.expm_multiply(
            (-1.0j) * hamiltonian,
            initial_states,
            start=0.0,
            stop=T_FINAL,
            num=N_TIMES,
            endpoint=True,
            traceA=trace_generator,
        )
        evolved_norms = np.sum(np.abs(evolved) ** 2, axis=1)
        maximum_norm_error = max(
            maximum_norm_error,
            float(np.max(np.abs(evolved_norms - 1.0))),
        )

        combined = np.concatenate(
            (
                ground_state[None, :],
                evolved[:, :, 0],
                evolved[:, :, 1],
                evolved[:, :, 2],
            ),
            axis=0,
        )
        entropy, information, local_diagnostics, content_norm_error = (
            record_content(combined, classical_layouts, darwinism)
        )
        diagnostics.absorb(local_diagnostics)
        maximum_norm_error = max(maximum_norm_error, content_norm_error)
        ground_information = information[0]

        zero_ground_proxy = np.zeros((1, N_SITES), dtype=np.float64)
        for delta in DELTAS:
            control_counts[delta] += len(
                registration_events(
                    entropy[0:1],
                    information[0:1],
                    ground_information,
                    zero_ground_proxy,
                    delta,
                )
            )

        slices = {
            "a": slice(1, 1 + N_TIMES),
            "b": slice(1 + N_TIMES, 1 + 2 * N_TIMES),
            "c": slice(1 + 2 * N_TIMES, 1 + 3 * N_TIMES),
        }
        centers = {"a": (0,), "b": (0, 3), "c": (0,)}
        for preparation in ("a", "b", "c"):
            sample_slice = slices[preparation]
            results.append(
                measure_case(
                    coupling=coupling,
                    preparation=preparation,
                    centers=centers[preparation],
                    states=combined[sample_slice],
                    entropy=entropy[sample_slice],
                    information=information[sample_slice],
                    ground_information=ground_information,
                    hamiltonian=hamiltonian,
                    trace_groups=trace_groups,
                    bond_layouts=bond_layouts,
                    ground_distinguishability=ground_d,
                    kappa=kappa,
                    witnesses=witnesses,
                )
            )
        del combined, evolved, entropy, information, hamiltonian

    # The excess gate subtracts each identical GS value from itself, so this is
    # an exact construction invariant rather than a floating-point tolerance.
    assert all(control_counts[delta] == 0 for delta in DELTAS), (
        "GS control acquired an impossible excess-gated event"
    )

    elapsed = time.monotonic() - started
    return build_output(
        results=results,
        panels=panels,
        control_counts=control_counts,
        diagnostics=diagnostics,
        maximum_ground_residual=maximum_ground_residual,
        maximum_norm_error=maximum_norm_error,
        maximum_phase_probability_error=maximum_phase_probability_error,
        reference_error=reference_error,
        hop_operator_error=hop_operator_error,
        elapsed=elapsed,
    )


def main() -> int:
    try:
        lines, exit_code = run()
    except Exception as exc:  # noqa: BLE001 -- preserve the stdout line budget.
        message = " ".join(str(exc).split())[:260]
        print(
            f"TOTAL MACHINERY-FAIL error={type(exc).__name__}:{message} "
            "SPEC-NOTE=engine-register-reference-link;eps_exc=0.02;"
            "classical-MI-from-basis-probabilities;phase-vs-hop-kick-asymmetry;"
            "v1-site-pointer-negative-retained;no-formation-rule,no-audit-status"
        )
        return 2
    for line in lines:
        print(line)
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
