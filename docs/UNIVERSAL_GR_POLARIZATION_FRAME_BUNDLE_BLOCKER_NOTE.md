# Universal GR Polarization-Frame Bundle Blocker Note

**Status:** bounded - bounded or caveated result note
**Date:** 2026-04-14  
**Branch:** `codex/review-active`  
**Role:** direct universal route / blocker note  
**Purpose:** isolate the smallest missing primitive on the straight-to-full-GR
**Primary runner:** [`scripts/frontier_universal_gr_polarization_frame_bundle.py`](../scripts/frontier_universal_gr_polarization_frame_bundle.py) (current default `PASS=13 FAIL=0`)
path after the exact scalar observable generator, exact `3+1` lift, exact
tensor-valued variational candidate, and unique symmetric quotient kernel are
already in hand

## Audit-scope repair (2026-06-18)

The auditable claim in this row is the **finite prototype frame-orbit support
result**:

- the displayed symmetric `3+1` quotient prototype has a nondegenerate Hessian
  Gram matrix;
- its scalar-channel/lapse-plus-trace projector is invariant on the sampled
  valid polarization frames;
- complementary localization coefficients move under a valid spatial-frame
  rotation;
- therefore this packet does not construct a canonical full
  polarization-frame/projector bundle or curvature-localization operator
  `Pi_curv`.

This row is **not** an exhaustive theorem that no alternative covariant bundle,
connection, horizontal distribution, curvature-localization map, or future
extension of the current stack can ever construct `Pi_curv`. It also does not
identify the Hessian with Einstein/Regge dynamics. Any downstream claim needing
that stronger conclusion must provide a separate N1-N8-complete route
exhaustion or a positive covariant bundle construction.

## Verdict

This packet records a sharp finite support obstruction for the direct
universal route. It shows that the supplied prototype data do not by
themselves select a canonical full polarization frame.

The current axiom-first stack gives:

- an exact scalar observable generator from the observable principle
- an exact `3+1` kinematic lift on `PL S^3 x R`
- an exact tensor-valued variational candidate on that lifted background
- an exact unique symmetric `3+1` quotient kernel on the finite prototype

This packet does **not** construct:

- a covariant `3+1` polarization-frame / projector bundle that canonically
  splits the symmetric Hessian kernel into lapse, shift, and spatial
  trace/shear channels before localization
- an exact curvature-localization operator `Pi_curv` derivable from the
  current stack alone

So the remaining gap exposed by this packet is not a scalar,
quotient-uniqueness, or generic action calculation inside the displayed
prototype. It is the missing covariant frame / projector bundle itself.

The current runner compares two valid `3+1` polarization frames for the same
prototype quotient kernel. The localized channel coefficients move under frame
rotation, so the displayed packet does not canonically fix the
lapse/shift/shear splitting.

The strongest exact object available here is the associated orbit of localized
channels over the sampled valid `3+1` polarization frames. That orbit is exact
for the finite prototype, but this packet does not supply a distinguished
connection or horizontal distribution that picks a canonical section.

## What is exact already

### Scalar generator

The axiom-side observable principle gives the scalar generator

`W[J] = log|det(D+J)| - log|det D|`

This is exact, but scalar.

### `3+1` lift

Route 2 gives the exact kinematic background

`PL S^3 x R`.

That is exact on the current atlas, but kinematic only.

### Tensor variational candidate

The scalar generator can be lifted into a tensor-valued quadratic form by
taking its metric-source Hessian on the lifted background:

`S_GR^cand[h] := 1/2 * D^2 W[g_*](h, h)`.

This is the exact tensor-valued variational candidate, but it is still only a
variational object until a curvature-localization map is supplied.

### Quotient uniqueness

On the symmetric `3+1` perturbation quotient, the Hessian kernel is the
unique bilinear lift of the scalar generator at quadratic order. On the finite
prototype used by the current runner, that quotient kernel is nondegenerate.

That proves uniqueness of the tensor candidate on the quotient. It does not
identify the kernel with Einstein/Regge curvature dynamics.

### Exact invariant section

The strongest exact projector latent in the current construction is the
rank-2 `A1` projector onto lapse and spatial trace:

`Pi_A1 = diag(1,0,0,0,1,0,0,0,0,0)`.

This is the exact minimal-covariance selector already visible in the current
universal stack. It is frame-independent across the sampled valid `3+1`
frames, but it only fixes the invariant `A1` block; the complement remains
frame-dependent.

## Why the current stack stops here

The present finite packet determines a unique bilinear kernel on the symmetric
quotient, and it also determines the exact `A1` invariant projector, but it
does not specify how to localize the complementary `E \oplus T1` channels into
curvature channels on `PL S^3 x R`.

In particular, the current stack has no exact object that:

1. is tensor-valued and covariant on the `3+1` quotient;
2. splits the Hessian kernel into lapse, shift, and spatial trace/shear
   components;
3. identifies those components with the Einstein/Regge tensor law.

Without that object, the Hessian remains a variational candidate in this
packet, not a GR dynamics law. The exact `A1` projector is the strongest
selector displayed here, but it is not the canonical localization bundle.

## Minimal missing primitive

The smallest honest missing object is now:

> a covariant `3+1` polarization-frame / projector bundle, equipped with a
> distinguished connection, that extends the exact rank-2 `A1` projector on
> lapse and spatial trace to the complementary `E \oplus T1` channels and
> splits the unique symmetric Hessian kernel into lapse, shift, and spatial
> trace/shear channels before localization.

Equivalently, the missing primitive is still a covariant `3+1`
curvature-localization operator `Pi_curv`. This packet demonstrates only that
the finite quotient/frame data supplied here determine a frame-orbit family of
candidate localizations rather than a canonical projector bundle.

## Honest status

The current direct universal route is:

- exact at the scalar observable level
- exact at the `3+1` kinematic lift level
- exact at the symmetric `3+1` quotient-kernel level
- blocked at the curvature-localization level

That is the sharpest disciplined statement this packet supports. Stronger
downstream use as a global no-go for all covariant `Pi_curv` constructions, or
as a positive Einstein/Regge dynamics theorem, is outside this row.
