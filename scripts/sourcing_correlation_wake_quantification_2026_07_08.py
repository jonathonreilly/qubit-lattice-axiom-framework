#!/usr/bin/env python3
"""Block02 two-channel WAKE quantification runner.

Purpose
-------
Block02 of the energy-to-records campaign: the WAKE quantification and
the two-channel sourcing structure. Records are permanent and site-locked
(axiom), so activity that deposits records leaves a permanent crowding trail:
a moving formation zone must slow clocks BEHIND itself, not only where it is.
This runner measures both channels honestly in the campaign-5 stochastic
comparator: the INSTANTANEOUS channel (clock suppression co-located with the
active zone) and the CUMULATIVE channel (permanent trail suppression after
passage), as a function of the deposition-per-transit parameter.

Companion note:
SOURCING_TWO_CHANNEL_WAKE_QUANTIFICATION_BOUNDED_NOTE_2026-07-08.md.

Comparator device; no formation rule chosen; no gravity/phenomenology claim
beyond the printed ratios; sets no audit status.

SPEC-NOTE design concerns surfaced here and in stdout:
* The normalized clock is (events per nominal site-time) / local attempt boost.
  This intentionally divides out the imposed activity boost and assigns zero
  clock to site-batches made unavailable by site-locked records, isolating the
  availability/crowding channel without conditioning away saturated intervals.
* The permanent fraction p is a comparator device: only records formed inside
  the moving activity zone are promoted to reset-immune, axiom-faithful records.
  All other records are resettable in the campaign-5 stationarity apparatus.
  That resettable background refreshes capacity and is a declared comparator
  artifact, not the axiom-faithful one-shot wake.
* Co-moving bins use the even-width window convention: offsets 0..9 are the
  wake/trailing half, and offsets 10..19 are the front/leading half.
* The saturation guard reports the maximum zone-width permanent trail density;
  resettable background occupancy is not treated as axiom permanence.
* The saturation wake leg turns background formation off outside the moving
  zone to isolate the zone's own deposition.  Background-formation physics
  remains the content of the two-channel comparator legs above.
* Saturation wake probes are non-invasive instantaneous-clock readouts: baseline
  formation attempts are counted from the frozen record field but are not
  committed as records.
"""

from __future__ import annotations

import importlib.util
import math
import sys
from dataclasses import dataclass
from pathlib import Path
from types import ModuleType

import numpy as np


L_RING = 300
ZONE_WIDTH = 20
SPEEDS = (0.5, 2.0)
BOOSTS = (2.0, 5.0)
PERMANENT_FRACTIONS = (0.0, 0.1, 0.5)
TRANSITS = 2.0
BURN_TIME = 1000.0
REPLICATES = 4
BATCHES_PER_REPLICATE = 24
SIGMA_WAKE_FRONT = 5.0
SIGMA_SPEED = 2.0
SIGMA_P0_WAKE = 2.0
SATURATION_WARN_DENSITY = 0.95
EPS = 1.0e-12
SATURATION_WAKE_SEED = 20260708
N_TRANSITS = 6
SATURATION_WAKE_V = 1.0
# Calibrated so first-transit fill lands in the partial-coverage regime
# (f ~ 0.35): fill ~ 1 - exp(-B * rate0 * dwell) with rate0 = 2.0 and
# dwell = ZONE_WIDTH / v = 20.  The b = 5 corner saturates in one transit
# (f = 1) and is kept as a reported corner, not a gate.
SATURATION_WAKE_BOOST = 0.011
SATURATION_WAKE_BOOST_CORNER = 5.0
SATURATION_WAKE_F_VALID = (0.10, 0.70)


@dataclass(frozen=True)
class EpochStats:
    counts: np.ndarray
    open_time: np.ndarray


@dataclass(frozen=True)
class TrialStats:
    baseline: EpochStats
    during: EpochStats
    after: EpochStats
    max_perm_window_density: float


@dataclass(frozen=True)
class ComboResult:
    v: float
    b: float
    p: float
    baseline_clock: float
    baseline_err: float
    during_clock: float
    during_err: float
    during_supp: float
    during_supp_err: float
    wake_clock: float
    wake_err: float
    front_clock: float
    front_err: float
    wake_front_z: float
    after_clock: float
    after_err: float
    after_supp: float
    after_supp_err: float
    wake_ratio: float
    wake_ratio_err: float
    max_perm_window_density: float


@dataclass(frozen=True)
class SaturationWakeResult:
    transit_totals: np.ndarray
    coverage: np.ndarray
    coverage_model: np.ndarray
    f_hat: float
    geometric_rms: float
    constant_rms: float
    suppression: np.ndarray
    suppression_increments: np.ndarray
    coverage_track_max_abs: float
    sigma_clock: np.ndarray
    one_shot_ok: bool
    check07_ok: bool
    check08_ok: bool
    check09_ok: bool
    check10_ok: bool
    corner_f: float
    corner_coverage: float

    @property
    def ok(self) -> bool:
        return self.check07_ok and self.check08_ok and self.check09_ok and self.check10_ok


def load_campaign5_source() -> ModuleType:
    """Import the named Block02 source; it is the only file this runner reads."""

    source_path = Path(__file__).with_name("formation_rate_law_class_reduction_2026_07_08.py")
    spec = importlib.util.spec_from_file_location("_campaign5_rate_law_source", source_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import campaign-5 source at {source_path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


SOURCE = load_campaign5_source()
SEED = int(SOURCE.SEED)
MU = float(SOURCE.MU)
LINEAR_PROFILE = next(profile for profile in SOURCE.SIM_PROFILES if profile.name == "linear1d")
LINEAR_LAW = next(law for law in SOURCE.RATE_LAWS if law.short == "lin")
AVAILABILITY_BY_NEIGHBORS = np.asarray(
    [float(LINEAR_PROFILE.availability(float(k))) for k in range(3)], dtype=float
)
INTRINSIC_RATE_BY_NEIGHBORS = np.asarray(
    [float(LINEAR_LAW.raw(a)) for a in AVAILABILITY_BY_NEIGHBORS], dtype=float
)
SITE_INDEX = np.arange(L_RING, dtype=int)


def zone_start(t_zone: float, v: float) -> int:
    return int(math.floor(v * t_zone + 1.0e-12)) % L_RING


def next_zone_boundary(t_zone: float, v: float, zone_duration: float) -> float:
    boundary = (math.floor(v * t_zone + 1.0e-12) + 1.0) / v
    if boundary <= t_zone + 1.0e-12:
        boundary += 1.0 / v
    return min(boundary, zone_duration)


def boost_and_offsets(t_zone: float, v: float, b: float) -> tuple[np.ndarray, np.ndarray]:
    start = zone_start(t_zone, v)
    offsets = (SITE_INDEX - start) % L_RING
    boosts = np.ones(L_RING, dtype=float)
    boosts[offsets < ZONE_WIDTH] = b
    return boosts, offsets


def formation_rates(
    temporary: np.ndarray,
    permanent: np.ndarray,
    boosts: np.ndarray,
) -> np.ndarray:
    recorded = temporary | permanent
    recorded_i = recorded.astype(np.int8)
    neighbor_count = np.roll(recorded_i, 1) + np.roll(recorded_i, -1)
    rates = boosts * INTRINSIC_RATE_BY_NEIGHBORS[neighbor_count]
    rates[recorded] = 0.0
    return rates


def max_zone_width_perm_density(permanent: np.ndarray) -> float:
    if not permanent.any():
        return 0.0
    perm_i = permanent.astype(float)
    best = 0.0
    for shift in range(ZONE_WIDTH):
        if shift == 0:
            window_sum = perm_i.copy()
        else:
            window_sum += np.roll(perm_i, -shift)
    best = float(window_sum.max() / ZONE_WIDTH)
    return best


def accumulate_open_time(
    out: EpochStats | None,
    batch_index: int,
    dt: float,
    temporary: np.ndarray,
    permanent: np.ndarray,
    offsets: np.ndarray | None,
) -> None:
    if out is None or dt <= 0.0:
        return
    open_mask = ~(temporary | permanent)
    if offsets is None:
        out.open_time[batch_index] += dt * open_mask
    else:
        out.open_time[batch_index, offsets] += dt * open_mask


def add_formation_count(
    out: EpochStats | None,
    batch_index: int,
    idx: int,
    offsets: np.ndarray | None,
) -> None:
    if out is None:
        return
    if offsets is None:
        out.counts[batch_index, idx] += 1.0
    else:
        out.counts[batch_index, int(offsets[idx])] += 1.0


def run_epoch(
    *,
    duration: float,
    rng: np.random.Generator,
    temporary: np.ndarray,
    permanent: np.ndarray,
    v: float,
    b: float,
    p: float,
    zone_active: bool,
    measure: bool,
) -> tuple[EpochStats | None, float]:
    batches = BATCHES_PER_REPLICATE
    batch_time = duration / batches
    stats = (
        EpochStats(
            counts=np.zeros((batches, L_RING), dtype=float),
            open_time=np.zeros((batches, L_RING), dtype=float),
        )
        if measure
        else None
    )
    t = 0.0
    batch_index = 0
    max_perm_density = max_zone_width_perm_density(permanent)

    while t < duration - 1.0e-12:
        if zone_active:
            boosts, offsets = boost_and_offsets(t, v, b)
            next_boundary = next_zone_boundary(t, v, duration)
        else:
            boosts = np.ones(L_RING, dtype=float)
            offsets = None
            next_boundary = duration

        form_rates = formation_rates(temporary, permanent, boosts)
        reset_rates = np.where(temporary, MU, 0.0)
        total_form = float(form_rates.sum())
        total_reset = float(reset_rates.sum())
        total = total_form + total_reset
        if total <= 0.0:
            raise RuntimeError("moving-zone process has zero total rate")

        dt_event = float(rng.exponential(1.0 / total))
        next_batch = min(duration, (batch_index + 1) * batch_time)
        dt_stop = min(dt_event, next_boundary - t, next_batch - t, duration - t)
        if dt_stop < -1.0e-12:
            raise RuntimeError("negative time step in epoch loop")
        dt = max(0.0, dt_stop)
        accumulate_open_time(stats, batch_index, dt, temporary, permanent, offsets)
        t += dt

        if t >= next_batch - 1.0e-12 and batch_index < batches - 1:
            batch_index += 1
            continue
        if zone_active and t >= next_boundary - 1.0e-12 and dt_event > dt + 1.0e-12:
            continue
        if dt_event > dt + 1.0e-12:
            continue
        if t >= duration - 1.0e-12:
            break

        draw = float(rng.random() * total)
        if draw < total_form:
            cumulative = np.cumsum(form_rates)
            idx = int(np.searchsorted(cumulative, draw, side="right"))
            if idx >= L_RING or temporary[idx] or permanent[idx] or form_rates[idx] <= 0.0:
                raise RuntimeError("selected invalid formation event")
            in_zone = False
            if zone_active and offsets is not None:
                in_zone = int(offsets[idx]) < ZONE_WIDTH
            if in_zone and rng.random() < p:
                permanent[idx] = True
                max_perm_density = max(max_perm_density, max_zone_width_perm_density(permanent))
            else:
                temporary[idx] = True
            add_formation_count(stats, batch_index, idx, offsets)
        else:
            reset_draw = draw - total_form
            cumulative_reset = np.cumsum(reset_rates)
            idx = int(np.searchsorted(cumulative_reset, reset_draw, side="right"))
            if idx >= L_RING or not temporary[idx]:
                raise RuntimeError("selected invalid reset event")
            temporary[idx] = False

    return stats, max_perm_density


def simulate_once(v: float, b: float, p: float, seed: int) -> TrialStats:
    rng = np.random.default_rng(seed)
    temporary = np.zeros(L_RING, dtype=bool)
    permanent = np.zeros(L_RING, dtype=bool)
    zone_duration = TRANSITS * L_RING / v

    run_epoch(
        duration=BURN_TIME,
        rng=rng,
        temporary=temporary,
        permanent=permanent,
        v=v,
        b=b,
        p=p,
        zone_active=False,
        measure=False,
    )
    baseline, max_base = run_epoch(
        duration=zone_duration,
        rng=rng,
        temporary=temporary,
        permanent=permanent,
        v=v,
        b=b,
        p=p,
        zone_active=False,
        measure=True,
    )
    during, max_during = run_epoch(
        duration=zone_duration,
        rng=rng,
        temporary=temporary,
        permanent=permanent,
        v=v,
        b=b,
        p=p,
        zone_active=True,
        measure=True,
    )
    after, max_after = run_epoch(
        duration=zone_duration,
        rng=rng,
        temporary=temporary,
        permanent=permanent,
        v=v,
        b=b,
        p=p,
        zone_active=False,
        measure=True,
    )
    if baseline is None or during is None or after is None:
        raise RuntimeError("missing measured epoch")
    return TrialStats(
        baseline=baseline,
        during=during,
        after=after,
        max_perm_window_density=max(max_base, max_during, max_after),
    )


def batch_clock(
    stats: EpochStats,
    selector: np.ndarray,
    epoch_duration: float,
    boost: float = 1.0,
) -> np.ndarray:
    """Site-locked normalized clock for a bin selector.

    The source runner's aggregate clock conditions on open-site time.  Here the
    wake question needs permanently occupied site-batches to read as zero clock,
    so the normalized event density is per nominal site-time and still divided
    by the imposed attempt boost.  This is the stated SPEC-NOTE normalization.
    """

    counts = stats.counts[:, selector].sum(axis=1)
    sites = int(selector.sum())
    if sites <= 0:
        raise RuntimeError("empty bin selector")
    batch_time = epoch_duration / BATCHES_PER_REPLICATE
    return counts / (batch_time * sites) / boost


def mean_err(values: np.ndarray) -> tuple[float, float]:
    if values.size < 2:
        raise RuntimeError("need at least two batches for an error estimate")
    mean = float(values.mean())
    err = float(values.std(ddof=1) / math.sqrt(values.size))
    return mean, err


def suppression(
    clock: float,
    clock_err: float,
    baseline: float,
    baseline_err: float,
) -> tuple[float, float]:
    if baseline <= 0.0:
        raise RuntimeError("non-positive baseline clock")
    value = 1.0 - clock / baseline
    err = math.hypot(clock_err / baseline, clock * baseline_err / (baseline * baseline))
    return float(value), float(err)


def ratio_with_err(num: float, num_err: float, den: float, den_err: float) -> tuple[float, float]:
    if abs(den) <= EPS:
        return math.nan, math.inf
    value = num / den
    err = math.hypot(num_err / den, num * den_err / (den * den))
    return float(value), float(abs(err))


def saturation_wake_zone_rates(permanent: np.ndarray, t_zone: float, boost: float = SATURATION_WAKE_BOOST) -> np.ndarray:
    """Formation rates for Leg 3: permanent records, zone-only attempts."""

    recorded_i = permanent.astype(np.int8)
    neighbor_count = np.roll(recorded_i, 1) + np.roll(recorded_i, -1)
    rates = boost * INTRINSIC_RATE_BY_NEIGHBORS[neighbor_count]
    rates[permanent] = 0.0
    start = zone_start(t_zone, SATURATION_WAKE_V)
    offsets = (SITE_INDEX - start) % L_RING
    rates[offsets >= ZONE_WIDTH] = 0.0
    return rates


def run_saturation_wake_transit(
    permanent: np.ndarray,
    rng: np.random.Generator,
    boost: float = SATURATION_WAKE_BOOST,
) -> np.ndarray:
    """Run one full zone transit with p=1 and no background formation."""

    deposits = np.zeros(L_RING, dtype=bool)
    duration = L_RING / SATURATION_WAKE_V
    t = 0.0
    while t < duration - 1.0e-12:
        rates = saturation_wake_zone_rates(permanent, t, boost)
        total = float(rates.sum())
        next_boundary = next_zone_boundary(t, SATURATION_WAKE_V, duration)
        if total <= 0.0:
            t = min(next_boundary, duration)
            continue

        dt_event = float(rng.exponential(1.0 / total))
        dt_stop = min(dt_event, next_boundary - t, duration - t)
        if dt_stop < -1.0e-12:
            raise RuntimeError("negative time step in saturation wake transit")
        dt = max(0.0, dt_stop)
        t += dt
        if dt_event > dt + 1.0e-12:
            continue
        if t >= duration - 1.0e-12:
            break

        draw = float(rng.random() * total)
        cumulative = np.cumsum(rates)
        idx = int(np.searchsorted(cumulative, draw, side="right"))
        if idx >= L_RING or permanent[idx] or deposits[idx] or rates[idx] <= 0.0:
            raise RuntimeError("selected invalid saturation wake deposit")
        deposits[idx] = True
        permanent[idx] = True
    return deposits


def saturation_probe_clock_field(permanent: np.ndarray) -> np.ndarray:
    """Non-invasive baseline-rate clock readout from a frozen record field."""

    empty_clock = float(INTRINSIC_RATE_BY_NEIGHBORS[0])
    if empty_clock <= 0.0:
        raise RuntimeError("non-positive empty-site probe clock")
    recorded_i = permanent.astype(np.int8)
    neighbor_count = np.roll(recorded_i, 1) + np.roll(recorded_i, -1)
    rates = INTRINSIC_RATE_BY_NEIGHBORS[neighbor_count].copy()
    rates[permanent] = 0.0
    return rates / empty_clock


def relative_rms(observed: np.ndarray, predicted: np.ndarray, scale: float) -> float:
    if scale <= 0.0:
        raise RuntimeError("non-positive rms scale")
    return float(np.sqrt(np.mean((observed - predicted) ** 2)) / scale)


def saturation_corner_report() -> tuple[float, float]:
    """One-transit corner at the saturating boost: (f_corner, coverage_1)."""

    rng = np.random.default_rng(SATURATION_WAKE_SEED + 1)
    permanent = np.zeros(L_RING, dtype=bool)
    deposits = run_saturation_wake_transit(permanent, rng, SATURATION_WAKE_BOOST_CORNER)
    f_corner = float(deposits.sum()) / float(L_RING)
    return f_corner, float(permanent.sum()) / float(L_RING)


def analyze_saturation_wake() -> SaturationWakeResult:
    rng = np.random.default_rng(SATURATION_WAKE_SEED)
    permanent = np.zeros(L_RING, dtype=bool)
    deposits = np.zeros((N_TRANSITS, L_RING), dtype=bool)
    probe_fields = np.zeros((N_TRANSITS, L_RING), dtype=float)

    for transit in range(N_TRANSITS):
        deposits[transit] = run_saturation_wake_transit(permanent, rng, SATURATION_WAKE_BOOST)
        probe_fields[transit] = saturation_probe_clock_field(permanent)

    deposits_by_site = deposits.sum(axis=0)
    one_shot_ok = bool(deposits_by_site.max() <= 1)
    if not one_shot_ok:
        raise RuntimeError("CHECK-07 one-shot bookkeeping violated")
    transit_totals = deposits.sum(axis=1).astype(float)
    swept_sites = float(L_RING)
    f_hat = float(transit_totals[0] / swept_sites)
    if not (SATURATION_WAKE_F_VALID[0] <= f_hat <= SATURATION_WAKE_F_VALID[1]):
        raise RuntimeError(
            f"Leg 3 boost miscalibrated: f_hat={f_hat:.3f} outside "
            f"{SATURATION_WAKE_F_VALID} — gates need the partial-coverage regime"
        )
    remainder = 1.0 - f_hat
    geometric_model = transit_totals[0] * remainder ** np.arange(N_TRANSITS, dtype=float)
    constant_model = np.full(N_TRANSITS, float(transit_totals.mean()), dtype=float)
    rms_scale = max(float(transit_totals[0]), 1.0)
    geometric_rms = relative_rms(transit_totals, geometric_model, rms_scale)
    constant_rms = relative_rms(transit_totals, constant_model, rms_scale)
    rejects_constant = constant_rms > 0.0 and geometric_rms < 0.5 * constant_rms
    # The geometric model assumes independent-site filling.  The crowding
    # mechanism suppresses deposition into gaps whose neighbors are already
    # recorded, so the physical claim is AT-LEAST-geometric decay: each
    # transit deposits no more than the independent-filling prediction, and
    # strictly less as crowding builds.  Equality is not expected.
    strictly_decreasing = bool(np.all(np.diff(transit_totals) < 0.0))
    at_most_geometric = bool(
        np.all(transit_totals <= geometric_model * 1.05 + 3.0)
    )
    check07_ok = bool(
        one_shot_ok and strictly_decreasing and at_most_geometric and rejects_constant
    )

    coverage = np.cumsum(transit_totals) / swept_sites
    coverage_model = 1.0 - remainder ** np.arange(1, N_TRANSITS + 1, dtype=float)
    coverage_abs_err = float(np.max(np.abs(coverage - coverage_model)))
    # Sub-geometric accumulation: the wake builds no faster than independent
    # filling, and its increments shrink (self-limiting trail).
    coverage_below_geometric = bool(np.all(coverage <= coverage_model + 0.02))
    increments_shrinking = bool(np.all(np.diff(np.diff(np.concatenate([[0.0], coverage]))) <= 1.0e-12))
    check08_ok = bool(coverage_below_geometric and increments_shrinking)

    suppression = 1.0 - probe_fields.mean(axis=1)
    suppression_increments = np.diff(suppression)
    monotone_suppression = bool(np.all(suppression_increments >= -1.0e-12))
    concave_suppression = bool(np.all(np.diff(suppression_increments) <= 1.0e-12))
    asymptoting_suppression = bool(
        abs(float(suppression_increments[-1]))
        <= 0.25 * abs(float(suppression_increments[0])) + 1.0e-12
    )
    if suppression[-1] <= 0.0 or coverage[-1] <= 0.0:
        coverage_track_max_abs = math.inf
    else:
        coverage_track = np.abs(suppression / suppression[-1] - coverage / coverage[-1])
        coverage_track_max_abs = float(coverage_track.max())
    check09_ok = bool(
        monotone_suppression
        and concave_suppression
        and asymptoting_suppression
        and coverage_track_max_abs <= 0.15
    )

    sigma_clock = probe_fields.std(axis=1)
    max_sigma = float(sigma_clock.max())
    max_suppression = float(suppression.max())
    check10_ok = bool(
        sigma_clock[-1] <= 0.4 * max_sigma + 1.0e-12
        and suppression[-1] >= 0.9 * max_suppression - 1.0e-12
    )

    corner_f, corner_coverage = saturation_corner_report()
    return SaturationWakeResult(
        transit_totals=transit_totals,
        coverage=coverage,
        coverage_model=coverage_model,
        f_hat=f_hat,
        geometric_rms=geometric_rms,
        constant_rms=constant_rms,
        suppression=suppression,
        suppression_increments=suppression_increments,
        coverage_track_max_abs=coverage_track_max_abs,
        sigma_clock=sigma_clock,
        one_shot_ok=one_shot_ok,
        check07_ok=check07_ok,
        check08_ok=check08_ok,
        check09_ok=check09_ok,
        check10_ok=check10_ok,
        corner_f=corner_f,
        corner_coverage=corner_coverage,
    )


def analyze_combo(v: float, b: float, p: float) -> ComboResult:
    trials: list[TrialStats] = []
    combo_seed_base = SEED + int(round(1000.0 * v)) + int(100 * b) + int(10000 * p)
    for rep in range(REPLICATES):
        trials.append(simulate_once(v, b, p, combo_seed_base + 7919 * rep))
    epoch_duration = TRANSITS * L_RING / v

    all_sites = np.ones(L_RING, dtype=bool)
    zone = np.zeros(L_RING, dtype=bool)
    zone[:ZONE_WIDTH] = True
    wake = np.zeros(L_RING, dtype=bool)
    wake[: ZONE_WIDTH // 2] = True
    front = np.zeros(L_RING, dtype=bool)
    front[ZONE_WIDTH // 2 : ZONE_WIDTH] = True

    baseline_batches = np.concatenate(
        [batch_clock(t.baseline, all_sites, epoch_duration) for t in trials]
    )
    during_batches = np.concatenate(
        [batch_clock(t.during, zone, epoch_duration, boost=b) for t in trials]
    )
    wake_batches = np.concatenate(
        [batch_clock(t.during, wake, epoch_duration, boost=b) for t in trials]
    )
    front_batches = np.concatenate(
        [batch_clock(t.during, front, epoch_duration, boost=b) for t in trials]
    )
    after_batches = np.concatenate(
        [batch_clock(t.after, all_sites, epoch_duration) for t in trials]
    )

    base, base_err = mean_err(baseline_batches)
    during, during_err = mean_err(during_batches)
    wake_clock, wake_err = mean_err(wake_batches)
    front_clock, front_err = mean_err(front_batches)
    after, after_err = mean_err(after_batches)
    during_supp, during_supp_err = suppression(during, during_err, base, base_err)
    after_supp, after_supp_err = suppression(after, after_err, base, base_err)
    wake_ratio, wake_ratio_err = ratio_with_err(
        after_supp,
        after_supp_err,
        during_supp,
        during_supp_err,
    )
    wake_front_z = (front_clock - wake_clock) / math.hypot(front_err, wake_err)
    max_density = max(t.max_perm_window_density for t in trials)

    return ComboResult(
        v=v,
        b=b,
        p=p,
        baseline_clock=base,
        baseline_err=base_err,
        during_clock=during,
        during_err=during_err,
        during_supp=during_supp,
        during_supp_err=during_supp_err,
        wake_clock=wake_clock,
        wake_err=wake_err,
        front_clock=front_clock,
        front_err=front_err,
        wake_front_z=float(wake_front_z),
        after_clock=after,
        after_err=after_err,
        after_supp=after_supp,
        after_supp_err=after_supp_err,
        wake_ratio=wake_ratio,
        wake_ratio_err=wake_ratio_err,
        max_perm_window_density=max_density,
    )


def result_map(results: list[ComboResult]) -> dict[tuple[float, float, float], ComboResult]:
    return {(r.v, r.b, r.p): r for r in results}


def fmt_float(value: float, digits: int = 3) -> str:
    if math.isnan(value):
        return "nan"
    if math.isinf(value):
        return "inf" if value > 0.0 else "-inf"
    return f"{value:.{digits}f}"


def fmt_series(values: np.ndarray, digits: int = 3) -> str:
    return "[" + ",".join(fmt_float(float(value), digits) for value in values) + "]"


def fmt_count_series(values: np.ndarray) -> str:
    return "[" + ",".join(str(int(round(float(value)))) for value in values) + "]"


def format_wake(results: list[ComboResult]) -> str:
    lookup = result_map(results)
    chunks: list[str] = []
    for v in SPEEDS:
        for b in BOOSTS:
            vals = []
            for p in PERMANENT_FRACTIONS:
                r = lookup[(v, b, p)]
                vals.append(
                    f"p={p:g}:R={fmt_float(r.wake_ratio, 3)} "
                    f"Sa={fmt_float(r.after_supp, 4)}+/-{fmt_float(r.after_supp_err, 4)}"
                )
            chunks.append(f"v={v:g},b={b:g}[{';'.join(vals)}]")
    return " | ".join(chunks)


def format_saturation_wake(result: SaturationWakeResult) -> str:
    verdict = "WAKE-SELF-REGULATING" if result.ok else "WAKE-NOT-SELF-REGULATING"
    max_suppression = float(result.suppression.max())
    s6_over_max = (
        float(result.suppression[-1] / max_suppression) if max_suppression > 0.0 else math.nan
    )
    return (
        "SATURATION-WAKE: "
        f"setup seed={SATURATION_WAKE_SEED} L={L_RING} W={ZONE_WIDTH} "
        f"v={SATURATION_WAKE_V:g} b={SATURATION_WAKE_BOOST:g} p=1 "
        f"N_TRANSITS={N_TRANSITS} profile={LINEAR_PROFILE.name} "
        f"law={LINEAR_LAW.name}:F(A)=A background_outside=0; "
        f"CHECK-07 one_shot={result.one_shot_ok} ok={result.check07_ok} "
        f"T={fmt_count_series(result.transit_totals)} f={fmt_float(result.f_hat, 3)} "
        f"rms_geo={fmt_float(result.geometric_rms, 3)} "
        f"rms_const={fmt_float(result.constant_rms, 3)}; "
        f"CHECK-08 ok={result.check08_ok} c={fmt_series(result.coverage, 3)} "
        f"c_geo={fmt_series(result.coverage_model, 3)}; "
        f"CHECK-09 ok={result.check09_ok} S={fmt_series(result.suppression, 3)} "
        f"dS={fmt_series(result.suppression_increments, 3)} "
        f"track_max={fmt_float(result.coverage_track_max_abs, 3)}; "
        f"CHECK-10 ok={result.check10_ok} sigma_N={fmt_series(result.sigma_clock, 3)} "
        f"S6_over_maxS={fmt_float(s6_over_max, 3)}; "
        "physics=UNIFORM-WAKE-IS-CONVENTION; "
        f"CORNER b={SATURATION_WAKE_BOOST_CORNER:g}: f={fmt_float(result.corner_f, 3)} "
        f"c1={fmt_float(result.corner_coverage, 3)} (saturates in one transit, reported not gated); "
        "SPEC-NOTE background-off isolates zone deposition; "
        "probe counts baseline attempts but commits no records; "
        "gates evaluated at the calibrated partial-coverage boost; "
        f"{verdict}"
    )


def format_during_gate(results: list[ComboResult]) -> str:
    relevant = [r for r in results if r.b == 5.0 and r.p >= 0.1]
    detail = ",".join(
        f"v={r.v:g},p={r.p:g}:z={fmt_float(r.wake_front_z, 1)} "
        f"W={fmt_float(r.wake_clock, 4)} F={fmt_float(r.front_clock, 4)}"
        for r in relevant
    )
    min_z = min(r.wake_front_z for r in relevant)
    return f"wake<front min_z(b=5,p>=0.1)={fmt_float(min_z, 1)}; {detail}"


def monotone_wake_in_p(results: list[ComboResult]) -> bool:
    lookup = result_map(results)
    for v in SPEEDS:
        for b in BOOSTS:
            vals = [lookup[(v, b, p)].wake_ratio for p in PERMANENT_FRACTIONS]
            if any(math.isnan(vv) for vv in vals):
                return False
            if not all(vals[i] <= vals[i + 1] + 1.0e-12 for i in range(len(vals) - 1)):
                return False
    return True


def p0_wake_consistent_with_zero(results: list[ComboResult]) -> bool:
    for r in results:
        if r.p != 0.0:
            continue
        if r.after_supp_err <= 0.0:
            if abs(r.after_supp) > EPS:
                return False
        elif abs(r.after_supp) >= SIGMA_P0_WAKE * r.after_supp_err:
            return False
    return True


def speed_scaling(results: list[ComboResult]) -> tuple[bool, float, list[str], list[float], str]:
    lookup = result_map(results)
    min_z = math.inf
    alphas: list[float] = []
    chunks: list[str] = []
    sdur_ratios: list[float] = []
    for b in BOOSTS:
        for p in PERMANENT_FRACTIONS:
            if p == 0.0:
                continue
            slow = lookup[(0.5, b, p)]
            fast = lookup[(2.0, b, p)]
            sep = slow.after_supp - fast.after_supp
            sep_err = math.hypot(slow.after_supp_err, fast.after_supp_err)
            z = sep / sep_err if sep_err > 0.0 else math.inf
            min_z = min(min_z, z)
            if slow.after_supp > EPS and fast.after_supp > EPS:
                alpha = math.log(slow.after_supp / fast.after_supp) / math.log(2.0 / 0.5)
            else:
                alpha = math.nan
            if fast.during_supp > EPS:
                sdur_ratios.append(slow.during_supp / fast.during_supp)
            alphas.append(alpha)
            chunks.append(
                f"b={b:g},p={p:g}:z={fmt_float(z, 1)} alpha={fmt_float(alpha, 2)}"
            )
    ok = min_z >= SIGMA_SPEED and all(not math.isnan(a) for a in alphas)
    if not all(
        lookup[(0.5, b, p)].after_supp > lookup[(2.0, b, p)].after_supp
        for b in BOOSTS
        for p in PERMANENT_FRACTIONS
        if p > 0.0
    ):
        ok = False
    if sdur_ratios:
        sdur_text = f"S_during_slow/fast_range={min(sdur_ratios):.2f}..{max(sdur_ratios):.2f}"
    else:
        sdur_text = "S_during_slow/fast_range=na"
    return ok, min_z, chunks, alphas, sdur_text


def run_all() -> tuple[str, ...]:
    results = [analyze_combo(v, b, p) for v in SPEEDS for b in BOOSTS for p in PERMANENT_FRACTIONS]
    saturation_wake = analyze_saturation_wake()
    during_ok = all(
        r.wake_clock < r.front_clock and r.wake_front_z >= SIGMA_WAKE_FRONT
        for r in results
        if r.b == 5.0 and r.p >= 0.1
    )
    p0_ok = p0_wake_consistent_with_zero(results)
    monotone_ok = monotone_wake_in_p(results)
    scaling_ok, min_speed_z, scaling_chunks, alphas, sdur_text = speed_scaling(results)
    max_density = max(r.max_perm_window_density for r in results)
    saturation_ok = max_density < SATURATION_WARN_DENSITY
    ratios = [r.wake_ratio for r in results if not math.isnan(r.wake_ratio)]
    ratio_range = (min(ratios), max(ratios)) if ratios else (math.nan, math.nan)
    finite_alphas = [a for a in alphas if not math.isnan(a)]
    dwell_alpha = float(sum(finite_alphas) / len(finite_alphas)) if finite_alphas else math.nan

    setup_line = (
        "SETUP: "
        f"seed={SEED} L={L_RING} W={ZONE_WIDTH} mu={MU:g} "
        f"profile={LINEAR_PROFILE.name} law={LINEAR_LAW.name}:F(A)=A "
        f"v={','.join(f'{v:g}' for v in SPEEDS)} b={','.join(f'{b:g}' for b in BOOSTS)} "
        f"p={','.join(f'{p:g}' for p in PERMANENT_FRACTIONS)} "
        f"batches={REPLICATES}x{BATCHES_PER_REPLICATE}; "
        "norm=(events/nominal-site-time)/attempt-boost; zone=2 transits; tail=same duration."
    )
    during_line = "DURING: " + format_during_gate(results)
    wake_line = "WAKE: " + format_wake(results)
    scaling_line = (
        "SCALING: "
        f"S_after slow>fast min_z={fmt_float(min_speed_z, 1)}; "
        + ",".join(scaling_chunks)
        + f"; {sdur_text}"
    )
    checks_line = (
        "CHECKS: "
        f"co_moving_dip={during_ok} p0_no_wake={p0_ok} "
        f"wake_monotone_in_p={monotone_ok} speed_gate={scaling_ok} "
        f"saturation_guard={saturation_ok} max_perm_window_density={max_density:.3f}; "
        "SPEC-NOTE normalized site-locked clock isolates crowding and gives saturated bins N=0; "
        "p is in-zone permanent fraction; "
        "co-moving wake/front are trailing/leading half-bins; "
        "resetting background refreshes capacity and is a comparator artifact; "
        "Leg3 background-off isolates zone deposition and probe attempts are counted without commits."
    )
    saturation_line = format_saturation_wake(saturation_wake)
    if all((during_ok, p0_ok, monotone_ok, scaling_ok, saturation_ok)):
        verdict = "TWO-CHANNEL-QUANTIFIED"
    else:
        verdict = "MACHINERY-FAIL"
    if saturation_wake.ok:
        verdict = f"{verdict} + WAKE-SELF-REGULATING"
    else:
        verdict = f"{verdict} + WAKE-NOT-SELF-REGULATING"
    total_line = (
        f"TOTAL: {verdict} (+ flags R_wake_range={fmt_float(ratio_range[0], 3)}.."
        f"{fmt_float(ratio_range[1], 3)}, wake_monotone_in_p={monotone_ok}, "
        f"dwell_alpha={fmt_float(dwell_alpha, 2)}, "
        f"saturation_wake={saturation_wake.ok})"
    )
    return setup_line, during_line, wake_line, scaling_line, checks_line, saturation_line, total_line


def main() -> int:
    try:
        lines = run_all()
        for line in lines:
            print(line)
        return (
            0
            if lines[-1].startswith("TOTAL: TWO-CHANNEL-QUANTIFIED")
            and "WAKE-SELF-REGULATING" in lines[-1]
            else 1
        )
    except Exception as exc:  # noqa: BLE001 - fail closed into the required token.
        print(f"TOTAL: MACHINERY-FAIL {type(exc).__name__}: {exc}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
