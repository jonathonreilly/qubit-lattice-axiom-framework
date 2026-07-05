# FRW C3 EOS Component Labels Kinetic Bridge Bounded Support

**Date:** 2026-06-18
**Claim type:** bounded_theorem
**Type:** bounded_theorem
**Status:** bounded support for ideal finite kinetic component labels only.
**Status authority:** independent audit lane only. This note is not an audit
result and does not alter any row status.
**Primary runner:**
[`scripts/frontier_frw_c3_eos_component_labels_kinetic_bridge_2026_06_18.py`](../scripts/frontier_frw_c3_eos_component_labels_kinetic_bridge_2026_06_18.py)
**Cached runner output:**
[`logs/runner-cache/frontier_frw_c3_eos_component_labels_kinetic_bridge_2026_06_18.txt`](../logs/runner-cache/frontier_frw_c3_eos_component_labels_kinetic_bridge_2026_06_18.txt)

## Claim-Status Certificate Snapshot

```yaml
actual_current_surface_status: bounded-support
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This is partial C3 support only; C1, C2, full FRW dynamics, and actual cosmological-fluid application remain open."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Target

The parent open gate
`FRW_ADIABATIC_EXPANSION_COSMOLOGICAL_BACKDROP_OPEN_GATE_NOTE_2026-05-28.md`
marks C3 as the standard radiation/matter/Lambda equation-of-state taxonomy.
The Lambda label is handled by a separate existing dark-energy EOS corollary;
the open C3 residue here is the non-Lambda pair:

```text
w_r = 1/3
w_m = 0
```

This bridge partially closes that residue for ideal kinetic component labels
only. It does not derive C1 or C2, does not derive the full FRW backdrop, does
not derive actual large-scale homogeneity/isotropy, and does not turn an ideal
kinetic label into a theorem about the real cosmological fluid inventory.
No new axiom, registry premise, Tier-A admission, observational comparator,
or fitted value is introduced.

## Statement

Let `P` be a finite multiset of integer momentum vectors in `Z^3`.

1. If `P` is a finite nonzero massless momentum shell, or a positive finite
   mixture of such shells, and every shell is closed under cubic signed
   permutations, then the orbit-averaged kinetic stress is isotropic and each
   pressure component satisfies

   ```text
   P_x / rho = P_y / rho = P_z / rho = 1/3.
   ```

   Thus the ideal radiation kinetic component label is `w_r = 1/3`.

2. If the massive component is a finite pressureless rest sector with
   `p = 0`, then all kinetic pressure components vanish while the energy
   density is positive:

   ```text
   P_x = P_y = P_z = 0,  rho > 0.
   ```

   Thus the ideal pressureless-matter label is `w_m = 0`.

3. If massive modes have nonzero finite momentum, then their kinetic pressure
   correction is positive. For one isotropic shell with squared momentum `q`
   and mass-squared `m^2 > 0`,

   ```text
   w = q / (3 * (m^2 + q)).
   ```

   This is not zero. Therefore this note supports the dust label only on the
   pressureless/rest idealization, not on arbitrary massive kinetic ensembles.

## Proof

For a shell closed under signed permutations of the three coordinate axes,
the signed-permutation orbit has equal axis-square sums:

```text
sum_p p_x^2 = sum_p p_y^2 = sum_p p_z^2.
```

Because each vector in one shell has the same squared norm `q`, the three
axis sums add to `n q`, where `n` is the shell size. Hence each axis sum is
`n q / 3`.

For massless modes, `E = |p| = sqrt(q)`. The energy density is proportional to
`n sqrt(q)`, while a pressure component is proportional to

```text
sum_p p_i^2 / sqrt(q) = (n q / 3) / sqrt(q) = n sqrt(q) / 3.
```

Therefore `3 P_i = rho` on each shell. Finite positive mixtures preserve this
identity term by term, so `w_r = 1/3` remains exact on finite shell mixtures.

For pressureless rest matter, `p = 0`, so every kinetic pressure component is
zero and `rho = n m > 0`. Hence `w_m = P/rho = 0`.

For a nonzero massive shell, `E^2 = m^2 + q` and the scalar pressure ratio is

```text
w = (1/3) q / E^2 = q / (3 * (m^2 + q)).
```

Since `q > 0` and `m^2 > 0`, this ratio is positive and strictly below `1/3`.
That positive correction is the boundary that prevents this support note from
identifying all massive kinetic ensembles with dust.

## Boundary

This note is intentionally small. It supplies ideal kinetic component labels
only. It does not derive C1 or C2, does not derive the full FRW backdrop, does
not derive the thermal history, does not derive entropy conservation, does not
derive the Friedmann equations, does not derive real cosmological perturbation
homogeneity, and does not supply `N_eff` or any observed cosmological
parameter.

The label `w_Lambda = -1` remains outside this note and belongs to the existing
dark-energy EOS corollary surface. The present bridge only narrows the
radiation/matter side of the parent C3 admission from "textbook label import"
to exact finite kinetic support for idealized component labels.

## Trace

The direct blocker being partially addressed is the parent audit request to
close or explicitly admit C1-C3 before re-auditing the FRW backdrop. This note
does not close the whole parent blocker. It partially closes C3 by replacing
the non-Lambda label import with an exact finite kinetic derivation on the
ideal component surface. The remaining parent work is:

- prove or explicitly admit C1;
- prove or explicitly admit C2;
- bridge the ideal finite kinetic labels to the actual cosmological fluids;
- keep Lambda EOS on its separate source surface;
- re-audit independently after the source-side bridge set is complete.

## Verification

Run:

```bash
python3 scripts/frontier_frw_c3_eos_component_labels_kinetic_bridge_2026_06_18.py
python3 scripts/cached_runner_output.py --refresh scripts/frontier_frw_c3_eos_component_labels_kinetic_bridge_2026_06_18.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_frw_c3_eos_component_labels_kinetic_bridge_2026_06_18.py
```

Expected result:

```text
VERDICT: bounded support passes for ideal finite kinetic EOS labels w_r=1/3 and w_m=0. The full FRW backdrop, C1/C2, cosmological-fluid application, and audit status remain open.
```
