# Supplied basin-table source-cubic sign comparison

**Type:** bounded_theorem
**Status:** conditional algebra / supplied finite evidence; physical selection open
**Primary runner:** `scripts/frontier_dm_abcc_exact_target_surface_source_cubic_closure_2026_04_21.py`

Supply the affine Hermitian chart H=Hbase+m*Tm+delta*Tdelta+q_+*Tq, constants gamma=1/2, E1=sqrt(8/3), E2=sqrt(8)/3, and the five numerical triples stored in the companion runner. Define I_src=Im(H12*H23*H31). A definition of I_src is not a law requiring I_src>0.

## Finite comparison and conditional implication

Using the additional chamber convention q_++delta>=E1, the displayed table has chamber members Basin 1, Basin 2 and Basin X. In this finite table I_src and det(H) are positive on Basin 1 and negative on Basin 2 and X. Therefore imposing I_src>0 selects Basin 1 among these three displayed candidates. This is conditional on a separate positivity selector. It neither derives that selector nor removes physical branch-choice obligations.

Extending the table statement to every exact-target solution would additionally require a genuine completeness proof. The formerly cited enumeration was archived as finite multistart evidence, not such a proof. No exact exhaustive root set is asserted here; supplied decimal coordinates are evaluated numerically.

Basin N has negative I_src but positive determinant; Basin P has positive I_src but negative determinant. These explicit finite controls disprove a universal sign equivalence on a domain containing those matrices. They do not establish an unrestricted physical no-go. The chart, selected chamber, complete solution census and physical positivity law remain distinct premises/obligations.

## Reproduction scope

The runner computes margins, cubic, projected determinant scalar and direct determinant, preserves numerical tolerances, and checks the finite selected set. Archived wording and literal-True conclusions no longer count as evidence. No global selection or exact target completeness is inferred from finite evaluations.

## Provenance and related definitions

Prior text is recoverable at Git `f24d17d97d372df977476e4a69674577f31af575` under this path. References supply the chart/definitions; this note does not inherit their entire physical or completeness claims.

- [dm_neutrino_source_surface_active_half_plane_theorem_note_2026-04-16](DM_NEUTRINO_SOURCE_SURFACE_ACTIVE_HALF_PLANE_THEOREM_NOTE_2026-04-16.md)
- [dm_pmns_upper_octant_source_cubic_selector_theorem_note_2026-04-20](DM_PMNS_UPPER_OCTANT_SOURCE_CUBIC_SELECTOR_THEOREM_NOTE_2026-04-20.md)
