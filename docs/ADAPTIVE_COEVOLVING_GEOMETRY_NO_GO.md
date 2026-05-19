# Adaptive / Coevolving Geometry Scout No-Go

**Date:** 2026-04-05  
**Status:** compact no-go / outside audit-ratified tier

## One-line read

The existing distinguishability-weighted node-placement machinery does
produce geometry that evolves rather than being imposed, but the smallest
weak-field scout we tried did **not** give a robust retained gravity
signal. The sign is seed-sensitive and changes with placement strength, so
this lane is not yet a clear positive.

## What was tested

The probe reused the current generated-geometry machinery in
[`scripts/node_placement_emergence.py`](/Users/jonreilly/Projects/Physics/scripts/node_placement_emergence.py):

- geometry evolves via distinguishability-weighted post-barrier placement
- weak-field observable only: far-field mass-induced centroid shift
- comparison against the flat-field control for the same geometry

The quick check swept `alpha ∈ {0, 1, 2, 4, 8}` over a small seed set and
measured the mean gravity shift sign.

## Quick probe read

The sign is mixed rather than stable:

- `alpha = 0.0`: `13/18` TOWARD, mean shift `+0.855`
- `alpha = 1.0`: `10/18` TOWARD, mean shift `+0.176`
- `alpha = 2.0`: `10/17` TOWARD, mean shift `+0.580`
- `alpha = 4.0`: `6/15` TOWARD, mean shift `-0.069`
- `alpha = 8.0`: `5/10` TOWARD, mean shift `+0.073`

The baseline is already noisy, and the evolving-geometry rows do not
improve the sign stability in a way that would justify a retained claim.

## Safe conclusion

- geometry-evolves-not-imposed is real in the placement rule
- the smallest weak-field scout did **not** produce a clean adaptive-geometry
  positive
- this is currently a **bounded no-go**, not a publishable retention point

## Next if revisited

If this lane comes back, it should not be a broader sweep. It should be a
single new control law that directly regulates the geometry observable
itself, rather than only biasing distinguishability.

---

**Audit requeue note, 2026-05-17:** the previous
`audited_conditional` verdict cited an incomplete restricted packet with
missing helper-script imports. The audit ledger now records
`helper_runner_paths` for this row, so the next audit packet should
include `scripts/generative_causal_dag_interference.py` alongside the
primary runner and cache. This note changes no science content; it makes
the re-audit hash drift explicit.

## Helper-runner code excerpt (load-bearing for restricted packet, inlined 2026-05-18)

Inlined here so the restricted audit packet is self-contained. Source of
truth: `scripts/generative_causal_dag_interference.py` at commit
`b179c2d2c`. The primary runner
`scripts/node_placement_emergence.py` imports `generate_causal_dag` from
this helper to build the uniform (baseline / control) DAG family that
all `placement alpha=*` rows are compared against. Without this function,
the baseline column in the quick-probe table above cannot be regenerated
from the restricted packet.

Only the directly-imported function is inlined (no private callees;
`generate_causal_dag` depends only on `math`, `random`, and
`collections.defaultdict` from the stdlib).

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
            # Seed: single source node at center
            idx = len(positions)
            positions.append((x, 0.0))
            arrival.append(0.0)
            layer_nodes.append(idx)
        else:
            # Spawn nodes at random y-positions in this layer
            for _ in range(nodes_per_layer):
                y = rng.uniform(-y_range, y_range)
                idx = len(positions)
                positions.append((x, y))
                layer_nodes.append(idx)

                # Connect to all reachable nodes in PREVIOUS layers
                # (creates the causal DAG — edges only go forward in x)
                best_arrival = float("inf")
                for prev_layer in layer_indices[max(0, layer - 2):]:  # Look back 2 layers
                    for prev_idx in prev_layer:
                        px, py = positions[prev_idx]
                        dist = math.sqrt((x - px) ** 2 + (y - py) ** 2)
                        if dist <= connect_radius:
                            adj[prev_idx].append(idx)
                            # Arrival time = parent arrival + edge distance
                            candidate = arrival[prev_idx] + dist
                            if math.isfinite(candidate) and candidate < best_arrival:
                                best_arrival = candidate

                arrival.append(best_arrival)

        layer_indices.append(layer_nodes)

    return positions, dict(adj), arrival
```
