# Quark Route-2 Color/Covariance Bridge Equivalence Support

**Date:** 2026-06-21
**Claim type:** bounded_theorem
**Claim scope:** bounded support boundary
**Status authority:** independent audit lane only. This source note does not set, claim, or predict an audit outcome.
**Actual current-surface status:** exact support / bridge-equivalence
boundary. This note does not derive `rho_E = 21/4`, does not derive the
typed color bridge, does not derive the typed covariance bridge, and does not
close the `s3_time_theta_to_slice_coupling_note` open gate.
**Primary runner:** [`scripts/frontier_quark_route2_color_covariance_bridge_equivalence_2026_06_21.py`](../scripts/frontier_quark_route2_color_covariance_bridge_equivalence_2026_06_21.py)
**Runner cache:** [`logs/runner-cache/frontier_quark_route2_color_covariance_bridge_equivalence_2026_06_21.txt`](../logs/runner-cache/frontier_quark_route2_color_covariance_bridge_equivalence_2026_06_21.txt)

## Scope

Two positive-looking Route-2 repair routes remain live:

1. derive the typed color/source bridge

   ```text
   c_TE = gamma_T(center)/gamma_E(center) = -F_adj = -8/9;
   ```

2. derive the typed same-domain covariance bridge

   ```text
   lambda = q_E/q_T = kappa^2 = 9/4.
   ```

Existing no-go notes show neither bridge follows from the current bank. This
note adds an exact support fact for future bridge work: under the current
T-side orientation, the two bridge targets are algebraically equivalent. They
are not two independent missing primitives.

## Inputs

Load-bearing authorities:

- [[`QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md`](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md)](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md)
  supplies the endpoint algebra
  `c_TE = s_TE q_T/q_E`, `lambda=q_E/q_T`, and the T-side candidate values.
- [[`OH_SEVEN_SITE_STAR_SHELL_LEVERAGE_POSITIVE_THEOREM_NOTE_2026-06-10.md`](OH_SEVEN_SITE_STAR_SHELL_LEVERAGE_POSITIVE_THEOREM_NOTE_2026-06-10.md)](OH_SEVEN_SITE_STAR_SHELL_LEVERAGE_POSITIVE_THEOREM_NOTE_2026-06-10.md)
  supplies the same-domain star leverage `kappa=3/2`, hence `kappa^2=9/4`,
  while explicitly not deriving a Route-2 readout entry.
- [[`EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md`](EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md)](EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md)
  supplies the exact group-theory color fraction
  `F_adj=(N_c^2-1)/N_c^2`, giving `F_adj=8/9` at `N_c=3`.
- [[`QUARK_ROUTE2_QE_KAPPA_SQUARED_COVARIANCE_SHARPER_NO_GO_NARROW_NOTE_2026-06-10.md`](QUARK_ROUTE2_QE_KAPPA_SQUARED_COVARIANCE_SHARPER_NO_GO_NARROW_NOTE_2026-06-10.md)](QUARK_ROUTE2_QE_KAPPA_SQUARED_COVARIANCE_SHARPER_NO_GO_NARROW_NOTE_2026-06-10.md)
  identifies `lambda=kappa^2` as the missing covariance bridge, not a
  consequence of equivariance.
- [[`QUARK_ROUTE2_RCONN_TYPED_BRIDGE_DERIVATION_BOUNDED_NOTE_2026-06-12.md`](QUARK_ROUTE2_RCONN_TYPED_BRIDGE_DERIVATION_BOUNDED_NOTE_2026-06-12.md)](QUARK_ROUTE2_RCONN_TYPED_BRIDGE_DERIVATION_BOUNDED_NOTE_2026-06-12.md)
  identifies `F_adj -> c_TE=-F_adj` as a missing typed Route-2 center bridge.

Forbidden proof inputs: observed masses, fitted Yukawa values, CKM/J target
minimization, nearest-rational endpoint selection, eta-floor endpoint fitting,
untyped color-to-readout identification, and audit verdicts.

## Exact Bridge Equivalence

Grant the current T-side candidate values:

```text
rho_T = beta_T/alpha_T = -1,
s_TE = alpha_T/alpha_E = -2,
q_T = 1 + rho_T/6 = 5/6.
```

Write

```text
lambda := q_E/q_T.
```

The endpoint algebra gives

```text
c_TE = s_TE q_T/q_E = s_TE/lambda.
```

The same-domain shell-leverage authority gives

```text
kappa = 3/2,
kappa^2 = 9/4.
```

The color/Fierz authority gives

```text
F_adj = (N_c^2-1)/N_c^2 = 8/9  at N_c=3.
```

Under `s_TE=-2`, these constants satisfy

```text
F_adj = -s_TE/kappa^2 = 2/(9/4) = 8/9.
```

Therefore

```text
lambda = kappa^2
<=> c_TE = s_TE/kappa^2
<=> c_TE = -F_adj.
```

When either bridge is supplied, the endpoint chain then gives

```text
q_E = lambda q_T = (9/4)(5/6) = 15/8,
rho_E = 6(q_E - 1) = 21/4.
```

Conversely, supplying the color bridge `c_TE=-F_adj` gives

```text
lambda = s_TE/c_TE = (-2)/(-8/9) = 9/4 = kappa^2.
```

Thus the color bridge and covariance bridge are the same algebraic missing
edge once the current T-side orientation is granted.

## Falsifiers

The equivalence is not numerology over any low rational. It depends on the
specific current inputs:

| Counterfactual | Exact result | Consequence |
|---|---:|---|
| `N_c=2`, keeping `kappa=3/2`, `s_TE=-2` | `F_adj=3/4`, `s_TE/(-F_adj)=8/3` | color bridge no longer equals `lambda=kappa^2`; implied `rho_E=22/3` |
| `kappa=1`, keeping `N_c=3`, `s_TE=-2` | `s_TE/kappa^2=-2` | covariance bridge no longer equals `-F_adj` |
| `s_TE=-1`, keeping `N_c=3`, `kappa=3/2` | `-s_TE/kappa^2=4/9` | color/covariance bridges separate |
| no T-side shell orientation | `c_TE=s_TE/lambda` remains symbolic | the sign and magnitude relation is not fixed |

So the support theorem is exact and conditional: it compresses the two bridge
targets only on the current Route-2 T-side surface.

## What This Adds

Previous packets correctly treated the color and covariance routes as
distinct slots:

```text
c_TE = -F_adj,
lambda = q_E/q_T = kappa^2.
```

This note records the exact algebraic relation between the slots:

```text
c_TE = s_TE/lambda,
F_adj = -s_TE/kappa^2.
```

With `s_TE=-2`, `N_c=3`, and `kappa=3/2`, deriving either typed bridge
derives the other bridge's target value. Future work should therefore not
count these as independent positive routes unless it supplies different typed
semantics for the bridge. The remaining Nature-grade task is one typed
source/readout theorem that justifies this bridge in the Route-2 endpoint
family.

## What Is Not Claimed

- This note does not derive `lambda=kappa^2`.
- This note does not derive `c_TE=-F_adj`.
- This note does not derive `rho_E=21/4`.
- This note does not derive the T-side candidates.
- This note does not identify a color fraction with a Route-2 endpoint ratio
  without a typed bridge.
- This note does not apply or predict an audit verdict.
- This note does not update repo-wide authority surfaces.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_color_covariance_bridge_equivalence_2026_06_21.py
```

Expected summary:

```text
TOTAL: PASS=23, FAIL=0
```
