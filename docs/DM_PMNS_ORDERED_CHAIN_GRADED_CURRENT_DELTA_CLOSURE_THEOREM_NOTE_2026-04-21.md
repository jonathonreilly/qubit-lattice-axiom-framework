# Ordered-chain graded-current coordinate recovery

**Type:** bounded_theorem
**Status:** conditional algebra / supplied finite evidence; physical selection open
**Primary runner:** `scripts/frontier_dm_pmns_ordered_chain_graded_current_delta_closure_2026_04_21.py`

Supply the affine chart H=Hbase+m*Tm+delta*Tdelta+q_+*Tq, grading N=diag(1,2,3), and the specified linear character current J_chi. Define J_N(H)=J_chi(i[N,H]). This construction recovers coordinates from a supplied H; it does not determine the values of the currents or select H.

## Exact affine identities

On the stated basis,

    J_N(Hbase)=-1/2+i*E1/2, J_N(Tm)=0,
    J_N(Tdelta)=-i/2, J_N(Tq)=-3i/2,
    J_chi(H)=q_+-i/4.

Linearity gives J_N(H)=-1/2+i*(E1/2-delta/2-3*q_+/2). Consequently

    q_+=Re J_chi(H),
    delta=E1-2*Im J_N(H)-3*Re J_chi(H).

The real map (delta,q_+) -> (Im J_N,Re J_chi) has Jacobian [[-1/2,-3/2],[0,1]], determinant -1/2. It is invertible and preserves two real degrees of freedom. Thus coordinate recovery is exact while selection of the two current values remains open. The spectator m is not selected by this pair.

## Response reconstruction and limits

The runner also constructs sector fixtures from supplied effective blocks, recovers those blocks from hw=1 response columns and checks the same coordinates. This tests recovery of a supplied target, not derivation of that target from axioms. A function signature that accepts H rather than named target parameters does not remove the physical information already in H.

The grading and current definitions are explicit inputs here. Their availability does not prove their values at the physical point. No exact-target native-source closure, scalar selection, or whole-package closure follows. No changes are made to the unrelated Koide/quark/scale lanes.

## Provenance and related definitions

Prior text is recoverable at Git `f24d17d97d372df977476e4a69674577f31af575` under this path. References supply the chart/definitions; this note does not inherit their entire physical or completeness claims.

- [dm_pmns_graph_first_ordered_chain_nonzero_current_activation_theorem_note_2026-04-21](DM_PMNS_GRAPH_FIRST_ORDERED_CHAIN_NONZERO_CURRENT_ACTIVATION_THEOREM_NOTE_2026-04-21.md)
- [dm_neutrino_source_surface_active_affine_point_selection_boundary_note_2026-04-16](DM_NEUTRINO_SOURCE_SURFACE_ACTIVE_AFFINE_POINT_SELECTION_BOUNDARY_NOTE_2026-04-16.md)
