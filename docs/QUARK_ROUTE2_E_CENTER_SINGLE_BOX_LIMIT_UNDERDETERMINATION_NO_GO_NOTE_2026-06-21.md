# Route-2 E-Center Single-Box Limit Underdetermination No-Go Note

**Date:** 2026-06-21
**Claim type:** no_go
**Claim scope:** single-box limit underdetermination no-go for exactifying the measured E-center calibration
**Status authority:** independent audit lane only. This source note does not set, claim, or predict an audit outcome.
**Actual current-surface status:** single-box limit underdetermination no-go for exactifying the measured E-center calibration
**Trace class:** negative_route_pruning
**Reachability to target:** prunes a Route-2 endpoint escape route; does not derive the endpoint triple.
**Primary runner:** [`scripts/frontier_quark_route2_single_box_limit_underdetermination_no_go_2026_06_21.py`](../scripts/frontier_quark_route2_single_box_limit_underdetermination_no_go_2026_06_21.py)
**Runner cache:** [`logs/runner-cache/frontier_quark_route2_single_box_limit_underdetermination_no_go_2026_06_21.txt`](../logs/runner-cache/frontier_quark_route2_single_box_limit_underdetermination_no_go_2026_06_21.txt)
**Authority links:** [QUARK_ROUTE2_E_CENTER_LIFT_MEASURED_CALIBRATION_NARROW_THEOREM_NOTE_2026-06-10.md](QUARK_ROUTE2_E_CENTER_LIFT_MEASURED_CALIBRATION_NARROW_THEOREM_NOTE_2026-06-10.md), [QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md](QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md), [QUARK_E_CHANNEL_ENDPOINT_QUOTIENT_LAW_NOTE_2026-04-19.md](QUARK_E_CHANNEL_ENDPOINT_QUOTIENT_LAW_NOTE_2026-04-19.md)

## Scope

The measured-calibration row is useful support: the stack's own `SIZE=15`
shell-response E-center lift lands near the target fingerprint

```text
q_E = 15/8,    rho_E = 21/4.
```

This note tests a narrower question:

```text
Can that one finite-box value alone certify the exact infinite-volume limit?
```

No.  A single finite-size datum cannot distinguish a law converging to `15/8`
from a nearby law converging to a different exact value.  This does not reject
the measured-calibration route; it states the exact next requirement for that
route.  In short, this does not reject the measured-calibration route.  It
requires a box-size scan, a convergence theorem, or an independent
source/readout derivation.

## Witness Construction

Let the measured `SIZE=15` value be `q_15`.  For any candidate limit `L`, the
finite-size law

```text
q_L(N) = L + (q_15 - L) * 15/N
```

satisfies

```text
q_L(15) = q_15,
lim_{N -> infinity} q_L(N) = L.
```

The runner constructs two such laws:

```text
L_target = 15/8,
L_alt    = 469/250 = 15/8 + 1/1000.
```

Both match the same measured `q_15` exactly.  They have small decaying
`1/N` corrections at the pinned box.  They converge to different exact limits:

```text
rho_target = 6(15/8 - 1) = 21/4,
rho_alt    = 6(469/250 - 1) = 657/125.
```

Thus the single-box datum is support but not an exactification theorem.

## Why This Matters

Block54 made the exact E-center fingerprint checkable.  The measured
calibration nearly hits that fingerprint, but the existing cache contains only
the pinned `SIZE=15` module chain.  Without additional box sizes or a
convergence law, the observed proximity cannot decide between:

- slower E-channel finite-size convergence to `15/8`; and
- convergence to a nearby value not equal to `15/8`.

The measured-calibration note already names this as the honest caveat.  This
packet turns the caveat into an executable no-go witness.

## Claim Status

Actual current surface status: `no-go` for single-box exactification.

Trace class: `negative_route_pruning`.

Reachability: prunes the route that treats the single measured calibration
point as an exact infinite-volume derivation.  It does not close or reject the
measured-calibration program.

## Runner Certificate

Expected local certificate:

```text
TOTAL: PASS=45 FAIL=0
```
