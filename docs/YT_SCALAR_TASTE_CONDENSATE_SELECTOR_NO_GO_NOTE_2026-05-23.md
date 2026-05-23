# Y_T Scalar/Taste-Condensate Selector No-Go

**Date:** 2026-05-23
**Claim type:** no_go
**Primary runner:** `scripts/frontier_yt_scalar_taste_condensate_selector_no_go.py`

## Claim Boundary

This note attacks the proposed positive bridge left open by
`YT_COLOR_PROJECTION_CORRECTION_NOTE.md`:

```text
derive kappa_Y = 0 from the scalar/taste-condensate Yukawa operator.
```

The result is negative for the standard one-Higgs, color-singlet
scalar/taste-condensate route.

> A nonzero color-singlet Higgs or scalar/taste-condensate Yukawa insertion
> has color matrix proportional to `I_color`. Under the finite-dimensional
> Hilbert-Schmidt color projection, this insertion has singlet weight `1`,
> not `0`. The connected-trace specialization `kappa_Y = 0` would require a
> nonzero traceless color insertion. Therefore the scalar/taste-condensate
> route cannot derive `kappa_Y = 0` unless it first replaces the physical
> color-singlet Higgs insertion by a nonzero color-adjoint/traceless scalar
> insertion, which is outside the one-Higgs top-Yukawa operator.

This is not a global impossibility theorem for every imaginable BSM scalar.
It is the route-specific no-go for the framework-native one-Higgs /
scalar-taste-condensate bridge that was supposed to close the Y_T color
selector.

## Algebraic Setup

Let the quark color space be `V_color = C^N`, `N >= 2`. A local Yukawa
color insertion is a matrix `M_color in End(V_color)` in the color contraction

```text
bar q_a (M_color)^a_b q^b.
```

For a color-singlet scalar, gauge invariance under `SU(N)` requires

```text
U^\dagger M_color U = M_color        for all U in SU(N).
```

By Schur's lemma for the irreducible fundamental representation, or by the
elementary torus-plus-permutation proof checked by the runner, every such
matrix is proportional to the identity:

```text
M_color = c I_color.
```

If `M_color` is also traceless, then

```text
0 = Tr_color M_color = c N,
```

so `c = 0`. Thus there is no nonzero color-singlet Yukawa insertion that is
also traceless.

## Projection Consequence

The Hilbert-Schmidt singlet fraction of a nonzero Hermitian color insertion
is

```text
rho_singlet(M_color)
  = ( |Tr_color M_color|^2 / N ) / Tr_color(M_color^2).
```

For `M_color = c I_color`, `c != 0`,

```text
rho_singlet(c I_color) = 1.
```

For any nonzero traceless generator insertion,

```text
rho_singlet(t^A) = 0.
```

Therefore, if a future matching theorem identifies the Yukawa readout
coefficient with this color-insertion singlet weight,

```text
kappa_Y = rho_singlet(M_color),
```

then the one-Higgs scalar/taste-condensate insertion gives

```text
kappa_Y = 1,
K_Y = 8/9 + 1/9 = 1,
```

not the package specialization

```text
kappa_Y = 0,
K_Y = 8/9.
```

This note does **not** assert that `kappa_Y = rho_singlet(M_color)` is already
an accepted matching rule. It uses that identification only as a diagnostic:
even the most direct projection reading of the scalar/taste route points to
the identity-channel completion, not to the connected-trace specialization.

## Why VEV Subtraction Does Not Fix This

The physical Higgs fluctuation is often written as a shifted scalar,

```text
phi(x) - <phi>.
```

That subtraction removes a c-number expectation value. It does not change the
color matrix through which the scalar couples to the quark bilinear. The
functional derivative of a color-singlet source coupled to

```text
bar q_a q^a
```

still inserts `I_color`. It does not insert a traceless generator.

So the route cannot obtain `kappa_Y = 0` by saying "use the connected
fluctuation" unless it supplies a separate theorem proving that the connected
fluctuation changes the color insertion from `I_color` to a nonzero traceless
matrix. The current scalar/taste-condensate route supplies no such theorem.

## Relation To Existing Y_T Color Work

`YT_COLOR_PROJECTION_CORRECTION_NOTE.md` correctly repairs the old
`sqrt(8/9)` claim into the conditional family

```text
K_Y(kappa_Y) = 8/9 + kappa_Y/9.
```

This note tests the most obvious positive bridge for selecting
`kappa_Y = 0`: identify the physical scalar/taste-condensate color insertion
and feed it into the projection. That bridge fails on the standard
one-Higgs route because the insertion is color identity.

Safe conclusion:

```text
scalar/taste-condensate one-Higgs route -> no derivation of kappa_Y = 0.
```

Unsafe conclusion:

```text
kappa_Y = 0 is derived because the physical Higgs is a connected scalar
fluctuation.
```

The latter silently changes "connected fluctuation" into "traceless color
insertion"; those are different statements.

## What Would Be Needed To Escape This No-Go

Any positive escape must prove at least one of the following:

1. the top-Yukawa scalar is not the color-singlet one-Higgs/taste-condensate
   insertion but a nonzero traceless color insertion;
2. the readout coefficient `kappa_Y` is not the color-insertion singlet
   weight, and a different retained matching theorem selects `kappa_Y = 0`;
3. the connected scalar fluctuation changes the color insertion itself from
   `I_color` to a traceless matrix without violating `SU(3)` color gauge
   invariance.

None of those escape routes is present in the current retained/repaired Y_T
color packet.

## Status

```yaml
actual_current_surface_status: no-go
conditional_surface_status: |
  conditional obstruction for the one-Higgs scalar/taste-condensate route;
  not a global no-go for all possible non-SM color-adjoint scalar theories.
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: |
  The block rules out the direct scalar/taste selector route for kappa_Y=0.
  It does not close positive Y_T.
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Out Of Scope

This note does not derive:

- `kappa_Y = 0`;
- `sqrt(8/9)` as a physical Y_T correction;
- the Ward identity route;
- a direct top correlator mass measurement;
- the Higgs VEV;
- any PDG comparator.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_yt_scalar_taste_condensate_selector_no_go.py
```

The runner checks the finite-dimensional color algebra, the identity versus
traceless projection weights, the color-singlet uniqueness argument, VEV
subtraction guardrails, and source overclaim boundaries.
