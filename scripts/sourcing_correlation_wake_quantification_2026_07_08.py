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
* Co-moving bins use the even-width window convention: offsets 0..9 are the
  wake/trailing half, and offsets 10..19 are the front/leading half.
* The saturation guard reports the maximum zone-width permanent trail density;
  resettable background occupancy is not treated as axiom permanence.
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


def run_all() -> tuple[str, str, str, str, str, str]:
    results = [analyze_combo(v, b, p) for v in SPEEDS for b in BOOSTS for p in PERMANENT_FRACTIONS]
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
        "co-moving wake/front are trailing/leading half-bins; resetting is comparator."
    )
    if all((during_ok, p0_ok, monotone_ok, scaling_ok, saturation_ok)):
        verdict = "TWO-CHANNEL-QUANTIFIED"
    else:
        verdict = "MACHINERY-FAIL"
    total_line = (
        f"TOTAL: {verdict} (+ flags R_wake_range={fmt_float(ratio_range[0], 3)}.."
        f"{fmt_float(ratio_range[1], 3)}, wake_monotone_in_p={monotone_ok}, "
        f"dwell_alpha={fmt_float(dwell_alpha, 2)})"
    )
    return setup_line, during_line, wake_line, scaling_line, checks_line, total_line


def main() -> int:
    try:
        lines = run_all()
        for line in lines:
            print(line)
        return 0 if lines[-1].startswith("TOTAL: TWO-CHANNEL-QUANTIFIED") else 1
    except Exception as exc:  # noqa: BLE001 - fail closed into the required token.
        print(f"TOTAL: MACHINERY-FAIL {type(exc).__name__}: {exc}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
