# Quark Route-2 Measured-Calibration Rescue-Transform Firewall

**Date:** 2026-06-21
**Claim type:** no_go
**Status:** exact current-bank firewall for post-box-scan rescue transforms
of the measured Route-2 E-center calibration. This note does not derive the
Route-2 endpoint triple and does not apply an audit verdict.
**Primary runner:**
[`scripts/frontier_quark_route2_measured_calibration_rescue_transform_firewall_2026_06_21.py`](../scripts/frontier_quark_route2_measured_calibration_rescue_transform_firewall_2026_06_21.py)
**Output:**
[`outputs/frontier_quark_route2_measured_calibration_rescue_transform_firewall_2026_06_21.txt`](../outputs/frontier_quark_route2_measured_calibration_rescue_transform_firewall_2026_06_21.txt)

## Scope

The measured-calibration note located a real stack-internal signal:

```text
q_E(N=15) approx 15/8,
q_T(N=15) approx 5/6,
q_E/q_T approx 9/4.
```

The box-size scan then answered the direct discriminator: this is not the
infinite-volume limit of that measured functional. This block asks the next
narrow question:

> After the box-size scan, can the same measured-calibration cache still rescue
> `q_E=15/8` by a non-fitted bulk/tail transform that does not select `N=15`?

Allowed inputs are the landed measured-calibration note, the landed box-size
scan cache, the exact readout algebra, and exact arithmetic on the cached
values. Forbidden inputs are observed quark masses, endpoint fits, new
functionals, and selecting `N=15` as a proof input.

## Current Cache Facts

The fixed-radius scan gives:

```text
N=11: q_T=+0.90206, q_E=+0.84613
N=13: q_T=+0.87009, q_E=-0.03887
N=15: q_T=+0.83333, q_E=+1.87625
N=17: q_T=-0.19680, q_E=-5.83700
N=19: q_T=-0.81228, q_E=-7.45520
N=21: q_T=-1.31647, q_E=-8.67461
N=25: q_T=-2.08540, q_E=-10.37720
N=29: q_T=-2.65468, q_E=-11.52705
```

Only `N=15` lands near the target chain. The bulk tail `N>=17` is all negative
for both `q_E` and `q_T`, so no positive-weight bulk average of that tail can
return the positive targets `15/8` or `5/6`.

The box-proportional probe-radius limit supplies a different, stable
unit-scale tail:

```text
q_E: +2.708, +0.906, +1.054, +0.981
q_T: +0.958, +0.871, +1.058, +0.976
```

The stable tail stays near unit scale, not the Route-2 target chain.

## Theorem

**Theorem (measured-calibration rescue-transform firewall).** On the current
box-size scan surface, after excluding the anomalous finite point `N=15` as a
proof selector, the measured-calibration cache does not supply the endpoint
chain

```text
q_E = 15/8,
q_T = 5/6,
q_E/q_T = 9/4.
```

Fixed-radius bulk tails have `q_E<0` and `q_T<0`, so the positive target values
are outside their convex hulls. Fixed-radius bulk covariance ratios stay above
`9/4`, not at it. Box-proportional stable tails converge near `(q_E,q_T)=(1,1)`
and their covariance stays near `1`, not `9/4`. Therefore the measured
calibration remains comparator evidence and a falsified finite-box rescue
route, not an exact endpoint primitive.

## What This Moves

This prunes a specific post-scan rescue:

```text
measured N=15 calibration + box-size cache
  -> non-fitted bulk/tail transform
  -> q_E=15/8.
```

The exact positive target remains unchanged. A future positive route must
supply a new E-center-sensitive source/readout primitive, a new physical
tensor observable, or an explicitly approved readout convention. It cannot get
the endpoint from the current measured-calibration cache by bulk averaging,
tail covariance, or same-functional limit extraction.

This note does not claim that every future nonlinear observable fails. It only
closes the current measured-calibration rescue transforms that reuse the
landed box-size scan surface.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_measured_calibration_rescue_transform_firewall_2026_06_21.py
```

Expected result:

```text
TOTAL: PASS=40, FAIL=0
VERDICT: current-box-scan rescue transforms do not recover the Route-2 endpoint from the measured calibration without selecting N=15.
```
