# Quark Route-2 Direct E-Center Readout Family No-Go

**Date:** 2026-06-22
**Claim type:** no_go
**Actual current-surface status:** no-go for restricted-family-only E-center selection
**Trace class:** negative_route_pruning
**Runner:** `scripts/frontier_quark_route2_direct_e_center_readout_family_no_go_2026_06_22.py`

Actual current-surface status: no-go for restricted-family-only E-center selection.

## Scope

This block makes the direct E-center theorem attempt requested by the Block65
handoff.  It asks whether the already available restricted Route-2 readout
family itself selects

```text
rho_E := beta_E / alpha_E = 21/4
```

without importing a typed E-center endpoint premise, a typed source-domain
bridge, observed quark data, or a fitted target selector.

This is not an audit verdict.  It does not close the parent
[`S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md`](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md)
row.

## Reduced Family

After the exact carrier reduction and the conditional T-side values are fixed,
the restricted family is

```text
P(rho_E) =
[[1, 0, rho_E, 0],
 [0, -2, 0, 2]].
```

The exact endpoint columns are

```text
E-shell  = (1, 0, 0,   0)
E-center = (1, 0, 1/6, 0)
T-shell  = (0, 1, 0,   0)
T-center = (0, 1, 0, 1/6).
```

The one-dimensional E-center shift

```text
rho_E -> rho_E + tau
```

adds `tau * delta_A1 u_E` to the E readout.  It vanishes on `E-shell`,
`T-shell`, and `T-center`, but moves the `E-center` E image by `tau/6`.

Therefore every proof input invariant under that shift leaves `rho_E` free.
The restricted family has no internal fixed point that selects `21/4`.

## Constraint Classifier

The runner classifies direct constraints on this family:

| Constraint form | Effect | What would select the target |
|---|---|---|
| Carrier split, shell normalization, T-side values | Preserved by `rho_E -> rho_E + tau` | Does not fix `rho_E`. |
| E-center-blind linear or ratio data | Same gauge orbit | Does not fix `rho_E`. |
| Affine E-center equation `a E_center_E + b E_shell_E + c = 0` | Fixes `rho_E` only if `a != 0` | Target iff the equation encodes excess `7/8`. |
| Direct `q_E = 15/8` | Fixes `rho_E = 21/4` | This is the E-center endpoint premise. |
| Direct `c_TE = -8/9` | Fixes `rho_E = 21/4` | This is the typed center-ratio bridge. |
| Direct `rho_E = 21/4` | Fixes the target | This is the target premise itself. |

Any direct constraint that fixes `rho_E` is therefore a non-invariant E-center premise.
At the target point, the following statements are exactly
equivalent:

```text
rho_E = 21/4
q_E = 15/8
e_E := q_E - 1 = 7/8
c_TE = -8/9
```

with the conditional T-side values `q_T = 5/6` and shell `T/E = -2`.

## Result

The direct restricted-family route is blocked:

```text
restricted Route-2 carrier/readout family
+ shell normalization
+ conditional T-side values
+ invariance under the E-center shift
=> no unique rho_E
```

This sharpens the remaining ambiguity.  The next positive target is not another invariant of the restricted family.
It must be one of:

```text
a typed E-center excess theorem e_E = 7/8;
a typed center-ratio bridge c_TE = -8/9;
a direct readout primitive rho_E = 21/4.
```

This block does not rule out those non-invariant E-center premises.  It rules
out the idea that the restricted readout family alone contains a natural
selection theorem for the E-center point.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_direct_e_center_readout_family_no_go_2026_06_22.py
```

Expected result:

```text
TOTAL: PASS=49, FAIL=0
```
