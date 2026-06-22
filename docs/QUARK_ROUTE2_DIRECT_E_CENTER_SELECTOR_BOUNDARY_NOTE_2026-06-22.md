# Quark Route-2 Direct E-Center Selector Boundary

**Date:** 2026-06-22
**Type:** exact negative boundary / direct readout stretch attempt
**Claim type:** no_go
**Actual current-surface status:** no-go
**Status authority:** independent audit lane only. This source note does not
set, predict, or apply an audit verdict.
**Primary runner:** [scripts/frontier_quark_route2_direct_e_center_selector_boundary_2026_06_22.py](../scripts/frontier_quark_route2_direct_e_center_selector_boundary_2026_06_22.py)
**Runner output:** [outputs/frontier_quark_route2_direct_e_center_selector_boundary_2026_06_22.txt](../outputs/frontier_quark_route2_direct_e_center_selector_boundary_2026_06_22.txt)

## Scope

Blocks112-114 isolated the source-unit route to a zero-weight coefficient
theorem or an independent distinct-weight calibration. This block pivots to
the direct consumer named by the S3/Route-2 handoffs: derive the E-center map
entry without the Hessian/source-unit chain.

The exact readout-map authority already gives the reduced family. If the two
T-side candidates are granted,

```text
beta_T / alpha_T = -1,
alpha_T / alpha_E = -2,
```

then the remaining family is:

```text
P(rho_E) = [[1, 0, rho_E, 0],
            [0, -2, 0, 2]].
```

The missing endpoint is:

```text
rho_E = beta_E / alpha_E = 21/4.
```

This block tests direct selector routes on that reduced family. The result is
negative: shell normalization, T-side constraints, linearity,
center-positivity, and minimal-norm/minimal-deformation selectors do not
select `21/4`. They either leave a continuum of admissible `rho_E` values or
select `rho_E=0`.

The exact positive residue is sharp. A direct E-center theorem must derive:

```text
q_E = gamma_E(center) / gamma_E(shell) = 15/8,
```

equivalently:

```text
rho_E = 6(q_E - 1) = 21/4.
```

That E-center lift theorem is not supplied by the current readout surface.

## A_min And Forbidden Imports

Allowed in this block:

- the exact restricted Route-2 readout map family;
- the exact endpoint carrier columns;
- the conditional T-side candidates `beta_T/alpha_T=-1` and
  `alpha_T/alpha_E=-2`;
- exact rational arithmetic in the one-parameter `rho_E` family;
- the S3 conditional coupling note as downstream consumer.

Forbidden proof inputs:

- observed masses;
- fitted endpoint values;
- nearest-rational selection;
- live endpoint measurements;
- literature values;
- assuming `rho_E=21/4`, `q_E=15/8`, or `c_TE=-8/9`;
- using the target endpoint chain as a selector;
- importing the Hessian/source-unit route as a direct E-center proof.

The target fractions appear only as exact consequences or comparison values.

## One-Hop Authorities

| Authority | Role used here |
| --- | --- |
| [QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md) | Direct parent: exact carrier/readout reduction and exact missing-map obstruction. |
| [S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md) | Downstream consumer: unique coupling remains blocked by the endpoint triple. |
| [QUARK_ROUTE2_TRIVIAL_CHARACTER_SOURCE_UNIT_OBSTRUCTION_NOTE_2026-06-22.md](QUARK_ROUTE2_TRIVIAL_CHARACTER_SOURCE_UNIT_OBSTRUCTION_NOTE_2026-06-22.md) | Previous pivot: source-unit normalization alone does not force the coefficient character. |
| [QUARK_ROUTE2_SOURCE_UNIT_SCALE_CHARACTER_BOUNDARY_NOTE_2026-06-22.md](QUARK_ROUTE2_SOURCE_UNIT_SCALE_CHARACTER_BOUNDARY_NOTE_2026-06-22.md) | Previous coefficient character boundary. |
| [QUARK_ROUTE2_NO_SCALE_CURVATURE_COEFFICIENT_NO_GO_NOTE_2026-06-22.md](QUARK_ROUTE2_NO_SCALE_CURVATURE_COEFFICIENT_NO_GO_NOTE_2026-06-22.md) | Previous no-scale coefficient compression. |

## Reduced Family Algebra

With `alpha_E=1`, `alpha_T=-2`, and `beta_T=2`, the readout maps are:

```text
P(rho) = [[1, 0, rho, 0],
          [0, -2, 0, 2]].
```

The exact endpoint columns are:

```text
E-shell  = (1, 0, 0,   0),
E-center = (1, 0, 1/6, 0),
T-shell  = (0, 1, 0,   0),
T-center = (0, 1, 0,   1/6).
```

Thus:

```text
gamma_E(shell)  = 1,
gamma_E(center) = 1 + rho/6,
gamma_T(shell)  = -2,
gamma_T(center) = -5/3.
```

The T-side row is already fixed:

```text
q_T = gamma_T(center)/gamma_T(shell) = 5/6,
s_TE = gamma_T(shell)/gamma_E(shell) = -2.
```

The only remaining variable is:

```text
q_E(rho) = 1 + rho/6.
```

The target `q_E=15/8` is exactly equivalent to `rho=21/4`.

## Direct Selector Fan-Out

### Shell normalization

Every `P(rho)` has:

```text
gamma_E(shell) = 1.
```

Shell normalization does not see `rho`.

### T-side constraints

Every `P(rho)` preserves:

```text
q_T = 5/6,
s_TE = -2.
```

The T-side constraints do not see `rho`.

### E-center positivity

E-center nonnegativity gives:

```text
1 + rho/6 >= 0,
```

or:

```text
rho >= -6.
```

This leaves a continuum of values, including `rho=0`, `rho=1`,
`rho=2`, and `rho=21/4`.

### Minimal deformation

The shell-normalized center lift differs from the shell by:

```text
q_E(rho)-1 = rho/6.
```

The minimal absolute deformation selector is:

```text
rho = 0,
```

not `21/4`.

### Minimal matrix norm

The reduced map has squared Frobenius norm:

```text
||P(rho)||_F^2 = 1 + rho^2 + 4 + 4 = 9 + rho^2.
```

This is also minimized at:

```text
rho = 0.
```

### Endpoint-chain selector

If one imports:

```text
c_TE = -8/9,
```

then:

```text
c_TE = s_TE q_T / q_E
```

forces `q_E=15/8` and hence `rho=21/4`. But that imports the target endpoint
chain. It is not a direct E-center derivation.

## Current-Surface Boundary

This block proves a scoped no-go:

```text
restricted readout family
+ T-side candidates
+ shell normalization
+ linearity
+ E-center positivity
+ minimal-deformation/minimal-norm selectors
does not select
rho_E = 21/4.
```

The exact positive route left open is:

```text
derive q_E = 15/8 directly
```

or equivalently:

```text
derive the E-center excess q_E - 1 = 7/8.
```

Without such a direct E-center law, the S3/Route-2 coupling remains a
conditional family over admissible readout maps.

## No-Go Discipline

N1 alternative routes:

| Route | Result |
| --- | --- |
| Shell normalization | Leaves `rho_E` free. |
| T-side endpoint constraints | Leaves `rho_E` free. |
| E-center positivity | Leaves continuum `rho_E >= -6`. |
| Minimal center deformation | Selects `rho_E=0`, not `21/4`. |
| Minimal Frobenius norm | Selects `rho_E=0`, not `21/4`. |
| Endpoint-chain selector | Selects `21/4` only by importing the target. |

N2 wall independence:

The direct E-center wall is independent of the source-unit coefficient chain.
It is the missing center lift in the reduced readout map.

N3 hidden-wall scan:

No observed masses, fitted endpoint values, nearest-rational selector,
literature value, or live endpoint measurement is used. The target endpoint
chain is not used as a selector.

N4 residual matching:

The residual matches the S3/Route-2 blocker: the unique coupling theorem is
blocked by the same unselected `E`-center map entry.

N5 rhetoric audit:

"Direct E-center theorem" and "E-center excess" name future theorem premises.
They are not asserted as current Route-2 framework content.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_direct_e_center_selector_boundary_2026_06_22.py
```

Expected final line:

```text
TOTAL: PASS=55, FAIL=0
```
