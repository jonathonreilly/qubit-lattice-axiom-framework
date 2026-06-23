# Quark Route-2 Fisher-Riesz Isometry Sufficient Support

**Date:** 2026-06-22
**Type:** exact-support / conditional Fisher-Riesz source-readout isometry theorem
**Actual current-surface status:** exact-support for a conditional Fisher-Riesz source-readout isometry theorem; not current-surface closure
**Trace class:** upstream_support
**Primary runner:** [`scripts/frontier_quark_route2_fisher_riesz_isometry_sufficient_support_2026_06_22.py`](../scripts/frontier_quark_route2_fisher_riesz_isometry_sufficient_support_2026_06_22.py)
**Cached output:** [`outputs/frontier_quark_route2_fisher_riesz_isometry_sufficient_support_2026_06_22.txt`](../outputs/frontier_quark_route2_fisher_riesz_isometry_sufficient_support_2026_06_22.txt)

This is not an audit verdict. It does not run audit workers and does not apply
audit outcomes.

## Question

Block128 pruned typed `Phi_ET` existence alone as a proof of source/readout
isometry. What exact framework-shaped theorem would be sufficient to supply
the missing metric pullback?

## Fisher-Riesz Isometry Sufficient Theorem

The existing finite sharp-record Fisher stack supplies a real unit-tangent
mechanism:

```text
finite sharp-record score tangent s,
Fisher pairing <s,t>_F = E_0[s t],
primitive signed record epsilon with ||epsilon||_F = 1,
scaled family lambda epsilon with norm lambda^2.
```

This generic mechanism becomes a Route-2 source/readout isometry only under
the following additional typed clauses:

```text
F1. route2_sharp_record:
    the physical P_R/E-T readout is realized as a finite sharp-record
    probability source/readout surface.

F2. same_source:
    that source/readout surface is the same source as the Block121
    connected-Hessian source used to obtain R_conn=8/9 and kappa=0.

F3. source_unit:
    the Block121 connected scalar line is a Fisher-unit score tangent.

F4. readout_riesz_unit:
    the physical center-ratio readout line is represented by a Fisher-unit
    Riesz vector in the same tangent space.

F5. phi_fisher_riesz:
    Phi_ET is the Fisher-Riesz identification between those unit lines, so
    Phi_ET^* g_readout = g_source on the normalized scalar line.

F6. sign_after_kappa:
    the endpoint orientation sign is consumed only after kappa=0.
```

Then `F1-F5` supply Block128's missing metric pullback and force:

```text
mu = 1.
```

With `F6` and Block121's internal connected fraction `R_* = 8/9`:

```text
c_TE = sigma * mu * R_* = (-1) * 1 * (8/9) = -8/9.
```

No endpoint value is used as an input.

## Boundary

This packet does not prove the current Route-2 surface already satisfies
`F1-F5`.

The source-measure/Fisher notes supply generic finite probability geometry and
finite orthonormal response-basis algebra. Block81 already prunes the shortcut
from those generic tools to a Route-2 full color-record ensemble/readout
theorem. Therefore the new missing primitive is not "use Fisher geometry" in
the abstract. It is:

```text
Route-2 Fisher-Riesz source/readout realization theorem:

realize the physical P_R/E-T center-ratio readout as the same finite
sharp-record Fisher tangent surface as the Block121 connected source; identify
the source scalar line and physical readout scalar line as Fisher-unit Riesz
vectors; and prove Phi_ET is the Riesz identification between them.
```

Expected runner result:

```text
TOTAL: PASS=86, FAIL=0
```
