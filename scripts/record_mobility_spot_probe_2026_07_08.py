#!/usr/bin/env python3
"""Owner-requested record-mobility spot probe.

Does record MOBILITY (records may hop between sites, one-per-site exclusion
kept) actually incur the costs attributed to it? Three computable objections
are tested head-on: (1) geometry anchoring -- does motion scramble the
causal-order reconstruction that builds spacetime's shape from records?;
(2) the wake -- does source-following motion kill it?; (3) frozen pockets /
saturation -- does mobility thaw them, or does exclusion freeze motion exactly
where saturation lives? Exploratory comparator content; no axiom change is made
or proposed; sets no audit status. Companion note:
RECORD_MOBILITY_SPOT_PROBE_NOTE_2026-07-08.md.
"""

from __future__ import annotations

import math
import sys
from dataclasses import dataclass

import numpy as np


SEED = 20260708
RATE_BY_NEIGHBORS = np.asarray([1.0, 0.5, 0.0], dtype=float)
EPS = 1.0e-12

ANCHOR_L = 200
ANCHOR_K = 400
ANCHOR_U = 0.5
ANCHOR_VMAX = 1.0
ANCHOR_HORIZON = 50
ANCHOR_MOTION_STEPS = 200
ANCHOR_DIFFUSION_RATE = 0.1
ANCHOR_BACKGROUND_COUNT = 8

WAKE_L = 300
WAKE_WIDTH = 20
# Calibrated for partial fill (~0.35) on the swept half; b = 5 saturates
# the path and makes relocation unmeasurable (run-1 artifact).
WAKE_BOOST = 0.011
WAKE_TRANSIT_FRACTION = 0.5
WAKE_V = 1.0
WAKE_DIFFUSION_RATE = 0.1

CORE_DIFFUSION_RATE = 0.1
CORE_LOSS_LAYERS = 5
CORE_MAX_STEPS = 300_000

POCKET_L = 300
POCKET_SEED_FRACTION = 0.30
POCKET_DIFFUSION_RATE = 0.1
POCKET_POST_DURATION = 1000.0


@dataclass(frozen=True)
class AnchoringResult:
    c0: float
    c_advected: float
    cross_advected: float
    diffusion_steps: tuple[int, ...]
    diffusion_curve: tuple[float, ...]
    diffusion_half_life: str
    gate_1a: bool


@dataclass(frozen=True)
class WakeMotionResult:
    density_frozen: float
    density_advected: float
    density_diffused: float
    s_frozen: float
    s_advected: float
    s_diffused: float
    width_frozen: int
    width_advected: int
    width_diffused: int
    integrated_crowding_ratio_advected: float
    integrated_crowding_ratio_diffused: float
    integrated_clock_ratio_diffused: float
    s_virgin_frozen: float
    s_virgin_advected: float
    gate_2a: bool
    gate_integral: bool


@dataclass(frozen=True)
class CoreResult:
    gate_3a: bool
    first_five_layers_t40: int
    first_five_layers_t80: int
    first_move_layer_times: tuple[int, ...]


@dataclass(frozen=True)
class PocketResult:
    frozen_sites: int
    thaw_fraction: float
    filled_fraction: float
    first_thaw_time: float
    post_duration: float


def fmt_float(value: float, digits: int = 3) -> str:
    if math.isnan(value):
        return "nan"
    if math.isinf(value):
        return "inf" if value > 0.0 else "-inf"
    return f"{value:.{digits}f}"


def ring_distance(a: np.ndarray, b: np.ndarray, length: int) -> np.ndarray:
    diff = np.abs(a - b)
    return np.minimum(diff, length - diff)


def neighbor_count(recorded: np.ndarray) -> np.ndarray:
    as_int = recorded.astype(np.int8)
    return np.roll(as_int, 1) + np.roll(as_int, -1)


def formation_rates(recorded: np.ndarray, boosts: np.ndarray | float = 1.0) -> np.ndarray:
    rates = np.asarray(boosts, dtype=float) * RATE_BY_NEIGHBORS[neighbor_count(recorded)]
    rates = rates.astype(float, copy=True)
    rates[recorded] = 0.0
    return rates


def choose_weighted_index(rates: np.ndarray, draw01: float) -> int:
    total = float(rates.sum())
    if total <= 0.0:
        raise RuntimeError("cannot choose from zero rates")
    cumulative = np.cumsum(rates)
    idx = int(np.searchsorted(cumulative, draw01 * total, side="right"))
    if idx >= rates.size:
        idx = rates.size - 1
    if rates[idx] <= 0.0:
        raise RuntimeError("selected zero-rate event")
    return idx


def generate_anchor_history() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    rng = np.random.default_rng(SEED + 11)
    times = np.arange(ANCHOR_K, dtype=float)
    source_mask = np.ones(ANCHOR_K, dtype=bool)
    background_idx = np.linspace(
        23, ANCHOR_K - 24, ANCHOR_BACKGROUND_COUNT, dtype=int
    )
    source_mask[np.unique(background_idx)] = False

    center = np.floor(ANCHOR_U * times).astype(int) % ANCHOR_L
    jitter = rng.integers(0, 2, size=ANCHOR_K)
    positions = (center + jitter) % ANCHOR_L
    background_jitter = rng.integers(0, 2, size=(~source_mask).sum())
    positions[~source_mask] = (center[~source_mask] + background_jitter) % ANCHOR_L
    return times, positions.astype(int), source_mask


def causal_consistency(
    times: np.ndarray,
    positions: np.ndarray,
    source_mask: np.ndarray,
    *,
    cross_subset_only: bool = False,
) -> float:
    compatible = 0
    total = 0
    for i in range(times.size - 1):
        j_stop = min(times.size, i + ANCHOR_HORIZON + 1)
        if j_stop <= i + 1:
            continue
        js = np.arange(i + 1, j_stop)
        if cross_subset_only:
            js = js[source_mask[js] != source_mask[i]]
            if js.size == 0:
                continue
        dt = times[js] - times[i]
        dist = ring_distance(positions[js], np.full(js.size, positions[i]), ANCHOR_L)
        compatible += int(np.count_nonzero(dist <= ANCHOR_VMAX * dt + 1.0 + EPS))
        total += int(js.size)
    if total <= 0:
        return math.nan
    return compatible / total


def diffuse_anchor_positions(
    initial_positions: np.ndarray,
    times: np.ndarray,
    source_mask: np.ndarray,
) -> tuple[tuple[int, ...], tuple[float, ...], str]:
    rng = np.random.default_rng(SEED + 12)
    positions = initial_positions.copy()
    sample_steps = (0, 50, 100, 150, 200)
    curve: list[float] = []
    half_life: str | None = None
    c0 = causal_consistency(times, initial_positions, source_mask)

    for step in range(ANCHOR_MOTION_STEPS + 1):
        if step in sample_steps:
            c_now = causal_consistency(times, positions, source_mask)
            curve.append(c_now)
            if half_life is None and c_now <= 0.5 * c0:
                half_life = str(step)
        if step == ANCHOR_MOTION_STEPS:
            break
        movers = rng.random(positions.size) < ANCHOR_DIFFUSION_RATE
        directions = np.where(rng.random(positions.size) < 0.5, -1, 1)
        positions[movers] = (positions[movers] + directions[movers]) % ANCHOR_L

    if half_life is None:
        half_life = f">{ANCHOR_MOTION_STEPS}"
    return sample_steps, tuple(curve), half_life


def run_anchoring() -> AnchoringResult:
    times, positions, source_mask = generate_anchor_history()
    c0 = causal_consistency(times, positions, source_mask)

    advected = positions.copy()
    source_displacement = int(round(ANCHOR_U * ANCHOR_MOTION_STEPS)) % ANCHOR_L
    advected[source_mask] = (advected[source_mask] + source_displacement) % ANCHOR_L
    c_advected = causal_consistency(times, advected, source_mask)
    cross_advected = causal_consistency(
        times, advected, source_mask, cross_subset_only=True
    )

    steps, curve, half_life = diffuse_anchor_positions(positions, times, source_mask)
    return AnchoringResult(
        c0=c0,
        c_advected=c_advected,
        cross_advected=cross_advected,
        diffusion_steps=steps,
        diffusion_curve=curve,
        diffusion_half_life=half_life,
        gate_1a=bool(c_advected >= 0.95 * c0),
    )


def zone_start(t_zone: float, speed: float, length: int) -> int:
    return int(math.floor(speed * t_zone + 1.0e-12)) % length


def next_zone_boundary(t_zone: float, speed: float, duration: float) -> float:
    boundary = (math.floor(speed * t_zone + 1.0e-12) + 1.0) / speed
    if boundary <= t_zone + 1.0e-12:
        boundary += 1.0 / speed
    return min(boundary, duration)


def wake_zone_rates(permanent: np.ndarray, t_zone: float) -> np.ndarray:
    start = zone_start(t_zone, WAKE_V, WAKE_L)
    offsets = (np.arange(WAKE_L, dtype=int) - start) % WAKE_L
    boosts = np.zeros(WAKE_L, dtype=float)
    boosts[offsets < WAKE_WIDTH] = WAKE_BOOST
    return formation_rates(permanent, boosts)


def run_wake_transit() -> np.ndarray:
    rng = np.random.default_rng(SEED + 21)
    permanent = np.zeros(WAKE_L, dtype=bool)
    duration = (WAKE_L * WAKE_TRANSIT_FRACTION) / WAKE_V
    t = 0.0
    while t < duration - 1.0e-12:
        rates = wake_zone_rates(permanent, t)
        total = float(rates.sum())
        boundary = next_zone_boundary(t, WAKE_V, duration)
        if total <= 0.0:
            t = boundary
            continue
        dt_event = float(rng.exponential(1.0 / total))
        dt = min(dt_event, boundary - t, duration - t)
        if dt < -1.0e-12:
            raise RuntimeError("negative wake transit time step")
        t += max(0.0, dt)
        if dt_event > dt + 1.0e-12 or t >= duration - 1.0e-12:
            continue
        idx = choose_weighted_index(rates, float(rng.random()))
        if permanent[idx]:
            raise RuntimeError("wake transit selected occupied site")
        permanent[idx] = True
    return permanent


def site_records_from_occupancy(occupied: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    sites = np.flatnonzero(occupied)
    site_record = np.full(occupied.size, -1, dtype=int)
    record_pos = sites.astype(int).copy()
    site_record[sites] = np.arange(sites.size, dtype=int)
    return site_record, record_pos


def occupancy_from_site_records(site_record: np.ndarray) -> np.ndarray:
    return site_record >= 0


def advect_records(initial: np.ndarray) -> np.ndarray:
    site_record, record_pos = site_records_from_occupancy(initial)
    steps = int(round((WAKE_L * WAKE_TRANSIT_FRACTION) / WAKE_V))
    for _ in range(steps):
        occupied_start = site_record >= 0
        movers: list[tuple[int, int, int]] = []
        for rid, pos in enumerate(record_pos):
            target = (int(pos) + 1) % WAKE_L
            if not occupied_start[target]:
                movers.append((rid, int(pos), target))
        for rid, old, target in movers:
            if site_record[old] != rid or site_record[target] != -1:
                continue
            site_record[old] = -1
            site_record[target] = rid
            record_pos[rid] = target
    return occupancy_from_site_records(site_record)


def diffuse_records_discrete(
    initial: np.ndarray,
    *,
    length: int,
    steps: int,
    rate: float,
    seed: int,
) -> np.ndarray:
    rng = np.random.default_rng(seed)
    site_record, record_pos = site_records_from_occupancy(initial)
    for _ in range(steps):
        for rid in rng.permutation(record_pos.size):
            if rng.random() >= rate:
                continue
            old = int(record_pos[rid])
            target = (old + (-1 if rng.random() < 0.5 else 1)) % length
            if site_record[target] != -1:
                continue
            site_record[old] = -1
            site_record[target] = rid
            record_pos[rid] = target
    return occupancy_from_site_records(site_record)


def probe_clock_field(permanent: np.ndarray) -> np.ndarray:
    rates = RATE_BY_NEIGHBORS[neighbor_count(permanent)].copy()
    rates[permanent] = 0.0
    return rates / RATE_BY_NEIGHBORS[0]


def suppression_on_mask(permanent: np.ndarray, mask: np.ndarray) -> float:
    if not bool(mask.any()):
        return math.nan
    return float((1.0 - probe_clock_field(permanent)[mask]).mean())


def suppression_width(permanent: np.ndarray) -> int:
    return int(np.count_nonzero(1.0 - probe_clock_field(permanent) > 0.1))


def run_wake_motion() -> WakeMotionResult:
    frozen = run_wake_transit()
    original_trail = frozen.copy()
    if not bool(original_trail.any()):
        raise RuntimeError("wake transit deposited no records")

    advected = advect_records(frozen)
    diffused = diffuse_records_discrete(
        frozen,
        length=WAKE_L,
        steps=int(round(WAKE_L / WAKE_V)),
        rate=WAKE_DIFFUSION_RATE,
        seed=SEED + 22,
    )

    half = int(WAKE_L * WAKE_TRANSIT_FRACTION)
    path_mask = np.zeros(WAKE_L, dtype=bool)
    path_mask[:half] = True
    virgin_mask = ~path_mask
    density_frozen = float(frozen[path_mask].mean())
    density_advected = float(advected[path_mask].mean())
    density_diffused = float(diffused[path_mask].mean())
    s_frozen = suppression_on_mask(frozen, path_mask)
    s_advected = suppression_on_mask(advected, path_mask)
    s_diffused = suppression_on_mask(diffused, path_mask)
    s_virgin_frozen = suppression_on_mask(frozen, virgin_mask)
    s_virgin_advected = suppression_on_mask(advected, virgin_mask)

    crowd0 = float(frozen.sum())
    if crowd0 <= 0.0:
        raise RuntimeError("zero wake crowding")
    integrated_crowding_ratio_advected = float(advected.sum() / crowd0)
    integrated_crowding_ratio_diffused = float(diffused.sum() / crowd0)
    clock0 = float((1.0 - probe_clock_field(frozen)).sum())
    clock_diffused = float((1.0 - probe_clock_field(diffused)).sum())
    integrated_clock_ratio_diffused = clock_diffused / clock0 if clock0 > 0.0 else math.nan
    gate_integral = bool(
        abs(integrated_crowding_ratio_advected - 1.0) <= 0.05
        and abs(integrated_crowding_ratio_diffused - 1.0) <= 0.05
    )

    return WakeMotionResult(
        density_frozen=density_frozen,
        density_advected=density_advected,
        density_diffused=density_diffused,
        s_frozen=s_frozen,
        s_advected=s_advected,
        s_diffused=s_diffused,
        width_frozen=suppression_width(frozen),
        width_advected=suppression_width(advected),
        width_diffused=suppression_width(diffused),
        integrated_crowding_ratio_advected=integrated_crowding_ratio_advected,
        integrated_crowding_ratio_diffused=integrated_crowding_ratio_diffused,
        integrated_clock_ratio_diffused=integrated_clock_ratio_diffused,
        s_virgin_frozen=s_virgin_frozen,
        s_virgin_advected=s_virgin_advected,
        # Relocation balance: suppression lost by the path matches the
        # suppression gained by the virgin half (zone-width overhang and
        # ring wrap make absolute thresholds mask-dependent; the balance
        # is the geometry-free statement), plus a majority-left condition.
        gate_2a=bool(
            s_advected < 0.5 * s_frozen
            and (s_virgin_advected - s_virgin_frozen) > 0.0
            and 0.7
            <= (s_frozen - s_advected)
            / max(s_virgin_advected - s_virgin_frozen, 1.0e-12)
            <= 1.3
        ),
        gate_integral=gate_integral,
    )


def make_core(block_size: int) -> tuple[np.ndarray, np.ndarray]:
    length = max(4 * block_size, 200)
    occupied = np.zeros(length, dtype=bool)
    start = (length - block_size) // 2
    occupied[start : start + block_size] = True
    layers = np.full(length, -1, dtype=int)
    for offset in range(block_size):
        layers[start + offset] = min(offset, block_size - 1 - offset)
    return occupied, layers


def simulate_core(block_size: int, seed: int) -> tuple[bool, int, tuple[int, ...]]:
    rng = np.random.default_rng(seed)
    occupied, site_layers = make_core(block_size)
    length = occupied.size
    site_record, record_pos = site_records_from_occupancy(occupied)
    initial_layers = site_layers[record_pos].copy()
    first_move_time = np.full(record_pos.size, -1, dtype=int)
    first_vacancy_time = np.full(length, -1, dtype=int)
    layer_move_times = np.full(CORE_LOSS_LAYERS + 2, -1, dtype=int)
    gate_ok = True

    layer_loss_mask = (site_layers >= 0) & (site_layers < CORE_LOSS_LAYERS)
    first_five_layers_time = -1

    for step in range(1, CORE_MAX_STEPS + 1):
        for rid in rng.permutation(record_pos.size):
            if rng.random() >= CORE_DIFFUSION_RATE:
                continue
            old = int(record_pos[rid])
            target = (old + (-1 if rng.random() < 0.5 else 1)) % length
            if site_record[target] != -1:
                continue
            was_boundary = site_record[(old - 1) % length] == -1 or site_record[
                (old + 1) % length
            ] == -1
            if initial_layers[rid] > 1 and first_move_time[rid] < 0 and not was_boundary:
                gate_ok = False
            site_record[old] = -1
            site_record[target] = rid
            record_pos[rid] = target
            if first_move_time[rid] < 0:
                first_move_time[rid] = step
                layer = int(initial_layers[rid])
                if 0 <= layer < layer_move_times.size and layer_move_times[layer] < 0:
                    layer_move_times[layer] = step
            if site_layers[old] >= 0 and first_vacancy_time[old] < 0:
                first_vacancy_time[old] = step

        if first_five_layers_time < 0 and np.all(first_vacancy_time[layer_loss_mask] >= 0):
            first_five_layers_time = step
            break

    if first_five_layers_time < 0:
        raise RuntimeError(f"core size {block_size} did not lose five layers")
    known_layer_times = layer_move_times[: CORE_LOSS_LAYERS]
    if np.any(known_layer_times < 0):
        gate_ok = False
    else:
        gate_ok = gate_ok and bool(np.all(np.diff(known_layer_times) >= 0))
    return gate_ok, first_five_layers_time, tuple(int(x) for x in known_layer_times)


def run_core() -> CoreResult:
    gate40, t40, layer_times40 = simulate_core(40, SEED + 31)
    gate80, t80, _ = simulate_core(80, SEED + 32)
    return CoreResult(
        gate_3a=bool(gate40 and gate80),
        first_five_layers_t40=t40,
        first_five_layers_t80=t80,
        first_move_layer_times=layer_times40,
    )


def run_formation_to_termination(seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    recorded = rng.random(POCKET_L) < POCKET_SEED_FRACTION
    while True:
        rates = formation_rates(recorded)
        total = float(rates.sum())
        if total <= 0.0:
            return recorded
        idx = choose_weighted_index(rates, float(rng.random()))
        recorded[idx] = True


def run_pockets() -> PocketResult:
    rng = np.random.default_rng(SEED + 41)
    recorded = run_formation_to_termination(SEED + 40)
    frozen_sites = (~recorded) & (neighbor_count(recorded) == 2)
    frozen_count = int(frozen_sites.sum())
    if frozen_count <= 0:
        raise RuntimeError("horizon-class termination produced no frozen pockets")

    site_record, record_pos = site_records_from_occupancy(recorded)
    thawed_by_formation = np.zeros(POCKET_L, dtype=bool)
    ever_filled = recorded.copy()
    t = 0.0
    first_thaw = math.inf

    while t < POCKET_POST_DURATION - 1.0e-12:
        occupied = occupancy_from_site_records(site_record)
        form_rates = formation_rates(occupied)

        move_events: list[tuple[int, int, int, float]] = []
        for rid, pos_raw in enumerate(record_pos):
            pos = int(pos_raw)
            for direction in (-1, 1):
                target = (pos + direction) % POCKET_L
                if site_record[target] == -1:
                    move_events.append(
                        (rid, pos, target, 0.5 * POCKET_DIFFUSION_RATE)
                    )

        total_form = float(form_rates.sum())
        total_move = float(sum(event[3] for event in move_events))
        total = total_form + total_move
        if total <= 0.0:
            break
        dt = float(rng.exponential(1.0 / total))
        if t + dt > POCKET_POST_DURATION:
            break
        t += dt
        draw = float(rng.random() * total)
        if draw < total_form:
            idx = choose_weighted_index(form_rates, draw / total_form)
            if site_record[idx] != -1:
                raise RuntimeError("pocket formation selected occupied site")
            rid = record_pos.size
            record_pos = np.append(record_pos, idx)
            site_record[idx] = rid
            ever_filled[idx] = True
            if frozen_sites[idx] and not thawed_by_formation[idx]:
                thawed_by_formation[idx] = True
                first_thaw = min(first_thaw, t)
        else:
            move_draw = draw - total_form
            cumulative = 0.0
            selected: tuple[int, int, int, float] | None = None
            for event in move_events:
                cumulative += event[3]
                if move_draw <= cumulative + EPS:
                    selected = event
                    break
            if selected is None:
                selected = move_events[-1]
            rid, old, target, _ = selected
            if site_record[old] != rid or site_record[target] != -1:
                continue
            site_record[old] = -1
            site_record[target] = rid
            record_pos[rid] = target
            ever_filled[target] = True

        if int(np.count_nonzero(thawed_by_formation & frozen_sites)) == frozen_count:
            break

    thawed = int(np.count_nonzero(thawed_by_formation & frozen_sites))
    filled = int(np.count_nonzero(ever_filled & frozen_sites))
    return PocketResult(
        frozen_sites=frozen_count,
        thaw_fraction=thawed / frozen_count,
        filled_fraction=filled / frozen_count,
        first_thaw_time=first_thaw,
        post_duration=POCKET_POST_DURATION,
    )


def format_anchoring(result: AnchoringResult) -> str:
    curve = ",".join(fmt_float(v, 3) for v in result.diffusion_curve)
    steps = ",".join(str(s) for s in result.diffusion_steps)
    return (
        "ANCHORING: "
        f"C0={fmt_float(result.c0, 4)} "
        f"C_adv={fmt_float(result.c_advected, 4)} gate1A={result.gate_1a} "
        f"cross_adv={fmt_float(result.cross_advected, 4)} "
        f"Cdiff[{steps}]={curve} half_life={result.diffusion_half_life}"
    )


def format_wake(result: WakeMotionResult) -> str:
    return (
        "WAKE-MOTION: "
        f"S0={fmt_float(result.s_frozen, 4)} "
        f"SA={fmt_float(result.s_advected, 4)} "
        f"SB={fmt_float(result.s_diffused, 4)} "
        f"Svirgin0={fmt_float(result.s_virgin_frozen, 4)} "
        f"SvirginA={fmt_float(result.s_virgin_advected, 4)} gate2A={result.gate_2a} "
        f"dens0/A/B={fmt_float(result.density_frozen, 3)}/"
        f"{fmt_float(result.density_advected, 3)}/{fmt_float(result.density_diffused, 3)} "
        f"width0/A/B={result.width_frozen}/{result.width_advected}/{result.width_diffused} "
        f"IcrowdA/B={fmt_float(result.integrated_crowding_ratio_advected, 3)}/"
        f"{fmt_float(result.integrated_crowding_ratio_diffused, 3)} "
        f"IclockB={fmt_float(result.integrated_clock_ratio_diffused, 3)} "
        f"gateI={result.gate_integral}"
    )


def format_core(result: CoreResult) -> str:
    layer_times = ",".join(str(v) for v in result.first_move_layer_times)
    return (
        "CORE: "
        f"gate3A={result.gate_3a} "
        f"first5layers_t40={result.first_five_layers_t40} "
        f"first5layers_t80={result.first_five_layers_t80} "
        f"first_move_layer_t0..4={layer_times}"
    )


def format_pockets(result: PocketResult) -> str:
    first = (
        f"{result.first_thaw_time:.3f}"
        if math.isfinite(result.first_thaw_time)
        else "none"
    )
    return (
        "POCKETS: "
        f"frozen={result.frozen_sites} "
        f"thaw_form_frac={fmt_float(result.thaw_fraction, 3)} "
        f"filled_frac={fmt_float(result.filled_fraction, 3)} "
        f"t_first_thaw={first} postT={fmt_float(result.post_duration, 1)}"
    )


def run_all() -> tuple[str, ...]:
    anchoring = run_anchoring()
    wake = run_wake_motion()
    core = run_core()
    pockets = run_pockets()

    geometry_flag = "preserved-under-advection" if anchoring.gate_1a else "degraded"
    wake_flag = "relocates-with-source" if wake.gate_2a else "persists-on-path"
    core_flag = "exclusion-frozen-boundary-peeling" if core.gate_3a else "mobile"
    pocket_flag = "thaw" if pockets.thaw_fraction > 0.0 else "survive"
    machinery_ok = bool(core.gate_3a and wake.gate_integral)
    machinery = "ok" if machinery_ok else "MACHINERY-FAIL"

    checks_line = (
        "CHECKS: "
        f"machinery={machinery} "
        f"K_gt_L_part1={ANCHOR_K}>{ANCHOR_L} "
        f"wake_integral_5pct={wake.gate_integral} "
        f"core_layer_assert={core.gate_3a} "
        f"stdout_lines=7"
    )
    total_line = (
        "TOTAL: "
        f"GEOMETRY-ANCHORING={geometry_flag}, "
        f"WAKE-UNDER-ADVECTION={wake_flag}, "
        f"SATURATED-CORE={core_flag}, "
        f"FROZEN-POCKETS={pocket_flag}"
        + ("" if machinery_ok else ", MACHINERY-FAIL")
    )
    spec_line = (
        "SPEC-NOTE: "
        "Part1 source-tagging is declared and cross-subset damage is separate; "
        "Part1 K=400>L=200 makes literal one-per-site diffusion impossible, so "
        "its diffusion curve is an abstract position stress test; blocked "
        "advection uses synchronous occupied-at-step-start waiting; probe "
        "readouts are counted-not-committed clocks, while Icrowd gates record "
        "count conservation."
    )
    return (
        format_anchoring(anchoring),
        format_wake(wake),
        format_core(core),
        format_pockets(pockets),
        checks_line,
        total_line,
        spec_line,
    )


def main() -> int:
    try:
        for line in run_all():
            print(line)
        return 0
    except Exception as exc:  # noqa: BLE001 - required fail-closed token.
        print(f"TOTAL: MACHINERY-FAIL {type(exc).__name__}: {exc}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
