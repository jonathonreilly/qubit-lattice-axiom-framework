#!/usr/bin/env python3
"""Block03: two-star merger in the coupled toy.

The clock well is short-ranged (nearest-neighbor availability), so distant
husks cannot attract each other and records never move: if merger happens at
all it must happen by BRIDGING -- the between-region ossifies until the husks
connect.  Declared comparator; no derivation; no audit status.  Companion
note: MERGER_BY_BRIDGING_BOUNDED_NOTE_2026-07-08.md.

This runner dynamically imports the read-only Block01 engine and Block02
frozen-star runner.  It uses the engine state/hop/deposition/displacement
primitives and the frozen-star periodic component and graph-distance
conventions.

Husk identity over time is anchored, not reselected: each star's husk is the
connected component containing that star's density peak, from the step the
peak first records, and is then tracked by containment continuity.  Records
are permanent, so components only merge and never split, which makes this
identity exact (a superset assertion is enforced every step).  The Block02
cardinality-first selector is a per-snapshot anatomy device; rerun every step
for identity it flickers between fragments early and aliases both stars onto
one component late (measured in the first draft of this runner), so it is not
used for identity here.

The engine's deposition input is a rate.  Formation is sampled with its
Poisson conversion ``1 - exp(-kappa * n * (A/A0) * dt)``; it is not clipped
or silently substepped here.  The native simultaneous-hop, blocked-hop,
nearest-open displacement, seeded tie split, and last-open-refuge conventions
are retained unchanged.
"""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import importlib.util
import json
from pathlib import Path
import struct
import sys
import time
from typing import Any

sys.dont_write_bytecode = True

import numpy as np


THIS_FILE = Path(__file__).resolve()
ENGINE_PATH = THIS_FILE.with_name("collapse_merger_toy_engine_2026_07_08.py")
FROZEN_PATH = THIS_FILE.with_name("collapse_frozen_star_2026_07_08.py")
NOTE_NAME = "MERGER_BY_BRIDGING_BOUNDED_NOTE_2026-07-08.md"

L = 400
BETA = 0.6
DT = 1.0
SEED = 20260708
CENTERS = (170, 230)
N_PER_BLOB = 150
N_PARCELS = 2 * N_PER_BLOB
INITIAL_SIGMA = 8.0
INITIAL_BLOB_RADIUS = 24  # fixed three-sigma arc
KAPPA = 0.001
T_STEPS = 6000
MARKERS = (40, 360)
OUTER_FLANK_BUFFER = 20
FAR_HUSK_DISTANCE = 30
EXTERIOR_OPEN_GATE = 0.30
MEMORY_FILL_MAX = 0.30


def load_module(path: Path, name: str) -> Any:
    """Dynamically load a named read-only sibling without package assumptions."""

    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import module from {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


engine = load_module(
    ENGINE_PATH, "collapse_merger_toy_engine_for_merger_bridging_20260708"
)
frozen = load_module(
    FROZEN_PATH, "collapse_frozen_star_for_merger_bridging_20260708"
)


def assert_imported_conventions() -> None:
    expected = {"L": L, "BETA": BETA, "DT": DT, "SEED": SEED}
    for label, module in (("engine", engine), ("frozen-star", frozen)):
        observed = {name: getattr(module, name) for name in expected}
        if observed != expected:
            raise AssertionError(
                f"{label} convention drift: expected={expected}, observed={observed}"
            )
    if engine.EngineState.__module__ != engine.__name__:
        raise AssertionError("engine state was not loaded from the named module")
    if frozen.connected_record_components.__module__ != frozen.__name__:
        raise AssertionError("component convention was not loaded from Block02")

    # Pin the user-requested Poisson interpretation against the imported
    # implementation rather than merely trusting a similarly named helper.
    records = np.zeros(L, dtype=np.bool_)
    parcels = np.zeros(L, dtype=np.int64)
    parcels[17] = 7
    probe = engine.EngineState(records=records, parcels=parcels)
    observed_probability = float(engine.deposition_probabilities(probe, KAPPA, DT)[17])
    rate = KAPPA * 7.0 * float(engine.availability_field(records)[17]) / float(engine.A0)
    expected_probability = float(-np.expm1(-rate * DT))
    if observed_probability != expected_probability:
        raise AssertionError("engine deposition is not the required Poisson form")


@dataclass(frozen=True)
class InitialBlobs:
    parcels: np.ndarray
    peaks: tuple[int, int]
    component_parcels: tuple[np.ndarray, np.ndarray]


@dataclass(frozen=True)
class Trajectory:
    initial: InitialBlobs
    records: np.ndarray
    parcels: np.ndarray
    husks: np.ndarray
    junction_recorded: np.ndarray
    junction_size: np.ndarray
    junction_complete: np.ndarray
    boundaries: np.ndarray
    exterior_open_fraction: np.ndarray
    outward_flux: np.ndarray
    net_outward_flux: np.ndarray
    both_husks_step: int | None
    selection_merge_step: int | None
    bridge_step: int | None
    digest: str


@dataclass(frozen=True)
class BridgeCheck:
    bridge_step: int | None
    left_pre_mass: int
    right_pre_mass: int
    merged_mass: int
    junction_recorded: int
    junction_size: int
    left_flank_open: float
    right_flank_open: float
    prebridge_distinct: bool
    channel_ok: bool
    area_ok: bool

    @property
    def bridge_ok(self) -> bool:
        return (
            self.bridge_step is not None
            and self.bridge_step <= T_STEPS
            and self.channel_ok
        )


@dataclass(frozen=True)
class HuskPermanenceCheck:
    ok: bool
    first_step: int | None
    star: int | None
    lost_sites: int


@dataclass(frozen=True)
class MemoryCheck:
    far_mask: np.ndarray
    left_fill: float
    right_fill: float
    fill: float
    adjacent_sites: int
    adjacent_clock: float
    clock_suppression: float
    flux_before: int
    flux_during: int
    flux_after: int
    net_flux_before: int
    net_flux_during: int
    net_flux_after: int
    records_permanent: bool
    status: str

    @property
    def gate_ok(self) -> bool | None:
        if self.status == "MEMORY-NOT-EXHIBITED":
            return None
        return self.status == "PASS"


def circular_offsets(center: int) -> np.ndarray:
    """Use Block02's minimum-image site convention."""

    return frozen.circular_offsets(center)


def fixed_blob_mask(center: int) -> np.ndarray:
    return np.abs(circular_offsets(center)) <= INITIAL_BLOB_RADIUS


def draw_initial_blobs(rng: np.random.Generator) -> InitialBlobs:
    """Draw the two rounded Gaussian parcel clouds from one continuing stream."""

    component_fields: list[np.ndarray] = []
    peaks: list[int] = []
    for center in CENTERS:
        positions = np.rint(
            rng.normal(loc=center, scale=INITIAL_SIGMA, size=N_PER_BLOB)
        ).astype(np.int64) % L
        field = np.bincount(positions, minlength=L).astype(np.int64, copy=False)
        maximum = int(field.max())
        candidates = np.flatnonzero(field == maximum)
        offsets = np.abs(circular_offsets(center)[candidates])
        # Block02 tie convention for the empirical peak: closest to the named
        # Gaussian centre, then lowest site label.
        peak = int(candidates[np.lexsort((candidates, offsets))[0]])
        component_fields.append(field)
        peaks.append(peak)
    parcels = component_fields[0] + component_fields[1]
    if int(parcels.sum()) != N_PARCELS:
        raise AssertionError("initial two-blob draw lost parcels")
    return InitialBlobs(
        parcels=parcels,
        peaks=(peaks[0], peaks[1]),
        component_parcels=(component_fields[0], component_fields[1]),
    )


def component_labels(records: np.ndarray) -> np.ndarray:
    """Label every recorded site with its periodic component index (-1 open)."""

    labels = np.full(L, -1, dtype=np.int64)
    for label, component in enumerate(frozen.connected_record_components(records)):
        labels[component] = label
    return labels


def component_extent(mask: np.ndarray, center: int) -> tuple[int, int]:
    """Return the component's outward/facing endpoints on the stars' fixed axis."""

    sites = np.flatnonzero(mask)
    if sites.size == 0:
        raise ValueError("an empty husk has no endpoints")
    offsets = circular_offsets(center)[sites]
    unwrapped = center + offsets
    return int(unwrapped.min()), int(unwrapped.max())


def premerger_boundaries(left: np.ndarray, right: np.ndarray) -> np.ndarray:
    """Return [left outer, left facing, right facing, right outer]."""

    left_outer, left_facing = component_extent(left, CENTERS[0])
    right_facing, right_outer = component_extent(right, CENTERS[1])
    return np.asarray(
        (left_outer, left_facing, right_facing, right_outer), dtype=np.int64
    )


def junction_sites(boundaries: np.ndarray) -> np.ndarray:
    """Sites strictly between the two facing endpoints on the short central arc."""

    left_facing = int(boundaries[1])
    right_facing = int(boundaries[2])
    separation = right_facing - left_facing
    if separation <= 0 or separation >= L:
        return np.empty(0, dtype=np.int64)
    return np.arange(left_facing + 1, right_facing, dtype=np.int64) % L


def default_junction_boundaries() -> np.ndarray:
    return np.asarray(
        (
            CENTERS[0] - INITIAL_BLOB_RADIUS,
            CENTERS[0] + INITIAL_BLOB_RADIUS,
            CENTERS[1] - INITIAL_BLOB_RADIUS,
            CENTERS[1] + INITIAL_BLOB_RADIUS,
        ),
        dtype=np.int64,
    )


def tracked_engine_step(
    state: Any, rng: np.random.Generator
) -> tuple[Any, np.ndarray, np.ndarray]:
    """Execute the native engine step while exposing accepted marker currents.

    Block01's ``engine_step`` does not return its internal ``HopStats``.  This
    is its operation order verbatim through exposed helpers: simultaneous hop,
    Poisson deposition draw, terminal-refuge guard, nearest-open displacement,
    step increment, permanence check, and state validation.  No rule is added
    or repaired here.
    """

    records_before = state.records.copy()
    hops = engine.hop_parcels(state, rng, beta=BETA, hops_enabled=True)
    probabilities = engine.deposition_probabilities(state, KAPPA, DT)
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
        engine.displace_formed_site_parcels(
            state.parcels, formed, records_after, rng
        )
        state.records = records_after
    state.step += 1
    if np.any(records_before & ~state.records):
        raise AssertionError("permanent record field decreased inside engine step")
    engine.validate_state(state, N_PARCELS)
    return hops, formed, probabilities


def marker_flux(hops: Any) -> tuple[int, int]:
    """Gross and net outward crossings on the bonds just beyond sites 40/360."""

    left, right = MARKERS
    gross = int(hops.accepted_left[left] + hops.accepted_right[right])
    inward = int(
        hops.accepted_right[(left - 1) % L]
        + hops.accepted_left[(right + 1) % L]
    )
    return gross, gross - inward


def update_digest_array(digest: Any, array: np.ndarray, dtype: str | None = None) -> None:
    canonical = array.astype(dtype, copy=False) if dtype is not None else array
    digest.update(canonical.tobytes())


def run_trajectory(seed: int = SEED) -> Trajectory:
    """Run once, retaining every field requested by the protocol."""

    rng = np.random.default_rng(seed)
    initial = draw_initial_blobs(rng)
    state = engine.EngineState(
        records=np.zeros(L, dtype=np.bool_), parcels=initial.parcels.copy()
    )
    engine.validate_state(state, N_PARCELS)

    records = np.zeros((T_STEPS + 1, L), dtype=np.bool_)
    parcels = np.zeros((T_STEPS + 1, L), dtype=np.int64)
    husks = np.zeros((T_STEPS + 1, 2, L), dtype=np.bool_)
    junction_recorded = np.zeros(T_STEPS + 1, dtype=np.int64)
    junction_size = np.zeros(T_STEPS + 1, dtype=np.int64)
    junction_complete = np.zeros(T_STEPS + 1, dtype=np.bool_)
    boundaries = np.full((T_STEPS + 1, 4), -1, dtype=np.int64)
    exterior_open_fraction = np.zeros(T_STEPS + 1, dtype=np.float64)
    outward_flux = np.zeros(T_STEPS + 1, dtype=np.int64)
    net_outward_flux = np.zeros(T_STEPS + 1, dtype=np.int64)

    fixed_arcs = fixed_blob_mask(CENTERS[0]) | fixed_blob_mask(CENTERS[1])
    exterior = ~fixed_arcs
    exterior_size = int(exterior.sum())
    if exterior_size == 0:
        raise AssertionError("fixed blob arcs leave no exterior")

    both_husks_step: int | None = None
    selection_merge_step: int | None = None
    bridge_step: int | None = None
    last_distinct_boundaries: np.ndarray | None = None
    husk_state = [np.zeros(L, dtype=np.bool_), np.zeros(L, dtype=np.bool_)]
    anchored = [False, False]
    digest = hashlib.sha256()
    digest.update(
        struct.pack(">qdddqq", seed, KAPPA, BETA, DT, T_STEPS, N_PARCELS)
    )
    update_digest_array(digest, initial.parcels, ">i8")
    digest.update(struct.pack(">qq", *initial.peaks))

    previous_records = state.records.copy()
    def snapshot(index: int, step_outward: int, step_net_outward: int) -> None:
        nonlocal both_husks_step
        nonlocal bridge_step
        nonlocal last_distinct_boundaries
        nonlocal selection_merge_step
        nonlocal previous_records

        if state.step != index:
            raise AssertionError(f"engine/history step mismatch: {state.step} != {index}")
        engine.validate_state(state, N_PARCELS)

        # CHECK-03 exact assertion: the full record count and site set never
        # decrease.  Site-set permanence is stronger than count monotonicity.
        if np.any(previous_records & ~state.records):
            raise AssertionError(f"record permanence failed at step {index}")
        if int(state.records.sum()) < int(previous_records.sum()):
            raise AssertionError(f"record count decreased at step {index}")

        labels = component_labels(state.records)
        husk_list: list[np.ndarray] = []
        for star in range(2):
            if not anchored[star]:
                peak_label = int(labels[initial.peaks[star]])
                if peak_label < 0:
                    selected = np.zeros(L, dtype=np.bool_)
                else:
                    selected = labels == peak_label
                    if selected[initial.peaks[1 - star]] and not anchored[1 - star]:
                        raise AssertionError(
                            "a star anchored onto a component already containing "
                            "the other star's unanchored peak (engulfment regime)"
                        )
                    anchored[star] = True
            else:
                anchor_site = int(np.flatnonzero(husk_state[star])[0])
                selected = labels == labels[anchor_site]
                if np.any(husk_state[star] & ~selected):
                    raise AssertionError(
                        f"anchored husk lost a site at step {index} "
                        "(record permanence/continuity violated)"
                    )
            husk_list.append(selected)
            husk_state[star] = selected
        current_husks = np.stack(husk_list)
        current_merged = bool(
            current_husks[0].any()
            and np.array_equal(current_husks[0], current_husks[1])
        )

        both_present = bool(current_husks[0].any() and current_husks[1].any())
        if both_present and both_husks_step is None:
            both_husks_step = index
        if both_present and not current_merged:
            last_distinct_boundaries = premerger_boundaries(
                current_husks[0], current_husks[1]
            )
        if current_merged and selection_merge_step is None:
            selection_merge_step = index
        if (
            bridge_step is None
            and current_merged
            and bool(current_husks[0][initial.peaks[0]])
            and bool(current_husks[0][initial.peaks[1]])
        ):
            bridge_step = index

        active_boundaries = (
            last_distinct_boundaries
            if last_distinct_boundaries is not None
            else default_junction_boundaries()
        )
        junction = junction_sites(active_boundaries)
        recorded_in_junction = int(state.records[junction].sum())

        records[index] = state.records
        parcels[index] = state.parcels
        husks[index] = current_husks
        boundaries[index] = active_boundaries
        junction_recorded[index] = recorded_in_junction
        junction_size[index] = int(junction.size)
        junction_complete[index] = bool(
            junction.size > 0 and recorded_in_junction == junction.size
        )
        exterior_open_fraction[index] = float((~state.records & exterior).sum()) / float(
            exterior_size
        )
        outward_flux[index] = step_outward
        net_outward_flux[index] = step_net_outward

        digest.update(struct.pack(">q", index))
        update_digest_array(digest, state.records, np.uint8)
        update_digest_array(digest, state.parcels, ">i8")
        update_digest_array(digest, current_husks, np.uint8)
        update_digest_array(digest, active_boundaries, ">i8")
        digest.update(
            struct.pack(
                ">qq?qq",
                recorded_in_junction,
                int(junction.size),
                bool(junction_complete[index]),
                step_outward,
                step_net_outward,
            )
        )
        digest.update(
            struct.pack(
                ">q",
                int((~state.records & exterior).sum()),
            )
        )
        update_digest_array(digest, engine.clock_field(state.records), ">f8")

        previous_records = state.records.copy()

    snapshot(0, 0, 0)
    for _ in range(T_STEPS):
        hops, _, _ = tracked_engine_step(state, rng)
        gross, net = marker_flux(hops)
        snapshot(state.step, gross, net)

    digest.update(
        json.dumps(
            rng.bit_generator.state, sort_keys=True, separators=(",", ":")
        ).encode("ascii")
    )
    digest.update(
        struct.pack(
            ">qqq",
            -1 if both_husks_step is None else both_husks_step,
            -1 if selection_merge_step is None else selection_merge_step,
            -1 if bridge_step is None else bridge_step,
        )
    )
    return Trajectory(
        initial=initial,
        records=records,
        parcels=parcels,
        husks=husks,
        junction_recorded=junction_recorded,
        junction_size=junction_size,
        junction_complete=junction_complete,
        boundaries=boundaries,
        exterior_open_fraction=exterior_open_fraction,
        outward_flux=outward_flux,
        net_outward_flux=net_outward_flux,
        both_husks_step=both_husks_step,
        selection_merge_step=selection_merge_step,
        bridge_step=bridge_step,
        digest=digest.hexdigest(),
    )


def evaluate_husk_permanence(run: Trajectory) -> HuskPermanenceCheck:
    """Assert the requested site-set inclusion at every applicable step.

    A failed scientific assertion is returned as CHECK-01=FAIL so the other
    declared gates can still be measured. Malformed histories and engine
    invariant failures remain MACHINERY-FAIL.
    """

    final_step = (
        run.selection_merge_step
        if run.selection_merge_step is not None
        else T_STEPS
    )
    for step in range(1, final_step + 1):
        for star in range(2):
            previous = run.husks[step - 1, star]
            current = run.husks[step, star]
            if not previous.any():
                continue
            lost = previous & ~current
            try:
                assert not lost.any(), (
                    f"star-{star + 1} selected husk lost/shifted sites at step {step}"
                )
            except AssertionError:
                return HuskPermanenceCheck(
                    ok=False,
                    first_step=step,
                    star=star + 1,
                    lost_sites=int(lost.sum()),
                )
    return HuskPermanenceCheck(
        ok=True, first_step=None, star=None, lost_sites=0
    )


def flank_open_fractions(records: np.ndarray, boundaries: np.ndarray) -> tuple[float, float]:
    """Open fractions on the two outward half-ring flanks beyond a 20-site buffer."""

    left_limit = int(boundaries[0]) - OUTER_FLANK_BUFFER
    right_limit = int(boundaries[3]) + OUTER_FLANK_BUFFER
    left_flank = np.arange(0, max(0, left_limit + 1), dtype=np.int64)
    right_flank = np.arange(min(L, right_limit), L, dtype=np.int64)
    if left_flank.size == 0 or right_flank.size == 0:
        return 0.0, 0.0
    return (
        float((~records[left_flank]).mean()),
        float((~records[right_flank]).mean()),
    )


def evaluate_bridge(run: Trajectory) -> BridgeCheck:
    bridge = run.bridge_step
    if bridge is None or bridge <= 0:
        return BridgeCheck(
            bridge_step=bridge,
            left_pre_mass=0,
            right_pre_mass=0,
            merged_mass=0,
            junction_recorded=0,
            junction_size=0,
            left_flank_open=0.0,
            right_flank_open=0.0,
            prebridge_distinct=False,
            channel_ok=False,
            area_ok=False,
        )
    pre = bridge - 1
    left_pre_mass = int(run.husks[pre, 0].sum())
    right_pre_mass = int(run.husks[pre, 1].sum())
    merged_mass = int(run.husks[bridge, 0].sum())
    prebridge_distinct = bool(
        run.husks[pre, 0].any()
        and run.husks[pre, 1].any()
        and not np.array_equal(run.husks[pre, 0], run.husks[pre, 1])
    )
    pre_boundaries = run.boundaries[pre]
    junction = (
        junction_sites(pre_boundaries)
        if prebridge_distinct
        else np.empty(0, dtype=np.int64)
    )
    junction_recorded = int(run.records[bridge, junction].sum())
    if prebridge_distinct:
        left_open, right_open = flank_open_fractions(
            run.records[bridge], pre_boundaries
        )
    else:
        left_open, right_open = float("nan"), float("nan")
    channel_ok = bool(
        prebridge_distinct
        and junction.size > 0
        and junction_recorded == junction.size
        and left_open > 0.5
        and right_open > 0.5
    )
    area_ok = merged_mass >= left_pre_mass + right_pre_mass
    return BridgeCheck(
        bridge_step=bridge,
        left_pre_mass=left_pre_mass,
        right_pre_mass=right_pre_mass,
        merged_mass=merged_mass,
        junction_recorded=junction_recorded,
        junction_size=int(junction.size),
        left_flank_open=left_open,
        right_flank_open=right_open,
        prebridge_distinct=prebridge_distinct,
        channel_ok=channel_ok,
        area_ok=area_ok,
    )


def period_flux(values: np.ndarray, start: int, bridge: int) -> tuple[int, int, int]:
    steps = np.arange(values.size, dtype=np.int64)
    before = int(values[(steps > 0) & (steps < start)].sum())
    during = int(values[(steps >= start) & (steps <= bridge)].sum())
    after = int(values[steps > bridge].sum())
    return before, during, after


def evaluate_memory(run: Trajectory) -> MemoryCheck:
    if run.bridge_step is None or run.bridge_step <= 0:
        empty = np.zeros(L, dtype=np.bool_)
        return MemoryCheck(
            far_mask=empty,
            left_fill=0.0,
            right_fill=0.0,
            fill=0.0,
            adjacent_sites=0,
            adjacent_clock=1.0,
            clock_suppression=0.0,
            flux_before=0,
            flux_during=0,
            flux_after=0,
            net_flux_before=0,
            net_flux_during=0,
            net_flux_after=0,
            records_permanent=True,
            status="NO-BRIDGE",
        )

    pre = run.bridge_step - 1
    premerger_husks = run.husks[pre, 0] | run.husks[pre, 1]
    # For exterior sites, Block02 graph distance to the husk equals distance
    # to its facing surface/boundary.  Intersect it with the fixed two outer
    # quarters [0,99] and [300,399], which contain the two marker sites.
    distances = frozen.graph_distance_to_mask(premerger_husks)
    sites = np.arange(L, dtype=np.int64)
    left_far = (sites < L // 4) & (distances >= FAR_HUSK_DISTANCE)
    right_far = (sites >= 3 * L // 4) & (distances >= FAR_HUSK_DISTANCE)
    far = left_far | right_far
    if not left_far.any() or not right_far.any():
        raise AssertionError("pre-merger husks leave no two far-exterior quarters")

    final_records = run.records[-1]
    left_fill = float(final_records[left_far].mean())
    right_fill = float(final_records[right_far].mean())
    fill = float(final_records[far].mean())
    far_records = final_records & far
    adjacent = (
        (np.roll(far_records, 1) | np.roll(far_records, -1))
        & far
        & ~final_records
    )
    adjacent_sites = int(adjacent.sum())
    if adjacent_sites:
        adjacent_clock = float(engine.clock_field(final_records)[adjacent].mean())
    else:
        adjacent_clock = 1.0
    clock_suppression = 1.0 - adjacent_clock

    records_permanent = not bool(
        np.any(run.records[:-1, far] & ~run.records[1:, far])
    )
    if not records_permanent:
        raise AssertionError("a far-exterior memory record cleared")

    start = run.both_husks_step
    if start is None:
        start = run.bridge_step
    flux_before, flux_during, flux_after = period_flux(
        run.outward_flux, start, run.bridge_step
    )
    net_before, net_during, net_after = period_flux(
        run.net_outward_flux, start, run.bridge_step
    )

    if not far_records.any():
        status = "MEMORY-NOT-EXHIBITED"
    elif (
        0.0 < fill <= MEMORY_FILL_MAX
        and adjacent_sites > 0
        and clock_suppression > 0.0
        and flux_before + flux_during + flux_after > 0
    ):
        status = "PASS"
    else:
        status = "FAIL"
    return MemoryCheck(
        far_mask=far,
        left_fill=left_fill,
        right_fill=right_fill,
        fill=fill,
        adjacent_sites=adjacent_sites,
        adjacent_clock=adjacent_clock,
        clock_suppression=clock_suppression,
        flux_before=flux_before,
        flux_during=flux_during,
        flux_after=flux_after,
        net_flux_before=net_before,
        net_flux_during=net_during,
        net_flux_after=net_after,
        records_permanent=records_permanent,
        status=status,
    )


def flag_text(flag: bool) -> str:
    return "PASS" if flag else "FAIL"


def optional_flag_text(flag: bool | None) -> str:
    if flag is None:
        return "MEMORY-NOT-EXHIBITED"
    return flag_text(flag)


def spec_note() -> str:
    return (
        "SPEC-NOTE: d=1 declared comparator; marker flux is gross outward accepted "
        "crossings on the immediately outward bonds 40->39 and 360->361 (signed net "
        "after reverse crossings also shown); bridging runs from first simultaneous "
        "nonempty distinct husks through t_bridge; the live junction is the open "
        "interval between distinct husk-facing endpoints on the short central arc "
        "(history freezes the last such interval, and the channel gate requires two "
        "distinct t_bridge-1 husks); "
        "far flanks use a 20-site outward buffer, exterior means outside both fixed "
        "3sigma arcs, and memory quarters are fixed [0,99]/[300,399] further filtered "
        "to graph distance >=30 from the t_bridge-1 husk union; husk identity is "
        "anchored at each star's density-peak component and tracked by containment "
        "continuity (records permanent => components only merge => identity exact; "
        "the Block02 cardinality-first per-snapshot selector flickers/aliases when "
        "reused for identity over time — measured in draft 1, declared here); "
        "nearest-neighbor record availability supplies no attraction at husk "
        "separation, records never move, so only intervening deposition can connect "
        "them; engine Poisson deposition and native displacement/refuge rules retained "
        "without repair; no derivation, no audit status."
    )


def run_validation() -> tuple[tuple[str, ...], str]:
    started = time.monotonic()
    assert_imported_conventions()
    primary = run_trajectory(SEED)
    husk_permanence = evaluate_husk_permanence(primary)
    bridge = evaluate_bridge(primary)
    memory = evaluate_memory(primary)
    repeated = run_trajectory(SEED)

    # Exact CHECK-06 includes every per-step physical/tracked state, clocks,
    # terminal RNG state, and the event times used by the gates.
    check06 = primary.digest == repeated.digest
    check01 = husk_permanence.ok
    check02 = bridge.bridge_ok
    check03 = bridge.area_ok  # record monotonicity is asserted inside each run
    check04 = primary.exterior_open_fraction[-1] >= EXTERIOR_OPEN_GATE
    check05 = memory.gate_ok

    violation = (
        "none"
        if husk_permanence.ok
        else (
            f"t={husk_permanence.first_step},star={husk_permanence.star},"
            f"lost={husk_permanence.lost_sites}"
        )
    )
    line01 = (
        f"CHECK-01 HUSKS NEVER TRANSLATE: {flag_text(check01)} exact site-set "
        f"superset assertions every step through selection-merge="
        f"{primary.selection_merge_step}; first-violation={violation}; "
        f"first-both={primary.both_husks_step},peaks={primary.initial.peaks}."
    )
    bridge_text = "NA" if bridge.bridge_step is None else str(bridge.bridge_step)
    flank_text = (
        f"{bridge.left_flank_open:.3f}/{bridge.right_flank_open:.3f}"
        if bridge.prebridge_distinct
        else "NA/NA"
    )
    line02 = (
        f"CHECK-02 MERGER BY BRIDGING: {flag_text(check02)} t_bridge={bridge_text}"
        f"<={T_STEPS}; junction@bridge={bridge.junction_recorded}/"
        f"{bridge.junction_size} recorded; far-flank-open(L/R)="
        f"{flank_text} (>0.5 each); "
        f"prebridge-distinct={bridge.prebridge_distinct},"
        f"component-contains-peaks={bridge.bridge_step is not None}."
    )
    line03 = (
        f"CHECK-03 AREA ANALOG: {flag_text(check03)} records-monotone=PASS "
        f"(exact site-set/count assertions every step),area-gate={flag_text(check03)}; "
        f"pre-left={bridge.left_pre_mass},pre-right={bridge.right_pre_mass},"
        f"merged={bridge.merged_mass} "
        f"(gate merged>=left+right)."
    )
    regime = "IN-REGIME" if check04 else "OUT-OF-REGIME"
    line04 = (
        f"CHECK-04 EXTERIOR SURVIVES: {flag_text(check04)} {regime}; "
        f"exterior-open(T)={primary.exterior_open_fraction[-1]:.3f} "
        f"(gate>={EXTERIOR_OPEN_GATE:.2f}), total-records(T)="
        f"{int(primary.records[-1].sum())}/{L}."
    )
    line05 = (
        f"CHECK-05 MEMORY IMPRINT: {optional_flag_text(check05)}; outward-flux "
        f"before/during/after={memory.flux_before}/{memory.flux_during}/"
        f"{memory.flux_after} (net={memory.net_flux_before:+d}/"
        f"{memory.net_flux_during:+d}/{memory.net_flux_after:+d}); far-quarter-fill "
        f"combined={memory.fill:.3f},L/R={memory.left_fill:.3f}/"
        f"{memory.right_fill:.3f} (gate 0<fill<={MEMORY_FILL_MAX:.1f}); "
        f"record-adjacent clock={memory.adjacent_clock:.6f},suppression="
        f"{memory.clock_suppression:.6f},sites={memory.adjacent_sites},"
        f"permanent={memory.records_permanent}; CHECK-06 DETERMINISM: "
        f"{flag_text(check06)} digest={primary.digest[:16]} same-seed full histories."
    )

    required = (check01, check02, check03, check04, check06)
    memory_allows_total = check05 is True or check05 is None
    if all(required) and memory_allows_total:
        verdict = "MERGER-BY-BRIDGING"
    else:
        verdict = "MERGER-BY-BRIDGING-PARTIAL"
    memory_flag = "exhibited" if check05 is True else "not-exhibited"
    flags = (
        f"01:{flag_text(check01)},02:{flag_text(check02)},03:{flag_text(check03)},"
        f"04:{flag_text(check04)},05:{optional_flag_text(check05)},"
        f"06:{flag_text(check06)}"
    )
    elapsed = time.monotonic() - started
    line06 = (
        f"TOTAL: {verdict}; flags[{flags}]; t_bridge={bridge_text}; "
        f"memory={memory_flag}; runtime={elapsed:.3f}s; " + spec_note()
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
        return 0 if verdict == "MERGER-BY-BRIDGING" else 1
    except Exception as exc:  # noqa: BLE001 - comparator runner fails closed.
        print(
            f"TOTAL: MACHINERY-FAIL {type(exc).__name__}: {exc}; " + spec_note()
        )
        return 2


if __name__ == "__main__":
    sys.exit(main())
