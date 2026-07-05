# Quark Route-2 Signed-Cancellation Firewall

**Date:** 2026-06-21
**Claim type:** no_go
**Claim scope:** scoped no-go / conditional support; source-side review packet only
**Status authority:** independent audit lane only. This source note does not set, claim, or predict an audit outcome.
**Actual current-surface status:** scoped no-go / conditional support; source-side review packet only
**Trace class:** negative_route_pruning
**Reachability to target:** prunes a Route-2 endpoint escape route; does not derive the endpoint triple.
**Primary runner:** [`scripts/frontier_quark_route2_signed_cancellation_firewall_2026_06_21.py`](../scripts/frontier_quark_route2_signed_cancellation_firewall_2026_06_21.py)
**Runner cache:** [`logs/runner-cache/frontier_quark_route2_signed_cancellation_firewall_2026_06_21.txt`](../logs/runner-cache/frontier_quark_route2_signed_cancellation_firewall_2026_06_21.txt)
**Authority links:** [ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md](ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md), [QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md](QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md), [QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md](QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md), [QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md](QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md), [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md)

## Scope

This block tests the signed affine escape left after the positive-cone and
density-square primitive packets:

```text
F_X = a / w_X + b.
```

It asks whether a signed one-pole cancellation can reach the Route-2 endpoint

```text
q_E/q_T = 9/4
```

without adding a new signed selector or positivity firewall.

## Exact Signed Fit

With `w_E=1/3` and `w_T=1/2`, the affine ratio is:

```text
F_E/F_T = (3a + b)/(2a + b).
```

Solving

```text
(3a + b)/(2a + b) = 9/4
```

gives:

```text
b = -6a/5.
```

So an exact signed fit exists. For example:

```text
F_X = 1/w_X - 6/5
F_E = 9/5
F_T = 4/5
F_E/F_T = 9/4.
```

The endpoint algebra then gives `q_E=15/8`, `rho_E=21/4`, and `c_TE=-8/9`.

## Firewall

Every nonzero affine one-pole fit requires opposite-sign coefficients. If
`a >= 0` and `b >= 0`, then:

```text
1 <= (3a+b)/(2a+b) <= 3/2,
```

so coefficient-positive affine rules cannot reach `9/4`.

Pointwise positivity of the final responses is weaker: the signed example
above has `F_E>0` and `F_T>0`. Therefore pointwise positivity does not derive
or reject the signed cancellation. A successful route must supply a typed
negative-coefficient selector together with an admissibility firewall.

## Current-Surface Boundary

The current named Route-2 bank does not supply that selector. The runner
quote-anchors:

- record/positivity conditions fix norm or bounds, not the readout direction;
- naturality leaves `rho_E` free without an extra endpoint/source/readout
  primitive;
- E-center blindness requires a real E-center lift or equivalent primitive;
- the minimal Record axiom supplies no signed selector, weighting rule, or
  readout context.

## Claim Boundary

This block does not prove that all signed or nonlinear future readouts are
impossible. It proves:

```text
coefficient-positive affine one-pole source/readout rules cannot reach 9/4,
and the exact signed affine fit requires a new negative-coefficient selector.
```

The signed fit remains conditional support, not current-surface derivation.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_signed_cancellation_firewall_2026_06_21.py
python3 -m py_compile scripts/frontier_quark_route2_signed_cancellation_firewall_2026_06_21.py
```

Expected result:

```text
PASS=92 FAIL=0 TOTAL=92
```
