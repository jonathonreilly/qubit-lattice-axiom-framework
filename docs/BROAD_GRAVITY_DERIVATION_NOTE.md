# Broad Gravity Signature Algebra Packet

**Date:** 2026-04-13 (2026-05-29 scope repair).
**Claim type:** bounded_theorem.
**Status:** bounded-support algebra over a supplied weak-field action; not a retained broad gravity derivation.
**Primary runner:** `scripts/broad_gravity_signature_algebra_scope_check.py`
**Status authority:** independent audit lane only.

## 2026-05-29 Scope Repair

The conditional audit found that the previous broad weak-field bundle still
load-bore on unretained physical inputs:

- `L^{-1} = G_0` closure;
- `rho = |psi|^2` as gravitational source;
- `S = L(1 - phi)` as weak-field test-mass response;
- continuum and null-geodesic identifications.

This repair removes those physical bridge inputs from the load-bearing claim.
The row now proves only the algebra that follows once a scalar profile `phi`
and weak-field action density are supplied.

No new axiom is introduced. No gravitational response, source readout,
continuum bridge, or null-geodesic bridge is claimed.

## In-Scope Theorem

Let a supplied weak-field action for a path of length `L` be

```text
S(path; k, phi) = k L (1 - phi)
```

for scalar `phi` independent of the probe wavenumber `k`.

Two algebraic consequences follow.

1. **Stationary paths are k-independent.** Since

   ```text
   S = k F(path, phi),
   ```

   the stationary-phase equation is

   ```text
   delta S = k delta F = 0.
   ```

   For `k != 0`, this is equivalent to `delta F = 0`. The stationary path of
   the supplied action is independent of `k`.

2. **Phase-rate ratios follow algebraically.** If local phase rate is supplied
   as

   ```text
   omega(x) = k (1 - phi(x)),
   ```

   then for two positions `x1`, `x2`,

   ```text
   omega(x1)/omega(x2) = (1 - phi(x1))/(1 - phi(x2)).
   ```

These are algebraic identities on the supplied action/readout form. They are
not physical gravity claims unless the response/readout bridges are separately
derived or admitted by review.

## Non-Claims

This row does not prove:

- `L^{-1} = G_0`;
- `rho = |psi|^2` as a gravitational source readout;
- `S = L(1 - phi)` as a physical weak-field action;
- weak equivalence principle as a physical theorem;
- gravitational time dilation as a physical theorem;
- conformal metric, geodesic equation, light-bending factor of 2, continuum
  limit, or null-geodesic identification;
- any unconditional broad gravity signature from the Cl(3)-on-`Z^3` baseline.

Those remain separate bridge problems.

## Verification

Run:

```bash
python3 scripts/broad_gravity_signature_algebra_scope_check.py
```

Expected closeout:

```text
BROAD_GRAVITY_SIGNATURE_ALGEBRA=TRUE
K_INDEPENDENT_STATIONARY_PATH_ALGEBRA=TRUE
PHASE_RATE_RATIO_ALGEBRA=TRUE
PHYSICAL_WEP_OR_TIME_DILATION_CLAIMED=FALSE
CONTINUUM_OR_NULL_GEODESIC_BRIDGE_CLAIMED=FALSE
ACTUAL_CURRENT_SURFACE_STATUS=BOUNDED_SUPPORT
```
