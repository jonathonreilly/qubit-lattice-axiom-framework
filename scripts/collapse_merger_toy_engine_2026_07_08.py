#!/usr/bin/env python3
"""Block01 collapse-merger comparator toy-engine validation runner.

Purpose
-------
Block01 of the collapse-merger-comparator campaign: a coupled d = 1 toy
in which gravity's loop runs end to end -- energy parcels fall along the
crowding-set clock gradient, deposit permanent records where they are active,
and the records slow the clocks.  Declared comparator device: the fall bias,
parcel model, and kappa are supplied toy couplings; the sign and class
structure are cited from the season's notes; nothing is derived here.  This
block validates the engine only.

Companion note:
COLLAPSE_MERGER_TOY_ENGINE_VALIDATION_NOTE_2026-07-08.md.

This runner sets no audit status.

The sign/class provenance is ``docs/RECORD_RATE_GRAVITY_BRIDGE_SYNTHESIS_2026-07-08.md``
(constraint-class crowding slows clocks; matter falls along
the time gradient) and its cited bounded notes.  The d=1 linear availability
profile, positive floor, linear law, normalization, and seed are mirrored from
``scripts/formation_rate_law_class_reduction_2026_07_08.py``; that source is
read-only and is not modified here.

Comparator conventions made precise
-------------------------------------
For a parcel at x, let ``D = clip(beta * (N[x-1] - N[x+1]) / 2,
-0.45, 0.45)``.  The probabilities are ``p_R = (1 + D) / 2`` and
``p_L = (1 - D) / 2``, hence ``p_R - p_L = D``.  A lower right-hand clock
therefore biases motion right.  Hops are simultaneous; an attempted hop into
a recorded site waits at its source.  Depositions are then sampled
simultaneously from the post-hop parcel counts.  Parcels on a newly recorded
site move to the closest sites that remain open; equal-distance left/right
destinations receive a seeded binomial split.

The positive-floor profile can propose recording the last open parcel-bearing
site.  That transition has no state satisfying both parcel conservation and
nearest-open displacement.  The displacement rule therefore supplies a
terminal one-open-site guard: if a simultaneous draw would close the whole
ring, one drawn site is retained as an open refuge.  This necessary boundary
consequence is included in the stdout SPEC-NOTE.

SPEC-NOTE design concerns are deliberately reported in stdout: the fall-bias
discretization above is a supplied comparator rule; displacement on formation
preserves energy but relocates it; and parcels are indistinguishable energy
counts with unrestricted multiple occupancy, not one-record-per-site objects.
"""

from __future__ import annotations

import hashlib
import json
import math
import struct
import sys
from dataclasses import dataclass

import numpy as np


L = 400
N_PARCELS = 200
BETA = 0.6
KAPPAS = (0.002, 0.01)
DT = 1.0
SEED = 20260708
T_STEPS = 2000
FALL_CLIP = 0.45
LINEAR_1D_FLOOR = 0.10
N_SIGN_SEEDS = 20
SIGN_STEPS = 200
SIGN_SIGMA_GATE = 5.0
NULL_SIGMA_GATE = 1.0
HUSK_REGION_SIZE = 10
HUSK_PARCELS = 60
HUSK_FILL_GATE = 0.80
BLOCK_SIZE = 20
EXCLUDED_STEPS = 200
SAMPLE_STEPS = (0, 1, 10, 100, 500, 1000, 2000)


# Campaign-5's mirrored d=1 tables: A(r)=max(0.1, 2.1-r), F(A)=A.
AVAILABILITY_BY_NEIGHBORS = np.asarray(
    [max(LINEAR_1D_FLOOR, LINEAR_1D_FLOOR + 2.0 - float(r)) for r in range(3)],
    dtype=np.float64,
)
A0 = float(AVAILABILITY_BY_NEIGHBORS[0])
NORMALIZED_CLOCK_BY_NEIGHBORS = AVAILABILITY_BY_NEIGHBORS / A0


@dataclass
class EngineState:
    """Complete mutable physical state; the clock is derived from records."""

    records: np.ndarray
    parcels: np.ndarray
    step: int = 0


@dataclass(frozen=True)
class StepStats:
    formed: np.ndarray
    offered_probability: np.ndarray
    blocked_hops: int


@dataclass(frozen=True)
class HopStats:
    blocked_hops: int
    accepted_right: np.ndarray
    accepted_left: np.ndarray


@dataclass(frozen=True)
class CoupledRun:
    state: EngineState
    samples: tuple[tuple[int, int, int], ...]
    digest: str


@dataclass(frozen=True)
class SignCheck:
    patch_fluxes: np.ndarray
    null_fluxes: np.ndarray
    patch_mean: float
    patch_error: float
    patch_sigma: float
    null_mean: float
    null_error: float
    null_sigma: float
    sign_exact: bool

    @property
    def ok(self) -> bool:
        return (
            self.sign_exact
            and self.patch_mean > 0.0
            and self.patch_sigma >= SIGN_SIGMA_GATE
            and abs(self.null_sigma) < NULL_SIGMA_GATE
        )


@dataclass(frozen=True)
class HuskCheck:
    active_fill: float
    control_fill: float
    first_gate_step: int | None
    fill_bins: np.ndarray
    empirical_rates: np.ndarray
    offered_rates: np.ndarray
    empirical_slope: float
    offered_slope: float

    @property
    def nucleation_ok(self) -> bool:
        return (
            self.active_fill >= HUSK_FILL_GATE
            and self.control_fill == 0.0
            and self.first_gate_step is not None
            and self.first_gate_step <= T_STEPS
        )

    @property
    def choking_ok(self) -> bool:
        return self.empirical_slope < 0.0 and self.offered_slope < 0.0


@dataclass(frozen=True)
class ExcludedCheck:
    maximum_inside: int
    transmitted: int
    blocked_hops: int
    boundary_profile: np.ndarray

    @property
    def ok(self) -> bool:
        return (
            self.maximum_inside == 0
            and self.transmitted == 0
            and self.blocked_hops > 0
            and self.boundary_profile[-1] > float(self.boundary_profile[:6].mean())
        )


def recorded_neighbor_count(records: np.ndarray) -> np.ndarray:
    recorded_i = records.astype(np.int8, copy=False)
    return np.roll(recorded_i, 1) + np.roll(recorded_i, -1)


def availability_field(records: np.ndarray) -> np.ndarray:
    return AVAILABILITY_BY_NEIGHBORS[recorded_neighbor_count(records)]


def clock_field(records: np.ndarray) -> np.ndarray:
    clocks = NORMALIZED_CLOCK_BY_NEIGHBORS[recorded_neighbor_count(records)].copy()
    clocks[records] = 0.0
    return clocks


def hop_probabilities(records: np.ndarray, beta: float = BETA) -> tuple[np.ndarray, np.ndarray]:
    clocks = clock_field(records)
    n_left = np.roll(clocks, 1)
    n_right = np.roll(clocks, -1)
    difference = np.clip(beta * (n_left - n_right) / 2.0, -FALL_CLIP, FALL_CLIP)
    p_right = (1.0 + difference) / 2.0
    p_left = (1.0 - difference) / 2.0
    if not np.allclose(p_right + p_left, 1.0, rtol=0.0, atol=0.0):
        raise AssertionError("hop probabilities do not sum exactly to one")
    if np.any((p_right < 0.0) | (p_right > 1.0)):
        raise AssertionError("invalid right-hop probability")
    return p_left, p_right


def hop_parcels(
    state: EngineState,
    rng: np.random.Generator,
    *,
    beta: float = BETA,
    hops_enabled: bool = True,
) -> HopStats:
    """Apply one simultaneous nearest-neighbor hop and expose actual hop currents."""

    if not hops_enabled:
        zeros = np.zeros(L, dtype=np.int64)
        return HopStats(blocked_hops=0, accepted_right=zeros, accepted_left=zeros.copy())
    _, p_right = hop_probabilities(state.records, beta)
    right = rng.binomial(state.parcels, p_right).astype(np.int64, copy=False)
    left = state.parcels - right
    right_blocked = np.roll(state.records, -1)
    left_blocked = np.roll(state.records, 1)
    blocked = int(right[right_blocked].sum() + left[left_blocked].sum())
    stay = np.where(right_blocked, right, 0) + np.where(left_blocked, left, 0)
    accepted_right = np.where(right_blocked, 0, right)
    accepted_left = np.where(left_blocked, 0, left)
    state.parcels = (
        stay + np.roll(accepted_right, 1) + np.roll(accepted_left, -1)
    ).astype(np.int64, copy=False)
    return HopStats(
        blocked_hops=blocked,
        accepted_right=accepted_right,
        accepted_left=accepted_left,
    )


def deposition_probabilities(state: EngineState, kappa: float, dt: float = DT) -> np.ndarray:
    """Return the specified per-open-site Bernoulli probabilities."""

    probabilities = (
        kappa * state.parcels.astype(np.float64) * availability_field(state.records) / A0 * dt
    )
    probabilities[state.records | (state.parcels == 0)] = 0.0
    if np.any(probabilities < 0.0):
        raise AssertionError("negative deposition probability")
    maximum = float(probabilities.max(initial=0.0))
    if maximum > 1.0:
        raise RuntimeError(
            f"specified discrete-time deposition probability exceeds one: {maximum:.6g}"
        )
    return probabilities


def closest_open_destinations(source: int, open_mask: np.ndarray) -> np.ndarray:
    open_sites = np.flatnonzero(open_mask)
    if open_sites.size == 0:
        raise RuntimeError("formation left no open site for parcel displacement")
    clockwise = (open_sites - source) % L
    counterclockwise = (source - open_sites) % L
    distances = np.minimum(clockwise, counterclockwise)
    nearest_distance = int(distances.min())
    return open_sites[distances == nearest_distance]


def displace_formed_site_parcels(
    parcels: np.ndarray,
    formed: np.ndarray,
    records_after: np.ndarray,
    rng: np.random.Generator,
) -> None:
    """Conserve parcels by moving them to nearest post-formation open sites."""

    open_mask = ~records_after
    for source in np.flatnonzero(formed):
        count = int(parcels[source])
        parcels[source] = 0
        if count == 0:
            continue
        destinations = closest_open_destinations(int(source), open_mask)
        if destinations.size == 1:
            parcels[int(destinations[0])] += count
        elif destinations.size == 2:
            to_first = int(rng.binomial(count, 0.5))
            parcels[int(destinations[0])] += to_first
            parcels[int(destinations[1])] += count - to_first
        else:
            allocation = rng.multinomial(count, np.full(destinations.size, 1.0 / destinations.size))
            np.add.at(parcels, destinations, allocation)


def validate_state(state: EngineState, expected_parcels: int) -> None:
    if state.records.shape != (L,) or state.records.dtype != np.bool_:
        raise AssertionError("record field must be a length-L boolean array")
    if state.parcels.shape != (L,) or not np.issubdtype(state.parcels.dtype, np.integer):
        raise AssertionError("parcel field must be a length-L integer array")
    if np.any(state.parcels < 0):
        raise AssertionError("negative parcel count")
    if int(state.parcels.sum()) != expected_parcels:
        raise AssertionError(
            f"parcel conservation failed: {int(state.parcels.sum())} != {expected_parcels}"
        )
    if np.any(state.parcels[state.records] != 0):
        raise AssertionError("parcel occupies a dynamically excluded recorded site")


def engine_step(
    state: EngineState,
    rng: np.random.Generator,
    *,
    kappa: float,
    beta: float = BETA,
    dt: float = DT,
    hops_enabled: bool = True,
    expected_parcels: int,
) -> StepStats:
    """Execute hop then deposition, asserting conservation and permanence."""

    records_before = state.records.copy()
    hop_stats = hop_parcels(state, rng, beta=beta, hops_enabled=hops_enabled)
    probabilities = deposition_probabilities(state, kappa, dt)
    eligible = np.flatnonzero(probabilities > 0.0)
    formed = np.zeros(L, dtype=np.bool_)
    if eligible.size:
        formed[eligible] = rng.random(eligible.size) < probabilities[eligible]
    if formed.any():
        if np.all(state.records | formed):
            refuge_candidates = np.flatnonzero(formed)
            refuge = int(rng.choice(refuge_candidates))
            formed[refuge] = False
        records_after = state.records | formed
        displace_formed_site_parcels(state.parcels, formed, records_after, rng)
        state.records = records_after
    state.step += 1
    if np.any(records_before & ~state.records):
        raise AssertionError("permanent record field decreased")
    validate_state(state, expected_parcels)
    return StepStats(
        formed=formed,
        offered_probability=probabilities,
        blocked_hops=hop_stats.blocked_hops,
    )


def uniform_parcels(records: np.ndarray, count: int) -> np.ndarray:
    """Place indistinguishable parcels as evenly as possible on open sites."""

    open_sites = np.flatnonzero(~records)
    if open_sites.size == 0 and count:
        raise ValueError("cannot place parcels without an open site")
    parcels = np.zeros(L, dtype=np.int64)
    if count:
        selected = open_sites[(np.arange(count, dtype=np.int64) * open_sites.size) // count]
        np.add.at(parcels, selected, 1)
    return parcels


def full_state_digest(
    state: EngineState,
    rng: np.random.Generator,
    *,
    kappa: float,
    beta: float = BETA,
    dt: float = DT,
) -> str:
    digest = hashlib.sha256()
    digest.update(state.records.astype(np.uint8, copy=False).tobytes())
    digest.update(state.parcels.astype(">i8", copy=False).tobytes())
    digest.update(clock_field(state.records).astype(">f8", copy=False).tobytes())
    digest.update(struct.pack(">qddd", state.step, kappa, beta, dt))
    digest.update(
        json.dumps(rng.bit_generator.state, sort_keys=True, separators=(",", ":")).encode("ascii")
    )
    return digest.hexdigest()


def coupled_run(kappa: float, seed: int = SEED) -> CoupledRun:
    records = np.zeros(L, dtype=np.bool_)
    state = EngineState(records=records, parcels=uniform_parcels(records, N_PARCELS))
    rng = np.random.default_rng(seed)
    validate_state(state, N_PARCELS)
    samples: list[tuple[int, int, int]] = [(0, 0, N_PARCELS)]
    sample_set = set(SAMPLE_STEPS)
    for _ in range(T_STEPS):
        engine_step(
            state,
            rng,
            kappa=kappa,
            expected_parcels=N_PARCELS,
        )
        if state.step in sample_set:
            samples.append((state.step, int(state.records.sum()), int(state.parcels.sum())))
    return CoupledRun(
        state=state,
        samples=tuple(samples),
        digest=full_state_digest(state, rng, kappa=kappa),
    )


def flux_trial(records: np.ndarray, left_probe: int, right_probe: int, seed: int) -> float:
    """Net accepted inward hops at the patch's two clock-gradient entry sites."""

    state = EngineState(records=records.copy(), parcels=uniform_parcels(records, N_PARCELS))
    rng = np.random.default_rng(seed)
    validate_state(state, N_PARCELS)
    net_toward = 0
    for _ in range(SIGN_STEPS):
        hops = hop_parcels(state, rng)
        net_toward += int(
            hops.accepted_right[left_probe]
            - hops.accepted_left[left_probe]
            + hops.accepted_left[right_probe]
            - hops.accepted_right[right_probe]
        )
        state.step += 1
        validate_state(state, N_PARCELS)
    return float(net_toward)


def mean_error_sigma(values: np.ndarray) -> tuple[float, float, float]:
    if values.size < 2:
        raise ValueError("at least two replicates are required")
    mean = float(values.mean())
    error = float(values.std(ddof=1) / math.sqrt(values.size))
    if error == 0.0:
        sigma = math.copysign(math.inf, mean) if mean != 0.0 else 0.0
    else:
        sigma = mean / error
    return mean, error, sigma


def check_attraction_sign() -> SignCheck:
    patch_start = L // 2 - BLOCK_SIZE // 2
    patch_sites = (patch_start + np.arange(BLOCK_SIZE, dtype=np.int64)) % L
    # Reflection-symmetric 50% fill, including both ends of the named patch.
    recorded_offsets = np.asarray((0, 2, 4, 6, 8, 11, 13, 15, 17, 19), dtype=np.int64)
    patch_records = np.zeros(L, dtype=np.bool_)
    patch_records[(patch_start + recorded_offsets) % L] = True
    if int(patch_records[patch_sites].sum()) * 2 != BLOCK_SIZE:
        raise AssertionError("CHECK-02 patch is not at 50% record fill")
    left_probe = (patch_start - 2) % L
    right_probe = (patch_start + BLOCK_SIZE + 1) % L

    # At x=start-2 the right neighboring clock is slowed by the endpoint record.
    _, p_right = hop_probabilities(patch_records)
    clocks = clock_field(patch_records)
    sign_exact = bool(
        clocks[(left_probe + 1) % L] < clocks[(left_probe - 1) % L]
        and p_right[left_probe] > 0.5
        and clocks[(right_probe - 1) % L] < clocks[(right_probe + 1) % L]
        and p_right[right_probe] < 0.5
    )

    seeds = [
        int(child.generate_state(1, dtype=np.uint64)[0])
        for child in np.random.SeedSequence(SEED).spawn(N_SIGN_SEEDS)
    ]
    patch_fluxes = np.asarray(
        [flux_trial(patch_records, left_probe, right_probe, seed) for seed in seeds],
        dtype=np.float64,
    )
    null_records = np.zeros(L, dtype=np.bool_)
    null_fluxes = np.asarray(
        [flux_trial(null_records, left_probe, right_probe, seed) for seed in seeds],
        dtype=np.float64,
    )
    patch_mean, patch_error, patch_sigma = mean_error_sigma(patch_fluxes)
    null_mean, null_error, null_sigma = mean_error_sigma(null_fluxes)
    return SignCheck(
        patch_fluxes=patch_fluxes,
        null_fluxes=null_fluxes,
        patch_mean=patch_mean,
        patch_error=patch_error,
        patch_sigma=patch_sigma,
        null_mean=null_mean,
        null_error=null_error,
        null_sigma=null_sigma,
        sign_exact=sign_exact,
    )


def check_husk_nucleation_and_choking() -> HuskCheck:
    active_region = np.arange(100, 100 + HUSK_REGION_SIZE, dtype=np.int64)
    control_region = np.arange(300, 300 + HUSK_REGION_SIZE, dtype=np.int64)

    active_records = np.zeros(L, dtype=np.bool_)
    active_parcels = np.zeros(L, dtype=np.int64)
    active_parcels[active_region] = HUSK_PARCELS // HUSK_REGION_SIZE
    if int(active_parcels.sum()) != HUSK_PARCELS:
        raise AssertionError("HUSK_PARCELS must divide evenly across the active region")
    active = EngineState(records=active_records, parcels=active_parcels)
    control = EngineState(
        records=np.zeros(L, dtype=np.bool_),
        parcels=np.zeros(L, dtype=np.int64),
    )
    active_rng = np.random.default_rng(SEED)
    control_rng = np.random.default_rng(SEED)
    exposures = np.zeros(HUSK_REGION_SIZE + 1, dtype=np.int64)
    event_totals = np.zeros(HUSK_REGION_SIZE + 1, dtype=np.int64)
    offered_totals = np.zeros(HUSK_REGION_SIZE + 1, dtype=np.float64)
    first_gate_step: int | None = None

    for _ in range(T_STEPS):
        pre_fill_count = int(active.records[active_region].sum())
        exposures[pre_fill_count] += 1
        active_stats = engine_step(
            active,
            active_rng,
            kappa=0.01,
            hops_enabled=False,
            expected_parcels=HUSK_PARCELS,
        )
        event_totals[pre_fill_count] += int(active_stats.formed[active_region].sum())
        offered_totals[pre_fill_count] += float(
            active_stats.offered_probability[active_region].sum()
        )
        if active.records[control_region].any() or active.parcels[control_region].any():
            raise AssertionError("same-ring CHECK-03 control ceased to be parcel-free")
        if (
            first_gate_step is None
            and float(active.records[active_region].mean()) >= HUSK_FILL_GATE
        ):
            first_gate_step = active.step

        # CHECK-03 is a first-passage gate (reach 0.8 within T), so its active
        # observation ends at the gate before displacement can carry the pinned
        # energy around the ring.  The independent zero-parcel control below is
        # still evolved for all T steps.
        if first_gate_step is not None:
            break

    for _ in range(T_STEPS):
        engine_step(
            control,
            control_rng,
            kappa=0.01,
            hops_enabled=False,
            expected_parcels=0,
        )
    if control.records.any():
        raise AssertionError("parcel-free control nucleated a record")
    growth_mask = (exposures > 0) & (np.arange(exposures.size) < HUSK_REGION_SIZE)
    fill_bins = np.arange(exposures.size, dtype=np.float64)[growth_mask] / HUSK_REGION_SIZE
    empirical_rates = event_totals[growth_mask] / exposures[growth_mask]
    offered_rates = offered_totals[growth_mask] / exposures[growth_mask]
    if fill_bins.size < 2:
        raise RuntimeError("too few occupied fill bins for CHECK-04 trend fit")
    empirical_slope = float(np.polyfit(fill_bins, empirical_rates, 1)[0])
    offered_slope = float(np.polyfit(fill_bins, offered_rates, 1)[0])
    return HuskCheck(
        active_fill=float(active.records[active_region].mean()),
        control_fill=max(
            float(active.records[control_region].mean()),
            float(control.records[control_region].mean()),
        ),
        first_gate_step=first_gate_step,
        fill_bins=fill_bins,
        empirical_rates=empirical_rates,
        offered_rates=offered_rates,
        empirical_slope=empirical_slope,
        offered_slope=offered_slope,
    )


def check_excluded_volume() -> ExcludedCheck:
    block_start = L // 2 - BLOCK_SIZE // 2
    block = (block_start + np.arange(BLOCK_SIZE, dtype=np.int64)) % L
    records = np.zeros(L, dtype=np.bool_)
    records[block] = True
    parcels = np.zeros(L, dtype=np.int64)
    release_sites = (block_start + np.arange(-20, -10, dtype=np.int64)) % L
    parcels[release_sites] = N_PARCELS // release_sites.size
    if int(parcels.sum()) != N_PARCELS:
        raise AssertionError("CHECK-05 release sites do not divide the parcel count")
    state = EngineState(records=records, parcels=parcels)
    rng = np.random.default_rng(SEED)
    far_side = (block_start + BLOCK_SIZE + np.arange(BLOCK_SIZE, dtype=np.int64)) % L
    profile_sites = (block_start + np.arange(-12, 0, dtype=np.int64)) % L
    maximum_inside = int(state.parcels[block].sum())
    transmitted = int(state.parcels[far_side].sum())
    blocked_hops = 0
    profile_samples: list[np.ndarray] = []

    for _ in range(EXCLUDED_STEPS):
        stats = engine_step(
            state,
            rng,
            kappa=0.0,
            expected_parcels=N_PARCELS,
        )
        maximum_inside = max(maximum_inside, int(state.parcels[block].sum()))
        transmitted = max(transmitted, int(state.parcels[far_side].sum()))
        blocked_hops += stats.blocked_hops
        if state.step > EXCLUDED_STEPS - 50:
            profile_samples.append(state.parcels[profile_sites].astype(np.float64))
    if len(profile_samples) != 50:
        raise AssertionError("CHECK-05 boundary averaging window has the wrong length")
    boundary_profile = np.mean(np.stack(profile_samples), axis=0)
    return ExcludedCheck(
        maximum_inside=maximum_inside,
        transmitted=transmitted,
        blocked_hops=blocked_hops,
        boundary_profile=boundary_profile,
    )


def pass_fail(value: bool) -> str:
    return "PASS" if value else "FAIL"


def format_samples(run: CoupledRun) -> str:
    return "[" + ",".join(f"{step}:{records}:{parcels}" for step, records, parcels in run.samples) + "]"


def format_profile(profile: np.ndarray) -> str:
    return "[" + ",".join(f"{value:.2f}" for value in profile) + "]"


def status_flags_and_spec() -> str:
    return (
        "flags(sign=pR-pL=clip(beta*(N_L-N_R)/2,[-0.45,0.45]);slower-target-favored,"
        "blocked-hop=wait,displacement=nearest-post-open/tie-seeded-binomial/terminal-refuge); "
        "SPEC-NOTE: fall-bias, parcel model, and kappa are supplied comparator couplings; "
        "formation displacement conserves but relocates energy (the last-open refuge is forced "
        "by that rule); parcels are indistinguishable multi-occupancy energy counts, not records; "
        "engine validation only, no audit status."
    )


def run_validation() -> tuple[tuple[str, ...], bool]:
    primary_runs = {kappa: coupled_run(kappa, SEED) for kappa in KAPPAS}
    check01 = all(
        all(sample[2] == N_PARCELS for sample in run.samples)
        and all(b[1] >= a[1] for a, b in zip(run.samples, run.samples[1:]))
        for run in primary_runs.values()
    )

    sign = check_attraction_sign()
    husk = check_husk_nucleation_and_choking()
    excluded = check_excluded_volume()

    repeated_runs = {kappa: coupled_run(kappa, SEED) for kappa in KAPPAS}
    check06 = all(
        primary_runs[kappa].digest == repeated_runs[kappa].digest for kappa in KAPPAS
    )
    all_ok = all(
        (
            check01,
            sign.ok,
            husk.nucleation_ok,
            husk.choking_ok,
            excluded.ok,
            check06,
        )
    )

    conservation_parts = " | ".join(
        f"kappa={kappa:g} samples(step:R:P)={format_samples(primary_runs[kappa])}"
        for kappa in KAPPAS
    )
    line01 = (
        f"CHECK-01 CONSERVATION: {pass_fail(check01)} exact every step; record monotone; "
        + conservation_parts
    )
    line02 = (
        f"CHECK-02 ATTRACTION SIGN: {pass_fail(sign.ok)} accepted gradient-entry flux "
        f"patch={sign.patch_mean:.2f}+/-{sign.patch_error:.2f} (z={sign.patch_sigma:.2f},toward) "
        f"null={sign.null_mean:.2f}+/-{sign.null_error:.2f} (z={sign.null_sigma:.2f}); "
        f"seeds={N_SIGN_SEEDS},steps={SIGN_STEPS},sign-exact={sign.sign_exact}"
    )
    line03 = (
        f"CHECK-03 HUSK NUCLEATION: {pass_fail(husk.nucleation_ok)} pinned-hops-off="
        f"{HUSK_PARCELS}/"
        f"{HUSK_REGION_SIZE} active-fill={husk.active_fill:.2f} first-0.8-step="
        f"{husk.first_gate_step} parcel-free-control={husk.control_fill:.2f} | "
        f"CHECK-04 CHOKING: {pass_fail(husk.choking_ok)} fit slopes "
        f"offered={husk.offered_slope:.4f},empirical={husk.empirical_slope:.4f}; "
        f"offered-rate={husk.offered_rates[0]:.4f}->{husk.offered_rates[-1]:.4f}/step"
    )
    line05 = (
        f"CHECK-05 EXCLUDED VOLUME: {pass_fail(excluded.ok)} inside-max="
        f"{excluded.maximum_inside} transmission={excluded.transmitted} blocked-hops="
        f"{excluded.blocked_hops} deposition=off; boundary-profile offsets[-12..-1],last50mean="
        f"{format_profile(excluded.boundary_profile)}"
    )
    hashes = ",".join(
        f"kappa={kappa:g}:{primary_runs[kappa].digest[:16]}"
        for kappa in KAPPAS
    )
    line06 = (
        f"CHECK-06 DETERMINISM: {pass_fail(check06)} full state+clock+RNG hash identical "
        f"across same-seed reruns ({hashes})"
    )
    verdict = "ENGINE-VALID" if all_ok else "MACHINERY-FAIL"
    total_line = f"TOTAL: {verdict}; {status_flags_and_spec()}"
    return (line01, line02, line03, line05, line06, total_line), all_ok


def main() -> int:
    try:
        lines, ok = run_validation()
        if len(lines) > 6:
            raise AssertionError("stdout contract exceeded six lines")
        for line in lines:
            print(line)
        return 0 if ok else 1
    except Exception as exc:  # noqa: BLE001 - validation runner fails closed.
        print(
            f"TOTAL: MACHINERY-FAIL {type(exc).__name__}: {exc}; "
            + status_flags_and_spec()
        )
        return 1


if __name__ == "__main__":
    sys.exit(main())
