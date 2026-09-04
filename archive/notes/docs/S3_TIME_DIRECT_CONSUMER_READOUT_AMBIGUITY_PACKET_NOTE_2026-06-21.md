# S3-Time Direct-Consumer Readout Ambiguity Packet

**Date:** 2026-06-21
**Claim type:** bounded_theorem
**Claim scope:** exact support / direct-consumer dependency split
**Status authority:** independent audit lane only. This source note does not set, claim, or predict an audit outcome.
**Primary runner:** [`scripts/frontier_s3_time_direct_consumer_readout_ambiguity_packet_2026_06_21.py`](../scripts/frontier_s3_time_direct_consumer_readout_ambiguity_packet_2026_06_21.py)
**Runner cache:** [`logs/runner-cache/frontier_s3_time_direct_consumer_readout_ambiguity_packet_2026_06_21.txt`](../logs/runner-cache/frontier_s3_time_direct_consumer_readout_ambiguity_packet_2026_06_21.txt)
**Primary parents:**
[`S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md`](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md),
[`S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md`](S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md),
[`S3_TIME_READOUT_PRIMITIVE_BRIDGE_ASSESSMENT_BOUNDED_NOTE_2026-06-12.md`](S3_TIME_READOUT_PRIMITIVE_BRIDGE_ASSESSMENT_BOUNDED_NOTE_2026-06-12.md),
[`S3_TIME_PRIMITIVE_CHAIN_NOTE.md`](S3_TIME_PRIMITIVE_CHAIN_NOTE.md),
[`QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md`](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md),
[`QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md`](QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md)

## Scope

This direct-consumer readout ambiguity packet classifies the immediate S3-time
consumers of the Route-2 readout map.

It separates:

- rho_E-blind structural support, which can use the conditional family and
  factor-rigidity statements without selecting the E-center lift; from
- E-center-sensitive consumer claims, which still require a selected readout
  map `P_R`.

This packet does not close the endpoint. It narrows which downstream statements
can safely use the conditional family and which statements remain blocked by
the E-center readout ambiguity.

## Exact Consumer Split

| Consumer | Dependency class | Safe use | Blocked use |
|---|---|---|---|
| `s3_time_theta_to_slice_coupling_note` | `e_center_sensitive_open_gate` | exact conditional family for supplied P_R | unique Theta_R -> Lambda_R law before P_R selection |
| `s3_time_theta_to_slice_coupling_factor_rigidity_note_2026-05-17` | `rho_independent_structural_support` | time-channel universality and rank-1 spatial prefactor localization | endpoint triple selection |
| `s3_time_readout_primitive_bridge_assessment_2026-06-12` | `membership_not_selector` (membership-not-selector) | eta-floor membership in the restricted bright class | physical/canonical readout primitive selection |
| `s3_time_primitive_chain_note` | `p2_readout_map_open` | exact stack through carrier, slice semigroup, and conditional P_R use | final unique readout-to-slice theorem before E-channel entry selection |

## Exact Column Dependence

For the normalized family

```text
P(rho_E) =
[[1, 0, rho_E, 0],
 [0,-2, 0,     2]],
```

and the conditional S3-time consumer

```text
Xi_P(t ; c) = (P_R c) tensor V_R(t),
V_R(t) = exp(-t Lambda_R) u_*,
```

the runner compares `rho_E = 0` with the target-family member.

The exact result is:

| Carrier column | Consumer dependence on `rho_E` |
|---|---|
| `E-shell` | blind |
| `E-center` | sensitive |
| `T-shell` | blind under granted T-side values |
| `T-center` | blind under granted T-side values |

For the E-center witness,

```text
Xi_target(t ; E-center) - Xi_0(t ; E-center)
  = ((P_target - P_0) E-center) tensor V_R(t),
```

so the ambiguity is rank-1 along the time trajectory. The time channel is
shared; the unresolved coordinate is the spatial E-center prefactor.

## Consequence

The direct consumer split is:

1. structural S3-time statements about the conditional family, semigroup, time
   channel, and rank-1 prefactor localization are usable without selecting
   `rho_E`;
2. statements that need a unique `Theta_R -> Lambda_R` law, a physical/canonical
   gate readout, or the final primitive-chain closure still need an E-center
   selector;
3. broad membership of a live affine readout in the restricted bright class is
   not a selector.

The positive target remains one of:

```text
E-center endpoint ratio
source-domain rule
stronger readout-map theorem
```

that selects the E-channel entry of `P_R`.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_s3_time_direct_consumer_readout_ambiguity_packet_2026_06_21.py
```

Expected branch result:

```text
TOTAL: PASS=35, FAIL=0
VERDICT: direct S3-time consumers split into rho_E-blind structural support and E-center-sensitive open claims.
```
