# Quark Route-2 Inverse-Square Channel-Law Gate Note

**Date:** 2026-06-21
**Status:** exact negative boundary / no-go for native/simple channel powers; open second-dual readout-law target.
**Primary runner:** `scripts/frontier_quark_route2_inverse_square_channel_law_gate_2026_06_21.py`
**Output:** `outputs/frontier_quark_route2_inverse_square_channel_law_gate_2026_06_21.txt`

## Claim Boundary

This block removes the CKM semantic bridge and attacks the pure Route-2
residual:

```text
Can the current O_h channel data force lambda=q_E/q_T=9/4?
```

The current per-arm projector weights are

```text
w_E = 1/3,
w_T1 = 1/2.
```

For a scale-free channel law

```text
C_X proportional to w_X^p,
lambda = C_E/C_T1,
```

the endpoint requires exactly

```text
p = -2.
```

That is the second-dual inverse-square law. Current native/simple powers miss:

| Law | Exponent | `lambda` | Endpoint result |
|---|---:|---:|---|
| second-dual inverse-square | `-2` | `9/4` | target |
| one-dual reciprocal | `-1` | `3/2` | misses |
| equal Schur scalar | `0` | `1` | misses |
| projector/per-arm trace | `1` | `2/3` | misses |
| quadratic diagonal weight | `2` | `4/9` | misses |

Therefore the current-bank target is no longer "some dimension ratio." It is
the specific second-dual law

```text
C_X proportional to w_X^-2.
```

## Exact Endpoint Consequences

With the granted T-side candidates,

```text
q_T = 5/6,
s_TE = -2,
q_E = q_T lambda,
rho_E = 6(q_E - 1),
c_TE = s_TE q_T/q_E.
```

The exponent table is exact:

```text
p=-2 -> lambda=9/4, q_E=15/8, rho_E=21/4, c_TE=-8/9
p=-1 -> lambda=3/2, q_E=5/4,  rho_E=3/2,  c_TE=-4/3
p= 0 -> lambda=1,   q_E=5/6,  rho_E=-1,   c_TE=-2
p= 1 -> lambda=2/3, q_E=5/9,  rho_E=-8/3, c_TE=-3
p= 2 -> lambda=4/9, q_E=10/27,rho_E=-34/9,c_TE=-9/2
```

Only `p=-2` recovers the target `rho_E=21/4`.

## Current-Bank Firewall

The Schur covariance no-go already proves that an `O_h`-invariant quadratic
functional has a free E:T1 coefficient ratio. This block isolates the exact
power-law meaning of that freedom:

- equal Schur scalars give `p=0`;
- projector trace/per-arm weighting gives `p=1`;
- quadratic diagonal weighting gives `p=2`;
- one-dual reciprocal weighting gives `p=-1`;
- the desired endpoint needs `p=-2`.

No checked current surface supplies the second reciprocal/second-dual step.
That missing step is a genuine readout primitive or theorem target, not a
normalization consequence of the existing carrier.

## What This Does Not Claim

This is not a global impossibility theorem over arbitrary future nonlinear
observables. It only closes the native/simple channel-power routes listed
above and restates the exact positive target:

```text
derive C_X proportional to w_X^-2 from Route-2 readout primitives.
```

No observed quark masses, fitted endpoint values, audit verdicts, or PR
merge-state facts are used.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_inverse_square_channel_law_gate_2026_06_21.py
```

Expected result:

```text
TOTAL: PASS=20, FAIL=0
```
