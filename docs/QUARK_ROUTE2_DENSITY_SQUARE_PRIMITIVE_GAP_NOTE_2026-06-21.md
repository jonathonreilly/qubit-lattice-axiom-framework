# Quark Route-2 Density-Square Primitive Gap

**Date:** 2026-06-21
**Status:** scoped no-go / conditional support; branch-local physics-loop packet only
**Primary runner:** `scripts/frontier_quark_route2_density_square_primitive_gap_2026_06_21.py`

## Scope

This block attacks the direct hard residual left by the Route-2 readout
endpoint:

```text
q_E/q_T = 9/4
rho_E = 21/4
c_TE = -8/9
```

The object under test is a current-surface source/readout primitive that would
make the channel-center lift scale as the inverse square of the channel's own
finite-star projector weight:

```text
q_X proportional to w_X^-2.
```

This is the explicit `p=-2` density-square primitive named by the Schur
covariance no-go as the sharpest visible gap.

## Conditional Exact Support

The finite-star weights are:

```text
w_E = 1/3,  w_T = 1/2,  r = w_E/w_T = 2/3.
```

If a source/readout primitive supplies:

```text
q_X proportional to w_X^-2,
```

then:

```text
q_E/q_T = (w_E/w_T)^-2 = (2/3)^-2 = 9/4.
```

With the already-granted T-side values:

```text
q_T = 5/6,
gamma_T(shell)/gamma_E(shell) = -2,
```

this gives:

```text
q_E = (9/4)(5/6) = 15/8,
rho_E = 6(q_E - 1) = 21/4,
c_TE = (-2)(5/6)/(15/8) = -8/9.
```

So the density-square primitive is exactly the right primitive if it can be
derived or admitted. The runner verifies this in exact rational arithmetic.

## Current-Surface Gap

The current named Route-2 bank does not supply the primitive.

The runner quote-anchors this boundary against the current notes:

- the Schur covariance note says no named functional produces an
  inverse-square-of-projector-weight center lift;
- the exact readout note keeps `rho_E` free in the reduced family;
- the s3 theta-to-slice parent keeps the endpoint triple upstream and open;
- the factor-rigidity note localizes the ambiguity in the spatial prefactor
  rather than the time channel;
- the E-center lift attempt did not find an exact E-channel source row;
- the bilinear carrier note is definition-only and does not prove a physical
  tensor primitive;
- the minimal Record axiom supplies no readout context, weighting, or
  normalization rule.

The runner also scans the registered premise/admission JSON for exact
density-square primitive tokens and builds a typed reachability graph. Current
edges reach the value `kappa^2 = 9/4` only as value arithmetic. Adding the
single missing `p=-2` density-square edge creates the endpoint path, but the
current edge bank has no typed path to `rho_E = 21/4`.

## Stuck Fan-Out Synthesis

The block checks five frames:

| Frame | Result |
|---|---|
| carrier/readout algebra | `rho_E` remains free in `P(rho_E)` |
| Schur/quadratic invariant | the E:T quadratic ratio is free; `p=-2` is not forced |
| time/slice coupling | `Lambda_R` and `V_R(t)` are readout-independent |
| Record/minimal axioms | no readout context, weighting, or normalization is supplied |
| source-domain color bridge | conditional `c_TE=-8/9` is a separate signed bridge, not a density-square theorem |

All frames point to the same hard residual: a new source/readout premise is
needed to evaluate the E-center column with the inverse-square weight.

## Claim Boundary

This block does not prove that no future nonlinear observable can supply the
primitive. It proves only:

```text
current named Route-2 authority bank
does not contain a typed p=-2 density-square primitive.
```

It also records the exact consequence if that primitive is later derived or
explicitly accepted.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_density_square_primitive_gap_2026_06_21.py
python3 -m py_compile scripts/frontier_quark_route2_density_square_primitive_gap_2026_06_21.py
```

Expected result:

```text
PASS=43 FAIL=0 TOTAL=43
```
