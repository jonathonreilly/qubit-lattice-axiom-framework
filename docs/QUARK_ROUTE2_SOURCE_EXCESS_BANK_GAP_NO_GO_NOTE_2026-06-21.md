# Quark Route-2 Source-Excess Bank Gap No-Go

**Date:** 2026-06-21
**Actual current-surface status:** bounded current-bank no-go for the source-excess target
**Trace class:** negative_route_pruning
**Runner:** `scripts/frontier_quark_route2_source_excess_bank_gap_no_go_2026_06_21.py`

Actual current-surface status: bounded current-bank no-go for the source-excess target.

## Scope

This block continues the S3/Route-2 endpoint campaign after isolating the
normalized center-excess source target. The exact target is:

```text
b_E/a_E = 7/2.
```

This is not an audit verdict and does not resolve the parent gate
`S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md`. It asks only whether the named
current Route-2 source/readout bank already contains a typed source-excess
primitive deriving that target.

## Named Current Bank

The checked bank is intentionally narrow and current-surface:

- `S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md`
- `QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md`
- `QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md`
- `QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md`
- `S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md`
- `scripts/frontier_quark_route2_qe_covariance_schur_quadratic_no_go_2026_06_14.py`
- `scripts/frontier_quark_route2_source_domain_bridge_no_go.py`

This bank contains the support carrier, the restricted readout family, the
endpoint algebra, the Schur one-power/inverse-square gap, and the existing
source-domain bridge no-go.

## Exact Target

The one-power readout premise gives:

```text
q_E/q_T = (w_E/w_T)^-1 = 3/2.
```

With `q_T = 5/6`, this gives:

```text
q_E = 5/4
rho_E = beta_E/alpha_E = 3/2.
```

The final endpoint target requires:

```text
rho_E' = 21/4.
```

Therefore the normalized E-only source-excess theorem would need:

```text
b_E/a_E = (21/4)/(3/2) = 7/2.
```

## Current-Bank Gap

The current named bank does not contain a typed source-excess primitive for
this target. In particular, the runner checks that the bank does not name:

```text
b_E/a_E
source-excess
S_dual
diag(a_E, ...)
7/2
```

as a source-preparation theorem or typed source primitive.

The typed graph also has no edge from the current source-side nodes
`delta_A1`, `u_E/u_T`, `K_R`, `schur_weights`, or the configured
`source_domain_bank` to the target node
`source_excess_tilt_7_2`.

Adding a future theorem

```text
typed_source_excess_theorem -> source_excess_tilt_7_2
```

would create that reachability immediately. That edge is precisely the missing
source theorem; it is not present in the current bank.

## Boundary

The pruned shortcut is:

```text
current named Route-2 source/readout bank
  => typed E-only source-excess tilt b_E/a_E = 7/2.
```

The implication is not present. This block does not say such a theorem cannot
be added. It says the current named bank does not already supply it.

The next route is either:

1. add a new typed source-excess theorem for `b_E/a_E = 7/2`; or
2. move to the readout-only inverse-square coefficient route.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_excess_bank_gap_no_go_2026_06_21.py
```

Expected result:

```text
TOTAL: PASS=60, FAIL=0
```
