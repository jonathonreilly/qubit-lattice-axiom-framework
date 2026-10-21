# PMNS local-selector finite-search diagnostic

**Date:** 2026-04-20; correction 2026-10-21
**Type:** open_gate
**Status:** numerical support; global exclusion remains unproved.
**Primary runner:** `scripts/frontier_dm_pmns_local_selector_family_no_go_theorem_2026_04_20.py`

The stable filename does not retain the former global no-go. The supplied
PMNS map is conditional on its explicit matrix and eigenvalue-ordering domain,
not a derived physical source or unique pairing. The target angle triple
(0.307, 0.0218, 0.545) is supplied comparison data.

The imported parity and curvature constructions return
`delta=q_+=sqrt(6)/3`. Their family-reduction arguments remain external premises:
[parity construction](DM_NEUTRINO_SOURCE_SURFACE_PARITY_COMPATIBLE_OBSERVABLE_SELECTOR_THEOREM_NOTE_2026-04-17.md),
[curvature construction](DM_NEUTRINO_SOURCE_SURFACE_ACTIVE_CURVATURE_23_SYMMETRIC_BASELINE_BOUNDARY_THEOREM_NOTE_2026-04-17.md).
The [supplied PMNS map](PMNS_FROM_DM_NEUTRINO_SOURCE_H_DIAGONALIZATION_CLOSURE_THEOREM_NOTE_2026-04-17.md)
is evaluated only where its eigenvectors and angle denominators are defined.

On that line, central differences with step 1e-4 and sign-change bracketing
locate two stationary candidates using 4001 samples on [-2000,2000]. The
lower located value is approximately 0.331582718643 at m=4.365005345286,
above the supplied solar target 0.307. The three-angle squared-error search
uses 8001 samples on [-200,200] and locates one candidate near m=1.278322119585,
with error 0.011428083950 and triple (0.37920275,0.05563746,0.47379695).
Five separately supplied candidate points also miss the target in this map.
These are finite numerical diagnostics, not certified minima.

A sign-change search can miss stationary roots and does not control the
unbounded line, degeneracies, or unsampled extrema. Consequently this does
not prove that every point on the line misses, exclude all local selectors,
or require a nonlocal selection law. Those proof obligations remain open.
Earlier exact/global/nonlocal-necessity wording is withdrawn and recoverable
at `f24d17d97d372df977476e4a69674577f31af575` under this path.
The runner's failure exit and numerical thresholds are preserved; obsolete
prose-endorsement checks are removed.
