# Gravitational Wave / Action-Form Sensitivity Probe

**Status:** bounded - bounded or caveated result note
**Type:** bounded_theorem
**Status authority:** independent audit lane only.

## 2026-05-28 Audit Repair (load-bearing core split from unsupplied bridge)

The 2026-05-28 audit verdict was `audited_conditional`:

> *"The runner computes internal toy-lattice differences, but the note relabels those differences as post-Newtonian or gravitational-wave-adjacent physics without a cited bridge theorem deriving the retarded potential, c_lattice, PN observable,"*

with repair: *"missing_bridge_theorem — derive and cite a retained theorem mapping the lattice propagation/readout and f^2 action to a physical post-Newtonian observable, then rerun a non-imposed comparator."*.

Supplying the named retained authority/bridge is substantive new work, out of
scope for this repair. This revision takes the **split path**:

- **Load-bearing (in scope):** The runner's internal toy-lattice computations: the measured propagation differences between retarded and instantaneous potential sampling (Tests B, C) and the f^2 action correction magnitudes (Test D) on the 20x20x20 lattice, which are exactly computed finite-lattice differences without reference to any physical observable.
- **NON-load-bearing (split off / admitted):** The identification of those toy-lattice differences with physical post-Newtonian or gravitational-wave observables; this requires a retained bridge theorem deriving the retarded-potential / PN-observable mapping from the lattice propagation/readout and f^2 action, which is not supplied and is recorded here as an admitted, not-derived relabeling.

No new axiom, import, or retained bridge is introduced. The runner-verified
core is the load-bearing content; the named bridge stays an admitted,
non-load-bearing input until a retained authority for it lands.

## Status: Three of four tests positive

## Scope Repair

Audit found that the finite runner distinguishes several internally defined
variants, but the old note overinterpreted those variants as physical
beyond-Newtonian / post-Newtonian / GR observables. The missing bridge is a
retained theorem deriving the dynamical carrier, retarded-source law,
`c_lattice` normalization, physical readout, and `f^2` coefficient from
framework primitives.

This repair keeps only the bounded finite-lattice sensitivity results and the
honest negative for Poisson-field gravitational waves.

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
   is elliptic/instantaneous. Truncated-field tests show the beam deflection is
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

The runner exits successfully and performs assertion checks on the returned
finite-runner data structures.

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
...
This runner does not derive GR, physical gravitational waves, a
post-Newtonian observable, c_lattice normalization, or an f^2
coefficient from retained framework primitives.
```
