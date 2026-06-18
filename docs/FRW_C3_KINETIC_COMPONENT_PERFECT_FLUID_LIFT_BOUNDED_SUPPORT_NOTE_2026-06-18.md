# FRW C3 Kinetic Component Perfect-Fluid Lift Bounded Support

**Date:** 2026-06-18
**Claim type:** bounded_theorem
**Type:** bounded_theorem
**Status:** bounded support for finite perfect-fluid lift of ideal C3 kinetic
labels only.
**Status authority:** independent audit lane only. This note is not an audit
result and does not alter any row status.
**Primary runner:**
[`scripts/frontier_frw_c3_kinetic_component_fluid_lift_2026_06_18.py`](../scripts/frontier_frw_c3_kinetic_component_fluid_lift_2026_06_18.py)
**Cached runner output:**
[`logs/runner-cache/frontier_frw_c3_kinetic_component_fluid_lift_2026_06_18.txt`](../logs/runner-cache/frontier_frw_c3_kinetic_component_fluid_lift_2026_06_18.txt)

## Claim-Status Certificate Snapshot

```yaml
actual_current_surface_status: bounded-support
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This is a finite perfect-fluid lift only; C1, C2, and real cosmological species allocation remain open."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Target

The parent FRW open gate left a C3 residual after the finite kinetic
component-label bridge:

```text
bridge the ideal finite kinetic labels to the actual cosmological fluids
```

This note partially closes the algebraic part of that residual. It proves
that, once a homogeneous/isotropic finite component decomposition is supplied,
the ideal kinetic labels lift to the mixed perfect-fluid stress tensor used by
the parent FRW surface.

This is finite perfect-fluid lift only. It does not derive C1, does not derive
C2, does not derive real cosmological species allocation, does not derive the
thermal history, and does not set audit status. No new axiom, registry
premise, Tier-A admission, observational comparator, or fitted value is
introduced.

## Inputs

This note uses three component surfaces:

1. The finite kinetic C3 label bridge
   [`FRW_C3_EOS_COMPONENT_LABELS_KINETIC_BRIDGE_BOUNDED_SUPPORT_NOTE_2026-06-18.md`](FRW_C3_EOS_COMPONENT_LABELS_KINETIC_BRIDGE_BOUNDED_SUPPORT_NOTE_2026-06-18.md),
   which supplies the ideal non-Lambda labels `w_r = 1/3` and `w_m = 0`.
2. The separate dark-energy EOS surface
   [`DARK_ENERGY_EOS_RETAINED_COROLLARY_THEOREM_NOTE.md`](DARK_ENERGY_EOS_RETAINED_COROLLARY_THEOREM_NOTE.md),
   which supplies `w_Lambda = -1` outside this note.
3. A supplied finite cell-homogeneity/isotropy setting: every background cell
   carries the same component stress tensors, and those tensors are diagonal
   with equal spatial pressure entries. This supplied setting is the local
   algebraic part of C1, not a derivation of C1.

## Statement

For a mixed-index stress tensor convention

```text
T^mu_nu = diag(-rho, p_x, p_y, p_z),
```

the finite kinetic components lift as follows:

```text
radiation:            T_r = diag(-rho_r, rho_r/3, rho_r/3, rho_r/3)
pressureless matter:  T_m = diag(-rho_m, 0,       0,       0)
Lambda input:         T_L = diag(-rho_L, -rho_L, -rho_L, -rho_L)
```

The finite direct sum is

```text
T_total = T_r + T_m + T_L
        = diag(-(rho_r + rho_m + rho_L),
               rho_r/3 - rho_L,
               rho_r/3 - rho_L,
               rho_r/3 - rho_L).
```

Thus the total tensor is still a perfect-fluid tensor, with

```text
rho_total = rho_r + rho_m + rho_L
p_total   = rho_r/3 - rho_L
w_eff     = (rho_r/3 - rho_L) / (rho_r + rho_m + rho_L).
```

The non-Lambda C3 labels survive the component-to-fluid lift exactly. The
Lambda term is a separate supplied surface and is included only to show that
the direct sum has the FRW diagonal form used by the parent note.

## Proof

The component tensors above are diagonal and have equal spatial pressure
entries. Finite tensor addition preserves diagonality and equality of the
spatial pressure entries. Therefore the direct sum is a perfect-fluid tensor.

For the radiation component,

```text
p_r / rho_r = (rho_r/3) / rho_r = 1/3.
```

For the pressureless rest-matter component,

```text
p_m / rho_m = 0 / rho_m = 0.
```

For the Lambda component,

```text
p_L / rho_L = -rho_L / rho_L = -1.
```

That last equation is not derived here; it is a separate input from the
dark-energy EOS surface. The theorem in this note is the finite algebraic
lift: once the component tensors are supplied, the direct sum is the FRW
perfect-fluid tensor and the non-Lambda labels retain their values.

If every cell in a finite background packet carries the same `T_total`, the
finite cell average is exactly `T_total` and every cell is pointwise
FRW-compatible. If two cells carry different component amplitudes, each cell
can still have the same local label `w_r = 1/3`, but the packet is not a
homogeneous FRW background. That failure is a C1 residual, not a C3 label
failure.

Similarly, the standard source-free continuity identity

```text
d rho / d ln a + 3(1 + w) rho = 0
```

maps `w_r = 1/3` to `rho_r proportional to a^-4` and maps `w_m = 0` to
`rho_m proportional to a^-3`. A nonzero source/injection term changes that
identity. That source-free condition belongs to C2 and is not derived by this
note.

## Boundary

This bridge does not derive:

- C1, the cosmological principle or actual large-scale homogeneity/isotropy;
- C2, adiabatic expansion or absence of entropy/source injection;
- real cosmological species allocation into the ideal radiation, rest-matter,
  and Lambda components;
- the Friedmann equations;
- the actual thermal history;
- `N_eff`, `Delta N_eff = 0.046`, or any observed cosmological parameter;
- an effective retained audit status.

The result is still useful because it removes another textbook/application
step from C3: the ideal kinetic labels are not merely names, and their
component tensors assemble into the FRW perfect-fluid form by finite algebra.

## Trace

The direct blocker being partially addressed is still the parent request to
close or explicitly admit C1-C3 before re-auditing the FRW backdrop. This note
does not close the whole parent blocker. It narrows C3 from "ideal labels need
application to the fluid form" to these remaining residuals:

- C1 must supply or derive actual large-scale homogeneity/isotropy;
- C2 must supply or derive source-free adiabatic evolution;
- a real species-allocation bridge must identify the actual cosmological
  radiation/matter content with the ideal kinetic components.

## Verification

Run:

```bash
python3 scripts/frontier_frw_c3_kinetic_component_fluid_lift_2026_06_18.py
python3 scripts/cached_runner_output.py --refresh scripts/frontier_frw_c3_kinetic_component_fluid_lift_2026_06_18.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_frw_c3_kinetic_component_fluid_lift_2026_06_18.py
```

Expected result:

```text
VERDICT: bounded support passes for the finite perfect-fluid lift of ideal kinetic C3 labels. C1, C2, real cosmological species allocation, and audit status remain open.
```
