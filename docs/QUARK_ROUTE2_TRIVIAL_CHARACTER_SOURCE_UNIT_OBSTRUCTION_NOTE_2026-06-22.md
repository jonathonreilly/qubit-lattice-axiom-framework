# Quark Route-2 Trivial-Character Source-Unit Obstruction

**Date:** 2026-06-22
**Type:** exact negative boundary / stretch attempt
**Claim type:** no_go
**Actual current-surface status:** no-go
**Status authority:** independent audit lane only. This source note does not
set, predict, or apply an audit verdict.
**Primary runner:** [scripts/frontier_quark_route2_trivial_character_source_unit_obstruction_2026_06_22.py](../scripts/frontier_quark_route2_trivial_character_source_unit_obstruction_2026_06_22.py)
**Runner output:** [outputs/frontier_quark_route2_trivial_character_source_unit_obstruction_2026_06_22.txt](../outputs/frontier_quark_route2_trivial_character_source_unit_obstruction_2026_06_22.txt)

## Scope

Block113 proved that regular positive-ray scale covariance reduces the
Route-2 Hessian coefficient to a character family:

```text
g(w) = C w^m.
```

The endpoint route needs the trivial character:

```text
m = 0.
```

This block is the required stretch attempt on that hard residual. It asks
whether physical source-unit normalization, by itself, forces `m=0`.

It does not. Primitive source-unit normalization can fix the source coordinate
or the RN/Fisher scale, but the coefficient may still carry a separate
positive-ray character weight unless the framework proves that the coefficient
is a scalar of source-unit weight zero.

The exact positive residue is sharper: inside the Block113 character family,
any independent same-coefficient calibration at two distinct weights forces
`m=0`. Therefore a future Route-2 theorem can close the coefficient subgate by
proving either:

```text
g(u) = g(v)        for one independent pair u != v,
```

or the stronger scalarity law:

```text
g(a w) = g(w).
```

The S3 endpoint pair `w_E=1/3`, `w_T=1/2` cannot be used as that calibration
unless it is derived independently of the endpoint target.

## A_min And Forbidden Imports

Allowed in this block:

- the exact Route-2 endpoint algebra and S3 blocker;
- the O_h weights `w_E=1/3`, `w_T=1/2`;
- supplied T-side values `q_T=5/6` and `s_TE=-2` as conditional stretch
  inputs;
- Block110's log-action Hessian consequence;
- Block111's affine-gauge finite-jet boundary;
- Block112's coefficient compression;
- Block113's regular character reduction;
- source-measure source-unit notes as analogies and boundary checks;
- exact rational arithmetic for integer-character witnesses.

Forbidden proof inputs:

- observed masses;
- fitted endpoint values;
- nearest-rational selection;
- live endpoint measurements;
- literature values;
- assuming `q_E=15/8`, `rho_E=21/4`, or `c_TE=-8/9`;
- assuming the coefficient is a source-unit scalar;
- using the E/T endpoint equality as the source-unit calibration.

The target fractions appear only as exact consequences or comparison values.

## One-Hop Authorities

| Authority | Role used here |
| --- | --- |
| [QUARK_ROUTE2_SOURCE_UNIT_SCALE_CHARACTER_BOUNDARY_NOTE_2026-06-22.md](QUARK_ROUTE2_SOURCE_UNIT_SCALE_CHARACTER_BOUNDARY_NOTE_2026-06-22.md) | Direct parent: regular covariance gives `g(w)=C w^m`; endpoint requires `m=0`. |
| [QUARK_ROUTE2_NO_SCALE_CURVATURE_COEFFICIENT_NO_GO_NOTE_2026-06-22.md](QUARK_ROUTE2_NO_SCALE_CURVATURE_COEFFICIENT_NO_GO_NOTE_2026-06-22.md) | Parent compression: `g_E/g_T=1` is equivalent to the endpoint ratio inside the prefactor family. |
| [QUARK_ROUTE2_SOURCE_ACTION_PRIMITIVE_BOUNDARY_NOTE_2026-06-22.md](QUARK_ROUTE2_SOURCE_ACTION_PRIMITIVE_BOUNDARY_NOTE_2026-06-22.md) | Parent readout gate: affine-gauge Hessian support still leaves `g(w) Phi''(w)` open. |
| [SOURCE_MEASURE_LOG_SELECTION_BOUNDARY_THEOREM_NOTE_2026-05-30.md](SOURCE_MEASURE_LOG_SELECTION_BOUNDARY_THEOREM_NOTE_2026-05-30.md) | Boundary analogy: finite source algebra leaves a unit scale open. |
| [SOURCE_MEASURE_PCAL_RN_COCYCLE_THEOREM_NOTE_2026-05-30.md](SOURCE_MEASURE_PCAL_RN_COCYCLE_THEOREM_NOTE_2026-05-30.md) | Positive analogy: primitive RN score fixes source coordinate only after RN-cocycle semantics are accepted. |
| [SOURCE_MEASURE_PLANCK_ACTION_RN_SOURCE_UNIT_BRIDGE_NOTE_2026-05-30.md](SOURCE_MEASURE_PLANCK_ACTION_RN_SOURCE_UNIT_BRIDGE_NOTE_2026-05-30.md) | Positive analogy: Planck/action coordinate fixes source unit only after action normalization is accepted. |
| [YT_PRIMITIVE_UNIT_SOURCE_ACTION_PHYSICAL_PREMISE_NO_GO_NOTE_2026-05-25.md](YT_PRIMITIVE_UNIT_SOURCE_ACTION_PHYSICAL_PREMISE_NO_GO_NOTE_2026-05-25.md) | Prior source-scale no-go: a lambda family preserves structural tests while changing the coefficient. |
| [S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md) | Downstream open gate and endpoint-triple blocker. |

## First-Principles Fan-Out

### Frame 1: one-point source-unit normalization

Set a primitive source unit at one reference weight:

```text
g(1) = C.
```

Every character member `g(w)=C w^m` satisfies this. One-point unit
normalization fixes the coefficient at the reference point, not its character
weight.

### Frame 2: primitive RN/Fisher source coordinate

The source-measure RN theorem fixes the unit source coordinate once physical
sources are identified with primitive RN cocycles. In symbols, it selects
`lambda=1`.

That is not yet a theorem about the Route-2 Hessian coefficient. Even with
`lambda=1`, the coefficient family

```text
g_m(w)=C w^m
```

has different E/T row ratios for different `m`.

### Frame 3: Planck/action source coordinate

The Planck/action bridge identifies the dimensionless action exponent
coordinate with the RN/Fisher coordinate once that source-action normalization
is accepted. This can fix the source coordinate. It still does not prove that
the separate Hessian prefactor is a source-unit scalar rather than a density
with character weight `m`.

### Frame 4: coordinate scalarity

If the coefficient is physically a scalar under positive source-unit changes,
then:

```text
g(a w) = g(w),
```

and Block112 closes the coefficient subgate. But this scalarity statement is
exactly the missing theorem. A tensor-density or weighted-source
interpretation can carry nonzero character weight while preserving regular
scale covariance.

### Frame 5: distinct-weight calibration

Inside the character family, a single independent same-coefficient calibration
at two distinct weights is decisive. If:

```text
g(u) = g(v),       u != v,
```

then:

```text
C u^m = C v^m,
```

so:

```text
(u/v)^m = 1.
```

For positive `u/v != 1`, regular real characters give:

```text
m = 0.
```

This is the best positive path found in the stretch attempt. The missing
science is an independent Route-2 reason for such a calibration, not the
algebra after it is supplied.

## Endpoint Consequence

With `g(w)=C w^m`, the log-action Hessian row ratio is:

```text
R_m(E/T) = (w_E/w_T)^(m-2).
```

For `w_E=1/3` and `w_T=1/2`, this is:

```text
R_m(E/T) = (3/2)^(2-m).
```

The endpoint route hits:

```text
R_m(E/T) = 9/4
```

only at `m=0`. But using this E/T equality to prove `m=0` is circular unless
the equality is independently derived from source/readout semantics.

## Current-Surface Boundary

This block proves a scoped no-go:

```text
primitive source-unit normalization
+ regular character covariance
does not force
chi(a)=1.
```

It also proves an exact support theorem:

```text
regular character covariance
+ independent distinct-weight same-coefficient calibration
=> chi(a)=1
=> g(w)=constant
=> Block112 coefficient subgate closes.
```

The current surface supplies no independent distinct-weight calibration and no
source-unit scalarity theorem for the Route-2 Hessian coefficient.

## No-Go Discipline

N1 alternative routes:

| Route | Result |
| --- | --- |
| One-point source-unit normalization | Leaves all `m` open. |
| Primitive RN/Fisher source coordinate | Fixes source coordinate only after source semantics; does not fix Hessian coefficient weight. |
| Planck/action coordinate | Fixes source coordinate only after action normalization; does not fix Hessian coefficient weight. |
| Coordinate scalarity of `g` | Sufficient, but exactly the missing theorem. |
| Distinct-weight calibration | Sufficient if independently derived; not supplied by current surface. |
| E/T endpoint equality | Diagnoses `m=0`, but is the target and cannot be proof input. |

N2 wall independence:

The remaining wall is the source-unit representation type of the Hessian
coefficient. It is not endpoint arithmetic, source coordinate normalization,
or the log functional equation.

N3 hidden-wall scan:

No observed masses, fitted endpoint values, nearest-rational selector,
literature value, or live endpoint measurement is used. No endpoint equality
is used as a source-unit premise.

N4 residual matching:

The residual matches the S3/Route-2 blocker: a unique E-channel map entry
still requires a physical source/readout primitive that fixes or bypasses the
coefficient character.

N5 rhetoric audit:

"Scalarity", "distinct-weight calibration", and "trivial character" name
future theorem premises. They are not asserted as current Route-2 framework
content.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_trivial_character_source_unit_obstruction_2026_06_22.py
```

Expected final line:

```text
TOTAL: PASS=61, FAIL=0
```
