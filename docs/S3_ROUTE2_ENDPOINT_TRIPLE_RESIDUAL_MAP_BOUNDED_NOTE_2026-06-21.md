# S3 Route-2 Endpoint Triple Residual Map

**Date:** 2026-06-21
**Claim type:** bounded_theorem
**Claim scope:** bounded direct-consumer residual map
**Status authority:** independent audit lane only. This source note does not set, claim, or predict an audit outcome.
**Actual current-surface status:** bounded direct-consumer residual map
**Trace class:** upstream_support plus negative_route_pruning
**Reachability to target:** supports the open Route-2 endpoint by isolating a bounded source/readout condition; does not derive the endpoint triple.
**Primary runner:** [`scripts/frontier_s3_route2_endpoint_triple_residual_map_2026_06_21.py`](../scripts/frontier_s3_route2_endpoint_triple_residual_map_2026_06_21.py)
**Runner cache:** [`logs/runner-cache/frontier_s3_route2_endpoint_triple_residual_map_2026_06_21.txt`](../logs/runner-cache/frontier_s3_route2_endpoint_triple_residual_map_2026_06_21.txt)
**Authority links:** [CTE_RCONN_SPATIAL_TENSOR_COLOR_BRIDGE_IS_A_CROSS_DOMAIN_COINCIDENCE_NARROW_NO_GO_NOTE_2026-06-08.md](CTE_RCONN_SPATIAL_TENSOR_COLOR_BRIDGE_IS_A_CROSS_DOMAIN_COINCIDENCE_NARROW_NO_GO_NOTE_2026-06-08.md), [QUARK_ROUTE2_ELL_E_STRUCTURAL_NARROWING_BOUNDED_NOTE_2026-06-12.md](QUARK_ROUTE2_ELL_E_STRUCTURAL_NARROWING_BOUNDED_NOTE_2026-06-12.md), [QUARK_ROUTE2_ENDPOINT_T_BALANCE_FD_PROVENANCE_AND_STEP_STABILITY_BOUNDED_NOTE_2026-06-11.md](QUARK_ROUTE2_ENDPOINT_T_BALANCE_FD_PROVENANCE_AND_STEP_STABILITY_BOUNDED_NOTE_2026-06-11.md), [QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md), [QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md), [QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md](QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md), [QUARK_ROUTE2_E_CENTER_LIFT_DERIVATION_ATTEMPT_BOUNDED_NOTE_2026-06-12.md](QUARK_ROUTE2_E_CENTER_LIFT_DERIVATION_ATTEMPT_BOUNDED_NOTE_2026-06-12.md), [QUARK_ROUTE2_E_CENTER_LIFT_MEASURED_CALIBRATION_NARROW_THEOREM_NOTE_2026-06-10.md](QUARK_ROUTE2_E_CENTER_LIFT_MEASURED_CALIBRATION_NARROW_THEOREM_NOTE_2026-06-10.md), [QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md](QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md), [QUARK_ROUTE2_QE_BOX_SIZE_SCAN_CLOSES_BULK_LIMIT_HATCH_NARROW_THEOREM_NOTE_2026-06-10.md](QUARK_ROUTE2_QE_BOX_SIZE_SCAN_CLOSES_BULK_LIMIT_HATCH_NARROW_THEOREM_NOTE_2026-06-10.md), [QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md](QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md), [QUARK_ROUTE2_QE_KAPPA_SQUARED_COVARIANCE_SHARPER_NO_GO_NARROW_NOTE_2026-06-10.md](QUARK_ROUTE2_QE_KAPPA_SQUARED_COVARIANCE_SHARPER_NO_GO_NARROW_NOTE_2026-06-10.md)

## Scope

This block is a direct-consumer packet for
[S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md). It does not derive the endpoint
triple and does not close the parent open_gate row. It records the current
finite route2/s3-time/rconn surface bank that mentions the endpoint datum and
maps the exact remaining typed selectors.

This is not an audit verdict. It is a source-side science packet for review.

## Exact Equivalence Class

The upstream parent wants the readout endpoint triple:

```text
(beta_T/alpha_T, alpha_T/alpha_E, beta_E/alpha_E)
  = (-1, -2, 21/4).
```

With the notation

```text
rho_T = beta_T/alpha_T,
mu    = alpha_T/alpha_E,
rho_E = beta_E/alpha_E,
q_X   = 1 + rho_X/6,
c_TE  = gamma_T(center)/gamma_E(center) = mu q_T/q_E,
```

the target is exactly equivalent to:

```text
rho_T = -1,
mu = -2,
rho_E = 21/4,
q_T = 5/6,
q_E = 15/8,
c_TE = -8/9,
q_E/q_T = 9/4.
```

The Schur projector weights also contain the structural value

```text
(w_E/w_T)^-2 = 9/4.
```

The current gap is not the arithmetic. It is a typed selector that turns one
of these exact equivalent forms into a current-surface theorem.

## Candidate Surface Sweep

The runner sweeps current `docs/` and `scripts/` surfaces whose path names
contain route2/s3-time/rconn tokens and whose text mentions one of the endpoint
tokens:

```text
rho_E, 21/4, 15/8, -8/9, beta_E/alpha_E,
gamma_T(center), gamma_E(center).
```

It verifies that the candidate sweep matches the expected finite target-near
surface bank.

Checked marker: candidate sweep matches the expected finite target-near surface bank.

This avoids two bad outcomes:

- claiming the parent row is vague when the residual is already sharply
  localized;
- claiming a closure theorem exists when the current route2/s3-time/rconn
  surfaces instead classify the target as open, bounded, no-go, comparator, or
  conditional.

## Residual Map

The remaining direct-consumer edges are:

| Missing selector | Current witness surface | What it would do |
|---|---|---|
| selected readout row P_R | [QUARK_ROUTE2_T_SIDE_ENDPOINT_THEOREM_ATTEMPT_BOUNDED_NOTE_2026-06-12.md](QUARK_ROUTE2_T_SIDE_ENDPOINT_THEOREM_ATTEMPT_BOUNDED_NOTE_2026-06-12.md) | Select `rho_T=-1` and `mu=-2` rather than merely reproduce them after the row is supplied. |
| E-center lift q_E=15/8 | [QUARK_ROUTE2_E_CENTER_LIFT_DERIVATION_ATTEMPT_BOUNDED_NOTE_2026-06-12.md](QUARK_ROUTE2_E_CENTER_LIFT_DERIVATION_ATTEMPT_BOUNDED_NOTE_2026-06-12.md) | Directly derive `rho_E=21/4` through `q_E=1+rho_E/6`. |
| signed R_conn center bridge | [QUARK_ROUTE2_RCONN_TYPED_BRIDGE_DERIVATION_BOUNDED_NOTE_2026-06-12.md](QUARK_ROUTE2_RCONN_TYPED_BRIDGE_DERIVATION_BOUNDED_NOTE_2026-06-12.md) and [QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md](QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md) | Supply `c_TE=-8/9`, which algebraically forces `q_E=15/8` and `rho_E=21/4` under the T-side values. |
| inverse-square readout coefficient law | [QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md](QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md) | Promote the structural value `9/4` from a Schur projector value to a readout coefficient law. |
| unique physical/admissible readout primitive | [S3_TIME_READOUT_PRIMITIVE_BRIDGE_ASSESSMENT_BOUNDED_NOTE_2026-06-12.md](S3_TIME_READOUT_PRIMITIVE_BRIDGE_ASSESSMENT_BOUNDED_NOTE_2026-06-12.md) | Select one admissible `P_R` for the S3 gate rather than membership in the broad restricted class. |

These edges are not independent mysteries. They are exact equivalent ways to
pin the same residual after the relevant T-side assumptions are supplied. The
runner keeps them separate because each route has a different proof burden.

## What This Adds

This packet is useful for the parent S3-time consumer because it replaces the
single phrase "missing endpoint triple" with a finite residual map:

- the exact conditional slice family already exists;
- the exact readout family already exists;
- factor rigidity already localizes the ambiguity to the spatial prefactor;
- the target arithmetic is exactly closed once any one of the selector edges is
  supplied;
- current target-near route2/s3-time/rconn surfaces do not supply those
  selectors as current-surface theorems.

So the next science target is not another restatement of the parent row. It is
one of the typed selector edges listed above.

## Boundary

This note does not rule out a future theorem. It does not say the endpoint
triple is impossible to derive. It says the current direct-consumer map is now
finite and exact: a reviewer can see which edge would change the parent row and
which existing surfaces only provide bounded, conditional, comparator, or
negative evidence.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_s3_route2_endpoint_triple_residual_map_2026_06_21.py
```

Expected result:

```text
TOTAL: PASS=102, FAIL=0
```
