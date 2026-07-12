#!/usr/bin/env python3
"""Gate B connectivity tolerance replay.

This freezes a bounded question:

  Under the declared finite propagation algorithm, what changes under
  fixed-adjacency coordinate jitter and under a same-coordinate adjacency
  replacement?

The harness compares a small fixed set of architectures:
  - ordered lattice baseline
  - jittered lattice with fixed connectivity
  - templated growth with fixed-offset connectivity
  - grown geometry with K-NN connectivity
  - snapped/grid-like connectivity

The goal is a bounded finite-algorithm theorem, not Gate B dynamics closure.
"""

from __future__ import annotations

import cmath
import math
import random
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple


BETA = 0.8
K = 5.0
FIELD_STRENGTH = 5e-5
N_LAYERS = 13
HALF = 5
Y_MASSES = (2, 3, 4)
SEEDS = (5, 18, 31, 44, 57, 70)
JITTER_SWEEP = (0.0, 0.1, 0.2, 0.3, 0.4, 0.5)
MASS_STRENGTHS = (0.75, 1.0, 1.25)
ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "GATE_B_CONNECTIVITY_TOLERANCE_NOTE.md"


CHECK_PASS = 0
CHECK_FAIL = 0


def _check(label: str, condition: bool, detail: str = "") -> None:
    global CHECK_PASS, CHECK_FAIL
    if condition:
        CHECK_PASS += 1
        tag = "PASS"
    else:
        CHECK_FAIL += 1
        tag = "FAIL"
    print(f"[{tag}] {label}")
    if detail:
        print(f"       {detail}")


def _source_boundary_checks() -> None:
    text = NOTE.read_text(encoding="utf-8")
    flat = " ".join(text.split())
    print()
    print("Source-boundary checks")
    print("-" * 40)
    _check(
        "registered runner validates the audited connectivity-tolerance note",
        NOTE.name == "GATE_B_CONNECTIVITY_TOLERANCE_NOTE.md"
        and "**Claim type:** bounded_theorem" in text
        and "finite-harness claim awaiting independent audit" in flat,
    )
    _check(
        "note defines detector window, TOWARD, F~M, and the 54-trial denominator",
        "W(y_m)={d: |y_d-y_m|<=1.5}" in flat
        and "`3 x 3 x 6 = 54`" in flat
        and "`delta(y_m,q)>0`" in flat
        and "`max(delta,1e-30)`" in flat,
    )
    _check(
        "note cites the finite-stencil authority and excludes physical overclaims",
        "GATE_B_LOCAL_STENCIL_CONNECTIVITY_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-18.md" in text
        and "No physical Poisson/source law" in flat
        and "physical detector-window, `TOWARD`, or `F~M` semantics" in flat
        and "architecture-independent theorem that connectivity is the bottleneck" in flat,
    )


@dataclass
class GraphFamily:
    name: str
    positions: List[Tuple[float, float, float]]
    layers: List[List[int]]
    adj: Dict[int, List[int]]


def _grid_index(layer: int, iy: int, iz: int, half: int) -> int:
    span = 2 * half + 1
    return layer * (span * span) + (iy + half) * span + (iz + half)


def _build_fixed_connectivity(n_layers: int, half: int) -> GraphFamily:
    span = 2 * half + 1
    positions: List[Tuple[float, float, float]] = []
    layers: List[List[int]] = []
    adj: Dict[int, List[int]] = {}

    for layer in range(n_layers):
        x = float(layer)
        nodes: List[int] = []
        for iy in range(-half, half + 1):
            for iz in range(-half, half + 1):
                idx = len(positions)
                positions.append((x, float(iy), float(iz)))
                nodes.append(idx)
        layers.append(nodes)

    for layer in range(n_layers - 1):
        for iy in range(-half, half + 1):
            for iz in range(-half, half + 1):
                src = _grid_index(layer, iy, iz, half)
                nbs: List[int] = []
                for dy in (-1, 0, 1):
                    for dz in (-1, 0, 1):
                        jy = iy + dy
                        jz = iz + dz
                        if -half <= jy <= half and -half <= jz <= half:
                            nbs.append(_grid_index(layer + 1, jy, jz, half))
                adj[src] = nbs

    return GraphFamily("ordered", positions, layers, adj)


def _jitter_positions(base: GraphFamily, jitter: float, seed: int) -> GraphFamily:
    rng = random.Random(seed)
    positions = []
    for x, y, z in base.positions:
        positions.append((x, y + rng.gauss(0.0, jitter), z + rng.gauss(0.0, jitter)))
    return GraphFamily(f"jitter={jitter:g}", positions, base.layers, base.adj)


def _templated_growth(n_layers: int, half: int, drift: float, seed: int, snap: bool = False) -> GraphFamily:
    rng = random.Random(seed)
    positions: List[Tuple[float, float, float]] = []
    layers: List[List[int]] = []

    # Keep the same layer-wise grid labels, but let the coordinates drift
    # locally from layer to layer.
    layer_state: Dict[Tuple[int, int], Tuple[float, float]] = {}
    for layer in range(n_layers):
        x = float(layer)
        nodes: List[int] = []
        for iy in range(-half, half + 1):
            for iz in range(-half, half + 1):
                if layer == 0:
                    y, z = float(iy), float(iz)
                else:
                    py, pz = layer_state[(iy, iz)]
                    y = py + rng.gauss(0.0, drift)
                    z = pz + rng.gauss(0.0, drift)
                    if snap:
                        y = round(y)
                        z = round(z)
                idx = len(positions)
                positions.append((x, y, z))
                nodes.append(idx)
                layer_state[(iy, iz)] = (y, z)
        layers.append(nodes)

    base = _build_fixed_connectivity(n_layers, half)
    name = "snapped" if snap else f"templated drift={drift:g}"
    return GraphFamily(name, positions, layers, base.adj)


def _knn_growth(n_layers: int, half: int, drift: float, k: int, seed: int) -> GraphFamily:
    rng = random.Random(seed)
    positions: List[Tuple[float, float, float]] = []
    layers: List[List[int]] = []
    layer_state: Dict[Tuple[int, int], Tuple[float, float]] = {}

    for layer in range(n_layers):
        x = float(layer)
        nodes: List[int] = []
        for iy in range(-half, half + 1):
            for iz in range(-half, half + 1):
                if layer == 0:
                    y, z = float(iy), float(iz)
                else:
                    py, pz = layer_state[(iy, iz)]
                    y = py + rng.gauss(0.0, drift)
                    z = pz + rng.gauss(0.0, drift)
                idx = len(positions)
                positions.append((x, y, z))
                nodes.append(idx)
                layer_state[(iy, iz)] = (y, z)
        layers.append(nodes)

    adj: Dict[int, List[int]] = {}
    for layer in range(n_layers - 1):
        src_nodes = layers[layer]
        dst_nodes = layers[layer + 1]
        dst_positions = [positions[i] for i in dst_nodes]
        for src in src_nodes:
            sx, sy, sz = positions[src]
            ranked = []
            for dst, (dx, dy, dz) in zip(dst_nodes, dst_positions):
                dist2 = (dx - sx) ** 2 + (dy - sy) ** 2 + (dz - sz) ** 2
                ranked.append((dist2, dst))
            ranked.sort(key=lambda item: item[0])
            adj[src] = [dst for _, dst in ranked[:k]]

    return GraphFamily(f"knn k={k}", positions, layers, adj)


def _field_for_mass(positions: Sequence[Tuple[float, float, float]], mass_idx: int, strength: float) -> List[float]:
    mx, my, mz = positions[mass_idx]
    field = []
    for x, y, z in positions:
        r = math.sqrt((x - mx) ** 2 + (y - my) ** 2 + (z - mz) ** 2) + 0.1
        field.append(strength / r)
    return field


def _blocked_barrier(layer_nodes: Sequence[int], positions: Sequence[Tuple[float, float, float]]) -> set[int]:
    blocked = set()
    for idx in layer_nodes:
        y = positions[idx][1]
        if -1.0 < y < 1.0:
            blocked.add(idx)
    return blocked


def _propagate(
    positions: Sequence[Tuple[float, float, float]],
    layers: Sequence[Sequence[int]],
    adj: Dict[int, List[int]],
    field: Sequence[float],
    blocked: set[int],
) -> List[complex]:
    n = len(positions)
    amps = [0j] * n
    source = layers[0][len(layers[0]) // 2]
    amps[source] = 1.0

    for layer in range(len(layers) - 1):
        for i in layers[layer]:
            if i in blocked:
                continue
            ai = amps[i]
            if abs(ai) < 1e-30:
                continue
            xi, yi, zi = positions[i]
            for j in adj.get(i, []):
                if j in blocked:
                    continue
                xj, yj, zj = positions[j]
                dx = xj - xi
                dy = yj - yi
                dz = zj - zi
                L = math.sqrt(dx * dx + dy * dy + dz * dz)
                if L < 1e-10:
                    continue
                lf = 0.5 * (field[i] + field[j])
                act = L * (1.0 - lf)
                theta = math.atan2(math.sqrt(dy * dy + dz * dz), max(dx, 1e-10))
                w = math.exp(-BETA * theta * theta)
                amps[j] += ai * cmath.exp(1j * K * act) * w / L

    return amps


def _centroid_y(amps: Sequence[complex], positions: Sequence[Tuple[float, float, float]], det: Sequence[int]) -> float:
    total = 0.0
    weighted = 0.0
    for d in det:
        p = abs(amps[d]) ** 2
        total += p
        weighted += p * positions[d][1]
    return weighted / total if total > 1e-30 else 0.0


def _detector_probs(amps: Sequence[complex], det: Sequence[int]) -> Dict[int, float]:
    raw = {d: abs(amps[d]) ** 2 for d in det}
    total = sum(raw.values())
    if total <= 1e-30:
        return {d: 0.0 for d in det}
    return {d: p / total for d, p in raw.items()}


def _normalized_distribution(probs: Dict[int, float]) -> bool:
    return (
        bool(probs)
        and all(math.isfinite(p) and p >= 0.0 for p in probs.values())
        and math.isclose(sum(probs.values()), 1.0, rel_tol=0.0, abs_tol=1e-12)
    )


def _mass_window_gain(
    probs_mass: Dict[int, float],
    probs_free: Dict[int, float],
    positions: Sequence[Tuple[float, float, float]],
    det: Sequence[int],
    y_mass: float,
    half_width: float = 1.5,
) -> float:
    gain = 0.0
    for d in det:
        if abs(positions[d][1] - y_mass) <= half_width:
            gain += probs_mass[d] - probs_free[d]
    return gain


def _fit_power(xs: Sequence[float], ys: Sequence[float]) -> float:
    if len(xs) < 2:
        return math.nan
    lx = [math.log(x) for x in xs if x > 0]
    ly = [math.log(y) for y in ys if y > 0]
    if len(lx) != len(xs) or len(ly) != len(ys):
        return math.nan
    mx = sum(lx) / len(lx)
    my = sum(ly) / len(ly)
    sxx = sum((x - mx) ** 2 for x in lx)
    if sxx < 1e-30:
        return math.nan
    sxy = sum((x - mx) * (y - my) for x, y in zip(lx, ly))
    return sxy / sxx


def _mass_index_for_label(layer_nodes: Sequence[int], y_mass: int) -> int | None:
    """Return the stable `(y_label, z_label) = (y_mass, 0)` site.

    Every graph family preserves the square grid-label ordering within a
    layer even when its embedded coordinates drift.  Selecting by that stable
    ordering keeps the source identity and trial panel fixed across jitter and
    across the same-coordinate templated/K-NN comparison.
    """
    span = math.isqrt(len(layer_nodes))
    if span * span != len(layer_nodes) or span % 2 != 1:
        return None
    half = (span - 1) // 2
    if not -half <= y_mass <= half:
        return None
    return layer_nodes[(y_mass + half) * span + half]


def _measure_family(graph: GraphFamily, mass_strengths: Sequence[float], y_masses: Sequence[int]) -> dict:
    positions = graph.positions
    layers = graph.layers
    adj = graph.adj
    det = layers[-1]
    bl = len(layers) // 3
    gl = 2 * len(layers) // 3
    barrier = layers[bl]
    blocked = _blocked_barrier(barrier, positions)
    field0 = [0.0] * len(positions)

    free = _propagate(positions, layers, adj, field0, blocked)
    free_probs = _detector_probs(free, det)
    normalization_ok = _normalized_distribution(free_probs)

    toward = 0
    total = 0
    mass_deltas: List[float] = []
    scale_deltas: List[float] = []

    for y_mass in y_masses:
        mass_idx = _mass_index_for_label(layers[gl], y_mass)
        if mass_idx is None:
            continue

        for strength in mass_strengths:
            field = _field_for_mass(positions, mass_idx, strength * FIELD_STRENGTH)
            mass = _propagate(positions, layers, adj, field, blocked)
            mass_probs = _detector_probs(mass, det)
            normalization_ok &= _normalized_distribution(mass_probs)
            delta = _mass_window_gain(mass_probs, free_probs, positions, det, float(y_mass))
            if strength == mass_strengths[len(mass_strengths) // 2]:
                mass_deltas.append(delta)
            if delta > 0:
                toward += 1
            total += 1

        # Estimate the mass-scaling exponent from the fixed z_mass, using the
        # same strength sweep for every family.
        scale_series = []
        for strength in mass_strengths:
            field = _field_for_mass(positions, mass_idx, strength * FIELD_STRENGTH)
            mass = _propagate(positions, layers, adj, field, blocked)
            mass_probs = _detector_probs(mass, det)
            normalization_ok &= _normalized_distribution(mass_probs)
            delta = _mass_window_gain(mass_probs, free_probs, positions, det, float(y_mass))
            scale_series.append(max(delta, 1e-30))
        scale_deltas.append(_fit_power(mass_strengths, scale_series))

    fpm = sum(v for v in scale_deltas if not math.isnan(v)) / max(
        1, sum(1 for v in scale_deltas if not math.isnan(v))
    )
    mean_delta = sum(mass_deltas) / len(mass_deltas) if mass_deltas else math.nan
    toward_frac = toward / total if total else math.nan
    return {
        "toward_frac": toward_frac,
        "mean_delta": mean_delta,
        "fpm": fpm,
        "free_centroid": _centroid_y(free, positions, det),
        "trial_count": total,
        "normalization_ok": normalization_ok,
    }


def _jitter_sweep(base: GraphFamily) -> List[Tuple[float, dict]]:
    rows = []
    for jitter in JITTER_SWEEP:
        acc = []
        for seed in SEEDS:
            graph = _jitter_positions(base, jitter=jitter, seed=seed)
            acc.append(_measure_family(graph, MASS_STRENGTHS, Y_MASSES))
        rows.append(
            (
                jitter,
                {
                    "toward_frac": sum(r["toward_frac"] for r in acc) / len(acc),
                    "mean_delta": sum(r["mean_delta"] for r in acc) / len(acc),
                    "fpm": sum(r["fpm"] for r in acc) / len(acc),
                    "trial_count": sum(r["trial_count"] for r in acc),
                    "normalization_ok": all(r["normalization_ok"] for r in acc),
                },
            )
        )
    return rows


def _architecture_suite() -> List[Tuple[str, dict]]:
    base = _build_fixed_connectivity(N_LAYERS, HALF)
    ordered = base
    jittered = _jitter_positions(base, jitter=0.5, seed=5)
    templated = _templated_growth(N_LAYERS, HALF, drift=0.22, seed=5, snap=False)
    knn = _knn_growth(N_LAYERS, HALF, drift=0.22, k=9, seed=5)
    snapped = _templated_growth(N_LAYERS, HALF, drift=0.22, seed=5, snap=True)
    fams = [
        ("ordered lattice", ordered),
        ("jittered lattice", jittered),
        ("templated growth", templated),
        ("K-NN grown", knn),
        ("snapped/grid-like", snapped),
    ]

    rows = []
    for name, graph in fams:
        acc = []
        for seed in SEEDS:
            if name == "ordered lattice":
                g = base
            elif name == "jittered lattice":
                g = _jitter_positions(base, jitter=0.5, seed=seed)
            elif name == "templated growth":
                g = _templated_growth(N_LAYERS, HALF, drift=0.22, seed=seed, snap=False)
            elif name == "K-NN grown":
                g = _knn_growth(N_LAYERS, HALF, drift=0.22, k=9, seed=seed)
            else:
                g = _templated_growth(N_LAYERS, HALF, drift=0.22, seed=seed, snap=True)
            acc.append(_measure_family(g, MASS_STRENGTHS, Y_MASSES))
        rows.append(
            (
                name,
                {
                    "toward_frac": sum(r["toward_frac"] for r in acc) / len(acc),
                    "mean_delta": sum(r["mean_delta"] for r in acc) / len(acc),
                    "fpm": sum(r["fpm"] for r in acc) / len(acc),
                    "trial_count": sum(r["trial_count"] for r in acc),
                    "normalization_ok": all(r["normalization_ok"] for r in acc),
                },
            )
        )
    return rows


def _finite_harness_checks(
    base: GraphFamily,
    jitter_rows: Sequence[Tuple[float, dict]],
    architecture_rows: Sequence[Tuple[str, dict]],
) -> None:
    """Check the exact finite statements promoted by the source note."""
    print()
    print("Finite-harness theorem checks")
    print("-" * 40)

    jitter_keeps_adjacency = all(
        _jitter_positions(base, jitter=jitter, seed=seed).adj == base.adj
        for jitter in JITTER_SWEEP
        for seed in SEEDS
    )
    _check(
        "fixed-connectivity jitter changes coordinates but never adjacency",
        jitter_keeps_adjacency,
    )

    stable_mass_panel = all(
        _mass_index_for_label(graph.layers[2 * len(graph.layers) // 3], y_mass) is not None
        for graph in (
            *(_jitter_positions(base, jitter=jitter, seed=seed) for jitter in JITTER_SWEEP for seed in SEEDS),
            *(_templated_growth(N_LAYERS, HALF, drift=0.22, seed=seed, snap=False) for seed in SEEDS),
            *(_knn_growth(N_LAYERS, HALF, drift=0.22, k=9, seed=seed) for seed in SEEDS),
            *(_templated_growth(N_LAYERS, HALF, drift=0.22, seed=seed, snap=True) for seed in SEEDS),
        )
        for y_mass in Y_MASSES
    )
    _check("all graph rows keep the same three stable mass-label sites", stable_mass_panel)

    paired_positions_match = True
    paired_adjacencies_differ = True
    for seed in SEEDS:
        templated = _templated_growth(N_LAYERS, HALF, drift=0.22, seed=seed, snap=False)
        knn = _knn_growth(N_LAYERS, HALF, drift=0.22, k=9, seed=seed)
        paired_positions_match &= templated.positions == knn.positions and templated.layers == knn.layers
        paired_adjacencies_differ &= templated.adj != knn.adj
    _check(
        "templated and K-NN rows use identical unsnapped coordinates seed by seed",
        paired_positions_match,
    )
    _check(
        "templated fixed-offset and K-NN distance-recomputed adjacencies differ",
        paired_adjacencies_differ,
    )

    _check(
        "every displayed row contains 54 trials with normalized terminal weights",
        all(row["trial_count"] == 54 and row["normalization_ok"] for _, row in jitter_rows)
        and all(row["trial_count"] == 54 and row["normalization_ok"] for _, row in architecture_rows),
    )

    jitter_display = [
        (f"{jitter:.2f}", f"{row['toward_frac']*100:.1f}%", f"{row['mean_delta']:+.6f}", f"{row['fpm']:.2f}")
        for jitter, row in jitter_rows
    ]
    expected_jitter_display = [
        ("0.00", "66.7%", "+0.000012", "0.66"),
        ("0.10", "55.6%", "+0.000003", "0.55"),
        ("0.20", "61.1%", "+0.000010", "0.61"),
        ("0.30", "55.6%", "+0.000014", "0.56"),
        ("0.40", "55.6%", "+0.000008", "0.55"),
        ("0.50", "72.2%", "+0.000007", "0.72"),
    ]
    _check("computed jitter rows match the frozen displayed table", jitter_display == expected_jitter_display)

    architecture_display = [
        (name, f"{row['toward_frac']*100:.1f}%", f"{row['mean_delta']:+.6f}", f"{row['fpm']:.2f}")
        for name, row in architecture_rows
    ]
    expected_architecture_display = [
        ("ordered lattice", "66.7%", "+0.000012", "0.66"),
        ("jittered lattice", "72.2%", "+0.000007", "0.72"),
        ("templated growth", "50.0%", "+0.000013", "0.50"),
        ("K-NN grown", "61.1%", "+0.000013", "0.61"),
        ("snapped/grid-like", "50.0%", "+0.000003", "0.50"),
    ]
    _check(
        "computed architecture rows match the frozen displayed table",
        architecture_display == expected_architecture_display,
    )

    architecture_map = {name: row for name, row in architecture_rows}
    templated_summary = architecture_map["templated growth"]
    knn_summary = architecture_map["K-NN grown"]
    _check(
        "same-coordinate adjacency replacement changes a reported finite functional",
        not math.isclose(
            templated_summary["toward_frac"],
            knn_summary["toward_frac"],
            rel_tol=0.0,
            abs_tol=1e-15,
        )
        or not math.isclose(
            templated_summary["mean_delta"],
            knn_summary["mean_delta"],
            rel_tol=0.0,
            abs_tol=1e-15,
        )
        or not math.isclose(
            templated_summary["fpm"],
            knn_summary["fpm"],
            rel_tol=0.0,
            abs_tol=1e-15,
        ),
    )

    toward_series = [row[1]["toward_frac"] for row in jitter_rows]
    monotone_nonincreasing = all(a >= b for a, b in zip(toward_series, toward_series[1:]))
    _check("fixed-stencil TOWARD series is not monotonically decreasing", not monotone_nonincreasing)


def main() -> None:
    base = _build_fixed_connectivity(N_LAYERS, HALF)
    jitter_rows = _jitter_sweep(base)
    architecture_rows = _architecture_suite()
    print("=" * 88)
    print("GATE B FINITE CONNECTIVITY COMPARISON")
    print("  Declared valley-linear algorithm on layered 3D graphs")
    print("  Question: what changes under coordinate jitter and same-coordinate adjacency replacement?")
    print("=" * 88)
    print()
    print(
        f"Setup: layers={N_LAYERS}, half-width={HALF}, mass strengths={MASS_STRENGTHS}, "
        f"mass y targets={Y_MASSES}"
    )
    print("Action definition: S = L(1-f), finite 3D forward propagation")
    print()

    print("Jitter sweep on fixed connectivity")
    print(f"  {'jitter':>6s}  {'toward':>8s}  {'mean_delta':>11s}  {'F~M':>6s}")
    print(f"  {'-' * 40}")
    for jitter, row in jitter_rows:
        print(
            f"  {jitter:6.2f}  {row['toward_frac']*100:7.1f}%  "
            f"{row['mean_delta']:+11.6f}  {row['fpm']:6.2f}"
        )

    print()
    print("Architecture comparison")
    print(f"  {'architecture':>18s}  {'toward':>8s}  {'mean_delta':>11s}  {'F~M':>6s}")
    print(f"  {'-' * 52}")
    for name, row in architecture_rows:
        print(
            f"  {name:18s}  {row['toward_frac']*100:7.1f}%  "
            f"{row['mean_delta']:+11.6f}  {row['fpm']:6.2f}"
        )

    print()
    print("Interpretation:")
    print("  - The fixed-stencil jitter rows show no monotone TOWARD collapse on the tested sweep.")
    print("  - Same-coordinate templated and K-NN rows isolate finite adjacency dependence.")
    print("  - TOWARD and F~M are declared finite functionals, not physical observables.")
    print("  - This is a bounded finite-harness theorem, not Gate B dynamics closure.")
    _finite_harness_checks(base, jitter_rows, architecture_rows)
    _source_boundary_checks()
    print(f"BOUNDARY_CHECKS: PASS={CHECK_PASS} FAIL={CHECK_FAIL}")
    if CHECK_FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
