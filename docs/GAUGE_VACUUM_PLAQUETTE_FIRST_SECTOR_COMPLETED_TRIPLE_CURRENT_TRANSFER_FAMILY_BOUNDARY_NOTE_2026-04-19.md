# Gauge-Vacuum Plaquette First-Sector Completed Triple Sampled-Grid Boundary

**Date:** 2026-04-19 (originally); 2026-05-03 (dense-grid certificate added); 2026-05-10 (scope-narrowed per audit verdict); 2026-05-16 (continuous-box Lipschitz certificate added)
**Type:** no_go
**Claim type:** no_go
**Status authority:** independent audit lane only.
**Primary runner:** [`scripts/gauge_vacuum_completed_triple_dense_box_certificate_2026_05_03.py`](../scripts/gauge_vacuum_completed_triple_dense_box_certificate_2026_05_03.py)
**Companion runner:** [`scripts/frontier_gauge_vacuum_plaquette_first_sector_completed_triple_current_transfer_family_boundary_2026_04_19.py`](../scripts/frontier_gauge_vacuum_plaquette_first_sector_completed_triple_current_transfer_family_boundary_2026_04_19.py)

## Scope Repair

The continuous-box version of this row depended on empirical 2.5x
sampled-gradient Lipschitz constants. Audit correctly held that finite
gradient sampling does not certify a global Lipschitz bound over the whole
continuous parameter box.

This repair removes the continuous-box no-go from the binding claim. The row
now claims only the finite sampled-grid no-go already supported by the primary
dense runner.

No new axiom, analytic Lipschitz theorem, interval-arithmetic certificate, or
audit verdict is introduced.

## 2026-05-28 Audit Repair (load-bearing core split from unsupplied bridge)

The 2026-05-28 audit verdict was `audited_conditional`:

> *"The finite sampled-grid statement closes against the provided runner output. The continuous-family no-go does not close because the global Lipschitz constants are empirical finite-difference bounds rather than analytic or interval-certified"*

with repair: *"missing_bridge_theorem: certify the Lipschitz constants analytically or by interval arithmetic, then rerun the continuous-box certificate with those certified bounds."*.

Supplying the named retained authority/bridge is substantive new work, out of
scope for this repair. This revision takes the **split path**:

- **Load-bearing (in scope):** The runner-certified sampled-grid no-go over the explicit 1440-point dense grid (PASS=3, FAIL=0), establishing that no point in the listed grid realizes the completed first-sector triple with gap below `7.79e-3`; the continuous-box Lipschitz subdivision runner provides conditional support for the continuous-box statement under the empirically validated 2.5x safety-cushion Lipschitz constants.
- **NON-load-bearing (split off / admitted):** The unconditional continuous-family no-go claim, which requires analytic or interval-arithmetic certification of the Lipschitz constants rather than the empirical finite-difference sup-gradient bounds currently recorded; that certification is the named missing bridge and stays an admitted, not-yet-closed derivation target.

No new axiom, import, or retained bridge is introduced. The runner-verified
core is the load-bearing content; the named bridge stays an admitted,
non-load-bearing input until a retained authority for it lands.

## No-Go Discipline Gate (review-loop 2026-05-29)

This gate passes only for the finite sampled-grid no-go. It does **not** pass
the unconditional continuous-family no-go.

- **N1 alternative routes:** direct 1440-point enumeration is tested; the
  empirical-Lipschitz subdivision route is conditional support only; analytic
  Lipschitz or interval-arithmetic certification is the named missing bridge;
  off-grid continuous minimizers are outside the retained claim; alternate
  transfer-family parameterizations outside the audited box are outside scope.
- **N2 wall independence:** the sampled-grid enumeration and the certified
  continuous-box bridge are independent; closing one does not close the other.
- **N3 hidden-wall scan:** "continuous", "canonical", and "box" language is
  non-load-bearing unless tied to the explicit grid or the stated empirical
  Lipschitz assumption.
- **N4 residual matching:** the residual retained here is only "no point on
  the explicit 1440-point grid"; the continuous-box residual is split off.
- **N5 rhetoric audit:** the negative statement is sampled-grid resolution
  only, not lattice-wide or continuum-family resolution.
- **N6 partial-closure path:** analytic derivative bounds or interval
  arithmetic can retire the continuous-family bridge without a new axiom.
- **N7 steelman:** a hostile reviewer can correctly object that a finite grid
  does not exclude an off-grid exact zero; this is accepted and is why the
  continuous-family no-go is non-load-bearing here.
- **N8 cross-cycle echo:** the earlier audit already identified the same
  finite-grid versus continuous-box gap; this repair keeps only the finite
  runner-backed no-go in scope.

## Claim

On the explicit `1440`-point dense grid covering the audited parameter box

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

attained at the sampled boundary corner

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
fraction below stated gap   = 0.0000
argmin grid point:
  tau_transfer = 1.0000e-04
  tau_boundary = 4.0000
  asym_decay   = 1.0000e-08
  linear_decay = 0.3214
```

Allowing the free overall scalar that the evaluator route leaves open, the
best sampled fit on the current `spatial_pair` witness family to the explicit
completed triple comes from

```text
Z^hat_best = (0.280527830070..., 0.789850309412..., 1.120725632470...),
c_best = 0.481383963846...,
```

so

```text
c_best Z^hat_best
  = (0.135041598808..., 0.380221272789..., 0.539499347342...),
```

with residual

```text
c_best Z^hat_best - Z^min
  = (-0.000123680754..., 0.006208392780..., -0.004344511202...).
```

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
- It does not prove the sampled argmin is the true continuous global minimum.
- It does not rule out a smaller gap or exact realization between grid points.
- It does not close the full framework-point packet.
- It does not add a new axiom or apply an audit verdict.

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
