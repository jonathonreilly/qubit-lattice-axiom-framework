# Quark Route-2 E-Center Inverse-Square Source-Law Firewall

**Date:** 2026-06-21
**Claim type:** no_go
**Claim scope:** exact negative boundary / bounded support
**Status authority:** independent audit lane only. This source note does not set, claim, or predict an audit outcome.
**Actual current-surface status:** exact negative boundary / bounded support
**Trace class:** negative_route_pruning plus upstream_support
**Reachability to target:** prunes a Route-2 endpoint escape route; does not derive the endpoint triple.
**Primary runner:** [`scripts/frontier_quark_route2_e_center_inverse_square_source_law_firewall_2026_06_21.py`](../scripts/frontier_quark_route2_e_center_inverse_square_source_law_firewall_2026_06_21.py)
**Runner cache:** [`logs/runner-cache/frontier_quark_route2_e_center_inverse_square_source_law_firewall_2026_06_21.txt`](../logs/runner-cache/frontier_quark_route2_e_center_inverse_square_source_law_firewall_2026_06_21.txt)
**Authority links:** [QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md), [QUARK_ROUTE2_E_CENTER_LIFT_DERIVATION_ATTEMPT_BOUNDED_NOTE_2026-06-12.md](QUARK_ROUTE2_E_CENTER_LIFT_DERIVATION_ATTEMPT_BOUNDED_NOTE_2026-06-12.md), [QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md](QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md), [QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md](QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md), [QUARK_ROUTE2_E_CENTER_LIFT_MEASURED_CALIBRATION_NARROW_THEOREM_NOTE_2026-06-10.md](QUARK_ROUTE2_E_CENTER_LIFT_MEASURED_CALIBRATION_NARROW_THEOREM_NOTE_2026-06-10.md), [QUARK_ROUTE2_QE_BOX_SIZE_SCAN_CLOSES_BULK_LIMIT_HATCH_NARROW_THEOREM_NOTE_2026-06-10.md](QUARK_ROUTE2_QE_BOX_SIZE_SCAN_CLOSES_BULK_LIMIT_HATCH_NARROW_THEOREM_NOTE_2026-06-10.md), [QUARK_ROUTE2_QE_KAPPA_SQUARED_COVARIANCE_SHARPER_NO_GO_NARROW_NOTE_2026-06-10.md](QUARK_ROUTE2_QE_KAPPA_SQUARED_COVARIANCE_SHARPER_NO_GO_NARROW_NOTE_2026-06-10.md), [QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md](QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md), [OH_SEVEN_SITE_STAR_SHELL_LEVERAGE_POSITIVE_THEOREM_NOTE_2026-06-10.md](OH_SEVEN_SITE_STAR_SHELL_LEVERAGE_POSITIVE_THEOREM_NOTE_2026-06-10.md), [QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md](QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md), [ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md](ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md), [S3_TIME_READOUT_PRIMITIVE_BRIDGE_ASSESSMENT_BOUNDED_NOTE_2026-06-12.md](S3_TIME_READOUT_PRIMITIVE_BRIDGE_ASSESSMENT_BOUNDED_NOTE_2026-06-12.md)

This is not an audit verdict. It is a source-side science
packet for review.

## Scope

This block attacks the direct E-center theorem target for the S3/Route-2
endpoint triple:

```text
q_E = gamma_E(center)/gamma_E(shell) = 15/8
rho_E = beta_E/alpha_E = 21/4.
```

It does not derive that target. It reduces the target to a sharper missing
source/readout theorem and checks that the current named source bank does not
already supply that theorem.

## Minimal Premise Set A_min

Allowed premises:

- the exact restricted Route-2 readout family
  `gamma_E = alpha_E u_E + beta_E delta_A1 u_E` and
  `gamma_T = alpha_T u_T + beta_T delta_A1 u_T`;
- the exact center-excess endpoint step
  `delta_A1(center) - delta_A1(shell) = 1/6`;
- the conditional T-side values
  `beta_T/alpha_T = -1` and `alpha_T/alpha_E = -2`;
- the exact `O_h` seven-site star per-arm weights
  `w_E = 1/3`, `w_T1 = 1/2`, hence `kappa = w_T1/w_E = 3/2`;
- exact rational arithmetic and current source-note markers.

## Forbidden Proof Inputs

Forbidden inputs:

- observed quark masses;
- fitted Yukawa or CKM/J target minimization;
- nearest-rational selection from live endpoint values;
- the N=15 measured E-center proximity as a proof input;
- an untyped color/support identification;
- a new primitive, convention, or owner decision inserted silently.

## Exact Reduction

With the T-side values granted,

```text
rho_T = -1 -> q_T = 5/6,
alpha_T/alpha_E = -2.
```

The E-center target is equivalent to

```text
rho_E = 21/4
q_E = 1 + rho_E/6 = 15/8
q_E/q_T = (15/8)/(5/6) = 9/4
gamma_T(center)/gamma_E(center) = -8/9.
```

The same-domain `O_h` star leverage supplies

```text
w_E = 1/3,
w_T1 = 1/2,
kappa = w_T1/w_E = 3/2,
kappa^2 = 9/4.
```

Therefore the direct E-center target is exactly equivalent to the source/readout
law

```text
q_E/q_T = (w_E/w_T1)^-2.
```

Call this the inverse-square source/readout law.

## Firewall

This block checks the natural law families visible from the current source
bank:

| Candidate law | Exact `q_E/q_T` | Result |
|---|---:|---|
| same lift, `p = 0` | `1` | gives `rho_E = -1` |
| one inverse power, `p = -1` | `3/2` | gives `rho_E = 3/2` |
| inverse-square, `p = -2` | `9/4` | gives `rho_E = 21/4` |
| positive quadratic weight, `p = +2` | `4/9` | wrong channel/value |

For nonnegative projector powers, `w_E/w_T1 = 2/3 < 1`, so the ratio cannot
exceed `1`; it cannot reach `9/4`. A one-power inverse law gives the structural
`3/2` value, not the target. The target requires exactly two inverse powers.

The quadratic `O_h` invariant route does not force this law either: the current
quadratic Schur note records that `Sym^2(perm_6)` has three independent
trivial components, so the E:T1 quadratic ratio is a free reduced-matrix-element
ratio. That can parameterize `9/4`, but it does not derive it.

## Current Source Bank

The runner checks these current surfaces:

- exact readout map: leaves `beta_E/alpha_E` as the missing map entry;
- E-center lift attempt: names the exact E-channel computation as missing;
- E-center blindness no-go: any repair must actually see the E-center column;
- naturality no-go: `rho_E` remains free absent E-center/source/readout input;
- measured calibration: keeps exact infinite-volume identification open;
- box-size scan: rejects the bulk-limit route to `15/8`;
- `kappa^2` sharper no-go: relocates the datum but does not derive the bridge;
- quadratic no-go: no named inverse-square functional exists;
- `O_h` leverage theorem: derives `kappa`, not the readout entry;
- source-domain bridge no-go: keeps the typed color bridge missing;
- record/positivity no-go: fixes norm or bound, not readout direction;
- readout primitive assessment: gives membership but not uniqueness;
- S3 parent/factor-rigidity: localizes ambiguity without selecting `rho_E`.

All of these preserve the same narrow conclusion: the current bank does not
derive the inverse-square source/readout law.

## Stuck Fan-Out

Five frames were checked:

1. Carrier-column frame. E-center-blind constraints are invariant under
   changing `rho_E`.
2. Same-domain leverage frame. `kappa = 3/2` is exact, but `q_E/q_T = kappa^2`
   is an additional bridge.
3. Power-law frame. Only the inverse-square law gives the target.
4. Quadratic Schur frame. Quadratic invariants have a free E:T1 ratio.
5. Current-bank frame. The named source/readout notes classify the
   inverse-square law or an equivalent E-center primitive as missing.

## Boundary

This is not a global impossibility theorem. It does not rule out a future
nonlinear source/readout primitive, an exact tensor endpoint theorem, a typed
color/support bridge, or an explicit owner convention. It says the current
direct E-center source/readout theorem has been sharpened to one missing
mechanism:

```text
derive the inverse-square source/readout law
q_E/q_T = (w_E/w_T1)^-2,
```

or supply an equivalent E-center distinguishing theorem.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_e_center_inverse_square_source_law_firewall_2026_06_21.py
```

Expected result:

```text
TOTAL: PASS=57, FAIL=0
```
