# Handoff

Repair target:
`statistics_atom_reduces_to_product_form_on_retained_gleason_surface_bounded_note_2026-06-12`.

Audit blocker addressed:
the old row made `sigma tensor sigma` a supplied state-level product premise.
Current `main` already contains a retained-bounded sibling proving that this is
overstrong: agreement-conditioned flow only needs outcome-level factorization.

What changed:

- The note now cites
  `PRODUCT_FORM_PREMISE_WEAKENS_TO_OUTCOME_FACTORIZATION_BOUNDED_NOTE_2026-06-12.md`
  as a load-bearing retained-bounded dependency.
- The theorem boundary now consumes only supplied quotient weights
  `m(j,k)=p_j p_k`.
- The `p_s > 0` finite-odds chart and endpoint handling are explicit.
- The runner checks the outcome-factorization premise, the old product-state
  witness, the endpoint/domain guard, and textual firewalls.

Remaining science:
physical outcome-level independence for repeated registrations remains open.
This PR does not adopt R-D, select an occupancy cell, fix `r`, or prove
record-stack independence.
