# Mesoscopic Surrogate Threshold 2D Note

**Date:** 2026-04-04 (finite-computation certificate expanded 2026-07-11)
**Status:** bounded support note for the listed finite 2D sourced-response stability sweep.
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only; effective status is pipeline-derived after independent review.

## Artifact chain

- Script: [`scripts/mesoscopic_surrogate_threshold_2d.py`](../scripts/mesoscopic_surrogate_threshold_2d.py)
- Computational helpers:
  [`scripts/mesoscopic_surrogate_two_stage_2d.py`](../scripts/mesoscopic_surrogate_two_stage_2d.py)
  and
  [`scripts/lattice_2d_continuum_distance.py`](../scripts/lattice_2d_continuum_distance.py)
- Audit cache stdout:
  [`logs/runner-cache/mesoscopic_surrogate_threshold_2d.txt`](../logs/runner-cache/mesoscopic_surrogate_threshold_2d.txt)
- Frozen legacy log:
  [`logs/2026-04-04-mesoscopic-surrogate-threshold-2d.txt`](../logs/2026-04-04-mesoscopic-surrogate-threshold-2d.txt)
- Reproduction command: `python3 scripts/mesoscopic_surrogate_threshold_2d.py`

## Question

Does shrinking the surrogate-source support on the retained 2D ordered-lattice
family produce a clear threshold where the two-stage sourced-response control
breaks?

## Frozen setup

- fixed 2D ordered-lattice harness with `h=0.5`, physical width `W=12`,
  physical length `L=20`, and next-layer reach `max_d_phys=5`
- point probe launched at `y=5`, field strength `5e-5`, inverse-distance
  softening `0.1`, angular weight `BETA=0.8`, and phase scale `K=5`
- barrier at layer `nl//3`, source field at layer `2*nl//3`, detector at the
  final layer, and slit boundary `|y| >= 3`
- distributed source weights normalized to one; equal-strength point control
  placed at the nearest lattice row to the distributed-source centroid
- support sweep over `topN = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 16, 20, 25,
  32, 40, 49, 64, 81`
- stability criterion:
  - relative stage-1 / stage-2 ratio difference `<= 1%`
  - source carry `>= 0.99`

## Computed quantities

Let `C_N[p]` retain the `N` largest entries of a normalized detector profile
`p` and renormalize the retained entries. For each scanned `N = topN`, the
runner computes

```text
s1 = C_N[p_free]
p1 = propagated detector profile sourced by s1
s2 = C_N[p1]
```

For a normalized source profile `s`, the sourced-response ratio is

```text
mu_H(s) = H round(mu(s) / H)
R(s)    = (mu(P_dist(s)) - mu(p_free))
          / (mu(P_point(mu_H(s))) - mu(p_free)),
```

where `P_dist(s)` is the propagated detector profile in the distributed field
of `s`, `P_point(mu_H(s))` is the equal-strength point-source control at the
nearest lattice realization of the centroid, `H=0.5`, and `mu` is the
detector-profile centroid. The two stability observables are therefore
computed, rather than imported, as

```text
ratio_rel_err = abs(R(s2) - R(s1)) / max(abs(R(s1)), 1e-30)
carry         = sum_y sqrt(s1(y) s2(y)).
```

A row is stable exactly when `ratio_rel_err <= 0.01` and `carry >= 0.99`.

## Result

Every scanned `topN` value stayed stable. The audit-cache rows expose the
higher-precision printed ratio error used by the gate:

| `topN` | `stage1_ratio` | `stage2_ratio` | `ratio_rel_err` | `carry` | stable |
|---:|---:|---:|---:|---:|:---:|
| 1 | 1 | 1 | 0 | 1.0000000 | yes |
| 2 | 1.30708334 | 1.30707376 | 7.323738e-06 | 1.0000000 | yes |
| 3 | 1.01866776 | 1.0186448 | 2.253890e-05 | 1.0000000 | yes |
| 4 | 1.0551808 | 1.05513844 | 4.014529e-05 | 1.0000000 | yes |
| 5 | 0.557478729 | 0.557433191 | 8.168514e-05 | 1.0000000 | yes |
| 6 | 1.78665921 | 1.78649651 | 9.106127e-05 | 1.0000000 | yes |
| 7 | 1.71323212 | 1.71310341 | 7.512914e-05 | 1.0000000 | yes |
| 8 | 0.874344611 | 0.874175303 | 1.936404e-04 | 1.0000000 | yes |
| 9 | 0.654904098 | 0.654779355 | 1.904749e-04 | 1.0000000 | yes |
| 10 | 0.773677005 | 0.773595599 | 1.052192e-04 | 1.0000000 | yes |
| 12 | 0.0302014108 | 0.0300018732 | 0.006606898 | 1.0000000 | yes |
| 16 | 0.467612959 | 0.467527065 | 1.836863e-04 | 1.0000000 | yes |
| 20 | 0.336642076 | 0.336590639 | 1.527923e-04 | 1.0000000 | yes |
| 25 | 0.371745590 | 0.371709488 | 9.711719e-05 | 1.0000000 | yes |
| 32 | 0.385423623 | 0.385390076 | 8.703918e-05 | 1.0000000 | yes |
| 40 | 0.116717007 | 0.116706969 | 8.600156e-05 | 1.0000000 | yes |
| 49 | 0.116753931 | 0.116743900 | 8.591456e-05 | 1.0000000 | yes |
| 64 | 0.116753931 | 0.116743900 | 8.591456e-05 | 1.0000000 | yes |
| 81 | 0.116753931 | 0.116743900 | 8.591456e-05 | 1.0000000 | yes |

The frozen rows show:

- the runner recomputes every listed support row from the 2D ordered-lattice
  harness
- the maximum relative stage-1 / stage-2 sourced-response ratio difference is
  `0.0066069`, below the `0.01` stability ceiling
- the support carry stays at `1.000` across the scan
- none of the listed support values causes a stability collapse

The detector profile has 49 bins, so `topN=64` and `topN=81` saturate the same
full-support profile as `topN=49`. They are retained in the frozen schedule and
their duplicate rows are explicit in the table.

The smallest scanned support, `topN = 1`, is already stable.

The current audit cache supplies the finite-computation packet with assertion
gates:

- `frozen_topN_support_list_scanned`
- `all_scanned_topN_stable`
- `stage_ratio_relative_error_within_one_percent`
- `support_carry_floor`
- `smallest_listed_support_stable`

## Safe read

This 2D control shows stable response at every listed support value.

So on the retained 2D family:

- no listed source-support choice is a collapse witness
- the mesoscopic surrogate remains stable at the smallest listed support
- intermediate unlisted supports and other geometries remain outside the
  finite claim

## Implication for the inertial-response lane

This note tightens the blocker rather than closing it:

- the broad mesoscopic surrogate survives support shrinkage in the retained
  2D family
- construction of a localized persistent-mass object lies outside this test
- so it remains a bounded control, not a persistent-mass theorem

The cheapest future move is therefore:

- try a smaller localized source object on another already-bounded family only
  if it preserves the same multistage sourced-response stability
- otherwise stop treating support shrinkage as the main bottleneck and move on
  to a genuinely different family or mechanism

## Audit boundary (2026-04-28)

The earlier status prose mixed bounded-control wording with a proposed
retention label, which was not a source-science statement and is no longer
used here. This note now carries only the bounded finite sweep and leaves all
audit verdicts to the independent audit lane.

## What this note does NOT claim

- A persistent-mass theorem.
- An inertial-response theorem.
- A sharp support-shrinking threshold (the sweep does not find one).

## What would close this lane (Path A future work)

A separate retained theorem deriving a persistent-mass object from the
sweep would require a registered runner with explicit pass thresholds
for what counts as "persistent mass" and "inertial response", with
assertion-gated support-shrinking criteria.
