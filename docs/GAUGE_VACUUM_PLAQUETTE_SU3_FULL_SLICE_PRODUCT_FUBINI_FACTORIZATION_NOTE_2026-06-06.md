---
claim_id: gauge_vacuum_plaquette_su3_full_slice_product_fubini_factorization_note_2026-06-06
claim_type_author_hint: bounded_theorem
status_authority: independent_audit_lane_only
direct_effective_status_change_allowed_from_this_note: false
---

# SU(3) Full-Slice Product-Fubini Factorization For Rim/Environment Splits

**Date:** 2026-06-06
**Status:** exact-support theorem for a supplied finite rim/far support
partition. This is a source-side repair note; it does not apply an audit
verdict and does not edit audit data.
**Primary runner:**
`scripts/audit_companion_gauge_full_slice_su3_product_fubini_factorization_2026_06_06.py`
with cache
`logs/runner-cache/audit_companion_gauge_full_slice_su3_product_fubini_factorization_2026_06_06.txt`.

## Purpose

The earlier full-slice rim-lift note used a finite SU(2) Monte Carlo toy to
check the rim/far Fubini step. That was useful support, but it was not a
framework-native SU(3) statement. This companion removes that import: the
factorization is a compact-product-measure theorem on finite `SU(3)` link
variables.

This note does not evaluate `B_6(W)`, `eta_6(W)`, or the physical environment
kernel. It closes only the mathematical product-Fubini step once the rim/far
support partition has been supplied.

## Theorem

Let `G = SU(3)`. Fix marked holonomy data `W` and edge-slice boundary data
`U`. Let the finite unmarked link variables split as a disjoint union

```text
Xi = Xi^rim sqcup Xi^far.
```

Assume the Wilson plaquette action has the support separation

```text
A(U,W; Xi) = A^rim(U,W; Xi^rim) + A^far(U; Xi^far) + A^0(U,W),
```

equivalently every nonconstant plaquette factor is supported either in
`Xi^rim` plus fixed boundary/marked variables, or in `Xi^far` plus fixed
boundary variables, and no plaquette contains both a rim variable and a far
variable.

With product Haar measure on the finite link set,

```text
dmu_Xi = dmu_H^(Xi^rim) dmu_H^(Xi^far),
```

the full-slice marginal factorizes pointwise:

```text
Psi_beta(W)(U)
 = exp((beta/3) A^0(U,W))
   B_beta(W)(U) F_beta(U),
```

where

```text
B_beta(W)(U)
 = int_{G^(Xi^rim)} exp((beta/3) A^rim(U,W; Xi^rim)) dmu_H^(Xi^rim),

F_beta(U)
 = int_{G^(Xi^far)} exp((beta/3) A^far(U; Xi^far)) dmu_H^(Xi^far).
```

Because `G` is compact and the Wilson plaquette action is continuous, the
integrand is bounded and measurable. Fubini/Tonelli applies directly to the
finite product Haar space.

## Class Projection

Let `P_cls` be the canonical projection in the marked `W` slot. Since
`F_beta(U)` is independent of `W`, linearity gives

```text
P_cls Psi_beta(W)(U)
 = exp((beta/3) A^0(U,W)) F_beta(U) P_cls B_beta(W)(U)
```

when `A^0` is already part of the marked/local scalar factor, or the same
identity after absorbing `exp((beta/3) A^0)` into `B_beta`. Thus the marked
class-sector data carried by the rim factor is `P_cls B_beta(W)`.

This is the exact SU(3) replacement for the earlier SU(2)-toy Fubini support.
It is not a separate proof of the temporal-gauge mixed-kernel compression
bridge.

## Repair Boundary For The 2026-04-17 Rim-Lift Row

This companion addresses one named blocker in
`GAUGE_VACUUM_PLAQUETTE_FULL_SLICE_RIM_LIFT_INTEGRAL_BOUNDARY_SCIENCE_ONLY_NOTE_2026-04-17.md`:
the prior runner verified only a toy SU(2) factorization. The source-side
repair is now SU(3)-native and exact at the product-measure level.

Remaining gates are explicit:

- supply or audit the actual physical rim/far support partition for the
  intended Wilson slab;
- prove the temporal-gauge mixed-kernel marked/non-marked compression bridge;
- evaluate the beta-six rim/environment integrals if a numerical plaquette
  value is needed.

## Non-Claims

This note does not claim:

- an explicit closed form for `B_6(W)`, `eta_6(W)`, `K_6^env`, or
  `rho_(p,q)(6)`;
- that the finite support partition has been derived for every physical
  untruncated Wilson environment;
- that non-marked mixed-link factors have been compressed to only
  trivial-channel scalars;
- any audit status promotion for the parent row;
- any edit to `docs/audit/data/*`.

## Verification

Run:

```bash
python3 scripts/audit_companion_gauge_full_slice_su3_product_fubini_factorization_2026_06_06.py
```

Expected summary:

```text
SUMMARY: PASS=20 FAIL=0
```
