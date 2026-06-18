# Universal GR Polarization-Frame Bundle Attempt on `PL S^3 x R`

**Status:** open - polarization-frame bundle attempt blocked by complement-frame ambiguity
**Date:** 2026-04-14  
**Branch:** `codex/review-active`  
**Role:** direct universal route / attempt note  
**Purpose:** test whether the current axiom-first universal stack can derive a
canonical covariant `3+1` polarization-frame / projector bundle before
curvature localization

**Primary runner:** scripts/frontier_universal_gr_polarization_frame_bundle.py

**Audit-scope note (2026-06-18):** the auditable source claim in this
row is the finite prototype frame-dependence diagnostic and the
downstream source-boundary firewall. The scalar-observable, `3+1`
lift, tensor-candidate, quotient-kernel, and blocker surfaces named
below are route-context handles for the historical universal route, not
one-hop proof authorities imported by this row. The primary runner now
checks the finite matrix calculation and this boundary language without
reading those upstream notes as proof inputs. Any downstream
current-stack or route-level closure must cite and audit the upstream
sources directly.

## Verdict

The route context investigated here does **not** derive a canonical
polarization-frame bundle from the scalar observable principle, the exact
`3+1` lift, and the unique symmetric quotient kernel alone. Those
upstream ingredients are context handles in this row; this packet's
auditable calculation is the finite prototype frame-orbit diagnostic
below.

The route context records:

- an exact scalar observable generator;
- an exact `3+1` kinematic background `PL S^3 x R`;
- an exact tensor-valued variational candidate;
- an exact unique symmetric `3+1` quotient kernel on the finite prototype.

What it does **not** give is a canonical full section or projector bundle that
splits the symmetric kernel into lapse, shift, and spatial trace/shear
channels before localization.

What it does give, exactly, is:

- an exact rank-2 scalar-channel projector (legacy irrep label `A_1`)
  onto lapse and spatial trace;
- an associated family of localized channel coefficients indexed by valid
  `3+1` polarization frames.

The scalar-channel projector is canonical. The complement is not. So the current stack
has an exact minimal-covariance selector, but it is not yet a canonical full
polarization section.

## Attempted derivation

The natural attempt is:

1. start from the exact `3+1` background scaffold `PL S^3 x R`;
2. use the unique symmetric quotient kernel to define the tensor channels;
3. declare the channel split to be the polarization bundle;
4. promote the induced localization to a curvature operator `Pi_curv`.

The attempt fails at step 2 -> 3 for the complementary `E \oplus T1`
channels.

The quotient kernel is unique, but the channel split is not canonical on the
current stack. Two valid `3+1` polarization frames related by a spatial
rotation yield different localized channel coefficients for the same kernel.
That is not a numerical artifact. It is the exact obstruction.

The primary runner records the frame dependence explicitly:

- the quotient kernel stays fixed;
- the localized channel coefficients change with polarization frame choice;
- the resulting channel mismatch is `frame_delta = 6.767e-02`.

So the current universal route determines:

- a canonical scalar-channel (`A_1`) section;
- an associated family of candidate localizations on the complement;
- not yet a canonical polarization section or projector bundle for the full
  symmetric kernel.

## Exact obstruction

The present stack does not supply a covariant polarization frame bundle with
a distinguished connection or horizontal distribution on the complement.

Equivalently, it does not supply a canonical `Pi_curv` on the full quotient
kernel alone.

The obstruction is now sharp:

- the scalar generator is exact;
- the `3+1` lift is exact;
- the symmetric quotient kernel is exact;
- the localization map is not canonical without an extra bundle primitive.

## Minimal extra primitive

The smallest missing object is now:

> a covariant `3+1` polarization-frame bundle, or equivalent projector
> bundle, equipped with a distinguished connection that extends the exact
> rank-2 scalar-channel (`A_1`) projector on lapse and spatial trace to the complementary
> `E \oplus T1` channels before curvature localization.

That is the extra primitive required to turn the exact quotient kernel into a
canonical Einstein/Regge dynamics law.

## Downstream source-boundary firewall

Allowed downstream uses of this packet are limited to:

- cite the finite prototype frame-dependence diagnostic;
- cite this packet as a context pointer to the scalar observable generator,
  `3+1` lift on `PL S^3 x R`, tensor-valued variational candidate, and
  unique symmetric quotient-kernel route handles, while citing those
  upstream sources directly if they are load-bearing;
- cite the exact rank-2 scalar-channel projector on lapse and spatial trace;
- cite the obstruction that complement-channel localization coefficients
  depend on valid polarization-frame choices.

Forbidden downstream uses without a new retained bridge:

- do not cite this packet as a canonical full polarization-frame bundle;
- do not cite it as a canonical full projector bundle;
- do not cite it as a curvature-localization operator `Pi_curv`;
- do not cite it as an Einstein/Regge dynamics law;
- do not cite it as a framework-level GR derivation;
- do not cite it as an exhaustive no-go against all curvature-localization
  routes;
- do not promote the frame-orbit obstruction into a positive theorem without
  supplying a distinguished covariant frame/projector bundle with connection.

Re-audit should be triggered if a downstream row uses this packet as more
than an open-gate blocker, scalar-channel support theorem, or associated
localization-orbit diagnostic. The missing retained bridge is still a
covariant `3+1` polarization-frame/projector bundle equipped with a
distinguished connection or horizontal distribution on the complement.

## Honest status

This packet's auditable source claim is:

- exact at the finite prototype Hessian / symmetric-basis level;
- exact for the displayed pair of valid `3+1` polarization frames;
- exact for the source-boundary statement that the complement-frame
  localization is an associated orbit, not a canonical full section;
- open at the covariant polarization-frame / curvature-localization
  level.

Route context, not one-hop authority in this row, records upstream work
that is:

- exact at the scalar observable level
- exact at the `3+1` kinematic lift level
- exact at the symmetric `3+1` quotient-kernel level
- blocked at the covariant polarization-frame / curvature-localization level.

This is the sharpest exact statement currently available on the universal
route.
