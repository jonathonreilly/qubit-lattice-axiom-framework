---
claim_id: d3_native_stable_orbit_upper_bound_composition_note_2026-06-09
claim_type_author_hint: bounded_theorem
status_authority: independent_audit_lane_only
direct_effective_status_change_allowed_from_this_note: false
---

# D3 Native Stable-Orbit Upper-Bound Composition Note

**Date:** 2026-06-09
**Type:** bounded_theorem (additive source-support wrapper)
**Status:** source-side proposal; independent audit lane only.
**Primary runner:**
[`scripts/d3_native_stable_orbit_upper_bound_composition_2026_06_09.py`](../scripts/d3_native_stable_orbit_upper_bound_composition_2026_06_09.py)
**Cached runner output:**
[`logs/runner-cache/d3_native_stable_orbit_upper_bound_composition_2026_06_09.txt`](../logs/runner-cache/d3_native_stable_orbit_upper_bound_composition_2026_06_09.txt)

## Purpose

This additive note records the narrow D3 upper-bound composition that can be
read from already-landed source surfaces without editing any retained/audited
source note. It is a review-loop-safe wrapper around the existing native
stable-circular-orbit edge:

- [`BERTRAND_STABLE_ORBIT_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md`](BERTRAND_STABLE_ORBIT_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md)
  derives the continuum Green-kernel potential shape
  `V(r) = -k/r^(d-2)` for integer `d >= 3` and the effective-potential
  stability sign `k(d-2)(4-d)/r_c^d`.
  Runner/cache:
  [`scripts/bertrand_stable_orbit_green_kernel_bridge.py`](../scripts/bertrand_stable_orbit_green_kernel_bridge.py),
  [`logs/runner-cache/bertrand_stable_orbit_green_kernel_bridge.txt`](../logs/runner-cache/bertrand_stable_orbit_green_kernel_bridge.txt).
- That support note states that stable circular orbits occur only for integer
  `d = 3`; `d = 4` is marginal and `d >= 5` is unstable.
- The full all-bounded-orbits-are-closed Bertrand theorem is not consumed by
  this composition. It remains context for a stronger claim, not the
  load-bearing finite-set edge used here.

The legacy-named wrapper
[`DIMENSION_SELECTION_UPPER_BOUND_TEXTBOOK_IMPORT_NOTE_2026-05-17.md`](DIMENSION_SELECTION_UPPER_BOUND_TEXTBOOK_IMPORT_NOTE_2026-05-17.md)
and existing gate
[`D3_UPPER_BOUND_IMPORT_SCOPE_GATE_NOTE_2026-06-06.md`](D3_UPPER_BOUND_IMPORT_SCOPE_GATE_NOTE_2026-06-06.md)
now consume this native stable-orbit edge on the current source surface; their
filenames are historical.

## Inputs

1. **Current lower-bound finite packet.**
   [`DIMENSION_SELECTION_NOTE.md`](DIMENSION_SELECTION_NOTE.md) exposes the
   checked lower-bound support set

   ```text
   L_runner = {3,4,5}.
   ```

   This note does not strengthen that lower-bound packet.

2. **Native stable-circular-orbit upper edge.**
   The stable-orbit support note proves the continuum Green-kernel bridge and
   the effective-potential sign test. For the integer dimensions in the
   current lower-bound packet, its load-bearing edge is

   ```text
   U_stable = {d : d <= 3}.
   ```

   This is a stable-circular-orbit edge only. It is not the full Bertrand
   closed-orbit theorem.

3. **Bounded Coulomb companion edge.**
   [`COULOMB_STABILITY_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md`](COULOMB_STABILITY_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md)
   proves the Green-kernel scaling lemma that excludes `d >= 5`, leaves
   `d = 4` marginal, and does not prove a physical hydrogenic `d = 3`
   spectrum. Its weak edge is
   runner/cache backed by
   [`scripts/frontier_coulomb_stability_scaling_repair.py`](../scripts/frontier_coulomb_stability_scaling_repair.py)
   and
   [`logs/runner-cache/frontier_coulomb_stability_scaling_repair.txt`](../logs/runner-cache/frontier_coulomb_stability_scaling_repair.txt).

   ```text
   U_Coulomb_weak = {d : d <= 4}.
   ```

## Composition Certificate

With only the current checked lower-bound packet,

```text
L_runner = {3,4,5}.
```

The native stable-circular-orbit edge gives

```text
L_runner intersect U_stable
  = {3,4,5} intersect {d : d <= 3}
  = {3}.
```

The bounded Coulomb companion gives

```text
L_runner intersect U_Coulomb_weak
  = {3,4,5} intersect {d : d <= 4}
  = {3,4}.
```

Therefore, for the current finite lower-bound packet, the unique `d = 3`
composition can be routed through the native stable-circular-orbit edge. The
Coulomb scaling edge remains compatible companion support, not the unique
selector.

## Why This Is Additive

This note deliberately does not edit retained-row source files. It cites the
existing stable-orbit support note as an already-present native edge and adds a
small composition certificate on top of it. Later source repairs may wire the
legacy-named wrapper/gate to this native edge without changing the support-note
claim itself.

## Non-Claims

This note does not claim:

- a full framework-internal proof of Bertrand's closed-orbit theorem;
- a full framework-internal proof of atomic stability;
- a framework-native electromagnetic sector or hydrogenic spectrum;
- a full dimension-selection theorem from the minimal axioms;
- a derivation of a `Z^d` lattice family from the current `Z^3` lattice;
- a repo-wide audit verdict, retained-grade promotion, or status change;
- any edit to `docs/audit/**`.

## Verification

Run:

```bash
python3 scripts/d3_native_stable_orbit_upper_bound_composition_2026_06_09.py
python3 scripts/cached_runner_output.py --refresh scripts/d3_native_stable_orbit_upper_bound_composition_2026_06_09.py
```

Expected summary:

```text
SUMMARY: PASS=50 FAIL=0
```

## Audit Boundary

This note adds a source-side composition certificate only. It does not write an
audit verdict, set an effective status, or change any retained-grade source
hash. Independent audit owns any effective-status change.
