---
claim_id: quark_route2_nonlinear_e_center_readout_primitive_boundary_note_2026-06-21
claim_type_author_hint: no_go
status_authority: independent_audit_lane_only
direct_effective_status_change_allowed_from_this_note: false
---

# Quark Route-2 Nonlinear E-Center Readout Primitive Boundary

**Date:** 2026-06-21
**Actual current-surface status:** no-go / exact negative boundary for the
named current nonlinear, log/determinant, tensor, and supplied-readout routes
checked here. This source note does not set, predict, or apply any audit
verdict.
**Trace class:** negative_route_pruning.
**Primary runner:**
[`scripts/frontier_quark_route2_nonlinear_e_center_readout_primitive_boundary_2026_06_21.py`](../scripts/frontier_quark_route2_nonlinear_e_center_readout_primitive_boundary_2026_06_21.py)
**Generated output:**
[`outputs/frontier_quark_route2_nonlinear_e_center_readout_primitive_boundary_2026_06_21.txt`](../outputs/frontier_quark_route2_nonlinear_e_center_readout_primitive_boundary_2026_06_21.txt)

## Purpose

The s3-time Route-2 readout-to-slice gate is blocked by a single readout-map
endpoint triple. The current carrier/time surfaces already give the exact
conditional family, but the unique theorem remains open because the readout
map does not derive

```text
(beta_T / alpha_T, alpha_T / alpha_E, beta_E / alpha_E)
  = (-1, -2, 21/4).
```

After the two T-side entries are granted, the remaining datum is

```text
rho_E := beta_E / alpha_E = 21/4.
```

This note asks whether the current nonlinear/log/determinant/tensor/readout
surfaces on `main` already supply a genuine E-center-sensitive primitive that
selects this value. They do not. The useful new output is a sharper target
sieve: a same-family channel-weight law would have to be an inverse-square
center-lift law

```text
q_X w_X^2 = 5/24,
```

and none of the checked named surfaces derives that law or its normalization.

## Minimal Premises And Forbidden Inputs

Allowed premises:

1. the exact Route-2 restricted endpoint carrier and readout algebra from
   [`QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md`](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md);
2. the exact conditional time/slice family from
   [`QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md`](QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md)
   and [`S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md`](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md);
3. the granted T-side stretch entries
   `beta_T/alpha_T = -1` and `alpha_T/alpha_E = -2`;
4. the current same-domain channel projector weights
   `w_E = 1/3` and `w_T = 1/2` as used by the finite-star covariance
   route;
5. exact rational arithmetic and the cited current source notes' own
   boundaries.

Forbidden proof inputs:

1. observed quark masses, CKM/J fits, or nearest-rational selection from live
   endpoint floats;
2. declaring the endpoint-fitted eta-floor map to be physical by convention;
3. importing `rho_E = 21/4`, `q_E = 15/8`, or `c_TE = -8/9` as a premise;
4. treating Record, determinant/log additivity, or tensor membership as if it
   supplied a physical E-center readout context when the cited notes say it
   does not.

## Exact Compression

With

```text
rho_T = beta_T / alpha_T = -1,
mu    = alpha_T / alpha_E = -2,
rho_E = beta_E / alpha_E,
```

the endpoint algebra is

```text
q_T  = 1 + rho_T / 6 = 5/6,
q_E  = 1 + rho_E / 6,
c_TE = gamma_T(center) / gamma_E(center) = mu q_T / q_E.
```

Therefore the target statements are equivalent:

```text
rho_E = 21/4
  <=> q_E = 15/8
  <=> c_TE = -8/9
  <=> q_E / q_T = 9/4.
```

The exact carrier still leaves the E-center row direction free:

```text
P(rho_E) =
[[1, 0, rho_E, 0],
 [0,-2, 0,     2]].
```

All values of `rho_E` agree on `E-shell`, `T-shell`, and `T-center`; they differ
only on

```text
E-center -> 1 + rho_E/6.
```

That is why any successful route must see the E-center column or supply an
equivalent distinguishing primitive.

## Nonlinear Target Sieve

The same-domain channel weights are

```text
w_E = 1/3,
w_T = 1/2.
```

The target channel ratio is

```text
q_E / q_T = (15/8) / (5/6) = 9/4.
```

If a same-family monomial channel law has the form

```text
q_X proportional to w_X^p,
```

then

```text
q_E / q_T = (w_E / w_T)^p = (2/3)^p.
```

Over the small integer powers checked by the runner, the unique exponent that
matches the target is

```text
p = -2.
```

Equivalently, the law must be

```text
q_X = C / w_X^2.
```

The T-side fixes the normalization:

```text
C = q_T w_T^2 = (5/6)(1/4) = 5/24.
```

Then the E-side would be

```text
q_E = (5/24) / (1/3)^2 = 15/8,
rho_E = 6(q_E - 1) = 21/4,
c_TE = (-2)(5/6)/(15/8) = -8/9.
```

So the nonlinear target is not vague. A successful current-surface primitive
must derive the inverse-square center-lift law

```text
q_X w_X^2 = 5/24
```

or an equivalent E-center-sensitive source/readout rule.

## Named Current Routes Checked

### E-center-blind and record/positivity routes

[`QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md`](QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md)
proves that shell-only, T-side, channel-preserving, low-rational, and other
E-center-blind constraints cannot select `rho_E`.

[`ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md`](ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md)
shows that registration/idempotency/positivity conditions fix a norm or a
one-sided bound, not the E-readout direction. They do not derive the
inverse-square law.

### Quadratic and covariance routes

[`QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md`](QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md)
already closes the quadratic `O_h` invariant route: the `E:T1` ratio is a free
reduced-matrix-element ratio. It also identifies the exact gap as an
inverse-square center-lift law, but does not derive it.

Common weight scalings miss the target:

| scaling | `q_E/q_T` |
|---|---:|
| constant | `1` |
| proportional to `w_X` | `2/3` |
| proportional to `1/w_X` | `3/2` |
| proportional to `w_X^2` | `4/9` |
| proportional to `1/w_X^2` | `9/4` |

Only the last line matches, and it is not produced by the named quadratic or
simple covariance surfaces.

### Tensor and gate-primitive routes

[`S3_TIME_READOUT_PRIMITIVE_BRIDGE_ASSESSMENT_BOUNDED_NOTE_2026-06-12.md`](S3_TIME_READOUT_PRIMITIVE_BRIDGE_ASSESSMENT_BOUNDED_NOTE_2026-06-12.md)
finds broad restricted-class membership for the endpoint-fitted affine map, but
not uniqueness and not an exact physical primitive selection theorem.

[`S3_TIME_TENSORIZED_SCHUR_PRIMITIVE_NOTE.md`](S3_TIME_TENSORIZED_SCHUR_PRIMITIVE_NOTE.md)
and
[`S3_TIME_CONSTRUCTED_SUPPORT_TENSOR_PRIMITIVE_NOTE.md`](S3_TIME_CONSTRUCTED_SUPPORT_TENSOR_PRIMITIVE_NOTE.md)
provide bounded tensor support and comparison primitives. They explicitly do
not supply the exact tensor carrier or endpoint coefficient theorem needed to
fix the E-center lift.

### Log, determinant, and registrable-readout routes

[`OBSERVABLE_PRINCIPLE_T1D_DETERMINANT_READOUT_INDEPENDENCE_NO_GO_NOTE_2026-06-16.md`](OBSERVABLE_PRINCIPLE_T1D_DETERMINANT_READOUT_INDEPENDENCE_NO_GO_NOTE_2026-06-16.md)
proves that determinant-only readout and source-block-to-record injectivity are
not consequences of Record plus determinant algebra alone.

[`OBSERVABLE_PRINCIPLE_T1D_DETERMINANT_CONTEXT_QUOTIENT_BRIDGE_NOTE_2026-06-18.md`](OBSERVABLE_PRINCIPLE_T1D_DETERMINANT_CONTEXT_QUOTIENT_BRIDGE_NOTE_2026-06-18.md)
shows that a supplied determinant-sector context can close that algebra inside
the supplied context, but it does not derive the context from Record.

[`REGISTRABLE_READOUT_DETERMINANT_CHARACTER_ALGEBRAIC_CORE_SPLIT_NOTE_2026-06-18.md`](REGISTRABLE_READOUT_DETERMINANT_CHARACTER_ALGEBRAIC_CORE_SPLIT_NOTE_2026-06-18.md)
isolates exact determinant-character phase-erasure algebra while preserving the
need for separate physical-readout identifications.

[`SOURCE_MEASURE_LOG_SELECTION_BOUNDARY_THEOREM_NOTE_2026-05-30.md`](SOURCE_MEASURE_LOG_SELECTION_BOUNDARY_THEOREM_NOTE_2026-05-30.md)
shows that finite record probability/Radon-Nikodym algebra selects a log
coordinate only up to a source scale. It does not supply a Route-2 E/T
center-weight rule.

[`POST_RECORD_SELECTOR_TANGENT_READOUT_WEIGHT_PROTOTYPE_2026-06-06.md`](POST_RECORD_SELECTOR_TANGENT_READOUT_WEIGHT_PROTOTYPE_2026-06-06.md)
is a supplied finite prototype and explicitly not selector/readout/tangent
authority from Record.

Together these notes do not derive an E-center distinguishing context, an
inverse-square center-lift law, or the normalization `5/24`.

## Boundary Theorem

**Theorem (named-current nonlinear E-center primitive boundary).** On the
current cited Route-2 readout surface, after granting the two T-side target
entries, the named current nonlinear/log/determinant/tensor/readout surfaces
checked in this note do not derive

```text
rho_E = 21/4.
```

The exact same-family monomial target sieve says any successful channel-weight
law must be the inverse-square center-lift law

```text
q_X w_X^2 = 5/24,
```

or an equivalent E-center-sensitive source/readout primitive. The checked
surfaces either remain E-center-blind, fix only norms or supplied contexts,
leave a reduced-matrix-element ratio free, provide only bounded tensor
membership, or require a separate physical readout context. None supplies the
missing law or its normalization.

## No-Go Discipline Gate

**N1. Alternative routes checked.** Checked route families: E-center-blind
constraints, registration/positivity, quadratic covariance, bounded tensor
primitive membership, determinant/log context, registrable determinant
character, source-measure log selection, and supplied selector/tangent
prototype.

**N2. Wall independence.** The wall is a single E-center-sensitive
distinguishing primitive. The checked routes fail in independent ways: some do
not see E-center, some fix norms but not direction, some require supplied
contexts, and some leave channel ratios free.

**N3. Hidden-wall scan.** The target rational values appear only as comparator
targets in the exact endpoint algebra and inverse-square sieve. No observed
mass, fit, or endpoint float is used as a proof input.

**N4. Residual matching.** The residual matches
[`S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md`](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md):
the readout-map endpoint triple is not derived, so the unique
`Theta_R -> Lambda_R` theorem is not closed.

**N5. Rhetoric audit.** The no-go is scoped to the named current surfaces. It
is not a claim that no future nonlinear observable, source-domain theorem, or
owner-approved primitive can derive the E-center law.

**N6. Partial-closure path scan.** The target is now sharper: derive an
E-center-sensitive inverse-square center-lift law, a typed source/readout rule
equivalent to `c_TE = -8/9`, or a physical readout context that supplies the
same information without importing target values.

**N7. Steelman.** A future genuinely nonlinear tensor observable could still
derive `q_X w_X^2 = 5/24`; this note only says the current named nonlinear,
log/determinant, tensor, and supplied-readout surfaces do not.

**N8. Cross-cycle echo.** This agrees with the existing naturality,
E-center-blindness, positivity, source-domain, covariance, and tensor-bridge
boundaries. It narrows the positive target rather than changing any audit
status.

## What Remains Open

The direct positive target is:

```text
derive q_X w_X^2 = 5/24
```

from current or newly supplied first-principles readout/source structure, or
derive an equivalent typed bridge:

```text
gamma_T(center) / gamma_E(center) = -8/9.
```

Until then,
[`S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md`](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md)
remains an exact conditional family with inherited readout non-uniqueness, not
a unique readout-to-slice theorem.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_nonlinear_e_center_readout_primitive_boundary_2026_06_21.py
```

Expected summary:

```text
TOTAL: PASS=90 FAIL=0
VERDICT: current named nonlinear/log/determinant/tensor routes do not derive the E-center primitive; inverse-square center-lift remains the sharp target.
```
