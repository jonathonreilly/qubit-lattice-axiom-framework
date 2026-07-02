# Quark Up-Amplitude Scalar-Bypass Firewall

**Date:** 2026-06-21
**Claim type:** no_go
**Claim scope:** exact negative boundary for the scalar-bypass route
**Status authority:** independent audit lane only. This source note does not set, claim, or predict an audit outcome.
**Primary runner:** [`scripts/frontier_quark_up_amplitude_scalar_bypass_firewall_2026_06_21.py`](../scripts/frontier_quark_up_amplitude_scalar_bypass_firewall_2026_06_21.py)
**Runner cache:** [`logs/runner-cache/frontier_quark_up_amplitude_scalar_bypass_firewall_2026_06_21.txt`](../logs/runner-cache/frontier_quark_up_amplitude_scalar_bypass_firewall_2026_06_21.txt)
**Authority links:** [`QUARK_UP_AMPLITUDE_NATIVE_AFFINE_NO_GO_NOTE_2026-04-19.md`](QUARK_UP_AMPLITUDE_NATIVE_AFFINE_NO_GO_NOTE_2026-04-19.md), [`QUARK_UP_AMPLITUDE_TWO_STEP_NATIVE_SCAN_NOTE_2026-04-19.md`](QUARK_UP_AMPLITUDE_TWO_STEP_NATIVE_SCAN_NOTE_2026-04-19.md), [`QUARK_UP_AMPLITUDE_SCALAR_COMPARISON_BRIDGE_NOTE_2026-04-19.md`](QUARK_UP_AMPLITUDE_SCALAR_COMPARISON_BRIDGE_NOTE_2026-04-19.md), [`QUARK_UP_AMPLITUDE_RPSR_MASS_RETENTION_BOUNDARY_NOTE_2026-04-28.md`](QUARK_UP_AMPLITUDE_RPSR_MASS_RETENTION_BOUNDARY_NOTE_2026-04-28.md), [`QUARK_UP_AMPLITUDE_TENSOR_ENDPOINT_RESOLUTION_NOTE_2026-04-19.md`](QUARK_UP_AMPLITUDE_TENSOR_ENDPOINT_RESOLUTION_NOTE_2026-04-19.md), [`QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md`](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md), [`QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md`](QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md), [`S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md`](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md)

## Purpose

The S3/Route-2 readout endpoint is blocked by the selected readout map

```text
(beta_T / alpha_T, alpha_T / alpha_E, beta_E / alpha_E)
= (-1, -2, 21/4).
```

Several current-main quark notes constrain the remaining up-sector scalar
`a_u` without starting from the Route-2 readout family. This block asks the
fallback question directly:

```text
Can the non-Route-2 up-amplitude scalar routes bypass the selected-P_R
ambiguity and determine the endpoint triple?
```

The answer on the current surface is no. The useful output is a sharper
firewall: the scalar routes that avoid `rho_E` are real support, but they do
not select `P_R`; the routes that touch endpoint readout data inherit the
same E-center/readout primitive.

## Firewall theorem

On current `main`, the live up-amplitude and Route-2 readout routes fall into
three classes.

### Class 1: rho_E-free scalar support

These routes constrain a reduced up-amplitude or scalar bridge without using
the Route-2 E-center readout entry:

- native projector/support grammars;
- CKM scalar-comparison bridge;
- STRC/RPSR reduced up-amplitude support.

They are valuable because they compress the scalar search. They do not select
the Route-2 map

```text
P_R = [[alpha_E, 0, beta_E, 0],
       [0, alpha_T, 0, beta_T]].
```

The native grammars still split between refit and anchored optima. The
scalar-comparison bridge gives a narrow `kappa` interval, but its refit and
anchored windows are disjoint. The RPSR surface gives exact reduced-amplitude
support, but still needs a typed edge from reduced amplitude to Yukawa/readout
data before it can affect the selected Route-2 map.

### Class 2: endpoint-readout-sensitive support

The tensor endpoint route uses endpoint-fixed readout coefficients

```text
gamma_E(delta_A1) = a_E + b_E delta_A1
gamma_T(delta_A1) = a_T + b_T delta_A1.
```

This route is closer to the Route-2 obstruction, but it does not bypass it.
The current endpoint data give a bounded slope ratio `|b_E / b_T|`; the
existing tensor endpoint resolution shows that no exact identity
`|b_E / b_T| = sqrt(7)` lands and that the endpoint grammar does not force one
unique anchored denominator.

So this route is endpoint-sensitive support, not a selected-map theorem.

### Class 3: selected-map Route-2 route

The exact Route-2 readout-map reduction already proves that the restricted
bright readout class reduces to one channelwise map. The same reduction also
proves the obstruction:

```text
P(rho_E) = [[1, 0, rho_E, 0],
            [0, -2, 0, 2]]
```

is still a one-parameter exact family after the T-side candidates are granted.
The choices `rho_E = 0` and `rho_E = 21/4` agree on the E-shell carrier but
differ on the E-center carrier. The S3 time-coupling family

```text
Xi_P(t ; c) = (P_R c) otimes exp(-t Lambda_R) u_*
```

therefore remains conditional on selected `P_R`.

## Consequence for the S3 endpoint

The non-Route-2 up-amplitude scalar routes do not retire the endpoint blocker.
They narrow where a future positive route must act.

A positive bypass would need one new typed edge of the form

```text
reduced up-amplitude/scalar support
  -> selected Route-2 P_R
```

or an equivalent first-principles E-center lift deriving

```text
beta_E / alpha_E = 21/4.
```

No such edge is present in the current-main scalar stack.

## What this moves

This block prunes a false continuation route:

```text
independent up-amplitude scalar support
  -> selected S3/Route-2 readout map
```

without a typed amplitude-to-readout theorem.

It also preserves the useful support:

- scalar routes remain useful for reduced quark amplitude structure;
- tensor endpoint routes remain useful for bounded endpoint readout structure;
- Route-2 exact time coupling remains exact once a map is supplied.

The remaining hard target is narrower: derive a real E-center/readout
primitive, or derive a typed bridge from the reduced up-amplitude surface to
the selected Route-2 map.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_up_amplitude_scalar_bypass_firewall_2026_06_21.py
```

Expected result:

```text
TOTAL: PASS=33, FAIL=0
Boundary classification: exact negative boundary for the scalar-bypass route.
```
