# DM Leptogenesis Conditional Flavor-Column Functional Identity

**Status:** conditional / support
**Date:** 2026-04-16; scope narrowed 2026-07-16
**Branch:** `codex/science-fix-dm-leptogenesis-flavor-column-functional-20260716`
**Script:** `scripts/frontier_dm_leptogenesis_flavor_column_functional_theorem.py`
**Framework convention:** "axiom" means only `Cl(3)` on `Z^3`

## Claim

This note records a supplied-premise integrating-factor identity. It does not derive a leptogenesis transport model from the framework.

Assume all of the following data are supplied:

1. a finite interval `[z_0, Z]`;
2. integrable real profiles `S(z)` and `W(z)`;
3. a supplied projector column
   `P = (P_e, P_mu, P_tau)` with `0 <= P_alpha <= 1`;
4. the decoupled initial-value equations

   `dY_alpha/dz = P_alpha S(z) - P_alpha W(z) Y_alpha`,

   with `Y_alpha(z_0) = 0`.

Then the integrating-factor solution is

`Y_alpha(Z) = Psi_[z_0,Z](P_alpha)`,

where

`Psi_[z_0,Z](q) = q integral_[z_0,Z] S(z)
exp(-q integral_[z,Z] W(t) dt) dz`.

Therefore the supplied finite-interval total is the column functional

`F_[z_0,Z](P) = sum_alpha Psi_[z_0,Z](P_alpha)`.

This implication is exact mathematics conditional on the four premises above.
It does not select or justify those premises.

## Proof

For fixed `alpha`, multiply the supplied equation by

`exp(P_alpha integral_[z_0,z] W(t) dt)`.

The left-hand side becomes the derivative of the product of this integrating
factor with `Y_alpha(z)`. Integrating from `z_0` to `Z` and using
`Y_alpha(z_0) = 0` gives

`Y_alpha(Z) =
 P_alpha integral_[z_0,Z] S(z)
 exp(-P_alpha integral_[z,Z] W(t) dt) dz`.

Summing the three independently supplied flavor equations gives the displayed
column functional. No transport provenance, profile-selection rule, packet
selection, or physical readout map enters this algebraic step.

## What the runner actually computes

The runner instantiates the identity on a finite numerical fixture:

- `z in [10^-3, 35]`;
- a `20,000`-point grid;
- a BDF occupancy solve from `scripts/dm_leptogenesis_exact_common.py`;
- a source profile obtained from the numerical occupancy grid;
- a trapezoidal washout tail and trapezoidal final integral;
- a canonical `N_e` packet obtained from supplied coordinates
  `(x, y, delta)` and a finite Hermitian eigensolve.

Those objects are supplied computational fixtures. The runner does not derive
the one-source flavored transport equations, the source or washout profiles,
their boundary conditions, the numerical constants used by the helper, or the
canonical packet from `Cl(3)` on `Z^3`.

The runner independently checks the functional against:

- closed-form constant-profile solutions;
- a separate ODE solve for a non-constant synthetic profile;
- the helper's direct flavored-transport solve on boundary, democratic,
  small-leakage, canonical, and deterministic random simplex columns;
- a second kernel recomputation using a different grid and the differential
  equation's source term rather than the primary numerical gradient.

## Finite canonical-packet result

For the supplied canonical `N_e` active block, the computed packet is

`[[0.915868, 0.071267, 0.012865],
  [0.074689, 0.900307, 0.025004],
  [0.009443, 0.028427, 0.962131]]`.

On the named finite kernel, both the scalar functional and the independent
direct ODE computation order the three columns with column index `1` first.

This is a finite supplied-packet ordering. It is not a derivation of a
canonical physical packet, a physical yield, or a leptogenesis readout.

## Channel-peak boundary

The old runner used a `1001`-point `q` grid to call the channel maximum unique.
That was not a uniqueness proof.

The repaired runner does only a narrower analytic local-isolation check for its
finite trapezoidal kernel. Writing that kernel as

`Psi_h(q) = q sum_j a_j exp(-q T_j)`,

with non-negative trapezoid weights `a_j`, it evaluates the analytic
derivative and brackets one local stationary point in
`[0.03549, 0.03550]`. On that bracket, `q T_j < 2` for every grid point, so
every analytic second-derivative term is non-positive and their sum is
strictly negative.

No global uniqueness claim is made on `[0,1]`, and no continuum uniqueness
claim is made for an underlying profile. Establishing either would require a
separate analytic or interval-certified theorem.

## Exact scope boundary

This note closes only:

- the integrating-factor identity conditional on supplied equations, profiles,
  interval, boundary data, and column;
- numerical agreement of two implementations on the named finite fixtures;
- middle-column ordering for the one supplied canonical packet and computed
  finite kernel;
- one locally isolated stationary point of the finite trapezoidal channel
  function.

This note does not close:

- an axiom-native flavored transport equation;
- an axiom-native source or washout profile;
- a physical yield/readout map;
- a canonical packet-selection theorem;
- global or continuum uniqueness of the channel maximum;
- physical leptogenesis closure.

The remaining repair class is therefore still
`missing_bridge_theorem`: derive retained one-hop authorities for the transport
law, profiles and boundary data, canonical packet, and physical readout map.
If global channel uniqueness remains scientifically load-bearing, add a
separate analytic or rigorous interval certificate for the intended continuum
object.

## Command

```bash
python3 scripts/frontier_dm_leptogenesis_flavor_column_functional_theorem.py
```
