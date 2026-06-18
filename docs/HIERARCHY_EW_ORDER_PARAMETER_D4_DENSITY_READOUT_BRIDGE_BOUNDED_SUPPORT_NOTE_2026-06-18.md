# Hierarchy EW Order-Parameter D4 Density Readout Bridge

**Date:** 2026-06-18
**Claim type:** bounded_theorem
**Type:** bounded_theorem
**Status:** bounded support for the EW order-parameter D4 density readout
bridge; endpoint selection and absolute scale remain open.
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.
**Primary runner:**
[`scripts/frontier_hierarchy_ew_order_parameter_d4_density_readout_bridge_2026_06_18.py`](../scripts/frontier_hierarchy_ew_order_parameter_d4_density_readout_bridge_2026_06_18.py)

```yaml
actual_current_surface_status: bounded-support
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "The bridge proves the EW order-parameter fourth-root coordinate for a supplied positive quartic D=4 density, but it does not derive that the hierarchy Matsubara endpoint coefficient is the physical Higgs density or derive the absolute EW scale."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Target Blocker

The audited-conditional row `hierarchy_dimensional_compression_note` still
needs a physical electroweak order-parameter/readout bridge identifying the
fixed positive D=4 density with the EW Higgs order-parameter coordinate and
the relevant endpoint coefficient surface.

This note closes the first half of that blocker: on the retained one-Higgs
neutral surface, the EW order-parameter coordinate `v` is exactly the positive
fourth-root coordinate of any positive quartic D=4 density

```text
rho_* = A(L) v(L)^4,       A(L) > 0.
```

It does not close the endpoint-selection half. It does not derive that the
hierarchy Matsubara endpoint coefficient is the physical Higgs density, does
not derive the absolute EW scale, and does not use an observed EW value.

## Theorem

On the one-Higgs electroweak surface used by the retained
[`EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26.md`](EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26.md),
take the neutral representative

```text
H(v) = (0, v/sqrt(2))^T,       v > 0.
```

Then the gauge-invariant neutral order-parameter norm

```text
q(H) := 2 H^dagger H
```

satisfies

```text
q(H(v)) = v^2.
```

Therefore any positive quartic D=4 density on this order-parameter coordinate

```text
rho_* = A(L) q(H(v(L)))^2,       A(L) > 0
```

is exactly

```text
rho_* = A(L) v(L)^4.
```

For two endpoints with the same fixed density,

```text
rho_* = A_ref v_ref^4 = A(L) v(L)^4,
```

the unique positive order-parameter ratio is

```text
v(L) / v_ref = (A_ref / A(L))^(1/4).
```

This is the same fourth-root readout as the fixed-density bridge
[`HIERARCHY_D4_DENSITY_SCALE_READOUT_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-16.md`](HIERARCHY_D4_DENSITY_SCALE_READOUT_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-16.md),
now tied to the retained EW neutral order-parameter coordinate rather than an
anonymous positive scalar `v`.

## Compatibility With The EW Gauge-Mass Dictionary

The retained EW diagonalization theorem gives, on the same neutral surface,

```text
M_W = g v / 2,
M_Z = sqrt(g^2 + g_Y^2) v / 2,
rho_tree = 1.
```

Thus at fixed gauge couplings the W/Z masses scale linearly with the same
positive coordinate `v`. The fourth-root density readout is therefore also the
fixed-coupling EW gauge-mass scale readout:

```text
(M_W(L) / M_W(ref))^4 = (v(L) / v_ref)^4 = A_ref / A(L),
```

and similarly for `M_Z`. The tree-level rho relation remains one because the
same `v^2` factor cancels.

## Endpoint Application Boundary

The hierarchy endpoint coefficient note supplies bounded endpoint algebra such
as

```text
A_2 = 1/(8 u_0^2),
A_4 = 1/(7 u_0^2),
A_2/A_4 = 7/8.
```

If those coefficients are supplied as the physical Higgs density coefficients,
the theorem above gives

```text
v_4 / v_2 = (7/8)^(1/4).
```

This note does not prove that supply step. The endpoint-selection residual
remains open: a later theorem must identify the hierarchy Matsubara endpoint
coefficient surface with the physical Higgs density surface.

## Negative Controls

- The direct placement `A(L)/A_ref` is the wrong fixed-density direction:
  it would increase the scale when the endpoint coefficient increases.
- A D=16 root is not the same readout. It fails the D=4 density equation
  unless the endpoint ratio is trivial.
- The theorem uses no observed EW value, no PDG comparator, no fitted selector,
  no new axiom, and no Tier-A admission.

## Verification

Run:

```bash
python3 scripts/frontier_hierarchy_ew_order_parameter_d4_density_readout_bridge_2026_06_18.py
```

Expected:

```text
TOTAL: PASS=12 FAIL=0
VERDICT: bounded support passes for the EW order-parameter D=4 density readout bridge. Endpoint selection, absolute scale, and hierarchy-to-physical-Higgs-density identification remain open.
```
