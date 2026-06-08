# Degenerate Supermetric Sign Algebra Under a Supplied Opposite-Signed Curvature Comparator

**Date:** 2026-06-08
**Claim type:** no_go / bounded comparator-sign algebra
**Status authority:** independent audit lane only. This source note writes no
audit verdict and does not retag any ledger row.
**Primary runner:** [`scripts/frontier_universal_gr_degenerate_supermetric_graviton_sign_no_go.py`](../scripts/frontier_universal_gr_degenerate_supermetric_graviton_sign_no_go.py)
**Runner cache:** [`logs/runner-cache/frontier_universal_gr_degenerate_supermetric_graviton_sign_no_go.txt`](../logs/runner-cache/frontier_universal_gr_degenerate_supermetric_graviton_sign_no_go.txt)

## 2026-06-08 Audit-Boundary Repair

This repair scopes the row to the algebra actually proven in the restricted
packet. The runner assumes a supplied opposite-signed linearized curvature
comparator:

```text
V_trace = -k^2/2,
V_TT    = +k^2/2.
```

It then checks the sign consequence of pairing those comparator signs with a
degenerate trace=shear supermetric. The packet does **not** derive the
Regge/Lichnerowicz potential signs from the framework, and it does **not** prove
that `omega^2 = V/G` is the framework-native dynamical gluing law.

The apparent `b^-2` versus `b^-4` drift is a normalization issue, not an
additional physics claim. The runner uses:

- symbolic DeWitt channel weights at `b^-4` to verify the trace/shear sign
  pattern and the lambda=1 GR control; and
- sign-normalized retained-supermetric weights at `b^-2` for the displayed
  comparator gluing diagnostic.

Only the channel signs and degeneracy are load-bearing in this row.

## Theorem (Bounded Comparator-Sign Algebra)

Given:

1. a degenerate trace=shear supermetric, `G_trace=G_TT=G`, and
2. a supplied opposite-signed comparator pair, `V_trace V_TT < 0`,

then

```text
omega_trace^2 * omega_TT^2 = (V_trace V_TT) / G^2 < 0.
```

Thus no overall normalization sign can make both channels have the same healthy
sign inside this comparator-gluing model. The lambda=1 GR control has opposite
trace/shear fiber signs and therefore does not suffer this specific sign
degeneracy in the runner.

`TOTAL: PASS=6 FAIL=0`.

## What This Establishes

The row establishes a bounded negative boundary: a degenerate trace=shear
supermetric cannot be paired with an opposite-signed comparator curvature pair
through the simple `V/G` gluing law while keeping both channel signs healthy.

It also reproduces the companion TT-kernel diagnostic: the scalar
metric-Hessian is rank-1 longitudinal and leaves TT in the kernel.

## What Remains Open

- Framework-native derivation of the finite-`k` Regge/Lichnerowicz signs.
- Framework-native derivation of the dynamical gluing law.
- Non-ultralocal or higher-order W routes.
- Finite-`k` stress-response routes, including the separate positive bounded
  diagnostics in the universal-GR lane.

## Relation to Inventory

This row sharpens the polarization-frame blocker only under the supplied
comparator-sign model. It does not overturn that blocker and does not rule out
all GR routes. The finite-`k` W/stress route remains a live bypass.

## Honest Auditor Read

The source is a sign-algebra packet. It is correct if the comparator signs and
the simple `V/G` gluing model are supplied, but those inputs are not derived
here. The valid no-go is therefore conditional and local: degenerate
trace=shear fiber signs plus opposite comparator potential signs force opposite
dispersion signs. Nothing broader is claimed.
