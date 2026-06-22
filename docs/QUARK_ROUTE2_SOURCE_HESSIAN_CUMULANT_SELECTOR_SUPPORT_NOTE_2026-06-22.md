# Quark Route-2 Source-Hessian Cumulant Selector Support

**Date:** 2026-06-22
**Claim type:** bounded_support
**Actual current-surface status:** conditional-support for source-Hessian connected-cumulant selector
**Trace class:** upstream_support
**Runner:** `scripts/frontier_quark_route2_source_hessian_cumulant_selector_support_2026_06_22.py`

Actual current-surface status: conditional-support for source-Hessian
connected-cumulant selector.

## Scope

The remaining Route-2 bridge blocker can be written as:

```text
kappa = 0.
```

Blocks71-75 prune routes that try to get this selector from full-trace
exclusion, local-current controls, generated typed-edge inventory, or the
graph-first SU(3) spatial/color bridge.  This block packages the positive
source/readout algebra behind the remaining route:

```text
read the connected source Hessian D^2 log Z.
```

No endpoint value is used.  The block does not import `rho_E`, a live
comparator, or a fitted E-center value.

This is not an audit verdict.  It does not resolve the parent
[`S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md`](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md)
row.

## Exact Cumulant Identity

For a source-coupled partition functional `Z[J]`, set:

```text
W[J] = log Z[J].
```

At zero source with `Z[0]=1`, the source Hessian is:

```text
D_i D_j W = D_i D_j Z - (D_i Z)(D_j Z).
```

Thus `D^2 log Z` subtracts factorizable disconnected products exactly.

In the two-channel Route-2 notation:

```text
F_adj = 8/9
F_singlet = 1/9.
```

If the singlet term is the one-point product:

```text
(D_i Z)(D_j Z) = 1/9,
```

then the raw moment Hessian reads:

```text
D_i D_j Z = 8/9 + 1/9 = 1,
```

while the connected source Hessian reads:

```text
D_i D_j log Z = 8/9.
```

That is exactly the `kappa=0` selector.

## Singlet-Purity Boundary

The theorem is conditional because connected cumulants subtract only the
factorizable disconnected product.  If the singlet channel has a connected
residual fraction `eta`, then:

```text
R_cumulant(eta) = 8/9 + eta/9.
```

So:

| Singlet typing | `eta` | `kappa` |
|---|---:|---:|
| Pure disconnected product | `0` | `0` |
| Half connected singlet residual | `1/2` | `1/2` |
| Pure connected singlet residual | `1` | `1` |

Therefore `D^2 log Z` forces `kappa=0` only after the Route-2 singlet term is
typed as a pure disconnected product for the same source/readout.

## Typed Reachability

The source/readout graph has two different Hessians:

```text
source_partition_Z -> raw_moment_hessian -> kappa=1
source_partition_Z -> log_generating_function_W -> connected_source_hessian
```

The connected source Hessian gives:

```text
connected_source_hessian -> kappa=eta_singlet_residual.
```

To reach the exact selector, the bank still needs:

```text
Route-2 physical readout is the connected source Hessian
pure-disconnected singlet identification
```

With those primitives:

```text
connected_source_hessian
+ pure-disconnected singlet identification
=> kappa=0.
```

Without them, the source-Hessian algebra is exact support, not a current-surface
derivation of the physical selector.

## Result

This block narrows the missing selector theorem:

```text
derive kappa=0
```

becomes:

```text
1. type the Route-2 physical readout as D^2 log Z for the relevant source;
2. type the 1/9 singlet term as a pure disconnected product for that source.
```

The exact cumulant algebra is closed.  The current packet still does not derive
the missing physical readout primitive.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_hessian_cumulant_selector_support_2026_06_22.py
```

Expected result:

```text
TOTAL: PASS=49, FAIL=0
```
