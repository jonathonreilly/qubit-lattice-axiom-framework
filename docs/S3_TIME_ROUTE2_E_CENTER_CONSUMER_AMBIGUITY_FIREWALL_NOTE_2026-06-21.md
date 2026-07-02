# S3-Time Route-2 E-Center Consumer Ambiguity Firewall

**Status:** exact-support, consumer-boundary artifact only.  
**Date:** 2026-06-21  
**Primary runner:** [`scripts/frontier_s3_time_route2_e_center_consumer_ambiguity_firewall_2026_06_21.py`](../scripts/frontier_s3_time_route2_e_center_consumer_ambiguity_firewall_2026_06_21.py)  
**Runner cache:** `logs/runner-cache/frontier_s3_time_route2_e_center_consumer_ambiguity_firewall_2026_06_21.txt`  
**Downstream target:** [`S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md`](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md)

## Boundary

This note does not derive `rho_E = 21/4`. It does not close the Route-2
readout endpoint triple, does not update an audit verdict, and is not a unique
exact `Theta_R -> Lambda_R` coupling theorem.

It is a consumer firewall for the already recorded conditional family

```text
Xi_P(t ; c) = (P_R c) tensor V_R(t)
```

on the s3-time arm. Its only claim is the exact support statement below:
the unresolved `rho_E` endpoint can propagate into the downstream consumer only
through the E-channel center-excess carrier coordinate.

No observed masses, fitted targets, PDG values, or phenomenological selectors
enter this note.

## Setup

After the T-side entries are granted, the reduced Route-2 readout family is

```text
P(rho_E) = [[1, 0, rho_E, 0],
            [0, -2, 0, 2]].
```

The restricted carrier coordinates are

```text
c = (u_E, u_T, delta_E, delta_T).
```

The shell/center columns used by the upstream exact readout note are

```text
E-shell  = (1, 0, 0,   0)
E-center = (1, 0, 1/6, 0)
T-shell  = (0, 1, 0,   0)
T-center = (0, 1, 0, 1/6).
```

## Exact Propagation Formula

For any two exact admissible values `rho_a` and `rho_b`,

```text
(P(rho_b) - P(rho_a)) c
  = ((rho_b - rho_a) delta_E, 0).
```

Therefore the downstream coupling difference is

```text
Delta Xi(t ; c)
  = ((rho_b - rho_a) delta_E, 0) tensor V_R(t).
```

This proves the ambiguity is rank-one in the E-readout amplitude and is
supported only by the `delta_E` coordinate. It is not a time-dynamics ambiguity:
the same exact slice factor `V_R(t)` multiplies the readout difference.

## Blind Sector

The following consumers are independent of `rho_E`:

- all carriers with `delta_E = 0`;
- the shell columns `E-shell` and `T-shell`;
- the `T-center` column;
- any downstream post-functional whose E-readout component is zero.

So shell-only and T-only downstream claims can be reused without importing the
missing `rho_E` theorem, provided they do not also use E-center data.

## Sensitive Sector

Any E-readout-sensitive consumer evaluated on a carrier with `delta_E != 0`
distinguishes admissible `rho_E` values.

In particular, for the E-center column,

```text
P(21/4) E-center - P(0) E-center = (7/8, 0),
```

and

```text
q_E(rho_E = 0)    = 1,
q_E(rho_E = 21/4) = 15/8.
```

Thus a unique E-center `Theta_R -> Lambda_R` theorem still needs the missing
endpoint primitive `rho_E = 21/4` or an exactly equivalent current-surface
selection principle.

## Relation to the Parent Consumer

[`S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md`](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md)
already records the exact conditional family and names the missing readout-map
endpoint triple as the blocker for uniqueness.

This firewall sharpens that parent boundary:

- the unresolved endpoint does not contaminate the slice semigroup;
- it does not contaminate shell-only or T-only consumer statements;
- it does contaminate E-center-sensitive coupling statements exactly through
  `delta_E`;
- therefore the parent row remains open for the unique theorem while its
  `rho_E`-blind subclaims have an exact support certificate.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_s3_time_route2_e_center_consumer_ambiguity_firewall_2026_06_21.py
```

Expected result:

```text
PASS=12 FAIL=0
```
