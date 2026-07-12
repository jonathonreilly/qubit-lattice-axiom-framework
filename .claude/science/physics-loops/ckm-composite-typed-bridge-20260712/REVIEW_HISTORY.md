# Review history

## Pre-review fanout — 2026-07-12

Three independent route checks converged:

1. Relative-basis route: derived
   `Tr(P_i^uP_j^d)=|V_ij|^2`, the two-family commutator form, and the fixed-`H_d`
   orientation countermodel.
2. Atlas-reuse route: found no existing authority supplying a
   generation-flavor to six-state lift or the relative alignment law; shared
   circulants and current NNI prose do not close it.
3. Spectral-character route: proved conditional uniqueness of `det^(1/6)`
   under added readout axioms and confirmed that it remains orientation-blind.

Initial exact runner result:
`SUMMARY: EXACT_PASS=18 BOUNDARY_PASS=14 FAIL=0`.

## Review-loop iteration 1

- Code/runner: PASS; independent random-unitary recomputation gave projector
  overlap and weak-basis covariance errors below `5e-16`.
- Physics/Nature/labeling: BOUNDED / BOUNDED / PASS. Findings: narrow the trace
  movement, remove unproved minimality, use the native mixed-role status, and
  remove branch-local source prose.
- Imports/governance/no-go discipline: fixes required for determinant-character
  premise disclosure, retained-authority links, and tabular N1-N8 evidence.

## Review-loop iterations 2-3

All verified findings were fixed and only changed files were re-reviewed.
Final dispositions:

- Code/runner: PASS.
- Physics claim: BOUNDED; parent physical bridge OPEN.
- Nature retention: BOUNDED; no Nature-readiness claim.
- Import support: PASS.
- Labeling convention: PASS.
- Repository governance: PASS.
- No-go discipline: PASS after the full N1-N8 evidence walk.

No reviewer applied an audit verdict. Independent audit remains required.

## Audit compatibility validation

The audit pipeline seeded one new leaf row,
`ckm_mass_operator_projector_overlap_typing_theorem_note_2026-07-12`, with
`claim_type=bounded_theorem`, `audit_status=unaudited`, the parent-note
dependency, and the paired runner. Strict lint passed with no errors (31
pre-existing warnings and 248 notices). All regenerated audit, publication,
and front-door outputs were restored from the intended stacked base and are
absent from the source diff.
