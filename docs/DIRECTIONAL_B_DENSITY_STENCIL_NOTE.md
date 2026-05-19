# Directional-B Density Stencil Note

**Status:** bounded transfer diagnostic on the fixed directional-measure lane  
**Date:** 2026-04-04
**Primary runner:** [`scripts/directional_b_density_stencil_transfer.py`](../scripts/directional_b_density_stencil_transfer.py)

## Scope

This note does not reopen the directional-measure denominator search. It asks a
smaller question forced by the new center-biased midlayer sentinel:

- is the recent continuous-density miss mode really a problem with the fourth-neighbor stencil?

The comparison reuses the existing artifact chain:

- original dense reference sample from the continuous-density bridge card
- branching-tree freeze control
- center-biased midlayer sentinel from the latest holdout

No new graph family or new threshold fit is introduced on the expanded sample.
The only frozen thresholds are the old dense-reference density-load rules:

- `knn3_density_load >= 1.9783`
- `knn4_density_load >= 2.7354`

## Helper-runner code excerpts (load-bearing for restricted packet, transitive helpers inlined 2026-05-18)

The primary runner [`scripts/directional_b_density_stencil_transfer.py`](../scripts/directional_b_density_stencil_transfer.py)
imports its data generation and evaluation functions from three sibling
helper modules, which in turn import a small number of core utilities from
four deeper helpers. To make the restricted audit packet self-contained, the
load-bearing functions are inlined here. These cover the four categories
flagged in the audit verdict: (i) generated rows, (ii) density-load features,
(iii) overlap labels, (iv) thresholds.

### From scripts/directional_b_overlap_continuous_density_bridge_card.py

```python
TARGET_BAND_WIDTH = 2.0 * TARGET_BAND_HALF_WIDTH


@dataclass(frozen=True)
class DensityRow:
    family: str
    size: int
    seed: int
    mass_nodes: int
    mu: float
    local_target_count: int
    source_load: float
    bracket_density_load: float
    local_gap_density_load: float
    knn3_density_load: float
    knn4_density_load: float
    bracket_expected_target_count: float
    local_gap_expected_target_count: float
    knn3_expected_target_count: float
    knn4_expected_target_count: float
    overlap: bool


@dataclass(frozen=True)
class DensityRule:
    feature: str
    op_name: str
    threshold: float
    tp: int
    fp: int
    fn: int
    tn: int
    accuracy: float


def _nearest_distances(values: list[float], target: float) -> list[float]:
    return sorted(abs(value - target) for value in values)


def _local_gap_mean(values: list[float], target: float) -> float:
    idx = 0
    while idx < len(values) and values[idx] < target:
        idx += 1

    local_gaps: list[float] = []
    if idx - 1 > 0:
        local_gaps.append(values[idx - 1] - values[idx - 2])
    if 0 < idx < len(values):
        local_gaps.append(values[idx] - values[idx - 1])
    if idx < len(values) - 1:
        local_gaps.append(values[idx + 1] - values[idx])

    if not local_gaps:
        return float("nan")
    return statistics.fmean(local_gaps)


def _expected_count_from_gap(gap: float) -> float:
    if not math.isfinite(gap) or gap <= 0.0:
        return float("nan")
    return TARGET_BAND_WIDTH / gap


def _expected_count_from_knn_radius(radius: float, k: int) -> float:
    if not math.isfinite(radius) or radius <= 0.0:
        return float("nan")
    # In 1D, rho_hat = k / (2 * r_k). Multiplying by the target-band width
    # 2 * TARGET_BAND_HALF_WIDTH reduces to k / r_k here.
    return k * TARGET_BAND_WIDTH / (2.0 * radius)


def _density_load(mass_nodes: int, expected_target_count: float) -> float:
    if not math.isfinite(expected_target_count) or expected_target_count <= 0.0:
        return float("nan")
    return mass_nodes / expected_target_count


def _build_row(
    family: str,
    size: int,
    seed: int,
    mass_nodes: int,
    target_b: float,
    positions: list[tuple[float, float]],
    grav_layer_nodes: list[int],
) -> DensityRow | None:
    center_y = statistics.fmean(y for _x, y in positions)
    selected = _select_mass_nodes(
        positions=positions,
        layer_nodes=grav_layer_nodes,
        center_y=center_y,
        target_b=target_b,
        mass_nodes=mass_nodes,
    )
    if len(selected) < mass_nodes:
        return None

    ys = [positions[node][1] for node in selected]
    actual_b = statistics.fmean(ys) - center_y
    h_mass = 0.5 * (max(ys) - min(ys))
    mu = ((actual_b - h_mass) / h_mass) if h_mass > 0.0 else float("inf")

    same_side_positions = sorted(
        positions[node][1] for node in grav_layer_nodes if positions[node][1] >= center_y
    )
    target_y = center_y + target_b
    local_target_count = sum(
        1 for y in same_side_positions if abs(y - target_y) <= TARGET_BAND_HALF_WIDTH
    )
    source_load = mass_nodes / max(1, local_target_count)

    idx = 0
    while idx < len(same_side_positions) and same_side_positions[idx] < target_y:
        idx += 1
    bracket_gap = float("nan")
    if 0 < idx < len(same_side_positions):
        bracket_gap = same_side_positions[idx] - same_side_positions[idx - 1]

    local_gap_mean = _local_gap_mean(same_side_positions, target_y)
    nearest_distances = _nearest_distances(same_side_positions, target_y)
    knn3_radius = nearest_distances[2] if len(nearest_distances) >= 3 else float("nan")
    knn4_radius = nearest_distances[3] if len(nearest_distances) >= 4 else float("nan")

    bracket_expected_target_count = _expected_count_from_gap(bracket_gap)
    local_gap_expected_target_count = _expected_count_from_gap(local_gap_mean)
    knn3_expected_target_count = _expected_count_from_knn_radius(knn3_radius, k=3)
    knn4_expected_target_count = _expected_count_from_knn_radius(knn4_radius, k=4)

    return DensityRow(
        family=family,
        size=size,
        seed=seed,
        mass_nodes=mass_nodes,
        mu=mu,
        local_target_count=local_target_count,
        source_load=source_load,
        bracket_density_load=_density_load(mass_nodes, bracket_expected_target_count),
        local_gap_density_load=_density_load(mass_nodes, local_gap_expected_target_count),
        knn3_density_load=_density_load(mass_nodes, knn3_expected_target_count),
        knn4_density_load=_density_load(mass_nodes, knn4_expected_target_count),
        bracket_expected_target_count=bracket_expected_target_count,
        local_gap_expected_target_count=local_gap_expected_target_count,
        knn3_expected_target_count=knn3_expected_target_count,
        knn4_expected_target_count=knn4_expected_target_count,
        overlap=mu <= 0.0,
    )


def _evaluate_baseline_dag(task: tuple[int, int, int, float]) -> DensityRow | None:
    mass_nodes, n_layers, seed, target_b = task
    positions, _adj, _meta = generate_causal_dag(
        n_layers=n_layers,
        nodes_per_layer=25,
        y_range=12.0,
        connect_radius=3.0,
        rng_seed=seed * 11 + 7,
    )
    by_layer: dict[int, list[int]] = defaultdict(list)
    for idx, (x, _y) in enumerate(positions):
        by_layer[round(x)].append(idx)
    layers = sorted(by_layer)
    mid = len(layers) // 2
    return _build_row(
        family=f"dag-m{mass_nodes}",
        size=n_layers,
        seed=seed,
        mass_nodes=mass_nodes,
        target_b=target_b,
        positions=positions,
        grav_layer_nodes=by_layer[layers[mid]],
    )


def _evaluate_holdout_dag(
    task: tuple[int, int, int, float, int, float, float, int],
) -> DensityRow | None:
    (
        mass_nodes,
        n_layers,
        seed,
        target_b,
        nodes_per_layer,
        y_range,
        connect_radius,
        seed_offset,
    ) = task
    positions, _adj, _meta = generate_causal_dag(
        n_layers=n_layers,
        nodes_per_layer=nodes_per_layer,
        y_range=y_range,
        connect_radius=connect_radius,
        rng_seed=seed * 11 + seed_offset,
    )
    by_layer: dict[int, list[int]] = defaultdict(list)
    for idx, (x, _y) in enumerate(positions):
        by_layer[round(x)].append(idx)
    layers = sorted(by_layer)
    mid = len(layers) // 2
    return _build_row(
        family=f"holdout-m{mass_nodes}",
        size=n_layers,
        seed=seed,
        mass_nodes=mass_nodes,
        target_b=target_b,
        positions=positions,
        grav_layer_nodes=by_layer[layers[mid]],
    )


def _feature_value(row: DensityRow, feature: str) -> float:
    return getattr(row, feature)


def _best_rule(rows: list[DensityRow], feature: str) -> DensityRule:
    values = [_feature_value(row, feature) for row in rows]
    finite_values = [value for value in values if math.isfinite(value)]
    best: DensityRule | None = None
    for threshold in _candidate_thresholds(finite_values):
        stats = _accuracy(
            rows,
            lambda row, f=feature, t=threshold: _feature_value(row, f) >= t,
        )
        rule = DensityRule(feature, ">=", threshold, *stats)
        if best is None or rule.accuracy > best.accuracy:
            best = rule
    assert best is not None
    return best
```

### From scripts/directional_b_overlap_continuous_density_midlayer_holdout.py

```python
@dataclass(frozen=True)
class DagConfig:
    family_prefix: str
    nodes_per_layer: int
    y_range: float
    connect_radius: float
    seed_offset: int
    midlayer_gamma: float | None = None


def _sample_y(rng: random.Random, y_range: float, gamma: float | None) -> float:
    if gamma is None:
        return rng.uniform(-y_range, y_range)
    u = rng.uniform(-1.0, 1.0)
    return math.copysign(abs(u) ** gamma, u) * y_range


def _generate_midlayer_holdout(
    *,
    n_layers: int,
    nodes_per_layer: int,
    y_range: float,
    connect_radius: float,
    rng_seed: int,
    midlayer_gamma: float | None,
) -> tuple[list[tuple[float, float]], dict[int, list[int]]]:
    rng = random.Random(rng_seed)
    positions: list[tuple[float, float]] = []
    adj: dict[int, list[int]] = defaultdict(list)
    arrival: list[float] = []
    layer_indices: list[list[int]] = []
    mid_layer = n_layers // 2

    for layer in range(n_layers):
        x = float(layer)
        layer_nodes: list[int] = []
        if layer == 0:
            idx = len(positions)
            positions.append((x, 0.0))
            arrival.append(0.0)
            layer_nodes.append(idx)
        else:
            gamma = midlayer_gamma if layer == mid_layer else None
            for _ in range(nodes_per_layer):
                y = _sample_y(rng, y_range, gamma)
                idx = len(positions)
                positions.append((x, y))
                layer_nodes.append(idx)

                best_arrival = float("inf")
                for prev_layer in layer_indices[max(0, layer - 2) :]:
                    for prev_idx in prev_layer:
                        px, py = positions[prev_idx]
                        dist = math.sqrt((x - px) ** 2 + (y - py) ** 2)
                        if dist <= connect_radius:
                            adj[prev_idx].append(idx)
                            candidate = arrival[prev_idx] + dist
                            if math.isfinite(candidate) and candidate < best_arrival:
                                best_arrival = candidate
                arrival.append(best_arrival)
        layer_indices.append(layer_nodes)

    return positions, dict(adj)


def _evaluate_midlayer_dag(
    task: tuple[DagConfig, int, int, int, float],
) -> DensityRow | None:
    config, mass_nodes, n_layers, seed, target_b = task
    positions, _adj = _generate_midlayer_holdout(
        n_layers=n_layers,
        nodes_per_layer=config.nodes_per_layer,
        y_range=config.y_range,
        connect_radius=config.connect_radius,
        rng_seed=seed * 11 + config.seed_offset,
        midlayer_gamma=config.midlayer_gamma,
    )
    by_layer: dict[int, list[int]] = defaultdict(list)
    for idx, (x, _y) in enumerate(positions):
        by_layer[round(x)].append(idx)
    layers = sorted(by_layer)
    mid = len(layers) // 2
    return _build_row(
        family=f"{config.family_prefix}-m{mass_nodes}",
        size=n_layers,
        seed=seed,
        mass_nodes=mass_nodes,
        target_b=target_b,
        positions=positions,
        grav_layer_nodes=by_layer[layers[mid]],
    )


def _collect_rows(
    tasks: list[tuple],
    evaluator,
    workers: int,
) -> list[DensityRow]:
    ctx = mp.get_context("fork")
    if workers <= 1:
        rows = [evaluator(task) for task in tasks]
    else:
        try:
            with ProcessPoolExecutor(max_workers=workers, mp_context=ctx) as pool:
                rows = list(pool.map(evaluator, tasks))
        except (OSError, PermissionError):
            rows = [evaluator(task) for task in tasks]
    return [row for row in rows if row is not None]
```

### From scripts/directional_b_overlap_continuous_density_tree_control.py

```python
FROZEN_COUNT_THRESHOLD = 2.5
FROZEN_KNN4_THRESHOLD = 2.735352889954456


def _evaluate_tree(task: tuple[int, int, float, int]) -> DensityRow | None:
    n_layers, branching_factor, target_b, mass_nodes = task
    positions, _adj, layer_indices = build_branching_tree(
        n_layers,
        branching_factor=branching_factor,
        y_range=10.0,
    )
    mid = len(layer_indices) // 2
    return _build_row(
        family="tree",
        size=n_layers,
        seed=0,
        mass_nodes=mass_nodes,
        target_b=target_b,
        positions=positions,
        grav_layer_nodes=layer_indices[mid],
    )
```

### From scripts/directional_b_overlap_onset_local_density_compare.py (transitive — provides `_accuracy`, `_candidate_thresholds`, and `TARGET_BAND_HALF_WIDTH`)

```python
TARGET_BAND_HALF_WIDTH = 1.0


def _accuracy(rows, predicate) -> tuple[int, int, int, int, float]:
    tp = fp = tn = fn = 0
    for row in rows:
        pred = predicate(row)
        if pred and row.overlap:
            tp += 1
        elif pred and not row.overlap:
            fp += 1
        elif not pred and row.overlap:
            fn += 1
        else:
            tn += 1
    return tp, fp, fn, tn, (tp + tn) / len(rows)


def _candidate_thresholds(values: list[float]) -> list[float]:
    ordered = sorted(set(values))
    mids = [(ordered[i] + ordered[i + 1]) / 2.0 for i in range(len(ordered) - 1)]
    return ordered + mids
```

### From scripts/directional_b_readout_compare.py (transitive — provides `_select_mass_nodes`)

```python
def _select_mass_nodes(
    positions: list[tuple[float, float]],
    layer_nodes: list[int],
    center_y: float,
    target_b: float,
    mass_nodes: int,
) -> list[int]:
    target_y = center_y + target_b
    ordered = sorted(
        layer_nodes,
        key=lambda node: (abs(positions[node][1] - target_y), positions[node][1]),
    )
    return ordered[:mass_nodes]
```

### From scripts/generative_causal_dag_interference.py (transitive — provides `generate_causal_dag`)

```python
def generate_causal_dag(
    n_layers: int = 20,
    nodes_per_layer: int = 15,
    y_range: float = 10.0,
    connect_radius: float = 2.5,
    rng_seed: int = 42,
) -> tuple[list[tuple[float, float]], dict[int, list[int]], list[float]]:
    """Generate a causal DAG by spawning layers of events.

    Each layer is at a fixed x-coordinate (the "time" direction).
    Within each layer, nodes are placed at random y-positions.
    Edges go ONLY from earlier layers to later layers (causal).
    A node connects to all nodes in the next layer within connect_radius.

    Returns: (positions, forward_adjacency, arrival_times)
    """
    rng = random.Random(rng_seed)
    positions: list[tuple[float, float]] = []
    adj: dict[int, list[int]] = defaultdict(list)
    arrival: list[float] = []
    layer_indices: list[list[int]] = []

    for layer in range(n_layers):
        x = float(layer)
        layer_nodes = []

        if layer == 0:
            idx = len(positions)
            positions.append((x, 0.0))
            arrival.append(0.0)
            layer_nodes.append(idx)
        else:
            for _ in range(nodes_per_layer):
                y = rng.uniform(-y_range, y_range)
                idx = len(positions)
                positions.append((x, y))
                layer_nodes.append(idx)

                best_arrival = float("inf")
                for prev_layer in layer_indices[max(0, layer - 2):]:
                    for prev_idx in prev_layer:
                        px, py = positions[prev_idx]
                        dist = math.sqrt((x - px) ** 2 + (y - py) ** 2)
                        if dist <= connect_radius:
                            adj[prev_idx].append(idx)
                            candidate = arrival[prev_idx] + dist
                            if math.isfinite(candidate) and candidate < best_arrival:
                                best_arrival = candidate

                arrival.append(best_arrival)

        layer_indices.append(layer_nodes)

    return positions, dict(adj), arrival
```

### From scripts/scaling_testbench.py (transitive — provides `build_branching_tree`)

```python
def build_branching_tree(n_layers, branching_factor=2, y_range=10.0):
    """Layered tree: each node connects to `branching_factor` nodes in next layer."""
    positions = [(0.0, 0.0)]
    adj = defaultdict(list)
    layer_indices = [[0]]

    for layer in range(1, n_layers):
        x = float(layer)
        layer_nodes = []
        prev = layer_indices[-1]

        for parent in prev:
            py = positions[parent][1]
            for b in range(branching_factor):
                y = py + (b - branching_factor/2 + 0.5) * (y_range / (branching_factor ** layer))
                y = max(-y_range, min(y_range, y))
                idx = len(positions)
                positions.append((x, y))
                adj[parent].append(idx)
                layer_nodes.append(idx)

        layer_indices.append(layer_nodes)

    return positions, dict(adj), layer_indices
```

Coverage of the four audit categories:

- **Generated rows.** `_evaluate_baseline_dag`, `_evaluate_holdout_dag`,
  `_evaluate_midlayer_dag`, and `_evaluate_tree` each call `_build_row` after
  generating positions via `generate_causal_dag`, `_generate_midlayer_holdout`,
  or `build_branching_tree`. These are the row producers consumed by the
  primary runner's `_dense_reference_rows`, `_tree_rows`, and `_midlayer_rows`.
- **Density-load features.** `_build_row` derives `knn3_density_load`,
  `knn4_density_load`, `bracket_density_load`, `local_gap_density_load`, and
  `source_load` from `_density_load`, `_expected_count_from_gap`, and
  `_expected_count_from_knn_radius` over the same-side positions slice.
- **Overlap labels.** `_build_row` sets `overlap = mu <= 0.0` where
  `mu = (actual_b - h_mass) / h_mass`. `_select_mass_nodes` picks the same-side
  mass nodes that feed `actual_b` and `h_mass`.
- **Thresholds.** The frozen 3-NN / 4-NN density-load thresholds the note
  reports (`1.9783`, `2.7354`) are produced by `_best_rule` over
  `_candidate_thresholds(values)` evaluated by `_accuracy`. The frozen counted
  source-load threshold `2.5` and the previously reported 4-NN threshold
  `2.735352889954456` are defined as `FROZEN_COUNT_THRESHOLD` and
  `FROZEN_KNN4_THRESHOLD` in the tree-control helper.

## Result

On the original reference sample plus the tree control, the frozen 4-NN law is
still cleaner:

- 4-NN: `21/2/3/37`, accuracy `0.9206`
- 3-NN: `22/5/2/34`, accuracy `0.8889`

But the center-biased midlayer sentinel reverses that preference:

- 4-NN: `4/0/6/30`, accuracy `0.8500`
- 3-NN: `8/0/2/30`, accuracy `0.9500`

So once the midlayer sentinel is added to the existing reference+tree sample,
the frozen 3-NN stencil becomes the better smooth law on the current expanded
dataset:

- extended sample 3-NN: `30/5/4/64`, accuracy `0.9126`
- extended sample 4-NN: `25/2/9/67`, accuracy `0.8932`

## Miss mode

The 4-NN failures are not random. They are mostly one-sided, low-occupancy
target bands on the midlayer sentinel:

- `5/6` frozen 4-NN false negatives have in-band nodes on only one side of the target plane
- `4/6` are rescued immediately by the frozen 3-NN stencil
- the remaining two misses are the sharpest shallow-overlap corners:
  - one nearly singular `m3` row with only one in-band node
  - one `m5` row with three in-band nodes but still a shallow overlap geometry

The bounded interpretation is that the fourth neighbor is the unstable sample on
this sentinel. Under one-sided midlayer densification, the fourth neighbor is
often the first point that jumps across the target-plane gap, so `r4` inflates
the estimated same-side support and makes the frozen 4-NN load too
conservative. The 3-NN stencil stays closer to the counted occupancy picture.

## Consequence

This does **not** overturn the current portable overlap statement:

- occupancy shortage is still the robust coarse bridge

It does sharpen the continuous-law story:

- 4-NN remains the cleaner fit on the original dense reference sample
- 3-NN is now the better frozen smooth-density candidate on the current
  expanded sample that includes the midlayer sentinel

A bounded residual probe sharpens the limit of that claim:

- the last two frozen 3-NN misses split into a sparse one-node shoulder and an
  asymmetric upper-shelf row
- a miss-local hybrid can close the current midlayer sentinel, but it degrades
  the old reference+tree control from `22/5/2/34` to `24/8/0/31`

So no frozen residual rescue law is promoted yet. The current portable
statement remains occupancy-first, and the next bounded continuous-law step, if
one is still needed, should start from the 3-NN stencil's residual anatomy or
another equally local occupancy-aware correction, not from a broader
denominator search.

---

## Audit Requeue Note (2026-05-17)

No science content changes. The prior non-clean audit cited restricted-packet
incompleteness from helper-runner imports. The audit pipeline now populates
transitive `helper_runner_paths`, so this source-note hash drift is an
explicit re-audit trigger for a complete restricted packet. Helper runner
paths:

- `scripts/density_matrix_analysis.py`
- `scripts/directional_b_overlap_continuous_density_bridge_card.py`
- `scripts/directional_b_overlap_continuous_density_midlayer_holdout.py`
- `scripts/directional_b_overlap_continuous_density_tree_control.py`
- `scripts/directional_b_overlap_onset_local_density_compare.py`
- `scripts/directional_b_readout_compare.py`
- `scripts/generative_causal_dag_interference.py`
- `scripts/gravity_observable_readout_scaling_compare.py`
- `scripts/gravity_packet_local_action_flow_transfer_compare.py`
- `scripts/scaling_testbench.py`
- `scripts/two_register_decoherence.py`
