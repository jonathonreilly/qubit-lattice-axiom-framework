# Hierarchy D=4 Effective-Potential Readout Bridge Bounded Theorem

**Date:** 2026-06-15
**Claim type:** bounded theorem
**Status:** source-side bridge; independent review/audit owns any effective
status change.
**Runner:** `scripts/hierarchy_d4_effective_potential_readout_bridge_2026_06_15.py`

## Purpose

This note supplies the narrow bridge missing from
`HIERARCHY_DIMENSIONAL_COMPRESSION_NOTE.md`: given an effective-potential
density coefficient `A(L_t)` in four spacetime dimensions, it fixes the
exponent, inverse/direct placement, sign, and normalization of the associated
dimension-one readout.

This is not a full hierarchy closure theorem. It proves the finite
effective-potential readout map under an explicit premise:

```text
rho_* = A(L_t) v(L_t)^4
```

where `rho_*` is the same dimension-four density scale compared across the
`L_t` endpoints. Equivalently,

```text
v(L_t) = (rho_* / A(L_t))^(1/4).
```

The premise is the bounded bridge. The algebra below proves what follows from
it on the framework's finite hierarchy endpoint formulas.

## Inputs

From `HIERARCHY_EFFECTIVE_POTENTIAL_ENDPOINT_NOTE.md`, the small-m
effective-potential density has

```text
Delta f(L_t,m) = A(L_t) m^2 + O(m^4)
A(L_t) = (1 / (2 L_t u_0^2)) sum_omega 1 / (3 + sin^2 omega).
```

On the APBC hierarchy endpoints:

```text
A_2   = 1 / (8 u_0^2)
A_4   = 1 / (7 u_0^2)
A_inf = 1 / (4 sqrt(3) u_0^2).
```

No observed target value, fitted selector, coupling value, or new axiom enters
this bridge.

## Theorem

Assume the D=4 effective-potential-density readout premise
`rho_* = A(L_t) v(L_t)^4` with a common `rho_*` across endpoints.
Then for any two endpoints `a,b`,

```text
v_b / v_a = (A_a / A_b)^(1/4).
```

Therefore:

```text
v_4 / v_2
  = (A_2 / A_4)^(1/4)
  = ((1/(8 u_0^2)) / (1/(7 u_0^2)))^(1/4)
  = (7/8)^(1/4).
```

The sign and placement are fixed:

- `A_4 > A_2`, so `v_4/v_2 < 1`; the factor is a downward compression.
- The correction multiplies `v` itself, not `v^2`, `v^4`, or the determinant.
- The `u_0` normalization cancels exactly in the endpoint ratio.

Likewise, for the infinite temporal-average endpoint,

```text
v_inf / v_2
  = (A_2 / A_inf)^(1/4)
  = (sqrt(3)/2)^(1/4)
  = (3/4)^(1/8).
```

## Boundary

This note does not claim:

- an effective retained status or audit verdict;
- a derivation of the physical electroweak scale from the primitive stack;
- selection of `L_t = 4` or `L_t = infinity` as the physical endpoint;
- a coupling, alpha, Planck-scale, or observed-value comparison;
- closure of the broader hierarchy formula.

It supplies a bounded source-side bridge: if the framework uses the D=4
effective-potential-density readout premise, then the exponent, sign,
placement, and normalization are no longer ambiguous.

## Verification

Run:

```bash
python3 scripts/hierarchy_d4_effective_potential_readout_bridge_2026_06_15.py
```

Expected:

```text
SUMMARY: PASS=15 FAIL=0
```
