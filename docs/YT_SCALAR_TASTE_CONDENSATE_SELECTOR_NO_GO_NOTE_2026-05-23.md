# Y_T Scalar/Taste-Condensate Selector No-Go

**Date:** 2026-05-23
**Claim type:** no_go
**Primary runner:** `scripts/frontier_yt_scalar_taste_condensate_selector_no_go.py`

## Claim Boundary

This note attacks the proposed positive bridge left open by
[`YT_COLOR_PROJECTION_CORRECTION_NOTE.md`](YT_COLOR_PROJECTION_CORRECTION_NOTE.md):

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

[`YT_COLOR_PROJECTION_CORRECTION_NOTE.md`](YT_COLOR_PROJECTION_CORRECTION_NOTE.md)
correctly repairs the old
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

None of those escape routes is present in the current repaired Y_T color
packet.

## No-Go Discipline Gate (review-loop 2026-05-23)

Status: **PASS for the route-specific no-go only**. This checklist does not
claim global Y_T impossibility.

### N1 - Alternative route enumeration

| Route | What it would attempt | Why it fails or remains outside this no-go | Marker |
| --- | --- | --- | --- |
| Direct color-singlet projection | Feed the one-Higgs scalar/taste color insertion into the Hilbert-Schmidt color projection. | The insertion is proportional to `I_color`, so the runner computes singlet weight `1`, not `0`. | ATTEMPTED |
| Connected/VEV subtraction | Argue that `phi - <phi>` makes the source connected and therefore traceless. | The subtraction changes a c-number source value, not the color matrix in `bar q_a q^a`; the runner checks that the derivative insertion remains `I_color`. | ATTEMPTED |
| Color-adjoint scalar insertion | Replace the scalar insertion by a nonzero traceless color matrix. | This can give singlet weight `0`, but it is no longer the one-Higgs color-singlet top-Yukawa operator attacked here. | ATTEMPTED |
| Taste-sector selector | Let taste structure supply the missing `kappa_Y = 0` selection while color remains singlet. | Taste structure alone does not change the color insertion; a separate matching theorem would be needed and is not present in this route. | ATTEMPTED |
| Alternative `kappa_Y` matching theorem | Define `kappa_Y` by something other than color-insertion singlet weight. | This is explicitly left open; it would be a different theorem, not a rescue of the direct scalar/taste-condensate projection route. | ATTEMPTED |
| Direct top-correlator measurement | Bypass scalar/taste projection and infer `m_t -> y_t` directly from an observable. | This is outside the scalar/taste selector route and remains an open positive path, so it is not claimed closed by this no-go. | ATTEMPTED |

### N2 - Wall-independence audit

Collapsed wall set:

| Wall | Description | Independent role |
| --- | --- | --- |
| W1 | One-Higgs color-singlet invariance forces `M_color = c I_color`. | Supplies the identity-channel conclusion. |
| W2 | The diagnostic `kappa_Y = 0` projection would require a nonzero traceless color insertion. | Supplies the target-channel requirement. |
| W3 | VEV/connected subtraction does not alter the color insertion. | Blocks the common attempted escape. |

W1 and W2 together form the contradiction for the direct route: nonzero
identity and nonzero traceless are incompatible. W3 does not follow from W1
or W2; it is an escape guard, not an additional independent theorem wall.

### N3 - Hidden-wall scan

Checked phrases: "standard one-Higgs", "framework-native", "physical",
"current repaired Y_T color packet", and "connected fluctuation".
"Standard one-Higgs" is the explicit route boundary, not an unlabelled import.
"Framework-native" and "physical" are used only to identify the intended
top-Yukawa route and are not load-bearing evidence. "Connected fluctuation"
is promoted into the explicit W3 guard above.

### N4 - Residual matching

| Witness | Residual attacked | Residual claimed here | Match? |
| --- | --- | --- | --- |
| [`YT_COLOR_PROJECTION_CORRECTION_NOTE.md`](YT_COLOR_PROJECTION_CORRECTION_NOTE.md) | Old direct jump from the color projection family to `kappa_Y = 0`. | Whether the scalar/taste-condensate route supplies `kappa_Y = 0`. | Yes; this note tests the named follow-up route. |

No other prior no-go is used as a witness.

### N5 - Rhetoric audit

The negative claim is stated at the local color-insertion/operator level:
`one-Higgs color-singlet scalar/taste insertion -> no derivation of
kappa_Y = 0`. It is not stated as a per-site, per-mode, per-family,
lattice-wide, or global BSM no-go. The untested broader resolutions are
excluded in "Out Of Scope" and in N1.

### N6 - Partial-closure path scan

No new axiom is requested. Two non-axiom partial-closure paths remain open:
a retained matching theorem for `kappa_Y` that is not the color-insertion
singlet weight, and a direct observable top-correlator route. Either path
could close positive Y_T later without contradicting this route-specific
negative result.

### N7 - Steelman

A hostile reviewer could argue that the connected scalar/taste fluctuation is
not merely a source subtraction: after full lattice renormalization, a Ward or
matching theorem might map the connected scalar response to the traceless
color channel even though the bare one-Higgs vertex is color singlet. That
would be a real positive route if proved. This note does not exclude that
future theorem; it only says the direct scalar/taste color-insertion
projection has not supplied it.

### N8 - Cross-cycle echo

The closest prior wall is the color-projection correction itself in
[`YT_COLOR_PROJECTION_CORRECTION_NOTE.md`](YT_COLOR_PROJECTION_CORRECTION_NOTE.md):
definition-by-specialization was replaced by the family
`K_Y(kappa_Y) = 8/9 + kappa_Y/9`, leaving `kappa_Y = 0` as a separate target.
That wall was not retired by vocabulary or convention; it was narrowed into a
real matching-theorem gap. The same mechanism applies here: preserve the
narrow negative route result while leaving matching-theorem and direct
observable routes open.

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
