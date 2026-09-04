# Quark Route-2 Reciprocal-Square Dimension Bridge Packet

**Date:** 2026-06-21
**Claim type:** bounded_theorem
**Claim scope:** conditional support plus bridge firewall
**Status authority:** independent audit lane only. This source note does not set, claim, or predict an audit outcome.
**Actual current-surface status:** conditional support plus bridge firewall
**Trace class:** upstream_support
**Reachability to target:** conditionally supports the open Route-2 endpoint by isolating a bridge that would close it; does not derive that bridge or the endpoint triple.
**Primary runner:** [`scripts/frontier_quark_route2_reciprocal_square_dimension_bridge_2026_06_21.py`](../scripts/frontier_quark_route2_reciprocal_square_dimension_bridge_2026_06_21.py)
**Runner cache:** [`logs/runner-cache/frontier_quark_route2_reciprocal_square_dimension_bridge_2026_06_21.txt`](../logs/runner-cache/frontier_quark_route2_reciprocal_square_dimension_bridge_2026_06_21.txt)
**Authority links:** [CKM_WOLFENSTEIN_ETA_INVERSE_SQUARE_GAP_THEOREM_NOTE_2026-04-26.md](CKM_WOLFENSTEIN_ETA_INVERSE_SQUARE_GAP_THEOREM_NOTE_2026-04-26.md), [QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md), [QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md](QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md), [S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md)

No audit verdict is applied. This note is a source note
for the independent review process.

## Safe Claim

The CKM inverse-square source/atlas packet contains the exact reciprocal-square
components

```text
1/N_pair^2 = 1/4,
1/N_color^2 = 1/9.
```

Their ratio is

```text
(1/4)/(1/9) = 9/4.
```

Therefore a bridge identifying the Route-2 readout covariance

```text
lambda := q_E/q_T
```

with the CKM inverse-square component ratio would close the exact Route-2
endpoint target:

```text
lambda = 9/4
q_E = 15/8
rho_E = beta_E/alpha_E = 21/4
c_TE = -8/9.
```

This is real conditional support. It does not make the CKM inverse-square row
a Route-2 readout theorem. It also does not treat the CKM inverse-square packet
as retained input for this Route-2 block: on this `origin/main` snapshot, the
paired CKM runner's retained-tier authority checks do not pass, even though the
exact component arithmetic does. The current bank still lacks the semantic
bridge from CKM inverse-square components to the Route-2 readout coefficient
law.

## Parent Blocker

The parent s3-time row remains blocked by the readout-map endpoint triple

```text
(beta_T / alpha_T, alpha_T / alpha_E, beta_E / alpha_E)
= (-1, -2, 21/4).
```

Under the T-side values, the E-side residual is equivalent to

```text
lambda = q_E/q_T = 9/4.
```

The covariance no-go identifies a future law

```text
q_X proportional to w_X^-2
```

as the sharp missing bridge. This note performs an atlas-reuse stretch: it
asks whether the repo's already-present inverse-square dimension reading can
serve as that law.

## One-Hop Sources

- [[CKM_WOLFENSTEIN_ETA_INVERSE_SQUARE_GAP_THEOREM_NOTE_2026-04-26.md](CKM_WOLFENSTEIN_ETA_INVERSE_SQUARE_GAP_THEOREM_NOTE_2026-04-26.md)](CKM_WOLFENSTEIN_ETA_INVERSE_SQUARE_GAP_THEOREM_NOTE_2026-04-26.md)
  packages the CKM-side inverse-square reading
  `eta^2 = 1/N_pair^2 - 1/N_color^2`.
- [[QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md)](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md)
  gives the endpoint algebra and the missing `beta_E/alpha_E=21/4` map entry.
- [[QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md](QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md)](QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md)
  identifies the inverse-square projector-weight law as the exact Route-2 gap.
- [[S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md)](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md)
  inherits the unresolved endpoint triple as the s3-time coupling blocker.

## Exact CKM Components

The CKM inverse-square note works with the structural counts

```text
N_pair = 2,
N_color = 3,
N_quark = 6.
```

It then decomposes the CKM CP package as

```text
eta^2 = 1/N_pair^2 - 1/N_color^2 = 5/36,
rho A^2 = 1/N_color^2 = 1/9,
eta^2 + rho A^2 = 1/N_pair^2 = 1/4.
```

Thus the two reciprocal-square components have the exact ratio

```text
(eta^2 + rho A^2)/(rho A^2)
= (1/N_pair^2)/(1/N_color^2)
= (1/4)/(1/9)
= 9/4.
```

That is the same rational value as the Route-2 target `lambda`.

## Conditional Route-2 Closure

If a future theorem supplies the bridge

```text
lambda = q_E/q_T
       = (eta^2 + rho A^2)/(rho A^2),
```

then the Route-2 endpoint algebra gives

```text
q_T = 5/6,
q_E = (9/4)(5/6) = 15/8,
rho_E = 6(q_E - 1) = 21/4,
c_TE = -2 q_T/q_E = -8/9.
```

So this route is exact conditional support for the endpoint triple.

## Firewall

The current repo does not supply the bridge above.

The CKM inverse-square note is scoped to CKM CP-phase bookkeeping and
structural count identities. It does not mention Route-2, `rho_E`, or the
Route-2 readout coefficient law. The usable-values index likewise scopes the
`eta^2` inverse-square row to CKM downstream bookkeeping and source-to-parameter
tables.

Additionally, running
`PYTHONPATH=scripts python3 scripts/frontier_ckm_wolfenstein_eta_inverse_square_gap.py`
on this branch gives `TOTAL: PASS=21, FAIL=7`: the failures are retained-tier
authority checks against the current audit ledger, while the exact arithmetic
checks for `1/4`, `1/9`, `5/36`, and the companion sums pass. This block
therefore uses those components only as algebraic atlas support and conditional
bridge evidence, not as retained Route-2 authority.

Several nearby maps are exact falsifiers:

| Map from CKM package to `lambda` | Result | Status |
|---|---:|---|
| gap only `eta^2` | `5/36` | wrong |
| direct `A^2` | `2/3` | wrong |
| color component alone | `1/9` | wrong |
| pair component alone | `1/4` | wrong |
| component ratio `(1/4)/(1/9)` | `9/4` | conditionally right |

Only the component ratio lands on the target. Therefore the missing theorem is
not "there exists an inverse-square identity somewhere in the CKM atlas." The
missing theorem is a typed semantic bridge from that component ratio to the
Route-2 readout covariance `q_E/q_T`.

## Result

This block sharpens the positive route:

```text
CKM inverse-square components
+ Route-2 endpoint algebra
+ bridge lambda = (1/N_pair^2)/(1/N_color^2)
=> (-1, -2, 21/4).
```

The algebra is exact. The bridge remains open.

Future work must derive the bridge from same-surface Route-2 primitives, admit
it as an explicit readout convention, or replace it with another E-center
source/readout primitive.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_reciprocal_square_dimension_bridge_2026_06_21.py
```

Current expected result:

```text
TOTAL: PASS=35, FAIL=0
```
