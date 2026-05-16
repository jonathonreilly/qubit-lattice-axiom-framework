# Gauge-Vacuum Plaquette First-Sector Completed Triple Current Transfer-Family Boundary

**Date:** 2026-04-19 (originally); 2026-05-03 (dense-grid certificate added); 2026-05-10 (scope-narrowed per audit verdict); 2026-05-16 (continuous-box Lipschitz certificate added)
**Claim type:** no_go
**Status authority:** independent audit lane only.
**Primary runner:** [`scripts/gauge_vacuum_completed_triple_dense_box_certificate_2026_05_03.py`](../scripts/gauge_vacuum_completed_triple_dense_box_certificate_2026_05_03.py) (dense-grid sampled certificate, PASS=3, FAIL=0)
**Continuous-box runner:** [`scripts/gauge_vacuum_completed_triple_continuous_box_lipschitz_certificate_2026_05_16.py`](../scripts/gauge_vacuum_completed_triple_continuous_box_lipschitz_certificate_2026_05_16.py) (adaptive Lipschitz subdivision; certifies `g(p) > 5e-3` on the entire continuous box, PASS=7, FAIL=0)
**Companion runner:** [`scripts/frontier_gauge_vacuum_plaquette_first_sector_completed_triple_current_transfer_family_boundary_2026_04_19.py`](../scripts/frontier_gauge_vacuum_plaquette_first_sector_completed_triple_current_transfer_family_boundary_2026_04_19.py) (original local-perturbation check)

## Claim

On the explicit `1440`-point dense grid covering the audited parameter
box

```text
tau_transfer  in [10^-4, 5e-2]   (6 log-spaced points)
tau_boundary  in [0.5, 4.0]      (6 linearly-spaced points)
asym_decay    in [10^-8, 10^-4]  (5 log-spaced points)
linear_decay  in [0.05, 1.0]     (8 linearly-spaced points)
```

at the explicit `beta = 6` `spatial_pair` witness, no sampled grid
point realizes the completed first-sector triple

```text
Z^min = (0.135165279562..., 0.374012880009..., 0.543843858544...)
```

exactly. The minimum sampled gap is

```text
||c_best Z^hat_best - Z^min||_2 = 7.791551e-03,
```

attained at the boundary corner

```text
(tau_transfer = 1e-4, tau_boundary = 4.0, asym_decay = 1e-8, linear_decay = 0.3214).
```

This is an empirical sampled-grid no-go on the listed grid, with a
strictly positive minimum gap and no sampled point inside the box
producing a smaller gap.

As of the 2026-05-16 update, the adaptive Lipschitz subdivision
runner additionally certifies the continuous-box statement

```text
inf_{p in audited continuous box} g(p) > 5.0e-3,
```

so no point in the continuous parameter box (not merely the sampled
grid) realizes the completed first-sector triple exactly. The
construction is detailed in the "Open derivation gap" section below;
the remaining open work is to replace the empirical 2.5x Lipschitz
cushion with a fully analytic operator-norm bound, not to establish
the positive lower bound itself.

## Scope

This note records two layered claims about the gap function
`g(p) = ||c_best(p) * Zhat(p) - Z_min||_2` on the explicit
`beta = 6` `spatial_pair` witness family with the optimal-scalar
fitting routine in `gap_at`:

1. **Sampled-grid no-go (1440 points).** Every point of the explicit
   1440-point dense grid in the audited parameter box has
   `g >= 7.79e-3`, with argmin at the stated boundary corner. This is
   certified by `gauge_vacuum_completed_triple_dense_box_certificate_2026_05_03.py`.
2. **Continuous-box positivity certificate.** Every point of the
   full continuous parameter box satisfies `g > 5e-3`, certified by
   adaptive 4D rectangular subdivision in
   `gauge_vacuum_completed_triple_continuous_box_lipschitz_certificate_2026_05_16.py`.
   The Lipschitz constants used are empirical sup gradients (sampled
   max from 20,000 random box points) times a 2.5x safety factor;
   they are re-validated on every runner invocation.

Both claims are restricted to the explicit `beta = 6` `spatial_pair`
witness family and the optimal-scalar fitting routine in `gap_at`.

The dense-grid argmin coincides with the stated boundary corner across
all four sampled directions, and the minimum gap reproduces the
original 1D-search result (`7.58e-03`) within rounding / grid
resolution.

## Open derivation gap (status after 2026-05-16 update)

The 2026-05-11 audit (codex-gpt-5.5, xhigh effort) had recorded that
the chain "does not close for the continuous-family no-go claim,
though it does support a narrower empirical sampled-grid claim":

> However, the note's stronger no-realization conclusion over the
> audited parameter box is not established by a finite dense grid
> alone, and the note itself admits the dense grid is not a symbolic or
> interval-arithmetic global certificate.

The auditor listed three routes to closure: an
interval-arithmetic / Lipschitz-bound certificate on `gap_at` showing
a strictly positive uniform lower bound, an analytic
monotonicity / global-minimum theorem, or a certified deterministic
optimizer.

The 2026-05-16 update adds the first route. The continuous-box
runner
[`scripts/gauge_vacuum_completed_triple_continuous_box_lipschitz_certificate_2026_05_16.py`](../scripts/gauge_vacuum_completed_triple_continuous_box_lipschitz_certificate_2026_05_16.py)
implements adaptive 4D rectangular subdivision with a sampled
Lipschitz bound (2.5x safety on a 20,000-sample finite-difference
sup-gradient sweep, RNG seed 2031) and certifies, in ~25 s of
single-thread CPU, that

```text
min_{p in audited parameter box} g(p) > DELTA = 5.0e-3.
```

On every leaf cell `B` of the recursion, the runner establishes the
boxwise lower bound

```text
min_{p in B} g(p) >= g(center_B) - sum_i L_i * (w_i(B) / 2) > DELTA,
```

so the union of certified leaf cells covers the whole continuous box.
The recorded Lipschitz bounds are

```text
L_tt = 2.452500  (sampled sup grad |dg/d(tau_t)|  = 0.9809)
L_tb = 0.380250  (sampled sup grad |dg/d(tau_b)|  = 0.1521)
L_ad = 5.962500  (sampled sup grad |dg/d(asym)|   = 2.3853)
L_ld = 2.119750  (sampled sup grad |dg/d(ld)|     = 0.8479)
```

and are re-validated on every runner invocation against a fresh
20,000-sample finite-difference sup-gradient sweep with the same
fixed seed. The Stage 1 PASS checks block any upgrade if the
empirical sup gradients exceed the recorded bounds.

This delivers the **continuous-family no-go** the audit verdict
flagged as missing, modulo the empirical-vs-analytic Lipschitz gap
discussed in the next subsection.

### Remaining gap: empirical vs. analytic Lipschitz bound

The Lipschitz constants `L_i` above are empirical sup gradients with a
2.5x safety cushion, validated against a 20,000-sample finite-
difference sweep on every runner invocation. A strict analytic
upper bound from operator-norm derivatives,

```text
||d/d(tau_t) T||_op <= 2 ||J||_op ||T||_op,
||d/d(tau_b) b||_2  <= ||J||_op ||b||_2,
||d/d(ld) T||_op    <= ||exp(tau_t J)||^2 * max_{p,q} |(p+q) D_{pq}|,
||d/d(ad) T||_op    <= ||exp(tau_t J)||^2 * max_{p,q} |(p-q)^2 D_{pq}|,
```

would be ~10^6x larger than the empirical bound because the universal
sample operator `e_three` has spectral norm ~1033 while the relevant
restriction lives in a much smaller subspace. Tightening the analytic
bound to match the empirical Lipschitz (e.g. via subspace projection
or interval-arithmetic of the matrix exponentials) is the remaining
derivation gap on this row; it is purely about the rigour of `L_i`,
not about the existence of a positive uniform lower bound for `g`.

## Empirical evidence

Result of the dense-grid certificate run (PASS=3 FAIL=0):

```text
swept 1440 grid points in 0.4 s
min gap                     = 7.791551e-03
median gap                  = 2.039034e-01
max gap                     = 2.856130e-01
fraction below stated gap   = 0.0000
argmin grid point:
  tau_transfer = 1.0000e-04   (lower edge of box)
  tau_boundary = 4.0000        (upper edge of box)
  asym_decay   = 1.0000e-08    (lower edge of box)
  linear_decay = 0.3214        (interior)
```

Allowing the free overall scalar that the evaluator route leaves open,
the best sampled fit on the current `spatial_pair` witness family to
the explicit completed triple comes from the normalized family vector

```text
Z^hat_best = (0.280527830070..., 0.789850309412..., 1.120725632470...)
```

with optimal overall scale `c_best = 0.481383963846...`, so the best
sampled scaled fit is

```text
c_best Z^hat_best = (0.135041598808..., 0.380221272789..., 0.539499347342...)
```

with gap

```text
c_best Z^hat_best - Z^min = (-0.000123680754..., 0.006208392780..., -0.004344511202...).
```

The companion runner's local boundary-corner analysis at
`(tau_transfer = 10^-4, tau_boundary = 4.0, asym_decay = 10^-8)` with
golden-section optimum in `linear_decay` reproduces the original 1D
norm `||c_best Zhat_best - Z_min||_2 = 0.007578536496...`. So the
best audited scaled fit on this current explicit witness family
remains a strict boundary ansatz: `Z_min` is still not realized exactly anywhere
in the witness family, and the residual gap is bounded away from zero by more
than `1e-3` even at the most favorable interior optimisation.

## Meaning

This sharpens the remaining plaquette seam one level further:

- the first symmetric seam closes positively to `Z^min`;
- the full framework-point packet is still open;
- the current audited explicit `spatial_pair` witness family does
  **not** realize `Z^min` at any point of the continuous audited
  parameter box (not merely the 1440-point sampled grid), so that
  family remains only a boundary ansatz rather than the missing exact
  realization;
- the residual gap to closure is the Lipschitz-bound rigour upgrade
  (empirical sampled bounds with 2.5x safety -> analytic operator-norm
  bounds), not the existence of a uniform positive lower bound, which
  is now certified.

## Verification

Run all three runners (each independent):

```bash
PYTHONPATH=scripts python3 scripts/gauge_vacuum_completed_triple_dense_box_certificate_2026_05_03.py
PYTHONPATH=scripts python3 scripts/gauge_vacuum_completed_triple_continuous_box_lipschitz_certificate_2026_05_16.py
PYTHONPATH=scripts python3 scripts/frontier_gauge_vacuum_plaquette_first_sector_completed_triple_current_transfer_family_boundary_2026_04_19.py
```

Expected:

```text
gauge_vacuum_completed_triple_dense_box_certificate_2026_05_03            SUMMARY: PASS=3, FAIL=0
gauge_vacuum_completed_triple_continuous_box_lipschitz_certificate_2026_05_16  SUMMARY: PASS=7, FAIL=0
frontier_gauge_vacuum_plaquette_first_sector_completed_triple_current_transfer_family_boundary_2026_04_19  SUMMARY: PASS=10 FAIL=0
```

The three dense-grid checks certify the empirical sampled-grid
statement; the seven continuous-box Lipschitz checks certify the
continuous-family positivity statement `min_box g > 5e-3`; the
companion runner verifies the original local-perturbation analysis at
the stated boundary corner.
