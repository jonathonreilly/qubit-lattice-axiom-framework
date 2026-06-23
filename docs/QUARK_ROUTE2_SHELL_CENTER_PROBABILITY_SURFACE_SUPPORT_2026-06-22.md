# Quark Route-2 Shell/Center Probability Surface Support

**Date:** 2026-06-22
**Type:** exact-support / conditional shell-center probability-surface theorem
**Actual current-surface status:** exact-support for a conditional four-slot probability surface; not current-surface closure
**Trace class:** upstream_support
**Primary runner:** [`scripts/frontier_quark_route2_shell_center_probability_surface_support_2026_06_22.py`](../scripts/frontier_quark_route2_shell_center_probability_surface_support_2026_06_22.py)
**Cached output:** [`outputs/frontier_quark_route2_shell_center_probability_surface_support_2026_06_22.txt`](../outputs/frontier_quark_route2_shell_center_probability_surface_support_2026_06_22.txt)

This is not an audit verdict. It does not run audit workers and does not apply
audit outcomes.

## Question

Block132 pruned the two-outcome `{E,T}` probability surface because Route-2
requires shell/center structure. What four-slot probability theorem would be
sufficient?

## Four-Slot Shell/Center Contract

A Route-2 shell/center probability-surface theorem is sufficient if it proves:

```text
S1. omega_four:
    Omega_R has typed events E-shell, E-center, T-shell, T-center.

S2. positive_reference:
    P0 is strictly positive and normalized on those four events.

S3. rn_source_path:
    P_h is a normalized RN source path with P_h << P0.

S4. readout_coordinate_functions:
    the RN score/cumulant readout has coordinate functionals for gamma_E(shell),
    gamma_E(center), gamma_T(shell), and gamma_T(center).

S5. center_ratio_scalar_line:
    the physical center-ratio scalar line is typed from the center coordinate
    functionals after shell/center typing is established.

S6. same_source_riesz:
    the Block121 source scalar and physical P_R/E-T readout scalar are
    same-source Fisher-unit Riesz lines.

S7. sign_after_kappa:
    the endpoint orientation sign is consumed only after kappa=0.
```

Then `S1-S6` supply Block131's probability surface and Block129's
Fisher-Riesz realization:

```text
Phi_ET^* g_readout = g_source,
mu = 1.
```

With `S7` and `R_* = 8/9`:

```text
c_TE = sigma * mu * R_* = (-1) * 1 * (8/9) = -8/9.
```

No endpoint value is used as an input.

## Boundary

This packet does not construct `P0`, `P_h`, or the coordinate functions from
current Route-2 primitives. It only records the exact four-slot theorem target
that survives Block132.

Expected runner result:

```text
TOTAL: PASS=85, FAIL=0
```
