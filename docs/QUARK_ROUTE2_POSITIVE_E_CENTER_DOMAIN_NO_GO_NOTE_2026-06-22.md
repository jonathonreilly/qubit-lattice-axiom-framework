# Quark Route-2 Positive E-Center Domain No-Go

**Date:** 2026-06-22
**Claim type:** no_go
**Actual current-surface status:** no-go for deriving q_E>0 from the exact reduced readout family
**Trace class:** negative_route_pruning
**Runner:** `scripts/frontier_quark_route2_positive_e_center_domain_no_go_2026_06_22.py`

Actual current-surface status: no-go for deriving q_E>0 from the exact reduced readout family.

## Scope

Block68 used a positive E-center readout domain premise:

```text
q_E > 0.
```

This block asks whether that domain premise is derived by the exact reduced
Route-2 readout family.  It is not.

This is not an audit verdict.  It does not close the parent
[`S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md`](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md)
row.

## Exact Domain Boundary

The exact readout-map reduction gives:

```text
q_E = gamma_E(center) / gamma_E(shell)
q_E = 1 + rho_E/6
rho_E = beta_E / alpha_E.
```

Therefore the positive-domain condition is exactly:

```text
q_E > 0  <=>  rho_E > -6.
```

The boundary is:

```text
rho_E = -6  <=>  q_E = 0.
```

## Non-Uniqueness Witnesses

The same exact reduced readout family admits:

| `rho_E` | `q_E` | Sign/domain |
|---:|---:|---|
| `-7` | `-1/6` | negative |
| `-6` | `0` | ratio boundary |
| `-1` | `5/6` | positive |
| `0` | `1` | positive |
| `21/4` | `15/8` | target positive |

All of these keep the E-shell normalization fixed.  The exact carrier,
shell normalization, and granted T-side candidates do not by themselves
exclude `rho_E <= -6`.

## Relation To Block68

The endpoint sign algebra is:

```text
c_TE = s_TE q_T / q_E.
```

With the conditional T-side values:

```text
s_TE = -2
q_T = 5/6 > 0,
```

the sign of `c_TE` is negative exactly when `q_E > 0`.  So Block68's sign
support is correctly conditional on the positive E-center domain.

## Conditional Rconn Support

Under the oriented Rconn selector ansatz:

```text
c_TE = -R_phys(kappa)
R_phys(kappa) = 8/9 + kappa/9,
q_E = (5/3) / R_phys(kappa),
```

every sampled nonnegative selector in the physical interval gives positive
`q_E`:

| `kappa` | `q_E` | `rho_E` |
|---:|---:|---:|
| `0` | `15/8` | `21/4` |
| `1/2` | `30/17` | `78/17` |
| `1` | `5/3` | `4` |

This is useful conditional support: if the oriented Rconn bridge ansatz and a
nonnegative selector are granted, `q_E>0` follows.  It is not a current-surface
derivation from the exact reduced readout family alone.

## Result

The direct positivity route is blocked:

```text
exact reduced readout family
+ shell normalization
+ granted T-side candidates
=> q_E > 0
```

is not a current-surface theorem.

The exact domain condition is now isolated:

```text
rho_E > -6.
```

The target value `rho_E=21/4` is one positive member of the family, but
positive domain alone leaves many exact non-target values.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_positive_e_center_domain_no_go_2026_06_22.py
```

Expected result:

```text
TOTAL: PASS=42, FAIL=0
```
