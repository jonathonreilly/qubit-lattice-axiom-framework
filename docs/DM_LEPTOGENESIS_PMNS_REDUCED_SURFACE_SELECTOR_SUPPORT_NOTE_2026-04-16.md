# DM Leptogenesis PMNS Reduced-Surface Selector Diagnostic

**Status:** bounded - bounded or caveated result note
**Type:** bounded_theorem
**Date:** 2026-04-16; scope corrected 2026-07-16
**Script:** `scripts/frontier_dm_leptogenesis_pmns_reduced_surface_selector_support.py`
**Framework baseline:** Lattice, Qubit, Admissibility, and Record axioms.

## Scope

The runner explores a supplied five-coordinate chart

`(u_1, u_2, v_1, v_2, delta) in [0,1]^4 x [-pi, pi]`

with

`x = 3 XBAR_NE * (u_1, (1-u_1)u_2, (1-u_1)(1-u_2))`

and

`y = 3 YBAR_NE * (v_1, (1-v_1)v_2, (1-v_1)(1-v_2))`.

This chart parametrizes the stipulated non-negative fixed-sum seed surface.
Neither this note nor its runner proves that the surface exhausts every
physically admissible PMNS/leptogenesis realization.

## Current deterministic diagnostic

The runner combines a small deterministic chart cover, previously known branch
anchors, and local SLSQP polishing. Its three-branch requirement is an explicit
test, not a theorem.

The current live runner finds two clustered candidates and exits nonzero because
it does not stabilize to the required three branches. The same failure is
present on the comparison baseline. Therefore this note does not claim:

- a certified three-branch count;
- a unique lowest-action branch;
- a global minimum on the supplied chart;
- a global minimum on any larger physical domain;
- a physical selector or yield/readout theorem.

The existing candidate coordinates remain useful debugging fixtures, but the
old stale-green cache is not current evidence for a three-branch result.

Every equality or favored-column calculation in this diagnostic is conditional
on the supplied transport equations, profiles, finite quadrature, packet
construction, and physical readout factors.

## Upstream inputs

- [DM_LEPTOGENESIS_FLAVOR_COLUMN_FUNCTIONAL_THEOREM_NOTE_2026-04-16.md](DM_LEPTOGENESIS_FLAVOR_COLUMN_FUNCTIONAL_THEOREM_NOTE_2026-04-16.md) — conditional finite flavor-column functional identity; no transport provenance or physical-readout authority is inherited.
- [DM_LEPTOGENESIS_PMNS_ACTIVE_PROJECTOR_REDUCTION_NOTE_2026-04-16.md](DM_LEPTOGENESIS_PMNS_ACTIVE_PROJECTOR_REDUCTION_NOTE_2026-04-16.md) — active-projector reduction.
- [DM_LEPTOGENESIS_PMNS_OBSERVABLE_RELATIVE_ACTION_LAW_NOTE_2026-04-16.md](DM_LEPTOGENESIS_PMNS_OBSERVABLE_RELATIVE_ACTION_LAW_NOTE_2026-04-16.md) — supplied observable-relative action helper.
- [DM_LEPTOGENESIS_PMNS_PROJECTOR_INTERFACE_NOTE_2026-04-16.md](DM_LEPTOGENESIS_PMNS_PROJECTOR_INTERFACE_NOTE_2026-04-16.md) — projector interface supplying `canonical_h`.

## Command

```bash
python3 scripts/frontier_dm_leptogenesis_pmns_reduced_surface_selector_support.py
```
