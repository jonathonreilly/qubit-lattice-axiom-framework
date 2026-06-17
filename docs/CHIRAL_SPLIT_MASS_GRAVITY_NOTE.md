# Chiral Split-Mass / Split-Gravity Note

**Primary runner:** `scripts/frontier_chiral_split_mass_gravity.py`
**Type:** open_gate
**Status authority:** independent audit lane only.
**Claim scope:** Exploratory diagnostic suggesting that, on this 1D
chiral-walk toy harness, the introduced `g` parameter gives an
independent linear control of the gravity-induced centroid shift at
fixed `theta_m`. No claim of `theta_m` flattening, k-achromaticity, or
overload-bottleneck closure is made by this note.

## Boundary repair (2026-05-23)

This note is narrowed to the runner-supported boundary: the harness is at
most an exploratory diagnostic suggesting that `g` gives an independent
linear control at fixed `theta_m`. The previous bottleneck-closure framing and
the associated "early-warning closure condition" language are withdrawn; the
runner's own internal verdict string is not load-bearing for any audited
claim.

## What the harness supports (within the named claim boundary)

The runner exercises a 1D unitary chiral walk with coin angle
modulated by a local scalar field. Two parameterizations are run:

- Overloaded baseline: `theta_eff = theta_m * (1 - theta_m * f)`.
  The same `theta_m` controls both the free dispersion gap and the
  local field response.
- Split parameterization: `theta_eff = theta_m * (1 - g * f)`.
  `theta_m` sets the free gap; `g` is a separate susceptibility
  parameter on the field-response coefficient.

On the harness's reference point `theta_m = 0.30`, `k0 = 0.60`,
strength `5e-4`, sweeping `g ∈ {0.0, 0.1, 0.2, 0.3, 0.4, 0.5}` the
centroid-shift response is linear in `g` to numerical fit accuracy
(`R^2 ≈ 1.0000` in the cached runner stdout). This is the single
observation that survives the audit boundary and is reported as an
exploratory diagnostic only.

## What this note does NOT claim

- It does not claim a flattening of the `theta_m` sweep. The runner
  shows split envelope CV ≈ 0.90 vs baseline CV ≈ 1.08 and split
  envelope exponent ≈ 2.80 vs baseline ≈ 3.80; the residual
  `theta_m`-dependence is not small.
- It does not claim k-achromaticity. The runner shows baseline and
  split `CV_k` both ≈ 2.66 at `theta_m = 0.30`; the response is
  strongly k-chromatic in both modes.
- It does not establish that overloading `theta_m` is a bottleneck.
  The split parameterization does not, on the supplied stdout,
  remove the `theta_m` sensitivity; the prior "bottleneck"
  conclusion is withdrawn.
- It does not import or modify any framework axiom and does not
  promote any audited row.

## Downstream source-boundary firewall

Allowed downstream uses of this packet are limited to:

- cite it as an exploratory fixed-theta `g`-linearity diagnostic in a
  1D local-unitary chiral-walk toy harness;
- cite the runner's local checks of free dispersion, field-strength
  scaling, `g`-sweep linearity, `theta_m` sweep, and `k` sweep;
- cite the negative boundary that theta sensitivity and k-achromatic
  closure remain open.

Forbidden downstream uses without a new retained bridge:

- do not cite this packet as a framework-level mass-gravity theorem;
- do not cite it as equivalence-principle closure;
- do not cite it as `theta_m` flattening closure;
- do not cite it as k-achromatic closure;
- do not cite it as overload-bottleneck closure;
- do not cite it as a physical gravitation value, fitted selector, or
  observational match;
- do not use it to promote any audited row.

Re-audit should be triggered if a downstream row applies this class-C
toy-harness diagnostic to a framework-level mass-gravity claim,
equivalence-principle claim, or residual-closure claim without adding a
new retained bridge and explicit numeric thresholds.

## Diagnostic context for the 10-card (informational only)

The following rows are recorded as the harness's current diagnostic
panels. They are exploratory diagnostics, not pass criteria:

1. `theta_m`-sweep at fixed `g` — records centroid shift across
   several `theta_m` values.
2. `g`-sweep at fixed `theta_m` — records linearity of the centroid
   shift in `g` at the harness's reference point.
3. `k`-sweep at fixed `theta_m` — records `CV` of the centroid shift
   across a fixed carrier band.
4. Free dispersion / KG fit — records that the field-free dispersion
   matches `arccos(cos(theta_m) cos(k))` and the small-`k` fit
   recovers the expected gap.
5. Field-strength scaling at fixed `theta_m` — records the slope of
   `|deflection|` vs strength.

These rows are reported for transparency; no pass/fail threshold in
the source note is load-bearing under the present claim boundary.

## What would close this lane (Path A future work)

Promoting from the present exploratory diagnostic to anything
stronger would require, at minimum:

1. A derivation in the framework primitives of what `theta_m`
   "flattening" would look like, with explicit numeric thresholds
   stated in the source note (e.g. a target on the split
   `theta_m`-envelope CV and on the baseline-vs-split CV ratio).
2. A runner verdict that enforces those thresholds together with a
   k-achromaticity threshold and an observable-consistency check
   (centroid vs peak vs first-arrival) and reports PASS/FAIL on
   each.
3. A demonstration on the supplied stdout (not merely a tuned toy
   threshold) that the split parameterization satisfies those
   thresholds simultaneously.

Until those exist, this row stays at the exploratory-diagnostic
boundary the auditor named.
