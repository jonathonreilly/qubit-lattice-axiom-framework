# Quark Route-2 Nonlinear Log-Curvature Readout Candidate Note

**Date:** 2026-06-21
**Claim type:** bounded_theorem
**Claim scope:** conditional support / open primitive target
**Status authority:** independent audit lane only. This source note does not set, claim, or predict an audit outcome.
**Actual current-surface status:** conditional support / open primitive target
**Trace class:** open_gate_boundary
**Reachability to target:** supports the open Route-2 endpoint by isolating a bounded source/readout condition; does not derive the endpoint triple.
**Primary runner:** [`scripts/frontier_quark_route2_nonlinear_log_curvature_readout_2026_06_21.py`](../scripts/frontier_quark_route2_nonlinear_log_curvature_readout_2026_06_21.py)
**Runner cache:** [`logs/runner-cache/frontier_quark_route2_nonlinear_log_curvature_readout_2026_06_21.txt`](../logs/runner-cache/frontier_quark_route2_nonlinear_log_curvature_readout_2026_06_21.txt)
**Authority links:** [QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md), [S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md), [QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md](QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md), [QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md](QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md)

## Claim Boundary

Block81 isolated the exact missing exponent for a pure Route-2 channel law:

```text
C_X proportional to w_X^-2.
```

This block tests a concrete nonlinear primitive that would produce that law:

```text
Phi_X(w_X) = -log(w_X),
d^2 Phi_X / dw_X^2 = 1/w_X^2.
```

For the Route-2 channel weights

```text
w_E = 1/3,
w_T1 = 1/2,
```

the log-barrier Hessian gives

```text
lambda = (w_E^-2)/(w_T1^-2) = 9/4.
```

With the granted T-side candidates, this returns

```text
q_E = 15/8,
rho_E = 21/4,
c_TE = -8/9.
```

So this is a real positive candidate: a Route-2 log-barrier curvature readout
would supply exactly the second-dual law identified by block81.

## Candidate Comparison

The runner compares four nonlinear/readout curvatures:

| Candidate | Curvature ratio | Endpoint status |
|---|---:|---|
| quadratic Hessian | `1` | misses |
| entropy Hessian `d^2(w log w)` | `3/2` | misses |
| log-barrier Hessian `d^2(-log w)` | `9/4` | target |
| reciprocal Hessian `d^2(1/w)` | `27/8` | misses |

This distinguishes the needed primitive sharply. Ordinary quadratic or entropy
curvature is not enough; the exact target is the log-barrier/second-dual
curvature.

## Current-Bank Firewall

This block does not claim current-surface closure. The checked Route-2 bank
does not supply:

- a positive-channel log-barrier action on `O_h` channel weights;
- a variational principle saying the readout coefficient is the channel-weight
  Hessian of that action;
- a proof that this Hessian is the same object as the E-center readout lift.

Those are now the concrete future theorem targets. Until one is supplied, the
parent [S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md) remains open.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_nonlinear_log_curvature_readout_2026_06_21.py
```

Expected result:

```text
TOTAL: PASS=18, FAIL=0
```
