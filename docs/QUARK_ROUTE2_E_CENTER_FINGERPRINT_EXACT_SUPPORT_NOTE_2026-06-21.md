# Route-2 E-Center Fingerprint Exact Support Note

**Date:** 2026-06-21
**Claim type:** bounded_theorem
**Claim scope:** exact support for a nonblind E-center acceptance test; not a derivation of the endpoint triple
**Status authority:** independent audit lane only. This source note does not set, claim, or predict an audit outcome.
**Actual current-surface status:** exact support for a nonblind E-center acceptance test; not a derivation of the endpoint triple
**Trace class:** upstream_support
**Reachability to target:** supports the open Route-2 endpoint by isolating a bounded source/readout condition; does not derive the endpoint triple.
**Primary runner:** [`scripts/frontier_quark_route2_e_center_fingerprint_exact_support_2026_06_21.py`](../scripts/frontier_quark_route2_e_center_fingerprint_exact_support_2026_06_21.py)
**Runner cache:** [`logs/runner-cache/frontier_quark_route2_e_center_fingerprint_exact_support_2026_06_21.txt`](../logs/runner-cache/frontier_quark_route2_e_center_fingerprint_exact_support_2026_06_21.txt)
**Authority links:** [QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md), [S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md), [S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md](S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md), [QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md](QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md), [QUARK_ROUTE2_E_CENTER_LIFT_MEASURED_CALIBRATION_NARROW_THEOREM_NOTE_2026-06-10.md](QUARK_ROUTE2_E_CENTER_LIFT_MEASURED_CALIBRATION_NARROW_THEOREM_NOTE_2026-06-10.md), [QUARK_E_CHANNEL_ENDPOINT_QUOTIENT_LAW_NOTE_2026-04-19.md](QUARK_E_CHANNEL_ENDPOINT_QUOTIENT_LAW_NOTE_2026-04-19.md)

## Scope

This packet sharpens the next direct consumer for the S3/Route-2 readout
endpoint triple.  It does not derive

```text
(beta_T/alpha_T, alpha_T/alpha_E, beta_E/alpha_E) = (-1, -2, 21/4).
```

Instead, it records the exact fingerprint any future nonblind E-center
source/readout primitive must supply to close the remaining E-channel gate.

## Exact Fingerprint

With the T-side values granted,

```text
q_T = 5/6,
s_TE = gamma_T(shell)/gamma_E(shell) = -2.
```

For the E-channel,

```text
q_E = gamma_E(center)/gamma_E(shell) = 1 + rho_E/6,
rho_E = beta_E/alpha_E.
```

The target E-center statement is equivalent to all of:

```text
rho_E = 21/4
q_E = 15/8
q_E - 1 = 7/8
q_E/q_T = 9/4
c_TE = gamma_T(center)/gamma_E(center) = -8/9
D_E = rho_E/2 = 21/8
```

The most local readout fingerprint is the E-center contrast

```text
P(21/4) E-center - P(21/4) E-shell = (7/8, 0).
```

In short, the E-center contrast `7/8` is the local acceptance-test scalar.

Equivalently, because the E-center column has center-excess coordinate `1/6`,
the excess derivative is

```text
(7/8)/(1/6) = 21/4.
```

So a proposed nonblind primitive is not enough merely because it sees
E-center.  It must compute this exact `7/8` contrast, or one of the equivalent
fingerprints above.

## Slice-Level Consequence

The s3-time readout-to-slice authority gives the exact conditional family

```text
Xi_P(t; c) = (P_R c) tensor V_R(t).
```

The factor-rigidity note shows that the time factor is shared across all
admissible readouts and that differences localize in the spatial prefactor.
For the E-center carrier column,

```text
Xi_target(t; E-center) - Xi_no-lift(t; E-center)
  = ((7/8, 0) tensor V_R(t)).
```

Thus the same fingerprint is visible at the slice level as a rank-1 amplitude
contrast with componentwise ratio `7/8` against the universal time vector.  A
future exact slice primitive can be checked against this ratio without
re-solving the whole readout family.

## Comparator Firewall

The measured-calibration note reports a stack-internal finite-box E-center lift
near the target.  That remains useful comparator evidence.  It is not used as
a proof input here, and the exact-support statement above does not assert that
the finite-box value extrapolates to `15/8`.

## What This Moves

This packet turns the open nonblind-primitve target into a compact exact
acceptance test:

```text
derive E-center contrast 7/8
  <=> derive q_E=15/8
  <=> derive rho_E=21/4
  <=> derive q_E/q_T=9/4
  <=> derive c_TE=-8/9.
```

What remains open is the derivation of that fingerprint from current source,
readout, color, gravity-metric, or slice primitives.

## Claim Status

Actual current surface status: `exact-support`.

Trace class: `upstream_support`.

Reachability: supports the Route-2 endpoint target by making the next nonblind
E-center theorem checkable.  It does not close the endpoint target, does not
apply an audit verdict, and does not update repo-wide authority surfaces.

## Runner Certificate

The paired runner checks exact rational equivalences, carrier/readout
fingerprints, slice-factor fingerprints, comparator firewalls, trace graph
reachability if the fingerprint is supplied, and source-note wording hygiene.

Expected local certificate:

```text
TOTAL: PASS=60 FAIL=0
```
