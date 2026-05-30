# Gauge-Vacuum Plaquette First-Sector Completed Triple Sampled-Grid Boundary

**Date:** 2026-04-19 (originally); 2026-05-03 (dense-grid certificate
added); 2026-05-10 (scope narrowed); 2026-05-16 (continuous-box Lipschitz
certificate added); 2026-05-27 (finite-grid scope repair)
**Type:** no_go
**Claim type:** no_go
**Primary runner:** [`scripts/gauge_vacuum_completed_triple_dense_box_certificate_2026_05_03.py`](../scripts/gauge_vacuum_completed_triple_dense_box_certificate_2026_05_03.py)
**Companion runner:** [`scripts/frontier_gauge_vacuum_plaquette_first_sector_completed_triple_current_transfer_family_boundary_2026_04_19.py`](../scripts/frontier_gauge_vacuum_plaquette_first_sector_completed_triple_current_transfer_family_boundary_2026_04_19.py)

## Scope Repair

The continuous-box version of this row depended on empirical 2.5x
sampled-gradient Lipschitz constants. Finite gradient sampling does not
certify a global Lipschitz bound over the whole continuous parameter box.

This repair removes the continuous-box no-go from the binding claim. The row
now claims only the finite sampled-grid no-go already supported by the primary
dense runner.

No new axiom, analytic Lipschitz theorem, or interval-arithmetic certificate is
introduced.

## No-Go Boundary Checklist

This gate passes only for the finite sampled-grid no-go. It does **not** pass
the unconditional continuous-family no-go.

- **N1 alternative routes:** direct 1440-point enumeration is tested by the
  primary runner; optimal-scalar fitting is included in the evaluated `gap_at`
  route; the sampled boundary-face reference is included and remains positive;
  off-grid continuous minimizers are a live route outside this claim; alternate
  transfer-family parameterizations outside the listed box are also outside
  this claim.
- **N2 wall independence:** the finite-grid enumeration and any future
  continuous-box certificate are independent; closing one does not close the
  other.
- **N3 hidden-wall scan:** "continuous", "canonical", and "box" language is
  non-load-bearing unless tied to the explicit grid or the recorded empirical
  Lipschitz assumption.
- **N4 residual matching:** the residual here is only "no point on the
  explicit 1440-point grid"; the continuous-box residual is split off.
- **N5 rhetoric check:** the negative statement is sampled-grid resolution
  only, not lattice-wide or continuum-family resolution.
- **N6 partial-closure path:** analytic derivative bounds or interval
  arithmetic can retire the continuous-family bridge without a new axiom.
- **N7 steelman:** a hostile reviewer can correctly object that a finite grid
  does not exclude an off-grid exact zero; this is accepted and is why the
  continuous-family no-go is non-load-bearing here.
- **N8 cross-cycle echo:** earlier review already identified the same
  finite-grid versus continuous-box gap; this repair keeps only the finite
  runner-backed no-go in scope.

## Claim

On the explicit `1440`-point dense grid covering the listed parameter box

```text
tau_transfer  in [10^-4, 5e-2]   (6 log-spaced points)
tau_boundary  in [0.5, 4.0]      (6 linearly-spaced points)
asym_decay    in [10^-8, 10^-4]  (5 log-spaced points)
linear_decay  in [0.05, 1.0]     (8 linearly-spaced points)
```

at the explicit `beta = 6` `spatial_pair` witness, no sampled grid point
realizes the completed first-sector triple

```text
Z^min = (0.135165279562..., 0.374012880009..., 0.543843858544...).
```

The minimum sampled gap is

```text
||c_best Z^hat_best - Z^min||_2 = 7.791551e-03,
```

attained at the sampled grid point

```text
(tau_transfer = 1e-4, tau_boundary = 4.0, asym_decay = 1e-8, linear_decay = 0.3214).
```

This is a finite sampled-grid no-go. It is not a continuous-parameter
exclusion theorem.

## Evidence

The primary runner exhaustively evaluates the listed finite grid and reports:

```text
swept 1440 grid points
min gap                     = 7.791551e-03
median gap                  = 2.039034e-01
max gap                     = 2.856130e-01
fraction below reference gap = 0.0000
argmin grid point:
  tau_transfer = 1.0000e-04
  tau_boundary = 4.0000
  asym_decay   = 1.0000e-08
  linear_decay = 0.3214
```

The older boundary-face reference fit is not load-bearing for this repaired
row, because its optimized `linear_decay` value is not the sampled-grid
minimizer. The finite-grid claim uses the runner's reported `min gap` over the
listed 1440 sampled points.

## What This Claims

- A finite no-go on the stated `6 x 6 x 5 x 8 = 1440` sampled grid.
- The sampled-grid argmin and positive sampled minimum gap reported by the
  primary runner.
- The sampled-grid result is scoped only to the explicit `beta = 6`
  `spatial_pair` witness family, explicit `Z^min`, and optimal scalar fit
  routine used by `gap_at`.

## What This Does Not Claim

- It does not prove a continuous-box no-go over unsampled parameter values.
- It does not certify analytic or interval Lipschitz constants.
- It does not prove the sampled argmin is the true continuous minimum.
- It does not rule out a smaller gap or exact realization between grid points.
- It does not close the full framework-point packet.
- It does not add a new axiom.

## Future Work

Upgrading beyond sampled-grid scope requires one of:

- interval arithmetic over `gap_at` on the full continuous box;
- analytic operator-norm/subspace Lipschitz bounds tight enough to certify a
  positive lower bound;
- a deterministic global optimizer with a proof-level certificate; or
- an analytic monotonicity/global-minimum theorem.

The archived empirical continuous-box Lipschitz runner may remain useful as a
scouting artifact, but it is not load-bearing for this repaired row.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/gauge_vacuum_completed_triple_dense_box_certificate_2026_05_03.py
```

Expected:

```text
gauge_vacuum_completed_triple_dense_box_certificate_2026_05_03  SUMMARY: PASS=3, FAIL=0
```

Optional companion context:

```bash
PYTHONPATH=scripts python3 scripts/frontier_gauge_vacuum_plaquette_first_sector_completed_triple_current_transfer_family_boundary_2026_04_19.py
```
