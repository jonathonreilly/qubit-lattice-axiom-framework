# Conditional Weak-Field Gravity IF-Chain on `Z^3`

**Date:** 2026-04-13. Scope repair: 2026-05-27. Green-kernel dependency
repair: 2026-06-09. Parent composition certificate: 2026-06-11.
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.
**Primary runner:** [`scripts/frontier_gravity_clean_weak_field_composition_certificate_2026_06_11.py`](../scripts/frontier_gravity_clean_weak_field_composition_certificate_2026_06_11.py)
with cached output
[`logs/runner-cache/frontier_gravity_clean_weak_field_composition_certificate_2026_06_11.txt`](../logs/runner-cache/frontier_gravity_clean_weak_field_composition_certificate_2026_06_11.txt).
The binding claim is the bounded implication below, with the cited one-hop
authorities supplying the premises at their own audited scopes.

## 2026-06-11 Weak-Field Bridge Repair

The previously open bridge inputs

```text
L^{-1} = G_0,
rho = |psi|^2,
S = L(1 - phi)
```

are now routed through
[`GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md`](GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md).
That bridge is a bounded weak-field variational theorem: it proves the
Euler equation of the source action, the uniqueness of the local
phase-invariant normalized source readout, and the first-order test-source
action response. It does not claim nonlinear gravity, physical `G_Newton`, or
any audit outcome.

## 2026-06-11 Parent Composition Certificate

The parent row now has a source-side certificate runner,
[`frontier_gravity_clean_weak_field_composition_certificate_2026_06_11.py`](../scripts/frontier_gravity_clean_weak_field_composition_certificate_2026_06_11.py).
It does not apply an audit verdict. It checks that this parent note routes all
three formerly row-local bridge inputs through the weak-field bridge, that the
bridge cache is SHA-pinned and passing, that the one-hop dependency links are
present, that the bounded weak-field status firewall remains explicit, and that
the composed `G(r) ~ 1/(4 pi r)` plus `S = L(1 - phi)` response gives a
bilinear inverse-square force in lattice units.

## Binding Claim

This note is a bounded weak-field gravity chain. It does **not**
derive Newton gravity from the one-qubit operator algebra on the `Z^3`
Lattice alone, and it does not claim a zero-free-parameter
physical-gravity closure.

The binding claim is:

> Given the following retained or source-side bridge inputs:
>
> 1. the `Z^3` staggered/scalar sector supplies the graph Laplacian
>    `-Delta_lat`;
> 2. the weak-field source-response bridge supplies `L^{-1} = G_0` on the
>    neutral response sector;
> 3. the same bridge supplies the local source readout `rho = |psi|^2`
>    (with zero-mode subtraction on finite tori);
> 4. the same bridge supplies the first-order test-mass response
>    `S = L(1 - phi)`;
> 5. the framework-local `Z^3` graph-Laplacian Green theorem supplies the
>    large-distance normalization `G(r) ~ 1/(4 pi r)`;
>
> then the lattice Poisson equation gives a `1/r` potential and an
> inverse-square force in lattice units.

The conclusion is therefore a bounded weak-field composition over named
one-hop inputs, not a nonlinear or SI-unit physical-gravity closure.

## One-Hop Inputs

The internal premises are made explicit through citation-graph dependencies:

- [`GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md`](GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md)
  supplies the weak-field variational bridge for `L^{-1}=G_0`, the local
  Born-density source readout `rho=|psi|^2`, and the first-order test-source
  response `S=L(1-phi)`.
- [`SELF_CONSISTENCY_FORCES_POISSON_NOTE.md`](SELF_CONSISTENCY_FORCES_POISSON_NOTE.md)
  supplies bounded finite/operator-family diagnostics for the route from
  self-consistency to the Poisson operator.
- [`POISSON_EXHAUSTIVE_UNIQUENESS_NOTE.md`](POISSON_EXHAUSTIVE_UNIQUENESS_NOTE.md)
  supplies bounded uniqueness diagnostics for the tested operator family.
- [`GRAVITY_FULL_SELF_CONSISTENCY_NOTE.md`](GRAVITY_FULL_SELF_CONSISTENCY_NOTE.md)
  states the broader self-consistency surface. The weak-field bridge above
  replaces the old row-local stipulation of `L^{-1} = G_0` for the linearized
  response sector.
- [`STAGGERED_FERMION_CARD_2026-04-11.md`](STAGGERED_FERMION_CARD_2026-04-11.md)
  supplies bounded fixed-run support for the staggered/Born-density side of
  the chain, within that card's own scoped finite-run limits.
- [`LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md`](LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md)
  supplies the framework-applied `Z^3` nearest-neighbor graph-Laplacian
  normalization `G(r) -> 1/(4 pi |r|)`, with Maradudin/Lawler/Spitzer kept as
  parallel references rather than load-bearing textbook authority.
- [`LATTICE_GREENS_MARADUDIN_ASYMPTOTIC_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md`](LATTICE_GREENS_MARADUDIN_ASYMPTOTIC_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md)
  records the legacy bridge row rerouted through that framework-local theorem.

These authorities are sufficient only for the bounded weak-field chain stated
here. They do not derive a nonlinear gravitational action or physical
`G_Newton` in SI units.

## Framework-Local Green-Kernel Input

The large-distance Green-function normalization is no longer treated here as
an imported textbook theorem. It is the framework-local nearest-neighbor
`Z^3` graph-Laplacian theorem applied to the exact stencil:

```text
G(r) = <r|(-Delta_lat)^(-1)|0> = 1/(4 pi |r|) + O(|r|^{-3})
```

for `|r| >> 1` on `Z^3`, modulo the usual lattice anisotropy corrections.
The standard Maradudin/Lawler/Spitzer references remain useful parallel
provenance for the same lattice-potential theorem, but this note's
load-bearing dependency is the repository's framework-applied Green-kernel
certificate. It is not a new framework axiom and is not a physical gravity
bridge.

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

5. With a second test mass read through the weak-field response bridge
   `S = L(1 - phi)`, the force on mass parameter `M_2` in the field sourced
   by `M_1` is bilinear:

   ```text
   |F_12| proportional to M_1 M_2 / r^2.
   ```

The product structure follows from Poisson linearity plus the variational
test-source response. The exponent follows from `d = 3` in the `Z^3`
Green-function asymptotic.

## Superseded Framing

Earlier text in this note described the result as a complete clean derivation
from the framework baseline with zero free parameters. That framing is
superseded by this 2026-05-27 repair.

The current binding statement is only the bounded conditional theorem above.
In particular:

- `L^{-1} = G_0` is supplied only at weak-field linearized order by the
  source-response bridge, not as a nonlinear self-gravity closure.
- `rho = |psi|^2` is supplied only as the unique local normalized
  phase-invariant source density on the amplitude carrier; total mass scale and
  SI units are not fixed here.
- `S = L(1 - phi)` is supplied only as a first-order test-source response, not
  as a full geodesic/action theorem.
- `G(r) ~ 1/(4 pi r)` is supplied by the framework-local `Z^3` graph-Laplacian
  Green theorem, not by importing textbook authority as a physical bridge.

## What This Note Does Not Claim

- No unconditional derivation of Newton gravity from the framework baseline.
- No clean-chain or zero-free-parameter physical-gravity closure.
- No derivation of physical `G_Newton` in SI units.
- No derivation of the full Einstein equations.
- No strong-field, horizon, frame-dragging, gravitational-wave, WEP,
  geodesic, or light-bending theorem.
- No audit verdict; the primary runner is only a source-side composition
  certificate for this bounded weak-field parent row.

## What Would Close The Stronger Lane

To promote beyond this bounded weak-field chain, future work would need:

1. independent audit of the weak-field source-response bridge added above;
2. a nonlinear self-gravity/Einstein-equation route that survives the retained
   no-go boundary;
3. composition of the already framework-local `Z^3` Green-function normalization
   with the exact framework source/readout normalization in the parent chain;
4. conversion of lattice units to physical `G_Newton` without importing a fitted
   calibration.

Until then, this row should be read only as a bounded weak-field implication in
lattice units.
