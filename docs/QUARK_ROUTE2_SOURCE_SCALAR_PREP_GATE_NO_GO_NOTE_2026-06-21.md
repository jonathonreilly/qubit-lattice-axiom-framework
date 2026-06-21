# Quark Route-2 Source-Scalar Prep Gate No-Go

**Date:** 2026-06-21
**Actual current-surface status:** no-go for channel-scalar source-preparation shortcut
**Trace class:** negative_route_pruning
**Runner:** `scripts/frontier_quark_route2_source_scalar_prep_gate_no_go_2026_06_21.py`

Actual current-surface status: no-go for channel-scalar source-preparation shortcut.

## Scope

This block continues the S3/Route-2 endpoint campaign after the source-slot
dualization gate. The previous block showed that the current conditional
family

```text
Xi_P(t ; c) = (P_R c) tensor V_R(t)
```

does not already contain an independent source-preparation slot. This block
tests the first obvious candidate for such a slot:

```text
S(a_E,a_T) = diag(a_E, a_T, a_E, a_T)
```

on the restricted carrier coordinates

```text
c = (u_E, u_T, delta_A1 u_E, delta_A1 u_T).
```

This is not an audit verdict and does not resolve the parent gate
`S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md`. It prunes only the shortcut that a
channel-scalar source map, including inverse Schur channel scaling, can supply
the missing source-side endpoint factor.

## Current Algebra

The current readout-map authority reduces the restricted readout class to

```text
P_R = [[alpha_E, 0, beta_E, 0],
       [0, alpha_T, 0, beta_T]].
```

The endpoint columns are

```text
E-shell  = (1, 0, 0,   0)
E-center = (1, 0, 1/6, 0)
T-shell  = (0, 1, 0,   0)
T-center = (0, 1, 0, 1/6).
```

After applying a channel-scalar source map before readout,

```text
P_R S(a_E,a_T),
```

the endpoint amplitudes become

```text
gamma_E(shell)  = alpha_E a_E
gamma_E(center) = a_E (alpha_E + beta_E/6)

gamma_T(shell)  = alpha_T a_T
gamma_T(center) = a_T (alpha_T + beta_T/6).
```

Therefore

```text
q_E' = gamma_E(center) / gamma_E(shell)
     = 1 + (beta_E/alpha_E)/6
     = q_E

q_T' = gamma_T(center) / gamma_T(shell)
     = 1 + (beta_T/alpha_T)/6
     = q_T.
```

The channel scalar changes only the shell T/E scale:

```text
s_TE' = (a_T/a_E) s_TE.
```

It leaves q_E and q_T unchanged.

## Canonical Inverse Schur Candidate

The Schur weights in this frame are

```text
w_E = 1/3
w_T = 1/2.
```

The naive inverse Schur channel source map is therefore

```text
a_E = 1/w_E = 3
a_T = 1/w_T = 2.
```

But because this map is still channel-scalar, it does not move
`beta_E/alpha_E` or `beta_T/alpha_T`. If the readout side has only the
one-sided canonical value `beta_E/alpha_E = 3/2`, the channel-scalar source
map leaves it at `3/2`, not `21/4`. If the shell ratio was `-2`, the same
source map changes it to `-4/3`.

So inverse Schur channel scaling is not the missing two-sided theorem. It
supplies a channel normalization, not a center-excess source law.

## Remaining Source-Map Condition

A source map that can affect the E-center ratio must distinguish shell from
center-excess coordinates:

```text
S = diag(a_E, a_T, b_E, b_T).
```

Then

```text
q_E' = 1 + (beta_E/alpha_E)(b_E/a_E)/6
q_T' = 1 + (beta_T/alpha_T)(b_T/a_T)/6.
```

Under the T-side conditional value `beta_T/alpha_T = -1`, keeping
`q_T = 5/6` forces

```text
b_T/a_T = 1.
```

The E-side target requires

```text
rho_E * (b_E/a_E) = 21/4,
```

where `rho_E = beta_E/alpha_E` is the readout-side E ratio before source
excess tilt. If `rho_E` is not already derived, choosing `b_E/a_E` is exactly
the missing E-center source theorem in another notation.

For example, starting from the readout-only canonical value

```text
rho_E = 3/2
```

would require

```text
b_E/a_E = (21/4)/(3/2) = 7/2.
```

That is a real, typed center-excess theorem to prove. It is not contained in
the channel-scalar candidate.

## No-Go Boundary

The pruned shortcut is:

```text
channel-scalar source preparation on (E,T) channels
  => second inverse Schur endpoint factor
  => beta_E/alpha_E = 21/4.
```

The implication fails because channel-scalar source preparation leaves the
center/shell ratios invariant. It can rescale shell T/E, but it cannot create
the E-center excess factor.

This does not rule out:

1. a future center-excess nonuniform `S_dual` theorem;
2. a future readout-only inverse-square coefficient theorem;
3. a theorem deriving `beta_E/alpha_E = 21/4` directly from another current
   Route-2 primitive.

## Stuck Fan-Out

| Frame | Result |
|---|---|
| Endpoint-column algebra | Channel scalar cancels in q_E and q_T. |
| Canonical inverse Schur source scaling | Gives `(a_E,a_T)=(3,2)` but leaves rho_E unchanged. |
| Shell T/E normalization | Channel scalar can tune shell T/E only through `a_T/a_E`. |
| Center-excess nonuniform map | Can move q_E, but requires the new ratio `b_E/a_E`. |
| Readout-only inverse square | Still open as an alternative theorem target. |

The next positive route is therefore sharper than "find source prep": derive
the typed center-excess nonuniform source law, or derive the readout-only
inverse-square law without a source map.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_scalar_prep_gate_no_go_2026_06_21.py
```

Expected result:

```text
TOTAL: PASS=66, FAIL=0
```
