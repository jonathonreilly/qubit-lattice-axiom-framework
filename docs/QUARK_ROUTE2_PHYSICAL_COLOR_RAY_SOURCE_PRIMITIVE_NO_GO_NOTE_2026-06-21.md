# Quark Route-2 Physical Color-Ray Source Primitive No-Go

**Date:** 2026-06-21
**Claim type:** no_go
**Claim scope:** current-bank no-go plus conditional support boundary
**Status authority:** independent audit lane only. This source note does not set, claim, or predict an audit outcome.
**Actual current-surface status:** current-bank no-go plus conditional support boundary
**Trace class:** negative_route_pruning
**Reachability to target:** prunes a Route-2 endpoint escape route; does not derive the endpoint triple.
**Primary runner:** [`scripts/frontier_quark_route2_physical_color_ray_source_primitive_no_go_2026_06_21.py`](../scripts/frontier_quark_route2_physical_color_ray_source_primitive_no_go_2026_06_21.py)
**Runner cache:** [`logs/runner-cache/frontier_quark_route2_physical_color_ray_source_primitive_no_go_2026_06_21.txt`](../logs/runner-cache/frontier_quark_route2_physical_color_ray_source_primitive_no_go_2026_06_21.txt)
**Authority links:** [COLOR_ORIENTATION_OF_THE_STATE_IS_PREDICTIVELY_VACUOUS_NARROW_THEOREM_NOTE_2026-06-09.md](COLOR_ORIENTATION_OF_THE_STATE_IS_PREDICTIVELY_VACUOUS_NARROW_THEOREM_NOTE_2026-06-09.md), [MATTER_COLOR_DEPOLARIZATION_NECESSARY_FOR_GAUGE_LINK_AD_INVARIANCE_NARROW_THEOREM_NOTE_2026-06-09.md](MATTER_COLOR_DEPOLARIZATION_NECESSARY_FOR_GAUGE_LINK_AD_INVARIANCE_NARROW_THEOREM_NOTE_2026-06-09.md), [EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md](EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md), [RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08.md](RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08.md), [Z3_CHARACTER_ISOMORPHISM_COLOR_GENERATION_OPEN_GATE_NOTE_2026-05-10.md](Z3_CHARACTER_ISOMORPHISM_COLOR_GENERATION_OPEN_GATE_NOTE_2026-05-10.md), [QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md)


## Question

The Route-2 endpoint residual can now be stated sharply. A physical color ray
`psi in C^3` would give

```text
H_psi = |psi><psi| - I_3/3,
```

one line in the 8-dimensional adjoint coordinate space, and a 7-dimensional
orthogonal complement. Reading that complement as the E-center excess gives

```text
e_E = 7/8,
q_E = 15/8,
rho_E = 21/4,
c_TE = -8/9
```

under the granted T-side Route-2 values. The question is whether the current
source/support bank already supplies that physical color-ray/source-line
primitive.

## Minimal Premises

Allowed:

- exact finite-dimensional `SU(3)` color algebra on `C^3`;
- the Gell-Mann basis with `Tr(T_a T_b)=delta_ab/2`;
- current source-bank notes for color orientation, color depolarization,
  Fierz/channel algebra, `Z_3` color/generation labels, and Route-2 readout;
- granted T-side Route-2 values `q_T=5/6` and `s_TE=-2`.

Forbidden:

- observed quark masses, CKM/J target fits, or live endpoint proximity;
- an untyped identification of a color orientation with physical source data;
- an untyped identification of Fierz `F_adj=8/9` with a Route-2 center ratio;
- a new physical readout/weighting rule, color frame, or source-line primitive.

## Conditional Positive Surface

If a physical color ray is supplied, the construction is exact:

```text
psi -> H_psi = |psi><psi| - I_3/3.
```

For `psi=e_3`, `H_psi` is traceless and nonzero. In adjoint coordinates it
defines a rank-one projector `P_line` in the 8-dimensional adjoint coordinate
space. The complement `I_8 - P_line` has rank `7`, so the normalized complement
fraction is `7/8`.

The endpoint arithmetic then gives:

```text
q_E = 1 + 7/8 = 15/8,
rho_E = 6(q_E - 1) = 21/4,
c_TE = (-2)(5/6)/(15/8) = -8/9.
```

So the missing primitive is not vague "non-invariant geometry." It is
specifically a physical color ray, gauge-frame source line, or equivalent datum
that selects one line inside the adjoint `8`.

## Current-Bank No-Go

The current source bank does not supply that primitive.

1. **Invariant/scalar data cannot select a line.** The only matrix commuting
   with the fundamental `SU(3)` generators is a scalar, and the traceless scalar
   is zero. Equivalently, the adjoint `8` has no nonzero invariant vector. Any
   scalar or invariant current-bank datum maps equivariantly to zero in the
   adjoint, not to a line.

2. **Color orientation is retired as physical source data.** The color
   orientation note states that requiring a particular color frame, direction,
   or point inside an `SU(3)` orbit is predictively vacuous for invariant
   observables. A chosen ray is gauge-covariant, not gauge-invariant, and the
   runner exhibits a nontrivial `SU(3)` rotation moving the line.

3. **Depolarization kills the traceless ray.** The depolarization note relocates
   first-moment centrality to `rho_color = I_3/3`. Its traceless part is zero,
   so it supplies no `H_psi` line.

4. **Fierz gives a block count, not an internal line selector.** The Fierz
   support gives the exact `1+8` split and `F_adj=8/9`. The runner checks that
   the isotropic adjoint block has rank `8` and full eigenvalue multiplicity
   `8`; it does not distinguish one line inside the adjoint.

5. **The `Z_3` color/generation bridge is open.** The axis-cycle character note
   records that a shared label action would be an extra bridge assumption, not
   a current primitive, and that the `SU(3)_c` center is not the desired bridge.

6. **Route-2 readout still needs the E-center primitive.** The exact readout map
   leaves the center E lift free; it does not derive the endpoint triple.

In typed-graph terms, the current bank has no path

```text
current_source_bank -> physical_color_ray_source_line
current_source_bank -> route2_adjoint_line_1_of_8
current_source_bank -> rho_E=21/4
```

through this route. Adding exactly the missing primitive creates the path, so
the blocker is localized rather than hidden.

## What This Prunes

This prunes the current-bank route:

```text
current color/source support already supplies a physical color ray
  -> one adjoint line
  -> 7/8 complement
  -> rho_E=21/4.
```

The conditional consequence is exact, but the first arrow is absent on the
actual current surface.

## What Remains Open

Open positive routes remain:

- derive a physical color-ray/source-line primitive from a new same-surface
  source theorem;
- derive an equivalent E-center lift primitive without color rays;
- prove a stronger readout-map theorem beyond the restricted endpoint carrier;
- abandon Route-2 endpoint readout for a different up-sector scalar-law route.

This note does not rule out any of those future routes. It only says the current
source bank does not already contain the color-ray primitive needed by this
line-selector mechanism.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_physical_color_ray_source_primitive_no_go_2026_06_21.py
```

Expected result:

```text
PASS=26 FAIL=0 TOTAL=26
```
