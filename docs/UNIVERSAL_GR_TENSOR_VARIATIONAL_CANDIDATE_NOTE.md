# Universal GR Tensor Variational Candidate on `PL S^3 x R`

**Status:** bounded - bounded or caveated result note
**Date:** 2026-04-14  
**Branch:** `codex/review-active`  
**Role:** direct universal route / theorem step  
**Purpose:** identify the first formal tensor-valued `3+1` variational
candidate from the axiom-side observable principle and the cited `3+1`
kinematic lift surface
**Status authority:** independent audit lane only.
**Primary runner:** [`scripts/frontier_universal_gr_tensor_variational_candidate.py`](../scripts/frontier_universal_gr_tensor_variational_candidate.py)
(`PASS=6 FAIL=0` on current main). The runner checks the finite Hessian
symmetry and quadratic-form prototype and keeps the Einstein/Regge
identification blocker in scope.

## Audit boundary

This row is a source-side route-candidate note, not an audit-ratified GR
closure. References below to the scalar observable, the `3+1` lift, and the
quotient kernel refer to the formal construction on the cited source surfaces;
they do not promote the imported observable-principle row, the `S^3`/anomaly
lift row, or the blocker row beyond their independent audit status. The
registered runner verifies that the Hessian candidate is well-defined and
symmetric on a finite prototype and that the Einstein/Regge identification
blocker remains open.

## Verdict

The direct universal route is still not closed, but it now has a concrete
tensor-valued variational candidate and a sharper finite-prototype check on
the current `3+1` perturbation space.

The scalar-observable source surface gives the generator

`W[J] = log|det(D+J)| - log|det D|`

and Route 2 gives the `3+1` kinematic background candidate

`PL S^3 x R`.

The first formal tensor-valued variational candidate on that lifted background
is the metric-source Hessian of `W` at the lifted background point.

In other words, if `g_*` denotes the lifted background metric source and
`h_{ab}` a symmetric `3+1` metric perturbation, then the candidate quadratic
form is

`S_GR^cand[h] := 1/2 * D^2 W[g_*](h, h)`.

This is the first direct-universal object that is:

- tensor-valued
- variational by construction
- grounded in the scalar-observable source surface
- defined on the inherited `3+1` background scaffold

## Why this is the right next object

The current blocker was not a missing scalar generator and not a missing
`3+1` lift.

The missing object was the first tensor-valued variational object that
could sit on top of both.

The Hessian is the minimal formal lift of the scalar generator into tensor
source space:

`B(h, k) := D^2 W[g_*](h, k)`

with

`B(h, k) = B(k, h)`.

So the direct universal route now has a precise candidate action family rather
than just a generic blocker.

## Formal structure of the candidate

On the current lifted background, the candidate behaves as:

1. scalar generator supplied: `W[J]` is the additive scalar observable
   generator on the axiom-side Grassmann surface;
2. `3+1` lift supplied at its inherited source boundary: `PL S^3 x R` is the
   background scaffold;
3. tensor candidate formalized: the second variation of `W` is a symmetric
   bilinear form on `3+1` metric sources.

This is enough to define a legitimate tensor-valued variational candidate.

It is **not** yet enough to prove that the candidate equals the Einstein/Regge
action on the full metric space.

## Strongest current candidate result

The current route now gives more than a bare candidate:

1. the candidate is the second variation of the scalar observable
   generator on the lifted background;
2. on the finite `3+1` prototype used by the current runner, that Hessian is
   symmetric as a bilinear form;
3. the finite prototype has bounded quadratic-form values on the tested
   perturbations.

That is the strongest honest candidate statement currently supported by the
runner. It does **not** identify the Hessian kernel with Einstein/Regge
curvature dynamics or prove a quotient-uniqueness theorem.

## What remains open

The remaining theorem is now sharply localized:

1. identify the unique symmetric `3+1` Hessian kernel with the local
   Einstein/Regge tensor law, or
2. derive an exact tensor-valued uniqueness theorem forcing that
   identification, or
3. prove the candidate cannot be promoted without a new curvature-localization
   primitive

The current stack does not yet supply that curvature-localization primitive.
The Hessian candidate is defined as a tensor-valued variational object, but it
still has no exact map into Einstein/Regge curvature channels on `PL S^3 x R`.

So the direct universal route is now one step more concrete:

> scalar observable principle + inherited `3+1` lift + tensor-valued
> variational candidate + finite symmetric-bilinear prototype

but it is still not a full closure theorem.

## Honest status

The current direct-universal theorem step is:

- scalar observable generator in hand
- inherited `3+1` kinematic lift in hand
- tensor-valued variational candidate in hand
- finite symmetric-bilinear prototype in hand
- exact Einstein/Regge identification still missing

That is the cleanest statement available on the current atlas.

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [observable_principle_from_axiom_note](OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md)
- [s3_anomaly_spacetime_lift_note](S3_ANOMALY_SPACETIME_LIFT_NOTE.md)
- `UNIVERSAL_GR_TENSOR_ACTION_BLOCKER_NOTE.md` (guardrail checked by the
  runner, not a load-bearing source parent for the Hessian candidate)
- `UNIVERSAL_GR_TENSOR_QUOTIENT_UNIQUENESS_NOTE.md` (downstream consumer; backticked to avoid length-2 cycle — citation graph direction is *downstream → upstream*)
- `UNIVERSAL_GR_CURVATURE_LOCALIZATION_BLOCKER_NOTE.md` (downstream consumer; backticked to avoid length-2 cycle — citation graph direction is *downstream → upstream*)
