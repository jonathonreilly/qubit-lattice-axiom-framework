# Quark Route-2 Rconn Signed Center-Bridge Selector Firewall

**Date:** 2026-06-21
**Claim type:** no_go
**Claim scope:** no_go
**Status authority:** independent audit lane only. This source note does not set, claim, or predict an audit outcome.
**Actual current-surface status:** exact current-bank selector firewall for the signed `R_conn`
**Trace class:** negative_route_pruning
**Reachability to target:** prunes a Route-2 endpoint escape route; does not derive the endpoint triple.
**Primary runner:** [`scripts/frontier_quark_route2_rconn_signed_center_bridge_selector_firewall_2026_06_21.py`](../scripts/frontier_quark_route2_rconn_signed_center_bridge_selector_firewall_2026_06_21.py)
**Runner cache:** [`logs/runner-cache/frontier_quark_route2_rconn_signed_center_bridge_selector_firewall_2026_06_21.txt`](../logs/runner-cache/frontier_quark_route2_rconn_signed_center_bridge_selector_firewall_2026_06_21.txt)
**Authority links:** [RCONN_DERIVED_NOTE.md](RCONN_DERIVED_NOTE.md), [EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md](EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md), [QUARK_ROUTE2_RCONN_TYPED_BRIDGE_DERIVATION_BOUNDED_NOTE_2026-06-12.md](QUARK_ROUTE2_RCONN_TYPED_BRIDGE_DERIVATION_BOUNDED_NOTE_2026-06-12.md), [QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md](QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md), [QUARK_ROUTE2_RCONN_CENTER_RATIO_BRIDGE_OBSTRUCTION_NOTE_2026-04-28.md](QUARK_ROUTE2_RCONN_CENTER_RATIO_BRIDGE_OBSTRUCTION_NOTE_2026-04-28.md), [CTE_RCONN_SPATIAL_TENSOR_COLOR_BRIDGE_IS_A_CROSS_DOMAIN_COINCIDENCE_NARROW_NO_GO_NOTE_2026-06-08.md](CTE_RCONN_SPATIAL_TENSOR_COLOR_BRIDGE_IS_A_CROSS_DOMAIN_COINCIDENCE_NARROW_NO_GO_NOTE_2026-06-08.md), [RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08.md](RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08.md), [QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md), [S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md), [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md)

center bridge. This note does not derive the Route-2 endpoint triple and does
not apply an audit verdict.
## Scope

The s3-time Route-2 parent row remains blocked by the upstream readout endpoint
triple

```text
(beta_T / alpha_T, alpha_T / alpha_E, beta_E / alpha_E)
  = (-1, -2, 21/4).
```

After the granted T-side values, the exact endpoint algebra says that the
E-side target is equivalent to

```text
c_TE := gamma_T(center) / gamma_E(center) = -8/9.
```

The tempting route is to reuse the exact SU(3) Fierz fraction

```text
F_adj = (N_c^2 - 1) / N_c^2 = 8/9 at N_c = 3
```

as the signed Route-2 center ratio:

```text
c_TE = -F_adj.
```

This note sharpens the current-bank boundary for that route. It separates the
collapsed bridge into the independent selectors a proof must actually supply.

## Minimal Premise Set

Allowed:

1. Exact Route-2 restricted readout algebra.
2. Granted T-side stretch values `beta_T / alpha_T = -1` and
   `alpha_T / alpha_E = -2`.
3. Exact SU(3) Fierz/channel-count support `F_adj = 8/9`.
4. Exact rational arithmetic.
5. Current one-hop notes that explicitly bound the Route-2/readout/`R_conn`
   source bank.

Forbidden:

1. Observed quark masses or measured Yukawa values.
2. CKM/J target minimization.
3. Nearest-rational selection from live endpoint data.
4. Untyped color-to-support identification.
5. Silent sign choice.
6. Silent placement of a color scalar into the Route-2 center slot.
7. A physical connected-trace selector `kappa_EW = 0` unless it is supplied by
   a separate current authority.

## Exact Selector Algebra

With the granted T-side values,

```text
q_T = 5/6,
s_TE = gamma_T(shell) / gamma_E(shell) = -2,
q_E = s_TE q_T / c_TE,
rho_E = beta_E / alpha_E = 6(q_E - 1).
```

Therefore:

```text
c_TE = -8/9  ->  q_E = 15/8   ->  rho_E = 21/4,
c_TE = +8/9  ->  q_E = -15/8  ->  rho_E = -69/4.
```

The minus sign is not cosmetic. The positive `F_adj` value gives the wrong
signed Route-2 lift.

If the proof routes through the physical connected-trace family rather than
the exact Fierz support alone,

```text
R_phys(kappa_EW) = F_adj + kappa_EW (1 - F_adj)
                 = (8 + kappa_EW) / 9.
```

Then the negative-center placement gives

```text
rho_E(kappa_EW) = 6(15 / (8 + kappa_EW) - 1).
```

The target `rho_E = 21/4` occurs only at `kappa_EW = 0`. The current
`Rconn Kappa EW Register-Not-Read Color-Trace Open Gate` note explicitly does
not supply that selector.

## Three Independent Selectors

The collapsed bridge

```text
F_adj = 8/9  ->  c_TE = -8/9
```

contains three independent choices:

| Selector | Needed statement | Why it is load-bearing |
|---|---|---|
| Domain functor | A SU(3) color-channel scalar is a Route-2 support-center readout ratio. | Without this, `F_adj` remains a color/Fierz support value, not a Route-2 endpoint object. |
| Sign/orientation | The Route-2 center ratio uses the negative orientation. | Positive placement gives `rho_E = -69/4`, not `21/4`. |
| Center-slot placement | The scalar is assigned to `c_TE = gamma_T(center)/gamma_E(center)`. | Placing `8/9` in `q_E`, `rho_E`, shell ratio, or another slot does not yield the target law. |

A fourth selector is required only for the physical `R_conn` route:

| Selector | Needed statement |
|---|---|
| Physical trace weight | `kappa_EW = 0`, so the physical connected-trace readout equals the exact Fierz adjoint fraction. |

The exact Fierz authority supplies the number `8/9`; it does not supply these
selectors. The Route-2 readout authority supplies the center algebra; it does
not import the color scalar. The current source-domain notes explicitly keep
the bridge as missing.

## Current-Bank Firewall

The current bank supplies:

1. Exact `F_adj = 8/9` support from the SU(3) Fierz/channel-count surface.
2. Exact Route-2 endpoint algebra showing that a supplied `c_TE = -8/9` would
   force `rho_E = 21/4`.
3. A typed-edge inventory and quote-anchored sweep in which the direct
   `R_conn -> c_TE` bridge remains absent.
4. A physical `kappa_EW` open gate that keeps the connected-trace selector
   separate from the exact Fierz fraction.
5. A cross-domain warning: the visible `c_TE` object is a Route-2 spatial
   support-center ratio, while `F_adj` is a fiber/color channel-count
   fraction.

The bank does not supply all required selectors. Therefore the collapsed
signed-center bridge is a current-bank no-go, not an endpoint-triple
derivation.

## Theorem

**Theorem (signed center-bridge selector firewall).** On the current
Route-2/readout/`R_conn` authority bank, after granting the T-side values
`beta_T / alpha_T = -1` and `alpha_T / alpha_E = -2`, the exact support value
`F_adj = 8/9` implies `rho_E = 21/4` only if all of the following extra
selectors are supplied:

1. a typed domain functor from the SU(3) color/Fierz scalar to a Route-2
   support-center readout ratio;
2. a negative sign/orientation selector;
3. placement of the scalar specifically in the `c_TE` center-ratio slot; and
4. if using physical `R_conn` rather than exact `F_adj`, a separate
   `kappa_EW = 0` physical trace-weight selector.

The current authority bank supplies the exact `8/9` support and the exact
conditional endpoint algebra, but it does not supply the selector package
above. Thus the signed `R_conn` center bridge remains an open target and the
color route is pruned as a current-bank derivation of `beta_E/alpha_E = 21/4`.

## What This Moves

This packet does not close the s3-time parent row. It narrows the remaining
Route-2 ambiguity by replacing the single vague bridge label

```text
R_conn -> gamma_T(center)/gamma_E(center) = -R_conn
```

with an explicit selector checklist. Future positive work can now target one
of those selectors directly rather than reusing `8/9` by numerical proximity.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_rconn_signed_center_bridge_selector_firewall_2026_06_21.py
```

Expected result:

```text
TOTAL: PASS=78, FAIL=0
VERDICT: current-bank no-go for the collapsed signed R_conn center bridge.
```
