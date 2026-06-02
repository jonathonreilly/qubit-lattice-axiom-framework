# The Hermitian-Records Target Is Import-Required (No-Relative-Branch-Phase), and Closing It Would Not Remove Bounded

**Date:** 2026-06-02
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only; effective status is
pipeline-derived after audit.
**Primary runner:** [`scripts/frontier_koide_hermitian_records_import_required.py`](../scripts/frontier_koide_hermitian_records_import_required.py)

## Context

The companion note
`KOIDE_RP_SPECTRUM_REDUCE_TO_TRANSFER_POSITIVITY_NARROW_THEOREM_NOTE_2026-06-02`
reduced reflection positivity and the spectrum condition to one statement -- the
emergent-time transfer operator `T` is positive Hermitian -- and exhibited a
route to it through the framework's records/decoherence completely-positive
structure with the retained tracial reference. That note flagged the route's
antecedent (the records/decoherence operators are Hermitian, hence the
dissipator is trace-symmetric) as an UNBUILT derivation target, not an
assumption. This note determines the status of that target.

## Claim

The Hermitian-records target is **import-required**, not forced from
A1 + A2 + retained. It reduces to a single named import,
**`NO-RELATIVE-BRANCH-PHASE`** (`U = I`: the record-writing instrument inserts
no relative phase between record branches). An explicit valid CPTP
counterexample shows persistence of a classical record does **not** force
Hermiticity. So the RP/spectrum cascade **trades** the staggered/Wilson import
for the `U = I` import -- it is import-traded, not importless. And closing the
target would **not** remove the `bounded` condition down the full charged-lepton
chain.

### A. The counterexample (persistence does not force Hermiticity)

A phase-twisted diagonal channel with Kraus operators

```text
K_r = sqrt(p_r) diag( e^{i a_r}, e^{i b_r} ),   relative branch phase (a_r - b_r) != 0,
```

is a valid CPTP map (Choi PSD), trace-preserving, UNITAL (it fixes the tracial
state `rho = I/2`), and it PERSISTS a classical record (the `Z`-diagonal
populations are preserved). Yet its Kraus operators are non-Hermitian, its
dissipator is not trace-symmetric, and the transfer superoperator has complex
eigenvalues:

```text
spec(T) = { 1, 1, 0.5 + 0.5 i, 0.5 - 0.5 i }   ->  T NOT positive Hermitian.
```

So a persistent classical record does not force the trace-symmetry the cascade
needs. The recorded observable (the pointer projectors) is Hermitian; only the
implementation phase -- the relative branch phase, the post-measurement unitary
`U` -- is non-trivial, and it is a free parameter.

### B. The fragment, and the exact import

With `U = I` (Hermitian projectors, no relative phase) the superoperator is
self-adjoint and `T` is positive Hermitian (`spec(T) = {0, 0, 1, 1}`). And for a
general instrument `K = U . P`, the superoperator is self-adjoint **iff**
`U = I` (verified: self-adjoint only at `theta = 0`). So the cascade closes if
and only if the relative branch phase vanishes -- the exact import named
`NO-RELATIVE-BRANCH-PHASE`.

The retained inventory confirms this is a convention, not a theorem:
`lsp_projective_derivation_from_naimark_frame_narrow_theorem_note_2026-05-22`
(**retained_bounded**) proves `K_P = P` is a canonical Naimark/Lüders frame
convention, explicitly admitting the `U`-twist as a distinct valid instrument;
`luders_rule_from_composition_consistency_note_2026-05-20` (**retained_bounded**)
generalizes the update to arbitrary Kraus operators; and the framework's
physical decoherence dynamics (`persistent_record_overlap_kernel_note`,
**retained_bounded**) carries phases `e^{i k S}`. So `U = I` is an import
requiring explicit user approval, not a derivation. It is named here and not
adopted.

### C. Closing it would not remove the bounded condition (the user's question)

Even granting the import, the route lands at **retained_bounded** at best: it
reuses `persistent_record_as_kraus_operator` (retained_bounded),
`decoherence_action_independence` (retained_bounded), `lsp_projective_derivation`
(retained_bounded), and `luders_rule` (retained_bounded); a chain is bounded by
its weakest input. Two further structural reasons it does not remove `bounded`
down the full chain:

1. **The matter-attachment leg would not even reach `retained`.** Hermitian
   records discharge only the specific `audited_conditional` blocker on
   `axiom_first_rp_two_step_transfer_matrix_positivity` (the non-Hermitian
   monodromy to Fock-kernel gap). The reduction consumer
   `free_sector_spin_statistics_level1...` (unaudited) rides siblings the target
   does not touch -- `axiom_first_spectrum_condition` (unaudited),
   `axiom_first_reflection_positivity` (unaudited),
   `osterwalder_schrader_from_framework` (unaudited),
   `axiom_first_microcausality_lieb_robinson` (unaudited) -- plus the standing
   `staggered_dirac_substep1_statistics_agnostic_no_forcing` (retained_no_go).

2. **The Koide VALUE chain is on a separate axis with zero dependence on
   records.** Its dominant open pins:
   - **`AC_phi_lambda`** -- the Tier-A admission bundling `delta = 2/9` and the
     abstract-sector to physical-species bridge, carried by
     `staggered_dirac_realization_gate_note_2026-05-03`
     (**audited_renaming**, `chain_closes = False`). The single most
     load-bearing open pin.
   - **`r = 1/2`** -- the block-vs-dimension weight / chiral-grading selection,
     `koide_q23_block_weight_frontier_bounded_note_2026-05-29`
     (**retained_bounded**, self-scoped to exclude the physical weight
     selection).
   - **the signed-vs-singular readout class** --
     `koide_signed_eigenvalue_vs_singular_value_readout_narrow_theorem_note_2026-05-29`
     is **audited_failed** on origin/main (a terminal boundary defect; any repair
     is in an open PR, not yet on main).

   Records-Hermiticity reaches none of these.

**Net:** closing the Hermitian-records target would at best upgrade one
conditional rung inside the dynamics leg; the charged-lepton carrier chain stays
`retained_bounded`/open, dominated by `AC_phi_lambda`, with `r = 1/2` the
value-side pin and the signed-readout class a third independent weakest-link.

## Verified tiers (origin/main audit ledger)

| claim_id | effective status |
|---|---|
| `lsp_projective_derivation_from_naimark_frame_narrow_theorem_note_2026-05-22` | retained_bounded |
| `luders_rule_from_composition_consistency_note_2026-05-20` | retained_bounded |
| `persistent_record_overlap_kernel_note` | retained_bounded |
| `persistent_record_as_kraus_operator_note_2026-05-20` | retained_bounded |
| `pre_record_reference_state_tracial_derivation_note_2026-05-20` | retained |
| `koide_q23_block_weight_frontier_bounded_note_2026-05-29` | retained_bounded |
| `staggered_dirac_realization_gate_note_2026-05-03` | audited_renaming |
| `koide_signed_eigenvalue_vs_singular_value_readout_narrow_theorem_note_2026-05-29` | audited_failed |
| `axiom_first_reflection_positivity_theorem_note_2026-04-29` | unaudited |
| `axiom_first_spectrum_condition_theorem_note_2026-04-29` | unaudited |
| `staggered_dirac_substep1_statistics_agnostic_no_forcing_note_2026-05-25` | retained_no_go |

## Non-circularity

The counterexample is an explicit finite CPTP channel; the self-adjointness
residual is a direct computation. Nothing assumes CAR, the faithful
representation, or `Q = 2/3`.

## Next paths this opens

- The relative branch phase that blocks Hermiticity is plausibly the SAME object
  the signed-vs-singular Koide readout depends on (the `sqrt(m)` sign / the
  det_R vs singular-value distinction). One principle -- e.g. a CPT / reality
  condition on the record-writing generator (the retained
  `cpt_exact_real_anti_hermitian_d` makes the staggered hopping real
  anti-Hermitian; a bridge from that reality to the records channel would fix the
  branch phase) -- could discharge both the CAR-forcing import and the readout
  class at once. This is the highest-value convergence to probe.
- A leaner detour: derive that the framework's physical decoherence channel has a
  real-symmetric Choi matrix (weaker than Hermitian Kraus), which also yields a
  self-adjoint superoperator, possibly from the real-amplitude structure of the
  propagator without touching the Lüders frame convention.
- The two corrections this audit surfaced (the `axiom_first` RP / spectrum rungs
  are unaudited, not a retained ladder; the signed-readout note is
  `audited_failed`) should be reflected wherever the chain is summarized.

This localizes the cascade's antecedent to one named import and answers the
bounded question; it is a localization, not a closure.
