# Kubo Continuum Limit — Family Portability (Partial, Later Narrowed)

**Date:** 2026-04-07
**Claim type:** bounded_theorem
**Status:** historical partial snapshot, later narrowed by Lane α++ — at H=0.25, Fam1=+5.986 and Fam3=+5.955 agree to 0.5%, while Fam2=+7.088 is a 12% outlier. This note still captures the pre-α++ portability snapshot. The later Fam2 H=0.20 refinement in `KUBO_FAM2_REFINEMENT_NOTE.md` (sibling artifact; cross-reference only — not a one-hop dep of this note) rejects the easy "Fam2 just needs finer H" rescue, so the current program-level read is narrower than the original 2/3-family partial positive.

## Artifact chain

- [`scripts/kubo_continuum_limit_families.py`](../scripts/kubo_continuum_limit_families.py)
- [`logs/2026-04-07-kubo-continuum-limit-families.txt`](../logs/2026-04-07-kubo-continuum-limit-families.txt)
- `docs/KUBO_FAM2_REFINEMENT_NOTE.md` (sibling artifact; cross-reference only — not a one-hop dep of this note)

## Helper-runner code excerpt (load-bearing for restricted packet, inlined 2026-05-18)

The primary runner `scripts/kubo_continuum_limit_families.py` imports the
three load-bearing helpers `grow`, `true_kubo_at_H`, and `finite_diff_dM`,
plus the physical-parameter constants, from the sister runner
`scripts/kubo_continuum_limit.py`. Under a restricted audit packet the
sister-runner source may not be visible, so the verbatim definitions are
reproduced below from `scripts/kubo_continuum_limit.py` (2026-04-07
state, the lane that produced
`logs/2026-04-07-kubo-continuum-limit-families.txt`). The only
stdlib dependencies are `math` and `random`; no transitive project
imports.

```python
# --- Excerpted verbatim from scripts/kubo_continuum_limit.py ---

import math
import random

# Physical parameters
T_PHYS = 15.0
PW_PHYS = 6.0
K_PER_H = 2.5
S_PHYS = 0.004
MASS_Z_PHYS = 3.0
SRC_LAYER_FRAC = 1.0 / 3.0
BETA = 0.8


def grow(seed, drift, restore, NL, PW, max_d_phys, H):
    rng = random.Random(seed)
    hw = int(PW / H)
    md = max(1, round(max_d_phys / H))
    pos = []
    adj = {}
    nmap = {}
    pos.append((0.0, 0.0, 0.0))
    nmap[(0, 0, 0)] = 0
    for layer in range(1, NL):
        x = layer * H
        for iy in range(-hw, hw + 1):
            for iz in range(-hw, hw + 1):
                if layer == 1:
                    y, z = iy * H, iz * H
                else:
                    prev = nmap.get((layer - 1, iy, iz))
                    if prev is None:
                        continue
                    _, py, pz = pos[prev]
                    y = py + rng.gauss(0, drift * H)
                    z = pz + rng.gauss(0, drift * H)
                    y = y * (1 - restore) + (iy * H) * restore
                    z = z * (1 - restore) + (iz * H) * restore
                idx = len(pos)
                pos.append((x, y, z))
                nmap[(layer, iy, iz)] = idx
        for iy in range(-hw, hw + 1):
            for iz in range(-hw, hw + 1):
                si = nmap.get((layer - 1, iy, iz))
                if si is None:
                    continue
                for dy in range(-md, md + 1):
                    for dz in range(-md, md + 1):
                        di = nmap.get((layer, iy + dy, iz + dz))
                        if di is not None:
                            adj.setdefault(si, []).append(di)
    return pos, adj, nmap


def true_kubo_at_H(pos, adj, NL, PW, H, k_phase, x_src, z_src, beta=BETA):
    """Parallel perturbation propagator for the static-gravity Kubo coefficient.

    Returns (dM_at_small_s, kubo_true, cz_free).

    - A_j = Σ amp at node j (free propagation)
    - B_j = d(amp_j)/ds at s=0 (parallel perturbation propagator)
    - kubo_true = d(cz)/ds at s=0 via chain rule
    - dM_at_small_s = finite-difference measurement at s=S_PHYS for
      cross-check with kubo_true * S_PHYS

    Imposed field: f = s / (r_field), where
      r_field = sqrt((mx - x_src)^2 + (mz - z_src)^2) + 0.1
      (single regularized distance, same convention as the main Kubo lane)
    """
    n = len(pos)
    A = [0j] * n
    B = [0j] * n
    A[0] = 1.0 + 0j
    order = sorted(range(n), key=lambda i: pos[i][0])
    h2 = H * H
    for i in order:
        ai = A[i]
        bi = B[i]
        if abs(ai) < 1e-30 and abs(bi) < 1e-30:
            continue
        for j in adj.get(i, []):
            dx = pos[j][0] - pos[i][0]
            dy = pos[j][1] - pos[i][1]
            dz = pos[j][2] - pos[i][2]
            L = math.sqrt(dx * dx + dy * dy + dz * dz)
            if L < 1e-10:
                continue
            mx = 0.5 * (pos[i][0] + pos[j][0])
            mz = 0.5 * (pos[i][2] + pos[j][2])
            r_field = math.sqrt((mx - x_src) ** 2 + (mz - z_src) ** 2) + 0.1
            phase = k_phase * L
            phi = complex(math.cos(phase), math.sin(phase))
            theta = math.atan2(math.sqrt(dy * dy + dz * dz), max(dx, 1e-10))
            w = math.exp(-beta * theta * theta)
            w_eff = w * h2 / (L * L)
            weight = phi * w_eff
            dphi_ds = complex(0.0, -k_phase * L / r_field) * phi
            A[j] += ai * weight
            B[j] += (bi * phi + ai * dphi_ds) * w_eff
    # Detector slice: nodes at layer NL-1
    hw = int(PW / H)
    npl = (2 * hw + 1) ** 2
    ds_idx = n - npl
    weights = [abs(A[k]) ** 2 for k in range(ds_idx, n)]
    zs = [pos[k][2] for k in range(ds_idx, n)]
    T0 = sum(weights)
    if T0 <= 0:
        return 0.0, 0.0, 0.0
    cz_free = sum(w * z for w, z in zip(weights, zs)) / T0
    # chain rule: d(cz)/ds = (Σ 2 Re[A*B] z)/T0 - cz_free * (Σ 2 Re[A*B])/T0
    dT_ds = sum(2.0 * (A[k].conjugate() * B[k]).real for k in range(ds_idx, n))
    dN_ds = sum(2.0 * (A[k].conjugate() * B[k]).real * pos[k][2]
                for k in range(ds_idx, n))
    N0 = T0 * cz_free
    kubo = dN_ds / T0 - N0 * dT_ds / (T0 * T0)
    return kubo, cz_free, T0


def finite_diff_dM(pos, adj, NL, PW, H, k_phase, x_src, z_src, s, beta=BETA):
    """Measure the static dM (cz displacement) at a small source strength s
    via direct beam propagation (no parallel propagator), for cross-check."""
    n = len(pos)
    field = [s / (math.sqrt((p[0] - x_src) ** 2 + (p[2] - z_src) ** 2) + 0.1)
             for p in pos]

    order = sorted(range(n), key=lambda i: pos[i][0])
    amps = [0j] * n
    amps[0] = 1.0
    h2 = H * H
    for i in order:
        if abs(amps[i]) < 1e-30:
            continue
        for j in adj.get(i, []):
            dx = pos[j][0] - pos[i][0]
            dy = pos[j][1] - pos[i][1]
            dz = pos[j][2] - pos[i][2]
            L = math.sqrt(dx * dx + dy * dy + dz * dz)
            if L < 1e-10:
                continue
            f = 0.5 * (field[i] + field[j])
            phase = k_phase * L * (1.0 - f)
            theta = math.atan2(math.sqrt(dy * dy + dz * dz), max(dx, 1e-10))
            w = math.exp(-beta * theta * theta)
            amps[j] += amps[i] * complex(math.cos(phase), math.sin(phase)) * w * h2 / (L * L)
    hw = int(PW / H)
    npl = (2 * hw + 1) ** 2
    ds_idx = n - npl
    weights = [abs(amps[k]) ** 2 for k in range(ds_idx, n)]
    zs = [pos[k][2] for k in range(ds_idx, n)]
    T0 = sum(weights)
    if T0 <= 0:
        return 0.0
    return sum(w * z for w, z in zip(weights, zs)) / T0

# --- end excerpt ---
```

Provenance: copied verbatim from `scripts/kubo_continuum_limit.py` as of
the 2026-04-07 lane-α snapshot. The `families.py` runner above the
results section uses exactly these definitions via `from
kubo_continuum_limit import grow, true_kubo_at_H, finite_diff_dM,
T_PHYS, PW_PHYS, K_PER_H, S_PHYS, MASS_Z_PHYS, SRC_LAYER_FRAC`. The
later Fam2 `H = 0.20` refinement note (`KUBO_FAM2_REFINEMENT_NOTE.md`)
is intentionally NOT inlined here because its narrowing is outside the
current bounded claim scope of this note.

## Later update

This note is kept because it is the first all-three-family snapshot at
`H = 0.25`. It is **not** the current final read on family portability.

What later changed:

- Lane α++ added Fam2 at `H = 0.20`
- Fam2 moved from `+7.0883` to `+4.5082`
- the oscillation amplitude grew from `12.2%` to `36.4%`
- the hypothesis "Fam2 just needs finer H to settle near `~5.97`" was rejected

So the current family-portability read is:

> Fam1 and Fam3 remain internally consistent near `~+5.97`; Fam2 does not
> share that behavior at the tested refinements. This note should be read as
> the pre-α++ partial snapshot, not as the current final verdict.

## Question

[`KUBO_CONTINUUM_LIMIT_NOTE.md`](KUBO_CONTINUUM_LIMIT_NOTE.md) showed
that `kubo_true` — the true first-order Kubo coefficient computed by
the parallel perturbation propagator on a static grown-DAG with
imposed 1/r field — converges to +5.986 on Fam1 with 0.2% drift at
the last refinement step (H=0.25). This lane tests whether the same
convergence holds on Fam2 and Fam3.

## Setup

Same physical parameters and refinement schedule as Lane α
(`kubo_continuum_limit.py`):

- T_phys = 15.0, PW_phys = 6.0, k*H = 2.5, S_phys = 0.004, z_src = 3.0
- Refinement: H ∈ {0.5, 0.35, 0.25}
- Three grown-DAG families: Fam1 (drift=0.20, restore=0.70),
  Fam2 (drift=0.05, restore=0.30), Fam3 (drift=0.50, restore=0.90)
- Same seed (0), same growth pattern, same Kubo computation

## Result

### kubo_true at each refinement

| H | Fam1 | Fam2 | Fam3 |
| ---: | ---: | ---: | ---: |
| 0.50 | +7.0619 | +6.6588 | +6.7420 |
| 0.35 | +5.9728 | +6.3168 | +6.3630 |
| 0.25 | **+5.9860** | **+7.0883** | **+5.9547** |

### Per-family convergence (last-step drift)

| Family | Δ last step | Status |
| --- | ---: | --- |
| Fam1 | **0.2%** | converged |
| Fam2 | **12.2%** | NOT converged, value bouncing up |
| Fam3 | **6.4%** | marginally converged, still decreasing |

### Family portability at finest H

- Fam1: +5.9860
- Fam2: +7.0883
- Fam3: +5.9547
- **Mean**: +6.3430
- **Max deviation from mean**: 0.7453 (**11.7%**)

The 11.7% max deviation exceeds the 10% family-portability
threshold for a clean positive. However:

### The internal pattern — Fam1 and Fam3 agree; Fam2 is the outlier

At H=0.25:
- Fam1 = +5.9860
- Fam3 = +5.9547
- Fam1 − Fam3 = 0.031 (**0.5%**)

**Fam1 and Fam3 agree to better than 1%** at the finest refinement.
Fam2 (+7.09) is the single outlier, and it is also the least
converged family (12.2% last-step drift, bouncing up from 6.32 to
7.09). The Fam2 finest-H value is probably still transient — its
convergence pattern is not monotone and the last step is large.

If we drop Fam2 as "not converged at this resolution," the two
converged families (Fam1, Fam3) give kubo_true ≈ **+5.97** with
spread of 0.5%. That would be a clean family-portable result on
the converged subset.

## What this establishes

1. **Lane α's Fam1 positive is not invalidated.** Fam1 still
   converges to +5.986 with 0.2% drift.
2. **Fam3 supports Fam1's value.** At the finest H, Fam3 gives
   +5.955, within 0.5% of Fam1. The two are internally consistent.
3. **Fam2 is not converged** at these refinements. Its trajectory is
   coarse → medium DOWN, medium → fine UP — non-monotone. At the time of
   this note, that left open whether finer H would rescue the family-portability
   story.
4. **Family portability cannot be claimed here.** The 11.7% max
   deviation exceeds the 10% threshold. In the original snapshot that left
   a "two out of three" partial result. After Lane α++, even that partial read
   has to be interpreted more narrowly.

## What this does NOT establish

- **Whether Fam2's converged value is also near 5.97.** This was the key open
  question in the original snapshot. Lane α++ later made the easy rescue read
  untenable.
- **Whether kubo_true is truly a family-invariant physical quantity.**
  Two of three families suggest yes, but one does not settle.
- **The origin of the discrepancy.** It could be:
  - Fam2's smaller drift (0.05) interacting with the integer rounding
    of NL / iz_range / src_layer in a way that disrupts convergence
  - A genuine family-specific continuum value for Fam2 that differs
    from Fam1/Fam3
  - Fam2 requires a longer NL at each H (i.e., larger T_phys) to
    reach the same effective integration depth as Fam1/Fam3

## Frontier map adjustment (Update 11, historical snapshot)

| Row | Update 10 (Lane α, Fam1 only) | This lane (all 3 families) |
| --- | --- | --- |
| kubo_true continuum convergence | +5.986 on Fam1, 0.2% drift | **Fam1 still converged; Fam3 converged to +5.955 (0.5% of Fam1); Fam2 not converged (12.2% last-step drift)** |
| Family portability of kubo_true | not tested | **historical partial snapshot** — Fam1/Fam3 agree within 0.5%, Fam2 outlier at H=0.25 |
| Compact underlying principle | first-order Kubo derived (Fam1 single-family) | **historically partially portable** at H=0.25; later narrowed by α++ |

## Honest read

As a standalone H=0.25 snapshot, this was not a clean positive and not a clean
negative either. After Lane α++, it should be read as:

- **Fam1 and Fam3 agree on a converged value around +5.97** with
  0.5% consistency — this is a real result.
- **Fam2 was already unstable** in this snapshot — its non-monotone
  trajectory 6.66 → 6.32 → 7.09 flagged the problem that Lane α++ later
  sharpened into a real negative.
- The 11.7% max deviation metric was dominated by Fam2 alone.
- Without Fam2, the family-portability claim would have held at this stage.
- Lane α++ later showed that the cheap Fam2 rescue does **not** land.

## What to attack next

1. **Treat Fam1/Fam3 as the retained portability subset** and stop citing
   Fam2 as an unresolved follow-up.
2. **If this lane is extended, vary the generator itself** (for example,
   restore strength) rather than re-asking whether the already-negative Fam2
   point "just needs finer H."
3. **Use other observables** like the direct-`dM` or exact-comparator lanes
   for complementary continuum evidence.

## Bottom line

> "At H=0.25, Fam1 and Fam3 already agreed to 0.5% near `~+5.97`,
> while Fam2 was a clear outlier. That original all-family snapshot is
> retained here. The later Fam2 H=0.20 refinement then rejected the easy
> rescue story: Fam2 did not settle toward `~+5.97`, it crashed to `+4.5082`
> with growing oscillation amplitude. So the current read is narrower than
> the original '2/3 partial positive': Fam1/Fam3 remain internally consistent,
> but Fam2 does not share that behavior at the tested refinements."

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- `KUBO_FAM2_REFINEMENT_NOTE.md`
  (see-also cross-reference; backticked to break cycle-0210 in the
  citation graph. The Fam2-refinement note's own §"Question" cites
  this continuum-limit families lane as the load-bearing parent that
  framed the open question driving the refinement; that direction is
  the load-bearing one. This back-edge is graph-bookkeeping
  navigation only.)
