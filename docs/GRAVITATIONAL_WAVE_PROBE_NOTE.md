# Gravitational Wave / Action-Form Sensitivity Probe

**Date:** original probe; scope and artifact repair 2026-05-29
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only.
**Primary runner:** [`scripts/frontier_grav_wave_post_newtonian.py`](../scripts/frontier_grav_wave_post_newtonian.py)
**Cached runner output:** [`logs/runner-cache/frontier_grav_wave_post_newtonian.txt`](../logs/runner-cache/frontier_grav_wave_post_newtonian.txt)

## 2026-05-29 Audit Repair

The audit row is conditional for two separable reasons:

```text
runner_artifact_issue:
provide the complete primary runner source, especially Tests B and C, then
re-audit the bounded toy-lattice scope; a separate retained bridge theorem is
still needed before citing physical PN/GW observables.
```

This repair addresses the artifact/scope part only. The primary runner source
in this branch contains complete implementations of Test B
`test_post_newtonian_moving_source` and Test C `test_wave_vs_laplace`; neither
is replaced by a placeholder marker. The note and runner are also narrowed so
the load-bearing claim is only finite toy-lattice sensitivity, not physical
post-Newtonian or gravitational-wave closure.

No new axiom, physical-observable bridge, or audit verdict is introduced.

## Finite Runner Surface

The runner uses a `20 x 20 x 20` ordered cubic lattice with:

```text
k = 5.0
beta = 0.8
Poisson field f from a point source
path action variants S = L(1 - f) and S = L(1 - f - f^2/2)
```

The retarded-source comparison is imposed inside the runner by sampling a
source position from an earlier layer. The `f^2` action term is also imposed
inside the runner. Neither is derived from retained framework primitives.

## Claim

On the supplied finite runner:

1. **Poisson-field gravitational waves are not established.** The Poisson field
   is elliptic/instantaneous. Radius-limited-field tests show the beam deflection is
   mostly controlled by field values near the sampled path; this is a bounded
   sensitivity result, not a dynamical wave equation.
2. **Imposed retarded-source sampling is distinguishable from instantaneous
   sampling.** For moving sources, the runner reports finite deflection
   differences between the instantaneous and hand-retarded field variants.
3. **Layer-order perturbations have layer-dependent sensitivity.** Local
   perturbations at different propagation layers affect the detector centroid
   differently because the ordered propagator has less remaining path after
   later perturbations.
4. **The imposed `f^2` action term is distinguishable from valley-linear
   action at tested strengths.** This is an action-form sensitivity result,
   not a derived post-Newtonian coefficient.

## What This Does Not Claim

- It does not derive physical gravitational waves.
- It does not derive a physical retarded potential, Lienard-Wiechert law, or
  post-Newtonian observable.
- It does not derive `c_lattice`, a physical speed-of-light normalization, or a
  map from layer index to physical time.
- It does not derive the `f^2` coefficient from Lorentz covariance or GR.
- It does not prove a continuum limit, gauge-invariant stress tensor, or
  dynamical field equation for gravity.
- It does not apply an audit verdict.

## Evidence

The primary runner source includes the full implementations of:

- Test A: `test_gravitational_waves`
- Test B: `test_post_newtonian_moving_source`
- Test C: `test_wave_vs_laplace`
- Test D: `test_action_forms`

The runner exits successfully and performs assertion checks on the returned
finite-runner data structures. It also performs executable artifact-source
checks that the Test B body, Test C body, and quantitative table-generation
strings (`d_instant`, `d_retarded`, `diff%`, `VL delta_z`, `PN delta_z`) are
present in the complete primary runner source before running the finite
toy-model tests.

Observed output includes:

```text
Poisson-field gravitational waves: NEGATIVE
Retarded-source sampling differs from instantaneous sampling up to about 15%
Layer perturbation sensitivity has a negative fitted slope
The imposed f^2 action term becomes distinguishable in the tested range
```

These are finite-runner observations only.

## Remaining Bridge

To promote this row beyond bounded toy-model sensitivity, a later theorem must
derive and audit:

- a dynamical gravitational field carrier;
- the retarded-source law rather than imposing it;
- `c_lattice` and physical time normalization;
- the physical observable/readout map; and
- the coefficient of any claimed post-Newtonian action term.

Until then, this row is only a bounded finite-lattice sensitivity probe.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_grav_wave_post_newtonian.py
```

Expected:

```text
Poisson-field gravitational waves: NEGATIVE.
Retarded-source sampling differs from instantaneous sampling up to about 15%
The imposed f^2 action term becomes distinguishable in the tested range
This runner does not derive GR, physical gravitational waves, a
post-Newtonian observable, c_lattice normalization, or an f^2 coefficient from
retained framework primitives.
```

Current cache also reports:

```text
ARTIFACT SOURCE CHECKS
  [PASS] Test B function body present
  [PASS] Test C function body present
  [PASS] source has full implementation span
```
