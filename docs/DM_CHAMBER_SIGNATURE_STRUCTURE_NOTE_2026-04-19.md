# DM chamber signature: supplied chart predicate, not DPLE selection

**Date:** 2026-04-19; affected-source correction 2026-10-21.
**Type:** bounded_theorem
**Status:** conditional mathematical support; no physical basin or audit closure.
**Primary runner:** `scripts/frontier_dm_dple_theorem.py`.

## Correction

The former claim that DPLE closes F4 and uniquely selects dimension three is
withdrawn. Its original source is recoverable at
`f24d17d97d372df977476e4a69674577f31af575`. The old finite basin tables and
PASS counts are historical observations, not fresh evidence or retained status.
The current argument is the
[corrected DPLE theorem](DM_DPLE_DIMENSION_PARAMETRIC_EXTREMUM_THEOREM_NOTE_2026-04-19.md).

For a supplied Hermitian pencil with p(t)=det(H0+tH1), a nonsingular
nondegenerate minimum of W=log|p| requires p'=0 and p''/p>0.
The upper bound floor(d/2) on their number does not imply that any exists,
that p is positive there, or that a physical source reaches it. Both d=2
and d=3 have an at-most-one bound; the companion gives an exact d=2 example.
Thus the old assertion that d=2 is vacuous is false.

The positive-chart predicate called F4 separately requires a point in (0,1)
with p'=0, p''>0 and p>0. A positive cubic derivative discriminant alone
neither locates its roots inside (0,1) nor fixes the determinant sign. The
plus-discriminant root is a p minimum; it is the smaller root only for a
negative cubic coefficient. The current runner reports four supplied decimal
basin fixtures as finite diagnostics and does not derive their physical role.

The [W-only sign limitation](DM_DPLE_ABCC_NO_GO_NOTE_2026-04-19.md) applies to
sign-paired pencils, not automatically to a fixed baseline or source chamber.
A chosen nonsingular continuous path preserves inertia, but its nonsingularity
and physical endpoint are additional obligations. The
[P3 specified-path note](DM_NEUTRINO_SOURCE_SURFACE_P3_SYLVESTER_LINEAR_PATH_SIGNATURE_THEOREM_NOTE_2026-04-18.md)
is context for that distinction, not a proof of physical endpoint selection.

## Verification boundary

The shared runner checks the corrected classification, exact d2/d4 controls,
and supplied decimal basin diagnostics. The DPLE proof supplies the count
bound. No old random-scan fraction, count of surviving basins, retained label,
or dimensional-selection conclusion is adopted by this corrected note.
