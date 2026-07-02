# Quark Route-2 Color-Ray Adjoint-Line Selector Boundary

**Date:** 2026-06-21
**Claim type:** bounded_theorem
**Claim scope:** conditional-support plus current-source boundary
**Status authority:** independent audit lane only. This source note does not set, claim, or predict an audit outcome.
**Primary runner:** [`scripts/frontier_quark_route2_color_ray_adjoint_line_selector_boundary_2026_06_21.py`](../scripts/frontier_quark_route2_color_ray_adjoint_line_selector_boundary_2026_06_21.py)
**Runner cache:** [`logs/runner-cache/frontier_quark_route2_color_ray_adjoint_line_selector_boundary_2026_06_21.txt`](../logs/runner-cache/frontier_quark_route2_color_ray_adjoint_line_selector_boundary_2026_06_21.txt)
**Authority links:** [`QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md`](QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md), [`QUARK_ROUTE2_RCONN_TYPED_BRIDGE_DERIVATION_BOUNDED_NOTE_2026-06-12.md`](QUARK_ROUTE2_RCONN_TYPED_BRIDGE_DERIVATION_BOUNDED_NOTE_2026-06-12.md), [`COLOR_ORIENTATION_OF_THE_STATE_IS_PREDICTIVELY_VACUOUS_NARROW_THEOREM_NOTE_2026-06-09.md`](COLOR_ORIENTATION_OF_THE_STATE_IS_PREDICTIVELY_VACUOUS_NARROW_THEOREM_NOTE_2026-06-09.md), [`MATTER_COLOR_DEPOLARIZATION_NECESSARY_FOR_GAUGE_LINK_AD_INVARIANCE_NARROW_THEOREM_NOTE_2026-06-09.md`](MATTER_COLOR_DEPOLARIZATION_NECESSARY_FOR_GAUGE_LINK_AD_INVARIANCE_NARROW_THEOREM_NOTE_2026-06-09.md), [`CL3_QUARK_ANTIQUARK_COLOR_SINGLET_THEOREM_NOTE_2026-05-02.md`](CL3_QUARK_ANTIQUARK_COLOR_SINGLET_THEOREM_NOTE_2026-05-02.md), [`EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md`](EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md), [`Z3_CHARACTER_ISOMORPHISM_COLOR_GENERATION_OPEN_GATE_NOTE_2026-05-10.md`](Z3_CHARACTER_ISOMORPHISM_COLOR_GENERATION_OPEN_GATE_NOTE_2026-05-10.md), [`S3_TIME_READOUT_PRIMITIVE_BRIDGE_ASSESSMENT_BOUNDED_NOTE_2026-06-12.md`](S3_TIME_READOUT_PRIMITIVE_BRIDGE_ASSESSMENT_BOUNDED_NOTE_2026-06-12.md)

```yaml
actual_current_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: "If a physical color ray is supplied as source data, it selects one adjoint line and its 7-dimensional complement, giving e_E=7/8 and the Route-2 endpoint triple."
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "The current source surface does not supply a physical color ray or gauge-frame orientation as source data."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Target

The parent `s3_time_theta_to_slice_coupling_note` remains open because the
Route-2 readout endpoint triple

```text
(beta_T/alpha_T, alpha_T/alpha_E, beta_E/alpha_E) = (-1, -2, 21/4)
```

is not derived. After the granted T-side values, the remaining entry is

```text
rho_E := beta_E/alpha_E.
```

The prior source-domain no-go and Rconn bridge attempt show that the exact
Fierz/adjoint fraction `F_adj = 8/9` is support, not a typed Route-2 center
readout. This note asks the next sharper question:

```text
Can a non-invariant source datum type the missing single adjoint line?
```

## Minimal Premises

Allowed:

- exact finite-dimensional `SU(3)` color algebra on `C^3`;
- the standard Gell-Mann basis with `Tr(t_a t_b)=delta_ab/2`;
- the Route-2 endpoint algebra after granting the T-side values
  `q_T=5/6` and `s_TE=-2`;
- current source notes as authority-boundary text.

Forbidden:

- observed quark masses or fitted Yukawa data;
- nearest-rational endpoint selection from live numerical readouts;
- an untyped identification of color orientation with physical source data;
- an untyped identification of `F_adj` with `c_TE`;
- a hidden readout convention for `P_R`.

## Conditional Construction

If a physical color ray `psi in C^3` is supplied, it defines a traceless
Hermitian color operator

```text
H_psi = |psi><psi| - I_3/3.
```

For `psi = e_3`,

```text
H_psi = diag(-1/3, -1/3, 2/3),
Tr(H_psi) = 0,
Tr(H_psi^2) = 2/3.
```

In adjoint coordinates this is a nonzero vector, hence a rank-one projector
`P_line` in the 8-dimensional adjoint space. Its orthogonal complement has
rank `7`, so the normalized complement fraction is

```text
Tr(I_8 - P_line) / 8 = 7/8.
```

Reading that complement fraction as the Route-2 E-center excess gives

```text
e_E = 7/8,
q_E = 1 + e_E = 15/8,
rho_E = 6 e_E = 21/4,
c_TE = (-2)(5/6)/(15/8) = -8/9.
```

So a supplied physical color ray is a sufficient non-invariant primitive for
the single-adjoint-line/complement mechanism.

## Current-Source Boundary

The same runner verifies why this is not a current-surface derivation.

- The selected line is gauge-covariant, not gauge-invariant: an `SU(3)`
  rotation moves `P_line`, and `[t_4,H_psi]` is nonzero.
- No nonzero traceless adjoint vector is invariant under all of `SU(3)`.
- The color-orientation surface treats a particular color direction or point
  inside an `SU(3)` orbit as predictively vacuous source data.
- The color-depolarization centrality route forces the traceless color mean to
  vanish; it does not select a color ray.
- The color-singlet and Fierz authorities supply the `1 + 8` channel split and
  `F_adj=8/9`, but not a line inside the adjoint `8`.
- The `Z_3` color/generation/axis bridge remains an open bridge and does not
  identify color labels with spatial axes.
- The Route-2 readout assessment still leaves unique `P_R` selection open.

Therefore the minimal working datum is not "some non-invariant geometry" in
the abstract. It is specifically a physical color ray, or an equivalent
gauge-frame/source-line primitive that survives the current color-orientation
firewall.

## Stuck Fan-Out

| Frame | Result |
|---|---|
| Fundamental color ray | Conditional success: `psi` selects `H_psi`, one adjoint line, complement `7/8`, and hence `rho_E=21/4`. |
| Invariant color surface | No success: `SU(3)` has no nonzero invariant traceless adjoint vector. |
| Depolarized color density | No success: centrality pushes toward `I_3/3`, erasing the traceless line source. |
| Fierz / singlet-adjoint channel | No success: gives `1+8` and `8/9`, not a distinguished line inside `8`. |
| Axis / cyclic label geometry | No success on current surface: label isomorphism is an open bridge, not a physical color-ray source. |

Synthesis: the next positive route must derive or approve a physical color-ray
source primitive. Without it, the best honest status is conditional support
plus a current-bank boundary.

## What This Moves

This block narrows the remaining Route-2 readout ambiguity:

- It identifies a concrete non-invariant primitive that would supply the
  block37-style single-adjoint-line selector.
- It shows why the current color/source bank does not supply that primitive.
- It separates three nearby but insufficient facts:
  - `F_adj=8/9` is channel-count support;
  - color depolarization is invariant-density support;
  - a physical color ray is the missing line-selector datum.

This does not derive the endpoint triple on the actual current surface. It
does not derive non-top quark masses, assign a physical color orientation, or
close the `s3_time_theta_to_slice_coupling_note`.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_color_ray_adjoint_line_selector_boundary_2026_06_21.py
```

Expected result:

```text
PASS=15 FAIL=0 TOTAL=15
```
