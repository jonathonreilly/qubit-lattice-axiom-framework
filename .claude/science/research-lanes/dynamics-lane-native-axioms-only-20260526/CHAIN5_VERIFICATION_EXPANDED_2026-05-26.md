# Chain 5 Verification — Expanded Query Results

**Date:** 2026-05-26 (cycle 2, extending initial CHAIN5_VERIFICATION)
**Method:** broader ledger query of `origin/main`'s `audit_ledger.json` for
self-gravity, cycle-battery, retarded-propagation, two-field, staggered, and
Callan-Harvey terminology.
**Status:** expansion of the lane's Chain 5 inventory.

## Newly identified retained native-dynamics pieces

### Full `retained` (positive theorem)

| Source | Status | Claim type |
|---|---|---|
| `poisson_self_gravity_zero_coupling_exact_reduction_narrow_theorem_note_2026-05-17` | **retained** | positive_theorem |

### `retained_bounded` (bounded theorem)

| Source | Status | Claim type |
|---|---|---|
| `cycle_battery_note_2026-04-10` | retained_bounded | bounded_theorem |
| `cycle_battery_scaled_note_2026-04-10` | retained_bounded | bounded_theorem |
| `self_gravity_scaling_note_2026-04-10` | retained_bounded | bounded_theorem |
| `staggered_3d_self_gravity_sign_note_2026-04-11` | retained_bounded | bounded_theorem |
| `staggered_two_field_wave_note` | retained_bounded | bounded_theorem |
| `two_field_retarded_family_closure_note_2026-04-10` | retained_bounded | bounded_theorem |
| `two_field_retarded_probe_note_2026-04-10` | retained_bounded | bounded_theorem |
| `poisson_self_gravity_born_audit_note` | retained_bounded | bounded_theorem |

### `retained_no_go` (additional obstructions)

| Source | Status | Claim type |
|---|---|---|
| `gate_b_poisson_self_gravity_note` | retained_no_go | no_go |
| `poisson_self_gravity_loop_v3_note` | retained_no_go | no_go |
| `self_gravity_backreaction_closure_note` | retained_no_go | no_go |
| `self_gravity_born_hardening_note` | retained_no_go | no_go |
| `self_gravity_failure_diagnosis` | retained_no_go | no_go |

## Verified expanded native surface (usable in this lane)

The lane now has substantially more verified retained native content than the
initial query showed:

1. **Decoherence (kinematic action-class)** — `retained_bounded`. Spatial per-link
   zero-field phase equality.
2. **Cycle batteries** — `retained_bounded`. Staggered irregular cycle/scaled
   diagnostics.
3. **Two-field retarded propagation** — `retained_bounded`. Includes family
   closure + probe + staggered wave.
4. **Self-gravity (bounded slice)** — `retained_bounded` + one **`retained`
   positive_theorem** (zero-coupling exact reduction). Bounded by multiple
   retained no-gos.
5. **Staggered 3D self-gravity sign** — `retained_bounded`.

## What's still memory-claimed-but-unverified

Specific items that memory mentioned but I haven't yet located:

- "Brannen-CH three-gap closure" with explicit Gap-1 (Berry=CH), Gap-2 (Ω=1
  derived), Gap-3 (operator map) — closest match `koide_brannen_callan_harvey_candidate_note_2026-04-22`
  which is `unaudited`. The closure-grade work memory described isn't visibly
  retained.
- "Corrected propagator `1/L^p`" — the `1/L²` lattice replay surfaces in
  decoherence notes but the broader "corrected propagator" framing per memory
  doesn't surface as a standalone retained source.
- "Mirror symmetry breakthrough on Z₂ DAGs" — not surfaced by the broader
  query; defer locate.
- "Axiom chain closure: gravity 2.0 SE + decoherence" — the decoherence and
  self-gravity slices are partially retained, but no integrated "axiom chain
  closure" source is visible. Memory may have been characterizing a
  branch-local synthesis that didn't make it through audit.

## Relevance to the δ question

The expanded verified surface includes self-gravity, cycle-battery, and
retarded-propagation results. **None of these directly address the C₃
generation-sector phase δ.** They are about:

- 3D lattice gravity (continuous-space, not generation sector)
- Cycle-battery statistical observables (lattice-internal, not generation-sector)
- Retarded propagation (time-direction, not C₃-axis)
- Staggered self-gravity sign (gravitational direction, not C₃-axis)

The structural separation between **spatial / temporal lattice dynamics** and
the **generation-sector C₃ azimuthal phase** holds across the expanded surface.

**Conclusion:** the verified retained native dynamics chain is substantial but
**sector-orthogonal to δ**. Direction α (native dynamics determination of δ) is
not unblocked by the expansion. The sector-mismatch finding from
`DIRECTION_ALPHA_FIRST_CYCLE_2026-05-26.md` stands.

## Updated direction priority

Given the sector-mismatch finding persists even with expanded Chain 5
verification:

1. **Direction γ** (native isolation of the π-bridge gap) becomes the lane's
   highest-priority attack. It uses only retained no-gos + L-W, doesn't need
   sector-coupling content.
2. **Direction δ** (boundary-condition reading of C₃ + Cl(3) without dynamics)
   is the next candidate; it stays purely kinematic.
3. **Direction α** remains blocked pending either (a) a retained
   sector-coupling result not yet located, or (b) a new derivation that
   produces such a coupling natively.

## Cited retained sources (load-bearing in this verification)

- `docs/audit/data/audit_ledger.json` on `origin/main` (effective-status source
  of truth)

All other retained source-note names are listed but their content is not
load-bearing in this verification; the verification only consumes their
ledger-level retention status.
