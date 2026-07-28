# Self-Consistency Preference for Poisson Field Equation

**Type:** bounded_theorem
**Status:** bounded - bounded or caveated result note
## Status: review hold; bounded operator-preference result

## Context

A key reviewer objection is that the framework may be dressing up Poisson
input as emergence. This note documents a narrower result: on the tested
nearest-neighbor cubic lattice, unscreened Poisson is the best-supported
member of the audited operator family and the only one in that sweep that
stays near the Newtonian target.

## The Self-Consistency Argument

If we demand that the gravitational field phi is sourced by the density
rho = |psi|^2 of the propagator that evolves IN that field, then:

1. The propagator uses action S = L(1-phi) with nearest-neighbor hops.
2. The density rho = |psi|^2 sources the field via some operator: L phi = -G rho.
3. Self-consistency requires the fixed point: phi_* such that
   L phi_* = -G |psi(phi_*)|^2.
4. On a graph with nearest-neighbor coupling, the propagator's Green's
   function IS the inverse of the graph Laplacian.
5. Therefore the inverse graph Laplacian is a natural candidate for a
   self-consistent field operator on this surface.

## Numerical Evidence

Script: `scripts/frontier_self_consistent_field_equation.py`
Lattice: 3D cubic, N=20 and N=24, Dirichlet BC.

### Test 1: Poisson Converges

Self-consistent iteration (propagate -> measure rho -> solve Poisson -> repeat)
converges in ~10 iterations with mixing alpha=0.3. The converged field is:
- Attractive (phi > 0 near source)
- Monotonically decaying
- Approximately `1/r^beta` with raw finite-grid `beta ~ 1.28` (no continuum
  interpretation is established; see caveat)

### Test 2: Alternative Field Equations Underperform

| Equation | Converged? | Attractive? | beta | Physical? |
|----------|-----------|-------------|------|-----------|
| Poisson (nabla^2 phi = rho) | Yes (10 iter) | YES | 1.28 | YES |
| Biharmonic (nabla^4 phi = rho) | Yes (22 iter) | NO | 0.87 | NO |
| 1/r^2 kernel | No (20 iter) | NO | 1.03 | NO |
| Local (phi = G*rho) | Yes (7 iter) | NO | 8.64 | NO |
| Random PD kernel | Yes (2 iter) | NO | 4.19 | NO |

Among the non-screened alternatives tested here, Poisson is the only one that
produces an attractive well with a near-Newtonian decay. That is a meaningful
discriminator, but it is not a proof that all other local operators fail.

### Test 3: Susceptibility Matches Poisson Green's Function

The propagator's integrated density response to localized field perturbations
at distance r correlates with the Poisson Green's function profile:
- Shape correlation: 0.93 (strong match)
- This confirms that the propagator's own structure selects the inverse
  Laplacian as its natural response kernel.

### Test 4: Screened Poisson Sweep

Among operators (nabla^2 - mu^2) phi = rho:
- mu^2 = 0 (pure Poisson): beta = 1.28 (closest to 1.0)
- mu^2 = 0.1: beta = 1.72
- mu^2 = 1.0: beta = 3.55
- mu^2 = 2.0: beta = 4.49

Within the screened-Poisson family, all tested `mu^2` values remain
self-consistent and attractive, but only the unscreened case stays close to
the `1/r` Newtonian target. Mass terms push the decay toward Yukawa behavior.

## Bounded Claims

1. On this 3D cubic lattice with nearest-neighbor coupling, unscreened
   Poisson is the best-supported operator in the tested family and the only
   tested one that stays close to the Newtonian target.

2. Among the tested alternatives, unscreened Poisson is preferred over
   biharmonic, local, random-kernel, and screened variants when the target is
   an attractive monotone field with near-`1/r` decay.

3. The propagator's density susceptibility profile correlates (`r = 0.93`)
   with the Poisson Green's function, providing supportive evidence that the
   inverse Laplacian is a natural response kernel on this surface.

## Caveats

- **Finite-grid beta**: The measured `beta ~ 1.28` is a raw fit on the
  declared small Dirichlet grids; this note does not establish that its
  difference from `1.0` is a finite-size effect. The previously cited
  distance-law script computes ray deflection in a prescribed `f=s/r` field,
  not this self-consistent beta. The bounded companion runner
  [`physical_poisson_self_consistent_beta_caveat_bounded_diagnostic_2026_07_26.py`](../scripts/physical_poisson_self_consistent_beta_caveat_bounded_diagnostic_2026_07_26.py)
  finds that two selected finite-data fits give intercepts `1.2747` and
  `1.1578`, while the parent propagator's per-layer normalization gives every
  computed density a uniform x-layer marginal `1/N`. A localized-source,
  source-exterior diagnostic or a bridge between the two observables remains
  open.

  Source-side repair record (2026-07-28, PR #5662): the unsupported continuum
  sentence was withdrawn and the beta statement narrowed to the finite
  numerical protocol; no audit grade or full parent-row closure is asserted.

- **Lattice-level result**: This demonstration is on an ordered cubic lattice.
  Extension to grown/random graphs requires separate verification.

- **Linear response regime**: The susceptibility test uses small perturbations
  (delta_phi = 0.1). Nonlinear regime behavior is not tested.

- **This is not a uniqueness theorem**: the code tests a finite operator
  family, not the full space of local or nonlocal kernels.

## Significance for the Paper

This result narrows the circularity objection but does not eliminate it
completely. The safe read is:

1. the propagator has nearest-neighbor coupling and a susceptibility profile
   close to the Poisson Green's function
2. unscreened Poisson is preferred over the tested alternatives when the goal
   is an attractive near-Newtonian self-consistent fixed point
3. this is strong review-grade evidence for Poisson preference on this surface,
   not a proof that Poisson is uniquely forced in full generality

That makes this a review-tier answer to the “just Poisson dressed up” critique,
but not yet a `main`-ready uniqueness claim.
