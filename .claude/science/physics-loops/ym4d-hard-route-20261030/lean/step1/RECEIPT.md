# Lean receipt: build step 1 of the computer-assisted tool (row 1428)

Written 2026-11-23T03:23Z (date -u) on the Mac mini (worker 2 account) by the row 1428 worker (Claude Fable 5.2, medium). Research-stage working state; no status granted.

- Toolchain: Lean (version 4.36.0, arm64-apple-darwin24.6.0, commit 611c117bfaf7b7ae1cfcf246ce6fba31e8f509e9, Release)
- Command for each file: `lean <file>` (measured with `/usr/bin/time -l`). Only `import Init`; no mathlib; no `native_decide`. Closing tactics: `decide`, `decide +kernel`, `rfl`, `rw`.
- Axioms: every theorem depends on no axiom or on `propext` only (verbatim output below). No `Classical.choice`, no `Quot.sound`, no `Lean.ofReduceBool`, no `sorryAx`.

| File | sha256 | wall | peak resident | exit |
|---|---|---:|---:|---:|
| `Inventory.lean` | 3070a6274b132e0784651bfe807ea5bf1116d93b3403fba000974150cf55c88a | 70.07 s | 1177108480 bytes | 0 |
| `Surface.lean` | 8289b084ca2208b43e234cb6724c007e326901208e3e29d44914ca4a7aee015d | 47.12 s | 1128185856 bytes | 0 |
| `GlueFixtures.lean` | b4e6ce1376513d9bfd1afa5473916ac4c25c4d76dc1b85fcfda199ac615bec24 | 0.41 s | 415744000 bytes | 0 |

`Inventory.lean` is generated: `python3 gen_inventory.py inventory_head.lean.txt values.txt Inventory.lean`. The 192 right-hand sides in `values.txt` came from Lean's `#eval`; the kernel checks each one, so the generator and the evaluator are not trusted.

## Output of `lean Inventory.lean`, verbatim

```text
'Step1.singlet_table' does not depend on any axioms
'Step1.w_is_singlet' does not depend on any axioms
'Step1.link_counts' does not depend on any axioms
'Step1.link_total_by_occupancy' does not depend on any axioms
'Step1.link_total_by_patterns' does not depend on any axioms
'Step1.div_mul_sanity' does not depend on any axioms
'Step1.D_one' does not depend on any axioms
'Step1.D_two' does not depend on any axioms
'Step1.corners_card' depends on axioms: [propext]
'Step1.corners_degree_six' depends on axioms: [propext]
'Step1.prunedS_eq' does not depend on any axioms
'Step1.octahedron_even' depends on axioms: [propext]
'Step1.octahedron_even_pruned' depends on axioms: [propext]
'Step1.octahedron_slots_agree' depends on axioms: [propext]
'Step1.split' does not depend on any axioms
'Step1.steps_eq' depends on axioms: [propext]
'Step1.stepsLit_split' does not depend on any axioms
'Step1.starts_eq' does not depend on any axioms
'Step1.starts_eq_masks' does not depend on any axioms
'Step1.slot_pieces' does not depend on any axioms
'Step1.even_pieces' does not depend on any axioms
'Step1.hist_pieces' does not depend on any axioms
'Step1.split0' does not depend on any axioms
'Step1.total_of_pieces' depends on axioms: [propext]
'Step1.even_subgraphs' depends on axioms: [propext]
'Step1.slots' depends on axioms: [propext]
'Step1.slot_bytes' does not depend on any axioms
'Step1.histogram' does not depend on any axioms
'Step1.histogram_labels' does not depend on any axioms
'Step1.first_moment' does not depend on any axioms
'Step1.second_moment' does not depend on any axioms
```

## Output of `lean Surface.lean`, verbatim

`#print axioms` is issued for cube orientations 0, 1, 63 and hemicube orientation 7 only; the other 67 orientation theorems are checked the same way and not printed.

```text
'Step1Surface.cube_counts' does not depend on any axioms
'Step1Surface.cube_closed' does not depend on any axioms
'Step1Surface.cube_consistent' depends on axioms: [propext]
'Step1Surface.cube_haarSum' depends on axioms: [propext]
'Step1Surface.cube_value' depends on axioms: [propext]
'Step1Surface.cube_value_cert' depends on axioms: [propext]
'Step1Surface.cube_orient_0' depends on axioms: [propext]
'Step1Surface.cube_orient_1' depends on axioms: [propext]
'Step1Surface.cube_orient_63' depends on axioms: [propext]
'Step1Surface.cube_reoriented_inconsistent' depends on axioms: [propext]
'Step1Surface.C1_one_link_missing_inv_d_rejected' depends on axioms: [propext]
'Step1Surface.C1_one_link_missing_inv_d_is_twice' depends on axioms: [propext]
'Step1Surface.C3_zero_over_zero_passes_unguarded' depends on axioms: [propext]
'Step1Surface.C3_zero_over_zero_rejected' depends on axioms: [propext]
'Step1Surface.C3_zero_link_denominator_rejected' depends on axioms: [propext]
'Step1Surface.C3_zero_target_denominator_rejected' depends on axioms: [propext]
'Step1Surface.C4a_one_face_centre_source_is_minus' depends on axioms: [propext]
'Step1Surface.C4a_one_face_centre_source_plus_rejected' depends on axioms: [propext]
'Step1Surface.C4b_face_masks' does not depend on any axioms
'Step1Surface.C4b_face_masks_cancel' depends on axioms: [propext]
'Step1Surface.C4b_closed_twist_trivial_generators' depends on axioms: [propext]
'Step1Surface.C4b_twist_is_nontrivial_on_faces' depends on axioms: [propext]
'Step1Surface.hemicube_counts' does not depend on any axioms
'Step1Surface.hemicube_closed' does not depend on any axioms
'Step1Surface.hemicube_not_consistent' depends on axioms: [propext]
'Step1Surface.hemicube_haarSum' depends on axioms: [propext]
'Step1Surface.hemicube_value' depends on axioms: [propext]
'Step1Surface.hemicube_orient_7' depends on axioms: [propext]
'Step1Surface.C4c_abs_eps_value' depends on axioms: [propext]
'Step1Surface.C4c_abs_eps_rejected' depends on axioms: [propext]
'Step1Surface.C4d_no_eps_value' depends on axioms: [propext]
'Step1Surface.C4d_no_eps_rejected' depends on axioms: [propext]
'Step1Surface.cube_blind_to_abs_eps' depends on axioms: [propext]
'Step1Surface.cube_blind_to_no_eps' depends on axioms: [propext]
'Step1Surface.torus_closed' does not depend on any axioms
'Step1Surface.torus_consistent' depends on axioms: [propext]
'Step1Surface.torus_haarSum' depends on axioms: [propext]
'Step1Surface.torus_value' depends on axioms: [propext]
'Step1Surface.C4e_wrapping_sheet_odd_twist_is_minus' depends on axioms: [propext]
'Step1Surface.C4e_wrapping_sheet_odd_twist_plus_rejected' depends on axioms: [propext]
'Step1Surface.torus_one_face_reversed' depends on axioms: [propext]
```

## Output of `lean GlueFixtures.lean`, verbatim

```text
'Step1Glue.square_ok' does not depend on any axioms
'Step1Glue.C1_one_missing_last_is_3456' does not depend on any axioms
'Step1Glue.C1_one_missing_last_rejected' does not depend on any axioms
'Step1Glue.C1_one_missing_first_is_3456' does not depend on any axioms
'Step1Glue.C1_one_missing_first_rejected' does not depend on any axioms
'Step1Glue.C1_two_missing_is_6912' does not depend on any axioms
'Step1Glue.C1_three_missing_is_13824' does not depend on any axioms
'Step1Glue.C1_targets_rejected' does not depend on any axioms
'Step1Glue.C2_drop_in_last_is_no_adjoint' does not depend on any axioms
'Step1Glue.C2_drop_in_last_rejected' does not depend on any axioms
'Step1Glue.C2_drop_in_first_is_no_adjoint' does not depend on any axioms
'Step1Glue.C2_drop_in_first_rejected' does not depend on any axioms
'Step1Glue.C3_zero_target_denominator_rejected' does not depend on any axioms
'Step1Glue.C3_zero_over_zero_passes_unguarded' does not depend on any axioms
'Step1Glue.C3_zero_over_zero_rejected' does not depend on any axioms
'Step1Glue.C3_zero_input_denominator_rejected' does not depend on any axioms
'Step1Glue.SM_relations' does not depend on any axioms
'Step1Glue.SM_x2y2' does not depend on any axioms
'Step1Glue.SM_sew_coefficients' does not depend on any axioms
```

## Negative controls (run, not committed)

Three false claims were substituted, one at a time, and Lean refused each with "Tactic `decide` proved that the proposition ... is false" (exit 1): the corrupted 2D gluing accepted as the known square; the cube with one missing 1/d accepted as 2^(-28); the hemicube sum claimed to be +16.

## What these files do not check

The Haar integral itself. The integer rules (second moments of a Haar unit quaternion; 2 int U_ab U_cd = eps_ac eps_bd; 2 int U_ab (U^-1)_cd = delta_ad delta_bc; Schur orthogonality) are inputs written in comments, not Lean theorems. See `library/gap-rg-build-step1-fable.md`.
