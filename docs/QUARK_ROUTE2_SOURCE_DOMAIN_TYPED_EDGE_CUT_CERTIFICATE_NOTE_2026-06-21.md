# Quark Route-2 Source-Domain Typed-Edge Cut Certificate

**Date:** 2026-06-21
**Claim type:** no_go
**Claim scope:** exact negative boundary / typed-edge cut certificate
**Status authority:** independent audit lane only. This source note does not set, claim, or predict an audit outcome.
**Primary runner:** [`scripts/frontier_quark_route2_source_domain_typed_edge_cut_certificate_2026_06_21.py`](../scripts/frontier_quark_route2_source_domain_typed_edge_cut_certificate_2026_06_21.py)
**Runner cache:** [`logs/runner-cache/frontier_quark_route2_source_domain_typed_edge_cut_certificate_2026_06_21.txt`](../logs/runner-cache/frontier_quark_route2_source_domain_typed_edge_cut_certificate_2026_06_21.txt)
**Primary parents:**
[`QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md`](QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md),
[`QUARK_ROUTE2_RCONN_TYPED_BRIDGE_DERIVATION_BOUNDED_NOTE_2026-06-12.md`](QUARK_ROUTE2_RCONN_TYPED_BRIDGE_DERIVATION_BOUNDED_NOTE_2026-06-12.md),
[`QUARK_ROUTE2_E_CENTER_LIFT_DERIVATION_ATTEMPT_BOUNDED_NOTE_2026-06-12.md`](QUARK_ROUTE2_E_CENTER_LIFT_DERIVATION_ATTEMPT_BOUNDED_NOTE_2026-06-12.md),
[`QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md`](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md),
[`QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md`](QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md),
[`RCONN_DERIVED_NOTE.md`](RCONN_DERIVED_NOTE.md),
[`RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08.md`](RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08.md)

## Scope

This note records a typed-edge cut certificate for the remaining
source-domain E-center rule in Route-2.

It does not select the E-center readout entry. Instead it identifies the exact
typed landing edge that a future positive theorem must supply. The current
quote-derived typed inventory has no path from

```text
su3_R_conn_8_9
```

to any of the Route-2 E-center readout nodes

```text
route2_center_TE_minus_8_9
route2_q_E_15_8
route2_rho_E_21_4.
```

The runner checks that scalar-only, sign-only, physical-selector-only, and
slot-existence additions still fail unless an edge lands in the Route-2
readout domain.

## Minimal typed-edge cut

Let the base edge bank be

```text
CURRENT_TYPED_EDGES + DERIVED_ADDITIONAL_EDGES
```

from `scripts/frontier_quark_route2_source_domain_bridge_no_go.py`.

The base bank contains:

- exact Route-2 support/carrier/readout edges;
- exact endpoint algebra edges;
- the granted T-side candidate edge;
- the exact SU(3) color-channel edge to `su3_R_conn_8_9`;
- reverse endpoint algebra edges derived from the current authority bank.

The base bank does not contain:

```text
su3_R_conn_8_9 -> route2_center_TE_minus_8_9.
```

Adding exactly that edge is the existing `MISSING_BRIDGE` object. Once added,
endpoint algebra gives the downstream path

```text
su3_R_conn_8_9
  -> route2_center_TE_minus_8_9
  -> route2_q_E_15_8
  -> route2_rho_E_21_4.
```

Thus the missing mathematical object is not another rational scan. It is a
typed source-domain rule that lands in a Route-2 E-center readout node.

## Equivalent discharge edges

There are three equivalent one-edge discharge forms, depending on which
Route-2 readout node the theorem targets:

| Edge | Meaning |
|---|---|
| `direct typed center-ratio bridge` | `su3_R_conn_8_9 -> route2_center_TE_minus_8_9` |
| `direct typed E-center lift bridge` | `su3_R_conn_8_9 -> route2_q_E_15_8` |
| `direct typed readout-entry bridge` | `su3_R_conn_8_9 -> route2_rho_E_21_4` |

All three are Route-2 typed readout statements. They differ only by where the
exact endpoint algebra is applied.

## Weak additions that still fail

The runner tests these tempting weaker additions and confirms that each still
has no path from `su3_R_conn_8_9` to `route2_rho_E_21_4`:

| Addition | Why it fails |
|---|---|
| `positive scalar only` | `+8/9` as an untyped scalar is not the signed Route-2 center ratio. |
| `signed scalar only` | `-8/9` as an untyped scalar is not yet `c_TE`. |
| `physical selector only` | A connected-trace selector is not a Route-2 center endpoint ratio. |
| `T-side sign only` | The granted T-side orientation does not supply the E-center magnitude. |
| `center slot only` | Knowing that a center-ratio slot exists does not supply its value. |
| `wrong signed typed bridge` | A `+8/9` Route-2 center ratio gives the wrong E-center entry. |

This is the cut: a proof must not merely produce the number `8/9`; it must
type the number into the Route-2 E/T center readout.

## Two-edge scalarization split

The direct missing bridge can be decomposed into two smaller premises:

```text
su3_R_conn_8_9 -> scalar_signed_minus_8_9
scalar_signed_minus_8_9 -> route2_center_TE_minus_8_9.
```

The first edge is a scalarization/sign edge. The second edge is the actual
typecast into the Route-2 readout domain.

The runner checks:

- the signed scalar edge alone fails;
- the typecast edge alone fails;
- the pair succeeds;
- the positive-scalar plus wrong-signed typecast does not reach the target.

Therefore the deep source-domain target can be stated precisely:

> supply a source-domain E-center rule that either directly lands in a Route-2
> readout node, or supplies both the signed scalarization and the Route-2
> typecast.

## Exact arithmetic boundary

The arithmetic downstream of the cut is already exact. With

```text
F_adj = (N_c^2 - 1) / N_c^2 = 8/9
```

and the granted T-side values

```text
q_T = 5/6,
s_TE = -2,
```

the signed center bridge gives

```text
c_TE = -F_adj = -8/9,
q_E = s_TE q_T / c_TE = 15/8,
rho_E = 6(q_E - 1) = 21/4.
```

Using the positive sign instead gives a different Route-2 readout entry:

```text
c_TE = +8/9,
rho_E = -69/4.
```

So the sign and the typed landing edge are both load-bearing.

## Handoff

For the next deep run, do not spend effort on a fresh numeric match to `8/9`
or a fresh endpoint-ratio scan. The useful target is a source-domain E-center
rule in one of these forms:

```text
su3_R_conn_8_9 -> route2_center_TE_minus_8_9
su3_R_conn_8_9 -> route2_q_E_15_8
su3_R_conn_8_9 -> route2_rho_E_21_4
```

or the two-edge scalarization split above. Anything weaker remains support or
context, not a current-surface readout theorem.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_domain_typed_edge_cut_certificate_2026_06_21.py
```

The runner checks source-note anchors, exact rational arithmetic, graph
reachability, weak-addition failures, two-edge scalarization behavior, and the
note inventory.

Expected branch result:

```text
TOTAL: PASS=53, FAIL=0
VERDICT: current source-domain work is blocked exactly at the typed Route-2 readout landing edge.
```
