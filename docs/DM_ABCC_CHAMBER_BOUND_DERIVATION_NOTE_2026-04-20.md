# Conditional positive-real-part chamber coordinate identity

**Type:** bounded_theorem
**Status:** conditional algebra / supplied finite evidence; physical selection open
**Primary runner:** `scripts/frontier_dm_abcc_chamber_bound_derivation.py`

Supply E1=sqrt(8/3), gamma=1/2, s=q_+-E1+delta and z=s-i*gamma. Then r31=|z| satisfies r31²=s²+1/4, hence r31>=1/2. This modulus identity alone does not fix the sign of s.

## Conditional theorem

Impose the additional branch convention s>=0. Then q_++delta>=E1, and conversely every point of that half-plane defines s>=0 and r31=sqrt(s²+1/4). The phase chosen by phi=atan2(gamma,s) lies in (0,pi/2], and z=r31*exp(-i*phi). Equality holds iff s=0, r31=1/2, phi=pi/2 modulo 2*pi. This proves the image equivalence for this supplied coordinate branch, not that all physically admissible sources must lie on it.

The negative control s=-1, r31=sqrt(5)/2 also satisfies r31²=s²+1/4 and gamma=1/2, but has q_++delta=E1-1. Its phase lies in (pi/2,pi). Modulus positivity therefore cannot discard this branch.

The upstream active-half-plane presentation explicitly uses the principal asin inverse and positive square root. The carrier normal form supplies gamma and even-response relations, but does not by itself prove the added s>=0 physical restriction. Deriving that restriction or identifying it as an appropriate convention remains a separate obligation.

## Supplied finite checks

The runner retains four historical coordinate samples, boundary and interior samples, and Hermiticity checks, with their old tolerances. It adds the negative-sign control. Their inclusion/exclusion is conditional on the declared branch. The four rows are not an exhaustive basin census; in particular this note makes no A-BCC or physical point-selection closure claim.

## Provenance and related definitions

Prior text is recoverable at Git `f24d17d97d372df977476e4a69674577f31af575` under this path. References supply the chart/definitions; this note does not inherit their entire physical or completeness claims.

- [dm_neutrino_source_surface_active_affine_point_selection_boundary_note_2026-04-16](DM_NEUTRINO_SOURCE_SURFACE_ACTIVE_AFFINE_POINT_SELECTION_BOUNDARY_NOTE_2026-04-16.md)
- [dm_neutrino_source_surface_active_half_plane_theorem_note_2026-04-16](DM_NEUTRINO_SOURCE_SURFACE_ACTIVE_HALF_PLANE_THEOREM_NOTE_2026-04-16.md)
- [dm_neutrino_source_surface_z3_doublet_block_point_selection_theorem_note_2026-04-16](DM_NEUTRINO_SOURCE_SURFACE_Z3_DOUBLET_BLOCK_POINT_SELECTION_THEOREM_NOTE_2026-04-16.md)
- [dm_neutrino_source_surface_intrinsic_slot_theorem_note_2026-04-16](DM_NEUTRINO_SOURCE_SURFACE_INTRINSIC_SLOT_THEOREM_NOTE_2026-04-16.md)
- [dm_neutrino_source_surface_slot_torsion_boundary_theorem_note_2026-04-16](DM_NEUTRINO_SOURCE_SURFACE_SLOT_TORSION_BOUNDARY_THEOREM_NOTE_2026-04-16.md)
