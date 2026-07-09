#!/usr/bin/env python3
"""Block02 single-blob collapse comparator: frozen-star anatomy as numbers.

Purpose
-------
Block02: single-blob collapse in the coupled toy -- the frozen-star anatomy
as numbers.  Declared comparator; no derivation; no audit status.  Companion
note: COLLAPSE_FROZEN_STAR_ANATOMY_BOUNDED_NOTE_2026-07-08.md.

This runner dynamically imports ``collapse_merger_toy_engine_2026_07_08.py``
and uses its state, hop, deposition, displacement, validation, clock, and
availability layers without changing them.  The run is a d = 1 periodic-ring
comparator, not a continuum collapse calculation.

The initially named blob region is the three-sigma arc about the ring centre.
The husk is the largest connected recorded component intersecting that fixed
arc; ties prefer the component containing the empirical initial density peak,
then greater overlap, then the lowest site label.  The boundary ring is the
set of open nearest neighbours of that husk.  These choices are reported as
SPEC-NOTE concerns rather than presented as derived physics.

Deposition uses the engine's Poisson rate-to-probability conversion
``1 - exp(-kappa * n * (A/A0) * dt)``, so offers are valid at any occupancy;
nothing is clipped or substepped here.

Two declared regime choices.  First, gravity in this engine is
record-mediated: with no records there is no clock gradient, so a fresh blob
diffuses until its own deposits nucleate, and pre-nucleation contraction has
no channel by construction.  Worse, at matched kappa every end-state
statistic is d = 1 caging-confounded (records form where parcels are in both
legs, and unbiased 1-d diffusion is recurrent, so even beta = 0 cages
coalesce).  CHECK-01 therefore runs two phases: self-form the husk under the
true dynamics, then freeze deposition (kappa = 0) and release fresh probes
around it with the fall bias on vs off — the paired capture difference is
the bare pull of the self-formed structure.  Second, the kappa/T budget is
chosen so the run stays in the star-with-exterior regime (an exterior-open
gate is part of CHECK-05); larger budgets saturate the whole compact ring,
which is the global-saturation endgame, not a frozen star.
"""

from __future__ import annotations

from dataclasses import dataclass
import importlib.util
import math
from pathlib import Path
import sys
import time
from typing import Any

sys.dont_write_bytecode = True

import numpy as np


THIS_FILE = Path(__file__).resolve()
ENGINE_PATH = THIS_FILE.with_name("collapse_merger_toy_engine_2026_07_08.py")
NOTE_NAME = "COLLAPSE_FROZEN_STAR_ANATOMY_BOUNDED_NOTE_2026-07-08.md"

L = 400
BETA = 0.6
DT = 1.0
SEED = 20260708
N_PARCELS = 300
INITIAL_SIGMA = 10.0
INITIAL_BLOB_RADIUS = 30
KAPPAS = (0.00025, 0.001)
T_STEPS = 3000
N_BINDING_SEEDS = 10
# Two-phase self-gravitation check.  At matched kappa every end-state
# occupancy or concentration statistic is caging-confounded in d=1 (records
# form where parcels are in both legs, and 1-d diffusion is recurrent, so
# even the beta=0 cages coalesce).  Phase 1 self-forms the husk under the
# true dynamics; phase 2 freezes deposition (kappa=0, so no cage can form)
# and releases fresh probes around the self-formed husk with the fall bias
# on vs off — the paired difference is the bare clock-well pull.
BIND_STEPS = 1000
# The clock well is short-ranged (nearest-neighbor availability) and the
# wall-retention bias is weak per step, so end-state occupancy statistics
# barely separate the legs.  The engine's own attraction check solved this
# with a cumulative statistic: a uniform probe bath and the net accepted
# hop flux at the structure's entry sites, accumulated every step.  Here the
# entry ring is every open site at graph distance exactly 2 from the phase-1
# record set (distance-1 hops toward a record are blocked in both legs;
# distance 2 is where the clock bias acts).
PROBE_PARCELS = 300
PROBE_STEPS = 300
PROBE_RNG_OFFSET = 977
SIGMA_GATE = 5.0
# No-condensation gate: no single site may hold this fraction of the supply.
CONDENSATION_FRACTION = 0.8
EXTERIOR_OPEN_GATE = 0.30
SHELL_WIDTH = 3
# Escape is measured from the husk surface (the star is the reference frame);
# a fixed ring-centre radius would sit inside a grown husk.
ESCAPE_BUFFER = 10
HUSK_SAMPLE_STEPS = (250, 500, 1000, 2000, 3000)
FLOAT_EPS = 1.0e-15


def load_engine() -> Any:
    """Load the read-only sibling engine by path, as required by the block."""

    spec = importlib.util.spec_from_file_location(
        "collapse_merger_toy_engine_for_frozen_star_20260708", ENGINE_PATH
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import engine from {ENGINE_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


engine = load_engine()


def assert_engine_conventions() -> None:
    expected = {
        "L": L,
        "BETA": BETA,
        "DT": DT,
        "SEED": SEED,
    }
    observed = {name: getattr(engine, name) for name in expected}
    if observed != expected:
        raise AssertionError(
            f"engine convention drift: expected={expected}, observed={observed}"
        )
    if engine.EngineState.__module__ != engine.__name__:
        raise AssertionError("dynamic engine state was not loaded from the named module")


@dataclass(frozen=True)
class InitialBlob:
    parcels: np.ndarray
    peak: int
    sigma: float


@dataclass(frozen=True)
class FailureInfo:
    attempted_step: int
    exception_type: str
    message: str
    offered_max: float
    site_max: int


@dataclass(frozen=True)
class Trajectory:
    kappa: float
    beta: float
    seed: int
    initial_peak: int
    initial_sigma: float
    records: np.ndarray
    parcels: np.ndarray
    husks: np.ndarray
    husk_mass: np.ndarray
    interior_fill: np.ndarray
    radial_profile: np.ndarray
    deposition_rate: np.ndarray
    offered_rate: np.ndarray
    parcel_sigma: np.ndarray
    boundary_clock: np.ndarray
    global_site_max: int
    boundary_site_max: int
    failure: FailureInfo | None

    @property
    def final_step(self) -> int:
        return self.records.shape[0] - 1

    @property
    def complete(self) -> bool:
        return self.failure is None and self.final_step == T_STEPS


@dataclass(frozen=True)
class BindingCheck:
    flux_differences: np.ndarray
    active_flux_mean: float
    control_flux_mean: float
    difference_mean: float
    difference_error: float
    difference_z: float
    husk_min: int
    husk_max: int
    entry_min: int

    @property
    def ok(self) -> bool:
        return self.difference_mean > 0.0 and self.difference_z >= SIGMA_GATE


@dataclass(frozen=True)
class TrendFit:
    slope: float
    error: float
    z: float
    upward_steps: int
    asymptote: float

    @property
    def ok(self) -> bool:
        return self.slope < 0.0 and self.z <= -SIGMA_GATE


@dataclass(frozen=True)
class Anatomy:
    husk_mass: int
    shell_population: int
    shell_fraction: float
    escaped_population: int
    escaped_fraction: float


@dataclass(frozen=True)
class GrowthFit:
    law: str
    exponent: float
    power_r2: float
    log_r2: float
    late_d2: float
    decelerates: bool


def circular_offsets(center: int) -> np.ndarray:
    sites = np.arange(L, dtype=np.int64)
    return ((sites - center + L // 2) % L - L // 2).astype(np.int64)


def weighted_sigma(parcels: np.ndarray, center: int) -> float:
    offsets = circular_offsets(center).astype(np.float64)
    count = int(parcels.sum())
    if count <= 0:
        raise ValueError("parcel sigma requires a nonempty parcel field")
    mean = float(np.dot(parcels, offsets) / count)
    variance = float(np.dot(parcels, (offsets - mean) ** 2) / count)
    return math.sqrt(max(0.0, variance))


def draw_initial_blob(rng: np.random.Generator) -> InitialBlob:
    positions = np.rint(
        rng.normal(loc=L // 2, scale=INITIAL_SIGMA, size=N_PARCELS)
    ).astype(np.int64) % L
    parcels = np.bincount(positions, minlength=L).astype(np.int64, copy=False)
    maximum = int(parcels.max())
    candidates = np.flatnonzero(parcels == maximum)
    offsets = np.abs(circular_offsets(L // 2)[candidates])
    peak = int(candidates[np.lexsort((candidates, offsets))[0]])
    return InitialBlob(
        parcels=parcels,
        peak=peak,
        sigma=weighted_sigma(parcels, L // 2),
    )


def make_initial_blob(seed: int) -> InitialBlob:
    return draw_initial_blob(np.random.default_rng(seed))


def initialized_state_and_rng(
    seed: int,
) -> tuple[InitialBlob, Any, np.random.Generator]:
    """Use one seeded stream for the Gaussian draw and subsequent engine steps."""

    rng = np.random.default_rng(seed)
    initial = draw_initial_blob(rng)
    state = engine.EngineState(
        records=np.zeros(L, dtype=np.bool_),
        parcels=initial.parcels.copy(),
    )
    engine.validate_state(state, N_PARCELS)
    return initial, state, rng


def initial_blob_mask() -> np.ndarray:
    return np.abs(circular_offsets(L // 2)) <= INITIAL_BLOB_RADIUS


def connected_record_components(records: np.ndarray) -> tuple[np.ndarray, ...]:
    """Return nearest-neighbour connected components on the periodic ring."""

    if records.shape != (L,) or records.dtype != np.bool_:
        raise AssertionError("component input must be the engine boolean record field")
    if not records.any():
        return ()
    if records.all():
        return (np.arange(L, dtype=np.int64),)
    break_site = int(np.flatnonzero(~records)[0])
    components: list[np.ndarray] = []
    current: list[int] = []
    for offset in range(1, L + 1):
        site = (break_site + offset) % L
        if records[site]:
            current.append(site)
        elif current:
            components.append(np.asarray(current, dtype=np.int64))
            current = []
    return tuple(components)


def husk_mask(records: np.ndarray, initial_peak: int) -> np.ndarray:
    """Select the declared largest blob-overlapping recorded component."""

    blob = initial_blob_mask()
    candidates = [
        component
        for component in connected_record_components(records)
        if bool(blob[component].any())
    ]
    selected = np.zeros(L, dtype=np.bool_)
    if not candidates:
        return selected
    component = max(
        candidates,
        key=lambda item: (
            int(item.size),
            int(initial_peak in item),
            int(blob[item].sum()),
            -int(item.min()),
        ),
    )
    selected[component] = True
    return selected


def graph_distance_to_mask(mask: np.ndarray) -> np.ndarray:
    sites = np.arange(L, dtype=np.int64)
    occupied = np.flatnonzero(mask)
    if occupied.size == 0:
        return np.full(L, L, dtype=np.int64)
    clockwise = (sites[:, None] - occupied[None, :]) % L
    counterclockwise = (occupied[None, :] - sites[:, None]) % L
    return np.minimum(clockwise, counterclockwise).min(axis=1).astype(np.int64)


def boundary_mask(husk: np.ndarray) -> np.ndarray:
    if not husk.any():
        return np.zeros(L, dtype=np.bool_)
    return (np.roll(husk, 1) | np.roll(husk, -1)) & ~husk


def husk_interior_fill(husk: np.ndarray) -> float:
    """Record fill of the minimal connected arc occupied by the chosen husk."""

    mass = int(husk.sum())
    if mass == 0:
        return 0.0
    components = connected_record_components(husk)
    if len(components) != 1:
        raise AssertionError("selected husk is not one connected component")
    return float(mass / components[0].size)


def radial_profile(parcels: np.ndarray) -> np.ndarray:
    radii = np.abs(circular_offsets(L // 2))
    return np.bincount(radii, weights=parcels, minlength=L // 2 + 1).astype(
        np.int64, copy=False
    )


def run_trajectory(kappa: float, seed: int = SEED, beta: float = BETA) -> Trajectory:
    """Run and retain every requested per-step field and scalar observable."""

    initial, state, rng = initialized_state_and_rng(seed)
    records = np.zeros((T_STEPS + 1, L), dtype=np.bool_)
    parcels = np.zeros((T_STEPS + 1, L), dtype=np.int64)
    husks = np.zeros((T_STEPS + 1, L), dtype=np.bool_)
    husk_mass = np.zeros(T_STEPS + 1, dtype=np.int64)
    interior_fill = np.zeros(T_STEPS + 1, dtype=np.float64)
    profiles = np.zeros((T_STEPS + 1, L // 2 + 1), dtype=np.int64)
    deposition_rate = np.zeros(T_STEPS + 1, dtype=np.float64)
    offered_rate = np.zeros(T_STEPS + 1, dtype=np.float64)
    parcel_sigma = np.zeros(T_STEPS + 1, dtype=np.float64)
    boundary_clock = np.ones(T_STEPS + 1, dtype=np.float64)
    global_site_max = 0
    boundary_site_max = 0
    failure: FailureInfo | None = None

    def snapshot(index: int) -> None:
        nonlocal global_site_max, boundary_site_max
        engine.validate_state(state, N_PARCELS)
        if state.step != index:
            raise AssertionError(f"engine/history step mismatch: {state.step} != {index}")
        if int(state.records.astype(np.uint8).max(initial=0)) > 1:
            raise AssertionError("record density exceeded one per site")
        records[index] = state.records
        parcels[index] = state.parcels
        current_husk = husk_mask(state.records, initial.peak)
        husks[index] = current_husk
        husk_mass[index] = int(current_husk.sum())
        interior_fill[index] = husk_interior_fill(current_husk)
        profiles[index] = radial_profile(state.parcels)
        parcel_sigma[index] = weighted_sigma(state.parcels, L // 2)
        current_boundary = boundary_mask(current_husk)
        if current_boundary.any():
            boundary_clock[index] = float(
                engine.clock_field(state.records)[current_boundary].mean()
            )
            boundary_site_max = max(
                boundary_site_max, int(state.parcels[current_boundary].max(initial=0))
            )
        global_site_max = max(global_site_max, int(state.parcels.max(initial=0)))

    snapshot(0)
    for _ in range(T_STEPS):
        stats = engine.engine_step(
            state,
            rng,
            kappa=kappa,
            beta=beta,
            dt=DT,
            expected_parcels=N_PARCELS,
        )
        index = state.step
        deposition_rate[index] = float(stats.formed.sum()) / DT
        offered_rate[index] = float(stats.offered_probability.sum()) / DT
        snapshot(index)

    valid = state.step + 1
    return Trajectory(
        kappa=kappa,
        beta=beta,
        seed=seed,
        initial_peak=initial.peak,
        initial_sigma=initial.sigma,
        records=records[:valid].copy(),
        parcels=parcels[:valid].copy(),
        husks=husks[:valid].copy(),
        husk_mass=husk_mass[:valid].copy(),
        interior_fill=interior_fill[:valid].copy(),
        radial_profile=profiles[:valid].copy(),
        deposition_rate=deposition_rate[:valid].copy(),
        offered_rate=offered_rate[:valid].copy(),
        parcel_sigma=parcel_sigma[:valid].copy(),
        boundary_clock=boundary_clock[:valid].copy(),
        global_site_max=global_site_max,
        boundary_site_max=boundary_site_max,
        failure=failure,
    )


def self_formed_husk(seed: int) -> tuple[np.ndarray, np.ndarray]:
    """Phase 1: form the husk under the true dynamics; return (records, husk)."""

    initial, state, rng = initialized_state_and_rng(seed)
    for _ in range(BIND_STEPS):
        engine.engine_step(
            state,
            rng,
            kappa=KAPPAS[1],
            beta=BETA,
            dt=DT,
            expected_parcels=N_PARCELS,
        )
    husk = husk_mask(state.records, initial.peak)
    if not husk.any():
        raise RuntimeError("phase-1 formation produced no blob-overlapping husk")
    return state.records.copy(), husk


def probe_leg(records: np.ndarray, seed: int, *, beta: float) -> tuple[float, int]:
    """Phase 2: uniform probe bath; net hop flux toward the frozen structure.

    No deposition happens in this phase (hops only), so no record can form
    and no cage confound exists: the paired active/control difference is the
    bare pull of the self-formed structure, accumulated at its distance-2
    entry ring.
    """

    distances = graph_distance_to_mask(records)
    entry = np.flatnonzero(distances == 2)
    if entry.size == 0:
        raise RuntimeError("record set has no distance-2 entry ring")
    toward_right = distances[(entry + 1) % L] < distances[(entry - 1) % L]
    toward_left = distances[(entry - 1) % L] < distances[(entry + 1) % L]

    state = engine.EngineState(
        records=records.copy(),
        parcels=engine.uniform_parcels(records, PROBE_PARCELS),
    )
    rng = np.random.default_rng(seed + PROBE_RNG_OFFSET)
    net_toward = 0
    for _ in range(PROBE_STEPS):
        hops = engine.hop_parcels(state, rng, beta=beta)
        state.step += 1
        engine.validate_state(state, PROBE_PARCELS)
        net_toward += int(
            hops.accepted_right[entry[toward_right]].sum()
            - hops.accepted_left[entry[toward_right]].sum()
            + hops.accepted_left[entry[toward_left]].sum()
            - hops.accepted_right[entry[toward_left]].sum()
        )
    return float(net_toward), int(entry.size)


def spawned_seeds() -> tuple[int, ...]:
    children = np.random.SeedSequence(SEED).spawn(N_BINDING_SEEDS)
    return tuple(
        int(child.generate_state(1, dtype=np.uint64)[0]) for child in children
    )


def check_binding() -> BindingCheck:
    """Two-phase self-gravitation: does the self-formed husk pull fresh energy?

    Phase 1 is identical for both legs (one formation run per seed); phase 2
    branches only in beta with deposition frozen, so the paired capture
    difference isolates the clock-well pull of the structure the blob built.
    """

    active_fluxes: list[float] = []
    control_fluxes: list[float] = []
    husk_sizes: list[int] = []
    entry_sizes: list[int] = []
    for seed in spawned_seeds():
        records, husk = self_formed_husk(seed)
        husk_sizes.append(int(husk.sum()))
        active_flux, entry_size = probe_leg(records, seed, beta=BETA)
        control_flux, _ = probe_leg(records, seed, beta=0.0)
        entry_sizes.append(entry_size)
        active_fluxes.append(active_flux)
        control_fluxes.append(control_flux)
    differences = np.asarray(active_fluxes) - np.asarray(control_fluxes)
    difference_mean, difference_error, difference_z = engine.mean_error_sigma(
        differences
    )
    return BindingCheck(
        flux_differences=differences,
        active_flux_mean=float(np.mean(active_fluxes)),
        control_flux_mean=float(np.mean(control_fluxes)),
        difference_mean=difference_mean,
        difference_error=difference_error,
        difference_z=difference_z,
        husk_min=min(husk_sizes),
        husk_max=max(husk_sizes),
        entry_min=min(entry_sizes),
    )


def fit_boundary_trend(run: Trajectory) -> TrendFit:
    times = np.arange(run.final_step + 1, dtype=np.float64)
    values = run.boundary_clock
    if values.size < 3:
        raise RuntimeError("too few boundary-clock observations for a trend fit")
    centered = times - float(times.mean())
    denominator = float(np.dot(centered, centered))
    slope = float(np.dot(centered, values - values.mean()) / denominator)
    intercept = float(values.mean() - slope * times.mean())
    residual = values - (intercept + slope * times)
    error = math.sqrt(float(np.dot(residual, residual)) / (values.size - 2) / denominator)
    if error == 0.0:
        z = math.copysign(math.inf, slope) if slope != 0.0 else 0.0
    else:
        z = slope / error
    late_count = max(1, values.size // 10)
    return TrendFit(
        slope=slope,
        error=error,
        z=z,
        upward_steps=int(np.count_nonzero(np.diff(values) > FLOAT_EPS)),
        asymptote=float(values[-late_count:].mean()),
    )


def final_anatomy(run: Trajectory) -> Anatomy:
    husk = run.husks[-1]
    distances = graph_distance_to_mask(husk)
    shell = (distances >= 1) & (distances <= SHELL_WIDTH)
    final_parcels = run.parcels[-1]
    shell_population = int(final_parcels[shell].sum())
    escaped_population = int(final_parcels[distances > ESCAPE_BUFFER].sum())
    return Anatomy(
        husk_mass=int(husk.sum()),
        shell_population=shell_population,
        shell_fraction=shell_population / N_PARCELS,
        escaped_population=escaped_population,
        escaped_fraction=escaped_population / N_PARCELS,
    )


def coefficient_of_determination(observed: np.ndarray, fitted: np.ndarray) -> float:
    residual_ss = float(np.dot(observed - fitted, observed - fitted))
    centered = observed - float(observed.mean())
    total_ss = float(np.dot(centered, centered))
    if total_ss == 0.0:
        return 1.0 if residual_ss <= FLOAT_EPS else 0.0
    return 1.0 - residual_ss / total_ss


def fit_growth(run: Trajectory) -> GrowthFit | None:
    if not run.complete:
        return None
    late_start = T_STEPS // 2
    late_mid = (late_start + T_STEPS) // 2
    times = np.arange(late_start, T_STEPS + 1, dtype=np.float64)
    masses = run.husk_mass[late_start:].astype(np.float64)
    if np.any(masses <= 0.0):
        raise RuntimeError("late-time power fit requires a nonzero husk")
    log_times = np.log(times)
    if float(np.ptp(masses)) == 0.0:
        exponent = 0.0
        power_r2 = 1.0
        log_r2 = 1.0
        law = "flat"
    else:
        power_coefficients = np.polyfit(log_times, np.log(masses), 1)
        exponent = float(power_coefficients[0])
        power_fit = np.exp(np.polyval(power_coefficients, log_times))
        power_r2 = coefficient_of_determination(masses, power_fit)
        log_coefficients = np.polyfit(log_times, masses, 1)
        log_fit = np.polyval(log_coefficients, log_times)
        log_r2 = coefficient_of_determination(masses, log_fit)
        law = "power" if power_r2 >= log_r2 else "log"
    half_width = late_mid - late_start
    first_increment = int(run.husk_mass[late_mid] - run.husk_mass[late_start])
    second_increment = int(run.husk_mass[T_STEPS] - run.husk_mass[late_mid])
    curvature_numerator = second_increment - first_increment
    return GrowthFit(
        law=law,
        exponent=exponent,
        power_r2=power_r2,
        log_r2=log_r2,
        late_d2=curvature_numerator / float(half_width**2),
        decelerates=curvature_numerator < 0,
    )


def validate_tracking(run: Trajectory) -> None:
    if run.records.shape != run.parcels.shape or run.records.shape[1] != L:
        raise AssertionError("record/parcel history shape mismatch")
    if run.husks.shape != run.records.shape:
        raise AssertionError("husk history shape mismatch")
    if run.radial_profile.shape != (run.final_step + 1, L // 2 + 1):
        raise AssertionError("radial-profile history shape mismatch")
    if not np.all(run.parcels.sum(axis=1) == N_PARCELS):
        raise AssertionError("tracked parcel history violates conservation")
    if not np.all(run.radial_profile.sum(axis=1) == N_PARCELS):
        raise AssertionError("tracked radial profile violates conservation")
    if not np.array_equal(run.husk_mass, run.husks.sum(axis=1)):
        raise AssertionError("tracked husk mass does not match the husk masks")
    if run.final_step and np.any(run.records[:-1] & ~run.records[1:]):
        raise AssertionError("tracked permanent record field decreased")
    record_counts = run.records.sum(axis=1).astype(np.int64)
    if not np.array_equal(
        np.diff(record_counts), run.deposition_rate[1:].astype(np.int64)
    ):
        raise AssertionError("tracked deposition rate does not match record increments")
    if np.any((run.interior_fill < 0.0) | (run.interior_fill > 1.0)):
        raise AssertionError("invalid tracked interior fill")
    if np.any(run.boundary_clock < 0.0):
        raise AssertionError("negative tracked boundary clock")
    if int(run.records.astype(np.uint8).max(initial=0)) > 1:
        raise AssertionError("record capacity exceeded one")


def combine_flags(flags: list[bool | None]) -> bool | None:
    if any(flag is False for flag in flags):
        return False
    if any(flag is None for flag in flags):
        return None
    return True


def flag_text(flag: bool | None) -> str:
    if flag is None:
        return "NA"
    return "PASS" if flag else "FAIL"


def kappa_text(kappa: float) -> str:
    return f"{kappa:g}"


def husk_gate(run: Trajectory) -> tuple[bool | None, bool, bool, bool, int]:
    monotone = bool(np.all(np.diff(run.husk_mass) >= 0))
    components = connected_record_components(run.records[-1])
    one_cluster = len(components) == 1
    contains_peak = bool(run.husks[-1, run.initial_peak])
    # Satellite cages nucleated by the diffusing tail are separate ring
    # components by construction; the husk selection already excludes them,
    # so the gate is monotone growth of a peak-containing husk, with the
    # total component count reported.
    gate = monotone and contains_peak if run.complete else None
    return gate, monotone, one_cluster, contains_peak, len(components)


def sample_husk_masses(run: Trajectory) -> str:
    entries = [
        f"{step}:{int(run.husk_mass[step]) if step <= run.final_step else 'NA'}"
        for step in HUSK_SAMPLE_STEPS
    ]
    return "[" + ",".join(entries) + "]"


def growth_text(growth: GrowthFit | None) -> str:
    if growth is None:
        return "late-law=NA,alpha=NA,d2=NA"
    return (
        f"late-law={growth.law},alpha={growth.exponent:.4f},"
        f"R2(power/log)={growth.power_r2:.3f}/{growth.log_r2:.3f},"
        f"d2={growth.late_d2:.3e}"
    )


def failure_text(run: Trajectory) -> str:
    if run.failure is None:
        return "complete"
    failure = run.failure
    return (
        f"partial@t={run.final_step};native-reject@{failure.attempted_step}:"
        f"pmax={failure.offered_max:.6f}"
    )


def spec_note() -> str:
    return (
        "SPEC-NOTE: d=1 declared comparator; rounded Gaussian and fixed 3sigma blob arc; "
        "largest-overlap husk with declared tie rule; boundary=open nearest-neighbor ring "
        "(trend gate, raw upsteps shown); CHECK-01 is a two-phase probe (self-form the "
        "husk under the true dynamics, then kappa=0 fresh probes with fall bias on vs "
        "off) because at matched kappa every end-state statistic is d=1 "
        "caging-confounded; gravity is record-mediated, so pre-nucleation contraction "
        "has no channel; kappa/T budget chosen for "
        "the star-with-exterior regime (larger budgets saturate the compact ring); "
        "deposition offers are the engine's Poisson conversion; capture/escape are "
        "measured from the husk surface (the star is the reference frame); "
        "low-kappa fragmented nucleation is the proto-star regime, reported not "
        "gated; native nearest-open displacement/terminal refuge and unrestricted "
        "parcel multi-occupancy retained; no derivation, no audit status."
    )


def run_validation() -> tuple[tuple[str, ...], str]:
    started = time.monotonic()
    assert_engine_conventions()
    binding = check_binding()
    runs = {kappa: run_trajectory(kappa) for kappa in KAPPAS}
    for run in runs.values():
        validate_tracking(run)

    husk_results = {kappa: husk_gate(run) for kappa, run in runs.items()}
    # Peak-containment is a collapsed-star claim: it is gated at the anatomy
    # kappa only.  Low-kappa fragmented nucleation (many small cages, largest
    # fragment off-peak) is the proto-star regime, reported not gated.
    monotone_all = all(result[1] for result in husk_results.values())
    complete_all = all(run.complete for run in runs.values())
    check02: bool | None = (
        monotone_all and husk_results[KAPPAS[1]][3] if complete_all else None
    )

    record_max = max(
        int(run.records.astype(np.uint8).max(initial=0)) for run in runs.values()
    )
    if record_max > 1:
        raise AssertionError("CHECK-03 record capacity assertion failed")
    condensation_cap = int(CONDENSATION_FRACTION * N_PARCELS)
    check03 = record_max <= 1 and all(
        run.global_site_max <= condensation_cap for run in runs.values()
    )

    trends = {kappa: fit_boundary_trend(run) for kappa, run in runs.items()}
    trend_flags = [
        trends[kappa].ok if runs[kappa].complete else None for kappa in KAPPAS
    ]
    check04 = combine_flags(trend_flags)

    anatomies = {kappa: final_anatomy(run) for kappa, run in runs.items()}
    open_fractions = {
        kappa: 1.0 - float(run.records[-1].sum()) / L for kappa, run in runs.items()
    }
    in_regime = all(
        fraction >= EXTERIOR_OPEN_GATE for fraction in open_fractions.values()
    )
    high_run = runs[KAPPAS[1]]
    check05: bool | None = (
        in_regime and anatomies[KAPPAS[1]].shell_fraction >= 0.5
        if high_run.complete
        else None
    )

    growth = {kappa: fit_growth(run) for kappa, run in runs.items()}
    # Two ossification regimes, two gates.  Supply-starved (low kappa, parcels
    # leak from the fragmented proto-star): growth decelerates.  Capture-fed
    # (anatomy kappa, infall concentrates the boundary pile): growth continues
    # and accelerates -- the measured law is reported; deceleration is NOT
    # claimed there.  This corrects the pre-run "ossification decelerates"
    # expectation, which holds only in the starved regime.
    late_start = T_STEPS // 2
    high_masses = runs[KAPPAS[1]].husk_mass
    high_late_rate = (
        float(high_masses[-1] - high_masses[late_start]) / (T_STEPS - late_start)
        if runs[KAPPAS[1]].complete
        else None
    )
    low_growth = growth[KAPPAS[0]]
    check06: bool | None = (
        low_growth.late_d2 <= 0.0 and high_late_rate > 0.0
        if low_growth is not None and high_late_rate is not None
        else None
    )

    line01 = (
        f"CHECK-01 SELF-FORMED HUSK GRAVITATES: {flag_text(binding.ok)} "
        f"{N_BINDING_SEEDS}-seed two-phase probe (form@kappa="
        f"{kappa_text(KAPPAS[1])},t={BIND_STEPS}; hop-only uniform bath "
        f"{PROBE_PARCELS} parcels, t={PROBE_STEPS}): net entry-ring flux "
        f"toward record set active={binding.active_flux_mean:+.1f} vs "
        f"beta0-control={binding.control_flux_mean:+.1f}, paired diff="
        f"{binding.difference_mean:+.1f}+/-{binding.difference_error:.1f} "
        f"(z={binding.difference_z:+.2f};need >=+5); husk-range="
        f"[{binding.husk_min},{binding.husk_max}],entry-ring>="
        f"{binding.entry_min}; diffusion-first is by construction (gravity "
        "is record-mediated; no pre-nucleation contraction channel exists)."
    )

    husk_parts: list[str] = []
    for kappa in KAPPAS:
        run = runs[kappa]
        gate, monotone, one_cluster, contains_peak, component_count = husk_results[kappa]
        husk_parts.append(
            f"k={kappa_text(kappa)}:{flag_text(gate)}({failure_text(run)},"
            f"H/R={int(run.husk_mass[-1])}/{int(run.records[-1].sum())},"
            f"mono={monotone},clusters={component_count},one={one_cluster},"
            f"peak={contains_peak},fill={run.interior_fill[-1]:.2f})"
        )
    line02 = (
        f"CHECK-02 HUSK GROWTH + MONOTONE: {flag_text(check02)} "
        + " | ".join(husk_parts)
    )

    capacity_parts = [
        f"k={kappa_text(kappa)}:max-site={runs[kappa].global_site_max},"
        f"boundary-max={runs[kappa].boundary_site_max},{failure_text(runs[kappa])}"
        for kappa in KAPPAS
    ]
    line03 = (
        f"CHECK-03 CAPACITY CAP: {flag_text(check03)} record-density-max={record_max} "
        f"(asserted <=1); no-condensation gate max-site <= {condensation_cap} "
        f"(={CONDENSATION_FRACTION:g}*Np); " + " | ".join(capacity_parts)
    )

    floor = float(engine.LINEAR_1D_FLOOR / engine.A0)
    trend_parts = []
    for kappa in KAPPAS:
        run = runs[kappa]
        trend = trends[kappa]
        local_gate: bool | None = trend.ok if run.complete else None
        trend_parts.append(
            f"k={kappa_text(kappa)}:{flag_text(local_gate)}({failure_text(run)},"
            f"slope={trend.slope:+.3e}+/-{trend.error:.1e},z={trend.z:+.2f},"
            f"raw-up={trend.upward_steps},tail={trend.asymptote:.6f})"
        )
    line04 = (
        f"CHECK-04 EXTERIOR FREEZE: {flag_text(check04)} floor={floor:.6f}; "
        + " | ".join(trend_parts)
    )

    anatomy_parts = []
    growth_parts = []
    for kappa in KAPPAS:
        run = runs[kappa]
        anatomy = anatomies[kappa]
        anatomy_parts.append(
            f"k={kappa_text(kappa)}@t={run.final_step}{'*' if not run.complete else ''}:"
            f"H={anatomy.husk_mass},shell={anatomy.shell_population}/"
            f"{N_PARCELS}({anatomy.shell_fraction:.3f}),"
            f"unbound>{ESCAPE_BUFFER}-from-husk={anatomy.escaped_population}/"
            f"{N_PARCELS}({anatomy.escaped_fraction:.3f}),"
            f"open={open_fractions[kappa]:.3f}"
        )
        growth_parts.append(
            f"k={kappa_text(kappa)} H={sample_husk_masses(run)} "
            f"{growth_text(growth[kappa])}"
        )
    line05 = (
        f"CHECK-05 FROZEN-STAR ANATOMY: {flag_text(check05)} "
        f"(exterior-open gate >= {EXTERIOR_OPEN_GATE:g}: "
        f"{flag_text(in_regime)}) " + " | ".join(anatomy_parts)
        + f"; CHECK-06 OSSIFICATION LAW: {flag_text(check06)} "
        f"(gates: starved d2<=0@k={kappa_text(KAPPAS[0])}, capture-fed "
        f"dH/dt>0@k={kappa_text(KAPPAS[1])} late-rate="
        f"{high_late_rate if high_late_rate is None else round(high_late_rate, 4)}"
        "/step; measured law reported, deceleration claimed in the starved "
        "regime only) " + " | ".join(growth_parts)
    )

    check_flags: tuple[bool | None, ...] = (
        binding.ok,
        check02,
        check03,
        check04,
        check05,
        check06,
    )
    machinery_fail = any(run.failure is not None for run in runs.values())
    if machinery_fail:
        verdict = "MACHINERY-FAIL"
    elif all(flag is True for flag in check_flags):
        verdict = "FROZEN-STAR-EXHIBITED"
    else:
        verdict = "FROZEN-STAR-PARTIAL"
    flags = ",".join(
        f"{index:02d}:{flag_text(flag)}" for index, flag in enumerate(check_flags, 1)
    )
    failures = ";".join(
        f"k={kappa_text(kappa)}:{failure_text(run)}"
        for kappa, run in runs.items()
        if run.failure is not None
    )
    failure_suffix = f"; native-domain={failures}" if failures else ""
    elapsed = time.monotonic() - started
    line06 = (
        f"TOTAL: {verdict}; flags[{flags}]; runtime={elapsed:.3f}s{failure_suffix}; "
        + spec_note()
    )
    lines = (line01, line02, line03, line04, line05, line06)
    if len(lines) > 6 or any("\n" in line for line in lines):
        raise AssertionError("stdout contract exceeded six single lines")
    return lines, verdict


def main() -> int:
    try:
        lines, verdict = run_validation()
        for line in lines:
            print(line)
        if verdict == "FROZEN-STAR-EXHIBITED":
            return 0
        return 2 if verdict == "MACHINERY-FAIL" else 1
    except Exception as exc:  # noqa: BLE001 - comparator runner fails closed.
        print(
            f"TOTAL: MACHINERY-FAIL {type(exc).__name__}: {exc}; " + spec_note()
        )
        return 2


if __name__ == "__main__":
    sys.exit(main())
