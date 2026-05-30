# Conditional Weak-Field Gravity IF-Chain on `Z^3`

**Date:** 2026-04-13. Scope repair: 2026-05-27.
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.
**Primary runner:** none registered for this row. The binding claim is the
bounded implication below, with the cited one-hop authorities supplying the
premises at their own audited scopes.

## Binding Claim

This note is a bounded conditional weak-field gravity chain. It does **not**
derive Newton gravity from the one-qubit operator algebra on the `Z^3`
spatial substrate alone, and it does not claim a zero-free-parameter
physical-gravity closure.

The binding claim is:

> If the framework supplies the following inputs:
>
> 1. the `Z^3` staggered/scalar sector supplies the graph Laplacian
>    `-Delta_lat`;
> 2. the field operator and propagator Green function are related by the
>    stipulated weak-field closure `L^{-1} = G_0`;
> 3. the source density entering the field equation is the Born/mass-density
>    readout `rho = |psi|^2`;
> 4. the weak-field test-mass response is read through `S = L(1 - phi)`;
> 5. the `Z^3` lattice Green function has the standard large-distance
>    normalization `G(r) ~ 1/(4 pi r)`;
>
> then the lattice Poisson equation gives a `1/r` potential and an
> inverse-square force in lattice units.

The conclusion is therefore an implication over named inputs, not an
unconditional derivation of those inputs.

## One-Hop Inputs

The internal premises are made explicit through citation-graph dependencies:

- [`SELF_CONSISTENCY_FORCES_POISSON_NOTE.md`](SELF_CONSISTENCY_FORCES_POISSON_NOTE.md)
  supplies bounded finite/operator-family diagnostics for the route from
  self-consistency to the Poisson operator.
- [`POISSON_EXHAUSTIVE_UNIQUENESS_NOTE.md`](POISSON_EXHAUSTIVE_UNIQUENESS_NOTE.md)
  supplies bounded uniqueness diagnostics for the tested operator family.
- [`GRAVITY_FULL_SELF_CONSISTENCY_NOTE.md`](GRAVITY_FULL_SELF_CONSISTENCY_NOTE.md)
  states the broader self-consistency surface and records `L^{-1} = G_0` as
  a stipulated closure identity, not a theorem derived from the framework
  baseline alone.
- [`STAGGERED_FERMION_CARD_2026-04-11.md`](STAGGERED_FERMION_CARD_2026-04-11.md)
  supplies bounded fixed-run support for the staggered/Born-density side of
  the chain, within that card's own scoped finite-run limits.

These authorities are sufficient only for the bounded IF-chain stated here.
They do not derive a physical mass-source law, a full gravitational action,
or physical `G_Newton` in SI units.

## External Mathematical Input

The large-distance Green-function normalization is standard lattice
potential theory:

```text
G(r) = <r|(-Delta_lat)^(-1)|0> = 1/(4 pi |r|) + O(|r|^{-3})
```

for `|r| >> 1` on `Z^3`, modulo the usual lattice anisotropy corrections.
This note uses that result as mathematical background in parallel with the
framework calculation. It is not a new framework axiom and is not a physical
gravity bridge.

## Conditional Chain

Under the inputs above:

1. The scalar lattice field equation is the Poisson form

   ```text
   (-Delta_lat) phi = rho.
   ```

2. For a localized source of mass parameter `M`,

   ```text
   phi(r) = M G(r).
   ```

3. By the `Z^3` Green-function asymptotic,

   ```text
   phi(r) ~ M / (4 pi r)
   ```

   in lattice units at large distance.

4. Taking the radial gradient gives an inverse-square force law:

   ```text
   |F(r)| proportional to M / r^2.
   ```

5. With a second test mass read through the assumed weak-field response
   `S = L(1 - phi)`, the force on mass parameter `M_2` in the field sourced
   by `M_1` is bilinear:

   ```text
   |F_12| proportional to M_1 M_2 / r^2.
   ```

The product structure follows from Poisson linearity plus the assumed
test-mass response. The exponent follows from `d = 3` in the `Z^3`
Green-function asymptotic.

## Superseded Framing

Earlier text in this note described the result as a complete clean derivation
from the framework baseline with zero free parameters. That framing is
superseded by this 2026-05-27 repair.

The current binding statement is only the bounded conditional theorem above.
In particular:

- `L^{-1} = G_0` is an input closure identity, not derived here from pure
  algebra or from the framework baseline alone.
- `rho = |psi|^2` as gravitational mass density is an input readout, not
  derived here as a physical source law.
- `S = L(1 - phi)` is an input weak-field response, not derived here as a
  full test-mass action theorem.
- `G(r) ~ 1/(4 pi r)` is used as a standard mathematical theorem about the
  `Z^3` Laplacian Green function, not as a physical bridge.

## What This Note Does Not Claim

- No unconditional derivation of Newton gravity from the framework baseline.
- No clean-chain or zero-free-parameter physical-gravity closure.
- No derivation of physical `G_Newton` in SI units.
- No derivation of the full Einstein equations.
- No strong-field, horizon, frame-dragging, gravitational-wave, WEP,
  geodesic, or light-bending theorem.
- No registered primary runner for this row.

## What Would Close The Stronger Lane

To promote beyond this bounded IF-chain, future work would need retained
bridge theorems for:

1. deriving `L^{-1} = G_0` rather than stipulating it as a weak-field closure
   identity;
2. deriving the physical gravitational source map `rho = |psi|^2`;
3. deriving the weak-field test-mass response `S = L(1 - phi)`;
4. applying or deriving the `Z^3` Green-function normalization with the exact
   framework source/readout normalization;
5. converting lattice units to physical `G_Newton` without importing a fitted
   calibration.

Until then, this row should be read only as a bounded conditional
weak-field implication.
