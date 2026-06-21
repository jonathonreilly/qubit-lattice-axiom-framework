# Route-2 Rank-One Carrier Leg-Factorization Boundary

**Date:** 2026-06-21  
**Claim type:** no-go / exact carrier-factorization boundary  
**Actual current-surface status:** no-go  
**Trace class:** negative_route_pruning  
**Reachability to target:** prunes the route that tries to extract the needed
two reciprocal source/readout factors from the current `K_R` carrier
factorization alone.  
**Primary runner:** [`scripts/frontier_quark_route2_rank_one_carrier_leg_factorization_boundary_2026_06_21.py`](../scripts/frontier_quark_route2_rank_one_carrier_leg_factorization_boundary_2026_06_21.py)  
**Runner cache:** `logs/runner-cache/frontier_quark_route2_rank_one_carrier_leg_factorization_boundary_2026_06_21.txt`

## Boundary

This note does not derive `rho_E = 21/4`, does not close the Route-2 endpoint
triple, does not update an audit verdict, and does not claim a unique exact
`Theta_R -> Lambda_R` theorem.

It performs the first-principles leg-level stretch attempt demanded by the
previous blocks: take the current minimal Route-2 bilinear carrier itself and
ask whether its exact source/readout factorization supplies the missing
reciprocal local projector-weight factors.

The answer is narrow and exact. The current `K_R` carrier does have a leg-level
factorization, but it is rank-one and channel-blind:

```text
K_R(q) = [[u_E(q), u_T(q)],
          [delta_A1(q) u_E(q), delta_A1(q) u_T(q)]]
       = [1, delta_A1(q)]^T [u_E(q), u_T(q)].
```

That factorization supplies the same source leg to the `E` and `T1` channels.
It has reciprocal degree zero. It therefore cannot supply the two independent
local Riesz-dual source/readout factors needed for `lambda = 9/4`.

No observed masses, fitted targets, PDG values, nearest-rational selection, or
live endpoint fit is used.

## Minimal Premise Set

Allowed:

1. the class-A carrier definition
   `K_R(q) = [[u_E, u_T], [delta_A1 u_E, delta_A1 u_T]]`;
2. the exact endpoint values `delta_A1(e0)=1/6` and
   `delta_A1(s/sqrt(6))=0`;
3. the six-arm projector weights `w_E=1/3`, `w_T1=1/2`;
4. exact endpoint algebra after the two T-side candidates are granted.

Forbidden:

1. observed quark masses;
2. fitted endpoint values;
3. live endpoint numerical selection;
4. inserting `rho_E = 21/4` as a proof input;
5. treating a physical tensor primitive bridge as already derived.

## Exact Rank-One Factorization

The current carrier is not a hidden two-leg source/readout object. It is the
outer product

```text
a(q) b(q)^T
```

with

```text
a(q) = [1, delta_A1(q)]^T,
b(q) = [u_E(q), u_T(q)]^T.
```

Therefore:

```text
det K_R(q) = 0
```

identically, and every endpoint column is the same source leg multiplied by
the chosen bright coordinate:

```text
E-shell  = [1, 0]^T,
E-center = [1, 1/6]^T,
T-shell  = [1, 0]^T,
T-center = [1, 1/6]^T,
```

after reading the nonzero channel column. The source leg does not distinguish
`E` from `T1`.

## Degree Consequence

The endpoint target requires

```text
lambda = q_E / q_T = 9/4 = (w_T1 / w_E)^2.
```

The `K_R` carrier factorization contributes no channel-dependent reciprocal
projector-weight factor:

```text
a_E(q) = a_T(q) = [1, delta_A1(q)]^T.
```

So the carrier source leg has degree

```text
d_source = 0.
```

The bright row in the current class-A definition uses the named aligned unit
coordinates `u_E` and `u_T`; it also has no built-in `1/w_E` versus `1/w_T1`
normalization. Thus the carrier readout leg has degree

```text
d_bright = 0.
```

The carrier alone therefore predicts only

```text
lambda_K = (w_T1 / w_E)^0 = 1,
q_E = q_T = 5/6,
rho_E = -1,
center T/E = -2.
```

That is the wrong endpoint.

## Relation To The Restricted Readout Map

The exact readout map note adds a separate channelwise linear readout:

```text
P_R = [[alpha_E, 0, beta_E, 0],
       [0, alpha_T, 0, beta_T]].
```

That readout can choose different `E` and `T1` endpoint lifts, but those
coefficients are precisely the unresolved readout-map entries. They are not
derived by the rank-one carrier factorization. In particular, after the T-side
candidates are granted, the missing entry remains

```text
beta_E / alpha_E = 21/4.
```

The rank-one carrier explains why the endpoint problem is localized to the
readout map: the carrier supplies a clean leg factorization, but that
factorization is channel-blind and degree-zero.

## Net

This block retires the route:

```text
current K_R leg factorization alone
  -> two reciprocal local projector-weight factors
  -> rho_E = 21/4.
```

The exact result is instead:

```text
current K_R = common A1 source leg times bright channel row
  -> channel-blind carrier source leg
  -> reciprocal degree zero
  -> no endpoint closure.
```

The remaining positive target is now stricter:

> derive an additional leg-level normalization primitive outside the class-A
> `K_R` carrier, or derive a nonseparable total-degree-2 primitive that is not
> reducible to the current rank-one carrier factorization.

## What Is / Is Not Claimed

- **Is:** the current `K_R` carrier factorizes exactly as a rank-one outer
  product.
- **Is:** that factorization is channel-blind on the source leg and has
  reciprocal projector-weight degree zero.
- **Is:** the current `K_R` factorization alone cannot produce `lambda=9/4`.
- **Is not:** does not rule out future source/readout normalization primitives;
  does not rule out a nonseparable degree-2 primitive; does not derive or
  adopt `rho_E = 21/4`.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_rank_one_carrier_leg_factorization_boundary_2026_06_21.py
```

Expected result:

```text
PASS=14 FAIL=0
```
