# Quark Route-2 Dual-Compliance Current Primitive Gate No-Go Note

**Date:** 2026-06-21
**Claim type:** no_go
**Claim scope:** no_go
**Status authority:** independent audit lane only. This source note does not set, claim, or predict an audit outcome.
**Actual current-surface status:** no-go
**Trace class:** negative_route_pruning
**Reachability to target:** prunes a Route-2 endpoint escape route; does not derive the endpoint triple.
**Primary runner:** [`scripts/frontier_quark_route2_dual_compliance_current_primitive_gate_no_go_2026_06_21.py`](../scripts/frontier_quark_route2_dual_compliance_current_primitive_gate_no_go_2026_06_21.py)
**Runner cache:** [`logs/runner-cache/frontier_quark_route2_dual_compliance_current_primitive_gate_no_go_2026_06_21.txt`](../logs/runner-cache/frontier_quark_route2_dual_compliance_current_primitive_gate_no_go_2026_06_21.txt)
**Authority links:** [S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md](S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md), [S3_TIME_READOUT_PRIMITIVE_BRIDGE_ASSESSMENT_BOUNDED_NOTE_2026-06-12.md](S3_TIME_READOUT_PRIMITIVE_BRIDGE_ASSESSMENT_BOUNDED_NOTE_2026-06-12.md), [ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md](ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md), [QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md](QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md), [QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md)

This is not an audit verdict. It follows the conditional-support block that
showed:

```text
dual-compliance p=2 => rho_E=21/4.
```

This note asks the next question: does the current named primitive bank already
derive or supply that `p=2` premise?

## Result

No. The current primitive bank does not supply the dual-compliance `p=2`
source/readout law.

The checked current primitives are:

| Current primitive class | What it supplies | Why it does not supply `p=2` |
|---|---|---|
| Bilinear `K_R` carrier | Definition-only carrier coordinates | The note explicitly says the physical tensor-primitive bridge is still open. |
| Eta-floor affine map | Endpoint-fitted bright-readout membership | It is membership, not uniqueness, and misses the exact normalized target at exact tolerance. |
| Record/positivity registration | Norm, idempotency, or one-sided positivity conditions | These fix norm or a bound, not the `rho_E` direction. |
| Generic quadratic Oh invariant | Same-domain quadratic invariant family | Schur leaves the E:T reduced-matrix-element ratio free. |

The prior conditional bridge remains useful: if a same-domain primitive proves
`p=2`, the endpoint follows. This block only prunes the shortcut:

```text
the current primitive bank already supplies p=2.
```

## Exact Controls

For a channel law

```text
q_X proportional to w_X^-p
```

on the six-arm Oh support, with `w_E=1/3`, `w_T=1/2`, and `q_T=5/6`, the
tested exponents give:

| `p` | `rho_E` |
|---:|---:|
| `0` | `-1` |
| `1` | `3/2` |
| `-2` | `-34/9` |
| `2` | `21/4` |

Only `p=2` gives the target. The current-bank classes above either select no
exponent or select a wrong control exponent. The `p=2` law is therefore a new
proof obligation, not a recovered fact from the current primitive bank.

## Boundary

This note does not close the parent S3/Route-2 gate. It does not derive the
endpoint triple. It does not prove arbitrary future nonlinear observables impossible, and it does not claim future primitives are impossible.

It narrows the next positive target:

```text
derive a same-domain dual-compliance p=2 primitive,
```

or replace it with a different same-domain source/readout theorem that fixes
the E-center lift.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_dual_compliance_current_primitive_gate_no_go_2026_06_21.py
```

Expected final line:

```text
TOTAL: PASS=52, FAIL=0
```
