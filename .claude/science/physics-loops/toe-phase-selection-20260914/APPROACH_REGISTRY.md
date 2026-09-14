# Active proof registry

The initial seven-family portfolio and stop/reopen conditions are in
`../../exercises/toe-phase-selection-20260914/APPROACH_REGISTRY.md`.

Current changes to that ranking:

- Exact local projection: working proof and coefficientwise checks complete;
  fixed-box spectral and product limits derived. Pending personal final scope
  check and independent review.
- Local operator comparison: the initial conditional charge-density route
  still needs sector-energy ordering. A different imaginary-time entrywise
  comparison now gives a lower bound on actual local probabilities without
  that premise. It is recorded in BLOCK1_LOCAL_PROBABILITY_DERIVATION.md.
- Sector energy ordering: remains open. Single-jump comparison is proved in
  the working note; its minimizing states do not compose automatically on
  overlapping plaquettes. Ten finite box/parameter comparisons found no
  charged winner and do not prove the general claim.
- Reflection and discrete rearrangement: concrete hypothesis gaps are recorded
  in BLOCK1_SECTOR_PROOF_SEARCH.md. No borrowed phase theorem is assumed.
- Actual phase estimates: still blocked-equivalent in the prior loop/filter
  formulation until a new estimate controls the actual ground state.

Artifact types (note, runner, cache, PR) are delivery forms, not proof families.
