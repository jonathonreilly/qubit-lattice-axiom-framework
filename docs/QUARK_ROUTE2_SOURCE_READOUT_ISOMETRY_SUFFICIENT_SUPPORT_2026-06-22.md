# Quark Route-2 Source-Readout Isometry Sufficient Support

**Date:** 2026-06-22
**Type:** exact-support / conditional source-readout unit isometry theorem
**Actual current-surface status:** exact-support for a conditional source-readout isometry theorem; not current-surface closure
**Trace class:** upstream_support
**Primary runner:** [`scripts/frontier_quark_route2_source_readout_isometry_sufficient_support_2026_06_22.py`](../scripts/frontier_quark_route2_source_readout_isometry_sufficient_support_2026_06_22.py)
**Cached output:** [`outputs/frontier_quark_route2_source_readout_isometry_sufficient_support_2026_06_22.txt`](../outputs/frontier_quark_route2_source_readout_isometry_sufficient_support_2026_06_22.txt)

This is not an audit verdict. It does not run audit workers and does not apply
audit outcomes.

## Question

Block126 pruned the shortcut from Block121 equal internal source-unit weights
to the physical readout calibration:

```text
mu = 1.
```

What exact primitive would be sufficient to satisfy Block123 C4 without
importing the endpoint value?

## Route-2 Source-Readout Isometry Sufficient Theorem

Let `R_* = 8/9` be the internal connected fraction supplied by the Block121
same-source source jet after the identity line has been subtracted as pure
normalization:

```text
R_* = R_conn = 8 / (8 + 1) = 8/9,
kappa = 0.
```

A Route-2 source-readout isometry theorem is sufficient when it supplies all
of the following typed clauses:

```text
I1. phi_et:
    construct a typed map Phi_ET from Block121 source-Hessian components to
    the finite P_R E/T readout rows.

I2. source_norm_fixed:
    prove the Block121 connected source fraction is normalized in the source
    unit consumed by Phi_ET.

I3. readout_norm_fixed:
    prove the Route-2 physical center-ratio magnitude is normalized in the
    readout unit supplied by Phi_ET.

I4. unit_preserving:
    prove Phi_ET is isometric on the normalized scalar line, so one source
    connected unit maps to one physical readout magnitude unit.

I5. sign_after_kappa:
    consume the endpoint orientation sign only after the connected selector
    has been fixed as kappa=0.
```

Then `I1-I4` force:

```text
mu = 1.
```

With `I5`:

```text
c_TE = sigma * mu * R_* = (-1) * 1 * (8/9) = -8/9.
```

No endpoint value is used as an input.

## Boundary

The theorem is sufficient only after the typed isometry is proven. This packet
does not prove that the current Route-2 surface already contains `Phi_ET`, the
source/readout norm identification, or the unit-preserving isometry.

If any of `source_norm_fixed`, `readout_norm_fixed`, or `unit_preserving` is
missing, the family

```text
c_TE(mu) = -mu * (8/9)
```

remains endpoint-free for rational choices such as:

```text
mu = 1/2, 1, 3/2.
```

Thus Block127 supplies a precise constructive target for the remaining bridge:

```text
Route-2 source-readout isometry theorem:

construct Phi_ET and prove that it preserves the normalized scalar unit from
the Block121 connected source fraction to the physical P_R/E-T center-ratio
readout. This must be a framework typing/isometry proof, not a fitted scalar
calibration or endpoint-value reversal.
```

Expected runner result:

```text
TOTAL: PASS=81, FAIL=0
```
