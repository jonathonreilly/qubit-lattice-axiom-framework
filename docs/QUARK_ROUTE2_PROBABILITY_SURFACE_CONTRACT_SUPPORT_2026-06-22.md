# Quark Route-2 Probability Surface Contract Support

**Date:** 2026-06-22
**Type:** exact-support / conditional Route-2 probability-surface contract
**Actual current-surface status:** exact-support for a conditional probability-surface contract; not current-surface closure
**Trace class:** upstream_support
**Primary runner:** [`scripts/frontier_quark_route2_probability_surface_contract_support_2026_06_22.py`](../scripts/frontier_quark_route2_probability_surface_contract_support_2026_06_22.py)
**Cached output:** [`outputs/frontier_quark_route2_probability_surface_contract_support_2026_06_22.txt`](../outputs/frontier_quark_route2_probability_surface_contract_support_2026_06_22.txt)

This is not an audit verdict. It does not run audit workers and does not apply
audit outcomes.

## Question

Block130 shows that the current finite `P_R` readout plus generic Fisher
support does not supply the Route-2 Fisher-Riesz realization. What exact
probability-surface primitive would be sufficient?

## Minimal Probability-Surface Contract

The following Route-2-specific clauses are sufficient:

```text
P1. omega_r:
    construct a finite Route-2 sharp-record sample space Omega_R typed to the
    physical P_R/E-T readout.

P2. positive_reference:
    construct a strictly positive normalized reference probability P0 on
    Omega_R from framework Route-2 data.

P3. rn_source_path:
    construct a normalized source path P_h with P_h << P0 whose RN score is
    the physical center-ratio scalar direction.

P4. disconnected_normalization:
    prove the identity/disconnected line is exactly the probability
    normalization line, so the RN score is zero-mean before connected
    cumulants are read.

P5. same_source_block121:
    prove this probability source is the same source as the Block121
    connected-Hessian source that gives R_conn=8/9 and kappa=0.

P6. fisher_unit_riesz:
    prove the Block121 source scalar line and physical P_R/E-T readout scalar
    line are Fisher-unit Riesz vectors and Phi_ET identifies those unit lines.

P7. sign_after_kappa:
    consume the endpoint orientation sign only after kappa=0.
```

Then `P1-P6` supply Block129's Route-2 Fisher-Riesz realization, hence:

```text
Phi_ET^* g_readout = g_source,
mu = 1.
```

With `P7` and `R_* = 8/9`:

```text
c_TE = sigma * mu * R_* = (-1) * 1 * (8/9) = -8/9.
```

No endpoint value is used as an input.

## Boundary

This packet is a contract, not a construction. It does not prove `Omega_R`,
`P0`, or `P_h` exist on the current surface.

It also does not bypass Block130. Block130 remains the current-surface no-go
for the shortcut from finite `P_R` rows plus generic Fisher support to this
probability surface.

## Remaining Primitive

The next exact construction target is:

```text
Route-2 sharp-record probability-surface theorem:

construct Omega_R, P0, and P_h satisfying P1-P7 from framework Route-2
primitives, without endpoint-value input or fitted scalar normalization.
```

Expected runner result:

```text
TOTAL: PASS=86, FAIL=0
```
