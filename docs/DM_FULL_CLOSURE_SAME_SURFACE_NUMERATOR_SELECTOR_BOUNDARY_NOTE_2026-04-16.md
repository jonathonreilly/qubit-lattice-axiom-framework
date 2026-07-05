# DM Full Closure Same-Surface Endpoint Non-Overlap Arithmetic Certificate

**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status:** bounded arithmetic certificate over helper-defined endpoint and
interval outputs only.
**Date:** 2026-04-16 (scope narrowed 2026-06-16 to arithmetic-only endpoint
non-overlap).
**Audit status:** assigned only by the independent audit lane.
**Script:** `scripts/frontier_dm_full_closure_same_surface_numerator_selector_boundary.py`

## Claim Boundary

This note verifies an arithmetic fact about the current helper-defined DM
same-surface packet:

- the helper layer supplies two endpoint couplings, `alpha_lo` and `alpha_hi`;
- the two endpoint couplings are distinct and both lie above the common
  ingredient `alpha_bare = 1/(4 pi)`;
- the helper-returned certified `R(alpha)` intervals at those endpoints are
  disjoint;
- after multiplying by the helper-returned `Omega_b`, the displayed
  `Omega_DM` intervals are also disjoint.

This is not a selector theorem, not an absence theorem, and not a
completeness theorem for the DM bank. The phrase "selector boundary" remains
only in the historical filename and runner name.

## Computed Endpoint Data

The runner obtains the following helper-defined values:

```text
alpha_lo = 0.090667836017286
alpha_hi = 0.092264992618360
alpha_bare = 0.079577471545948
```

and certified interval outputs:

```text
R(alpha_lo) in [5.442019867867, 5.442019867931]
R(alpha_hi) in [5.482855571890, 5.482855571936]

Omega_DM(alpha_lo) in [0.267709052538, 0.267709052541]
Omega_DM(alpha_hi) in [0.269717881594, 0.269717881596]
```

The arithmetic conclusion is exactly:

```text
alpha_bare < alpha_lo < alpha_hi,
R(alpha_lo)_hi < R(alpha_hi)_lo,
Omega_DM(alpha_lo)_hi < Omega_DM(alpha_hi)_lo.
```

## What This Does Not Prove

This note does not prove:

- that either endpoint is selected by the framework;
- that no other same-surface scale-selection datum exists;
- that the helper packet is complete;
- that the plaquette endpoint, eta/omega conversion, or certified-bound
  helpers have independent retained status in this row.

Any selector or completeness claim requires a separate bridge theorem.

## Verification

Run:

```bash
python3 scripts/frontier_dm_full_closure_same_surface_numerator_selector_boundary.py
```

Expected final line:

```text
SUMMARY: PASS=8 FAIL=0
```

Regenerate the cache with the standard runner-cache tool after editing the
runner.

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [dm_full_closure_same_surface_thermal_selector_sensitivity_boundary_note_2026-04-16](DM_FULL_CLOSURE_SAME_SURFACE_THERMAL_SELECTOR_SENSITIVITY_BOUNDARY_NOTE_2026-04-16.md)
- [dm_full_closure_same_surface_converged_thermal_selector_support_note_2026-04-16](DM_FULL_CLOSURE_SAME_SURFACE_CONVERGED_THERMAL_SELECTOR_SUPPORT_NOTE_2026-04-16.md)
