# Quark Route-2 Source-Unit Scale-Character Boundary

**Date:** 2026-06-22
**Type:** exact negative boundary / no-go plus exact support
**Claim type:** no_go
**Actual current-surface status:** no-go
**Status authority:** independent audit lane only. This source note does not
set, predict, or apply an audit verdict.
**Primary runner:** [scripts/frontier_quark_route2_source_unit_scale_character_boundary_2026_06_22.py](../scripts/frontier_quark_route2_source_unit_scale_character_boundary_2026_06_22.py)
**Runner output:** [outputs/frontier_quark_route2_source_unit_scale_character_boundary_2026_06_22.txt](../outputs/frontier_quark_route2_source_unit_scale_character_boundary_2026_06_22.txt)

## Scope

Block112 compressed the remaining Route-2 coefficient wall to:

```text
derive the physical source-unit/no-scale law g(a w) = g(w),
or find a direct E-center route around the Hessian chain.
```

This block attacks the first option from a positive-ray naturality frame. It
asks whether regular scale covariance of the coefficient under positive-ray
rescaling is enough to force the no-scale law.

It is not. Regular scale covariance gives a scale character

```text
g(a w) = chi(a) g(w),       chi(a b) = chi(a) chi(b).
```

Under regularity, this character has the power form `chi(a)=a^m`, so the
coefficient is `g(w)=C w^m`. The Route-2 endpoint is recovered only for the
trivial character `m=0`. The current surface does not derive that the
coefficient carries zero source-unit weight.

The exact positive support is equally sharp: a future theorem proving either

```text
chi(a) = 1
```

for every positive `a`, or equivalently

```text
g(a w) = g(w),
```

would force the constant coefficient and close the Block112 coefficient
subgate. This block does not prove that theorem.

## A_min And Forbidden Imports

Allowed in this block:

- the exact Route-2 endpoint algebra and S3 blocker;
- the O_h weights `w_E=1/3`, `w_T=1/2`;
- supplied T-side values `q_T=5/6` and `s_TE=-2` as conditional stretch
  inputs;
- Block110's log-action Hessian consequence;
- Block111's affine-gauge finite-jet boundary;
- Block112's coefficient compression;
- regular multiplicative-character algebra on the positive ray;
- existing source-measure notes as source-scale analogies and boundary
  checks;
- exact rational arithmetic for integer-character witnesses.

Forbidden proof inputs:

- observed masses;
- fitted endpoint values;
- nearest-rational selection;
- live endpoint measurements;
- literature values;
- assuming `q_E=15/8`, `rho_E=21/4`, or `c_TE=-8/9`;
- assuming from the start that the coefficient character is trivial;
- using endpoint equality as a proof of the physical source-unit law.

The target fractions appear only as exact consequences or comparison values.

## One-Hop Authorities

| Authority | Role used here |
| --- | --- |
| [QUARK_ROUTE2_NO_SCALE_CURVATURE_COEFFICIENT_NO_GO_NOTE_2026-06-22.md](QUARK_ROUTE2_NO_SCALE_CURVATURE_COEFFICIENT_NO_GO_NOTE_2026-06-22.md) | Direct parent: the endpoint ratio is equivalent to `g_E/g_T=1`, and full `g(a w)=g(w)` would force constant `g`. |
| [QUARK_ROUTE2_SOURCE_ACTION_PRIMITIVE_BOUNDARY_NOTE_2026-06-22.md](QUARK_ROUTE2_SOURCE_ACTION_PRIMITIVE_BOUNDARY_NOTE_2026-06-22.md) | Parent readout gate: affine-gauge finite-jet support leaves `g(w) Phi''(w)` open. |
| [QUARK_ROUTE2_LOG_ACTION_COCYCLE_HESSIAN_BOUNDARY_NOTE_2026-06-22.md](QUARK_ROUTE2_LOG_ACTION_COCYCLE_HESSIAN_BOUNDARY_NOTE_2026-06-22.md) | Positive bridge: log-action plus Hessian row gives the endpoint. |
| [SOURCE_MEASURE_LOG_SELECTION_BOUNDARY_THEOREM_NOTE_2026-05-30.md](SOURCE_MEASURE_LOG_SELECTION_BOUNDARY_THEOREM_NOTE_2026-05-30.md) | Source-scale analogy: product/RN algebra selects log coordinate up to scale, not source unit. |
| [SOURCE_MEASURE_PCAL_RN_COCYCLE_THEOREM_NOTE_2026-05-30.md](SOURCE_MEASURE_PCAL_RN_COCYCLE_THEOREM_NOTE_2026-05-30.md) | Positive source-unit analogy: primitive RN score fixes the unit only after source intervention semantics are identified. |
| [SOURCE_MEASURE_PLANCK_ACTION_RN_SOURCE_UNIT_BRIDGE_NOTE_2026-05-30.md](SOURCE_MEASURE_PLANCK_ACTION_RN_SOURCE_UNIT_BRIDGE_NOTE_2026-05-30.md) | Bounded bridge analogy: action exponent coordinate can fix RN source unit only after that action normalization is accepted. |
| [YT_PRIMITIVE_UNIT_SOURCE_ACTION_PHYSICAL_PREMISE_NO_GO_NOTE_2026-05-25.md](YT_PRIMITIVE_UNIT_SOURCE_ACTION_PHYSICAL_PREMISE_NO_GO_NOTE_2026-05-25.md) | Prior source-scale no-go: a lambda family preserves structural tests while changing the coefficient. |
| [S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md) | Downstream open gate and endpoint-triple blocker. |

## Scale-Character Lemma

Let `g` be a positive coefficient on the positive weight ray. Suppose positive
rescaling of the ray acts on the coefficient by a channel-independent regular
character:

```text
g(a w) = chi(a) g(w),       a,w > 0.
```

Applying two rescalings gives:

```text
g(a b w) = chi(a b) g(w)
```

and also

```text
g(a b w) = chi(a) g(b w) = chi(a) chi(b) g(w).
```

Since `g(w)>0`, the scale factor obeys:

```text
chi(a b) = chi(a) chi(b).
```

Regular multiplicative characters of the positive ray have the form:

```text
chi(a) = a^m.
```

Setting `w=1` in the covariance law gives:

```text
g(a) = chi(a) g(1),
```

so

```text
g(w) = C w^m.
```

Thus ordinary scale covariance does not force the no-scale coefficient. It
reduces the freedom from arbitrary `g(w)` to a one-parameter source-unit
weight `m`.

## Endpoint Consequence

For the log-action Hessian representative,

```text
Phi''(w) = C_0 / w^2.
```

With `g(w)=C w^m`, the row has degree:

```text
R_m(w) proportional w^(m-2).
```

Using

```text
w_E = 1/3,       w_T = 1/2,
```

the E/T row ratio is:

```text
R_m(E/T) = (w_E/w_T)^(m-2) = (3/2)^(2-m).
```

The endpoint requires `R_m(E/T)=9/4`, so inside the regular character family:

```text
m = 0.
```

Concrete integer witnesses:

| `m` | `chi(a)` | `g_E/g_T` | `R_m(E/T)` | `q_E` | `rho_E` | `c_TE` |
| ---: | --- | ---: | ---: | ---: | ---: | ---: |
| `-1` | `a^-1` | `3/2` | `27/8` | `45/16` | `87/8` | `-16/27` |
| `0` | `1` | `1` | `9/4` | `15/8` | `21/4` | `-8/9` |
| `1` | `a` | `2/3` | `3/2` | `5/4` | `3/2` | `-4/3` |
| `2` | `a^2` | `4/9` | `1` | `5/6` | `-1` | `-2` |

So the phrase "source-unit naturality" must be strong enough to prove the
trivial character. A theorem that merely proves regular scale-character
covariance still leaves nonzero `m` witnesses.

## Endpoint Equality Is A Diagnostic, Not A Source Law

Inside the character family, endpoint matching diagnoses the trivial
character:

```text
R_m(E/T) = 9/4
  <=> (2/3)^m = 1
  <=> m = 0.
```

This is not a derivation of the physical source-unit law. It uses the endpoint
equality that the S3/Route-2 lane is trying to derive. The source theorem must
therefore come from independent source/action or readout semantics, not from
plugging in the target endpoint.

## Source-Scale Analogy

The existing source-measure boundary has the same shape. Finite product/RN
source algebra selects a logarithmic coordinate only up to scale:

```text
W_c = c log Z.
```

The scaled RN family has score `lambda O` and Fisher norm `lambda^2`; finite
record algebra alone leaves `lambda` free. The positive RN-cocycle and
Planck-action bridge notes show how the unit can be fixed after an additional
source-intervention or action-normalization premise is supplied.

Block113 transfers only the discipline, not the conclusion: the Route-2
coefficient needs its own zero-weight theorem. The source-measure analogies
show why "regular source scale" is too weak unless the primitive unit is
also fixed.

## Current-Surface Boundary

This block proves a scoped no-go:

```text
regular positive-ray scale-character covariance of g
does not force
g(a w) = g(w).
```

The exact support route left open is:

```text
physical Route-2 source-unit theorem
  -> chi(a)=1
  -> g(w)=constant
  -> log-action Hessian endpoint ratio 9/4
  -> with the stated T-side stretch inputs, q_E=15/8, rho_E=21/4,
     c_TE=-8/9.
```

The current surface still does not derive the Route-2 source-unit theorem, the
positive-ray source-action semantics, or the endpoint triple.

## No-Go Discipline

N1 alternative routes:

| Route | Result |
| --- | --- |
| Arbitrary smooth coefficient | Block112: leaves all `g(w)` open. |
| Regular scale-character covariance | This block: reduces to `g(w)=C w^m`, but leaves `m` open. |
| Endpoint equality inside character family | Selects `m=0` only after importing the endpoint target. |
| Primitive unit / trivial character | Sufficient for the endpoint, but not derived here. |
| Direct E-center theorem | Still open and may bypass the coefficient chain. |

N2 wall independence:

The wall is the zero-weight source-unit theorem for the Hessian coefficient.
It is independent of endpoint arithmetic, affine-gauge derivative-order
selection, and the log functional equation once their premises are supplied.

N3 hidden-wall scan:

No observed masses, fitted endpoint values, nearest-rational selector,
literature value, or live endpoint measurement is used. The target endpoint is
not used as a source-law proof input.

N4 residual matching:

The residual matches the S3/Route-2 blocker: the E-channel map entry remains
unselected because the physical source/readout primitive still lacks a
zero-weight coefficient theorem.

N5 rhetoric audit:

"Trivial character" and "source-unit theorem" name future theorem premises.
They are not asserted as current Route-2 framework content.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_unit_scale_character_boundary_2026_06_22.py
```

Expected final line:

```text
TOTAL: PASS=145, FAIL=0
```
