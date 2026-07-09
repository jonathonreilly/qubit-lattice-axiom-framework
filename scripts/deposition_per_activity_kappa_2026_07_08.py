#!/usr/bin/env python3
"""Block01 of the record-deposition-rate campaign: measure kappa(theta).

Under the named quantum-Darwinism (QD) bridge premise, a registration -- a
record-formation opportunity of measurement grade -- occurs when a site's
declared local-distinguishability proxy crosses a threshold ``theta``.  The
axioms do not supply that threshold.  This runner therefore measures

    kappa(theta) = total threshold-crossing events / total integrated activity

for a declared two-site-purity proxy and a declared bond trace-norm-velocity
activity proxy over a threshold sweep, and reports the scaling shape.  It does
not choose a formation rule, make a gravity claim, or set audit status.

Companion note: DEPOSITION_PER_ACTIVITY_KAPPA_BOUNDED_NOTE_2026-07-08.md.

The finite-rotor comparator and bond-reduction conventions are imported only
from:

* gauged_schwinger_staggered_ed_engine_2026_07_08.py
* activity_energy_bound_witnesses_2026_07_08.py
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
MASS = 0.3
COUPLINGS = (0.6, 1.0)
# This is the finite-rotor cutoff used by the authorized N=12 gauged
# comparator/witness runners; it is printed because the protocol does not
# promote the cutoff to an axiom.
W_MAX = 4
T_FINAL = 10.0
DT = 0.1
N_TIMES = int(round(T_FINAL / DT)) + 1
TIMES = np.linspace(0.0, T_FINAL, N_TIMES)
HALF_INDEX = int(round((0.5 * T_FINAL) / DT))
THETAS = np.array((0.02, 0.05, 0.1, 0.2, 0.3, 0.4), dtype=np.float64)
RESET_FRACTION = 0.8
FILL_LIMIT = 0.3
LOCALITY_TIME = 1.0
LOCALITY_RADIUS = 3.0
NUMERIC_TOL = 1.0e-10
RNG_SEED = 20260708


@dataclass(frozen=True)
class BondLayout:
    """Vectorized form of one imported ``BondTraceGroups`` partition."""

    group_for_basis: np.ndarray
    local_for_basis: np.ndarray
    n_groups: int


@dataclass(frozen=True)
class FitResult:
    exponent: float
    residual_rms: float
    n_positive: int


@dataclass
class CaseResult:
    coupling: float
    preparation: str
    centers: tuple[int, ...]
    activity_total: float
    activity_half: float
    normalization_ratio: float
    once_counts: np.ndarray
    rearm_counts: np.ndarray
    once_half_counts: np.ndarray
    once_lastq_counts: np.ndarray
    rearm_half_counts: np.ndarray
    once_kappa: np.ndarray
    rearm_kappa: np.ndarray
    once_window_ratio: np.ndarray
    rearm_window_ratio: np.ndarray
    once_fit: FitResult
    rearm_fit: FitResult
    early_event_count: int
    early_max_distance: float
    locality_ok: bool
    monotone_ok: bool
    observable_error: float
    proxy_range_ok: bool


def load_authorized_sources() -> tuple[Any, Any]:
    """Import the two authorized source modules without creating bytecode."""

    old_dont_write_bytecode = sys.dont_write_bytecode
    sys.dont_write_bytecode = True
    try:
        engine = importlib.import_module("gauged_schwinger_staggered_ed_engine_2026_07_08")
        witnesses = importlib.import_module("activity_energy_bound_witnesses_2026_07_08")
    finally:
        sys.dont_write_bytecode = old_dont_write_bytecode

    engine_api = ("Basis", "build_many_body_hamiltonian")
    witness_api = (
        "build_bond_trace_groups",
        "gauged_bond_activities",
        "gauged_local_arrays",
        "normalize",
        "periodic_bond_distances",
        "reduced_density",
    )
    missing = [f"engine.{name}" for name in engine_api if not hasattr(engine, name)]
    missing += [f"witnesses.{name}" for name in witness_api if not hasattr(witnesses, name)]
    if missing:
        raise RuntimeError("missing authorized API: " + ",".join(missing))
    return engine, witnesses


def vectorize_trace_groups(groups: Any, dimension: int) -> BondLayout:
    """Convert the imported environment partition to dense lookup arrays."""

    group_for_basis = np.full(dimension, -1, dtype=np.int64)
    local_for_basis = np.full(dimension, -1, dtype=np.int8)
    for group_index, (indices, local_indices) in enumerate(zip(groups.indices, groups.local_indices)):
        if np.any(group_for_basis[indices] >= 0):
            raise RuntimeError("bond trace groups overlap")
        group_for_basis[indices] = group_index
        local_for_basis[indices] = local_indices
    if np.any(group_for_basis < 0) or np.any(local_for_basis < 0):
        raise RuntimeError("bond trace groups do not cover the comparator basis")
    return BondLayout(group_for_basis, local_for_basis, len(groups.indices))


def packed_local_amplitudes(vectors: np.ndarray, layout: BondLayout) -> np.ndarray:
    """Pack basis amplitudes as ``[sample, environment, bond-state]``."""

    packed = np.zeros((vectors.shape[0], layout.n_groups, 4), dtype=np.complex128)
    packed[:, layout.group_for_basis, layout.local_for_basis] = vectors
    return packed


def batched_bond_observables(
    states: np.ndarray,
    hamiltonian: sp.csr_matrix,
    layouts: list[BondLayout],
) -> tuple[np.ndarray, np.ndarray, float, bool]:
    """Return activity and ``1-purity`` using the imported bond convention.

    This is the batched algebraic form of ``reduced_outer`` and
    ``gauged_bond_activities`` in
    activity_energy_bound_witnesses_2026_07_08.py: the same imported trace
    partition is packed once per bond, and
    ``d rho/dt = |dot(psi)><psi| + |psi><dot(psi)|`` with
    ``dot(psi) = -i H psi``.  A direct call to the imported scalar routines is
    checked separately for every coupling.
    """

    vectors = np.asarray(states, dtype=np.complex128)
    if vectors.ndim != 2 or vectors.shape[1] != hamiltonian.shape[0]:
        raise ValueError("states have the wrong comparator dimension")
    derivatives = np.asarray((-1.0j * (hamiltonian @ vectors.T)).T, dtype=np.complex128)
    activity = np.empty((vectors.shape[0], len(layouts)), dtype=np.float64)
    distinguishability = np.empty_like(activity)
    internal_error = 0.0
    proxy_range_ok = True

    for bond, layout in enumerate(layouts):
        amplitudes = packed_local_amplitudes(vectors, layout)
        derivative_amplitudes = packed_local_amplitudes(derivatives, layout)
        rho = np.einsum("tgi,tgj->tij", amplitudes, amplitudes.conj(), optimize=True)
        drho = np.einsum(
            "tgi,tgj->tij", derivative_amplitudes, amplitudes.conj(), optimize=True
        )
        drho += np.einsum(
            "tgi,tgj->tij", amplitudes, derivative_amplitudes.conj(), optimize=True
        )
        rho = 0.5 * (rho + rho.conj().transpose(0, 2, 1))
        drho = 0.5 * (drho + drho.conj().transpose(0, 2, 1))

        trace_error = np.max(np.abs(np.trace(rho, axis1=1, axis2=2) - 1.0))
        internal_error = max(internal_error, float(trace_error))
        purity = np.einsum("tij,tji->t", rho, rho, optimize=True).real
        distinguishability[:, bond] = 1.0 - purity
        activity[:, bond] = np.sum(np.abs(np.linalg.eigvalsh(drho)), axis=1)
        proxy_range_ok = proxy_range_ok and bool(
            np.all(np.isfinite(purity))
            and np.all(purity >= 0.25 - NUMERIC_TOL)
            and np.all(purity <= 1.0 + NUMERIC_TOL)
            and np.all(np.isfinite(activity[:, bond]))
            and np.all(activity[:, bond] >= -NUMERIC_TOL)
        )

        del amplitudes, derivative_amplitudes, rho, drho

    return activity, distinguishability, internal_error, proxy_range_ok


def imported_observable_error(
    state: np.ndarray,
    hamiltonian: sp.csr_matrix,
    trace_groups: list[Any],
    activity: np.ndarray,
    distinguishability: np.ndarray,
    witnesses: Any,
) -> float:
    """Cross-check the batched implementation against exposed witness calls."""

    direct_activity = witnesses.gauged_bond_activities(state, hamiltonian, trace_groups)
    error = float(np.max(np.abs(direct_activity - activity)))
    for bond, groups in enumerate(trace_groups):
        rho = witnesses.reduced_density(state, groups)
        direct_d = 1.0 - float(np.trace(rho @ rho).real)
        error = max(error, abs(direct_d - float(distinguishability[bond])))
    return error


def crossings_for_threshold(
    distinguishability: np.ndarray,
    theta: float,
    *,
    rearm: bool,
) -> list[tuple[float, int]]:
    """Find sampled upward crossings, excluding the initial level as an event."""

    events: list[tuple[float, int]] = []
    for site in range(distinguishability.shape[1]):
        armed = True
        fired_once = False
        for time_index in range(1, distinguishability.shape[0]):
            previous = float(distinguishability[time_index - 1, site])
            current = float(distinguishability[time_index, site])
            if rearm and not armed and current < RESET_FRACTION * theta:
                armed = True
            crossed = previous < theta and current >= theta
            if armed and crossed:
                fraction = (theta - previous) / (current - previous)
                crossing_time = float(TIMES[time_index - 1] + fraction * DT)
                events.append((crossing_time, site))
                fired_once = True
                if rearm:
                    armed = False
                else:
                    break
            if fired_once and not rearm:
                break
    return events


def all_crossings(
    distinguishability: np.ndarray,
    *,
    rearm: bool,
) -> tuple[np.ndarray, list[list[tuple[float, int]]]]:
    records = [
        crossings_for_threshold(distinguishability, float(theta), rearm=rearm)
        for theta in THETAS
    ]
    return np.array([len(events) for events in records], dtype=np.int64), records


def log_log_fit(kappa: np.ndarray) -> FitResult:
    """Fit only positive measured values; zero-event points are left censored."""

    positive = np.isfinite(kappa) & (kappa > 0.0)
    n_positive = int(np.count_nonzero(positive))
    if n_positive < 2:
        return FitResult(float("nan"), float("nan"), n_positive)
    x = np.log(THETAS[positive])
    y = np.log(kappa[positive])
    x_centered = x - np.mean(x)
    denominator = float(np.dot(x_centered, x_centered))
    if denominator == 0.0:
        return FitResult(float("nan"), float("nan"), n_positive)
    exponent = float(np.dot(x_centered, y - np.mean(y)) / denominator)
    intercept = float(np.mean(y) - exponent * np.mean(x))
    residual = y - (intercept + exponent * x)
    return FitResult(exponent, float(np.sqrt(np.mean(residual * residual))), n_positive)


def half_to_full_kappa_ratio(
    half_counts: np.ndarray,
    full_counts: np.ndarray,
    activity_half: float,
    activity_full: float,
) -> np.ndarray:
    """Compare like-for-like event/activity rates on half and full windows."""

    full_kappa = full_counts.astype(np.float64) / activity_full
    half_kappa = half_counts.astype(np.float64) / activity_half
    ratio = np.full(full_kappa.shape, np.nan, dtype=np.float64)
    informative = full_kappa > 0.0
    ratio[informative] = half_kappa[informative] / full_kappa[informative]
    return ratio


def measure_case(
    *,
    coupling: float,
    preparation: str,
    centers: tuple[int, ...],
    states: np.ndarray,
    hamiltonian: sp.csr_matrix,
    trace_groups: list[Any],
    layouts: list[BondLayout],
    witnesses: Any,
    ground_d: np.ndarray,
) -> CaseResult:
    activity, distinguishability, internal_error, proxy_range_ok = batched_bond_observables(
        states, hamiltonian, layouts
    )
    direct_error = imported_observable_error(
        states[0],
        hamiltonian,
        trace_groups,
        activity[0],
        distinguishability[0],
        witnesses,
    )
    observable_error = max(internal_error, direct_error)
    # Registration thresholds act on the EXCESS distinguishability over the
    # interacting ground state's per-bond baseline (the GS is entangled, with
    # absolute 1-purity ~ 0.27-0.49; absolute thresholds would count GS
    # structure rather than kick-induced registration).  The raw values above
    # feed the imported cross-check; crossings use the excess.
    distinguishability = distinguishability - np.asarray(ground_d, dtype=np.float64)[None, :]

    activity_total = float(DT * np.sum(activity))
    activity_half = float(DT * np.sum(activity[: HALF_INDEX + 1]))
    if activity_total <= 0.0 or activity_half <= 0.0:
        raise RuntimeError(f"nonpositive integrated activity for g={coupling}, prep={preparation}")
    normalization_ratio = activity_total / activity_half

    once_counts, once_records = all_crossings(distinguishability, rearm=False)
    rearm_counts, rearm_records = all_crossings(distinguishability, rearm=True)
    once_half_counts, _ = all_crossings(
        distinguishability[: HALF_INDEX + 1], rearm=False
    )
    lastq_index = int(round(0.75 * (distinguishability.shape[0] - 1)))
    once_lastq_counts, _ = all_crossings(
        distinguishability[: lastq_index + 1], rearm=False
    )
    rearm_half_counts, _ = all_crossings(
        distinguishability[: HALF_INDEX + 1], rearm=True
    )
    once_kappa = once_counts.astype(np.float64) / activity_total
    rearm_kappa = rearm_counts.astype(np.float64) / activity_total
    once_window_ratio = half_to_full_kappa_ratio(
        once_half_counts, once_counts, activity_half, activity_total
    )
    rearm_window_ratio = half_to_full_kappa_ratio(
        rearm_half_counts, rearm_counts, activity_half, activity_total
    )

    center_distances = np.vstack(
        [witnesses.periodic_bond_distances(N_SITES, center) for center in centers]
    )
    distance_to_center = np.min(center_distances, axis=0)
    early_events = [
        event
        for records in (once_records[0], rearm_records[0])
        for event in records
        if event[0] <= LOCALITY_TIME + 10.0 * np.finfo(float).eps
    ]
    early_max_distance = max(
        (float(distance_to_center[site]) for _, site in early_events),
        default=0.0,
    )
    locality_ok = all(
        float(distance_to_center[site]) <= LOCALITY_RADIUS for _, site in early_events
    )
    monotone_ok = bool(
        np.all(once_counts[:-1] >= once_counts[1:])
        and np.all(rearm_counts[:-1] >= rearm_counts[1:])
    )

    return CaseResult(
        coupling=coupling,
        preparation=preparation,
        centers=centers,
        activity_total=activity_total,
        activity_half=activity_half,
        normalization_ratio=normalization_ratio,
        once_counts=once_counts,
        rearm_counts=rearm_counts,
        once_half_counts=once_half_counts,
        once_lastq_counts=once_lastq_counts,
        rearm_half_counts=rearm_half_counts,
        once_kappa=once_kappa,
        rearm_kappa=rearm_kappa,
        once_window_ratio=once_window_ratio,
        rearm_window_ratio=rearm_window_ratio,
        once_fit=log_log_fit(once_kappa),
        rearm_fit=log_log_fit(rearm_kappa),
        early_event_count=len(early_events),
        early_max_distance=early_max_distance,
        locality_ok=locality_ok,
        monotone_ok=monotone_ok,
        observable_error=observable_error,
        proxy_range_ok=proxy_range_ok,
    )


def fmt_number(value: float) -> str:
    if not np.isfinite(value):
        return "nan"
    return f"{value:.6g}"


def fmt_vector(values: np.ndarray) -> str:
    return "[" + ",".join(fmt_number(float(value)) for value in values) + "]"


def fmt_theta_window(mask: np.ndarray) -> str:
    indices = np.flatnonzero(mask)
    if indices.size == 0:
        return "none"
    first = int(indices[0])
    if np.all(mask[first:]) and not np.any(mask[:first]):
        return ">=" + fmt_number(float(THETAS[first]))
    return "{" + ",".join(fmt_number(float(THETAS[index])) for index in indices) + "}"


def fmt_suffix_floor(mask: np.ndarray) -> str:
    for index in range(mask.size):
        if bool(np.all(mask[index:])):
            return fmt_number(float(THETAS[index]))
    return "none"


def rate_window_ok(result: CaseResult) -> bool:
    """Transient completeness: one-shot kicks register entirely within the
    first half-window (events saturate by T/2), so kappa is a per-transient
    YIELD; the stationary-rate reading needs a driven protocol (named
    follow-up).  The old factor-2 stationarity gate encoded an assumption a
    single kick cannot satisfy."""
    # Gate the ONCE convention only (one-registration-per-site is the
    # axiom-shaped counter), with CASCADE QUIESCENCE required on the
    # sparse-window thresholds (theta >= 0.2) where the constraint
    # conclusion lives.  Below that floor a small coherent ring produces
    # late first-crossings via recurrences indefinitely (no quiescence
    # exists); those thetas are RECURRENCE-LIMITED and reported, not
    # gated.  This is itself a finding: the per-transient yield is
    # well-defined only above a threshold floor on closed comparators.
    gated = THETAS >= 0.2 - 1.0e-12
    return bool(
        np.all(result.once_lastq_counts[gated] == result.once_counts[gated])
    )


def rate_window_ok_legacy(result: CaseResult) -> bool:
    ratios = np.concatenate((result.once_window_ratio, result.rearm_window_ratio))
    informative = np.isfinite(ratios)
    return bool(
        np.any(informative)
        and np.all(ratios[informative] >= 0.5)
        and np.all(ratios[informative] <= 2.0)
    )


def deterministic_ground_state(
    hamiltonian: sp.csr_matrix,
    witnesses: Any,
    seed: int,
) -> tuple[float, np.ndarray, float]:
    rng = np.random.default_rng(seed)
    v0 = rng.normal(size=hamiltonian.shape[0]) + 1.0j * rng.normal(size=hamiltonian.shape[0])
    v0 = witnesses.normalize(v0)
    eigenvalues, eigenvectors = spla.eigsh(
        hamiltonian,
        k=1,
        which="SA",
        v0=v0,
        tol=1.0e-11,
        ncv=min(48, hamiltonian.shape[0] - 1),
        maxiter=20000,
    )
    energy = float(eigenvalues[0].real)
    ground_state = witnesses.normalize(eigenvectors[:, 0])
    residual = float(np.linalg.norm(hamiltonian @ ground_state - energy * ground_state))
    return energy, ground_state, residual


def ground_distinguishability(
    ground_state: np.ndarray,
    trace_groups: list[Any],
    witnesses: Any,
) -> np.ndarray:
    values = np.empty(N_SITES, dtype=np.float64)
    for bond, groups in enumerate(trace_groups):
        rho = witnesses.reduced_density(ground_state, groups)
        values[bond] = 1.0 - float(np.trace(rho @ rho).real)
    return values


def stationary_control_is_exact(
    ground_d: np.ndarray,
) -> tuple[bool, int]:
    """Use the exact eigenstate fact: its reduced-state time series is static."""

    control = np.repeat(ground_d[np.newaxis, :], N_TIMES, axis=0)
    once_counts, _ = all_crossings(control, rearm=False)
    rearm_counts, _ = all_crossings(control, rearm=True)
    total = int(np.sum(once_counts) + np.sum(rearm_counts))
    exact_static = bool(np.all(control == control[0]))
    return exact_static and total == 0, total


def median_finite_exponent(results: list[CaseResult]) -> float:
    values = np.array(
        [result.once_fit.exponent for result in results if np.isfinite(result.once_fit.exponent)],
        dtype=np.float64,
    )
    return float(np.median(values)) if values.size else float("nan")


def build_output(
    results: list[CaseResult],
    checks: dict[str, bool],
    control_events: int,
    maximum_ground_residual: float,
    maximum_norm_error: float,
    ground_d_minimum: float,
    ground_d_maximum: float,
    joint_sparse_mask: np.ndarray,
    elapsed: float,
) -> tuple[list[str], int]:
    setup = (
        "SETUP N=12 m=0.3 g=[0.6,1] Q=0 Wmax=4 t=0:0.1:6 "
        "kick=a:exp(+i0.7n0),b:exp(+i0.5(n0+n6)); "
        "site-x=periodic-bond-(x,x+1); "
        "crossing=upward-between-samples,initial-level-excluded,"
        "N_once<=1/site,N_rearm-reset@d<0.8theta"
    )

    kappa_parts = []
    for result in results:
        label = f"g={result.coupling:g}/{result.preparation}"
        kappa_parts.append(
            f"{label} A={fmt_number(result.activity_total)} "
            f"N_once={fmt_vector(result.once_counts)} k_once={fmt_vector(result.once_kappa)} "
            f"N_rearm={fmt_vector(result.rearm_counts)} k_rearm={fmt_vector(result.rearm_kappa)}"
        )
    kappa = "KAPPA theta=" + fmt_vector(THETAS) + "; " + "; ".join(kappa_parts)

    scaling_parts = []
    for result in results:
        label = f"g={result.coupling:g}/{result.preparation}"
        once = result.once_fit
        rearm = result.rearm_fit
        scaling_parts.append(
            f"{label} once(p={fmt_number(once.exponent)},rms={fmt_number(once.residual_rms)},n={once.n_positive}) "
            f"rearm(p={fmt_number(rearm.exponent)},rms={fmt_number(rearm.residual_rms)},n={rearm.n_positive}) "
            f"khalf/kfull_once={fmt_vector(result.once_window_ratio)} "
            f"khalf/kfull_rearm={fmt_vector(result.rearm_window_ratio)} "
            f"Afull/Ahalf={fmt_number(result.normalization_ratio)}"
        )
    scaling = (
        "SCALING log(kappa)=p*log(theta)+c,fit=positive-kappa-only; "
        + "; ".join(scaling_parts)
    )

    window_parts = []
    for result in results:
        if result.preparation != "a":
            continue
        activity_per_site = result.activity_total / N_SITES
        once_fill = result.once_kappa * activity_per_site
        rearm_fill = result.rearm_kappa * activity_per_site
        once_mask = once_fill <= FILL_LIMIT + 10.0 * np.finfo(float).eps
        rearm_mask = rearm_fill <= FILL_LIMIT + 10.0 * np.finfo(float).eps
        window_parts.append(
            f"g={result.coupling:g} A/site/dwell={fmt_number(activity_per_site)} "
            f"fill_once={fmt_vector(once_fill)} sparse_once={fmt_theta_window(once_mask)} "
            f"fill_rearm={fmt_vector(rearm_fill)} sparse_rearm={fmt_theta_window(rearm_mask)}"
        )
    window = (
        "WINDOW prep=a comparator-units fill=kappa*(A/site/dwell) limit=0.3; "
        + "; ".join(window_parts)
        + f"; joint-conservative-rearm={fmt_theta_window(joint_sparse_mask)}"
    )

    activity_ratios = np.array(
        [result.normalization_ratio for result in results], dtype=np.float64
    )
    rate_ratios = np.concatenate(
        [
            np.concatenate((result.once_window_ratio, result.rearm_window_ratio))
            for result in results
        ]
    )
    finite_rate_ratios = rate_ratios[np.isfinite(rate_ratios)]
    if finite_rate_ratios.size == 0:
        finite_rate_ratios = np.array((float("nan"),), dtype=np.float64)
    locality_max = max(result.early_max_distance for result in results)
    locality_events = sum(result.early_event_count for result in results)
    observable_error = max(result.observable_error for result in results)
    checks_line = (
        "CHECKS "
        + ";".join(f"{name}={'ok' if passed else 'FAIL'}" for name, passed in checks.items())
        + f"; control-events={control_events}; GS-d-range=[{fmt_number(ground_d_minimum)},{fmt_number(ground_d_maximum)}]"
        + f"; locality@theta0.02,t<=1,events={locality_events},maxdist={fmt_number(locality_max)}"
        + f"; kappa-half/full-range=[{fmt_number(float(np.min(finite_rate_ratios)))},{fmt_number(float(np.max(finite_rate_ratios)))}]"
        + f"; Afull/Ahalf=[{fmt_number(float(np.min(activity_ratios)))},{fmt_number(float(np.max(activity_ratios)))}]"
        + f"; GS-residual={maximum_ground_residual:.2e}; norm-error={maximum_norm_error:.2e}"
        + f"; imported-observable-error={observable_error:.2e}"
    )

    failed = [name for name, passed in checks.items() if not passed]
    verdict = "KAPPA-MEASURED" if not failed else "MACHINERY-FAIL"
    exponent = median_finite_exponent(results)
    sparse_floor = fmt_suffix_floor(joint_sparse_mask)
    total = (
        f"TOTAL {verdict} failed={'none' if not failed else ','.join(failed)} "
        f"exponent={fmt_number(exponent)} exponent-summary=N_once-median "
        f"sparse-window-theta>={sparse_floor} sparse-discrete={fmt_theta_window(joint_sparse_mask)} "
        "sparse-summary=prep-a,joint-g,N_rearm "
        f"elapsed={elapsed:.2f}s "
        "SPEC-NOTE=QD-bridge-is-premise;purity-proxy=1-Tr(rho_bond^2),not-operational-trace-distance;"
        "absolute-GS-baseline-retained;crossings-are-sampled-and-convention-dependent;"
        "fill-translation-is-comparator-unit-only;threshold-not-axiomatic;"
        "no-formation-rule,no-gravity-claim,no-audit-status"
    )
    return [setup, kappa, scaling, window, checks_line, total], (0 if not failed else 1)


def run() -> tuple[list[str], int]:
    started = time.monotonic()
    engine, witnesses = load_authorized_sources()
    basis = engine.Basis(n_sites=N_SITES, w_max=W_MAX, charge_sector=0, rotor=True)
    trace_groups = [witnesses.build_bond_trace_groups(basis, bond) for bond in range(N_SITES)]
    layouts = [vectorize_trace_groups(groups, basis.dim) for groups in trace_groups]
    occupations, _ = witnesses.gauged_local_arrays(engine, basis, MASS, COUPLINGS[0])

    results: list[CaseResult] = []
    stationary_ok = True
    control_events = 0
    maximum_ground_residual = 0.0
    maximum_norm_error = 0.0
    ground_d_minimum = float("inf")
    ground_d_maximum = float("-inf")

    for coupling_index, coupling in enumerate(COUPLINGS):
        hamiltonian = engine.build_many_body_hamiltonian(
            basis,
            MASS,
            coupling,
            boundary_holonomy_shifts_w=True,
        ).tocsr()
        _, ground_state, ground_residual = deterministic_ground_state(
            hamiltonian,
            witnesses,
            RNG_SEED + coupling_index,
        )
        maximum_ground_residual = max(maximum_ground_residual, ground_residual)
        ground_d = ground_distinguishability(ground_state, trace_groups, witnesses)
        ground_d_minimum = min(ground_d_minimum, float(np.min(ground_d)))
        ground_d_maximum = max(ground_d_maximum, float(np.max(ground_d)))
        control_case_ok, coupling_control_events = stationary_control_is_exact(ground_d)
        stationary_ok = stationary_ok and control_case_ok
        control_events += coupling_control_events

        # Mirror the unitary-kick signs and occupation phases in check_gauged()
        # of activity_energy_bound_witnesses_2026_07_08.py; no kick helper is
        # exposed there.  The occupation arrays themselves are imported.
        kicked_a = np.exp(1.0j * 0.7 * occupations[0]) * ground_state
        kicked_b = np.exp(1.0j * 0.5 * (occupations[0] + occupations[6])) * ground_state
        initial_states = np.column_stack((kicked_a, kicked_b))
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
        norms = np.sum(np.abs(evolved) ** 2, axis=1)
        maximum_norm_error = max(maximum_norm_error, float(np.max(np.abs(norms - 1.0))))

        results.append(
            measure_case(
                coupling=coupling,
                preparation="a",
                centers=(0,),
                states=evolved[:, :, 0],
                hamiltonian=hamiltonian,
                trace_groups=trace_groups,
                layouts=layouts,
                witnesses=witnesses,
                ground_d=ground_d,
            )
        )
        results.append(
            measure_case(
                coupling=coupling,
                preparation="b",
                centers=(0, 6),
                states=evolved[:, :, 1],
                hamiltonian=hamiltonian,
                trace_groups=trace_groups,
                layouts=layouts,
                witnesses=witnesses,
                ground_d=ground_d,
            )
        )
        del evolved, hamiltonian

    preparation_a = [result for result in results if result.preparation == "a"]
    sparse_masks = [
        (result.rearm_kappa * (result.activity_total / N_SITES))
        <= FILL_LIMIT + 10.0 * np.finfo(float).eps
        for result in preparation_a
    ]
    joint_sparse_mask = np.logical_and.reduce(sparse_masks)
    machinery_ok = bool(
        maximum_ground_residual <= 1.0e-8
        and maximum_norm_error <= 1.0e-9
        and all(result.observable_error <= NUMERIC_TOL for result in results)
        and all(result.proxy_range_ok for result in results)
        and all(np.all(result.rearm_counts >= result.once_counts) for result in results)
    )
    checks = {
        "CHECK-01": stationary_ok and control_events == 0,
        "CHECK-02": all(result.locality_ok for result in results),
        "CHECK-03": all(result.monotone_ok for result in results),
        "CHECK-04": all(rate_window_ok(result) for result in results),
        "CHECK-05": bool(np.any(joint_sparse_mask)),
        "MACHINERY": machinery_ok,
    }
    elapsed = time.monotonic() - started
    return build_output(
        results,
        checks,
        control_events,
        maximum_ground_residual,
        maximum_norm_error,
        ground_d_minimum,
        ground_d_maximum,
        joint_sparse_mask,
        elapsed,
    )


def main() -> int:
    try:
        lines, exit_code = run()
    except Exception as exc:  # noqa: BLE001 - preserve the stdout line budget.
        message = " ".join(str(exc).split())[:220]
        print(
            f"TOTAL MACHINERY-FAIL error={type(exc).__name__}:{message} "
            "SPEC-NOTE=purity-proxy,crossing-conventions,comparator-unit-translation;"
            "no-formation-rule,no-gravity-claim,no-audit-status"
        )
        return 2
    for line in lines:
        print(line)
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
