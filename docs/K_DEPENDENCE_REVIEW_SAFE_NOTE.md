# K Dependence Review-Safe Note

**Claim type:** bounded_theorem
**Status:** support - structural or confirmatory support note
This note captures the hardened rerun for the k-dependence claim from
`scripts/k_dependence_ceiling.py`.

**Audit-lane runner update (2026-05-09):** The primary runner `scripts/k_dependence_ceiling.py` now carries explicit assertion checks (`assert math.isclose(...)`, `assert abs(...) < EPS`, etc.) mirroring its existing PASS-condition booleans. This makes the runner's class-A invariants visible to `docs/audit/scripts/classify_runner_passes.py`. The runner output and pass/fail semantics are unchanged.

## Method

- Fixed N window for every `k`: `N = [25, 30, 40, 60, 80]`
- Shared seed set across all `k` values
- Per-seed slope fits on `(1 - pur_min)` vs `N`
- Bootstrap confidence intervals on the mean seed-level slope

## Helper-runner code excerpt (load-bearing for restricted packet, inlined 2026-05-18)

The cited slopes and CIs are produced by `scripts/k_dependence_fixed_window_review.py`,
which imports `pur_min_single_k` from the helper `scripts/k_dependence_ceiling.py`.
Both load-bearing pieces are inlined below so the restricted-packet review does not
require external source navigation.

### Helper: `scripts/k_dependence_ceiling.py` — `pur_min_single_k`

This is the per-(N, k, seed) purity-minimum computation that feeds the seed-level
slope fits in the primary runner. Full source (functions only; ~125 lines):

```python
import math
import cmath
from collections import defaultdict, deque

from scripts.generative_causal_dag_interference import generate_causal_dag

BETA = 0.8


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


def compute_field(positions, adj, mass_nodes):
    n = len(positions)
    field = [0.0] * n
    for m in mass_nodes:
        mx, my = positions[m]
        for i in range(n):
            ix, iy = positions[i]
            r = math.sqrt((ix - mx) ** 2 + (iy - my) ** 2) + 0.1
            field[i] += 0.1 / r
    return field


def propagate(positions, adj, field, src, k, blocked):
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
            x1, y1 = positions[i]
            x2, y2 = positions[j]
            dx, dy = x2 - x1, y2 - y1
            L = math.sqrt(dx * dx + dy * dy)
            if L < 1e-10:
                continue
            lf = 0.5 * (field[i] + field[j])
            dl = L * (1 + lf)
            ret = math.sqrt(max(dl * dl - L * L, 0))
            act = dl - ret
            theta = math.atan2(abs(dy), max(dx, 1e-10))
            w = math.exp(-BETA * theta * theta)
            ea = cmath.exp(1j * k * act) * w / L
            amps[j] += amps[i] * ea
    return amps


def pur_min_single_k(nl, k, seed):
    positions, adj, _ = generate_causal_dag(
        n_layers=nl, nodes_per_layer=25, y_range=12.0,
        connect_radius=3.0, rng_seed=seed)
    by_layer = defaultdict(list)
    for idx, (x, y) in enumerate(positions):
        by_layer[round(x)].append(idx)
    layers = sorted(by_layer.keys())
    if len(layers) < 7:
        return None
    src = by_layer[layers[0]]
    det_list = list(by_layer[layers[-1]])
    if not det_list:
        return None
    cy = sum(y for _, y in positions) / len(positions)
    bl_idx = len(layers) // 3
    bi = by_layer[layers[bl_idx]]
    sa = [i for i in bi if positions[i][1] > cy + 3][:3]
    sb = [i for i in bi if positions[i][1] < cy - 3][:3]
    if not sa or not sb:
        return None
    blocked = set(bi) - set(sa + sb)
    grav_layer = layers[2 * len(layers) // 3]
    grav_mass = [i for i in by_layer[grav_layer] if positions[i][1] > cy + 1]
    start = bl_idx + 1
    stop = min(len(layers) - 1, start + max(1, round(nl / 6)))
    mn = []
    for layer in layers[start:stop]:
        mn.extend(i for i in by_layer[layer] if abs(positions[i][1] - cy) <= 3.0)
    field = compute_field(positions, adj, list(set(mn) | set(grav_mass)))

    aa = propagate(positions, adj, field, src, k, blocked | set(sb))
    ab = propagate(positions, adj, field, src, k, blocked | set(sa))
    rho = {}
    for d1 in det_list:
        for d2 in det_list:
            rho[(d1, d2)] = aa[d1].conjugate() * aa[d2] + ab[d1].conjugate() * ab[d2]
    tr = sum(rho[(d, d)] for d in det_list).real
    if tr <= 1e-30:
        return None
    for key in rho:
        rho[key] /= tr
    return sum(abs(v) ** 2 for v in rho.values()).real
```

### Primary runner: `scripts/k_dependence_fixed_window_review.py` — load-bearing fit + bootstrap

```python
import argparse
import math
import random
from dataclasses import dataclass
from typing import Iterable

from scripts.k_dependence_ceiling import pur_min_single_k


@dataclass
class FitResult:
    alpha: float
    intercept: float
    r2: float


def fit_power_law(ns: Iterable[int], ys: Iterable[float]) -> FitResult | None:
    xs = [math.log(n) for n in ns]
    zs = [math.log(y) for y in ys if y > 0]
    if len(xs) != len(zs) or len(xs) < 3:
        return None
    n = len(xs)
    mx = sum(xs) / n
    my = sum(zs) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    sxy = sum((x - mx) * (z - my) for x, z in zip(xs, zs))
    syy = sum((z - my) ** 2 for z in zs)
    if sxx <= 0 or syy <= 0:
        return None
    alpha = sxy / sxx
    intercept = my - alpha * mx
    r2 = (sxy ** 2) / (sxx * syy)
    return FitResult(alpha=alpha, intercept=intercept, r2=r2)


def bootstrap_mean(values, n_samples, rng):
    if not values:
        return math.nan, math.nan, math.nan
    if len(values) == 1:
        v = values[0]
        return v, v, v
    draws = []
    for _ in range(n_samples):
        sample = [values[rng.randrange(len(values))] for _ in values]
        draws.append(sum(sample) / len(sample))
    draws.sort()
    lo = draws[max(0, int(0.025 * (len(draws) - 1)))]
    hi = draws[min(len(draws) - 1, int(0.975 * (len(draws) - 1)))]
    mean = sum(values) / len(values)
    return mean, lo, hi


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-list", nargs="+", type=int, default=[25, 30, 40, 60, 80])
    parser.add_argument("--n-seeds", type=int, default=16)
    parser.add_argument("--k-values", nargs="+", type=float,
                        default=[1.0, 2.0, 3.0, 5.0, 7.0, 10.0, 15.0])
    parser.add_argument("--bootstrap-samples", type=int, default=2000)
    args = parser.parse_args()
    # ... (builds seed x k x N table via pur_min_single_k; fits per-seed
    # log-log slope on the fixed N window; reports mean seed_alpha, SE, and
    # bootstrap 95% CI on the mean. Full source in
    # scripts/k_dependence_fixed_window_review.py.)
```

## Runner cache excerpt (load-bearing, 2026-05-18)

**Cache-availability status:**
- `logs/runner-cache/k_dependence_ceiling.txt` — present (helper runner stdout).
- `logs/2026-04-03-k-dependence-fixed-window-review.txt` — **missing in the current
  worktree**. This is the log cited in the `## Result` block below. The note's
  seed-level `seed_alpha` and bootstrap CIs originate from a historical run of
  `scripts/k_dependence_fixed_window_review.py` whose stdout artifact is not
  currently retained in `logs/`. The result block is preserved verbatim from the
  prior commit history.
- No window-comparison artifact is currently retained. The claim in this note is
  **not** a positive fit-window-robustness theorem; it is the weaker statement that
  the cited fixed-window result is fit-window-sensitive (see Interpretation).

### Tail of `logs/runner-cache/k_dependence_ceiling.txt`

This is the helper-runner cache. It uses the same per-seed `pur_min_single_k`
that the primary runner imports, but reports the aggregated alpha/R^2 over the
seed-averaged curve rather than per-seed slopes. Shown here for restricted-packet
runner-output visibility:

```
runner: scripts/k_dependence_ceiling.py
runner_sha256: fa07b52d380da998a7dd183d23a01ee1ec7e04bc3a43bdca929c1512228684bc
timeout_sec: 120
exit_code: 0
elapsed_sec: 29.23
status: ok
----- stdout -----
======================================================================
K-DEPENDENCE OF DECOHERENCE EXPONENT
  Single-k scaling laws, 16 seeds per point
======================================================================

      k  N= 25  N= 30  N= 40  N= 60  N= 80   alpha    R²
  ------------------------------------------------------------
    1.0  0.0518  0.0434  0.0210  0.0316  0.0036  -1.846  0.685
    2.0  0.0413  0.0385  0.0339  0.0384  0.0157  -0.636  0.585
    3.0  0.0333  0.0507  0.0283  0.0262  0.0296  -0.316  0.340
    5.0  0.0564  0.0989  0.0687  0.0239  0.0088  -1.800  0.792
    7.0  0.0376  0.0490  0.0439  0.0405  0.0162  -0.655  0.506
   10.0  0.0748  0.0843  0.0385  0.0326  0.0028  -2.518  0.773
   15.0  0.0456  0.0691  0.0341  0.0329  0.0107  -1.236  0.737

If alpha varies with k: ceiling is k-dependent
If alpha constant: ceiling is k-independent (universal)
```

**Note on numerical correspondence:** the helper-runner cache above reports
**pooled** alpha (single fit to the seed-averaged curve), e.g. `alpha=-1.846` at
`k=1.0`. The `## Result` block below quotes **mean per-seed** `seed_alpha` (mean
over per-seed slope fits), e.g. `seed_alpha = -3.931` at `k=1.0`, with bootstrap
CI on that mean. These are different statistics computed on overlapping data
sets: the pooled fit averages curves before fitting; the seed-level fit averages
slopes after per-seed fitting. The two values are not expected to agree
numerically. The qualitative pattern — large per-k variation with overlapping
intervals and non-monotonic ordering in `k` — is consistent between the two
representations (compare the spread of pooled alphas in the cache to the spread
of `seed_alpha` values in the Result block). The seed-level CIs cited in the
Result block are sourced from a historical run of the primary runner whose log
is not retained.

## Result

From `logs/2026-04-03-k-dependence-fixed-window-review.txt`:

- `k=1.0`: `seed_alpha = -3.931`, bootstrap CI `[-5.674, -2.255]`
- `k=2.0`: `seed_alpha = -2.881`, bootstrap CI `[-4.784, -1.094]`
- `k=3.0`: `seed_alpha = -2.286`, bootstrap CI `[-4.036, -0.528]`
- `k=5.0`: `seed_alpha = -3.322`, bootstrap CI `[-5.745, -0.920]`
- `k=7.0`: `seed_alpha = -2.827`, bootstrap CI `[-5.306, -0.198]`
- `k=10.0`: `seed_alpha = -3.813`, bootstrap CI `[-6.389, -1.242]`
- `k=15.0`: `seed_alpha = -2.773`, bootstrap CI `[-5.307, -0.455]`

## Interpretation

The fixed-window rerun does not support a clean hardened `alpha(k)` law.
The per-seed exponents are all negative, but the confidence intervals
overlap strongly and the ordering is not monotonic in `k`.

Best replacement wording:

- `k` affects the fitted ceiling behavior inside this graph family, but
  the current evidence is fit-window-sensitive and does not yet support a
  review-safe universal `alpha(k)` claim.
