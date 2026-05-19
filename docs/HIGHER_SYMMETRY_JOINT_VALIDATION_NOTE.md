# Higher-Symmetry Joint Validation Note — Cached N Range (Binding)

**Date:** 2026-04-03 (scope narrowed 2026-05-17 per audited_conditional `runner_artifact_issue` repair: binding scope is exactly the cached log range; the N=120 promotion claim requires the missing dense N=80/100/120 joint-validation log + registered joint-validator runner)
**Status:** bounded positive on the cached registered log range for
`Z₂ × Z₂`; the `N = 120` proposed_retained promotion is **out of
binding scope** until the missing dense N=80/100/120 joint-validation
log is registered and the joint validator is registered as this row's
primary runner.

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

## Registered cache excerpt (load-bearing, 2026-05-18)

The binding scope of this note is exactly the sparse N=25,40,60,80
`Z₂ × Z₂` row from the joint-validator (see Scope narrowing section
above). The dense N=80/100/120 row is **out of binding scope** until the
missing dense joint-validation log + registered joint-validator cache is
attached, so its cache is **not inlined** here per the audit verdict
("include the dense N=80/100/120 cache only if N=120 is to be binding"
— N=120 is explicitly NOT binding in this revision).

**Note on missing registered runner-cache:** as of 2026-05-18 there is
no `logs/runner-cache/higher_symmetry_joint_validation.txt` registered
cache file for `scripts/higher_symmetry_joint_validation.py`. The
binding evidence below is the existing raw log
`logs/2026-04-03-higher-symmetry-joint-validation.txt`, which is the
stdout output of the joint validator on the sparse N=25,40,60,80
window. Registering this stdout as a SHA-pinned runner cache (in the
`logs/runner-cache/` directory under the joint-validator's name) is the
remaining `runner_artifact_issue` engineering step; until that lands,
the joint validator is not the primary registered runner of this row
in the runner classification ledger and the N=120 promotion remains
out of binding scope.

Raw joint-validator stdout (sparse N=25,40,60,80, binding):

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
