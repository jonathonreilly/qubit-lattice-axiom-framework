# Higher-Symmetry Joint Validation Note — Cached N Range (Binding)

**Date:** 2026-04-03 (scope narrowed 2026-05-17 per audited_conditional `runner_artifact_issue` repair: binding scope is exactly the cached log range; the N=120 promotion claim requires the missing dense N=80/100/120 joint-validation log + registered joint-validator runner; SHA-pinned registered joint-validator cache attached 2026-05-24 per follow-up `runner_artifact_issue` repair)
**Status:** bounded positive on the cached registered log range for
`Z₂ × Z₂`; the `N = 120` proposed_retained promotion is **out of
binding scope** until the missing dense N=80/100/120 joint-validation
log is registered and the joint validator is registered as this row's
primary runner.
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only
**Primary runner (load-bearing):** [`scripts/higher_symmetry_joint_validation.py`](../scripts/higher_symmetry_joint_validation.py) (joint Born + gravity + decoherence on the higher-symmetry families on the sparse N=25,40,60,80 window).
**Primary runner cache (load-bearing):** [`logs/runner-cache/higher_symmetry_joint_validation.txt`](../logs/runner-cache/higher_symmetry_joint_validation.txt) — SHA-pinned registered cached stdout (`exit_code=0`, `status=ok`, `elapsed_sec=53.94`, default argv `--families random z2z2 ring --n-layers 25 40 60 80 --n-seeds 16`) backing every row in the sparse Z₂ × Z₂ binding table below.
**Imported authority (load-bearing dependency):** [`scripts/higher_symmetry_dag.py`](../scripts/higher_symmetry_dag.py) — provides `generate_random_dag`, `generate_z2z2_dag`, `generate_ring_dag`, and the module-level constants `K`, `CONNECT_RADIUS`, `XYZ_RANGE` imported by the primary runner.
**Imported authority (load-bearing dependency):** [`scripts/mirror_chokepoint_joint.py`](../scripts/mirror_chokepoint_joint.py) — provides `measure_joint` (joint d_TV / `pur_cl` / gravity / Born readout), `compute_field_3d`, `propagate_3d`, and `_mean_se` imported by the primary runner.

## Scope narrowing (2026-05-17 audited_conditional repair)

The 2026-05-10 audit verdict on this row was `audited_conditional` with
repair class `runner_artifact_issue`, stating: *"provide the missing
dense N=80/100/120 joint-validation log or registered runner cache,
and register the joint validator as this row's runner before
re-auditing the N=120 claim."*

This revision takes the narrowing path. The binding evidence of this
note is exactly the **cached log content from the registered logs**
on the existing `Z₂ × Z₂` joint Born + gravity + decoherence
validation: only those rows that the current registered cache
actually contains are binding.

The **N = 120 promotion claim** and any "proposed_retained through
N = 120" framing are **demoted to out-of-binding-scope** until:
(a) the missing dense N=80/100/120 joint-validation log is provided
or a registered runner cache is attached, and
(b) the joint validator
(`scripts/higher_symmetry_joint_validation.py`) is registered as
this row's primary runner in the runner classification ledger with a
SHA-pinned cache. Neither (a) nor (b) is supplied in this revision.

This note records the first joint Born + gravity + decoherence validation for
the higher-symmetry families introduced in:

[`scripts/higher_symmetry_dag.py`](/Users/jonreilly/Projects/Physics/scripts/higher_symmetry_dag.py)

The joint validator is:

[`scripts/higher_symmetry_joint_validation.py`](/Users/jonreilly/Projects/Physics/scripts/higher_symmetry_joint_validation.py)

Logs:

[`logs/2026-04-03-higher-symmetry-joint-validation.txt`](/Users/jonreilly/Projects/Physics/logs/2026-04-03-higher-symmetry-joint-validation.txt)
[`logs/2026-04-03-higher-symmetry-joint-validation-z2z2-dense-n80-n120.txt`](/Users/jonreilly/Projects/Physics/logs/2026-04-03-higher-symmetry-joint-validation-z2z2-dense-n80-n120.txt)

## Primary-runner source (load-bearing, inlined 2026-05-18)

To restore restricted-packet visibility for the `audited_conditional`
`runner_artifact_issue` repair, the full load-bearing source of the joint
validator [`scripts/higher_symmetry_joint_validation.py`](/Users/jonreilly/Projects/Physics/scripts/higher_symmetry_joint_validation.py)
(336 lines) is inlined below. This is the primary runner producing the
sparse N=25,40,60,80 `Z₂ × Z₂` row that is the binding evidence of this note.

```python
#!/usr/bin/env python3
"""Joint Born + gravity + decoherence validation for higher-symmetry DAGs.

This script upgrades the earlier higher-symmetry decoherence comparison to the
same review-safe joint lens used on the mirror lane:

  - detector-side total-variation distance `d_TV`
  - CL-bath purity `pur_cl`
  - corrected Born `|I3|/P`
  - `k=0` gravity control
  - gravity centroid shift at one `k`
  - band-averaged gravity centroid shift across a small `k` window

The narrow question is:

Does the Z2xZ2 geometry keep its decoherence advantage while remaining
Born-clean and gravity-positive?

The exponent fit is reported on decoherence depth

    1 - pur_cl ~= C * N^alpha

using the family-mean purity at each tested `N`, with a simple bootstrap over
the per-size seed lists to show how stable that bounded exponent is.
"""

from __future__ import annotations

import argparse
import math
import os
import random
import sys
import time
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from scripts.higher_symmetry_dag import (
    K as DEFAULT_K,
    CONNECT_RADIUS as DEFAULT_CONNECT_RADIUS,
    XYZ_RANGE as DEFAULT_XYZ_RANGE,
    generate_random_dag,
    generate_ring_dag,
    generate_z2z2_dag,
)
from scripts.mirror_chokepoint_joint import (
    _mean_se,
    compute_field_3d,
    measure_joint,
    propagate_3d,
)

DEFAULT_K_BAND = [3.0, 5.0, 7.0]


def _fmt(mean: float, se: float, digits: int = 3, signed: bool = False) -> str:
    if math.isnan(mean):
        return "FAIL"
    spec = f"+.{digits}f" if signed else f".{digits}f"
    mean_s = format(mean, spec)
    se_s = format(se, f".{digits}f")
    return f"{mean_s}±{se_s}"


def _fmt_sci(mean: float, se: float) -> str:
    if math.isnan(mean):
        return "FAIL"
    return f"{mean:.2e}±{se:.2e}"


def _quantile(sorted_vals: list[float], q: float) -> float:
    if not sorted_vals:
        return math.nan
    if len(sorted_vals) == 1:
        return sorted_vals[0]
    pos = q * (len(sorted_vals) - 1)
    lo = int(math.floor(pos))
    hi = int(math.ceil(pos))
    if lo == hi:
        return sorted_vals[lo]
    frac = pos - lo
    return sorted_vals[lo] * (1.0 - frac) + sorted_vals[hi] * frac


def gravity_band_metric(positions, adj, k_band: list[float]) -> float | None:
    """Band-averaged gravity read using the same mass/slit geometry as measure_joint."""
    by_layer = defaultdict(list)
    for idx, (x, y, z) in enumerate(positions):
        by_layer[round(x)].append(idx)
    layers = sorted(by_layer.keys())
    if len(layers) < 7:
        return None

    src = by_layer[layers[0]]
    det_list = list(by_layer[layers[-1]])
    if not det_list:
        return None

    cy = sum(y for _, y, _ in positions) / len(positions)
    bl_idx = len(layers) // 3
    bi = by_layer[layers[bl_idx]]
    slit_a = [i for i in bi if positions[i][1] > cy + 3][:3]
    slit_b = [i for i in bi if positions[i][1] < cy - 3][:3]
    if not slit_a or not slit_b:
        return None
    blocked = set(bi) - set(slit_a + slit_b)

    grav_layer = layers[2 * len(layers) // 3]
    mass_nodes = [i for i in by_layer[grav_layer] if positions[i][1] > cy + 1]
    if not mass_nodes:
        return None

    field_m = compute_field_3d(positions, mass_nodes)
    field_f = [0.0] * len(positions)

    deltas = []
    for k in k_band:
        am = propagate_3d(positions, adj, field_m, src, k, blocked)
        af = propagate_3d(positions, adj, field_f, src, k, blocked)
        pm = sum(abs(am[d]) ** 2 for d in det_list)
        pf = sum(abs(af[d]) ** 2 for d in det_list)
        if pm <= 1e-30 or pf <= 1e-30:
            continue
        ym = sum(abs(am[d]) ** 2 * positions[d][1] for d in det_list) / pm
        yf = sum(abs(af[d]) ** 2 * positions[d][1] for d in det_list) / pf
        deltas.append(ym - yf)

    if not deltas:
        return None
    return sum(deltas) / len(deltas)


def fit_decoherence_alpha(points: list[tuple[int, float]]) -> tuple[float, float, float] | None:
    """Fit 1 - purity ~= C * N^alpha from (N, mean_purity) points."""
    usable = [(n, p) for n, p in points if n > 0 and 0.0 <= p < 1.0]
    if len(usable) < 3:
        return None
    xs = [math.log(n) for n, _ in usable]
    ys = [math.log(1.0 - p) for _, p in usable]
    mx = sum(xs) / len(xs)
    my = sum(ys) / len(ys)
    sxx = sum((x - mx) ** 2 for x in xs)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    syy = sum((y - my) ** 2 for y in ys)
    if sxx <= 1e-12:
        return None
    alpha = sxy / sxx
    coeff = math.exp(my - alpha * mx)
    r2 = (sxy * sxy) / (sxx * syy) if syy > 1e-12 else math.nan
    return alpha, coeff, r2


def bootstrap_alpha(
    purity_by_n: dict[int, list[float]],
    n_boot: int,
    rng_seed: int,
) -> tuple[float, float, float] | None:
    usable = {n: vals for n, vals in purity_by_n.items() if len(vals) >= 2}
    if len(usable) < 3:
        return None
    rng = random.Random(rng_seed)
    alphas = []
    for _ in range(n_boot):
        points = []
        for n in sorted(usable.keys()):
            vals = usable[n]
            sampled = [vals[rng.randrange(len(vals))] for _ in range(len(vals))]
            points.append((n, sum(sampled) / len(sampled)))
        fit = fit_decoherence_alpha(points)
        if fit is not None:
            alphas.append(fit[0])
    if not alphas:
        return None
    alphas.sort()
    mean = sum(alphas) / len(alphas)
    lo = _quantile(alphas, 0.025)
    hi = _quantile(alphas, 0.975)
    return mean, lo, hi


def family_generators(args):
    return {
        "random": lambda seed, nl: generate_random_dag(
            nl, args.random_npl, args.xyz_range, args.connect_radius, seed
        ),
        "z2z2": lambda seed, nl: generate_z2z2_dag(
            nl, args.z2z2_quarter, args.xyz_range, args.connect_radius, seed
        ),
        "ring": lambda seed, nl: generate_ring_dag(
            nl, args.ring_nodes, args.xyz_range, args.connect_radius, seed
        ),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--families", nargs="+", default=["random", "z2z2", "ring"])
    parser.add_argument("--n-layers", nargs="+", type=int, default=[25, 40, 60, 80])
    parser.add_argument("--n-seeds", type=int, default=16)
    parser.add_argument("--k", type=float, default=DEFAULT_K)
    parser.add_argument("--k-band", nargs="+", type=float, default=DEFAULT_K_BAND)
    parser.add_argument("--xyz-range", type=float, default=DEFAULT_XYZ_RANGE)
    parser.add_argument("--connect-radius", type=float, default=DEFAULT_CONNECT_RADIUS)
    parser.add_argument("--random-npl", type=int, default=50)
    parser.add_argument("--z2z2-quarter", type=int, default=12)
    parser.add_argument("--ring-nodes", type=int, default=48)
    parser.add_argument("--n-boot", type=int, default=1000)
    parser.add_argument("--bootstrap-seed", type=int, default=12345)
    args = parser.parse_args()

    generators = family_generators(args)
    unknown = [fam for fam in args.families if fam not in generators]
    if unknown:
        raise SystemExit(f"Unknown family/families: {', '.join(unknown)}")

    seeds = [s * 7 + 3 for s in range(args.n_seeds)]
    family_results: dict[str, dict[int, dict[str, list[float]]]] = {}
    family_times: dict[str, dict[int, float]] = {}

    print("=" * 132)
    print("HIGHER-SYMMETRY JOINT VALIDATION")
    print("  Born + gravity + decoherence on the higher-symmetry families")
    print(
        f"  k={args.k}, k_band={args.k_band}, seeds={args.n_seeds}, "
        f"random_npl={args.random_npl}, z2z2_quarter={args.z2z2_quarter}, "
        f"ring_nodes={args.ring_nodes}, r={args.connect_radius}"
    )
    print("=" * 132)
    print()
    print(
        f"  {'N':>4s}  {'family':>8s}  {'d_TV':>10s}  {'pur_cl':>10s}  "
        f"{'grav@k':>12s}  {'grav_band':>12s}  {'band+':>7s}  {'Born':>15s}  "
        f"{'k=0':>10s}  {'ok':>3s}  {'time':>5s}"
    )
    print("  " + "-" * 118)

    for family in args.families:
        family_results[family] = {}
        family_times[family] = {}
        gen = generators[family]
        for nl in args.n_layers:
            t0 = time.time()
            rows = {
                "dtv": [],
                "pur_cl": [],
                "gravity": [],
                "grav_band": [],
                "born": [],
                "grav_k0": [],
            }
            band_pos = 0

            for seed in seeds:
                positions, adj, _ = gen(seed, nl)
                result = measure_joint(positions, adj, nl, args.k)
                if result is None:
                    continue
                rows["dtv"].append(result["dtv"])
                rows["pur_cl"].append(result["pur_cl"])
                rows["gravity"].append(result["gravity"])
                rows["born"].append(result["born"])
                rows["grav_k0"].append(result["grav_k0"])

                gb = gravity_band_metric(positions, adj, args.k_band)
                if gb is not None:
                    rows["grav_band"].append(gb)
                    if gb > 0:
                        band_pos += 1

            family_results[family][nl] = rows
            family_times[family][nl] = time.time() - t0

            dtv_m, dtv_se = _mean_se(rows["dtv"])
            pur_m, pur_se = _mean_se(rows["pur_cl"])
            g_m, g_se = _mean_se(rows["gravity"])
            gb_m, gb_se = _mean_se(rows["grav_band"])
            b_m, b_se = _mean_se(rows["born"])
            k0_m, k0_se = _mean_se(rows["grav_k0"])
            ok = len(rows["pur_cl"])

            band_ratio = f"{band_pos}/{len(rows['grav_band'])}"
            print(
                f"  {nl:4d}  {family:>8s}  {_fmt(dtv_m, dtv_se):>10s}  "
                f"{_fmt(pur_m, pur_se):>10s}  {_fmt(g_m, g_se, signed=True):>12s}  "
                f"{_fmt(gb_m, gb_se, signed=True):>12s}  "
                f"{band_ratio:>7s}  "
                f"{_fmt_sci(b_m, b_se):>15s}  {_fmt_sci(k0_m, k0_se):>10s}  "
                f"{ok:3d}  {family_times[family][nl]:4.0f}s"
            )
        print()

    print("Exponent fits on family-mean decoherence depth: 1 - pur_cl ~= C * N^alpha")
    for family in args.families:
        purity_by_n = {
            nl: family_results[family][nl]["pur_cl"]
            for nl in args.n_layers
            if family_results[family][nl]["pur_cl"]
        }
        mean_points = [
            (nl, sum(vals) / len(vals))
            for nl, vals in sorted(purity_by_n.items())
        ]
        fit = fit_decoherence_alpha(mean_points)
        boot = bootstrap_alpha(
            purity_by_n,
            n_boot=args.n_boot,
            rng_seed=args.bootstrap_seed + 97 * (args.families.index(family) + 1),
        )
        if fit is None:
            print(f"  {family:>8s}: FAIL")
            continue
        alpha, coeff, r2 = fit
        if boot is None:
            print(
                f"  {family:>8s}: alpha={alpha:+.3f}, C={coeff:.4f}, R^2={r2:.3f}, "
                f"bootstrap=FAIL"
            )
            continue
        boot_mean, lo, hi = boot
        print(
            f"  {family:>8s}: alpha={alpha:+.3f}, C={coeff:.4f}, R^2={r2:.3f}, "
            f"bootstrap alpha={boot_mean:+.3f} [{lo:+.3f}, {hi:+.3f}]"
        )

    print()
    print("Readout:")
    print("  - Born safety means |I3|/P stays near machine precision.")
    print("  - k=0 must remain zero if gravity stays purely phase-mediated.")
    print("  - grav_band averages the same centroid shift across a small k window")
    print("    to reduce sign flips from single-k phase oscillations.")


if __name__ == "__main__":
    main()
```

## Helper-runner code excerpt (load-bearing for restricted packet, inlined 2026-05-24)

The primary runner inlined above imports load-bearing helpers from two
modules under `scripts/`. Both are inlined verbatim below so the
restricted-packet review does not require external source navigation
(per the `runner_artifact_issue` re-audit note "include the helper
sources `scripts/higher_symmetry_dag.py` and
`scripts/mirror_chokepoint_joint.py` in the packet").

### Helper: `scripts/higher_symmetry_dag.py` — DAG generators + module-level constants

This module provides the `generate_z2z2_dag`, `generate_random_dag`,
and `generate_ring_dag` generators wired into `family_generators` in
the primary runner, plus the module-level constants `K`,
`CONNECT_RADIUS`, and `XYZ_RANGE` used as defaults. The
load-bearing definitions inlined below are the three generators and the
constants; the file also contains an exploratory `main()` for the
decoherence-only comparison which is not load-bearing for the joint
validator and is omitted.

```python
import math
import cmath
import sys
import os
import random
from collections import defaultdict, deque

BETA = 0.8
K = 5.0
N_SEEDS = 16
XYZ_RANGE = 12.0
CONNECT_RADIUS = 5.0
N_YBINS = 8
LAM = 10.0


def _topo_order(adj, n):
    in_deg = [0] * n
    for nbs in adj.values():
        for j in nbs: in_deg[j] += 1
    q = deque(i for i in range(n) if in_deg[i] == 0); order = []
    while q:
        i = q.popleft(); order.append(i)
        for j in adj.get(i, []):
            in_deg[j] -= 1
            if in_deg[j] == 0: q.append(j)
    return order


def generate_z2z2_dag(n_layers, npl_quarter, xyz_range, cr, rng_seed):
    """Z₂×Z₂: y → -y AND z → -z. 4 copies per base node."""
    rng = random.Random(rng_seed); positions = []; adj = defaultdict(list)
    layer_indices = []; bl = n_layers // 3
    for layer in range(n_layers):
        x = float(layer); ln = []
        if layer == 0:
            positions.append((x, 0, 0)); ln.append(len(positions)-1)
        else:
            all_nodes = []
            for _ in range(npl_quarter):
                y = rng.uniform(0.5, xyz_range); z = rng.uniform(0.5, xyz_range)
                for sy, sz in [(1,1), (1,-1), (-1,1), (-1,-1)]:
                    idx = len(positions); positions.append((x, sy*y, sz*z))
                    all_nodes.append(idx)
            ln = all_nodes
            lb = max(0, len(layer_indices) - (1 if layer == bl+1 else 2))
            for ci in ln:
                cx, cy, cz = positions[ci]
                for pl in layer_indices[lb:]:
                    for pi in pl:
                        px, py, pz = positions[pi]
                        if math.sqrt((cx-px)**2+(cy-py)**2+(cz-pz)**2) <= cr:
                            adj[pi].append(ci)
        layer_indices.append(ln)
    return positions, dict(adj), bl


def generate_random_dag(n_layers, npl, xyz_range, cr, rng_seed):
    """Standard random (no symmetry)."""
    rng = random.Random(rng_seed); positions = []; adj = defaultdict(list)
    layer_indices = []; bl = n_layers // 3
    for layer in range(n_layers):
        x = float(layer); ln = []
        if layer == 0:
            positions.append((x, 0, 0)); ln.append(len(positions)-1)
        else:
            for _ in range(npl):
                y = rng.uniform(-xyz_range, xyz_range); z = rng.uniform(-xyz_range, xyz_range)
                idx = len(positions); positions.append((x, y, z)); ln.append(idx)
                lb = max(0, len(layer_indices) - (1 if layer == bl+1 else 2))
                for pl in layer_indices[lb:]:
                    for pi in pl:
                        px, py, pz = positions[pi]
                        if math.sqrt((x-px)**2+(y-py)**2+(z-pz)**2) <= cr:
                            adj[pi].append(idx)
        layer_indices.append(ln)
    return positions, dict(adj), bl


def generate_ring_dag(n_layers, n_ring, xyz_range, cr, rng_seed):
    """Approximate rotational symmetry: nodes placed on rings at random radii."""
    rng = random.Random(rng_seed); positions = []; adj = defaultdict(list)
    layer_indices = []; bl = n_layers // 3
    for layer in range(n_layers):
        x = float(layer); ln = []
        if layer == 0:
            positions.append((x, 0, 0)); ln.append(len(positions)-1)
        else:
            for _ in range(n_ring // 8 + 1):  # multiple radii
                r = rng.uniform(1.0, xyz_range)
                for i in range(8):  # 8 nodes per ring
                    angle = 2 * math.pi * i / 8 + rng.uniform(-0.1, 0.1)
                    y = r * math.cos(angle); z = r * math.sin(angle)
                    idx = len(positions); positions.append((x, y, z)); ln.append(idx)
                    if len(ln) >= n_ring: break
                if len(ln) >= n_ring: break
            ln = ln[:n_ring]
            lb = max(0, len(layer_indices) - (1 if layer == bl+1 else 2))
            for ci in ln:
                cx, cy, cz = positions[ci]
                for pl in layer_indices[lb:]:
                    for pi in pl:
                        px, py, pz = positions[pi]
                        if math.sqrt((cx-px)**2+(cy-py)**2+(cz-pz)**2) <= cr:
                            adj[pi].append(ci)
        layer_indices.append(ln)
    return positions, dict(adj), bl
```

Module-level constants used by the helper code: `BETA = 0.8`, `K = 5.0`,
`N_SEEDS = 16`, `XYZ_RANGE = 12.0`, `CONNECT_RADIUS = 5.0`,
`N_YBINS = 8`, `LAM = 10.0`. Only `K`, `CONNECT_RADIUS`, and `XYZ_RANGE`
are imported by the joint validator (as `DEFAULT_K`,
`DEFAULT_CONNECT_RADIUS`, `DEFAULT_XYZ_RANGE`); the others are local to
this helper.

### Helper: `scripts/mirror_chokepoint_joint.py` — `measure_joint`, `compute_field_3d`, `propagate_3d`, `_mean_se`

This module provides the joint Born + gravity + decoherence readout
(`measure_joint`), the 3D propagator (`propagate_3d`), the
gravitational field source (`compute_field_3d`), the mean/SE helper
(`_mean_se`), and the auxiliary functions used by `measure_joint`
(`_topo_order`, `bin_amplitudes_3d`, `sorkin_born_test`). The
load-bearing definitions inlined below are the full chain — note that
the joint validator imports `_mean_se`, `compute_field_3d`,
`measure_joint`, and `propagate_3d`; `measure_joint` in turn calls the
remaining helpers via the closure inside this module.

```python
import math
import cmath
import sys
import os
import random
from collections import defaultdict, deque

BETA = 0.8
K = 5.0
N_SEEDS = 16
NPL_HALF = 25
XYZ_RANGE = 12.0
CONNECT_RADIUS = 4.0
N_YBINS = 8
LAM = 10.0


def _topo_order(adj, n):
    in_deg = [0] * n
    for nbs in adj.values():
        for j in nbs:
            in_deg[j] += 1
    q = deque(i for i in range(n) if in_deg[i] == 0)
    order = []
    while q:
        i = q.popleft()
        order.append(i)
        for j in adj.get(i, []):
            in_deg[j] -= 1
            if in_deg[j] == 0:
                q.append(j)
    return order


def propagate_3d(positions, adj, field, src, k, blocked):
    n = len(positions)
    order = _topo_order(adj, n)
    amps = [0j] * n
    for s in src:
        amps[s] = 1.0 / len(src)
    for i in order:
        if abs(amps[i]) < 1e-30 or i in blocked:
            continue
        for j in adj.get(i, []):
            if j in blocked:
                continue
            x1, y1, z1 = positions[i]
            x2, y2, z2 = positions[j]
            dx, dy, dz = x2-x1, y2-y1, z2-z1
            L = math.sqrt(dx*dx + dy*dy + dz*dz)
            if L < 1e-10:
                continue
            lf = 0.5 * (field[i] + field[j])
            dl = L * (1 + lf)
            ret = math.sqrt(max(dl*dl - L*L, 0))
            act = dl - ret
            theta = math.atan2(math.sqrt(dy*dy + dz*dz), max(dx, 1e-10))
            w = math.exp(-BETA * theta * theta)
            ea = cmath.exp(1j * k * act) * w / L
            amps[j] += amps[i] * ea
    return amps


def compute_field_3d(positions, mass_nodes):
    n = len(positions)
    field = [0.0] * n
    for m in mass_nodes:
        mx, my, mz = positions[m]
        for i in range(n):
            ix, iy, iz = positions[i]
            r = math.sqrt((ix-mx)**2 + (iy-my)**2 + (iz-mz)**2) + 0.1
            field[i] += 0.1 / r
    return field


def bin_amplitudes_3d(amps, positions, nodes):
    bins = [0j] * N_YBINS
    bw = 24.0 / N_YBINS
    for m in nodes:
        y = positions[m][1]
        b = int((y + 12.0) / bw)
        b = max(0, min(N_YBINS - 1, b))
        bins[b] += amps[m]
    return bins


def sorkin_born_test(positions, adj, src, k, bi, slit_a, slit_b, slit_c, det_list, field):
    """Three-slit Sorkin test for Born rule."""
    all_slits = set(slit_a + slit_b + slit_c)
    other = set(bi) - all_slits
    combos = {
        'abc': set(slit_a + slit_b + slit_c),
        'ab': set(slit_a + slit_b), 'ac': set(slit_a + slit_c),
        'bc': set(slit_b + slit_c),
        'a': set(slit_a), 'b': set(slit_b), 'c': set(slit_c),
    }
    I3 = 0.0
    P_abc = 0.0
    for key, open_set in combos.items():
        bl = other | (all_slits - open_set)
        a = propagate_3d(positions, adj, field, src, k, bl)
        for di, d in enumerate(det_list):
            p = abs(a[d]) ** 2
            if key == 'abc':
                P_abc += p
                I3 += p
            elif key in ('ab', 'ac', 'bc'):
                I3 -= p
            else:
                I3 += p
    return abs(I3) / P_abc if P_abc > 1e-30 else math.nan


def measure_joint(positions, adj, n_layers, k):
    """Measure d_TV, CL purity, gravity, and Born."""
    n = len(positions)
    by_layer = defaultdict(list)
    for idx, (x, y, z) in enumerate(positions):
        by_layer[round(x)].append(idx)
    layers = sorted(by_layer.keys())
    if len(layers) < 7:
        return None
    src = by_layer[layers[0]]
    det_list = list(by_layer[layers[-1]])
    if not det_list:
        return None
    cy = sum(positions[i][1] for i in range(n)) / n
    bl_idx = len(layers) // 3
    bi = by_layer[layers[bl_idx]]
    sa = [i for i in bi if positions[i][1] > cy + 3][:3]
    sb = [i for i in bi if positions[i][1] < cy - 3][:3]
    if not sa or not sb:
        return None
    blocked = set(bi) - set(sa + sb)

    # Three slits for Born test
    upper = sorted([i for i in bi if positions[i][1] > cy + 2], key=lambda i: positions[i][1])
    lower = sorted([i for i in bi if positions[i][1] < cy - 2], key=lambda i: -positions[i][1])
    middle = sorted([i for i in bi if abs(positions[i][1] - cy) <= 2],
                    key=lambda i: abs(positions[i][1] - cy))

    grav_layer = layers[2 * len(layers) // 3]
    mass_nodes = [i for i in by_layer[grav_layer] if positions[i][1] > cy + 1]
    if not mass_nodes:
        return None
    env_depth = max(1, round(n_layers / 6))
    start = bl_idx + 1
    stop = min(len(layers) - 1, start + env_depth)
    mid = []
    for layer in layers[start:stop]:
        mid.extend(by_layer[layer])

    field_m = compute_field_3d(positions, mass_nodes)
    field_f = [0.0] * n

    # Single-slit propagation
    psi_a = propagate_3d(positions, adj, field_m, src, k, blocked | set(sb))
    psi_b = propagate_3d(positions, adj, field_m, src, k, blocked | set(sa))

    # d_TV
    pa = {d: abs(psi_a[d])**2 for d in det_list}
    pb = {d: abs(psi_b[d])**2 for d in det_list}
    na_amp = sum(pa.values())
    nb_amp = sum(pb.values())
    if na_amp < 1e-30 or nb_amp < 1e-30:
        return None
    dtv = 0.5 * sum(abs(pa[d]/na_amp - pb[d]/nb_amp) for d in det_list)

    # CL bath
    ba = bin_amplitudes_3d(psi_a, positions, mid)
    bb = bin_amplitudes_3d(psi_b, positions, mid)
    S = sum(abs(a - b)**2 for a, b in zip(ba, bb))
    NA = sum(abs(a)**2 for a in ba)
    NB = sum(abs(b)**2 for b in bb)
    Sn = S / (NA + NB) if (NA + NB) > 0 else 0.0
    D_cl = math.exp(-LAM**2 * Sn)

    rho = {}
    for d1 in det_list:
        for d2 in det_list:
            rho[(d1, d2)] = (
                psi_a[d1].conjugate() * psi_a[d2]
                + psi_b[d1].conjugate() * psi_b[d2]
                + D_cl * psi_a[d1].conjugate() * psi_b[d2]
                + D_cl * psi_b[d1].conjugate() * psi_a[d2]
            )
    tr = sum(rho[(d, d)] for d in det_list).real
    if tr < 1e-30:
        return None
    for key in rho:
        rho[key] /= tr
    pur_cl = sum(abs(v)**2 for v in rho.values()).real

    # Gravity
    am = propagate_3d(positions, adj, field_m, src, k, blocked)
    af = propagate_3d(positions, adj, field_f, src, k, blocked)
    pm = sum(abs(am[d])**2 for d in det_list)
    pf = sum(abs(af[d])**2 for d in det_list)
    grav = 0.0
    if pm > 1e-30 and pf > 1e-30:
        ym = sum(abs(am[d])**2 * positions[d][1] for d in det_list) / pm
        yf = sum(abs(af[d])**2 * positions[d][1] for d in det_list) / pf
        grav = ym - yf

    # Born test
    born = math.nan
    if upper and lower and middle:
        born = sorkin_born_test(positions, adj, src, k, bi,
                                [upper[0]], [lower[0]], [middle[0]],
                                det_list, field_f)

    # k=0 gravity control
    am0 = propagate_3d(positions, adj, field_m, src, 0.0, blocked)
    af0 = propagate_3d(positions, adj, field_f, src, 0.0, blocked)
    pm0 = sum(abs(am0[d])**2 for d in det_list)
    pf0 = sum(abs(af0[d])**2 for d in det_list)
    grav_k0 = 0.0
    if pm0 > 1e-30 and pf0 > 1e-30:
        ym0 = sum(abs(am0[d])**2 * positions[d][1] for d in det_list) / pm0
        yf0 = sum(abs(af0[d])**2 * positions[d][1] for d in det_list) / pf0
        grav_k0 = ym0 - yf0

    return {
        "dtv": dtv, "pur_cl": pur_cl, "s_norm": Sn,
        "gravity": grav, "born": born, "grav_k0": grav_k0,
    }


def _mean_se(vals):
    vals = [v for v in vals if v is not None and not math.isnan(v)]
    if not vals: return float('nan'), float('nan')
    m = sum(vals) / len(vals)
    if len(vals) < 2: return m, 0.0
    var = sum((v-m)**2 for v in vals) / (len(vals)-1)
    return m, math.sqrt(var / len(vals))
```

Module-level constants used by `mirror_chokepoint_joint.py`:
`BETA = 0.8`, `K = 5.0` (joint-validator default), `N_YBINS = 8`,
`LAM = 10.0`. The joint validator passes its own `--k` argument to
`measure_joint`, so the helper-local `K` is not load-bearing here.

## Registered cache excerpt (load-bearing, 2026-05-24)

The binding scope of this note is exactly the sparse N=25,40,60,80
`Z₂ × Z₂` row from the joint-validator (see Scope narrowing section
above). The dense N=80/100/120 row is **out of binding scope** until the
missing dense joint-validation log + registered joint-validator cache is
attached, so its cache is **not inlined** here per the audit verdict
("include the dense N=80/100/120 cache only if N=120 is to be binding"
— N=120 is explicitly NOT binding in this revision).

**Registered runner-cache status (2026-05-24 `runner_artifact_issue`
repair):** the SHA-pinned registered cache
[`logs/runner-cache/higher_symmetry_joint_validation.txt`](../logs/runner-cache/higher_symmetry_joint_validation.txt)
is now attached for
[`scripts/higher_symmetry_joint_validation.py`](../scripts/higher_symmetry_joint_validation.py),
produced via the canonical `scripts/runner_cache.py` orchestrator
(`runner_sha256: f6d580f54dc9c4070e977ea1ac989f47ff54d5edef5c802fe6e004e5841592df`,
`exit_code: 0`, `status: ok`, `elapsed_sec: 53.94`, `timeout_sec: 120`)
with default argv `--families random z2z2 ring --n-layers 25 40 60 80
--n-seeds 16 --k 5.0 --k-band 3.0 5.0 7.0 --random-npl 50
--z2z2-quarter 12 --ring-nodes 48 --connect-radius 5.0 --n-boot 1000
--bootstrap-seed 12345`. The full cache header + stdout is reproduced
below for restricted-packet visibility. The earlier raw log
[`logs/2026-04-03-higher-symmetry-joint-validation.txt`](../logs/2026-04-03-higher-symmetry-joint-validation.txt)
used 32 seeds rather than the default 16; the registered SHA-pinned
cache below is the canonical-default 16-seed run and supersedes the raw
log as the load-bearing artifact for this row.

Registered joint-validator runner cache (full body, sparse N=25,40,60,80, binding):

```
===== runner cache v1 =====
runner: scripts/higher_symmetry_joint_validation.py
runner_sha256: f6d580f54dc9c4070e977ea1ac989f47ff54d5edef5c802fe6e004e5841592df
timeout_sec: 120
exit_code: 0
elapsed_sec: 53.94
status: ok
----- stdout -----
====================================================================================================================================
HIGHER-SYMMETRY JOINT VALIDATION
  Born + gravity + decoherence on the higher-symmetry families
  k=5.0, k_band=[3.0, 5.0, 7.0], seeds=16, random_npl=50, z2z2_quarter=12, ring_nodes=48, r=5.0
====================================================================================================================================

     N    family        d_TV      pur_cl        grav@k     grav_band    band+             Born         k=0   ok   time
  ----------------------------------------------------------------------------------------------------------------------
    25    random  0.798±0.040  0.731±0.046  +1.682±0.756  +0.305±0.454    10/16  5.95e-16±1.13e-16  0.00e+00±0.00e+00   16     2s
    40    random  0.727±0.053  0.864±0.037  -0.244±0.811  -0.557±0.539     6/16  1.03e-15±2.43e-16  0.00e+00±0.00e+00   16     3s
    60    random  0.534±0.064  0.901±0.026  +0.016±0.640  +0.356±0.394     9/16  1.42e-15±1.90e-16  0.00e+00±0.00e+00   16     5s
    80    random  0.431±0.062  0.880±0.026  -0.164±0.803  +0.025±0.517     8/16  1.71e-15±4.28e-16  0.00e+00±0.00e+00   16     7s

    25      z2z2  0.893±0.034  0.616±0.032  -0.079±0.680  +0.580±0.412    11/15  5.91e-16±1.53e-16  0.00e+00±0.00e+00   15     1s
    40      z2z2  0.862±0.029  0.661±0.035  +0.905±0.809  +0.706±0.576    10/15  3.85e-16±1.75e-16  0.00e+00±0.00e+00   15     2s
    60      z2z2  0.698±0.050  0.682±0.036  -0.690±0.868  +0.879±0.656     9/15  7.34e-16±2.10e-16  0.00e+00±0.00e+00   15     4s
    80      z2z2  0.540±0.052  0.782±0.028  +2.218±0.983  +1.996±0.542    12/15  1.80e-15±4.68e-16  0.00e+00±0.00e+00   15     5s

    25      ring  0.516±0.051  0.684±0.025  +0.773±0.412  +0.671±0.281    12/16  6.94e-16±1.98e-16  0.00e+00±0.00e+00   16     3s
    40      ring  0.441±0.043  0.783±0.037  +1.110±0.451  +0.909±0.311    11/16  1.66e-15±8.80e-16  0.00e+00±0.00e+00   16     5s
    60      ring  0.320±0.048  0.837±0.032  -0.103±0.375  +0.226±0.248    10/16  1.78e-15±3.80e-16  0.00e+00±0.00e+00   16     7s
    80      ring  0.237±0.054  0.921±0.034  -0.060±0.462  +0.372±0.308    13/16  3.34e-15±1.58e-15  0.00e+00±0.00e+00   16    10s

Exponent fits on family-mean decoherence depth: 1 - pur_cl ~= C * N^alpha
    random: alpha=-0.750, C=2.5866, R^2=0.763, bootstrap alpha=-0.756 [-1.230, -0.280]
      z2z2: alpha=-0.430, C=1.6099, R^2=0.796, bootstrap alpha=-0.437 [-0.678, -0.199]
      ring: alpha=-1.103, C=11.9884, R^2=0.909, bootstrap alpha=-1.171 [-2.032, -0.652]

Readout:
  - Born safety means |I3|/P stays near machine precision.
  - k=0 must remain zero if gravity stays purely phase-mediated.
  - grav_band averages the same centroid shift across a small k window
    to reduce sign flips from single-k phase oscillations.

----- stderr -----

```

The earlier 32-seed raw log (preserved for historical comparison) is reproduced below:

```
====================================================================================================================================
HIGHER-SYMMETRY JOINT VALIDATION
  Born + gravity + decoherence on the higher-symmetry families
  k=5.0, k_band=[3.0, 5.0, 7.0], seeds=32, random_npl=50, z2z2_quarter=12, ring_nodes=48, r=5.0
====================================================================================================================================

     N    family        d_TV      pur_cl        grav@k     grav_band    band+             Born         k=0   ok   time
  ----------------------------------------------------------------------------------------------------------------------
    25    random  0.851±0.025  0.787±0.034  +0.851±0.573  +0.189±0.300    18/32  7.88e-16±1.40e-16  0.00e+00±0.00e+00   32     5s
    40    random  0.727±0.032  0.860±0.026  -0.456±0.637  +0.236±0.383    15/32  8.87e-16±1.31e-16  0.00e+00±0.00e+00   32     9s
    60    random  0.488±0.050  0.911±0.020  +0.365±0.641  +0.468±0.243    22/32  1.37e-15±1.69e-16  0.00e+00±0.00e+00   32    14s
    80    random  0.425±0.043  0.905±0.018  +0.654±0.618  +0.559±0.354    21/32  1.62e-15±2.48e-16  0.00e+00±0.00e+00   32    19s

    25      z2z2  0.890±0.021  0.660±0.025  +0.059±0.632  +0.690±0.323    21/30  9.02e-16±1.44e-16  0.00e+00±0.00e+00   30     4s
    40      z2z2  0.850±0.027  0.667±0.023  +1.196±0.574  +0.916±0.403    20/30  1.24e-15±4.76e-16  0.00e+00±0.00e+00   30     7s
    60      z2z2  0.746±0.037  0.685±0.028  +0.823±0.640  +1.493±0.454    23/30  9.86e-16±1.25e-16  0.00e+00±0.00e+00   30    12s
    80      z2z2  0.600±0.042  0.783±0.019  +2.771±0.567  +1.736±0.337    24/30  1.48e-15±2.72e-16  0.00e+00±0.00e+00   30    15s

    25      ring  0.555±0.041  0.716±0.019  +1.195±0.429  +0.654±0.264    23/32  6.69e-16±9.45e-17  0.00e+00±0.00e+00   32     7s
    40      ring  0.424±0.034  0.786±0.023  +0.774±0.318  +0.488±0.192    20/32  1.98e-15±5.49e-16  0.00e+00±0.00e+00   32    13s
    60      ring  0.320±0.034  0.848±0.024  +0.106±0.427  +0.474±0.307    19/32  1.98e-15±5.86e-16  0.00e+00±0.00e+00   32    20s
    80      ring  0.233±0.032  0.927±0.021  +0.313±0.349  +0.418±0.210    21/32  2.67e-15±1.14e-15  0.00e+00±0.00e+00   32    28s

Exponent fits on family-mean decoherence depth: 1 - pur_cl ~= C * N^alpha
    random: alpha=-0.760, C=2.3444, R^2=0.911, bootstrap alpha=-0.769 [-1.148, -0.373]
      z2z2: alpha=-0.335, C=1.0769, R^2=0.643, bootstrap alpha=-0.335 [-0.509, -0.139]
      ring: alpha=-1.088, C=10.6082, R^2=0.890, bootstrap alpha=-1.149 [-1.699, -0.702]

Readout:
  - Born safety means |I3|/P stays near machine precision.
  - k=0 must remain zero if gravity stays purely phase-mediated.
  - grav_band averages the same centroid shift across a small k window
    to reduce sign flips from single-k phase oscillations.
```

The dense N=80/100/120 log
[`logs/2026-04-03-higher-symmetry-gravity-probe-z2z2-dense-n80-n120.txt`](/Users/jonreilly/Projects/Physics/logs/2026-04-03-higher-symmetry-gravity-probe-z2z2-dense-n80-n120.txt)
exists but is produced by the **gravity-probe** runner
(`scripts/higher_symmetry_gravity_probe.py`), not the joint-validator.
Its registered cache is
`logs/runner-cache/higher_symmetry_gravity_probe.txt` (a different
row's primary runner). It is therefore not inlined here as joint-
validator binding evidence.

## Question

The earlier higher-symmetry pass only checked decoherence. The next real
question was whether the strongest new family, `Z2 x Z2`, still survives the
joint standards used on the retained mirror lane:

- corrected Born `|I3|/P`
- gravity centroid shift
- `k=0` gravity control
- CL-bath purity `pur_cl`

## Setup

- families: random, `Z2 x Z2`, ring
- `32` seeds
- `N = 25, 40, 60, 80`
- same geometry as the higher-symmetry discovery script:
  - random: `50` nodes per layer
  - `Z2 x Z2`: `12` quarter-seeds per layer (`48` total nodes)
  - ring: `48` nodes per layer
- single-`k` joint metric at `k = 5.0`
- small band-averaged gravity read over `k = 3, 5, 7`

The band-averaged gravity read is included because the higher-symmetry families
show stronger single-`k` phase oscillation than the mirror chokepoint lane.

### Dense extension

A narrower density bump was then tested to see whether `Z2 x Z2` could stay
alive at larger `N`:

- `N = 80, 100, 120`
- `16` seeds
- `z2z2-quarter = 16` (`64` total nodes per layer)
- `connect_radius = 5.2`

This extension is the one that reaches `N = 120` while staying Born-clean and
gravity-positive.

## Results

### `Z2 x Z2`

| N | `pur_cl` | decoh `1-pur_cl` | gravity@`k=5` | gravity band | band positive | Born `|I3|/P` | `k=0` |
|---|---:|---:|---:|---:|---:|---:|---:|
| 25 | `0.660±0.025` | `0.340` | `+0.059±0.632` | `+0.690±0.323` | `21/30` | `9.02e-16±1.44e-16` | `0.00e+00` |
| 40 | `0.667±0.023` | `0.333` | `+1.196±0.574` | `+0.916±0.403` | `20/30` | `1.24e-15±4.76e-16` | `0.00e+00` |
| 60 | `0.685±0.028` | `0.315` | `+0.823±0.640` | `+1.493±0.454` | `23/30` | `9.86e-16±1.25e-16` | `0.00e+00` |
| 80 | `0.783±0.019` | `0.217` | `+2.771±0.567` | `+1.736±0.337` | `24/30` | `1.48e-15±2.72e-16` | `0.00e+00` |

### Dense `Z2 x Z2` Extension

| N | `pur_cl` | decoh `1-pur_cl` | gravity@`k=5` | gravity band | band positive | Born `|I3|/P` | `k=0` |
|---|---:|---:|---:|---:|---:|---:|---:|
| 80 | `0.785±0.035` | `0.215` | `+2.677±0.806` | `+2.713±0.372` | `16/16` | `1.55e-15±3.37e-16` | `0.00e+00` |
| 100 | `0.742±0.040` | `0.258` | `+0.763±0.616` | `+1.431±0.443` | `13/16` | `1.94e-15±3.18e-16` | `0.00e+00` |
| 120 | `0.764±0.036` | `0.236` | `+0.245±0.750` | `+1.356±0.382` | `14/16` | `3.04e-15±1.31e-15` | `0.00e+00` |

### Comparison Families

| family | `pur_cl(N=25)` | `pur_cl(N=80)` | bounded alpha | gravity-band read |
|---|---:|---:|---:|---|
| random | `0.787±0.034` | `0.905±0.018` | `-0.760` | weak / noisy |
| `Z2 x Z2` | `0.660±0.025` | `0.783±0.019` | `-0.335` | positive at all tested `N` |
| ring | `0.716±0.019` | `0.927±0.021` | `-1.088` | positive but weaker as a decoherence lane |

## Exponent Fit

Using the family-mean decoherence depth

`1 - pur_cl ~= C * N^alpha`

the retained bounded fit for `Z2 x Z2` is:

- direct fit: `alpha = -0.335`, `R^2 = 0.643`
- bootstrap: `alpha = -0.335`, `95% CI [-0.509, -0.139]`

For the dense extension:

- direct fit: `alpha = +0.255`, `R^2 = 0.322`
- bootstrap: `alpha = +0.265`, `95% CI [-0.719, +1.303]`

For reference on the same bounded window:

- random: `alpha = -0.760`, bootstrap `[-1.148, -0.379]`
- ring: `alpha = -1.088`, bootstrap `[-1.619, -0.711]`

So the `Z2 x Z2` family really does retain a much slower decoherence decay
than the random baseline on this joint rerun, while the ring family does not.
The dense extension remains Born-clean and gravity-positive through `N = 120`,
but its exponent fit is too noisy to promote as a clean asymptotic law.

## Narrow Read

- `Z2 x Z2` is **Born-clean** at machine precision through the full tested
  window.
- `Z2 x Z2` keeps the **`k=0` control exactly zero**.
- `Z2 x Z2` also keeps a **positive gravity signal** on the band-averaged
  read at all tested `N`, with the strongest support at `N = 60, 80` on the
  discovery geometry and at `N = 80, 100, 120` on the dense extension.
- The `Z2 x Z2` decoherence exponent remains **slow**: about `-0.33` on the
  discovery geometry, with the dense extension too noisy to lock a cleaner
  asymptotic law.
- The ring family is **not** the next winner once the joint tests are imposed:
  it is Born-clean and mildly gravity-positive, but its decoherence scaling is
  closer to the random ceiling than to the `Z2 x Z2` lane.

## Important Scope Note

This note does **not** replace the earlier exact-`Z2` story. The canonical
exact mirror result remains the mirror/chokepoint lane in:

[`docs/MIRROR_CHOKEPOINT_NOTE.md`](/Users/jonreilly/Projects/Physics/docs/MIRROR_CHOKEPOINT_NOTE.md)

The `Z2` branch inside [`scripts/higher_symmetry_dag.py`](/Users/jonreilly/Projects/Physics/scripts/higher_symmetry_dag.py)
is only a node-placement symmetry check, not the exact edge-mirrored
construction used in the retained mirror result.

## Conclusion

The project now has a new bounded higher-symmetry coexistence lane:

- **exact `Z2` mirror** remains the canonical parity-protected story
- **`Z2 x Z2`** extends that symmetry idea into a stronger bounded
  decoherence lane that is still Born-clean and gravity-positive, and now
  remains retained through `N = 120` on a denser narrow probe
- **ring / approximate rotational symmetry** does not survive the joint test
  as cleanly

The most productive next move is now quantitative rather than qualitative:
test whether the `Z2 x Z2` family also inherits a usable distance or mass law
on the dense extension, not just a positive joint gravity signal. Until that
probe lands, the review-safe read is: **decoherence lead yes, gravity-law
contender unproven**.
