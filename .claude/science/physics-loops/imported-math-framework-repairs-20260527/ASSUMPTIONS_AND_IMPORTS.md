# Assumptions And Imports

## KMS / Brydges Majorant

Retired import:

- External Kroschinsky-Marchetti-Salmhofer / Brydges-Battle-Federbush majorant
  theorem as a load-bearing imported result for the framework row.

Replacement:

- The source note now proves the finite framework comparison lemma directly:
  if `Y_{j+1} <= R_j Y_j / (1 - q_j Y_j)` on a finite scale mesh, then
  `Y_n <= E_n Y_0 / (1 - Q_n Y_0)` with
  `E_n = product R_j` and `Q_n = sum q_j product_{i<j} R_i`.
- The runner checks exact Fraction arithmetic for the scalar and mesh
  comparison maps, composition, monotonicity, and the source firewall.

Residual assumptions:

- A later framework use must still construct the polymer norm, prove the
  one-step inequality, identify the framework effective action with the
  coefficient vector, verify small-data hypotheses, and establish the physical
  bridge.
- KMS remains a parallel background citation, not a binding import.

## Born / Gleason-Busch

Retired import:

- Raw standard-math import of Gleason/Busch, Kraus/Choi, Naimark, and Luders as
  untracked external load-bearing premises for this row.

Replacement:

- The row now cites direct in-repo framework authorities:
  - `gleason_on_qubit_lattice_projection_lattice_narrow_theorem_note_2026-05-20`
  - `busch_povm_extension_on_qubit_lattice_narrow_theorem_note_2026-05-20`
  - `pre_record_reference_state_tracial_derivation_note_2026-05-20`
  - `kraus_choi_representation_on_qubit_lattice_narrow_theorem_note_2026-05-20`
  - `lsp_projective_derivation_from_naimark_frame_narrow_theorem_note_2026-05-22`
  - `luders_rule_from_composition_consistency_note_2026-05-20`
  - `luders_sequential_product_conditional_bridge_narrow_theorem_note_2026-05-22`
- The new runner checks those dependencies are retained-grade in the ledger and
  verifies finite-region tracial probabilities, projective Luders conditioning,
  rank-one Born form, sequential projective effects, projective Kraus trace
  preservation, and source firewall language.

Residual assumptions:

- The row remains finite-region and ideal-record scoped.
- Durable/native persistent record formation remains outside this row.
- Arbitrary unsharp instrument uniqueness remains outside this row.
- Native apparatus dynamics remain outside this row.

## Axiom Count

No new axiom is added by this repair. The changes replace raw imports with
framework-local bounded proof/dependency surfaces and preserve independent audit
as the authority for any effective status.
