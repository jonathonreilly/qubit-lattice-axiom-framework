# Universal GR Polarization-Frame Finite Orbit Support Note

**Status:** bounded-support source note; effective status is set only by
independent audit
**Date:** 2026-04-14  
**Branch:** `codex/review-active`  
**Role:** direct universal route / finite frame-orbit support note
**Purpose:** record the exact finite prototype support result behind the
polarization-frame obstruction without claiming an exhaustive no-go against all
possible curvature-localization constructions.
**Primary runner:** [`scripts/frontier_universal_gr_polarization_frame_bundle.py`](../scripts/frontier_universal_gr_polarization_frame_bundle.py) (PASS=14/0)

## Source Inputs

The verifier consumes these source-side authorities:

- [`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`](OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md)
  for the scalar observable generator.
- [`S3_ANOMALY_SPACETIME_LIFT_NOTE.md`](S3_ANOMALY_SPACETIME_LIFT_NOTE.md)
  for the `PL S^3 x R` lift.
- [`UNIVERSAL_GR_TENSOR_VARIATIONAL_CANDIDATE_NOTE.md`](UNIVERSAL_GR_TENSOR_VARIATIONAL_CANDIDATE_NOTE.md)
  for the tensor-valued Hessian candidate.
- [`UNIVERSAL_GR_TENSOR_QUOTIENT_UNIQUENESS_NOTE.md`](UNIVERSAL_GR_TENSOR_QUOTIENT_UNIQUENESS_NOTE.md)
  for the unique symmetric quotient-kernel packet.
The verifier also reads `UNIVERSAL_GR_TENSOR_ACTION_BLOCKER_NOTE.md`,
`UNIVERSAL_GR_CURVATURE_LOCALIZATION_BLOCKER_NOTE.md`, and
`UNIVERSAL_GR_POLARIZATION_FRAME_BUNDLE_ATTEMPT.md` as guardrail text; they
are named here as plain text, not markdown dependency edges.

## 2026-06-18 scope repair

A prior source framing made this row read like an exhaustive theorem that the
current axiom stack cannot derive any covariant curvature-localization
operator `Pi_curv`. That was too broad. The runner proves a narrower and
useful finite statement:

- the scalar observable generator and `3+1` lift feed a finite symmetric
  Hessian prototype;
- the symmetric quotient Gram matrix is nondegenerate on the 10-dimensional
  prototype;
- the scalar-line restriction matches the same Hessian;
- the rank-2 scalar-channel projector on lapse and spatial trace is stable;
- the complement-channel localization coefficients move under a valid spatial
  frame rotation, with `frame_delta = 6.767360754447e-02`.

This is finite frame-orbit support for the polarization-frame bundle gap. It
is not an exhaustive no-go against every possible covariant projector bundle,
connection, horizontal distribution, or alternative construction of
`Pi_curv`. Downstream rows may cite this note as an exact finite orbit
diagnostic and scalar-channel support packet, not as full GR closure.

No audit verdict, ledger status, publication status, or repo-wide authority
surface is changed by this source-side repair.

## Verdict

This note now claims the exact finite frame-orbit support result, not a
universal impossibility theorem.

## 2026-06-18 source-side route-exhaustion repair pointer

The source-side repair packet
`UNIVERSAL_GR_PICURV_ROUTE_EXHAUSTION_NO_GO_NOTE_2026-06-18.md` adds the
route-exhaustion gate that this older packet did not contain. It
does not change audit status, does not retag this row, and does not claim a
framework-level GR closure. Its narrower role is to separate:

- the exact finite frame-delta/orbit witness already in this packet;
- the exact A1 and Casimir/block projectors already present elsewhere;
- supplied-atlas or supplied-action positive GR routes; and
- the still-missing full `Pi_curv` object on the current direct-universal
  `PL S^3 x R` surface.

The repair note is therefore compatible with later positive channel/projector
work: it is a current-stack no-go for deriving full `Pi_curv` without an
additional distinguished connection, TT-reduction, source-coupling law, or
supplied geometric action/atlas input. Independent audit remains the authority
on whether that new packet satisfies the conditional row's re-audit request.

The current axiom-first stack gives:

- an exact scalar observable generator from the observable principle
- an exact `3+1` kinematic lift on `PL S^3 x R`
- an exact tensor-valued variational candidate on that lifted background
- an exact unique symmetric `3+1` quotient kernel on the finite prototype
- an exact rank-2 scalar-channel projector on lapse and spatial trace
- an associated family of complement-channel localization coefficients over
  valid `3+1` polarization frames

This source packet does **not** prove:

- a covariant `3+1` polarization-frame / projector bundle that canonically
  splits the symmetric Hessian kernel into lapse, shift, and spatial
  trace/shear channels before localization
- an exact curvature-localization operator `Pi_curv` derivable from the
  current stack alone
- an exhaustive no-go ruling out all possible constructions of such an
  operator

The finite certificate shows that the sampled quotient kernel plus sampled
valid frames do not by themselves supply a frame-independent complement
localization. That is the support result. Any stronger statement requires a
separate exhaustive no-go or a positive bundle construction.

The current runner compares two valid `3+1` polarization frames. The localized
channel coefficients move under frame rotation, so the finite prototype does
not carry a canonical complement-channel section by this route.

The strongest exact object available here is the associated orbit of
localized channels over the valid `3+1` polarization frames. That orbit is
exact on the finite prototype, but this note does not supply a distinguished
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

## What the finite certificate supports

The present data determine a unique bilinear kernel on the symmetric quotient,
and they also determine the exact `A1` invariant projector, but they do not
specify, within this finite two-frame certificate, how to localize the
complementary `E \oplus T1` channels into curvature channels on
`PL S^3 x R`.

In particular, this packet does not construct an exact object that:

1. is tensor-valued and covariant on the `3+1` quotient;
2. splits the Hessian kernel into lapse, shift, and spatial trace/shear
   components;
3. identifies those components with the Einstein/Regge tensor law.

Without that object, the Hessian remains a variational candidate, not a GR
dynamics law. The exact `A1` projector is the strongest selector already
latent in the current stack, but it is not the canonical localization bundle.

## Minimal missing primitive

The finite support result points to the same missing object, without proving
that no alternative route can supply it:

> a covariant `3+1` polarization-frame / projector bundle, equipped with a
> distinguished connection, that extends the exact rank-2 `A1` projector on
> lapse and spatial trace to the complementary `E \oplus T1` channels and
> splits the unique symmetric Hessian kernel into lapse, shift, and spatial
> trace/shear channels before localization.

Equivalently, a future closure would need a covariant `3+1`
curvature-localization operator `Pi_curv` or an equivalent source-side
projector-bundle theorem. The exact structure supplied here is only the
finite frame-orbit family of candidate localizations, not a canonical
projector bundle.

## Honest status

The current direct universal route is:

- exact at the scalar observable level
- exact at the `3+1` kinematic lift level
- exact at the symmetric `3+1` quotient-kernel level
- blocked at the curvature-localization level

That is the sharpest disciplined statement this source packet supports. It
does not close universal GR, does not derive `Pi_curv`, and does not rule out
future covariant projector-bundle constructions.
