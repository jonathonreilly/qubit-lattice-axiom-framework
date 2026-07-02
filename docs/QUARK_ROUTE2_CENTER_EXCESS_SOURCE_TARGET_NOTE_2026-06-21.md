# Quark Route-2 Center-Excess Source Target

**Date:** 2026-06-21
**Claim type:** bounded_theorem
**Claim scope:** bounded support for the normalized center-excess source target
**Status authority:** independent audit lane only. This source note does not set, claim, or predict an audit outcome.
**Actual current-surface status:** bounded support for the normalized center-excess source target
**Trace class:** upstream_support
**Reachability to target:** supports the open Route-2 endpoint by isolating a bounded source/readout condition; does not derive the endpoint triple.
**Primary runner:** [`scripts/frontier_quark_route2_center_excess_source_target_2026_06_21.py`](../scripts/frontier_quark_route2_center_excess_source_target_2026_06_21.py)
**Runner cache:** [`logs/runner-cache/frontier_quark_route2_center_excess_source_target_2026_06_21.txt`](../logs/runner-cache/frontier_quark_route2_center_excess_source_target_2026_06_21.txt)
**Authority links:** [QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md)

## Scope

This block continues the S3/Route-2 endpoint campaign after pruning the
channel-scalar source-preparation shortcut. It asks the sharper source-map
question:

```text
If the readout side supplies one inverse Schur-weight factor, what exact
endpoint-normalized center-excess source theorem would finish the p=2 target?
```

This is not an audit verdict and does not resolve the parent gate
[S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md). It is a bounded support packet for
the exact next source theorem target.

## Premises

Allowed current-surface premises:

1. the exact Route-2 readout endpoint algebra;
2. the conditional T-side values
   `beta_T/alpha_T = -1`, `alpha_T/alpha_E = -2`;
3. Schur-frame weights
   `w_E = 1/3`, `w_T = 1/2`;
4. the one-power readout premise
   `(w_E/w_T)^-1 = 3/2`, so
   `q_E = (5/6)(3/2) = 5/4` and
   `rho_E = beta_E/alpha_E = 3/2`.

Forbidden proof inputs:

1. observed quark masses;
2. fitted Yukawa entries;
3. nearest-rational selection from the live endpoint data;
4. untyped adoption of the target value.

## Source-Excess Parameterization

Let the source-preparation map be diagonal on the restricted carrier
coordinates:

```text
S = diag(a_E, a_T, b_E, b_T)
```

acting on

```text
c = (u_E, u_T, delta_A1 u_E, delta_A1 u_T).
```

After source preparation and readout, the endpoint ratios transform as:

```text
s_TE' = (a_T/a_E) s_TE
rho_T' = (beta_T/alpha_T)(b_T/a_T)
rho_E' = (beta_E/alpha_E)(b_E/a_E).
```

The one-power readout premise gives:

```text
rho_T = -1
s_TE = -2
rho_E = 3/2.
```

The endpoint target requires:

```text
rho_T' = -1
s_TE' = -2
rho_E' = 21/4.
```

Solving these three equations gives the unique endpoint-normalized source
target:

```text
a_T/a_E = 1
b_T/a_T = 1
b_E/a_E = 7/2.
```

Equivalently, up to common E/T shell normalization, the needed center-excess
tilt is:

```text
S_excess = diag(1, 1, 7/2, 1).
```

## Consequence

With that source-excess target:

```text
rho_E' = (3/2)(7/2) = 21/4
q_E' = 1 + (21/4)/6 = 15/8
q_T' = 1 + (-1)/6 = 5/6
c_TE' = (-2)(5/6)/(15/8) = -8/9.
```

So the exact endpoint triple follows from the stated source target and the
declared one-power readout premise. The existence of such a typed source map
is still open. This packet makes the next proof obligation explicit:

```text
derive b_E/a_E = 7/2 as the exact next source theorem target.
```

## Boundary

This block does not say the current authority bank already contains
`S_excess`. It says that any endpoint-normalized source-preparation theorem
which completes the one-power readout route must supply exactly that
center-excess E tilt.

The pruned alternatives from prior blocks remain pruned:

1. current `Xi_P(t;c)` does not already name an independent source slot;
2. channel-scalar source preparation cannot move `q_E`;
3. a generic quadratic invariant does not force the inverse-square bridge.

The next science route is now concrete: find a typed current primitive that
produces `b_E/a_E = 7/2`, or prove that the current source bank cannot produce
that E-only center-excess tilt.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_center_excess_source_target_2026_06_21.py
```

Expected result:

```text
TOTAL: PASS=43, FAIL=0
```
